import json
import numpy as np

def sector(q,n):
    bath=(1<<n)-1;mask=(1<<q)-1;starts=[bath<<q,(bath<<q)|mask];states=set(starts);todo=starts[:]
    while todo:
        s=todo.pop();a=s&mask;b=s>>q
        moves=[]
        if a in (0,mask):moves.append(s^mask)
        for j in range(q):
            if ((s>>j)&1)!=((s>>(q+j))&1):moves.append(s^(1<<j)^(1<<(q+j)))
        for z in moves:
            if z not in states:states.add(z);todo.append(z)
    states=sorted(states);ix={s:i for i,s in enumerate(states)};H0=np.eye(len(states));V=np.zeros_like(H0)
    for s in states:
        a=s&mask;i=ix[s]
        if a in (0,mask):H0[i,i]=.5;H0[ix[s^mask],i]=-.5
        for j in range(q):
            f=(s>>j)&1;c=(s>>(q+j))&1
            if f!=c:
                between=(s>> (j+1))&((1<<(q-1))-1)
                sign=(-1)**between.bit_count();V[ix[s^(1<<j)^(1<<(q+j))],i]=sign
    return H0,V

def check():
    rows=[];q=6
    for n in range(q//2+1):
        H0,V=sector(q,n);count=sum(abs(np.linalg.eigvalsh(H0))<1e-13);assert count==(2 if n==0 else 1)
        pred4=q-q*q/4-3*(n-q/2)**2;prev=None
        for t in (.04,.025,.015):
            low=np.linalg.eigvalsh(H0+t*V)[:count];pred=-q*t*t/2+pred4*t**4;error=max(abs(low-pred))
            assert error<3000*t**6
            if prev is not None:assert error<prev
            prev=error;rows.append({'n':n,'sector_dimension':len(H0),'t':t,'exact_low':low.tolist(),'fourth_order':pred,'remainder_over_t6':float(error/t**6)})
    return rows
if __name__=='__main__':print(json.dumps(check(),indent=2))
