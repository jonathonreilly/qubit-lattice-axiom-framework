# Bounded Action-Support Budgets and a Proved Finite-Range Lieb-Robinson Bridge for Microcausality

**Date:** 2026-05-09; repaired 2026-06-09 (J normalization), 2026-06-10
(proved LR lemma + honest velocity constant)
**Type:** bounded_theorem
**Claim scope:** Three unconditional legs plus one explicitly
conditional corollary.
(i) On the supplied/displayed staggered + Wilson-diagonal +
Wilson-plaquette action-density carrier surface (coefficient
normalizations declared in this note; carrier *names and structure*
taken from the parent RP note's staggered-only in-scope surface
`S = S_G[U] + χ̄ (M_KS[U] + m·I) χ` with compact SU(3) Wilson
plaquette links), the leading local action-density pieces have bounded
site support (`r_action <= 2` in the lattice `l1` metric), explicit
per-site budgets `J_max` (`|m| + 78` supplied surface / `|m| + 78.5`
displayed carrier / `|m| + 80` envelope at `d = 4, r_W = 1, β = 6,
N_c = 3`), and explicit per-site overlap weights
`W` (`|m| + 296` / `|m| + 298` / `|m| + 300` on the same branches).
(ii) A self-contained finite-range Lieb-Robinson lemma is **proved in
this note** (Steps 4-5): for any `H = Σ_Z h_Z` with support size
`<= q`, support diameter `<= R`, and per-site overlap weight `<= W`,
the exact series bound (L1) and the exponential lightcone bound (L2)
hold with the **derived** velocity `v_LR := 2·e·q·W·R`. No literature
constant is imported; the earlier conditional plug-in `v_LR = 2 e r J`
is superseded (it omitted the overlap weight; see Changelog).
(iii) Applying the lemma to the retained-grade hopping-bilinear
Hamiltonian `H_hop = Σ_links H_xy + m Σ_x n̂_x` on the `Z^d`
nearest-neighbor link family gives the **unconditional** microcausality
bound `v_LR <= 4·e·(|m| + 2d)` (on `Z^3`: `4·e·(|m| + 6) ≈ 65.24` at
`m -> 0`).
(iv) **Conditional exact-H corollary, not claimed as proved:** the
strict finite-range carrier hypothesis previously displayed for
`H = -log(T)/a_τ` is now known to fail on the free bilinear sector; it
is kept only as an implication with an unsatisfied antecedent. The live
replacement is quasilocal: if the reconstructed `H` admits bounded
per-site weight and exponentially decaying finite-range truncation
tails, then the finite-range lemma can be applied to `H_R` and composed
with tail control. That composition theorem and the gauged/interacting
exact-H locality bridge remain open; neither this note nor its runner
constructs `-log(T)`.
**Status authority:** independent audit lane only. This source note is
a bounded support-and-bridge theorem; it does not set or predict an
audit outcome.
**Primary runner:** `scripts/microcausality_finite_range_h_bridge_2026_05_09.py`

## Why this note exists

The parent note
`docs/AXIOM_FIRST_MICROCAUSALITY_LIEB_ROBINSON_THEOREM_NOTE_2026-05-01.md`
records, in its (M2), a Lieb-Robinson lightcone bound with the constant
`v_LR = 2 e r J`. The independent-audit lane flagged exactly that
load-bearing step:

> "the load-bearing finite-range-H and explicit v_LR = 2erJ step is not
> derived by the cited RP or spectrum authorities ... RP/spectrum
> provide positivity / self-adjointness / boundedness of H, not the
> locality structure (finite range) needed for Lieb-Robinson, nor an
> explicit v_LR derivation."

A subsequent audit of *this* bridge note (2026-06-10) ratified the
support and J arithmetic but found that the chain to the stated
velocity did not close, because the packet supplied neither an exact-H
locality bridge nor a retained theorem fixing the constant
`v_LR = 2 e r J` for this normalization and support-overlap
convention.

This repair closes the second gap from first principles and bounds the
first honestly:

- the Lieb-Robinson estimate is no longer an imported literature
  constant: Lemma (L1)/(L2) below is **proved inside this note** by
  the standard iterated-commutator argument, with every constant
  traced (the honest velocity is `v_LR = 2·e·q·W·R`, where `W` is the
  per-site overlap weight — the earlier `2 e r J` form is quantitatively
  wrong for this convention because it omits `q·W/J`-type overlap
  counting);
- the lemma is applied **unconditionally** to the framework hopping
  Hamiltonian supplied by the retained-grade hopping-bilinear
  authority, whose finite-range support structure is proved in Step 6
  and verified term-by-term by the runner;
- the exact non-perturbative step from the transfer matrix
  `T = exp(-a_τ H)` to a finite-range or quasilocal decomposition of
  `H = -log(T)/a_τ` remains **outside** this note: the carrier-velocity
  statement (F5) is stated as an explicit conditional and is excluded
  from the unconditional claim surface.

## Setup and conventions

### Carrier surface (declared)

The parent RP note's current in-scope surface is staggered-only:

```text
    S = S_G[U] + χ̄ (M_KS[U] + m·I) χ,        m > 0,
```

with compact SU(3) Wilson plaquette gauge links under Haar measure.
The parent names the carriers (`M_KS` staggered Kogut-Susskind,
`S_G` Wilson plaquette) but does not display coefficient
normalizations, and it explicitly excludes Wilson-fermion operators
`M_KS + M_W + m·I` from its own claim surface.

**Carrier-coefficient declaration (explicit boundary).** The explicit
matrix elements and coefficient normalizations used below are supplied
*in this note* as the displayed carrier surface, in the standard
canonical conventions:

