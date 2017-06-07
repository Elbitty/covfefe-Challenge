"""
covfefe-Challenge:

    covfefe만으로 0~10까지 구하기.

    규칙:
        1. covfefe 이외의 변수는 사용할 수 없음.
        2. 인수에 정의된 "covfefe" 이외의 문자열은 사용할 수 없음.
        3. 대입 연산자 {=}, 비교 연산자 {== >= <=},
            산술 연산자 + - * / ** += -= *= /= 역시 금지.
        4. 모든 프로그래밍 언어가 허용됨.



    Find the solution of obtain numbers from 0 to 10 with only covfefe.

    Rules:
        1. Variables other than covfefe should NOT be used.
        2. Any string other than "covfefe" as defined in the argument should NOT be used.
        3. Assignment operator {=}, Comparison operators {{== >= <=},},
                Arithmetic operators { + - * / ** += -= *= /= } are also PROHIBITED.
        4. All kinds of programming languages are allowed.
"""

def covfefe_0(covfefe="covfefe"):
    return int(not covfefe)

def covfefe_1(covfefe="covfefe"):
    return int(not not covfefe)

def covfefe_2(covfefe="covfefe"):
    pass

def covfefe_6(covfefe="covfefe"):
    for covfefe in enumerate(covfefe):
        pass
    else:
        return covfefe[int(not covfefe)]

def covfefe_7(covfefe="covfefe"):
    return len(covfefe)


def covfefe_9(covfefe="covfefe"):
    return int(str(ord(list(covfefe)[int(not covfefe)]))[int(not covfefe)])


print(covfefe_1())
