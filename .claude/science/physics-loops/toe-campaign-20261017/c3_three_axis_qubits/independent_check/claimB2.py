import sys, time, pickle
sys.path.insert(0,'/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/indep_C3')
from core import *
t0=time.time()
D=pickle.load(open('/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/indep_C3/B.pkl','rb'))
reps,cl=D['reps'],D['cliques']
Glab={(0,0,0),(1,0,0),(0,2,0),(0,0,3),(1,2,0),(1,0,3),(0,2,3),(1,2,3)}
out={}
for c in sorted(cl,key=len):
    signed=[(s,T) for u in c for T,s in reps[u][1].items()]
    labs=set(tuple(T[3*i:3*i+3]) for _,T in signed for i in range(7))
    basis,bad=local_basis(signed)
    # O-closure of the signed rule
    rd={T:s for s,T in signed}
    closed=all(act(R,T)[1] in rd and act(R,T)[0]*s==rd[act(R,T)[1]] for s,T in signed for R in O)
    res=[len(c),len(signed),'localrank',len(basis),'localbad',len(bad),'Oclosed',closed,'labels_in_G',labs<=Glab]
    for L in ((3,4,5,6) if len(c)<100 else (4,)):
        d,b=torus_dim(basis,L); res+=['L%d'%L,d,'bad',len(b)]
    print(res, round(time.time()-t0,1)); sys.stdout.flush()
    out[tuple(sorted(c))]=basis
pickle.dump(out,open('/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/indep_C3/bases.pkl','wb'))
# 187 family: check all member orbits labels within G
big=max(cl,key=len)
print('187 family all labels in G:', all(tuple(T[3*i:3*i+3]) in Glab for u in big for T in reps[u][1] for i in range(7)))
print('any non-187 orbit with labels in G only:', [u for u in range(len(reps)) if u not in big and all(tuple(T[3*i:3*i+3]) in Glab for T in reps[u][1] for i in range(7))])
# overlap structure between cliques
print('clique overlaps:', sorted({len(set(a)&set(b)) for a in cl for b in cl if a is not b}))
