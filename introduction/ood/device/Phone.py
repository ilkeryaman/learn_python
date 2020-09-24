class Phone:
    def call_someone(self, phone):
        if phone:
            print("{} is calling".format(phone))
        else:
            raise ValueError("Phone must be provided")


"""
__name__ is a special variable for Python. It will be main if and only if this file is run directly.
Below statement will not work, if Phone class is imported to other classes.
"""
if __name__ == "__main__":
    phone = Phone()
    phone.call_someone("+5329998877")

