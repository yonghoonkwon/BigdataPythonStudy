import pandas as pd
 
encoding = 'latin1'

#�Ʒ� 3���� ������ csv ������ ���ؼ� ��������. sep="::" �� ����Ͽ� �����ϼ���. header=None�̸�, 
# encoding�� latin1 �� �ּ���. 

uers_db = pd.read_csv('movielens/users.dat', sep='::', encoding='utf-8') 
ratings_db = pd.read_csv('movielens/ratings.dat', sep='::', encoding='utf-8')
movies_db = pd.read_csv('movielens/movies.dat', setp='::', encoding='utf-8')

# user.dat�� ��� �����Դϴ�. ['user_id', 'gender','age','occpuation','zip']
# ratings.dat�� ��� �����Դϴ�.['user_id','movie_id','rating','timestamp']
# movies.dat�� ��� �����Դϴ�. ['movie_id', 'title','genres']


# users���� �տ��� 5���� ������ ����ϼ���.


