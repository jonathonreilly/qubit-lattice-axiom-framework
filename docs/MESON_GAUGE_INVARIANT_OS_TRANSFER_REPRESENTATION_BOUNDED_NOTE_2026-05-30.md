# Gauge-Invariant, Number-Conserving Meson OS Transfer Representation Equality on a Finite 3+1 Staggered Carrier — Bounded Note

**Date:** 2026-05-30
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Review boundary:** source-surface bounded theorem proposal. This note records
runner-backed source content; downstream effective status is not set here.
**Primary runner:** [`scripts/meson_gauge_invariant_os_transfer_representation_2026-05-30.py`](../scripts/meson_gauge_invariant_os_transfer_representation_2026-05-30.py)
**Cached runner output:** [`logs/runner-cache/meson_gauge_invariant_os_transfer_representation_2026-05-30.txt`](../logs/runner-cache/meson_gauge_invariant_os_transfer_representation_2026-05-30.txt)
**Source packet verifier:** [`scripts/meson_os_transfer_source_packet_manifest_2026_06_06.py`](../scripts/meson_os_transfer_source_packet_manifest_2026_06_06.py)
(SUMMARY: MESON OS SOURCE PACKET PASS=37 FAIL=0)
**Source packet verifier cache:** [`logs/runner-cache/meson_os_transfer_source_packet_manifest_2026_06_06.txt`](../logs/runner-cache/meson_os_transfer_source_packet_manifest_2026_06_06.txt)
**Source packet verifier JSON:** [`outputs/meson_os_transfer_source_packet_manifest_2026_06_06.json`](../outputs/meson_os_transfer_source_packet_manifest_2026_06_06.json)
**Source role:** finite-carrier *representation* theorem for the **gauge-invariant,
number-conserving meson** observable of the 2-step blocked staggered transfer matrix.
On explicit finite **3+1** carriers it records the equality between the runner's
det-weighted finite Haar-sample/quadrature average of the time-reflected Berezin
**meson two-point correlator** `<Theta(F_L) F_L>` (a connected 4-fermion correlator) and
the matching operator-side transfer-matrix meson two-point (the particle-hole
connected quark-line loop). It **handles, rather than dodges, the vacuum-annihilation
obstruction** that the base note left open: `Ohat_meson|Omega> = 0`, yet
`<Theta(F_L) F_L>` is nonzero and equals the operator connected quark-line loop. This note
does **not** establish the continuum / OS-reconstruction (Wightman) limit, Euclidean
rotational (Lorentz) restoration, the compact-group Wilson-boundary positivity (H1),
or a full interacting-RP closure; and it does not close the per-config fermion 2-step
rung (a separate unresolved row).

## The deliverable (lead)

This note establishes, on explicit finite **3+1** carriers (3 spatial + 1 temporal;
the transfer matrix runs in the time direction, the spatial lattice is the regulator)
and the runner's finite Haar samples/quadratures, the **gauge-invariant,
number-conserving meson representation equality** for a basis of OS-block meson
representatives

```text
   F_L(U) = bar(chi)_+ L_U(V) chi_+,
   L_U(V) = W_b(U) V(U) W_a(U)^dag,
   V_(x,a),(y,c)(U) = U(x,y)_ac .
```

Here `V` labels the Wilson-line meson `Fhat_V=c^dag V c` on the operator one-particle
space. `F_L` is its raw two-slice Berezin representative. The claim is for this
OS-block projected representative, **not** for inserting `V` on one unprojected raw
time slice. The isometries `W_a,W_b` are fixed from the one-field cross kernels before
and independently of `V`, and the same pair is used for every observable. The two sides
are computed by **separate kernel-build paths**:

```text
   <Theta(F_L) F_L>_Berezin,Q
       = (1/Z_Q) sum_{U in Q} w_U det(M[U]) <Theta(F_L) F_L>^ferm_U
       = G_operator,Q(V,V) ,
   Z_Q = sum_{U in Q} w_U det(M[U]),  w_U = exp(-S_G[U]).
```

Here `Q` is the runner's finite U(1) quadrature or fixed SU(3) Haar sample, not an
exact full Haar integral.

