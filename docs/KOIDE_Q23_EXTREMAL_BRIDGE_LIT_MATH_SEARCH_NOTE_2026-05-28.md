# Koide Q = 2/3 Extremal-Principle Bridge — Literature & Mathematics Search

**Date:** 2026-05-28
**Type:** search report (NOT a theorem, NOT a closure, NOT a new admission)
**Status authority:** none. This is a survey/findings document produced by a
literature-and-mathematics search task. It does **not** set or predict any
audit verdict, promote any row, wire into any index, or admit any primitive.
It records what an external search found and maps it onto the already-named
open atom. Everything external is flagged as not-retained.

## 0. Purpose and scope

The task: search the external literature and the mathematics for anything that
would force the physical charged-lepton packet to sit at the Q = 2/3 extremum
of the block-total Frobenius functional, and cross-check against existing repo
content.

The headline finding is in two parts:

1. **The repo has already localized this gap more sharply than the published
   literature has.** Every external derivation of Q = 2/3 either (a) assumes a
   structure that forces it, or (b) merely reparametrizes it. None derives the
   weighting/coefficient that the repo has isolated as the single open atom. So
   no off-the-shelf import closes the bridge.

2. **The repo's open atom has a precise, standard mathematical home that the
   prior probe campaign approached but did not name in these exact terms:** the
   F1-vs-F3 weighting selection is the choice between the **central
   (normalized) trace** and the **matrix (Hilbert–Schmidt) trace** on the real
   group algebra `R[Z_3] ≅ R ⊕ C`, and the "`U(1)_b` angular convention on the
   `C_3`-doublet plane" named as the open sub-locus in
   [`BAE_F1_F3_CANONICAL_SELECTION_BOUNDED_OBSTRUCTION_NOTE_2026-05-17.md`](BAE_F1_F3_CANONICAL_SELECTION_BOUNDED_OBSTRUCTION_NOTE_2026-05-17.md)
   **is exactly the Schur commutant `C` of the Frobenius–Schur complex-type
   (`FS = 0`) doublet.** This reframes the open atom in named mathematics but
   does **not** close it; rather, it identifies precisely which extra axiom
   would close it and confirms that axiom is not in the retained inventory.

## 1. Where the repo already stands (cross-check)

The charged-lepton Koide bridge has been reduced to a single scalar primitive
across the retained surface:

```text
equal real-irrep-block power  <=>  E_+ = E_perp  <=>  a^2 = 2|b|^2
  <=>  kappa = 2  <=>  |b|^2/a^2 = 1/2  <=>  Brannen c = sqrt(2)  <=>  Q = 2/3
```

(see [`KOIDE_Q_BRIDGE_SINGLE_PRIMITIVE_NOTE_2026-04-22.md`](KOIDE_Q_BRIDGE_SINGLE_PRIMITIVE_NOTE_2026-04-22.md)).

The extremal-principle framing is retained at the algebraic level: on the
`C_3`-equivariant Hermitian circulant `H = a I + b C + b̄ C^2`, with block-total
Frobenius energies `E_+ = 3a^2` (trivial isotype) and `E_perp = 6|b|^2`
(doublet isotype), the **multiplicity-weighted log-functional**

```text
F1(H) = log E_+ + log E_perp        (weighting (1,1))
```

has its unique interior critical point (at fixed `E_+ + E_perp`) at `kappa = 2`,
i.e. exactly the Koide locus; the Hessian is strictly negative-definite (strict
maximum). This is the retained
[`BAE_BLOCK_TOTAL_FROBENIUS_DERIVATION_NARROW_THEOREM_NOTE_2026-05-16.md`](BAE_BLOCK_TOTAL_FROBENIUS_DERIVATION_NARROW_THEOREM_NOTE_2026-05-16.md)
chain (T1–T3).

The single unclosed atom is the **weighting selection**. The rank-weighted
alternative

```text
F3(H) = log E_+ + 2 log E_perp      (weighting (1,2))
```

has its interior critical point at `kappa = 1`, **not** at Koide. So the bridge
is open precisely because no retained content forces `F1` over `F3`. This is
the content of:

- [`BAE_F1_F3_CANONICAL_SELECTION_BOUNDED_OBSTRUCTION_NOTE_2026-05-17.md`](BAE_F1_F3_CANONICAL_SELECTION_BOUNDED_OBSTRUCTION_NOTE_2026-05-17.md)
  — consolidates 9 attack vectors; names the open sub-locus as the **`U(1)_b`
  angular convention on the `C_3`-doublet plane**.
