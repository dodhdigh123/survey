import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# 폰트 설정
plt.rcParams['font.family'] = 'NanumBarunGothic'
import matplotlib.font_manager as fm
fm._rebuild()

# 경고 메시지 무시
import warnings
warnings.filterwarnings('ignore')

def draw_barplot(x, y, hue, data, ax):
    colors = sns.color_palette('pastel')[0:2]
    sns.set_palette(sns.color_palette(colors))
    sns.barplot(x=x, y=y, hue=hue, data=data, ax=ax)
    return None

def draw_pie(data, column, ax, title='Distribution'):
    column_counts = data[column].value_counts()
    colors = sns.color_palette('pastel')[0:5]
    ax.pie(column_counts, labels=column_counts.index, autopct='%1.1f%%', startangle=90, colors=colors)
    ax.set_title(title)
    return None
