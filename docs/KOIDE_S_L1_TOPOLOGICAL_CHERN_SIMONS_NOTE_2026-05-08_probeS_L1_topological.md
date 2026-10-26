# Supplied CS/knot diagnostics and corrected character-domain boundary

**Type:** bounded_theorem
**Date:** 2026-05-10; correction 2026-10-23
**Claim scope:** finite supplied mathematical comparisons and character-domain
controls; no general CS-to-beta impossibility theorem.
**Primary runner:** `scripts/cl3_koide_s_L1_topological_2026_05_08_probeS_L1_topological.py`
**Status authority:** independent audit lane only.

## Correction and complete recovery

The original universal O13 phase obstruction is false. The character map
[c] -> exp(2 pi i c) on R/Z admits arbitrary real classes. On a free cycle
Z, h(n)=n a mod1 is a flat character for every real a. Supplying
`a=1/(9 pi)` gives `exp(i 2/9)`. This counterexample does not derive that
choice physically or produce a beta-function coefficient.

For a class g of order three, additivity instead requires
`3h(g)=h(3g)=0 mod1`, hence h(g) is 0,1/3,2/3 mod1. The proposed c=2/9
fails this relation. This exact torsion restriction is not a restriction on
all differential characters or all Chern-Simons constructions. The corrected
[parent character note](KOIDE_A1_O13_CHEEGER_SIMONS_RZ_NO_GO_NOTE_2026-04-24.md)
provides the same domain distinction. No audit status is inferred from it.

The former note, runner and execution are preserved byte-for-byte in
`archive/notes/review_feedback/pr9845-consumers-2026-10-23/`.
The old literal-True authority checks, cardinality arguments, 19/47-style
count requirements and universal phase obstruction are historical, not live
proof. The prior claim that one integer cannot encode a rational vector is
not valid without restricting the decoding map. Differences in dimension,
metric or scheme expose missing matching data, not a proof that every bridge
is impossible. Those general impossibility claims are withdrawn.

## Preserved finite calculations

With the same supplied conventions and tolerances as the original runner:

- The level-k SU(3) representation count `(k+1)(k+2)/2` is compared with
  explicit enumeration for k=1,2,3,5,10.
- The supplied quantum integer
  `[3]_q=(q^(3/2)-q^(-3/2))/(q^(1/2)-q^(-1/2))`,
  q=exp(2 pi i/(k+3)), is evaluated at the same six levels. The finite
  reference values 1, phi, 2, 1+sqrt(2) and large-k comparisons remain.
  This is evaluation of the chosen convention, not a complete field theorem.
- The supplied trefoil Laurent polynomial `-q^-4+q^-3+q^-1` is evaluated
  at the same four SU(2) levels. Finite output and V(1)=1 are checked;
  the runner does not derive its skein formula or count printed values as
  a proof of algebraicity. Rationals lie in cyclotomic fields, so field
  membership cannot exclude the rational beta_2 comparators.
- `C_F=4/3`, `C_A=3`, `T_F=1/2`, N_f=6 and the original TVZ comparator
  vector `(2857/54,-1415/54,-205/18,79/54,11/9,1/2)` remain supplied.
  `beta_0=11-(2/3)N_f` gives 7 at N_f=6, different from h^vee=3.
  The unchanged tests at N_f=0,3,6,11,16 retain their negative result.
  The old all-N_f assertion is withdrawn: N_f=12 gives 3.
- The exact order-three Fraction checks and the numerical free-cycle
  counterexample distinguish the valid restricted obstruction from the
  false universal phase claim. Quotient invariance under an integer lift
  is also checked. Floating checks illustrate the exact formulas above.

## What remains open

No map from these finite CS/knot data to physical QCD beta_2 or beta_3
channel weights is constructed. The beta_2/beta_3 literature values are
comparators, not predictions. Scheme, metric/regulator and physical-source
identifications would have to be stated for any proposed bridge. This
failure to construct a map is not a no-go theorem, nor a proof that imported
loop integrals are the only possible route. No new axiom, physical selector,
retained status or lane closure is supplied.

The standard CS/knot formulas are imported conventions (Witten 1989,
Reshetikhin–Turaev 1991, Kauffman 1987); the QCD comparison coefficients are
from Tarasov–Vladimirov–Zharkov 1980 and van Ritbergen–Vermaseren–Larin 1997.
The original bibliography and full argument remain in the recovery copy.
The companion executes only the described finite calculations. Source hashes
certify provenance, not correctness; independent review remains required.
