# Bounded Action-Support J Bound for the Microcausality / Lieb-Robinson Bridge

**Date:** 2026-05-09
**Type:** bounded_theorem
**Claim scope:** On the symmetric-canonical staggered +
Wilson-diagonal + Wilson-plaquette action-density surface read off
from the parent reflection-positivity note's action carriers
([`AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md`](AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md),
eq. (1) for `M = M_KS + M_W + m·I` and eq. (2) for the Wilson plaquette
gauge action), the leading local action-density pieces have bounded
site support radius `r_action <= 2` in the lattice `l1` metric
(nearest-neighbor matter terms plus elementary plaquettes) and a
conservative gauge-background-independent operator-norm bound
`J_action <= |m| + 78` at `d = 4`, `r_W = 1`, `β = 6`, `N_c = 3`.
That value reads the Wilson piece on the supplied diagonal surface
`M_W = r_W · d · I`. A companion carrier-faithful branch (F2b) bounds
the displayed standard spatial nearest-neighbor Wilson term of eq. (8)
directly, giving `J_action <= |m| + 78.5`, and the all-direction
standard-Wilson envelope gives `J_action <= |m| + 80`; all three
readings share `r_action <= 2`, so no Wilson-surface bridge is
load-bearing for the finiteness of the budget.
If an exact reconstructed Hamiltonian decomposition `H = sum_z h_z`
with compatible finite-range/quasilocal constants is independently
established, the standard Hastings-Koma / Nachtergaele-Sims estimate
then gives the corresponding `v_LR <= 2 e r J` bound. This note
supplies bounded action-support evidence for the parent microcausality
bridge; it does not prove the exact non-perturbative
`H = -log(T)/a_tau` finite-range step.
**Audit repair:** 2026-06-09 J-normalization + Wilson-surface bridge
repair. The previous draft bounded each Wilson plaquette by
`2β/N_c`; on the canonical Wilson surface
`S_W = (β/N_c) sum_P (N_c - Re Tr U_P) =
β sum_P (1 - Re Tr U_P/N_c)`, the normalized plaquette slot is
bounded by `2β`. This raises the conservative bound from `|m| + 30`
to `|m| + 78` and removes the double division by `N_c`.
**Status authority:** independent audit lane only. This source note is
a bounded support theorem; it does not set or predict an audit outcome.
**Primary runner:** `scripts/microcausality_finite_range_h_bridge_2026_05_09.py`

## Why this note exists

The parent note
`docs/AXIOM_FIRST_MICROCAUSALITY_LIEB_ROBINSON_THEOREM_NOTE_2026-05-01.md`
records, in its (M2), the Lieb-Robinson lightcone bound

```text
    ‖ [α_t(O_x), O_y] ‖_op  ≤  2 ‖O_x‖ ‖O_y‖ · exp(- d(x,y) + v_LR · |t|)
```

with `v_LR = 2 e r J`. The independent-audit lane verdict (audit row
`axiom_first_microcausality_lieb_robinson_theorem_note_2026-05-01`,
2026-05-05) flagged exactly the load-bearing step

> "the load-bearing finite-range-H and explicit v_LR = 2erJ step is not
> derived by the cited RP or spectrum authorities ... RP/spectrum
> provide positivity / self-adjointness / boundedness of H, not the
> locality structure (finite range) needed for Lieb-Robinson, nor an
> explicit v_LR derivation."

This note supplies a bounded part of that bridge. Reading the *same*
canonical action carriers that the parent RP note already uses (eq. (1)
and (2) of the parent), it records the local action-density support and
computes a conservative upper bound on the local coefficient/norm
budget. The exact non-perturbative step from the transfer matrix
`T = exp(-a_τ H)` to a finite-range or quasilocal decomposition of
`H = -log(T)/a_τ` remains outside this note.

The standard Hastings-Koma / Nachtergaele-Sims estimate is therefore
used conditionally: once a finite-range reconstructed Hamiltonian with
explicit `r` and `J` is independently available, the velocity is
`v_LR = 2 e r J`.

## Setup and conventions

