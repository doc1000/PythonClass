get multiple stats from a dataframe
[[x,len(df[x].unique()),df[x].mean(),df[x].max(),df[x].min(),df[x].median()] for x in df.columns]

pd.DataFrame([[x,len(df[x].unique()),df[x].mean(),df[x].max(),df[x].min(),df[x].median()] for x in df.columns],columns = ['type','len','mean','max','min','med'])


df[(df['pH']>3.0)&(df['pH']<3.5)][df['residual sugar']<2.0]


df.groupby('quality')['chlorides'].mean()

df[(df['pH']>3.0)&(df['pH']<4.0)].groupby('pH')['alcohol'].mean()

For observations with an alcohol value between 9.25 and 9.5, find the highest amount of residual sugar.
df[(df['alcohol']>9.25)&(df['alcohol']<9.5)]['residual sugar'].max()

add a new column
df['total acidity'] = df['fixed acidity'] + df['volatile acidity']

df.sort_values(by='density',ascending=True)['density'][:5]