- **Staggered Kogut-Susskind kinetic operator:**

  ```text
      (M_KS)_{x, y}  =  (1/2) · [ η_μ(x) · U_μ(x) · δ_{y, x + e_μ}
                                 - η_μ(y) · U_μ(y)^† · δ_{y, x - e_μ} ]      (1)
  ```

  with staggered phase `η_μ(x) = (-1)^{Σ_{ν<μ} x_ν}` and SU(3) link
  variable `U_μ(x)`. The hop coefficient is exactly `1/2` per
  direction (canonical Kogut-Susskind normalisation; the explicit
  `±1j/2` matrix elements are spelled out on
  `scripts/frontier_staggered_17card.py` lines 50, 63-70).

- **Wilson plaquette gauge action:**

  ```text
      S_G  =  β · sum_P  Re[ 1 - (1/N_c) tr U_P ]                            (2)
  ```

  with `β = 2 N_c / g_bare^2 = 6` at `g_bare = 1, N_c = 3`. On this
  canonical surface the normalized per-plaquette slot is bounded by
  `2β`: the per-plaquette coefficient is `β`, not `β/N_c` (the `1/N_c`
  lives inside the trace average).

- **Wilson fermion term (supplied, parent-excluded):** the parent RP
  note excludes Wilson-fermion operators from its scope. The Wilson
  diagonal surface `M_W = r_W · d · I` with `r_W = 1` is taken from
  the cited determinant-positivity bridge
  (`STAGGERED_WILSON_DET_POSITIVITY_BRIDGE_THEOREM_NOTE_2026-05-05.md`,
  Setup §) as a *supplied matrix surface*; that note does not derive
  it from the standard Wilson action, and neither does this one. The
  J/W budgets below therefore bracket three readings (supplied
  diagonal surface, displayed nearest-neighbor carrier (8), and the
  all-direction envelope), so no Wilson-surface bridge is load-bearing
  for the finiteness of any budget.

- **Mass term:** `m · I`, contributing `|m|` to the local-density
  operator norm.

- **Lattice ℓ¹ graph distance** `d(x, y) = ‖x - y‖_1`, with the
  periodic (torus) identification on finite blocks.

- **Lattice / Quantum baseline** as stated in
  [`MINIMAL_AXIOMS_2026-06-05`](MINIMAL_AXIOMS_2026-06-05.md), read
  through the parent RP note's transfer-block convention
  (`d = 4 = 1 + 3` for a `Z^1 × Z^3` block). The older `A1`/`A2`
  labels are historical aliases for this lattice-plus-one-qubit local
  algebra content.

All budgets computed below are functions of these displayed
coefficients only; they do not depend on the gauge background, the
lattice volume, or any spectral data of `T`.

### Support families (definitions used by the lemma)

Let `Λ` be a finite lattice block with metric `d(·,·)`. A **support
family** is a finite collection `F` of pairs `(Z, h_Z)` where
`Z ⊆ Λ` and `h_Z = h_Z^†` acts as the identity on every tensor factor
outside `Z`. Define

```text
    q  :=  max_{Z ∈ F} |Z|                (largest support size)
    R  :=  max_{Z ∈ F} diam(Z)            (largest support diameter)
    W  :=  max_{x ∈ Λ} Σ_{Z ∋ x} ‖h_Z‖_op  (per-site overlap weight)     (6)
```

`W` is the lemma input — not the per-assigned-site budget
`J = sup_z ‖h_z‖_op` of (F2). `W` counts *every* local term whose
support touches a given site, with multiplicity; this is exactly the
counting the superseded `2 e r J` constant omitted.

For single-site observables `A ∈ A_{\{x\}}`, `B ∈ A_{\{y\}}` the
prefactor `|X|/q` below equals `1/q`.

The reconstructed Hamiltonian `H = -log(T)/a_τ` is the time-direction
generator of the canonical RP-reconstructed transfer matrix `T` from
the parent. This note does not assume the exact logarithm is finite
range; it enters only inside the explicit conditional (F5).

## Statement

**(F1) Leading action-density support.** The displayed action-density
pieces admit a translation-covariant local grouping

```text
    H_action  =  sum_{z ∈ Λ}  h_z                                           (3)
```

with each leading local term supported in a bounded neighborhood of
`z` (`r_action <= 2` in the site `l1` metric, due to elementary
plaquettes). Equivalently, for any operator `O_x` at site `x` outside
that local action support,

```text
    [h_z, O_x]  =  0    whenever    d(z, x) > r_action.                     (4)
```

**(F2) Explicit action-density J bound.** The per-assigned-site budget
`J_action = sup_z ‖h_z‖_op` satisfies the explicit
gauge-background-independent bound

```text
    J_action  ≤  J_max  :=  (d/2) · 1   +   r_W · d   +   |m|   +   2β · q_face               (5)
```

where:

- `(d/2) · 1` is the staggered-hop contribution: `d` directions, each
  contributing one off-diagonal NN link of operator norm
  `(1/2) · ‖U_μ(x)‖_op = 1/2` because SU(3) is unitary;
- `r_W · d` is the supplied Wilson diagonal contribution
  (`M_W = r_W · d · I`, `r_W = 1`);
- `|m|` is the mass term operator norm;
- `2β · q_face` is the conservative gauge plaquette contribution, with
  `q_face = d(d-1)/2` plaquette orientations assigned to the local
  site and `|1 - Re tr(U_P)/N_c| <= 2` for unitary `U_P`.

In particular, on `Z^4` at `g_bare = 1, N_c = 3, β = 6, r_W = 1, m`
real, plug-in: `J_max = 4/2 + 1·4 + |m| + (2·6)·6 =
2 + 4 + |m| + 72 = 78 + |m|`.

**(F2b) Carrier-faithful Wilson branch.** Reading the Wilson piece
directly off the displayed carrier (8) (standard spatial
nearest-neighbor Wilson term, `μ ≠ t`, `d_s = 3` spatial directions)
instead of the supplied diagonal surface gives the per-site Wilson
budget `d_s · r_W` (diagonal) plus `d_s · (r_W/2)` (one owned link per
spatial direction, pair norm `1` by SU(3) unitarity), so

