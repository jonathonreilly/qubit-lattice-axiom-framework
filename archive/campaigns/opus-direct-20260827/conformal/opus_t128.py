"""T128 - THE PLANCK LENGTH IN UNITS OF THE SPACING.  (determining the O(1) in R72)

R72 left G = 12 pi c a^2 with c undetermined, because tau_0 was an imposed
proper-time cutoff.  But in this framework NOTHING is imposed: the lattice IS the
regulator -- the spectrum is finite and bounded above by the spacing.  So the
effective tau_0 is not a choice, it is a property of the framework's own operator,
and it can be measured.

Match the two regulators on a quantity that needs no curvature at all, so the
closed 4D window of R67 never enters.  Differentiate the effective action in m^2:

   lattice:        dW/dm^2 = (1/2) Tr(Delta + m^2)^{-1} = (1/2) sum_i 1/(lambda_i + m^2)
   proper time:    dW/dm^2 = (1/2) int_{tau_0}^inf ds (4 pi s)^{-2} Vol e^{-s m^2}
                           -> (1/2) Vol/(16 pi^2 tau_0)   as m -> 0

so                 tau_0 = Vol / (16 pi^2 sum_i 1/(lambda_i + m^2)).

The sum is UV-dominated (mode density ~ lambda dlambda in d=4, so sum 1/lambda ~
Lambda^2), which is exactly why this converges fast in L and needs no curvature.

Then, with R72's  G = (3 pi/2) tau_0  for the Kahler-Dirac fibre,
   ell_Planck = sqrt(G) = sqrt(3 pi tau_0 / 2)   in units of the spacing a.

CONTROL: tau_0/a^2 must be L-INDEPENDENT.  If it drifts with L it is not a
property of the operator and the whole reading is void."""
import numpy as np, itertools, sys
sys.path.insert(0,"/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-gravity-toe-lane-work-427b0b/25068357-42e8-431c-96c9-c149512f0305/scratchpad")
from opus_t116 import kuhn, positions, lengths_from_positions, spectrum

print("T128  the framework's own cutoff, and the Planck length in units of the spacing")
print()
print("   Vol = 1 (unit 4-torus), spacing a = 1/L, so tau_0/a^2 = tau_0 L^2 must be")
print("   L-independent for the reading to mean anything.")
print()
print(f"   {'L':>3} {'N':>6} {'a=1/L':>8} {'sum 1/lambda':>14} {'tau_0':>12} {'tau_0/a^2':>11} {'G/a^2':>10} {'ell_P/a':>9}")
rows=[]
for L in (4,5,6,7,8):
    verts,vid,simp=kuhn(L); N=len(verts)
    l20=[lengths_from_positions(positions(s,lambda X:0.0*X,L)) for s in simp]
    lam=spectrum(simp,l20,N)
    m2=1e-6
    S=float(np.sum(1.0/(lam+m2)))      # zero mode regulated by m^2; its weight is O(1/N)
    Snz=float(np.sum(1.0/lam[1:]))     # and dropped entirely, as a cross-check
    tau0=1.0/(16*np.pi**2*Snz)
    G=1.5*np.pi*tau0
    rows.append((L,tau0*L*L,G*L*L,np.sqrt(G)*L))
    print(f"   {L:3d} {N:6d} {1.0/L:8.4f} {Snz:14.4f} {tau0:12.3e} {tau0*L*L:11.5f}"
          f" {G*L*L:10.5f} {np.sqrt(G)*L:9.5f}",flush=True)
print()
d=[r[1] for r in rows]
print(f"   tau_0/a^2 across L=4..8: spread {max(d)-min(d):.2e} on {np.mean(d):.5f}"
      f"  ({100*(max(d)-min(d))/np.mean(d):.2f}%)")
print()
print("   CROSS-CHECK by an independent route: mode counting.  The lattice has")
print("   exactly N = L^4 modes; a continuum cutoff Lambda admits Vol Lambda^4/(32 pi^2).")
print("   Equating:  Lambda^4 = 32 pi^2 L^4,  tau_0 = 1/Lambda^2 = a^2/sqrt(32 pi^2).")
print(f"      mode-counting tau_0/a^2 = {1.0/np.sqrt(32*np.pi**2):.5f}")
print(f"      measured      tau_0/a^2 = {np.mean(d):.5f}")
print(f"      ratio = {np.mean(d)*np.sqrt(32*np.pi**2):.4f}")
print()
print(f"   => ell_Planck / a = {np.mean([r[3] for r in rows]):.4f}")
print("   Two different definitions of 'the framework's cutoff' agreeing to O(1) is")
print("   the claim; agreeing exactly would be a coincidence, not a requirement.")
