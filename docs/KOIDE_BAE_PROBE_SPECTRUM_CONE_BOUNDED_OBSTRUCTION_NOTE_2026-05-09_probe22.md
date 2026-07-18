# Abstract Circulant Cone-Slack Rewrite (historical Koide Probe 22) — Bounded Theorem

**Date:** 2026-05-09
**Type:** bounded_theorem
**Scope:** review-loop source-note proposal — historical Probe 22 of the Koide
Frobenius-equipartition closure campaign (legacy alias: Brannen Amplitude
Equipartition, BAE). It tests the
**spectrum-level cone localization rewrite** on a supplied abstract
Hermitian circulant. The note tests whether the cone slack is distinct from
the parameter-level routes already enumerated by Probes 1-21. The
pivot asks: instead of deriving `(a, b)` such that `|b|²/a² = 1/2`
(BAE), derive directly that the eigenvalues
`{λ_0, λ_1, λ_2}` of the abstract circulant
`H = aI + bC + b̄C²` on `hw=1` lie on the Koide cone
`λ_0² + λ_1² + λ_2² = 4(λ_0λ_1 + λ_0λ_2 + λ_1λ_2)`, and close
an abstract ratio statement via the polynomial identity
`KOIDE_CONE_THREE_FORM_EQUIVALENCE`.
**Status:** source-note proposal for an exact abstract residual identity. On a
supplied `Herm_circ(3)` matrix, the spectrum cone slack is proportional to the
parameter slack. This does not supply P1, a matter-sector carrier, a physical
selector, or an exhaustive no-go against separately supplied spectral
functionals. This repair adds no premise and changes no premise registry.
**Authority role:** source-note proposal — audit verdict and
downstream status set only by the independent audit lane.
**Loop:** koide-bae-probe-spectrum-cone-20260509
**Primary runner:** [`scripts/cl3_koide_bae_probe_spectrum_cone_2026_05_09_probe22.py`](../scripts/cl3_koide_bae_probe_spectrum_cone_2026_05_09_probe22.py)
**Cache:** [`logs/runner-cache/cl3_koide_bae_probe_spectrum_cone_2026_05_09_probe22.txt`](../logs/runner-cache/cl3_koide_bae_probe_spectrum_cone_2026_05_09_probe22.txt)

## Authority disclaimer

This is a source-note proposal. Pipeline-derived status is generated
only after the independent audit lane reviews the claim, dependency
chain, and runner. The claim type, scope, supplied/open premises, and
bounded-obstruction classification are author-proposed; the audit
lane has full authority to retag, narrow, or reject the proposal.

## Current naming and historical alias

The current framework baseline uses the named **Lattice**, **Qubit**,
**Admissibility**, and **Record** axioms. The historical phrase "framework
axiom A1" is obsolete. Here BAE is retained only as a historical alias for
the Koide Frobenius-equipartition condition `|b|²/a² = 1/2` on `a != 0`
for the supplied abstract circulant; the explicit name is used for the live
claim.

## Question

Probes 1-21 attacked closure at the **parameter level** — derive
`(a, b)` values such that `|b|²/a² = 1/2`. All 18 named probes
returned bounded structural obstruction; the campaign synthesis
([`KOIDE_A1_11_PROBE_CAMPAIGN_BOUNDED_ADMISSION_META_NOTE_2026-05-08.md`](KOIDE_A1_11_PROBE_CAMPAIGN_BOUNDED_ADMISSION_META_NOTE_2026-05-08.md))
+ Probes 12-13 + Probe 18 sharpened the missing primitive to
"the canonical (1,1)-multiplicity-weighted Frobenius pairing on
`M_3(ℂ)_Herm` under `C_3`-isotype decomposition" / equivalently
"the U(1)_b angular quotient on the non-trivial doublet of
`A^{C_3}`."

