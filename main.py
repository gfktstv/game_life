import numpy as np
from time import sleep


class Emulation:
    """
    Emulates the game "Life" until the Field is empty
    """
    def __init__(self):
        self.creatures = None
        self.field = None

    def period(self):
        """Emulates one time unit. Returns updated Field"""
        for creature in self.creatures:
            creature.move()
        print('---'*10)


    def visualize(self):
        """Visualizes Field for one time unit"""
        pass

    def start(self):
        """Starts emulation by generating world and continuing emulation until the Field is empty"""
        print('Game has started!')
        sleep(1)
        self.creatures, self.field = WorldGeneration().generate()
        sleep(1)
        while len(self.creatures) > 0:
            print(f'Amount of creatures on the field: {len(self.creatures)}')
            sleep(1)
            self.period()


class WorldGeneration:
    """
    Class for world generation. Returns list of instances and field instance

    Arguments:
        self.creatures(list): List of instances of classes Carnivore, Herbivore, Omnivore, Plant
        self.field(list): Instance of class Field

    Methods:
        generate: Generates world
    """
    def __init__(self):
        self.creatures = list()
        self.field = Field()

    def generate(self, number_of_creatures=np.random.randint(5000, 7000)):
        """
        Generate Field 100x100 cells and random number of creatures. Returns field matrix
        """
        number_of_creatures = 10000
        for creature_index in range(number_of_creatures):
            # Randomly chooses what to create — animal or plant
            animal = bool(np.random.randint(0, 2))
            creature = None
            if animal:
                animal_choice = np.random.randint(0, 3)
                if animal_choice == 0:
                    # Creates Carnivore instance
                    creature = Carnivore(self.field, self.creatures)
                    # Generates position
                    creature.generate_position()
                elif animal_choice == 1:
                    # Creates Herbivore instance
                    creature = Herbivore(self.field, self.creatures)
                    # Generates position
                    creature.generate_position()
                elif animal_choice == 2:
                    # Creates Omnivore instance
                    creature = Omnivore(self.field, self.creatures)
                    # Generates position
                    creature.generate_position()
            elif not animal:
                # Creates Plant instance
                creature = Plant(self.field, self.creatures)
                # Generates position
                creature.generate_position()
            # Adds instance to self.creatures
            self.creatures.append(creature)
        print('---' * 10)
        print('World generated')
        print('---' * 10)
        return self.creatures, self.field

    def create_creature(self):
        """Create Creature instance with random position"""
        assert isinstance(self.field, Field)
        return Creature(self.field, self.creatures)


class Field:
    """
    Stores field list and updates cells of the field

    Attributes:
        field_list(list): Field matrix

    Methods:
        occupy_cell: Sets a Creature instance into particular cell by position
        leave_cell: Removes a Creature instance from particular cell by position

    """
    def __init__(self):
        self.field_list = list()
        for row in range(100):
            row = [None for x in range(100)]
            self.field_list.append(row)

    def occupy_cell(self, cell_position, creature_instance):
        """Sets a Creature instance into particular cell by position"""
        cell = self.field_list[cell_position[0]][cell_position[1]]
        if cell is None:
            # Sets a creature instance to the empty cell
            self.field_list[cell_position[0]][cell_position[1]] = creature_instance
        elif type(cell) is list:
            # Appends to a list if the cell is already occupied by two or more creatures
            cell.append(creature_instance)
        else:
            # Creates a list if the cell is already occupied by one creature
            cell_list = list()
            cell_list.append(cell)
            cell_list.append(creature_instance)
            self.field_list[cell_position[0]][cell_position[1]] = cell_list

    def leave_cell(self, cell_position, creature_instance):
        """Removes a Creature instance from particular cell by position"""
        cell = self.field_list[cell_position[0]][cell_position[1]]
        if cell is creature_instance:
            # Sets None if there is only the Creature instance
            cell = None
        elif type(cell) is list:
            # Removes from a list if there is more than one Creature instance
            cell.remove(creature_instance)

        # Checks if the list in the cell is empty
        if cell == list():
            cell = None

    def expand(self):
        """Expands field_list for 5 cells in each side"""
        # Adds 5 new cells in the beginning and in the end of each existing row
        for exisiting_row in self.field_list:
            for new_cell in range(5):
                exisiting_row.insert(new_cell, None)
                exisiting_row.append(None)

        new_row_len = len(self.field_list[0]) + 10
        # Adds 5 new rows above with additional 5 elements in the beginning and in the end
        for new_row in range(5):
            self.field_list.insert(new_row, [None for x in range(new_row_len)])
        # Adds 5 new rows below with additional 5 elements in the beginning and in the end
        for new_row in range(5):
            self.field_list.append([None for x in range(new_row_len)])


