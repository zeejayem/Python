from random import random

def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

def coinToss(n,p_H):
    coinTosses = ''
    for i in range(n):
        if random() <= p_H:
            coinTosses = coinTosses + 'H'
        else:
            coinTosses = coinTosses + 'T'
    return coinTosses

def main():
    tosses = [5, 10, 20, 50]
    probability = [0.5, 0.52, 0.55, 0.6]
    times = [1000, 10000, 100000]
    L=[]
    label=0
    accumProb=0
    mTotal=0

    outfileName = input("Name of the output file for results: ")
    outfile = open(outfileName, "w")

    print("This program simulates the tossing of a coin using random",file=outfile)
    print("on; 50%, 52%, 55% and 60% probabilities for heads with a",file=outfile)
    print("simulated weighted coin. We are tossing the coin 5, 10, 20",file=outfile)
    print("and 50 times, repeating the experiment for each value;",file=outfile)
    print(times[0],",",times[1],", and",times[2],"times the tosses for each probability.", file=outfile)
    print('',file=outfile)
    print('',file=outfile)
    print('{:*^50}'.format(" Start Full Simulation "),file=outfile)
    print('',file=outfile)

    for i in tosses:
        n = i
        for o in probability:
            p_H = o           
            for j in times:
                M = n*j
                print("Tosses =",n,"   Times",j," =",M, file=outfile)
                print("Probability used: {:.2%}".format(p_H), file=outfile)
                print('',file=outfile)
                
                for k in range(n+1):
                    L.append(0)                   
                for l in range(M):
                    result = coinToss(n,p_H)
                    AllTails = 'T'*n
                    D = histogram(result)
                    if result == AllTails:
                        L[0] += 1
                    else:
                        L[D['H']] += 1

                        
                for m in L:
                    P='Heads= '
                    P+=str(label)
                    label+=1
                    prob = m/M
                    accumProb += prob
                    mTotal += m
                    print('{0:^15}   Result:{1:<10}   Percentage:{2:<10.2%}'.format(P,m,prob), file=outfile)

                print('',file=outfile)
                print("{:-^50}".format(" CHECKSUMS "), file=outfile)
                print("Accumulated Probability:{:.2%}".format(accumProb), file=outfile)
                print("Total times counted:", mTotal,file=outfile)                               
                print('',file=outfile)
                print('*'*50,file=outfile)
                print('',file=outfile)
                print('',file=outfile)
                L=[]
                label=0
                accumProb=0
                mTotal=0

    outfile.close()
    print("Results have been sent to:",outfileName)
                

main()
