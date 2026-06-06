# Gauge-Invariant, Number-Conserving Meson OS Transfer Representation Equality on a Finite 3+1 Staggered Carrier — Bounded Note

**Date:** 2026-05-30
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Review boundary:** source-surface bounded theorem proposal. This note records
runner-backed source content; downstream effective status is not set here.
**Primary runner:** [`scripts/meson_gauge_invariant_os_transfer_representation_2026-05-30.py`](../scripts/meson_gauge_invariant_os_transfer_representation_2026-05-30.py)
**Cached runner output:** [`logs/runner-cache/meson_gauge_invariant_os_transfer_representation_2026-05-30.txt`](../logs/runner-cache/meson_gauge_invariant_os_transfer_representation_2026-05-30.txt)
**Source packet verifier:** [`scripts/meson_os_transfer_source_packet_manifest_2026_06_06.py`](../scripts/meson_os_transfer_source_packet_manifest_2026_06_06.py)
(SUMMARY: MESON OS SOURCE PACKET PASS=30 FAIL=0)
**Source packet verifier cache:** [`logs/runner-cache/meson_os_transfer_source_packet_manifest_2026_06_06.txt`](../logs/runner-cache/meson_os_transfer_source_packet_manifest_2026_06_06.txt)
**Source packet verifier JSON:** [`outputs/meson_os_transfer_source_packet_manifest_2026_06_06.json`](../outputs/meson_os_transfer_source_packet_manifest_2026_06_06.json)
**Source role:** finite-carrier *representation* theorem for the **gauge-invariant,
number-conserving meson** observable of the 2-step blocked staggered transfer matrix.
On explicit finite **3+1** carriers it records the equality between the runner's
det-weighted finite Haar-sample/quadrature average of the time-reflected Berezin
**meson two-point correlator** `<Theta(F) F>` (a connected 4-fermion correlator) and
the matching operator-side transfer-matrix meson two-point (the particle-hole
connected quark-line loop). It **handles, rather than dodges, the vacuum-annihilation
obstruction** that the base note left open: `Ohat_meson|Omega> = 0`, yet
`<Theta(F) F>` is nonzero and equals the operator connected quark-line loop. This note
does **not** establish the continuum / OS-reconstruction (Wightman) limit, Euclidean
rotational (Lorentz) restoration, the compact-group Wilson-boundary positivity (H1),
or a full interacting-RP closure; and it does not close the per-config fermion 2-step
rung (a separate unresolved row).

## The deliverable (lead)

This note establishes, on explicit finite **3+1** carriers (3 spatial + 1 temporal;
the transfer matrix runs in the time direction, the spatial lattice is the regulator)
and the runner's finite Haar samples/quadratures, the **gauge-invariant,
number-conserving meson representation equality** for a basis of meson bilinears

```text
   F = chibar(x) U(x,y) chi(y)        (one creation chibar + one annihilation chi),
```

the gauge-invariant Wilson-line-transported staggered meson observable. The two sides
are computed by **separate kernel-build paths**:

```text
   <Theta(F) F>_Berezin,Q
       = (1/Z_Q) sum_{U in Q} w_U det(M[U]) <Theta(F) F>^ferm_U
       = G_operator,Q(F,F) ,
   Z_Q = sum_{U in Q} w_U det(M[U]),  w_U = exp(-S_G[U]).
```

Here `Q` is the runner's finite U(1) quadrature or fixed SU(3) Haar sample, not an
exact full Haar integral.

- **Berezin** — a genuine many-field Grassmann/Wick construction. At each fixed gauge
  background `U`, `<Theta(F) F>^ferm_U` is the connected four-field contraction of the
  time-reflected meson bilinear pair. The runner reconstructs the forward 2-step block
  propagator `G_f` from the Grassmann temporal-chain block metric per spatial-hop mode,
  rotates it to the position-color basis by the hop eigenbasis, and then evaluates the
  explicit four-index connected loop. A separate full-spacetime `M[U]^{-1}` block-metric
  spectrum check verifies the same block eigenvalues. The `U`-average is the det-weighted
  finite Haar-sample/quadrature average `(1/Z_Q) sum_{U in Q} e^{-S_G[U]} det(M[U]) (...)`
  with `det(M[U])` **actually applied**.
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
Berezin-side block kernel is built by Grassmann temporal-chain inversions and independently
checked against a full-spacetime `M[U]^{-1}` block-metric spectrum; the operator side
builds the same kernel from the fermion-Fock one-body transfer matrix `e^{-2 Hhat[U]}`.
The agreement is therefore **not tautological**.