class Position:
    """
    Generates and changes position of the Creature instance in the specific Field instance

    Attributes:
        field (list): instance of class Field
        coordinates_list (list): current coordinates of the Creature instance
    """
    def __init__(self, field):
        assert isinstance(field, Field)
        self.field = field
        self.coordinates_list = list()

    def generate_position(self, creature_instance):
        """
        Generates position for a Creature instance by its size.
        If there is no room for it's size then we do not create position and delete the Creature instance
        """
        assert isinstance(creature_instance, Creature)
        # Creates start position for the Creature instance
        start_position = [np.random.randint(0, 100), np.random.randint(0, 100)]
        if self.field.field_list[start_position[0]][start_position[1]] is not None:
            # Changes position if it is occupied in the field
            start_position = [np.random.randint(0, 100), np.random.randint(0, 100)]
        # Occupies start position cell with the Creature instance
        self.field.occupy_cell(start_position, creature_instance)
        self.coordinates_list.append(start_position)
        # If the size of the Creature instance is 2 or 3 then occupy 2 or 3 cells accordingly.
        # We use occupied_cells_counter to occupy only amount of cells that equal to size of the Creature instance
        if creature_instance.size >= 2:
            occupied_cells_counter = 1
            for x in [start_position[0], start_position[0] - 1, start_position[0] + 1]:
                for y in [start_position[1], start_position[1] - 1, start_position[1] + 1]:
                    try:
                        if (self.field.field_list[x][y] is None) and (occupied_cells_counter < creature_instance.size):
                            self.field.occupy_cell([x, y], creature_instance)
                            self.coordinates_list.append([x, y])
                            occupied_cells_counter += 1
                    except IndexError:
                        # If the index is out of range we ignore it
                        continue
            # If current surrounding of the Creature instance does not allow to occupy amount of cells
            # that are equal to it's size then we delete this Creature instance.
            if occupied_cells_counter != creature_instance.size:
                del creature_instance

    def change_position(self, animal_instance, new_coordinates, relocate=False, size_change=False):
        """Change position of a Creature instance because of an action"""
        assert isinstance(animal_instance, Animal)
        try:
            self.field.field_list[new_coordinates[0]][new_coordinates[1]]
        except IndexError:
            print('Field expanded')
            sleep(5)
            self.field.expand()

        # Changes position if an Animal instance relocates
        if relocate:
            # Clears old positions
            for coordinates in self.coordinates_list:
                self.field.leave_cell(coordinates, animal_instance)
            # Clears coordinates list
            self.coordinates_list = list()
            # Sets new coordinates
            self.coordinates_list.append(new_coordinates)
            self.field.occupy_cell(self.coordinates_list[0], animal_instance)
            # Occupies additional cells if size of the animal is 2 or 3
            occupied_cells_counter = 1
            if (animal_instance.size == 2) or (animal_instance.size == 3):
                for x in [new_coordinates[0], new_coordinates[0] - 1, new_coordinates[0] + 1]:
                    for y in [new_coordinates[1], new_coordinates[1] - 1, new_coordinates[1] + 1]:
                        try:
                            if occupied_cells_counter < animal_instance.size:
                                self.field.occupy_cell([x, y], animal_instance)
                                self.coordinates_list.append([x, y])
                                occupied_cells_counter += 1
                        except IndexError:
                            # If the index is out of range we ignore it
                            continue

        if size_change:
            pass

    def set_position(self, coordinates, creature_instance):
        start_position = coordinates
        # Occupies start position cell with the Creature instance
        self.field.occupy_cell(start_position, creature_instance)
        self.coordinates_list.append(start_position)
        # If the size of the Creature instance is 2 or 3 then occupy 2 or 3 cells accordingly.
        # We use occupied_cells_counter to occupy only amount of cells that equal to size of the Creature instance
        if creature_instance.size >= 2:
            occupied_cells_counter = 1
            for x in [start_position[0], start_position[0] - 1, start_position[0] + 1]:
                for y in [start_position[1], start_position[1] - 1, start_position[1] + 1]:
                    try:
                        if occupied_cells_counter < creature_instance.size:
                            self.field.occupy_cell([x, y], creature_instance)
                            self.coordinates_list.append([x, y])
                            occupied_cells_counter += 1
                    except IndexError:
                        # If the index is out of range we ignore it
                        continue


