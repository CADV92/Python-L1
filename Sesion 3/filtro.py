DATA = [
    {
        'name': 'Mario',
        'age': 72,
        'organization': 'Chambita 1',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisa',
        'age': 33,
        'organization': 'Chambita 2',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Ulises',
        'age': 19,
        'organization': 'Chambita 1',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Chambita 1',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Chambita 1',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Chambita 3',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Chambita 4',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def run():

    # Comprehensions solutions
    all_python_devs = [worker["name"] for worker in DATA if worker["language"] == "python"]
    all_Chambita1_workers = [worker["name"] for worker in DATA if worker["organization"] == "Chambita 1"]
    adults =  [worker["name"] for worker in DATA if worker["age"] > 18]
    # old_people = list(map(lambda worker: worker | {"old": worker["age"] > 70}, DATA))
    old_people = list(map(lambda worker: {**worker, **{"old": worker["age"] > 70}}, DATA))

    for worker in all_python_devs:
        print(worker)


if __name__ == '__main__':
    run()