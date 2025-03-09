temp = {}

icream = {"메로나" : "1000", "폴라포" : "1200", "빵빠레" : "1800"}
print(icream)
icream["죠스바"] = 1200
icream["월드콘"] = 1500
print(icream)
print(f"메로나 가격 :{icream['메로나']}")
icream["메로나"] = 1300 #메로나 가격 변경 
print(f"메로나 가격 :{icream['메로나']}")
icream.pop('메로나') #메로나 삭제
print(icream)

'''
>> icecream = {'폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
>> icecream['누가바']
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    icecream['누가바']
KeyError: '누가바'
<---키의 상한하는 value 값이 없음
''' 