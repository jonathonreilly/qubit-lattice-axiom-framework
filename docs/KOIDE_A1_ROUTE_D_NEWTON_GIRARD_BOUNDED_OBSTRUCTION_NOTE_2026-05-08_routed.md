# Newton-Girard Polynomial Candidate (historical Koide Route D) — Bounded Obstruction

**Date:** 2026-05-08
**Type:** bounded_theorem
**Scope:** review-loop source-note proposal — historical Route D closure
attempt for the Koide Frobenius-equipartition condition
on the charged-lepton Koide lane.
**Status:** source-note proposal for a negative Route D closure —
shows narrowly that Newton-Girard identities and the named candidate
functionals tested here do not select the identification
`p_2/e_1² = 2/3` (equivalently `e_1² = 6 e_2`, equivalently
`|b|²/a² = 1/2`). It does not prove that every symmetric-polynomial
functional or every cited-source route fails. This repair adds no premise and
changes no premise registry.
**Authority role:** source-note proposal — audit verdict and
downstream status set only by the independent audit lane.
**Loop:** koide-a1-route-d-newton-girard-20260508
**Primary runner:** [`scripts/cl3_koide_a1_route_d_newton_girard_2026_05_08_routed.py`](../scripts/cl3_koide_a1_route_d_newton_girard_2026_05_08_routed.py)
**Cache:** [`logs/runner-cache/cl3_koide_a1_route_d_newton_girard_2026_05_08_routed.txt`](../logs/runner-cache/cl3_koide_a1_route_d_newton_girard_2026_05_08_routed.txt)

## Authority disclaimer

This is a source-note proposal. Pipeline-derived status is generated
only after the independent audit lane reviews the claim, dependency
chain, and runner. The claim type, scope, supplied/open premises, and
bounded-obstruction classification are author-proposed; the audit lane
has full authority to retag, narrow, or reject the proposal.

## Question

`KOIDE_A1_DERIVATION_STATUS_NOTE.md`
identifies the historical **Route D** (Newton-Girard polynomial structure) as
a candidate closure route for the Koide Frobenius-equipartition condition.
The proposed structural identification is

> `V(Φ)  =  [e_1²  −  6 e_2]²  =  0`  on Herm_circ(3),

equivalently the rational coefficient identity

> `p_2 / e_1²  =  2/3`

where `(p_k, e_k)` are the power sums and elementary symmetric
polynomials in the eigenvalues `λ_k` of the supplied C_3-equivariant
Hermitian circulant
`H = aI + bC + b̄C^2` on hw=1. By Newton-Girard,
`p_2 = e_1² - 2 e_2`, so the two forms are equivalent.

This is **structurally distinct** from the Lie-algebraic norm routes
that closed Routes E and F negatively
([`KOIDE_A1_ROUTE_E_KOSTANT_WEYL_BOUNDED_OBSTRUCTION_NOTE_2026-05-08_routee.md`](KOIDE_A1_ROUTE_E_KOSTANT_WEYL_BOUNDED_OBSTRUCTION_NOTE_2026-05-08_routee.md),
[`KOIDE_A1_ROUTE_F_CASIMIR_DIFFERENCE_BOUNDED_OBSTRUCTION_NOTE_2026-05-08_routef.md`](KOIDE_A1_ROUTE_F_CASIMIR_DIFFERENCE_BOUNDED_OBSTRUCTION_NOTE_2026-05-08_routef.md)).
Routes E and F failed because their candidate `1/2` values were
**convention-dependent under continuous root-length / hypercharge
normalization conventions**. Route D's `2/3` is by contrast a
**rational coefficient in a polynomial identity** — its trap profile,
if it has one, must be different.

**Question:** Can the structural identification
`p_2/e_1² = 2/3` (equivalently `e_1² = 6 e_2`, equivalently
`|b|²/a² = 1/2`) be derived from cited Cl(3)/Z³ source content via
Newton-Girard polynomial structure alone — no empirical loading, no
new axioms, and crucially without falling into a structurally
analogous trap to Routes E/F?

## Answer

**Not from Newton-Girard identities alone.** Those identities are coordinate
relations, not spectrum constraints, and the circulant family leaves the ratio
continuous. The runner also falsifies several named candidate extremizations.
This is a narrow route result, not an exhaustive cited-source no-go.

The computed observations (20 algebraic PASS, with sibling-route context,
prose synthesis, and PDG
anchors explicitly uncounted) are:

1. **Newton-Girard is identity, not constraint (D1).** The
   Newton-Girard relation `p_2 = e_1² − 2 e_2` is a textbook bijection
   between power sums and elementary symmetric polynomials. It holds
   for any 3-tuple of (real or complex) numbers and imposes ZERO
   structural constraint. The runner verifies the identity holds
   exactly for 50/50 random triples and on 50/50 random circulants
   while the ratio `p_2/e_1²` ranges over `[0.336, 10.481]` — clearly
   not pinned at `2/3`. The Newton-Girard machinery alone therefore
   does not single out any specific value.