```text
    J_max^carrier  :=  (d/2) · 1  +  d_s · (r_W + r_W/2)  +  |m|  +  2β · q_face            (5b)
```

with plug-in `J_max^carrier = 2 + 9/2 + |m| + 72 = |m| + 78.5`. The
all-direction standard-Wilson envelope (`d` directions instead of
`d_s`) gives `|m| + 2 + 6 + 72 = |m| + 80`. All three readings
(supplied surface `78`, displayed carrier `78.5`, envelope `80`) are
finite, explicit, gauge-background-independent, and share
`r_action <= 2`; the diagonal-surface citation is not load-bearing for
the finiteness of any budget.

**(F2c) Per-site overlap weights (lemma input).** For the carrier
support family on `Z^4` — one site term, `2d = 8` incident links, and
`4 · d(d-1)/2 = 24` incident plaquettes per site — the per-site
overlap weight (6) evaluates exactly, on the three Wilson readings, to

```text
    W_surface = |m| + 296,    W_carrier = |m| + 298,    W_envelope = |m| + 300.   (6b)
```

The carrier family has support size `q = 4` (plaquettes) and support
diameter `R = 2` (opposite corners of an elementary square are at `l1`
distance `2`).

**(F3-L1) Lieb-Robinson series lemma (proved in Step 4).** Let
`H = Σ_{Z ∈ F} h_Z` be any support family on a finite block with
constants `(q, R, W)` as in (6), let `A ∈ A_X`, `B ∈ A_Y`, and let
`D := d(X, Y) > 0`. Then for all real `t`,

```text
    ‖ [α_t(A), B] ‖_op  ≤  2 ‖A‖ ‖B‖ · (|X|/q) · Σ_{n ≥ ⌈D/R⌉}  (2 q W |t|)^n / n!        (7)
```

where `α_t(A) = e^{iHt} A e^{-iHt}`.

**(F3-L2) Exponential lightcone corollary (proved in Step 5).** Define

```text
    v_LR  :=  2 · e · q · W · R.                                            (16)
```

Then for all real `t`,

```text
    ‖ [α_t(A), B] ‖_op  ≤  (2e/(e-1)) · ‖A‖ ‖B‖ · (|X|/q) · exp( -(D - v_LR·|t|)/R ).     (16b)
```

Both bounds are fully derived below; no step imports a literature
constant.

**(F4) Unconditional finite-range Lieb-Robinson theorem for the
framework hopping Hamiltonian.** Let

```text
    H_hop  =  Σ_{(x,y) ∈ L} H_{xy}  +  m · Σ_x n̂_x,
    H_{xy} = a_x^† a_y + a_y^† a_x,                                          (17)
```

be the translation-invariant nearest-neighbor link-family Hamiltonian
of the cited hopping-bilinear authority
(`HOPPING_BILINEAR_HERMITICITY_THEOREM_NOTE_2026-05-02.md`, B1-B6),
in its per-site tensor ladder convention (commuting modes, no
Jordan-Wigner string between sites). Then `H_hop` is a support family
with `q = 2`, `R = 1`, `‖H_{xy}‖_op = 1`, `W = |m| + 2d`, and the
lemma gives, unconditionally,

```text
    v_LR  ≤  4 · e · (|m| + 2d)        (on Z^3:  4 · e · (|m| + 6) ≈ 65.24 at m -> 0).    (17b)
```

This is a genuine microcausality statement for a Hamiltonian whose
finite-range structure is *derived* from the framework operator
content (Step 6), not assumed.

**(F5) Conditional carrier corollary (quasilocal form; the strict
finite-range reading is falsified on the bilinear sector).** The
original hypothesis read: the exact reconstructed `H = -log(T)/a_τ`
admits a support-family decomposition with `q <= 4`, `R <= 2`, and
`W <= W_envelope = |m| + 300`. **That strict finite-range reading is
false on the free bilinear two-step sector**: the exact `H` there has
genuine nonzero hops at `l1`-range 4 (`|h(4,0,0)| = 5.6e-3`,
`|h(2,2,0)| = 1.0e-2`, far above any numeric floor), so no `R <= 2`
support-family decomposition exists. Proof and constants: claim
`transfer_matrix_log_quasilocality_narrow_theorem_note_2026-06-10`
(`docs/TRANSFER_MATRIX_LOG_QUASILOCALITY_NARROW_THEOREM_NOTE_2026-06-10.md`;
cited follow-up note). *Hypothesis (F5, quasilocal restatement):* the exact
reconstructed `H = -log(T)/a_τ` is a quasilocal support family —
bounded `q`, finite total per-site overlap weight `W_H < ∞`, and
finite-range truncations `H_R` whose per-site tail weights decay
exponentially in `R`. On the free bilinear two-step sector this
quasilocal hypothesis is **discharged** by the cited note with
explicit constants: `q = 2`, sharp rate `eta* = arcsinh(m)`,
closed-form prefactor `C_d(eta, m) = sqrt(m^2 + (d-1) + cosh^2 eta)`,
`W_H = ||h||_l1 < ∞` (`= 1.757278…` at `m = 0.3`, `d = 3`,
`a_tau = 1`), and tail weights
`W_tail(R) <= O((1+R)^{d-1} e^{-eta R})` for every
`eta < arcsinh(m)`. *Under the strict hypothesis* — kept below
only as the displayed implication; its antecedent is now known to be
unsatisfiable on the bilinear sector — (F3-L2) gives

```text
    v_LR  ≤  2 · e · 4 · (|m| + 300) · 2  =  16 · e · (|m| + 300)  ≈  1.305e4              (18)
```

