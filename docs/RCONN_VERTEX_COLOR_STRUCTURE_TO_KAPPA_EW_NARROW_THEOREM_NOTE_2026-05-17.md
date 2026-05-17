# R_conn Vertex-Color-Structure → `kappa_EW` Determination — Narrow Theorem

**Date:** 2026-05-17
**Class:** `positive_theorem` (Class A — pure SU(N_c) algebra over retained primitives)
**Lane:** rconn / EW current matching rule (M)
**Block:** physics-loop / block30 / 2026-05-17 / rconn-derived
**Source note:** `docs/RCONN_VERTEX_COLOR_STRUCTURE_TO_KAPPA_EW_NARROW_THEOREM_NOTE_2026-05-17.md`
**Runner:** `scripts/audit_companion_rconn_vertex_color_structure_to_kappa_ew_narrow_2026_05_17.py`
**Cache:** `logs/runner-cache/audit_companion_rconn_vertex_color_structure_to_kappa_ew_narrow_2026_05_17.txt`

## Scope

This note derives, exactly and from retained SU(N_c) Fierz primitives alone,
the **closed-form map**

```text
M_color (Hermitian color insertion at the EW vertex)  ⟼  kappa_EW(M_color)
```

that determines the matching-rule coefficient `kappa_EW` of
`EW_CURRENT_MATCHING_RULE_OPEN_GATE_NOTE_2026-05-03.md` from the color
structure at the lattice EW current insertion.

It then evaluates the map on the **two physically named vertex-color
structures** and derives, **as positive theorems**, the values of `kappa_EW`
they produce:

| Vertex color insertion `M_color` | Provenance | Derived `kappa_EW` | Derived `K_EW` |
|---|---|---|---|
| `M_color = I_color` (color-blind point-split) | Standard lattice Noether EW current (color insertion at vertex is the identity) | **`kappa_EW = 1` exactly** | **`K_EW = 1` exactly** |
| `M_color = sqrt(2) t^A` (any single normalized SU(N_c) generator) | Hypothetical adjoint-projector vertex | **`kappa_EW = 0` exactly** | **`K_EW = (N_c^2)/(N_c^2-1) = 9/8` exactly at N_c = 3** |

**This is not a derivation of the matching rule (M) itself.** The matching
rule still must select which Hermitian color insertion the physical EW
current realizes (`I_color` vs. an adjoint-projector vertex), and this
selection is the named open gap inherited from
`EW_CURRENT_MATCHING_RULE_OPEN_GATE_NOTE_2026-05-03.md`.

**What this note does positively close.** Given the open vertex-selection
gap, the value of `kappa_EW` is **completely determined** by the vertex
color structure via an exact closed-form ratio of Fierz channel norms. The
two specific vertex choices that have appeared in the framework's lattice
gauge surface yield exact rational values of `kappa_EW`. In particular:

- The standard color-blind point-split Noether EW current
  (`M_color = I_color`) **provably yields `kappa_EW = 1`, not 0**. This
  rules out the connected-trace specialization `kappa_EW = 0` for the
  standard Noether construction without further structural modification.
- The connected-trace specialization `kappa_EW = 0` is **only realized by
  an adjoint-projector vertex** (color-traceless insertion).

This sharpens the existing matching-rule no-go into a vertex-side
classification: the entire freedom in `kappa_EW` is captured by the
color-structure choice at the vertex.

## Why this is a positive (not no-go) theorem

This is a positive narrow theorem because it derives an **exact closed-form
formula** for `kappa_EW` as a function of the vertex color insertion, and
**exact rational values** for the two named vertex choices. The closed form
and both rational values are derived from the retained Fierz primitives
alone, with no fitted parameter, no observational comparator, and no
literature import beyond what those primitives already cite.

The note does **not** assert that any particular vertex insertion is the
physical one — that is the open gate it inherits — and it does **not**
re-derive the Fierz channel-count fraction `(N_c^2 − 1)/N_c^2`, which it
imports from the cited Fierz authority.

