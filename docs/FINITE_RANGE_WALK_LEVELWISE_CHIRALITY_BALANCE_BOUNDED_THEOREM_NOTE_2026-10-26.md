# Finite-range walks on Z^3 balance Weyl chirality at every clean quasienergy

**Date:** 2026-10-26
**Type:** bounded_theorem
**Status authority:** independent audit only; no retained status asserted.
**Primary runner:** `scripts/finite_range_walk_levelwise_chirality_balance_2026_10_26.py`
**Cached output:** `logs/runner-cache/finite_range_walk_levelwise_chirality_balance_2026_10_26.txt`

## Supplied class, imported result and conventions

The walk class is the supplied class of
[the three-winding vanishing note](FINITE_RANGE_WALK_THREE_WINDING_VANISHING_BOUNDED_THEOREM_NOTE_2026-10-26.md):
single-particle translation-invariant unitary walks U(k) on Z^3 with n internal
states and finitely many hops. That note's theorem, W3[U] = 0 for every such
walk, is imported here; it rests on its own cited K-theory input. No dynamics
is derived from the framework axioms.

- Quasienergy: an eigenvector of U(k) with U(k) psi = exp(-iE) psi has
  quasienergy E (mod 2 pi). The level set at eps is
  F_eps = {k : exp(-i eps) in spec U(k)}. The level is **clean** when F_eps is
  finite.
- W3 is the three-winding of the companion note, in the same orientation (the
  analytic map V_2 of that note has W3 = -1).
- For a smooth projector family P on a closed oriented surface,
  Ch(P) = (i/2 pi) int tr(P dP ^ dP).
- A **Weyl node** at eps is an isolated point p at which exactly two bands meet
  at quasienergy eps with
  U(p + dk) ~ exp(-i eps) exp(-i (t.dk + sum_ij v_ij dk_i sigma_j)) on the
  two-dimensional degenerate space, det v != 0, and |v^{-1} t| < 1 (type I, so
  the touching is isolated in F_eps). Its chirality is chi_p = sign det v.

## Theorem 1 (localization identity)

Let U: T^3 -> U(n) be smooth (finite range is not needed) and fix eps. Let
B_1, ..., B_m be disjoint closed boxes with F_eps contained in the union of
their interiors. For each i let phi_i in (eps, eps + 2 pi) be a quasienergy
absent on the whole box: exp(-i phi_i) is not an eigenvalue of U(k) for any k
in B_i. On the boundary of B_i let P_<^(i)(k) be the spectral projector of U(k)
onto the eigenvalues exp(-iE) with E in (phi_i - 2 pi, eps); it is smooth
there because no eigenvalue equals exp(-i eps) or exp(-i phi_i). Then

```
W3[U] = - sum_i Ch(P_<^(i) on dB_i),   dB_i oriented by the outward normal.
```

**Proof.** Write omega(g) = tr((g^{-1} dg)^3), so that W3[g] is the integral of
omega(g) over T^3 divided by 24 pi^2.

1. *Global logarithm off the level set.* On T^3 minus F_eps, the logarithm
   H_eps = i Log U with branch cut at exp(-i eps) (spectrum in
   (eps, eps + 2 pi)) is smooth by holomorphic functional calculus. Put
   M = T^3 minus the union of the open boxes, and G(k, t) = exp(-i t H_eps(k))
   on M x [0, 1]. Then G(., 0) = 1 and G(., 1) = U. The form omega is closed,
   and the oriented boundary of M x [0, 1] is dM x [0, 1] - M x {1} + M x {0}.
   Stokes gives: the integral of omega(U) over M equals the integral of
   omega(G) over dM x [0, 1], which is minus the sum over i of the integrals
   over dB_i x [0, 1], because dM is the union of the dB_i with reversed
   orientation.
2. *Local factorization.* On B_i let H_reg = i Log U with branch cut at
   exp(-i phi_i); it is smooth on all of B_i. On dB_i the two logarithms differ
   exactly on the eigenvalues with quasienergy in (phi_i - 2 pi, eps), which
   are shifted by 2 pi: H_eps = H_reg + 2 pi P_<, the two terms commuting.
   Hence G = g h with g = exp(-i t H_reg) and
   h = exp(-2 pi i t P_<) = 1 + (z - 1) P_<, z = exp(-2 pi i t).