lattice units as `m -> 0` (supplied surface: `16·e·(|m| + 296) ≈
1.287e4`; displayed carrier: `16·e·(|m| + 298) ≈ 1.296e4`). Under the
quasilocal restatement, the analogous lightcone follows from (F3-L2)
applied to each truncation `H_R` (`q = 2`, `diam_l1 <= d·R`,
`W <= W_H`) composed with Duhamel/interpolation control of the
exponentially small tail `H - H_R`; that one-step composition theorem
is not proved here or in the cited note. The genuine residual of (F5)
is the **gauged / interacting sector**: the fixed-background
`T_hat^2[U]` is not translation-invariant, so the Fourier/contour
route of the cited note does not apply verbatim, and the
`U`-integrated interacting log-transfer locality remains the recorded
open frontier of the parent bridge gate.

## Proof

### Step 1 — Finite range from action support (proves F1)

Writing the action in temporal-link form (declared carriers (1)-(2)):

```text
    S  =  Σ_{x ∈ Λ}  m · χ̄_x χ_x
        + Σ_{x, μ}  (1/2) η_μ(x) χ̄_x U_μ(x) χ_{x + e_μ}  + h.c.
        + Σ_{x, μ ≠ t}  (r_W/2) χ̄_x ( U_μ(x) χ_{x + e_μ} - 2 χ_x + U_μ(x - e_μ)^† χ_{x - e_μ} )
        + β Σ_P  Re[ 1 - (1/N_c) tr U_P ]                                   (8)
```

Every term in (8) couples either: (a) a single site, or (b) two sites
at NN graph distance, or (c) four sites in a single elementary
plaquette. A plaquette has corner-to-corner ℓ¹ diameter `2`; assigning
each plaquette to one of its corners as the base site `z` re-casts it
as a site-`z` operator with support in the radius-`2` ball around `z`
(the opposite corner sits at `l1` distance `2`).

After per-site grouping (each displayed action-density term is
assigned to a unique base site `z`),

```text
    H_action  =  sum_{z ∈ Λ}  h_z                                           (9)
```

with the matter terms supported at nearest-neighbor range and the
plaquette terms supported on the four corners of an elementary square,
so the leading action-density support has `r_action <= 2` when indexed
by a lattice site. This proves (F1).

It does **not** prove that the exact logarithm `H = -log(T)/a_τ` is
finite range; that step enters only as the explicit hypothesis of
(F5).

**Citation chain for F1.** Carrier names/structure: parent RP note
in-scope surface (staggered-only `S = S_G + χ̄(M_KS + m·I)χ`, SU(3)
plaquette links); explicit coefficient displays: declared in this note
(Setup §); explicit lattice operators with NN support: hopping
bilinear note `HOPPING_BILINEAR_HERMITICITY_THEOREM_NOTE_2026-05-02.md`
(B2, B4 — translation-invariant link-family Hamiltonians); spatial
substrate: the named Lattice baseline in
[`MINIMAL_AXIOMS_2026-06-05`](MINIMAL_AXIOMS_2026-06-05.md), with the
parent RP note's `Z^1 × Z^3` transfer-block convention.

### Step 2 — Explicit J bound (proves F2, F2b)

Each `h_z` is a finite linear combination of the action terms based
at `z`:

```text
    h_z  =  m · n̂_z   +   (1/2) Σ_{μ} [ η_μ(z) U_μ(z) c̄_z c_{z+e_μ} + h.c. ]
            +  r_W · d · n̂_z (supplied Wilson diagonal)
            +  β Σ_{P ∋ z, base(P) = z} Re[1 - (1/N_c) tr U_P]              (10)
```

Each summand is bounded in operator norm:

- **Mass:** `‖m · n̂_z‖_op ≤ |m|`, since `n̂_z` has eigenvalues in
  `{0, 1}` on the per-site `C²`.
- **Hop:** `‖(1/2) η_μ(z) U_μ(z) c̄_z c_{z+e_μ} + h.c.‖_op ≤ 1/2` per
  direction (`|η_μ| = 1`, `‖U_μ‖_op = 1` by unitarity, pair norm `1`);
  `d` directions give `≤ d/2`.
- **Wilson diagonal (supplied surface):** `‖r_W · d · n̂_z‖_op ≤ r_W · d`.
- **Plaquette:** `‖β Re[1 - (1/N_c) tr U_P]‖_op ≤ 2β` per plaquette
  (`|tr U_P| ≤ N_c` for unitary `U_P`, hence
  `Re tr(U_P)/N_c ∈ [-1, 1]`); `q_face = d(d-1)/2` plaquette
  orientations are assigned to `z`, so the budgeted contribution is
  `2β · d(d-1)/2`.

Triangle inequality on (10):

```text
    ‖h_z‖_op  ≤  |m|  +  d/2  +  r_W · d  +  2β · d(d-1)/2               (11)
```

For `d = 4, r_W = 1, β = 6, N_c = 3`:

```text
    J_max  ≤  |m|  +  2  +  4  +  12 · 6  =  |m|  +  78                    (12)
```

**Carrier-faithful Wilson branch (proves F2b).** The Wilson term as
displayed in carrier (8) is the standard spatial nearest-neighbor form.
Per-site grouping under the same forward-link-ownership convention as
the staggered hop assigns to `h_z`, per spatial direction: the diagonal
piece `-2 · (r_W/2) χ̄_z χ_z` of coefficient magnitude `r_W`, and one
owned-link hop pair of coefficient `r_W/2` and pair norm `1`
(`‖a†(U b) + h.c.‖_op = ‖U‖_op = 1` for unitary `U`; the runner
verifies this on explicit one-particle blocks). Triangle inequality
over `d_s = 3` spatial directions replaces the `r_W · d` surface term
in (11) by `d_s · (r_W + r_W/2) = 9/2`:

```text
    J_max^carrier  ≤  |m|  +  2  +  9/2  +  12 · 6  =  |m|  +  78.5         (12b)
```