Adopt the parent reflection-positivity note's action carriers verbatim:

- **Lattice / Quantum baseline** as stated in
  [`MINIMAL_AXIOMS_2026-06-05`](MINIMAL_AXIOMS_2026-06-05.md), read through
  the parent RP note's transfer-block convention (`d = 4 = 1 + 3` for a
  `Z^1 × Z^3` block). The older parent labels `A1`/`A2` are historical
  aliases for this lattice-plus-one-qubit local algebra content.
- **Staggered Kogut-Susskind kinetic operator** from parent eq. (1):

  ```text
      (M_KS)_{x, y}  =  (1/2) · [ η_μ(x) · U_μ(x) · δ_{y, x + e_μ}
                                 - η_μ(y) · U_μ(y)^† · δ_{y, x - e_μ} ]      (1)
  ```

  with staggered phase `η_μ(x) = (-1)^{Σ_{ν<μ} x_ν}` and SU(3) link
  variable `U_μ(x)`. The hop coefficient is exactly `1/2` per direction
  (canonical Kogut-Susskind normalisation, verified against the
  symbolic structure on `scripts/frontier_staggered_17card.py` lines
  50, 63-70 which spell out the explicit `±1j/2` matrix elements for
  the staggered Dirac on `Z^d`).

- **Wilson term** from parent §3a: `M_W` with canonical Wilson
  coefficient `r_W = 1`, supported on the same NN link family as
  `M_KS`; on the symmetric-canonical surface
  (`STAGGERED_WILSON_DET_POSITIVITY_BRIDGE_THEOREM_NOTE_2026-05-05.md`),
  `M_W = r_W · d · I` so its operator-norm contribution is the diagonal
  bound `r_W · d`. This note uses that cited symmetric-canonical
  Wilson surface; it does not separately derive that diagonal surface
  from the full standard Wilson nearest-neighbor action. The J budget
  below therefore brackets both readings: (F2) uses this supplied
  diagonal surface, while (F2b) bounds the displayed nearest-neighbor
  form in eq. (8) directly, with the all-direction standard-Wilson
  envelope recorded alongside, so neither reading is load-bearing for
  the finiteness of the budget.

- **Mass term** from parent eq. (1): `m · I`, contributing `|m|` to
  the local-density operator norm.

- **Wilson plaquette gauge action** from parent eq. (2):

  ```text
      S_G  =  β · sum_P  Re[ 1 - (1/N_c) tr U_P ]                            (2)
  ```

  with `β = 2 N_c / g_bare^2 = 2 N_c = 6` at `g_bare = 1, N_c = 3`. A
  plaquette `P` couples four sites that span a single elementary
  square; in the time-direction transfer-matrix decomposition each
  plaquette term contributes to `h_z` for `z` at the plaquette corner.
  Equivalently, on the canonical Wilson surface,
  `S_G = (β/N_c) · sum_P (N_c - Re Tr U_P)
       = β · sum_P (1 - Re Tr U_P/N_c)`. The factor `1/N_c`
  normalizes the trace inside the plaquette slot; after this rewrite
  the per-plaquette coefficient is `β`, not `β/N_c`.

- **Lattice ℓ¹ graph distance** `d(x, y) = ‖x - y‖_1` on `Z^d`.

- **Coordination number** `Z_lat = 2 d` (`= 8` on `Z^4`, `= 6` on `Z^3`).

The reconstructed Hamiltonian `H = -log(T)/a_τ` is the time-direction
generator of the canonical RP-reconstructed transfer matrix `T` from
the parent. This note does not assume that the exact logarithm is
finite range; it records the leading action-density support and the
local norm budget that a later exact-H bridge must preserve or replace
with a quasilocal LR estimate.

## Statement

**(F1) Leading action-density support.** The canonical action-density
pieces admit a translation-covariant local grouping

```text
    H_action  =  sum_{z ∈ Λ}  h_z                                           (3)
```

with each leading local term supported in a bounded local
action-support neighborhood around `z` (`r_action <= 2` in the site
`l1` metric, due to elementary plaquettes). Equivalently, for any
operator `O_x` at site `x` outside that local action support,

