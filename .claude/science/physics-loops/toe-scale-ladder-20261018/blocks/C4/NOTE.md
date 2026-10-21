# C4 — Cubic-covariant one-qubit Clifford QCAs on Z^3

**Block:** C4 of `toe-scale-ladder-20261018` (target: `SCALE_LADDER_MAP.md`, section C4).
**Date:** 2026-10-18.
**Status:** Independently reviewed (REVIEW.md); unaudited. No axiom, primitive or dynamics clause
is adopted.

## Result up front

1. **Soldered actions freeze Clifford QCAs dynamically (exhaustive certificates).** Take one
   qubit per site of Z^3 and a translation-invariant Clifford QCA α, covariant under the proper
   cubic group O acting by the **axis** or the **full** soldering action.
   - **Cell.** If the image of each single-site Pauli lies in the 27-point cell {-1,0,1}^3, then α
     is the identity automorphism, phases included.
   - **125-ball.** If the images may lie in {-2..2}^3, there are exactly 4 such QCAs, phases
     included, for each of axis and full. They are the identity and 3 entangling involutions
     (α^2 = id, period 2 with phases). Two of them are proved to be finite-depth circuits of
     commuting covariant Pauli rotations, α = ∏_r exp(±iπ/4 P_r):
     - P = X(±x) Y(±y) Z(±z), Chamon's octahedral stabilizer (`docs/ONE_QUBIT_..._2026-10-17`);
     - P = the 12-site cuboctahedral string X on (0,±1,±1), Y on (±1,0,±1), Z on (±1,±1,0).

     The structure of the third is not established. All four have constant trace, so nothing
     propagates (Theorem 2).
   - **Prediction checked.** I had predicted "identity only at radius 2". **That prediction
     failed** (`logs/c4_06_radius2.txt` keeps the two FAIL lines). The dynamical freeze survives.
2. **The unsoldered actions allow genuinely entangling, ballistically spreading QCAs
   (exhaustive certificate plus proof).** For the **trivial** action there are 528 such QCAs
   with phases (132 without phases); for the **sign** action there are 176. Every one has the
   form C1 · E(g) · C2. Here C1 and C2 are on-site Cliffords and E(g) is one O-symmetric layer
   of commuting CZ gates (plus an optional S gate), placed along an O-orbit polynomial g. So every
   one is a finite-depth circuit with no shift. 84 of the 132 unsigned matrices have a
   nonconstant trace. For the trivial action all 84 admit valid phases (336 signed QCAs). For the
   sign action only 14 do (56 signed). These spread ballistically with a sharp linear light cone, and they have no
   glider. The fifth Clifford realisation of the sign character, **sign-f**, gives only
   involutions (16 unsigned, 32 signed).
3. **There are no gliders at any range under O or T (proved theorem).** This holds for every
   one-qubit translation-invariant Clifford QCA on Z^3 that is covariant under O or T, for any
   Clifford-valued soldering action and **any finite range**. It is a trichotomy in τ = tr M:
   - τ ∈ {0,1}: periodic, with M^2 = 1 or M^3 = 1.
   - τ nonconstant: no nonidentity finite Pauli operator ever returns to a translate of itself.
     Every such operator's support diameter grows without bound, and the front reaches
     n·vert(Newt τ) at step n.

   A glider (an operator translating by r ≠ 0) needs τ = x^r + x^{-r}. That needs an orbit {±r},
   which O and T do not have. D4, D3 and D2 do have such orbits, and gliders appear there: along
   the fourfold axis (D4) and the body diagonal (D3), but only for the trivial and sign actions.
4. **Answer to the C4 prediction.** For axis and full soldering the *dynamical* prediction holds
   at ranges 1 and 2: nothing moves, no glider appears, and nothing spreads.
   - Range 1: only the identity survives.
   - Range 2: covariant entangling involutions appear. They are Pauli-rotation circuits built on
     Chamon-type commuting strings, so the literal "on-site Clifford × translation only" is false
     at range 2.
   - Unsoldered actions (trivial, sign): here the prediction **fails** already at range 1.
     Entangling covariant circuits exist and spread ballistically. They are still trivial as
     QCAs (circuits, no shift), and none has a mobile localized excitation.

## Setup and premises (all supplied; named)

