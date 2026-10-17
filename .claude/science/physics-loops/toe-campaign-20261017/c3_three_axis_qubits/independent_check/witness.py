"""Find explicit sign-independent -1 witness in the 23/31/187 sets and verify with dense Pauli matrices."""
import sys, pickle, itertools, numpy as np
sys.path.insert(0,'/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/indep_C3')
from core import *
D=pickle.load(open('/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/indep_C3/B.pkl','rb'))
reps,cl=D['reps'],D['cliques']
P=[np.eye(2),np.array([[0,1],[1,0]]),np.array([[0,-1j],[1j,0]]),np.array([[1,0],[0,-1]])]
NM='IXYZ'
def show(T): return ' '.join(f"{POS[i]}:{''.join(NM[l] for l in T[3*i:3*i+3])}" for i in range(7) if any(T[3*i:3*i+3]))
def dense(Ts):
    # tensor product of per-qubit 2x2 products; returns scalar c if product == c*I, else None
    c=1.0+0j
    for s,_ in Ts: c*=s
    for k in range(21):
        M=np.eye(2,dtype=complex)
        for _,T in Ts: M=M@P[T[k]]
        if abs(M[0,1])>1e-9 or abs(M[1,0])>1e-9 or abs(M[0,0]-M[1,1])>1e-9: return None,21
        c*=M[0,0]
    return c,21
for c in sorted(cl,key=len)[8:]:
    imgs=[(u,T,s) for u in c for T,s in reps[u][1].items()]
    # search for small sign-independent witness: pairs of images from same orbit u (counted twice) not allowed; search
    # triples/quads over images: product = -I with every orbit used an even number of times -> need >=2 per orbit
    # general approach: brute force subsets of size<=4 of images with phase -1 relation, then combine
    found=None
    by=[(to_op(T,s,5),u,T,s) for u,T,s in imgs]
    # pairs from orbit u x orbit v (each twice): product of 4 images a1 a2 b1 b2
    for (i,A),(j,B) in itertools.combinations(enumerate(by),2):
        pass
    # exhaustive over size-4 subsets with orbit multiplicities even (2+2) or (4)
    from collections import defaultdict
    orb=defaultdict(list)
    for k,(op,u,T,s) in enumerate(by): orb[u].append(k)
    for u,v in itertools.combinations_with_replacement(c,2):
        for p in itertools.combinations(orb[u],2):
            for q in (itertools.combinations(orb[v],2) if u!=v else [()]):
                ks=list(p)+list(q)
                if u==v: continue
                op=[0,0,0]
                for k in ks: op=mul(op,by[k][0])
                if op[0]==0 and op[1]==0 and op[2]==2: found=ks; break
            if found: break
        if found: break
    if found is None:
        # try size-6 with three orbits (2+2+2)
        for u,v,w in itertools.combinations(c,3):
            for p in itertools.combinations(orb[u],2):
                for q in itertools.combinations(orb[v],2):
                    for r in itertools.combinations(orb[w],2):
                        ks=list(p)+list(q)+list(r); op=[0,0,0]
                        for k in ks: op=mul(op,by[k][0])
                        if op[0]==0 and op[1]==0 and op[2]==2: found=ks; break
                    if found: break
                if found: break
            if found: break
    print('set size',len(c),'witness size',None if found is None else len(found))
    if found:
        Ts=[(by[k][3],by[k][2]) for k in found]
        for k in found: print('   orbit',by[k][1],'sign',by[k][3],show(by[k][2]))
        M,ns=dense(Ts); print('   per-qubit matrix product scalar:',M)
        # pairwise commutation check (all translates) of witness members
        print('   witness members commute pairwise:',all(commute_all_translates(a[1],b[1]) for a in Ts for b in Ts))