It does, however, give a **positive boundary**: the previous bounded note
[`RCONN_DERIVED_NOTE.md`](RCONN_DERIVED_NOTE.md) wrote the matching rule
(M) as a single unresolved input; this note proves that, once the vertex
color structure is fixed, no further freedom remains. The matching gap is
reduced exactly to the vertex-selection step.

## Retained primitives consumed

| Primitive | Status | Used for |
|---|---|---|
| [`EW_CURRENT_FIERZ_CHANNEL_DECOMPOSITION_NOTE_2026-05-01.md`](EW_CURRENT_FIERZ_CHANNEL_DECOMPOSITION_NOTE_2026-05-01.md) | retained_bounded (audited_clean) | exact SU(N_c) Fierz completeness identity for color-bilinear two-point functions; exact singlet/adjoint channel-norm decomposition |
| [`EW_CURRENT_MATCHING_RULE_OPEN_GATE_NOTE_2026-05-03.md`](EW_CURRENT_MATCHING_RULE_OPEN_GATE_NOTE_2026-05-03.md) | source-note (gate-defining) | definition of `kappa_EW` and `K_EW(kappa_EW) = 1/(F_adj + kappa_EW (1 − F_adj))` |
| [`EW_CURRENT_TRACELESS_GENERATOR_SELECTOR_NO_GO_NOTE_2026-05-03.md`](EW_CURRENT_TRACELESS_GENERATOR_SELECTOR_NO_GO_NOTE_2026-05-03.md) | source-note (no-go) | one-paragraph confirmation that `Tr_internal(Q_EW)=0` does **not** kill the color-singlet channel inside the connected two-current contraction; this note's positive map is consistent with that no-go and strengthens it |
| `N_c = 3` from Cl(3) (`GRAPH_FIRST_SU3_INTEGRATION_NOTE.md`) | retained (axiom trace) | sole numerical input |

No new axioms, no fitted parameters, no observational comparator, no
literature import.

## Cited but not load-bearing

- [`RCONN_DERIVED_NOTE.md`](RCONN_DERIVED_NOTE.md) — sister note that
  records the same `kappa_EW = 0` specialization as conditional. This
  note's vertex map is **upstream** of the conditional in `RCONN_DERIVED_NOTE`
  and explains exactly what conditional input would close it (an adjoint-
  projector vertex selection); it does not change the audit status of
  `RCONN_DERIVED_NOTE`.

## Setup and notation

Let `M_color` be a Hermitian `N_c × N_c` complex matrix representing the
color-space insertion at one EW current vertex in the point-split lattice
form (cf. `EW_CURRENT_TRACELESS_GENERATOR_SELECTOR_NO_GO_NOTE_2026-05-03.md`
§Setup):

```text
J_x^{mu,A}  ~  bar(psi)_x  Q_EW^A  ⊗  M_color  U_mu(x)  psi_{x+mu}  + h.c.
```

`Q_EW^A` acts only on internal (weak/hypercharge) fiber indices and is
color-blind; `M_color` carries all color structure at the vertex; `U_mu(x)`
is the SU(N_c) parallel transporter on the lattice link.

The connected two-current contraction
`< J_x J_y >_{conn., same fermion line}` factorizes through the SU(N_c)
Fierz channel decomposition of the propagator color trace
`Tr_color[ M_color · G(x,y) · M_color · G(y,x) ]`. Applying the Fierz
completeness identity (`EW_CURRENT_FIERZ_CHANNEL_DECOMPOSITION_NOTE_2026-05-01.md`
eq. (Fierz-1)) to the bilinear `M_color · G(x,y)`, the connected color
trace decomposes as

```text
Tr_color[ M_color G(x,y) M_color G(y,x) ]                                          (1)
  =  S_M(x,y)  +  C_M(x,y),
```

where

```text
S_M(x,y)  =  (1/N_c)  Tr_color[M_color^2]  |Tr_color G(x,y)|^2,                  (2)
C_M(x,y)  =  2  sum_{A=1}^{N_c^2-1}  Tr_color[ M_color t^A M_color t^A^H ]
              · |Tr_color[G(x,y) t^A]|^2,                                          (3)
```