2. **Block-counting weight comparison (D2).** The polynomial form
   `e_1² - 6 e_2` vanishes at A1. Separately, the `(1,1)` and `(1,2)`
   block-log laws land at `kappa=2` and `kappa=1`. The runner explicitly
   verifies that polynomial coefficient zeros are not in one-to-one
   correspondence with those weighted extrema. This comparison is consistent
   with the weight-choice residue discussed by
   [`KOIDE_KAPPA_BLOCK_TOTAL_FROBENIUS_MEASURE_THEOREM_NOTE_2026-04-19.md`](KOIDE_KAPPA_BLOCK_TOTAL_FROBENIUS_MEASURE_THEOREM_NOTE_2026-04-19.md)
   §4 ("Residue"), but is not itself a universal no-go.

3. **Brannen ansatz + extra input required (D3).** On a generic
   Hermitian 3×3 operator outside Herm_circ(3) (i.e., not C_3-equivariant),
   `p_2/e_1²` ranges widely. Even on the supplied Brannen circulant
   ansatz `λ_k = a + 2|b|cos(arg b + 2πk/3)`, the ratio is
   `p_2/e_1² = 1/3 + (2/3)(|b|/a)²`, a continuous function of `|b|/a`.
   The cited R1+R2 source statement from
   [`KOIDE_CIRCULANT_CHARACTER_DERIVATION_NOTE_2026-04-18.md`](KOIDE_CIRCULANT_CHARACTER_DERIVATION_NOTE_2026-04-18.md))
   forces the Brannen form, but the SPECIFIC value `|b|/a = 1/√2`
   requires a separate principle.

4. **Polynomial-coefficient circularity (D4).** Substituting Brannen
   parameters into the polynomial form gives the symbolic identity

   ```
   e_1² − 6 e_2 = 9 (2|b|² − a²),

   V(Φ) = [e_1² − 6 e_2]² = 81 (a² − 2|b|²)².
   ```

   So `V(Φ) = 0 ⟺ a² = 2|b|²` (Frobenius equipartition). The
   polynomial form is **algebraically equivalent** to the open A1
   target, written in different coordinates. The coefficient `6`
   numerically matches `n(n−1)=3·2`; the rewrite does not derive a
   physical Frobenius selector or the origin of that coefficient.

5. **Named extremization candidate checks (D5).** A finite scan at the
   explicitly stated points gives:

   - **Discriminant** of the characteristic polynomial: on the chosen
     nondegenerate slice `delta=2/9`, it is nonzero and
     `d(Disc)/dr != 0` at the A1 radius. Degenerate phases such as `delta=0`
     are not covered by this check.
   - **Tschirnhaus depressed cubic** coefficient `p = e_2 − e_1²/3`:
     equals `−3 r²` at A1 (free parameter, no special vanishing).
   - **Ratio `e_1²/e_2`**: equals 6 at A1 by construction; but
     `d/dr [e_1²/e_2] ≠ 0` at A1 (NOT
     extremized).

   This finite scan is not exhaustive. For example,
   `(e_1²-6e_2)²` has its global minimum on A1 by construction; treating
   that functional as physical would itself be an unsupplied selector.

The combined picture is narrow: Newton-Girard plus the named candidates do not
select A1. A future derivation could still supply a justified functional,
dynamics, or other selector; this note does not classify that possibility as
a new axiom or rule it out.

## Setup

### Premises (A_min for Route D closure attempt)