```text
    [h_z, O_x]  =  0    whenever    d(z, x) > r_action.                     (4)
```

**(F2) Explicit action-density J bound.** The local action-density
operator-norm `J_action = sup_z ‖h_z‖_op`
satisfies the **explicit gauge-background-independent bound**

```text
    J_action  ≤  J_max  :=  (d/2) · 1   +   r_W · d   +   |m|   +   2β · q_face               (5)
```

where:

- `(d/2) · 1` is the staggered-hop contribution: `d` directions, each
  contributing one off-diagonal NN link of operator norm
  `(1/2) · ‖U_μ(x)‖_op = (1/2) · 1` because SU(3) is unitary
  (`‖U_μ‖_op = 1` always);
- `r_W · d` is the symmetric-canonical Wilson diagonal contribution
  (per `STAGGERED_WILSON_DET_POSITIVITY_BRIDGE_THEOREM_NOTE_2026-05-05.md`
  using `M_W = r_W · d · I` with `r_W = 1`);
- `|m|` is the mass term operator norm;
- `2β · q_face` is the conservative gauge plaquette
  contribution, with `q_face = d(d-1)/2` plaquette orientations
  assigned to the local site. The factor 2 comes from
  `|1 - Re tr(U_P)/N_c| <= 2`, using `|tr U_P| <= N_c` for unitary
  `U_P`.

In particular, on `Z^4` at `g_bare = 1, N_c = 3, β = 6, r_W = 1, m`
real, plug-in: `J_max = 4/2 + 1·4 + |m| + (2·6)·6 =
2 + 4 + |m| + 72 = 78 + |m|`.

`J_max` does NOT depend on the gauge background `{U_μ}`, on the lattice
volume, or on any spectral data of `T`. It depends only on the fixed
action coefficients.

**(F2b) Carrier-faithful Wilson branch.** Reading the Wilson piece
directly off the displayed carrier (8) (standard spatial
nearest-neighbor Wilson term, `μ ≠ t`, `d_s = 3` spatial directions)
instead of the supplied diagonal surface gives the per-site Wilson
budget `d_s · r_W` (diagonal, `2 · (r_W/2)` per spatial direction)
plus `d_s · (r_W/2)` (one owned link per spatial direction, pair norm
`1` by SU(3) unitarity, same convention as the staggered-hop bullet),
so

```text
    J_max^carrier  :=  (d/2) · 1  +  d_s · (r_W + r_W/2)  +  |m|  +  2β · q_face            (5b)
```

with plug-in `J_max^carrier = 2 + 9/2 + |m| + 72 = |m| + 78.5` at the
same canonical values. The all-direction standard-Wilson envelope
(`d` directions instead of `d_s`) gives `|m| + 2 + 6 + 72 = |m| + 80`.
All three readings (supplied surface `78`, displayed carrier `78.5`,
envelope `80`) are finite, explicit, gauge-background-independent, and
share the same support radius `r_action <= 2`; the diagonal-surface
citation is therefore not load-bearing for the finiteness of the
budget, and the conditional velocity statement below quotes the
envelope as the reading-independent ceiling.

**(F3) Conditional Lieb-Robinson velocity bound.** If the exact
reconstructed Hamiltonian has a finite-range/quasilocal decomposition
with the same action-support radius and local bound, then plugging
(F1)–(F2) into the Hastings-Koma / Nachtergaele-Sims
iterated-commutator combinatorial estimate (Lieb-Robinson 1972 /
Nachtergaele-Sims 2010 §3-4) yields the explicit Lieb-Robinson
velocity

```text
    v_LR  =  2 · e · r · J                                                  (6)
```

with `r` supplied by the exact-H locality bridge and `J ≤ J_max` from
(F2). If the exact-H bridge preserves the leading action support
radius, then `r <= 2` and `v_LR <= 4 e J_max`. The Lieb-Robinson bound
(parent (M2) eq. (5)) becomes

