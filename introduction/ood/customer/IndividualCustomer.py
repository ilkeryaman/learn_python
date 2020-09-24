class IndividualCustomer:
    def __init__(self, name, surname, phone):
        """
        Constructor
        :param name: Name of customer
        :param surname: Surname of customer
        :param phone: Mobile phone number of customer
        """
        self.name = name
        self.surname = surname
        self.phone = phone

    def __str__(self):
        return "Name: {}, Surname: {}, Phone: {}".format(self.name, self.surname, self.phone)

    def show_phone(self):
        print("Phone: {}".format(self.phone))
