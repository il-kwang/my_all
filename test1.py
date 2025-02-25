"""
국어 = 80
영어 = 75
수학 = 55

avg = (국어+영어+수학)/3
print(avg)


num = 13%2
if num%2 == 1:
    print("홀수")
else:
    print("짝수")

주민등록번호 = "881120-1068234" 
print(type(주민등록번호))
print(주민등록번호.split('-'))
성별 = int(주민등록번호[7])
print(성별)
if 성별 %2 == 1:
    print("남자")
else:
    print("여자")

my = "a:b:c:d"
you = my.replace(':',"#")
print(my) 
print(you)

my_list = [1,3,5,4,2]
my_list.sort()
print(my_list)
my_list.reverse()
print(my_list)


# list -> str type 변경 )       ex ) .txt 출력 할 떄 
new_list = ['Life', 'is', 'too', 'short']
str_new_list = ' '.join(new_list)
print(' '.join(new_list))
print(str_new_list,type(str_new_list))



my_tuple = (1,2,3)
you_tuple = (4,) #그냥 정수만 들어가 있으면 int형 tuple로 인식 하게 하려면 쉼표, 하나 넣어주면 됨.
print(my_tuple + you_tuple)
print(you_tuple,type(you_tuple))
rmy_tuple = list(my_tuple)
print(rmy_tuple,type(rmy_tuple))
rmy_tuple.append(4)
print(rmy_tuple,type(rmy_tuple))
my_tuple = tuple(rmy_tuple)
print(my_tuple,type(my_tuple))



#No.9 딕셔너리, 리스트  <---리스트는 주소 호출의 느낌이 강함 딕셔너리는 키의 이름에 들어 갈 수 있는 것이 더 많다다

a = {'A':90, 'B':80, 'C':70}
#from_a_key = list(a) #key 값만 보임
print(a['B'])



# set로 형변화 할 수있음 순서보장은 못함 
list_a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
dictToList = dict.fromkeys(list_a)
print(type(list_a))
print(dictToList)
list_a = list(dictToList)
print(list_a)

#No.12 리스트에서 같은 주소값을 사용한다? a = b = [1,2,3] 일 경우 a,b 는 같은 주소값을 가짐 
"""

a  = "Life is too short, you need python"

if "wife" in a: 
    print("wife")
elif "python" in a and "you" not in a: 
    print("python")
elif "shirt" not in a: 
    print("shirt")
elif "need" in a: 
    print("need")
else: 
    print("none")

result = 0

i = 1
while i <= 1000:
    if i%3 ==0:
        result += i
    i += 1
print(result)


x = 0
while True:
    x += 1
    if x > 6:
        break
    else:
        print("*"*x)

for i in range(1,101,1):
    print(i)



A = [70,60,55,75,95,90,80,80,85,100]
total = 0

for score in A:
    total += score
average = total/len(A)
print(average)

numbers = [1,2,3,4,5]

print("예시코드")
result = []
for n in numbers:
    if n % 2 == 1:
        result.append(n*2)
print(result)

resutl2= [2*x for x in numbers if x % 2 == 1 ]
print(resutl2)