```text
    ‖ [α_t(O_x), O_y] ‖_op  ≤  2 ‖O_x‖ ‖O_y‖ · exp(- d(x, y) + v_LR · |t|)    (7)
```

with the constants read off the action coefficients only. The remaining
bridge is the exact-H locality step for `H = -log(T)/a_τ`.

## Proof

### Step 1 — Finite range from action support (proves F1)

The transfer matrix `T` is defined by integrating out a single time
slice in the lattice path integral on `Λ_+ = { x : t ≥ 0 }`. Writing
the action in temporal-link form (parent eq. (1)–(2)):

```text
    S  =  S_F  +  S_G
       =  Σ_{x ∈ Λ}  m · χ̄_x χ_x
        + Σ_{x, μ}  (1/2) η_μ(x) χ̄_x U_μ(x) χ_{x + e_μ}  + h.c.
        + Σ_{x, μ ≠ t}  (r_W/2) χ̄_x ( U_μ(x) χ_{x + e_μ} - 2 χ_x + U_μ(x - e_μ)^† χ_{x - e_μ} )
        + β Σ_P  Re[ 1 - (1/N_c) tr U_P ]                                   (8)
```

Every term in (8) couples either: (a) a single site, or (b) two sites
at NN graph distance, or (c) four sites in a single elementary
plaquette (which has corner-to-corner ℓ¹ diameter `2`, but every
plaquette can be assigned to one of its corners as the "site index"
and re-cast as a site-z operator with support in the radius-`1` ball
around `z`).

The transfer-matrix machinery of the parent RP note (eq. (R3)) gives
`T = e^{-a_τ · H}` with `H = -log(T)/a_τ`. Lattice translation
covariance of `S` (lattice Noether N1, cited via the
`HOPPING_BILINEAR_HERMITICITY_THEOREM_NOTE_2026-05-02.md` chain)
implies `T` is built from translation-equivariant couplings over the
spatial slice. Each spatial-link, mass, Wilson, or plaquette term in
`S` is supported on a fixed-radius ball around its base point.

Concretely, the first-order temporal-link transfer-matrix expansion
has the form `T = exp(-a_τ H_kinetic) · exp(-a_τ H_gauge) + O(a_τ^2)`,
where each displayed factor is a sum of local action-density terms.
After per-site grouping (each displayed action-density term is assigned
to a unique base site `z`),

```text
    H_action  =  sum_{z ∈ Λ}  h_z                                           (9)
```

with the matter terms supported at nearest-neighbor range and the
plaquette term supported on the four corners of an elementary square.
The Wilson plaquette has corner-to-corner `l1` diameter `2`, so the
leading action-density support has `r_action <= 2` when indexed by a
lattice site.

This proves the bounded action-support statement (F1). It does not
prove that the exact logarithm `H = -log(T)/a_τ` is finite range.
BCH/Trotter commutators of local terms can enlarge range, and a
non-perturbative finite-range or quasilocal estimate for the exact
reconstructed `H` remains a separate bridge.

**Citation chain for F1.** Action structure: parent RP note Step 1
(gauge plaquette decomposition) + Step 2 (staggered hop
decomposition); explicit lattice operators with NN support: hopping
bilinear note `HOPPING_BILINEAR_HERMITICITY_THEOREM_NOTE_2026-05-02.md`
(B2, B4 — translation-invariant link-family Hamiltonians);
spatial substrate: the named Lattice baseline in
[`MINIMAL_AXIOMS_2026-06-05`](MINIMAL_AXIOMS_2026-06-05.md), with the parent
RP note's `Z^1 × Z^3` transfer-block convention. The argument is now
traceable to the minimal axiom authority through these source notes, not
asserted.

### Step 2 — Explicit J bound (proves F2)

Each `h_z` is a finite linear combination of the action terms based
at `z`:

```text
    h_z  =  m · n̂_z   +   (1/2) Σ_{μ} [ η_μ(z) U_μ(z) c̄_z c_{z+e_μ} + h.c. ]
            +  r_W · n̂_z (Wilson diagonal)
            +  β Σ_{P ∋ z} Re[1 - (1/N_c) tr U_P]                          (10)
```