3. *Polyakov-Wiegmann.* omega(g h) = omega(g) + omega(h) + d(...), where the
   exact term is a multiple of tr(g^{-1} dg ^ dh h^{-1}). Its integral over
   dB_i x [0, 1] reduces to the ends t = 0 and t = 1, where h = 1 identically
   on dB_i, so dh pulls back to zero and the exact term contributes nothing.
4. *Regular part.* g is smooth on B_i x [0, 1] with g(., 0) = 1 and
   g(., 1) = U, so Stokes gives: the integral of omega(g) over
   dB_i x [0, 1] equals the integral of omega(U) over B_i.
5. *t-winding lemma.* For a smooth projector family P on a closed oriented
   surface S and h = 1 + (z - 1) P, the integral of omega(h) over S x [0, 1]
   (orientation (S, t)) equals 24 pi^2 Ch(P). Indeed
   h^{-1} dh = -2 pi i P dt + B with B = (z - 1) dP + |1 - z|^2 P dP. B has no
   dt component, so B^3 = 0 on S x [0, 1], and omega(h) = -6 pi i dt ^ tr(P B ^ B).
   From P dP P = 0 one gets tr(P B ^ B) = -|1 - z|^2 tr(P dP ^ dP); the
   integral of |1 - z|^2 over [0, 1] is 2, so the integral is
   12 pi i times the integral of tr(P dP ^ dP), that is 24 pi^2 Ch(P).
6. *Collecting.* The integral of omega(U) over T^3 is the integral over M plus
   the integrals over the B_i, which by steps 1-5 equals
   -sum_i [integral over B_i of omega(U) + 24 pi^2 Ch_i] + sum_i (integral over
   B_i of omega(U)) = -24 pi^2 sum_i Ch_i. QED

Changing phi_i only moves bands that extend smoothly over B_i into or out of
P_<, and those have Ch = 0 on dB_i; so the right side does not depend on the
choices.

## Lemma 2 (local charges)

- A Weyl node p at eps, enclosed alone in a small box, contributes
  Ch(P_<) = chi_p: on the box surface P_< is the lower band of the touching pair
  (projector (1 - nhat.sigma)/2 with nhat the unit vector of v^T dk) plus bands
  that extend smoothly over the box, and Ch of the lower band is the degree of
  nhat, which is sign det v. The tilt t is a scalar and does not enter. The
  runner checks the sign convention against a direct integral.
- An isolated touching of more than two bands, or an isolated non-degenerate
  extremum of a single simple band at eps, contributes the integer
  Ch(P_<) on a small enclosing surface; the extremum contributes 0, since there
  P_< extends smoothly over the box.

## Corollaries for finite-range walks

Let U be a finite-range translation-invariant unitary walk (any n). By the
imported theorem W3[U] = 0.

1. **Level-wise balance.** At every clean level eps, the local charges of the
   points of F_eps sum to zero. If every point of a clean level is a Weyl node,
   then sum_{p in F_eps} chi_p = 0. This holds separately at quasienergy 0, at
   pi and at every other clean level.
2. **No partner only at the cutoff.** No finite-range walk has a clean level at
   which its Weyl nodes carry nonzero net chirality. In particular nodes at
   quasienergy 0 with net chirality +1, compensated only by nodes at
   quasienergy pi, cannot occur: each clean level is separately balanced. If the
   Weyl nodes at a level carry nonzero net chirality, that level is not clean:
   it contains non-isolated points (Fermi sheets). The source packet also
   proves that the compensating charge is then the Berry flux of those sheets at
   the same quasienergy; that refinement is not checked by the runner and is
   not claimed here.
3. **Determinant.** If some level of U is clean, det U is constant. On the
   complement of the finite set F_eps, det U = exp(-i tr H_eps) with tr H_eps
   continuous; loops avoiding a finite set generate the fundamental group of
   T^3, so det U has zero winding on every loop, and a unit monomial
   c exp(i m.k) with zero windings has m = 0.

The same corollaries hold for any step generated by a Bloch Hamiltonian
H(k, t) piecewise continuous in t and smooth in k, because such a step has
W3 = 0 by homotopy (consequence in the three-winding note).

