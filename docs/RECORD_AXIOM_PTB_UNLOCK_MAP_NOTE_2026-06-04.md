# Record Axiom Pressure-Test B — The "Unlock-Map" Bundle

**Date:** 2026-06-04
**Claim type:** meta
**Runner:** `scripts/frontier_record_axiom_ptB_unlock_map_2026_06_04.py` (SCORECARD 38/38)
**Cache:** `logs/runner-cache/frontier_record_axiom_ptB_unlock_map_2026_06_04.log`

This is an honest reach-assessment of a **candidate** record axiom, not an
adoption proposal. The currently approved Record axiom
([`MINIMAL_AXIOMS_2026-06-04.md`](MINIMAL_AXIOMS_2026-06-04.md),
`docs/audit/AXIOM_MINIMALITY_POLICY.md` §6) is the *narrow* statement "finite
scalar record readout is additive over disjoint record collections" and
explicitly disclaims Born weights, time arrow, measurement, superselection, and
source/action. The candidate below is a much stronger sentence; the question is
how much of its advertised reach is genuine.

## The candidate axiom

> *A record is an irreversible registration of which **real (CPT-even)
> superselection sector** is realized.*

Claimed bundled consequences: **(i)** TIME = formation order; **(ii)**
CLASSICAL/QUANTUM CUT = the real Wedderburn center is the frozen/classical
structure; **(iii)** the measure dial; **(iv)** multi-lane occupancy. It also
carries two implicit qualifiers: **CPT-evenness** (the word "real") and a
**Born** claim (what the dial weights are).

## The unlock map (5 items)

| Item | Verdict | One-line reason |
| --- | --- | --- |
| 1. TIME (arrow) | **TOUCHES-CONSTRAINS** | Irreversibility *orients* a pre-given index; it supplies the direction, not the index set (= time itself). |
| 2. CLASSICAL/QUANTUM CUT | **TOUCHES-AND-UNLOCKS** | center(M_n) = scalars (verified): no classical facts *inside* a block; the cut **is** the real Wedderburn block decomposition, and "real" fixes the block count. Genuinely derived from the axiom's own content. |
| 3. CPT | **ASSUMES** | "real" ⟺ CPT-even is an exact equivalence (verified), but the axiom *posits* records are real; it does not derive CPT-exactness of the dynamics. |
| 4. BORN | **TOUCHES-CONSTRAINS** | The dial's fixed points are not the Born weights: records-sharpening `r→2r²` fixes `r=1/2` (block-counting, unstable); the Born/tracial weight is `r=1` and is not even a fixed point. |
| 5. UNIFICATION (4-from-1) | **NOT genuine as advertised** | One distinct mechanism (the cut; multi-lane is its trivial corollary) is a real unlock; the arrow direction is a partial touch; CPT and Born are co-assumed/constrained. |

**Genuine-consequence count: 1 distinct mechanism unlocked** (the cut, with
multi-lane occupancy as the same content re-read across blocks), **1 partial**
(arrow direction), **2 co-assumed/contradicted** (CPT, Born). The headline
"one statement organizes time + cut + CPT + dial" is **a bundle of four
separate premises wearing one sentence**, with exactly one of them genuinely
flowing from the registration content.

## Item-by-item

### 1. TIME — TOUCHES-CONSTRAINS (the wall the axiom can't break)
"Irreversible registration ⟹ records monotonically accumulate ⟹ formation
order = arrow." The runner confirms the monotone-accumulation logic, but it
also exhibits the honest gap: a monotone map `t ↦ R(t)` is monotone *in the
index `t`*; reversing the index reverses the order. Irreversibility therefore
supplies an **orientation on** a pre-existing index; it does not manufacture
the index set. So "record-formation orders time" **restates** the
time-emergence question rather than strengthening it: the arrow's *direction*
is the new content, but the *existence of the ordering parameter* (time as a
set) is co-assumed. This is consistent with — and does not add to — the
retained `anomaly_forces_time` / single-clock line, which reaches the discrete
signature `(3,1)` and a clock, not an independent construction of the index
from irreversibility alone. **Honest:** irreversibility *is* the arrow assumed,
re-expressed as record accumulation; it is not the arrow derived.

