# from personinfo import Person

# p1 = Person(
#     id="ORCID:9876",
#     full_name="John Doe",
#     aliases=["Johnny", "JD"],
#     phone="123-456-7890",
#     age=30
# )

# print(p1)

from personinfo import Person, PersonStatus

person = Person(id='P1', full_name='Julius Caesar', status="DEAD")
print(f'STATUS={person.status}')
print(f'MEANING={person.status.meaning}')
