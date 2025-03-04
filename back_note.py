'''#10926
# 준하는 사이트에 회원가입을 하다가 joonas라는 아이디가 이미 존재하는 것을 보고 놀랐다. 
# 준하는 놀람을 ??!로 표현한다. 준하가 가입하려고 하는 사이트에 이미 존재하는 아이디가 주어졌을 때, 놀람을 표현하는 프로그램을 작성하시오.
# 조건 1. 이미 존재하는 아이디가 주어진다. 길이는 50자를 넘지 않는다.


id = input()
print(id + "??!")
'''

'''#18108
ICPC Bangkok Regional에 참가하기 위해 수완나품 국제공항에 막 도착한 팀 레드시프트 일행은 눈을 믿을 수 없었다. 공항의 대형 스크린에 올해가 2562년이라고 적혀 있던 것이었다.
불교 국가인 태국은 불멸기원(佛滅紀元), 즉 석가모니가 열반한 해를 기준으로 연도를 세는 불기를 사용한다. 
반면, 우리나라는 서기 연도를 사용하고 있다. 불기 연도가 주어질 때 이를 서기 연도로 바꿔 주는 프로그램을 작성하시오.

입력
서기 연도를 알아보고 싶은 불기 연도 y가 주어진다. (1000 ≤ y ≤ 3000)

#543년 차이가 난다
 즉 서기 년도 + 543을 하면 불기 년도를 알 수 있다 
출력
불기 연도를 서기 연도로 변환한 결과를 출력한다.

y = int(input())
print(y-543)

#11382

A, B, C= map(int,input().split()) #한줄에 여러개 입력 받기

print(A+B+C)
'''
#1330
'''
문제
두 정수 A와 B가 주어졌을 때, A와 B를 비교하는 프로그램을 작성하시오.

입력
첫째 줄에 A와 B가 주어진다. A와 B는 공백 한 칸으로 구분되어져 있다.

출력
첫째 줄에 다음 세 가지 중 하나를 출력한다.

A가 B보다 큰 경우에는 '>'를 출력한다.
A가 B보다 작은 경우에는 '<'를 출력한다.
A와 B가 같은 경우에는 '=='를 출력한다.
제한
-10,000 ≤ A, B ≤ 10,000

A, B = map(int,input().split())
if A > B:
    print('>')
elif B > A:
    print('<')
elif A == B:
    print('==')
    '''
