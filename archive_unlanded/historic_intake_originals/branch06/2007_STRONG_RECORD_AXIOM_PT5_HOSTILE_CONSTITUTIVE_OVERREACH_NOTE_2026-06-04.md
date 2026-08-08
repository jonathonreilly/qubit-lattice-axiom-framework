# Strong Record Axiom (PT5, Hostile): Restatement on Its Load-Bearing Clause, and Overreach (Quark/Neutrino Falsification + Born Collision)

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the
> canonical source-of-truth doc.

**Date:** 2026-06-04
**Claim type:** meta
**Status authority:** independent audit lane only. This note sets no audit
status, approves no axiom, and approves no import. It is a hostile pressure-test
(PT5) of a *candidate* axiom; it characterizes that candidate's content and
records an honest negative. The framework's actually-adopted Record axiom is the
WEAK one in [`MINIMAL_AXIOMS_2026-06-04.md`](MINIMAL_AXIOMS_2026-06-04.md), which
this note does not modify.
**Primary runner:**
[`scripts/strong_record_axiom_pt5_hostile_constitutive_overreach_2026_06_04.py`](../scripts/strong_record_axiom_pt5_hostile_constitutive_overreach_2026_06_04.py)
(SCORECARD PASS=32, FAIL=0)
**Cached log:**
[`logs/runner-cache/strong_record_axiom_pt5_hostile_constitutive_overreach_2026_06_04.txt`](../logs/runner-cache/strong_record_axiom_pt5_hostile_constitutive_overreach_2026_06_04.txt)

---

## The candidate under test

> "A record registers WHICH real classical alternative is realized; the real
> classical alternatives are the real superselection sectors (real Wedderburn
> blocks); each is ONE alternative; record readout counts alternatives
> ADDITIVELY, DIMENSION-BLIND."

The skeptic's charge: this is the equal-power / real-`K0`-block-count MEASURE
(`AC_phi_lambda`, the `(1,1)` weighting) renamed as an axiom, and it OVERREACHES.
The defender's claim: each clause is standard measurement theory, and `r=1/2`
(`Q=2/3`) is a downstream consequence.

## Two headline verdicts

