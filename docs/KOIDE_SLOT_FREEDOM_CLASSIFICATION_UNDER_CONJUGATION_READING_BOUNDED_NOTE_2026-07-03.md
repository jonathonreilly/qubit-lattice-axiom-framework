# Slot-Freedom Classification Under The Hypothetical Conjugation Reading

**Date:** 2026-07-03
**Type:** open_gate
**Claim type:** open_gate (bounded classification conditional on hypothetical H-conj; the remaining slot-weighting decision is not discharged here).
**Audit boundary:** audit lane owns any formal verdict; this note records only
the repaired classification wording.
**Primary runner:** [`scripts/frontier_koide_slot_freedom_classification_2026_07_03.py`](../scripts/frontier_koide_slot_freedom_classification_2026_07_03.py)

This note uses hypothetical H-conj only as a prepared reading for owner
decision. The hypothetical H-conj sentence is: "The supplied algebraic structure
includes its conjugation; presentations differing by conjugation present the
same possibility." Nothing in this note lands hypothetical H-conj, changes
axiom text, or sets an audit outcome.

Under hypothetical H-conj, conjugate configurations are one possibility. That
decides P-phase in the negative for this classification. P-transport is assumed
at the doublet grade. The remaining question is the slot convention: one slot
per possibility gives `r = 1/2`, while one slot per real coordinate gives
`r = 1`.

## Source Anchors

The w template
([`W_SCALE_ABSORPTION_TWO_CELL_READOUT_CLASSIFICATION_BOUNDED_NOTE_2026-07-02.md`](W_SCALE_ABSORPTION_TWO_CELL_READOUT_CLASSIFICATION_BOUNDED_NOTE_2026-07-02.md))
supplies the inventory method:

```text
Each row is classified only under its stated premise:
```

The custody chain
([`CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02.md`](CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02.md))
supplies the exact lever:

```text
exact `Q = 1/3 + (2/3)r`, `r=\|b\|²/a²`
```

The staggered realization note
([`KOIDE_STAGGERED_FIRST_ORDER_GENERATION_DETERMINANT_BOUNDED_THEOREM_NOTE_2026-06-11.md`](KOIDE_STAGGERED_FIRST_ORDER_GENERATION_DETERMINANT_BOUNDED_THEOREM_NOTE_2026-06-11.md))
supplies the measure-order fact:

```text
the partition function is `det(D + A)` to the
**first power** (checks 6–7).
```

It also localizes the count-twice term:

```text
on the K-real line
`c = b̄` the Wirtinger derivative `∂² det₃ / ∂b ∂b̄ = −3a`
(Laplacian `−12a`) — the count-twice `|b|²` term of the rank-2 modulus
wall appears exactly there (check 15).
```

The same source states the horn-neutrality boundary:

```text
the fork relocated, not resolved
What remains is not a measure-order question at all.
Neither horn is derived here
```

The factorization source
([`KOIDE_OCCUPANCY_DERIVED_FROM_POSSIBILITY_INDIVIDUATION_BOUNDED_NOTE_2026-07-03.md`](KOIDE_OCCUPANCY_DERIVED_FROM_POSSIBILITY_INDIVIDUATION_BOUNDED_NOTE_2026-07-03.md))
names the three premises:

```text
P-transport: the one-site individuation discipline transports to the derived generation doublet.
P-phase: record content fixes the orbit magnitude `|b|^2` and not the conjugate-sector relative phase.
P-occupancy: one admissible possibility supplies one statistical slot.
```

## Readout Inventory Classification

The slot bit is evaluated through the custody lever
`Q(r) = 1/3 + (2/3)r = (1 + 2r)/3`. Therefore:

```text
Q(1) = 1
Q(1/2) = 2/3
Q(1) - Q(1/2) = 1/3
Q(1) / Q(1/2) = 3/2
```

| Readout from the w inventory | Does the landed formula consume `r`? | Classification | Value at `r = 1` | Value at `r = 1/2` |
|---|---|---|---|---|
| EW shape `g1^2/(g1^2+g2^2)`, read as `sin^2 theta_W` on its stated context | No. The listed formula has no Koide `r` input. | SLOT-DEAD | `g1^2/(g1^2+g2^2)` | `g1^2/(g1^2+g2^2)` |
| Koide-shape witness | Yes. It is exactly the degree-zero shape `Q(r)`. | SLOT-ALIVE | `1` | `2/3` |
| Mass ratios | Yes, once the chain reads masses as `m_k = lambda_k^2` on the circulant surface. With the landed phase `delta = 2/9`, the scale-free entries have `m_k(r) proportional to (1 + 2*sqrt(r)*cos(2/9 + 2*pi*k/3))^2`, for `k = 0,1,2`. | SLOT-ALIVE | `(1 + 2*cos(2/9 + 2*pi*k/3))^2`, up to one common scale | `(1 + sqrt(2)*cos(2/9 + 2*pi*k/3))^2`, up to one common scale |
| Calibrated absolute mass vector | The calibration unit itself is a scale choice, but every non-reference member inherits the mass-ratio dependence on `r`. | SLOT-ALIVE for the calibrated vector away from the chosen reference | `M_j*(1 + 2*cos(2/9 + 2*pi*k/3))^2/(1 + 2*cos(2/9 + 2*pi*j/3))^2` | `M_j*(1 + sqrt(2)*cos(2/9 + 2*pi*k/3))^2/(1 + sqrt(2)*cos(2/9 + 2*pi*j/3))^2` |
| `8/9` central-sector count | No. The w template treats it as a cardinality fact, not an inter-sector weight. | SLOT-DEAD | `8/9` | `8/9` |

