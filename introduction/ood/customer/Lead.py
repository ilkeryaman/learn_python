from introduction.ood.customer.IndividualCustomer import IndividualCustomer


class Lead(IndividualCustomer):
    def show_phone(self):
        super().show_phone()
        print("Remember that this is a lead customer")

    def __del__(self):
        print("Lead customer object is destroyed")
