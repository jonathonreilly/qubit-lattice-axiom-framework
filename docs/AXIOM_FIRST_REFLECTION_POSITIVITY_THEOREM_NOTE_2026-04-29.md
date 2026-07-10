# Axiom-First Reflection Positivity: Staggered-Only, 2-Step Block Formulation

**Date:** 2026-04-29 (original); 2026-05-26 (staggered-only narrowing);
2026-05-27 (single-step spin-basis no-go acknowledgment + 2-step
narrowing); 2026-05-28 (in-repo first-principles 2-step transfer-matrix
positivity replacing the prior citation-only treatment); 2026-06-07
(Wilson-plane sign-repair source packet, conditional on independent audit of
the companion bridge note); 2026-06-08 (rerouted through the retained-bounded
Wilson temporal-gauge bridge).
**Type:** bounded_theorem
**Loop:** `axiom-first-foundations`
**Status authority:** independent audit lane only.
**Primary runner:** [`scripts/axiom_first_reflection_positivity_wilson_temporal_reroute_2026_06_08.py`](../scripts/axiom_first_reflection_positivity_wilson_temporal_reroute_2026_06_08.py)
(parent reroute guard: replays the free staggered 2-step checks C1-C6 through
the construction runner below, then verifies the retained-bounded Wilson
temporal-gauge reroute and factorized reduction guard C7).
**Cached primary-runner output:** [`logs/runner-cache/axiom_first_reflection_positivity_wilson_temporal_reroute_2026_06_08.txt`](../logs/runner-cache/axiom_first_reflection_positivity_wilson_temporal_reroute_2026_06_08.txt)
**Free-case construction runner:** [`scripts/axiom_first_rp_two_step_transfer_matrix_positivity.py`](../scripts/axiom_first_rp_two_step_transfer_matrix_positivity.py)
(positive 2-step exhibit; in-repo construction + proof: the free staggered-KS
2-step blocked transfer matrix `T_hat^2` is positive Hermitian,
`T_hat^2 = B^dag B`, `H_hat = -log(T_hat^2)/(2 a_tau) >= 0`, derived from
the action and anchored to the exact free staggered dispersion; single-step
`T_hat` is shown non-positive in the same construction).
**Cached free-case output:** [`logs/runner-cache/axiom_first_rp_two_step_transfer_matrix_positivity.txt`](../logs/runner-cache/axiom_first_rp_two_step_transfer_matrix_positivity.txt)
**Secondary no-go runner:** [`scripts/axiom_first_rp_spin_basis_single_step_psd_failure.py`](../scripts/axiom_first_rp_spin_basis_single_step_psd_failure.py)
(no-go demonstration: single-step Lagrangian RP for staggered KS in
spin basis is verifiably non-PSD; this is the load-bearing exhibit for
the 2026-05-27 narrowing).
**Cached runner output:** [`logs/runner-cache/axiom_first_rp_spin_basis_single_step_psd_failure.txt`](../logs/runner-cache/axiom_first_rp_spin_basis_single_step_psd_failure.txt)
**Secondary runner:** [`scripts/axiom_first_reflection_positivity_check.py`](../scripts/axiom_first_reflection_positivity_check.py)
(Hamiltonian-level positivity exhibits E1-E6; these are structural
finite-block checks for a chosen `H_lat`, not Lagrangian RP exhibits).

## 2026-05-27 Audit Repair

The prior version of this note claimed a single-step Lagrangian
reflection-positivity theorem for staggered Kogut-Susskind fermions in
the spin basis under the Sharatchandra link-reflection convention. An
independent verification (the load-bearing no-go runner above) shows
that this claim cannot be derived in that surface:

- The Gram matrix `G_{IJ} = <Theta(F_I) . F_J>_S` constructed directly
  from the Berezin path integral with propagator `M[U]^{-1}` is **not
  PSD even in the free U=1 case**. Diagonal entries for the simplest
  degree-1 monomials `chi_x` and `bar(chi)_x` at positive-time sites
  come out at `-0.4`, and the minimum eigenvalue is `-0.80`. Across 5
  random U(1) gauge configurations PSD fails in 5/5 cases.
- This matches the published literature's warning that the standard
  constructive route in the spin basis is not a direct positive
  one-lattice-spacing transfer matrix. Caracciolo-Palumbo, Phys. Rev.
  D 87 (2013) 014507 (arXiv:1210.1786), report failed attempts at a
  positive single-spacing transfer matrix and then construct the
  spin-basis result through block variables.
