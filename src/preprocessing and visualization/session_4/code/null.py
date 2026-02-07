import pandas as pd

def chk_nulls(pd):
    null = df.isnull().sum()
    ratio = null / df.shape[0]
    return pd.DataFrame({'Null': null, 'Ratio' : ratio}).T