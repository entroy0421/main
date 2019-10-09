import random as R
def output(i,S,H,D,C):
    print('S ',end='')
    for x in range(13):
        if S[x][1]==i:print(S[x][0],end='',sep='')
    print()
    print('H ',end='')
    for x in range(13):
        if H[x][1]==i:print(H[x][0],end='',sep='')
    print()
    print('D ',end='')
    for x in range(13):
        if D[x][1]==i:print(D[x][0],end='',sep='')
    print()
    print('C ',end='')
    for x in range(13):
        if C[x][1]==i:print(C[x][0],end='',sep='')
    print()
def main():
    card=list('A23456789TJQK')
    area=['North:','East:','South:','West:']
    S=[[]for x in range(13)]
    H=[[]for x in range(13)]
    D=[[]for x in range(13)]
    C=[[]for x in range(13)]
    for i in range(13):
        S[i].append(card[i])
        S[i].append(R.randint(1,4))
        H[i].append(card[i])
        H[i].append(R.randint(1,4))
        D[i].append(card[i])
        D[i].append(R.randint(1,4))
        C[i].append(card[i])
        C[i].append(R.randint(1,4))
    for x in range(4):
        print(area[x])
        output(x+1,S,H,D,C)
if __name__=='__main__':main()