**This probe asks:** is the displayed spectrum-cone equation algebraically
distinct from the parameter slack? Specifically, for eigenvalues
`{λ_0, λ_1, λ_2}` of the abstract
circulant `H = aI + bC + b̄C²` lie on the Koide cone
`λ_0² + λ_1² + λ_2² = 4(λ_0λ_1 + λ_0λ_2 + λ_1λ_2)`, with the
retained polynomial identity
[`KOIDE_CONE_THREE_FORM_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-02`](KOIDE_CONE_THREE_FORM_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-02.md)
closing `Q = 2/3` from cone-localization?

## Answer

**For the displayed cone slack, no.** The finite circulant identity
[`KOIDE_CIRCULANT_CHARACTER_BRIDGE_NARROW_THEOREM_NOTE_2026-05-09`](KOIDE_CIRCULANT_CHARACTER_BRIDGE_NARROW_THEOREM_NOTE_2026-05-09.md))
makes the spectrum-level cone localization equation
**arithmetically identical** to the parameter-level BAE on
`Herm_circ(3)`:

```text
3 (λ_0² + λ_1² + λ_2²) − 2 (λ_0 + λ_1 + λ_2)²  =  −9 (a² − 2|b|²).   (*)
```

The cone slack on the left and the parameter slack on the right
have the same global polynomial zero locus,
[`CHARGED_LEPTON_KOIDE_CONE_ALGEBRAIC_EQUIVALENCE_NOTE`](CHARGED_LEPTON_KOIDE_CONE_ALGEBRAIC_EQUIVALENCE_NOTE.md))
are the **same equation up to a non-vanishing real prefactor of −9**.
Vanishing of one is vanishing of the other; both have the same zero
set on `(a, |b|)`-space, including the origin. On the domain \(a\ne0\)
(and hence \(b\ne0\) on the nonzero polynomial locus), this is also
equivalent to the quotient statements \(Q=2/3\) and
\(|b|^2/a^2=1/2\). Neither quotient is defined at the origin. Therefore:

- "spectrum lies on the Koide cone" and
- "operator parameters satisfy BAE"

are not distinct mathematical statements on `Herm_circ(3)`. They are
the SAME equation in DIFFERENT variables.

**Narrow verdict.** This particular cone-localization equation is a rewrite of
the parameter equation. A separately supplied phase-sensitive spectral
functional could use `e_3`; this note neither supplies nor rules out such a
selector. No premise or registry entry is changed.

## Setup

### Premises (A_min for probe 22)

| ID | Statement | Class |
|---|---|---|
| Qubit | `M_2(C)` / `Cl(3,0)` local algebraic presentation | framework context; see `MINIMAL_AXIOMS_2026-06-29.md`; not load-bearing in the finite circulant calculation |
| Lattice | `Z³` nearest-neighbour substrate | framework context; same source; not load-bearing in the finite circulant calculation |
| BZ | hw=1 BZ-corner triplet ≅ `ℂ³` with `C_3[111]` action | source dependency; see [`STAGGERED_DIRAC_BZ_CORNER_FORCING_THEOREM_NOTE_2026-05-07.md`](STAGGERED_DIRAC_BZ_CORNER_FORCING_THEOREM_NOTE_2026-05-07.md) |
| 3GenObs | hw=1 carries `M_3(ℂ)` algebra; no proper exact quotient | source dependency; see [`THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md`](THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md) |
| Circulant (R1) | `C_3`-equivariant Hermitian on hw=1 is `aI + bC + b̄C²` | source dependency; see [`KOIDE_CIRCULANT_CHARACTER_DERIVATION_NOTE_2026-04-18.md`](KOIDE_CIRCULANT_CHARACTER_DERIVATION_NOTE_2026-04-18.md) R1 |
| Spectrum (R2) | `λ_k = a + bω^k + b̄ω^{−k} = a + 2\|b\|cos(arg(b) + 2πk/3)` | source dependency; see [`KOIDE_CIRCULANT_CHARACTER_DERIVATION_NOTE_2026-04-18.md`](KOIDE_CIRCULANT_CHARACTER_DERIVATION_NOTE_2026-04-18.md) R2 |
| Bridge | `a₀ = √3 a`, `\|z\|² = 3\|b\|²`, `a₀² − 2\|z\|² = 3a² − 6\|b\|²` | source dependency; see [`KOIDE_CIRCULANT_CHARACTER_BRIDGE_NARROW_THEOREM_NOTE_2026-05-09.md`](KOIDE_CIRCULANT_CHARACTER_BRIDGE_NARROW_THEOREM_NOTE_2026-05-09.md) (positive_theorem) |
| ConeIdentity | Polynomial cone equation; equivalent to `Q = 2/3` only when its denominator is nonzero | source dependency; see [`KOIDE_CONE_THREE_FORM_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-02.md`](KOIDE_CONE_THREE_FORM_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-02.md) (positive_theorem) |
| KoideAlg | Polynomial slack equivalence globally; quotient forms only on their nonzero-denominator domains | source dependency; see [`CHARGED_LEPTON_KOIDE_CONE_ALGEBRAIC_EQUIVALENCE_NOTE.md`](CHARGED_LEPTON_KOIDE_CONE_ALGEBRAIC_EQUIVALENCE_NOTE.md) |
| Campaign | 18-probe terminal residue: `(1,1)`-weighted Frobenius / `U(1)_b` angular quotient | source dependency; see [`KOIDE_A1_11_PROBE_CAMPAIGN_BOUNDED_ADMISSION_META_NOTE_2026-05-08.md`](KOIDE_A1_11_PROBE_CAMPAIGN_BOUNDED_ADMISSION_META_NOTE_2026-05-08.md) + Probes 12, 13, 14, 18 |

