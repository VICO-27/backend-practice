try:
    x = int(input('input an integer: '))
    print(x)
except:
    print('Someething went Wrong')
else:
    print('nothing went wrong')
finally:
    print('code finished')