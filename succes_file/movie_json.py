import json #json 형태 파일을 읽어오기 위한 라이브러리
import urllib.request 
import datetime as dt #날짜class
import requests



myToken="" #slack bot token 정보
ch="#test2" #체널을 변경할수도 있어서 변수생성  
url="https://movie.daum.net/api/premovie?page=1&size=100&flag=C" #사이즈를 100으로해 페이지 불러오기
text_data=urllib.request.urlopen(url).read().decode('utf-8') #urllib.request를 이용해 읽어오기
movies=json.loads(text_data)
content=movies["contents"] 
x=dt.datetime.now() #날짜 적용
year=x.year #year 변수생성
month=x.month #month 변수생성
day=x.day #day 변수생성

'''
슬랙 봇 메세지 함수
'''

def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": text}  
    )  
    print(response)


'''
    개봉영화날짜 크롤링 정보가 ex)20220308 형태로 되어있음
'''


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




    

    #print(isinstance(movies["page"], list)) #list형식인지 확인
    #print(content[1]) #list문이 작동하는지 확인
    #post_message(myToken, ch, "작동확인") #def response 작동하는지 확인

   



    '''
    다음영화 크롤링
    '''

for movie in content:
    movie_title=movie["titleKorean"]
    movie_link=movie["id"]    
    open_dates=movie["countryMovieInformation"]["releaseDate"]
   

    if open_dates.startswith(date): #오늘날짜에 맞는 개봉영화만 출력           
    #if dates.startswith("20221020"): #개봉날짜를 임의로 지정해 테스트
        post_message(myToken,ch,f"오늘의 개봉예정영화:{movie_title}") 
        post_message(myToken,ch,f"개봉날짜:{open_dates}")
        post_message(myToken,ch,"바로가기 :{}".format("https://movie.daum.net/moviedb/main?movieId="+str(movie_link)))       
        post_message(myToken,ch,"ㅡ"*30) #next_movie랑 구분짓기위함
                

   

# '''
#     크롤링 정보가 잘 출력되는지 확인코드
# '''
#     # print(f"제목 : {title}")
#     # print(f"개봉날짜:{dates}")
#     # print("바로가기 :{}".format("https://movie.daum.net/moviedb/main?movieId="+str(link)))
#     # print("ㅡ"*30) 
