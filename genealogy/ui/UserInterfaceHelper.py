class UserInterfaceHelper:
    @staticmethod
    def print_welcome_message():
        print("""=========================
Welcome to your GENEALOGY
=========================""")

    @staticmethod
    def get_operation():
        return int(input("""
Operations List:
----------------
1 - Add a member to family tree
2 - Set father of a member
3 - Set mother of a member
4 - Set spouse of a member
5 - Show family tree
6 - Show all data
7 - Load from file
8 - Save to file
9 - Exit program

Please select an operation: """))

    @staticmethod
    def show_family_tree(tree, member_id):
        if tree.is_member_exist(member_id):
            person = tree.find_member_by_id(member_id)
            UserInterfaceHelper.print_separation_line()
            print("Name of person: {}".format(person.name))
            print("Spouse of person: {}".format(person.spouse.name)) if person.has_spouse() else None
            UserInterfaceHelper.print_parents(person)
            UserInterfaceHelper.print_separation_line()
        else:
            print("Member with id {} is not exist.".format(member_id))

    @staticmethod
    def print_parents(person, relation=""):
        UserInterfaceHelper.print_separation_line() if person.has_father() or person.has_mother() else None
        print("Name of father{}: {}".format(relation, person.father.name)) if person.has_father() else None
        print("Name of mother{}: {}".format(relation, person.mother.name)) if person.has_mother() else None

        UserInterfaceHelper.print_parents(person.father, " of father" + relation) if person.has_father() else None
        UserInterfaceHelper.print_parents(person.mother, " of mother" + relation) if person.has_mother() else None

    @staticmethod
    def print_separation_line():
        print("====================================================")

    @staticmethod
    def show_all_data(tree):
        print(tree)
