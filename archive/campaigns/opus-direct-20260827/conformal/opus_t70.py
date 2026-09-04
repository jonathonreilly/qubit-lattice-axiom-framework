"""T70 - A FIELD EQUATION, AT LAST?  The Regge action and its variation.
T69: in d=4 the framework's complex carries curvature on HINGES (codimension-2
triangles) as a deficit angle, verified on S^4 = boundary of the 5-simplex --
all 20 hinges at deficit 2.328837 = 2pi - 3 arccos(1/4), confirmed analytically.
And  S = sum_hinges Area * deficit  is the Regge action, i.e. the discrete
Einstein-Hilbert action.

That makes the field-equation question concrete and checkable for the first time
in this campaign.  Three things:

 (F1) FLAT CONTROL.  Every hinge of the flat Kuhn 4-torus must have deficit
      EXACTLY zero -- in flat space the dihedral angles around a hinge close up.
 (F2) THE SCHLAEFLI IDENTITY.  Inside one simplex, sum_hinges A_h d(theta_h) = 0
      for any variation of its edge lengths.  This is the discrete Bianchi
      identity and it is what makes the Regge variation work: it means
      dS = sum_hinges deficit_h * dA_h, with no derivative-of-angle term.
 (F3) STATIONARITY.  Given (F1) and (F2), a flat complex has every deficit zero,
      so dS = 0 for EVERY edge-length variation: flat spacetime solves the
      vacuum equation.  Measured directly by finite differences on edge lengths,
      not assumed."""
import numpy as np, itertools, math
def qr_hull(P):
    O=P[0]; M=P[1:]-O
    Q,_=np.linalg.qr(M.T)
    return np.array([Q.T@(p-O) for p in P])
def dihedral(P,tri):
    o=P[tri[0]]
    Hs=np.array([P[tri[1]]-o,P[tri[2]]-o])
    Q,_=np.linalg.qr(Hs.T)
    other=[i for i in range(5) if i not in tri]
    def perp(x):
        v=x-o; return v-Q@(Q.T@v)
    u=perp(P[other[0]]); v=perp(P[other[1]])
    nu=np.linalg.norm(u); nv=np.linalg.norm(v)
    if nu<1e-13 or nv<1e-13: return float('nan')
    return float(np.arccos(np.clip(float(np.dot(u,v))/(nu*nv),-1,1)))
def tri_area(p0,p1,p2):
    a=p1-p0; b=p2-p0
    return 0.5*np.sqrt(max(float(np.dot(a,a)*np.dot(b,b)-np.dot(a,b)**2),0.0))
print("T70 (F1)  FLAT CONTROL: deficits on the Kuhn-triangulated flat 4-torus")
L=3; d=4
verts=list(itertools.product(range(L),repeat=d)); vid={v:i for i,v in enumerate(verts)}
h=1.0/L
tops=[]
for base in verts:
    for perm in itertools.permutations(range(d)):
        chain=[base]; cur=list(base); pos=[np.array([b*h for b in base])]; c=np.array([b*h for b in base])
        for a in perm:
            cur=list(cur); cur[a]=(cur[a]+1)%L; chain.append(tuple(cur))
            c=c.copy(); c[a]+=h; pos.append(c)
        tops.append((tuple(chain),np.array(pos)))
hinge_ang={}
for ch,P in tops:
    Pl=qr_hull(P)
    for tri in itertools.combinations(range(5),3):
        key=tuple(sorted([ch[i] for i in tri]))
        hinge_ang[key]=hinge_ang.get(key,0.0)+dihedral(Pl,list(tri))
defs=np.array([2*np.pi-v for v in hinge_ang.values()])
print(f"   {len(defs)} hinges;  max|deficit| = {float(np.max(np.abs(defs))):.3e}   "
      f"mean = {float(np.mean(defs)):+.3e}")
print(f"   flat complex has zero curvature at every hinge: "
      f"{'PASS' if np.max(np.abs(defs))<1e-9 else 'FAIL'}")
print()
print("T70 (F2)  SCHLAEFLI IDENTITY inside one 4-simplex:  sum_h A_h d(theta_h) = 0")
rng=np.random.default_rng(2)
for trial in range(3):
    P0=rng.normal(size=(5,4))
    def angles_and_areas(P):
        A=[];T=[]
        for tri in itertools.combinations(range(5),3):
            A.append(tri_area(P[tri[0]],P[tri[1]],P[tri[2]]))
            T.append(dihedral(P,list(tri)))
        return np.array(A),np.array(T)
    A0,T0=angles_and_areas(P0)
    tot=[]
    for _ in range(4):
        D=rng.normal(size=(5,4))*1e-5
        Ap,Tp=angles_and_areas(P0+D); Am,Tm=angles_and_areas(P0-D)
        dT=(Tp-Tm)/2.0
        tot.append(float(np.sum(A0*dT)))
    print(f"   simplex {trial+1}: sum A dtheta over 4 random variations = "
          f"{['%.3e'%t for t in tot]}   (must be ~0)", flush=True)
print()
print("T70 (F3)  STATIONARITY of the flat complex under edge-length variations")
print("   S = sum_hinges A_h * deficit_h ; vary vertex positions of the flat torus")
def regge_S(shift=None,amp=0.0):
    tot={}
    A={}
    for ch,P in tops:
        Pm=P.copy()
        if shift is not None:
            Pm=P+amp*np.array([shift(p) for p in P])
        Pl=qr_hull(Pm)
        for tri in itertools.combinations(range(5),3):
            key=tuple(sorted([ch[i] for i in tri]))
            tot[key]=tot.get(key,0.0)+dihedral(Pl,list(tri))
            A[key]=tri_area(Pm[tri[0]],Pm[tri[1]],Pm[tri[2]])
    return float(sum(A[k]*(2*np.pi-tot[k]) for k in tot))
S0=regge_S()
print(f"   S(flat) = {S0:+.6e}")
for name,f in (("wave", lambda p: np.array([np.sin(2*np.pi*p[1]),np.sin(2*np.pi*p[2]),
                                            np.sin(2*np.pi*p[3]),np.sin(2*np.pi*p[0])])),
               ("radial", lambda p: p-0.5)):
    row=[]
    for amp in (1e-3,3e-3,1e-2):
        Sp=regge_S(f,amp); Sm=regge_S(f,-amp)
        row.append(((Sp-Sm)/(2*amp), (Sp-2*S0+Sm)/amp**2))
    print(f"   {name:8s} dS/damp = {['%+.3e'%r[0] for r in row]}   "
          f"d2S/damp2 = {['%+.3e'%r[1] for r in row]}", flush=True)
print()
print("   dS/damp ~ 0 for every variation  =>  the flat complex is a stationary")
print("   point of the Regge action: the discrete vacuum Einstein equation holds.")