- **Berezin** — a genuine many-field Grassmann/Wick construction. At each fixed gauge
  background `U`, `<Theta(F_L) F_L>^ferm_U` is the connected part of the explicit
  four-field `2 x 2` covariance minor of one full-spacetime `M[U]^{-1}`. The same
  `Lt=28` matrix supplies `det(M[U])`. Its two cross-reflection blocks independently
  determine the particle and hole temporal isometries; the runner checks their sign,
  normalization, eigenvectors, orthogonality, spatial-mode decoupling, and intertwining
  with the operator kernel before lifting the meson into the two-slice field space. The
  `U`-average is the det-weighted finite Haar-sample/quadrature average
  `(1/Z_Q) sum_{U in Q} e^{-S_G[U]} det(M[U]) (...)`, evaluated with stable `slogdet`
  weights from that same `M[U]`.
- **Operator** — the transfer-matrix meson two-point. The forward 2-step block
  propagator is built **independently** from the fermion-Fock transfer matrix,
  `G_f^op = C_BLOCK · Q diag(e^{-2 E_j}) Q^dag`, equivalently
  `G_f^op[b,b'] = C_BLOCK <Omega| c_b e^{-2 Hhat[U]} c_{b'}^dag |Omega>` in the
  position-color basis. The meson two-point is the connected loop + disconnected bubble.
  The **connected (OS-positive) meson channel** is

  ```text
     Tc(F) = Tr[ V^dag G_f V G_f ] = || G_f^{1/2} V G_f^{1/2} ||_F^2  >= 0 ,
  ```

  **manifestly a Gram** — the free connected quark-line loop, both legs
  forward-propagating after the OS reflection sends the `chibar` leg to the image half.
  This is **not** the trivially-zero `<Omega| Ohat_meson^dag T Ohat_meson |Omega>`, and
  **not** a vacuum sum `sum_n |<n| Ohat_meson |0>|^2` (which vanishes since
  `Ohat_meson|0> = 0`).

The two paths share **only the lattice action** (the spatial-hop spectrum
`{lambda_j(U), E_j(U)}` and the hop-eigenbasis `Q`, properties of `S[U]`, not of either
Hilbert-space construction) — the same independence boundary the base note used. The
Berezin side builds and inverts the full finite Grassmann matrix, extracts both temporal
isometries from its cross-reflection eigenvectors, and evaluates covariance minors. The
operator side builds `G_f` from the fermion-Fock one-body transfer matrix
`e^{-2 Hhat[U]}`. The direct minor never calls the reduced operator trace.

The equality holds to a worst `|Berezin − operator|` of `5.14e-12` over the
gauge-invariant meson basis on the finite 3+1 carriers (well inside the `1e-9` assertion
gate). This is the **lattice / transfer-matrix** representation, exhibited on a finite
carrier and **illustrating** the cited general transfer-matrix meson-spectroscopy
construction; **no continuum claim is made either way**.

## 2026-07-29 Same-Matrix Four-Field Repair

The prior packet still mixed two finite measures: `det_M_finite(..., nt=1)` supplied an
`Lt=2` determinant, while the reflected block kernel came from an `nt=14`, `Lt=28`
chain. Moreover, the old `meson_correlator_full_berezin` expanded the reduced trace
after constructing a two-point kernel; it did not evaluate a four-field minor of the
matrix supplying the determinant. This repair removes both gaps.

For each fixed gauge background, the runner now builds exactly one

```text
M_U = M_KS[U] + m I,       Lt = 2 NT_BULK = 28,
S_U = M_U^{-1},            det weight = det(M_U).
```

Let `+` denote block slices `(0,1)` and `-` their ordered OS images `(-1,-2)`. Define
the raw cross blocks `A=S_U[+,-]` and `C=S_U[-,+]`. In the spatial-hop eigenbasis they
split, to numerical precision, into rank-one `2 x 2` temporal blocks. The positive
temporal eigenvectors of `A` and `-C` give independently extracted isometries `W_a`
and `W_b`. The runner checks

