#from create_sub_df import gen_sub_df
import pandas as pd
def trim_df(dataframe,hours):
    frames = []
    

    for x in hours:
        y = pd.DataFrame(dataframe.loc[dataframe['hour'] == x])
        frames.append(y)
    df = pd.concat(frames)
    df.to_csv("sub_df_trim.csv")
    return df
