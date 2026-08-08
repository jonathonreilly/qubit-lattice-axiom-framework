# Pressure-test A of a candidate maximal-unlock record axiom — the dial is real, r=1/2 is the SYMMETRIC stationary point (corrected symmetry), and the multi-lane reading is CONSISTENT without overreach

**Date:** 2026-06-04
**Claim type:** meta
**Claim boundary:** a pressure-test (not an adoption) of a candidate record-axiom *consequence* — verifies the dial structure, the genuine dial symmetry and its fixed point, the arrow-dependent stability, and the per-sector multi-lane no-overreach. Consumes no PDG value to derive anything; observed Koide Q's enter only as labelled observational inputs for a consistency comparison. No axiom and no import is adopted.
**Status authority:** independent audit lane only; effective status is pipeline-derived after audit. This note proposes nothing for promotion and writes no audit verdict.
**Runner:** [`scripts/record_axiom_ptA_dial_stability_multilane_2026_06_04.py`](../scripts/record_axiom_ptA_dial_stability_multilane_2026_06_04.py) (SCORECARD PASS=31, FAIL=0).
**Cache:** [`logs/runner-cache/record_axiom_ptA_dial_stability_multilane_2026_06_04.txt`](../logs/runner-cache/record_axiom_ptA_dial_stability_multilane_2026_06_04.txt).

## The candidate axiom under test (NOT adopted)

> *A record is an irreversible registration of which REAL (CPT-even) superselection sector is realized.*

Consequence (iii), the object of this pressure-test: the sector-weight is a **free dial** `r = |b|²/a² ∈ [0,∞)`;
the **equipartition** weight (equal real-block count → `r=1/2` → `Q=2/3`) is the **symmetric stationary point**;
the **extremal** weights (`r=0`→`Q=1/3`, `r=1`→`Q=1`) are **broken stationary points**; each fermion sector
occupies the stationary point compatible with its symmetry.

This is the **maximal-unlock / multi-lane** reframe: we do **not** force `r=1/2`; we show it is a distinguished
(symmetric) point on a dial, **not exclusive** — other sectors occupy other points. The earlier **forcing**
version was falsified because quarks/neutrinos are not at `Q=2/3`. This note tests whether the multi-lane
version survives honestly.

## The dial + Q map (Pillar 1)

For the `C₃`-equivariant Hermitian circulant `H = aI + bC + b̄C²` on `hw=1 ≅ ℂ³`,
`Q = Tr H²/(Tr H)² = 1/3 + (2/3)r` exactly (the `Q=2/3 ⟺ r=1/2` biconditional is **retained** on
origin/main — `CHARGED_LEPTON_KOIDE_CONE_ALGEBRAIC_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-10`). With the
2-sector power fractions `p_s = ‖aI‖²/(‖aI‖²+‖bC+b̄C²‖²) = 1/(1+2r)` and `p_d = 2r/(1+2r)`:

| dial point | Q | isotype weight (singlet:doublet) | (p_s, p_d) | spectrum | reading |
|---|---|---|---|---|---|
| `r=0` | `1/3` | `(1:0)` | `(1, 0)` | `[1,1,1]` | pure singlet / democratic / `S₃`-degenerate |
| `r=1/2` | `2/3` | `(1:1)` equal block power | `(½, ½)` | `[2.41,0.29,0.29]` | **equipartition / charged leptons** |
| `r=1` | `1` | `(1:2)` dimension/Plancherel | `(⅓, ⅔)` | `[3,0,0]` | Born/dimension / one-dominant / two massless |

## r=1/2 is the SYMMETRIC stationary point — with a corrected symmetry (Pillar 2)

The honest landmine: the prior note `FLAVOR_R_HALF_STABLE_UNDER_THERMALIZING_ARROW_2026-06-02` correctly
found the involution `r↔1−r` (i.e. `|b|²→a²−|b|²`) is **not** a dial symmetry — it changes `Tr H²`
(`4.8` vs `7.2`) — and therefore (correctly, given only that candidate) concluded the stability "rests on
equipartition + endpoint-exclusion + the entropy arrow, *not* on symmetry-protection."

This note supplies the **genuine** dial symmetry that prior note was missing. The natural symmetry is the
**singlet↔doublet power-block exchange** `p_s ↔ p_d` on the 2-sector simplex. Since `p_d/p_s = 2r`, the swap
sends `2r → 1/(2r)`, i.e. it acts on the dial as

