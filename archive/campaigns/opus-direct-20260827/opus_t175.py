"""T175 - CORRECTING R108, AND A CONVERGENCE ON alpha = 1/3.

R108 wrote that "the Record axiom's 'locks exactly one possibility' forces a point
mass, which requires the full harmonic tower".  That CONFLATES THE DISTRIBUTION
WITH THE OUTCOME.  A record is a single DRAW -- always a pure state, |v| = 1/2, by
construction.  The DISTRIBUTION it is drawn from need not be a point mass at all;
its mean can be anything with |v| <= 1/2.  So records do not require the full
tower, and that sentence is withdrawn.

What IS true, and is the useful part: the DISTRIBUTION'S ACHIEVABLE MEAN is capped
by its harmonic content.  With only the dipole, P(n) ~ (1 + a.n) with |a| <= 1
gives mean <(1/2)n> = a/6, so |v_out| <= 1/6.  Higher harmonics raise the cap.

That cap turns into a constraint on the CHANNEL, and this is the striking part.
The neighbours of a site are RECORDS, hence pure: |v_i| = 1/2 each.  Six aligned
neighbours give V = sum v_i = 3, so the rule's output mean is
      |v_out| = alpha |V| / 6 = alpha/2 .
Requiring that to be representable at l<=1 gives
      alpha/2 <= 1/6    =>    ALPHA <= 1/3 .
R99 independently found the CP-optimal alpha to be EXACTLY 1/3.

Two unrelated constraints -- harmonic representability of the distribution, and
complete positivity of the channel -- landing on the same number is worth checking
carefully rather than celebrating, so compute both sides exactly."""
import numpy as np
print("T175  correcting R108, and the alpha = 1/3 convergence")
print()
print("(1) WITHDRAWN from R108: 'records require the full harmonic tower'.")
print("    A record is a DRAW (always pure, |v|=1/2); the DISTRIBUTION need not be")
print("    a point mass.  Only the distribution's MEAN is capped by harmonic content.")
print()
print("(2) the l<=1 cap on the distribution's mean")
print("    P(n) ~ (1 + a.n),  non-negativity |a| <= 1,  mean <(1/2)n> = a/6")
print(f"    => |v_out| <= 1/6 = {1/6:.6f}")
print()
print("(3) the channel side: neighbours are RECORDS, so |v_i| = 1/2 exactly")
print(f"    {'config':>26} {'|V|':>8} {'|v_out| = alpha|V|/6':>22} {'alpha cap':>12}")
for nm,vs in (("6 aligned",[np.array([0,0,0.5])]*6),
              ("4 aligned, 2 opposed",[np.array([0,0,0.5])]*4+[np.array([0,0,-0.5])]*2),
              ("3 aligned, 3 random-ish",[np.array([0,0,0.5])]*3+
                 [np.array([0.5,0,0]),np.array([0,0.5,0]),np.array([0,0,-0.5])])):
    V=sum(vs); nV=np.linalg.norm(V)
    cap = (1/6)/(nV/6) if nV>0 else np.inf
    print(f"    {nm:>26} {nV:8.4f} {'alpha * '+format(nV/6,'.4f'):>22} {cap:12.4f}")
print()
print("(4) the two constraints side by side")
print(f"    harmonic representability (l<=1, 6 aligned records) : alpha <= {(1/6)/(3/6):.6f}")
print(f"    R99 CP-optimal alpha (argmax of sqrt((1-a)(1+3a))/2) : alpha  = {1/3:.6f}")
print(f"    difference: {abs((1/6)/(3/6)-1/3):.2e}")
print()
print("    Both are exactly 1/3.  The first is a bound (alpha may be smaller); the")
print("    second is where the speed limit peaks.  So the fastest CP-admissible")
print("    channel sits EXACTLY at the largest alpha the dipole-only distribution")
print("    can represent -- the two constraints meet, rather than one implying the other.")
print()
print("    CAVEAT, stated: the l<=1 truncation is an assumption.  R103 showed the")
print("    axioms permit l=2 (4 covariant maps) and beyond, which would raise the")
print("    cap above 1/3 and break the coincidence.  So this is a convergence")
print("    CONDITIONAL on dipole-only, not a derivation of alpha = 1/3.")