#9498
'''
문제
시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 시험 점수가 주어진다. 시험 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.

출력
시험 성적을 출력한다.

score = int(input())

if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
else:
    print('F')
'''
#2753
'''
문제
연도가 주어졌을 때, 윤년이면 1, 아니면 0을 출력하는 프로그램을 작성하시오.

윤년은 연도가 4의 배수이면서, 100의 배수가 아닐 때 또는 400의 배수일 때이다.

예를 들어, 2012년은 4의 배수이면서 100의 배수가 아니라서 윤년이다. 
1900년은 100의 배수이고 400의 배수는 아니기 때문에 윤년이 아니다. 
하지만, 2000년은 400의 배수이기 때문에 윤년이다.

입력
첫째 줄에 연도가 주어진다. 연도는 1보다 크거나 같고, 4000보다 작거나 같은 자연수이다.

출력
첫째 줄에 윤년이면 1, 아니면 0을 출력한다.

youn = int(input())

if (youn % 4 == 0 and youn % 100 != 0) or youn % 400 == 0 :
    print(1)
else:
    print(0)


#14681 사분면 추적 좌표 값을 보고 사분면 어디 위치하는지 출력하기 

x = int(input())
y = int(input())

if x >= 1 and y >= 1:
    print(1)
elif x >= 1 and y < 0:
    print(4)
elif x < 0 and y >= 1:
    print(2)
else:
    print(3)

'''
#2884 알람시계
'''
문제
상근이는 매일 아침 알람을 듣고 일어난다. 
알람을 듣고 바로 일어나면 다행이겠지만, 항상 조금만 더 자려는 마음 때문에 매일 학교를 지각하고 있다.
상근이는 모든 방법을 동원해보았지만, 조금만 더 자려는 마음은 그 어떤 것도 없앨 수가 없었다.
이런 상근이를 불쌍하게 보던 창영이는 자신이 사용하는 방법을 추천해 주었다.
바로 "45분 일찍 알람 설정하기"이다.

이 방법은 단순하다. 원래 설정되어 있는 알람을 45분 앞서는 시간으로 바꾸는 것이다. 
어차피 알람 소리를 들으면, 알람을 끄고 조금 더 잘 것이기 때문이다. 
이 방법을 사용하면, 매일 아침 더 잤다는 기분을 느낄 수 있고, 학교도 지각하지 않게 된다.
현재 상근이가 설정한 알람 시각이 주어졌을 때, 창영이의 방법을 사용한다면, 이를 언제로 고쳐야 하는지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 두 정수 H와 M이 주어진다. 
(0 ≤ H ≤ 23, 0 ≤ M ≤ 59) 그리고 이것은 현재 상근이가 설정한 알람 시간 H시 M분을 의미한다.
입력 시간은 24시간 표현을 사용한다. 
24시간 표현에서 하루의 시작은 0:0(자정)이고, 끝은 23:59(다음날 자정 1분 전)이다. 
시간을 나타낼 때, 불필요한 0은 사용하지 않는다.

출력
첫째 줄에 상근이가 창영이의 방법을 사용할 때, 설정해야 하는 알람 시간을 출력한다. (입력과 같은 형태로 출력하면 된다.)


H, M = map(int,input().split())

if M >= 45:
    print(H, M-45)
elif M <= 45 and H > 0:
    print(H-1, M+15)
else:
    print(23, M+15)
'''

#2525 
'''
문제
KOI 전자에서는 건강에 좋고 맛있는 훈제오리구이 요리를 간편하게 만드는 인공지능 오븐을 개발하려고 한다. 
인공지능 오븐을 사용하는 방법은 적당한 양의 오리 훈제 재료를 인공지능 오븐에 넣으면 된다. 
그러면 인공지능 오븐은 오븐구이가 끝나는 시간을 분 단위로 자동적으로 계산한다.
또한, KOI 전자의 인공지능 오븐 앞면에는 사용자에게 훈제오리구이 요리가 끝나는 시각을 알려 주는 디지털 시계가 있다.
훈제오리구이를 시작하는 시각과 오븐구이를 하는 데 필요한 시간이 분단위로 주어졌을 때, 오븐구이가 끝나는 시각을 계산하는 프로그램을 작성하시오.

입력
첫째 줄에는 현재 시각이 나온다. 현재 시각은 시 A (0 ≤ A ≤ 23) 와 분 B (0 ≤ B ≤ 59)가 정수로 빈칸을 사이에 두고 순서대로 주어진다. 두 번째 줄에는 요리하는 데 필요한 시간 C (0 ≤ C ≤ 1,000)가 분 단위로 주어진다.

출력
첫째 줄에 종료되는 시각의 시와 분을 공백을 사이에 두고 출력한다. (단, 시는 0부터 23까지의 정수, 분은 0부터 59까지의 정수이다. 디지털 시계는 23시 59분에서 1분이 지나면 0시 0분이 된다.)

A, B = map(int,input().split()) # 시작 시간 
C = int(input()) # 진행 시간 먼저 분으로 환산 해준다. ex) 240 = 6 시간
d = C //60
e = C % 60

A += d
B += e 
if B >= 60:
    d = B // 60
    B %= 60
    A = A + d
    if A >= 24:
        print(A-24,B)
    else:
        print(A,B)
elif A >= 24 :
    print(A-24,B)
else:
    print(A, B)
    '''

