# block01 — Cluster 2 section: READOUT-CONTEXT / OBJECTIVITY / SECTOR-MEASURE

**Lane:** axiom-update-proposals, branch
`physics-loop/axiom-update-proposals-block01-20260620`.
**Cluster:** C2 — readout-context / objectivity / sector-measure axiom
[GATE: readout context / sector measure / objectivity / occupancy].
**Proposal note:** `docs/AXIOM_UPDATE_PROPOSAL_READOUT_CONTEXT_OBJECTIVITY_2026-06-20.md`
**Runner:** `scripts/axiom_update_proposal_readout_context_objectivity_runner_2026_06_20.py`
**Cache:** `logs/runner-cache/axiom_update_proposal_readout_context_objectivity_runner_2026_06_20.txt`
(**TOTAL: PASS=41 FAIL=0**)
**hypothetical_axiom_status:** `"conditional on accepted new axiom; not retained
on the actual current surface."` (on every conditional derivation below). Adopts
nothing; audit lane / owner is sole status authority.

---

## Candidate primitive (weakest sufficient)

> **Readout-context / outcome-measure primitive (CANDIDATE; NOT adopted).** A
> supplied readout context's central-sector measure assigns **one statistical
> slot per irreducible record OUTCOME** (`K`/CPT orbit / irreducible Dirac–record
> factor), not per central-sector real component; equivalently the physical
> readout criterion is **maximum objective information over the objective outcome
> alphabet** (count `K`-real outcome labels / atom-share, not Born/rank weight);
> and the scalar readout of a sector is one objective scalar of that sector (the
> determinant character on the matter block), with disjoint outcomes registering
> as disjoint records.

One binary, dimension-blind structural choice: **count OUTCOMES, not
components.** Supplies a measure *class* only — no weight, probability,
normalization, Born rule, phase, or mass number. Same category as the approved
`kinetic_isotropy_primitive`.

## Walls discharged (conditional)

| Wall | Discharge (conditional) | Fanout |
|---|---|---|
| **R1** Koide `r=1/2` equal-block measure | equal-block `(1,1)` face ⇒ `t=1` ⇒ `r*=1/2`, `Q=2/3` (exact) | ~1 direct + koide cone 327 |
| **R2** Koide `r=1/2` objectivity selector | max-objective-information over 2 labels ⇒ uniform `(1/2,1/2)` ⇒ `r=1/2`; **coincides with R1** | shared koide/flavor |
| **R3** `W_t`-independence countermodel | the einselection fixed point gives `t=2` (`r=1`), so a Cluster-1 dynamics axiom does **not** pin the measure ⇒ the readout-context measure primitive is **exactly** the missing `t=1` pin | demarcation (no extra fanout; defines minimality) |
| **R4** observable T1-d det-readout identification | form half = no-new-axiom theorem (SKb); Record-additivity + the one identification clause ⇒ Cauchy ⇒ `W = c log det`, `c=1` | observable identification half of 887 |
| **R5** P-REC single-taste pointer | per-site `gamma_5` impossible (`ω=iI`); selector must be readout-context = "one outcome per irreducible factor" = same orbit-occupancy choice | shared with anomaly P-REC (Cluster 3 supplies factor existence) |

All five are the **same** choice (`t=1` = count outcomes), so ONE primitive
discharges them — the weakest sufficient addition.

## Conditional derivation the runner verifies

Lever (landed, no axiom): `Q = (1+2r)/3`, capacity max `r* = w_p/(2 w_s)`, free
ratio `t = w_p/w_s`. Candidate pins `t=1` ⇒ `r=1/2`, `Q=2/3`. R4: det positive on
zero-source staggered surface ⇒ `log|det|=log det`; additivity + identification ⇒
`W(Z_1 Z_2)=W(Z_1)+W(Z_2)` ⇒ Cauchy ⇒ `W=log det` (residual `4e-16`). R5:
exhaustive search finds no on-site anticommutant of the Pauli triple. SKc: the
two exhibited models `M_sector` (slots/component=3 ⇒ `r=1`) and `M_orbit`
(slots/outcome=2 ⇒ `r=1/2`) give the convention-free occupancy fiber
`r_sector/r_orbit = Z_sector/Z_orbit = 2`.

## Skeptical re-attack (the one genuine no-new-axiom attempt)

**SKa — is equal-block forced by a missed symmetry?** Tested `U(3)`-invariance
(⇒ `I/3` ⇒ **rank** `(1/3,2/3)`, `r=1`, not equal), `K`/CPT (fixes both
projectors, **no** swap — basis only), `Z_3`-equivariance (circulant operators
**commute** with the grading, `||[C,P_s]||=0` — cannot split the orbit).
**Verdict: the wall WALLS** — no symmetry forces the measure; a new readout-
context premise is required. (Honest contrast with the two corrected B-AXIS
no_gos: here the attack confirms the wall instead of breaking it.)

Bonus crack **SKb** (shrinks the wall, no new axiom): the det-vs-trace **form**
is already a theorem (multiplicative character; trace fails), so the 887 fanout
of `observable_principle_from_axiom_note` is **not** a missing axiom — only the
thin Z↔record identification remains, and it is in the same readout-context gate.

## Minimality / does NOT grant

ONE binary choice (outcomes-vs-components), no fitted number; outputs are exact
fractions (`Q ∈ {2/3, 1}`). Does NOT grant: weights/probabilities/Born rule,
normalization, CP phase `δ` (separate radian-period admission), mass values,
record-PRODUCTION dynamics (Cluster 1 — R3 shows those give the *wrong* value),
or gauge/particle content (Cluster 3 — the *existence* of the Dirac factor whose
outcome R5 selects). Folds the conditional note's "two inputs" into one
(atom-share = label-count, runner-verified) — the SK-4 minimality crack.

## Tensions with retained no-gos

None. Every retained no_go in scope (`FLAVOR_QD_...`, `KOIDE_RECORDS_OBJECTIVITY
_CONDITIONAL`, `KOIDE_ORBIT_OCCUPANCY`, `NO_PER_SITE_CHIRALITY`, T1-d boundary,
Record non-supply clause) asserts the measure is **not forced**, never that it is
**impossible/forbidden**; several explicitly name the indifference/atom-share
rule as a coherent possible extra principle. An addition that supplies it is
consistent with all of them. It is new content in a declared-open gate, not a
reword of an axiom (policy §1).

## Falsifiers

(1) a no-new-axiom derivation of `t=1` from the current surface; (2) the
einselection fixed point shown to give `t=1` (would make Cluster 1 sufficient,
primitive redundant); (3) the five faces shown genuinely independent (breaks
minimality); (4) sharpened charged-lepton `Q` materially off `2/3`; (5) SKb
overturned (det form not a theorem).

## Owner sequencing

Fanout-per-unit-strength **C2 ≈ C1 > C3** (sibling `WALL_TO_GATE_MAP.md`). C2 is
a weak readout-criterion addition with large transitive reach (koide cone 327 +
observable identification half of 887 + flavor readout rows). Recommend C1 then
C2 (weak, high-leverage); C3 deferred. Approval, if any, routes through
`AXIOM_MINIMALITY_POLICY.md` §6.
