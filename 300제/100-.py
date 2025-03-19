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
'''#124
number1 = int(input('input1: '))
number2 = int(input('input2: '))
number3 = int(input('input3: '))

print(max(number1,number2,number3))'''

'''#125
input125 = input('휴대전화 번호 입력:')
if input125[0:3] == 011:
    print('당신은 SKT 사용자입니다.')
elif input125[0:3] == 016:
    print('당신은 KT 사용자입니다.')
elif input125[0:3] == 019:
    print('당신은 LGU 사용자입니다.')
else:
    print('알 수 없습니다.')

'''
'''#126
post_number = input('우편번호 : ')
if post_number[2] == 0 or post_number[2] == 1 or post_number[2] ==2:
    print('강북구')
elif post_number[2] == 3 or post_number[2] == 4 or post_number[2] == 5:
    print('도봉구')
elif post_number[2] == 6 or post_number[2] == 7 or  post_number[2] == 8 or post_number[2] == 9:
    print('노원구')
    '''
'''#127
input127 = input('입력 : ')
if input127[7] == '1' or input127[7] =='3':
    print('남자')
elif input127[7] == '2' or input127[7] =='4':
    print('여자')
else:
    print('알 수 없습니다.')'''
'''#128
input128 = input('입력 :')

if input128[8] == '0':
    if input128[9] == '9':
        print('서울이 아닙니다.')
    else:
        print("서울 입니다.") 
else:
    print('서울이 아닙니다.')
    
#129'''

input129 = input('입력 :')
#821010 - 1635210
inta1 = int (input129[0]) * 2  #16 + 6 + 4 + 0 + 6 + 0 + 8 +54 + 6 +15 + 8 + 5  = 128
inta2 = int (input129[1]) * 3
inta3 = int (input129[2]) * 4
inta4 = int (input129[3]) * 5
inta5 = int (input129[4]) * 6
inta6 = int (input129[5]) * 7
inta7 = int (input129[7]) * 8
inta8 = int (input129[8]) * 9
inta9 = int (input129[9]) * 2
inta10 = int (input129[10]) * 3
inta11 = int (input129[11]) * 4
inta12 = int (input129[12]) * 5
print(input129)

input_sum = inta1 + inta2 + inta3 + inta4 + inta5 + inta6 + inta7 + inta8 + inta9 + inta10 + inta11 + inta12
one_int = input_sum % 11
print(f"input_sum = {input_sum} / 11의 나머지 = {one_int}")
print(one_int)