Each summand is bounded in operator norm:

- **Mass:** ‖m · n̂_z‖_op ≤ |m| · ‖n̂_z‖_op = |m|, since `n̂_z` is a
  number operator with eigenvalues in `{0, 1}` on the per-site Pauli
  C² (per-site uniqueness chain).
- **Hop:** ‖(1/2) η_μ(z) U_μ(z) c̄_z c_{z+e_μ}‖_op ≤ (1/2) · 1 · 1 · 1
  = 1/2 (using `|η_μ| = 1`, `‖U_μ‖_op = 1` because U is unitary,
  fermion ladder operators bounded by 1). There are `d` directions
  and a `+ h.c.` term, so the total hop contribution is `≤ d/2`.
  (Note: the Hermitian sum doubles the count but the absolute
  value is shared, so the operator-norm bound is `(d/2) · 1 = d/2`.)
- **Wilson diagonal:** ‖r_W · d · I‖_op = r_W · d (parent §3a
  symmetric-canonical surface).
- **Plaquette:** ‖β Re[1 - (1/N_c) tr U_P]‖_op
  ≤ β · |1 - (1/N_c) tr U_P| ≤ 2β
  per plaquette (using `|tr U_P| ≤ N_c` for unitary U_P, hence
  `Re tr(U_P)/N_c ∈ [-1, 1]`). Summing over plaquette orientations
  assigned to `z`, there are `q_face = d(d-1)/2` such plaquettes. The
  conservative per-site bound is therefore
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
displayed in carrier (8) is the standard spatial nearest-neighbor form
`Σ_{x, μ ≠ t} (r_W/2) χ̄_x ( U_μ(x) χ_{x+e_μ} - 2 χ_x + U_μ(x-e_μ)^† χ_{x-e_μ} )`.
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
standard-Wilson envelope, conservative against any temporal-Wilson
reading) gives `d · (r_W + r_W/2) = 6` and `J_max ≤ |m| + 80`. Both
branches read only displayed carrier coefficients; the supplied
diagonal surface enters only the (12) branch value.

This is a closed-form bound depending only on the action coefficients,
gauge group rank, lattice dimension, and mass. **No gauge-background
spectral data is used.**

### Step 3 — v_LR from Hastings-Koma combinatorial estimate (proves F3)

