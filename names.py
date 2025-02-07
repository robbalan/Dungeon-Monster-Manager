import random
import pandas as pd

# Imports name chunks from CSVs for random name 
try:
    import_goblins = pd.read_csv("goblinnames.csv", header=None).squeeze("columns")
    import_orcs = pd.read_csv("orcnames.csv", header=None).squeeze("columns")
    import_ogres = pd.read_csv("ogrenames.csv", header=None).squeeze("columns")
    import_dragons = pd.read_csv("dragonnames.csv", header=None).squeeze("columns")
except Exception as e:
    print(e)
    print("What's my name again?")

def goblin_names():
    """
    Generates a random name for goblins when hired.
    
    Returns:
        string: a randomly generated goblin name.   
    """
    return(
        import_goblins.iloc[random.randint(0, len(import_goblins)-1)] + 
        import_goblins.iloc[random.randint(0, len(import_goblins)-1)].lower() + 
        import_goblins.iloc[random.randint(0, len(import_goblins)-1)].lower()
        )

def orc_names():
    """
    Generates a random name for orcs when hired.
    
    Returns:
        string: a randomly generated orc name.
    """
    return(
        import_orcs.iloc[random.randint(0, len(import_orcs)-1)] + 
        import_orcs.iloc[random.randint(0, len(import_orcs)-1)].lower()
        )


def ogre_names():
    """
    Generates a random name for ogre when hired.
    
    Returns:
        string: a randomly generated ogre name.    
    """
    return(
        import_ogres.iloc[random.randint(0, len(import_ogres)-1)] + 
        import_ogres.iloc[random.randint(0, len(import_ogres)-1)].lower()
        )


def dragon_names():
    """
    Generates a random name for dragons when hired.
    
    Returns:
        string: a randomly generated dragon name.    
    """
    return(
        import_dragons.iloc[random.randint(0, len(import_dragons)-1)] + 
        import_dragons.iloc[random.randint(0, len(import_dragons)-1)].lower()
        )