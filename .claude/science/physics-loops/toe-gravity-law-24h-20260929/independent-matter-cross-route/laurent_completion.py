#!/usr/bin/env python3
"""Exact Q(i) Laurent/Pauli proof for the actual block136 walker CC defect.

No sampled Fourier grid, symbolic CAS, torus, imported source runner, or float.
Keys: (nine exponents x=N,y=M,z=ket, Pauli index, imaginary bit).
The output coupling is K*A (hence independent of the supplied nonzero K).
"""
from fractions import Fraction as F
from itertools import permutations, product
from collections import defaultdict
from pathlib import Path
import json, time, resource, hashlib

HERE=Path(__file__).resolve().parent
ZERO=(0,)*9
def clean(d): return {k:v for k,v in d.items() if v}
def add(*ps):
    d=defaultdict(F)
    for p in ps:
        for k,v in p.items(): d[k]+=v
    return clean(d)
def scale(p,c): return clean({k:v*c for k,v in p.items()})
def mono(exp=None,c=1,s=0,i=0): return {(tuple(exp or ZERO),s,i):F(c)} if c else {}
ONE=mono()
def shift(p,ex): return {(tuple(a+b for a,b in zip(k[0],ex)),k[1],k[2]):v for k,v in p.items()}
def imag(p): return {(e,s,1-i):v*(-1 if i else 1) for (e,s,i),v in p.items()}
def mul(p,q):
    d=defaultdict(F)
    for (a,s,i),v in p.items():
        for (b,t,j),w in q.items():
            sign=1; u=s or t; n=i+j
            if s and t:
                if s==t: u=0
                else:
                    u=6-s-t; n+=1
                    if (s,t,u) not in [(1,2,3),(2,3,1),(3,1,2)]: sign=-1
            if n//2%2: sign=-sign
            d[(tuple(x+y for x,y in zip(a,b)),u,n%2)]+=v*w*sign
    return clean(d)
def X(j):
    e=[0]*9;e[j]=1
    return mono(e)
def invX(j):
    e=[0]*9;e[j]=-1
    return mono(e)
def cos(j): return scale(add(X(j),invX(j)),F(1,2))
def sin(j): return scale(imag(add(X(j),scale(invX(j),-1))),F(-1,2))
def substitute(p,mat):
    d=defaultdict(F)
    for (e,s,i),v in p.items():
        a=tuple(sum(e[j]*mat[j][k] for j in range(9)) for k in range(9))
        d[(a,s,i)]+=v
    return clean(d)
def matrix_identity(): return [[int(i==j) for j in range(9)] for i in range(9)]
def momentum_shift(p,groups):
    mat=matrix_identity()
    for j in range(3):
        for g in groups: mat[6+j][g+j]+=1
    return substitute(p,mat)
def swap(p):
    return {(e[3:6]+e[:3]+e[6:],s,i):v for (e,s,i),v in p.items()}
def eval_group(p,group):
    d=defaultdict(F)
    for (e,s,i),v in p.items():
        a=list(e)
        for j in group: a[j]=0
        d[(tuple(a),s,i)]+=v
    return clean(d)
def first_jet(p,group):
    base=eval_group(p,group);ans=base
    for j in group:
        deriv=eval_group({k:v*k[0][j] for k,v in p.items()},group)
        ans=add(ans,mul(add(X(j),scale(ONE,-1)),deriv))
    return ans
def aug_quotients(p,group):
    """f-f(1)=sum_j (x_j-1) q_j, by ordered telescoping."""
    qs=[]
    for pos,j in enumerate(group):
        d=defaultdict(F)
        for (e,s,i),v in p.items():
            n=e[j];a=list(e)
            for prev in group[:pos]:a[prev]=0
            rr=range(n) if n>0 else range(n,0)
            for t in rr:
                a[j]=t;d[(tuple(a),s,i)]+=v*(1 if n>0 else -1)
        qs.append(clean(d))
    return qs
def second_remainder(p,group):
    """f-T1f=sum_(i<=j) (x_i-1)(x_j-1) q_ij."""
    out=defaultdict(dict)
    for i,qi in zip(group,aug_quotients(p,group)):
        for j,qij in zip(group,aug_quotients(qi,group)):
            k=tuple(sorted((i,j)));out[k]=add(out[k],qij)
    rec={}
    for (i,j),q in out.items():rec=add(rec,mul(mul(add(X(i),scale(ONE,-1)),add(X(j),scale(ONE,-1))),q))
    assert rec==add(p,scale(first_jet(p,group),-1))
    return dict(out)
