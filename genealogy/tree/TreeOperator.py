from genealogy.entity.Person import Person
from genealogy.entity.Tree import Tree
from genealogy.enum.Relation import Relation
from genealogy.file.FileOperator import FileOperator
from genealogy.ui.UserInterfaceHelper import UserInterfaceHelper
from genealogy.validator.MemberIdValidator import MemberIdValidator
from genealogy.validator.RelationValidator import RelationValidator


class TreeOperator:
    def __init__(self,):
        self.tree = Tree()
        self.file_operator = FileOperator()

    def prepare_and_validate(self, person_id, related_person_id, relation):
        if relation == Relation.FATHER.value:
            father_id, mother_id, spouse_id = related_person_id, None, None
        elif relation == Relation.MOTHER.value:
            father_id, mother_id, spouse_id = None, related_person_id, None
        elif relation == Relation.SPOUSE.value:
            father_id, mother_id, spouse_id = None, None, related_person_id
        else:
            father_id, mother_id, spouse_id = None, None, None

        self.validate(person_id, father_id, mother_id, spouse_id, relation)

    def validate(self, person_id, father_id, mother_id, spouse_id, relation):
        if not MemberIdValidator.validate(self.tree, person_id, father_id, mother_id, spouse_id):
            raise ValueError("Invalid id is supplied.")
        elif not RelationValidator.validate_relations(person_id, father_id, mother_id, spouse_id):
            raise ValueError("Invalid relation.")
        elif relation in (Relation.FATHER.value, Relation.MOTHER.value):
            if not RelationValidator.validate_parents(self.tree, person_id, father_id, mother_id):
                raise ValueError("Father and mother of person should be spouse of each other.")

    @staticmethod
    def set_by_relation(person, related_person, relation):
        if relation == Relation.FATHER.value:
            person.set_father(related_person)
        elif relation == Relation.MOTHER.value:
            person.set_mother(related_person)
        elif relation == Relation.SPOUSE.value:
            person.set_spouse(related_person)
        else:
            raise ValueError("Relation type not found.")

    def add_member(self):
        print("Adding a member ...")
        member_name = input("Member name: ")

        if member_name == "":
            print("Member name is required.")
        else:
            person_id = None
            father_id = input("Id of father (If not exists, press enter): ")
            mother_id = input("Id of mother (If not exists, press enter): ")
            spouse_id = input("Id of spouse (if not exists press enter): ")

            if father_id == "":
                father_id = None
            else:
                father_id = int(father_id)
            if mother_id == "":
                mother_id = None
            else:
                mother_id = int(mother_id)
            if spouse_id == "":
                spouse_id = None
            else:
                spouse_id = int(spouse_id)

            self.validate(person_id, father_id, mother_id, spouse_id, None)
            person = Person(member_name,
                            self.tree.find_member_by_id(father_id),
                            self.tree.find_member_by_id(mother_id),
                            self.tree.find_member_by_id(spouse_id))
            self.tree.add_member(person)

    def set_related(self, relation):
        print("Setting {} ...".format(relation))
        person_id = input("Id of member: ")
        if person_id == "":
            print("Member id is required.")
        else:
            person_id = int(person_id)
            try:
                person = self.tree.find_member_by_id(person_id)
                related_person_id = input("Id of {} (If not exists, press enter): ".format(relation))

                if related_person_id == "":
                    related_person_id = None
                else:
                    related_person_id = int(related_person_id)

                self.prepare_and_validate(person_id, related_person_id, relation)
                related_person = self.tree.find_member_by_id(related_person_id)
                TreeOperator.set_by_relation(person, related_person, relation)
            except ValueError:
                print("Invalid member id ({}) is supplied.".format(person_id))

    def load_tree(self):
        self.tree = Tree()
        relations = []
        lines = self.file_operator.load_from_file()
        for line in lines:
            person_data = line.split(",")
            person = Person(person_data[1])
            relations.append((int(person_data[2]), int(person_data[3]), int(person_data[4])))  # father, mother, spouse
            self.tree.add_member(person)

        i = 0
        while i < len(self.tree.members):
            person = self.tree.members[i][1]
            father_index = relations[i][0]
            mother_index = relations[i][1]
            spouse_index = relations[i][2]
            person.set_father(None if father_index == -1 else self.tree.members[father_index-1][1])
            person.set_mother(None if mother_index == -1 else self.tree.members[mother_index-1][1])
            person.set_spouse(None if spouse_index == -1 else self.tree.members[spouse_index-1][1])
            i += 1

    def save_tree(self):
        if input("Are you sure? (y: yes, n: no): ") in ("Y", "y"):
            members = self.tree.members
            lines = [",".join([
                str(m[0]),
                m[1].name,
                str(self.tree.find_id_by_member(m[1].father)) if m[1].has_father() else "-1",
                str(self.tree.find_id_by_member(m[1].mother)) if m[1].has_mother() else "-1",
                str(self.tree.find_id_by_member(m[1].spouse)) if m[1].has_spouse() else "-1",
                "\n"]) for m in members]
            self.file_operator.save_to_file(lines)

    def show_family_tree(self):
        try:
            member_id = int(input("Id of member: "))
            UserInterfaceHelper.show_family_tree(self.tree, member_id)
        except ValueError:
            print("Invalid value entered.")

    def show_all_data(self):
        UserInterfaceHelper.show_all_data(self.tree)
