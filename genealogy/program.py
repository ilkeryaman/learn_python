from genealogy.enum.Operation import Operation
from genealogy.enum.Relation import Relation
from genealogy.tree.TreeOperator import TreeOperator
from genealogy.ui.UserInterfaceHelper import UserInterfaceHelper


treeOperator = TreeOperator()
UserInterfaceHelper.print_welcome_message()

while True:
    try:
        operation = UserInterfaceHelper.get_operation()

        if operation == Operation.ADD_MEMBER.value:
            try:
                treeOperator.add_member()
            except ValueError as e:
                print(e)
        elif operation == Operation.SET_FATHER.value:
            treeOperator.set_related(Relation.FATHER.value)
        elif operation == Operation.SET_MOTHER.value:
            treeOperator.set_related(Relation.MOTHER.value)
        elif operation == Operation.SET_SPOUSE.value:
            treeOperator.set_related(Relation.SPOUSE.value)
        elif operation == Operation.SHOW_FAMILY_TREE.value:
            treeOperator.show_family_tree()
        elif operation == Operation.SHOW_ALL_DATA.value:
            treeOperator.show_all_data()
        elif operation == Operation.LOAD_FROM_FILE.value:
            treeOperator.load_tree()
        elif operation == Operation.SAVE_TO_FILE.value:
            treeOperator.save_tree()
        elif operation == Operation.EXIT_PROGRAM.value:
            break
        else:
            print("Invalid operation number is supplied.")
    except ValueError:
        print("Invalid operation is supplied.")
