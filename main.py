import numpy as np
import uuid


class Emulation:
    """
    Emulates the game "Life" until the Field is empty
    """

    def __init__(self):
        pass

    def period(self):
        """Emulates one time unit. Returns updated Field"""
        pass

    def visualize(self):
        """Visualizes Field for one time unit"""
        pass

    def start(self):
        """Starts emulation by generating world and continuing emulation until the Field is empty"""
        pass


class WorldGeneration:
    """
    Class for world generation. Returns list of instances and field instance

    Arguments:
        self.instances(list): List of instances of classes Carnivore, Herbivore, Omnivore, Plant
        self.field(list): Instance of class Field

    Methods:
        generate: Generates world
    """
    def __init__(self):
        self.instances = list()
        self.field = Field()

    def generate(self):
        """
        Generate Field 100x100 cells and random number of creatures. Returns field matrix
        """
        number_of_instances = np.random.randint(5000, 7000)
        for instance_index in range(number_of_instances):
            # Randomly chooses what to create — animal or plant
            animal = bool(np.random.randint(0, 2))
            instance = None
            if animal:
                animal_choice = np.random.randint(0, 3)
                if animal_choice == 0:
                    # Creates Carnivore instance
                    instance = Carnivore(self.field)
                    # Generates position
                    instance.generate_position()
                elif animal_choice == 1:
                    # Creates Herbivore instance
                    instance = Herbivore(self.field)
                    # Generates position
                    instance.generate_position()
                elif animal_choice == 2:
                    # Creates Omnivore instance
                    instance = Omnivore(self.field)
                    # Generates position
                    instance.generate_position()
            elif not animal:
                # Creates Plant instance
                instance = Plant(self.field)
                # Generates position
                instance.generate_position()
            # Adds instance to self.instances
            self.instances.append(instance)

        return self.instances, self.field

    def create_creature(self):
        """Create Creature instance with random position"""
        assert isinstance(self.field, Field)
        return Creature(self.field)


class Field:
    """

    """
    def __init__(self):
        self.field_list = list()
        for row in range(100):
            row = [None for x in range(100)]
            self.field_list.append(row)

    def occupy_cell(self, cell_position, creature_instance):
        """Set a Creature instance into particular cell by position"""
        self.field_list[cell_position[0]][cell_position[1]] = creature_instance

    def clear_cell(self, cell_position):
        """Set None type of cell by position"""
        self.field_list[cell_position[0]][cell_position[1]] = None


class Position:
    """
    Generates and changes position of the Creature instance in the specific Field instance

    Attributes:
        field (list): instance of class Field
        position (list): current position of the Creature instance
    """
    def __init__(self, field):
        assert isinstance(field, Field)
        self.field = field
        self.position = list()

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
        if creature_instance.size == 1:
            # If the size of the Creature instance is 1 then occupy 1 cell
            self.field.occupy_cell(start_position, creature_instance)
            self.position.append(start_position)
        # If the size of the Creature instance is 2 or 3 then occupy 2 or 3 cells accordingly.
        # We use occupied_cells_counter to occupy only amount of cells that equal to size of the Creature instance
        occupied_cells_counter = 1
        for x in [start_position[0], start_position[0] - 1, start_position[0] + 1]:
            for y in [start_position[1], start_position[1] - 1, start_position[1] + 1]:
                try:
                    if (self.field.field_list[x][y] is None) and (occupied_cells_counter < creature_instance.size):
                        self.field.occupy_cell([x, y], creature_instance)
                        self.position.append([x, y])
                        occupied_cells_counter += 1
                except IndexError:
                    # If the index is out of range we ignore it
                    continue
        # If current surrounding of the Creature instance does not allow to occupy amount of cells
        # that are equal to it's size then we delete this Creature instance.
        if occupied_cells_counter != creature_instance.size:
            del creature_instance

    def change_position(self, creature_instance, move=True, size_change=True):
        """Change position of a Creature instance because of an action"""
        assert isinstance(creature_instance, Creature)
        pass


class Creature:
    """
    Parent class for classes Animal and Plant

    Attributes:

    Methods:

    """
    def __init__(self, field):
        self.age = np.random.randint(0, 100)
        self.mass = np.random.randint(0, 300)
        self.size = int(self.mass/100)+1
        # Creates a Position instance for a Creature instance and generates position by size
        assert isinstance(field, Field)
        self.field = field
        self.position = None

    def generate_position(self):
        self.position = Position(self.field)
        self.position.generate_position(self)

    def grow(self):
        """"""
        pass

    def die(self):
        """"""
        pass

    def reproduce(self):
        """"""
        pass


class Animal(Creature):
    """

    """
    def __init__(self, field):
        super(Animal, self).__init__(field)
        self.sex = bool(np.random.randint(0, 2))
        self.hunger = 0
        self.hp = 100
        self.speed = int(self.hp/20)

    def move(self):
        """"""
        pass


class Carnivore(Animal):
    """

    """
    def __init__(self, field):
        super(Carnivore, self).__init__(field)
        self._aggressiveness = 0

    def __repr__(self):
        return 'Carnivore'

    @property
    def aggressiveness(self):
        return self._aggressiveness

    @aggressiveness.setter
    def aggressiveness(self, updated_aggressiveness=np.random.randint(0, 10)):
        self._aggressiveness = updated_aggressiveness

    def attack(self):
        """"""
        pass


class Herbivore(Animal):
    """

    """

    def __init__(self, field):
        super(Herbivore, self).__init__(field)

    def __repr__(self):
        return 'Herbivore'

    def eat(self):
        """"""
        pass

    def create_pack(self):
        """"""
        pass

    def join_pack(self):
        """"""
        pass


class Omnivore(Animal):
    """

    """

    def __init__(self, field):
        super(Omnivore, self).__init__(field)

    def __repr__(self):
        return 'Omnivore'

    def attack(self):
        """"""
        pass

    def eat(self):
        """"""
        pass


class Pack(Creature):
    """

    """

    def __init__(self, amount):
        super().__init__()
        self.amount = amount
        self.size = super().size

    def __repr__(self):
        return f'Pack {self.amount}'

    def eat(self):
        """"""
        pass


class Plant(Creature):
    """

    """

    def __init__(self, field):
        super(Plant, self).__init__(field)
        self.toxicity = bool(np.random.randint(0, 2))

    def __repr__(self):
        return 'Plant'


a = WorldGeneration()
for row in a.generate()[1].field_list:
    for instance in row:
        if instance is not None:
            print(instance.size)