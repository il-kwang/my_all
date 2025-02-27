# utf-8로 인코딩해라 <-type은 byte가 됨
a = 'Life is too short'
b = a.encode('utf-8')
print(b, type(b))

str_a = '한글'
encode_a = str.encode('euc-kr')
print(encode_a,type(encode_a))
decode_a = encode_a.decode('utf-8')
# decode_str = str_a.decode('utf-8')
print(decode_a,type(decode_a))

# closure 함수안에 내부 함수를 구현하고 그 내부 함수를 리턴하는 함수

#이터레이터 iterator 와 제너레이터 generator
a = [1,2,3] 
ia = iter(a) #한번 반복하면 안나옴 
for i in ia:
    print(i)

for i in ia:
    print(i)