- `HIGHER_ORDER_STRUCTURAL_THEOREMS_NOTE.md` Theorem 5 — no retained
  `C_3`-invariant variational principle forces the Koide cone (six candidates
  surveyed); names the candidate missing primitive as **"real-irrep-block
  democracy: one log-term per real-irrep block, independent of complex-irrep
  multiplicity."**
- [`KOIDE_A1_PROBE_PLANCHEREL_PETER_WEYL_BOUNDED_OBSTRUCTION_NOTE_2026-05-09_probe12.md`](KOIDE_A1_PROBE_PLANCHEREL_PETER_WEYL_BOUNDED_OBSTRUCTION_NOTE_2026-05-09_probe12.md)
  — Plancherel/Peter–Weyl gives the `(3:6)` real-dimension weighting (→ F3),
  not `(1,1)`.
- [`KOIDE_A1_PROBE_REAL_STRUCTURE_BOUNDED_OBSTRUCTION_NOTE_2026-05-09_probe13.md`](KOIDE_A1_PROBE_REAL_STRUCTURE_BOUNDED_OBSTRUCTION_NOTE_2026-05-09_probe13.md)
  — the retained complex conjugation `K` (the `T` factor of CPT) supplies the
  `Z_2` part of `R`-isotype counting (it glues `chi_omega` and
  `chi_omega-bar`), but **not** the `SO(2)`/`U(1)_b` angular quotient on the
  doublet that the `(1,1)` weighting needs.

So the repo's own statement of the gap is: *which trace/weighting is canonical,
and what selects the `U(1)_b` quotient on the doublet plane.*

## 2. External literature — every derivation assumes or reparametrizes

Search across the published Koide literature returns the same structural verdict
the repo reached independently: **no published mechanism derives `Q = 2/3` from
first principles; each either assumes a structure that forces it, or
reparametrizes it.** Detail by approach (all external; none retained):

| External approach | Derives 2/3? | What it actually does |
|---|---|---|
| Foot 45° geometric angle | No | Reparametrizes: `Q = 2/3` ⇔ 45° between `(√m_i)` and `(1,1,1)`. No mechanism for the angle. |
| Koide 1990 `U(3)` Higgs potential `V(Φ) = [2(trΦ)^2 − 3 tr(Φ^2)]^2` | Conditional | `V = 0` ⇔ Koide, but the `(2:−3)` Wilson-coefficient ratio is **assumed**. This is the repo's Route A, already a bounded obstruction. |
| Cubic-polynomial / symmetric-function identity | Algebraic only | Roots of a specific cubic satisfy a Koide-type ratio; assumes the cubic structure. |
| Sumino `U(3)` family gauge | Stabilizes, not derives | Cancels the **QED radiative correction** so the *pole* masses keep a tree relation; does not derive the tree `2/3`. |
| Brannen circulant `√m = μ(1 + √2 cos(δ + 2πn/3))` | No | Two-parameter reparametrization; `c = √2` (i.e. `κ = 2`) and `δ ≈ 2/9` are inputs, not outputs. |
| Koide 1981–83 preon `z`-constraints | Algebraic only | `Q = 2/3` follows once `Σz_i = 0` and `(1/3)Σz_i^2 = z_0^2` are postulated. |
| "Zero-Interaction Principle" / recent NUVO "first-principles" notes | claimed | These posit a scalar-geometry / topological-moment substrate and then read off 45°; the `45°` (equivalently the `√2`) is built into the geometry, not derived from an independent dynamical principle. Treat as not-retained, same reparametrization class. |

**Conclusion of the literature scan:** the published frontier sits at exactly
the same wall the repo isolated — the `(2:−3)` coefficient / the `√2` amplitude
/ the 45° / the `(1,1)` block democracy are all the *same* unforced datum under
different coordinates. There is **no external import** that supplies it as a
theorem. This is a genuine open problem, and the repo's localization (to the
weighting selection on `Herm_circ(3)`) is *sharper* than the published state.

## 3. The mathematics — where "real-irrep-block democracy" actually lives

This is the section with new (to the campaign) precision. It is **mathematics,
not a closure**: it reframes the open atom and pinpoints the missing axiom.

### 3.1 Frobenius–Schur classification of the `C_3` content

