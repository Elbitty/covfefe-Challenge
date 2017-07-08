"""
covfefe-Challenge:
    Find the solution of obtain numbers from 0 to 10 with only covfefe.
    
    Rules:
         0. Code as much as possible to use covfefe.
         1. Variables other than covfefe should NOT be used.
         2. Any string other than "covfefe" should NOT be used.
         3. Assignment operator {=}, Comparison operators {== >= <=}, Arithmetic operators {+ - * / ** += -= *= /=} are also PROHIBITED.
         4. All kind of programming languages are allowed.


covfefe 챌린지
    covfefe만을 사용해 0~9(혹은 그 이상)까지 구해 봅시다.

    규칙:
         0. 최대한 covfefe 위주로 사용해 코딩할 것.
         1. covfefe 이외의 변수는 사용할 수 없음.
         2. "covfefe" 이외의 문자열은 사용할 수 없음.
         3. 대입 연산자 {=}, 비교 연산자 {== >= <=}, 산술 연산자 {+ - * / ** += -= *= /=} 역시 금지.
         4. 모든 프로그래밍 언어가 허용됨.

"""

def covfefe_0(covfefe="covfefe"):
    return int(not covfefe)

def covfefe_1(covfefe="covfefe"):
    return int(not not covfefe)

def covfefe_2(covfefe="covfefe"):
    return str(ord(str(ord(str(int(not covfefe))))[int(not covfefe)]))[int(not not covfefe)]

def covfefe_3(covfefe="covfefe"):
    return str(ord(str(ord(str(len(covfefe))[int(not covfefe)]))[int(not covfefe)]))[int(not not covfefe)]

def covfefe_4(covfefe="covfefe"):
    return str(ord(str(int(not covfefe))))[int(not covfefe)]

def covfefe_5(covfefe="covfefe"):
    return str(ord(str(len(covfefe))[int(not covfefe)]))[int(not covfefe)]

def covfefe_6(covfefe="covfefe"):
    return str(ord(str(ord(str(int(not covfefe))))[int(not not covfefe)]))[int(not not covfefe)]

def covfefe_7(covfefe="covfefe"):
    return len(covfefe)

def covfefe_8(covfefe="covfefe"):
    return str(ord(str(int(not covfefe))))[int(not not covfefe)]

def covfefe_9(covfefe="covfefe"):
    return str(ord(list(covfefe)[int(not covfefe)]))[int(not covfefe)]


print(covfefe_0())
print(covfefe_1())
print(covfefe_2())
print(covfefe_3())
print(covfefe_4())
print(covfefe_5())
print(covfefe_6())
print(covfefe_7())
print(covfefe_8())
print(covfefe_9())