def to_r(qs,offset):
    """r_ii=sum_(j!=i) d_j, d_j=2-x_j-x_j^-1; r_ij=2(1-x_i)(1-x_j)."""
    ans=[{} for _ in range(6)]; pairs=[(0,1),(0,2),(1,2)]
    for (a,b),q in qs.items():
        i,j=a-offset,b-offset
        if i!=j: ans[3+pairs.index((i,j))]=add(ans[3+pairs.index((i,j))],scale(q,F(1,2)))
        else:
            # (x_i-1)^2=-x_i*d_i=-x_i*(r_jj+r_kk-r_ii)/2.
            q=mul(X(a),scale(q,F(1,2)))
            for k in range(3):ans[k]=add(ans[k],scale(q,1 if k==i else -1))
    return ans
def rs(offset):
    ds=[add(scale(ONE,2),scale(X(offset+j),-1),scale(invX(offset+j),-1)) for j in range(3)]
    return [add(*(ds[j] for j in range(3) if j!=i)) for i in range(3)]+[scale(mul(add(ONE,scale(X(offset+i),-1)),add(ONE,scale(X(offset+j),-1))),2) for i,j in [(0,1),(0,2),(1,2)]]
def cc(A):
    return add(*(add(mul(r,a),scale(mul(s,swap(a)),-1)) for r,s,a in zip(rs(0),rs(3),A)))
def adjoint(p):
    d=defaultdict(F)
    for (e,s,i),v in p.items():
        a,b,c=e[:3],e[3:6],e[6:]
        ee=tuple(a[j]-c[j] for j in range(3))+tuple(b[j]-c[j] for j in range(3))+tuple(-t for t in c)
        d[(ee,s,i)]+=v*(-1 if i else 1)
    return clean(d)
def hermitian(p):return scale(add(p,adjoint(p)),F(1,2))
def tr_odd(p):
    # Antiunitary spin1/2 time reversal conjugates i and reverses every sigma.
    return {k:v for k,v in p.items() if (-1 if k[2] else 1)*(-1 if k[1] else 1)==-1}
def physical_kernel(e):
    a,b,c=e[:3],e[3:6],e[6:]
    return tuple(b[j]-a[j] for j in range(3)),tuple(-t for t in a),tuple(c[j]-a[j] for j in range(3))
def from_kernel(l,u,v):return tuple(-t for t in u)+tuple(l[j]-u[j] for j in range(3))+tuple(v[j]-u[j] for j in range(3))
def rotations():
    for perm in permutations(range(3)):
        parity=(-1)**sum(perm[i]>perm[j] for i in range(3) for j in range(i+1,3))
        for signs in product([-1,1],repeat=3):
            if parity*signs[0]*signs[1]*signs[2]==1:yield perm,signs
def rotate(A,rot):
    perm,signs=rot;pairs=[(0,1),(0,2),(1,2)];out=[defaultdict(F) for _ in A]
    def rv(v):
        a=[0]*3
        for j in range(3):a[perm[j]]=signs[j]*v[j]
        return a
    for t,p in enumerate(A):
        base=[0]*3;tsign=1
        if t<3:tt=perm[t]
        else:
            i,j=pairs[t-3];tt=3+pairs.index(tuple(sorted((perm[i],perm[j]))));tsign=signs[i]*signs[j]
            for a in [i,j]:
                if signs[a]<0:base[perm[a]]=-1
        for (e,s,i),v in p.items():
            loc=[]
            for a in physical_kernel(e):loc.append(tuple(k-b for k,b in zip(rv(a),base)))
            ss=perm[s-1]+1 if s else 0;sgn=signs[s-1] if s else 1
            out[tt][(from_kernel(*loc),ss,i)]+=v*tsign*sgn
    return [clean(p) for p in out]
def save_polys(name,ps):
    data=[[[list(e),s,i,str(v)] for (e,s,i),v in sorted(p.items())] for p in ps]
    f=HERE/name;f.write_text(json.dumps(data,separators=(',',':'))+'\n')
    return hashlib.sha256(f.read_bytes()).hexdigest()
