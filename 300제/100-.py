'''#101 
'''
'''True/False 를 갖는 데이터 타입
bool type
'''
'''

print(3==5) # False 출력
print(3<5) #True 출력
x = 4
print(1 < x < 5) #True 출력
print ((3 == 3) and (4 != 3)) #3 과 3이 같고 4와 3은 갖지 않을 때 True False 출력
# print(3 => 4) # 문법 자체가 틀림
if 4 < 3 :
    print("Hello world")
#아무일 일어나지 않는다.

if 4 < 3:
    print("Hello World.")
else:
    print("Hi, there.")

# Hi, There 가 출력이 된다.

if True :
    print ("1")
    print ("2")
else :
    print("3")
print("4")
# 1 2 4 이렇게 출력된다.

if True :
    if False:
        print("1")
        print("2")
    else:
        print("3")
else :
    print("4")
print("5")

# 3 5 이렇게 출력 된다.

#111
a = input()
print(a*2)
#112
b = int(input("숫자를 입력하세요 : "))
print(b + 10)
#113
c = int(input("홀짝 판별 :"))
if c % 2 == 0:
    print("짝수")
else:
    print("홀수")
   
#114
input114 = int(input("입력값 : "))
input114 += 20
if input114 > 255 :
    input114 = 255
    print(input114)
else:
    print(input114)

#115
input115 = int(input("입력값 : "))
input115 -= 20
if input115 < 0 :
    input115 = 0
    print(input115)
elif input115 > 255:
    input115 = 255
    print(input115)

else:
    print(input115) 
   

#116
input116 = input("현재시간:")
if input116[-2:] =="00":
    print("정각 입니다.")
else:
    print("정각이 아닙니다.")


#117
fruit = ["사과", "포도", "홍시"]

choice = input("좋아하는 과일은?")
if choice in fruit:
    print("정답입니다.")
else:
    print("오답입니다.")

#118
warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]

warn = input("관심 종목 : ")
if warn in warn_investment_list:
    print("투자 경고 종목입니다.")
else:
    print("투자 경고 종목이 아닙니다.")


#119
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}

choice_119 = input("제가 좋아하는 계절은:")
if choice_119 in fruit:
    print("정답입니다.")
else:
    print("오답입니다.")

#120
choice_120= input("제가 좋아하는 과일은?")
if choice_120 in fruit.values():
    print("정답입니다.")
else:
    print("오답입니다.")
'''    
'''
#121
input121 =input('알파벳을 입력해주세요.')
if input121.islower(): #소문자일 떄 True
    print(input121.upper()) #대문자로 바꾼다.
else:
    print(input121)
'''

'''#122
score = int(input("score :"))#int형 으로 입력 받기

if 81 <= score <= 100:
    print("grade is A")
elif 61 <= score <= 80:
    print('grade is B')
elif 41 <= score <= 60:
    print('grade is C')
elif 21 <= score <= 40:
    print('grade is D')
else:
    print('grade is E')'''
'''
#123
input123money, input123 = float(input("입력: ")) , input() 
print(input123money, input123)

if input123 == "달러":
    input123money *= 1167
elif input123 == "엔":
    input123money *= 1.096
elif input123 == "유로":
    input123money *= 1268
elif input123 == "위안":
    input123money *= 171
else:
    print("지원하지 않는 화폐입니다.")
print(input123money, "원")
'''
#124
number1 = int(input('input1: '))
number2 = int(input('input2: '))
number3 = int(input('input3: '))

print(max(number1,number2,number3))