| ID | Statement | Class |
|---|---|---|
| Qubit | `M_2(C)` / `Cl(3,0)` local algebraic presentation | framework context; see `MINIMAL_AXIOMS_2026-06-29.md`; not load-bearing in the finite circulant calculation |
| Lattice | `Z³` nearest-neighbour substrate | framework context; same source; not load-bearing in the finite circulant calculation |
| Embed | Cl⁺(3) ≅ ℍ → SU(2)_L; ω pseudoscalar → U(1)_Y; Y_L, Y_H fixed | cited source context; current ledger unaudited: [`CL3_SM_EMBEDDING_THEOREM.md`](CL3_SM_EMBEDDING_THEOREM.md) |
| GS | One-Higgs gauge selection: Y_e is arbitrary 3×3 complex matrix | cited source context; current ledger unaudited: [`SM_ONE_HIGGS_YUKAWA_GAUGE_SELECTION_THEOREM_NOTE_2026-04-26.md`](SM_ONE_HIGGS_YUKAWA_GAUGE_SELECTION_THEOREM_NOTE_2026-04-26.md) |
| WardFree | No direct Ward lift forces y_τ; Y_e remains free 3×3 | cited source context; current ledger unaudited: [`CHARGED_LEPTON_DIRECT_WARD_FREE_YUKAWA_NO_GO_NOTE_2026-04-26.md`](CHARGED_LEPTON_DIRECT_WARD_FREE_YUKAWA_NO_GO_NOTE_2026-04-26.md) |
| R1 (Circulant) | C_3-equivariant Hermitian on hw=1 is `aI + bU + b̄U^{-1}` | supplied source premise; current ledger unaudited: [`KOIDE_CIRCULANT_CHARACTER_DERIVATION_NOTE_2026-04-18.md`](KOIDE_CIRCULANT_CHARACTER_DERIVATION_NOTE_2026-04-18.md) R1 |
| R2 (Spectrum) | Eigenvalues `λ_k = a + 2|b|cos(arg b + 2πk/3)` | supplied source premise; current ledger unaudited: same source R2 |
| C3Pres | C_3[111] is preserved (not broken) on hw=1 in cited content | cited source context; current ledger unaudited: [`C3_SYMMETRY_PRESERVED_INTERPRETATION_NOTE_2026-05-08.md`](C3_SYMMETRY_PRESERVED_INTERPRETATION_NOTE_2026-05-08.md) |
| 3GenObs | hw=1 BZ-corner triplet has M_3(C) algebra; C_3[111] cycles corners | cited source context; current ledger unaudited: [`THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md`](THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md) |
| Substep4 | AC_φλ remains the explicit identification residual on hw=1 | cited source context; current ledger unaudited: [`STAGGERED_DIRAC_SUBSTEP4_AC_NARROW_BOUNDED_NOTE_2026-05-07_substep4ac.md`](STAGGERED_DIRAC_SUBSTEP4_AC_NARROW_BOUNDED_NOTE_2026-05-07_substep4ac.md) |
| KoideAlg | Koide Q = 2/3 ⟺ a₀² = 2|z|² ⟺ \|b\|²/a² = 1/2 ⟺ p_2/e_1² = 2/3 | cited source context; current ledger unaudited: [`CHARGED_LEPTON_KOIDE_CONE_ALGEBRAIC_EQUIVALENCE_NOTE.md`](CHARGED_LEPTON_KOIDE_CONE_ALGEBRAIC_EQUIVALENCE_NOTE.md) |
| Abstract Fourier invariant | On a defined `Herm_circ(3)` matrix, `a_0² − 2\|z\|² = 3(a² − 2\|b\|²)` with the same polynomial zero locus | finite algebra only: [`KOIDE_KAPPA_SPECTRUM_OPERATOR_BRIDGE_THEOREM_NOTE_2026-04-19.md`](KOIDE_KAPPA_SPECTRUM_OPERATOR_BRIDGE_THEOREM_NOTE_2026-04-19.md); it supplies no P1 mass assignment, physical carrier, or selector |
| BTF | Block-total Frobenius source proposal: supplied (1,1) weights yield κ=2 | cited source context; current ledger unaudited: [`KOIDE_KAPPA_BLOCK_TOTAL_FROBENIUS_MEASURE_THEOREM_NOTE_2026-04-19.md`](KOIDE_KAPPA_BLOCK_TOTAL_FROBENIUS_MEASURE_THEOREM_NOTE_2026-04-19.md) |
| MRUDemo | MRU SO(2)-quotient is supplementary, not load-bearing | cited source context; current ledger unaudited: [`KOIDE_MRU_DEMOTION_NOTE_2026-04-20.md`](KOIDE_MRU_DEMOTION_NOTE_2026-04-20.md) |
| RouteD_Form | `V(Φ) = [e_1² − 6 e_2]²` is the candidate Newton-Girard form for A1 | route-status note: `KOIDE_A1_DERIVATION_STATUS_NOTE.md` §"Route D" |

### Forbidden imports

- NO PDG observed mass values used as derivation input (anchor-only at
  end, clearly marked per
  [`STAGGERED_DIRAC_SUBSTEP4_AC_NARROW_BOUNDED_NOTE_2026-05-07_substep4ac.md`](STAGGERED_DIRAC_SUBSTEP4_AC_NARROW_BOUNDED_NOTE_2026-05-07_substep4ac.md)).
- NO lattice MC empirical measurements
- NO fitted matching coefficients
- NO same-surface family arguments
- **NO new axiom, premise, or registry entry**
- NO supplied SM Yukawa-coupling pattern as derivation input
- NO SO(2)-quotient postulate (per the cited MRU demotion source)

## The structural identification at issue

**Proposed identification (Route D):**

```
p_2 / e_1²  =  2/3      on circulant Hermitian on hw=1 ≅ ℂ³
```

