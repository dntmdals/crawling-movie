from tkinter import Menu
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base #상속class 를 알아서 매핑
from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Integer, String



engine = create_engine(
"mysql:///movies?charset=utf8mb4"
    ,echo=True, future=True
    ) #echo=True 문으로 결과값 출력
Base = declarative_base() #상속class 를 알아서 매핑

class Movie(Base):
    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True) 
    title = Column(String(255))
    dates = Column(String(255))
    link = Column(String(255)) #link글자수 제한 100자

Movie.__table__.create(bind=engine, checkfirst=True)

Session = sessionmaker(bind=engine) #session 생성
session = Session()


'''
예시로 아바타,20221022,naver.com을 table에 저장해
데이터베이스와 연결과 동작을 테스트 한다.
'''
# movie_list=Movie(title="아바타",  dates="20221022", link="naver.com")

# session.add(movie_list)
# session.commit()

# result = session.query(Movie).all()
# for row in result:
#   print(row.date,row.rank,row.movieNm,row.movieCd,row.salesAmt,row.audiCnt)

# movie_list=Movie(title="아바타",dates="20221021",link="naver.com")

# query = session.query(Movie).filter(Movie.dates == 20221021)
# query_data =query.all() #type list
# print(query)
# # print(query_data[0].title)