#2480 
'''
문제
1에서부터 6까지의 눈을 가진 3개의 주사위를 던져서 다음과 같은 규칙에 따라 상금을 받는 게임이 있다.

1. 같은 눈이 3개가 나오면 10,000원+(같은 눈)×1,000원의 상금을 받게 된다.
2. 같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)×100원의 상금을 받게 된다.
3. 모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)×100원의 상금을 받게 된다.

예를 들어, 3개의 눈 3, 3, 6이 주어지면 상금은 1,000+3×100으로 계산되어 1,300원을 받게 된다. 
또 3개의 눈이 2, 2, 2로 주어지면 10,000+2×1,000 으로 계산되어 12,000원을 받게 된다. 
3개의 눈이 6, 2, 5로 주어지면 그중 가장 큰 값이 6이므로 6×100으로 계산되어 600원을 상금으로 받게 된다.

3개 주사위의 나온 눈이 주어질 때, 상금을 계산하는 프로그램을 작성 하시오.

입력
첫째 줄에 3개의 눈이 빈칸을 사이에 두고 각각 주어진다.

출력
첫째 줄에 게임의 상금을 출력 한다.

a, b, c =map(int,input().split()) # 정수 3개를 받아온다.

if a == b == c :
    print(a *1000 + 10000)
elif a==b and a !=c:
    print(a*100+1000)
elif a==c and a !=b:
    print(a*100 + 1000)
elif b==c and a != b:
    print(b*100+1000)
else:
    print(max(a,b,c)*100)

    '''

#2739 
'''
문제
N을 입력받은 뒤, 구구단 N단을 출력하는 프로그램을 작성하시오. 출력 형식에 맞춰서 출력하면 된다.

입력
첫째 줄에 N이 주어진다. N은 1보다 크거나 같고, 9보다 작거나 같다.

출력
출력형식과 같게 N*1부터 N*9까지 출력한다.

n = int(input())

for x in range(1,10,1):
    print(f"{n} * {x} =",n*x)
    '''

#10950
'''문제
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다.

각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

출력
각 테스트 케이스마다 A+B를 출력한다.

t = int(input())

for n in range(0,t,1):
    a,b = map(int,input().split())
    print(a+b)
'''

#8393
'''
문제
n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 n (1 ≤ n ≤ 10,000)이 주어진다.

출력
1부터 n까지 합을 출력한다.


n = int(input())
result = 0
for x in range(1,n+1,1):
    result += x  # 1 + 2 + 3 + 4 + 5''n

print(result)

'''

#25304
'''
문제
준원이는 저번 주에 살면서 처음으로 코스트코를 가 봤다. 정말 멋졌다. 
그런데, 몇 개 담지도 않았는데 수상하게 높은 금액이 나오는 것이다! 
준원이는 영수증을 보면서 정확하게 계산된 것이 맞는지 확인해보려 한다.

영수증에 적힌,

구매한 각 물건의 가격과 개수
구매한 물건들의 총 금액
을 보고, 구매한 물건의 가격과 개수로 계산한 총 금액이 영수증에 적힌 총 금액과 일치하는지 검사해보자.
입력
첫째 줄에는 영수증에 적힌 총 금액 
$X$가 주어진다.
둘째 줄에는 영수증에 적힌 구매한 물건의 종류의 수 
$N$이 주어진다.
이후 
$N$개의 줄에는 각 물건의 가격 
$a$와 개수 
$b$가 공백을 사이에 두고 주어진다.

출력
구매한 물건의 가격과 개수로 계산한 총 금액이 영수증에 적힌 총 금액과 일치하면 Yes를 출력한다. 
일치하지 않는다면 No를 출력한다.


# 총 금액   -->(물건의 종류 수 만큼 반복)  - (물건 가격격 * 갯수)'' = 0  일때 Yes   0이 아닐 때 No

pull_price = int(input())  
object_num = int(input())

for x in range(0,object_num,1):
    object_price, num = map(int,input().split())
    a = object_price*num
    pull_price -= a

if pull_price == 0:
    print('Yes')
else:
    print('No')
    '''