```text
W_a^dag W_a = W_b^dag W_b = I,
W_a^dag A W_a = G_f^op,
-W_b^dag C W_b = G_f^op,
A W_a = W_a G_f^op,
C W_b = -W_b G_f^op,
eig_phys(A) = eig_phys(-C) = 2 exp(-2 E).
```

Thus the `C_BLOCK=2` normalization and both particle/hole eigenvector identifications
are recovered from the same full matrix, rather than assumed inside the meson
contraction. For a position-color meson matrix `V`, the claimed Grassmann observable is
`F_L=bar(chi)_+ L_U(V) chi_+`, with `L_U(V)=W_b V W_a^dag`. The isometries are obtained
once per background, before `V` is supplied, so this is a common block-field
identification rather than an observable-by-observable fit. The full normalized
four-field Gaussian integral is evaluated
as the explicit Wick minor

```text
sum_{p,q,k,l} conj(L_I[p,q]) L_J[k,l]
  det [[ S_U[-p,-q], S_U[-p,+k] ],
       [ S_U[+l,-q], S_U[+l,+k] ]].
```

Subtracting the first (disconnected) determinant term leaves the connected correlator

```text
-sum_{p,q,k,l} conj(L_I[p,q]) L_J[k,l]
    C[p,k] A[l,q],
```

which is compared independently with `Tr[V_I^dag G_f^op V_J G_f^op]`. An explicit
permutation implementation of Wick's theorem is separately checked against the `2 x 2`
minor ordering. The correct one-field reflection `Theta(chi)=-bar(chi)` makes `A` and
`-C` positive on their physical subspaces; reversing it makes the entire physical
one-field spectrum negative. A meson bilinear contains two reflected fields, so its
global sign alone cannot choose this convention; the one-field block check does.

The same `slogdet(M_U)` weights both the direct-minor and operator averages. Across the
listed carriers the worst fixed-background direct-minor/operator residual is
`5.14e-12`, the worst determinant-weighted average residual is `5.39e-14`, the worst
particle/hole eigenvector-intertwining residual is `3.13e-12`, and all determinant
phase residuals are below `3.5e-15`.

## Scope (honest — what is delivered vs open)

- **Number-conserving meson block representative — delivered (finite carrier).** The
  observable is `F_L=bar(chi)_+ W_b V W_a^dag chi_+`, the 2-step representative of the
  gauge-invariant operator `Fhat_V=c^dag V c` with Wilson-line matrix `V`. A raw
  single-slice `bar(chi)_0 V chi_0` equality is outside the claim. The
  vacuum-annihilation obstruction is handled (control **K1**):
  `Ohat_meson|Omega> = 0` exactly, yet the meson two-point `<Theta(F_L) F_L>` is nonzero and
  equals the operator particle-hole connected quark-line loop. This addresses the scope
  limitation the base note left open on the finite carrier.
- **Multi-spatial-dimensional SU(3) — delivered (finite carrier).** The meson equality is
  verified on a genuine **multi-spatial-dimensional SU(3)** carrier: the `2 x 2 x 1`
  spatial sheet at **N_c = 3** (12 modes, 4 sites, genuine color-mixing). The base note's
  second scope limitation (genuine SU(3) color-mixing on a 1-spatial-dimensional `2 x 1 x 1`
  carrier only, with the `2 x 2 x 1` sheet abelian) is therefore also addressed here for
  the meson observable.
- **Operator side is the fermion-Fock transfer two-point.** On a finite lattice the gauge
  field is a c-number integration variable; the verified equality is between the Berezin
  path and the per-configuration fermion-Fock meson two-point, identically classically
  `U`-averaged on both sides with the weight `e^{-S_G[U]} det(M[U])` and the Wilson
  amplitudes `U(x,y)`. No literal `H_gauge ⊗ H_ferm` quantum operator-sandwich claim is
  made.
- **Continuum / Lorentz out of scope.** The continuum / OS-reconstruction (Wightman)
  limit and Euclidean rotational (Lorentz) restoration are **not** addressed; the
  framework is 3+1 and **no continuum claim is made either way**.