- **Lattice and Qubit axioms** (`docs/MINIMAL_AXIOMS_2026-06-29.md`): Z^3, translations, the
  proper cubic group O about each site, and M_2(C) per site.
- **(D-QCA), supplied dynamics premise.** One tick is a translation-invariant *Clifford* QCA α
  on the quasi-local Pauli algebra. It is a *-automorphism that maps Pauli strings to Pauli
  strings, and the image of each single-site Pauli is supported in N + site, where N is the
  Chebyshev ball of radius 1 (the 27-cell), or radius 2 where stated. Not covered: QCAs that are
  not Clifford.
- **(S), soldering action.** We follow exactly the convention of
  `docs/ONE_QUBIT_CUBIC_COVARIANT_NEAREST_NEIGHBOUR_STABILIZER_RULES_..._2026-10-17.md` and its
  runner. A homomorphism Q: O → SO(3) sends σ_a at r to Σ_b Q(R)_{ba} σ_b at Rr. We write β_R for
  this map. The menu actions come from
  `docs/THE_SOLDERING_MENU_FOUR_ACTIONS_..._2026-09-22.md`: trivial; sign diag(1,s,s); axis s|R|;
  full R. Each Q(R) is a signed permutation matrix of determinant 1. The runner checks that each is
  conjugation by an explicit SU(2) unitary, so β_R is a Clifford automorphism.
- **Covariance.** α ∘ β_R = β_R ∘ α for all R ∈ H, with H = O unless stated. We test it with
  phases, on X_0 and Z_0, for every R.
- **Neighbourhood choice and why.** We use the 27-cell, Chebyshev radius 1. This is the
  "range-1" stencil of the companion free-walk freeze note
  (`docs/CUBIC_COVARIANCE_FREEZES_A_ONE_QUBIT_TICK_CELL_..._2026-10-16.md`). It contains the
  axis (seven-site star) neighbourhood of the 2026-10-17 stabilizer note, the face-diagonal
  neighbourhood and the body-diagonal neighbourhood. A classification on the cell therefore
  restricts to each of them: the star-supported solutions are exactly the listed solutions whose
  polynomials use only the centre and face orbits.

**The fifth action.** Up to SO(3)-conjugacy the menu has four entries. A Clifford QCA, however,
sees the action only up to conjugacy by *Clifford* unitaries, which form the octahedral group. The
runner enumerates all homomorphisms O → O exhaustively and finds 58. They fall into **5**
Clifford classes, with sizes 1, 3, 6, 24, 24. Four classes are the menu. The fifth, **sign-f**,
sends odd rotations to a *face-diagonal* half turn, for example (0,1,1): X→−X, Y↔Z. It is
SO(3)-conjugate to the sign action but not Clifford-conjugate to it. We cover it too, so the
classification includes every Clifford-valued soldering action.

## Method (symplectic Laurent formalism)

A Clifford QCA with one qubit per site has a 2×2 matrix M over R = F_2[x^±, y^±, z^±]. Its
columns are the (X-part; Z-part) polynomials of α(X_0) and α(Z_0) (Haah; Schlingemann–Vogts–Werner
2008). α preserves commutation exactly when M^† Λ M = Λ, with Λ = [[0,1],[1,0]] and † meaning
transpose plus antipode. In components:

- ⟨v_X, T_t v_X⟩ = 0 and ⟨v_Z, T_t v_Z⟩ = 0 for every t;
- ⟨v_X, T_t v_Z⟩ = δ_{t,0}.

Symplecticity implies invertibility, M^{-1} = Λ M^† Λ, so every survivor is an automorphism.

The covariance relations, with phases dropped, are **linear over F_2**: v_{ρ(R)a} = B_R v_a. Their
solution space W is computed by exact F_2 elimination; on the cell, dim W = 7 to 36. Its elements
are then enumerated **exhaustively** under the quadratic conditions, imposed over all overlapping
translates t ∈ {-2..2}^3. Two enumerators are used:

- brute force over span(W);
- a split enumerator: loop over the X-image, solve the linear system for the Z-image exactly, and
  filter.

