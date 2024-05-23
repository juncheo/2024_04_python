import os
import datetime
from day15.review import yeerToZodiac
# print(os.getlogin())

# # 바탕화면 경로따기
# desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']),'Desktop')
# # folder_name = "운동가야지"
# #
# # folder_path = os.path.join(desktop_path,folder_name)
# # os.mkdir(folder_path)
# # 바탕화면경로와 폴더이름 합치기
# folder_path = os.path.join(desktop_path,'과장님부당업무지시폴더')
#
# os.mkdir(folder_path)
# # 오늘 날짜 가져오기
# start_date = datetime.date.today()
#
#
# for x in range(365):
#     date_folder = start_date + datetime.timedelta(days=x)
#     path = os.path.join(folder_path, date_folder.strftime("%Y-%m-%d"))
#     os.mkdir(path)

# 폴더 : 용띠의해_5월_23일_목요일


desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']),'Desktop')

folder_path = os.path.join(desktop_path,'부장님')

os.mkdir(path)

start_date = datetime.date.today()

for x in range(365):
    date_folder = start_date + datetime.timedelta(days=x)
    year_zodiac = yearToZodiac(int(date_folder.strftime("%Y")))
    folder_name = f"{year_zodiac}띠의해_{date_folder.strftime('%m_%d_%A')}"
    path = os.path.join(folder_path,folder_name)
    os.mkdir(path)












