"""Independent physical charge/field construction; no source runner imported."""
from itertools import combinations
from collections import defaultdict
import numpy as np
import scipy.sparse as sp

L=8

def words(n=6):
    minus=(n-4)//2
    out=[]
    for occ in combinations(range(L),n):
        for neg in combinations(occ,minus):
            q=tuple(0 if i not in occ else (-1 if i in neg else 1) for i in range(L))
            out.append(q)
    return sorted(out)

def grade(q): return sum(q[i]==0 for i in range(0,L,2))

def offsets(q):
    accum=0; ret=[]
    for i,x in enumerate(q):
        accum+=x-int(i%2==0); ret.append(accum)
    assert accum==0
    return tuple(ret)

def hop_data(q):
    """(qout, df, link, shift, original field offset), excluding amplitude."""
    g=offsets(q)
    for e in range(L):
        j=(e+1)%L
        for a,b,direction in ((e,j,1),(j,e,-1)):
            if q[a] and not q[b]:
                c=q[a]; k=-direction*c
                qq=list(q); qq[a]=0; qq[b]=c
                yield tuple(qq), k if e==L-1 else 0, e,k,g[e]

def birth_data(q):
    g=offsets(q)
    for e in range(L):
        j=(e+1)%L
        if q[e]==q[j]==0:
            for c in (-1,1):
                qq=list(q); qq[e]=c; qq[j]=-c
                yield tuple(qq),c if e==L-1 else 0,e,c,g[e]

def weight(f,g,k,S):
    if S is None: return 1.
    e=f+g
    if abs(e)>S or abs(e+k)>S:return 0.
    return np.sqrt(max(0.,1-e*(e+k)/(S*(S+1))))

PWORDS=[q for q in words() if grade(q)==0]
PINDEX={q:i for i,q in enumerate(PWORDS)}

def h2_paths(q):
    for q1,d1,e1,k1,g1 in hop_data(q):
        assert grade(q1)==1
        for q2,d2,e2,k2,g2 in hop_data(q1):
            if grade(q2)==0:
                yield q2,d1+d2,(g1,k1),(d1+g2,k2)

def rotor_h2(theta):
    H=np.zeros((36,36),complex)
    for j,q in enumerate(PWORDS):
        for qq,d,_,_ in h2_paths(q):H[PINDEX[qq],j]-=np.exp(1j*d*theta)
    return H

def flat_basis(theta):
    """Analytic mode basis from independent wedge coordinates, 36 by 12."""
    pairs=list(combinations(range(4),2)); vectors=[]
    for j in range(6):
        phi=(4*theta+2*np.pi*j)/6
        for m in (0,1):
            n=m+2; km=(2*np.pi*m+np.pi+phi)/4; kn=(2*np.pi*n+np.pi+phi)/4
            v=[]
            for q in PWORDS:
                x,y=[i//2 for i in range(1,8,2) if q[i]]
                r=[q[i] for i in range(8) if q[i]].index(-1)
                a=(np.exp(1j*(km*x+kn*y))-np.exp(1j*(kn*x+km*y)))/4
                b=np.exp(1j*r*(phi-theta))/np.sqrt(6)
                v.append(a*b)
            vectors.append(v)
    return np.array(vectors).T

def flat_projector(theta):
    V=flat_basis(theta); return V@V.conj().T

def p_basis(S):
    ret=[]
    for q in PWORDS:
        g=offsets(q)
        for f in range(-S-min(g),S-max(g)+1):ret.append((q,f))
    return ret

def finite_operators(S,coherent=False):
    C=S*(S+1); p=p_basis(S); pidx={s:i for i,s in enumerate(p)}
    w1=[]; w2=[]
    for q in words():
        if grade(q) not in (1,2):continue
        g=offsets(q)
        for f in range(-S-min(g),S-max(g)+1):
            (w1 if grade(q)==1 else w2).append((q,f))
    def hopmat(src,dst):
        di={s:i for i,s in enumerate(dst)}; rr=[];cc=[];vv=[]
        for j,(q,f) in enumerate(src):
            for qq,d,e,k,g in hop_data(q):
                si=(qq,f+d)
                if si in di:
                    rr.append(di[si]);cc.append(j);vv.append(-weight(f,g,k,S))
        return sp.csc_matrix((vv,(rr,cc)),shape=(len(dst),len(src)))
    A=hopmat(p,w1); Q=hopmat(w1,w2); M=A.T@A; Z=Q@A
    H2=-M; H4=M@M-Z.T@Z/2
    n8=[]
    for q in words(8):
        g=offsets(q)
        for f in range(-S-min(g),S-max(g)+1):n8.append((q,f))
    ni={s:i for i,s in enumerate(n8)}
    rows=defaultdict(list);cols=defaultdict(list);vals=defaultdict(list)
    for j,(q,f) in enumerate(w1):
        for qq,d,e,c,g in birth_data(q):
            si=(qq,f+d)
            if si in ni:
                ch=e if coherent else (e,c)
                rows[ch].append(ni[si]);cols[ch].append(j);vals[ch].append(weight(f,g,c,S))
    jumps={ch:-(sp.csc_matrix((vals[ch],(rows[ch],cols[ch])),shape=(len(n8),len(w1)))@A) for ch in rows}
    loss=sum((B.T@B for B in jumps.values()),sp.csc_matrix(H2.shape))
    return p,n8,H2,H4,jumps,loss

def polynomial_h2_correction():
    """Map (out-index,in-index,flux change) -> [constant, linear, quadratic]."""
    ret=defaultdict(lambda:np.zeros(3,dtype=object))
    from fractions import Fraction
    for j,q in enumerate(PWORDS):
        for qq,d,(g,k),(h,l) in h2_paths(q):
            ret[PINDEX[qq],j,d]+=np.array([Fraction(g*(g+k)+h*(h+l),2),Fraction(2*g+k+2*h+l,2),1],dtype=object)
    return ret

if __name__=='__main__':
    print('word_counts',len(words()),len(PWORDS))
    for th in (0.,.37,1.2):
        V=flat_basis(th); H=rotor_h2(th)
        print('flat',th,np.linalg.norm(V.conj().T@V-np.eye(12)),np.linalg.norm((H+4*np.eye(36))@V))
