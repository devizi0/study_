import copy
from collections import deque

def solution(storage, requests):
    space = []
    ans = 0
    total_cnt = 0
    for aa in storage:
        for bb in aa:
            total_cnt = total_cnt + 1
    
    ## INIT
    for x in storage:
        space.append(list(x))
    
    # 외부 공기에서 BFS로 해당 좌표까지 도달 가능한지 체크
    def is_accessible(space, y, x):
        n = len(space)
        m = len(space[0])
        # 패딩 포함한 방문 배열 (창고 주변에 가상의 외부 공간 추가)
        visited = [[False]*(m+2) for _ in range(n+2)]
        # (0,0)은 외부 공기 시작점
        q = deque([(0, 0)])
        visited[0][0] = True
        
        # 실제 좌표를 패딩 좌표로 변환
        target_y = y + 1
        target_x = x + 1
        
        while q:
            cy, cx = q.popleft()
            # 상하좌우 탐색
            for dy, dx in [(-1,0),(1,0),(0,-1),(0,1)]:
                ny, nx = cy+dy, cx+dx
                if 0 <= ny < n+2 and 0 <= nx < m+2 and not visited[ny][nx]:
                    # 목표 지점에 도달하면 가능.
                    if ny == target_y and nx == target_x:
                        return True
                    visited[ny][nx] = True
                    # 패딩 좌표를 실제 창고 좌표로 변환
                    gy, gx = ny-1, nx-1
                    # 패딩 영역이거나 빈 공간(True)이면 계속 탐색
                    if gy < 0 or gx < 0 or gy >= n or gx >= m:
                        q.append((ny, nx))  # 패딩 영역 = 외부 공기
                    elif space[gy][gx] == True:
                        q.append((ny, nx))  # 빈 공간 = 공기 통과 가능
        return False
        
    for x in requests: # 요청당
        space_copy = copy.deepcopy(space)
        god_mode = False #크레인인가여부
        request_cnt = 0 #요청당 카운트
        output_item = x[0] #꺼내고 싶은 아이템
        if len(x) > 1: 
            god_mode = True # 2자리면 크레인
            
        y_index = 0
        for y_line in space: # 줄만큼 실행 (Y)
            line_len = len(y_line)
            x_index = 0
            for x_line in range(0, line_len): # 줄에 있는 모든 아이템당. (X)
                if y_line[x_line] == True:  # 빈 공간은 Continue
                    x_index = x_index + 1
                    continue
                if y_line[x_line] == output_item: # 찾는거하고 같을때
                    # 크레인이면 무조건 꺼냄, 아니면 외부에서 접근 가능한지 BFS로 체크
                    if god_mode or is_accessible(space, y_index, x_index):
                        request_cnt = request_cnt + 1 
                        space_copy[y_index][x_index] = True
                x_index = x_index + 1
            y_index = y_index + 1
        
        #print("Request Processed. OK ")
        ans = ans + request_cnt
        space = space_copy
        #print(space)
    
    return total_cnt - ans