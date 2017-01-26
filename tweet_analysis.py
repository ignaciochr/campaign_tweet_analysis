# Python Notebook - Untitled Report

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = df[['candidato', 'creado', 'creado_semana', 'fav', 'rt', 'texto', 'url', 'hashtag', 'pregunta', 'exclamacion', 'mention', 'empleo' ]]
df['creado_dia'] = df['creado']
df['creado_dia'] = pd.to_datetime(df['creado_dia'])

s = "01/01/2017"
ts = time.mktime(datetime.datetime.strptime(s, "%d/%m/%Y").timetuple())
value = datetime.datetime.fromtimestamp(ts)
df2 = df[df['creado_dia'].apply(lambda x: x >= value)]
df3 = df2[['candidato', 'creado', 'creado_semana', 'fav', 'rt', 'texto', 'url', 'hashtag', 'pregunta', 'exclamacion', 'mention', 'empleo']]
dfp = df3.pivot_table(index='creado',columns='candidato',values='rt',aggfunc='count')

# Define and plot bar graph with Matplotlib
dfp.plot(kind='bar', stacked=True, figsize=[16,6], color=['r', 'b', 'g'])

# Define and plot boxplot with Seaborn
plt.figure(figsize=(9, 9))
sns.set_style("white")
plt.ylim(-100, 4000)
sns.despine(top=True)
sns.boxplot(x="candidato", y="rt", order=['Guillermo_Lasso','Lenin_Moreno', 'Cynthia_Viteri'], data=df3)

# Define and plot swarmplot with Seaborn
sns.set_style("white")
plt.figure(figsize=(12, 8))
plt.ylim(0, 1300)
sns.swarmplot(x="creado_semana", y="rt", hue="candidato", hue_order=['Guillermo_Lasso','Lenin_Moreno', 'Cynthia_Viteri'], size=10, data=df3[::-1], edgecolor="white")
sns.despine(top=True)

top_tw = df3
top_tw['engagements'] = top_tw['rt'] + top_tw['fav']
df3['longitud'] = df3['texto'].apply(lambda x: len(x))
df3['engagements'] = df3['rt'] + df3['fav']
eng_vs_long = df3[['candidato','creado','longitud','engagements']]

# Print candidate mean engagements and tweet length
print top_tw.groupby(['candidato'])[["engagements",'longitud']].mean()

# Define and plot pairplot with Seaborn
sns.set(style="ticks", color_codes=True)
sns.pairplot(eng_vs_long, hue="candidato", hue_order=['Guillermo_Lasso','Lenin_Moreno', 'Cynthia_Viteri'], size=5)

tz2 = top_tw.groupby(['candidato', 'hashtag'])[["engagements"]].mean()
tz2['engagements'] = tz2['engagements'].apply(lambda x: int(x))
results_table = tz2

v = ['mention', 'url', 'empleo', 'exclamacion', 'pregunta']

for i in range(len(v)):
  tzw = top_tw.groupby(['candidato', v[i]])[["engagements"]].mean()
  tzw['engagements'] = tzw['engagements'].apply(lambda x: int(x))
  results_table = pd.concat([results_table, tzw], ignore_index=False)
  
results_table.reset_index(inplace=True)

lv = ['hashtag', 'mention', 'url', 'empleo', 'exclamacion', 'pregunta']
len_lv = len(lv)
rows = len(results_table['candidato'])
rows_noq = rows - 5
v_groups = rows_noq / len_lv
results_table2 = results_table
results_table2['idx'] = np.arange(rows)
results_table2

def sn(x):
  if x == 0:
    return '' #'no : '
  else:
    return '' #'si : '

def find_type(x):
  if x < 6:
    return sn(results_table2['hashtag'][x]) + lv[0]
  elif x >= 6 and x < 6*2:
    return sn(results_table2['hashtag'][x]) + lv[1]
  elif x >= 6*2 and x < 6*3:
    return sn(results_table2['hashtag'][x]) + lv[2]
  elif x >= 6*3 and x < 6*4:
    return sn(results_table2['hashtag'][x]) + lv[3]
  elif x >= 6*4 and x < 6*5:
    return sn(results_table2['hashtag'][x]) + lv[4]
  else:
    return sn(results_table2['hashtag'][x]) + lv[5]

results_table2['type'] = results_table2['idx'].apply(lambda x: find_type(x))
results_table3 = results_table2
results_table3 = results_table3[['candidato','type','hashtag','engagements']]
results_table3

# Define and plot comparative bar graphs with Seaborn
g = sns.FacetGrid(results_table3[:18], col="type", size=6, aspect=.7, ylim=(0, 3000))
(g.map(sns.barplot, "candidato", "engagements", "hashtag")
.despine(left=True)
.add_legend(title="Con (1) o Sin (0)"))

# Define and plot comparative bar graphs with Seaborn
g2 = sns.FacetGrid(results_table3[18:], col="type", size=6, aspect=.7, ylim=(0, 3000))
(g2.map(sns.barplot, "candidato", "engagements", "hashtag")
.despine(left=True)

optimal_len = eng_vs_long[['candidato','engagements','longitud']]

# Define and plot individual jointplots with Seaborn
sns.jointplot("longitud", "engagements", data=optimal_len, kind="reg")
m1 = optimal_len[(df.candidato == 'Lenin_Moreno')]
sns.jointplot("longitud", "engagements", data=m1, kind="reg", color="g", xlim=(0, 140))
m2 = optimal_len[(df.candidato == 'Guillermo_Lasso')]
sns.jointplot("longitud", "engagements", data=m2, kind="reg", color="b", xlim=(0, 140))
.add_legend(title="Con (1) o Sin (0)"))
m4 = optimal_len[(df.candidato == 'Cynthia_Viteri')]
sns.jointplot("longitud", "engagements", data=m4, kind="reg", color="r", xlim=(0, 140))

# Print candidate stats summary
print "Lenin Moreno"
print m1.describe()
print ""
print "Guillermo Lasso:"
print m2.describe()
print ""
print "Cynthia Viteri:"
print m4.describe()



