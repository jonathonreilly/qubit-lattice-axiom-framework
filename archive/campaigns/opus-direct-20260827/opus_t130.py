"""T130 - WHERE IS THE PROPER-TIME WINDOW, REALLY?  (checking R75's root-cause claim)

The farmed bridge lane returns a qualified negative and pins the cause: the Kuhn
FEM Laplacian reportedly reaches the continuum a_0 only for tau_0 >~ 8 a^2, with
ratios Tr e^{-s Delta}/[(4 pi s)^{-2} Vol] = 1.16 (s=2), 1.07 (4), 1.03 (8),
1.016 (16) -- 1.6% error still at s = 16 a^2 -- concluding no window exists at
L <= 8 and L >~ 16 is needed.

That is in tension with my own T120, where the L=8 lattice matched the EXACT
torus heat trace (winding sum included) to 1.4e-6 at tau = 0.40, which in lattice
units is s = tau L^2 = 25.6 a^2.  Converting T120's numbers to a relative error
on K gives roughly 1% at s ~ 9 a^2 and 0.01% at s ~ 18 a^2 -- far better than
1.6% at s = 16.

This matters, and not academically: their fit ran at tau_0 in [0.5, 4].  If the
true window opens near s ~ 9-12 a^2 then the entire fit sat BELOW it, which would
explain the drifting B without any of it being about lattice size.  The remedy
would then be "refit at larger tau_0", not "build L = 16".

So measure it directly, against the right reference.  The continuum flat torus has
NO higher heat coefficients -- every a_k>0 vanishes -- so the exact answer is the
winding sum, and any deviation is pure lattice error:

    K_exact(s) = (4 pi s)^{-2} Vol * sum_{w in Z^4} e^{-|w|^2 (L a)^2/(4 s)}

Report, in lattice units, BOTH the lattice error and the winding contamination,
since the window is where both are small at once."""
import numpy as np, itertools, sys
sys.path.insert(0,"/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-gravity-toe-lane-work-427b0b/25068357-42e8-431c-96c9-c149512f0305/scratchpad")
from opus_t116 import kuhn, positions, lengths_from_positions, spectrum

def windsum(s,side,W=8):
    t=0.0
    for w in itertools.product(range(-W,W+1),repeat=4):
        n2=sum(x*x for x in w); t+=np.exp(-n2*side*side/(4.0*s))
    return t

print("T130  the proper-time window, in lattice units (a = 1)")
print()
for L in (6,8):
    verts,vid,simp=kuhn(L); N=len(verts)
    l20=[lengths_from_positions(positions(s_,lambda X:0.0*X,L)) for s_ in simp]
    lam=spectrum(simp,l20,N)/(L*L)      # rescale to a = 1: lengths x L, so lambda / L^2
    Vol=float(N)                        # N cells of unit volume
    print(f"   L={L}  (torus side {L} a, Vol = {Vol:.0f} a^4)")
    print(f"      {'s/a^2':>7} {'K_lat':>13} {'leading only':>14} {'K_exact(wind)':>14}"
          f" {'LATTICE err':>12} {'winding frac':>13}")
    for s in (0.05,0.1,0.2,0.5,1.0,2.0,4.0,8.0,16.0):
        Kl=float(np.sum(np.exp(-s*lam)))
        lead=Vol/(4*np.pi*s)**2
        ws=windsum(s,float(L))
        Ke=lead*ws
        print(f"      {s:7.1f} {Kl:13.5f} {lead:14.5f} {Ke:14.5f}"
              f" {abs(Kl-Ke)/Ke:12.2e} {ws-1.0:13.2e}",flush=True)
    print()
print("   The window is where BOTH last columns are small.  'Lattice err' is what the")
print("   bridge lane measured as 1.6% at s=16; 'winding frac' is what it would have")
print("   been measuring instead if its reference was the leading term alone.")
