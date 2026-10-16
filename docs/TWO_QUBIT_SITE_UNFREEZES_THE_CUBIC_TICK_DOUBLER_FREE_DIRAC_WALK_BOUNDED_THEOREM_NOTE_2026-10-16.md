---
claim_id: two_qubit_site_unfreezes_the_cubic_tick_doubler_free_dirac_walk_bounded_theorem_note_2026-10-16
claim_type: bounded_theorem
claim_scope: "Conditional on a two-qubit site C^2 (flavor) (x) C^2 (spin) with the proper cubic rotations acting as 1 (x) D(R) (outside the Qubit axiom's one-site algebra M_2(C); the parked M_4(C) fork is not adopted). Exact: walks U = f + i(h1 tau1 + h2 tau2) + i tau3 (x) g.sigma on the 27-point cell, with f, h1, h2 O-invariant and g O-equivariant, are exactly O-covariant, and are unitary iff f^2 + h1^2 + h2^2 + |g|^2 = 1; writing g = sum b_j v_j, this holds iff the uniquely determined Gram matrix G(b) is positive semidefinite of rank <= 3; an explicit algebraic b* satisfies det G(b*) = 0 with the other eigenvalues positive, so moving O-covariant one-tick walks exist on a two-qubit site. Exact: the cone speed s = b0 + 2 b1 + b2 obeys s^2 <= 1 and the axis doublers sit at quasienergy 2 arcsin|s|, so doubler-free on the axes iff s < 1; the light-speed member is unique up to sign, b_gold = ((9 sqrt5 - 5)/38, (5 sqrt5 - 7)/19, (71 - 29 sqrt5)/38), with f(t,0,0) = cos t and pi-mode doublers; a walk commuting with the chirality tau3 (x) 1 splits into two one-qubit covariant cell walks and is frozen, so moving covariant cell walks must break chirality. Numerical: the walk built from b* is unitary to 1e-15, has a single massless isotropic Dirac cone at k = 0 (speed 0.914) and gapped doublers at the seven other time-reversal-invariant momenta (gaps 2.20-2.31 rad); no other band touching on a 40^3 grid. Searches found no moving walk for the irreducible 4-dimensional coin (spin 3/2 = E (x) spin 1/2). Within the family nearest-neighbour-only walks are impossible (moving needs corner hops, b2 != 0); isolated rank-two members with h2 = 0 exist at small cone speed (independent Groebner computation). A one-qubit walk with sublattice-dependent coefficients (staggering) folds into this class with an extra twist symmetry and is then frozen (exact within the Clifford class; no staggered moving walk found numerically)."
upstream_dependencies:
  - minimal_axioms
  - cubic_covariance_freezes_a_one_qubit_tick_cell_classification_bounded_theorem_note_2026-10-16
runner: scripts/two_qubit_cubic_dirac_tick_2026_10_16.py
---

# A two-qubit site unfreezes the cubic tick: a doubler-free Dirac walk

**Date:** 2026-10-16
**Type:** bounded_theorem
**Status:** bounded-support; exact existence and characterization of a
declared walk family on a declared (non-axiom) site; numerical spectral
statements labelled; unaudited.

## Result up front

The companion note shows that on one qubit per site no unitary tick on the
27-point cell can be exactly covariant under the proper cubic group and move.
Doubling the site removes the obstruction, and the walks it admits have a
forced Dirac structure.

1. **Exact covariant motion on a two-qubit site.** With the cubic group acting
   on the spin factor only, the walks

       U(k) = f(k) + i (h1(k) tau1 + h2(k) tau2) (x) 1 + i tau3 (x) g(k).sigma

   are exactly O-covariant whenever f, h1, h2 are cubic-invariant and g is
   cubic-equivariant. Because the five matrices tau1, tau2, tau3 sigma_a
   anticommute, U is unitary iff f^2 + h1^2 + h2^2 + |g|^2 = 1.
