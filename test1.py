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

new_list = ['Life', 'is', 'too', 'short']
print(' '.join(new_list))

my_tuple = (1,2,3)
rmy_tuple = list(my_tuple)
print(rmy_tuple,type(rmy_tuple))
rmy_tuple.append(4)
print(rmy_tuple,type(rmy_tuple))
my_tuple = tuple(rmy_tuple)
print(my_tuple,type(my_tuple))

#

a = {'A':90, 'B':80, 'C':70}
print(a.values())