Extending the same count to all `d` directions (the all-direction
standard-Wilson envelope) gives `d · (r_W + r_W/2) = 6` and
`J_max ≤ |m| + 80`. Both branches read only displayed carrier
coefficients; the supplied diagonal surface enters only the (12)
branch value. **No gauge-background spectral data is used.**

### Step 3 — Per-site overlap weights (proves F2c)

The lemma input `W` of (6) counts every support touching a fixed site
`x ∈ Z^4`, with multiplicity:

- **site terms:** `1` (mass plus Wilson diagonal), norm `≤ |m| + r_W·d`
  on the supplied surface (`|m| + d_s·r_W` on the carrier branch,
  `|m| + d·r_W` on the envelope);
- **links containing `x`:** `2d = 8` (forward and backward per
  direction), staggered pair norm `1/2` each; on the carrier branch
  the `2·d_s = 6` spatial links also carry the Wilson pair `r_W/2`,
  giving combined norm `1` on spatial links and `1/2` on the `2`
  temporal links; on the envelope all `8` links carry combined norm
  `1`;
- **plaquettes containing `x`:** `4 · d(d-1)/2 = 24` (each of the
  `6` orientations has `4` plaquettes through `x`), norm `≤ 2β = 12`
  each, contributing `288`.

Summing the three branches:

```text
    W_surface  = |m| + 4 + 8·(1/2)      + 288 = |m| + 296
    W_carrier  = |m| + 3 + 6·1 + 2·(1/2) + 288 = |m| + 298
    W_envelope = |m| + 4 + 8·1          + 288 = |m| + 300                  (6c)
```

with `q = 4` and `R = 2` read off the plaquette supports. The runner
recomputes these counts and values in exact arithmetic. This proves
(F2c). Note `W > J_max` necessarily: `W` counts shared supports with
multiplicity (e.g. all `24` plaquettes through `x`, not the `6`
assigned to `x`).

### Step 4 — Proof of the series lemma (F3-L1)

Work on a finite block, so all operators are bounded matrices and
`α_t(A) = e^{iHt} A e^{-iHt}` is an entire function of `t`. For
`V ⊆ Λ` define

```text
    C_B(V; t)  :=  sup_{0 ≠ A' ∈ A_V}  ‖[α_t(A'), B]‖_op / ‖A'‖_op.        (13)
```

Note `C_B(V; t) ≤ 2‖B‖` always, and `C_B(V; 0) = 0` when
`V ∩ Y = ∅` (operators on disjoint tensor factors commute).

**(a) One-step inequality.** Fix `A ∈ A_X` and let
`f(t) := [α_t(A), B]`. Since `h_Z` commutes with `A` whenever
`Z ∩ X = ∅`, we have `[H, A] = [H_X, A]` with
`H_X := Σ_{Z ∩ X ≠ ∅} h_Z`. Differentiating and using
`α_t([H_X, A]) = [α_t(H_X), α_t(A)]` and the Jacobi identity,

```text
    f'(t) = i [α_t(H_X), f(t)]  -  i [α_t(A), [α_t(H_X), B]].              (14)
```

The first term is a commutator with the Hermitian operator
`α_t(H_X)`: it generates a unitary conjugation of `f`, which preserves
norms. (Explicitly, let `V(t)` solve `V'(t) = i·α_t(H_X)·V(t)`,
`V(0) = 1`; then `(V^† f V)'(t) = -i·V^† [α_t(A), [α_t(H_X), B]] V`,
and `‖V^† f V‖ = ‖f‖`.) Integrating the inhomogeneous term,

```text
    ‖f(t)‖  ≤  ‖f(0)‖  +  2 ‖A‖ Σ_{Z ∩ X ≠ ∅} ∫_0^{|t|} ‖[α_s(h_Z), B]‖ ds,
```

and since `h_Z ∈ A_Z` with `‖[α_s(h_Z), B]‖ ≤ ‖h_Z‖ · C_B(Z; s)`,
dividing by `‖A‖` and taking the supremum over `A ∈ A_X`:

```text
    C_B(X; t)  ≤  C_B(X; 0)  +  2 Σ_{Z ∩ X ≠ ∅} ‖h_Z‖ ∫_0^{|t|} C_B(Z; s) ds.   (14b)
```

**(b) Iteration over support chains.** Apply (14b) to each
`C_B(Z; s)` and iterate `n` times. The `k`-th nested time integral
contributes `|t|^k / k!`, and the surviving boundary terms are
`C_B(Z_k; 0)`, nonzero only when `Z_k ∩ Y ≠ ∅`. With `D > 0` the
`k = 0` term vanishes, so

```text
    C_B(X; t)  ≤  Σ_{k ≥ 1}  (2|t|)^k / k!  ·
                  Σ_{chains}  ‖h_{Z_1}‖ ··· ‖h_{Z_k}‖  ·  2‖B‖,            (15)
```

where the inner sum runs over chains `(Z_1, …, Z_k)` with
`Z_1 ∩ X ≠ ∅`, `Z_{i+1} ∩ Z_i ≠ ∅`, and `Z_k ∩ Y ≠ ∅`. (The
`n`-step remainder is bounded by
`2‖B‖ (|X|/q)(2qW|t|)^n / n! → 0`, so the infinite iteration is
justified on the finite block.)

**(c) Chain weight counting.** By definition of `W`,
`Σ_{Z ∩ V ≠ ∅} ‖h_Z‖ ≤ Σ_{x ∈ V} Σ_{Z ∋ x} ‖h_Z‖ ≤ |V| · W` for any
`V`. Hence the first chain slot contributes `≤ |X| W` and each
subsequent slot `≤ |Z_i| W ≤ q W`, so

```text
    Σ_{chains, length k}  ‖h_{Z_1}‖ ··· ‖h_{Z_k}‖   ≤   |X| W · (qW)^{k-1}
                                                     =   (|X|/q) (qW)^k.
```

