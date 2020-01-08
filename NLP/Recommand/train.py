import pandas as pd

movies = pd.read_csv("data/movies.csv")
ratings = pd.read_csv("data/ratings.csv")
data = pd.merge(movies, ratings, on="movieId")
pd.set_option('max_columns', 10)
pd.set_option('max_rows', 100)
# print(data.head())

'''
Merge the data with movies.csv and ratings.csv
'''
data[['userId', 'rating', 'movieId', 'title']].sort_values('userId').to_csv('data/data.csv', index=False)

'''
Read the data
'''

## def the dict,存放每位用户评论的电影和评分
dict_data = {}

# with open('data/data.csv', 'r', encoding='utf-8') as f:
file = open('data/data.csv', 'r', encoding='utf-8')

for line in file.readlines():
    # for line in file.readlines()[1:100]:
    #     print('line={}'.format(line))
    line = line.strip().split(',')
    if not line[0] in dict_data.keys():
        dict_data[line[0]] = {line[3]: line[1]}
    else:
        dict_data[line[0]][line[3]] = line[1]
# print(dict_data.keys()
# print(dict_data.get("2"))
# print(dict_data)
# print(len(dict_data))
# print(dict_data.items())



print('pow test: 100 pow 2 = {}'.format(pow(100, 2)))

from math import *


def get_distance(user1, user2):
    user1_data = dict_data[user1]
    user2_data = dict_data[user2]
    # print('user2_data={}'.format(user2_data))
    distance = 0
    for key in user1_data.keys():
        # print('user1_data1.key={}'.format(key))
        if key in user2_data.keys():
            # print('user2_data1.key={}'.format(key))
            distance = distance + pow(float(user1_data[key]) - float(user2_data[key]), 2)
    return 1 / (1 + sqrt(distance))


'''
计算某个用户与其他用户的相似度
'''


def top10_similar(userID):
    res = []
    for userid in dict_data.keys():
        if not userid == userID:
            res.append((userid, get_distance(userid, userID)))
    res.sort(key=lambda val: val[1])
    # print('res={}'.format(res))
    return res[:4]



RES = top10_similar('2')
# print('RES={}'.format(RES))
