from introduction.ood.customer.IndividualCustomer import IndividualCustomer
from introduction.ood.customer.Contact import Contact
from introduction.ood.customer.Lead import Lead

ind1 = IndividualCustomer("Alex", "Sanchez", "532112233")
print("""
*************************
Individual Customer:
*************************""")
print(ind1)
ind1.show_phone()

print("""
*************************
Contact:
*************************""")
cnt1 = Contact("Martin", "Fowler", "532443322")
print(cnt1)
cnt1.show_phone()

print("""
*************************
Lead:
*************************""")
lead = Lead("Rob", "McQuinn", "5357778899")
print(lead)
lead.show_phone()