## Mandatory non-vacuity controls (each fires)

The runner reports, for every carrier:

- **K1 — vacuum-annihilation handled (decisive).** `Ohat_meson|Omega> = 0` exactly
  (`||F|Omega>|| = 0`, via genuine Jordan-Wigner occupation action) **and** the meson
  two-point `<Theta(F_L) F_L>` is nonetheless **NONZERO** (min over the meson basis `0.06`–`0.87`)
  and equals the operator particle-hole connected quark-line loop. Proves the obstruction is
  handled, not papered over.
- **K2 — per-mode-factorized Berezin BREAKS.** On a mode-mixing carrier (non-uniform
  links lifting the spatial-mode degeneracy), replacing the genuine (non-diagonal)
  forward block propagator `G_f` by its per-mode-diagonal restriction (the prior-vacuity
  object) **breaks** the meson equality: worst `|G_ber_permode − G_op|` is **large**
  (`0.46` for SU(3) 2×2×1, `0.27` for U(1) 2×2×1). On the *degenerate* minimal carrier the
  reconstructed propagator is diagonal and the per-mode object does **not** differ (gap
  `~5.3e-14`) — the explicit demonstration that the prior vacuity is the degenerate /
  mode-diagonal regime.
- **K3 — det-weight.** Replacing the theorem's same-`M` det-weighted `U`-average by a flat
  `U`-average changes the target value (gap `0.13`–`0.34`). This proves the determinant
  weight is load-bearing for the stated measure; it is not a claim that the two code paths
  would disagree if both were intentionally evaluated with the same flat measure.
- **K4 — single-step.** The single-step (no 2-step blocking) reflected metric is
  **indefinite** (min eigenvalue `< 0`; the `-0.80` Caracciolo–Palumbo obstruction in this
  tested construction), so it cannot equal the positive operator sandwich used by this
  representation. This is a negative control for the runner, not a repo-wide
  impossibility theorem.
- **K5 — gauge invariance.** The Wilson-line matrix `V(U)` is covariant under SU(3)/U(1)
  endpoint transformations, and the cross-kernel isometries transform with the same
  one-particle action. Consequently `F_L` is a color singlet. Under
  `chi(y) -> g_y chi(y)`, `chibar(x) -> chibar(x) g_x^dag`,
  `U(x,y) -> g_x U(x,y) g_y^dag`, `F` is unchanged. The runner verifies (a) the
  Wilson-line covariance `g_x U(x,y) g_y^dag = U_g(x,y)` to `~1e-16`, and (b) the meson
  direct-minor two-point `<Theta(F_L) F_L>` is invariant under random gauge transforms
  to `~1e-15`.

Positive results: the per-config Berezin = operator meson instance holds to `~1e-12`
(**P1**); the det-weighted finite-sample average to `~1e-12` (**P0**); the forward block
propagator's positive eigenvalue equals `C_BLOCK · e^{-2E}` with `C_BLOCK = 2` a priori
(**P_block**), confirmed three independent ways — the per-mode temporal-chain block metric
(Grassmann `M^{-1}`), the operator Fock `e^{-2 Hhat}`, **and** the full-spacetime `M[U]^{-1}`
block metric spectrum (a single `(Lt · N_s · N_c)`-dimensional matrix inverse, the most
independent Berezin build) — all agreeing to `~1e-12`; and `det(M[U]) > 0` over the whole
`U`-quadrature.

### Worst residuals (deterministic, single-seed; `SCORECARD PASS=116 FAIL=0`)