Over `C`, the cyclic group `Z_3` has three 1-dimensional irreps:
`χ_0 = 1`, `χ_1` (action by `ω = e^{2πi/3}`), `χ_2` (action by `ω^2 = ω̄`).
The Frobenius–Schur indicator `ν(χ) = (1/|G|) Σ_g χ(g^2)` evaluates to:

```text
ν(χ_0) = +1   (real type;    commutant = R)
ν(χ_1) =  0   (complex type; χ_1* = χ_2 ≠ χ_1)
ν(χ_2) =  0   (complex type; χ_2* = χ_1 ≠ χ_2)
```

Over `R`, `χ_1 ⊕ χ_2` realifies to a **single 2-dimensional real-irreducible
representation** `ρ_doublet` (rotation by `120°`). By Schur's lemma + the
Frobenius theorem, its endomorphism algebra (commutant) is a real division
algebra; for the complex type it is

```text
End_{R[Z_3]}(ρ_doublet) ≅ C.
```

Hence the real group algebra splits as

```text
R[Z_3] ≅ R ⊕ C,                                                       (SPLIT)
```

with **exactly two real-irreducible blocks**: the trivial block (commutant `R`)
and the doublet block (commutant `C`). This is standard, fully proved
representation theory.

### 3.2 The doublet's commutant `C` IS the open `U(1)_b`

On the circulant family `H = a I + b C + b̄ C^2`, the trivial isotype is the
`a`-axis (`E_+ = 3a^2`) and the doublet isotype is the `b`-plane
(`E_perp = 6|b|^2`). The commutant `C ≅ End_{R[Z_3]}(ρ_doublet)` acts on the
`b`-plane as `b ↦ e^{iθ} b` — i.e. it is **precisely the `U(1)_b` rotation of
the `C_3`-doublet plane** named as the open sub-locus in the F1/F3 note and as
the missing `SO(2)`-angular quotient in Probe 13.

This is the clean identification the campaign was circling:

```text
"U(1)_b angular convention on the C_3-doublet plane"
        ≡  the Schur commutant U(1) ⊂ C = End_{R[Z_3]}(complex-type doublet).
```

The retained `K` (complex conjugation / `T`) realizes the `Z_2` that swaps
`χ_1 ↔ χ_2` — i.e. complex conjugation on `End ≅ C`. What remains unselected is
the **scale/weight assigned to this `C`-block**, which is the connected `U(1)`
(equivalently `SO(2)`) part — exactly Probe 13's residue.

### 3.3 F1 vs F3 = central trace vs matrix trace on `R ⊕ C`

A finite-dimensional real `*`-algebra `R ⊕ C` carries a one-real-parameter
family of invariant traces, weighting the two blocks by `(w_R, w_C)`. Two are
canonical:

- **Matrix / Hilbert–Schmidt trace** `Tr`: weights each block by its dimension
  **over the base field `R`**, giving `(1, 2)` (the `C`-block is 2-real-dim).
  This is the Plancherel / Peter–Weyl weighting (Probe 12) and yields **`F3`**
  → `κ = 1` → **not Koide**.

- **Central / normalized trace** `τ` (the canonical tracial *state*,
  `τ(1) = 1`, equal weight on each minimal central projection / superselection
  sector): weights each block by its dimension **over its own commutant
  division algebra** (`R` over `R`, `C` over `C`, both `= 1`), giving `(1, 1)`.
  This is **`F1`** → `κ = 2` → **exactly Koide Q = 2/3**.

So the entire bridge reduces to a single, named, classical fork:

```text
Koide Q = 2/3   <=>   F1   <=>   "dimension over the commutant" weighting
                                  <=>   central tracial STATE on R[Z_3].
not-Koide       <=>   F3   <=>   "dimension over the base field R" weighting
                                  <=>   matrix trace / Plancherel measure.
```

### 3.4 What is proved vs what is conjectured

**Proved (standard mathematics, no import needed):**
- `(SPLIT)`: `R[Z_3] ≅ R ⊕ C`, two real-irreducible blocks. (Maschke + FS.)
- The doublet is FS complex-type with commutant `C`; the `C`-action is the
  `U(1)_b` of the open sub-locus.
- `F1` ⇔ central tracial state weighting `(1,1)`; `F3` ⇔ matrix-trace
  weighting `(1,2)`. Each is an extremum-defining functional; their critical
  points are `κ = 2` and `κ = 1` respectively (already in the retained chain).

