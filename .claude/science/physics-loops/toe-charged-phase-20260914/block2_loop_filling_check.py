"""Exact integer-chain challenge of the bounded coordinate-walk filling."""
from collections import Counter
from itertools import product
from pathlib import Path
import json


def clean(c):
    return {k:v for k,v in c.items() if v}


def edge_chain(word,d):
    p=[0]*d;c=Counter();points=[tuple(p)]
    for axis,sg in word:
        anchor=p.copy()
        if sg<0:anchor[axis]-=1
        c[(tuple(anchor),axis)]+=sg;p[axis]+=sg;points.append(tuple(p))
    return clean(c),points


def fill(word,d):
    word=list(word);surface=Counter();swaps=0
    while True:
        changed=False;p=[0]*d
        for i in range(len(word)-1):
            a,sa=word[i];b,sb=word[i+1]
            if a>b:
                anchor=p.copy()
                if sa<0:anchor[a]-=1
                if sb<0:anchor[b]-=1
                surface[(tuple(anchor),b,a)]+=-sa*sb
                word[i],word[i+1]=word[i+1],word[i];swaps+=1;changed=True
            axis,sg=word[i];p[axis]+=sg
        if not changed:break
    return clean(surface),swaps,word


def boundary(surface,d):
    c=Counter()
    for (p,a,b),coeff in surface.items():
        pa=list(p);pa[a]+=1;pb=list(p);pb[b]+=1
        c[(p,a)]+=coeff;c[(tuple(pa),b)]+=coeff
        c[(tuple(pb),a)]-=coeff;c[(p,b)]-=coeff
    return clean(c)


out=[]
for d,lengths in [(2,[0,2,4,6,8]),(3,[2,4,6]),(4,[2,4,6])]:
    choices=[(i,s) for i in range(d) for s in [-1,1]]
    for n in lengths:
        count=0;maxarea=0;maxswaps=0
        for word in product(choices,repeat=n):
            if any(sum(s for a,s in word if a==i) for i in range(d)):continue
            count+=1;chain,points=edge_chain(word,d);surface,swaps,sortedword=fill(word,d)
            assert boundary(surface,d)==chain
            assert edge_chain(sortedword,d)[0]=={}
            area=sum(abs(x) for x in surface.values())
            assert area<=swaps<=n*(n-1)//2
            lo=[min(p[i] for p in points) for i in range(d)];hi=[max(p[i] for p in points) for i in range(d)]
            for (p,a,b),coeff in surface.items():
                assert all(lo[i]<=p[i] and p[i]+int(i in (a,b))<=hi[i] for i in range(d))
            if n<4:assert area==0
            maxarea=max(maxarea,area);maxswaps=max(maxswaps,swaps)
        out.append({'dimension':d,'length':n,'closed_words':count,'maximum_filling_l1':maxarea,'maximum_swaps':maxswaps,'stated_swap_bound':n*(n-1)//2})
        print(out[-1],flush=True)
# A length-L periodic winding closes only after taking residues. It must not
# enter the open-box filling family. Its unit constant-field circulation is L.
L=5;wind=[(0,1)]*L
assert edge_chain(wind,2)[1][-1]==(L,0)
assert L%L==0 and sum(s for a,s in wind if a==0)==L
Path(__file__).with_name('BLOCK2_LOOP_FILLING_CHECK.json').write_text(json.dumps(out,indent=2)+'\n')