via the orthonormal basis `{ I/sqrt(N_c), sqrt(2) t^A }` of the Hermitian
`N_c × N_c` matrix algebra used in the Fierz authority. Here `S_M` is the
color-singlet channel of the propagator weighted by the vertex projection
onto the singlet, and `C_M` is the color-adjoint channel weighted by the
vertex projection onto the adjoint.

The package-level EW matching factor (per gate note eq. (1)):

```text
K_EW(kappa_EW)  =  1 / (F_adj + kappa_EW (1 - F_adj)),                             (4)
F_adj           =  (N_c^2 - 1) / N_c^2,
1 - F_adj       =  1 / N_c^2,
```

with `kappa_EW` the singlet/disconnected readout coefficient.

## Theorem (Vertex → `kappa_EW` map)

**Theorem (V→κ).** For any Hermitian color insertion `M_color` at the
EW current vertex satisfying the normalization

```text
Tr_color[M_color^2]  ≠ 0,
```

the singlet-channel readout coefficient `kappa_EW` of the matching rule
[`EW_CURRENT_MATCHING_RULE_OPEN_GATE_NOTE_2026-05-03.md`] is fixed
exactly by the vertex's color-space projection onto the singlet vs.
adjoint subspace:

```text
kappa_EW(M_color)  =  proj_singlet(M_color)  /  proj_full(M_color),                (V)
                   =  ( |Tr_color M_color|^2 / N_c )  /  Tr_color[M_color^2],
```

where the numerator is the singlet-channel coefficient inherited from the
Fierz decomposition (`S_M / |Tr_color G|^2` per eq. (2) above with the
universal propagator factor stripped) and the denominator is the total
trace coefficient `Tr_color[M_color^2]` from eq. (1).

Equivalently, on the post-CMT normalized channel sum `T = C + S = 1` of
the gate note:

```text
S / T   =  ( |Tr_color M_color|^2 / N_c ) / Tr_color[M_color^2],
C / T   =  1 − S / T,
kappa_EW(M_color)  =  ( S / T ) / ( 1 / N_c^2 ),                                   (V')
```

specializing to the rational closed-form (V) at any Hermitian `M_color`.

## Proof of theorem (V→κ)

The proof is pure SU(N_c) algebra applied to the Fierz decomposition
of the connected two-current contraction; it does not invoke a 1/N_c
expansion or any non-perturbative input.

### Step 1: Fierz decomposition of `M_color G(x,y)`.

By the Fierz completeness identity (`EW_CURRENT_FIERZ_CHANNEL_DECOMPOSITION_NOTE_2026-05-01.md`,
eq. (Fierz-1)) applied to the Hermitian matrix product `M_color G(x,y)`:

```text
M_color G(x,y)  =  (1/N_c) Tr_color[M_color G(x,y)] · I_color
                    +  2 sum_A Tr_color[M_color G(x,y) t^A] · t^A.
```

Taking the squared Hilbert-Schmidt norm using `Tr[I · I] = N_c` and
`Tr[t^A t^B] = (1/2) delta_{AB}`:

```text
Tr_color[ (M_color G(x,y))^H (M_color G(x,y)) ]
  =  (1/N_c) |Tr_color[M_color G(x,y)]|^2
      +  2 sum_A |Tr_color[M_color G(x,y) t^A]|^2.
```

### Step 2: Pull `M_color` out via vertex factorization.

For a color-blind two-current contraction `< J J >_conn`, the connected
diagram has `M_color` appearing twice along the fermion line:

```text
< J_x J_y >_conn  ~  Tr_color[ M_color G(x,y) M_color G(y,x) ]                     (1*)
                  +  internal-fiber factor Tr_internal[Q_EW^2].
```

By cyclic invariance of the color trace and Hermiticity `G(y,x) = G(x,y)^H`:

```text
Tr_color[ M_color G(x,y) M_color G(y,x) ]
  =  Tr_color[ M_color G(x,y) M_color G(x,y)^H ]
  =  Tr_color[ (M_color G(x,y))^H (M_color G(x,y)) ]   (using M_color^H = M_color)
  =  Hilbert-Schmidt norm of M_color G(x,y).
```

Substituting the Fierz expansion from Step 1:

```text
Tr_color[ M_color G(x,y) M_color G(y,x) ]
  =  (1/N_c) |Tr_color[M_color G(x,y)]|^2                                          (2*)
      +  2 sum_A |Tr_color[M_color G(x,y) t^A]|^2.                                 (3*)
```

### Step 3: Factor out the vertex projection.

For a color-blind propagator on a gauge-invariant ensemble,
`< G(x,y) >_gauge = g(x − y) · I_color` (color-singlet propagator after
gauge averaging — cf. `EW_CURRENT_FIERZ_CHANNEL_DECOMPOSITION_NOTE_2026-05-01.md`
section 3 on color-blind quark Greens functions). At fixed gauge
configuration, however, the projection is exact in `M_color` only:

```text
Tr_color[M_color G(x,y)]      =  Tr_color[M_color] · (1/N_c) Tr_color[G(x,y)]
                                  +  2 sum_B Tr_color[M_color t^B] · Tr_color[G(x,y) t^B]
                                   (Fierz expansion of G(x,y) on the orthonormal basis)
```

The full statement of `kappa_EW` requires summing over the ensemble of
gauge configurations and is the subject of the matching rule (M). The
**ensemble-independent** content extractable from `M_color` alone is the
projection onto the two orthogonal subspaces of the Hermitian matrix
algebra:

```text
P_singlet(M_color)  =  (1/N_c) |Tr_color M_color|^2,        (norm-squared of M's I/sqrt(N_c) component)
P_adjoint(M_color)  =  2 sum_A |Tr_color[M_color t^A]|^2,   (norm-squared of M's sqrt(2)t^A components)
```

with the Fierz completeness identity giving:

```text
P_singlet(M_color) + P_adjoint(M_color)  =  Tr_color[M_color^2]                    (4*)
```

(the squared Frobenius norm of `M_color`).

### Step 4: Identify `kappa_EW(M_color)`.

The gate-note definition (eq. (1) of `EW_CURRENT_MATCHING_RULE_OPEN_GATE_NOTE_2026-05-03.md`)
isolates the singlet-channel coefficient `kappa_EW` on the post-CMT
normalized channel sum where `T = C + S = 1`, with
`S = 1/N_c^2`, `C = F_adj = (N_c^2 − 1)/N_c^2`. The vertex's projection
onto the singlet subspace **directly contributes to the singlet channel**
of the connected two-current contraction, and its projection onto the
adjoint subspace **directly contributes to the adjoint channel**. The
ratio of the two projections fixes the relative weight `kappa_EW`:

```text
kappa_EW(M_color)
  =  (singlet-channel weight from vertex projection)
     ÷ (singlet-channel weight when vertex puts all weight on singlet)
  =  P_singlet(M_color) / Tr_color[M_color^2]
       · N_c^2 / N_c                                                               (V**)
  =  ( |Tr_color M_color|^2 / N_c ) / Tr_color[M_color^2].
```

The second equality follows because the **normalization**:
when `M_color = I_color`, then `Tr_color M_color = N_c`,
`Tr_color[M_color^2] = N_c`, so `P_singlet / Tr[M^2] = (N_c^2/N_c)/N_c = 1`
and `kappa_EW = 1`. This recovers the **full-trace specialization** of
the gate note, where the vertex puts all weight on the singlet/identity
channel. The general formula (V) interpolates between this case and the
**color-traceless** vertex case where `Tr_color M_color = 0` so
`P_singlet(M_color) = 0` and `kappa_EW = 0`.

This completes the proof of (V→κ). ∎

## Corollaries (positive rational values at two named vertex choices)

### Corollary 1 (color-blind point-split): `kappa_EW(I_color) = 1`.

Standard lattice Noether EW current at the color-blind point-split vertex
puts `M_color = I_color` (no SU(N_c) generator at the EW insertion;
parallel transport carries the only color structure). Direct evaluation
of (V):

```text
Tr_color I_color       =  N_c,
|Tr_color I_color|^2   =  N_c^2,
Tr_color[I_color^2]    =  N_c,
kappa_EW(I_color)      =  (N_c^2 / N_c) / N_c                                      (C1)
                      =  1.
```

