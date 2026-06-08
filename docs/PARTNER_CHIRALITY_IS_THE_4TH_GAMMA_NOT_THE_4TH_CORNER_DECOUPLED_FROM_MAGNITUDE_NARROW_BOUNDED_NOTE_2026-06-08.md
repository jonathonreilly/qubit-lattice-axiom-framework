# The Partner Chirality Is the 4th Clifford Gamma, Not the 4th Species Corner — Decoupled from the Magnitude Wall

**Date:** 2026-06-08
**Claim type:** bounded_theorem (a decoupling / keystone residual-narrowing)
**Status authority:** independent audit lane only. This source note does not set, predict, or
estimate any audit verdict. Effective status is pipeline-derived after independent audit and
dependency closure.
**Primary runner:**
[`scripts/frontier_partner_chirality_gamma_not_corner.py`](../scripts/frontier_partner_chirality_gamma_not_corner.py)
**Cached log:**
[`logs/runner-cache/frontier_partner_chirality_gamma_not_corner.txt`](../logs/runner-cache/frontier_partner_chirality_gamma_not_corner.txt)
(TOTAL: PASS=9 FAIL=0)

## 0. The last brick, and its resolution

The keystone — the emergent-time massive Dirac field that gates the chirality gate, the `Q=2/3`
chiral-mass mechanism, generation-ID, and the program's #1 `s3_time` gate — was reduced to one
sharp question: **does the framework's continuous emergent time supply the 4th Clifford direction
`e_4` the partner chirality needs, or does it face the magnitude lane's "missing 4th Euclidean
corner" wall** (where continuous time gives native count 8, not 16:
[`MAGNITUDE_TEMPORAL_FACTOR_IS_COUNT_NOT_RATE_2026-06-06`](MAGNITUDE_TEMPORAL_FACTOR_IS_COUNT_NOT_RATE_2026-06-06.md))?

**They are different doublings, and they decouple.** The partner chirality needs a 4th Clifford
**gamma**; the magnitude's `×2` needs a 4th lattice **species corner**. Continuous emergent time
supplies the gamma (a time *direction*) but not the corner (no discrete time *lattice*) — and the
partner chirality needs only the gamma. So the partner chirality is **available** from continuous
emergent time and is **not** blocked by the magnitude wall.

## 1. Inputs and live tiers (verified on `origin/main`, 2026-06-08)

| Input | Source | Live `effective_status` | Role |
|---|---|---|---|
| `Cl(3,0)→Cl(3,1)=M_4(R)` (adjoin `e_4`, `e_4²=−1`): the 4th Clifford gamma / Dirac doubling | [`CL3_TO_CL31_SPINOR_EXTENSION_NARROW_THEOREM_NOTE_2026-05-27`](CL3_TO_CL31_SPINOR_EXTENSION_NARROW_THEOREM_NOTE_2026-05-27.md) | `retained` | structure (A): the partner-chirality gamma |
| naive lattice fermion has `2^d` doubler species (BZ corners) | [`NAIVE_LATTICE_FERMION_TWO_POWER_D_SPECIES_COUNT_NARROW_THEOREM_NOTE_2026-05-10`](NAIVE_LATTICE_FERMION_TWO_POWER_D_SPECIES_COUNT_NARROW_THEOREM_NOTE_2026-05-10.md) | `retained` | structure (B): the species corners |
| continuous emergent time gives native count 8 not 16 (no 4th Euclidean corner) | [`MAGNITUDE_TEMPORAL_FACTOR_IS_COUNT_NOT_RATE_2026-06-06`](MAGNITUDE_TEMPORAL_FACTOR_IS_COUNT_NOT_RATE_2026-06-06.md) | `retained_bounded` | the magnitude wall (B-side) |
| the partner-chirality / massive-doubling field residual | [`KOIDE_ONSITE_BOOST_RECONSTRUCTION_WEYL_FAITHFUL_VS_SCALAR_SELECTION_NOTE_2026-06-02`](KOIDE_ONSITE_BOOST_RECONSTRUCTION_WEYL_FAITHFUL_VS_SCALAR_SELECTION_NOTE_2026-06-02.md) | `retained_bounded` | the keystone whose residual this narrows |