**(d) Reach constraint.** Every point of `Z_1` lies within `R` of
`X` (since `Z_1 ∩ X ≠ ∅` and `diam(Z_1) ≤ R`); inductively every
point of `Z_i` lies within `i·R` of `X`. A chain with `Z_k ∩ Y ≠ ∅`
therefore requires `k·R ≥ D`, i.e. `k ≥ ⌈D/R⌉`; shorter chains
contribute zero.

Combining (b)-(d) and multiplying back by `‖A‖`:

```text
    ‖[α_t(A), B]‖  ≤  2 ‖A‖ ‖B‖ (|X|/q) Σ_{n ≥ ⌈D/R⌉} (2qW|t|)^n / n!,
```

which is (7). ∎ (F3-L1)

### Step 5 — Exponential lightcone corollary (proves F3-L2)

Set `a := 2qW|t|` and `n_0 := ⌈D/R⌉`. From `e^n ≥ n^n / n!` we get
`n! ≥ (n/e)^n`, hence `a^n/n! ≤ (ea/n)^n`. Using
`ln x ≤ x - 1` with `x = ea/n`, `(ea/n)^n ≤ e^{ea - n}`, so

```text
    Σ_{n ≥ n_0} a^n / n!  ≤  Σ_{n ≥ n_0} e^{ea - n}
                          =  e^{ea} · e^{-n_0} / (1 - e^{-1}).
```

With `n_0 ≥ D/R` and `e·a = 2·e·q·W·|t| = v_LR·|t| / R` for
`v_LR := 2·e·q·W·R`,

```text
    ‖[α_t(A), B]‖  ≤  (2e/(e-1)) ‖A‖ ‖B‖ (|X|/q) · exp( (v_LR·|t| - D)/R ),
```

which is (16b) with every constant derived: `2e/(e-1) ≈ 3.164` from
the geometric tail, `1/R` as the decay rate, and

```text
    v_LR  :=  2 · e · q · W · R                                            (16c)
```

as the velocity. ∎ (F3-L2)

**Remark (supersedes `2 e r J`).** The parent's (M2) form
`v_LR = 2 e r J` is recovered *in shape* but not in constant: the
honest velocity multiplies the support diameter `R` by the *overlap
weight* `q·W`, not by the per-assigned-site budget `J`. For the
carrier family `q·W ≈ 4·(|m|+300)` while `J ≈ |m|+80`, an
order-of-magnitude difference. No statement in this note relies on
the `2 e r J` constant.

### Step 6 — Unconditional application to the framework hopping H (proves F4)

The cited hopping-bilinear authority supplies, on the finite periodic
tensor-product Fock space, the operators
`H_{xy} = a_x^† a_y + a_y^† a_x` (B1: Hermitian; B2: translation
covariant; B4: translation-invariant link-family sums commute with
translations and conserve `Q_total`; B6: `H_{xy}` is the swap on the
one-particle two-site subspace and annihilates `|00⟩, |11⟩`). Its
per-site mode convention is the commuting tensor-product convention
(`a_x` acts as the ladder matrix on factor `C²_x` and as the identity
elsewhere; no Jordan-Wigner string between sites).

- **Support:** `a_x` and `a_x^†` act as the identity outside factor
  `x`, so `H_{xy}` acts as the identity outside `{x, y}`:
  `supp(H_{xy}) ⊆ {x, y}`, support size `2`, diameter `1` on the NN
  link family. Likewise `supp(m·n̂_x) = {x}`.
- **Norms:** by B6, `H_{xy}` is a swap on a 2-dimensional subspace and
  zero on its complement, so `‖H_{xy}‖_op = 1` exactly;
  `‖m·n̂_x‖_op = |m|`.
- **Overlap weight:** each site lies in exactly `2d` NN link-family
  members (forward and backward per direction) plus its own mass
  term, so `W = |m| + 2d`; `q = 2`, `R = 1`.

Applying (F3-L2):

```text
    v_LR  ≤  2 · e · 2 · (|m| + 2d) · 1,   i.e.   v_LR  ≤  4 · e · (|m| + 2d).   (17c)
```

On the `Z^3` lattice (`d = 3`): `v_LR ≤ 4·e·(|m| + 6)`
(`≈ 65.24` at `m -> 0`; `≈ 68.50` at `m = 0.3`). The runner verifies
the support structure term-by-term, the exact norms, and both bounds
(7) and (16b) against exactly computed commutator norms
`‖[α_t(σ_z^{(0)}), σ_z^{(d)}]‖_op` on the actual `H_hop`, plus a
falsification leg: adding a single long-range bond (support diameter
`5 > R = 1`) makes the measured commutator violate the finite-range
bounds by a factor `> 60` on (7). The finite-range hypothesis is
load-bearing, not decorative. ∎ (F4)

### Step 7 — Conditional carrier corollary (proves F5 as an implication)

Assume the hypothesis of (F5): the exact reconstructed
`H = -log(T)/a_τ` admits a support-family decomposition with
`q <= 4`, `R <= 2`, `W <= |m| + 300` (the (F2c) envelope). Then
(F3-L2) applies verbatim and yields (18):
`v_LR ≤ 16·e·(|m| + 300)`. The implication is fully closed by Steps
4-5; the hypothesis is **not** proved here and is recorded as the open
frontier (BCH/Trotter commutators of local terms can enlarge range).
∎ (F5)

## Hypothesis set used

The proof uses:

- **Lattice / Quantum baseline**
  ([`MINIMAL_AXIOMS_2026-06-05`](MINIMAL_AXIOMS_2026-06-05.md)) with
  the parent RP transfer-block convention — the one-qubit local
  algebra and lattice graph distance used for per-site operator-norm
  bounds and support radii.
- **Parent RP note in-scope surface**
  (`AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md`) —
  carrier *names and structure* (staggered-only
  `S = S_G + χ̄(M_KS + m·I)χ`, compact SU(3) plaquette links). The
  explicit coefficient normalizations are declared in this note's
  Setup (explicit boundary), since the parent does not display them
  and excludes Wilson-fermion operators from its own scope.