The equality holds to a worst `|Berezin − operator|` of `5.1e-12` over the
gauge-invariant meson basis on the finite 3+1 carriers (well inside the `1e-9` assertion
gate). This is the **lattice / transfer-matrix** representation, exhibited on a finite
carrier and **illustrating** the cited general transfer-matrix meson-spectroscopy
construction; **no continuum claim is made either way**.

## 2026-06-06 Source Packet Exposure Repair

The current audit blocker asks for the complete primary runner source
or a source-hash-pinned runner artifact so the Berezin/operator kernel-build
functions and determinant-weighted averaging path can be audited. The source
packet verifier above checks that:

- the primary runner and cache are linked from this note;
- the primary runner is complete and contains the Berezin block-kernel,
  operator block-kernel, full-spacetime `M^{-1}` spectrum check,
  vacuum-annihilation control, four-fermion Berezin correlator,
  operator meson correlator, determinant-weighted average, and gauge-transform
  functions;
- the runner cache is SHA-fresh, successful, and contains the scorecard plus
  the P0/P1 and K1-K5 controls.

This does not set an audit verdict or widen the finite-carrier scope.

Current source-packet output:

```text
SUMMARY: MESON OS SOURCE PACKET PASS=30 FAIL=0
```

## Why the naive single-matrix-element vanishes, and how the obstruction is handled

The base note `MIXED_ENTANGLED_OS_TRANSFER_REPRESENTATION_BOUNDED_NOTE_2026-05-30.md`
on main scoped its mixed observable to a **single-creation** transported
bilinear `F = sum_b W_b(U) chibar_b` (`Ohat|Omega>` a one-particle state) and explicitly
left the number-conserving four-fermion `chibar(x) U(x,y) chi(y)` **open**, flagging that
it annihilates the OS vacuum (`chi(y)|Omega> = 0`), a genuine convention obstruction.

This note handles that obstruction rather than dodging it. The meson operator on Fock
space is the number-conserving one-body operator `Ohat_meson = sum_{ab} V_ab c_a^dag c_b`
(with `V_{(x,a),(y,c)} = U(x,y)_{ac}`). Then **`Ohat_meson|Omega> = 0`** (every
annihilation `c_b` kills the empty Fock vacuum) — the runner verifies this **exactly**
(`||F|Omega>|| = 0`, computed by genuine Jordan-Wigner occupation-number action, not
assumed). The naive single matrix element `<Omega| Ohat_meson^dag T Ohat_meson |Omega>`
is therefore trivially zero.

The **correct OS object is the meson two-point correlator** `<Theta(F) F>`, a connected
4-fermion correlator. By OS positivity
`<Theta(F) F>_connected = Tr[V^dag G_f V G_f] = sum_{j,k} |(Q^dag V Q)_{jk}|^2 (C_BLOCK e^{-2 E_j})(C_BLOCK e^{-2 E_k}) >= 0`
-- the free connected quark-antiquark one-loop, both legs forward-propagating after the
OS reflection sends the `chibar` leg to the image half. (It is **not** a vacuum sum
`sum_n |<n| Ohat_meson |0>|^2`, which vanishes since `Ohat_meson|0> = 0`.) The runner confirms
`<Theta(F) F>` is **nonzero** (minimum over the meson basis `0.06`–`0.87` depending on
carrier) and equals the operator connected quark-line loop `Tc = Tr[V^dag G_f V G_f]`. This
is the standard lattice meson spectroscopy via the transfer matrix (Lüscher 1977;
Osterwalder–Seiler 1978; Montvay–Münster Ch. 3; Smit §6).

