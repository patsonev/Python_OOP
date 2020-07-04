class Lion:

    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
        self.type = "Lion"

    def get_needs(self):
        return int(50)

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"


class Tiger:

    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
        self.type = "Tiger"

    def get_needs(self):
        return int(45)

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"


class Cheetah:

    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
        self.type = "Cheetah"

    def get_needs(self):
        return int(60)

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"


class Keeper:

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        self.type = "Keeper"

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}"


class Caretaker:

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        self.type = "Caretaker"

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}"


class Vet:

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        self.type = "Vet"

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}"


class Zoo:

    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if len(self.animals) < self.__animal_capacity and price <= self.__budget:
            self.__budget -= price
            self.animals.append(animal)
            # tova e ako nqmame self.type vyv klasovete po gore
            #return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
            return f"{animal.name} the {animal.type} added to the zoo"
        elif price > self.__budget:
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {worker.type} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        to_pay_workers = sum([worker.salary for worker in self.workers])
        if self.__budget >= to_pay_workers:
            self.__budget -= to_pay_workers
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        to_tend_animals = sum(animal.get_needs() for animal in self.animals)
        if self.__budget >= to_tend_animals:
            self.__budget -= to_tend_animals
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = ""
        result += f"You have {len(self.animals)} animals\n"
        result += f"----- {len([animal for animal in self.animals if animal.type == 'Lion'])} Lions:\n"
        for animal in self.animals:
            if animal.type == 'Lion':
                result += f"{repr(animal)}\n"
        result += f"----- {len([animal for animal in self.animals if animal.type == 'Tiger'])} Tigers:\n"
        for animal in self.animals:
            if animal.type == 'Tiger':
                result += f"{repr(animal)}\n"
        result += f"----- {len([animal for animal in self.animals if animal.type == 'Cheetah'])} Cheetahs:\n"
        for animal in self.animals:
            if animal.type == 'Cheetah':
                result += f"{repr(animal)}\n"
        return result

    def workers_status(self):
        result = ""
        result += f"You have {len(self.workers)} workers\n"
        result += f"----- {len([worker for worker in self.workers if worker.type == 'Keeper'])} Keepers:\n"
        for worker in self.workers:
            if worker.type == "Keeper":
                result += f"{repr(worker)}\n"
        result += f"----- {len([worker for worker in self.workers if worker.type == 'Caretaker'])} Caretakers:\n"
        for worker in self.workers:
            if worker.type == "Caretaker":
                result += f"{repr(worker)}\n"
        result += f"----- {len([worker for worker in self.workers if worker.type == 'Vet'])} Vets:\n"
        for worker in self.workers:
            if worker.type == "Vet":
                result += f"{repr(worker)}\n"
        return result


zoo = Zoo("Zootopia", 3000, 5, 8)

# Animals creation
animals = [Cheetah("Cheeto", "Male", 2), Cheetah("Cheetia", "Female", 1), Lion("Simba", "Male", 4), Tiger("Zuba", "Male", 3), Tiger("Tigeria", "Female", 1), Lion("Nala", "Female", 4)]

# Animal prices
prices = [200, 190, 204, 156, 211, 140]

# Workers creation
workers = [Keeper("John", 26, 100), Keeper("Adam", 29, 80), Keeper("Anna", 31, 95), Caretaker("Bill", 21, 68), Caretaker("Marie", 32, 105), Caretaker("Stacy", 35, 140), Vet("Peter", 40, 300), Vet("Kasey", 37, 280), Vet("Sam", 29, 220)]

# Adding all animals
for i in range(len(animals)):
    animal = animals[i]
    price = prices[i]
    print(zoo.add_animal(animal, price))

# Adding all workers
for worker in workers:
    print(zoo.hire_worker(worker))
# Tending animals
print(zoo.tend_animals())

# Paying keepers
print(zoo.pay_workers())

# Fireing worker
print(zoo.fire_worker("Adam"))

# Printing statuses
print(zoo.animals_status())
print(zoo.workers_status())