### Forbidden imports

- NO PDG observed mass values used as derivation input (per
  [`STAGGERED_DIRAC_SUBSTEP4_AC_NARROW_BOUNDED_NOTE_2026-05-07_substep4ac.md`](STAGGERED_DIRAC_SUBSTEP4_AC_NARROW_BOUNDED_NOTE_2026-05-07_substep4ac.md))
- NO lattice MC empirical measurements
- NO fitted matching coefficients
- NO new premise, axiom, or registry entry added by this probe
- NO new axioms (per user 2026-05-09 clarification: closure must come
  from already-cited source-stack content or from a derivation extending the
  retained library)

## Derivation

### Step 1 — Spectrum-level cone localization is the spectral form of BAE

Substitute the supplied spectrum formula (R2) `λ_k = a + bω^k + b̄ω^{−k}`
into the elementary symmetric polynomials:

```text
e₁ ≡ λ₀ + λ₁ + λ₂  =  3a               (uses 1 + ω + ω² = 0)
e₂ ≡ Σ_{i<j} λ_i λ_j  =  3a² − 3|b|²
p₂ ≡ λ₀² + λ₁² + λ₂²  =  e₁² − 2 e₂  =  9a² − 6a² + 6|b|²
                                            =  3a² + 6|b|²
```

(Runner Section 3, T3.2, T4.2 verifies the explicit forms.)

The cone localization condition

```text
3 p₂  =  2 e₁²
```

(equivalent to `Q = 2/3` per retained
[`KOIDE_CONE_THREE_FORM_EQUIVALENCE`](KOIDE_CONE_THREE_FORM_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-02.md)
T2) becomes

```text
3 (3a² + 6|b|²)  =  2 (3a)²
9 a² + 18 |b|²  =  18 a²
9 |b|²  =  9 (a² − |b|²) ... (rearranged)
```

Equivalently, the **cone slack** is

```text
3 p₂ − 2 e₁²  =  9 a² + 18 |b|² − 18 a²
              =  − 9 (a² − 2 |b|²)                     (*)
```

The right-hand side is the **BAE slack** `(a² − 2|b|²)` multiplied
by the non-vanishing real constant `−9`. (Runner Section 3, T3.3
verifies this exactly.)

### Step 2 — Bridge identity is the algebraic content of (*)

The finite Koide-Circulant Character Bridge identity (T3 of
[`KOIDE_CIRCULANT_CHARACTER_BRIDGE_NARROW_THEOREM_NOTE_2026-05-09`](KOIDE_CIRCULANT_CHARACTER_BRIDGE_NARROW_THEOREM_NOTE_2026-05-09.md))
states:

```text
a₀² − 2 |z|²  =  3 a² − 6 |b|²                        (Bridge T3)
```

Combined with the eigenvalue-side Plancherel identity
`p₂ = a₀² + 2|z|²` (as defined in
[`CHARGED_LEPTON_KOIDE_CONE_ALGEBRAIC_EQUIVALENCE_NOTE`](CHARGED_LEPTON_KOIDE_CONE_ALGEBRAIC_EQUIVALENCE_NOTE.md)
equation 1) and `e₁² = 3 a₀²` (equation 2), the cone slack rewrites:

```text
3 p₂ − 2 e₁²  =  3 (a₀² + 2|z|²) − 2 · 3 a₀²
              =  3 a₀² + 6 |z|² − 6 a₀²
              =  − 3 (a₀² − 2 |z|²)
              =  − 3 (3 a² − 6 |b|²)                   (by Bridge T3)
              =  − 9 (a² − 2 |b|²).
```

This recovers (*) algebraically. Runner Section 2 verifies T3
symbolically; Section 3 T3.3 verifies the chain to (*) symbolically.

### Step 3 — The two slack expressions have the same zero set

Equation (*) is an algebraic identity on `Herm_circ(3)`. The cone
slack `3 p₂ − 2 e₁²` and the BAE slack `(a² − 2 |b|²)` differ only
by the non-vanishing real constant `−9`. Therefore:

```text
{(a, b) ∈ ℝ × ℂ  :  cone slack = 0}
   =  {(a, b) ∈ ℝ × ℂ  :  BAE slack = 0}
   =  {(a, b)  :  a² = 2|b|²}                          (BAE locus)
```

Vanishing of either slack is the BAE condition `|b|²/a² = 1/2`
(when `a ≠ 0`). Runner Section 4 T4.4 verifies this on six concrete
sample points (three BAE-satisfying, three off-BAE) and Section 4
T4.6 verifies the prefactor `−9` is non-vanishing.

### Step 4 — Spectrum invariants on the abstract circulant
### The displayed cone slack uses only `(a, |b|)`

The supplied abstract circulant `H = aI + bC + b̄C²` has three real
coordinates `(a, b_re, b_im)`.
The eigenvalue triple `(λ_0, λ_1, λ_2)` is parametrized by
`(a, |b|, arg(b))` via the Brannen/Rivero spectral form
`λ_k = a + 2|b|cos(arg(b) + 2πk/3)`.

The full set of spectrum invariants is `{e_1, e_2, e_3}` (or
equivalently `{p_1, p_2, p_3}`):

```text
e_1  =  3 a                        (delta-INDEPENDENT)
e_2  =  3 a² − 3 |b|²              (delta-INDEPENDENT)
e_3  =  a³ − 3 a |b|² + 2 |b|³ cos(3 δ)   (delta-DEPENDENT)
```

(where `δ = arg(b)`, runner Section 5 T5.3 verifies). Of the three
spectrum invariants, only `e_3` carries `δ`-dependence — through
`cos(3δ)`. **The BAE condition is `δ`-independent** (it's `a² = 2|b|²`,
which contains no `δ`). Therefore this particular cone/BAE slack uses
`e_1` and `e_2`, both functions of `(a,|b|)`. The phase-sensitive invariant
`e_3` is a genuine additional spectral coordinate; it simply does not enter
the displayed slack. No universal claim about every spectrum-level selector
is made.

(Runner Section 5 T5.1.1, T5.1.2, T5.2.e_1, T5.2.e_2 verify
δ-independence of `e_1, e_2, p_1, p_2`. Section 5 T5.1.3, T5.2.e_3
verify `e_3, p_3` ARE δ-dependent. The following boundary statement is
intentionally uncounted.)

### Step 5 — The closure step is correct, conditional on antecedent