equivalently `e_1² = 6 e_2`, equivalently
`V(Φ) = [e_1² − 6 e_2]² = 0`, equivalently `|b|²/a² = 1/2` (A1).

Where, for eigenvalues `(λ_0, λ_1, λ_2)` of `H = aI + bC + b̄C^2`:

- `p_k = λ_0^k + λ_1^k + λ_2^k`  (k-th power sum)
- `e_1 = λ_0 + λ_1 + λ_2`  (1st elementary symmetric)
- `e_2 = λ_0 λ_1 + λ_0 λ_2 + λ_1 λ_2`  (2nd elementary symmetric)
- `e_3 = λ_0 λ_1 λ_2`  (3rd elementary symmetric)

The Newton-Girard identity (textbook):

```
p_2  =  e_1²  −  2 e_2.
```

Substituting the Brannen R2 spectrum:

- `p_1 = e_1 = 3a` (cosine sum vanishes at n=3)
- `p_2 = 3a² + 6|b|²` (cosine-squared sum is 3/2 at n=3)
- `e_2 = (e_1² − p_2)/2 = (9a² − 3a² − 6|b|²)/2 = 3a² − 3|b|²`

Therefore A1 (`a² = 2|b|²`) is equivalent to `e_1² = 6 e_2`:

```
A1: a² = 2|b|²
⟺ 9a² = 6 (3a² − 3|b|²) = 18 a² − 18|b|²
⟺ 18|b|² = 9 a²
⟺ a² = 2|b|² ✓
```

On the domain `a != 0`, equivalently
`p_2/e_1² = (3a² + 6|b|²)/9a² = 1/3 + (2/3)(|b|/a)² = 2/3`
when `(|b|/a)² = 1/2` (A1).

This is mathematically clean and convention-independent at the
identity level (the trigonometric identities involved — `Σcos = 0`,
`Σcos² = 3/2` at n=3 — are pure trigonometry, no Lie-algebraic
normalization). However, the SPECIFIC VALUE `2/3` (or equivalently the
coefficient `6` in `e_1² = 6 e_2`) is **NOT forced** by Newton-Girard
alone. The runner verifies the free-ratio family directly and tests several
additional named candidates.

## Theorem (narrow Newton-Girard obstruction)

**Theorem.** For the displayed Hermitian-circulant family on `a != 0`,

```text
p_2/e_1² = 1/3 + (2/3)(|b|/a)².
```

Newton-Girard supplies `p_2=e_1²-2e_2` but imposes no constraint selecting
`|b|²/a²=1/2`. Moreover,

```text
e_1²-6e_2 = 9(2|b|²-a²),
```

so imposing that polynomial zero is exactly a rewrite of the target A1
condition. The discriminant, depressed-cubic coefficient, and ratio
candidates explicitly tested by the runner do not have an A1 critical point.
No conclusion is asserted for all possible symmetric-polynomial functionals
or all cited-content routes.

**Proof.** Direct substitution into the finite circulant eigenvalues and the
Newton-Girard identity; the named candidate derivatives are checked
symbolically by the paired runner.

### Barrier D1: Newton-Girard is identity, not constraint

The Newton-Girard relation `p_2 = e_1² − 2 e_2` is a textbook
elementary-symmetric-polynomial bijection. It holds for ANY 3-tuple
of (real or complex) numbers and imposes ZERO structural constraint.

The runner verifies this in three ways:

- 50/50 random eigenvalue triples satisfy `p_2 = e_1² − 2 e_2`
  exactly to numerical tolerance.
- 50/50 random Brannen-form circulants give `p_2/e_1²` ranging from
  ≈0.336 to ≈10.481 — clearly not pinned at 2/3.
- Explicit counterexamples `(a, b) = (1, 0.3)`, `(1, 0.7+0.4i)`,
  `(1, 1)`, `(1, 0.5+0.5i = A1)` all satisfy Newton-Girard but only
  one (the last) satisfies A1.

The Newton-Girard machinery is a tool for INTER-CONVERTING (p_k) and
(e_k); it is not a constraint that picks out A1.

### Barrier D2: Block-counting weight ambiguity

The cited
[`KOIDE_KAPPA_BLOCK_TOTAL_FROBENIUS_MEASURE_THEOREM_NOTE_2026-04-19.md`](KOIDE_KAPPA_BLOCK_TOTAL_FROBENIUS_MEASURE_THEOREM_NOTE_2026-04-19.md)
§4 compares two supplied log-laws on Herm_circ(3):

- **Block-total log-law** with multiplicity weights `(μ, ν) = (1, 1)`:
  extremum at `E_+ = E_perp`, equivalently `kappa = 2`, equivalently
  A1. Separately, the polynomial `e_1² − 6 e_2` vanishes at A1.
