class Person:
    def __init__(self, name, father=None, mother=None, spouse=None):
        self.name, self.father, self.mother, self.spouse = name, None, None, None
        self.set_father(father)
        self.set_mother(mother)
        self.set_spouse(spouse)
        self.children = []

    def set_father(self, father):
        if self.has_father():
            self.remove_from_old_parent(self.father)
        self.father = father
        if father is not None:
            self.add_to_new_parent(father)

    def set_mother(self, mother):
        if self.has_mother():
            self.remove_from_old_parent(self.mother)
        self.mother = mother
        if mother is not None:
            self.add_to_new_parent(mother)

    def set_spouse(self, spouse):
        if self.has_spouse():
            self.spouse.spouse = None
        self.spouse = spouse
        if spouse is not None:
            self.spouse.spouse = self

    def has_father(self):
        return self.father is not None

    def has_mother(self):
        return self.mother is not None

    def has_spouse(self):
        return self.spouse is not None

    def add_child(self, child):
        self.children.append(child)

    def add_to_new_parent(self, parent):
        parent.children.append(self)

    def remove_from_old_parent(self, parent):
        parent.children.remove(self)