The OS sign is load-bearing: with the staggered `gamma_0`-type reflection
`Theta(chi) = -bar(chi)` (the convention fixed by reflection = adjoint, not a free
parameter), the full meson correlator `<Theta(F) F>` is positive over the meson basis
**and** over random meson `V`; the opposite sign gives negative values. The runner
reports the averaged meson Gram as positive-semidefinite and the connected loop as
`>= 0` for any `V`.

## Scope (honest — what is delivered vs open)

- **Number-conserving meson observable — delivered (finite carrier).** The
  gauge-invariant, number-conserving meson bilinear `F = chibar(x) U(x,y) chi(y)` is the
  observable here. The vacuum-annihilation obstruction is handled (control **K1**):
  `Ohat_meson|Omega> = 0` exactly, yet the meson two-point `<Theta(F) F>` is nonzero and
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
  two-point `<Theta(F) F>` is nonetheless **NONZERO** (min over the meson basis `0.06`–`0.87`)
  and equals the operator particle-hole connected quark-line loop. Proves the obstruction is
  handled, not papered over.
- **K2 — per-mode-factorized Berezin BREAKS.** On a mode-mixing carrier (non-uniform
  links lifting the spatial-mode degeneracy), replacing the genuine (non-diagonal)
  forward block propagator `G_f` by its per-mode-diagonal restriction (the prior-vacuity
  object) **breaks** the meson equality: worst `|G_ber_permode − G_op|` is **large**
  (`0.73` for SU(3) 2×2×1, `0.22` for U(1) 2×2×1). On the *degenerate* minimal carrier the
  reconstructed propagator is diagonal and the per-mode object does **not** differ (gap
  `~5.3e-14`) — the explicit demonstration that the prior vacuity is the degenerate /
  mode-diagonal regime.
- **K3 — det-weight.** Replacing the theorem's det-weighted `U`-average by a flat
  `U`-average changes the target value (gap `0.04`–`0.06`). This proves the determinant
  weight is load-bearing for the stated measure; it is not a claim that the two code paths
  would disagree if both were intentionally evaluated with the same flat measure.
- **K4 — single-step.** The single-step (no 2-step blocking) reflected metric is
  **indefinite** (min eigenvalue `< 0`; the `-0.80` Caracciolo–Palumbo obstruction in this
  tested construction), so it cannot equal the positive operator sandwich used by this
  representation. This is a negative control for the runner, not a repo-wide
  impossibility theorem.
- **K5 — gauge invariance.** `F = chibar(x) U(x,y) chi(y)` is invariant under SU(3)/U(1)
  gauge transforms at the endpoints (a genuine color singlet): under
  `chi(y) -> g_y chi(y)`, `chibar(x) -> chibar(x) g_x^dag`,
  `U(x,y) -> g_x U(x,y) g_y^dag`, `F` is unchanged. The runner verifies (a) the
  Wilson-line covariance `g_x U(x,y) g_y^dag = U_g(x,y)` to `~1e-16`, and (b) the meson
  two-point `<Theta(F) F>` is invariant under random gauge transforms to `~1e-15`.

Positive results: the per-config Berezin = operator meson instance holds to `~1e-12`
(**P1**); the det-weighted finite-sample average to `~1e-12` (**P0**); the forward block
propagator's positive eigenvalue equals `C_BLOCK · e^{-2E}` with `C_BLOCK = 2` a priori
(**P_block**), confirmed three independent ways — the per-mode temporal-chain block metric
(Grassmann `M^{-1}`), the operator Fock `e^{-2 Hhat}`, **and** the full-spacetime `M[U]^{-1}`
block metric spectrum (a single `(Lt · N_s · N_c)`-dimensional matrix inverse, the most
independent Berezin build) — all agreeing to `~1e-12`; and `det(M[U]) > 0` over the whole
`U`-quadrature.

### Worst residuals (deterministic, single-seed; `SCORECARD PASS=64 FAIL=0`)