class Creature:
    """
    Parent class for classes Animal and Plant

    Attributes:

    Methods:

    """
    def __init__(self, field, creatures):
        self.age = np.random.randint(0, 30)
        self.mass = np.random.randint(0, 300)
        self.size = int(self.mass/100)+1
        # Creates a Position instance for a Creature instance and generates position by size
        assert isinstance(field, Field)
        self.field = field
        self.creatures = creatures
        self.position = None

    def aging(self):
        self.age += 1
        if self.age >= 30:
            self.die()

    def generate_position(self):
        self.position = Position(self.field)
        self.position.generate_position(self)

    def set_position(self, position):
        """Sets position for a new creature produced by reproduction"""
        self.position = Position(self.field)
        self.position.set_position(position, self)

    def die(self):
        """Emulates death of the creature instance. Deletes the creature instance and clear occupied cells"""
        try:
            self.creatures.remove(self)
        except ValueError:
            pass
        print(f'Creature {self} died')
        del self


class Animal(Creature):
    """

    """
    def __init__(self, field, creatures):
        super(Animal, self).__init__(field, creatures)
        self.sex = bool(np.random.randint(0, 2))
        self.hunger = 0
        self.hp = 100
        self.hit = np.random.randint(15, 45)
        self.speed = int(self.hp/20)
        self.surroundings = list()

    def update_hp(self):
        self.hp = 100 - self.hunger
        if self.hp <= 0:
            self.die()

    def update_mass(self):
        self.mass -= 0.2 * self.mass
        if self.mass <= 0:
            self.die()

    def relocate(self):
        """Relocates the Animal instance into new position"""
        x = np.random.randint(-self.speed, self.speed)
        y = np.random.randint(-self.speed, self.speed)
        print(f'Creature {self} changed its position')
        self.position.change_position(self, [x, y], relocate=True)

    def period(self):
        """Emulates aging and hp, hunger and mass loss each move"""
        self.aging()
        self.hunger += 15 + 0.2 * self.mass
        self.update_hp()
        self.update_mass()


class Carnivore(Animal):
    """

    """
    def __init__(self, field, creatures):
        super(Carnivore, self).__init__(field, creatures)
        # Each move aggressiveness updates. At the beginning (generation) it is equal 0
        self.aggressiveness = 0

    def __repr__(self):
        return 'Carnivore'

    def attack(self):
        """
        Attacks another creature if conditions such as the same position,
        particular hunger and aggressiveness levels allow it
        """
        # Checks each coordinate that the carnivore occupies for other creatures to attack
        for coordinates in self.position.coordinates_list:
            # If there is creatures in
            if type(self.field.field_list[coordinates[0]][coordinates[1]]) is list:
                # Creates list of creatures that are in cells that the carnivore occupies
                creatures_list = self.field.field_list[coordinates[0]][coordinates[1]]
                # Attacks each creature in the list if the carnivore is hungry/aggressive
                for creature in creatures_list:
                    # Conditions for attack on a carnivore instance
                    if (type(creature) is Carnivore) and (self.hunger > 30) and (self.aggressiveness > 30):
                        self.fight(creature)
                    # Conditions for attack on a herbivore or omnivore instance
                    elif ((type(creature) is Herbivore) or (type(creature) is Omnivore)) and (self.hunger > 30):
                        self.fight(creature)
                    # If it's a plant instance
                    else:
                        pass
            # If there is no creatures
            if type(self.field.field_list[coordinates[0]][coordinates[1]]) == self:
                pass

    def fight(self, animal_instance):
        """Emulates fight between the carnivore and an animal instance"""
        print(f'Fight between {self} and {animal_instance} was started!')
        if type(animal_instance) is Herbivore:
            # Sets win probability for the carnivore (based on hunger) and for the herbivore instances
            if self.hunger > 50:
                carnivore_win_probability = np.random.randint(0, 100) + self.hunger*0.1
            else:
                carnivore_win_probability = np.random.randint(0, 100) - self.hunger*0.1
            herbivore_win_probability = np.random.randint(0, 100)

            if carnivore_win_probability >= herbivore_win_probability:
                print(f'{self} won')
                self.hunger = 0
                self.mass += 0.5 * animal_instance.mass
                animal_instance.die()
            else:
                print(f'{self} lost')
                self.hp -= animal_instance.hit
        elif (type(animal_instance) is Omnivore) or (type(animal_instance) is Carnivore):
            # Sets win probability for the attacking carnivore based on mass and aggressiveness
            attacker_win_probability = np.random.randint(0, 100) + self.mass*0.3 + self.aggressiveness * 0.2
            # Sets win probability for the defending animal based on mass (increased mass parameter)
            defender_win_probability = np.random.randint(0, 100) + self.mass*0.5

            if attacker_win_probability >= defender_win_probability:
                print(f'{self} won')
                self.hunger = 0
                self.mass += 0.5 * animal_instance.mass
                animal_instance.die()
            else:
                print(f'{self} lost')
                animal_instance.hunger = 0
                animal_instance.mass += 0.5 * self.mass
                self.die()

    def reproduce(self):
        for coordinates in self.position.coordinates_list:
            if type(self.field.field_list[coordinates[0]][coordinates[1]]) is list:
                for creature in self.field.field_list[coordinates[0]][coordinates[1]]:
                    same_type = type(creature) is type(self)
                    if same_type:
                        sufficient_age = (creature.age >= 20) and (self.age >= 20)
                        different_sex = creature.sex is not self.sex
                        if sufficient_age and different_sex:
                            self.create_child(coordinates)
                    else:
                        pass
            else:
                pass

    def create_child(self, coordinates):
        child = Carnivore(self.field, self.creatures)
        child.set_position(coordinates)
        print(f'{child} born!')
        return child

    def move(self):
        """Makes a move of a Carnivore instance"""
        self.period()
        relocate_choice = bool(np.random.randint(0, 2))
        if relocate_choice is True:
            self.relocate()
        self.aggressiveness = np.random.randint(0, 100)
        self.attack()
        self.reproduce()


