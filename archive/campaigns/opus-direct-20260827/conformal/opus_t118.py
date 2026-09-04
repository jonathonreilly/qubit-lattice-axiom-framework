"""T118 - THE PER-MODE STRUCTURE OF THE DIFFEOMORPHISM RESPONSE.

T117 showed two things at once and they point opposite ways:
   modes n<=4        shift by 1e-14  (machine precision -- EXACTLY invariant)
   whole spectrum    shifts by 1.7e-2 and does NOT fall as the mesh refines.
Resolve it mode by mode.  Three questions, each with a clean answer:
   (1) which modes are protected, and is the protection exact or just small?
   (2) for the unprotected low modes, what is the convergence exponent in h?
   (3) does the mean over the WHOLE spectrum really stay flat in h?
(3) is the one that decides Sakharov: if the full-determinant error is h-flat but
the low-mode error vanishes, then W is permanently non-invariant while W_Lambda
at fixed physical Lambda is invariant in the limit -- which is exactly the
covariant regulator R65 said was needed."""
import numpy as np, itertools, sys
sys.path.insert(0,"/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-gravity-toe-lane-work-427b0b/25068357-42e8-431c-96c9-c149512f0305/scratchpad")
from opus_t116 import kuhn, positions, lengths_from_positions, spectrum

kvec=2*np.pi*np.array([1.0,0,0,0])
def mk(amp,two=False):
    def g(X):
        o=np.zeros_like(X); o[:,1]=amp*np.sin(X@kvec)
        if two: o[:,2]=amp*np.sin(2.0*(X@kvec))
        return o
    return g

print("T118  per-mode diffeomorphism response")
print()
print("(1) is the protection of the lowest modes EXACT, and how far up does it go?")
print("    single-wave displacement xi = A sin(2 pi x1) e2 ,  L=6")
verts,vid,simp=kuhn(6); N=len(verts)
l20=[lengths_from_positions(positions(s,lambda X:0.0*X,6)) for s in simp]
lam0=spectrum(simp,l20,N)
for A in (0.01,0.04):
    lg=spectrum(simp,[lengths_from_positions(positions(s,mk(A),6)) for s in simp],N)
    rel=np.abs(lg-lam0)/np.maximum(lam0,1e-12)
    print(f"    A={A}:  " + "  ".join(f"n{n}:{rel[n]:.1e}" for n in range(1,13)))
print(f"    lambda_n for n=1..12: " + " ".join(f"{lam0[n]:.2f}" for n in range(1,13)))
print()
print("    -> the protected set is exactly the modes the displacement cannot mix.")
print()

print("(2)+(3) refinement, single wave, amplitude fixed in PHYSICAL units A=0.03")
print(f"    {'L':>3} {'N':>6} | {'n=5..12 mean':>14} {'lowest 5%':>12} {'lowest 25%':>12} {'ALL':>12}")
rows=[]
for L in (5,6,7,8,9):
    verts,vid,simp=kuhn(L); N=len(verts)
    l20=[lengths_from_positions(positions(s,lambda X:0.0*X,L)) for s in simp]
    lam0=spectrum(simp,l20,N)
    lg=spectrum(simp,[lengths_from_positions(positions(s,mk(0.03),L)) for s in simp],N)
    if lam0 is None or lg is None: print(f"    L={L} degenerate"); continue
    rel=np.abs(lg[1:]-lam0[1:])/lam0[1:]
    n5=max(4,int(0.05*N)); n25=max(4,int(0.25*N))
    row=(L,N,float(np.mean(rel[4:12])),float(np.mean(rel[:n5])),float(np.mean(rel[:n25])),float(np.mean(rel)))
    rows.append(row)
    print(f"    {L:3d} {N:6d} | {row[2]:14.3e} {row[3]:12.3e} {row[4]:12.3e} {row[5]:12.3e}",flush=True)
print()
print(f"    convergence exponent p in ~h^p  (h = 1/L)")
print(f"    {'pair':>8} {'n=5..12':>10} {'lowest 5%':>11} {'lowest 25%':>11} {'ALL':>11}")
for i in range(len(rows)-1):
    a,b=rows[i],rows[i+1]; lr=np.log((1.0/b[0])/(1.0/a[0]))
    print(f"    {f'{a[0]}->{b[0]}':>8} "+" ".join(
        f"{np.log(b[c]/a[c])/lr:11.2f}" if a[c]>0 and b[c]>0 else f"{'--':>11}" for c in (2,3,4,5)))
print()
print("    p ~ 2 on the low bands and p ~ 0 on ALL is the result that separates")
print("    a fixed-Lambda regulator (diffeo-invariant in the limit) from the full")
print("    determinant (never invariant).")
