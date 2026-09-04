"""T115 - THE RATIO OF THE TT AND CONFORMAL COEFFICIENTS.
Result 64 claimed the graviton's SIGN and k^2 scaling but explicitly declined to
claim the coefficient, because an exactly-recurring -2/pi^2 is the signature of a
lattice identity (the trap that made Result 60 wrong).

A ratio is the way out.  Measure the TT and CONFORMAL second variations ON THE
SAME LATTICE, at the SAME wavevector, in the SAME units.  Lattice normalisation
constants cancel in the ratio, and continuum GR predicts a definite number for it.

Continuum, expanding int R sqrt(g) about flat to second order:
  * conformal   g -> e^(2 phi) g       gives  +6 int (d phi)^2       (Result 60/63)
  * TT          g -> delta + h^TT      gives  -(1/4) int (d h)^2  with the standard
                                       normalisation  |h|^2 = h_ab h_ab
So the predicted ratio, for perturbations normalised the same way, is a pure
number.  Rather than trust my continuum algebra, measure the ratio at several
wavevectors and lattice sizes and see whether it is (i) constant -- which is the
real test -- and (ii) what value it takes."""
import numpy as np, itertools
exec(open("/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-gravity-toe-lane-work-427b0b/25068357-42e8-431c-96c9-c149512f0305/scratchpad/opus_t114b.py").read().split('print("T114b')[0])
print("T115  ratio of TT to conformal second variation, same lattice, same k")
print("      (lattice normalisation cancels in the ratio; a CONSTANT ratio is the test)")
for L in (4,6):
    verts,vid,tops,edges,emid,edir,base_len=build(L)
    S0=S_of(tops,edges,base_len)
    print(f"\n   L={L}: S(flat) = {S0:.1e}")
    print(f"   {'n':>3} {'k^2':>10} {'d2S conformal':>15} {'d2S TT':>13} {'ratio TT/conf':>15}")
    kdir=np.array([1.0,0.0,0.0,0.0])
    eTT=np.zeros((4,4)); eTT[1,2]=eTT[2,1]=1.0
    for n in range(1,L//2+1):
        kv=2*np.pi*n*kdir
        k2=float(kv@kv)
        # CONFORMAL with the SAME plane wave: h_ab = phi delta_ab, phi = cos(k.x)
        # so an edge scales by 1 + (1/2) phi  (since u^a u^b delta_ab = 1)
        def ell_conf(eps):
            ell=base_len.copy()
            for key,e in edges.items():
                u=edir[key]; nu=np.linalg.norm(u)
                ell[e]=nu*(1.0+0.5*eps*np.cos(float(kv@emid[key])))
            return ell
        def ell_tt(eps):
            ell=base_len.copy()
            for key,e in edges.items():
                u=edir[key]; nu=np.linalg.norm(u); uh=u/nu
                hab=eps*np.cos(float(kv@emid[key]))*eTT
                ell[e]=nu*(1.0+0.5*float(uh@hab@uh))
            return ell
        eps=1e-3
        a=S_of(tops,edges,ell_conf(eps)); b=S_of(tops,edges,ell_conf(-eps))
        c=S_of(tops,edges,ell_tt(eps));   d=S_of(tops,edges,ell_tt(-eps))
        if None in (a,b,c,d):
            print(f"   {n:3d}  degenerate"); continue
        dc=(a-2*S0+b)/eps**2
        dt=(c-2*S0+d)/eps**2
        # normalise: the conformal h_ab = phi delta_ab has |h|^2 = 4 phi^2 in d=4,
        # while the TT h_ab = e_12 has |h|^2 = 2 eps^2.  Rescale to equal |h|^2.
        dc_n = dc/4.0; dt_n = dt/2.0
        print(f"   {n:3d} {k2:10.3f} {dc:15.6f} {dt:13.6f} {dt_n/dc_n:15.6f}", flush=True)
print()
print("   a CONSTANT ratio across k and L is the real result; its value is the")
print("   framework's prediction for the relative weight of the two sectors, and")
print("   the SIGN must be negative (they have opposite signs in GR).")