The Hastings-Koma / Nachtergaele-Sims iterated-commutator estimate
(Nachtergaele-Sims 2010 Theorem 3.1; the same argument that the parent
microcausality note's Step 2 already adapts) takes as input *only*:

1. a finite-range Hamiltonian `H = Σ_z h_z` with each `h_z` supported
   in a radius-`r` ball around `z`,
2. an upper bound `J ≥ sup_z ‖h_z‖_op`.

It outputs the lightcone bound

```text
    ‖ [α_t(O_x), O_y] ‖_op  ≤  2 ‖O_x‖ ‖O_y‖ · exp(- d(x,y) + v_LR |t|)    (13)
```

with `v_LR = 2 · e · r · J`. The proof is an iterated commutator series
(parent (M2) Step 2 eqs. (8), (10)) and is purely combinatorial; it
does not use any further structural input beyond `r` and `J`.

Conditionally substituting the leading action-support radius
`r_action <= 2` and `J ≤ J_max` from F2 into the standard HK/NS bound:

```text
    v_LR  ≤  2 · e · 2 · J_max  =  4 · e · (|m| + 78)                      (14)
```

on the supplied diagonal-surface branch, and the reading-independent
ceiling from the F2b envelope

```text
    v_LR  ≤  4 · e · (|m| + 80)                                            (14b)
```

For massless / small-mass surfaces (`|m| -> 0` continuum limit) this
gives `v_LR ≤ 312 · e ≈ 848.10` (supplied surface), `≤ 314 · e ≈ 853.54`
(displayed carrier), `≤ 320 · e ≈ 869.85` (envelope ceiling) in lattice
units, which converts to the
emergent speed of light `c` via the lattice-spacing ratio
`v_LR · a_s / a_τ → c < ∞` (parent (M3); see also
`docs/EMERGENT_LORENTZ_INVARIANCE_NOTE.md` for the fixed-slope limit).

This proves the conditional velocity statement (F3). ∎

## Hypothesis set used

The proof uses:

- **Lattice / Quantum baseline** ([`MINIMAL_AXIOMS_2026-06-05`](MINIMAL_AXIOMS_2026-06-05.md))
  with the parent RP transfer-block convention — the one-qubit local algebra
  and lattice graph distance used for per-site operator-norm bounds (`|m|`,
  `n̂_z`) and support radius.
- **Parent RP note action carriers** (`AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md`,
  eqs. (1)–(2)) — explicit form of `M_KS`, `M_W`, `m·I`, plaquette
  action. Used for finite-range link-support of `h_z` and for the
  coefficient values `(1/2, r_W, m, β, N_c)`.
- **Hopping bilinear note** (`HOPPING_BILINEAR_HERMITICITY_THEOREM_NOTE_2026-05-02.md`,
  Statements B2 & B4) — translation-invariant Hermitian Hamiltonian
  built from NN hopping bilinears is a valid framework Hamiltonian.
- **Symmetric-canonical Wilson form** (`STAGGERED_WILSON_DET_POSITIVITY_BRIDGE_THEOREM_NOTE_2026-05-05.md`,
  Setup §) — `M_W = r_W · d · I`, providing the Wilson diagonal value
  of the (F2) supplied-surface branch only. After the (F2b)
  carrier-faithful bracket this citation is not load-bearing for the
  finiteness of the budget or for the (14b) envelope ceiling.
- **SU(3) link unitarity** — `‖U_μ‖_op = 1` always, since
  `U_μ ∈ SU(3)`. Pure group-theoretic fact; no input from physics.
- **Hastings-Koma / Nachtergaele-Sims combinatorial estimate** —
  takes `r, J` as input and outputs `v_LR = 2erJ`. This is a
  pure-mathematics theorem (Lieb-Robinson 1972 §III, Nachtergaele-Sims
  2010 §3-4); no further physics input.

No fitted parameters. No observed values. The repair only makes the
Wilson-surface normalization already present in the parent action
carriers explicit; it is not a new numerical import or a retained-status
claim. F1 and F2 are derived from action coefficients, not inferred from
RP/spectrum positivity; the exact finite-range/quasilocal property of
the reconstructed logarithmic Hamiltonian is not derived here.

## Corollaries

C1. **Narrows the parent (M2) gap.** The parent gap is no longer an
undifferentiated missing bridge: action-density radius and the
coefficient/norm budget are explicit. The remaining missing step is the
exact non-perturbative finite-range/quasilocal control of
`H = -log(T)/a_tau`.

C2. **Explicit conditional numerical v_LR.** On the canonical surface
(`d = 4, r_W = 1, β = 6, N_c = 3, m_phys`), the action-density bound
gives `v_LR ≤ 4·e·(|m_phys| + 78) ≈ 312·e ≈ 848.10` lattice units for
`|m_phys| -> 0` on the supplied diagonal Wilson surface, and the
reading-independent F2b envelope `v_LR ≤ 4·e·(|m_phys| + 80) ≈ 320·e ≈
869.85`, conditional on an exact-H locality bridge preserving
the leading `r_action <= 2` support radius.

C3. **Compatibility with cluster-decomposition note.** The companion
cluster-decomposition note uses the same `v_LR = 2 e J Z_lat R_int`
form (its eq. (1)) with `R_int = 1`, `Z_lat = 2d`. This bridge note's
`J_max` is compatible with that form as bounded support context; it is
not a load-bearing dependency of the present action-support result.

C4. **Higher-order Trotter / BCH corrections.** The leading-order
bounded action-support structure receives BCH corrections of order
`a_τ · J_max ≈ a_τ · 78` (`a_τ · 80` on the F2b envelope). For
sufficiently small `a_τ` (the canonical
fine-temporal-lattice surface), these corrections are exponentially
suppressed and preserve the lightcone structure. A separate fully
non-perturbative bound on the BCH corrections is recorded as the
open frontier of this note.

## Honest status

**Bounded support theorem on the symmetric-canonical action-density
surface.** Statements (F1)–(F3) are derived from:

- Lattice / Quantum baseline (algebraic core; legacy parent `A1`/`A2`
  labels only);
- the canonical action coefficients in parent RP note eqs. (1)–(2);
- the `r_W · d · I` symmetric-canonical Wilson form (cited bridge;
  supplied-surface branch (F2)/(12) only — the (F2b) carrier branch
  and the (14b) envelope bound the displayed standard Wilson term
  without it);
- SU(3) link unitarity;
- the Hastings-Koma / Nachtergaele-Sims combinatorial Lieb-Robinson
  estimate (admitted-context as a pure-math theorem).

The runner verifies (F1) on a toy nearest-neighbor action-density
carrier; (F2) by constructing a local block with random SU(3) gauge
backgrounds and comparing `‖h_z‖_op` against the conservative
`J_max`; (F2b) by checking the unit pair norm
`‖[[0, U], [U†, 0]]‖_op = 1` on random SU(3) links and the grouped
spatial-Wilson block norm against the `d_s · (r_W + r_W/2)` budget on
explicit one-particle matrices, then the exact branch arithmetic
`78 ≤ 78.5 ≤ 80`; (F3/F4) by checking the standard LR bound on a
finite-range toy Hamiltonian. It does not construct the exact RP
logarithm.

**What this rules out.**

- Treating the action-density support/J budget as unknown or spectral.
  Those pieces are now explicit and gauge-background-independent.

**Not in scope.**

- A non-perturbative finite-range or quasilocal bound for the exact
  reconstructed `H = -log(T)/a_tau`. This remains the parent bridge
  gate.
- A rigorous Lorentz-continuum extrapolation. Parent (M3) handles
  this via the cited emergent-Lorentz authorities, which remain
  audit-pending.
- Promotion of the parent note to retained on the canonical paper
  package.

## Citations

- minimal axioms: [`MINIMAL_AXIOMS_2026-06-05`](MINIMAL_AXIOMS_2026-06-05.md)
- parent microcausality note (context only, not a load-bearing input):
  `AXIOM_FIRST_MICROCAUSALITY_LIEB_ROBINSON_THEOREM_NOTE_2026-05-01.md`
- parent RP note (action carriers):
  [`AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md`](AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md)
- companion cluster-decomposition note (compatibility context only):
  `AXIOM_FIRST_CLUSTER_DECOMPOSITION_THEOREM_NOTE_2026-04-29.md`
- hopping bilinear note (B2, B4 used for translation-invariant link-family Hamiltonian):
  [`HOPPING_BILINEAR_HERMITICITY_THEOREM_NOTE_2026-05-02.md`](HOPPING_BILINEAR_HERMITICITY_THEOREM_NOTE_2026-05-02.md)
- symmetric-canonical Wilson surface:
  [`STAGGERED_WILSON_DET_POSITIVITY_BRIDGE_THEOREM_NOTE_2026-05-05.md`](STAGGERED_WILSON_DET_POSITIVITY_BRIDGE_THEOREM_NOTE_2026-05-05.md)
- standard external proofs (theorem-grade, no numerical input):
  Lieb-Robinson 1972; Hastings-Koma 2006; Nachtergaele-Sims 2010 §3-4.

## Audit dependency repair links

This graph-bookkeeping section records the explicit dependency
chain. It does not promote this note or change the audited claim
scope.

- [axiom_first_reflection_positivity_theorem_note_2026-04-29](AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md)
- [hopping_bilinear_hermiticity_theorem_note_2026-05-02](HOPPING_BILINEAR_HERMITICITY_THEOREM_NOTE_2026-05-02.md)
- [staggered_wilson_det_positivity_bridge_theorem_note_2026-05-05](STAGGERED_WILSON_DET_POSITIVITY_BRIDGE_THEOREM_NOTE_2026-05-05.md)
