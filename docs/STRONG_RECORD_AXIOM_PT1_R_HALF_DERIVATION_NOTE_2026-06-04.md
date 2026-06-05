# Strong Record Axiom — Pressure-Test #1: Does it Derive the Koide r=½?

**Date:** 2026-06-04
**Claim type:** meta
**Status:** axiom-design pressure test. This note proposes no framework
theorem, adds no axiom to the framework, sets no audit verdict, and changes no
existing row. It records a finite-algebra adjudication of whether a *candidate*
axiom, taken on its own terms, derives the Brannen modulus `r = |b|²/a² = ½`
(Koide `Q = 2/3`) on the 3-generation factor. The independent audit lane sets
any audit/effective status.
**Primary runner:**
[`scripts/strong_record_axiom_pt1_r_half_derivation_2026_06_04.py`](../scripts/strong_record_axiom_pt1_r_half_derivation_2026_06_04.py)
(SCORECARD 53/53), cache
[`logs/runner-cache/strong_record_axiom_pt1_r_half_derivation_2026_06_04.txt`](../logs/runner-cache/strong_record_axiom_pt1_r_half_derivation_2026_06_04.txt).

## The candidate axiom under test

> "A record registers **which real classical alternative** is realized. The real
> classical alternatives of the local algebra are its **real superselection
> sectors** (real Wedderburn blocks); each sector is one alternative; record
> readout **counts** alternatives — additive over disjoint alternatives, and
> **dimension-blind** (one unit per real sector)."

The pressure-test frame is explicit: we judge the *statement as an axiom*, and
do **not** defer to the framework's existing "convention slot" language. The
question is whether the axiom, granted, **cleanly and uniquely** derives `r=½`.

## Verdict

**DERIVES-WITH-RESIDUAL.** The axiom uniquely selects the isotype weight `(1,1)`
over both `(1,2)` rivals, and `(1,1)` lands `r=½, Q=2/3`. But the last step from
the axiom's *count* to the Koide *value* needs one extra identification —
"record-weight per sector := Frobenius (squared-amplitude) channel energy" —
that the axiom's wording does not itself force. A different equally-natural
"one unit per real block" reading (equal bare amplitude per block) lands `r=1`.
So the axiom fixes the **count** cleanly; the **count→energy realization** is a
residual.

## The chain, verified (runner)

### 1. Real vs complex Wedderburn of `ℝ[Z₃]` (STEP 0–1)
`Z₃` acts on the 3 generations by the regular rep `g ↦ C` (3-cycle), giving the
real circulant algebra `ℝ[Z₃] = span_ℝ{I, C, C²}` (commutative, dim_ℝ 3).

- **Complex:** `C` diagonalizes over `ℂ` with simple eigenvalues `{1, ω, ω²}`, so
  `ℂ[Z₃] = ℂ ⊕ ℂ ⊕ ℂ` — **three** blocks, `K₀-complex = ℤ³`.
- **Real:** the conjugate pair `{ω, ω²}` cannot split over `ℝ`. The real-irreducible
  decomposition is the trivial singlet `ℝ` (all-ones `u=(1,1,1)`, eigenvalue 1)
  plus the 2-dim standard block. Both isotypic projectors `P_sing = J/3` and
  `P_doub = I − J/3` are **real**, **central** (`[P,C]=0`), orthogonal idempotents
  summing to `I` (real dims `1+2`). So `ℝ[Z₃] = ℝ ⊕ ℂ` — **two** blocks,
  `K₀-real = ℤ²`.

### 2. The doublet block is ONE real simple block = the field `ℂ` (STEP 1c)
`J_cs = (C − C²)/√3` is real, antisymmetric, `C₃-equivariant`, vanishes on the
singlet, and satisfies `J_cs² = −P_doub`. So `span_ℝ{P_doub, J_cs} ≅ ℂ` (unit
`P_doub`, imaginary unit `J_cs`): the doublet is a **real-irreducible module of
complex type**, Frobenius–Schur indicator `ν₂ = 0`, division ring `ℂ`. It is
**one** real simple block. Counting it once is exactly the `K₀-real` count.