The theta mass-side composition in the factorization source consumes the
K-real reading and the P-transport, P-phase, and P-occupancy premise structure.
It does not consume `r` as an independent readout variable. Its consequence
reports `r = 1/2` after the orbit grading has already been selected; it is not a
separate formula `F(r)` whose value is evaluated at both slot conventions.

The w note's residual triple is not an additional landed readout formula. It
lists off-diagonal evaluation, cross-family comparison without common
calibration, and raw absolute normalization not routed through the
scale-reference primitive. This note classifies the listed current-source
readouts and does not invent formulas for those residual contexts.

## Absorbability

The w freedom is absorbable on the diagonal because it enters as a common
prefactor. The slot bit does not have that form. It enters the Koide shape as
the affine lever `Q(r) = 1/3 + (2/3)r`.

A common rescaling of masses cannot absorb the difference. For any common
positive factor `alpha`,
`Q(alpha*m) = alpha*sum(m)/(sqrt(alpha)*sum(sqrt(m)))^2 = Q(m)`. The exact
shape values still differ:

```text
r = 1      gives Q = 1
r = 1/2    gives Q = 2/3
```

Therefore the slot bit is not an overall scale convention. It is visible to a
ratio readout before any absolute mass unit is chosen. The same obstruction
propagates to mass ratios and to calibrated absolute masses, because a
calibrated vector would otherwise have the same degree-zero Koide shape.

## Dynamical Discharge Test: REFUTED -- the fork stands

An adversarial seat refuted the discharge form; this section is the repaired
wording.

The June 11 staggered realization note shows that the actual one-component
matter measure produces a first-order determinant. It does not produce
`|det|^2`; the count-twice term appears on the K-real restriction of coupling
parameters. The source says the count-twice structure "is supplied by the
**parameter restriction** `c = b̄`," the K-reality selector already named as an
operative admitted input.

That first-order determinant is horn-neutral. Read on the K-real section
(`c = b̄`, the Hermitian channel), the doublet contributes the `|b|^2`
two-real-coordinate Gaussian weight, `Z` proportional to `2pi/g`, giving
`r = 1` and `Q = 1`. Read on the conjugate-orbit quotient, the same `det^1`
object contributes the single-slot weight, `Z` proportional to `pi/g`, giving
`r = 1/2` and `Q = 2/3`.

The source's own boundary sentences are decisive: "What remains is not a
measure-order question at all"; "the fork relocated, not resolved"; "Neither
horn is derived here." The landed measure-order computation decides nothing
between the horns.

Under hypothetical H-conj, the conjugate pair is one possibility. That
hypothetical H-conj reading supplies the orbit reading; it does not eliminate
the weighting input. The occupancy content is carried by hypothetical H-conj
plus that orbit reading, not eliminated by the dynamics. The K-real-section
reading remains available unless hypothetical H-conj, with the orbit reading it
carries, is adopted.

The custody K-reality selector is therefore re-consumed, not discharged. The
source residual about the declared probe coupling is also inherited whenever
the question is expanded from slot counting to a full generation-Yukawa
derivation.

The static no-go source
([`KOIDE_R_HALF_POLARIZATION_SELECTOR_TESTED_STATIC_READOUT_NO_GO_NOTE_2026-06-08.md`](KOIDE_R_HALF_POLARIZATION_SELECTOR_TESTED_STATIC_READOUT_NO_GO_NOTE_2026-06-08.md))
and the orbit-occupancy source
([`KOIDE_ORBIT_OCCUPANCY_INDEPENDENCE_AND_PREMISE_CANDIDATE_NOTE_2026-06-09.md`](KOIDE_ORBIT_OCCUPANCY_INDEPENDENCE_AND_PREMISE_CANDIDATE_NOTE_2026-06-09.md))
are used only for the quoted negative-boundary and arithmetic checks exercised
by the runner. The current axiom context is
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md); this note does
not modify it.

## Decision Surface

In this modeled hypothetical H-conj stack, the conjugation clause buys
individuation only. One bit of genuine physical input remains:
per-possibility versus per-real-coordinate weighting of the realized measure.

Among the listed current-source readouts, that bit is alive on the flavor
readouts classified above. The Koide shape changes from `Q = 1` under the
per-real-coordinate reading to `Q = 2/3` under the per-possibility reading.
Mass ratios and calibrated absolute mass vectors inherit the same `r`
dependence. The EW shape formula and the `8/9` central-sector count do not
consume this bit.

Nothing in Part 2 absorbs the bit. A common mass rescaling leaves `Q`
unchanged, so the exact ratio readout still separates the two readings.

Within this lane model, two owner-facing options remain.

Option (a): add a new axiom sentence supplying the one-slot weighting. Its
intent defense is weak: the static no-go source treats "No possibility is
privileged" as not naming a weighting, and that is a hostile precedent for
this route.

Option (b): keep the bit as the flavor admission's remaining sharply
factorized content. Under hypothetical H-conj, the admission's piece narrows to
this one bit plus the transport statement.

This note does not supply a third route in this lane. The three tested
derivation attempts from measure-neutrality, individuation, and measure-order
remain non-discharging in the cited sources: June 8 static, July 3
individuation, and July 3 discharge.

## Runner

Run:

```bash
python3 scripts/frontier_koide_slot_freedom_classification_2026_07_03.py
```

Expected terminal form: `CHECK NN: PASS/FAIL -- <description>` lines,
`TOTAL: PASS=<n> FAIL=0`, then five `SUMMARY` lines naming files/check count,
the horn-neutrality exhibit, owner option (a), owner option (b), and
uncertainties.
