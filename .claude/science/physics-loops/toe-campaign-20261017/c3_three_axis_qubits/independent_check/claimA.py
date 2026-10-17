import sys, time, itertools
sys.path.insert(0,'/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/indep_C3')
from core import *
t0=time.time()
def site(p): return PIDX[p]
def e(a,s): v=[0,0,0]; v[a]=s; return tuple(v)
A=[0]*21
for a in range(3):
    for s in (1,-1): A[3*site(e(a,s))+a]=1
A=tuple(A)
Bs=[]
for c in range(3):
    a,b=[k for k in range(3) if k!=c]
    B=[0]*21
    for s in (1,-1):
        B[3*site(e(a,s))+b]=3; B[3*site(e(b,s))+a]=3
    Bs.append(tuple(B))
rule={A:1, **{B:1 for B in Bs}}
# O-closure (unsoldered)
closed=all(act(R,S,False)[1] in rule and act(R,S,False)[0]==1 for R in O for S in rule)
print('O-closed (unsoldered, signs +):',closed)
gens=list(rule)
print('commuting:',all(commute_all_translates(S,T) for S in gens for T in gens))
# single-site Paulis commuting with all generator translates
cnt=0
for labs in itertools.product(range(4),repeat=3):
    if labs==(0,0,0): continue
    P=tuple(list(labs)+[0]*18)
    if all(commute_all_translates(P,T) for T in gens): cnt+=1; print('commuting single-site',labs)
print('single-site commutant count (nontrivial):',cnt)
basis,bad=local_basis([(1,S) for S in gens]); print('local basis',len(basis),'bad',bad)
for L in (3,4,5,6):
    d,bad=torus_dim(basis,L); print('L',L,'log2dim',d,'-1 relations',len(bad))
# mobility: vertex violation moved by single Z on qubit a at e_a: check syndrome of Z_a(e_a)
for a in range(3):
    P=[0]*21; P[3*site(e(a,1))+a]=3; P=tuple(P)
    viol=[(t,'A') for t in TRANS if any(symp(P[3*i+q],A[3*j+q]) for i,j in OVL[t] for q in range(3)) and sum(symp(P[3*i+q],A[3*j+q]) for i,j in OVL[t] for q in range(3))%2]
    violB=[(t,k) for t in TRANS for k,B in enumerate(Bs) if sum(symp(P[3*i+q],B[3*j+q]) for i,j in OVL[t] for q in range(3))%2]
    print('Z on qubit',a,'at e_a violates A at',viol,' B:',violB)
print('time',time.time()-t0)
