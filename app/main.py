class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[f"{self.name}"] = self


def create_person_list(people: list) -> list:
    person_list = [Person(data["name"], data["age"]) for data in people]
    for index in range(len(people)):
        if (people[index].get("wife") or people[index].get("husband")
                in Person.people):
            person_list[index].wife \
                = Person.people.get(people[index].get("wife"))
            person_list[index].husband \
                = Person.people.get(people[index].get("husband"))
    return person_list
