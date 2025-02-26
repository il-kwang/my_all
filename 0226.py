'''
#클래스 = 객체   instance - 객체 어디 소속 
class KeyBoard:   #클래스 안에 클래스 시작은 대문자로 
    def __init__(self, name, price):
        self.name = name  #멤버변수 
        self.price = price
        
    def set_LED(self,name): #클래스 내 함수
        print(f"{self.name}led ON")


class BtKeyBoard(KeyBoard):
    def set_auto_sleep(self,min):
        super().__init__(name)
        print(f'{self.name}은 {min}분 동안 사용하지 않아 수면모드에 진입합니다.')


    print('블루투스 지원 키보드입니다.')




k1 = KeyBoard('로지텍',120000)  #키보드 안에 객체 변수 
k2 = BtKeyBoard('레오폴드',100000)
k2.set_auto_sleep(10)
k1.led = True
k1.set_LED()

print()

print('k1은 KeyBoard의 소속이 되어 있나? ',isinstance(k1,KeyBoard))   #k1은 Keyboard의 인스턴스인지 맞으면 True /



#__init__adsa


class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):

class Calculator:
    def __init__(self):
        self.value = 0 #이거를 불러와야 됨

    def add(self, val):
        self.value += val


class Upgradecalculator(Calculator):
   # super().__init__(self.value)
    def minus(self, val):
        self.value -= val


#02 매소드 오버라이딩 발생 부모 클래스에서 add를 사용하지 않음.
class MaxLimitCalculator(Calculator):    
    def add(self, val):
        self.value += val
        if self.value >= 100:
            self.value = 100

    

#01
cal = Upgradecalculator() #여기에서 호출 시 value 값이 0으로 초기 화화
cal.add(10) #add 함수에 인자 10이 val로 전달 
cal.minus(3)
print(cal.value)

#02
cal = MaxLimitCalculator()
cal.add(50)
cal.add(51)
print(cal.value)

#GPT01 
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def greet(self):
        print(f"{self.name}님은 {self.age}")


a = Person("ss",2321)
a.greet()

'''

num1 = 3
num2 = '2'



try:
    result = num1/int('일')
    print(f'연산결과는 {result}입니다')
except ZeroDivisionError as err:
    print('0으로 나눌 수 없습니다.')
except TypeError as err:
    print('숫자끼리 계산하세요')
except ValueError as err:
    print('숫자를 적으세요')
except:
    print('에러가 발생했습니다.')
else:
    print('정상 동작했습니다.')
finally:
    print('수행 종료')