2. **A one-condition classification of this family.** Writing
   g = b_0 (s_a) + b_1 (s_a(c_b + c_c)) + b_2 (s_a c_b c_c), the identity
   fixes the Gram matrix G of (f, h1, h2) over the invariant basis
   {1, sum c, sum cc, c1c2c3} uniquely in terms of b. The family is nonempty
   for b exactly when G(b) is positive semidefinite of rank at most three;
   rank three needs det G(b) = 0, a degree-eight equation even in b_1. The
   triple (f, h1, h2) is then a factor of G, unique up to a constant SO(3)
   rotation.
3. **An explicit member with one light Dirac fermion.** At
   b* = (11/30, sqrt(u*), 3/20), with u* the smallest positive root of the
   quartic det G = 0, G is positive semidefinite of rank three (exact). Using
   the rotation freedom to set (f, h1, h2)(0) = (1, 0, 0):
   - the bands are cos omega = f(k), each doubly degenerate;
   - at k = 0 the walk is a massless Dirac fermion with an isotropic cone,
     omega = 0.914 |k| + O(k^2) (g = (b_0 + 2 b_1 + b_2) k + O(k^3), and
     invariant h have zero gradient at k = 0);
   - the seven other time-reversal-invariant momenta, where g vanishes by
     symmetry, are gapped by 2.20–2.31 rad (numerical);
   - tau3 is the chirality; the h terms break it at O(k^2), as a Wilson term
     does, so the absence of doublers is consistent with Nielsen–Ninomiya.

4. **Speed and doubling trade off exactly.** For every member, s^2 <= 1:
   the cone moves at most one site per tick. The doublers at the three axis
   points (pi,0,0), (0,pi,0), (0,0,pi) sit at quasienergy 2 arcsin|s|, so
   they are gapped iff s < 1.
5. **A unique light-speed walk over the golden field.** s = 1 is attained
   only at b = +-b_gold with b_gold = ((9 sqrt5 - 5)/38, (5 sqrt5 - 7)/19,
   (71 - 29 sqrt5)/38). There f(t,0,0) = cos t exactly, the axes are
   light-like, and the axis doublers become massless pi-modes.
6. **Exact chiral symmetry freezes motion.** If a two-qubit O-covariant cell
   walk commutes with a flavor chirality tau3 (x) 1, it is block-diagonal and
   each block is a one-qubit O-covariant cell walk, hence constant by the
   companion note. Moving covariant matter on the cell must break chirality;
   the h terms are forced, not chosen.

## Premises and declared objects

- **Not framework content.** The two-qubit site C^2 (x) C^2 and the action
  1 (x) D(R) are hypotheses. The Qubit axiom fixes the one-site algebra M_2(C);
  enlarging it to M_4(C) is a parked owner decision
  (`docs/repo/DEFERRED_DECISIONS.md`, fork 4) that this note does not adopt.
  The result says what that enlargement would buy kinematically.
- **Walk and covariance** as in the companion note, with D(R) replaced by
  1 (x) D(R) on the doubled coin.
- **Cell functions.** c_a = cos k_a, s_a = sin k_a; the O-invariant cell
  functions are spanned by phi = (1, sum c_a, sum_{a<b} c_a c_b, c1 c2 c3) and
  the O-equivariant cell vectors by v_0 = (s_a), v_1 = (s_a (c_b + c_c)),
  v_2 = (s_a c_b c_c) (companion note, Theorem 1).

## Theorem 1 — covariance and unitarity of the Clifford family

Conjugation by 1 (x) D(R) fixes tau_j (x) 1 and maps tau3 (x) sigma.v to
tau3 (x) sigma.(Rv); with f, h invariant and g equivariant this gives
U(Rk) = W U(k) W^dagger, W = 1 (x) D(R). Write U = f + i X with
X = h1 Gamma_1 + h2 Gamma_2 + sum_a g_a Gamma_{2+a}; the Gamma's are Hermitian,
square to one and anticommute pairwise, so X^2 = h1^2 + h2^2 + |g|^2 and
U U^dagger = f^2 + X^2. ∎ (runner: exact matrix identities)

