import itertools, sys, numpy as np
D='/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/indep_C2/'
site=[(0,0,0),(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
SI={s:i for i,s in enumerate(site)}
P1={0:'I',1:'X',2:'Z',3:'Y'}
AX={1:0,3:1,2:2}; AXP={0:1,1:3,2:2}
G=[]
for p in itertools.permutations(range(3)):
    for sg in itertools.product([1,-1],repeat=3):
        M=np.zeros((3,3),int)
        for i in range(3): M[p[i],i]=sg[i]
        if round(np.linalg.det(M))==1: G.append(M)
assert len(G)==24
def act(M,S,mode):
    pi=[int(np.nonzero(M[:,i])[0][0]) for i in range(3)]
    out=[0]*7
    for r,l in enumerate(S):
        v=tuple(int(x) for x in M@np.array(site[r]))
        s=l&3; f=l>>2
        s2=AXP[pi[AX[s]]] if s else 0
        f2=(AXP[pi[AX[f]]] if f else 0) if mode==1 else f
        out[SI[v]]=s2|(f2<<2)
    return tuple(out)
def sym1(a,b): return ((a&1)&(b>>1&1))^((a>>1&1)&(b&1))
def comm(a,b): return sym1(a&3,b&3)^sym1(a>>2,b>>2)
def name(S):
    return ' '.join(P1[l&3]+P1[l>>2] for l in S)
def commute_all_translates(S,T):
    # S vs T shifted by t for all t
    for t in itertools.product(range(-2,3),repeat=3):
        x=0
        for r in range(7):
            v=tuple(site[r][k]+t[k] for k in range(3))
            if v in SI: x^=comm(S[SI[v]],T[r])
        if x: return False
    return True
def run(mode,fn):
    strs=[int(l) for l in open(D+fn)]
    S=set(tuple((n>>(4*r))&15 for r in range(7)) for n in strs)
    orbs=[];seen=set()
    for s in sorted(S):
        if s in seen: continue
        o=set(act(M,s,mode) for M in G)
        assert o<=S
        seen|=o; orbs.append(sorted(o))
    return S,orbs
if __name__=='__main__':
    mode=int(sys.argv[1]); fn=sys.argv[2]
    S,orbs=run(mode,fn)
    print('strings',len(S),'orbits',len(orbs))
    import pickle; pickle.dump(orbs,open(D+'orbs%d.pkl'%mode,'wb'))