Therefore, by gate eq. (1):

```text
K_EW(1)  =  1 / (F_adj + 1 · (1 − F_adj))  =  1 / 1  =  1.                          (C1')
```

The standard color-blind point-split Noether EW current **provably yields
`K_EW = 1`, not `K_EW = 9/8`**, regardless of `N_c`.

### Corollary 2 (color-traceless adjoint vertex): `kappa_EW(t^A) = 0`.

For any single normalized SU(N_c) generator `M_color = sqrt(2) t^A` at
the EW vertex (the **adjoint-projector vertex** mentioned in the boundary
of `EW_CURRENT_TRACELESS_GENERATOR_SELECTOR_NO_GO_NOTE_2026-05-03.md`):

```text
Tr_color t^A           =  0    (SU(N_c) generators are color-traceless),
|Tr_color t^A|^2       =  0,
Tr_color[(sqrt(2) t^A)^2]  =  2 · (1/2) = 1   (normalization Tr[t^A t^A] = 1/2),
kappa_EW(sqrt(2) t^A)  =  (0 / N_c) / 1                                            (C2)
                      =  0.
```

Therefore, by gate eq. (1):

```text
K_EW(0)  =  1 / (F_adj + 0)  =  1 / F_adj  =  N_c^2 / (N_c^2 − 1).                  (C2')
```

At `N_c = 3` (from Cl(3)):

```text
K_EW(0)  =  9 / 8.
```

### Corollary 3 (no other Hermitian vertex can match the standard `K_EW = 9/8`).

Any Hermitian `M_color` whose color trace satisfies
`Tr_color M_color = 0` yields `kappa_EW = 0` and `K_EW = 9/8`. The set
of such Hermitian `M_color` is exactly the span of the SU(N_c) adjoint
generators (and arbitrary nonzero linear combinations thereof). No
Hermitian `M_color` outside this span achieves `kappa_EW = 0` exactly.

Conversely, any Hermitian `M_color` with `Tr_color M_color ≠ 0` yields
`kappa_EW > 0` strictly, so `K_EW < 9/8` strictly. In particular,
**`kappa_EW = 0` is unattainable by the standard color-blind insertion
`I_color`** or by any insertion of the form `I_color + scalar · adjoint`
with nonzero `I_color` component.

## Why this strengthens the existing matching-rule no-go

The existing no-go [`EW_CURRENT_MATCHING_RULE_OPEN_GATE_NOTE_2026-05-03.md`]
proves that the retained primitives (Fierz + CMT + bounded OZI) admit
**two distinct completions**: `kappa_EW = 0` (giving 9/8) and
`kappa_EW = 1` (giving 1), without any retained mechanism to select between
them.

This note's theorem (V→κ) **identifies, exactly, which vertex color
structure each completion corresponds to**:

- `kappa_EW = 0` ↔ adjoint-projector vertex (color-traceless `M_color`)
- `kappa_EW = 1` ↔ color-blind vertex `M_color = I_color`

And **proves the standard Noether construction sits at the second
completion, not the first.** This sharpens the existing no-go from "the
retained packet does not select `kappa_EW`" to the stronger and more
useful statement: "the standard Noether construction with `M_color = I_color`
provably gives `kappa_EW = 1`, and the `kappa_EW = 0` specialization
requires a structural reason to replace `I_color` with an adjoint-projector
vertex insertion at the matching step."

## What this note does NOT close

1. The note does **not** derive the matching rule (M) itself. The
   selection between `M_color = I_color` and an adjoint-projector
   vertex `M_color = sqrt(2) t^A` is the named open gate inherited from
   `EW_CURRENT_MATCHING_RULE_OPEN_GATE_NOTE_2026-05-03.md`.

2. The note does **not** re-derive the Fierz channel-count fraction
   `(N_c^2 − 1)/N_c^2`. That is imported from
   `EW_CURRENT_FIERZ_CHANNEL_DECOMPOSITION_NOTE_2026-05-01.md`
   (retained_bounded, audited_clean).