**NOT proved / conjectured (this is the live gap):**
- That the *physical* charged-lepton packet must be weighted by the central
  tracial state rather than the matrix trace. **Nothing in the retained
  `A1 + A2 + Cl(3)/Z^3` inventory forces "equal weight per superselection
  sector" / "dimension over the commutant."** Selecting the central tracial
  state is a *Born/probabilistic normalization axiom* (a unital state assigning
  equal a-priori weight to orthogonal sectors), which is exactly the class of
  principle the repo's
  `BAE_MAX_ENTROPY_RETAINED_BOUNDED_OBSTRUCTION_NOTE_2026-05-10_baemaxent.md`
  found **does not** follow from retained Born-rule operationalism + physical-
  lattice baseline + Jaynes max-entropy.

So the FS / central-trace framing **does not close the bridge**. Its value is
that it (i) names the missing primitive in standard terms (central tracial
state on `R[Z_3] ≅ R ⊕ C`), (ii) explains *why* it is genuinely unforced (two
legitimate canonical traces exist; abstract algebra does not prefer one), and
(iii) confirms the campaign's Probe-12/13 residue is the connected `U(1)`
commutant scale, not an artifact.

## 4. Answers to the five search sub-questions

1. **Extremal conditions in representation theory (Schur, Frobenius
   reciprocity, characters).** The relevant theorem is the Schur/Frobenius
   reality classification (FS indicator), not Schur orthogonality of matrix
   coefficients. It *classifies* the doublet as complex-type with commutant `C`
   and thereby *names* the open `U(1)_b`, but it does **not** by itself fix the
   block weight. No extremal theorem in character theory forces `(1,1)` over
   `(1,2)`; the choice is a trace-normalization, which character theory leaves
   as a free positive scaling per block.

2. **Variational principles native to lattice gauge theory / staggered
   fermions.** None found (external or retained) that selects the Koide cone.
   Theorem 5 already surveyed six `C_3`-invariant variational principles
   (Cauchy–Schwarz midpoint, max-entropy, Legendre partition function,
   Fisher–Rao, …) — all negative. The lattice/staggered action supplies the
   Hilbert–Schmidt (matrix-trace) inner product naturally (it is the
   `Σ_x Tr(...)` measure), which is the `F3` side — i.e. the lattice's *default*
   measure points the **wrong way** (κ = 1). Forcing `F1` requires a sector-
   counting (state) normalization the bare action does not carry.

3. **Cl(3) structure constants forcing `Q = 2/3`.** No. The retained
   `CL3_PAULI_IRREP_UNIQUENESS_NARROW_THEOREM_NOTE_2026-05-10` fixes the Pauli
   realization on `M_2(C)` uniquely, and the support face
   `dim(spinor)/dim(Cl^+(3)) = 2/4 = 1/2` lands on the same primitive `P_Q =
   1/2` — but as a *coincident value*, not a forcing derivation (Route A / Route
   E / Route F all bounded-obstruction). The Clifford structure constants do not
   single out the central trace over the matrix trace; `Cl(3) ≅ M_2(C)` is a
   single simple block, so its own canonical trace is unambiguous and says
   nothing about the *two-block* `R ⊕ C` weighting that the `Z_3` flavor
   structure introduces.

4. **Trace/norm conditions from gauge symmetry.** The retained Casimir
   identities `T(T+1) − Y^2 = 1/2` (lepton doublet and Higgs, uniquely) and
   `C_2(SU(2)_L) − Y^2 = 3/4 − 1/4 = 1/2`, plus Kostant `|ρ_{A_1}|^2 = 1/2`,
   all hit the primitive value `1/2`. These are striking but remain
   convention-dependent coincidences (Route E/F bounded obstructions): there is
   no retained normalization map from the gauge Cartan–Killing form to the
   flavor block weighting, so they do not discharge the central-vs-matrix trace
   choice.

5. **`Z_3` (Koide cyclic) ↔ `Z^3` (lattice) symmetry.** The Koide `Z_3` is the
   *flavor*/generation cyclic symmetry acting on the three-slot packet; the
   lattice `Z^3` is the *spatial* translation lattice. They are not identified
   in the retained framework (Theorem-1-class no-go: `Z_3` invariance alone
   gives the triply-degenerate `I_3`, not the Koide cone). The search found no
   structural bridge that promotes spatial `Z^3` periodicity into the flavor
   `Z_3` block-democracy weighting. This remains a *distinct* `Z_3`, and
   conflating them would be an unforced identification.

## 5. Bottom line

- **The bridge is genuinely open, and the repo is at or ahead of the published
  frontier.** No literature import closes it; every external derivation assumes
  the very datum (the `(2:−3)` / `√2` / 45° / `(1,1)` democracy) that is the gap.
