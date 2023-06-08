try:
    print('a' * 5)
    print('b' + 5)
except TypeError as e:
    print(f'can not add symbol and integer,\n{e}')

