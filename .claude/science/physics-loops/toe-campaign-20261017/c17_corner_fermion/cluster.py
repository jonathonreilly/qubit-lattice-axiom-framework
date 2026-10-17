import numpy as np, itertools, sys
ARGS=sys.argv[1:]
exec(open('band.py').read().split("def H(t1,t2):")[0])
exec(open('chiral.py').read().split("TRI=oriented_triangles()")[0].split("# oriented triangle edges")[1].join(["",""]) if False else "")
li={g:i for i,g in enumerate(loc)}
def cl(t1,lam):
    Hc=np.zeros((12,12),complex)
    for k in C.EDGES:
        i,j=tuple(k)
        if C.edges[k]=='onsite' and i in li and j in li:
            a=-t1*(-1.0)**u[C.EID[k]]; Hc[li[i],li[j]]+=a; Hc[li[j],li[i]]+=a
    v=(0,0,0)
    for s in itertools.product((1,-1),repeat=3):
        x,y,z=(s[0],0,0),(0,s[1],0),(0,0,s[2])
        cyc=[(v,frozenset((x,y))),(v,frozenset((y,z))),(v,frozenset((z,x)))]
        if round(np.linalg.det(np.array([x,y,z])))<0: cyc=cyc[::-1]
        for a in range(3):
            q,r=cyc[a],cyc[(a+1)%3]; i,j=li[C.VID[q]],li[C.VID[r]]
            amp=1j*lam*(-1.0)**u[C.eid(q,r)]; Hc[j,i]+=amp; Hc[i,j]+=np.conj(amp)
    return Hc
for t1,lam in [(-1,-0.5),(-1,0.5),(1,-0.5),(1,0.5)]:
    Hc=cl(t1,lam)
    for M in Mt: assert np.allclose(M@Hc,Hc@M)
    ev,V=np.linalg.eigh(Hc); out=[]; i=0
    while i<12:
        j=i
        while j<12 and abs(ev[j]-ev[i])<1e-8: j+=1
        Pj=V[:,i:j]@V[:,i:j].conj().T
        out.append((round(ev[i],3),dec(np.array([np.trace(Pj@M) for M in Mt])))); i=j
    print(f'triangle={ARGS[0]} t1={t1:+} chiral={lam:+}:', out)
