"""T129 - INDEPENDENT CHECK OF THE LORENTZIAN GRAVITON'S -1/3.

A farmed lane reports the Lorentzian Regge graviton: d^2S exactly proportional to
eta^{ab} k_a k_b (9.9e-7 over 24 comparisons), POSITIVE for timelike k with the
conformal mode negative -- positive graviton energy -- and a TT/conformal ratio
of exactly -1/3 to 7 digits at every (L, n, k-type) point.

An exact rational recurring at finite spacing is precisely the signature that
burned this campaign in R60 (a "6.000000 to 7 digits" that was a lattice identity
matched against itself).  So -1/3 gets checked, two ways.

FIRST, derive the continuum ratio myself rather than take theirs.  For S = (1/2) int R sqrt(g):
  * conformal:  g = e^{2 phi} delta gives int R sqrt(g) = 6 int (grad phi)^2 to O(phi^2)
    (the same expansion T119 used).  With h_ab = eps cos(k.x) delta_ab, i.e.
    phi = (eps/2) cos(k.x):  int (grad phi)^2 = eps^2 k^2 V/8, so
    S^(2) = (1/2)(6)(eps^2 k^2 V/8)  =>  d^2S/d eps^2 = +(3/4) k^2 V.
  * TT:  d^2S = -(1/8)|e|^2 k^2 V, and for e = diag(0,1,-1,0), |e|^2 = e_ab e^ab = 2,
    so d^2S = -(1/4) k^2 V.
  RATIO = (-1/4)/(3/4) = -1/3.  Confirmed independently.  The number is right.

SECOND, and this is the real question: is -1/3 EXACT on the lattice because the
tensor structure is protected, or is it an accident of that one polarisation?
The lane's own data says the two TT polarisations DISAGREE at finite ka -- so the
lattice does break the polarisation degeneracy -- yet e22-e33 still gives exactly
-1/3.  The distinguishing feature is that e22-e33 and the conformal mode are both
DIAGONAL.  So the test is a SECOND diagonal transverse-traceless polarisation:
   e = diag(0, 1, 1, -2)   (transverse to spatial k along x1, traceless)
If the diagonal sector is protected by the lattice's residual hypercubic symmetry
it must also give exactly -1/3.  If it does not, -1/3 is special to one direction
and is not the continuum tensor structure.

Run in EUCLIDEAN signature with my own verified T114b machinery -- a different
signature, different code, different author from the claim being checked."""
import numpy as np, itertools, sys
sys.path.insert(0,"/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-gravity-toe-lane-work-427b0b/25068357-42e8-431c-96c9-c149512f0305/scratchpad")
from opus_t114b import build, S_of

print("T129  is the -1/3 the continuum tensor structure, or one polarisation's accident?")
print("      Euclidean signature, my own machinery.  Continuum ratio derived above: -1/3")
print()
pols={}
e=np.zeros((4,4)); e[2,3]=e[3,2]=1.0;              pols["e_23 (off-diag)"]=e
e=np.zeros((4,4)); e[2,2]=1.0; e[3,3]=-1.0;        pols["e_22-e_33 (diag)"]=e
e=np.zeros((4,4)); e[2,2]=1.0; e[3,3]=1.0; e[1,1]=-2.0;  pols["diag(0,-2,1,1)"]=e
e=np.zeros((4,4)); e[1,2]=e[2,1]=1.0;              pols["e_12 (off-diag)"]=e
CONF=np.eye(4)
for L in (4,6):
    verts,vid,tops,edges,emid,edir,base_len=build(L)
    S0=S_of(tops,edges,base_len)
    print(f"   L={L}:  {len(edges)} edges,  S(flat) = {S0:.2e}")
    print(f"      {'polarisation':>20} {'n':>3} {'d2S':>14} {'d2S/(k^2 V)':>14} {'ratio to conformal':>20}")
    for n in range(1,L//2+1):
        kv=2*np.pi*n*np.array([0.0,1.0,0.0,0.0]); k2=float(kv@kv)
        def d2(ep):
            def ell_of(s):
                ell=base_len.copy()
                for key,ei in edges.items():
                    u=edir[key]; nu=np.linalg.norm(u)
                    # perturb SQUARED length linearly, matching the Lorentzian convention
                    l2=nu*nu+s*np.cos(float(kv@emid[key]))*float(u@ep@u)
                    ell[ei]=np.sqrt(max(l2,1e-14))
                return ell
            h=1e-3
            return (S_of(tops,edges,ell_of(h))-2*S0+S_of(tops,edges,ell_of(-h)))/h**2
        dc=d2(CONF)
        for nm,ep in pols.items():
            v=d2(ep)
            print(f"      {nm:>20} {n:3d} {v:14.6f} {v/k2:14.6f} {v/dc:20.9f}")
        print(f"      {'conformal (delta_ab)':>20} {n:3d} {dc:14.6f} {dc/k2:14.6f} {1.0:20.9f}")
        print()
print("   Two diagonal polarisations both at exactly -1/3 = the lattice preserves the")
print("   continuum trace/traceless tensor structure in the diagonal sector, and the")
print("   ratio is physics.  Only one of them at -1/3 = it is an accident of direction.")
