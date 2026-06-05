
def giaiThua(n):
    if n ==0 or n == 1:
        return 1
    return n*giaiThua(n-1)

def tinhTong(n):
    if n==0:
        return 0
    return n+tinhTong(n-1)


if __name__ == "__main__":
    # print(giaiThua(25))
    print(tinhTong(5)) # 5+4+3+2+1