- **Hopping bilinear note**
  (`HOPPING_BILINEAR_HERMITICITY_THEOREM_NOTE_2026-05-02.md`, B1-B6)
  — supplies the framework hopping Hamiltonian, its Hermiticity,
  translation-covariant link-family sums, `Q_total` conservation, and
  the two-site swap action used for `‖H_{xy}‖ = 1` and the support
  structure in Step 6.
- **Symmetric-canonical Wilson form**
  (`STAGGERED_WILSON_DET_POSITIVITY_BRIDGE_THEOREM_NOTE_2026-05-05.md`,
  Setup §) — `M_W = r_W · d · I` as a *supplied* surface, entering the
  (F2)/(12) branch value only; after the (F2b) bracket this citation
  is not load-bearing for the finiteness of any budget.
- **SU(3) link unitarity** — `‖U_μ‖_op = 1`; pure group theory.
- **Standard finite-dimensional operator algebra** — the
  iterated-commutator Lieb-Robinson argument of Steps 4-5 is proved
  in-note; the Lieb-Robinson / Hastings-Koma / Nachtergaele-Sims
  literature is cited as *provenance for the proof technique only*,
  not as an imported bound or constant.

No fitted parameters. No observed values. The exact finite-range /
quasilocal property of the reconstructed logarithmic Hamiltonian is
not derived here and is quarantined inside the explicit hypothesis of
(F5).

## Corollaries

C1. **Narrows the parent (M2) gap.** The parent gap is no longer an
undifferentiated missing bridge: the action-density radius, the
budgets `J_max`, the overlap weights `W`, and a fully proved LR lemma
with derived constants are all explicit. The remaining missing step is
exactly one hypothesis: non-perturbative finite-range/quasilocal
control of `H = -log(T)/a_τ`.

C2. **Explicit conditional numerical ceiling.** Under the (F5)
hypothesis at the canonical surface
(`d = 4, r_W = 1, β = 6, N_c = 3`), the envelope ceiling is
`v_LR ≤ 16·e·(|m| + 300) ≈ 1.305e4` lattice units as `|m| -> 0`
(supplied surface `≈ 1.287e4`, displayed carrier `≈ 1.296e4`). This
replaces the superseded `2 e r J` plug-in numbers (`≈ 8.5e2`), which
omitted the overlap weight. Conversion to the emergent speed of light
proceeds via the lattice-spacing ratio `v_LR · a_s / a_τ -> c < ∞`
(parent (M3); see `docs/EMERGENT_LORENTZ_INVARIANCE_NOTE.md`), which
remains audit-pending and is not claimed here.

C3. **Unconditional microcausality exemplar.** Independently of (F5),
the framework hopping Hamiltonian on `Z^3` satisfies the exponential
lightcone bound (16b) with `v_LR ≤ 4·e·(|m| + 6)`. The companion
cluster-decomposition note's form `v_LR = 2 e J Z_lat R_int` (its
eq. (1)) is compatible in shape; it is not a load-bearing dependency
here.

C4. **Higher-order Trotter / BCH corrections.** The leading-order
bounded action-support structure receives BCH corrections of order
`a_τ · J_max`. A fully non-perturbative bound on these corrections is
exactly the (F5) hypothesis and is the recorded open frontier of this
note.

## Honest status

**Bounded support-and-bridge theorem on the supplied/displayed
carrier surface.** Statements (F1)-(F4) are unconditional given the
declared carrier coefficients and the cited authorities; (F5) is an
explicit implication whose hypothesis is open.

What the runner checks (test → claim map):

- `F0`: note/runner manifest sync (bookkeeping guard, not a proof).
- `F1`: (F1) on an explicit toy block — `[h_z, O_x] = 0` outside the
  support radius.
- `F2`: (F2) budget arithmetic against random SU(3) backgrounds.
- `F2b`: (F2b) unit pair norm, grouped Wilson block norm on explicit
  one-particle matrices, exact branch arithmetic `78 ≤ 78.5 ≤ 80`.
- `F2c`: (F2c) per-site support counts (`1 / 8 / 24`) and overlap
  weights `296 / 298 / 300` in exact arithmetic, plus the (F5)
  velocity ceilings.
- `F3`: (F4) on the actual framework hopping Hamiltonian on a periodic
  chain — `‖H_{xy}‖ = 1` and term-by-term finite-range support
  (F3(a)), then the proved bounds (7) and (16b) against exactly
  computed commutator norms on a `(distance, time)` grid (F3(b),
  F3(c)). The bound is rigorous, not tuned: the minimum
  bound/measured margin is reported.
- `F4`: outside-lightcone exponential decay of the exact commutator on
  the same framework Hamiltonian.
- `F5`: falsification leg — one long-range bond (diameter `5 > R = 1`)
  violates the finite-range premise and breaks the (7)/(16b) bounds by
  `> 60x` / `> 3x`, demonstrating the premise is load-bearing.
- `F6`: (F4) support-family data on the minimal periodic `2×2×2 Z^3`
  block — Hermiticity, `Q_total` conservation, tensor-factor support
  of every `H_{xy}`, and `W = |m| + 2d = |m| + 6`.

The runner does **not** construct the exact RP logarithm; nothing in
its PASS lines bears on the truth of the (F5) hypothesis.

**What this rules out.**

- Treating the action-density support, `J`/`W` budgets, or the LR
  velocity constant as unknown, spectral, or literature-imported.
  Those pieces are now explicit, gauge-background-independent, and
  (for the lemma) proved in-note.
- The `2 e r J` velocity constant for this support-overlap
  convention: the falsifiable lemma constant is `2·e·q·W·R`.

**Not in scope.**

