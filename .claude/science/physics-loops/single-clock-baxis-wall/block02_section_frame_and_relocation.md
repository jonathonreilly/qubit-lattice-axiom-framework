# Unified B-AXIS Obstruction Note — FRAMING SECTIONS (block02)

**Branch:** `physics-loop/single-clock-baxis-wall-block02-20260620` (stacked on block01)
**Type:** no_go (negative_route_pruning) + exact-support pin — FRAMING component
**Claim type (intended audit classification):** retained_no_go-grade obstruction;
proposal_allowed: false; bare_retained_allowed: false;
audit_required_before_effective_retained: true.
**Status authority:** independent audit lane ONLY. This note authors no audit grade,
sets no publication status, and edits no audit-lane file.
**No new axiom / no new primitive.** A_min = Lattice + Quantum + Record only. Every
load-bearing fact below is recomputed in-tree by an absorbed runner (Section MC);
no load-bearing edge is taken to the conditional parent keystone, the unaudited
finite-speed cone note, or the downstream ANOMALY_FORCES_TIME consumer.

Target keystone: `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03`
(audited_conditional, bounded_theorem, downstream fanout 959 / Class A). Its only
undischarged edge is the **B-AXIS** missing-bridge premise.

---

## 2. B-AXIS three-clause decomposition (N2 / N4 / N5) and per-clause retirement path

The B-AXIS premise of the single-clock keystone is not one opaque assumption. It
decomposes into exactly three premise clauses, each owning a distinct missing-bridge
question. The clause labels N2/N4/N5 are inherited verbatim from the governing fence
`SINGLE_CLOCK_UNIQUENESS_SCOPE_BOUNDARY_2026-06-06` (retained_no_go): that note's
N2/N4/N5 checklist clauses *became* B-AXIS.1/.2/.3, and it is cited here as the
governing boundary whose scope each clause inherits — Stone uniqueness held there only
**transfer-relative and τ-relative**, which is precisely why none of the three clauses
is auto-discharged by the spectral core.

| clause | B-AXIS slot | question | current honest status | retirement path (named supplier shape, NOT a closure) |
|---|---|---|---|---|
| **N2** | B-AXIS.1 | one supplied blocked time-step `2a_τ` | **split**: N2a exact-support-FORCED; N2b open | N2a needs nothing further (forced by the supplied `T̂²`). N2b retires only by a supplied **clock/rate bridge** carrying units of `1/time`. |
| **N4** | B-AXIS.2 | one declared evolution axis / RP-transfer construction (which of 4 Euclidean directions is time) | **open** (declared premise) | retires by a **non-transportable registration-direction bridge** OR a declared **per-axis Z₂ BC-asymmetry datum**, derived from A_min — neither exists. |
| **N5** | B-AXIS.3 | no independent commuting transfer factor admitted as a second clock | **open** (declared premise) | retires by a **`T̂²` irreducibility/nonfactorization theorem**, OR a **physical-clock-admission ray** `(L_s−1)`-param, OR a **gauge/redundancy theorem** — none supplied by A_min. |

**N2 sub-split (governing detail, absorbed from the blocked-time-unit-split branch and
re-run in block01).** N2 must never again be relisted as a single import:
- **N2a (exact-support, FORCED — NOT a wall):** for the supplied two-step staggered
  transfer `T̂² = exp(−2 a_τ H)`, the aligned reconstruction
  `H_block = −(1/(2a_τ)) log(T̂²/M_T)` is forced internally by the retained two-step
  blocked-time normalization bridge. The one-step denominator `1/a_τ` is a
  falsifier that doubles every non-vacuum energy (`H_wrong = 2·H_block`). This is a
  source-side consequence of the already-retained `T̂²`, not a new import.
- **N2b (open / no-go):** the *absolute* physical clock unit `a_τ` (a number carrying
  units of time) is NOT derived. This is the only walling half of N2.

Each clause's retirement path names a **supplier shape**, never a new axiom. Per the
no-new-axiom hard rule, a clause that could only close by adding a primitive is
`infeasible`; every path above is an A_min-internal supplier that is simply *absent*
on the retained surface, which is exactly the no-go content.

---

## 3. NON-VACUITY witnesses — the premises exclude realizable things (load-bearing, not cosmetic)

A premise is cosmetic if dropping it changes nothing realizable. We exhibit two
explicit, machine-verified realizable objects that the B-AXIS premises *exclude*. Both
are recomputed in-tree (Section MC); neither is cited blind.

