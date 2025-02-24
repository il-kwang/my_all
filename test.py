#정수, 실수
print(1)
print(3.14)
#문자열
print('2hello')
print("안녕")

#변수 선언
evel = 10000
evel2 = 20000
evel3 = '반갑습니다'
print(evel)
print(evel2)
print(evel3)

한글변수 = '한글'
print(한글변수)

#변수 설정 시 공백, 특수문자, 숫자로 시작하는, 예약어 사용 못함

#형변환
#int() <- 정수형으로 변환 시 실수일 경우  ex) 2.4  int(float('2.4'))
#float() <- 실수형으로
#-------------단 변환 시 문자가 섞여 있을 경우 애러발생.
#str() <- 문자열 

print( int(float('3.14'))) # 출력 시 소수점 없이 출력. 

#산술 연산자   +  -  *  / %   //  **
print(5+2)
print(5-2)
print(5*2)
print(5/2)
print(5%2) #나머지
print(5 // 2) #몫만
print(5 ** 2) #제곱
print('ㄴㄴ')
#비교 연산자 문자 비교 가능능
print(5 < 2)
print(5 > 2)
print(5 <= 2)
print(5 >= 2)
print(5 == 2)
print(5 != 2)
#논리 연산자
print(1 < 2 and 2 < 3)
print(1 < 2 or 2 < 3)
print(not 1 < 2)
print(1 < 2 & 2 < 3)
print(1 < 2 | 2 < 3)
#멤버 연산자
print('c'in'cat') #cat이라는 문자열 안에 c가 있냐?
print('c'not in'cat') #cat이라는 문자열 안에 c가 없냐? 없으면 True / 있으면 False
#bool 형변화
print(bool()) #bool 안에 값이 있으면 True / 없으면 False 자주 사용은 안함 
print(bool(0)) #bool 안에 값이 있으면 True / 없으면 False 자주 사용은 안함 
print(bool(None)) #bool 안에 값이 있으면 True / 없으면 False 자주 사용은 안함 
print(bool('False'))
#주석 <--
'''
여
러
줄
주
석
'''
#인덱스와 슬라이싱
#인덱싱 문자열 필요한거 하나를 뽑아오는거
lang = "PYTHON"
print(lang[0]) #lang 문자열 첫번째 문자 
print(lang[-1]) #-1은 마지막을 의미

print(lang[1:]) #lang 문자열 1~끝까지
print(lang[:5]) #lang 문자열 처음부터 5이하까지 0~4
print(lang[2:6])
print(lang[:-1]) #문자열 마지막 빼고
#문자열 포매팅 파이썬에서 잘 안씀 
print("%10s" % "hi")
#문자열 처리 자료형태만 맞으면 연산도 가능 다르면 바꿔야 됨 
snack = '과자'
two = '2'
print(snack + two)

juseyo = snack + ' ' + two 
juseyo = juseyo + '주세요' # juseyo += ' 주세요' 한번에 호출이 더 적기 때문에 이게 더 나음

print(juseyo)


num = 3 
num = num + 2 # num += 2

print(len(snack)) #문자열의 길이를 출력하는 함수 공백 인식 함함

snacks = '''
주석이

아니다'''
print(snacks) #변수 이름에 ''' 이 들어갈 때 개행 그대로 변수에 들어간다. '''
print('#' * 60)

#메소드 method 함수 
#문자열 메소드    ex)문자열.메소드()
letter = 'how are You?'
print(letter.lower()) #문자열을 모두 소문자로 변경
print(letter.upper()) #대문자로 변경
print(letter.capitalize()) #문자열 첫번째만 대문자로
print(letter.title()) #어절에 첫번째만 대문자
print(letter.swapcase()) #대소문자 스압
print(letter.split()) #나눠주는 함수
print(letter.count('how')) #how 라는 문자열이 몇번 나오는지?

a = '나도고등학교'
print(a.startswith('나도')) #문자열의 시작이 '나도'로 시작하는지? True/False
print(a.endswith('학교')) #문자열 끝이 '학교'로 끝나는지? True /False

b = '...나도고등학교...' #글자 기준으로 인자와 동일한것을 제거
print(b.strip('.'))
print(b.lstrip('.'))
print(b.rstrip('.'))
print(b.replace('고등','초등')) # 문자열.replace('찾을 인자','변경하고 싶은 값')
print(b.find('학교'))
print(a.center(10,'-'))
#출력 옵션
python = '파이썬'
java = '자바'
C = 'C언어'
print(python + java)
print(python,java)
print('개발언어에는',' ' + python, java + " 등이 있다.") #개더러움
print('개발 언어에는 {}, {}, {}등이 있어요'.format(python,java,C)) #포맷팅하는 법
print(f'개발언어에는 {python},{java},{C}가 있어요') #f-string 단, python3.6이상 f' {} `` '
#따옴표 문제
print('친구가 "안녕" 이라고 말했다.')
print("나는 속으로 '엄청 어려운데'라고 생각했다.")
#탈출 문자 \  역슬레시
print('하지만 \'나만 당할 수 없지\' 라는 생각에 "엄청 쉽지" 라고했다.')

print('C:\\Users\\302\\Documents\\my_all') #하지만 경로가 너무 길어진다면
print(r'C:\Users\302\Documents\my_all\av\cs\wr\gr\gg')#row string

snack2 = "꿀꽈베기는 \n너무\n맛있어요." # \n 줄 바꿈 
print(snack2)

#리스트
my_list = ["오예스","몽쉘","초코파이"]#중복 값 허용
your_list = ["1,2.3,True,'아무거나'"]#인자 상관없음
empty_list = []#빈 리스트트
print(my_list[0])
print(my_list[-1])
print(my_list[:3])
print(my_list[2:])
print(my_list[1:3])
print(len(my_list))

my_list[1] = '몽쉘통통'
print(my_list)
my_list.append('가나초콜릿')

print(my_list)

my_list.remove('오예스')
print(my_list)

print(my_list + your_list) #이것도 가능하지만
my_list.extend(your_list) #확장 시기키
print(my_list)
my_list.insert(1,'1번이에여')
print(my_list)
my_list.pop()

#튜플  추가 제거 수정 안됨
my_tuple = ("오예스","몽쉘","초코파이")
print(my_tuple.count)

a, b, c = my_tuple

numbers = (1,2,3,4,5,6,7,8,9,10)
one,two, *others = numbers
print(one)
print(two)
print(others)
print('others = ' , others)
#set 중복 X ,순서 보장 안됨   추가 삭제는 가능능
A = {'돈까스','보쌈','제육덮밥'}
B = {"짬뽕", "초밥", "제육덮밥"}
print(A.intersection(B)) #교집함
print(A.union(B)) #합집합
print(A.difference(B))
A.add('닭갈비')

#딕셔너리 (key, vakue) {key:value}

person = {'이름' : '나귀욤', '나이':'7'}
print(person['이름'])
print(person['나이'])
print(person.get('별명'))
person['키'] = 130
person['최종학력'] = '유치원'
person.update({'키' : 180})
print(person)
person.pop('최종학력')
print(person)
#자주 쓰는애들
print(person.keys())
print(person.values())
print(person.items())
#---------------------------------
print(person.fromkeys('이름'))
print(person.popitem())
#print(person.setdefault())

print(my_tuple ,type(my_tuple))
my_list_to_tuple = list(my_tuple)
print(my_list_to_tuple,type(my_list_to_tuple))
my_list_to_tuple.append('자가비')
print(my_list_to_tuple,type(my_list_to_tuple))
my_tuple = tuple(my_list_to_tuple)
print(my_tuple, type(my_tuple))

my_list = ["오예스","몽쉘","초코파이","초코파이","초코파이"]
my_dic = dict.fromkeys(my_list)
print(my_dic)
my_list = list(my_dic)
print(my_list)































