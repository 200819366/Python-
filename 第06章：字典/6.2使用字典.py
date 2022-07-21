alien_0 = {'color': 'green', 'point': 5}
print(alien_0)

# 添加键值对
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# 创建空字典
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

# 修改字典的值
alien_0 = {'color': 'green'}
print("The alien is " + alien_0['color'] + '.')

alien_0['color'] = 'red'
print("Now the alien is " + alien_0['color'] + '.')

# 修改字典的值第二个例子
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position : " + str(alien_0['x_position']))

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] += x_increment
print("New x-position : " + str(alien_0['x_position']))

# 删除键值对
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)
