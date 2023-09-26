from flask import Flask, render_template, request, redirect, url_for, Response
import sys
application = Flask(__name__)
import database
from dashboard import draw_barplot
from dashboard import draw_pie
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import time



@application.route("/")
def main():
    return render_template("main.html")


@application.route("/haeundae")
def haeundae():
    return render_template("haeundae.html")



@application.route("/gwanganri")
def gwanganri():
    return render_template("gwanganri.html")

@application.route("/Dashboard")
def Dashboard():
    congestion = request.args.get("congestion")
    gender = request.args.get("gender")
    question = request.args.get("question")
    add = request.args.get("add")
    database.save(congestion,gender,question,add)
    
    # 데이터 불러오기
    data1 = pd.read_csv("./data1.csv", encoding='cp949', thousands=',') 
    data2 = pd.read_csv("./data2.csv", encoding='cp949', thousands=',') 
    data3 = pd.read_csv("./database.csv", encoding='utf-8', thousands=',') 

    # 그래프 그리기
    fig, axes = plt.subplots(2, 3, figsize=(20, 10))

    draw_barplot(x="시군구", y='유동인구', hue='성별', data=data1, ax=axes[0, 0])
    draw_barplot(x="장소명", y='카드이용금액', hue='기준분기', data=data2, ax=axes[1, 1])
    draw_pie(data=data3, column='congestion', ax=axes[0, 1], title='Congestion Distribution')

    # 이미지 저장
    fig.savefig("static/img/duu_image.jpeg")
    
    return render_template("Dashboard.html")


@application.route("/Dashboardshow")
def Dashboardshow():
    return render_template("Dashboardshow.html", time=time, int=int)
    
if __name__ == "__main__":
    application.run(host='0.0.0.0')