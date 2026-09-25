# The fall of a pull-bound pair's binding energy: block 145 by other routes

Task `J:derive:the-fall-of-a-pull-bound-pairs-binding-energy:a1`, worker `w-macbookpro9927a-j607a`, model claude-opus-5-5.
Checker: `check.py` in this directory. It is exact (sympy series in `1/c`, symbols), takes about 3 s, and reports `TOTAL: PASS=4 FAIL=0`.

**Sources.**
- Block 145 (PR #9233) is closed and landed on `origin/main` at `25b8c1874f`. Its landed wording is a supplied perturbative model:
  - self-field-subtracted continuum charges;
  - a postulated moving charge equation;
  - a trace-free, no-free-wave field momentum;
  - a finite-cluster extension.
- Blocks 60 (T2, T4) and 144 are read as landed.

**Related prior work, disclosed.** My #9245 confirmed block 144, including the inertial weight `W = 1` of pull-bound pairs and the general-coefficient formula. This attempt treats the passive side (block 145 T3) and T1–T2 by different routes. There are no earlier attempts on this problem.

## 1. Statement attempted

Within block 145's supplied charge model for block 60's bilinear members `X = l^{p/2}`:
- `X = 1 + sum_j Q_j g(., x_j)` and `Q_i X(x_i) = E_i/c`;
- the ledger is `c sum_i Q_i`;
- `G = 1/(2 pi c)`, and `p = 1` is the curvature member with `c = 8K`.

The claims to check, by other routes:
- **T1:** the static ledger to second order, for every `N`.
- **T2(a):** the moving-body coefficient `1/2 + 1/p`.
- **T3:** the passive mass `M + 2a<T> + 2s2<U>`, and its difference `(1 - 1/p)<U>` from the pair's energy.

The extension: keep the self-fields of block 60's finite-box solution.

## 2. Steps

**F1. T1 for every `N`. PROVED; CHECKED for `N = 3` and `4`.**
- **The expansion.** Iterating `Q_i = (m_i/c)(1 + sum_j Q_j g_ij)^{-1}` gives `L = sum_i m_i (1 - phi_i + phi_i^2 + sum_j (m_j/c) g_ij phi_j) + O(c^-3)`, with `phi_i = sum_{j!=i} m_j g_ij/c`.
- **Symmetry.** `g` is symmetric, so `sum_{i,j} m_i (m_j/c) g_ij phi_j = sum_j m_j phi_j^2`. Hence `L = sum_i m_i (1 - phi_i + 2 phi_i^2)`.
- **The continuum reading.** With `g = 1/(4 pi r)`, this is `M - sum_{a<b} G M_a M_b/r_ab + (G^2/2) sum_a M_a (sum_b M_b/r_ab)^2`, with `G = 1/(2 pi c)`.
- **Scope.** Block 145 checked three bodies; the identity above holds for every `N`.

**F2. T2(a). CHECKED.**
- With the moving charge equation `Q_i X(x_i) = sqrt(m_i^2 + k_i^2 X^{-4/p})/c` (block 145's supplied postulate), the two-body ledger's first-order term at order `k^2` is

  `-(G m1 m2/r)[1 + (1/2 + 1/p)(k1^2/m1^2 + k2^2/m2^2)]`,

  computed directly as a series.
- The `1/2` comes from the bodies' own kinetic energy. The `1/p` comes from `l^{-2} = X^{-4/p}`.

**F3. T3 by Hamilton's equations. PROVED; CHECKED.**
- **The coupling.** With the third body at rest, the Hamiltonian couples to it through `H_ext = sum_{a=1,2} Phi(x_a)[m_a + 2a T_a + s2 U]`. The remaining `s2 (G^2 m3/2)(...)^2` term is suppressed for a small pair (block 145 T3(a)).
- **The force.** In a linear far field, `dP/dt = -sum_a dH/dx_a = -grad Phi [M + 2a T + 2 s2 U]` exactly. The `U`-gradient terms from `Phi(x_1) + Phi(x_2)` cancel, because `sum_a dU/dx_a = 0`.
- **The difference from energy.** With the virial `<2T + U> = 0`, the passive mass minus the energy `M + <T> + <U>` is `(2 s2 - a - 1/2)<U>`.
  - For block 60's members (`a = 1/2 + 1/p`, `s2 = 1`) this is `(1 - 1/p)<U>`.
  - It vanishes only at `p = 1`.
- **Independence.** This route uses the force on the pair's total momentum, not block 145's derivative in `m3`. With block 144's inertia `W = 1` (re-checked in my #9245), the pair falls like one body at first order.

**F4. Extension: the finite box keeps self-fields. PROVED; CHECKED for `N = 2` and `3`.**
- **The setting.** Block 60 T4's finite-box charges include the diagonal `g(x_i, x_i) = g0`. A body alone has the dressed ledger `M_i = m_i - g0 m_i^2/c + 2 g0^2 m_i^3/c^2`.
- **The result.** In dressed masses, the `N`-body ledger is the self-subtracted T1 form plus a leftover `(2 g0/c^2) sum_{i!=j} m_i^2 m_j g_ij`.
- **The reading.** Body `i` couples to the others with `m_i + 2 E_self,i`, where `E_self,i = -g0 m_i^2/c`. That is T3's passive formula `M + 2 s2 U` at `<T> = 0`: a body pinned on a site has no virial balance, so its self-energy weighs twice.
- **Consistency.** This agrees with block 145's stated exclusion of the constituents' compactness, and it quantifies that exclusion.

## 3. Result

- **No error found.** Block 145's T1–T3 hold within its supplied model by independent routes:
  - T1 for every `N`;
  - T2(a)'s coefficient directly;
  - T3's passive mass from Hamilton's equations.
- **Extension.** The finite-box self-fields give the pinned-body case of the same formula. A static self-energy weighs `2E_self`, so compact pinned bodies would fall with a Nordtvedt-type offset `E_self` in this static model.

## 4. What would finish or extend it

1. T2(b), the field momentum, in another gauge. Here it is taken from block 145, and my #9245 checked the exchange route of block 144.
2. Compact bodies with internal motion: whether a virialized self-bound walker restores `M_grav = E`, which T3 suggests.
3. The nonlinear dynamical completion that block 145 leaves open.