### 3. The axiom's count = (1,1); the rivals = (1,2) (STEP 2, 4)
Counting real sectors, one unit each, dimension-blind: singlet `→1`, doublet
`→1`, giving the isotype weight **(1,1)**. The two rivals **coincide** at (1,2):
the complex/`K₀-complex` count (conjugate pair = two complex blocks) and the
dimension/Born reading (doublet weighted by its real dimension 2). The runner
confirms **(1,1) is reached by the full conjunction `real ∧ count` only**; drop
`real` → (1,2); drop `count` (use dimension) → (1,2); drop both → (1,2). Given
`real ∧ count`, "dimension-blind" is **entailed** (the doublet *is* one real
block) — it is not an independent third dial.

### 4. The map (1,1) → r=½ → Q=2/3 (STEP 3)
A `C₃-equivariant` real-spectrum Yukawa is the circulant `H = aI + bC + bC²`,
eigenvalues `{a+2b (singlet), a−b (doublet, ×2)}`. The Frobenius energy splits
orthogonally into channels (cross term 0):
```
E₊  = ‖aI‖²_F      = 3a²     (singlet channel)
E⊥  = ‖bC+bC²‖²_F  = 6b²     (doublet channel)
```
With `Q = (Σλ²)/(Σλ)² = (1 + 2r)/3`, `r = b²/a²`:
- **Axiom (1,1) as equal channel energy:** `3a² = 6b² ⇒ r = ½ ⇒ Q = 2/3`.
- **Rival (1,2) as equal energy-per-dimension:** `3a² = 6b²/2 ⇒ r = 1 ⇒ Q = 1`.

Numeric cross-check: `(a,b)=(√2,1) → r=½, Q=0.666667`; `(1,1) → r=1, Q=1`.

## Where the residual sits (the honest part)

