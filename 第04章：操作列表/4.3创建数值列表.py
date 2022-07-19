# 使用 range 函数
for value in range(1, 5):
    print(value)


# 数字列表
numbers = list(range(1, 6))
print(numbers)


squares = []
for value in range(1, 11):
    square = value**2
    squares.append(square)
print(squares)

# 简单的统计工作
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

# 列表解析
squares = [value**2 for value in range(1, 11)]
print(squares)
