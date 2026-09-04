"""T117 - THE REFINEMENT GATE ON THE DIFFEOMORPHISM RESPONSE.

T116 measured, on a fixed mesh, the eigenvalue shift caused by a pure
re-triangulation of flat space (moving the vertices).  It is ~1.6e-2 and FLAT
across the spectrum -- it does not climb into the UV.  So the first guess
("the diffeomorphism failure is a UV effect") is WRONG as stated.

But that does not close the route, because there is a second mechanism that a
flat relative error is entirely consistent with.  W = (1/2) sum_i log(lambda_i)
sums over ALL modes, and in d=4 the number of modes below lambda grows like
lambda^2.  A uniform relative error per mode therefore produces a total error
dominated by the count of UV modes, not by the size of any one error.  Cutting
at a fixed PHYSICAL Lambda keeps a fixed number of modes -- and the question
becomes whether the per-mode error on THOSE modes vanishes as h -> 0.

That is the refinement gate, and it is the honest test.  Fix the displacement
field in PHYSICAL units (a genuine diffeomorphism of the torus, independent of
the mesh), refine L, and track |dlambda_n|/lambda_n at fixed physical mode n.

  * falls as h^2  =>  the low spectrum is diffeomorphism invariant in the limit
                      (consistent with R23-R26), the failure is a finite-h
                      artifact, and a fixed-Lambda regulator is diffeo-invariant
                      in the continuum limit.  Sakharov reopens.
  * flat in h      =>  the operator is genuinely triangulation-dependent even in
                      the limit, and the route is closed for good."""
import numpy as np, itertools, sys
sys.path.insert(0, "/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-gravity-toe-lane-work-427b0b/25068357-42e8-431c-96c9-c149512f0305/scratchpad")
from opus_t116 import kuhn, positions, lengths_from_positions, spectrum, d

AMP = 0.02        # PHYSICAL displacement amplitude, in units of the torus side 1
kvec = 2*np.pi*np.array([1.0,0,0,0])
def gauge(X):
    out = np.zeros_like(X)
    out[:,1] = AMP*np.sin(X@kvec)
    out[:,2] = AMP*np.sin(2.0*(X@kvec))
    return out

print("T117  refinement gate on the diffeomorphism response")
print(f"      physical displacement field xi = {AMP} [sin(2 pi x1) e2 + sin(4 pi x1) e3],")
print("      held FIXED in physical units while the mesh refines.")
print()
print(f"   {'L':>3} {'h^2':>9} {'N':>6} | {'lam_1':>9} {'|dl|/l  n=1':>13} {'n<=4':>11} {'n<=10':>11} {'n<=40':>11} {'ALL':>11}")
prev=None
rows=[]
for L in (4,5,6,7,8):
    verts, vid, simp = kuhn(L); N=len(verts)
    l2_0=[lengths_from_positions(positions(s, lambda X: 0.0*X, L)) for s in simp]
    l2_g=[lengths_from_positions(positions(s, gauge, L)) for s in simp]
    lam0=spectrum(simp,l2_0,N); lamg=spectrum(simp,l2_g,N)
    if lam0 is None or lamg is None:
        print(f"   L={L}: degenerate simplex"); continue
    rel=np.abs(lamg[1:]-lam0[1:])/lam0[1:]
    def m(k): return float(np.mean(rel[:k]))
    row=(L,(1.0/L)**2,N,lam0[1],rel[0],m(4),m(10),m(40),float(np.mean(rel)))
    rows.append(row)
    print(f"   {L:3d} {row[1]:9.5f} {N:6d} | {row[3]:9.4f} {row[4]:13.3e} {row[5]:11.3e}"
          f" {row[6]:11.3e} {row[7]:11.3e} {row[8]:11.3e}", flush=True)

print()
print("   convergence exponents  p  in  |dlambda|/lambda ~ h^p   (successive pairs)")
print(f"   {'L pair':>10} {'n=1':>9} {'n<=4':>9} {'n<=10':>9} {'n<=40':>9} {'ALL':>9}")
for i in range(len(rows)-1):
    a,b=rows[i],rows[i+1]
    ha,hb=1.0/a[0],1.0/b[0]
    ps=[]
    for c in (4,5,6,7,8):
        if a[c]>0 and b[c]>0: ps.append(np.log(b[c]/a[c])/np.log(hb/ha))
        else: ps.append(float('nan'))
    print(f"   {f'{a[0]}->{b[0]}':>10} " + " ".join(f"{p:9.2f}" for p in ps))
print()
print("   p ~ 2 on the low modes = the refinement gate PASSES for the")
print("   diffeomorphism response, and a fixed-physical-Lambda regulator inherits it.")