| Carrier (spatial × N_c) | Object | worst residual / value |
|---|---|---|
| SU(3) 2×2×1 (4 sites, 12 modes) | **det-weighted finite-sample avg** Berezin == operator meson (the headline; multi-dim SU(3)) | `6.2e-13` |
| SU(3) 2×2×1 | per-config Berezin (4-ferm) == operator meson | `2.6e-12` |
| SU(3) 2×2×1 | **K1** `\|\|F\|Omega>\|\|` (vacuum annihilation; must be `0`) / min `<Theta(F)F>` (must be `>0`) | `0.0` / `0.41` |
| SU(3) 2×2×1 | full-spacetime `M^{-1}` block spectrum vs operator `e^{-2E}` | `2.6e-12` |
| SU(3) 2×2×1 | **K2** per-mode gap / **K3** flat-vs-det gap / **K4** single-step min eig / **K5** gauge inv | `0.73` / `0.06` / `-0.55` / `1.0e-15` |
| SU(3) 2×1×1 (2 sites, 6 modes) | det-weighted finite-sample avg Berezin == operator meson | `2.4e-12` |
| SU(3) 2×1×1 | per-config Berezin (4-ferm) == operator meson | `5.1e-12` |
| U(1) 2×2×1 (4 sites, 4 modes) | det-weighted finite-sample avg Berezin == operator meson | `2.8e-14` |
| U(1) 2×2×1 | **K1** min `<Theta(F)F>` (nonzero) / **K2** per-mode gap (mixing) | `0.06` / `0.22` |
| U(1) 2×1×1 (minimal; DEGENERATE) | det-weighted avg Berezin == operator meson | `5.3e-14` |
| U(1) 2×1×1 (minimal) | **K2** per-mode gap (degenerate ⇒ no mixing ⇒ no break) | `5.3e-14` |

The worst `|Berezin − operator|` over the gauge-invariant meson basis is `5.1e-12`
(SU(3) 2×1×1 per-config). The exact worst residuals and control gaps are printed by the
runner.

**On the minimal degenerate carrier.** The U(1) 2×1×1 (2-site, 1-color) carrier has
*degenerate* spatial modes, so the reconstructed forward block propagator collapses to a
multiple of the identity (off-diagonal `0`) — exactly the prior-note vacuity regime. There
the per-mode-factorized object does **not** differ from the genuine one (K2 gap `~5.3e-14`):
this is reported as the explicit demonstration that the prior vacuity is precisely the
*degenerate / mode-diagonal* regime. The decisive K2 break is carried by the **mixing**
carriers — U(1) 2×2×1 and the SU(3) carriers — where the non-uniform links lift the
degeneracy and the reconstructed propagator is genuinely non-diagonal.

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
  reflected Berezin **meson two-point correlator** `<Theta(F) F>` of the gauge-invariant,
  **number-conserving** meson bilinear `F = chibar(x) U(x,y) chi(y)` **equals** the
  operator transfer-matrix meson two-point (the particle-hole connected quark-line loop) on a
  finite 3+1 carrier, with the staggered `eta_1(t) = (-1)^t` 2-step bookkeeping under
  `theta(t, x_vec) = (-1 - t, x_vec)`, via separate Berezin block-kernel and Fock
  transfer-kernel builds feeding the same connected loop, with `det(M[U])` **actually
  applied** to the `U`-average;
- the **correct handling of the vacuum-annihilation obstruction**: `Ohat_meson|Omega> = 0`
  (verified exactly) yet `<Theta(F) F>` nonzero and equal to the connected quark-line loop;
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
of gauge-invariant, number-conserving meson bilinears `F = chibar(x) U(x,y) chi(y)`
(Wilson-line transported staggered mesons) on the 2-step block, the **det-weighted finite
Haar-sample/quadrature** reflected Berezin **meson two-point correlator** equals the
matching operator-side transfer-matrix meson two-point,

```text
   (1/Z_Q) sum_{U in Q} e^{-S_G[U]} det(M[U]) <Theta(F) F>^ferm_U
       = G_operator,Q(F,F) ,
   <Theta(F) F>^ferm connected  =  Tr[ V^dag G_f V G_f ]
                                =  sum_{j,k} |(Q^dag V Q)_{jk}|^2 (C_BLOCK e^{-2 E_j})(C_BLOCK e^{-2 E_k})  >= 0 ,
```

