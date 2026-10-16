"""Exact binomial Gram construction and algebraic pole certificate, no imports of other checks."""
from pathlib import Path
import itertools,json,math,platform,sys
import numpy as np
import sympy as sp
OUT=Path(sys.argv[1]).resolve();N=6;dim=1<<N

def bit(x,j):return (x>>(N-1-j))&1
patterns=[()]
for r in (1,2):
    for sites in itertools.combinations(range(N),r):
        for units in itertools.product(((1,1),(0,1),(1,0)),repeat=r):
            patterns.append(tuple((j,a,b) for j,(a,b) in zip(sites,units)))
raw=np.zeros((dim,len(patterns)*(N+1)),dtype=np.int64)
for i,A in enumerate(patterns):
    for x in range(dim):
        if not all(bit(x,j)==b for j,a,b in A):continue
        y=x
        for j,a,b in A:
            if a!=b:y^=1<<(N-1-j)
        raw[y,i*(N+1)+x.bit_count()]+=1

def product_unit(A,B):
    a={j:(x,y) for j,x,y in A};b={j:(x,y) for j,x,y in B};out=[]
    for j in sorted(set(a)|set(b)):
        if j in a and j in b:
            if a[j][0]!=b[j][0]:return None
            out.append((j,a[j][1],b[j][1]))
        elif j in a:out.append((j,a[j][1],a[j][0]))
        else:out.append((j,b[j][0],b[j][1]))
    return out
def binomial_gram(wrong=False):
    G=np.zeros((raw.shape[1],raw.shape[1]),dtype=np.int64)
    for i,A in enumerate(patterns):
        for j,B in enumerate(patterns):
            C=product_unit(A,B)
            if C is None:continue
            a=sum(x for _,x,_ in C);b=sum(y for _,_,y in C);s=len(C)
            for k in range(N+1):
                l=k-a+b;h=k-a
                upper=N-s+(1 if wrong else 0)
                if 0<=l<=N and 0<=h<=upper:G[i*(N+1)+k,j*(N+1)+l]=math.comb(upper,h)
    return G
gram=binomial_gram();direct=raw.T@raw
assert np.array_equal(gram,direct)
wrong=binomial_gram(True)
wrong_count=int(np.count_nonzero(wrong!=direct));assert wrong_count>0

def mod_pivots(A,p=65521):
    M=np.array(A,dtype=np.int64)%p;r=0;piv=[]
    for j in range(M.shape[1]):
        choices=np.flatnonzero(M[r:,j])
        if not len(choices):continue
        i=r+int(choices[0]);M[[r,i]]=M[[i,r]]
        M[r]=(M[r]*pow(int(M[r,j]),-1,p))%p
        if r+1<len(M):M[r+1:]=(M[r+1:]-M[r+1:,j:j+1]*M[r])%p
        piv.append(j);r+=1
        if r==len(M):break
    return piv
piv=mod_pivots(raw)
basis=sp.Matrix(raw[:,piv].tolist())
null=basis.T.nullspace();C=sp.Matrix.hstack(*null)
assert C.T*sp.Matrix(raw.tolist())==sp.zeros(len(null),raw.shape[1])
assert len(piv)+len(null)==dim

L=sp.zeros(dim)
for j in range(N-1):
    for x in range(dim):
        y=x if bit(x,j)==bit(x,j+1) else x^(1<<(N-1-j))^(1<<(N-2-j))
        L[x,x]+=1;L[y,x]-=1
assert basis.T*L*C==sp.zeros(len(piv),len(null))
outside=(C.T*C).inv()*(C.T*L*C)
x=sp.Symbol('x');pout=sp.Poly(outside.charpoly(x).as_expr(),x)
pfull=sp.Poly(L.charpoly(x).as_expr(),x)
pin=sp.exquo(pfull,pout)
assert pin*pout==pfull
intervals=pout.intervals(eps=sp.Rational(1,10**8))
last=intervals[-1][0]
factors=sp.factor_list(pout)[1]
selected=[f for f,m in factors if f.count_roots(last[0],last[1])==1]
assert len(selected)==1
f=selected[0];gcd=sp.gcd(f,pin)
assert gcd.degree()==0
assert last[0]>0 and last[1]<2*(N-1)<20
result={'scope':'Exact finite Gram and algebraic pole checks; no complexity claim for total compiler.',
    'versions':{'python':platform.python_version(),'numpy':np.__version__,'sympy':sp.__version__},
    'N':N,'patterns':len(patterns),'spanning_columns':raw.shape[1],
    'all_gram_entries_compared':int(gram.size),'exact_gram_match':True,
    'wrong_N_minus_support_plus_one_entries_rejected':wrong_count,
    'rank_lower_bound_mod_65521':len(piv),'exact_annihilator_dimension':len(null),
    'exact_G2_dimension':len(piv),'exact_L_reduction':True,
    'outside_polynomial':str(pout.as_expr()),'outside_factorization':str(sp.factor(pout.as_expr())),
    'selected_root_isolating_interval':[str(last[0]),str(last[1])],
    'selected_irreducible_factor':str(f.as_expr()),'gcd_selected_factor_with_G2_characteristic':str(gcd.as_expr()),
    'inside_characteristic_factorization':str(sp.factor(pin.as_expr())),
    'interpretation':'Let alpha be the largest root of the displayed outside polynomial. It is absent from G2 by exact coprimality. Then c=-alpha makes the full source inverse singular while its G1 and G2 compressions are nonsingular. Taking omega=20 and lambda=20-alpha gives a positive bus field and a full Q/P resonance outside H2.'}
(OUT/'EXACT_GRAM_RESULT.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
