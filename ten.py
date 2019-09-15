#
import math

def pi(input):
    # 通过空格将字符串分隔符，把各个单词分隔为列表
    m1=1
    m2=math.pow(100, input['x']-1)
    print(m2)
    v1=1
    v2=-100.0
    n=0
    while v1>v2:
        d=m1*v1+m2*v2
        v1=d*2/(m1+m2)-v1
        v2=d*2/(m1+m2)-v2
        n+=1
        print('v1=',v1,'v2=',v2)
        if v1<0:
            v1=-v1
            n+=1
            print('v1=',v1)
        else:
            break
    return n
 
if __name__ == "__main__":
    input = {'x':5}
    n = pi(input)
    print('弹性碰撞+撞墙(次数)=pi=', n)
