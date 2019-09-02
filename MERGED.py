import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
plt.style.use('ggplot')

data1 = pd.read_csv('D:\\New2\\QikProp_PROJECT.CSV', header = 0, sep=';')
data1.columns = data1.columns.str.replace('#','_')
data1 = data1[['Title', 'QPlogHERG', 'CNS', 'PercentHumanOralAbsorption', '_rtvFG', 'docking score', 'HumanOralAbsorption', '_stars', 'RuleOfFive', 'RuleOfThree', 'FOSA', 'FISA']]
data2 = pd.read_csv('D:\\New2\\XP_resist_residue.csv', header = 0)[['Title', 'docking score']]


data3 = data2.merge(data1, left_on = 'Title', right_on = 'Title')
data3.rename(columns = {'docking score_x':'resist_score','docking score_y':'score'}, inplace = True)
data3['sum'] = np.sum(data3[['resist_score', 'score']], axis = 1)
data3.sort_values(by = ['sum'], inplace = True)
top10 = data3.head(10).to_excel('D:\\New2\\top10.xlsx')

# data3[['Title','sum','HumanOralAbsorption']].head(20).plot.scatter('sum','HumanOralAbsorption')

rate = data3[:]
rate['6BKL_rate'] = rate['score'] / -4.412
rate['2LY0_rate'] = rate['resist_score'] / -1.527
def Plot_violin(data, columns):
    n_axes = len(columns)
    fig, axes = plt.subplots(nrows = n_axes)
    axes = [[axes[x].violinplot(data[column], showmedians = True, vert = False),  axes[x].set_xlabel(column, color = 'b'), axes[x].set_yticks([])] for x, column in enumerate(columns)]
    return axes

rate.dropna(inplace = True)
Plot_violin(rate, ['6BKL_rate', '2LY0_rate', 'CNS', 'QPlogHERG', 'PercentHumanOralAbsorption'])
plt.tight_layout()
plt.show()

plt.boxplot(rate['score_rate'])

rate.loc[rate.isnull().any(axis = 1)]


data = rate
columns = ['6BKL_rate', '2LY0_rate', 'CNS', 'QPlogHERG', 'PercentHumanOralAbsorption']
n_axes = len(columns)
fig, axes = plt.subplots(nrows = n_axes)
[[axes[x].violinplot(data[column], showmedians = True, vert = False),  axes[x].set_xlabel(column, color = 'b'), axes[x].set_yticks([])] for x, column in enumerate(columns)]

axes[2].set_xticks(np.arange(-2,3,1))
[axes[2].get_xticklabels()[x].set_color('y') for x in range(3,5)]
[axes[3].get_xticklabels()[x].set_color('y') for x in [1]]
axes[4].set_xticks(np.arange(0,125,25))
[axes[4].get_xticklabels()[x].set_color('y') for x in range(0,2)]
plt.tight_layout()
plt.show()





# FOSA FISA
new = data3.head(10).reset_index()[['FOSA', 'FISA']]
new['FISA/FOSA'] = new['FISA']/new['FOSA']
new.to_excel('D:/New2/FIFO.xlsx')
