def solution(n, w, num):
    space = []
    ### 공간 생성하기
    cnt = 1
    line = 0
    dir = True # R
    temp = []
    q=0
    if n%w >0:
        q=1
    for y in range(0,((int(n/w)+q))): # 각 줄마다 실행
        #print(y)
        tmp = 0
        for _ in range (0,w): # 임시배열 리셋
            temp.append(None) # 초기화 None으로
        for x in range(0,w):
            if(cnt>n):
                break;
            if dir is not True:
                x= w-x-1
            temp[x] = cnt
            cnt += 1 #카운트 올리고
            
        dir = not dir #한줄끝나면 방향 바꾸고
        line += 1 #한줄 올리고
        space.append(temp)
        temp = []
    idx = -1
    ans = 0
    for Line in space:
        #print(qq)
        index_count = 0
        for x in Line:
            if (x==num):
                #print("a")
                idx = index_count
            if (index_count == idx) and (x is not None):
                ans+=1
            index_count +=1
    return ans