#25314
'''오늘은 혜아의 면접 날이다. 면접 준비를 열심히 해서 앞선 질문들을 잘 대답한 혜아는 이제 마지막으로 칠판에 직접 코딩하는 문제를 받았다. 
혜아가 받은 문제는 두 수를 더하는 문제였다. C++ 책을 열심히 읽었던 혜아는 간단히 두 수를 더하는 코드를 칠판에 적었다. 
코드를 본 면접관은 다음 질문을 했다. “만약, 입출력이 
$N$바이트 크기의 정수라면 프로그램을 어떻게 구현해야 할까요?”

혜아는 책에 있는 정수 자료형과 관련된 내용을 기억해 냈다. 책에는 long int는 
$4$바이트 정수까지 저장할 수 있는 정수 자료형이고 long long int는 
$8$바이트 정수까지 저장할 수 있는 정수 자료형이라고 적혀 있었다. 혜아는 이런 생각이 들었다. “int 앞에 long을 하나씩 더 붙일 때마다 
$4$바이트씩 저장할 수 있는 공간이 늘어나는 걸까? 분명 long long long int는 
$12$바이트, long long long long int는 
$16$바이트까지 저장할 수 있는 정수 자료형일 거야!” 그렇게 혜아는 당황하는 면접관의 얼굴을 뒤로한 채 칠판에 정수 자료형을 써 내려가기 시작했다.

혜아가 
$N$바이트 정수까지 저장할 수 있다고 생각해서 칠판에 쓴 정수 자료형의 이름은 무엇일까?

입력
첫 번째 줄에는 문제의 정수 
$N$이 주어진다. 
$(4\le N\le 1\, 000$; 
$N$은 
$4$의 배수
$)$ 

출력
혜아가 
$N$바이트 정수까지 저장할 수 있다고 생각하는 정수 자료형의 이름을 출력하여라.


Num = int(input())
N = int(Num/4)
long_size = []

for x in range(0,N,1):
    long_size.append('long')


long_size.append('int') #마지막에 한 번만 int를 붙여준다다
print(' '.join(long_size))# 출력하기 전에 join함수로 문자열을 합쳐준다.
'''

#15552
'''
빠른 A+B 성공

문제
본격적으로 for문 문제를 풀기 전에 주의해야 할 점이 있다. 입출력 방식이 느리면 여러 줄을 입력받거나 출력할 때 시간초과가 날 수 있다는 점이다.

C++을 사용하고 있고 cin/cout을 사용하고자 한다면, cin.tie(NULL)과 sync_with_stdio(false)를 둘 다 적용해 주고, endl 대신 개행문자(\n)를 쓰자. 단, 이렇게 하면 더 이상 scanf/printf/puts/getchar/putchar 등 C의 입출력 방식을 사용하면 안 된다.

Java를 사용하고 있다면, Scanner와 System.out.println 대신 BufferedReader와 BufferedWriter를 사용할 수 있다. BufferedWriter.flush는 맨 마지막에 한 번만 하면 된다.

Python을 사용하고 있다면, input 대신 sys.stdin.readline을 사용할 수 있다. 
단, 이때는 맨 끝의 개행문자까지 같이 입력받기 때문에 문자열을 저장하고 싶을 경우 .rstrip()을 추가로 해 주는 것이 좋다.

또한 입력과 출력 스트림은 별개이므로, 테스트케이스를 전부 입력받아서 저장한 뒤 전부 출력할 필요는 없다. 테스트케이스를 하나 받은 뒤 하나 출력해도 된다.

자세한 설명 및 다른 언어의 경우는 이 글에 설명되어 있다.

이 블로그 글에서 BOJ의 기타 여러 가지 팁을 볼 수 있다.

입력
첫 줄에 테스트케이스의 개수 T가 주어진다. T는 최대 1,000,000이다. 다음 T줄에는 각각 두 정수 A와 B가 주어진다. A와 B는 1 이상, 1,000 이하이다.

출력
각 테스트케이스마다 A+B를 한 줄에 하나씩 순서대로 출력한다.

import sys

T = int(input())

for x in range(0,T,1):
    a, b = map(int,sys.stdin.readline().split())
    print(a+b)
    '''
