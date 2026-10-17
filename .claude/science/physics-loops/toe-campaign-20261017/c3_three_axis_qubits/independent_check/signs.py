"""Is there a choice of orbit signs making each maximal set's group free of -1 (locally and on L-tori)?"""
import sys, time, pickle
sys.path.insert(0,'/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/indep_C3')
from core import *
t0=time.time()
D=pickle.load(open('/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/indep_C3/B.pkl','rb'))
reps,cl=D['reps'],D['cliques']

def elim_masked(items, nbits):
    """items: list of (op,mask). returns pivots list (op,mask) and equations (mask, rhs)."""
    piv={}; eqs=[]
    for op,m in items:
        v=list(op); mm=m
        while True:
            key=(v[0]<<nbits)|v[1]
            if key==0:
                assert v[2] in (0,2); eqs.append((mm, v[2]//2)); break
            hb=key.bit_length()-1
            if hb in piv: w,wm=piv[hb]; v=mul(v,w); mm^=wm
            else: piv[hb]=(v,mm); break
    return list(piv.values()), eqs

def solve(eqs, nvar):
    piv={}  # GF(2) with augmented bit at position nvar
    for m,r in eqs:
        row=m|(r<<nvar)
        while row & ((1<<nvar)-1):
            hb=(row & ((1<<nvar)-1)).bit_length()-1
            if hb in piv: row^=piv[hb]
            else: piv[hb]=row; break
        else:
            if row: return False, len(piv)
    return True, len(piv)

def star_to_torus(op5, L, shift):
    # re-embed an op given on L=5 star placement into torus L with shift
    x,z,ph=op5; X=0; Z=0
    for i,p in enumerate(POS):
        r5=[p[k]%5 for k in range(3)]; b5=((r5[0]*5+r5[1])*5+r5[2])*3
        r=[(p[k]+shift[k])%L for k in range(3)]; b=((r[0]*L+r[1])*L+r[2])*3
        for a in range(3):
            if (x>>(b5+a))&1: X|=1<<(b+a)
            if (z>>(b5+a))&1: Z|=1<<(b+a)
    return [X,Z,ph]

if __name__=="__main__":
 for c in sorted(cl,key=len):
     items=[]
     for k,u in enumerate(c):
         for T,s in reps[u][1].items(): items.append((to_op(T,s,5),1<<k))
     basis,eqs=elim_masked(items,375)
     res=[len(c),'local eqs',len(eqs)]
     ok,rk=solve(eqs,len(c)); res+=['local solvable',ok,'eqrank',rk]
     for L in ((4,6) if len(c)<100 else (4,)):
         n=3*L**3
         tit=[(star_to_torus(op,L,(a,b,d)),m) for op,m in basis for a in range(L) for b in range(L) for d in range(L)]
         _,teqs=elim_masked(tit,n)
         ok2,rk2=solve(eqs+teqs,len(c)); res+=['L%d solvable'%L,ok2,'eqrank',rk2]
     print(res, round(time.time()-t0,1)); sys.stdout.flush()
