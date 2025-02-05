import random
# import pandas

gob_a = ["A", "B", "C"]
gob_b = ["1", "2", "3"]
gob_c = ["X", "Y", "Z"]


def goblin_names():
    """
    Generates a random name for goblins when hired.
    
    Returns:
        string: a randomly generated goblin name.   
    """
    return(gob_a[random.randint(0, len(gob_a)-1)] + gob_b[random.randint(0, len(gob_b)-1)] + gob_c[random.randint(0, len(gob_c)-1)])

def orc_names():
    """
    Generates a random name for orcs when hired, currently uses goblin lists.
    
    Returns:
        string: a randomly generated orc name.
    """
    return(gob_a[random.randint(0, len(gob_a)-1)] + gob_b[random.randint(0, len(gob_b)-1)] + gob_c[random.randint(0, len(gob_c)-1)])

def ogre_names():
    """
    Generates a random name for ogre when hired, currently uses goblin lists.
    
    Returns:
        string: a randomly generated ogre name.    
    """
    return(gob_a[random.randint(0, len(gob_a)-1)] + gob_b[random.randint(0, len(gob_b)-1)] + gob_c[random.randint(0, len(gob_c)-1)])

def dragon_names():
    """
    Generates a random name for dragons when hired, currently uses goblin lists.
    
    Returns:
        string: a randomly generated dragon name.    
    """
    return(gob_a[random.randint(0, len(gob_a)-1)] + gob_b[random.randint(0, len(gob_b)-1)] + gob_c[random.randint(0, len(gob_c)-1)])