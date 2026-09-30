# Pre-registration, T49 (written before any script was run)

Question (lane's own cheapest test, L10-W1): is a charge-2 (Delta N = 2) term
forbidden by covariance alone, or is U(1)_N a free choice of the dynamics
clause?

Model tested (supplied, not derived; assumptions M1-M3):
- M1. The repo's emergent fermion: one mode c_v per coarse vertex v of Z^3,
  Kawamoto-Smit hopping H = -t sum eta_ij (c_i^dag c_j + h.c.), eta_1 = 1,
  eta_2 = (-1)^{v1}, eta_3 = (-1)^{v1+v2}
  (docs/CHARGE_CONJUGATION_..._2026-09-03.md, definitions block; I checked by hand
  that T_ij = (i/2) A_ij (B_i - B_j) = c_i^dag c_j + c_j^dag c_i).
- M2. The axiom group (translations, proper cubic rotations) acts on the qubit
  code by qubit permutation with trivial internal action. Then A_ij -> +-A_{gi,gj},
  B_v -> B_{gv}, so on the fermion it is a real signed permutation
  c_v -> s(v) c_{g v}. The signs s(v) are fixed (up to one global sign) by
  requiring the hopping term to be invariant.
- M3. Quadratic (free) sector only.

Object: for each displacement class D (orbit of d under the 24 proper cubic
rotations, merged with -d) on an 8^3 torus, the number of independent real
invariants of
  (P) a pairing form  sum_{v,w} Delta_vw c_v c_w   (Delta antisymmetric), and
  (H) a hopping form  sum h_vw c_v^dag c_w         (control).

Predictions (analytic, from bond-reversing C2 rotations):
- Control: nearest-neighbour hopping (1,0,0) has exactly 1 invariant.
- P1. Pairing has 0 invariants in every class with -d in O.d. That includes
  (1,0,0), (1,1,0), (1,1,1), (2,0,0), (2,1,0), (2,1,1), (2,2,1)... i.e.
  every class with a zero component or two equal |components|.
- P2. Pairing has >= 1 invariant only in classes whose three |components| are
  distinct and nonzero. Smallest on the torus: (1,2,3), |d| = sqrt(14).

PASS (for the "covariance protects U(1)_N up to range sqrt 14" reading):
 control = 1, P1 and P2 both hold.
FAIL / other readings:
 - any pairing invariant with |d| < sqrt 14  => a worked covariant charge-2
   extension exists inside the model: (C2-X) is refuted as a target and the
   wall becomes a pure choice (Dirac must be imposed).
 - control != 1 => machinery wrong; discard.
 - if the invariant appears only for classes P1 excludes => my sign
   bookkeeping is wrong; investigate before reading.

Side check (Part B, plain cubic, no KS signs): lowest degree of an odd
polynomial in k invariant under the 24 proper rotations. Predicted 9
(x y z (x^2-y^2)(y^2-z^2)(z^2-x^2)).

Part C (numbers for W2): Planck-scale-suppressed Weinberg operator
m = c v^2 / M_Pl, and the c that reaches 0.05 eV. No pass/fail; arithmetic.
