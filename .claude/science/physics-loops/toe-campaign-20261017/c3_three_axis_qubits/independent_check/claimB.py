import sys, time, itertools, pickle
sys.path.insert(0,'/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/indep_C3')
from core import *
import numpy as np, networkx as nx
t0=time.time()
C4z=np.array([[0,-1,0],[1,0,0],[0,0,1]]); C3=np.array([[0,0,1],[1,0,0],[0,1,0]])
def gen_group(g):
    H=[np.eye(3,dtype=int)]; M=g.copy()
    while not (M==np.eye(3,dtype=int)).all(): H.append(M); M=M.dot(g)
    return H
def fixed_strings(g):
    H=gen_group(g)
    # brute-force over orbit representatives of (site,qubit) slots
    slots=list(range(21)); seen=set(); orbits=[]
    for s in slots:
        if s in seen: continue
        i,a=divmod(s,3); orb=set()
        for R in H:
            j=PIDX[tuple(int(v) for v in R.dot(POS[i]))]; pa=int(np.nonzero(R[:,a])[0][0]); orb.add(3*j+pa)
        seen|=orb; orbits.append(sorted(orb))
    # candidate: for each orbit, rep label; propagate; then verify fixedness by direct action
    choices=[]
    for orb in orbits:
        opts=[]
        for l in range(4):
            S=[0]*21; S[orb[0]]=l
            # propagate
            T=[0]*21
            for R in H:
                _,img=act(R,tuple(S))
                for k in range(21):
                    if img[k]: T[k]=img[k]
            opts.append(T)
        choices.append(opts)
    out=set()
    for combo in itertools.product(*choices):
        S=[0]*21
        for T in combo:
            for k in range(21):
                if T[k]: S[k]=T[k]
        S=tuple(S)
        if all(act(R,S)[1]==S for R in H): out.add(S)
    return out
F4=fixed_strings(C4z); F3=fixed_strings(C3)
print('fixed by C4z',len(F4),'by C3',len(F3),'both',len(F4&F3),'union',len(F4|F3))
cand=sorted(F4|F3)
# vectorized self-commutation check
N=len(cand); Sarr=np.array(cand,dtype=np.int8)                      # N x 21
LXa=np.array(LX,np.int8); LZa=np.array(LZ,np.int8)
imgs=np.zeros((N,24,21),np.int8)
# action as slot permutation + label map (soldered), per R
for r,R in enumerate(O):
    perm=[None]*21; lmap=np.zeros((3,4),np.int8)
    for i,p in enumerate(POS):
        j=PIDX[tuple(int(v) for v in R.dot(p))]
        for a in range(3): perm[3*i+a]=3*j+int(np.nonzero(R[:,a])[0][0])
    labmap=np.array([0]+[int(np.nonzero(R[:,b])[0][0])+1 for b in range(3)],np.int8)
    for k in range(21): imgs[:,r,perm[k]]=labmap[Sarr[:,k]]
ok=np.ones(N,bool)
for t,pr in OVL.items():
    s=np.zeros((N,24),np.int8)
    for i,j in pr:
        for a in range(3):
            L1=Sarr[:,3*i+a][:,None]; L2=imgs[:,:,3*j+a]
            s^=(LXa[L1]*LZa[L2]+LZa[L1]*LXa[L2])&1
    ok&=~(s.any(1))
good=[cand[k] for k in range(N) if ok[k]]
print('self-commuting (incl identity?)',len(good),'identity in:',tuple([0]*21) in good)
# spot check vectorized vs scalar on random subset
import random; random.seed(1)
for k in random.sample(range(N),300):
    S=cand[k]; sc=all(commute_all_translates(S,act(R,S)[1]) for R in O)
    assert sc==ok[k]
# orbits
def canon(S): return min(act(R,S)[1] for R in O)
orbs={}
for S in good: orbs.setdefault(canon(S),[]).append(S)
print('orbits among good',len(orbs))
def signed_orbit(S):
    d={}
    for R in O:
        s,T=act(R,S)
        if T in d and d[T]!=s: return None
        d[T]=s
    return d
reps=[]; incons=0
for c,mem in orbs.items():
    so=signed_orbit(mem[0])
    if so is None: incons+=1
    else: reps.append((mem[0],so))
print('sign-consistent orbits',len(reps),'inconsistent',incons)
# also: all orbit images (not only those in restricted class) commute? check orbit closure
idS=tuple([0]*21)
reps=[r for r in reps if r[0]!=idS]
print('nonidentity consistent orbits',len(reps))
# pairwise orbit commutation
M=len(reps); Gr=nx.Graph(); Gr.add_nodes_from(range(M))
for u in range(M):
    for v in range(u+1,M):
        S=reps[u][0]
        if all(commute_all_translates(S,T) for T in reps[v][1]): Gr.add_edge(u,v)
cl=list(nx.find_cliques(Gr))
print('maximal cliques',len(cl),'sizes',sorted(len(c) for c in cl))
pickle.dump({'reps':reps,'cliques':cl,'good':good},open('/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/indep_C3/B.pkl','wb'))
print('time',time.time()-t0)
