"""Functions to parse a file containing villager data."""


def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - set[str]: a set of strings
    """

    species = set()

    # open file so that it will automatically close
    with open(filename) as file:
        # evaluate each line
        for line in file:

            # strip trailing spaces and create list using '|' as a value separator
            line = line.rstrip().split('|')
            
            # add the 2nd value of line to species set
            species.add(line[1])

    return species

# print(all_species('villagers.csv'))

def get_villagers_by_species(filename, search_string="All"):
    """Return a list of villagers' names by species.

    Arguments:
        - filename (str): the path to a data file
        - search_string (str): optional, the name of a species

    Return:
        - list[str]: a list of names
    """

    villagers = []

    # open file so that it will automatically close
    with open(filename) as file:

        # evaluate each line
        for line in file:

            # strip trailing spaces and create list using '|' as a value separator
            line = line.rstrip().split('|')

            # check if species (line[1]) is equal to search_string
            if line[1] == search_string or search_string == 'All':
                
                # add villager name to villagers list
                villagers.append(line[0])

    return sorted(villagers)

# print(get_villagers_by_species('villagers.csv', 'Wolf'))

def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """

    names = [[],[],[],[],[],[]]

    hobbies = ['Fitness', 'Nature', 'Education', 'Music', 'Fashion', 'Play']

    # open file so that it will automatically close
    with open(filename) as file:

        # evaluate each line
        for line in file:

            # strip trailing spaces and create list using '|' as a value separator
            line = line.rstrip().split('|')

            # for loop to Fitness, Nature, Education, Music, Fashion, then Play
            for idx in range(6):
                if line[3] == hobbies[idx]:
                    names[idx].append(line[0])
            
    return names

print(all_names_by_hobby('villagers.csv'))

def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """

    all_data = []

    # open file so that it will automatically close
    with open(filename) as file:

        # evaluate each line
        for line in file:

            # strip trailing spaces and create list using '|' as a value separator
            line = tuple(line.rstrip().split('|'))

            all_data.append(line)

    return all_data

# print(all_data('villagers.csv'))

def find_motto(filename, villager_name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - str: the villager's motto or None
    """

    info = all_data(filename)

    # evaluate each line
    for line in info:

        # return motto if line matches villagers name
        if line[0] == villager_name:
            return line[4]
    
    return None

# print(find_motto('villagers.csv', 'Audie'))

def find_likeminded_villagers(filename, villager_name):
    """Return a set of villagers with the same personality as the given villager.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name
    
    Return:
        - set[str]: a set of names

    For example:
        >>> find_likeminded_villagers('villagers.csv', 'Wendy')
        {'Bella', ..., 'Carmen'}
    """


    info = all_data(filename)

    # evaluate each line
    for line in info:

        # find villager then find their personality
        if line[0] == villager_name:
            personality = line[2]
            break

    villagers = set()

    # evaluate each line
    for line in info:

        # create set of villagers with given personality
        if line[2] == personality:
            villagers.add(line[0])

    return villagers

# print(find_likeminded_villagers('villagers.csv', 'Skye'))