''' 

#11021
A+B - 7 
문제
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다.

각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

출력
각 테스트 케이스마다 "Case #x: "를 출력한 다음, A+B를 출력한다. 테스트 케이스 번호는 1부터 시작한다.
import sys
T = int(input())

for x in range(0,T,1):
    a, b = map(int,sys.stdin.readline().split())
    print(f'Case #{x+1}:',a+b)
    ''' 
#11022
#A+B - 8
'''
import sys
T = int(input())

for x in range(0,T,1):
    a, b = map(int,sys.stdin.readline().split())
    print(f'Case #{x+1}: {a} + {b} =',a+b)

N = int(input())

for x in range(N):
    print('*'*(x+1))
    '''
#2439
'''
별 찍기 - 2 성공
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	128 MB	368140	205698	172772	56.036%
문제
첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제

하지만, 오른쪽을 기준으로 정렬한 별(예제 참고)을 출력하시오.

입력
첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

출력
첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.


N = int(input())

for i in range(N):
    a = ('*'*(i+1)) 
    b = a.rjust(N)
    print(b)

while True:
    a,b = map(int,input().split())
    if a == 0 and b == 0:
        break
    else:
        print(a+b)
'''
# 10951
'''
문제
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

입력
입력은 여러 개의 테스트 케이스로 이루어져 있다.

각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

출력
각 테스트 케이스마다 A+B를 출력한다.
import sys

for i in sys.stdin:
    a,b=map(int, i.split())
    print(a+b)

    '''

# 개수 세기
'''

문제
총 N개의 정수가 주어졌을 때, 정수 v가 몇 개인지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 정수의 개수 N(1 ≤ N ≤ 100)이 주어진다. 둘째 줄에는 정수가 공백으로 구분되어져있다. 셋째 줄에는 찾으려고 하는 정수 v가 주어진다. 입력으로 주어지는 정수와 v는 -100보다 크거나 같으며, 100보다 작거나 같다.

출력
첫째 줄에 입력으로 주어진 N개의 정수 중에 v가 몇 개인지 출력한다.

N = int(input()) # 몇번 반복할 지.
list_a = list(map(int,input().split())) #한줄로 받아온거 저장해 
v = int(input()) #찾을 번호 
print(list_a.count(v)) #몇개 있는지 찾기
'''

#X보다 작은 수 성공
'''
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	256 MB	359858	197052	158174	54.297%
문제
정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 N과 X가 주어진다. (1 ≤ N, X ≤ 10,000)

둘째 줄에 수열 A를 이루는 정수 N개가 주어진다. 주어지는 정수는 모두 1보다 크거나 같고, 10,000보다 작거나 같은 정수이다.

출력
X보다 작은 수를 입력받은 순서대로 공백으로 구분해 출력한다. X보다 작은 수는 적어도 하나 존재한다.
'''
## 10871
'''
N, X = map(int,input().split())
A = list(map(int,input().split()))

for x in range(N):
    if A[x] < X:
        print(A[x],end= ' ')
'''       

#10818
'''
N = int(input())
A = list(map(int,input().split()))

print(min(A),max(A))

'''
#2562
'''
A = []
for i in range(9):
    A.append(int(input()))

print(max(A))
print(A.index(max(A))+1)'''

#10810 공 넣기 
'''
N,M = map(int,input().split()) # 바구니의 수 , 공 넣기 횟수

box = ['0'] *N #빈 바구니를 구현현
for x in range(M):
    i,j,k = map(int,input().split())
    for x in range(i-1,j):
        box[x]= str(k)
print(' '.join(box))
'''