For contrast, the analytic map V_2 with exponentially decaying hops has
W3 = -1: its eight time-reversal-invariant momenta are Weyl nodes, seven at
quasienergy 0 with chirality sum +1 and one at quasienergy pi with chirality
+1. Each clean level is unbalanced by -W3, as Theorem 1 requires. Strict
finite range is what removes this possibility.

## What the runner checks

Expected values are never fed in: W3 comes from the bulk integral (or from an
exact grid for finite-range walks), and the right-hand side of Theorem 1 from a
certified decomposition of the level set into boxes and lattice Chern numbers on
the box surfaces.

- **Sign lemmas.** The Fukui-Hatsugai-Suzuki lattice Chern sum against a direct
  finite-difference integral; Ch(lower band) = sign det v for random v; the
  t-winding identity of step 5 by quadrature.
- **Theorem 1 on maps with W3 != 0.** V_2 (W3 = -1) and V_0 (W3 = +2) at levels
  0 and pi, with per-box Ch equal to the enclosed chirality; and a coupled n = 3
  map C(V_2 (+) e^{-2i}) whose level sets are pockets, testing the box form
  without nodes.
- **Finite-range walks.** The one-qubit product walk Q = S_x S_y S_z (eight Weyl
  nodes at each of 0 and pi), the D'Ariano-Perinotti body-centred-cubic Weyl
  walk written on Z^3, and the supplied O-covariant two-qubit walk at its
  light-speed parameter point deformed by the axial coin exp(0.15 i 1 (x) sigma_3)
  (C4z-covariant; two Weyl nodes at quasienergy 0 and six at pi). Each has
  exact-grid W3 = 0, box sums zero at levels 0 and pi, and nodal chirality sums
  zero at its clean levels.
- **Sharpness witness.** T2 = exp(i k_x) Q(2,1,1) (range 3, n = 2) has
  exact-grid W3 = 0, four isolated type-I Weyl nodes at quasienergy 0, all with
  chi = -1 and Ch = -1 in certified boxes, and non-degenerate eigenvalue-1
  points elsewhere at level 0. Its level 0 is therefore not clean, as
  corollary 2 requires, and its determinant exp(2 i k_x) is not constant, as
  corollary 3 allows. The node list is certified complete through the
  inventory of Q(2,1,1), because the degeneracies of exp(i k_x) Q are those of Q.

Certification limits: the level set is excluded from coarse cells by a
Lipschitz bound, rigorous up to floating-point rounding. The lattice Chern sums
are exact integers when the link variables are nonzero, and mesh adequacy is
evidenced by agreement at two meshes, not proved. Node lists inside a box are
evidence; the box Chern number is the computed object.

## Scope and boundaries

- Single-particle translation-invariant walks with one cell per site (a larger
  cell is a larger n); not interacting dynamics and not disorder.
- Theorem 1 needs smoothness only; the corollaries need W3 = 0, supplied for
  finite range by the imported theorem and for Hamiltonian-generated steps by
  homotopy.
- A chiral imbalance inside a projected or adiabatic band subspace of a
  multiband walk is not excluded by this note.
- The level-wise relation between W3 and nodal chirality is known in the
  literature (Higashikawa-Nakagawa-Ueda, PRL 123, 066403 (2019);
  Sun-Xiao-Bzdusek-Zhang-Fan, PRL 121, 196401 (2018); Bessho-Sato,
  arXiv:2006.04204); the static analogue is Haldane's Fermi-surface Berry-flux
  sum rule. Novelty is not claimed. The note supplies a self-contained proof
  with explicit hypotheses and its combination with the finite-range theorem.

## Source recovery

This is the canonical form of campaign block C5b of PR #9831, preserved at the
frozen head `e294c1dc745dad0c95b4c8688efc6f3f0be03613` under
`.claude/science/physics-loops/toe-scale-ladder-20261018/blocks/C5b/`. The helper
module is that block's reviewed library with only import and naming edits. Its
separate-context review (same model family as the author) confirmed the
localization identity with a second proof, the determinant corollary and the
answer to the cutoff-partner question, and corrected a sign in the sheet
version and a hypothesis in a window corollary. Not carried over: the window
corollary (it needs a single-adjacent-band-pair hypothesis per ball), the
sheet-flux refinement as a checked claim, the n = 3 constant-determinant
witness, and the remaining coupled n = 3 and n = 4 battery members; all remain
in that recovery path with their logs.
