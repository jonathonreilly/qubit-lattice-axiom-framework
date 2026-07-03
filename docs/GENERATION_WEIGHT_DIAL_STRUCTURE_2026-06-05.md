# GENERATION_WEIGHT_DIAL_STRUCTURE — the two-sector weight is a one-parameter dial r(s)=2^(s-1) with block-count and Born endpoints

**Date:** 2026-06-05
**Claim type:** theorem
**Status authority:** independent audit lane only; effective status is
pipeline-derived after audit. This note does not set, predict, or propose an
audit outcome.
**Primary runner:** [`scripts/generation_weight_dial_structure_2026_06_05.py`](../scripts/generation_weight_dial_structure_2026_06_05.py)
(sympy; **SCORECARD 28 PASS / 0 FAIL**).
**Cached log:** [`logs/runner-cache/generation_weight_dial_structure_2026_06_05.txt`](../logs/runner-cache/generation_weight_dial_structure_2026_06_05.txt).

## Scope and honesty (read first)

This note derives the **structure of the sector-weight dial** on the two
generation isotype sectors: given the two-sector readout and the `dim^s`
weighting convention, the inter-sector amplitude ratio `r := |b|^2 / a^2` of
the C_3-equivariant circulant mass operator is the single-parameter family
`r(s) = 2^(s-1)`. Its two endpoints are the block-count and Born/dimension
measures. It does **not** derive the per-sector **position** `s` (equivalently
the physical value of `r`).
That position is a **separate, genuinely open selection**: which point on the
dial the framework sits at (e.g. `s=0 -> r=1/2 -> Q=2/3` vs `s=1 -> r=1 -> Q=1`) is
a measure/mode-count choice that Lattice, Quantum, and Record leave free — see the sibling
derivations
[`FLAVOR_DOUBLET_METRIC_DEFAULT_IS_DETR_2026-06-02`](FLAVOR_DOUBLET_METRIC_DEFAULT_IS_DETR_2026-06-02.md)
and
[`FLAVOR_EINSELECTION_2SECTOR_MODULO_KREALITY_2026-06-02`](FLAVOR_EINSELECTION_2SECTOR_MODULO_KREALITY_2026-06-02.md).
No preferred `s` is claimed or implied here. The contribution is precisely the
**dial structure**: that the two named measures discussed across the
charged-lepton lane are not two unrelated prescriptions but the two endpoints
`s in {0,1}` of one exact log-linear interpolation, with `r(s)=2^(s-1)` between
them.

## Adopted axioms (cited by name)

- **Lattice (`Z^3`, nearest-neighbour).** Supplies the three highest-weight
  (`hw=1`) generation patterns and their only relabeling symmetry, the order-3
  cyclic shift `C` with `C^3 = I` (the C_3 group acting on the generation
  carrier).
- **Quantum (qubit / `M_2(C) ~= Cl(3,0)`).** The on-site amplitude algebra is
  complex; the mass operator is a complex-linear operator on the 3-generation
  carrier, so its C_3-equivariant form has a complex off-diagonal coefficient
  `b`.
- **Record.** Given the supplied finite central-sector decomposition and fixed
  `K`/CPT conjugation, the record names only the realized `K`/CPT orbit and the
  scalar readout `I` is finitely additive over disjoint records. The adopted
  `K`/CPT-real readout condition pins the diagonal amplitude `a` real and allows
  the singlet and doublet powers to be added. Record itself supplies no readout
  context, decomposition, `K`/CPT structure, weighting, normalization,
  probability, dynamics, or occupancy rule.

The **two-sector structure** (singlet real-dim 1, doublet real-dim 2) is
**imported, not re-derived here**, from the sibling readout/metric derivations
[`RECORD_GENERATION_READOUT_TWO_SECTORS`](RECORD_GENERATION_READOUT_TWO_SECTORS_2026-06-05.md),
[`FLAVOR_DOUBLET_METRIC_DEFAULT_IS_DETR_2026-06-02`](FLAVOR_DOUBLET_METRIC_DEFAULT_IS_DETR_2026-06-02.md)
(which computes the Lattice coherent-state field-space metric `diag(3,6,6)` on
`(a, Re b, Im b)` and isolates the doublet mode-count) and
[`FLAVOR_EINSELECTION_2SECTOR_MODULO_KREALITY_2026-06-02`](FLAVOR_EINSELECTION_2SECTOR_MODULO_KREALITY_2026-06-02.md)
(which einselects the two real-irreducible blocks: singlet `P_0` rank 1,
doublet `P_1` rank 2). The parent open-gate row
`CHARGED_LEPTON_KOIDE_NOTE_2026-04-18` (backticked non-load-bearing context
reference; open-gate admission surface preserved, not consumed)
is preserved.

## Theorem (`GENERATION_WEIGHT_DIAL_STRUCTURE`)

