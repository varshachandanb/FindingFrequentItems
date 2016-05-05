import itertools
import random
import sys


all_pairs={}

def find_all_freq_pairs(baskets):
    global all_pairs
    all_pairs={}
    max=1
    for m in range(1,len(baskets)+1):
        if(len(baskets[m])>max):
            max=len(baskets[m])
    for n in range(1,max+1):
        all_pairs[n]=[]
    for x in range(1,len(baskets)+1):
        for y in range(1,len(baskets[x])+1):
            items=(list(itertools.combinations(sorted(baskets[x]),y)))
            for val in items:
                if(y==1):
                    all_pairs[y].append(val[0])
                else:
                    all_pairs[y].append(val)
            all_pairs[y]=sorted(all_pairs[y])
    return all_pairs

def toivonen_algo(baskets):
        global rs_freq_pairs
        global support
        global all_pairs
        global iteration
        global repeat
        global rs_support
        global max_comb
        repeat=0
        iteration=iteration+1
        global rs_freq_pairs
        rs_all_pairs={}
        threshold=fraction*len(baskets)
        rs_freq_pairs={}
        rs_freq_pairs[1]=[]
        rs_temp_freq_pairs={}
        rs_temp_freq_pairs[1]=[]
        rs_temp_all_pairs={}
        rs_temp_all_pairs[1]=[]
        neg_border={}
        poss_neg_border={}
        poss_neg_border[1]=[]
        neg_border[1]=[]
        rs_distinct_pairs={}
        max=1
        randm_num=[]
        negative=0
        for m in range(1,len(baskets)+1):
            if(len(baskets[m])>max):
                max=len(baskets[m])

        for s in range(1,int(threshold)+1):
            num=(random.randint(1,len(baskets)))
            while(num in randm_num):
                num=(random.randint(1,len(baskets)))
            randm_num.append(num)

        for n in range(1,max+1):
            rs_all_pairs[n]=[]

        for x in range(1,int(threshold)+1):
                for y in range(1,len(baskets[randm_num[x-1]])+1):
                    #rs_all_pairs[y].append(list(set(itertools.combinations(sorted(baskets[randm_num[x-1]]),y))))
                    items=(list(itertools.combinations(sorted(baskets[randm_num[x-1]]),y)))
                    for val in items:
                        if(y==1):
                            rs_all_pairs[y].append(val[0])
                        else:
                            rs_all_pairs[y].append(val)
        rs_distinct_pairs[1]=list(set(rs_all_pairs[1]))
        for m in range(0,len(rs_distinct_pairs[1])):
            if(rs_all_pairs[1].count(rs_distinct_pairs[1][m])>=rs_support):
                rs_temp_freq_pairs[1].append(rs_distinct_pairs[1][m])
            else:
                poss_neg_border[1].append(rs_distinct_pairs[1][m])

        for n in range(len(poss_neg_border[1])):
            if(all_pairs[1].count(poss_neg_border[1][n])>=support):
                neg_border[1].append(poss_neg_border[1][n])
                negative=1
                return negative

        if(negative==0):
            for x in range(len(rs_temp_freq_pairs[1])):
                if(all_pairs[1].count(rs_temp_freq_pairs[1][x])>=support):
                     rs_freq_pairs[1].append(rs_temp_freq_pairs[1][x])


        for y in range(2,max+1):
            rs_temp_all_pairs[y]=[]
            rs_distinct_pairs[y]=[]
            items=(list(itertools.combinations(sorted(rs_freq_pairs[1]),y)))
            for val in items:
                rs_temp_all_pairs[y].append(val)
            rs_distinct_pairs[y]=list(set(sorted(rs_temp_all_pairs[y])))
        negative=0
        stop=0
        present=0
        temp={}
        for p in range(2,max+1):
            negative=0
            present=0
            neg_border[p]=[]
            rs_temp_freq_pairs[p]=[]
            rs_freq_pairs[p]=[]
            poss_neg_border[p]=[]

            if(p==2):
                for val in rs_distinct_pairs[p]:
                    if(rs_all_pairs[p].count(val)>=rs_support):
                        rs_temp_freq_pairs[p].append(val)
                    else:
                        poss_neg_border[p].append(val)

                for x in range(len(poss_neg_border[p])):
                    if(all_pairs[p].count(poss_neg_border[p][x])>=support):
                        neg_border[p].append(poss_neg_border[p][x])
                        negative=1
                        return negative
                if(negative==0):
                    for y in range(len(rs_temp_freq_pairs[p])):
                        if(all_pairs[p].count(rs_temp_freq_pairs[p][y])>=support):
                            present=1
                            max_comb=p
                            rs_freq_pairs[p].append(rs_temp_freq_pairs[p][y])
                if(present==0):
                    del rs_freq_pairs[p]

            if(p>2):
                temp[p]=[]
                if(stop==0):
                    for val in rs_distinct_pairs[p]:
                        items=(list(itertools.combinations(sorted(val),p-1)))
                        ct=0
                        for data in items:
                            if(rs_all_pairs[p-1].count(data)>=rs_support):
                                ct=ct+1
                        if(ct==p):
                            temp[p].append(val)

                    for dt in range(len(temp[p])):
                        if(rs_all_pairs[p].count(dt)>=support):
                            rs_temp_freq_pairs[p].append(dt)
                        else:
                            poss_neg_border[p].append(dt)

                    for vl in poss_neg_border[p]:
                        if(all_pairs[p].count(vl)>=support):
                            negative=1
                            return negative
                    if(negative==0):
                        for y in range(len(rs_temp_freq_pairs[p])):
                            if(all_pairs[p].count(rs_temp_freq_pairs[p][y])>=support):
                                present=1
                                max_comb=p
                                rs_freq_pairs[p].append(rs_temp_freq_pairs[p][y])
                    if(present==0):
                        del rs_freq_pairs[p]
                        stop=1


if __name__ == '__main__':
    item_set={}
    baskets={}
    hash_val={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}

    with open(sys.argv[1],"r") as inpt:
        lines=inpt.readlines()
        bkt=1
        for line in lines:
            line=line.rstrip('\n')
            items=line.split(',')
            baskets[bkt]=[]
            for val in items:
                baskets[bkt].append(val)
            bkt=bkt+1
    max_comb=0
    support=int(sys.argv[2])
    fraction=0.5
    rs_support=support*fraction*0.8
    iteration=0
    repeat=0
    rs_freq_pairs={}
    temp={}
    inpt.close()
    all_pairs=find_all_freq_pairs(baskets)
    repeat=toivonen_algo(baskets)
    if(repeat==1):
        toivonen_algo(baskets)

    print iteration
    print fraction
    for i in range(1,max_comb+1):
        temp[i]=[]
        for val in rs_freq_pairs[i]:
            temp[i].append(list(val))
    for x in range(1,len(temp)+1):
        print sorted(temp[x])