> **the block-swap `r → 1/(4r)`.**

Verified facts (runner Pillar 2):
- `r → 1/(4r)` is a **genuine involution** (`swap∘swap = id`) and **exactly exchanges** `p_s ↔ p_d`.
- Its **unique fixed point** on `(0,∞)` is `r=1/2` (`r = 1/(4r) ⟹ r² = ¼`), the equipartition configuration
  `p_s = p_d = ½`.
- The 2-sector entropy `S₂` is **exactly invariant** under `r → 1/(4r)` (entropy is symmetric in its two
  arguments), and `S₂` is **stationary and maximal** (`= ln 2`) precisely at `r=1/2`.

So `r=1/2` **is** the unique fixed point of a real involutive dial symmetry, and the symmetry-respecting
potential `S₂` is extremized there. The prior note's `r↔1−r` and this `r→1/(4r)` happen to **share** the
fixed point `r=1/2` but disagree everywhere else; only `r→1/(4r)` is an actual symmetry of the structure.
This **strengthens** the prior result: there *is* a symmetry-protection statement, on the correct involution.

## Stability is arrow-dependent (Pillar 3, honest)

The framework has two known record-flows, and `r=1/2`'s stability is **arrow-dependent** (both flows are
already bounded_theorems on origin/main):

- **Records/Lüders sharpening** `r → 2r²` (observer / entropy-*decreasing*): fixed points `r=0`
  (`f'=0`, **stable**) and `r=1/2` (`f'=2`, **unstable separatrix**). The repelling watershed between the
  degenerate (`r=0`) and hierarchy (`r→∞`) basins.
- **Closed-system thermalizing** `g(r)=√(r/2)` (second-law / entropy-*increasing*, the time-reverse):
  `r=1/2` is the **stable global attractor** (`g'(1/2)=½`); every seed flows there.

Reversing the entropy arrow flips repeller↔attractor at the **same** fixed point `r=1/2`. **Honest verdict
label: SYMMETRIC-STATIONARY** — `r=1/2` is *unconditionally* the symmetry-fixed point and the `S₂` extremum,
but calling it "stable" requires naming the (thermalizing) arrow. It is **not** a bare attractor; it is a
**symmetric stationary point** that is also the thermalizing equilibrium.

## THE NO-OVERREACH TEST (Pillar 4, decisive)

Per-sector `r = (3Q−1)/2` from **observed** Koide `Q` (clearly labelled **inputs**, repo-sourced — a
consistency comparison, not a fit). Sources: charged/up/down from
`QUARK_MASS_SPECTRUM_KOIDE_SCHEME_OPEN_GATE_NOTE_2026-05-26`; neutrinos (normal-ordering sweep `Q ∈ [1/3, 0.585]`,
"never reaches `2/3`") from `FLAVOR_BOTH_READINGS_CHARGE_SELECTS_NOTE_2026-05-30`.

| sector | observed Q (input) | r = (3Q−1)/2 | dial point |
|---|---|---|---|
| **charged leptons** | `0.66666` | `0.49999` | **AT the symmetric point `r=1/2`** (equipartition) |
| up quarks | `0.848` | `0.772` | broken — hierarchy side `r>1/2` |
| down quarks | `0.731` | `0.597` | broken — hierarchy side `r>1/2` |
| neutrinos (NO) | `[1/3, 0.585]` | `[0, 0.378]` | broken — degenerate side `r<1/2` |

- **Charged leptons are uniquely at the symmetric point** (`|r−½| < 10⁻⁴`); every other sector is
  off-symmetric.
- **No non-charged sector lands at `r=1/2` (`Q=2/3`).** The falsified **forcing** version put *every* sector
  at `Q=2/3`; the multi-lane version does **not** — so it **does not overreach**.
- The breaking is **sector-correlated** (a consistency narrative, **explicitly not a derivation**): colored
  quarks (QCD dresses the doublet block) sit on the hierarchy side `r>1/2`; neutrinos (Majorana/seesaw
  structure) sit on the degenerate side `r<1/2`. Charged leptons — the only color-singlet, electrically
  charged, Dirac, non-sector-mixing fermions — are the cleanest candidate to realize the symmetric
  block-balanced record partition.
- **Cross-sector grounding:** the **same** dial governs neutrinos — `NEWPHYSICS_NP_NEUTRINO_PMNS_NOTE_2026-05-10`
  eq B3 `Q_ν = (1 + 2ρ_ν)/3` is **identically** `1/3 + (2/3)ρ`. One dial `r/ρ` for all four sectors, not four
  separate ansätze.