class Herbivore(Animal):
    """

    """

    def __init__(self, field, creatures):
        super(Herbivore, self).__init__(field, creatures)

    def __repr__(self):
        return 'Herbivore'

    def eat(self):
        """Emulates eating plant"""
        for coordinates in self.position.coordinates_list:
            if type(self.field.field_list[coordinates[0]][coordinates[1]]) == list:
                # Creates list of creatures that are in cells that the herbivore occupies
                creatures_list = self.field.field_list[coordinates[0]][coordinates[1]]
                for creature in creatures_list:
                    if type(creature) is Plant:
                        if creature.toxicity:
                            if bool(np.random.randint(0, 2)):
                                self.die()
                        else:
                            print(f'{self} ate {creature}')
                            self.hunger = self.hunger - creature.mass
                            if self.hunger < 0:
                                self.hunger = 0
                            self.mass += 0.5 * creature.mass
                            creature.die()

    def reproduce(self):
        for coordinates in self.position.coordinates_list:
            if type(self.field.field_list[coordinates[0]][coordinates[1]]) is list:
                for creature in self.field.field_list[coordinates[0]][coordinates[1]]:
                    same_type = type(creature) is type(self)
                    if same_type:
                        sufficient_age = (creature.age >= 20) and (self.age >= 20)
                        different_sex = creature.sex is not self.sex
                        if sufficient_age and different_sex:
                            self.create_child(coordinates)
                    else:
                        pass
            else:
                pass

    def create_child(self, coordinates):
        child = Herbivore(self.field, self.creatures)
        child.set_position(coordinates)
        print(f'{child} born!')
        return child

    def move(self):
        """Makes a move of a Herbivore instance"""
        self.period()
        relocate_choice = bool(np.random.randint(0, 2))
        if relocate_choice is True:
            self.relocate()
        self.eat()
        self.reproduce()


