# 이 코드를 실핼 시  error가 뜰것이다. 이유는 튜플은 원소 값이 변경이 되면 안된다.


t = (1, 2, 3)
t[0] = 'a'
