import pandas as pd 
import matplotlib.pyplot as plt  
from adjustText import adjust_text 
import seaborn as sns 

data1 = pd.read_csv('D:\\New2\\1_residue_dist.csv', header = 0)
[data1.drop([ind], inplace = True) for ind in data1[data1.pep_only.str.contains('HOH')].index]
data2_res = pd.read_csv('D:\\New2\\2_residue_resist_dist.csv', header = 0)

data1.to_excel('D:\\New2\\1_residue_dist.xlsx')
data2_res.to_excel('D:\\New2\\2_residue_dist.xlsx')

def Plot(datas, title):
	fig, axes = plt.subplots(ncols = len(datas))
	for n, data in enumerate(datas):
		box_dict = axes[n].boxplot(data['dist'])
		flier = box_dict['fliers']
		position = [(flier[i].get_xdata(),flier[i].get_ydata()) for i in range(len(flier))]
		post = [(position[0][0][i], position[0][1][i]) for i in range(len(position[0][0]))]
		pep_name = [data[data['dist'] == y]['pep_only'].values[0] for x, y in post]
		[axes[n].text(x + 0.02, y + 0.02, s = data[data['dist'] == y]['pep_only'].values[0], color = 'r') for x,y in post]
		axes[n].set_xticks([],[])
		axes[n].set_title(title[n], color = 'b')
		axes[n].set_ylabel('Khoảng cách trung bình (Angstrom)')
		texts = [axes[n].annotate(data.iloc[i]['pep_only'], color = 'r', xy = (1, data.iloc[i]['dist']), xytext = (1.12, data.iloc[i]['dist'] + 0.05), arrowprops=dict(arrowstyle="fancy", color = 'r', connectionstyle="angle3,angleA=0,angleB=-90"))  for i in range(4) if all(~data.iloc[i].isin(pep_name))]
		adjust_text(texts)

def Boxplot(datas, title):
	fig, axes = plt.subplots(ncols = len(datas))
	[axes[i].boxplot(data['dist']) for i, data in enumerate(datas)]
	[(axes[i].set_xticks([],[]), axes[i].set_title(title[i], color = 'b'), axes[i].set_ylabel('Khoảng cách (Angstrom)')) for i, data in enumerate(datas)]
	plt.subplots_adjust(wspace = 1000)


def Plotsame(datas, title):
	fig, axes = plt.subplots()
	box_dict = axes.boxplot([datas[0]['dist'], datas[1]['dist']])
	axes.set_xticklabels(title, color = 'b', fontsize = 13)
	axes.set_ylabel('Khoảng cách trung bình (angstrom)', fontsize = 13)

def Plotswarm(datas, title):
	data = pd.concat([datas[0]['dist'], datas[1]['dist']], axis = 1, keys = title).stack(0).reset_index(level = 1)
	data.columns = ['index', 'value']
	axes = sns.swarmplot(x = 'index', y = 'value', data = data, order = title)
	# text1 = [axes.annotate(datas[n].iloc[i]['pep_only'], color = 'r', xy = (n, datas[n].iloc[i]['value']), xytext = (n + 0.05, datas[n].iloc[i]['value'] - 0.05), fontsize = 11) for n in range(1) for i in range(10) if datas[n].iloc[i]['value'] < -3]
	# text2 = [axes.annotate(datas[n].iloc[i]['pep_only'], color = 'r', xy = (n, datas[n].iloc[i]['value']), xytext = (n + 0.1, datas[n].iloc[i]['value'] - 0.05), arrowprops=dict(arrowstyle="fancy", color = 'grey', alpha = 0.3, connectionstyle="angle3,angleA=0,angleB=-90"), fontsize = 11) for n in range(1,2) for i in range(10) if datas[n].iloc[i]['value'] < -3]
	# text3 = [axes.annotate(datas[n].iloc[i]['pep_only'], color = 'g', xy = (n, datas[n].iloc[i]['value']), xytext = (n + 0.1, datas[n].iloc[i]['value'] - 0.05), arrowprops=dict(arrowstyle="fancy", color = 'grey', alpha = 0.3, connectionstyle="angle3,angleA=0,angleB=-90"), fontsize = 11) for n in range(1,2) for i in range(len(datas[1])) if datas[n].iloc[i]['value'] > 0]
	axes.set_xticklabels(title, color = 'b', fontsize = 13)
	axes.set_ylabel('Khoảng cách trung bình (angstrom)', fontsize = 13)
	axes.set_xlabel('')
	# adjust_text(text2)
	# adjust_text(text3)

# Plot(datas = [data1, data2_res], title = ['(1)','(2)'])
# Boxplot(datas = [data1, data2_res], title = ['6BKL','2LY0'])
Plotswarm(datas = [data1, data2_res], title = ['6BKL','2LY0'])
plt.tight_layout()
plt.show()


data = pd.read_csv(r'D:\New2\1_HTVS\1st _ HTVS Joined.csv')
data.to_excel(r'D:\New2\1_HTVS\1st _ HTVS Joined.xlsx')