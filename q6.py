def solution(N, stages):
    failure = {}
    players = len(stages)
    for i in range(1,N+1):
        if players != 0:
            fail = stages.count(i)
            failure[i] = fail / players
            players -= fail
        else:
            failure[i] = 0
    return sorted(failure, key=lambda x: failure[x], reverse=True)

N = 4
stages = [4,4,4,4,4]
answer = solution(N, stages)
print(answer)