- **Det log-law** with dimensional weights `(μ, ν) = (1, 2)`
  (rank P_+ = 1, rank P_perp = 2): extremum at `E_perp = 2 E_+`,
  equivalently `kappa = 1`, NOT A1.

The runner verifies that `V_{(1,1)} = e_1² − 6 e_2` vanishes at A1
(target value `9·a²/2` is replaced by 0 there), while the dimensional-
weight form `V_{(1,2)} = e_1² − 3 e_2` does NOT vanish at A1
(`V_{(1,2)} |_A1 = 9a²/2 ≠ 0`). And the (1,2) Lagrangian extremum
(at `r=a`, i.e., `kappa = 1`) gives `e_2 = 0` (a degenerate
manifold), illustrating that polynomial coefficient zeros and
Lagrangian-extremum points are not in 1-1 correspondence.

The two supplied log-laws select different leaves. The cited MRU demotion
note discusses the same functional-choice issue (per
[`KOIDE_MRU_DEMOTION_NOTE_2026-04-20.md`](KOIDE_MRU_DEMOTION_NOTE_2026-04-20.md)).

This is context for the missing selector, not an identification of the `(1,2)`
log-law with `e_1²-3e_2=0`; the runner explicitly disproves that
one-to-one correspondence.

### Barrier D3: Brannen ansatz + extra input required

The runner confirms two scopes:

- **Generic Hermitian 3×3** (NOT cyclic-equivariant): random sampling
  gives `p_2/e_1²` ranging from ≈0.795 to ≈1652.704. Newton-Girard
  imposes zero constraint.
- **Supplied Brannen circulant**: `p_2/e_1² = 1/3 + (2/3)(r/a)²`
  is a continuous function of `r/a`, taking values in [1/3, ∞).
  Specific values: 1/3 at b=0 (degenerate), 2/3 at A1, 3 at r=2a.

The supplied circulant premise narrows the operator class but does
not pin the SPECIFIC value `r/a = 1/√2`. A separate principle is
required, which is exactly the open Koide Frobenius-equipartition condition.

### Barrier D4: Polynomial-coefficient circularity

The runner verifies symbolically:

```
e_1² − 6 e_2  =  9 (2 r² − a²)   on Brannen ansatz
V(Φ) = [e_1² − 6 e_2]²  =  81 (a² − 2 r²)²  =  81 (a² − 2|b|²)²
```

The polynomial form is **algebraically equivalent** to the Frobenius
equipartition condition `a² = 2|b|²`, which is exactly A1. The coefficient
`6` numerically matches `n(n−1)=3·2`, the off-diagonal-entry count for `n=3`.
The identity alone does not establish that count as the physical reason for
selecting this polynomial.

So "deriving 2/3 via polynomial structure" reduces to "deriving
`a² = 2|b|²` via Frobenius structure" — but that is exactly the
open Koide Frobenius-equipartition condition this route was supposed to
close. The polynomial framing is **not a new derivation**; it is the same
condition in different
coordinates.

### D5 check: named symmetric-polynomial candidates do not pick A1

The runner scans candidate symmetric-polynomial functionals on
`(e_1, e_2, e_3)`:

- **Discriminant** `Δ = 18 e_1 e_2 e_3 − 4 e_1³ e_3 + e_1² e_2² − 4 e_2³ − 27 e_3²`:
  at the explicitly chosen nondegenerate slice `(a=1, δ=2/9)`,
  `Δ ≠ 0` and `dΔ/dr |_A1 ≈ 43.80`. This is not phase-global;
  degenerate slices such as `δ=0` have `Δ=0`.
- **Tschirnhaus depressed cubic** `p = e_2 − e_1²/3`: At A1,
  `p = −3a²/2` (free parameter, no special vanishing).
- **Ratio `e_1²/e_2`**: equals 6 at A1 (BY CONSTRUCTION — this IS the
  polynomial form of A1); but `d/dr [e_1²/e_2] |_A1 ≈ 16.97` (not
  extremized).

At the stated test points these candidate derivatives do not select A1. This
is a finite scan, not a universal no-go; the discriminant conclusion is only
for `delta=2/9`. In particular `(e_1²-6e_2)²` has its global
minimum on A1 by construction, and using it physically would require a
separately justified selector.

## Why the 2/3 = 2/3 numerical match is not a derivation