## Theorem 2 — the Gram criterion

For real coefficients, f^2 + h1^2 + h2^2 = phi^T G phi with G = F^T F, F the
3 x 4 coefficient matrix of (f, h1, h2). The map G -> phi^T G phi from
symmetric 4 x 4 matrices to cell functions is injective, and
phi^T G phi = 1 - |g|^2 has the unique solution

    G00 = 1 - 3 b0^2,   G01 = -2 b0 b1,   G02 = b1^2 - b0^2 - b0 b2,   G03 = -3 b1 (b0 - b2),
    G11 = b0^2 - 2 b1^2,  G12 = b1 (b0 - b2),  G13 = b0 b2 - b1^2 + b2^2,
    G22 = 2 b1^2 - b2^2,  G23 = 2 b1 b2,   G33 = 3 b2^2.

A real F exists iff G(b) is positive semidefinite of rank at most 3, and then
F is unique up to left multiplication by O(3). ∎ (runner: exact identity and
injectivity)

## Theorem 3 — an explicit algebraic member

With b0 = 11/30 and b2 = 3/20, det G is a quartic in u = b1^2 with three
positive roots; at the smallest, u* ≈ 0.0395524, det G = 0 and the coefficients
e1, e2, e3 of the characteristic polynomial are positive, so the three
remaining eigenvalues are positive (approximately 0.0173, 0.0529, 0.706).
Hence G(b*) is positive semidefinite of rank three and an O-covariant moving
walk exists. ∎ (runner: exact root-divisibility and sign evaluation)

## Theorem 4 — the speed bound and the axis doublers

On the axis line, phi(t,0,0) = v + w cos t with v = (1,2,1,0) and
w = (0,1,2,1), so F(t,0,0) = F v + F w cos t and g(t,0,0) = (s sin t, 0, 0)
with s = b0 + 2 b1 + b2. From G(b) one checks the identities
v^T G v = 1 - s^2, w^T G w = s^2 and v^T G w = 0. Since G >= 0, s^2 <= 1. The
cone at k = 0 has speed |s|. F(0).F(pi,0,0) = (v+w)^T G (v-w) = 1 - 2 s^2, and
|F| = 1 at both points (g vanishes there), so with F(0) on the f axis
f(pi,0,0) = 1 - 2 s^2 = cos(2 arcsin|s|). ∎

The explicit member above has s = 0.9144 and axis gap 2 arcsin(0.9144) =
2.308, matching the numerical spectrum. The same computation at the other
time-reversal-invariant classes gives, with F(0) on the f axis,

    cos theta_M = 1 - 8 s (b0 - b2)                       (three face points),
    cos theta_R = 1 - 6 (3 b0^2 + 2 b0 b2 + 3 b2^2 - 8 b1^2)   (corner point),

so the whole doubler spectrum is an explicit quadratic function of b.

## Theorem 5 — the light-speed member

s^2 = 1 forces v^T G v = 0, hence G v = 0 (G >= 0). The four polynomial
equations G(b) v = 0 have exactly four real solutions, ±b_gold and a second
pair at which G is indefinite. At b_gold, det G = 0, the other three
eigenvalues are positive (≈ 7.7e-4, 0.0432, 0.692), s = 1, and
f(t,0,0) = cos t. So the light-speed Clifford cell walk exists and is unique
up to sign and the internal SO(3) rotation; its axis doublers are massless at
quasienergy pi, while the face and corner doublers are gapped at 2.665 and
2.455 rad. ∎

**Dispersion of the light-speed member.** Exactly,

    omega^2 = |k|^2 - (7/6 - sqrt5/2) (|k|^4 - sum_a k_a^4) + O(k^6),

