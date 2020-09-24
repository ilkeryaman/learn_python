class RelationValidator:
    @staticmethod
    def validate_relations(person_id, father_id, mother_id, spouse_id):
        is_relations_valid = True

        if person_id is not None:
            if father_id is not None and person_id == father_id:
                print("Member cannot be his/her own father.")
                is_relations_valid = False
            elif mother_id is not None and person_id == mother_id:
                print("Member cannot be his/her own mother.")
                is_relations_valid = False
            elif spouse_id is not None and person_id == spouse_id:
                print("Member cannot be his/her own spouse.")
                is_relations_valid = False

        if father_id is not None and mother_id is not None:
            if father_id == mother_id:
                print("Father and mother of member cannot be same person.")
                is_relations_valid = False

        if spouse_id is not None:
            if father_id is not None and father_id == spouse_id:
                print("Father and spouse of member cannot be same person.")
                is_relations_valid = False
            if mother_id is not None and mother_id == spouse_id:
                print("Mother and spouse of member cannot be same person.")
                is_relations_valid = False

        return is_relations_valid

    @staticmethod
    def validate_parents(tree, person_id, father_id, mother_id):
        is_parents_valid = True
        person = tree.find_member_by_id(person_id)
        if father_id is None and mother_id is not None and person.has_father():
            mother = tree.find_member_by_id(mother_id)
            if mother.spouse != person.father:
                is_parents_valid = False
        elif father_id is not None and mother_id is None and person.has_mother():
            father = tree.find_member_by_id(father_id)
            if father.spouse != person.mother:
                is_parents_valid = False
        return is_parents_valid