### Residual R1 — the count→energy bridge (REAL) (STEP 5)
The axiom's output is a **measure on the sector index**: `μ(singlet) =
μ(doublet) = 1` (a counting measure — that is what "one unit per real sector,
dimension-blind" *says*). The Koide value needs an **equality of operator
channel energies** `3a² = 6b²`. Bridging "equal count" → "equal Frobenius
energy" is the identification
> record-weight of a sector := the squared-amplitude (Frobenius) energy the
> operator places in that sector's isotype channel.

That identification is a *second* ingredient. The runner exhibits **three**
distinct "one unit per real block" readouts on the *same* (1,1) count:

| Readout (all "equal per real block") | Locus | `r` | `Q` |
|---|---|---|---|
| equal **Frobenius channel energy** `3a²=6b²` | interior | **½** | **2/3** |
| equal **bare amplitude** per block `a=b` | interior | 1 | 1 |
| equal **eigenvalue magnitude** `|a+2b|=|a−b|` | none (a,b>0) | — | — |

Two inequivalent interior loci (`½` and `1`) both honour the (1,1) count. So the
count alone does **not** pin `r`; only the *Frobenius-energy* realization gives
`½`. The axiom as worded fixes which **sectors are counted and how many** (the
hard, genuinely-selective part — it kills the (1,2) rivals), but it does not, by
its own words, state that the per-sector unit is *realized as squared-amplitude
channel energy* rather than as a bare-coefficient unit.

*Steelman, and why R1 survives it:* one can argue "additive over disjoint
alternatives" + a Born/amplitude reading of "amount" forces the energy bridge,
since the Born content of a sector is its squared amplitude. That is a coherent
*completion* of the axiom — but it is an added Born clause, not the counting
clause. The literal text ("counts … one unit per real sector, dimension-blind")
is a counting measure, which is silent on the operator's per-channel amplitude.
R1 is therefore a real residual of *the stated axiom*, closable by appending a
single explicit clause ("the per-sector unit is the Born/Frobenius channel
energy"), at which point the derivation is clean.

### Residual R2 — "classical = real" (DISCHARGED-BY-STIPULATION) (STEP 6)
The axiom's word **real** does legitimate work and is **not** contradicted by
the framework. The carrier `ℝ[Z₃]` has rational structure constants (manifestly
real). The one complexification the framework forces — the `Cl(3)` central
pseudoscalar `ω_Cl = σ₁σ₂σ₃ = i·I₂` — lives on the per-site **qubit** factor and
acts on the generation index as the **scalar** `i·I₃` (eig `{i,i,i}`, singlet and
doublet alike), **not** as the doublet complex structure `J_cs` (eig `{0,+i,−i}`).
So the forced qubit `i` does not complexify the generation factor; "classical =
real" is a substantive, uncontradicted premise the axiom may legitimately
**stipulate**. (This matches, and re-derives from scratch, the qubit-`i`-is-a-
generation-scalar finding already on main; see cross-check below.)

## Bottom line

- **Selective power (clean):** the axiom's `real ∧ count` clauses **uniquely**
  defeat both `(1,2)` rivals (complex-count and dimension/Born), which are the
  exact readings that give `r=1`. This is the substantive achievement — it picks
  `(1,1)` non-arbitrarily, grounded in the real Artin–Wedderburn structure and
  `K₀-real = ℤ²`.
- **Residual (named):** turning the `(1,1)` *count* into the `r=½` *value* needs
  the extra clause "per-sector unit := Born/Frobenius channel energy." Without
  it, a bare-amplitude reading of "one per block" gives `r=1`. The axiom is **one
  explicit clause short** of a clean derivation; it is not circular and not
  blocked — the gap is precisely localizable and closable by augmenting the
  axiom's readout statement.
- **`classical = real`** is fine — substantive and uncontradicted.

## Prior-art cross-check (NOT load-bearing)

The finite real/complex Wedderburn block count, the doublet-as-`ℂ` complex-type
block, the qubit-`i`-is-a-generation-scalar fact, and the `E₊=3a², E⊥=6b²`
channel energies are independently established on `main` in
[`KOIDE_Q23_K0_REAL_BLOCK_EQUIVALENCE_NOTE_2026-05-30.md`](KOIDE_Q23_K0_REAL_BLOCK_EQUIVALENCE_NOTE_2026-05-30.md)
and
[`FLAVOR_SPLIT_THE_BRICK_DOUBLET_COMPLEX_STRUCTURE_2026-06-04.md`](FLAVOR_SPLIT_THE_BRICK_DOUBLET_COMPLEX_STRUCTURE_2026-06-04.md),
both of which leave the physical measure **open**. This note's runner re-derives
that math from the regular representation with no imported authority, then asks
the new question — does the *candidate axiom* close the slot — and reports the
residual R1 those notes localize as "the discrete readout bit" (signed/`det_C`
vs sign-blind/Born). Consistently with
[`KOIDE_R_HALF_NOT_SYMMETRY_PROTECTED_…_NO_GO_NOTE_2026-06-04`](KOIDE_R_HALF_NOT_SYMMETRY_PROTECTED_DYNAMICAL_NORM_BALANCE_NARROW_NO_GO_NOTE_2026-06-04.md),
`r=½` is the equal-channel-energy norm-balance point; this note identifies
*exactly* the additional axiom clause (Born/energy realization of the count)
that would force that balance from the record axiom.

## The next path this opens (not a closure)

The residual is a single, sharp drafting choice for the axiom: **does record
readout assign each real sector its Born (squared-amplitude / Frobenius-energy)
weight, or a bare counting unit?** Pressure-test #2 should test the *augmented*
axiom — "real classical alternatives, counted, each carrying its Born channel
weight" — and check whether that statement (a) still uniquely selects the real
2-block picture and (b) now forces `3a²=6b²` cleanly. If so, the strong Record
axiom derives `r=½` outright; if a further hinge appears, this note's STEP 5
table is where to look for it.
