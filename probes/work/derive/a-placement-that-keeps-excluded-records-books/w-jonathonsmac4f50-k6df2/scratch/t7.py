from engine import *
import itertools, time
t0=time.time()
pairs=[(0,1),(0,2),(1,2)]
Ws={S:Walk(2,3,S) for S in [(),((0,1),),((0,2),),((1,2),),((0,1),(0,2),(1,2))]}
full=Ws[((0,1),(0,2),(1,2))]
def O(S,v,comp): return Ws[S].O16(v,comp)
# 1) cluster factorisation: adjacent pair + far third
st=(((0,0),0),((1,0),1),((20,0),0))
for comp in (0,1):
    o=O(((0,1),(0,2),(1,2)),{st:(1,0)},comp)
    o01=O(((0,1),),{st:(1,0)},comp)
    # pair-only 2-record result times spectator at (20,0),0 : only states with spectator unchanged?  compare directly
    diff=vsum(o,vscale(o01,(-1,0)))
    print("far third: full - pair01-only is zero:",len(diff)==0,"nonzero full:",len(o)>0)
# 2) connected three-body part C = O_full - sum_pairs O_pair on 3-record clusters
cnt=0; tot=0; examples=[]
import random
random.seed(2)
sites=[(0,0),(1,0),(0,1),(1,1),(2,0),(0,2),(-1,0),(2,1)]
for trip in itertools.permutations(sites,3):
    if not (trip[0]<trip[1]<trip[2]): continue
    for cs in itertools.product(range(2),repeat=3):
        st=tuple((trip[i],cs[i]) for i in range(3))
        for comp in (0,):
            tot+=1
            of=O(((0,1),(0,2),(1,2)),{st:(1,0)},comp)
            s=vsum(O(((0,1),),{st:(1,0)},comp),O(((0,2),),{st:(1,0)},comp),O(((1,2),),{st:(1,0)},comp))
            C=vsum(of,vscale(s,(-1,0)))
            if C:
                cnt+=1
                if len(examples)<3: examples.append((st,len(C)))
print("connected 3-body part nonzero on",cnt,"of",tot,"cluster basis states; examples",examples, time.time()-t0)
# 3) is connected part supported only when all three are within range?  test a chain 0-1-2 far apart (gaps) 
for gap in range(1,8):
    st=(((0,0),0),((gap,0),0),((2*gap,0),1))
    of=O(((0,1),(0,2),(1,2)),{st:(1,0)},0)
    s=vsum(O(((0,1),),{st:(1,0)},0),O(((0,2),),{st:(1,0)},0),O(((1,2),),{st:(1,0)},0))
    C=vsum(of,vscale(s,(-1,0)))
    print("gap",gap,"connected part nonzero:",len(C)>0)
