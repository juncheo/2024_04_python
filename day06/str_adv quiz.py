# 1. 뉴스 기사를 스크랩 해오고, 유저가 입력한 단어를 뉴스기사에서 그 해당 단어를 모두 대문자로 바꿔서
# 다시 보여주기

# news = """Dubai Airport is a busy place. It is one of the biggest airports in the world.
#
# Last week, heavy rain hits the United Arab Emirates and Oman. Rain is not usual in these countries at all. In one day, there is more rain than in the whole year. The rain damages things. One person is dead. The streets in Dubai look like rivers. The airport cancels flights. Many people must stay at the airport. They cannot leave.
#
# Experts are not sure what causes the rain. But such things may happen more often in the future. Even in places with very little rain.
#
# Difficult words: damage (to hurt), cause (to make something happen), future (time ahead).
#
# You can watch the original video in the Level 3 section."""
#
# word = input("단어 입력: ")
# newNews = news.replace(word,word.upper())
# print(newNews)




# 2. 영어 기사를 스크랩 해오고,
# 단어 사이에 🍎 넣고 출력하기

news = """Dubai Airport is a busy place. It is one of the biggest airports in the world.

Last week, heavy rain hits the United Arab Emirates and Oman. Rain is not usual in these countries at all. In one day, there is more rain than in the whole year. The rain damages things. One person is dead. The streets in Dubai look like rivers. The airport cancels flights. Many people must stay at the airport. They cannot leave.

Experts are not sure what causes the rain. But such things may happen more often in the future. Even in places with very little rain.

Difficult words: damage (to hurt), cause (to make something happen), future (time ahead).

You can watch the original video in the Level 3 section."""


words = news.split(" ")
news1 = "🍎".join(words)
print(news1)