The two agree wherever both run (O and T, all actions; D4, all actions). Every survivor is
re-verified in Laurent-polynomial arithmetic. Phases are then fixed by testing the four sign
choices against the signed covariance relation for every R. A third count for H = O,
`c4_05_independent_O.py`, uses a different route: orbit labelling, explicit complex Pauli
matrices, and commutation counting, with no F_2 linear algebra and no shared enumerator.
It reproduces 528 / 176 / 32 / 1 / 1 signed QCAs, and in the axis and full cases the identity (`logs/c4_05_independent_O.txt`, PASS=7 FAIL=0). Disclosure: its expected constants were taken from c4_02's output. It is a cross-route comparison, not a blind prediction.

## Theorem 1 — O-covariant classification on the 27-cell (exhaustive certificate)

| action | dim W | unsigned M | signed QCAs | on-site (unsigned) | τ nonconstant | structure |
|---|---|---|---|---|---|---|
| trivial | 16 | 132 | 528 | 6 | 84 | = {C1 E(g) C2 : C_i ∈ SL2(F2), g ∈ V} exactly |
| sign | 16 | 132 | 176 | 6 | 84 | same 132 matrices; phases cut to 176 |
| sign-f | 10 | 16 | 32 | 2 | 0 | all τ = 0 (involutions); ⊂ C1 E(g) C2 |
| axis | 7 | 1 | 1 | 1 | 0 | identity only |
| full | 7 | 1 | 1 | 1 | 0 | identity only |

Here V is the 16-element F_2-span of the four O-orbit sums on the cell: centre, 6 faces,
12 edges, 8 corners. Each orbit is closed under r → −r, so every g ∈ V is self-adjoint, and
E(g) = [[1,0],[g,1]] is the circuit made of S^{g_0} at every site together with a CZ between r
and r+n for each pair ±n in g. E(g) is O-covariant for the trivial action. Every solution has
det M = 1. Counts are constant on every Clifford-conjugacy class of actions (all 58
homomorphisms were run separately). Log: `logs/c4_02_classify_O_r1.txt`.

*Claim type:* exhaustive finite certificate, exact over F_2, with phases. *Domain:* the radius-1
cell, H = O, the five Clifford actions, one qubit per site.

## Theorem 1b — radius 2, H = O, soldered actions (exhaustive certificate) — `logs/c4_06_radius2.txt`, `logs/c4_07_radius2_analysis.txt`, `logs/c4_08_circuit_decomposition.txt`

On the 125-ball the covariance space has dim W = 25 for both axis and full. Z is determined by X,
so 2^25 X-images are enumerated exhaustively and the conditions are checked over all 729 overlapping
translates. The result is **4 unsigned / 4 signed QCAs for each action**:

- [0] the identity;
- [2] α = ∏_r exp(iπ/4 C_r), where C = X(±x) Y(±y) Z(±z) is the Chamon octahedron.
  Its matrix is M = 1 + v v^†Λ with v = (s_x + s_y, s_y + s_z) and s_a = x_a + x_a^{-1}, checked
  exactly.
- [1] the same construction with the 12-site cuboctahedral string. It is confirmed with phases
  by the independent reviewer (REVIEW.md, rv_circuits.log), and so is [2]. The sign of the
  exponent does not matter.
- [3] a 73-site-image involution. Its structure is **open**: it is not decomposed here, and the
  reviewer did not decompose it either.

All four have τ = 0, M^2 = 1 and signed period 1 or 2. The four are *not* closed under
composition within radius 2: the closure check FAILs in c4_07, so some products have larger range.
Mechanism: any covariant Pauli string P whose translates all commute gives a covariant QCA
∏_r exp(iπ/4 P_r) of range diam(P), provided the phases are consistent. On the 27-cell no such
QCA has images inside the cell, because the images of 1 + v v^†Λ reach twice the radius of P.
That is why radius 1 has only the identity.

## Theorem 2 — trace trichotomy, light cone and glider no-go (proved; any range)

Let α be a translation-invariant one-qubit Clifford QCA on Z^d, of any finite range, with matrix
M. Suppose α is covariant under a group H of lattice rotations through some Clifford-valued action,
and H fixes no nonzero vector. O, T, D4, D3 and the axis D2 all satisfy this. Put τ = tr M.

(a) det M = 1, and τ is H-invariant.
(b) If τ = 0 then M^2 = 1; if τ = 1 then M^3 = 1. With phases, α has period dividing 4 or 6.
    The runner observed periods 1, 2, 3 and 4.
