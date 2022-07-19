players = ['charles', 'matina', 'michael', 'florence', 'eli']
print(players[0:3])

print('---')

players = ['charles', 'matina', 'michael', 'florence', 'eli']
print('Here are the first three players on my team：')
for player in players[:3]:
    print(player.title())


print('---')
# 复制列表，可以创建一个包含整个列表的切片
# 让Python 创建一个始于第一个元素，终止于最后一个元素的切片，即复制整个列表
my_foods = ['pizza', 'falafel', 'carrot cake']
friende_foods = my_foods[:]

print(my_foods)
print(friende_foods)