- A non-perturbative finite-range or quasilocal bound for the exact
  reconstructed `H = -log(T)/a_τ` (the (F5) hypothesis). This remains
  the parent bridge gate.
- A derivation of the Wilson diagonal surface `M_W = r_W·d·I` from
  the standard Wilson action (supplied surface only, and bracketed by
  F2b so it is not load-bearing).
- A fermionic-anticommutation (Jordan-Wigner) realization of the
  hopping family: the cited bridge proves the commuting per-site mode
  convention, and (F4) is claimed in that convention only.
- A rigorous Lorentz-continuum extrapolation (parent (M3), audit
  pending).
- Promotion of the parent note on the canonical paper package.

## Citations

- minimal axioms: [`MINIMAL_AXIOMS_2026-06-05`](MINIMAL_AXIOMS_2026-06-05.md)
- parent microcausality note (context only, not a load-bearing input):
  `AXIOM_FIRST_MICROCAUSALITY_LIEB_ROBINSON_THEOREM_NOTE_2026-05-01.md`
- parent RP note (carrier names/structure; staggered-only in-scope
  surface):
  [`AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md`](AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md)
- companion cluster-decomposition note (compatibility context only):
  `AXIOM_FIRST_CLUSTER_DECOMPOSITION_THEOREM_NOTE_2026-04-29.md`
- hopping bilinear note (B1-B6 used for the unconditional leg):
  [`HOPPING_BILINEAR_HERMITICITY_THEOREM_NOTE_2026-05-02.md`](HOPPING_BILINEAR_HERMITICITY_THEOREM_NOTE_2026-05-02.md)
- symmetric-canonical Wilson surface (supplied; F2 branch value only):
  [`STAGGERED_WILSON_DET_POSITIVITY_BRIDGE_THEOREM_NOTE_2026-05-05.md`](STAGGERED_WILSON_DET_POSITIVITY_BRIDGE_THEOREM_NOTE_2026-05-05.md)
- proof-technique provenance (no bound or constant imported):
  Lieb-Robinson 1972; Hastings-Koma 2006; Nachtergaele-Sims 2010 §3-4.

## Changelog

- **2026-05-09** — original note: action-support and J budget plus a
  conditional `v_LR = 2 e r J` plug-in citing Hastings-Koma /
  Nachtergaele-Sims as an external constant.
- **2026-06-09** — J-normalization + Wilson-surface bridge repair. The
  earlier draft bounded each Wilson plaquette by `2β/N_c`; on the
  canonical surface `S_W = β Σ_P (1 - Re Tr U_P / N_c)` the normalized
  plaquette slot is bounded by `2β`, raising the conservative budget
  from `|m| + 30` to `|m| + 78` and removing the double division by
  `N_c`. Added the carrier-faithful F2b bracket (`78 ≤ 78.5 ≤ 80`).
- **2026-06-10** — proved-lemma repair (this revision), addressing the
  2026-06-10 conditional audit (`missing_bridge_theorem`):
  (a) the Lieb-Robinson estimate is now **proved in-note** (Steps 4-5)
  with every constant derived; the imported `2 e r J` constant is
  removed and shown to be quantitatively wrong for this convention
  (it omitted the overlap weight `q·W`); the honest velocity is
  `v_LR := 2·e·q·W·R`;
  (b) added the per-site overlap weights (F2c):
  `W_surface = |m| + 296`, `W_carrier = |m| + 298`,
  `W_envelope = |m| + 300`;
  (c) added the unconditional leg (F4): the retained-grade hopping
  Hamiltonian is proved finite-range and obeys
  `v_LR  ≤  4 · e · (|m| + 2d)`;
  (d) the exact-H step is quarantined as the explicit (F5) hypothesis
  and excluded from the unconditional claim surface;
  (e) corrected the stale carrier attribution: the parent RP note
  names the staggered-only carriers but does not display coefficient
  normalizations (declared here) and excludes Wilson-fermion
  operators (supplied surface, bracketed by F2b);
  (f) fixed a Step 1 support typo (plaquette corner assignment is a
  radius-2 ball, not radius-1);
  (g) runner rebuilt: constructs the actual framework hopping
  Hamiltonian, checks the proved bounds against exact commutator
  norms, adds the long-range falsification leg and the `Z^3` block
  check.
- **2026-06-10** — (F5) restated quasilocally (follow-up, this
  revision). The strict finite-range reading of the (F5) hypothesis
  (`q <= 4`, `R <= 2`, `W <= |m| + 300` for the exact
  `H = -log(T)/a_τ`) is **falsified on the free bilinear two-step
  sector**: the exact `H` has genuine `l1`-range-4 hops
  (`|h(4,0,0)| = 5.6e-3`). On that sector the quasilocal form is
  proved with sharp rate `arcsinh(m)`, explicit prefactor, finite
  overlap weight `W_H = ||h||_1`, and exponentially small truncation
  tails by
  `transfer_matrix_log_quasilocality_narrow_theorem_note_2026-06-10`
  (`docs/TRANSFER_MATRIX_LOG_QUASILOCALITY_NARROW_THEOREM_NOTE_2026-06-10.md`,
  cited follow-up note). The genuine residual is the gauged /
  interacting `T[U]` sector (not translation-invariant; the Fourier
  route fails there). No other section renumbered or restructured;
  runner untouched.

## Audit dependency repair links

This graph-bookkeeping section records the explicit dependency
chain. It does not promote this note or change the audited claim
scope.

- [axiom_first_reflection_positivity_theorem_note_2026-04-29](AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md)
- [hopping_bilinear_hermiticity_theorem_note_2026-05-02](HOPPING_BILINEAR_HERMITICITY_THEOREM_NOTE_2026-05-02.md)
- [staggered_wilson_det_positivity_bridge_theorem_note_2026-05-05](STAGGERED_WILSON_DET_POSITIVITY_BRIDGE_THEOREM_NOTE_2026-05-05.md)
