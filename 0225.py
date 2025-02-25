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
'''
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