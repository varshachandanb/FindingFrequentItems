import itertools
import sys


def pcy_algo(baskets):
        bucket_map={}
        bitmap={}
        cand_pairs={}
        freq_pairs={}
        tmp_freq={}
        all_pairs={}
        #support=3
        #hash_len=20
        support=int(sys.argv[2])
        hash_len=int(sys.argv[3])
        #with open("otpt.txt","w") as otpt:
        for x in range(1,len(baskets)+1):
            for y in range(1,len(baskets[x])+1):
                if y not in all_pairs:
                    all_pairs[y]=[]
                items=(list(itertools.combinations(sorted(baskets[x]),y)))
                for val in items:
                    all_pairs[y].append(val)
                all_pairs[y]=sorted(all_pairs[y])        
        for p in range(1,len(set(all_pairs[1]))+1):
            cand_pairs[p]=[]
            freq_pairs[p]=[]
            tmp_freq[p]=[]
            len_bucket_map={}
            empty_bkt=0
            for i in range(0,hash_len):
                bucket_map[i]=[]
                len_bucket_map[i]={}
                bitmap[i]=0

            if(p>=2):
                for val in all_pairs[p]:
                    hsh=0
                    for q in range(0,p):
                        hsh=hsh+int(hash_val[val[q]])
                    map=bucket_map[hsh%hash_len]
                    map.append(val)
                for key in bucket_map:
                    len_bucket_map[p][key]=len(bucket_map[key])
                    if(len(bucket_map[key])>=support):
                        bitmap[key]=1
                        lst=set(bucket_map[key])
                        for j in lst:
                            cand_pairs[p].append(j)
                cand_pairs[p]=sorted(cand_pairs[p])
                for data in cand_pairs[p]:
                    if(all_pairs[p].count(data)>=support):
                        items=(list(itertools.combinations(sorted(data),p-1)))
                        ct=0
                        for m in range(0,len(items)):
                            if(p==2):
                                if(items[m][0] in freq_pairs[p-1]):
                                    ct=ct+1
                            else:
                                if(items[m] in freq_pairs[p-1]):
                                    ct=ct+1
                        if(ct==p):
                            freq_pairs[p].append(data)
                for t in freq_pairs[p]:
                    tmp_freq[p].append(list(t))

                if(p==2):
                    #sys.stdout.write()
                    print "memory for hash table counts for size %s itemsets: %s " %(str(p),str(hash_len*4))
                    print(str(len_bucket_map[p]))
                    print("frequent itemsets of size "+str(p-1)+" : "+str(freq_pairs[p-1])+'\n')
                    if(len(freq_pairs[p])==0):
                        break
                    print("memory for frequent itemsets of size "+str(p-1)+" : "+str(len(freq_pairs[p-1])*8))
                    print("bitmap size:"+str(hash_len))
                    print("memory for candidates counts of size "+str(p)+" : "+str(len(cand_pairs[p])*4))
                    print("frequent itemsets of size "+str(p)+" : "+str(tmp_freq[p])+'\n')
                if(len(freq_pairs[p])==0):
                        break
                if(p!=2 ):
                    print("memory for frequent itemsets of size "+str(p-1)+" : "+str(len(freq_pairs[p-1])*(4*p)))
                    print("memory for hash table counts for size "+str(p)+" itemsets: "+str(hash_len*4))
                    print(str(len_bucket_map[p])+'\n')
                    print("bitmap size:"+str(hash_len))
                    print("memory for candidates counts of size "+str(p)+" : "+str(len(cand_pairs[p])*4))
                    print("frequent itemsets of size "+str(p)+" : "+str(tmp_freq[p])+'\n')

                

            else:
                mem_items=len(set(all_pairs[1]))*8
                print("memory for item counts: "+str(mem_items))
                for val in all_pairs[p]:
                    if(all_pairs[p].count(val)>=support):
                        #freq_pairs[p].append(val)
                        #for no commas
                        freq_pairs[p].append(val[0])
                freq_pairs[p]=set(freq_pairs[p])
                freq_pairs[p]=sorted(freq_pairs[p])
        #otpt.close()


if __name__ == '__main__':
    item_set={}
    baskets={}
    hash_val={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}
    #with open("input2.txt","r") as inpt:
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
    inpt.close()
    pcy_algo(baskets)

