# Dial Occupancy Irreducibility — the per-sector setting `s` is the irreducible Yukawa-texture input; the framework derives the dial STRUCTURE and its distinguished settings, not the per-sector POSITION

**Date:** 2026-06-05
**Type:** meta
**Claim type:** meta
**Claim boundary:** hostile-assessment / cross-note disentanglement. Sets no
audit status, assigns no grade, changes no row. It records where a single
remaining quantity — the per-sector "dial occupancy" — sits in the derivation
tree, using only facts already on `origin/main` (verified statuses cited inline)
plus a paired runner of exact/numeric checks. It does **not** force `r=1/2`, add
an axiom, import a comparator, or claim a closure.
**Primary runner:** [`scripts/frontier_dial_occupancy_irreducibility.py`](../scripts/frontier_dial_occupancy_irreducibility.py) (PASS=32, FAIL=0; cache `logs/runner-cache/frontier_dial_occupancy_irreducibility.txt`).
**Status authority:** independent audit lane only; effective status is pipeline-derived after review.

## 0. The object

The per-sector Koide structure (charged leptons, quarks, neutrinos) sits on **one
derived family**

```text
Q(r) = 1/3 + (2/3) r ,        r = |b|^2 / a^2 >= 0 ,
```

carried by the single `C_3[111]`-circulant Hermitian operator
`H = a I + b C + bbar C^2` on the hw=1 generation factor
([CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02.md](CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02.md),
links L1–L10; `Q=1/3+(2/3)r` is **retained**;
[KOIDE_KAPPA_BLOCK_TOTAL_FROBENIUS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md](KOIDE_KAPPA_BLOCK_TOTAL_FROBENIUS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md)).
Writing the multi-lane dial `r(s) = 2^(s-1)` (so `s=0 <=> r=1/2`), the per-sector
occupancies under assessment are

```text
neutrinos        s ~ -0.61    (r ~ 0.328,  Q ~ 0.552)
charged leptons  s  =  0      (r  = 0.500,  Q  = 0.667)   <- the separatrix
down             s ~ +0.26    (r ~ 0.599,  Q ~ 0.733)
up               s ~ +0.63    (r ~ 0.774,  Q ~ 0.849)
```

The dial is a faithful, strictly-monotone relabelling of `r > 0`
(`s = 1 + log2(r)`): it adds no content beyond `r`, so any statement about `r`
transports verbatim to `s` (runner §A). The framework-frame caveat is respected:
`r=1/2` is **not forced** — it is one distinguished setting (`s=0`) of a family
whose distinguished points are
[FLAVOR_R_HALF_IS_A_STATIONARY_POINT_NOT_FORCED_2026-06-02.md](FLAVOR_R_HALF_IS_A_STATIONARY_POINT_NOT_FORCED_2026-06-02.md)
(**retained_bounded**) and the separatrix of the records flow `r -> 2r^2`
([FLAVOR_R_HALF_IS_THE_RECORDS_FLOW_SEPARATRIX_2026-06-02.md](FLAVOR_R_HALF_IS_THE_RECORDS_FLOW_SEPARATRIX_2026-06-02.md),
**retained_bounded**).

## 1. Verdict

> **The dial OCCUPANCY `s` (which setting each fermion sector takes) is an
> IRREDUCIBLE-PER-SECTOR INPUT.** The framework derives the dial *structure* —
> the family `Q=1/3+(2/3)r`, the generation count 3, the carrier operator, and
> the distinguished settings `r in {0, 1/2, 1}` (`Q in {1/3, 2/3, 1}`) — but the
> per-sector *position* is the genuine Yukawa-texture datum. It is **not**
> derivable via the color→generation bridge (a no-go), and **not** via any
> non-color native selector tested (each is either flat in `s` or selects an
> *endpoint*, never an interior sector). This is already the framework's own
> bookkeeping: the occupancy is exactly the single highest-leverage admitted
> input `AC_phi_lambda`.

This is the honest floor — and it is the *standard* floor: the Standard Model
likewise leaves the Yukawa eigenvalues free. The framework still derives strictly
more than the SM here (the family, the count, the operator class, and the
discrete lane structure), reducing the free per-sector data to **one real number
`s` per sector** on a derived axis.

## 2. Where else could `s` come from? Non-color routes, tested

