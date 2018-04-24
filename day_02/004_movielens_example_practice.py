import pandas as pd
 
encoding = 'latin1'

#아래 3개의 파일을 csv 파일을 통해서 읽으세요. sep="::" 를 사용하여 구분하세요. header=None이며, 
# encoding은 latin1 을 주세요. 

uers_db = pd.read_csv('movielens/users.dat', sep='::', encoding='utf-8') 
ratings_db = pd.read_csv('movielens/ratings.dat', sep='::', encoding='utf-8')
movies_db = pd.read_csv('movielens/movies.dat', setp='::', encoding='utf-8')

# user.dat의 헤더 정보입니다. ['user_id', 'gender','age','occpuation','zip']
# ratings.dat의 헤더 정보입니다.['user_id','movie_id','rating','timestamp']
# movies.dat의 헤더 정보입니다. ['movie_id', 'title','genres']


# users에서 앞에서 5개의 정보를 출력하세요.


