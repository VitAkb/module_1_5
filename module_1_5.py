"modul_1_5"
immutable_var = (1, 3, 5, [10, 8, 6], "String", True)
print(immutable_var)
# immutable_var[1] = 200  {программа будет выдавать ошибку, так как кортеж не позволяет изменять элементы внутри себя}
immutable_var[3][1] = 200 # однако, элементы внутреннего списка изменять дозволено
print(immutable_var)
mutable_list = [1, 2, 3, "String_List", False]
print(mutable_list)
mutable_list[3] = "Change"
mutable_list.extend(["New"])
print(mutable_list)