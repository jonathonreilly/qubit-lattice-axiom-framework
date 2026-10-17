import numpy as np, itertools, sys
ARGS=sys.argv[1:]
exec(open('band.py').read().split("def H(t1,t2):")[0].replace("triangle=int(ARGS[0]),plaquette=1,tube=int(ARGS[1])","triangle=int(ARGS[0]),plaquette=1,tube=int(ARGS[1])"))
# oriented triangle edges: triangle at v for octant s: corners (x,y)->(y,z)->(z,x), oriented counterclockwise about the outward diagonal s
def oriented_triangles():
    out=[]
    for v in C.SITES:
        for s in itertools.product((1,-1),repeat=3):
            x,y,z=(s[0],0,0),(0,s[1],0),(0,0,s[2])
            cyc=[(v,frozenset((x,y))),(v,frozenset((y,z))),(v,frozenset((z,x)))]
            # orientation: x->y->z is right-handed about s iff det(x,y,z)>0
            det=round(np.linalg.det(np.array([x,y,z])))
            if det<0: cyc=cyc[::-1]
            out.append(cyc)
    return out
TRI=oriented_triangles()
def H(t1,t2,lam):
    Hm=np.zeros((n,n),complex)
    for k in C.EDGES:
        i,j=tuple(k); t=t1 if C.edges[k]=='onsite' else t2
        a=-t*(-1.0)**u[C.EID[k]]; Hm[i,j]+=a; Hm[j,i]+=a
    for cyc in TRI:
        for a in range(3):
            q,r=cyc[a],cyc[(a+1)%3]; i,j=C.VID[q],C.VID[r]
            amp=1j*lam*(-1.0)**u[C.eid(q,r)]
            Hm[j,i]+=amp; Hm[i,j]+=np.conj(amp)
    return Hm
for t1,t2,lam in [(-1,0.3,0.2),(-1,0.3,-0.2),(1,0.3,0.2),(1,0.3,-0.2),(-1,1,0.3),(-1,1,-0.3)]:
    Hm=H(t1,t2,lam)
    for R in range(24):
        Mfd=Mf[R].toarray()
        assert np.allclose(Mfd@Hm,Hm@Mfd), "not O-invariant"
    ev,V=np.linalg.eigh(Hm); e0=ev[0]; m=np.sum(np.abs(ev-e0)<1e-7); Pj=V[:,:m]
    ch=np.array([sgn[k]*(1j**W1[proj[k]])*np.trace(Pj.conj().T@(Mf[proj[k]]@Pj)) for k in range(48)])
    print(f't1={t1:+} t2={t2:+} chiral={lam:+}: lowest E={e0:.4f} deg={m} gap={ev[m]-e0:.4f} irreps={dec(ch)}')
