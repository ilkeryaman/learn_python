import requests
import json
import sys
import logging

########################################################
"""
# Parameters to change
"""
realm_name = "dxp"
keycloak_admin_user = "admin"
keycloak_admin_password = "kcpw"

"""
# Users to define
"""
dxpcsr1 = {"name": "dxpcsr1", "password": "Dxp@1234", "roles": ["CSR-level1", "User Profile Administrators"]}
dxpconfigadmin = {"name": "dxpconfigadmin", "password": "Dxp@1234", "roles": ["SYS-ADMIN"]}
dxpsystem = {"name": "dxpsystem", "password": "Dxp@1234", "roles": ["DXP-SYSTEM", "User Profile Administrators"]}
users = [dxpcsr1, dxpconfigadmin, dxpsystem]
########################################################

# logging settings
logger = logging.getLogger(__name__)
out_handler = logging.StreamHandler(sys.stdout)
out_handler.setFormatter(logging.Formatter('%(asctime)s %(message)s'))
out_handler.setLevel(logging.INFO)
logger.addHandler(out_handler)
logger.setLevel(logging.INFO)
requests.packages.urllib3.disable_warnings()


def create_user(token, username, password):
    url = "{ingress}/auth/admin/realms/{realm}/users".format(ingress=ingress, realm=realm_name)
    headers = {'Authorization': 'Bearer ' + token, 'Content-Type': 'application/json'}
    payload = "{\"username\":\"" + username + "\",\"enabled\":true,\"totp\":false,\"emailVerified\":false,\"notBefore\":0,\"access\":{\"manageGroupMembership\":true,\"view\":true,\"mapRoles\":true,\"impersonate\":true,\"manage\":true},\"credentials\":[{\"type\":\"password\",\"temporary\":false,\"value\":\"" + password + "\"}]}"
    response = requests.request("POST", url, headers=headers, data=payload, verify=False)
    if response.status_code == 201:
        logger.info("User is created")
    elif response.status_code == 409:
        logger.info("User already exists")
    else:
        logger.info("No new user is created")


def get_user_id(token, username):
    url = "{ingress}/auth/admin/realms/{realm}/users".format(ingress=ingress, realm=realm_name)
    headers = {'Authorization': 'Bearer ' + token, 'Content-Type': 'application/json'}
    response = requests.request("GET", url, headers=headers, verify=False)
    if response.status_code == 200:
        user_list = json.loads(response.text)
        user_id = list(filter(lambda user: user["username"] == username, user_list))[0]["id"]
        return user_id
    else:
        return None


def get_role_id_by_name(token, role_name):
    url = "{ingress}/auth/admin/realms/{realm}/roles/{role}".format(ingress=ingress, realm=realm_name, role=role_name)
    headers = {'Authorization': 'Bearer ' + token, 'Content-Type': 'application/json'}
    response = requests.request("GET", url, headers=headers, verify=False)
    return json.loads(response.text)["id"]


def delete_redundant_roles(token, user_id):
    offline_access = get_role_id_by_name(token, "offline_access")
    uma_authorization = get_role_id_by_name(token, "uma_authorization")

    url = "{ingress}/auth/admin/realms/{realm}/users/{userid}/role-mappings/realm".format(ingress=ingress,
                                                                                          realm=realm_name,
                                                                                          userid=user_id)
    headers = {'Authorization': 'Bearer ' + token, 'Content-Type': 'application/json'}
    payload = "[{\"id\":\"" + offline_access + "\",\"name\":\"offline_access\"}, {\"id\":\"" + uma_authorization + "\",\"name\":\"uma_authorization\"}]"
    response = requests.request("DELETE", url, headers=headers, data=payload, verify=False)
    logger.info("Redundant roles are deleted")


def assign_roles_to_user(token, user_id, user_roles):
    url = "{ingress}/auth/admin/realms/{realm}/users/{userid}/role-mappings/realm".format(ingress=ingress,
                                                                                          realm=realm_name,
                                                                                          userid=user_id)
    headers = {'Authorization': 'Bearer ' + token, 'Content-Type': 'application/json'}
    payload = "["
    for role in user_roles:
        role_id = get_role_id_by_name(token, role)
        payload += "{\"id\":\"" + role_id + "\", \"name\":\"" + role + "\"},"
    payload = payload[:-1] + "]"
    response = requests.request("POST", url, headers=headers, data=payload, verify=False)
    if response.status_code == 204:
        logger.info("Roles {} are assigned to user".format(user_roles))
    else:
        logger.info("No new role is assigned to user")


def create_users():
    token = get_token()
    for user in users:
        username = user["name"]
        print("""
######## Operations for {} ########""".format(username))
        create_user(token, username, user["password"])
        user_id = get_user_id(token, username)
        delete_redundant_roles(token, user_id)
        assign_roles_to_user(token, user_id, user["roles"])


def get_token():
    token = None
    iam_token_endpoint = "{ingress}/auth/realms/master/protocol/openid-connect/token".format(ingress=ingress)
    headers = {'Content-type': 'application/x-www-form-urlencoded'}
    payload = {'client_id': 'admin-cli', 'grant_type': 'password', 'username': keycloak_admin_user,
               'password': keycloak_admin_password}
    response = requests.request("POST", iam_token_endpoint, headers=headers, data=payload, verify=False)
    if response.status_code == 200:
        logger.info("Admin token fetched")
        response_data = json.loads(response.text)
        token = response_data['access_token']
    else:
        raise ValueError('ERROR: Unable to fetch token!')

    return token


if __name__ == "__main__":
    global ingress
    ingress = input("Please enter ingress for keycloak: ")
    if not ingress.startswith("https"):
        ingress = "https://" + ingress
    create_users()