class Omnivore(Animal):
    """

    """

    def __init__(self, field, creatures):
        super(Omnivore, self).__init__(field, creatures)

    def __repr__(self):
        return 'Omnivore'

    def attack(self):
        """
        Attacks another creature if another creature in the same cell and the Omnivore instance is hungry
        """
        # Checks each coordinate that the carnivore occupies for other creatures to attack
        for coordinates in self.position.coordinates_list:
            # If there is creatures in
            if type(self.field.field_list[coordinates[0]][coordinates[1]]) is list:
                # Creates list of creatures that are in cells that the carnivore occupies
                creatures_list = self.field.field_list[coordinates[0]][coordinates[1]]
                # Attacks each creature in the list if the carnivore is hungry/aggressive
                for creature in creatures_list:
                    # Conditions for attack on an animal instance
                    if (type(creature) is not Plant) and (self.hunger > 30):
                        self.fight(creature)
            # If there is no creatures
            if type(self.field.field_list[coordinates[0]][coordinates[1]]) == self:
                pass

    def eat(self):
        """Emulates eating plant"""
        for coordinates in self.position.coordinates_list:
            if type(self.field.field_list[coordinates[0]][coordinates[1]]) == list:
                # Creates list of creatures that are in cells that the herbivore occupies
                creatures_list = self.field.field_list[coordinates[0]][coordinates[1]]
                for creature in creatures_list:
                    if type(creature) is Plant:
                        if creature.toxicity:
                            self.die()
                        else:
                            print(f'{self} ate {creature}')
                            self.hunger = self.hunger - creature.mass
                            self.mass += 0.5 * creature.mass
                            creature.die()

    def fight(self, animal_instance):
        """Emulates fight between the carnivore and an animal instance"""
        print(f'Fight between {self} and {animal_instance} started!')
        if type(animal_instance) is Herbivore:
            # Sets win probability for the carnivore (based on hunger) and for the herbivore instances
            if self.hunger > 50:
                carnivore_win_probability = np.random.randint(0, 100) + self.hunger*0.1
            else:
                carnivore_win_probability = np.random.randint(0, 100) - self.hunger*0.1
            herbivore_win_probability = np.random.randint(0, 100)

            if carnivore_win_probability >= herbivore_win_probability:
                print(f'{self} won')
                self.hunger = 0
                self.mass += 0.5 * animal_instance.mass
            else:
                print(f'{self} lost')
                self.hp -= animal_instance.hit
        elif (type(animal_instance) is Omnivore) or (type(animal_instance) is Carnivore):
            # Sets win probability for the attacking carnivore based on mas
            attacker_win_probability = np.random.randint(0, 100) + self.mass*0.5
            # Sets win probability for the defending animal based on mass (increased mass parameter)
            defender_win_probability = np.random.randint(0, 100) + self.mass*0.5

            if attacker_win_probability >= defender_win_probability:
                print(f'{self} won')
                self.hunger = 0
                self.mass += 0.5 * animal_instance.mass
                animal_instance.die()
            else:
                print(f'{self} lost')
                animal_instance.hunger = 0
                animal_instance.mass += 0.5 * self.mass
                self.die()

    def reproduce(self):
        tumbler = False
        for coordinates in self.position.coordinates_list:
            if tumbler:
                break
            if type(self.field.field_list[coordinates[0]][coordinates[1]]) is list:
                for creature in self.field.field_list[coordinates[0]][coordinates[1]]:
                    same_type = type(creature) is type(self)
                    if same_type:
                        sufficient_age = (creature.age >= 30) and (self.age >= 30)
                        different_sex = creature.sex is not self.sex
                        if sufficient_age and different_sex:
                            self.create_child(coordinates)
                            tumbler = True
                            break
                    else:
                        pass
            else:
                pass

    def create_child(self, coordinates):
        child = Omnivore(self.field, self.creatures)
        child.set_position(coordinates)
        print(f'{child} born!')
        return child

    def move(self):
        """Makes a move of the Herbivore instance"""
        self.period()
        relocate_choice = bool(np.random.randint(0, 2))
        if relocate_choice is True:
            self.relocate()
        self.eat()
        self.attack()
        self.reproduce()


class Plant(Creature):
    """

    """

    def __init__(self, field, creature):
        super(Plant, self).__init__(field, creature)
        self.toxicity = bool(np.random.randint(0, 2))

    def __repr__(self):
        return 'Plant'

    def update_mass(self):
        self.mass += 50
        if self.mass > 300:
            self.mass = 300

    def period(self):
        """Emulates aging and mass grow or reproduction"""
        self.aging()
        choice = np.random.randint(0, 10)
        if choice == 0:
            self.reproduce()
        else:
            self.update_mass()

    def reproduce(self):
        """Reproduces new plant in one of the near cells"""
        coordinates_index = np.random.randint(0, len(self.position.coordinates_list))
        coordinates = self.position.coordinates_list[coordinates_index]
        self.create_child(coordinates)

    def create_child(self, coordinates):
        child = Plant(self.field, self.creatures)
        child.set_position(coordinates)
        print(f'{child} born!')
        return child

    def move(self):
        """Makes a move of a Plant instance"""
        self.period()


for i in range(10):
    Emulation().start()