### Witness W-1 — [C-2CLK]: a genuine two-commuting-tensor-factor transfer with 2D generator span (kills "N5 is vacuous")

If N5 (no independent commuting transfer factor) were vacuous, A_min + equal-time
tensor locality would already force a single one-parameter clock orbit. It does not.
The supplied two-step transfer is itself **maximally factorized**:

`T̂² = ⊗_p diag(1, e^{−2E(p)})`,  `E(p) = arcsinh(√(m²+sin²p))`,

a tensor product of `L_s` commuting positive per-mode factor clocks. The recomputation
(runner `single_clock_n5_irreducibility_factor_clock_2026_06_20.py`, PASS=36/0) shows:
- the per-mode factors are positive-definite and **commute pairwise** (max comm
  resid = 0.00e+00);
- the **factor-generator tangent span has dimension `L_s`** (rank = 3 at `L_s = 3`),
  and two distinct mode generators `n_p, n_q` are linearly independent
  (`rank(n_0, n_1) = 2`) — a genuinely **2D (≥2-parameter) abelian generator span**,
  not a reparametrized single orbit;
- the relative factor flow is **not gauge** (a single-mode clock freezes a durable
  record `⟨n_1⟩` while `Ĥ` moves it; no swept single-clock time reproduces the alt
  clock's durable occupation, min-dist ≈ 0.40), so the second clock is
  **Record-visible**, hence realizable, hence genuinely excluded by the N5 premise.

The companion 2-qubit form (T_A⊗I, I⊗T_B commute resid 0, rank-2 span, U_A(1)⊗I off
the diagonal one-clock orbit min_gap 0.292) is the canonical [C-2CLK] countermodel of
the n5-factor-boundary branch; we cite it and do **not** rebuild it. Either form proves
the same thing: **a second commuting clock is realizable on the A_min surface, so N5 is
load-bearing.**

### Witness W-2 — [τ-RESCALE]: `2a_τ → 2c·a_τ` gives identical dimensionless transfer data (kills "N2b is vacuous")

If N2b (absolute clock unit) were vacuous, the surface would already pin `a_τ`. It does
not. The joint rescaling `a_τ → c·a_τ`, `H → H/c`, `Q → Q/c` is an **exact
one-parameter gauge** of every A_min observable (runner
`single_clock_n2b_joint_clock_unit_check_2026_06_20.py`, PASS=18/0):
- `T̂²` invariant (max Δ 5.6e-17), record-block kernel `K = exp(2a_τ Q)` invariant
  (max Δ 3.3e-16), full per-block evolution `T2 ⊗ K` invariant (max Δ 3.3e-16);
- the two retained rate gates jointly fix only the **dimensionless** datum
  (`m_gap · relaxation-time`, ratio invariant to 5.6e-17), while every dimensionful
  number (mass gap, relaxation rate) rescales.

So a whole one-parameter family of distinct absolute clock units yields *identical*
dimensionless transfer data: the absolute unit is realizable-but-unfixed, which is
exactly what the N2b premise must supply. **N2b is load-bearing.**

### Why N4 is non-vacuous (same shape, recorded for completeness)

N4 is load-bearing by the dual fact: the signed exchange unitary
`W = P_{τ↔1}·diag((−1)^{x_τ x_1})`, upgraded to **S₄-transitivity** over all four
Euclidean axes, maps every candidate temporal axis onto a spatial axis with residual 0
(absorbed from the S4-transportable branch and recomputed in block01's
`single_clock_n4_aut_enrichment_stabilizer_2026_06_20.py`, `|G_bare| = 384`,
axis image = transitive S₄, PASS=17/0). A whole orbit of four axis labels gives
identical surface data; the axis label is realizable-but-unfixed. **N4 is load-bearing.**

**Conclusion of Section 3.** N2/N4/N5 each exclude an explicitly realizable object
(a commuting second clock; a rescaled clock unit; an exchange-equivalent axis label).
None is cosmetic. The B-AXIS premise carries genuine content.

---

## 9. UNIFIED RESIDUAL RELOCATION — N2b + N4 + N5 funnel to one emergent-dynamics OPEN GATE

The three open residuals are not three independent missing lemmas. They are one and the
same residual, made visible by the **native-on-Z³ framing**.

### The native-on-Z³ framing

Treat time NOT as a 4th lattice coordinate (the Euclidean 4-torus reconstruction that
carries W / S₄), but as the **parameter of a one-parameter group/semigroup** `U(t)`
acting on a *fixed* spatial Hilbert space `⊗_{x∈Z³} C²`. In this framing there is no
"4th axis" object at all: time is `t ∈ R`, not `x_4 ∈ Z`. The
**which-of-4-axes question DISSOLVES** — there is nothing to permute, so W / S₄ have no
axis to act on, and N4's axis-label problem evaporates as a *question*.

But dissolving the question is not deriving the answer. The framing **RELOCATES, does
not derive**:
- the generator of `U(t)` is **not axiom-supplied**. The only retained lattice generator
  is the RP/transfer reconstruction — i.e. the 4-torus route that carries W / S₄. A
  generator sourced from a record-production layer lands squarely in the
  emergent-dynamics OPEN GATE (record formation is not unconditionally forced by A_min);
- the **rate / metric** still needs a supplied `τ` (this is N2b — the
  [τ-RESCALE] gauge is exactly the statement that `U(t)` has no native unit);
- **no-second-commuting-clock** is still unproven (this is N5 — the [C-2CLK] 2D span
  is exactly the statement that `⊗_{x∈Z³} C²` admits commuting factor flows on the
  fixed spatial space);
- **orientation** (past → future) is NOT sourced by the framing: it is carried by the
  **past-hypothesis** (low-record initial condition `↔` spectrum-condition `H ≥ 0`).

So the three residuals collapse onto a single object: **the existence/derivation of a
one-parameter generator over the fixed spatial Hilbert space from a conditional
record-production dynamics layer, with a supplied time-step/rate `τ` and a
no-second-commuting-clock admission rule.** That object is precisely the
**emergent-dynamics OPEN GATE of `MINIMAL_AXIOMS_2026-06-05`**: Lattice supplies
`Z³` + adjacency but no dynamics / no metric scale; Quantum supplies the site algebra
but no dynamics; Record supplies durable additive registration but no time metric / no
occupancy rule / no dynamics. Arrow, measurement, decoherence, and **record-production
dynamics** are listed there as EXPLICIT OPEN GATES outside axiom content.

```
                          native-on-Z³ framing
   N4 (which axis?)  ──────────────────────────────►  DISSOLVED as a question
                                                       (no 4th coordinate to permute)
                                  │
   N2b (absolute unit a_τ) ───────┤
                                  ├──► ONE emergent-dynamics OPEN GATE:
   N5 (second commuting clock) ───┤    derive U(t) over ⊗_{x∈Z³} C² from a
                                  │    record-production dynamics layer
   orientation (t → −t) ──────────┴──► carried by PAST-HYPOTHESIS, not records
                                       (ARROW_FROM_RECORD_FORMATION_PAST_HYPOTHESIS_
                                        RESIDUAL_2026-06-05)
```

### Orientation firewall (cite, do not re-derive)

The arrow is *not* records-sourced and must not be claimed as derived here. It is fixed
only by the spectrum-condition `H ≥ 0` ⟺ low-record past hypothesis, per
`ARROW_FROM_RECORD_FORMATION_PAST_HYPOTHESIS_RESIDUAL_2026-06-05` (the records-arrow
note onto which the genuine orientation source is relocated). The block01 fresh-attempt
R-N4-REGDIR confirmed in-tree that the A_min record-accumulation monotone is a
W-invariant reflection-symmetric **ball, not a cone**, and that the up/down record
profile is set by the supplied low/high-record boundary — i.e. by the past hypothesis,
not by records per se.

### What relocation does NOT buy

Relocation is honest, not triumphant. The native framing is **an honester premise shape,
NOT fewer admissions**: it does not reduce the admission content, it renames where the
admission lives. The residual is genuinely open; B-AXIS stays **live**. The note is a
no-go about the **retained surface**, not an impossibility proof. (Off-surface,
dimension-selection — why `Z³` and one time — remains axiomatic; the exact-zero W / S₄
facts are bounded to **even cubic-symmetric** blocks, odd-`L` falsifier resid 6.000.)

---

## MC. MACHINE-CERTIFICATE INDEX (absorbed / consolidated runners)

Every load-bearing framing fact above is **recomputed in-tree**, not cited blind. All
four block01 runners were re-run in this section and report the stated totals.

| runner (absolute path) | clause / fact | PASS/FAIL | branch | absorbed for |
|---|---|---|---|---|
| `/Users/jonBridger/tp-audit-bridge-20260620/scripts/single_clock_n4_aut_enrichment_stabilizer_2026_06_20.py` | N4: `|G_bare|=384`, axis image transitive S₄; every A_min enrichment joint stabilizer full-S₄ or trivial; even-extent scope | **PASS=17 FAIL=0** | in-tree (block01-20260620) | §3 N4 non-vacuity (S₄ orbit); §9 native framing |
| `/Users/jonBridger/tp-audit-bridge-20260620/scripts/single_clock_n5_irreducibility_factor_clock_2026_06_20.py` | N5: supplied `T̂²` maximally factorized, `L_s` commuting per-mode clocks, rank-`L_s` generator span, factors not gauge | **PASS=36 FAIL=0** (B_AXIS_DERIVED=FALSE, SECOND_PHYSICAL_CLOCK_EXCLUDED=FALSE) | in-tree (block01-20260620) | §3 W-1 [C-2CLK]; §9 N5 funnel |
| `/Users/jonBridger/tp-audit-bridge-20260620/scripts/single_clock_n2b_joint_clock_unit_check_2026_06_20.py` | N2b: joint `a_τ→c·a_τ, H→H/c, Q→Q/c` exact 1-param gauge; gates fix only dimensionless ratio; N2a forced | **PASS=18 FAIL=0** | in-tree (block01-20260620) | §3 W-2 [τ-RESCALE]; §2 N2 split; §9 N2b funnel |
| `/Users/jonBridger/tp-audit-bridge-20260620/scripts/single_clock_registration_direction_bridge_n4_regdir_2026_06_20.py` | N4: record-accumulation monotone is W-invariant ball not cone; LR cone transports with H (circular); arrow = past-hypothesis | **PASS=20 FAIL=0** | in-tree (block01-20260620) | §9 orientation firewall / relocation |

**Aggregate of the four absorbed framing runners: PASS=91 FAIL=0, cracks=0**
(matches `SINGLE_CLOCK_BAXIS_FRESH_ATTEMPTS_STRETCH_NOTE_2026-06-20.md`).

### Source-discipline statement (load-bearing)

This framing component takes **NO load-bearing citation edge** to:
- the **conditional parent keystone**
  `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03`
  (audited_conditional — citing it blind would make the wall conditional on an
  unaudited parent);
- the **unaudited finite-speed registration cone note**
  (the R-N4-REGDIR cone fact is recomputed in-runner instead);
- the **downstream ANOMALY_FORCES_TIME consumer**
  (count-not-label is recomputed, not inherited from the consumer).

Every load-bearing fact is reproduced by an in-tree runner listed above (the
source-discipline lesson established by the axis-nogo-self-contained branch:
recompute, do not cite blind).

### Authorities CITED as authorities (not recomputed — RETAINED no-gos + minimal axioms)

These may be cited per the campaign hard rules; they are the governing fences and the
witnesses block01 does not itself cover:
- `SINGLE_CLOCK_UNIQUENESS_SCOPE_BOUNDARY_2026-06-06` (retained_no_go) — governing
  fence; source of the N2/N4/N5 clause labels; Stone transfer-/τ-relative.
- `SINGLE_CLOCK_AXIS_SELECTION_FROM_RECORD_DURABILITY_NARROW_NO_GO_2026-06-11`
  (retained_no_go) — OS/GNS, durability, cone-circularity, anomaly count-not-label
  W-transport witnesses; sharpened pin (per-axis Z₂ BC-asymmetry).
- `SINGLE_CLOCK_KMS_APBC_AXIS_SUPPLIER_NO_GO_2026-06-16` (retained_no_go) — KMS/APBC
  exchange-covariant (W maps APBC-τ → APBC-x₁); cited as pruned route, not re-tested.
- `MINIMAL_AXIOMS_2026-06-05` — A_min content + the EXPLICIT OPEN GATES (arrow,
  measurement, decoherence, record-production dynamics) that §9 relocates onto.
- `ARROW_FROM_RECORD_FORMATION_PAST_HYPOTHESIS_RESIDUAL_2026-06-05` — orientation
  carried by past-hypothesis (§9 orientation firewall).

**Boundary flags:** B_AXIS_DERIVED = FALSE; B_AXIS_CONSUMED_AS_PREMISE = TRUE;
AUDIT_LEDGER_WRITTEN = FALSE; AUDIT_VERDICT_APPLIED = FALSE. Independent audit lane is
the sole status authority.