Let `Y` be the C_3-equivariant mass operator on the 3-generation carrier, with
singlet sector (trivial character, real-dim 1) carrying spectral power `a^2` and
doublet sector (two faithful characters, real-dim 2) carrying spectral power
`2|b|^2`. Define the **sector-weight dial** by weighting each block's power by
`dim^s` and imposing the balance

```text
singlet_power : doublet_power  =  dim_singlet^s : dim_doublet^s  =  1^s : 2^s.
```

Then the inter-sector amplitude ratio `r := |b|^2 / a^2` is the
**one-parameter family**

```text
            r(s) = 2^(s-1),
```

with:

1. **endpoint `s = 0`** (equal spectral power **per block**, weights `(1,1)` —
   the **block-count / det_C** measure): `r(0) = 1/2`  (`⇒ κ = a^2/|b|^2 = 2`);
2. **endpoint `s = 1`** (equal spectral power **per real mode**, weights
   `(1,2)` = the real dimensions — the **Born / dimension / det_R** measure):
   `r(1) = 1`  (`⇒ κ = a^2/|b|^2 = 1`);
3. `r(s) = 2^(s-1)` is **strictly increasing** (`dr/ds = 2^(s-1) ln 2 > 0`) and
   **log-linear** (`log_2 r(s) = s - 1`); over `s in [0,1]` it sweeps exactly
   `[1/2, 1]`, so the two canonical measures are precisely its two endpoints,
   with a continuum of intermediate weightings in between.

**Out of scope (separate, open):** the value of `s` itself (the per-sector
position on the dial) is not fixed by Lattice, Quantum, or Record.

## Proof

### Step 1 — C_3-equivariance ⇒ circulant `Y = aI + bC + conj(b)C^2`
The only relabeling symmetry of the three `hw=1` generation patterns is the
order-3 shift `C` (Lattice), with `C^3 = I` and `C^2 = C^T = C^{-1}` (the C_3 group is
realized faithfully). By Schur's lemma for the abelian group C_3, the commutant
of `⟨C⟩` is exactly the algebra of **circulants** (the runner solves
`[M, C] = 0` and finds the general solution is a circulant fixed by its first
column: 3 free complex parameters). Imposing Hermiticity forces the `C^2`
coefficient to be the conjugate of the `C` coefficient; the adopted
`K`/CPT-real readout condition fixes the diagonal `a` real. Hence

```text
Y = a·I + b·C + conj(b)·C^2,   a ∈ R,  b ∈ C,
```

which is Hermitian and satisfies `[Y, C] = 0` (both verified symbolically).
*(Runner: S1.1–S1.5.)*

### Step 2 — isotype powers: singlet `a^2`, doublet `2|b|^2`
The C_3 Fourier vectors `f_j = (1, w^j, w^{2j})` (with `w = e^{2πi/3}`)
diagonalize `Y`. Because the shift acts as `C f_j = w^{−j} f_j`, the eigenvalue
on character `j` is `λ_j = a + b·w^{−j} + conj(b)·w^{−2j}`; in particular the
**singlet** eigenvalue is `λ_0 = a + b + conj(b) = a + 2 Re b` (the trivial
character reads the row-sum). *(Runner: S2.1–S2.2; all eigenvector residuals are
exactly zero.)*

The **sector power** is the spectral power carried in each C_3 isotype, read off
the group-algebra coordinates of `Y` in the Hilbert–Schmidt-orthonormal basis
`{I/√3, C/√3, C^2/√3}` of `M_3(C)^{C_3}`. HS-projection confirms the coordinates
are `(coord I, coord C, coord C^2) = (a, b, conj b)`. Therefore:

- the **trivial character (singlet)** is carried by the `I`-coordinate ⇒
  **singlet power = `|a|^2 = a^2`**;
- the **two faithful characters (doublet)** are carried by the `C, C^2`
  coordinates ⇒ **doublet power = `|b|^2 + |conj b|^2 = 2|b|^2`**.

This is consistent with the full spectrum by Parseval:
`||Y||_HS^2 = Tr(Y^H Y) = Σ_j |λ_j|^2 = 3a^2 + 6|b|^2 = 3·(a^2) + 3·(2|b|^2)`.
*(Runner: S2.2b–S2.5b.)*

### Step 3 — the `dim^s` balance and the closed form
With `dim_singlet = 1`, `dim_doublet = 2` (the imported two-sector structure),
weight each block's power by `dim^s` and balance:

```text
a^2 · 2^s  =  (2|b|^2) · 1^s          (i.e. singlet_power·dim_doublet^s = doublet_power·dim_singlet^s).
```

Dividing by `a^2 > 0` gives `2^s = 2r`, hence

```text
r(s) = |b|^2/a^2 = 2^s / 2 = 2^(s-1).
```

The runner both solves the balance for the unique positive root and verifies the
closed form `r(s) = 2^(s-1)` matches exactly, plus the independent one-line
re-derivation `2^s = 2r => r = 2^(s-1)`. *(Runner: S3.0-S3.4.)*