The brief asks: if the color→generation bridge is a no-go, is `s` sourced by EW
isospin texture, the signed-vs-singular readout class, the Yukawa hierarchy, or
Dirac-vs-Majorana structure? Each candidate is checked in the runner; **none**
delivers the per-sector `s`.

| candidate native selector | what it actually does | does it pin `s`? |
|---|---|---|
| **Born / tracial dimension weight** (the genuine second-law/Born equilibrium) | weights the two isotype blocks by **dimension** 1:2 → `r=1` (`s=1`) | **No** — picks the hierarchy **endpoint**, not any sector (runner §B1) |
| **block-counting / det_C measure** | equal power per block → `r=1/2` (`s=0`) | only by **choosing** the non-Born measure; Born and block-counting **disagree** → the measure is itself the free choice ([FLAVOR_EINSELECTION_2SECTOR_MODULO_KREALITY_2026-06-02.md](FLAVOR_EINSELECTION_2SECTOR_MODULO_KREALITY_2026-06-02.md), **retained_bounded**) |
| **SU(3)_c center `Z_3` character bridge** | color fundamental char `(3, 3w, 3w^2)` decomposes as **3 copies of one nontrivial irrep**; generation regular char `(3,0,0)` is the **regular rep** (each irrep once) | **No** — the two are **inequivalent**; the bridge that could carry color structure onto `r` is **absent** ([Z3_CHARACTER_ISOMORPHISM_COLOR_GENERATION_OPEN_GATE_NOTE_2026-05-10.md](Z3_CHARACTER_ISOMORPHISM_COLOR_GENERATION_OPEN_GATE_NOTE_2026-05-10.md); runner §B2) |
| **signed-vs-singular readout class** | the Hermitian (signed) readout gives `Q_signed=(1+2r)/3` for **all** `r`; singular-value readout is `θ`-dependent at fixed `r` | **No** — fixes the **sign of √m** (which readout class is phenomenology-compatible), *orthogonal* to the position `r` ([KOIDE_SIGNED_EIGENVALUE_VS_SINGULAR_VALUE_READOUT_NARROW_THEOREM_NOTE_2026-05-29.md](KOIDE_SIGNED_EIGENVALUE_VS_SINGULAR_VALUE_READOUT_NARROW_THEOREM_NOTE_2026-05-29.md), **retained**; runner §B3) |
| **Frobenius / isotype singlet:doublet split** | fixes the **block structure** (1 singlet + 1 doublet), not the ratio; `(a,\|b\|) ↦ r` is **onto** `[0,∞)` | **No** — `r` is a **free** continuous ratio; **retained_no_go** ([KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS_NOTE_2026-04-21.md](KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS_NOTE_2026-04-21.md); runner §B4) — **this is the core no-go** |
| **EW isospin texture** | the up/down split within a doublet is itself part of the *flavor* (Yukawa) input; the up-sector partition lane collapses to a phase-deformed edge, not a derived interior partition | **No** — does not derive interior partition variables ([UP_SECTOR_PARTITION_REVISIT_NOTE_2026-04-19.md](UP_SECTOR_PARTITION_REVISIT_NOTE_2026-04-19.md), bounded): isospin re-labels the same free texture |
| **Dirac-vs-Majorana (neutrinos)** | the Majorana block carries a **radial** observable `log‖s‖`; its scale is **not selected** (no intrinsic scale; finite-point selection still open) | **No** — neutrinos have their *own* unselected radial scale ([NEUTRINO_MAJORANA_NAMBU_RADIAL_OBSERVABLE_NOTE.md](NEUTRINO_MAJORANA_NAMBU_RADIAL_OBSERVABLE_NOTE.md)); supplies no `s` |

The pattern is uniform and is the no-coincidence signal of *one input wearing
many faces*: every proposed selector is **flat in `s`** (readout class; isotype
split) or **lands on an endpoint** (`r=0` or `r=1`), and the only thing that ever
produces an *interior* value does so by *choosing* a non-canonical measure. The
cross-PR consolidation already reached this convergence independently — six
routes reduce to **one residual**, equal-block-vs-dimension =
`AC_phi_lambda`/det_C-vs-det_R, "proven NOT forced by rep theory, records
dynamics, reality-of-matrix, or Berry curvature"
([OPEN_KOIDE_FLAVOR_CLUSTER_CONSOLIDATION_MAP_2026-06-02.md](OPEN_KOIDE_FLAVOR_CLUSTER_CONSOLIDATION_MAP_2026-06-02.md)).