| Carrier (spatial × N_c) | Object | worst residual / value |
|---|---|---|
| SU(3) 2×2×1 (4 sites, 12 modes) | **same-M det-weighted finite-sample avg** direct Wick minor == operator meson (the headline; multi-dim SU(3)) | `5.39e-14` |
| SU(3) 2×2×1 | per-config same-M Berezin minor (4-ferm) == operator meson | `2.65e-12` |
| SU(3) 2×2×1 | **K1** `\|\|Fhat_V\|Omega>\|\|` / min `<Theta(F_L)F_L>` | `0.0` / `0.41` |
| SU(3) 2×2×1 | full-spacetime `M^{-1}` block spectrum vs operator `e^{-2E}` | `2.6e-12` |
| SU(3) 2×2×1 | same-M eigvec / explicit-Wick-vs-minor / det-phase / direct-minor gauge inv | `1.37e-12` / `1.11e-16` / `3.23e-15` / `1.78e-15` |
| SU(3) 2×2×1 | **K2** per-mode gap / **K3** flat-vs-det gap / **K4** single-step min eig / **K5** gauge inv | `0.46` / `0.15` / `-0.55` / `1.78e-15` |
| SU(3) 2×1×1 (2 sites, 6 modes) | same-M det-weighted finite-sample avg direct minor == operator meson | `8.37e-16` |
| SU(3) 2×1×1 | per-config same-M Berezin minor (4-ferm) == operator meson | `5.14e-12` |
| U(1) 2×2×1 (4 sites, 4 modes) | same-M det-weighted finite-sample avg direct minor == operator meson | `1.78e-15` |
| U(1) 2×2×1 | **K1** min `<Theta(F_L)F_L>` / **K2** per-mode gap (mixing) | `0.06` / `0.27` |
| U(1) 2×1×1 (minimal; DEGENERATE) | same-M det-weighted avg direct minor == operator meson | `8.35e-17` |
| U(1) 2×1×1 (minimal) | **K2** per-mode gap (degenerate ⇒ no mixing ⇒ no break) | `1.11e-16` |

The worst `|Berezin − operator|` over the gauge-invariant meson basis is `5.14e-12`
(SU(3) 2×1×1 per-config). The exact worst residuals and control gaps are printed by the
runner.

## What is cited (standard methodology) vs derived (in-repo)

**Cited** — imported as standard lattice-gauge methodology, not reproven here:

- Lüscher, *Comm. Math. Phys.* **54** (1977) 283 — transfer-matrix construction,
  reflection = adjoint, Hilbert-space reconstruction from the Euclidean correlator;
  meson two-point spectral decomposition;
- Osterwalder–Seiler, *Ann. Phys.* **110** (1978) 440 — gauge + fermion lattice OS
  positivity and the reflection on Grassmann fields;
- Montvay–Münster Ch. 3; Smit §6 — meson-correlator transfer-matrix spectroscopy;
- Sharatchandra–Thun–Weisz, *Nucl. Phys.* **B192** (1981) 205, and Palumbo,
  *Phys. Rev. D* **66** (2002) 077503 — the **staggered 2-step** transfer matrix and the
  coherent-state Berezin slice reconstruction.

The gauge Hilbert space `H_gauge = L^2(G^links)`, the free-fermion Fock space with its
coherent-state Berezin slice resolution, reflection = adjoint, and the meson two-point's
particle-hole spectral representation are imported as cited methodology. The *existence* of
the transfer matrix is cited.

**Derived in-repo** — the load-bearing new finite-carrier content:

- the explicit dual computation that the **det-weighted finite-sample/quadrature**
  reflected Berezin correlator `<Theta(F_L) F_L>` of the OS-block representative
  `L_U(V)=W_b V W_a^dag` for the gauge-invariant, **number-conserving** Wilson-line
  meson operator `Fhat_V=c^dag V c` **equals** the
  operator transfer-matrix meson two-point (the particle-hole connected quark-line loop) on a
  finite 3+1 carrier, with the staggered `eta_1(t) = (-1)^t` 2-step bookkeeping under
  `theta(t, x_vec) = (-1 - t, x_vec)`, via a direct same-`M` four-field covariance minor
  and an independent Fock transfer-kernel loop, with that same `det(M[U])` **actually
  applied** to the `U`-average;
- the **correct handling of the vacuum-annihilation obstruction**: `Ohat_meson|Omega> = 0`
  (verified exactly) yet `<Theta(F_L) F_L>` nonzero and equal to the connected quark-line loop;
- the five controls K1–K5 establishing the test is non-vacuous and the observable is a
  genuine gauge singlet (vacuum-annihilation handled; per-mode-factorized **breaks**;
  flat no-det differs from the det-weighted target; single-step indefiniteness control
  fires; gauge invariance verified).