### Step 4 — the two endpoints are the two canonical measures
- `s = 0`: weights `(1^0, 2^0) = (1,1)` — count each block once. Balance is
  `a^2 = 2|b|^2`, so `r(0) = 1/2` and `κ = a^2/|b|^2 = 2`. This is the
  **block-count / det_C** measure (the doublet counted as **one complex mode**).
- `s = 1`: weights `(1^1, 2^1) = (1,2)` — the real dimensions. Balance is
  `2a^2 = 2|b|^2`, so `|b|^2 = a^2`, `r(1) = 1`, `κ = 1`. This is the
  **Born / dimension / det_R** measure (the doublet counted as **two real
  modes**). *(Runner: S4.1–S4.6.)*

### Step 5 — monotonicity ⇒ the endpoints bracket the dial
`dr/ds = 2^(s-1) ln 2 > 0` for all real `s` (strictly increasing); equivalently
`log_2 r(s) = s - 1` is exactly linear. Hence `r(0) = 1/2 < r(1) = 1` are
distinct and ordered, and over `s in [0,1]` the dial sweeps exactly `[1/2, 1]`:
the two canonical measures are precisely its two endpoints, with the interior
`s in (0,1)` a continuum of intermediate (non-canonical) weightings. Finite
additivity of the Record readout allows the singlet and doublet powers to be
summed (`total = singlet_power + doublet_power = a^2 + 2|b|^2`), while the
per-block (`s=0`) and per-mode (`s=1`) normalizations remain separate weighting
conventions. *(Runner: S5.1-S5.5.)*

∎ (28/28 symbolic checks; see cached log.)

## What this is and is NOT

- **IS:** an exact, sympy-verified derivation that the singlet/doublet
  sector-weight is the one-parameter dial `r(s) = 2^(s-1)`, log-linear and
  strictly monotone, whose two endpoints are *exactly* the block-count
  (`r=1/2`) and Born/dimension (`r=1`) measures — i.e. the two measures debated
  across the charged-lepton lane are the `s=0` and `s=1` ends of one structure.
- **IS NOT:** a determination of the position `s` (the physical `r`). The
  per-sector position is a separate, open selection; this note adds the
  structural fact that the selection lives on a single monotone dial bracketed
  by the two canonical measures, not a derivation of where on it the framework
  sits. No "retained"/closure language is used or implied.

## Relation to the lane (no new imports)

The endpoints and their measure-theoretic identities (`det_C` block-count vs
`det_R` Born/dimension; `κ = 2` vs `κ = 1`; `Q=2/3` vs `Q=1`) are the same two
poles already characterized in the sibling derivations above and in
[`CHARGED_LEPTON_KOIDE_TWO_GATE_TIER_A_BOUNDED_THEOREM_NOTE_2026-06-02`](CHARGED_LEPTON_KOIDE_TWO_GATE_TIER_A_BOUNDED_THEOREM_NOTE_2026-06-02.md)
(its `c := 2r/a`, `Q := 1/3 + c^2/6` parametrization). Nothing new is imported:
the circulant form, the two-sector `(1,2)` dimensions, and the two measures all
come from cited material; the new content is purely the **dim^s interpolation**
and its closed form. The `(scale a, ratio |b|, phase δ)` circulant
parametrization and the `Q∈[1/3,1]` range are Koide's own Z_3-symmetric
parametrization (Koide–Nishiura arXiv:1301.4143) and standard Koide/Brannen
lore; the framework's contribution is the axioms-up derivation of that structure
and — here — that its two named measures are the endpoints of one monotone dial.

## Provenance / honesty notes

- Sibling/parent anchors confirmed present on `origin/main`:
  `FLAVOR_DOUBLET_METRIC_DEFAULT_IS_DETR_2026-06-02`,
  `FLAVOR_EINSELECTION_2SECTOR_MODULO_KREALITY_2026-06-02`,
  `CHARGED_LEPTON_KOIDE_NOTE_2026-04-18`,
  `CHARGED_LEPTON_KOIDE_TWO_GATE_TIER_A_BOUNDED_THEOREM_NOTE_2026-06-02`.
- **Non-circular:** the derivation never assumes any target value of `r` or `Q`.
  It posits the `dim^s` weighting as the definition of the dial and computes the
  consequence; the endpoints `1/2` and `1` *emerge* from `s=0,1`, they are not
  inserted.
- **All computation is symbolic (sympy):** circulant/Schur commutant, eigenvalue
  diagonalization (exact zero residuals), HS group-algebra coordinates, Parseval
  power bookkeeping, the balance equation, the closed form `2^(s-1)`, both
  endpoints, monotonicity, and log-linearity. 28 PASS / 0 FAIL.
- This is a **structure** result. Promotion/audit status is left entirely to the
  independent post-landing process; no audit-ledger action is asserted here.
