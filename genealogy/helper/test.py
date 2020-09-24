from genealogy.entity.Person import Person

list1 = [(1, "ilker")]
print(len(list(filter(lambda l: l is not None and l[0] == 2, list1))))
f = list(filter(lambda l: l is not None and l[0] == 1, list1))
print(f)

count_of_member = 5
member_id = count_of_member = count_of_member + 1
print(member_id)

p = Person("ilker")
p2 = Person("mahmut")
p3 = Person("mehmet")
p4 = Person("rıza")
p.children.append(p2)
p.children.append(p3)
p.children.append(p4)
print(p.children)
p.children.remove(p3)
print(p.children)
