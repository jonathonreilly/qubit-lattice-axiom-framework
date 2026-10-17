import pickle, sys
from orbits import *
mode=int(sys.argv[1])
orbs=pickle.load(open(D+'orbs%d.pkl'%mode,'rb'))
n=len(orbs)
C=(1,1,3,3,2,2)  # spin chamon labels on sites 1..6: X on +-x, Y on +-y, Z on +-z
CH=tuple([0]+list(C))
bell={0,1|4,3|12,2|8}
def comp(i,j):
    a=orbs[i][0]
    return all(commute_all_translates(a,b) for b in orbs[j])
# fast path for soldered: Bell-only orbits pairwise compatible
isbell=[all(l in bell for l in o[0]) for o in orbs]
adj=[set() for _ in range(n)]
for i in range(n):
    for j in range(i+1,n):
        if mode==1 and isbell[i] and isbell[j]: ok=True
        else: ok=comp(i,j)
        if ok: adj[i].add(j); adj[j].add(i)
cl=[]
def bk(R,P,X):
    if not P and not X: cl.append(R); return
    u=max(P|X,key=lambda v:len(adj[v]&P))
    for v in list(P-adj[u]):
        bk(R|{v},P&adj[v],X&adj[v]); P=P-{v}; X=X|{v}
bk(set(),set(range(n)),set())
print('maximal cliques',len(cl),'sizes',sorted(len(c) for c in cl))
def spin(s): return tuple(l&3 for l in s)
def flav(s): return tuple(l>>2 for l in s)
for c in cl:
    strs=[s for i in c for s in orbs[i]]
    sp=set(spin(s) for s in strs); fl=set(l for s in strs for l in flav(s))
    print(len(c),'orbits',len(strs),'strings; spin parts:',[('CH' if x==CH else ('I' if x==(0,)*7 else ''.join(P1[l] for l in x))) for x in sp],'flavour labels',sorted(P1[l] for l in fl))
    if len(c)<6:
        for i in c: print('   ',[name(s) for s in orbs[i]])
nonbell=[i for i in range(n) if not isbell[i]]
print('non-Bell orbits:',len(nonbell))
for i in nonbell: print('  ',[name(s) for s in orbs[i]])
pickle.dump((cl,adj),open(D+'cl%d.pkl'%mode,'wb'))