### 2. CLASSICAL/QUANTUM CUT — TOUCHES-AND-UNLOCKS (the real win)
This is the one place the bundle earns its keep. Two verified facts:

- **center(M_n(C)) = scalars** for `n = 2,3,4` (the commutant of a full matrix
  algebra is 1-dimensional, equal to the identity). So within any simple
  (full-matrix) block there are **no nontrivial central / superselection /
  classical facts**: within-block is irreducibly quantum/reversible.
- The classical facts therefore live exactly in the **block decomposition**,
  i.e. the Wedderburn center of the algebra. "Which sector is realized" is a
  central (block-label) datum; "irreversible registration" of it freezes the
  central coordinate while leaving the within-block unitary structure intact.

The axiom thereby **locates the measurement cut at the center** — a place
usually put in by hand. The `real` qualifier is load-bearing and non-trivial
here: on the `Z₃` generation carrier, `ℂ[Z₃] = ℂ³` has **3** one-dimensional
sectors, but `ℝ[Z₃] = ℝ ⊕ ℂ` has **2** real-irreducible blocks (singlet +
degenerate doublet). The K-real / CPT-even observable `C + C²` has eigenvalues
`{2,−1,−1}` and resolves **exactly 2** sectors; resolving the third
(`ω` vs `ω²`) requires the K-**odd** observable `i(C − C²)` (eigenvalues
`{0, ±√3}`). So "real (CPT-even)" is not decoration: it **fixes the
superselection sector count** to the real Wedderburn count. This matches the
retained_bounded `flavor_einselection_2sector_modulo_kreality` finding by an
independent route. **The cut + multi-lane occupancy (item 4) are the same
content** — the realized block is the lane, and multiple blocks = multiple
lanes.

### 3. CPT — ASSUMES
`D` real anti-Hermitian ⟹ `T D T = D` ⟹ `Θ = CPT` invariance is an **exact
equivalence** (verified; a generic *complex* anti-Hermitian operator breaks
`T D T = D`), matching the retained `cpt_exact_note` core
([`CPT_EXACT_REAL_ANTI_HERMITIAN_D_NARROW_THEOREM_NOTE_2026-05-10.md`](CPT_EXACT_REAL_ANTI_HERMITIAN_D_NARROW_THEOREM_NOTE_2026-05-10.md),
premise (3)). But the candidate axiom **inserts** reality as the qualifier
("real sector"); it does not derive that the dynamics are real/CPT-even. The
equivalence makes "real" and "CPT-even" interchangeable labels for the same
premise — it does not turn either into a consequence. So CPT-exactness is
**co-assumed**, not unlocked.

### 4. BORN — TOUCHES-CONSTRAINS (and the naive identification is false)
Does the dial, at its stationary points, reproduce Born weights? **No.** On the
2-block structure with power ratio `r`:
- Born / tracial state `ρ = I/3` weights blocks by **dimension** → `r = 1`.
- The records-sharpening (Lüders) map `r → 2r²` has its only finite positive
  fixed point at `r = 1/2` (the **block-counting** weight), and that point is
  **unstable** (`|f′(1/2)| = 2`); the stable fixed point is `r = 0`
  (singlet-collapse).
- The Born point `r = 1` is **not** a fixed point of the records map
  (`f(1) = 2`).

So the dial's stationary structure and the Born weights **diverge** (and the
records-flow stable point is neither). Independently, power-family readouts
`p^q` are multiplicative for every `q`; the unique additive coordinate is
`c·log p` (the log is *inserted*, not derived). This reproduces the
`OBSERVABLE_PRINCIPLE_RECORD_SCALAR_MAP_NO_GO_NOTE_2026-06-05` and the
just-demoted Born finite-record bridge
([`BORN_RULE_FROM_GLEASON_BUSCH_DERIVATION_NOTE_2026-05-20.md`](BORN_RULE_FROM_GLEASON_BUSCH_DERIVATION_NOTE_2026-05-20.md),
now "bounded support note"). **Born is co-assumed at best**; the dial does not
deliver Born-form weights — it can even contradict them at its attractor.