where `G_f = C_BLOCK · Q diag(e^{-2 E_j(U)}) Q^dag` is the forward 2-step block propagator
(`E_j(U) = asinh(sqrt(m^2 + lambda_j(U)^2))`, `lambda_j(U)` the anti-Hermitian spatial-hop
eigenvalues), `Hhat[U] = sum_{pq} (Q diag(E_j(U)) Q^dag)_{pq} c_p^dag c_q` is the
second-quantized one-body staggered Hamiltonian in the position-color basis, and
`V_{(x,a),(y,c)} = U(x,y)_{ac}` is the meson one-body matrix (a genuine color singlet).
Although `Ohat_meson|Omega> = 0`, the connected meson two-point is the manifestly-positive
Gram `|| G_f^{1/2} V G_f^{1/2} ||_F^2` = the particle-hole connected quark-line loop. The
runner verifies this on explicit carriers (`Lt = 2*14` bulk slices for the block-metric
decay; `N_c = 1` on the `2 x 2 x 1` sheet and the minimal `2 x 1 x 1`, and `N_c = 3` on
both the `2 x 2 x 1` sheet and the `2 x 1 x 1` carrier; `m = 0.5`), per configuration and
on the det-weighted finite-sample/quadrature average, to `~1e-12`.

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
`Tr[V^dag G_f V G_f]`), computed by separate code paths and asserted equal (worst `5.1e-12`,
gate `1e-9`) on finite 3+1 carriers. For the meson observable the two paths feed the
identical connected contraction `Tr[V^dag G_f V G_f]`; the load-bearing **independent**
content is the forward block-propagator identity `G_f^Berezin == G_f^operator`, verified
three independent ways (per-mode temporal-chain `M^{-1}`, Fock `e^{-2 Hhat}`, and a
full-spacetime `M[U]^{-1}` block-metric spectrum), from which the meson equality follows — together with the correct vacuum-annihilation handling and the five controls
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
  connected four-field contraction through the runner's Berezin block kernel,
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

## Citation-graph note

The following are context / sibling rows whose construction this note restates
self-contained, not upstream load-bearing premises; following the existing RP notes'
citation-graph convention they are written as plain-text backtick filenames so the
citation-graph builder does not parse them as upstream dependency edges:

- `MIXED_ENTANGLED_OS_TRANSFER_REPRESENTATION_BOUNDED_NOTE_2026-05-30.md` — the on-main
  base note that established the det-weighted Berezin = operator equality for a
  Wilson-line-transported **single-creation** bilinear, and explicitly left the
  **number-conserving** four-fermion `chibar U chi` observable (and genuine
  multi-spatial-dimensional SU(3)) **open**; this note addresses both finite-carrier steps
  for the meson observable, handling the vacuum-annihilation obstruction.
- `MIXED_OS_TRANSFER_REPRESENTATION_BOUNDED_NOTE_2026-05-30.md` — the prior fermion-sector
  note on main.
- `RP_MIXED_OBSERVABLE_SINGLE_TRANSFER_MATRIX_NARROW_THEOREM_NOTE_2026-05-29.md` — the prior
  **assembly** lemma (`T_full = W^dag W` once posited).
- `AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md` — the 2-step blocked
  free-case construction this note's representation equality reuses.
- `RP_P2_GAUGE_EXTENSION_AND_REALIZATION_RESIDUAL_NOTE_2026-05-28.md` — the fixed-background
  per-configuration positivity (anti-Hermitian-hop modal reduction) reused here for the
  per-config fermion sector.
- The Wilson temporal-gauge transfer-kernel positivity (H1) is developed on the separate
  not-yet-merged branch `claude/wilson-su3-gauge-transfer-kernel-positivity-2026-05-30`; it
  is named here in plain text only and is context, not an on-main dependency edge.
- `MINIMAL_AXIOMS_2026-06-04.md` — Lattice + Quantum + Record baseline surface, named as
  setup context only.

## Validation

Primary runner:
[`scripts/meson_gauge_invariant_os_transfer_representation_2026-05-30.py`](../scripts/meson_gauge_invariant_os_transfer_representation_2026-05-30.py)
verifies, with `numpy` linear algebra on finite 3+1 carriers (single-seed deterministic):

