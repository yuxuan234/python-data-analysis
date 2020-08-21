# 题目1答案：分数等级划分
while True:
    score = input('input score:\n')
    if score == 'stop':
        break

    score = int(score)
    if score >= 90:
        grade = 'A'
    elif score >= 60:
        grade = 'B'
    else:
        grade = 'C'

    print('{score} belongs to {grade}'.format(score=score, grade=grade))
while True:
    score = input('input score:\n')
    if score == 'stop':
        break

    score = int(score)
    if score >= 90:
        grade = 'A'
    elif score >= 60:
        grade = 'B'


# 方法2
while True:
    score = input('input score:\n')
    if score == 'stop':
        break

    score = int(score)
    if score >= 90:
        grade = 'A'

    if score >= 60 and score < 90:
        grade = 'B'

    if score < 60:
        grade = 'C'

    print('{score} belongs to {grade}'.format(score=score, grade=grade))


# 题目2答案：分数求和
up = 2
down = 1
sum = 0
for i in range(20):
    sum += up / down
    tmp = up
    up = up + down
    down = tmp

print(sum)


# 题目3答案：猴子吃桃
total = 1
for day in range(9, 0, -1):
    total = (total + 1) * 2

print(total)


# 方法2
current = 1
for day in range(9, 0, -1):
    yestoday = (current + 1) * 2
    current = yestoday

print(yestoday)


# 题目4：人狗大战
class People():
    agressivity = 10
    life_value = 100

    def __init__(self, name):
        self.name = name

    def attack(self, dog):
        dog.life_value -= 10

    def __str__(self):
        return '人%s剩余生命值:%s，状态值%s' % (
            self.name, self.life_value, self.agressivity)


class Dogs():
    agressivity = 15
    life_value = 80

    def __init__(self, name):
        self.name = name

    def attack(self, people):
        people.life_value -= 10

    def __str__(self):
        return '狗%s剩余生命值:%s，状态值%s' % (
            self.name, self.life_value, self.agressivity)


p1 = People('Tom')
p2 = People('Jack')
d1 = Dogs('niker')
d2 = Dogs('geeker')
d3 = Dogs('chaox')

print(p1)
print(p2)

p1.attack(d1)

print(d1)


# 题目5：弹小球
# 初始高度
height = 100
# 第一次弹起前的距离，初始化
highs = height
# 第2次能弹起来的高度
height = height / 2

for i in range(2, 11):
    # 第2次弹起来的距离，是弹起高度的来回
    highs += height * 2
    # 准备下一次的高度
    height /= 2

print(height, highs)

# 注意是从第2次弹起来开始计算，因为第一次弹起不具备循环
