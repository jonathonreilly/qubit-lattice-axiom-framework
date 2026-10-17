import sys, random; sys.argv=['q','4']
exec(open('qubits.py').read().split("if __name__ == '__main__':")[0])
EDGES=[]; seen=set()
for q in VERTS:
    for k,e,nb in INC[q]:
        key=frozenset((VID[q],VID[nb]))
        if key not in seen: seen.add(key); EDGES.append((q,nb) if canon_first(q,nb) else (nb,q))
Aop={e:A(*e) for e in EDGES}
rot=[]
for R in ROTS:
    perm=qperm(R); cz=cz_network(R); zf=0
    for e in EDGES:
        img=apply_cz(apply_perm(Aop[e],perm),cz); q,r=e
        Rq=(rs(R,q[0]),rc(R,q[1])); Rr=(rs(R,r[0]),rc(R,r[1]))
        if (img[2]-A(Rq,Rr)[2])%4==2:
            if not canon_first(Rq,Rr): Rq,Rr=Rr,Rq
            zf^=1<<edge_zqubit(Rq,*[ed for k,ed,nb in INC[Rq] if nb==Rr][0])
    rot.append((perm,cz,zf))
def U(k,P):
    perm,cz,zf=rot[k]; return apply_zfix(apply_cz(apply_perm(P,perm),cz),zf)
def rid(M):
    for k,S in enumerate(ROTS):
        if (S==M).all(): return k
random.seed(3); bad={}
for a in range(24):
    for b in range(24):
        ab=rid(ROTS[a]@ROTS[b])
        for i in random.sample(range(NQ),30):
            P=(1<<i,0,0); l=U(a,U(b,P)); r=U(ab,P)
            if l!=r:
                kind='z' if l[1]!=r[1] else 'sign'
                bad.setdefault((a,b),set()).add((kind, LABS[i%48][0]))
print(len(bad),'bad pairs'); 
from collections import Counter
print(Counter(frozenset(v) for v in bad.values()))
