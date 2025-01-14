import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
# 1
df = pd.read_csv('medical_examination.csv')
print(df.columns)
# 2
df['overweight'] = (df['weight']/((df['height']/100)**2)) > 25
df['overweight'] = df['overweight'].replace({True: 1, False: 0})
# 3 0 = always good, 1 = always bad
df['cholesterol'] = df['cholesterol'].map(lambda x: 0 if x == 1 else 1)
df['gluc'] = df['gluc'].map(lambda x: 0 if x == 1 else 1)
# 4
def draw_cat_plot():
    # 5

    # 6

    # 7

    # 8

    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # 12
    corr = round(df_heat.corr(), 2)

    # 13



    # 14


    # 15



    # 16
    fig.savefig('heatmap.png')
    return fig
