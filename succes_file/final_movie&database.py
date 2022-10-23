import json #json 형태 파일을 읽어오기 위한 라이브러리
import urllib.request 
import datetime as dt #날짜class
import requests
from tkinter import Menu
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base #상속class 를 알아서 매핑
from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Integer, String
import pymysql
#engine 생성
engine = create_engine(
"mysql:///movies?charset=utf8mb4"
    ,echo=True, future=True
    ) #echo=True 문으로 결과값 출력 , 스키마 만든후에 해야함
Base = declarative_base() #상속class 를 알아서 매핑

class Movie(Base):
    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True) 
    title = Column(String(255))
    dates = Column(String(255))
    link = Column(String(255))

Movie.__table__.create(bind=engine, checkfirst=True)

Session = sessionmaker(bind=engine) #session 생성
session = Session()

x=dt.datetime.now() #날짜 적용
year=x.year #year 변수생성
month=x.month #month 변수생성
day=x.day #day 변수생성

url="https://movie.daum.net/api/premovie?page=1&size=100&flag=C" #사이즈를 100으로해 페이지 불러오기
text_data=urllib.request.urlopen(url).read().decode('utf-8') #urllib.request를 이용해 읽어오기
movies=json.loads(text_data)
content=movies["contents"] 


if month<10: #month가 한자리일 경우(앞에0을 붙여서 출력)
    month=str(x.month)
    #date=str(year)+"0"+month
    if day<10: #day가 한자리일 경우(앞에0을 붙여서 출력)
        date=str(year)+"0"+month+"0"+str(day)
    else: #day가 두자리일 경우 그냥 출력
        date=str(year)+"0"+month+str(day)

else:#month가 한자리일 경우
    month=str(x.month)
    if day<10: #day가 한자리일 경우(앞에0을 붙여서 출력)
        date=str(year)+month+"0"+str(day)
    else: #day가 두자리일 경우 그냥 출력
        date=str(year)+month+str(day)


for movie in content:
    movie_name=movie["titleKorean"]
    movie_link_id=movie["id"]    
    open_dates=movie["countryMovieInformation"]["releaseDate"]
    movie_link="https://movie.daum.net/moviedb/main?movieId="+str(movie_link_id)
    
    if open_dates.startswith(date):
        
        movie_list=Movie(title=movie_name,  dates=open_dates, link=movie_link)
        session.add(movie_list)
        session.commit()
