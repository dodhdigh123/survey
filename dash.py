from IPython.core.display import display, HTML
display(HTML("<style>.container { width:90% !important; }</style>"))
display(HTML("<style>.input_area pre {font-family: Consolas; font-size: 8pt; line-height: 120%;}</style>"))
display(HTML("<style>.output_area pre {font-family: Consolas; font-size: 11pt; line-height: 120%;}</style>"))
import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
from datetime import datetime as dt 
from matplotlib import colors as mcolors
# %matplotlib inline
import seaborn as sns

from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = 'all'

from matplotlib import font_manager, rc
plt.rcParams['font.family'] = 'NanumBarunGothic'

import matplotlib.font_manager as fm
fm._rebuild()
# font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
# rc('font', family=font_name)


import matplotlib as mpl
mpl.rcParams['axes.unicode_minus']=False

import warnings
warnings.filterwarnings('ignore')
plt.style.use('fivethirtyeight')

# 파일 경로 수정
store_all = pd.read_csv("./data1.csv", encoding='cp949', thousands=',') 

data2 = pd.read_csv("./data2.csv", encoding='cp949', thousands=',') 
data3 = pd.read_csv("./database.csv", encoding='utf-8', thousands=',') 

fig, axes = plt.subplots(2, 3, figsize=(20, 10))


colors = ["blue", "red"]
sns.set_palette(sns.color_palette(colors))

sns.barplot(data=store_all, x = "시군구", y = '유동인구',hue='성별',ax=axes[0, 0])
sns.barplot(data=data2, x = "장소명", y = '카드이용금액',hue='기준분기',ax=axes[1, 1])

congestion_counts = data3['congestion'].value_counts()

# 파이 차트 그리기
colors = ['#ff9999', '#ffc000', '#8fd9b6', '#d395d0']
axes[0, 1].pie(congestion_counts, labels=congestion_counts.index, autopct='%1.1f%%', startangle=90, colors=colors)
axes[0, 1].set_title('Congestion Distribution')

fig.savefig("static/img/dashboard_image.jpeg")
# import os
# print(os.getcwd())
