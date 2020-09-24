class Tree:
    def __init__(self):
        self.members = []
        self.count_of_member = 0

    def add_member(self, person):
        member_id = self.count_of_member = self.count_of_member + 1
        self.members.append((member_id, person))

    def find_member_by_id(self, member_id):
        if member_id is None:
            return None
        else:
            filtered = list(filter(lambda member: member is not None and member[0] == member_id, self.members))
            if len(filtered) == 0:
                raise ValueError("Invalid member id ({}) is supplied.".format(member_id))
            else:
                return filtered[0][1]

    def find_id_by_member(self, person):
        if person is None:
            return None
        else:
            filtered = list(filter(lambda member: member is not None and member[1] == person, self.members))
            if len(filtered) == 0:
                raise ValueError("Invalid person is supplied.")
            else:
                return filtered[0][0]

    def is_member_exist(self, member_id):
        try:
            return self.find_member_by_id(member_id) is not None
        except ValueError:
            return False

    def __str__(self):
        result = ""
        """
        leaves = list(filter(lambda member: member is not None and len(member[1].children) > -1, self.members))
        for x, y in leaves:
            result += ", {}- {}".format(x, y.name)
        return result[2:]
        """
        for member_id, person in self.members:
            result += "Member Id: {}, Name: {}".format(member_id, person.name)
            if person.has_father():
                result += ", Name of father: {}".format(person.father.name)
            if person.has_mother():
                result += ", Name of mother: {}".format(person.mother.name)
            if person.has_spouse():
                result += ", Name of spouse: {}".format(person.spouse.name)
            child_list = [child.name for child in person.children]
            if len(child_list) > 0:
                result += ", Children: {}".format(child_list)
            result += "\n"

        return result