If, hypothetically, the antecedent "spectrum on the displayed cone" were
supplied for the abstract circulant, the
retained polynomial identity
[`KOIDE_CONE_THREE_FORM_EQUIVALENCE`](KOIDE_CONE_THREE_FORM_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-02.md)
T2 would imply `Q = 2/3`, and the cited algebraic
equivalence
[`CHARGED_LEPTON_KOIDE_CONE_ALGEBRAIC_EQUIVALENCE_NOTE`](CHARGED_LEPTON_KOIDE_CONE_ALGEBRAIC_EQUIVALENCE_NOTE.md)
would correctly close BAE. **The closure step is sound**; the
problem is the antecedent.

By Steps 1-3, "spectrum on this cone" is the same polynomial zero locus as the
parameter slack. This equivalence alone does not transfer a broader campaign
no-go to every possible spectral functional.

(Runner Section 6 recomputes three algebraic checks; the prose boundary is
uncounted.)

## Theorem (abstract cone-slack identity)

**Theorem.** For a supplied abstract Hermitian circulant
`H=aI+bC+conj(b)C²`,

```text
3 (lambda_0²+lambda_1²+lambda_2²)
  - 2 (lambda_0+lambda_1+lambda_2)²
= -9 (a²-2|b|²).
```

Consequently the displayed cone slack and parameter slack have exactly the
same global zero locus, including the origin. On the appropriate
nonzero-denominator domains (`a!=0` for `Q` and `|b|²/a²`, `b!=0` for
`a²/|b|²`), the associated ratio statements are equivalent; no quotient is
extended to the origin. The
quantities `e_1,e_2,p_1,p_2` entering this slack are phase-independent, while
`e_3,p_3` retain `cos(3 arg(b))` dependence. Thus this theorem is an exact
rewrite of one slack, not a no-go against phase-sensitive spectral selectors
and not physical Koide closure.

**Proof.** Direct finite Fourier substitution, Newton-Girard algebra, and the
nonzero prefactor `-9`, all recomputed in runner Sections 1-6.

## Convention-robustness check

The spectrum-level pivot is invariant under:

- **Scale invariance**: `H → cH` rescales `(a, b) → (ca, cb)` and
  `λ_k → c λ_k`. Both cone slack and BAE slack scale as `c²`, so the
  zero set `(a² = 2|b|²)` is preserved. ✓ (Runner Section 4 T4.4
  on three BAE-satisfying samples at three different scales
  `a ∈ {sqrt(2), 2sqrt(2), sqrt(2)/2}`.)
- **Basis change** `C → C^{-1} = C²`: preserves the `C_3`-action and
  isotype structure (swaps `ω ↔ ω̄`). The eigenvalue spectrum is
  unchanged (just relabels the cube roots). ✓ (Implicit in R1, R2.)
- **`arg(b)`-shift** `b → e^{iα} b`: for arbitrary `α`, the full spectrum
  generally changes through `e_3`; only shifts by multiples of `2π/3` merely
  permute the labels. The displayed cone slack and `e_1,e_2` remain
  phase-independent. ✓ (Runner Sections 4-5.)

The abstract circulant form is supplied for this calculation. No physical
matter-sector carrier, `(1,1)` weighting, quotient, or selector is derived.

## Relation to prior probes

Prior campaign notes are context only. This note contributes the exact
cone-slack proportionality and separates the phase-independent
`e_1,e_2,p_1,p_2` from phase-sensitive `e_3,p_3`. It does not inherit or extend
their no-go verdicts and proposes no new premise or registry entry.

### What this probe DOES

1. Verifies the supplied R1 + R2 forms on a concrete abstract circulant
   `H = aI + bC + b̄C²` (Section 1).
2. Verifies the finite Bridge identity (T1, T2, T3) symbolically
   (Section 2).
3. Verifies that the spectrum-level cone slack
   `3 p₂ − 2 e₁²` equals `−9 (a² − 2|b|²)` algebraically (Section 3).
4. Verifies that the polynomial cone slack and parameter slack cut out the
   same global locus, with ratio statements restricted to their domains
   (Section 4).
5. Verifies that BAE-relevant spectrum invariants are δ-independent
   (Section 5).
6. Recomputes the abstract polynomial implication from the cone equation
   (Section 6).