with 7/6 - sqrt5/2 ≈ 0.0486: light-like along the axes to this order and
slowest along the body diagonals, where the group velocity is
1 - 0.0486 (k a)^2. For every O-covariant walk the band functions are
O-invariant; the O-invariant polynomials on R^3 are generated in degrees
2, 4, 6 and 9, so omega(k) - omega(-k) = O(k^9) and the leading anisotropy
is quadratic in k a. This contrasts with the one-qubit D2 walk of the
companion note, whose leading correction is linear and handed
(-n1 n2 n3 |k|^2). That cubic symmetry pushes lattice anisotropy to
O(a^2) is standard; the new point is the contrast within these tick laws.

## Theorem 6 — exact chirality freezes motion

tau3 (x) 1 commutes with every coin operator 1 (x) D(R). If U commutes with
tau3 (x) 1 it is U_+ ⊕ U_- on the tau3 eigenspaces, and each U_± is a unitary
one-qubit walk on the cell, covariant under O with the spin-1/2 coin action.
By the companion note (Theorem 1) each is a constant. ∎ In the Clifford
family this says that h ≡ 0 is impossible for a moving walk; together with
Nielsen–Ninomiya it explains why the surviving walks are vector-like
(Dirac) with Wilson-type chirality breaking.

**Remark (no net chirality in the family).** Every Clifford walk has the
form U = cos theta + i sin theta n.Gamma with n in S^4 (five anticommuting
Gamma's), so U(k) lies in a copy of S^5 inside U(4). Since H^3(S^5) = 0, the
three-winding form restricts to an exact form there, and its pullback over the
closed torus integrates to zero: W_3 = 0 for every member (numerically
|W_3| < 1e-17 on a 24^3 grid for the explicit member). No member evades
fermion doubling through a Floquet (quasienergy pi) imbalance.

## Corollary — staggering one qubit per site does not unfreeze the tick

Keep one qubit per site but let the hop coefficients depend on the parity
p(x) = x1 + x2 + x3 mod 2 of the source site (a two-site cell). Rotations about
any site preserve parity, so each family A^{(p)} is O-covariant, giving
U_p(k) = sum_n A^{(p)}_n e^{i k.n}. With Q = (pi, pi, pi) and the projector
(Pi_p psi)(k) = (psi(k) + (-1)^p psi(k+Q))/2, the walk acts on
(psi(k), psi(k+Q)) as

    W(k) = [[S(k), D(k)], [D(k+Q), S(k+Q)]],  S = (U0 + U1)/2,  D = (U0 - U1)/2,

an O-covariant two-qubit cell walk with trivial flavor action and the extra
symmetry W(k+Q) = tau1 W(k) tau1. Suppose W is of the Clifford form in some
constant flavor frame (as all seven sampled two-qubit walks are). The twist is
then a flavor involution preserving that form, so it maps tau3 to eps tau3 with
eps = ±1 and forces g(k+Q) = eps g(k). Under k -> k+Q the vectors v0, v2 are
odd and v1 is even (exact). For eps = -1, b1 = 0 and G >= 0 gives G22 = -b2^2
>= 0, so b2 = 0, and then G02 = -b0^2 forces b0 = 0. For eps = +1, b0 = b2 = 0
and G13 = -b1^2 forces b1 = 0. Either way g = 0: no motion. So within the
Clifford class staggering is frozen (exact); for general two-qubit walks this
rests on the universality evidence above. Independent numerical searches of the
staggered problem itself (two coefficient families; 22 starts at motion bound
0.05 and 7 at 0.5) found no moving walk, with the same two
recurring minima (residuals 1.0e-5 at the bound, 9.5e-4). A genuinely doubled
site, not a two-site cell, is what the unfreezing needs.

## Numerical properties of the explicit member (labelled numerical)

| quantity | value |
|---|---|
| max ‖U U† − 1‖ over 2000 random k | 1.3e-15 |
| U(0) | 1 (massless point) |
| cone speed b0 + 2 b1 + b2 | 0.9144 |
| doubler gaps (rad) at the seven other TRIM points | 2.308 (three axis points), 2.196 (three face points), 2.198 (corner) |
| band touchings on a 40^3 grid | k = 0 only |

## Which sites unfreeze (search table and a criterion)

Analytic-Jacobian searches of the full O-covariant family on the cell, with a
scale-free lower bound on motion (δ = 0.05, and δ = 0.5 where the δ = 0.05
optimum sat in the quartic valley of the constant walk):

| coin (rep of the binary cubic group) | as spinor (x) flavor | moving walk found |
|---|---|---|
| spin 1/2 | spinor | none (exact freeze, companion note) |
| 2 x spin 1/2 | spinor (x) C^2, trivial flavor action | yes (this note) |
| spin 3/2 = E (x) spin 1/2 | spinor (x) E | none (16 + 16 starts) |
| spin 1 | not spinorial | none (20 starts) |
| spin 1 + spin 0 = spin 1/2 (x) spin 1/2 | spinor (x) spinor | none (16 + 16 starts) |
| 2 x spin 1 | not spinorial | none (16 + 12 starts) |

**Criterion (observed, proved only in part).** In the Clifford mechanism the
moving part is g.Gamma with Gamma_a a vector triple of anticommuting Hermitian
involutions (D Gamma_a D^dagger = sum_b R_ba Gamma_b). Such triples generate
Cl(3), whose representations are spinorial, so they need a spin-1/2 factor in
the coin; integer-spin coins have none. With one triple and no invariant
involution anticommuting with it, unitarity reduces to the companion note's
identity f^2 + |g|^2 = 1, which freezes (exact). The only coin in the table
with both ingredients, a spinor factor and an invariant anticommuting
partner, is 2 x spin 1/2: for spin 3/2 the flavor factor E is irreducible
(no invariant flavor generator, by Schur), and for spin 1/2 (x) spin 1/2 no
invariant anticommutes with the triple. In every case searched, cubic-covariant
one-tick motion appeared exactly when the site is a spin-1/2 doublet, i.e.
carries Dirac-spinor structure. Coins large enough for two anticommuting
triples are not covered.

## What did not unfreeze (search evidence, not proof)

- **Irreducible 4-dimensional coin.** Spin 3/2 restricted to the binary
  octahedral group is its irreducible 4-dimensional representation, equal to
  E (x) spin 1/2. Analytic-Jacobian searches (16 starts each, with a
  scale-free lower bound on motion) and polished pinned searches found no
  moving O-covariant cell walk for either form (best residuals 2.4e-3 and
  1.3e-3).
- **One extra square — corrected.** My searches for f^2 + h^2 + |g|^2 = 1
  with a single extra invariant (G of rank <= 2) found none, but they bounded
  the motion below by sum b^2 >= 0.2. The independent check (below) found, by
  an exact Groebner basis of the 3 x 3 minors of G, isolated rank-two points
  b ≈ (-0.0861, ±0.0272, 0.0144) (b2^2 the smaller root of
  27x^2 - 153432x + 32), where G ≈ diag-spectrum (0, 0, 0.0077, 0.978); their
  walks are unitary (4.6e-16) with slow cones (speeds 0.017, 0.126). So
  h2 ≡ 0 is possible at these points; rank two is confirmed to 40 digits but
  not proved.
- **Nearest-neighbour hops only** on the two-qubit site: impossible in the
  Clifford family (exact, independent check): G ⪰ 0 forces
  b0^2 >= 2 b1^2 >= 3 b2^2 and 3 b0^2 <= 1, any moving member needs
  b2 ≠ 0 (corner hops), and with b1 = b2 = 0 the identity forces b0 = 0. A
  general two-qubit search on the nearest-neighbour stencil also found none in
  20 starts.

**Universality evidence.** Unconstrained searches over the full 28-dimensional
O-covariant two-qubit cell family (analytic Jacobian, scale-free lower bound
on motion) found seven moving walks. For each, the real-linear condition
"U(k)(C (x) 1) has scalar Hermitian part for all k" has a 3-dimensional
solution space for the constant flavor matrix C, containing a unitary to
<= 4.2e-15; so every hit is of the Clifford form of Theorem 1 up to a constant
flavor gauge. That all two-qubit O-covariant cell walks have this form is
supported by these seven samples and is not proved.

**Local universality (numerical).** At each of the seven hits the Jacobian of
the unitarity equations on the 56-dimensional real covariant family has
nullity 9. At the explicit member the Clifford family's own tangent directions
(two along the det G = 0 surface, and the flavor gauge orbit, which has
dimension 7 and already contains the internal SO(3) rotations of (f, h1, h2))
span exactly 9 dimensions, all in that null space. So near every sampled walk
the solution variety coincides with the Clifford family; a separate component
that no search reached is not excluded.

## Independent check

A fresh agent context, given a neutral statement of the claims and no access
to this note or runner, rebuilt everything and confirmed: covariance and the
unitarity reduction (exact); uniqueness of G(b) (exact; the ten products
phi_i phi_j are independent); existence at b* by interval arithmetic on an
isolating interval of width 1e-45 for u* (the quartic
259200000000u^4 - 453744000000u^3 + 12644840000u^2 + 1185396800u - 39225499
is irreducible over Q); the spectrum, single cone, cone speed 0.9144223 and
doubler quasienergies (numerical); and the corrected one-extra-square and
nearest-neighbour statements above. Its scripts are kept in
`.claude/science/physics-loops/toe-campaign-20261015/independent_check_B3/`.
Limits of independence: same model family, new context and new
implementation.

## Relation to prior work

Wilson-type mass terms in discrete-time quantum walks, which lift doublers
at the price of chiral symmetry, are known (e.g. arXiv:1807.08303; doubling
in 3+1-dimensional Dirac walks is analysed in arXiv:2601.15885).
D'Ariano–Perinotti Dirac automata couple two Weyl automata on the
body-centred-cubic Cayley graph with a constant mass. New here, within the
framework's conventions: exact soldered cubic covariance of a single tick on
the simple cubic cell; the Gram-matrix characterization of the anticommuting
family; that this doubling is what lifts the one-qubit freeze, while the
irreducible 4-dimensional coin did not in the searches; and an explicit
member with exactly one light Dirac fermion.

## Bearing on the parked M_4(C) fork (information for the owner, not an adoption)

Fork 4 of `docs/repo/DEFERRED_DECISIONS.md` (enlarge the one-site domain from
M_2(C) to M_4(C)) wakes when a live lane hits the M_2(C) wall. The companion
note and this one locate such a wall for discrete-time motion: on the
27-point cell, M_2(C) admits no exactly cubic-covariant moving tick under any
soldering action, while M_2(C) (x) M_2(C) = M_4(C) does. The surviving walks
use a maximal anticommuting set in M_4(C): three lattice directions
tau3 sigma_a, whose product i tau3 makes tau3 the chirality, and two
directions with no lattice partner (tau1, tau2) carrying Wilson- and
twisted-mass terms. Generic members need both; only isolated rank-two points
use one. This is consistent with the archived proposal's reading of an extra
Clifford direction without a lattice partner; whether the carrier there
matches the repository's carrier is the audit question the fork records and
is not addressed here.

## What this does not do

- It does not adopt a two-qubit site, a dynamics clause or a tick.
- It does not classify all two-qubit O-covariant walks, or walks beyond the
  cell.
- It does not identify the walk with a physical fermion, fix its mass or
  speed, or couple it to anything.

## No-Go Discipline Gate

The only negative statements are search results, labelled as such in
"What did not unfreeze". N1–N8 do not apply to the positive theorems; the
negative searches name their routes (irreducible coin, single extra square,
nearest-neighbour stencil) and their evidence level, and make no
impossibility claim.

## Verification

```bash
python3 scripts/two_qubit_cubic_dirac_tick_2026_10_16.py
```

Expected: `TOTAL: PASS=24 FAIL=0` (a few seconds).