(c) If τ is nonconstant, write P = Newt(τ); then 0 ∈ P. For every n ≥ 1 and every vertex v of P,
    the monomial x^{nv} occurs in tr(M^n). So α^n(X_0) has an X/Y factor at site nv, or
    α^n(Z_0) has a Z/Y factor there. The support of α^n(P_0) lies in n·N. This is a ballistic
    front, linear in n, exact at every n, not only asymptotically.
(d) A *glider* is a finite Pauli operator Q ≠ 1, with n ≥ 1 and t ∈ Z^d, such that α^n(Q) ∝ the
    translate of Q by t. A glider with t ≠ 0 exists **iff** τ = x^r + x^{-r} for some r ≠ 0.
    An operator recurring in place (t = 0) exists iff τ is constant. Consequently:
    - If τ is nonconstant **and not of the form x^r + x^{-r}**, every nonidentity finite Pauli
      operator has support diameter tending to infinity under iteration. The glider form is
      nonconstant, but it carries bounded gliders; the D4 and D3 rows below contain them. This
      fix is from review issue C-1. It does not change any O or T conclusion, because the glider
      form cannot occur under O or T.
    - Under H = O or T there is no glider at any range, for every action. τ is H-invariant, and
      x^r + x^{-r} is H-invariant only if H·r ⊆ {±r}, which forces r = 0 for O and T.

*Proof.*
(a) Covariance gives M ↦ ρ̃(R) M^{R} ρ̃(R)^{-1}, where ρ̃(R) ∈ SL_2(F_2) is the action's symbol
    and M^R is M with monomials substituted. So tr and det are R-invariant. det M is a unit, a
    monomial x^m, because det M · det M^† = 1. If m is fixed by H then m = 0.
(b) Cayley–Hamilton in characteristic 2: M^2 = τM + 1.
(c) Let λ be a root of λ^2 + τλ + 1. Then tr(M^n) = λ^n + λ^{-n} = D_n(τ), with D_0 = 0,
    D_1 = τ and D_n = τD_{n-1} + D_{n-2}. D_n is monic of degree n in τ, and only powers
    τ^{n-2j} occur. H-invariance puts the centroid 0 in P. Take a linear functional maximised on
    P only at v; then ℓ(v) > 0. In τ^n the coefficient at nv is 1, as a product of vertex
    coefficients. Every τ^{n-2j} with j ≥ 1 has Newton polytope (n−2j)P, which does not contain
    nv. Finally tr(M^n) = (M^n)_{11} + (M^n)_{22}.
(d) M^n v = x^t v with v ≠ 0 requires det(M^n − x^t) = 0, so some eigenvalue satisfies
    λ^{±n} = x^t.
    - If λ ∈ Frac(R): λ is a root of a monic polynomial over the integrally closed ring R with
      product of roots 1, so λ is a monomial x^r and τ = x^r + x^{-r}. Then t = nr, and the
      eigenvector gives a glider with n = 1.
    - If λ ∉ Frac(R), with τ ≠ 0 so the equation is separable: Galois conjugation sends λ to
      λ^{-1} and fixes x^t. So λ^n = λ^{-n} = x^t, hence x^{2t} = 1, t = 0, and λ is a root of
      unity. Then τ = λ + λ^{-1} is algebraic over F_2 and lies in R, so τ ∈ F_2.
    - Unbounded support: if supports stayed bounded, then up to translation only finitely many
      operators could occur. By pigeonhole, α^{n}(Q) would be a translate of α^{m}(Q), giving a
      glider or a recurrence.
∎

Checked on instances (`logs/c4_04_dynamics.txt`) for all 168 spreading-class unsigned solutions
(trivial and sign) and n ≤ 8: Cayley–Hamilton, the Dickson identity, the vertex claim, the cone
bound, and the absence of glider eigenvalues. *Numerics (evidence, not proof):* there are 28
representatives, one per (action, orbit shapes of τ, orbit shapes of M), iterated exactly over F_2
up to n = 32 from both X_0 and Z_0. For all 28, the Chebyshev front radius equals n at every step,
so the front saturates the cell light cone even when Newt(τ) is only the octahedron. log |supp|
against log n has slope 1.9 to 2.7, below 3, so the support is a sparse, fractal-like subset of
the cone, as expected from Frobenius in characteristic 2. Example: τ = 1 + face orbit gives
|supp α^n(X_0)| = 7, 37, 199, 1069, 5743 at n = 2, 4, 8, 16, 32.

