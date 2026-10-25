# J:derive:review-20261016-global-dirac-torus:a1 — global zero / pi touching set of the two-qubit Clifford walk family

Same-family (Claude Sonnet 5.5), unrefereed. Owner-requested research work; no status is claimed.
Reads done before choosing premises: `docs/MINIMAL_AXIOMS_2026-06-29.md` (full) and
`docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` (full) on main `a77a3449c9`. Source branch
`claude/toe-campaign-24h-20261015` at `b0178fa585cad5ac9e02e70dff2175593dbc5dab`; both source objects verified by
sha256 (see RECOVERY_STATUS.json). The current-main version of the note differs from the frozen one
(axis-doubler wording corrected to 0<|s|<1, k^6 coefficient corrected, Theorem 8 demoted to an archived
candidate). None of those differences touches the Gram matrix G(b) used here.

## Plain-language summary

The source writes a family of walks parametrised by three numbers b = (b0, b1, b2), allowed when a 4x4 matrix
G(b) is positive semidefinite (PSD) of rank at most 3. The question was whether the walk can touch quasienergy
0 or pi anywhere on the Brillouin torus other than the intended cone at k = 0. The source only checked a mesh.

Result (computer-assisted, exact algebra, for the family normalised to be massless at k = 0):

* For every allowed b other than b = 0, the walk touches quasienergy 0 at k = 0 and nowhere else. (b = 0 is
  the identity walk; it touches everywhere.)
* The walk touches quasienergy pi at no point, except for exactly 8 explicit values of b. Two of them are the
  source's light-speed member +-b_gold (three axis points). The other six are new: +-b_M (three face points,
  cone speed cos(pi/12) = 0.966, so s < 1) and four corner members with b2^2 = 7/396, b1^2 = 5/132, b0 = 3 b2
  (one corner point; they are two pairs of one spectrum relabelled by k -> k + (pi,pi,pi)).
* So "s < 1" does not make a member doubler-free: the axis doublers are gapped but the face or corner doublers
  can sit exactly at pi. The source's two named members b* and b_iso are not among the 8, hence they have no
  other zero/pi touching on the entire torus (their previous support was a grid).

## Setting, premises, and what is not new

* ASSUMED (A1): the site is C^2 (flavor) (x) C^2 (spin) with rotations acting as 1 (x) D(R). This lies outside
  the Qubit axiom's one-site algebra M_2(C) (axiom file lines 43-53); the M_4(C) fork is not adopted here. No
  dynamics clause is assumed: the axiom file (lines 114-123) says Admissibility does not choose a Hamiltonian or
  transfer operator, so the walk is a supplied model, not framework content. No primitive from the registry
  (scale reference, kinetic isotropy, realized state) is used.
* ASSUMED (A2): the Clifford ansatz U = f + i(h1 tau1 + h2 tau2) + i tau3 g.sigma with f,h1,h2 invariant and g
  equivariant, and the Gram parametrisation of the source (Theorems 1-2, frozen note lines 93-115): G(b) is
  uniquely fixed, a real factor F with F^T F = G exists iff G is PSD of rank <= 3, and F is unique up to O(3).
  The Gram identity is re-verified (check 0.1).
