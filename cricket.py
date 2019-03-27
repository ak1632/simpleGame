import random
score1=0
score2=0
player1=str(input('enter team1 '))
player2=str(input('enter team2 '))
player1.upper()
player2.upper()
print('TOSS TIME.\nWho is gonna call for the toss? ')
tcall=str(input())
if tcall==player1:
    tcall==tcall
    toss=str(input('CALL HEADS or TAILS...(1/0) '))
else:
    tcall==player2
    tcall==tcall
    toss=str(input('Call HEADS or TAILS....  (1/0) '))
t=random.randint(0,1)
if t==toss:
    print(tcall,' WON THE TOSS')
    tchoice=str(input('WHAT YOU WANNA CHOOSE.... BAT OR BOWL? '))
    if tchoice=='BAT':
        l=[]
        while True:
            a=random.randint(1,6)
            run1=int(input())
            l.append(run1)
            score1=score1+run1
            if a==run1:
                scorecard1=(score1-l[-1])
                print(scorecard1)
                break
            else:
                continue
        m=[]
        while True:
            target=scorecard1+1
            b=random.randint(1,6)
            run2=int(input())
            m.append(run2)
            score2=score2+run2
            target=target-score2
            if b==run2:
                scorecard2=(score2-m[-1])
                print(scorecard2)
                break
            else:
                continue
           
    else:
        tchoice=='BOWL'
        m=[]
        while True:
            b=random.randint(1,6)
            run2=int(input())
            m.append(run2)
            score2=score2+run2
            if b==run2:
                scorecard2=(score2-m[-1])
                print(scorecard2)
                break
            else:
                continue
        l=[]
        while True:
            target=scorecard2+1
            a=random.randint(1,6)
            run1=int(input())
            l.append(run1)
            score1=score1+run1
            target=target-score1
            if score1>socre2:
                print('TEAM BATTING SECOND WINS')
                break
            else:
                continue
            if a==run1:
                scorecard1=(score1-l[-1])
                print(scorecard1)
                break
            else:
                continue
           
        
    
else:
    print(tcall,' LOST THE TOSS')
    print('******************  ****************  *************')
    tchoice=str(input('WHAT YOU WANNA CHOOSE.... BAT OR BOWL? '))
    if tchoice=='BAT':
        m=[]
        while True:
            b=random.randint(1,6)
            run2=int(input())
            m.append(run2)
            score2=score2+run2
            if b==run2:
                scorecard2=(score2-m[-1])
                print(scorecard2)
                break
            else:
                continue
        l=[]
        while True:
            target=scorecard2+1
            a=random.randint(1,6)
            run1=int(input())
            l.append(run1)
            score1=score1+run1
            target=target-score1
            if a==run1:
                scorecard1=(score1-l[-1])
                print(scorecard1)
                break
            else:
                continue
    else:
        tchoice=='BOWL'
        l=[]
        while True:
            a=random.randint(1,6)
            run1=int(input())
            l.append(run1)
            score1=score1+run1
            if a==run1:
                scorecard1=(score1-l[-1])
                print(scorecard1)
                break
            else:
                continue
        m=[]
        while True:
            target=scorecard1+1
            b=random.randint(1,6)
            run2=int(input())
            m.append(run2)
            score2=score2+run2
            target=target-score2
            if b==run2:
                scorecard2=(score2-m[-1])
                print(scorecard2)
                break
            else:
                continue
            

if target<0:
    print('TEAM BATTING SECOND WINS')
elif scorecard1==scorecard2:
    print('MATCH TIED')
else:
    scorecard1>scorecard2
    print('TEAM BATTING FIRST WINS')


    







