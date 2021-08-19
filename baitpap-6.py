a = int(input('nhập một số bất kỳ '))
if a<0 :
    a = a * (-1)
    print('năm bạn nhập là ', a)
else:
    a = a
    print('năm bạn nhập là ', a)
stra =  str(a)
if ((a%4 == 0 ) and (a%100 != 0)) or (a%400 == 0):
    print('năm này là năm nhuận ')
else:
    str = str(a)
    print('năm này không phải năm nhuận')
quit()



