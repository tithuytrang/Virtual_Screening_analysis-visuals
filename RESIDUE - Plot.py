import pandas as pd 
import matplotlib.pyplot as plt  
from adjustText import adjust_text 
import seaborn as sns

data1 = pd.read_csv('D:\\New2\\1_residue.csv', header = 0)
[data1.drop([ind], inplace = True) for ind in data1[data1.pep_only.str.contains('HOH')].index]
data2_res = pd.read_csv('D:\\New2\\2_residue_resist.csv', header = 0)

data1.to_excel('D:\\New2\\1_residue.xlsx')
data2_res.to_excel('D:\\New2\\2_residue.xlsx')

def Plot(datas, title):
	fig, axes = plt.subplots(ncols = len(datas))
	for n, data in enumerate(datas):
		box_dict = axes[n].boxplot(data['value'])
		flier = box_dict['fliers']
		position = [(flier[i].get_xdata(),flier[i].get_ydata()) for i in range(len(flier))]
		post = [(position[0][0][i], position[0][1][i]) for i in range(len(position[0][0]))]
		pep_name = [data[data['value'] == y]['pep_only'].values[0] for x, y in post]
		[axes[n].text(x + 0.02, y + 0.02, s = data[data['value'] == y]['pep_only'].values[0], color = 'r') for x,y in post]
		axes[n].set_xticks([],[])
		axes[n].set_title(title[n], color = 'b')
		axes[n].set_ylabel('Năng lượng tự do trung bình (kcal/mol)')
		texts = [axes[n].annotate(data.iloc[i]['pep_only'], color = 'r', xy = (1, data.iloc[i]['value']), xytext = (1, data.iloc[i]['value'] + 0.05), arrowprops=dict(arrowstyle="fancy", color = 'r', connectionstyle="angle3,angleA=0,angleB=-90"))  for i in range(5) if all(~data.iloc[i].isin(pep_name))]
		adjust_text(texts)


def Plotsame(datas, title):
	fig, axes = plt.subplots()
	# axes.violinplot([datas[0]['value'], datas[1]['value']])
	box_dict = axes.boxplot([datas[0]['value'], datas[1]['value']])
	flier = box_dict['fliers']
	position = [(flier[i].get_xdata(),flier[i].get_ydata()) for i in range(len(flier))]
	post = [(position[0][0][i], position[0][1][i]) for i in range(len(position[0][0]))]
	pep_name = [datas[int(x)-1][datas[int(x)-1]['value'] == y]['pep_only'].values[0] for x, y in post]
	[axes.text(x + 0.02, y + 0.02, s = datas[int(x)-1][datas[int(x)-1]['value'] == y]['pep_only'].values[0], color = 'r', fontsize = 11) for x,y in post]
	axes.set_xticklabels(title, color = 'b', fontsize = 13)
	axes.set_ylabel('Năng lượng tự do trung bình (kcal/mol)', fontsize = 13)
	texts = [axes.annotate(datas[n].iloc[i]['pep_only'], color = 'r', xy = (n+1, datas[n].iloc[i]['value']), xytext = (n+1, datas[n].iloc[i]['value'] + 0.05), arrowprops=dict(arrowstyle="fancy", color = 'r', connectionstyle="angle3,angleA=0,angleB=-90"), fontsize = 11) for n in range(2) for i in range(6) if (n+1, datas[n].iloc[i]['value']) not in post]
	adjust_text(texts)


def Plotswarm(datas, title):
	data = pd.concat([datas[0]['value'], datas[1]['value']], axis = 1, keys = title).stack(0).reset_index(level = 1)
	data.columns = ['index', 'value']
	axes = sns.swarmplot(x = 'index', y = 'value', data = data, order = title)
	text1 = [axes.annotate(datas[n].iloc[i]['pep_only'], color = 'r', xy = (n, datas[n].iloc[i]['value']), xytext = (n + 0.05, datas[n].iloc[i]['value'] - 0.05), fontsize = 11) for n in range(1) for i in range(10) if datas[n].iloc[i]['value'] < -3]
	text2 = [axes.annotate(datas[n].iloc[i]['pep_only'], color = 'r', xy = (n, datas[n].iloc[i]['value']), xytext = (n + 0.1, datas[n].iloc[i]['value'] - 0.05), arrowprops=dict(arrowstyle="fancy", color = 'grey', alpha = 0.3, connectionstyle="angle3,angleA=0,angleB=-90"), fontsize = 11) for n in range(1,2) for i in range(10) if datas[n].iloc[i]['value'] < -3]
	# text3 = [axes.annotate(datas[n].iloc[i]['pep_only'], color = 'g', xy = (n, datas[n].iloc[i]['value']), xytext = (n + 0.1, datas[n].iloc[i]['value'] - 0.05), arrowprops=dict(arrowstyle="fancy", color = 'grey', alpha = 0.3, connectionstyle="angle3,angleA=0,angleB=-90"), fontsize = 11) for n in range(1,2) for i in range(len(datas[1])) if datas[n].iloc[i]['value'] > 0]
	axes.set_xticklabels(title, color = 'b', fontsize = 13)
	axes.set_ylabel('Năng lượng tự do trung bình (kcal/mol)', fontsize = 13)
	axes.set_xlabel('')
	adjust_text(text2)
	# adjust_text(text3)

# Plot(datas = [data1, data2_res], title = ['6BKL','2LY0'])
Plotswarm(datas = [data1, data2_res], title = ['6BKL','2LY0'])
plt.tight_layout()
plt.show()