- The resolution is the **2-step blocked** transfer matrix
  `T_hat^2 = S_hat^2` over two lattice spacings. As of the 2026-05-28
  repair this is **derived in-repo from first principles** (free case
  explicit), not imported: the new positive 2-step runner constructs
  `T_hat^2` from the staggered action and proves it is positive
  Hermitian, anchored to the exact free staggered dispersion. The same
  standard object appears in the lattice literature (Palumbo, Phys.
  Rev. D 66 (2002) 077503 = hep-lat/0208005, flavour basis;
  Sharatchandra-Thun-Weisz spin-diagonal construction, Nucl. Phys. B
  192 (1981) 205; Smit, *Introduction to QFT on a Lattice*, §6) — these
  are named for context, but the load-bearing positivity is now the
  in-repo derivation, not a citation.

This repair therefore takes the **2-step narrowing path**:

- the load-bearing positive claim is the 2-step blocked formulation;
- the direct single-step spin-basis Lagrangian RP surface under
  Sharatchandra Theta alone is explicitly declared out-of-scope and is
  no-go per the cached runner;
- Hamiltonian-level positivity exhibits in the secondary runner are
  kept as structural finite-block consistency checks, not as a
  proof of the single-step Lagrangian RP claim.

The Wilson-fermion subsurface remains out of scope per the 2026-05-26
narrowing. This note continues to claim only the staggered-only
fermion sector.

### Convention note (settled 2026-05-28)

The single-step no-go runner uses the standard Berezin contraction
ordering for `S = bar(chi) M chi` with `exp(-S)`:

```text
<chi_b bar(chi)_a> =  (M^{-1})[b, a],
<bar(chi)_a chi_b> = -(M^{-1})[b, a].
```

The minus sign in the second line is the Grassmann reordering sign. A
2026-05-27 attempted retraction of the single-step no-go used the
wrong transpose/sign convention; the review-loop rejection of that
retraction was correct. The current runner implements the settled
ordering through its Wick-pairing sign and reproduces the non-PSD Gram.

This source note does not set or predict an audit outcome; later
status is generated by the audit pipeline after independent review.

## Scope

In scope (load-bearing):

- finite lattice blocks with the parent temporal-link reflection map
  `theta(t, x_vec) = (-1 - t, x_vec)`;
- compact `SU(3)` Wilson plaquette gauge links with Haar measure;
- Kogut-Susskind staggered fermions with positive real mass
  `M = M_KS + m I`, `m > 0`;
- the **2-step blocked transfer matrix** `T_hat^2` over two lattice
  spacings, as in Palumbo 2002 / Sharatchandra-Thun-Weisz 1981 / Smit;
- polynomial observables supported in the positive-time half that are
  invariant under the 2-step blocking.

