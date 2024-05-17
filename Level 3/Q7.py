def create_dict(names, subjects):
    return {name: subject for name, subject in zip(names, subjects)}

names = ['Sam', 'Alice', 'Mona']
subjects = ['Commerce', 'Science', 'Computer']
result_dict = create_dict(names, subjects)
print(result_dict)
