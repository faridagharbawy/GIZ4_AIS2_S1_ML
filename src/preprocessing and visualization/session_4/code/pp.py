import pandas as pd

def chk(df):
 
    dtypes = df.dtypes
    no_unique = df.nunique()
    return pd.DataFrame({'Dtypes': dtypes, 'no of unique' : no_unique}).T