# Function(함수) : input[int, str, [],None] -> output
# 마술 상자 : [100 -> 500 , 200 -> 1000, 300 -> ?]
# f(x): len(x), str(x), int(x), print(x),input(x)

def koreaIt():
    return "코리아아이티"
a = koreaIt()
print(a)

def koreaIt(x):
    return x + "코리아아이티"
a = koreaIt("인천점")
print(a)



def add(x,y):
    return x+y


# 어떠한 단어를 넣었을때 그 단어가 5글자 이상이면
# 글자가 길어요! , 아니면 글자가 짧아요!


def word(x):
    if len(x) >= 5:
        return "글자가 길어요!"
    else:
        return "글자가 짧아요!"


# 함수 : input -> [로직] -> output

# abc(5,'★')

def abc(x,y):
    return [y for x in range(x)]

# 🥚🐣🐥🐓🍗
# 🥚 -> 🐣
# 🐣 -> 🐥
# 🐥 -> 🐓
# 🐓 -> 🍗


def emoji(x):
    if x == '🥚':
        return '🐣'
    elif x == '🐣':
        return '🐥'
    elif x == '🐥':
        return '🐓'
    elif x == '🐓':
        return '🍗'
    else:
        return "error"

def emoji(x):
    emoji = {
        '🥚' : '🐣',
        '🐣' : '🐥',
        '🐥' : '🐓',
        '🐓' : '🍗',
    }
    return emoji[x]

print(emoji('🍗'))