7. Prints the physical/source boundary without counting it as theorem evidence.

### What this probe DOES NOT do

1. Does NOT close BAE.
2. Does NOT add any new axiom, premise, or registry entry.
3. Does NOT modify any cited source (BZ, 3GenObs, Circulant R1,
   Spectrum R2, Bridge T1-T3, ConeIdentity T2, KoideAlg, Campaign,
   any prior Probe).
4. Does NOT promote any downstream theorem.
5. Does NOT load-bear PDG values into a derivation step.
6. Does NOT modify the audit-honest options enumerated by the
   campaign synthesis (supply / derive / pivot).
7. Does NOT propose `U(1)_b` as a new primitive (per user 2026-05-09
   constraint: no new axioms, no external imports).

## Honest assessment

The exact outcome is a partial narrowing: for the supplied abstract
circulant, the displayed cone slack and parameter slack are the same equation
up to `-9`. This does not derive the zero locus, P1, a physical carrier, or a
selector. It also does not rule out phase-sensitive spectral constructions,
because `e_3` and `p_3` vary with `cos(3 arg(b))`.

## Cross-references

### Foundational baseline

- Minimal axioms: `MINIMAL_AXIOMS_2026-06-29.md`
- Substep-4 AC narrowing: [`STAGGERED_DIRAC_SUBSTEP4_AC_NARROW_BOUNDED_NOTE_2026-05-07_substep4ac.md`](STAGGERED_DIRAC_SUBSTEP4_AC_NARROW_BOUNDED_NOTE_2026-05-07_substep4ac.md)

### Cited provenance and supplied context

- BZ-corner forcing: [`STAGGERED_DIRAC_BZ_CORNER_FORCING_THEOREM_NOTE_2026-05-07.md`](STAGGERED_DIRAC_BZ_CORNER_FORCING_THEOREM_NOTE_2026-05-07.md)
- M_3(ℂ) on hw=1: [`THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md`](THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md)
- Circulant R1 + Spectrum R2: [`KOIDE_CIRCULANT_CHARACTER_DERIVATION_NOTE_2026-04-18.md`](KOIDE_CIRCULANT_CHARACTER_DERIVATION_NOTE_2026-04-18.md)
- Bridge T1-T3 (positive_theorem): [`KOIDE_CIRCULANT_CHARACTER_BRIDGE_NARROW_THEOREM_NOTE_2026-05-09.md`](KOIDE_CIRCULANT_CHARACTER_BRIDGE_NARROW_THEOREM_NOTE_2026-05-09.md)
- Cone polynomial identity (positive_theorem): [`KOIDE_CONE_THREE_FORM_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-02.md`](KOIDE_CONE_THREE_FORM_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-02.md)
- Cone completing-root (positive_theorem): [`KOIDE_CONE_COMPLETING_ROOT_NARROW_THEOREM_NOTE_2026-05-02.md`](KOIDE_CONE_COMPLETING_ROOT_NARROW_THEOREM_NOTE_2026-05-02.md)
- Charged-lepton Koide cone equivalence: [`CHARGED_LEPTON_KOIDE_CONE_ALGEBRAIC_EQUIVALENCE_NOTE.md`](CHARGED_LEPTON_KOIDE_CONE_ALGEBRAIC_EQUIVALENCE_NOTE.md)
- Abstract Hermitian-circulant Fourier invariant only: [`KOIDE_KAPPA_SPECTRUM_OPERATOR_BRIDGE_THEOREM_NOTE_2026-04-19.md`](KOIDE_KAPPA_SPECTRUM_OPERATOR_BRIDGE_THEOREM_NOTE_2026-04-19.md). It does not supply P1, a mass spectrum, a physical carrier, or a selector.

### Eleven-probe campaign + Probes 12-18