**So all the non-color routes are equally admitted: they relabel the same free
`r`, never source it.**

## 3. Is `s` irreducibly a per-sector INPUT? — yes; the framework already says so

The strongest evidence is the framework's *own* registry. The single
highest-leverage admitted input
([`docs/audit/data/tier_a_admissions.json`](audit/data/tier_a_admissions.json),
**leverage 41** — the largest of the two genuine admitted inputs; the other is
strong-CP `θ=0`) is

```text
AC_phi_lambda  (canonical id: staggered_dirac_realization_gate_note_2026-05-03)
  "generation mass-pattern input: the C_3-breaking phase/orientation PLUS the
   abstract-sector to physical-species bridge; bare e/mu/tau naming is a
   convention, not a derivation target"
  class: discrete flavor input with labeling convention stripped
```

The clause **"the abstract-sector to physical-species bridge"** *is* the dial
occupancy: assigning to each physical sector (charged lepton / up / down /
neutrino) its position on the abstract `r`-family. `staggered_dirac_realization_gate`
is **audited_conditional** on `origin/main` — i.e. a registered, accepted-as-premise
admitted input, not a derived theorem. The chain-of-custody note states the same
split in words: *structure derived, value reached only modulo `AC_phi_lambda`*.

So the honest floor is not a fresh discovery — it is the *already-recorded*
classification, re-confirmed here against the inequivalence (color), the
flatness (readout class), and the surjectivity (isotype split) facts.

## 4. The 49-row color-identification gate vs the dial occupancy — DIFFERENT problems, ONE label

The brief asks whether the color-identification gate is the *same* character
bridge as the dial occupancy. **They are different problems wearing one label.**

