import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
data1 = pd.read_csv('D:\\New2\\QikProp_PROJECT.CSV', header = 0, sep=';')
data1.columns = data1.columns.str.replace('#','_')
data1 = data1[['Title', 'QPlogHERG', 'CNS', 'PercentHumanOralAbsorption', '_rtvFG', 'docking score', 'HumanOralAbsorption','_stars', 'RuleOfFive', 'RuleOfThree']]
data2 = pd.read_csv('D:\\New2\\XP_resist_residue.csv', header = 0)[['Title', 'docking score']]


data3 = data2.merge(data1, left_on = 'Title', right_on = 'Title')
data3.rename(columns = {'docking score_x':'resist_score','docking score_y':'score'}, inplace = True)
data3['sum'] = np.sum(data3[['resist_score', 'score']], axis = 1)
data3.sort_values(by = ['sum'], inplace = True)


rate = data3[:]
rate['6BKL_rate'] = rate['score'] / -4.412
rate['2LY0_rate'] = rate['resist_score'] / -1.527
rate.dropna(inplace = True)


def Plot_violin(data, columns):
    n_axes = len(columns)
    fig, axes = plt.subplots(nrows = n_axes)
    return [[axes[x].violinplot(data[column], showmedians = True, vert = False),  axes[x].set_xlabel(column, color = 'b'), axes[x].set_yticks([])]
    for x, column in enumerate(columns)]


Plot_violin(rate, ['6BKL_rate', '2LY0_rate'])
plt.tight_layout() 
plt.show()



plt.style.use('seaborn')


# fig, (axe1, axe2, axe3, axe4) = plt.subplots(1, 4, gridspec_kw = {"width_ratios": [np.max(dropnan['_stars'])-np.min(dropnan['_stars']), np.max(dropnan['_rtvFG'])-np.min(dropnan['_rtvFG']), np.max(dropnan['RuleOfThree']) - np.mean(dropnan['RuleOfThree']), np.max(dropnan['RuleOfFive']) - np.min(dropnan['RuleOfFive'])]})

# N1, bins1, patches1 = axe1.hist(dropnan['_stars'])
# bins1 = range(8)
# [patches1[i].set_fc('r') for i in bins1 if i > 5]
# axe1.set_title('stars')
# axe1.set_xticks(range(8))
# plt.xticks(bins1)

# N2, bins2, patches2 = axe2.hist(dropnan['_rtvFG'], bins = 5)
# bins2 = range(7)
# [patches2[i].set_fc('r') for i in bins2 if i > 2]
# axe2.set_title('rtvFG')
# axe2.set_xticks(range(7))
# plt.xticks(bins2)

# N3, bins3, patches3 = axe3.hist(dropnan['RuleOfFive'])
# bins3 = range(3)
# [patches3[i].set_fc('r') for i in bins3 if i > 4]
# axe3.set_title('RuleOfFive')
# # axe3.set_xticks(range(3))
# plt.xticks(bins3)

# N4, bins4, patches4 = axe4.hist(dropnan['RuleOfThree'])
# bins = range(3)
# [patches4[i].set_fc('r') for i in bins4 if i > 2]
# axe4.set_title('RuleOfThree')
# # axe4.set_xticks(range(3))

# [ok[column].value_counts().plot(kind = 'bar', ax = axes[x], title = column) for x, column in enumerate(ok.columns)]

# [print(column, axe) for column, axe in zip(ok.columns,(axe1, axe2, axe3, axe4))]

# ok['_stars'].value_counts().plot(kind = 'bar', ax = axes[1])
fig, axes = plt.subplots(ncols = 4)
rate = rate[['_stars', 'RuleOfFive', 'RuleOfThree', '_rtvFG']]
[rate[column].value_counts().reset_index().sort_values(by = 'index').set_index('index').reindex(range(int(max(rate[column])+1))).plot(kind = 'bar', ax = axes[x], legend = 0, fontsize = 13) for x, column in enumerate(rate.columns)]
[axes[x].set_xlabel('') for x, column in enumerate(rate.columns)]
[axes[x].set_title(column, color = 'b', fontsize = 15) for x, column in enumerate(rate.columns)]
axes[3].get_children()[3].set_color('y')
axes[3].get_children()[4].set_color('y')
plt.tight_layout()
plt.show()