- Campaign synthesis: [`KOIDE_A1_11_PROBE_CAMPAIGN_BOUNDED_ADMISSION_META_NOTE_2026-05-08.md`](KOIDE_A1_11_PROBE_CAMPAIGN_BOUNDED_ADMISSION_META_NOTE_2026-05-08.md)
- Probe 12 (Plancherel/Peter-Weyl): [`KOIDE_A1_PROBE_PLANCHEREL_PETER_WEYL_BOUNDED_OBSTRUCTION_NOTE_2026-05-09_probe12.md`](KOIDE_A1_PROBE_PLANCHEREL_PETER_WEYL_BOUNDED_OBSTRUCTION_NOTE_2026-05-09_probe12.md)
- Probe 13 (Real-structure): [`KOIDE_A1_PROBE_REAL_STRUCTURE_BOUNDED_OBSTRUCTION_NOTE_2026-05-09_probe13.md`](KOIDE_A1_PROBE_REAL_STRUCTURE_BOUNDED_OBSTRUCTION_NOTE_2026-05-09_probe13.md)
- Probe 14 (Retained-U(1) hunt): [`KOIDE_A1_PROBE_RETAINED_U1_HUNT_BOUNDED_OBSTRUCTION_NOTE_2026-05-09_probe14.md`](KOIDE_A1_PROBE_RETAINED_U1_HUNT_BOUNDED_OBSTRUCTION_NOTE_2026-05-09_probe14.md)

### BAE rename

- Rename note: [`BRANNEN_AMPLITUDE_EQUIPARTITION_BAE_RENAME_META_NOTE_2026-05-09.md`](BRANNEN_AMPLITUDE_EQUIPARTITION_BAE_RENAME_META_NOTE_2026-05-09.md) (PR #790, 2026-05-09).

## Validation

```bash
python3 scripts/cl3_koide_bae_probe_spectrum_cone_2026_05_09_probe22.py
```

Expected: `=== TOTAL: PASS=30, FAIL=0 ===`

The runner verifies:

1. Section 1 (5 tests) — Supplied finite-algebra inputs realized on
   concrete `H = aI + bC + b̄C²`: `C³ = I`, `C` unitary, `C`
   eigenvalues `{1, ω, ω̄}`, `H` Hermitian, eigenvalues match
   Brannen/Rivero form.
2. Section 2 (3 tests) — Finite Bridge identity (T1, T2, T3)
   verified symbolically: `a₀ = √3 a`, `|z|² = 3|b|²`,
   `a₀² − 2|z|² = 3a² − 6|b|²`.
3. Section 3 (4 tests) — Spectrum-level cone reduces to BAE:
   `F_orbit = const · (a² − 2|b|²)` symbolically, sum identities,
   cone slack = `−9 (a² − 2|b|²)`, BAE iff cone-localization at
   concrete sample points.
4. Section 4 (7 tests) — Spectrum-level pivot is bridge-identical to
   parameter-level: Brannen/Rivero spectral form, δ-independence of
   `e₁, e₂`, Q = 2/3 ⇔ BAE, locus equality on six samples,
   δ-independence of cone localization at BAE, prefactor `−9`
   non-vanishing, and the origin domain guard for quotient forms.
5. Section 5 (8 tests) — `e₁,e₂,p₁,p₂` are δ-independent while
   `e₃,p₃` are δ-dependent; the uncounted boundary does not foreclose a
   phase-sensitive selector.
6. Section 6 (3 tests) — Abstract polynomial implication from the cone:
   `F_ratio' = −F_orbit_retained` (T2 identity), concrete cone-on
   triple (1, 1, 4 + 3√2), concrete off-cone triple (1, 1, 1),
   closure step soundness conditional on antecedent.
7. Section 7 (0 counted tests) — source and physical boundaries are printed
   but uncounted.

All 30 PASSes are keyed to substantive symbolic or numerical computations;
prose verdicts are uncounted.

## Retention and status boundary

The preserved scientific content is the exact finite-algebra identity, its
global zero-locus equivalence, and the phase-dependence split between
`e_1,e_2,p_1,p_2` and `e_3,p_3`. No empirical comparator is load-bearing. The
source note does not set an audit result, introduce a premise, or claim
physical closure. P1, the matter carrier/readout, and any spectral selector
remain open.
