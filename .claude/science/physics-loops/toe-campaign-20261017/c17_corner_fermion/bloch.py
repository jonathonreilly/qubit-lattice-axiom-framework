"""Translation-invariant gauge for the corner model and 12x12 Bloch Hamiltonians."""
import itertools, numpy as np, sys
DIRS=[(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
def neg(d): return tuple(-x for x in d)
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def perp(d,e): return dot(d,e)==0 and d!=e
CORN=[frozenset((d,e)) for d,e in itertools.combinations(DIRS,2) if dot(d,e)==0]
CI={c:i for i,c in enumerate(CORN)}
# edge types: (c1, c2, shift) meaning corner c1 at cell 0 to corner c2 at cell shift
etypes=[]; ekey={}
def addt(c1,c2,sh,kind):
    k1=(c1,c2,sh); k2=(c2,c1,neg(sh))
    if k1 in ekey or k2 in ekey: return
    ekey[k1]=len(etypes); ekey[k2]=len(etypes); etypes.append((c1,c2,sh,kind))
Z=(0,0,0)
for c in CORN:
    d,e=tuple(c)
    for a,b in ((d,e),(e,d)):
        for f in DIRS:
            if perp(f,a) and perp(f,b) and f!=neg(b) and f!=neg(a):
                addt(c,frozenset((a,f)),Z,'onsite')
        addt(c,frozenset((neg(a),b)),a,'link')
nT=len(etypes); assert nT==36
def tid(c1,c2,sh): return ekey[(c1,c2,sh)]
def vadd(a,b): return tuple(x+y for x,y in zip(a,b))
def cyc(seq):
    # seq of (corner, cell); returns list of (type, orientation) hops
    out=[]
    for i in range(len(seq)):
        (c1,p1),(c2,p2)=seq[i],seq[(i+1)%len(seq)]
        sh=tuple(y-x for x,y in zip(p1,p2)); out.append(tid(c1,c2,sh))
    return out
cycles={'square':[],'triangle':[],'plaquette':[],'tube':[]}
for d in DIRS:
    a=[f for f in DIRS if perp(f,d) and f!=neg(d)]; a0=a[0]; b0=[f for f in a if perp(f,a0) and f!=neg(a0)][0]
    ring=[a0,b0,neg(a0),neg(b0)]
    cycles['square'].append(cyc([(frozenset((d,r)),Z) for r in ring]))
    for i in range(4):
        p,q=ring[i],ring[(i+1)%4]
        cycles['tube'].append(cyc([(frozenset((d,p)),Z),(frozenset((neg(d),p)),d),(frozenset((neg(d),q)),d),(frozenset((d,q)),Z)]))
for s in itertools.product((1,-1),repeat=3):
    x,y,z=(s[0],0,0),(0,s[1],0),(0,0,s[2])
    cycles['triangle'].append(cyc([(frozenset((x,y)),Z),(frozenset((y,z)),Z),(frozenset((z,x)),Z)]))
for d,e in (((1,0,0),(0,1,0)),((0,1,0),(0,0,1)),((0,0,1),(1,0,0))):
    cycles['plaquette'].append(cyc([(frozenset((d,e)),Z),(frozenset((neg(d),e)),d),(frozenset((neg(d),neg(e))),vadd(d,e)),(frozenset((d,neg(e))),e)]))
def solve(F):
    rows=[];rhs=[]
    for k,cs in cycles.items():
        for c in cs:
            r=0
            for t in c: r^=(1<<t)
            rows.append(r); rhs.append(F[k])
    piv={}
    for r,b in zip(rows,rhs):
        x=r|(b<<nT)
        while True:
            low=x&((1<<nT)-1)
            if low==0:
                if x: return None
                break
            c=low.bit_length()-1
            if c in piv: x^=piv[c]
            else: piv[c]=x; break
    sol=0
    for c in sorted(piv):
        x=piv[c]; rest=x&((1<<c)-1)
        if ((x>>nT)&1)^(bin(rest&sol).count('1')&1): sol|=(1<<c)
    return [ (sol>>j)&1 for j in range(nT)]
def bloch(u,k,t1,t2,lam,tri_orient):
    H=np.zeros((12,12),complex)
    for j,(c1,c2,sh,kind) in enumerate(etypes):
        t=t1 if kind=='onsite' else t2
        a=-t*(-1.0)**u[j]*np.exp(1j*np.dot(k,sh))
        i1,i2=CI[c1],CI[c2]
        H[i2,i1]+=a; H[i1,i2]+=np.conj(a)
    for (q,r) in tri_orient:
        j=ekey[(q,r,Z)]
        amp=1j*lam*(-1.0)**u[j]
        H[CI[r],CI[q]]+=amp; H[CI[q],CI[r]]+=np.conj(amp)
    return H
TRI=[]
for s in itertools.product((1,-1),repeat=3):
    x,y,z=(s[0],0,0),(0,s[1],0),(0,0,s[2])
    cy=[frozenset((x,y)),frozenset((y,z)),frozenset((z,x))]
    if round(np.linalg.det(np.array([x,y,z])))<0: cy=cy[::-1]
    for i in range(3): TRI.append((cy[i],cy[(i+1)%3]))
if __name__=='__main__':
    for F in itertools.product((0,1),repeat=4):
        Fd=dict(zip(('square','triangle','plaquette','tube'),F))
        print(Fd, 'translation-invariant gauge' if solve(Fd) is not None else 'needs larger cell')
