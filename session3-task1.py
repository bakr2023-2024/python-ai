contacts = {
    "ahmed":"07775000",
    "mona":"012012012",
    "shady":"9909910091",
}
print(contacts.keys())
prompt = input('search by name: ')
if prompt in contacts:
    print(contacts[prompt])
else:
    print('not found')