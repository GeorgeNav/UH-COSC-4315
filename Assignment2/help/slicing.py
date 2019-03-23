tokens = [0, '1', 2, 3, 4, 5, 6, False, 7]
lpar_index = 2
rpar_index = 5
first_part = tokens[0:lpar_index]
func = tokens[lpar_index:rpar_index+1]
last_part = tokens[rpar_index+1:]
a = first_part + func + last_part
print(first_part)
print(func)
print(last_part)
for token in tokens:
    if isinstance(token, bool):
        print('bool')
    elif isinstance(token, int):
        print('int')
    elif isinstance(token, str):
        print('str')
    else:
        print('Ouch')

a = [1, 2, 3]
a.append([3, 4])
print(a)

a = []
print(len(a))