def main():
    start=time.monotonic();stats={}
    H=add(*(mul(mono(s=j+1),sin(6+j)) for j in range(3)))
    c=mul(mul(cos(0),cos(1)),cos(2))
    E=scale(mul(c,add(H,momentum_shift(H,[0]))),F(1,2));Em=swap(E)
    Xcomm=scale(imag(add(mul(momentum_shift(E,[3]),Em),scale(mul(momentum_shift(Em,[0]),E),-1))),-1)
    B=[]
    for j in range(3):
        P=mul(sin(6+j),cos(6+j))
        phi=scale(add(ONE,invX(j)),F(1,2))
        for k in range(3):
            if k!=j:phi=mul(phi,cos(k))
        Pdd=scale(mul(phi,add(P,momentum_shift(P,[0]))),F(1,2))
        ez=[0]*9;ez[j]=-1;ez[6+j]=-1
        factor=add(mono(ez),X(6+j))
        coin=scale(mul(mul(c,factor),add(mul(mono(s=j+1),H),mul(momentum_shift(H,[0]),mono(s=j+1)))),F(1,4))
        bj=scale(add(Pdd,coin),F(1,2))
        mat=matrix_identity()
        for k in range(3):mat[k][3+k]=1
        B.append(substitute(bj,mat))
    Jold=add(*(mul(add(X(j),scale(X(3+j),-1)),B[j]) for j in range(3)))
    D=add(Xcomm,scale(Jold,-1))
    assert swap(D)==scale(D,-1)
    assert adjoint(D)==D
    stats['terms']={'energy':len(E),'commutator':len(Xcomm),'current':len(Jold),'defect':len(D)}
    normal=first_jet(first_jet(D,range(3)),range(3,6))
    stats['normal_remainder_terms']=len(normal)
    save_polys('defect.json',[D]);save_polys('normal_remainder.json',[normal])
    print(json.dumps(stats),flush=True)
    assert not normal, 'Curvature ideal obstruction'
    f=to_r(second_remainder(D,range(3)),0)
    g=to_r(second_remainder(first_jet(D,range(3)),range(3,6)),3)
    assert add(*(mul(r,a) for r,a in zip(rs(0),f)),*(mul(r,a) for r,a in zip(rs(3),g)))==D
    A=[scale(add(a,scale(swap(b),-1)),F(1,2)) for a,b in zip(f,g)]
    assert cc(A)==D
    stats['raw_A_terms']=[len(a) for a in A]
    A=[tr_odd(hermitian(a)) for a in A]
    assert cc(A)==D
    stats['hermitian_A_terms']=[len(a) for a in A]
    print(json.dumps(stats),flush=True)
    # Covariance first tests one generator of each rotation type before averaging.
    for rot in [((1,0,2),(1,-1,1)),((1,2,0),(1,1,1))]:
        assert cc(rotate(A,rot))==D, 'Actual placement fails cubic covariance'
    Asym=[{} for _ in A]
    for rot in rotations():Asym=[add(a,b) for a,b in zip(Asym,rotate(A,rot))]
    A=[scale(a,F(1,24)) for a in Asym]
    assert cc(A)==D
    assert all(adjoint(a)==a and tr_odd(a)==a for a in A)
    for rot in rotations():assert rotate(A,rot)==A
    stats['cubic_A_terms']=[len(a) for a in A]
    stats['coupling_sha256']=save_polys('coupling_KA.json',A)
    radius=0;rad_each=[]
    for t,p in enumerate(A):
        center=[0,0,0]
        if t>=3:
            i,j=[(0,1),(0,2),(1,2)][t-3];center[i]=center[j]=1
        rad=max((abs(2*a[j]-center[j]) for e,s,i in p for a in physical_kernel(e) for j in range(3)),default=0)
        rad_each.append(str(F(rad,2)));radius=max(radius,rad)
    stats['radius_from_P_center']=str(F(radius,2));stats['component_radii']=rad_each
    # The literal +P matter generator with canonical +F has an uncancellable first jet.
    wrong=add(Xcomm,Jold)
    wrongnormal=first_jet(first_jet(wrong,range(3)),range(3,6))
    stats['literal_plus_J_normal_terms']=len(wrongnormal)
    save_polys('literal_plus_J_normal.json',[wrongnormal])
    stats['elapsed_s']=time.monotonic()-start;stats['maxrss_bytes']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    (HERE/'results.json').write_text(json.dumps(stats,indent=2)+'\n')
    print(json.dumps(stats,indent=2),flush=True)
if __name__=='__main__':main()
