from collections import deque

def solution(begin, target, words):
    answer = 0

    n = len(begin)
    checked = {}
    q = deque([begin])
    checked[begin] = 0
    while q:
        v = q.popleft()
        if v == target:
            answer = checked[v]
            break
        for w in words:
            cnt = 0
            for i in range(n):
                if v[i] != w[i]:
                    cnt += 1
                if cnt > 1:
                    break
            if cnt == 1 and w not in checked:
                q.append(w)
                checked[w] = checked[v] + 1
                
    return answer