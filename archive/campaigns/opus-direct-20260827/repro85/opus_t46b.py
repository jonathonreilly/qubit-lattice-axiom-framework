"""T46 - independent verification of T45b, from two directions at once.
T45b: the complex-native Kahler-Dirac operator has ker = Betti numbers, satisfies
McKean-Singer exactly, and reproduces the sphere's l(l+1) spectrum.  Two checks
that probe DIFFERENT things:

 (V1) SQUASH THE SPHERE into an ellipsoid.  Topology is unchanged, geometry is
      not.  A correct operator must therefore keep Str exp(-t D^2) = 2 EXACTLY
      while the 0-form spectrum MOVES OFF l(l+1).  An operator that merely
      counted combinatorics would keep both; one that merely measured geometry
      would lose the invariant.  Both halves have to fire.

 (V2) THE HEAT-KERNEL CURVATURE TERM.  For a closed surface,
         Tr exp(-t Lap_0)  =  Area/(4 pi t)  +  (1/4pi) int R/6  +  O(t)
      and with R = 2K and Gauss-Bonnet int K = 2 pi chi, the constant term is
      exactly  chi/6.  So  Tr exp(-t Lap_0) - Area/(4 pi t)  ->  chi/6:
      1/3 for the sphere, 0 for the torus.  This measures the CURVATURE INTEGRAL
      out of the spectrum, by a completely different route from l(l+1).
      (Only modes below the mesh cutoff are trustworthy, so a plateau in t is
      what to look for, not the t -> 0 limit.)

 (V3) a different mesh of the same sphere (octahedral rather than icosahedral),
      to confirm nothing depends on the combinatorics."""
import numpy as np
exec(open("/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-gravity-toe-lane-work-427b0b/25068357-42e8-431c-96c9-c149512f0305/scratchpad/opus_t45b.py").read().split('print("T45')[0])
def octasphere(nsub):
    V=[np.array(v,dtype=float) for v in
       [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]]
    F=[(0,2,4),(2,1,4),(1,3,4),(3,0,4),(2,0,5),(1,2,5),(3,1,5),(0,3,5)]
    for _ in range(nsub):
        mid={}; NF=[]
        def m(i,j):
            k=(min(i,j),max(i,j))
            if k not in mid: V.append((V[i]+V[j])/2); mid[k]=len(V)-1
            return mid[k]
        for (a,b,c) in F:
            ab,bc,ca=m(a,b),m(b,c),m(c,a); NF+=[(a,ab,ca),(b,bc,ab),(c,ca,bc),(ab,bc,ca)]
        F=NF
    return [v/np.linalg.norm(v) for v in V],F
def squash(V,sx,sy,sz):
    return [np.array([p[0]*sx,p[1]*sy,p[2]*sz]) for p in V]
def analyse(V,F,tn=None,label="",area_exact=None,chi=None):
    d0,d1,s0,s1,s2,nv,ne,nf=geometry(V,F,tn)
    try:
        D,A0,A1,nv,ne,nf=operator(d0,d1,s0,s1,s2)
    except ValueError as ex:
        print(f"  {label}   SKIPPED: {ex}"); return None,None
    L0=A0.T@A0; L1=A0@A0.T+A1.T@A1; L2=A1@A1.T
    e0=np.clip(np.linalg.eigvalsh(L0),0,None)
    e1=np.clip(np.linalg.eigvalsh(L1),0,None); e2=np.clip(np.linalg.eigvalsh(L2),0,None)
    area=float(np.sum(s0))
    ker=int(np.sum(np.abs(np.linalg.eigvalsh(D))<1e-8))
    st=[float(np.sum(np.exp(-t*e0))-np.sum(np.exp(-t*e1))+np.sum(np.exp(-t*e2)))
        for t in (0.05,0.5,5.0)]
    cl=[]
    for z in np.sort(e0)[:20]:
        if cl and abs(z-cl[-1][0])<0.12*max(1.0,abs(z)): cl[-1][1]+=1
        else: cl.append([z,1])
    print(f"  {label}   V={nv} E={ne} F={nf}  chi_comb={nv-ne+nf}  area={area:.5f}"
          + (f" (exact {area_exact:.5f})" if area_exact else ""))
    print(f"     ker D = {ker}   Str exp(-tD^2) at t=0.05,0.5,5.0 : "
          f"{st[0]:+.6f} {st[1]:+.6f} {st[2]:+.6f}")
    print(f"     0-form spectrum: {[f'{v:.4f}x{c}' for v,c in cl[:5]]}", flush=True)
    return e0, area
print("T46 (V1)  SQUASH THE SPHERE: topology must hold, geometry must move")
Vi,Fi=icosphere(3)
analyse(Vi,Fi,label="round sphere      ",area_exact=4*np.pi,chi=2)
for s in ((1.0,1.0,0.94),(1.0,1.0,0.88),(1.0,0.95,0.90)):
    analyse(squash(Vi,*s),Fi,label=f"ellipsoid {s}")
print()
print("T46 (V3)  a DIFFERENT MESH of the same sphere")
Vo,Fo=octasphere(4); analyse(Vo,Fo,label="octahedral sphere ",area_exact=4*np.pi)
print()
print("T46 (V2)  heat-kernel curvature term:  Tr exp(-t Lap_0) - Area/(4 pi t) -> chi/6")
print(f"   {'t':>7} {'sphere (want 1/3 = 0.3333)':>28} {'torus (want 0)':>20}")
Vh,Fh=icosphere(4); e0s,areaS=analyse(Vh,Fh,label="  [sphere sub=4 for the heat trace]",area_exact=4*np.pi)
Vt,Ft,tn=flat_torus(14); e0t,areaT=analyse(Vt,Ft,tn=tn,label="  [flat torus n=14]")
for t in (0.02,0.04,0.08,0.15,0.3,0.6):
    hs=float(np.sum(np.exp(-t*e0s)))-areaS/(4*np.pi*t)
    ht=float(np.sum(np.exp(-t*e0t)))-areaT/(4*np.pi*t)
    print(f"   {t:7.3f} {hs:28.5f} {ht:20.5f}", flush=True)