#10813 공 바꾸기

'''
N,M = map(int,input().split()) # 바구니의 수 , 공 교환 횟수
box = ['0'] * N
for x in range(N):
    box[x] = x+1


for x in range(M):
    i, j = map(int,input().split())
    box[i-1] , box[j-1] = box[j-1],box[i-1] #list swap 

print(' '.join(map(str,box)))
'''
#5597
'''
num = []
for i in range(30):
    num.append(i+1)

for x in range(28):
    num.remove(int(input()))
print('\n'.join(map(str,num)))
'''

#3052
'''
B = 42
num_list = []
for x in range(10):
    A = int(input())
    num_list.append(A%B)

set_num = set(num_list)

#set_num.remove(0)
print(len(set_num))
#for x in range(10):
    
'''
# box = [i for i in range(1,n+1)] #n을 입력 받아 원소를 리스트에 채워 넣음 1~n+1 까지
'''
N,M = map(int,input().split())
box = []


#print(f'바구니의 수 : {N} swap count :{M}')

for x in range(N):
    box.append(x+1)

#print(f'박스 리스트 : ',box)



for k in range(M):
    i,j = map(int,input().split())
    revers_box = box[i-1:j]
    revers_box.reverse()
    box[i-1:j] = revers_box
    #print(box)

print(*box) #리스트 쉼표 및 대괄호없이 출력.
'''



'''
N = int(input())
score = list(map(int,input().split()))
#print(score)
max_score = max(score)


for x in range(N):
    score[x] = score[x]/max_score*100
average = sum(score) / N


print(average)
'''

#27866
'''
S = input()
i = int(input())

print(S[i-1])'''

#2743
'''S = input()
print(len(S))'''

#9086
'''N = int(input())
string_grupe = []

for x in range(N):
    a = input() # 문자열로 먼저 입력 받기 : 문자열로 먼저 받아서 첫글자 마지막 글자를 가공하고 리스트에 넣는게 효율적이라고 생각 함
    b = a[0] + a[-1]
    string_grupe.append(b) 

print(*string_grupe, sep='\n')
'''
# 11654
'''print(ord(input()))#키보드로 입력 받은 것을 출력해라. ord(입력) ==  키보드 입력한 문자 -> 아스키 번호
'''

#11720

'''N = int(input())
int_num = int(input())
list_num = list(map(int,str(int_num)))
print(sum(list_num))

'''

#10809  문자열로 for문 if문 둘다 돌릴 수 있는거 
'''
S = input()
abc ='abcdefghijklmnopqrstuvwxyz'

for i in abc:
    if i in S:
        print(S.index(i), end= ' ')
        
    else:
        print(-1,end= ' ')
'''
#2675
'''
N = int(input())

for x in range(N):
    R, S = input().split()
    for i in range(len(S)):
        print(int(R) * S[i],end='')
    print()
'''

#1152

'''string = input().split()
print(len(string))
'''
#2908 

'''A, B = input().split()
A = int(A[::-1])
B = int(B[::-1])
if A>=B:
    print(A)
else:
    print(B) 
'''
#5622 다시 풀어야 되는 문제
'''
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
a = input()
ret = 0
for j in range(len(a)):
    for i in dial:
        if a[j] in i:
            ret += dial.index(i)+3
print(ret)

'''

'''while True :
    try :
        print(input())
    except EOFError:
        break
'''


'''
full_set = [1,1,2,2,2,8]
find_obj = list(map(int,input().split()))

print(find_obj)

print(*list(i-x for i,x in zip(full_set,find_obj)))


#for i, x in zip(full_set,find_obj):
    #print(i,x,i-x)
'''
N = int(input())
centet_num = N*2-1
for x in range(N):
    result = ('*' *(x*2+1)).center(centet_num)
    print(result)
    #result.centet(centet_num)
for x in range(1,N,-1):
    result = ('*'*((x-1)*2-1))
    print(result)