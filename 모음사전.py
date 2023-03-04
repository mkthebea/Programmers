def solution(word):
    answer = 0
    words = []
    al = ['A', 'E', 'I', 'O', 'U']
    for a in al:
        words.append(a)
        for b in al:
            words.append(a+b)
            for c in al:
                words.append(a+b+c)
                for d in al:
                    words.append(a+b+c+d)
                    for e in al:
                        words.append(a+b+c+d+e)
    answer = words.index(word) + 1                     
    return answer