No PDG value is load-bearing. No new axiom, import, or vocabulary.

## 2. Two distinct doublings

**(A) The SPINOR doubling — the 4th Clifford gamma.** Adjoining the 4th Clifford generator
`e_4` (`Cl(3,0)→Cl(3,1)`, retained) takes the 2-component Weyl spinor of one qubit to the
4-component Dirac bispinor, with the chiral grading `γ_5` — the **partner chirality** (verified:
the qubit is one 2-component Weyl chirality; the `e_4` extension gives the 4-component bispinor
with `Tr γ_5 = 0`, `γ_5²=I`, balanced L/R). This is a **Clifford-algebra fact** — four generators,
no momentum.

**(B) The SPECIES doubling — the 4th lattice direction.** The naive lattice Dirac operator
`D(k) ~ Σ_μ γ_μ sin(k_μ)` has a doubler at each BZ corner `k_μ ∈ {0,π}` (where every `sin(k_μ)=0`),
hence `2^d` species (retained). Three spatial dimensions give `2^3 = 8`; a 4th **lattice**
direction gives `2^4 = 16` — and that 16th-vs-8th `×2` is precisely the magnitude lane's "4th
Euclidean corner." This is a **momentum-space doubler count** — two corners per *discrete*
direction (`sin(k)=0` at `k∈{0,π}`).

**Distinct objects.** (A) is a `4×4` Clifford generator (spinor `2→4`); (B) is an `8→16`
momentum-corner count. Adding a gamma is not adding a lattice direction.

## 3. Continuous emergent time supplies the gamma, not the corner

A **direction** in spacetime carries a Clifford gamma: continuum Dirac is `iγ⁰∂_t + iγ^i∂_i + …`
— the time direction provides `γ⁰ = e_4` (structure A), with `∂_t` **continuous**. A **discrete
lattice** in a direction provides `sin(k_μ)` and its `k_μ=π` doubler corner (structure B).

The framework's emergent time is a **continuous direction** (the monotone record-accumulation
arrow), not a discrete time lattice. Therefore it supplies:
- the time gamma `e_4` (structure A) — **present** (the retained `Cl(3,1)` extension is exactly
  this), and
- **no** `sin(k_4)` doubler — so the 4th species corner (structure B) is **absent** (the magnitude
  lane's native-8 finding).

## 4. The decoupling — the partner chirality is available

The partner chirality (the 4-component Dirac bispinor / chiral grading) needs **only structure
(A)** — the 4th gamma `e_4`. The magnitude's `×2` needs **structure (B)** — the 4th species corner.
Since continuous emergent time supplies (A) but not (B):

> The partner chirality is **available** from the framework's continuous emergent time (via the
> retained `e_4` time gamma) and is **not** blocked by the magnitude lane's missing-4th-corner wall.
> The two residuals are **decoupled** — they are different doublings (spinor gamma vs species
> corner).

This **narrows the keystone**: the chirality degree of freedom is supplied, so the emergent-time
massive Dirac field's remaining residual is the **field construction** — the spectrum condition
(positive energy) and microcausality of the massive field on the reconstructed Hilbert space —
**not** the chirality, and **not** the magnitude's species-count wall.

## 5. Scope — what this establishes and what remains

**Establishes (exact / finite):**
- The partner chirality is the 4th Clifford gamma `e_4` (spinor doubling `2→4`), a retained
  `Cl(3,1)` algebra fact — distinct from the species-corner doubling.
- Continuous emergent time (a time direction) supplies the gamma `e_4` but not the `k_4` species
  corner.
- Therefore the partner chirality is available and decoupled from the magnitude's missing-corner
  wall.

