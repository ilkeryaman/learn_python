class MemberIdValidator:
    @staticmethod
    def validate(tree, person_id, father_id, mother_id, spouse_id):
        is_valid = True
        if person_id is not None:
            is_valid = tree.is_member_exist(person_id)
            if not is_valid:
                print("Invalid person id ({}) is supplied.".format(person_id))
        if is_valid and father_id is not None:
            is_valid = tree.is_member_exist(father_id)
            if not is_valid:
                print("Invalid father id ({}) is supplied.".format(father_id))
        if is_valid and mother_id is not None:
            is_valid = tree.is_member_exist(mother_id)
            if not is_valid:
                print("Invalid mother id ({}) is supplied.".format(mother_id))
        if is_valid and spouse_id is not None:
            is_valid = tree.is_member_exist(spouse_id)
            if not is_valid:
                print("Invalid spouse id ({}) is supplied.".format(spouse_id))
        return is_valid