The **continuum / OS-reconstruction (Wightman) limit and Euclidean rotational (Lorentz)
restoration are not addressed** (out of scope); the per-config fermion 2-step rung is a
separate unresolved row; the Wilson-boundary (H1) positivity is on a separate branch.

## Setup and statement

On the finite 2-step blocked transfer carrier for the staggered-only action surface

```text
    S = S_G[U] + bar(chi) (M_KS[U] + m I) chi ,        m > 0 ,
```

on a small **3+1** spatial lattice (a `2 x 2 x 1` spatial sheet, or the minimal
`2 x 1 x 1`), in temporal gauge (`U_0 = 1`, residual spatial links `U_i(x_vec)`), with
the temporal-link reflection `theta(t, x_vec) = (-1 - t, x_vec)` and staggered phases
`eta_0 = 1`, `eta_mu(n) = (-1)^{n_0 + ... + n_{mu-1}}`:

**Representation theorem, gauge-invariant meson sector (finite carrier).** For the basis
of gauge-invariant Wilson-line matrices `V(U)`, let
`F_L=bar(chi)_+ W_b(U)V(U)W_a(U)^dag chi_+` be the common 2-step block-field
representative of `Fhat_V=c^dag V c`. For this representative, the **det-weighted finite
Haar-sample/quadrature** reflected Berezin **meson two-point correlator** equals the
matching operator-side transfer-matrix meson two-point,

```text
   (1/Z_Q) sum_{U in Q} e^{-S_G[U]} det(M[U]) <Theta(F_L) F_L>^ferm_U
       = G_operator,Q(V,V) ,
   <Theta(F_L) F_L>^ferm connected  =  Tr[ V^dag G_f V G_f ]
                                =  sum_{j,k} |(Q^dag V Q)_{jk}|^2 (C_BLOCK e^{-2 E_j})(C_BLOCK e^{-2 E_k})  >= 0 ,
```

where `G_f = C_BLOCK · Q diag(e^{-2 E_j(U)}) Q^dag` is the forward 2-step block propagator
(`E_j(U) = asinh(sqrt(m^2 + lambda_j(U)^2))`, `lambda_j(U)` the anti-Hermitian spatial-hop
eigenvalues), `Hhat[U] = sum_{pq} (Q diag(E_j(U)) Q^dag)_{pq} c_p^dag c_q` is the
second-quantized one-body staggered Hamiltonian in the position-color basis, and
`V_{(x,a),(y,c)} = U(x,y)_{ac}` is the meson one-body matrix (a genuine color singlet).
Although `Ohat_meson|Omega> = 0`, the connected meson two-point is the manifestly-positive
Gram `|| G_f^{1/2} V G_f^{1/2} ||_F^2` = the particle-hole connected quark-line loop. The
runner verifies this on explicit carriers (`Lt = 2*14 = 28` slices for the single matrix
supplying both determinant and minor; `N_c = 1` on the `2 x 2 x 1` sheet and the minimal
`2 x 1 x 1`, and `N_c = 3` on both the `2 x 2 x 1` sheet and the `2 x 1 x 1` carrier;
`m = 0.5`), per configuration and on the det-weighted finite-sample/quadrature average,
to `~1e-12`.

This meson equality is the gauge-invariant, number-conserving instance of the
Lüscher/Osterwalder–Seiler transfer-matrix meson-spectroscopy **representation** theorem
(cited); the in-repo derived content is the explicit finite-carrier **dual computation**
with the number-conserving meson observable, the correct vacuum-annihilation handling, the
det-weighted `U`-average, and the staggered 2-step `eta_1` bookkeeping — together with the
five non-vacuity controls.

## Why two steps, and why the single-step version breaks the equality

Under `theta(t, x_vec) = (-1 - t, x_vec)` the staggered phase flips,
`eta_1(theta t) = -eta_1(t)`. This is precisely where the single-step construction fails.
The runner handles it explicitly:

