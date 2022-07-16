# 使用方法修改字符串的大小写
name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())
# 储存数据时，方法lower()很好用。
# 很多时候，你无法依靠用户来提供正确的大小写。
# 因此需要将字符串先转换为小写，再储存他们。


# 合并（拼接）字符串
first_name = "ada"
last_name = "lovelace"
full_name = first_name+" " + last_name

print(full_name)
print("Hello," + " " + full_name.title()+" !")

# 使用制表符或换行符来添加空白
print("\tPython")

print("Languages:\nPython\nC\nJavaScript")

print("Languages:\n\tPython\n\tC\n\tJavaScript")

# 删除空白
favorite_language = "python "
print(favorite_language)
print(favorite_language.rstrip())