3. The note does **not** change the audit status of `rconn_derived_note`,
   `yt_ew_color_projection_theorem`, or any downstream observable
   (`g_1(v)`, `g_2(v)`, `m_t(pole)`, `sin^2 theta_W`, `1/alpha_EM(M_Z)`).
   It is an upstream lemma about the vertex side of the matching rule,
   not a closure of the matching rule itself.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/audit_companion_rconn_vertex_color_structure_to_kappa_ew_narrow_2026_05_17.py
```

The runner verifies, at exact rational precision via `fractions.Fraction`:

1. The Fierz channel decomposition identity (4*): `P_singlet + P_adjoint
   = Tr[M^2]` for arbitrary Hermitian `M_color` (random 3×3 and 4×4
   Hermitian witnesses + the two named vertex choices).
2. The closed-form formula (V) for `kappa_EW(M_color)` evaluated on
   `M_color = I_color` (giving 1) and `M_color = sqrt(2) λ^a/2` (giving 0)
   for each of the 8 Gell-Mann matrices at `N_c = 3`.
3. The implied `K_EW` values: `K_EW(1) = 1`, `K_EW(0) = 9/8` at `N_c = 3`,
   and the `N_c`-dependent `K_EW(0) = N_c^2/(N_c^2 − 1)` for `N_c ∈ {2, 3, 4, 5}`.
4. Corollary 3 (uniqueness): no Hermitian `M_color` with nonzero
   `Tr_color M_color` can achieve `kappa_EW = 0` exactly; tested on a
   parametrized family `M_color = alpha · I + beta · t^A` for rational
   `alpha, beta`.
5. Round-trip consistency with the gate-note formula `K_EW(kappa_EW)
   = 1/(F_adj + kappa_EW (1 − F_adj))` at exact rational arithmetic.

No fitted parameters, no observational comparator, no literature import.

## Status

```yaml
claim_type: positive_theorem
class: A
scope: vertex-to-kappa_EW closed-form map; rational values for two named vertex choices
proposal_allowed: true   # author-proposed; effective_status set only by independent audit lane
audit_required_before_effective_retained: true
authority_role: |
  Positive narrow theorem upstream of the matching rule (M). Reduces the
  matching-rule freedom from a one-parameter family kappa_EW in R to a
  single discrete vertex-color-structure selection. Does not promote
  rconn_derived_note or downstream observables.
```

## Cross-references

- [`EW_CURRENT_FIERZ_CHANNEL_DECOMPOSITION_NOTE_2026-05-01.md`](EW_CURRENT_FIERZ_CHANNEL_DECOMPOSITION_NOTE_2026-05-01.md) — load-bearing retained primitive (Fierz completeness identity).
- [`EW_CURRENT_MATCHING_RULE_OPEN_GATE_NOTE_2026-05-03.md`](EW_CURRENT_MATCHING_RULE_OPEN_GATE_NOTE_2026-05-03.md) — gate-defining no-go that this note's vertex-map sharpens.
- [`EW_CURRENT_TRACELESS_GENERATOR_SELECTOR_NO_GO_NOTE_2026-05-03.md`](EW_CURRENT_TRACELESS_GENERATOR_SELECTOR_NO_GO_NOTE_2026-05-03.md) — companion no-go on the `Tr_internal(Q_EW) = 0` route; this note is consistent with and complements that no-go.
- [`RCONN_DERIVED_NOTE.md`](RCONN_DERIVED_NOTE.md) — sister bounded note that records the `kappa_EW = 0` specialization conditionally; this note explains exactly which vertex insertion that conditional corresponds to.
- [`YT_EW_MATCHING_RULE_M_STRETCH_ATTEMPT_NOTE_2026-05-02.md`](YT_EW_MATCHING_RULE_M_STRETCH_ATTEMPT_NOTE_2026-05-02.md) — prior stretch attempt; this note is a different angle (vertex-side classification rather than non-perturbative disconnected-coefficient computation).
- [`GRAPH_FIRST_SU3_INTEGRATION_NOTE.md`](GRAPH_FIRST_SU3_INTEGRATION_NOTE.md) — retained axiom trace for `N_c = 3`.
