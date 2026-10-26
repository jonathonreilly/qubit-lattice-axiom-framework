# Finite-range translation-invariant walks on Z^3 have zero three-winding

**Date:** 2026-10-26
**Type:** bounded_theorem
**Status authority:** independent audit only; no retained status asserted.
**Primary runner:** `scripts/finite_range_walk_three_winding_vanishing_2026_10_26.py`
**Cached output:** `logs/runner-cache/finite_range_walk_three_winding_vanishing_2026_10_26.txt`

## Supplied class and conventions

The [minimal axiom memo](MINIMAL_AXIOMS_2026-06-29.md) supplies the Z^3
lattice and the one-qubit site only. The walk class below is a supplied
mathematical class, not a dynamics derived from the axioms. A single-particle
translation-invariant walk with n internal states per cell is a unitary on
l^2(Z^3) (x) C^n with Bloch symbol

```
U(k) = sum_{x in S} A_x exp(i k.x),   S a subset of Z^3,   A_x in M_n(C).
```

It has finite range when S is finite. n = 2 is one qubit per site; larger n
covers larger cells or enlarged sites, which are not framework premises. No
symmetry is assumed.

The three-winding of a smooth map g from the torus T^3 into GL_n(C) is

```
W3[g] = (1/(24 pi^2)) int_{[0,2pi)^3} sum_{abc} eps_abc tr(A_a A_b A_c) d^3k,   A_a = g^{-1} d_a g.
```

Write R = C[z1^{+-1}, z2^{+-1}, z3^{+-1}] with z_a = exp(i k_a). A finite-range
walk is a matrix U in M_n(R) whose inverse U^{-1} = U^dagger is again in
M_n(R). So every finite-range unitary walk lies in GL_n(R).

## Theorem (three-winding vanishing)

For every n >= 1 and every M in GL_n(R), W3[M] = 0. In particular every
finite-range translation-invariant unitary walk on Z^3 has W3 = 0, for any
internal dimension n, any finite stencil and any coin.

**Imported input (load-bearing, cited and not re-proved).** The determinant
induces an isomorphism K_1(R) = R^x = C^* x {z^m : m in Z^3}; equivalently
SK_1(R) = 0. This is the fundamental theorem of algebraic K-theory for regular
Noetherian rings, K_1(A[t, t^{-1}]) = K_1(A) (+) K_0(A) with NK_1(A) = 0,
applied three times starting from K_1(C) = C^*, together with
K_0(C[Z^d]) = Z for d <= 2 (the same theorem in degree 0, with NK_0 = 0 and
K_{-1} = 0 for regular rings); the K_0 summand enters through units such as
z_a (Bass-Heller-Swan for K_1; Quillen's fundamental theorem; see Weibel,
*The K-book*, chapters III and V).
Suslin's stability theorem gives the stronger unstable statement
SL_N(R) = E_N(R) for N >= 3; it is recalled for orientation and is not used.
No finite computation can verify this input, and the runner does not try.

**Proof.**

1. The 3-form tr((g^{-1}dg)^3) is closed on GL_N(C), so W3 is a homotopy
   invariant of continuous maps T^3 -> GL_N(C). It is additive under pointwise
   products: tr(((gh)^{-1}d(gh))^3) differs from the sum of the two forms by an
   exact form (Polyakov-Wiegmann). It is unchanged under g -> g (+) 1. It
   vanishes on a map whose only nonconstant entry is one scalar on the
   diagonal, because a scalar 1-form wedged with itself is zero.
2. By the imported input, the class of M in K_1(R) = GL(R)/E(R) (Whitehead
   lemma) equals the class of diag(det M, 1, ..., 1). Hence, for some N >= n,
   M (+) 1_{N-n} = diag(det M, 1, ..., 1) E_1 ... E_s with elementary matrices
   E_j = 1 + p_j e_{i_j l_j}, p_j in R, i_j != l_j.
3. Each E_j is joined to the identity by E_j(t) = 1 + t p_j e_{i_j l_j},
   0 <= t <= 1, which has determinant 1 for every t and k. So W3[E_j] = 0.
4. det M is a unit of R, hence a unit monomial c z^m, and
   W3[diag(c z^m, 1, ..., 1)] = 0 by step 1.
5. Additivity and stability give W3[M] = W3[M (+) 1] = 0. QED

## Consequences

Each follows from the theorem or, where stated, from step 1 of its proof alone.

