# 导入库
# 数据分析和探索
import pandas as pd
import numpy as np
import random as rnd

# 可视化
import seaborn as sb
import matplotlib.pyplot as plt

# 机器学习模型
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC, LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import Perceptron
from sklearn.linear_model import SGDClassifier
from sklearn.tree import DecisionTreeClassifier

train_df = pd.read_csv('../data/train.csv')
test_df = pd.read_csv('../data/test.csv')
combine = [train_df, test_df]
pd.set_option('display.max_columns', None)
sb.set_style("whitegrid")
#print(test_df.head())
# 查看各特征非空样本量及字段类型
#train_df.info()
#print("_"*40)
test_df.info()


# 查看数值类（int，float）特征的数据分布情况
#print(train_df.describe())

# 查看非数值类型特征值数据分布情况

#print(train_df.describe(include=['O']))

# 几个枚举型特征与Survived的关联性（直接group汇总求均值）

    #1.社会地位与生存率的关联
x1 = train_df[["Pclass","Survived"]].groupby(["Pclass"]).mean()
x2 = train_df[["Pclass","Survived"]].groupby(["Pclass"],as_index=True).mean().sort_values(by = "Pclass",ascending= False)

#print(x2)
    #2.男性女性与生存率的关联
Sex = train_df[["Sex","Survived"]].groupby(["Sex"]).mean()
#print(x3)
    #3.SibSp  同行的兄弟姐妹或配偶总数
SibSp = train_df[["SibSp","Survived"]].groupby(["SibSp"]).mean()

    #4.Parch 同行的父母或孩子总数
Parch = train_df[["Parch","Survived"]].groupby(["Parch"]).mean().sort_values(by = "Survived",ascending = False)

# print(Parch)
    #5.查看年龄的关系
Age = train_df[["Age","Survived"]].groupby(["Age"]).mean().sort_values(by = "Age",ascending= False)

#print(Age)

    # 对年龄这类分布较长的数据采用直方图分别查看生存与否的分布
sur = sb.FacetGrid(train_df,col = "Survived", row= "Sex")
sur.map(plt.hist,"Age",bins = 20)
# sur.map(plt.hist,"Fare",bins = 20)
# plt.show()
    # Embarked 登船港口  Pclass 船票级别
# em = train_df[["Embarked"]].groupby(["Embarked"])
em = sb.FacetGrid(train_df,col= "Embarked")
# em.map(plt.hist,"Survived",bins =20)
#   pointplot 不知道是啥
# em.map(sb.pointplot,"Sex","Pclass","Survived",palette = "deep")
# plt.show()
# em.map(sb.pointplot,"Pclass","Sex","Survived",palette = "deep")
# plt.show()
em.map(sb.pointplot,"Pclass","Survived","Sex",palette = "deep")
# plt.show()

    # 观察sex,fare,survived,Embarked之间的关联
grid = sb.FacetGrid(train_df,row="Embarked",col="Survived")
grid.map(sb.barplot,"Sex","Fare")
plt.show()