* ASSUMED (A3) (the "family" examined): the massless-at-0 normalisation F(0) = e_f, which exists for every
  allowed b (the source's Theorem 7). Then f(k) = phi0^T G phi(k), phi0 = (1,3,3,1), and bands are cos(omega) = f
  (each doubly degenerate). Rotations that do not fix F(0) are a different choice; see step 12.
* NOT NEW: local cone at k = 0, the four light-speed nodes (PR9658 follow-up; my Jacobian (check 4.3) reproduces
  the transverse speed sqrt5 - 2 = b0 - b2 at b_gold), s^2 <= 1, the TRIM gap formulas cos theta_X/M/R, the grid
  statements, the existence of b* and b_iso.

## Steps

1. PROVED. U(k) = f + iX, X^2 = 1 - f^2 (from the five anticommuting Hermitian involutions, source Theorem 1).
   Eigenvalues are exp(+-i omega), cos omega = f. U has eigenvalue +1 iff f = 1 and -1 iff f = -1. The zero/pi
   touching sets are T_0 = {f = 1}, T_pi = {f = -1}; there U = +-1 (all four bands meet).

2. PROVED (Lemma 1; identity checked exactly, check 0.5). Write psi_eps(k) = phi(k) - eps phi0. Exactly,
   psi^T G psi + |g|^2 = 2 - 2 eps f. If G is PSD and f = eps then psi^T G psi = -|g|^2 <= 0, so g(k) = 0 and
   G psi_eps(k) = 0. Conversely G psi_eps = 0 gives f = eps. Hence
   T_0 = {k : G(phi(k) - phi0) = 0}, T_pi = {k : G(phi(k) + phi0) = 0}, and both lie in Z(b) = {g = 0}.

3. PROVED (check 0.3, 0.4). g_a = sin k_a B_a(c) with B_a = b0 + b1(c_b + c_c) + b2 c_b c_c, c_a = cos k_a, and
   B_1 - B_2 = (c2 - c1)(b1 + b2 c3) (cyclic). So g = 0 iff for each a either c_a = +-1 or B_a = 0.
   phi depends on k only through c, and symmetrically; the problem is on the cube c in [-1,1]^3.

4. PROVED by exhaustion on which axes are interior (|c_a| < 1). Let A be the set of interior axes.
   * A empty: the 8 TRIM points; phi takes only the four values phi_0, phi_X, phi_M, phi_R.
   * |A| = 1, c = (x, e2, e3), e = +-1: B_1 = 0 is a linear condition (s = 0, b0 = b2, or b0 - 2b1 + b2 = 0).
   * |A| = 2, c = (g1, g2, eps): B_1 = B_2 = 0 gives (b1 + eps b2) g1 = (b1 + eps b2) g2 = -(b0 + eps b1). Either
     g1 = g2 = g (diagonal stratum), or b1 + eps b2 = 0 = b0 + eps b1, i.e. b = t(1,-1,1) (eps = 1) or
     b = t(1,1,1) (eps = -1), or no solution.
   * |A| = 3: by step 3's difference identities: all c equal (B(g) = 0); exactly two equal, then
     b1 = -b2 g, b0 = b2 g^2, b = B2 (g^2, -g, 1) with the third c free; or all distinct, then b1 = b2 = 0 and
     b0 = 0 (check 3.10).
   The lines t(1,-1,1) and t(1,1,1) and the line (0,b1,0) are not PSD for t != 0 (checks 1.1, 1.2, 1.3).

5. CHECKED (exact; sympy Groebner bases, ideal membership over C, check.py parts 2-3). For each stratum and each
   sign, the system G psi = 0 together with the stratum relation (and x != 1, g != 1 where psi would vanish) has
   complex solutions only in:
   * f = +1: {b = 0} or {b = t(1,-1,1)}, or b = (0,b1,0) (body diagonal). All non-PSD except b = 0.
     (TRIM classes X, M, R; axis lines; diagonal strata; two-equal stratum.)
   * f = -1, non-TRIM strata: no real solution in the cube at all (unit ideal, or x = 31/8, g = -2,
     roots of (g+4)(g^3+10g^2+17g-44) and of 8g^4+47g^3+138g^2+201g+141, none in [-1,1] / none real).
   * f = -1, TRIM classes: three zero-dimensional systems. X: b2 is a root of (19b2^2-71b2+11)(19b2^2+71b2+11),
     4 real points, 2 PSD (+-b_gold). M: b2 a root of the degree-8 polynomial
     65536 b2^8 - 163840 b2^6 + 90624 b2^4 - 26752 b2^2 + 529 (irreducible over Q), 4 real points, 2 PSD (+-b_M,
     b2 = +-0.14575653, b0 = 0.40457557, b1 = 0.20779686, s = (sqrt2+sqrt6)/4 to 60 digits). R: b2^2 = 7/396,
     b1^2 = 5/132, b0 = 3 b2 (exact, in Q(sqrt77, sqrt165)), 4 points, all PSD of rank 3.
   PSD of the M and R points is by 60-digit eigenvalues (the X and R point residuals G psi = 0 are verified
   exactly in radicals; for M exactly modulo the minimal relation). That PSD step is CHECKED numerically, not an
   interval proof.

6. PROVED modulo step 5 (T_0). For every allowed b != 0, T_0(b) = {k = 0}. For b = 0: G = diag(1,0,0,0), f = 1, so
   U = 1 and T_0 = the whole torus; T_pi is empty.

7. PROVED modulo step 5 (T_pi). For allowed b outside P = {+-b_gold, +-b_M, four b_R}, T_pi(b) is empty. At each
   member of P, T_pi is exactly one TRIM orbit: axis points (X) for +-b_gold, face points (M) for +-b_M, the
   corner (R) for the R members; no other TRIM class touches 0 or pi there (check 4.2).

8. CHECKED (exact Jacobian + 60-digit evaluation). At every node of P the Jacobian of g is nonsingular
   (X: diag(-s, b0-b2, b0-b2); M at (pi,pi,0): diag(-(b0-b2), -(b0-b2), b0-2b1+b2); R: -(b0-2b1+b2) 1), and
   pi - omega = |J q| (1 + O(q)), relative error 1e-7 at |q| = 1e-3. Each node is a massless Dirac cone at
   quasienergy pi, anisotropic at M. Speeds: R members have cone speeds (s, node speed) = (0.9211, 0.1426) or
   (0.1426, 0.9211); M members (0.9659 at k = 0; node velocities 0.2588, 0.2588, 0.1348 up to sign).
   PROVED (check 0.7, 4.5): the two R pairs are one spectrum relabelled by k -> k + (pi,pi,pi), omega -> omega + pi.

9. PROVED modulo step 5 (corollary). For allowed b != 0, s = b0 + 2b1 + b2 != 0: s = 0 gives w^T G w = s^2 = 0, so
   G w = 0, whose solutions are only b = 0 or the non-PSD line (check 3.12). The cone speed at k = 0 is
   strictly positive for every nonzero member; the rank-2 candidates of the source (speeds 0.017, 0.126) are
   consistent.

10. PROVED modulo steps 5-7 (global statement for named members). The source's b* = (11/30, sqrt u*, 3/20) and
    b_iso are allowed (check 5.1, 5.2), nonzero, and not in P (distances 0.037 and 0.045; TRIM cos values > -0.91).
    Therefore each has T_0 = {k = 0} and T_pi = empty on the whole torus, not only on a mesh.

11. CHECKED (numerical, disjoint method, check.py part 6). 6.9e3 admissible samples built from the quartic in b1^2
    (det G = 0) plus perturbations of P: min over a 25^3 k-grid of 1 + f is >= 0.32 at all 5.3e3 samples farther
    than 0.1 from P and below 0.02 only within 0.015 of P; 1 - f has no extra zero; at each P member the grid
    set {f = -1} equals the predicted orbit and {f = +1} is {0}. This corroborates but does not prove steps 6-7.

12. NOT DONE (first unresolved step). Other normalisations u = F(k1) of the same b (members massless at a point
    k1 of Z(b) other than 0). The touching sets of the member (b,u) are {k in Z(b): F(k) = +-u}; for u outside
    +-F(Z(b)) the member has no touching at all. Done only for TRIM-TRIM pairs (checks 3.13-3.15): F(T1) = F(T2)
    only at b = 0; F(T1) = -F(T2) only at the b1 -> -b1 images of the P systems, or non-PSD (X,M). Open: pairs
    (k1,k2) involving non-TRIM zeros of g (the diagonal points (g,g,+-1) exist for generic b when |g| < 1) —
    the two-point system G(phi(k1) -+ phi(k2)) = 0 on those strata.

## Other limits

* "Complete" is for the Clifford family with the massless-at-0 normalisation (A1-A3). Non-Clifford two-qubit
  covariant walks are not covered (the source's universality is numerical).
* Steps 5-7 depend on exact computer algebra that I did not re-derive by hand; the stratification itself
  (steps 3-4) is hand-argued and was the part most exposed to omission. Check 3.10, 3.5 and the numerical scan
  are the cross-checks. No second implementation or referee has seen this.
* The route is distinct from the source's Theorem 5 (which solves G v = 0 for the axis direction only).
* No physical claim: nothing here identifies a species or settles the positivity-to-C3 bridge.

## Files

check.py (65 checks, about 6 s), RECOVERY_STATUS.json.