Within the supplied circulant structure, the Brannen ansatz
holds, and the cosine-sum / cosine-squared-sum identities give
`p_1 = 3a` and `p_2 = 3a² + 6|b|²` exactly. The "6" coefficient in
`p_2 = 3a² + 6|b|²` IS structural (it's `n(n-1)` for n=3). But A1's
value `2/3` for the ratio `p_2/e_1²` requires the additional condition
`6|b|² = 3a²`, which is the Frobenius equipartition itself — the open
open condition.

So the pattern is:
- LHS = `p_2/e_1²` ranges freely in [1/3, ∞) for `a!=0` on this family.
- A1 condition forces this to 2/3 — which IS the value Koide observes
  in PDG charged-lepton masses.
- Both LHS and RHS evaluate to 2/3 BECAUSE A1 is imposed; not because
  Newton-Girard derives A1.

This is a consistency equality rather than a derivation, in the terminology of
`feedback_consistency_vs_derivation_below_w2.md`: "consistency
equality is not derivation."

## Counterfactual: alternative coefficient choices

The coefficient-zero family obeys, for `a!=0`,
`e_1²=C e_2 => kappa=C/(C-3)` when `C!=3` and `b!=0`:

- `e_1² = 6 e_2` gives `kappa = 2`, equivalently A1.
- `e_1² = 3 e_2` instead forces `b=0`, where `kappa` is undefined; it
  does **not** represent the `(1,2)` log-law extremum `kappa=1`.
- General coefficient zeros and weighted-log extrema are distinct families.

The algebra alone does not select `C=6`; imposing it is not a
Newton-Girard derivation.

## Comparison to Routes E and F (trap-profile contrast)

The runner explicitly verifies the comparison:

| Route | Trap value | Convention dependence | Profile |
|---|---|---|---|
| **E (Kostant Weyl-vector)** | `\|ρ_{A_1}\|²` | continuous: {1/4, 1/2, 1} under {\|α\|²=1, 2, 4} root-length conventions | continuous norm convention |
| **F (Casimir difference)** | `T(T+1) − Y²` | binary: {1/2, -1/4} under {Y_PDG, Y_SU5} hypercharge conventions | binary hypercharge convention |
| **D (Newton-Girard)** | `e_1² / e_2` | coefficient choice is not identified with the block-log weight family | distinct candidate families |

The listed/contextual E/F normalization examples and computed D
coefficient/weight examples are descriptively different. The runner does not
count a theorem claim that these
profiles are exhaustive or structurally identical.

## What this establishes

- **Narrow Newton-Girard result.** The identities alone leave the target ratio
  free, the displayed coefficient zero is a rewrite of A1, and the named
  candidate derivatives do not select A1.
- **Sharpens the bare candidate.** The prior "structurally suggestive, not
  closing" Newton-Girard rewrite is shown not to be a selector. Other
  justified polynomial or dynamical functionals remain outside this result.

## What this does NOT close

- The Koide Frobenius-equipartition condition remains an open, load-bearing
  step on the Brannen circulant lane.
- Route A (Koide-Nishiura quartic) remains the strongest open
  candidate (outside Theorem 6's cancellation).
- Charged-lepton Koide closure remains a bounded observational-pin
  package (status from
  [`CHARGED_LEPTON_MASS_HIERARCHY_REVIEW_NOTE_2026-04-17.md`](CHARGED_LEPTON_MASS_HIERARCHY_REVIEW_NOTE_2026-04-17.md)
  unchanged).
- The abstract Hermitian-circulant Fourier theorem
  ([`KOIDE_KAPPA_SPECTRUM_OPERATOR_BRIDGE_THEOREM_NOTE_2026-04-19.md`](KOIDE_KAPPA_SPECTRUM_OPERATOR_BRIDGE_THEOREM_NOTE_2026-04-19.md))
  retains only its exact polynomial identity and zero-locus equivalence on a
  defined abstract matrix. It does not identify either side with a physical
  mass spectrum, P1, MRU, or a charged-lepton carrier. This Route-D no-go
  continues to address whether Newton-Girard polynomial structure selects the
  displayed zero locus; it does not obtain a physical identification from the
  abstract Fourier identity.
- The block-total Frobenius source proposal
  ([`KOIDE_KAPPA_BLOCK_TOTAL_FROBENIUS_MEASURE_THEOREM_NOTE_2026-04-19.md`](KOIDE_KAPPA_BLOCK_TOTAL_FROBENIUS_MEASURE_THEOREM_NOTE_2026-04-19.md))
  supplies exact conditional functional algebra but no independent physical
  selector. This note does not change that boundary or its audit status.
- AC_φλ residual (substep 4) is unaffected.
- L3a trace-surface bounded obstruction status unchanged.

## Empirical falsifiability

| Claim | Falsifier |
|---|---|
| Newton-Girard identity (D1) | Demonstrate a 3-tuple of eigenvalues for which `p_2 ≠ e_1² − 2 e_2` (mathematically impossible — refutes any framework using NG). |
| Block-counting weight ambiguity (D2) | Derive a source-supported selection between (1,1) multiplicity and (1,2) dimensional weighting from existing axioms; that closes the open SO(2)-quotient / weight-class residue and would discharge D2. |
| Brannen ansatz + extra input (D3) | Derive a source-supported constraint pinning `\|b\|/a = 1/√2` from R1+R2 alone (gauge-only, no extra input); refutes D3. |
| Polynomial circularity (D4) | Find a polynomial expression in `(e_1, e_2, e_3)` that is NOT algebraically equivalent to `a² = 2\|b\|²` and STILL vanishes at A1; refutes D4. |
| Named-candidate scan (D5) | A named candidate tested here is falsified if its symbolic derivative actually vanishes at A1. Other functionals are outside this finite scan. |
| Numerical match (anchor) | Falsified if charged-lepton Koide Q deviates significantly from 2/3 in updated PDG; representative anchor values give `Q = 0.666661`, `Q_lin = 0.500005` (sub-0.001% match). |

## Review boundary

This note proposes `claim_type: bounded_theorem` for the independent
audit lane. The bounded theorem is the narrow Newton-Girard boundary: the
identities leave the ratio free, the displayed polynomial is a rewrite, and
the named finite candidate scan does not select A1. No exhaustive route
closure or new-axiom requirement is claimed.

No new premise or registry entry is proposed. The Koide
Frobenius-equipartition condition remains open and load-bearing on the Brannen
circulant lane. The
independent audit lane may retag, narrow, or reject this proposal.

## Promotion-Value Gate (V1-V5)

| # | Question | Answer |
|---|---|---|
| V1 | Verdict-identified obstruction closed? | The bare Newton-Girard candidate is narrowed to an identity-not-selection result; other selectors remain open. |
| V2 | New derivation? | The exact free-ratio and polynomial-rewrite identities are the substantive content. |
| V3 | Audit lane could complete? | Yes — the algebraic identities and each named candidate derivative are independently checkable. |
| V4 | Marginal content non-trivial? | Yes — the free-ratio identity and the exact rewrite expose why the coefficient-zero equation is not a selector. |
| V5 | One-step variant? | The note retains exact identities and finite candidate checks without claiming an exhaustive multi-wall no-go. |

**Source-note V1-V5 screen: pass for bounded-obstruction audit
seeding.**

## Retention boundary

Per `feedback_physics_loop_corollary_churn.md`, the user-memory rule
is to avoid one-step relabelings of already-landed cycles. This note:

- The exact free-ratio and polynomial-rewrite identities are preserved.
- The named candidate checks are finite and explicitly scoped; other
  polynomial/dynamical selectors remain open.
- The block-log weight family and coefficient-zero family are not identified.
- Sibling-route normalization tables and PDG values are context only and are
  not counted as Route-D theorem evidence.

## Cross-references

- A1 derivation status (parent): `KOIDE_A1_DERIVATION_STATUS_NOTE.md`
- Sister-route bounded obstructions:
  - Route F (Casimir difference): [`KOIDE_A1_ROUTE_F_CASIMIR_DIFFERENCE_BOUNDED_OBSTRUCTION_NOTE_2026-05-08_routef.md`](KOIDE_A1_ROUTE_F_CASIMIR_DIFFERENCE_BOUNDED_OBSTRUCTION_NOTE_2026-05-08_routef.md)
  - Route E (Kostant Weyl-vector): see commit b38cccbb9 (filename `KOIDE_A1_ROUTE_E_KOSTANT_WEYL_BOUNDED_OBSTRUCTION_NOTE_2026-05-08_routee.md`)
- Abstract Hermitian-circulant Fourier invariant (finite algebra only): [`KOIDE_KAPPA_SPECTRUM_OPERATOR_BRIDGE_THEOREM_NOTE_2026-04-19.md`](KOIDE_KAPPA_SPECTRUM_OPERATOR_BRIDGE_THEOREM_NOTE_2026-04-19.md)
- Block-total Frobenius (source proposal; current ledger unaudited): [`KOIDE_KAPPA_BLOCK_TOTAL_FROBENIUS_MEASURE_THEOREM_NOTE_2026-04-19.md`](KOIDE_KAPPA_BLOCK_TOTAL_FROBENIUS_MEASURE_THEOREM_NOTE_2026-04-19.md)
- MRU demotion (related residue): [`KOIDE_MRU_DEMOTION_NOTE_2026-04-20.md`](KOIDE_MRU_DEMOTION_NOTE_2026-04-20.md)
- Circulant character derivation: [`KOIDE_CIRCULANT_CHARACTER_DERIVATION_NOTE_2026-04-18.md`](KOIDE_CIRCULANT_CHARACTER_DERIVATION_NOTE_2026-04-18.md)
- Charged-lepton Koide-cone algebraic equivalence: [`CHARGED_LEPTON_KOIDE_CONE_ALGEBRAIC_EQUIVALENCE_NOTE.md`](CHARGED_LEPTON_KOIDE_CONE_ALGEBRAIC_EQUIVALENCE_NOTE.md)
- CL3 SM embedding: [`CL3_SM_EMBEDDING_THEOREM.md`](CL3_SM_EMBEDDING_THEOREM.md)
- One-Higgs gauge selection: [`SM_ONE_HIGGS_YUKAWA_GAUGE_SELECTION_THEOREM_NOTE_2026-04-26.md`](SM_ONE_HIGGS_YUKAWA_GAUGE_SELECTION_THEOREM_NOTE_2026-04-26.md)
- Direct Ward-free Yukawa no-go: [`CHARGED_LEPTON_DIRECT_WARD_FREE_YUKAWA_NO_GO_NOTE_2026-04-26.md`](CHARGED_LEPTON_DIRECT_WARD_FREE_YUKAWA_NO_GO_NOTE_2026-04-26.md)
- Substep 4 AC narrowing: [`STAGGERED_DIRAC_SUBSTEP4_AC_NARROW_BOUNDED_NOTE_2026-05-07_substep4ac.md`](STAGGERED_DIRAC_SUBSTEP4_AC_NARROW_BOUNDED_NOTE_2026-05-07_substep4ac.md)
- Three-generation observable: [`THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md`](THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md)
- Physical lattice baseline: [`PHYSICAL_LATTICE_FOUNDATIONAL_INTERPRETATION_NOTE_2026-05-08.md`](PHYSICAL_LATTICE_FOUNDATIONAL_INTERPRETATION_NOTE_2026-05-08.md)
- Higher-order structural theorems: [`HIGHER_ORDER_STRUCTURAL_THEOREMS_NOTE.md`](HIGHER_ORDER_STRUCTURAL_THEOREMS_NOTE.md)
- MINIMAL_AXIOMS: `MINIMAL_AXIOMS_2026-06-29.md`
- Brocard fingerprint analog (different lane): [`CKM_BROCARD_POLYNOMIAL_VIETA_STRUCTURAL_INTEGERS_THEOREM_NOTE_2026-04-25.md`](CKM_BROCARD_POLYNOMIAL_VIETA_STRUCTURAL_INTEGERS_THEOREM_NOTE_2026-04-25.md) — uses Newton-Girard structural integer fingerprint `p_2 = 2 e_1²` for N_pair = 2 in the CKM lane; analogous machinery, different content; NOT directly transferable to Koide A1.

## Validation

```bash
python3 scripts/cl3_koide_a1_route_d_newton_girard_2026_05_08_routed.py
```

Expected output: computed verification of (i) Newton-Girard identity
universality (any 3-tuple of eigenvalues), (ii) Barrier D1 (NG is
identity, not constraint), (iii) Barrier D2 ((1,1)-vs-(1,2) weight
ambiguity), (iv) Barrier D3 (Brannen ansatz + extra input required),
(v) D4 (polynomial-coefficient rewrite), and (vi) the named D5 candidate
derivatives. E/F tables, prose boundaries, and PDG anchors are displayed but
uncounted. Total: 20 computed PASS / 0 FAIL.

Cached: [`logs/runner-cache/cl3_koide_a1_route_d_newton_girard_2026_05_08_routed.txt`](../logs/runner-cache/cl3_koide_a1_route_d_newton_girard_2026_05_08_routed.txt)

## User-memory feedback rules respected

- `feedback_consistency_vs_derivation_below_w2.md`: this note
  specifically applies the "consistency equality is not derivation"
  rule. The numerical match `2/3 = 2/3` is a consistency equality,
  not a structural Newton-Girard identity, and the proposed
  identification cannot load-bear A1 closure on this basis.
- `feedback_hostile_review_semantics.md`: this note stress-tests the
  semantic claim that "the polynomial coefficient `6` is structurally
  forced" by showing that its zero is exactly the target condition; no
  physical selector follows from that rewrite.
- `feedback_retained_tier_purity_and_package_wiring.md`: no automatic
  cross-tier promotion. This note is a bounded obstruction; the
  parent Koide Frobenius-equipartition condition remains open. No
  authority-tier promotion implied.
- `feedback_physics_loop_corollary_churn.md`: the exact free-ratio and
  polynomial-rewrite identities, plus named candidate derivatives, are the
  substantive scientific content.
- `feedback_compute_speed_not_human_timelines.md`: alternative routes
  (A primarily) characterized in terms of WHAT additional content
  would be needed (weight-class selection or extremization principle),
  not how-long-they-would-take.
- The runner counts only recomputed algebra; synthesis and empirical anchors
  remain visible but uncounted.
- `feedback_bridge_gap_fragmentation_2026_05_07.md`: Route D's failure
  identifies that "polynomial-coefficient" candidates — like the
  Casimir-difference / Weyl-vector candidates — are not free of
  convention-dependence traps; they face their own variant. This
  fragments the bridge gap into more honestly-named pieces.
