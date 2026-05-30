# Gauge-Fermion-Entangled OS Transfer Representation Equality on a Finite 3+1 Staggered Carrier — Bounded Note

**Date:** 2026-05-30
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Primary runner:** [`scripts/mixed_entangled_os_transfer_representation_2026-05-30.py`](../scripts/mixed_entangled_os_transfer_representation_2026-05-30.py)
**Cached runner output:** [`logs/runner-cache/mixed_entangled_os_transfer_representation_2026-05-30.txt`](../logs/runner-cache/mixed_entangled_os_transfer_representation_2026-05-30.txt)
**Source role:** finite-carrier *representation* theorem for the tested
**gauge-fermion-entangled (mixed-observable)** single-creation sector of the
2-step blocked staggered transfer matrix. On explicit finite **3+1** carriers
it records the equality between the runner's det-weighted finite
Haar-sample/quadrature average of the time-reflected Berezin correlator of a
**genuinely-mixed** (gauge × fermion) observable and the matching
classically-U-averaged fermion-Fock Gram. The finite tensor-product
`T_full` construction is checked separately by the operator-Schmidt-rank
diagnostic. This note does **not** establish the continuum / OS-reconstruction
(Wightman) limit, Euclidean rotational (Lorentz) restoration, the compact-group
Wilson-boundary positivity (H1), or a full interacting-RP closure; and it does
not close the per-config fermion 2-step rung (a separate unresolved row).

## The deliverable (lead)

This note establishes, on explicit finite **3+1** carriers (3 spatial + 1 temporal;
the transfer matrix runs in the time direction, the spatial lattice is the
regulator) and the runner's finite Haar samples/quadratures, the
**gauge-fermion-entangled representation equality** for a basis of
**genuinely-mixed** observables `F` that entangle gauge and fermion degrees of
freedom and do **not** factor into (gauge) × (fermion):

```text
   <Theta(F) F>_Berezin,Q
       = (1/Z_Q) sum_{U in Q} w_U det(M[U]) <Theta(F) F>^ferm_U
       = G_operator,Q(F,F) ,
   Z_Q = sum_{U in Q} w_U det(M[U]),  w_U = exp(-S_G[U]).
```

Here `Q` is the runner's finite U(1) quadrature or fixed SU(3) Haar sample,
not an exact full Haar integral.

The mixed observable is a **gauge-covariant Wilson-line-transported staggered
fermion creation**,

```text
   F = sum_b W_b(U) chibar_b ,
```

where the transport amplitude `W_b(U)` is a Wilson line built from the spatial
gauge links, so `F` is a sum of gauge × fermion terms sharing color/site indices
and does **not** factor. The two sides are computed by **completely separate code
paths**:

- **Berezin** — a genuine many-field Grassmann integral. At each fixed gauge
  background `U`, `<Theta(F) F>^ferm_U` is computed by Wick contraction with the
  staggered propagator `M[U]^{-1}` (the 2-step block metric, **every Grassmann
  cross-contraction**, rotated to the position-color basis — **not** a per-mode
  product). The `U`-average is the det-weighted finite Haar-sample/quadrature
  average `(1/Z_Q) sum_{U in Q} e^{-S_G[U]} det(M[U]) (...)` with `det(M[U])`
  **actually applied**.
- **Operator-side P0** — the classically-U-averaged fermion-Fock Gram
  `G_operator,Q(F,F)` built per configuration from
  `<Ω| c_b e^{-2 Hhat[U]} c_{b'}^† |Ω>` in the **position-color basis** (the gauge
  links genuinely couple the fermion modes; `Hhat[U]` is **not** mode-diagonal once
  the links are non-uniform). The finite `H_gauge ⊗ H_ferm` tensor-product
  `T_full` is exhibited separately by the C4 operator-Schmidt-rank diagnostic.