Out of scope (removed from this row's claim surface):

- **single-step** spin-basis Lagrangian RP for staggered KS under
  Sharatchandra Theta alone (the load-bearing no-go runner documents
  this);
- Wilson-fermion operators `M_KS + M_W + m I`;
- symmetric-canonical Wilson determinant bridges;
- configuration-by-configuration Wilson-fermion determinant positivity;
- continuum OS reconstruction in the Wightman sense;
- any publication or ledger status promotion.

## Dependencies

The source package uses an in-repo first-principles derivation of the
2-step positivity (a standalone free-case note + its primary positive
runner, plus a retained_bounded fixed-`SU(3)` gauge-extension note),
plus two local authorities that supply the remaining factors of the
gauge-case reduction, plus the single-step no-go runner:

- The **free-case fermion-sector 2-step transfer-matrix positivity** is
  supplied in-repo by the standalone derivation note
  [AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28.md](AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28.md)
  and its primary positive runner
  [`axiom_first_rp_two_step_transfer_matrix_positivity.py`](../scripts/axiom_first_rp_two_step_transfer_matrix_positivity.py)
  (free `U = 1` case explicit; see §"In-repo first-principles
  construction and proof"). This is the load-bearing positive piece and
  is **derived in-repo, not imported** from the literature.
- The **fixed-`SU(3)` gauge-background extension** of that same 2-step
  positivity is the retained_bounded note
  [RP_P2_GAUGE_EXTENSION_AND_REALIZATION_RESIDUAL_NOTE_2026-05-28.md](RP_P2_GAUGE_EXTENSION_AND_REALIZATION_RESIDUAL_NOTE_2026-05-28.md),
  which establishes `T_hat^2[U]` positive Hermitian config-by-config at
  fixed arbitrary spatial `SU(3)` (and `U(1)`) background in temporal
  gauge, by a finite anti-Hermitian-hop modal reduction (the free
  `U = 1` case is the translation-invariant specialization of the note
  above). In the gauge-case reduction this carries the per-config
  fermion-sector factor from `U = 1` to fixed nontrivial background.
- [STAGGERED_ONLY_DET_POSITIVITY_CASE_A_NOTE_2026-05-17.md](STAGGERED_ONLY_DET_POSITIVITY_CASE_A_NOTE_2026-05-17.md)
  proves the configuration-by-configuration determinant positivity
  `det(M_KS + m I) = prod (m^2 + sigma_i^2) >= m^n > 0` for `m > 0` on
  every `SU(3)` background. In the gauge-case reduction this supplies
  the **positive determinant weight** factor. It is not by itself the
  fermion-sector transfer positivity (which is the in-repo runner
  above) and is not by itself sufficient for the single-step Lagrangian
  Gram-matrix positivity (per the load-bearing no-go runner).
- [REFLECTION_POSITIVITY_GAUGE_HALF_CAUCHY_SCHWARZ_NARROW_THEOREM_NOTE_2026-05-10.md](REFLECTION_POSITIVITY_GAUGE_HALF_CAUCHY_SCHWARZ_NARROW_THEOREM_NOTE_2026-05-10.md)
  supplies an abstract finite Cauchy-Schwarz norm-square identity
  under explicit symmetry hypotheses. In the gauge-case reduction this
  supplies the **gauge/bosonic-half norm-square** factor. That note
  explicitly disclaims the Wilson-plaquette boundary application; this
  row therefore cites it only for the abstract identity, not for a
  Wilson-plaquette boundary closure.
- The **Wilson temporal-gauge bridge for the gauge-half / Wilson-plane
  application** is supplied by
  [AXIOM_FIRST_REFLECTION_POSITIVITY_WILSON_TEMPORAL_GAUGE_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md](AXIOM_FIRST_REFLECTION_POSITIVITY_WILSON_TEMPORAL_GAUGE_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md)
  and
  [`audit_companion_reflection_positivity_wilson_temporal_gauge_2026_06_05.py`](../scripts/audit_companion_reflection_positivity_wilson_temporal_gauge_2026_06_05.py).
  That retained-bounded bridge translates the abstract gauge-half
  Cauchy-Schwarz hypotheses to the Wilson plaquette temporal-gauge
  boundary setup: it fixes the Wilson sign as
  `S_W = -B + constant`, proves the reflection split
  `B = B_+ + B_- + B_0` with `B_- = Theta B_+`, certifies the
  reflection-plane kernel `exp(B_0)` as a nonnegative character-coefficient
  Gram kernel on the displayed tractable groups, and verifies the integrated
  three-factor form `G = W diag(kappa) W^dag` with `kappa >= 0` on the
  `A_+^(2)` observable basis. This is the current load-bearing route for
  the Wilson-plane/gauge-half factor. The older
  `RP_WILSON_TEMPORAL_GAUGE_BRIDGE_SIGN_AND_POSITIVITY_REPAIR_NOTE_2026-06-06`
  source packet is historical context only here and is not a load-bearing
  dependency of this parent row.

The det-positivity and Cauchy-Schwarz authorities are cited only for
their stated narrow surfaces, each covering one named factor of the
proposed gauge-case reduction. The free-case derivation below (now
captured in the standalone free-case note) is the load-bearing positive
theorem support, and the fixed-`SU(3)` gauge-extension note carries it
to nontrivial background; the full interacting gauge closure remains limited
to the named factorized reduction claim and must be judged by the independent
audit lane. This note does not import any fitted value,
observed target value, literature numerical comparator, same-surface
family selector, or admitted unit convention.

## Statement (2-step blocked formulation)

Let `A_+^(2)` be the polynomial algebra generated by gauge and
staggered fermion fields supported in the positive-time half and
invariant under the 2-step blocking (one block = two lattice
spacings). On the staggered-only action surface

```text
    S = S_G[U] + bar(chi) (M_KS[U] + m I) chi,        m > 0,
```

the 2-step blocked transfer matrix `T_hat^2 = S_hat^2` over two
lattice spacings is positive Hermitian on the 2-step physical Hilbert
space `H_phys^(2)`. With vacuum-energy subtraction,

```text
    T_hat_tilde^2 := T_hat^2 / lambda_max(T_hat^2),
    H_hat_tilde   := -log(T_hat_tilde^2) / (2 a_tau),
```

one has `||T_hat_tilde^2|| = 1` and `H_hat_tilde >= 0`, i.e., the
2-step-blocked lattice energy spectrum is non-negative.

### 2026-06-08 Wilson temporal-gauge bridge reroute

The latest conditional audit of this row names one remaining parent blocker:
derive the full Wilson-plaquette gauge-half sesquilinear PSD form for the
non-time-symmetric, `U`-integrated configuration space, or keep the row
bounded. Current `main` now has a retained-bounded bridge for exactly the
Wilson plaquette temporal-gauge / gauge-half application:
[`AXIOM_FIRST_REFLECTION_POSITIVITY_WILSON_TEMPORAL_GAUGE_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md`](AXIOM_FIRST_REFLECTION_POSITIVITY_WILSON_TEMPORAL_GAUGE_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md).
This row is therefore rerouted through that bridge rather than through the
unaudited June 6 sign-repair packet.

On the finite factorized `A_+^(2)` surface above, for generators

```text
    F(U,chi) = F_G(U) F_f(chi),
```

the audited temporal-gauge bridge uses the corrected Wilson sign convention

```text
    S_W = -B + constant,       exp(-S_W) = constant * exp(B),
```

so the reflection-plane Boltzmann factor is `exp(B_0)`, not an
anti-ferromagnetic `exp(-beta Re Tr)` kernel. The bridge proves the reflection
split `B = B_+ + B_- + B_0`, realizes the Wilson-plane kernel as a
nonnegative character-coefficient Gram kernel, and verifies the integrated
three-factor RP form

```text
    G = W diag(kappa) W^dag,      kappa >= 0
```

on the stated `A_+^(2)` observable basis. Under that bridge, the parent
reflected form decomposes into the product/integral of four non-negative
factors:

```text
    <Theta(F) F>
      = integral dU
          K_mixed(U)
          det(M_KS[U] + m I)
          || exp(-S_+(U)) F_G(U) ||^2
          <vac_U | F_f^dag T_hat^2[U] F_f | vac_U>.
```

The signs of the four factors are supplied one hop:

- `K_mixed(U) > 0` from the temporal-gauge mixed-kernel factorization
  theorem
  [GAUGE_TEMPORAL_GAUGE_MIXED_KERNEL_SPATIAL_LINK_FACTORIZATION_NARROW_THEOREM_NOTE_2026-05-10.md](GAUGE_TEMPORAL_GAUGE_MIXED_KERNEL_SPATIAL_LINK_FACTORIZATION_NARROW_THEOREM_NOTE_2026-05-10.md);
- `det(M_KS[U] + m I) > 0` from the staggered determinant positivity
  theorem;
- the gauge-half norm square / plane-kernel PSD from the audited Wilson
  temporal-gauge bridge, with the abstract Cauchy-Schwarz note used only for
  the finite norm-square identity it actually proves;
- `<vac_U | F_f^dag T_hat^2[U] F_f | vac_U> >= 0` from the fixed-background
  two-step transfer positivity theorem, with the free construction below as
  its explicit specialization.

Finite linear combinations inherit a positive semidefinite Gram form by
polarization over these same factorized generators. This reroute supplies the
missing Wilson-plane application named in this row's latest conditional verdict
from a retained-bounded source. This note still does not mark this parent row
or any downstream row retained; independent audit must judge the composed
parent claim.

**2026-07-09 in-packet supplier for the plane-kernel / composed-Gram step.**
The third factor's plane-kernel PSD and the integrated two-slice Gram PSD are
now proved in-packet by
[SU3_WILSON_PLANE_KERNEL_CHARACTER_POSITIVITY_AND_COMPOSED_GRAM_NARROW_THEOREM_NOTE_2026-07-09.md](SU3_WILSON_PLANE_KERNEL_CHARACTER_POSITIVITY_AND_COMPOSED_GRAM_NARROW_THEOREM_NOTE_2026-07-09.md):
for every `beta >= 0` the `SU(3)` fundamental Wilson plane kernel
`exp(beta Re tr W)` has nonnegative character coefficients, hence the
reflection-plane kernel is positive semidefinite and the integrated two-slice
temporal-gauge Gram is positive semidefinite on the stated `A_+^(2)` surface
at any finite `L_s`. The paired reroute runner now evaluates the actual
composed `SU(3)` form directly — the Haar-sampled plane-kernel Gram, the
composed two-slice Gram at `L_s = 2` through that supplier's machinery, and a
no-conjugation rejector — in place of the earlier synthetic product model.

### In-repo first-principles construction and proof (free case)

This positivity is **derived in-repo from the staggered action**, not
imported. The standalone derivation note is
[AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28.md](AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28.md),
and the construction with its numerical verification is the primary
positive runner
[`scripts/axiom_first_rp_two_step_transfer_matrix_positivity.py`](../scripts/axiom_first_rp_two_step_transfer_matrix_positivity.py).
The free case (`U = 1`) is treated explicitly and decisively below; the
fixed-`SU(3)` gauge-background extension of the same object is the
retained_bounded note
[RP_P2_GAUGE_EXTENSION_AND_REALIZATION_RESIDUAL_NOTE_2026-05-28.md](RP_P2_GAUGE_EXTENSION_AND_REALIZATION_RESIDUAL_NOTE_2026-05-28.md),
and the full gauge case is reduced to that extension plus two retained
dependencies (see "Gauge-case reduction" below).

**Why two steps (mechanism, not citation).** With the canonical
staggered phases `eta_0 = 1` and `eta_1(t) = (-1)^t` the temporal hop
is clean but the spatial phase alternates with the time slice. The
single-step transfer operator therefore alternates between two forms
`T_even` (slices with `(-1)^t = +1`) and `T_odd` (slices with
`(-1)^t = -1`); the physical object is `T_hat^2 = T_odd . T_even` over
two lattice spacings. This is the same alternation that makes the
single-step Lagrangian Gram matrix non-PSD (no-go runner, min eig
`-0.80`); the two surfaces are distinct.

**Step 1 — single-step transfer from the action.** For free staggered
fermions in `1+1d` (one Grassmann component per site, `L_s` spatial
sites, periodic) at fixed spatial momentum `p`, the staggered action's
banded-in-time mode equation is

```text
    alpha_t psi_t + (1/2) psi_{t+1} - (1/2) psi_{t-1} = 0,
    alpha_t = m + i eta_1(t) sin(p) = m + i (-1)^t sin(p),
```

which rearranges to `psi_{t+1} = -2 alpha_t psi_t + psi_{t-1}`, i.e.
the single-step classical transfer matrix on the amplitude 2-vector
`V_t = (psi_t, psi_{t-1})`:

```text
    V_{t+1} = T_s V_t,    T_s = [[ -2 alpha_s, 1 ], [ 1, 0 ]],
    alpha_even = m + i sin(p),   alpha_odd = m - i sin(p).
```

`T_even`, `T_odd` come straight from the action; no convention is
admitted.

**Step 2 — single-step non-positivity (consistent with the no-go).**
For `p != 0`, `spec(T_even)` and `spec(T_odd)` are genuinely complex
(off the positive real axis); the runner reports
`max |Im eig(T_even/T_odd)| = 1.62` at `m = 0.5`. A single-step
transfer operator with complex single-particle spectrum is not a
positive operator. This independently reproduces the single-step
no-go on the transfer-matrix side.

**Step 3 — dispersion anchor (faithfulness).** The 2-step classical
matrix `T2cl(p) = T_odd(p) . T_even(p)` has eigenvalues
`{ e^{+2 E(p)}, e^{-2 E(p)} }` with

```text
    E(p) = arcsinh( sqrt( m^2 + sin^2 p ) ),    sinh^2 E(p) = m^2 + sin^2 p,
```

the exact free staggered `1+1d` dispersion. The decaying (physical)
eigenvalue is `e^{-2 E(p)}`, real and positive. The runner verifies
this match across the Brillouin zone with maximum residual
`3.4e-16`. Reproducing the known dispersion is the proof that the
construction is faithful to the staggered action, not an artifact.

**Step 4 — many-body 2-step positivity.** For a free (quadratic)
fermion theory the many-body transfer operator is the second
quantization `Gamma(t1)` of the single-particle transfer kernel `t1`
(the standard free-fermion relation between a lattice fermion transfer
matrix and its single-particle kernel). The single-particle 2-step
kernel is the action-derived decaying eigenvalue
`t1^(2)(p) = e^{-2 E(p)}` from Step 3, real and positive, so on the
Fock space `H = tensor_p {|0>, |1>}` (dimension `2^{L_s}`)

```text
    T_hat^2 = Gamma( t1^(2) ) = tensor_p diag( 1, e^{-2 E(p)} )
            = exp( -2 a_tau H_hat ),     H_hat = sum_p E(p) a_p^dag a_p.
```

Since `E(p) >= 0` for all `p`, `H_hat >= 0`, hence `T_hat^2` is
positive Hermitian with `||T_hat^2|| = 1` (vacuum) and admits the
explicit factorization

```text
    T_hat^2 = B^dag B,    B = exp( -a_tau H_hat ) = tensor_p diag( 1, e^{-E(p)} ).
```

This is exactly the 2-step reflection-positivity statement:
`H_hat = -log(T_hat^2) / (2 a_tau)` is self-adjoint and bounded below
by `0`. The runner builds `T_hat^2` from the action-derived classical
2-step eigenvalue (not posited), confirms positive Hermitian
(`min eig > 0`) and the exact `B^dag B` reconstruction
(`||T_hat^2 - B^dag B|| ~ 6e-17`) for `L_s in {2, 3, 4, 6}`, and over
a mass range `m in [0.05, 5.0]`.

**Cross-check (route R2 — 2-step OS Gram).** The Osterwalder-Schrader
reflected two-point correlator on the 2-step blocked surface, in the
transfer-matrix representation, is
`G(F_I, F_J) = <vac| F_I^dag T_hat^2 F_J |vac>` for second-quantized
positive-time observables. This is the genuine OS Gram on the 2-step
blocked surface; it is manifestly Hermitian and PSD iff `T_hat^2 >= 0`.
The runner builds it explicitly on the Fock space and confirms it is
Hermitian with `min eig = 0` (PSD), in direct contrast to the
single-step naive Lagrangian Gram (`min eig = -0.80`). R1 and R2 agree.

### Gauge-case reduction target

The intended `SU(3)`-gauged staggered 2-step RP closure is the
following reduction target:

```text
    (temporal-gauge mixed kernel K_mixed(U) > 0)          [retained dep]
  x (positive determinant weight det(M_KS + m I) > 0)     [retained dep]
  x (Wilson gauge-half plane-kernel/norm-square bridge)   [retained_bounded dep]
  x (fixed-background 2-step fermion transfer positivity) [retained_bounded dep]
```

The fermion-sector 2-step transfer-matrix positivity is supplied
in-repo: the free `U = 1` case is the construction above (Steps 1–4 +
R2), captured in
[AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28.md](AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28.md),
and the fixed-`SU(3)` gauge-background extension (`T_hat^2[U]` positive
Hermitian config-by-config at arbitrary fixed spatial background in
temporal gauge) is the retained_bounded note
[RP_P2_GAUGE_EXTENSION_AND_REALIZATION_RESIDUAL_NOTE_2026-05-28.md](RP_P2_GAUGE_EXTENSION_AND_REALIZATION_RESIDUAL_NOTE_2026-05-28.md).
The positive gauge weight is the retained Case A determinant note
(`det(M_KS + m I) = prod (m^2 + sigma_i^2) >= m^n > 0`
config-by-config on every `SU(3)` background). The gauge/bosonic half is
now routed through the retained-bounded Wilson temporal-gauge bridge plus the
abstract gauge-half Cauchy-Schwarz identity, rather than through the abstract
identity alone. The full interacting `U`-integrated positivity is not claimed
beyond this explicitly scoped factorized reduction target and remains subject
to independent audit of this parent row.

This replaces the prior citation-only treatment: the 2-step blocked
positivity is now the in-repo first-principles result above (free case
explicit, gauge case reduced), with the published STW 1981 /
Palumbo 2002 / Smit §6 treatments named only as context for the same
standard object.

## Single-step no-go (load-bearing on the runner)

The primary runner builds the staggered KS Dirac matrix
`M = M_KS + m I` on `L_t = 4`, `L_s = 2`, `m = 0.5`, with U(1)
Abelian gauge links and link-reflection `theta(t, x) = (-1-t, x)`. It
computes the Gram matrix

```text
    G_{IJ} = <Theta(F_I) . F_J>_S
```

via Berezin/Wick contraction with propagator `M^{-1}` for a basis of
monomials in `A_+` up to degree 2 (37 basis elements), and reports the
minimum eigenvalue of the Hermitised Gram matrix.

Results from the cached run:

- Free `U = 1` case: Gram minimum eigenvalue `= -0.80`. Diagonal
  entries for degree-1 monomials `chi_x` and `bar(chi)_x` are all
  `-0.4`.
- 5 random U(1) gauge configurations: 5/5 PSD violations with
  minimum eigenvalues in `[-2.10, -1.08]`.

The mechanism behind the no-go is structural: under temporal
reflection `theta(t, x) = (-1-t, x)`, the staggered spatial phase
`eta_1(x) = (-1)^{t_x}` flips sign across the reflection plane,
because parity of the temporal index is exchanged. The simple
Sharatchandra Theta (chi swap chi-bar with site relabel) does not
include a phase compensator for this asymmetry, so the action is not
reflection-invariant under Theta alone in the spin basis. The result
matches Caracciolo-Palumbo (arXiv:1210.1786).

The 2-step blocked formulation works around this by using a 2-step
temporal interval, where the alternating spatial phase `eta_1 = (-1)^t`
returns to its original sign and the single-step transfer factors
`T_even`, `T_odd` combine into the positive `T_hat^2 = T_odd . T_even`.
This is now derived in-repo (§"In-repo first-principles construction
and proof"); the same standard object appears in STW 1981, Palumbo
2002, Smit, and the Golterman 2024 staggered review (arXiv:2406.02906).

This no-go is deliberately narrow. It rules out the direct
single-step spin-basis Lagrangian Gram matrix under Sharatchandra
Theta alone, as tested by the runner. It does not rule out a
phase-compensated reflection, a square-root construction, a flavour-
basis construction, or the 2-step blocked transfer matrix; those are
separate surfaces, and the 2-step blocked surface is kept as the
positive scope of this note.

## Hamiltonian-level secondary exhibits

The secondary runner
[`scripts/axiom_first_reflection_positivity_check.py`](../scripts/axiom_first_reflection_positivity_check.py)
provides structural finite-block checks for the chosen lattice
Hamiltonian `H_lat` (built from KS hop matrix plus mass):

- `E1`: `T = exp(-a_tau H_lat)` is Hermitian and positive (trivially,
  because `H_lat` is Hermitian by construction);
- `E2`: U(1) Wilson plaquette transfer matrix is Hermitian and
  positive (trivial, for the same reason);
- `E3`: `<vac| F^dagger T^tau F |vac>` is non-negative for a finite
  list of `F` monomials acting on the chosen `H_lat`;
- `E4`: the Gram matrix on the Fock basis is PSD (which equals `T`
  itself, again trivial);
- `E5`: the staggered chirality anticommutation `{epsilon, M_KS} = 0`
  (a structural algebraic identity);
- `E6`: a Wilson-fermion determinant diagnostic (non-load-bearing).

`E1`-`E4` are not Lagrangian RP exhibits. They demonstrate
**Hamiltonian-level positivity** for a chosen `H_lat` via the trivial
fact that `exp(-a_tau H)` is positive if `H` is Hermitian. The
load-bearing Lagrangian RP claim is governed by the primary no-go
runner, not by these structural exhibits.

`E5` is a genuine algebraic identity that supports the determinant
positivity input (it is the source of the +/- lambda paired-eigenvalue
identity used in the Case A determinant note).

These secondary `E1`-`E4` exhibits are distinct from the new positive
2-step runner. The secondary runner assumes a Hermitian `H_lat` and
notes `exp(-a_tau H_lat)` is positive (trivial). The new primary
positive runner instead **constructs** the transfer operator from the
staggered Lagrangian action: it derives that the single-step `T_hat`
is non-positive (complex single-particle spectrum) while the 2-step
`T_hat^2 = T_odd . T_even` is positive Hermitian with
`H_hat = sum_p E(p) a_p^dag a_p >= 0`, with `E(p)` fixed by the action
(the free staggered dispersion). That `H_hat >= 0` is a derived
consequence of the action's two-step structure, not an assumed
Hermiticity.

## What this note does NOT claim

The newly load-bearing positive support is the **free-case** fermion-
sector 2-step transfer positivity (explicit, §"In-repo first-principles
construction and proof"). The gauge-case text records a reduction
target to two retained deps, not a fresh interacting proof. The note
does **not** claim:

- single-step Lagrangian RP for staggered KS in the spin basis;
- a universal impossibility theorem for every conceivable one-step
  staggered transfer-matrix construction;
- a from-scratch full interacting `SU(3)` 2-step RP proof: the gauge
  case is reduced to named retained/retained-bounded factor authorities,
  not re-derived;
- an interacting-fermion-sector 2-step transfer positivity from scratch
  on a non-trivial `SU(3)` background: the explicit construction is the
  free (`U = 1`) case, and the gauge sector enters only through the
  retained positive determinant weight;
- an author-applied retained status for this parent row; the Wilson
  temporal-gauge bridge is cited at its own retained-bounded scope, and this
  row's composed parent claim still requires independent audit;
- a full staggered + Wilson fermion RP theorem;
- an unconditional Wilson-sector determinant positivity statement;
- continuum-limit / OS-reconstruction RP from this lattice setup
  alone;
- a global claim that every historical citation to this row is safe
  without checking whether the downstream consumer uses single-step
  or 2-step RP (downstream consumers that depend on single-step RP
  specifically need to be re-audited; consumers that only need
  "RP holds for staggered KS lattice in the standard sense" are
  compatible with the 2-step formulation).

## No-Go Discipline Gate

This gate applies only to the narrow negative claim:

```text
Direct single-step spin-basis Lagrangian RP for staggered KS under
Sharatchandra Theta alone is non-PSD on the tested finite surface.
```

The gate does not assert a universal no-go over all possible one-step
or phase-compensated constructions.

- **N1 Alternative routes.**
  1. Direct Sharatchandra single-step Gram matrix: ATTEMPTED; the
     primary runner gives a free-configuration counterexample with
     minimum eigenvalue `-0.80`.
  2. Same direct surface under random U(1) links: ATTEMPTED; the
     primary runner finds PSD failure in 5/5 sampled configurations.
  3. Pure Hamiltonian positivity `T = exp(-aH)`: ATTEMPTED by the
     secondary runner, but it proves only Hamiltonian positivity for a
     chosen `H_lat`; it does not prove Lagrangian RP.
  4. 2-step blocked transfer matrix: DERIVED IN-REPO (free case) by
     the new positive 2-step runner — `T_hat^2 = T_odd . T_even` is
     positive Hermitian, with single-step `T_hat` non-positive in the
     same construction. This is the adopted positive scope, not a
     counter to the narrow single-step no-go.
  5. Phase-compensated or square-root one-step construction:
     UNTESTED AND OUT OF SCOPE; the note does not claim this route is
     impossible.
- **N2 Wall independence.** The narrow no-go has one collapsed wall:
  the direct single-step Sharatchandra-Theta spin-basis Lagrangian
  Gram matrix is non-PSD. Basis choice, single-step timing, and
  missing phase compensation are not independent walls; they are the
  defining components of the tested surface.
- **N3 Hidden-wall scan.** "Published literature" is context for the
  2-step surface, not proof of the single-step finite counterexample.
  "Standard" means the 2-step blocked construction. The *secondary*
  runner's `H_lat` exhibits (E1-E4) remain non-load-bearing for the
  negative no-go claim. (Separately, the *positive* 2-step runner's
  Hamiltonian-level result `H_hat >= 0` is derived from the action and
  is load-bearing for the positive 2-step claim, not for this gate.)
- **N4 Residual matching.** The runner attacks exactly the residual
  from the prior overclaim: direct single-step `G_{IJ} =
  <Theta(F_I) F_J>_S` positivity for staggered KS in the spin basis.
  The literature citations support the 2-step replacement surface and
  are not used as finite counterexample evidence.
- **N5 Rhetoric audit.** The negative phrase is restricted to this
  per-finite-block, per-tested-Gram-surface construction. It is not
  stated as a lattice-wide impossibility theorem or as a no-go for
  all one-step transfer matrices.
- **N6 Partial-closure path.** The partial closure path is the 2-step
  blocked formulation; it is adopted here, derived in-repo (free case)
  by the positive 2-step runner, and does not require a new axiom.
- **N7 Steelman.** A hostile reviewer could argue that a modified
  reflection with compensating staggered phases, a square root of a
  2-step transfer matrix on a different Fock space, or a flavour-basis
  construction might define a positive one-step object. This note does
  not deny that possibility; it narrows the claim to the directly
  tested Sharatchandra-Theta spin-basis Lagrangian surface.
- **N8 Cross-cycle echo.** The 2026-05-26 Wilson-subsurface repair
  already showed that this row must not absorb unsupported stronger
  fermion-sector claims. The same mechanism applies here: preserve
  the durable positive scope, remove the unsupported stronger surface,
  and queue the source row for independent re-audit.

Gate outcome: **PASS for the narrow no-go; FAIL for any broader
universal single-step impossibility claim.** This note ships only the
narrow no-go.

## Honest Status

Branch-local source-surface repair. The narrowed source claim is a
**2-step blocked** staggered-only reflection-positivity theorem
proposal for independent re-audit. As of 2026-05-28 the 2-step
positive claim is **derived in-repo from first principles** (free case
explicit, via the new positive 2-step runner; gauge case recorded as a
reduction target to two retained deps), replacing the prior
citation-only treatment. The
explicit single-step no-go runner remains intact and documents the
failure of the prior overreach. This note does not set or predict an
audit outcome; it is not an author-applied audit promotion, and
independent audit is still required.

What this can support if audit passes:

- downstream claims that need reflection positivity for the standard
  staggered-KS lattice (interpreted as 2-step blocked) can continue
  to cite this row, now backed by the in-repo free-case construction;
- downstream claims that load-bear specifically on **single-step**
  Lagrangian RP in the spin basis must be re-audited against the
  no-go runner here.

What this does not support:

- a full single-step staggered RP theorem (no-go per the single-step
  runner + Caracciolo-Palumbo 2013);
- a from-scratch interacting `SU(3)` 2-step RP proof: the explicit
  construction is the free case; the gauge case is only a scoped
  reduction target to the two named retained deps;
- a full staggered + Wilson-fermion RP theorem;
- an unconditional Wilson-sector determinant positivity statement.

## Audit dependency repair links

This graph-bookkeeping section records explicit dependency links named by a prior conditional audit so the audit citation graph can track them. It does not promote this note or change the audited claim scope.

- [gauge_os_step1_wilson_plaquette_decomposition_theta_invariance_reflection_hermiticity_narrow_theorem_note_2026-06-02](GAUGE_OS_STEP1_WILSON_PLAQUETTE_DECOMPOSITION_THETA_INVARIANCE_REFLECTION_HERMITICITY_NARROW_THEOREM_NOTE_2026-06-02.md)