### 5. UNIFICATION — a bundle, not a theorem
Of the four advertised consequences, **one distinct mechanism** is genuinely
unlocked (the cut, with multi-lane its corollary); the arrow contributes only
its *direction*; CPT and Born are separate premises. The sentence reads as one
statement but factors into: (a) "there is a sector structure with a real center"
[the cut — genuine], (b) "registration is irreversible" [arrow direction —
partial, presupposes the index], (c) "sectors are real/CPT-even" [a reality
premise], (d) an unstated weight rule [Born — neither supplied nor matched].
The unification claim is therefore **not** genuine as advertised.

## Net verdict

The candidate axiom **genuinely unlocks the classical/quantum cut** — it locates
the measurement cut at the real Wedderburn center (no classical facts within a
simple block; "real" fixes the sector count), and multi-lane occupancy is the
same content. The **time arrow's direction** is a real but partial touch
(orientation, not index). **CPT and Born are co-assumptions**, not consequences.
So the honest score is **1 genuine distinct unlock + 1 partial + 2
co-assumed**, and the "one statement organizes all four" headline is a bundle
of four separate premises. The win to keep is the cut; the overreach to flag is
the unification.

## Scope and discipline

- This note **does not** propose adopting the candidate axiom. The approved
  Record axiom remains the narrow scalar-additivity statement
  (`MINIMAL_AXIOMS_2026-06-04.md`, policy §6). Any stronger record axiom is an
  unmade owner-level decision per `AXIOM_MINIMALITY_POLICY.md`.
- It **does not** set or predict an audit status; later status is generated by
  the independent audit pipeline.
- It **does not** import PDG values, literature comparators, or fitted
  selectors. All checks are pure algebra on `M_n(C)`, the `Z₃` carrier, real
  anti-Hermitian operators, and the supplied `r → 2r²` map.

## Cross-references
- [`MINIMAL_AXIOMS_2026-06-04.md`](MINIMAL_AXIOMS_2026-06-04.md) — approved
  narrow Record axiom (the baseline this candidate would exceed).
- [`OBSERVABLE_PRINCIPLE_RECORD_SCALAR_MAP_NO_GO_NOTE_2026-06-05.md`](OBSERVABLE_PRINCIPLE_RECORD_SCALAR_MAP_NO_GO_NOTE_2026-06-05.md)
  — Record alone does not derive the branch-to-scalar (Born) map.
- [`FLAVOR_EINSELECTION_2SECTOR_MODULO_KREALITY_2026-06-02.md`](FLAVOR_EINSELECTION_2SECTOR_MODULO_KREALITY_2026-06-02.md)
  — K-real coupling einselects the 2 real sectors; Born gives `r=1`, not `r=1/2`.
- [`FLAVOR_R_HALF_IS_THE_RECORDS_FLOW_SEPARATRIX_2026-06-02.md`](FLAVOR_R_HALF_IS_THE_RECORDS_FLOW_SEPARATRIX_2026-06-02.md)
  — `r=1/2` is the unstable separatrix of `r→2r²`.
- [`CPT_EXACT_REAL_ANTI_HERMITIAN_D_NARROW_THEOREM_NOTE_2026-05-10.md`](CPT_EXACT_REAL_ANTI_HERMITIAN_D_NARROW_THEOREM_NOTE_2026-05-10.md)
  — real anti-Hermitian `D` ⟺ `Θ`-invariance (the CPT-even equivalence).
- `docs/audit/AXIOM_MINIMALITY_POLICY.md` §6 — explicit owner-approval gate for
  axiom changes.