- **Determinant.** det U(k) = c exp(i m.k) for every finite-range unitary walk,
  because the units of R are the unit monomials.
- **Distance bound.** If U is a finite-range unitary walk and V: T^3 -> U(n)
  is continuous with W3[V] != 0, then sup_k ||U(k) - V(k)|| >= 1. Otherwise
  (1 - t)U + tV = U(1 + t U^dagger (V - U)) is invertible for all t in [0, 1],
  and homotopy invariance would give W3[U] = W3[V].
- **Hamiltonian-generated steps.** If U(k) is the time-ordered exponential of a
  Bloch Hamiltonian H(k, t) continuous on T^3 x [0, T], then s -> U_s is a
  homotopy from the identity, so W3[U] = 0 by step 1 alone, without any range
  hypothesis.
- **Symmetry alone imposes nothing.** For R in GL_3(Z) and a constant unitary D,
  W3[k -> D U(R^{-1} k) D^dagger] = det(R) W3[U]. Proper cubic rotations with
  any coin action therefore preserve W3. The analytic map
  V_M = (f + i g.sigma)/|(f, g)|, f = M - sum_a cos k_a, g = (sin k_a), is
  exactly covariant under the 24 proper cubic rotations with the spin-1/2 coin
  action, and has W3 = c (0, 1, -2, 1, 0) on M in (3, inf), (1, 3), (-1, 1),
  (-3, -1), (-inf, -3), with c = -1 in this orientation. The predicted
  integers come from a preimage count at the eight time-reversal-invariant
  momenta (V_M = +-1 exactly where g = 0, with local degree
  prod_a sign cos p_a); only the global sign c is read from one integral.
  V_M has exponentially decaying hops, not finitely many. So the vanishing
  in the theorem is forced by strict finite range, not by cubic covariance.

## Supporting lemma: the two-qubit Clifford family

Let Gamma = (tau1, tau2, tau3 sigma1, tau3 sigma2, tau3 sigma3) on C^2 (x) C^2,
five pairwise anticommuting Hermitian involutions, and
Phi(x) = x0 + i sum_{j=1}^{5} x_j Gamma_j for x in S^5. Then Phi maps S^5 into
U(4), and the pullback of tr(theta^3), theta = Phi^{-1} dPhi, vanishes
identically on S^5. Hence W3 = 0 for every continuous map T^3 -> Phi(S^5),
finite range or not.

*Proof.* The runner checks that all 20 antisymmetrised components of
tr(theta^3) vanish as polynomials (exact symbolic computation), and that the
same routine gives a nonzero component on SU(2) = S^3. A hand proof: the
transposes Gamma_j^T again form a Clifford system, and the scalar
Gamma_1 ... Gamma_5 is invariant under reversal of its five factors (sign
(-1)^10 = +1), so Gamma_j^T = C Gamma_j C^{-1} for one constant C. Then
Phi(x)^T = C Phi(x) C^{-1}, while transposition reverses the cyclic order of
three odd forms: tr((theta^T)^3) = -tr(theta^3). So the pulled-back form
equals its own negative. For three Pauli matrices the reversal sign is -1 and
the argument correctly fails. This covers the supplied two-qubit walk family
of `TWO_QUBIT_SITE_UNFREEZES_THE_CUBIC_TICK_DOUBLER_FREE_DIRAC_WALK_BOUNDED_THEOREM_NOTE_2026-10-16.md`
at every parameter point, and sharpens its cohomological remark to pointwise
vanishing.

## What the runner checks

The theorem's load-bearing step is the imported K-theory input. The runner
checks every other ingredient on explicit instances.

- **Finite integration lemma.** If U is a range-r unitary Laurent matrix, the
  W3 density is a trigonometric polynomial of degree at most 6r per axis. The
  N-point periodic rule integrates exp(i m k) exactly for |m| < N, so N >= 6r+1
  gives W3 exactly up to rounding. For a Laurent matrix with Laurent inverse of
  range r' the degree is at most 3(r + r'). The runner uses N = 6r+2 and 6r+5
  and checks the degree bound on one density by Fourier analysis.
- **Controls.** V_M reproduces the five predicted integers with c fixed from
  M = 2 only, and its exact O-covariance is checked on 300 samples.
