'''
#if문 만약 ~라면  if 조건 :
today = "월요일"
if today == '일요일': #만약 today가 일요일 이라면
    print("놀자") #"놀자" 출력
elif today == '토요일': #만약에 today가 토요일 이라면
    print('조금만 놀자') # "조금만 놀자" 출력
else:                   #그게 아니라면
    print('학원가야됨')  # '학원가야됨' 이 출력
print('산책가자')

#이중 if 문 if문 안에 if문이 있는 형태태
yellow_card = 1
foul = True #값이 있다/ 없다 
if foul: #if foul == True 
    yellow_card +=1
    if yellow_card == 2:
        print('경고 누적 퇴장')
    else: 
        print('조심')
else:
    print('양심경기 中')

#for문  ~할 때 까지 for 변수 in 반복 범위 또는 대상 :
#x = 임시 변수 *직관적인 것으로 사용 하는 것이 좋음음
# range : start, stop, range(step)     인자 1개 일 때 :stop 인자   2개 일 때 : start, stop  인자 3개 일 때 :  start, stop, range(step)
for x in range(1,11,2):
    print(f"{x}")


#for문 구구단 short code
for x in range(1,10,1):
    for y in range(1,10,1):
        print(f'{x}*{y} = ',(x*y))
#list - for 문 활용
my_list = [1, 2, 3]
for x in my_list:
        print(x)
#dir - for문 활용
person = {'이름': '나귀욤', '나이': 7,'키': 120, '몸무게': 23}
for k, v in person.items():   #items return 값 2개로 한번에 처리 가능 
    print(k, v)
#문자 - for문 활용법
fruit = 'apple'
for x in fruit:
    print(x)

#for vs while   for 문은 정해진 만큼만 while문 일단 시작 파이썬은       do-while문 없음 
#while문 무한반복 
max = 25 # 최대 허용 무게
weight = 0 # 현재 캐리어 무게
item = 3 # 각 짐의 무게

while weight + item <= max:
    weight += item
    print(f'짐 {weight} 추가했습니다.')
print(f'총 무게는 {weight}입니다.') 



drama = ['시즌1', '시즌2', '시즌3', '시즌4', '시즌5']
for x in drama:
    if x == '시즌3':
        print(f'{x} 재미 없대, 그만 보자')
        break
    print(f'{x}')

for x in range(10):
    if x % 2 == 1:
        continue
    print(x)

#들여쓰기 indent

# List Comprehension
#리콜 대상 제품 조회
products = ['JOA-2020', 'JOA-2021', 'SIRO-2021', 'SIRO-2022'] #전체 제품 리스트
recall = [] #리콜 제품 리스트가 들어갈 빈 공간
for p in products:# 전체 제품 조회
    if p.startswith('SIRO'): #'SIRO'로 시작하는 제품일 경우
        recall.append(p)#recall []에 추가해라 
print(recall)

my_list = [1,2,3,4,5,]
new_list = [x for x in my_list if x>3]  #new_list = [변수 활용 for 변수 in 리스트 if 조건] <---한줄로 만든거
print(new_list)

recall2 = [x for x in products if x.startswith('SIRO')]
print(recall2)



def show_price(cusromer): #함수 생성 def 함수명(인자):  + return 반환값 
    print(f'{cusromer} 고객님 안녕하세요.')
    print('커트 가격은 10000원입니다.')

def get_price(is_vip):
    if is_vip == True:
        return 10000
    else:
        return 15000

price = get_price(True)
print(price)

고객_번호_1 = '나장발'
cus1 = '장발'
cus2 = '수염'

show_price(고객_번호_1) #함수 호출 
show_price(cus1) #함수 호출 
show_price(cus2) #함수 호출 


def cal(a,b):
    return a+b, a-b, a*b, a/b

print(cal(3,5))

result = cal(1,2)
sum, minus, multilple, division = result
print(result)
print(sum)


def defalt_get_price(is_vip = False):
    if is_vip ==True:
        return 10000
    else:
        return 15000
    
price1 = defalt_get_price()
print(price1)
price2 = defalt_get_price(True)
print(price2)

def orfer(shipping = '선불'):
    print(f'주문이 완료되었습니다. 배송료는 {shipping}')

# 전달값이 많아질 때

def order(shot=2, size='Regular', takeout=True): # 커피 주문
    print(f'아메리카노 {size} 사이즈 {shot}샷')
    if takeout:
        print('포장 주문이 완료되었습니다')
    else:
        print('주문이 완료 되었습니다')


# 키워드인자로 넘기지 않을거면 순서를 맞춰야 됨.
#order()   기본 디폴트로 결과가 나옴
#order(2, takeout=True) 2는 shot에 대입 size는 디폴트 takeout은 키워드 인자
#order(size=“Regular”)키워드 인자 받음 
#order(“Regular”, takeout=True) 인자 전달 시 순서에 맞지 않아 다르게 출력된다.

#가변인자 * 한 함수에 한번만 사용 가능,
def visit(today, *customers ):
    print(today)
    for customers in customers:
        print(customers)

visit('오늘', '첫번째', '두놈')

def print_kwargs(**kwargs): #딕셔너리 전용 가변인자
    print(kwargs)
    return kwargs

result = print_kwargs(name='ss', age=3,height = 170)
print(type(result))


message = '전역 변수'

#지역 변수 local
def secret():
    message = '지역 변수'
    return message
#print(message) <---함수 내 지역변수 임으로 호출 불가능


# 전역 변수 global
def no_secret():
    return message

def global_secret():
    global message
    message = '지역변수'
    print(message,id(message))

print(secret(),id(message)) #포인터는 전역변수의 포인터를 가져와서 주소값이 밑이랑 똑같음 제대로 확인 하고싶으면 함수 내에서 호출해야됨됨
print(no_secret(),id(message))# 
global_secret()

name = input('이름이 뭔가요?')
num = int(input('총 몇명이신가요?')) #input 함수는 기본적으로 str type으로 입력 받음
if num > 4:
    print('죄송합니다. 저희는 4명까지만 예약가능합니다.')
print(f'{name} 고객님 총 {num}명 예약완료하였습니다.')






with open('list.txt', 'r', encoding='utf8') as f:
    contents = f.read()
    print(contents)
#with문이 끝나면 파일이 알아서 닫힘
#with open('파일.확장자','r/w', encoding='utf8) as 변수:



#주어진 문자열을 반대로 뒤집는 함수 reverse_string을 작성하세요. 예를 들어, 입력 문자열이 "Python"이면 출력은 "nohtyP"이어야 합니다.
str = "Python"
def reverse_string(s):
    return s[::-1] #-1 간격으로 = 거꾸로 

output = reverse_string(str)
print(output)

#주어진 숫자가 소수인지 아닌지를 판별하는 함수 is_prime을 작성하세요. 소수는 1과 자기 자신만을 약수로 갖는 1보다 큰 양의 정수입니다. 함수는 소수일 경우 True를 반환하고, 아닐 경우 False를 반환해야 합니다.

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(is_prime(5))
        
        
# 사용자로부터 숫자를 입력받아 그 숫자의 제곱 값을 출력하는 프로그램을 작성하세요.

def is_x():
    num = int(input("제곱하기 원하는 숫자를 입력하세요."))
    return num*num

print(is_x())

#사용자로부터 이름과 나이를 입력받아, 10년 후의 나이를 출력하는 프로그램을 작성하세요.

def years_10():
    name = input("당신의 이름을 적어주세요.")
    after_year = int(input("현재 나이를 입력해주세요.")) + 10
    print(f"{name}님 10년뒤 나이는 {after_year}살 입니다.")
    #return after_year

#print( f"당신의 10년뒤 나이는", years_10(),"살입니다")
years_10()

# 사용자로부터 입력받은 내용을 파일에 작성하는 프로그램을 작성하세요. 파일 이름은 "input.txt"로 합니다.

user_input = input("입력하고 싶은 내용을 적어주세요.")

with open("input.txt", "w",encoding = "utf8") as file:
    file.write(user_input)

# 파일에 있는 모든 줄을 읽어 대문자로 변환하여 출력하는 프로그램을 작성하세요. 파일 이름은 "example.txt"로 합니다.

with open("example.txt","r",encoding="utf8")as file:
        for line in file:
            print(line.upper().strip())



# 명령 줄 인수로 두 숫자와 사칙연산 기호(+, -, *, /)를 입력받아 계산 결과를 출력하는 프로그램을 작성하세요.
def cal(a,b):
      print(a+b,a-b,a*b,a/b)

cal(1,3)



import sys
args = sys.argv[1:]
sum = 0
for i in args:
    sum += int(i)

print(sum)
'''

# 사용자로부터 정수를 입력받고, 그 정수가 짝수인지 홀수인지 판별하는 프로그램을 작성하세요.
num = int(input("숫자 :"))
if num % 2 == 1:
    print(f"{num} = 홀수 입니다.")
else:
    print(f"{num} = 짝수 입니다.")

# 사용자로부터 세 개의 정수를 입력받고, 가장 큰 수를 출력하는 프로그램을 작성하세요.
a, b, c = int(input("세숫자를 입력 해주세요."))