- **Single-step (negative control K4).** The naive single-slice reflection (the
  Sharatchandra map without the staggered-phase compensator) yields a reflected
  positive-cone metric that is **indefinite** (per-mode min eigenvalue `< 0`; the
  documented `-0.80` Caracciolo–Palumbo obstruction for the full naive Lagrangian Gram).
  An indefinite metric cannot equal the positive operator sandwich used by this runner,
  so the single-step equality is violated in the tested construction.
- **Two-step (the fix).** The 2-step blocking restores `Theta`-covariance. On the block
  the Osterwalder–Seiler fermion reflection carries the `gamma_0`-type sign
  `Theta(chi) = - bar(chi)_{theta}` (the convention fixed by reflection = adjoint, not a
  free parameter). The reflected block metric is then positive-semidefinite, with one
  physical positive eigenvalue per spatial mode equal to `C_BLOCK · e^{-2 E_j}`,
  `C_BLOCK = 2` (two Grassmann pairs per 2-step block; a mode-independent normalization,
  verified numerically against `e^{-2 E_j}` three independent ways).

## Honest status

Source-surface bounded theorem. The new load-bearing content is the explicit **dual
computation** in the **gauge-invariant, number-conserving meson** sector — the det-weighted
finite-sample/quadrature reflected Berezin meson two-point correlator versus the matching
operator transfer-matrix meson two-point (the free connected quark-line loop
`Tr[V^dag G_f V G_f]`), computed by separate code paths and asserted equal (worst
`5.14e-12`, gate `1e-9`) on finite 3+1 carriers. The Berezin path evaluates the connected
part of the explicit `2 x 2` Wick minor after lifting `V` with two temporal isometries
extracted from the full inverse; it does not call the reduced trace. The same full
`M[U]` supplies the determinant weight. The load-bearing independent content includes
the sign, normalization, spectrum, and eigenvector-intertwining checks that identify both
cross kernels with `G_f^operator`, followed by the direct four-field minor comparison —
together with the correct vacuum-annihilation handling and the five controls
(vacuum-annihilation handled; per-mode-factorized **breaks**; flat no-det differs from
the det-weighted target; single-step indefiniteness control fires; gauge invariance
verified). The general form of the equality is the
cited Lüscher/Osterwalder–Seiler/STW/Palumbo transfer-matrix meson-spectroscopy
representation theorem; this note verifies its gauge-invariant, number-conserving instance
on explicit finite carriers, including a genuine multi-spatial-dimensional SU(3) carrier
(`2 x 2 x 1` at N_c = 3). The runner verifies the equality on a finite carrier — it does
**not** verify the continuum / OS-reconstruction (Wightman) limit, Euclidean rotational
restoration, the Wilson-boundary (H1) positivity, or any interacting-RP closure, and it
does not close the per-config fermion 2-step rung. This note does not set or predict
downstream effective status.

What this can support after independent review:

- the interacting reflection-positivity program can cite this note for the finite-carrier
  **gauge-invariant, number-conserving meson** representation equality (det-weighted,
  connected same-matrix four-field Wick minor,
  finite-sample/quadrature averaged, vacuum-annihilation handled) in the 2-step blocked
  staggered transfer matrix, as one ingredient of the
  conditional bridge — with the continuum reconstruction, the Wilson-boundary (H1)
  positivity, and the per-config fermion 2-step rung all still open or contextual;
- downstream consumers needing the gauge-invariant meson operator/path-integral
  identification at fixed lattice spacing for the 2-step blocked staggered-KS theory can
  cite this equality.

What this does not support:

- single-step Lagrangian RP closure; K4 only records tested single-step indefiniteness;
- the continuum-limit / OS-reconstruction (Wightman) RP, or Euclidean rotational (Lorentz)
  restoration (out of scope; no claim either way);
- the compact-group Wilson-boundary positivity (H1; separate branch);
- any full interacting staggered + Wilson-fermion RP closure;
- closure of the per-config fermion 2-step rung (separate unresolved row);
- a literal `H_gauge ⊗ H_ferm` quantum operator-sandwich (the verified object is the
  classically-`U`-averaged fermion-Fock meson two-point).