1. **CONSTITUTIVE or RESTATEMENT? -> RESTATEMENT on the load-bearing clause.**
   The clauses with genuine, record-independent content (additivity; "registers
   which alternative"; "each block is one alternative") are all
   `(1,1)`-vs-`(1,2)` **neutral** -- they fix the *form* (an additive measure)
   and the *atom count* (2 sectors), but not the weight. The *only* clause that
   produces `(1,1)` is "count, **dimension-blind**", which has no
   measurement-theory justification independent of choosing the block-count
   measure. It is `AC_phi_lambda` renamed. Granting the defender's best point
   (no clause forward-references `2/3`, so `Q=2/3` is a true output) does not
   rescue it: "computing a value from an assumed measure" is exactly what a
   restatement looks like; constitutiveness requires the *measure itself* to be
   forced by record-meaning, and it is not.

2. **OVERREACH? -> YES, on two independent fronts.**
   - **Quark/neutrino falsification (fatal if read as universal).** If
     "records count blocks" were a constitutive law it would hold in *every*
     fermion sector. Empirically only the charged leptons sit at the block-count
     point: `Q_e = 2/3` (`r=1/2`), but `Q_up = 0.849`, `Q_down = 0.731`
     (`r_up != 1/2`, `r_down != 1/2`), and the neutrino literature value
     `Q_nu ~ 1/3` implies `r_nu = 0` (the opposite end). A sector-universal
     block-count law is empirically falsified; the only survival is
     sector-contingency (quarks do not live on the same circulant,
     [`QUARK_BAE_ANALOG_BOUNDED_OBSTRUCTION_NOTE_2026-05-10_quarkBAE.md`](QUARK_BAE_ANALOG_BOUNDED_OBSTRUCTION_NOTE_2026-05-10_quarkBAE.md)),
     which *concedes* that block-count is a per-sector measure choice, not a
     constitutive record law.
   - **Born collision.** Objective decoherence records carry the **Born** weight
     on the *same* two sectors: the tracial reference `I/3` pushed through the
     singlet/doublet split is `(1/3, 2/3)` = the rank weighting = `r=1` = `Q=1`
     (the QD-objectivity panel,
     [`FLAVOR_QD_OBJECTIVITY_FIXES_BASIS_NOT_WEIGHT_2026-06-02.md`](FLAVOR_QD_OBJECTIVITY_FIXES_BASIS_NOT_WEIGHT_2026-06-02.md)).
     The candidate says the record readout is the **count** `(1,1)` = `Q=2/3`.
     These are non-proportional rays on the same sectors; worded as "*the* record
     readout counts alternatives, dimension-blind", the strong axiom asserts the
     single record functional is the count and thereby contradicts the Born
     weight the same objective records must carry.

The genuinely constitutive, non-overreaching content is exactly the WEAK adopted
axiom (additive scalar readout), which does **not** force `r=1/2`.

---

## Front-by-front

### Front 1 -- Constitutive vs Restatement (the central charge): RESTATEMENT

Strip the candidate to operational clauses and test each against the two
competing weightings on the 2 sectors `{singlet (rank 1), doublet (rank 2)}`:
block-count `w=(1,1)` and dimension/trace `w=(1,2)`.

| Clause | Independent (record/measurement) content? | Picks `(1,1)`? |
|---|---|---|
| additive over disjoint records | YES (it is an atomic measure) | NO -- both `(1,1)` and `(1,2)` are additive |
| registers WHICH alternative | YES (the readout separates sectors) | NO -- any strictly positive weight separates |
| each block is ONE alternative | YES (fixes atom count = 2) | NO -- fixes #channels, not the weight (`r* = w_p/2w_s`, continuous) |
| count, **DIMENSION-BLIND** | NO independent justification | **YES -- this *is* `w=(1,1)` = `AC_phi_lambda`** |

So three clauses are real measurement-theory content but `(1,1)`-`(1,2)`-neutral;
the fourth, which carries the entire result, is the disputed measure renamed
(runner F1.1-F1.5, F1.4b). This matches the standing result that the block-count
weight is **permitted-not-forced**
([`KOIDE_REAL_REP_BLOCK_COUNT_PERMITTED_NOT_FORCED_NOTE_2026-05-30.md`](KOIDE_REAL_REP_BLOCK_COUNT_PERMITTED_NOT_FORCED_NOTE_2026-05-30.md),
[`KOIDE_Q23_K0_REAL_BLOCK_EQUIVALENCE_NOTE_2026-05-30.md`](KOIDE_Q23_K0_REAL_BLOCK_EQUIVALENCE_NOTE_2026-05-30.md)).

### Front 2 -- Overreach: quark/neutrino sectors (potential fatal): YES if universal

Empirical Koide values (PDG comparators, same as
[`KOIDE_X_L1_THRESHOLD_HEAVY_QUARK_WILSON_NOTE_2026-05-08_probeX_L1_threshold.md`](KOIDE_X_L1_THRESHOLD_HEAVY_QUARK_WILSON_NOTE_2026-05-08_probeX_L1_threshold.md)):

| Sector | Koide `Q` | implied `r = (3Q-1)/2` | at block-count `r=1/2`? |
|---|---|---|---|
| charged leptons | `0.6667` | `0.50` | YES |
| up-type quarks | `0.849` | `0.77` | NO |
| down-type quarks | `0.731` | `0.60` | NO |
| neutrinos (Foot/Brannen `Q_nu~1/3`) | `0.333` | `0.00` | NO |

Only one of four sectors sits at the block-count point (runner F2.1-F2.8). A
constitutive "records count blocks -> `Q=2/3`" law would have to hold in all
sectors and does not. The escape -- different generation algebra per sector --
saves the axiom from falsification but concedes Front 1: block-count is then a
per-sector measure choice, not what a record *is*.

### Front 3 -- Coherence / well-definedness on `M_n(C)`: UNDER-DEFINED

"Real classical alternative" is not well-defined until `K0` is pinned. `Z_3` has
Frobenius-Schur indicators `(+1,0,0)`: `K0`-real(`R[Z_3]`) `= 2` blocks
(singlet + one complex-type doublet), `K0`-complex(`C[Z_3]`) `= 3` blocks. For a
simple block `M_n(C)` the central-idempotent count and the real-block count are
both `1`, while the complex/Born/trace reading weights it by `n` -- so the
"count" is well-defined only after the disputed dimension-blind choice (runner
F3.1-F3.3). The forced `Cl(3)` pseudoscalar acts as the *generation scalar*
`i*I_3`, not the doublet Schur structure `diag(0,+i,-i)`, so it does not pin
`K0`-real on the generation factor: well-definedness is a free slot, not forced.

### Front 4 -- Minimality: cuts AGAINST the axiom

No weaker clause yields `(1,1)`:
- "CPT-even / real" alone buys only a `Z_2` sign; the CPT reflection acts
  *within* the rank-2 doublet (`det -1`) and does not collapse it to one slot
  ([`KOIDE_RECORDS_REALITY_SHRINKS_IMPORT_TO_SIGN_NOTE_2026-06-02.md`](KOIDE_RECORDS_REALITY_SHRINKS_IMPORT_TO_SIGN_NOTE_2026-06-02.md);
  runner F4.1).
- "registers a classical outcome" alone yields the Born/rank weight
  `(1/3, 2/3)` -> `Q=1`, the opposite of the candidate (runner F4.2).

So the minimal sufficient clause *is* the dimension-blind measure, and the
removable clauses point to `Q=1` (runner F4.3). Minimality therefore confirms
Front 1 rather than rescuing the axiom.

### Front 5 -- The Born collision (deepest): OVERREACH, with a conceding repair

On the same two sectors: objective/Born records give `(1/3, 2/3)` -> `r=1` ->
`Q=1` (runner F5.1); the candidate's count gives `(1,1)` -> `r=1/2` -> `Q=2/3`
(F5.2). A **dual** readout is *formally* possible -- the space of additive
weightings on 2 atoms is 2-dimensional, so distinct mass- and
probability-functionals can coexist (F5.3). But the axiom as **worded**
("*record readout* counts alternatives, dimension-blind") makes the single
record functional the count, which collides with the Born weight the same
records carry (F5.4): the two are non-proportional rays (`cos<1`, F5.7), so no
normalization reconciles them. The coherent repair -- "count for masses, Born for
probability" -- is exactly the WEAK axiom plus an *extra named* mass-readout
convention; it rescues consistency only by demoting the count from
record-meaning to an added convention, conceding Fronts 1 and 4 (F5.5). The WEAK
adopted axiom does not collide, because "additive" is satisfied by the Born
weight `(1,2)` itself (F5.6) -- the collision is created solely by the strong
clause.

---

## What survives, and the path this opens

The honest survivor is the WEAK adopted Record axiom: additive scalar record
readout, `I(R_1 \sqcup R_2) = I(R_1) + I(R_2)`, which explicitly disclaims Born
weights and `AC_phi_lambda` (per
[`MINIMAL_AXIOMS_2026-06-04.md`](MINIMAL_AXIOMS_2026-06-04.md)). That axiom is
constitutive and non-overreaching, and it does not force `r=1/2`: it fixes the
*form* (a measure) and, together with the two-sector pointer, the *atom count*
(`#channels=2`), but leaves the weight ray free
(`r* = w_p/(2 w_s)`).

This sharpens, rather than closes, the open question. The `r=1/2` value still
requires a genuine selection of the block-count weight over the dimension/Born
weight on the generation factor -- a selection that "record-meaning" does not
supply. Two live directions remain open (neither a no-go): a future source
result could (a) derive the block-count weight from added structure that is
*not* a renamed measure and that *also* explains why the quark/neutrino sectors
differ (sector-contingent generation algebra), or (b) instead select the
dimension/trace/Born reading and force `Q=1`. The Born-collision analysis also
opens a concrete dual-readout question: whether a record can coherently carry the
count for the mass functional while carrying the Born weight for the probability
functional, as two *separately motivated* readouts of one record -- which, if
built, would be the WEAK axiom plus a named mass-readout convention, not a
strengthening of the Record axiom itself.

---

## Load-bearing authorities

- [`MINIMAL_AXIOMS_2026-06-04.md`](MINIMAL_AXIOMS_2026-06-04.md) (the adopted
  WEAK Record axiom; the disclaimer of Born weights and `AC_phi_lambda`)
- [`KOIDE_REAL_REP_BLOCK_COUNT_PERMITTED_NOT_FORCED_NOTE_2026-05-30.md`](KOIDE_REAL_REP_BLOCK_COUNT_PERMITTED_NOT_FORCED_NOTE_2026-05-30.md)
- [`KOIDE_Q23_K0_REAL_BLOCK_EQUIVALENCE_NOTE_2026-05-30.md`](KOIDE_Q23_K0_REAL_BLOCK_EQUIVALENCE_NOTE_2026-05-30.md)
- [`FLAVOR_QD_OBJECTIVITY_FIXES_BASIS_NOT_WEIGHT_2026-06-02.md`](FLAVOR_QD_OBJECTIVITY_FIXES_BASIS_NOT_WEIGHT_2026-06-02.md)
- [`KOIDE_RECORDS_OBJECTIVITY_CONDITIONAL_NOTE_2026-05-31.md`](KOIDE_RECORDS_OBJECTIVITY_CONDITIONAL_NOTE_2026-05-31.md)
- [`KOIDE_RECORDS_REALITY_SHRINKS_IMPORT_TO_SIGN_NOTE_2026-06-02.md`](KOIDE_RECORDS_REALITY_SHRINKS_IMPORT_TO_SIGN_NOTE_2026-06-02.md)
- [`KOIDE_X_L1_THRESHOLD_HEAVY_QUARK_WILSON_NOTE_2026-05-08_probeX_L1_threshold.md`](KOIDE_X_L1_THRESHOLD_HEAVY_QUARK_WILSON_NOTE_2026-05-08_probeX_L1_threshold.md)
- [`QUARK_BAE_ANALOG_BOUNDED_OBSTRUCTION_NOTE_2026-05-10_quarkBAE.md`](QUARK_BAE_ANALOG_BOUNDED_OBSTRUCTION_NOTE_2026-05-10_quarkBAE.md)

## No-Go Discipline Gate

This gate applies to the narrow negatives actually claimed: (a) the strong
Record axiom is a restatement on its load-bearing clause, and (b) it overreaches
(quark/neutrino falsification if universal; Born collision).

**N1 -- Alternative routes.** Four routes to make the candidate constitutive were
checked and each fails: (1) additivity forces the weight -- fails, both `(1,1)`
and `(1,2)` are additive; (2) "which alternative" forces it -- fails, any
positive weight separates; (3) "each block one alternative" forces it -- fails,
fixes atom count not weight; (4) "dimension-blind" is independent measurement
content -- fails, it is the measure renamed and has no record-independent
justification.

**N2 -- Wall independence.** The two overreach fronts are independent: the
quark/neutrino falsification is empirical and sector-level; the Born collision is
structural on a single sector pair. Neither relies on the other.

**N3 -- Hidden-wall scan.** The runner uses only finite linear algebra: the 2
weightings, the rank-1/rank-2 projectors, the Hermitian circulant signed-`Q`,
the tracial push-forward, Frobenius-Schur block counts, and PDG comparators. No
hidden Koide-outcome assumption is smuggled in; `Q=2/3` appears only as the
*output* of the assumed `(1,1)` weight.

**N4 -- Residual matching.** The negative is exactly: the strong axiom's only
result-bearing clause is the disputed measure, and that clause overreaches. It is
NOT a claim that no future principle can select `(1,1)`, nor that the WEAK
adopted axiom is wrong.

**N5 -- Rhetoric audit.** "Restatement" and "overreach" are scoped to the
*candidate strong axiom*, not to the adopted Record axiom, and not to the Koide
program. The path-forward section keeps both selection directions open.
