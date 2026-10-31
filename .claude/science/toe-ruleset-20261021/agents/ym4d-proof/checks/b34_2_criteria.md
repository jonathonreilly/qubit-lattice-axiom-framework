# b34_2 — criteria (written 2026-10-29, BEFORE the script b34_2_rwcc.py exists)

Owner: BFT34_55.md (claude-opus-5-5). Exact rational arithmetic (fractions.Fraction), plain python, no floats.

## What is tested
The exact algebra of BFT34_55's Proposition RW-cc (cc-localised parametrix), in a finite-dimensional model with no
locality: X = Q^n, a symmetric positive semidefinite bilinear form Bf (matrix) whose kernel is exactly Ran D
(D: Q^g -> Q^n, the "gauge directions"), a right inverse R of D^T (D^T R = I_g; the "routing"), P_cc := I - R D^T,
cutoffs chi_b (diagonal, sum_b chi_b = I) and psi_b (diagonal, psi_b = 1 on supp y_b), local responses
u_b := (Bf + D D^T)^{-1} y_b, P~y := sum_b psi_b u_b, c(y) := sum_b (Bf psi_b u_b - psi_b Bf u_b).
Claimed identities, for every y with D^T y = 0 ("cc"):
- (I1) sum_b y_b = y, where y_b := P_cc chi_b y;
- (I2) Bf u_b = y_b (the local responses solve the full equation, not only on a slice);
- (I3) Bf P~y = y + c(y)  (the parametrix identity);
- (I4) D^T c(y) = 0  (the remainder is cc, although the single terms Bf psi_b u_b - psi_b Bf u_b are not).

## Instances
n = 12, g = 3, four "boxes" b; three seeds. D random integer full column rank; Bf := M^T M with
M := N (I - D (D^T D)^{-1} D^T), N a random 11 x 12 integer matrix; reseed unless rank Bf = n - g exactly (so that
ker Bf = Ran D). R := a sparse right inverse of D^T (columns supported on 3 coordinates each, solved exactly).
chi_b: random rationals in [0, 1] per coordinate, normalised to sum 1 over b. psi_b: 1 on supp y_b, random in [0, 1]
elsewhere. y := P_cc (random integer vector).

## PASS / FAIL (pre-registered)
- P1: (I1)-(I4) hold EXACTLY for every seed.
- P2: at least one single term t_b := Bf psi_b u_b - psi_b Bf u_b has D^T t_b != 0 in every seed (so (I4) is a
  cancellation, not termwise).
- Controls — each must FIRE, else the check is NON-DECISIVE (reported as a FAIL of the design):
  - K1 (non-cc input): y' with D^T y' != 0 and the same construction: (I3) must FAIL (sum_b y'_b = P_cc y' != y').
  - K2 (no routing): y_b := chi_b y (no P_cc), u_b := (Bf + D D^T)^{-1} y_b: (I2) or (I4) must FAIL.
  - K3 (psi_b != 1 somewhere on supp y_b): (I3) must FAIL.
Overall PASS iff P1, P2 hold and K1-K3 all fire.

## What this check cannot decide
Locality (finite reading/writing radii), the norm bounds (W-comm), (W-lin)^cc, the HR routing bounds, the walk
expansion's convergence, k-uniformity: none is tested. It tests only that the identity has no algebra or sign error.

## WITHDRAWN before any script was written (appended 2026-10-29T01:47Z)
Writing the construction out (before coding) shows the check cannot decide anything (systemic defect 3, a tautology):
with c(y) defined as sum_b (Bf psi_b u_b - psi_b Bf u_b) and psi_b y_b = y_b, one has identically
Bf P~y = c(y) + sum_b y_b, so (I3) <=> (I1); (I1) is linearity of P_cc plus sum_b chi_b = I; and (I4) follows from
D^T Bf = 0 and D^T y = 0 in one line. Every control would fire for the same definitional reason. The content of
Proposition RW-cc that a check would need to test is the LOCALITY/TRANSPLANT step (local-torus responses, pairing radius,
psi_b = 1 on the reading region), which a finite model without locality cannot test. No script b34_2_* exists; no
PASS is claimed. The identity is proved in BFT34_55 §2.5 instead.