**Twisted versions.** TR-twist conjugation sends α to α^{-1}, and tr M^{-1} = tr M, so τ is still
invariant and Theorem 2 still applies. For twisted (ρ_in ≠ ρ_out) intertwiners Theorem 2 does not
apply directly, but there are no signed solutions (below).

## Subgroups (exhaustive certificate, 27-cell) — `logs/c4_03_subgroups_*.txt`

| H | action | unsigned | signed | on-site | periodic | glider | spreading |
|---|---|---|---|---|---|---|---|
| T | trivial / sign / sign-f | 132 each | 528 each | 6 | 48 | 0 | 84 |
| T | axis | 3 | 3 | 3 | 3 | 0 | 0 |
| T | full | 3 | 1 | 3 | 3 | 0 | 0 |
| D4 | trivial | 780 | 3120 | 6 | 192 | 6 (along the 4-fold axis) | 582 |
| D4 | sign | 780 | 1040 | 6 | 192 | 6 (2 with valid phases) | 582 (132 with valid phases) |
| D4 | sign-f | 64 | 128 | 2 | 64 | 0 | 0 |
| D4 | axis | 64 | 128 | 2 | 64 | 0 | 0 |
| D4 | full | 64 | 64 | 2 | 64 (32 with valid phases) | 0 | 0 |
| D3 | trivial | 600 | 2400 | 6 | 198 | 12 (along the 3-fold axis) | 390 |
| D3 | sign | 600 | 800 | 6 | 198 | 12 (4 valid) | 390 (64 valid) |
| D3 | sign-f | 64 | 128 | 2 | 64 | 0 | 0 |
| D3 | axis / full | 2 each | 2 each | 1 | 2 | 0 | 0 |
| D2 | trivial / sign / sign-f / axis (all restrict to the trivial action on D2) | 4020 each | 16080 each | 6 | 768 | 18 (along all three axes) | 3234 |
| D2 | full | 4020 | 2680 | 6 | 768 (382 valid) | 18 (**0 valid**) | 3234 (**288 valid**) |

For T, the sign and sign-f actions restrict to the trivial action, because T = A4 is their
kernel. For D2 = V4, the axis action restricts to the trivial action too. "periodic / glider / spreading" counts unsigned matrices; "valid" means at least one phase
choice is covariant.

**What this says about motion with soldering.** Under axis or full soldering, no subgroup of
order ≥ 6 (T, D4, D3) allows any glider or any spreading Clifford QCA on the cell; everything is
periodic. This differs from the single-particle walk freeze, where D4 and D3 permit axial
conditional shifts. Those walks are U(1)-number-conserving linear walks, which are not Clifford
QCAs. Under the unsoldered actions, D4 and D3 allow gliders along their distinguished axis. This
is consistent with Theorem 2(d).

## Twists: inner Clifford twist, time reversal