## Dependencies (load-bearing markdown-link edges)

This note's verified result **consumes** the positive determinant weight: the det-weighted
`U`-average uses `det(M[U]) > 0` config-by-config, and replacing that measure by a flat
`U`-average changes the target value (control K3). The determinant positivity is therefore
a **genuinely load-bearing** upstream dependency here.

- [`STAGGERED_ONLY_DET_POSITIVITY_CASE_A_NOTE_2026-05-17.md`](STAGGERED_ONLY_DET_POSITIVITY_CASE_A_NOTE_2026-05-17.md)
  — the upstream positive determinant-weight statement
  `det(M_KS + m I) >= m^n > 0` config-by-config. It is the gauge-measure weight that this
  note's det-weighted `U`-average **actually applies**, so it is a load-bearing dependency.

## Validation

Primary runner:
[`scripts/meson_gauge_invariant_os_transfer_representation_2026-05-30.py`](../scripts/meson_gauge_invariant_os_transfer_representation_2026-05-30.py)
verifies, with `numpy` linear algebra on finite 3+1 carriers (single-seed deterministic):

- **P_block:** the forward block propagator's positive eigenvalue equals `C_BLOCK · e^{-2E}`
  per mode with `C_BLOCK = 2` a priori (worst `~1e-12`), confirmed three independent ways —
  per-mode temporal-chain block metric (`M^{-1}`), operator Fock `e^{-2 Hhat}`, and the
  full-spacetime `M[U]^{-1}` block-metric spectrum;
- **P_same-M:** one `Lt=28` matrix supplies `slogdet(M)` and the raw inverse used in the
  four-field minor; its particle/hole cross blocks are Hermitian, mode-block-diagonal,
  have normalization `2 exp(-2E)`, and intertwine with the operator kernel through two
  orthonormal temporal isometries. The explicit permutation Wick sum agrees with the
  `2 x 2` covariance determinant to `1.7e-16`, and the wrong one-field reflection sign
  makes the physical cross-kernel spectra negative;
- **K1 — vacuum-annihilation handled:** `||Ohat_meson|Omega>|| = 0` exactly (genuine
  Jordan-Wigner occupation action) **and** the meson two-point `<Theta(F_L) F_L>` is nonzero
  (min over basis `0.06`–`0.87`) and equals the operator connected quark-line loop;
- **P1 — per-config genuine meson dual:** the connected part of the direct same-`M`
  four-field Wick minor == operator (Fock `e^{-2 Hhat}` block loop) for the
  gauge-invariant meson basis, worst `5.14e-12`;
- **P0 — det-weighted finite-sample/quadrature dual (the headline):** the det-weighted
  finite `U`-average of the direct minor equals the operator meson two-point, with the
  same `Lt=28` determinant on both sides, worst `5.39e-14` (gate `1e-9`);
- **Ppos — OS positivity:** the averaged meson Gram is positive-semidefinite and the
  connected loop `>= 0` over random meson `V`;
- **Pdet:** the same-`M` determinant has positive phase over the whole `U`-quadrature
  (worst phase residual `3.5e-15`);
- **herm:** the averaged meson Gram is Hermitian to `~1e-17` (cited reflection = adjoint
  property);
- **K2 — per-mode-factorized Berezin BREAKS** the meson equality on the mixing carriers
  (gap `0.46` SU(3) 2×2×1, `0.27` U(1) 2×2×1); on the degenerate minimal carrier it
  consistently does not break (gap `~1.1e-16`, the prior-vacuity regime);
- **K3 — flat (no-det) `U`-average differs from the det-weighted target** (gap
  `0.13`–`0.34`);
- **K4 — single-step block-metric is indefinite** (min eig `< 0`);
- **K5 — gauge invariance:** the Wilson-line covariance `g_x U g_y^dag = U_g` to `~1e-16`
  and the meson two-point invariance under random gauge transforms to `~1e-15`.

Reproduction:

```bash
python3 scripts/meson_gauge_invariant_os_transfer_representation_2026-05-30.py
```

Expected scorecard: `SCORECARD PASS=116 FAIL=0`.