- **Mechanism on GL_3(R).** Products diag(c z^m, 1, 1) E_1 E_2 E_3 E_4 with
  mixed upper and lower elementary factors and random Laurent entries have a
  nonzero density and W3 = 0 on exact grids. W3[V_2 (+) 1] and
  W3[(V_2 (+) 1) E] both equal c, and W3[V_2 V_2] = 2c.
- **The hypothesis cannot be dropped.** The range-2 and range-3 Fourier
  truncations of V_2 are Laurent polynomial matrices, invertible on the torus,
  whose determinants are not unit monomials. They are therefore not in
  GL_2(R), and they carry W3 = c = -1.
- **Battery of finite-range unitary walks.** Random shift-coin products with
  n = 2, 3, 4 whose shift axes cycle through all three directions; the
  D2-covariant product walk; and two n = 2 range-1 walks with all 27 hop
  matrices nonzero, found by solving U U^dagger = 1 with no product structure
  imposed (the solver's closed-form Jacobian was checked against finite
  differences during development, not in the runner; a solution whose density
  is near zero tests nothing, so it is reported and skipped, never counted).
  Each is unitary, moving,
  has a unit-monomial determinant, a W3 density that is not identically zero,
  and exact-grid W3 = 0. Two further members have a density that vanishes
  pointwise for a structural reason, which the runner confirms: the D3
  body-diagonal shift depends on k1 + k2 + k3 only, and the O-covariant
  two-qubit Clifford walk at the parameter point b* of the two-qubit note above
  is covered by the Clifford lemma below.
- **Clifford lemma.** The exact symbolic certificate and the S^3 control.

Shift-coin products are already covered by an elementary argument
(Polyakov-Wiegmann additivity plus the fact that a conditional shift is
conjugate to a diagonal map), so the walks with no imposed structure are the
discriminating finite-range instances. Instances support but cannot prove the
theorem.

## Scope and boundaries

- Single-particle Bloch unitaries only. Interacting quantum cellular automata
  are not covered; nontrivial three-dimensional QCAs exist (Haah;
  Fidkowski-Haah-Hastings), and many-body anomalies are a separate question.
- Exact translation invariance with one cell per site; a larger cell is a
  larger n. Disordered walks are not treated.
- Strict finite range. Exponentially decaying hops escape, as V_M shows.
- W3 of the whole step only. Chirality carried by a band subspace of a
  multiband walk is not W3 of U and is not addressed here; the level-wise
  statement is in
  `FINITE_RANGE_WALK_LEVELWISE_CHIRALITY_BALANCE_BOUNDED_THEOREM_NOTE_2026-10-26.md`,
  which imports this theorem.
- The identification of W3 with the net Weyl chirality of the quasienergy bands
  (Higashikawa-Nakagawa-Ueda, PRL 123, 066403 (2019)) is not used.

## Relation to existing results

`CUBIC_COVARIANCE_FREEZES_A_ONE_QUBIT_TICK_CELL_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-10-16.md`
records, as a numerical observation, that every moving walk it found has zero
three-winding. The theorem here covers every finite-range walk, every n, every
stencil and every coin action; it does not edit or re-grade that note.
Related literature: quantum-walk and Floquet winding invariants
(Kitagawa-Rudner-Berg-Demler, PRB 82, 235114 (2010); Rudner-Lindner-Berg-Levin,
PRX 3, 031005 (2013)); the K_0 sibling, that strictly local band projectors
have zero Chern number (cf. Dubail-Read, PRB 92, 205307 (2015)). The statement
is a short consequence of classical theorems and is likely known to experts;
novelty is unverified and is not claimed.

## Source recovery

This is the canonical form of campaign block C5 of PR #9831, preserved at the
frozen head `e294c1dc745dad0c95b4c8688efc6f3f0be03613` under
`.claude/science/physics-loops/toe-scale-ladder-20261018/blocks/C5/`
(note, review, worklog, scripts and logs). That block's separate-context
review, by the same model family as the author, accepted the K-theory step and
wrote a second route that avoids it: the Toeplitz index bundle over T^2, whose
cokernel module is projective over C[z1^{+-1}, z2^{+-1}] with trivial
determinant because the Picard group of that unique factorisation domain is
zero, calibrated so that c_1 of the index equals -W3. That route is recorded
there and is not re-derived or relied on here. Not carried over: the one-qubit
per-level corollary (generalised in the level-wise note), the numerical
unitarity-defect floors (upper bounds only), and an unresolved comparison
question about Floquet constructions with nonzero W3.