The two paths share **only the lattice action** (the spatial-hop spectrum
`{lambda_j(U), E_j(U)}` and the hop-eigenbasis `Q`, which are properties of `S[U]`,
not of either Hilbert-space construction) — the same independence boundary the prior
fermion-sector note used. The agreement is therefore **not tautological**: the
per-configuration magnitude `c_block · e^{-2E_j}` is obtained on the Berezin side by
Grassmann/Wick contraction over the temporal chain with `M[U]^{-1}` and on the
operator side by Fock second-quantization of `e^{-2 Hhat[U]}` (verified: the operator
code path references neither the block metric nor the Berezin Gram). The runner
confirms both sides reproduce the **same off-diagonal** position-color entanglement
structure to `~1e-16` per configuration.

The equality holds to a worst `|Berezin − operator|` of `7.2e-13` over the
genuinely-mixed basis on the finite 3+1 carriers (well inside the `1e-9` assertion
gate). This is the **lattice / transfer-matrix** representation, exhibited on a
finite carrier and **illustrating** the cited general transfer-matrix construction;
**no continuum claim is made either way**.

## Scope (honest — three explicit limitations)

- **Operator side is the classically-U-averaged fermion-Fock Gram, not a quantum
  `H_gauge ⊗ H_ferm` sandwich.** On a finite lattice the gauge field is a c-number
  integration variable, so the verified equality (checks P0/P1) is between the
  Berezin path and the **per-configuration fermion-Fock vacuum correlator**
  `<Ω| c_b e^{-2 Hhat[U]} c_{b'}^† |Ω>`, **identically classically U-averaged** on
  both sides with the weight `e^{-S_G[U]} det(M[U])` and the Wilson amplitudes
  `W_b(U)`. The genuine tensor-product `T_full` on `H_gauge ⊗ H_ferm` (with `What_b`
  a quantum multiplication operator) is exhibited **separately** as the
  operator-Schmidt-rank diagnostic (C4, rank 6); it is **not** the object the P0
  equality numerically evaluates, and no literal `H_gauge ⊗ H_ferm`
  operator-sandwich claim is made.
- **SU(3) color-mixing is 1-spatial-dimensional only.** Genuine SU(3) color-mixing
  is exhibited **only on the 1-spatial-dimensional `2×1×1` carrier** (6 modes,
  rank 3). The multi-spatial-dimensional `2×2×1` sheet runs at **N_c=1 (U(1),
  abelian)** for Fock-tractability. **No full multi-dimensional SU(3) entangled
  result is claimed.**
- **Single-creation observable, not the four-fermion bilinear.**
  `F = Σ_b W_b(U) χ̄_b` is a Wilson-line-transported **single-creation** staggered
  bilinear (`Ô|Ω>` is a one-particle state, `<N>=1`). It is **not** the
  number-conserving four-fermion `χ̄(x) U(x,y) χ(y)`, which annihilates the OS
  vacuum (a genuine convention obstruction, diagnosed not papered over). The
  "mixed gauge-fermion-entangled observable" claim is scoped to the single-creation
  transported bilinear.

## Why this is NOT the per-mode restatement that sank the prior headline

The prior note `MIXED_OS_TRANSFER_REPRESENTATION_BOUNDED_NOTE_2026-05-30.md`
(on-main, unaudited) honestly delivered only the **fermion-sector** equality.
Its "mixed" check was **vacuous** for two structural reasons, both removed here:

1. **Shared wrapper / per-mode-factorized Berezin.** There the operator Gram and
   the Berezin Gram shared an identical gauge half and Fock wrapper and differed
   **only** in a per-mode-FACTORIZED fermion block
   `Tber = (x)_j diag(1, cov_j)` vs `Top`; so `G_ber - G_op` was a pure function of
   the per-block scalar `Tber - Top`, the entanglement structure cancelled
   identically, and forcing `Tber := Top` gave residual `0` while the
   operator-Schmidt rank stayed `6`. The "equality" reduced to a per-mode scalar.
2. **`det(M[U])` was computed but never used** in the `U`-average (a flat
   reference).

Here, **both defects are removed and the test has teeth**:

- The mixed observable `F = sum_b W_b(U) chibar_b` makes the reconstructed
  position-color Gram per configuration genuinely **non-diagonal** — because the
  spatial links are **non-uniform** (distinct group elements on distinct bonds),
  the gauge configuration mixes the fermion modes (the runner reports an
  off-diagonal magnitude of the reconstructed Gram of order `0.1`–`0.2`). Replacing
  the genuine Gram `G_recon[U] = c_block <b| e^{-2 Hhat_1[U]} |b'>` by its
  **per-mode-diagonal restriction** (the prior vacuity object) therefore **BREAKS**
  the equality for the mixed observables (a **large** nonzero residual gap — see
  the worst-residuals table). This is decisive: the test discriminates against
  exactly the prior per-mode object. (With *uniform* links the two spatial modes
  would be degenerate and `G_recon` would collapse to a multiple of the identity,
  recreating the prior vacuity — which is precisely why this construction uses
  non-uniform links.)
- The `U`-average is the finite-sample/quadrature
  `(1/Z_Q) sum_{U in Q} e^{-S_G[U]} det(M[U]) (...)`, and
  **dropping `det(M[U])` (a flat average) BREAKS** the equality (a **large** gap).
  The determinant weight is load-bearing — the prior B2 defect is addressed.

So the entanglement, the determinant weight, and the 2-step `eta_1` bookkeeping are
all **load-bearing** here, not diagnostics of a shared wrapper.

## Mandatory non-vacuity controls (each fires)

The runner reports, for every carrier:

- **C1 — entanglement-detection (decisive).** On a carrier with genuine mode-mixing
  (non-uniform links lifting the spatial-mode degeneracy), replacing the Berezin
  side with the per-mode-FACTORIZED object (the prior note's per-mode `Tber`)
  **breaks** the equality for the genuinely-mixed `F`: worst `|G_ber_permode - G_op|`
  is **large** (`0.228` for U(1) 2×2×1, `0.190` for SU(3) 2×1×1). Proves the test
  discriminates against the prior vacuity. On the *degenerate* minimal carrier the
  reconstructed Gram is diagonal and the per-mode object does **not** differ (gap
  `~3.6e-14`) — the explicit demonstration that the prior vacuity is the
  degenerate / mode-diagonal regime.
- **C2 — det-weight.** Dropping the `det(M[U])` weight (flat `U`-average) **breaks**
  the equality (large gap). Proves the determinant weight is load-bearing.
- **C3 — single-step.** The single-step (no 2-step blocking) reflected metric is
  **indefinite** (min eigenvalue `< 0`; the `-0.80` Caracciolo–Palumbo no-go), so
  it cannot equal any positive operator sandwich. Proves `Theta`-covariance needs
  the 2-step block.
- **C4 — operator-Schmidt rank `> 1`.** The 2-step transfer `T_full` on
  `H_gauge (x) H_ferm` has operator-Schmidt rank `> 1` (genuine gauge-fermion
  entanglement present), **and** the equality holds for the entangled observables.

Positive results: the per-config Berezin = operator instance holds to `~1e-12`; the
block-metric positive eigenvalue equals `c_block · e^{-2E}` with `c_block = 2` a
priori; and `det(M[U]) > 0` over the whole `U`-quadrature (consistent with the
upstream Case-A determinant-positivity note, now a **genuinely load-bearing**
ingredient because `det(M[U])` actually weights the average).

### Worst residuals (deterministic, single-seed; `SCORECARD PASS=27 FAIL=0`)

| Carrier (spatial × N_c) | Object | worst residual / value |
|---|---|---|
| U(1) 2×2×1 (4 sites) | per-config Berezin == operator (genuinely-mixed basis) | `2.4e-13` |
| U(1) 2×2×1 | **det-weighted finite-sample avg** Berezin == operator (the headline) | `2.2e-14` |
| U(1) 2×2×1 | recon-Gram off-diagonal (mode-mixing present) | `0.21` |
| U(1) 2×2×1 | **C1** per-mode-factorized Berezin gap (must be LARGE) | `0.228` |
| U(1) 2×2×1 | **C2** flat (no-det) `U`-average gap (must be LARGE) | `0.100` |
| U(1) 2×2×1 | **C3** single-step block-metric min eig (must be `<0`) | `-0.456` |
| U(1) 2×2×1 | **C4** operator-Schmidt rank of `T_full` (must be `>1`) | `6` |
| SU(3) 2×1×1 (2 sites, 6 modes) | det-weighted finite-sample avg Berezin == operator | `7.2e-13` |
| SU(3) 2×1×1 | recon-Gram off-diagonal (color-mode mixing present) | `0.18` |
| SU(3) 2×1×1 | **C1** per-mode-factorized gap / **C2** no-det gap / **C3** / **C4** | `0.190` / `0.055` / `-0.541` / `6` |
| U(1) 2×1×1 (minimal; DEGENERATE) | det-weighted finite-sample avg Berezin == operator | `3.6e-14` |
| U(1) 2×1×1 (minimal) | **C1** per-mode gap (degenerate ⇒ no mixing ⇒ no break) | `3.6e-14` |

The worst `|Berezin − operator|` over the genuinely-mixed basis is `7.2e-13`
(SU(3) det-weighted finite-sample average). The exact worst residuals and control gaps are
recorded in the cached runner output.

**On the minimal degenerate carrier.** The U(1) 2×1×1 (2-site, 1-color) carrier has
*degenerate* spatial modes, so the reconstructed Gram collapses to a multiple of the
identity (off-diagonal `0`) — exactly the prior-note vacuity regime. There the
per-mode-factorized object does **not** differ from the genuine one (C1 gap `~0`):
this is reported as the explicit demonstration that the prior vacuity is precisely
the *degenerate / mode-diagonal* regime. The decisive C1 break (and the genuine
gauge-fermion entanglement) is carried by the **mixing** carriers — U(1) 2×2×1 and
SU(3) 2×1×1 — where the non-uniform links lift the degeneracy and the reconstructed
Gram is genuinely non-diagonal.

## What is cited (standard methodology) vs derived (in-repo)

**Cited** — imported as standard lattice-gauge methodology, not reproven here:

- Lüscher, *Comm. Math. Phys.* **54** (1977) 283 — transfer-matrix construction,
  reflection = adjoint, Hilbert-space reconstruction from the Euclidean correlator;
- Osterwalder–Seiler, *Ann. Phys.* **110** (1978) 440 — gauge + fermion lattice OS
  positivity and the reflection on Grassmann fields;
- Sharatchandra–Thun–Weisz, *Nucl. Phys.* **B192** (1981) 205, and Palumbo,
  *Phys. Rev. D* **66** (2002) 077503 — the **staggered 2-step** transfer matrix and
  the coherent-state Berezin slice reconstruction;
- Montvay–Münster Ch. 3; Smit §6 — textbook treatments.

The gauge Hilbert space `H_gauge = L^2(G^links)`, the free-fermion Fock space with
its coherent-state Berezin slice resolution, and reflection = adjoint are imported
as cited methodology. The *existence* of the transfer matrix is cited.

**Derived in-repo** — the load-bearing new finite-carrier content:

- the explicit dual computation that the **det-weighted finite-sample/quadrature**
  reflected Berezin correlator of a **genuinely-mixed (gauge-fermion-entangled)**
  observable `F = sum_b W_b(U) chibar_b` **equals** the classically-U-averaged
  fermion-Fock operator Gram on a finite 3+1 carrier, with the staggered
  `eta_1(t) = (-1)^t` 2-step bookkeeping under `theta(t, x_vec) = (-1 - t, x_vec)`,
  via two completely separate code paths (Grassmann/Wick with `M[U]^{-1}` vs Fock
  operator algebra), with `det(M[U])` **actually applied** to the `U`-average;
- the four controls C1–C4 establishing the test is non-vacuous: the
  per-mode-factorized Berezin **breaks** the equality (C1), the flat no-det
  `U`-average **breaks** it (C2), the single-step **breaks** `Theta`-covariance
  (C3), and the operator-Schmidt rank is `> 1` with the equality holding for the
  entangled observables (C4).

The **continuum / OS-reconstruction (Wightman) limit and Euclidean rotational
(Lorentz) restoration are not addressed** (out of scope); the per-config fermion
2-step rung is a separate unresolved row; the Wilson-boundary (H1)
positivity is on a separate branch.

## Setup and statement

On the finite 2-step blocked transfer carrier for the staggered-only action surface

```text
    S = S_G[U] + bar(chi) (M_KS[U] + m I) chi ,        m > 0 ,
```

on a small **3+1** spatial lattice (e.g. a `2 x 2 x 1` spatial sheet, or the
minimal `2 x 1 x 1`), in temporal gauge (`U_0 = 1`, residual spatial links
`U_i(x_vec)`), with the temporal-link reflection `theta(t, x_vec) = (-1 - t, x_vec)`
and staggered phases `eta_0 = 1`, `eta_mu(n) = (-1)^{n_0 + ... + n_{mu-1}}`:

**Representation theorem, mixed (gauge-fermion-entangled) sector (finite carrier).**
For the basis of genuinely-mixed observables `F = sum_b W_b(U) chibar_b` (Wilson-line
transported staggered creations) on the 2-step block, the **det-weighted finite
Haar-sample/quadrature** reflected Berezin correlator equals the matching
classically-U-averaged fermion-Fock Gram,

```text
   (1/Z_Q) sum_{U in Q} e^{-S_G[U]} det(M[U]) <Theta(F) F>^ferm_U
       = G_operator,Q(F,F) ,
   T_full = ( T_gauge^{1/2} (x) I ) . ( oplus_U  e^{-2 Hhat[U]} ) . ( T_gauge^{1/2} (x) I ) ,
```

where `Hhat[U] = sum_{pq} (Q diag(E_j(U)) Q^dag)_{pq} c_p^dag c_q` is the
second-quantized one-body staggered Hamiltonian in the **position-color basis**
(`E_j(U) = asinh(sqrt(m^2 + lambda_j(U)^2))`, `lambda_j(U)` the anti-Hermitian
spatial-hop eigenvalues), `T_gauge` is the Wilson temporal-gauge transfer kernel,
and `Ohat = sum_b What_b (x) c_b^dag` is the genuinely-entangling mixed operator.
The runner verifies this on explicit carriers (`Lt = 2*14` bulk slices for the
block-metric decay; `N_c = 1` on the `2 x 2 x 1` spatial sheet and the minimal
`2 x 1 x 1`, and `N_c = 3` on the `2 x 1 x 1` spatial carrier — chosen so the
fermion Fock dimension `2^{n_modes}` stays tractable; `m = 0.5`), per configuration
and on the det-weighted finite-sample/quadrature average, to `~1e-12`.

This mixed equality is the gauge-fermion-entangled instance of the
Lüscher/Osterwalder–Seiler transfer-matrix **representation** theorem (cited); the
in-repo derived content is the explicit finite-carrier **dual computation** with the
genuinely-mixed observable, the det-weighted `U`-average, and the staggered 2-step
`eta_1` bookkeeping — together with the four non-vacuity controls.

## Why two steps, and why the single-step version breaks the equality

Under `theta(t, x_vec) = (-1 - t, x_vec)` the staggered phase flips,
`eta_1(theta t) = -eta_1(t)`. This is precisely where the single-step construction
fails. The runner handles it explicitly:

- **Single-step (negative control C3).** The naive single-slice reflection
  (the Sharatchandra map without the staggered-phase compensator) yields a
  reflected positive-cone metric that is **indefinite** (per-mode min eigenvalue
  `< 0`; the documented `-0.80` Caracciolo–Palumbo no-go for the full naive
  Lagrangian Gram). An indefinite metric cannot equal any positive operator
  sandwich, so the single-step equality is violated.
- **Two-step (the fix).** The 2-step blocking restores `Theta`-covariance. On the
  block the Osterwalder–Seiler fermion reflection carries the `gamma_0`-type sign
  `Theta(chi) = - bar(chi)_{theta}` (the convention fixed by reflection = adjoint,
  not a free parameter). The reflected block metric is then positive-semidefinite,
  with one physical positive eigenvalue per spatial mode equal to
  `c_block · e^{-2E_j}`, `c_block = 2` (two Grassmann pairs per 2-step block; a
  mode-independent normalization, verified numerically against `e^{-2E_j}`).

## Honest status

Source-surface bounded theorem. The new load-bearing content is the explicit
**dual computation** in the **gauge-fermion-entangled (mixed-observable)** sector —
the det-weighted finite-sample/quadrature reflected Berezin correlator of a
genuinely-mixed observable versus the matching classically-U-averaged
fermion-Fock Gram,
computed by separate code paths and asserted equal (worst `7.2e-13`, gate `1e-9`)
on finite 3+1 carriers — together with the four controls (per-mode-factorized **breaks**; flat
no-det **breaks**; single-step **breaks**; Schmidt rank `> 1` with equality
holding). The general form of the equality is the cited
Lüscher/Osterwalder–Seiler/STW/Palumbo transfer-matrix representation theorem; this
note verifies its gauge-fermion-entangled instance on explicit finite carriers. The
runner verifies the equality on a finite carrier — it does **not** verify the
continuum / OS-reconstruction (Wightman) limit, Euclidean rotational restoration,
the Wilson-boundary (H1) positivity, or any interacting-RP closure, and it does not
close the per-config fermion 2-step rung. This note does not set or predict an audit
outcome; independent audit is still required.

What this can support if audit passes:

- the interacting reflection-positivity program can cite this note for the
  finite-carrier **gauge-fermion-entangled** representation equality (det-weighted,
  full cross-contractions, finite-sample/quadrature averaged) in the 2-step blocked staggered transfer
  matrix, as one ingredient of the conditional bridge — with the continuum
  reconstruction, the Wilson-boundary (H1) positivity, and the per-config fermion
  2-step rung all still open or contextual;
- downstream consumers needing the mixed operator/path-integral identification at
  fixed lattice spacing for the 2-step blocked staggered-KS theory can cite this
  equality.

What this does not support:

- single-step Lagrangian RP (genuine no-go, reproduced as C3);
- the continuum-limit / OS-reconstruction (Wightman) RP, or Euclidean rotational
  (Lorentz) restoration (out of scope; no claim either way);
- the compact-group Wilson-boundary positivity (H1; separate branch);
- any full interacting staggered + Wilson-fermion RP closure;
- closure of the per-config fermion 2-step rung (separate unresolved row);
- a literal `H_gauge ⊗ H_ferm` quantum operator-sandwich (the verified P0 object is
  the classically-U-averaged fermion-Fock Gram; see **Scope** above);
- multi-spatial-dimensional SU(3) entanglement (SU(3) color-mixing is exhibited on
  the 1d `2×1×1` carrier only; the `2×2×1` sheet is N_c=1 abelian);
- the number-conserving four-fermion `χ̄ U χ` observable (which annihilates the OS
  vacuum; `F` here is a single-creation transported bilinear).

## Dependencies (load-bearing markdown-link edges)

This note's verified result **consumes** the positive determinant weight: the
det-weighted `U`-average uses `det(M[U]) > 0` config-by-config, and dropping it
breaks the equality (control C2). The determinant positivity is therefore a
**genuinely load-bearing** upstream dependency here (unlike the prior note, whose
fermion-sector check used a flat reference and did not consume it).

- [`STAGGERED_ONLY_DET_POSITIVITY_CASE_A_NOTE_2026-05-17.md`](STAGGERED_ONLY_DET_POSITIVITY_CASE_A_NOTE_2026-05-17.md)
  — the upstream positive determinant-weight statement
  `det(M_KS + m I) >= m^n > 0` config-by-config. It is the gauge-measure weight
  that this note's det-weighted `U`-average **actually applies**, so it is a
  load-bearing dependency.

## Citation-graph note

The following are context / sibling rows whose construction this note restates
self-contained, not upstream load-bearing premises; following the existing RP notes'
citation-graph convention they are written as plain-text backtick filenames so the
citation-graph builder does not parse them as upstream dependency edges:

- `MIXED_OS_TRANSFER_REPRESENTATION_BOUNDED_NOTE_2026-05-30.md` — the prior
  fermion-sector note (on-main, unaudited) that left the full
  gauge-fermion-entangled mixed-observable equality **open**; this note closes that
  finite-carrier step and removes its two vacuity defects (per-mode-factorized
  Berezin; unused `det(M[U])`).
- `RP_MIXED_OBSERVABLE_SINGLE_TRANSFER_MATRIX_NARROW_THEOREM_NOTE_2026-05-29.md` —
  the prior **assembly** lemma (`T_full = W^dag W` once posited); the home of the
  open full mixed-observable representation equality this note's finite-carrier
  result feeds into.
- `AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md` — the 2-step
  blocked free-case construction this note's representation equality reuses.
- `RP_P2_GAUGE_EXTENSION_AND_REALIZATION_RESIDUAL_NOTE_2026-05-28.md` — the
  fixed-background per-configuration positivity (anti-Hermitian-hop modal
  reduction) reused here for the per-config fermion sector.
- The Wilson temporal-gauge transfer-kernel positivity (H1) is developed on the
  separate not-yet-merged branch
  `claude/wilson-su3-gauge-transfer-kernel-positivity-2026-05-30`; it is named here
  in plain text only and is context, not an on-main dependency edge.
- `MINIMAL_AXIOMS_2026-05-20.md` — repo baseline surface, named as setup context
  only.

## Validation

Primary runner:
[`scripts/mixed_entangled_os_transfer_representation_2026-05-30.py`](../scripts/mixed_entangled_os_transfer_representation_2026-05-30.py)
verifies, with `numpy` linear algebra on finite 3+1 carriers (single-seed
deterministic):

- **P_block:** the block-metric positive eigenvalue equals `c_block · e^{-2E}` per
  mode with `c_block = 2` a priori (worst `~1e-16`);
- **P1 — per-config genuine mixed dual:** Berezin (`M[U]^{-1}` block-metric Wick,
  rotated to the position-color basis) == operator (Fock `e^{-2 Hhat[U]}` sandwich)
  for the genuinely-mixed basis, worst `~1e-12`;
- **P0 — det-weighted finite-sample/quadrature dual (the headline):** the det-weighted finite
  `U`-average of the reflected mixed Berezin correlator equals the operator
  Gram, worst `7.2e-13` (gate `1e-9`);
- **Pdet:** `det(M[U]) > 0` over the whole `U`-quadrature;
- **herm:** the averaged Gram is Hermitian to `~1e-9` (cited reflection = adjoint
  property);
- **C1 — per-mode-factorized Berezin BREAKS** the equality for mixed `F` on the
  mixing carriers (gap `0.228` U(1) 2×2×1, `0.190` SU(3) 2×1×1); on the degenerate
  minimal carrier it consistently does not break (gap `~3.6e-14`, the prior-vacuity
  regime);
- **C2 — flat (no-det) `U`-average BREAKS** the equality (large gap);
- **C3 — single-step block-metric is indefinite** (min eig `< 0`);
- **C4 — operator-Schmidt rank `> 1`** with the equality holding.

Reproduction:

```bash
python3 scripts/mixed_entangled_os_transfer_representation_2026-05-30.py
```

Expected scorecard: `SCORECARD PASS=27 FAIL=0`.