- **The open atom now has a clean classical name:** select the **central
  tracial state** (equal weight per real-irreducible superselection block,
  "dimension over the commutant") over the **matrix/Hilbert–Schmidt trace**
  ("dimension over `R`", = Plancherel) on `R[Z_3] ≅ R ⊕ C`. Koide `Q = 2/3`
  ⇔ central trace; not-Koide (`κ = 1`) ⇔ matrix trace.
- **The connected `U(1)_b` that Probe 13 found missing is exactly the Schur
  commutant `U(1) ⊂ C = End_{R[Z_3]}(complex-type doublet).`**
- **What would close it (and what is missing):** an axiom that the physical
  flavor measure is a *unital state assigning equal a-priori weight to
  orthogonal superselection sectors* (Born-type sector democracy). That axiom
  is **not** in the retained `A1 + A2 + Cl(3)/Z^3` inventory; `baemaxent`
  already found the Born/max-entropy route insufficient as retained content.
  So this is a precise statement of the missing primitive, **not** its
  derivation.

This document imports nothing as load-bearing, admits no primitive, promotes no
row, and is not wired into any index. It is a search report.

## References (external, not retained)

- Koide formula overview and derivation survey — en.wikipedia.org/wiki/Koide_formula
- Y. Sumino, "Family Gauge Symmetry and Koide's Mass Formula", arXiv:0812.2090;
  "…as an Origin of Koide's Mass Formula and Charged Lepton Spectrum",
  arXiv:0812.2103 / 0903.3640 (QED-correction cancellation; stabilization, not
  tree derivation).
- Koide & Nishiura, `S_3`/`U(3)` flavor Higgs quartic, hep-ph/0509214 (= repo
  Route A).
- C. Brannen, "The Lepton Masses", brannenworks.com/MASSES2.pdf (circulant
  eigenvalue / `√2` / `δ ≈ 2/9` parametrization).
- R. Foot, geometric 45° interpretation (arXiv:hep-ph/9402242, as summarized).
- Koide `Z_3`-symmetric parametrization for quarks, arXiv:1210.4125, 1301.4143
  (`δ_U ≈ 2/27`, `δ_D ≈ 4/27`).
- Frobenius–Schur indicator and real/complex/quaternionic classification —
  en.wikipedia.org/wiki/Frobenius–Schur_indicator (standard; load-bearing math
  in §3 is textbook and independently verifiable).

## Repo cross-references (retained context)

- [`KOIDE_Q_BRIDGE_SINGLE_PRIMITIVE_NOTE_2026-04-22.md`](KOIDE_Q_BRIDGE_SINGLE_PRIMITIVE_NOTE_2026-04-22.md)
- [`BAE_BLOCK_TOTAL_FROBENIUS_DERIVATION_NARROW_THEOREM_NOTE_2026-05-16.md`](BAE_BLOCK_TOTAL_FROBENIUS_DERIVATION_NARROW_THEOREM_NOTE_2026-05-16.md)
- [`BAE_F1_F3_CANONICAL_SELECTION_BOUNDED_OBSTRUCTION_NOTE_2026-05-17.md`](BAE_F1_F3_CANONICAL_SELECTION_BOUNDED_OBSTRUCTION_NOTE_2026-05-17.md)
- [`KOIDE_A1_PROBE_PLANCHEREL_PETER_WEYL_BOUNDED_OBSTRUCTION_NOTE_2026-05-09_probe12.md`](KOIDE_A1_PROBE_PLANCHEREL_PETER_WEYL_BOUNDED_OBSTRUCTION_NOTE_2026-05-09_probe12.md)
- [`KOIDE_A1_PROBE_REAL_STRUCTURE_BOUNDED_OBSTRUCTION_NOTE_2026-05-09_probe13.md`](KOIDE_A1_PROBE_REAL_STRUCTURE_BOUNDED_OBSTRUCTION_NOTE_2026-05-09_probe13.md)
- [`KOIDE_A1_DERIVATION_STATUS_NOTE.md`](KOIDE_A1_DERIVATION_STATUS_NOTE.md)
- `HIGHER_ORDER_STRUCTURAL_THEOREMS_NOTE.md` (Theorem 5: real-irrep-block democracy)
- `BAE_MAX_ENTROPY_RETAINED_BOUNDED_OBSTRUCTION_NOTE_2026-05-10_baemaxent.md`