## Verdicts

- **VERDICT 1 — `r=1/2` is SYMMETRIC-STATIONARY.** It is the unique fixed point of the genuine dial symmetry
  (the block-swap `r→1/(4r)`) and the symmetric maximum of `S₂`; its stability is arrow-dependent (unstable
  under sharpening, stable under thermalizing). **Distinguished by symmetry unconditionally; "stable" only
  under the second-law arrow.** It is **not** merely an unstable separatrix — that is the sharpening-arrow
  reading only — but neither is it a bare attractor; the precise, honest word is **symmetric-stationary**.
- **VERDICT 2 — the multi-lane reading is CONSISTENT-MULTILANE (no overreach).** Each sector occupies a
  distinct dial point; only charged leptons sit at the symmetric one; no other sector is at `Q=2/3`. This is
  **consistency with the observed Q values**, not a derivation of them — and it cleanly avoids the
  falsified forcing version.

## What this does and does not establish

- **Does:** confirms the dial structure is exact and matches all sector Q's via one formula; identifies the
  *correct* dial symmetry (`r→1/(4r)`, correcting the prior `r↔1−r`) and proves `r=1/2` is its unique fixed
  point and the `S₂` extremum; gives the honest arrow-dependent stability; demonstrates the multi-lane
  occupancy is consistent without overreach.
- **Does not:** adopt the candidate axiom, add any axiom or import, or *derive* any sector's `r` from the
  axiom. The sector→dial-point assignment ("which symmetry fixes which point") and the dynamical
  *selection* of the 2-sector (block-count) coarse-graining over the per-DOF one remain the open gate the
  whole campaign reduces to (`frobenius_isotype_split` retained_no_go declines to rank `(1,1)` vs `(1,2)`).
  The "colored→hierarchy, Majorana→degenerate" breaking story is a **consistency narrative**, not derived.

## Provenance & prior-art consistency (verified 2026-06-04, origin/main `d23220baf`)

- Exact dial `Q=1/3+(2/3)r` and `Q=2/3 ⟺ r=1/2`: **retained** cone biconditional
  (`CHARGED_LEPTON_KOIDE_CONE_ALGEBRAIC_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-10`).
- Sharpening `r→2r²`, `r=1/2` unstable separatrix: `FLAVOR_R_HALF_IS_THE_RECORDS_FLOW_SEPARATRIX_2026-06-02`
  (bounded_theorem; grounded in `luders_rule_from_composition_consistency`, retained_bounded).
- Thermalizing `g(r)=√(r/2)`, `r=1/2` stable attractor + the `r↔1−r`-is-not-a-symmetry correction:
  `FLAVOR_R_HALF_STABLE_UNDER_THERMALIZING_ARROW_2026-06-02` (bounded_theorem).
- Stationary-point reframe: `FLAVOR_R_HALF_IS_A_STATIONARY_POINT_NOT_FORCED_2026-06-02`.
- Per-sector Q inputs: `QUARK_MASS_SPECTRUM_KOIDE_SCHEME_OPEN_GATE_NOTE_2026-05-26`,
  `FLAVOR_BOTH_READINGS_CHARGE_SELECTS_NOTE_2026-05-30`, `NEWPHYSICS_NP_NEUTRINO_PMNS_NOTE_2026-05-10`.
- **New content** vs origin/main: the block-swap involution `r→1/(4r)` as the *genuine* dial symmetry whose
  unique fixed point is `r=1/2` (correcting the bogus `r↔1−r`), and the explicit multi-lane no-overreach
  table. Consistent with — does not contradict — every cited note. Does not load-bear on
  `closure_c_staggered_dirac_gate` or `koide_phase_aps_eta_parity_route`.

## Next paths this opens

- The dial symmetry is now pinned (`r→1/(4r)`). The sharply-posed open object is unchanged but better lit:
  **what dynamically selects the 2-sector (block-count) coarse-graining as the record partition** for the
  charged-lepton sector — the same einselection / det_C gate. With the symmetry identified, the question
  becomes *why the charged-lepton record-writing channel is invariant under the block-swap* while the
  colored/Majorana channels break it.
- A first-principles version of the "colored→`r>1/2`, Majorana→`r<1/2`" breaking (currently a consistency
  narrative) would upgrade the multi-lane reading from consistent to predictive.