- **P_block:** the forward block propagator's positive eigenvalue equals `C_BLOCK · e^{-2E}`
  per mode with `C_BLOCK = 2` a priori (worst `~1e-12`), confirmed three independent ways —
  per-mode temporal-chain block metric (`M^{-1}`), operator Fock `e^{-2 Hhat}`, and the
  full-spacetime `M[U]^{-1}` block-metric spectrum;
- **K1 — vacuum-annihilation handled:** `||Ohat_meson|Omega>|| = 0` exactly (genuine
  Jordan-Wigner occupation action) **and** the meson two-point `<Theta(F) F>` is nonzero
  (min over basis `0.06`–`0.87`) and equals the operator connected quark-line loop;
- **P1 — per-config genuine meson dual:** Berezin connected four-field loop through the
  Grassmann block kernel == operator (Fock `e^{-2 Hhat}` block loop) for the
  gauge-invariant meson basis, worst `~1e-12`;
- **P0 — det-weighted finite-sample/quadrature dual (the headline):** the det-weighted
  finite `U`-average of the reflected meson two-point equals the operator meson two-point,
  worst `6.2e-13` (gate `1e-9`);
- **Ppos — OS positivity:** the averaged meson Gram is positive-semidefinite and the
  connected loop `>= 0` over random meson `V`;
- **Pdet:** `det(M[U]) > 0` over the whole `U`-quadrature;
- **herm:** the averaged meson Gram is Hermitian to `~1e-17` (cited reflection = adjoint
  property);
- **K2 — per-mode-factorized Berezin BREAKS** the meson equality on the mixing carriers
  (gap `0.73` SU(3) 2×2×1, `0.22` U(1) 2×2×1); on the degenerate minimal carrier it
  consistently does not break (gap `~5.3e-14`, the prior-vacuity regime);
- **K3 — flat (no-det) `U`-average differs from the det-weighted target** (gap
  `0.04`–`0.06`);
- **K4 — single-step block-metric is indefinite** (min eig `< 0`);
- **K5 — gauge invariance:** the Wilson-line covariance `g_x U g_y^dag = U_g` to `~1e-16`
  and the meson two-point invariance under random gauge transforms to `~1e-15`.

Reproduction:

```bash
python3 scripts/meson_gauge_invariant_os_transfer_representation_2026-05-30.py
```

Expected scorecard: `SCORECARD PASS=64 FAIL=0`.

## 2026-06-06 Source Packet Re-audit Repair

This repair responds to the artifact-completeness blocker asking for the
complete primary runner source, or a source-hash-pinned runner artifact. It
does not promote this row or change the bounded source-surface claim boundary;
independent audit owns any ledger/status movement.

The restricted packet now exposes:

- [`scripts/meson_gauge_invariant_os_transfer_representation_2026-05-30.py`](../scripts/meson_gauge_invariant_os_transfer_representation_2026-05-30.py)
- [`logs/runner-cache/meson_gauge_invariant_os_transfer_representation_2026-05-30.txt`](../logs/runner-cache/meson_gauge_invariant_os_transfer_representation_2026-05-30.txt)
- [`scripts/meson_gauge_invariant_os_transfer_source_packet_manifest_2026_06_06.py`](../scripts/meson_gauge_invariant_os_transfer_source_packet_manifest_2026_06_06.py)
- [`logs/runner-cache/meson_gauge_invariant_os_transfer_source_packet_manifest_2026_06_06.txt`](../logs/runner-cache/meson_gauge_invariant_os_transfer_source_packet_manifest_2026_06_06.txt)
- [`outputs/meson_gauge_invariant_os_transfer_source_packet_manifest_2026_06_06.json`](../outputs/meson_gauge_invariant_os_transfer_source_packet_manifest_2026_06_06.json)

The manifest checks that the note names the primary runner/cache, that the
source is complete and contains the load-bearing functions
`block_metric_per_mode`, `block_fwd_propagator_berezin`,
`block_metric_spacetime_eigs`, `meson_correlator_full_berezin`, and
`u_averaged_meson`, and that the cache header is SHA-fresh against the current
runner source. It also checks the cached scorecard snippets for `P_block`, `P1`,
`P0`, `K2`, `K5`, and `SCORECARD PASS=64 FAIL=0`.
