#Importing necessary library
def collection_base():
    """
    Parameters
    ----------
    calling basic libraries
    1. Pandas as pd
    2. Numpy as np
    3. matplot.pyplot as plt
    4. Seaborn as sns
    5. Warning(to no show warning)
    6. gc(garbage collector)
    """

    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns
    sns.set_style('whitegrid')
    import warnings
    import gc
    warnings.simplefilter(action='ignore', category=FutureWarning)
    warnings.simplefilter(action='ignore', category=DeprecationWarning)
def collection_upld():
    """
    Parameters
    ----------
    jovian as jv

    """

    import jovian as jv