- **Different input and output soldering**, α β^{ρ}_R = β^{ρ'}_R α. This is what composing a
  covariant α with an on-site Clifford C produces: C∘α intertwines ρ and CρC^{-1}. All 25 pairs
  of Clifford classes were run under H = O on the cell. Unsigned intertwiners exist only for
  trivial↔sign and axis↔full, and **none of them satisfies the phase relations**. Because classes
  are taken up to independent on-site Clifford conjugation of input and output, this covers
  "α composed with any global on-site Clifford". Result: no new QCAs.
- **Covariance modulo global Pauli conjugation** (projective sign freedom): this is exactly the
  unsigned count. For axis and full it is still 1, the identity.
- **Time-reversal twist.** Odd rotations conjugate α to α^{-1}, realised either unitarily or
  antiunitarily (β_R∘K). We ran this under H = O on the cell.
  - axis and full: 3 unsigned solutions, all on-site (identity and the two order-3 Cliffords); no
    entangling ones.
  - trivial and sign: the solutions are exactly the τ = 0 subset of the ordinary O-covariant ones.
  - sign-f: 46 unsigned, 30 of them new. 28 have nonconstant τ, so they spread ballistically, and
    they have no gliders by Theorem 2.
  - Signed counts are in the log.

  Adding time reversal as an *extra* symmetry can only shrink the lists.
- Not covered: improper rotations or inversion as an additional symmetry, which only restricts;
  and charge-conjugation-type antiunitary twists other than K composed with the action.

## Answers to the C4 questions

(a) **On-site Clifford × shift vs entangling.** Every covariant α has det M = 1, so no shift. An
    O-invariant shift t needs Rt = t for all R, so t = 0. On the cell:
    - axis and full: only the identity;
    - trivial and sign: 6 on-site Cliffords (unsigned) and 126 entangling C1 E(g) C2;
    - sign-f: 2 on-site and 14 entangling involutions, all of the form C1 E(g) C2.

    Every one is a finite-depth Clifford circuit. For the trivial action each factor is itself
    O-covariant. On the 125-ball under axis or full soldering we have the identity and two
    commuting-Pauli-rotation circuits, each proved to be a circuit. The fourth solution is
    undecided as a circuit, but it is an involution with constant trace. No nontrivial
    (Haah/FHH-type) QCA element appears among the decided cases.

(b) **Gliders and propagation.**
    - None under O or T, at any range, for any action (Theorem 2).
    - Ballistic, unbounded spreading occurs exactly for the nonconstant-τ matrices. With valid
      phases there are 84 matrices (336 signed QCAs) for the trivial action and only 14 matrices
      (56 signed) for the sign action, out of the same 84 unsigned matrices. The front reaches
      n·vert(Newt τ). Numerically the front radius equals n at every step for all 28
      representatives. The support is sparse and fractal-like
      (characteristic 2). See the numerics under Theorem 2.
    - Under the soldered actions nothing propagates at all on the cell (O, T, D4, D3).

## What is not covered (honest scope)

- **Non-Clifford QCAs** of any kind: general locality-preserving automorphisms, or the U(1)
  single-particle walks of the 10-16 note. This is the main gap. Freezing the Clifford class does
  not freeze general QCAs.
- **Larger range.** Radius 2 is covered only for H = O with the axis, full and sign-f actions.
  sign-f at radius 2 gives 1024 unsigned solutions, 2048 signed, all with constant trace. Radius
  ≥ 3 is not classified. Theorem 2 (no gliders under O/T, the trichotomy and the light cone) holds at
  every range, but it does not classify.
- More than one qubit per site, qudits, or block or staggered cells.
- Subgroups C4, C3, C2 and the trivial group.
- Any physical identification, tick, clock or adoption of (D-QCA).

## Novelty and relation to prior work

- **Formalism.** Polynomial or symplectic Clifford QCA formalism: Schlingemann, Vogts and Werner,
  J. Math. Phys. 49, 112104 (2008); Haah, Commun. Math. Phys. 324, 351 (2013).
- **Trace trichotomy.** The 1D version (periodic / glider / fractal according to the trace) is due
  to Gütschow, Uphoff, Werner and Zimborás, J. Math. Phys. 51, 015203 (2010). We recall it from
  memory and have not re-checked it against the paper. Our Theorem 2 is the same mechanism in Z^d,
  with a proof that uses only Cayley–Hamilton, Dickson polynomials and Galois conjugation.
  *New here:* the covariance corollary (H-invariance of τ kills gliders under O and T at any
  range) and the exact Newton-polytope front.
- **Index and triviality.** For index and triviality theory see Gross, Nesme, Vogts and Werner,
  CMP 310, 419 (2012) (GNVW index, 1D); Freedman and Hastings, CMP 376, 1171 (2020); Haah,
  J. Math. Phys. 62, 092202 (2021) (Clifford QCA: trivial modulo circuits and shifts in 2D,
  Witt-group-valued in 3D); and Haah, Fidkowski and Hastings, CMP 398 (2023), for nontrivial 3D
  examples. We do not rely on the qubits-per-site count of those examples; it is not checked here.
  We do not use these classifications. Triviality of our solutions is shown directly by explicit
  covariant circuit decompositions.
- **Novelty claim.** The exhaustive classification under cubic covariance with the framework's
  soldering menu, including the fifth Clifford action, the twisted and time-reversal variants, and
  the subgroup tables, appears new. We did not find it in the literature recalled above; no web
  search was done. Novelty does not bear on correctness.

## Reproduction

```bash
cd .claude/science/physics-loops/toe-scale-ladder-20261018/blocks/C4/scripts
python3 c4_01_actions.py          # TOTAL: PASS=34 FAIL=0   (seconds)
python3 c4_02_classify_O.py       # TOTAL: PASS=41 FAIL=0   (~1 min)
C4_GROUPS=T,D4,D3 python3 c4_03_subgroups.py   # PASS=63 FAIL=0 (~15 min, brute-force cross-checks)
C4_GROUPS=D2 C4_BRUTE_MAX=0 python3 c4_03_subgroups.py
python3 c4_04_dynamics.py         # dynamics checks + numerics
python3 c4_05_independent_O.py    # independent recount for O
python3 c4_06_radius2.py          # radius-2 ball, O, axis/full/sign-f: PASS=5 FAIL=2 (2 FAILs = falsified prediction)
python3 c4_07_radius2_analysis.py # structure of the radius-2 soldered solutions: PASS=4 FAIL=2 (closure FAILs)
python3 c4_08_circuit_decomposition.py  # transvection (Pauli-rotation circuit) certificates: PASS=4 FAIL=0
```
Logs: `logs/c4_0*_*.txt`; D2 has its own log, `logs/c4_03_subgroups_D2.txt` (PASS=15 FAIL=0).
c4_04 reports PASS=21 FAIL=0; c4_05 reports PASS=7 FAIL=0. Runtimes: c4_06 and c4_07 take about
13 min per action, c4_03 for D2 about 25 min.

## Load-bearing step for an independent check

Two certificates matter most. The first says **only the identity** is O-covariant under axis or
full soldering on the cell. The second says there are **exactly 4** such QCAs on the 125-ball,
all with constant trace. Together they carry the "soldered ⇒ frozen" conclusion. The best check is an independent implementation: it should rebuild
the covariance conditions from the action with phases, or work directly in the Laurent ring, and
it should not reuse `c4lib.py`. `c4_05` is a partial independent route written by the same agent.
Theorem 2 is short and pen-checkable. Its step most worth re-checking is the claim that the
Galois-conjugation case forces τ to be constant (part d).


## Review dispositions

The independent review is in `REVIEW.md`. It was written by the same model family in a fresh
context, with its own code that does not import or copy `c4lib.py`.

- **Disclosure.** The reviewer's Phase A was blind to the author's logs and code but **not** to
  the headline counts: the orchestrator's prompt included them. Its code is independent.
- **Reproduced independently:**
  - Theorem 1 counts on the 27-cell for all five actions, signed and unsigned;
  - the 84 nonconstant-τ matrices and the sign-f involutions;
  - Theorem 1b at range 2: 4/4 each for axis and full, with sign (+,+) only;
  - the Chamon and cuboctahedral circuits [2] and [1], with phases;
  - Theorem 2 (a)–(d), including the Galois step and the O/T glider no-go;
  - the non-closure of the range-2 solutions under composition.
- **C-1 (minor): accepted and applied.** Theorem 2(d) for general H now excludes
  τ = x^r + x^{-r}. The O and T conclusions are unchanged.
- **Cosmetic: accepted.** The exponent sign in ∏ exp(±iπ/4 P_r) is immaterial.
- **Still open:** the structure of the 73-site range-2 solution [3].
- **Not independently re-checked** (author evidence only):
  - the subgroup tables (T, D4, D3, D2);
  - the twist runs (in/out soldering pairs and the time-reversal twist);
  - the 58-homomorphism sweep and the 5-class result, which come from c4_01 and c4_02;
  - the C1 E(g) C2 structure claim;
  - the sign-f radius-2 count;
  - the c4_04 dynamics numerics.
- **Correction confirmation (end of REVIEW.md, rv_sign_spread.log): accepted.** Under the sign
  action only 14 of the 84 spreading matrices admit valid phases. My own recount agrees: 14
  matrices and 56 signed QCAs, against 84 matrices and 336 signed for the trivial action.
  Result item 2 and Answer (b) are corrected. The c4_04 instance checks ran on all 168 unsigned
  matrices (84 trivial + 84 sign), a superset, so they still apply.