- **The IDENTIFICATION gate** (which physical species *is* the abstract hw=1
  `C_3` triplet, and the color-vs-generation labelling) is a **discrete
  labelling** problem. Its obstruction is exactly the **character mismatch** of
  §2/§B2: the `SU(3)_c` center `Z_3` does not act on color the way the cyclic
  permutation acts on generations (`(3,3w,3w^2)` vs `(3,0,0)`). It is the
  substep-4 "physical-species reading" of
  [STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md](STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md)
  (item 4: *"forcing the physical-species reading of the hw=1 triplet as three SM
  matter generations"*), left open by
  [STAGGERED_DIRAC_GATE_CLOSURE_SYNTHESIS_THEOREM_NOTE_2026-05-17.md](STAGGERED_DIRAC_GATE_CLOSURE_SYNTHESIS_THEOREM_NOTE_2026-05-17.md)
  (Theorem T5: *"the physical-species / SM-generation identification remains an
  open bridge"*).

- **The OCCUPANCY** (which `r` each *already-identified* sector takes) is a
  **continuous** datum left free by the **isotype no-go** (§B4), *independently*
  of any labelling.

They are logically independent (runner §C):

1. `r = |b|^2/a^2` is defined on the abstract operator **before** any physical
   species label is attached — so occupancy does **not** presuppose the
   identification; and
2. the character bridge, *even if it existed*, constrains **labels**, not `r`
   (the isotype split leaves `r` free regardless) — so identification would
   **not** deliver occupancy.

Yet both are **bundled under the same single admitted input** `AC_phi_lambda`:
the gate's "abstract-sector to physical-species bridge" covers *both* the
labelling (identification) and the texture (occupancy). This matches the standing
"counting-vs-splitting" tension: the same `C_3` that gives the **count** 3 (and
forces the circulant block structure) does **not** also fix the **value** `r`;
and *distinctness* of the three masses is reachable — it is not the obstruction —
so the obstruction is specifically the (discrete) chiral/labelling split for
identification and the (continuous) measure/ratio for occupancy. The 49-row
color portfolio is therefore the **identification** half; the dial occupancy is
the **texture** half — one Tier-A label, two separable sub-questions.

## 5. The next paths this opens (not closing)

- **Occupancy texture as a relation, not four independent numbers.** The four `s`
  are not obviously independent: the cross-sector `A^2`/CKM bridges
  ([CROSS_SECTOR_A_SQUARED_KOIDE_VCB_BRIDGE_PROMOTED_VIA_V8_THEOREM_NOTE_2026-04-29.md](CROSS_SECTOR_A_SQUARED_KOIDE_VCB_BRIDGE_PROMOTED_VIA_V8_THEOREM_NOTE_2026-04-29.md))
  tie the quark `s` to mixing data. The open object is whether a *single*
  inter-sector relation (e.g. an `s`-additivity or a `Σ s` constraint across the
  four sectors) reduces the four inputs to fewer — turning "four free `s`" into
  "one texture law + boundary data."
- **A `T`-odd / chiral structure for the measure half.** The block-counting
  (det_C, `r=1/2`) vs dimension (Born, `r=1`) choice is the one undischarged bit;
  the einselection note isolates it to **K-reality** + the **measure** choice,
  with the chirality grading the candidate `T`-odd ingredient. If a native `T`-odd
  structure selects the equal-power measure for the charged-lepton sector, the
  `s=0` occupancy (not the others) would be derived — leaving the *relative* `s`
  offsets as the residual.
- **Neutrino radial scale.** The Majorana radial observable `log‖s‖` is exact but
  scale-free; a finite-point selection on the already-normalized response curve
  would fix the neutrino `s`. This is a *separate* handle from the charged-lepton
  measure question.

None of these is closed here; each is a concrete object the irreducibility floor
makes precise.

## 6. Honest caveats / ledger checks (verified against `origin/main` before landing)

- `koide_frobenius_isotype_split_uniqueness` = **retained_no_go** (the load-bearing
  core: `r` is free).
- `z3_character_isomorphism_color_generation_open_gate` = **unaudited** — so the
  color→generation no-go reasoning rests on the **textbook character calculation
  itself** (verified in the runner), *not* on a retained tier. The conclusion does
  not load-bear on the unaudited note's status.
- `koide_signed_eigenvalue_vs_singular_value_readout` = **retained**;
  `flavor_einselection_2sector_modulo_kreality`,
  `flavor_r_half_is_a_stationary_point_not_forced`,
  `flavor_r_half_is_the_records_flow_separatrix`,
  `koide_generation_id_cl3_grade1_bridge` = **retained_bounded**;
  three-generation count/structure rows = **retained**.
- `staggered_dirac_realization_gate` (= `AC_phi_lambda`) = **audited_conditional**.
- **Provenance correction:** the records-flow-separatrix note cites
  `luders_rule_from_composition_consistency` as `retained_bounded`; on the current
  ledger that row is **audited_conditional**. The `r -> 2r^2` flow is therefore on
  a conditional, not a retained, anchor. This note does **not** load-bear on that
  flow — it uses only the (B1)–(B4) facts and the textbook character calculation —
  so the verdict is unaffected, but the weaker tier is flagged for honesty.

## 7. What this does NOT claim

- Does not derive `r=1/2`, the per-sector `s`, `Q=2/3`, `δ=2/9`, or any mass.
- Does not force the block-counting measure over the Born measure (they disagree;
  the choice is the residual).
- Does not assert the color→generation bridge is *impossible* — only that the
  center-character route is **inequivalent** (the standing open gate), and that no
  *currently-tested* native selector pins `s`.
- Does not add an axiom, import a literature comparator, or consume a PDG value
  (the empirical `Q≈2/3` and the PDG-extracted `s` are comparators only).
- Does not set, predict, or propose an audit/effective-status outcome; it
  re-confirms the framework's existing `AC_phi_lambda` classification.

## 8. Verification

```bash
PYTHONPATH=scripts python3 scripts/frontier_dial_occupancy_irreducibility.py
```

Expected: `PASS=32 FAIL=0`. The runner checks (A) the dial↔family faithfulness
and the four distinct sector `r`/`Q`; (B1) Born→`r=1` vs block-counting→`r=1/2`
disagreement; (B2) the exact `Z_3` character decompositions (color = 3×one irrep;
generation = regular = 1+1+1) and their inequivalence; (B3) `Q_signed=(1+2r)/3`
for all `r` (readout class ≠ occupancy selector) and the `θ`-dependent
singular-value contrast; (B4) surjectivity of `(a,|b|)↦r` onto `[0,∞)` and the
dial bijection; (C) the discrete-labelling vs continuous-`r` independence; and
(D) the assembled meta verdict.