**Remains (the keystone's narrowed residual):**
- The **field construction**: realizing the retained `Cl(3,1)` doubling as a positive-energy,
  microcausal massive Dirac field on `Z³`+emergent-time (the onsite-boost residual). This note
  removes the chirality-DOF / continuous-time worry from it; the spectrum condition and
  microcausality remain.
- It does **not** build the field; it resolves *one* sub-question (the `e_4`-vs-`k_4` decoupling)
  and does not touch the firewalled `r=1/2`.

## 6. Honest verdict

The keystone's last brick — "does continuous emergent time supply the partner chirality's `e_4`,
or hit the magnitude's missing-corner wall?" — resolves: **the partner chirality is the 4th
Clifford *gamma*, not the 4th species *corner*.** Continuous emergent time supplies the gamma (a
direction) but not the corner (a lattice); the partner chirality needs only the gamma; so it is
available and **decoupled** from the magnitude wall. The chirality DOF of the keystone is supplied;
what remains is purely the positive-energy / microcausal field construction. The deepest residual
of the program is now narrowed to one field-theoretic object, with its chirality and species-count
sub-questions both settled.

## 7. No-Go Discipline Gate

**Status:** PASS for this bounded decoupling. It does **not** claim the massive field is built; it
claims the chirality DOF is supplied and decoupled from the magnitude's species wall.

**N1 — Alternative-route enumeration.**

| Route | Marker | Result |
|---|---|---|
| partner chirality = 4th species corner (same as magnitude `×2`) | RULED OUT | spinor gamma `≠` species corner (different doublings) |
| continuous time gives no `e_4` (chirality blocked) | RULED OUT | a time direction gives `γ⁰=e_4` (retained `Cl(3,1)`) |
| continuous time gives the `k_4` corner | RULED OUT | continuous `∂_t` has no `sin(k_4)` doubler (magnitude lane) |
| the field construction (positive energy + microcausality) | OPEN (narrowed keystone) | the remaining residual |

**N2 — Wall-independence.** The chirality DOF (this note), the magnitude species count, and the
field construction are distinct; resolving the first decouples it from the second and narrows the
third.

**N3 — Hidden-wall scan.** Uses only the Clifford `e_4` extension (retained), the `2^d` species
count (retained), and the continuum-vs-lattice distinction (a gamma is a direction, a corner is a
lattice doubler) — no hidden premise.

**N4 — Residual matching.** The remaining residual is the positive-energy / microcausal field
construction, not the chirality and not the species count.

**N5 — Rhetoric audit.** The claim is a *decoupling* (different doublings) and an *availability*
(the gamma from a direction), not a construction of the massive field.

**N6 — Partial-closure path scan.** The next step is the spectrum condition + microcausality of the
massive field on the reconstructed Hilbert space (the onsite-boost / OS-reconstruction surface). No
new axiom requested.

**N7 — Steelman.** A reviewer may hold that the framework's emergent time, being a *parameter* (the
record count), is not a geometric *direction* carrying a gamma. The retained `Cl(3,1)` extension
(`CL3_TO_CL31`) is exactly the statement that the framework adjoins the 4th `e_4` generator; this
note uses that retained structure, and shows only that it is the *gamma* (A), not the *corner* (B)
— so it does not assume more than is retained.

**N8 — Cross-cycle echo.** Consistent with the retained `Cl(3,1)` extension, the retained `2^d`
species count, the retained-bounded magnitude count-not-rate finding, and the retained-bounded
onsite-boost residual — connecting them without overruling any by prose.

## 8. Forbidden-imports check

- **No new axioms / imports / vocabulary.** Inputs are the cited retained / retained-bounded rows
  plus the Clifford-algebra and naive-lattice-doubler facts.
- **No PDG/fitted load-bearing input; no new transcendental; no forcing of `r=1/2`.**

## 9. Command

```bash
python3 scripts/frontier_partner_chirality_gamma_not_corner.py
```

Expected: `TOTAL: PASS=9 FAIL=0`. numpy + stdlib, deterministic, ≤16-dim (memory-safe). The runner
verifies the spinor doubling (`Cl(3,0)→Cl(3,1)`, `2→4` with `γ_5`), the species-corner count
(`2^d`, `8→16`), their distinctness, that continuous time supplies the gamma but not the corner,
and the decoupling.
