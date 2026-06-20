# Single-Clock B-AXIS Wall — Reassessment Note (Block 05, exercise-surfaced routes)

**Date:** 2026-06-20
**Branch:** `physics-loop/single-clock-baxis-wall-block05-20260620`
**Type:** no_go-correction + reassessment (additive amendment of the block02
unified no_go; no new derivation, no closure)
**Claim type:** no_go-correction (a reassessment of an existing `no_go`, not a
fresh negative-route-pruning and not a `bounded_theorem`)
**Status:** honest reassessment of the consolidated B-AXIS obstruction on the
retained even-extent staggered-Dirac surface. Two block02 overclaims corrected
(N5 linear-span algebra; N5 `(L_s−1)`-param ray; N4-as-label consumer
over-specification); two clauses confirmed walled, sharper (N2b form↔spacing;
the corrected-algebra N5 wall still stands); NO clause closes from A_min + the
four approved primitives; NO new axiom or primitive; all residuals stay on the
emergent-dynamics / boundary-condition OPEN GATE. `proposal_allowed=false`;
`bare_retained_allowed=false`; `audit_required_before_effective_retained=true`.
Independent audit lane is the sole status authority.

**Boundary flags:** B_AXIS_DERIVED = FALSE; B_AXIS_CONSUMED_AS_PREMISE = TRUE;
SECOND_PHYSICAL_CLOCK_EXCLUDED = FALSE; N4_LABEL_DERIVED = FALSE;
AUDIT_LEDGER_WRITTEN = FALSE; AUDIT_VERDICT_APPLIED = FALSE;
NEW_AXIOM_ADDED = FALSE.

**A_min = Lattice + Quantum + Record + the FOUR approved primitives only**
(`minimal_axioms`, `scale_reference_primitive`, `kinetic_isotropy_primitive`,
`realized_state_primitive`, per `docs/audit/data/axiom_premise_nodes.json`). The
approved primitives are legitimate premises that chain-satisfy without bounding;
they are NOT new axioms. Per the primitive registry: `kinetic_isotropy` grants
ONLY structural OS0 form isotropy `c_t=c_s` (not a spacing ratio, scale,
selector, or dynamics); `scale_reference` is units-only; `realized_state` is
pointwise specialization (the counterfactual clause: a realized-state-dependent
result is registered data, not a derivation).

**Consolidated reassessment runner:**
`scripts/single_clock_baxis_reassessment_2026_06_20.py`
(TOTAL **PASS=34 FAIL=0**; cache
`logs/runner-cache/single_clock_baxis_reassessment_2026_06_20.txt`), which
re-exercises the four load-bearing corrected facts in-tree. The five
per-route runners (aggregate PASS=143 FAIL=0) are indexed in Section 6.

---

## 0. Provenance — this is an exercise reassessment, not a fresh campaign block

This note reassesses the block02 consolidated no_go
(`docs/SINGLE_CLOCK_BAXIS_OBSTRUCTION_UNIFIED_NO_GO_NOTE_2026-06-20.md`) in light
of the `baxis-wall-break` exercise (packet
`.claude/science/exercises/baxis-wall-break/`: `EXERCISE.md` states the wall
neutrally; `ATTACK_VECTORS.md`, `ASSUMPTIONS_TABLE.md`, `LITERATURE_SEARCH.md`,
`MATH_SECTOR_SEARCH.md`, `REFRAMING.md` are the route-portfolio panels). The
exercise surfaced five attack routes against the B-AXIS wall; each was verified
by an independent max-rigor route author with its own runner. This note is the
**block05 synthesis**: it records each verified outcome, states the corrected
(sharper, sometimes weaker) wall scope, and feeds an additive correction section
into the block02 unified no_go.

**Posture (binding).** This is honest verification, NOT a defense of the
existing no_go. Where a route shows block02 overclaimed, we say so plainly and
quantify the correct statement. Where a route confirms the wall by an
independent mechanism, we record it sharper. NO route closed a clause; NO route
cracked the wall.

---

## 1. Executive reassessment — what shrank, what stays walled

| route | clause(s) | exercise claim | verified outcome | corrects block02? | runner |
|---|---|---|---|---|---|
| **R-FC-N5** | N5 | "second clock is functional calculus of ONE operator `{f(Ĥ)}`, not a second operator; linear span `{I,Ĥ}` is the wrong algebra" | **confirms_wall_sharper** (with an embedded overclaim correction): algebra critique CORRECT, but exercise's *predicted dissolution* FALSE — the supplied `Ĥ` is heavily degenerate, so a real second-clock room survives. **Wall STANDS, re-grounded on `{Ĥ}''`.** | **yes** (N5 reasoning + ray size) | `single_clock_n5_functional_calculus_one_clock_2026_06_20.py` PASS=50/0 |
| **R-COUNT-N4** | N4 | "the 959 consumer reads only the COUNT `d_t≤1`, not the axis LABEL" | **corrects_overclaim**: the count is S₄-invariant / label-free (one orbit); the LABEL is genuine non-derivable data but **over-specified for the sole consumer**. N4-as-label-wall shrinks *for the cone*. | **yes** (consumer-relevance framing) | `single_clock_count_label_free_n4_2026_06_20.py` PASS=16/0 |
| **R-DICHOTOMY-N5** | N5 | "the `L_s`-fold tower is the free-fermion integrable charge tower, not a generic A_min obstruction" | **shrinks_wall**: `Ĥ` is a free-fermion `H`; a minimal A_min-admissible local interaction destroys the tower. Corrected N5 holds **conditional on non-integrability** — a one-bit premise, not `(L_s−1)` params. | **yes** (ray → one bit) | `single_clock_n5_integrability_dichotomy_2026_06_20.py` PASS=37/0 |
| **R-KINFORM-N2b** | N2b | "form isotropy `c_t=c_s` + units-only scale pin `a_τ`" | **confirms_wall_sharper**: the hoped form↔spacing identity `c_t/c_s == a_τ/a_s` is FALSE; the primitives do NOT discharge the absolute clock unit. N2b stays open, no-go gains a sharper 6th column. | **no** (additive only) | `single_clock_kinform_spacing_bridge_n2b_2026_06_20.py` PASS=16/0 |
| **R-DEFINABILITY** | N2b+N4+N5 | "upgrade route-exhaustion to a Beth/Svenonius independence theorem; crack-check the three primitives" | **confirms_wall_sharper**: independence theorem ships (`a_τ`, axis-label, clock-ray each undefinable from A_min + all three primitives); **NO CRACK**. Sharpens N4 (kinetic_isotropy grants the isotropic `S₄`-transitive form, closing REFRAMING A1). | **no** (additive sharpening) | `single_clock_definability_independence_2026_06_20.py` PASS=24/0 |

**Net.** Three corrections of block02 (all three about the *shape/size/relevance*
of a wall, none flipping a derivation result), two independent sharper
confirmations, zero closures, zero cracks. The corrected B-AXIS wall is
**smaller and more honest** than block02's, and rests on the right algebra.

---

## 2. The corrected B-AXIS wall scope (per clause)

### 2.1 N5 (B-AXIS.3) — corrected on TWO independent axes; wall STANDS

Two routes attacked N5 and both corrected block02; their corrections compose.

**(a) R-FC-N5 — the algebra (functional calculus, not linear span).**
Block02 §6.2 `[GAUGE]` and Witness W-1 argue the per-mode factor flows are "not
gauge ⇒ independent second clocks" because their generators escape
`span{I,Ĥ}` (resid ≈0.65), concluding an `(L_s−1)`-parameter admission ray.
**This is the wrong algebra.** "Function of the single generator `Ĥ`" is not
"in the 2-d linear span `{I,Ĥ}`"; it is membership in `{Ĥ}'' = {f(Ĥ)}`, the
spectral functions of `Ĥ`, whose dimension is the **number of distinct
eigenvalues of `Ĥ`** — generally far larger than 2 (`Ĥ²`, `√Ĥ`, `log Ĥ`, every
spectral projector escape `span{I,Ĥ}` yet none is a second clock). Escaping
`span{I,Ĥ}` is **necessary but far from sufficient**; the correct discriminator
is `n_p ∉ {f(Ĥ)}`.

The corrected test still finds a real second-clock room, but for a reason
block02 never identified: the **supplied many-body `Ĥ = Σ_p E(p) n_p` is heavily
degenerate**. Recomputed in-tree (runner `[FC]`):

| `L_s` | Fock dim `2^{L_s}` | #distinct eigs = dim `{f(Ĥ)}` | undercount vs span `{I,Ĥ}`=2 | second-clock room `2^{L_s}−#distinct` | block02 `(L_s−1)` |
|---|---|---|---|---|---|
| 4 | 16 | 9 | 7 | **7** | 3 |
| 6 | 64 | 15 | 13 | **49** | 5 |
| 8 | 256 | 45 | 43 | **211** | 7 |

Every `n_p` has a nonzero functional-calculus residual (`min` fc-resid 1.41 /
2.83 / 5.66) — **0 of `L_s` factor directions are functions of `Ĥ`**; all
distinguish a degenerate `Ĥ`-eigenspace. The degeneracy is structural
(reflection `E(p)=E(L_s−p)` since `sin²p = sin²(2π−p)`: distinct single-mode
`E` = 2/2/3 of 4/6/8) plus accidental energy-sum collisions. The **falsifier**
seals the dichotomy: a generic non-degenerate generator makes every `n_p=f(Ĥ)`
exactly (room 0, single clock outright; runner `[FC]` FALSIFIER, max resid 0).

> **Corrected N5 (algebra).** A commuting durable-record observable is a
> re-clocking of the single supplied clock **iff** it lies in `{Ĥ}'' = {f(Ĥ)}`,
> whose dimension is the number of DISTINCT eigenvalues of `Ĥ`, NOT 2. Genuine
> independent commuting clock directions live ONLY inside `Ĥ`'s DEGENERATE
> eigenspaces, of total dimension `2^{L_s} − #distinct`. On a non-degenerate
> spectrum this room is 0 (N5 holds with a single clock outright). On the
> supplied staggered surface `Ĥ` IS degenerate, so the N5 wall STANDS — but its
> size and cause are corrected to the `Ĥ`-degeneracy room, not a `(L_s−1)`-param
> linear-span escape.

So block02 got the **right answer (live wall) for the wrong reason**.

**(b) R-DICHOTOMY-N5 — the cause (integrability, not generic A_min).**
The `L_s`-fold commuting tower `{n_p}` is the textbook **free-fermion
conserved-charge tower** of the Gaussian `Ĥ = Σ_p E(p) n_p` (recomputed: `Ĥ` is
quadratic, `spec(h)=E(p)`). It is the **integrable signature**, not a generic
A_min obstruction. A minimal A_min-admissible local interaction
`V = g Σ_x n_x n_{x+1}` (Hermitian, on-site `M_2(ℂ)`, number-preserving,
dimensionless `g`) **destroys the tower**: every mode charge decommutes
(`min ‖[Ĥ_int,n_k]‖ = 0.165`), and the bilinear conserved-charge span collapses
(clean NN chain `L=5`: **9 → 1**, toward `{I,N,Ĥ}`), generically in `g`.

> **Corrected N5 (cause).** The `L_s`-fold tower is the free/integrable
> signature; a generic (non-integrable) A_min-admissible local interaction
> collapses it to a single conserved `Ĥ`. N5 holds **conditional on
> non-integrability of the emergent dynamics** — a one-bit generic-position
> premise, NOT an `(L_s−1)`-parameter physical-clock-admission ray.

**Composed corrected N5.** The genuine residual freedom is one open bit ("is the
emergent dynamics integrable?"), and the room — *should* the dynamics be the
special free/integrable one — lives precisely inside `Ĥ`'s degenerate
eigenspaces (`{Ĥ}''` complement), not in a `(L_s−1)`-d linear-span escape.
**N5 stays a LIVE wall**: A_min supplies no dynamics (the emergent-dynamics OPEN
GATE), so it can assert neither non-integrability nor a degeneracy-lifting clock
selector. No approved primitive supplies it: `kinetic_isotropy` gives only OS0
form isotropy (not a clock selector); `scale_reference` is units-only;
`realized_state` would make any degeneracy-lifting clock pick
realized-state-dependent registered data, not a derivation (counterfactual
clause). The missing supplier is **unchanged in kind, crisper in shape**: either
a second independently-supplied positive transfer (A_min supplies exactly one
`T̂²`) or a non-integrability / degeneracy-lifting rule.

### 2.2 N4 (B-AXIS.2) — label dissolved FOR THE SOLE CONSUMER; label-derivation still walled

**R-COUNT-N4.** The keystone's only consumer is
`docs/ANOMALY_FORCES_TIME_THEOREM.md` (downstream fanout 959). Verbatim, it
reads from B-AXIS exactly the codim-1 **COUNT** cap `d_t ≤ 1` ("given B-AXIS,
there is one admitted clock factor, so `d_t ≤ 1`"), never the axis **LABEL**
(its non-circularity section: the argument "constrains only the *count* `d_t`
… not which axis is temporal"; its conclusion is the pure signature `(3,1)`).

Recomputed in-tree (runner `[CNT]`): the four per-axis codim-1 constructions
form **exactly one** inequivalence class modulo S₄ (every `g ∈ G_bare`, `|G|=384`,
maps `D_a → ±D_{π(a)}` with resid 0; orbit of axis 0 = `{0,1,2,3}`), so the
count `d_t ≤ 1` is an **S₄-invariant, label-free** statement, and is supplied
(one declared construction). The label is genuine, non-vacuous data
(`‖D_0−D_1‖ = 1.41` before the quotient; `W_{0,1}` carries `D_0` onto `D_1`
exactly after it) — but the consumer **never reads it**.

> **Corrected N4 scope.** N4 splits into a COUNT part and a LABEL part. The count
> part (`d_t ≤ 1`) is the only N4 content the 959-cone consumer reads; it is
> supplied and S₄-invariant (label-free). The LABEL part ("which Euclidean axis
> is time") remains **non-derivable from A_min** (S₄-transitive — the genuine
> wall) but is **over-specified for this consumer**: no step, nor the
> `(3,1)`-signature conclusion, reads the label. For the 959 cone, N4 functions
> as a *count* premise, not a *label* premise.

This is a **consumer-relative scope correction**, not a closure: it does NOT
derive N4 from A_min, does NOT touch N2b, and does NOT touch N5 (which IS the
count cap and stays a genuine wall). The N4-derivation wall (S₄-transitivity) is
recomputed and stands.

### 2.3 N2b (B-AXIS.1, open half) — confirmed walled, sharper; no overclaim

**R-KINFORM-N2b.** The tempting route: `kinetic_isotropy` (form `c_t=c_s`) +
`scale_reference` (`a_s = 1/M_Pl`) pin `a_τ`. It requires a separate form↔spacing
theorem `c_t/c_s == a_τ/a_s`. Exact sympy (runner `[KIN]`) shows that identity is
**false in every legitimate normalization convention**: the bare-dispersion `k²`
coefficient is 1 on every axis (spacing-independent), so `c_t/c_s` is 1
(continuum-normalized convention, a tautology) or `(a_s/a_τ)²` (bare-hopping
convention) — never `a_τ/a_s`. Form isotropy `c_t=c_s` is satisfiable at
**`a_τ ≠ a_s`** via the unfixed anisotropic kinetic weights `(κ_t, κ_s)`
(witness: at `a_τ=2a_s`, `κ_t/κ_s=4` restores `c_t=c_s`, resid 0). Recovering
`a_τ=a_s` requires `κ_t=κ_s`, which **is** the form-primitive content (circular).
`scale_reference` is units-only and pins one spacing, never the ratio.

> **N2b stays OPEN.** The approved primitives do NOT discharge the absolute clock
> unit. `kinetic_isotropy` grants only the form ratio `c_t/c_s`, never the spacing
> ratio `a_τ/a_s`; the form↔spacing bridge is not a theorem from A_min + the form
> primitive (it needs `κ_t=κ_s`, the form primitive itself). This is an
> **additive sharper 6th N2b column**, not a correction of any block02 wording.

### 2.4 All three clauses — independence theorem, NO CRACK on any primitive

**R-DEFINABILITY.** Writing the observable structure's automorphism group
explicitly (`G1` τ-rescale `ℝ_{>0}`; `G2` factor-permutation `S_{L_s}`; `G3`
signed `B₄` with transitive `S₄` axis image) and applying Svenonius upgrades the
block02 route-exhaustion to a definability **independence theorem**: `a_τ` (N2b),
the axis label (N4), and the clock-ray (N5) are each moved by an automorphism
that **survives adjoining all three approved primitives**, hence each is
**undefinable** from `A_min + {scale_reference, kinetic_isotropy,
realized_state}`. The crack check finds **NO CRACK**: `scale_reference` fixes
only the spatial unit (the spacing ratio `a_τ/a` is disclaimed); `kinetic_isotropy`
supplies the **isotropic** `c_t=c_s` form whose axis image is transitive `S₄`
(the axis-selecting datum `c_t≠c_s` is exactly what it does NOT grant — this
closes the REFRAMING A1 open lead); `realized_state` gives only pointwise
evaluation and the realized axis varies over W-conjugate record loci, so it is
registered data by the counterfactual clause.

> **Additive sharpening of block02 §5.2.** Block02's headline "NO A_min
> enrichment has a one-axis-selecting (S₃) stabilizer" should record that a
> one-axis-selecting enrichment DOES exist — the anisotropic kinetic form
> `c_t≠c_s` — and that it is excluded not because no S₃ enrichment exists but
> because the approved `kinetic_isotropy` primitive supplies the **isotropic**
> form (transitive S₄). The N4 wall thus rests on the positive premise-level
> fact "the granted kinetic form is the symmetric one" — strictly stronger.

---

## 3. Honest residual — what stays genuinely open

After all five routes, the B-AXIS wall is **smaller and re-grounded**, but no
clause closes:

- **N2b** — the absolute clock unit `a_τ` is undefinable from A_min + all three
  primitives (independence theorem); the form↔spacing bridge that would let the
  primitives pin it does not exist. **Open.**
- **N4-label** — undefinable from A_min + the primitives (transitive S₄ survives
  `kinetic_isotropy`'s isotropic form). It is **over-specified** for the sole
  959 consumer (which reads only the S₄-invariant count `d_t ≤ 1`), so the
  *label-wall shrinks for the cone* — but N4-label-derivation **stays walled**.
- **N5** — the second-clock room is corrected to the `Ĥ`-degeneracy room
  (`{Ĥ}''` complement) and the missing supplier shrinks from an `(L_s−1)`-param
  ray to **one non-integrability bit**, but A_min supplies no dynamics, so N5
  stays a **LIVE wall** conditional on the open emergent-dynamics gate.

All residuals still funnel to the single **emergent-dynamics / boundary-condition
OPEN GATE** of `MINIMAL_AXIOMS_2026-06-05` (no dynamics, no time metric, no
record-production dynamics, no boundary datum, no occupancy rule). The native-on-Z³
framing of block02 §7 is unchanged: it dissolves the which-axis *question* but
relocates rather than derives.

---

## 4. Scope (binding on every exact-zero / corrected statement)

1. **Even cubic-symmetric only.** The S₄-transport facts (N4), the `Ĥ`-degeneracy
   counts (N5 R-FC), and the definability automorphisms hold on EVEN
   cubic-symmetric staggered-Dirac blocks; the odd-`L` falsifier
   `‖W M Wᵀ − M‖ = 6` is inherited from block02 §10.1. (Honesty leg: R-COUNT-N4
   shows the COUNT cap stays axis-uniform even on the odd block where the LABEL
   transport `W` fails — the count the consumer reads is robust beyond the
   even-extent LABEL-wall scope.)
2. **`L_s=3` excluded for the integrability route.** The 3-site periodic ring is
   the complete graph `K₃`, so `V` is number-only and cannot break the tower;
   R-DICHOTOMY uses `L_s ≥ 4`.
3. **Surface-specific, not an impossibility proof.** The degeneracy counts and
   tower dimensions are surface-specific; the single-clock-iff-non-degenerate
   dichotomy and the integrability collapse are general facts proved on the
   generic + clean-NN legs. No continuum claim.
4. **Conditional parent.** The keystone parent
   (`axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03`,
   audited_conditional) is itself conditional; every load-bearing fact here is
   recomputed in-runner, not cited blind from the parent, the unaudited
   finite-speed cone note, or the downstream ANOMALY_FORCES_TIME consumer (whose
   non-circularity / count-cap text R-COUNT-N4 recomputes verbatim).

---

## 5. Source-discipline statement (load-bearing)

This note takes **NO load-bearing citation edge** to the conditional parent
keystone, the unaudited finite-speed registration cone note, or the downstream
ANOMALY_FORCES_TIME consumer as a derivation authority. Every corrected
load-bearing fact (functional-calculus reachability + degeneracy; label-free
count S₄-invariance; integrability collapse; form↔spacing separation) is
recomputed in the consolidated runner and the five per-route runners from the
supplied dispersion `E(p)=arcsinh(√(m²+sin²p))` and finite linear algebra /
exact sympy. ANOMALY_FORCES_TIME is referenced (R-COUNT-N4) only to recompute
*what it reads* (count vs label), not as a derivation authority.

---

## 6. Machine certificate index

**Consolidated reassessment runner (this note):**

| runner | corrected facts | PASS/FAIL |
|---|---|---|
| `scripts/single_clock_baxis_reassessment_2026_06_20.py` | `[FC]` `{f(Ĥ)}` dim = #distinct eigs (9/15/45), room `2^{L_s}−#distinct` (7/49/211), 0 of `L_s` reachable, generic-falsifier room 0; `[CNT]` `|G_bare|=384`, count equivariant resid 0, single S₄ orbit, label≠count; `[INT]` free tower commutes then collapses 9→1 under A_min-admissible `V`, generic in `g`; `[KIN]` `c_t/c_s ≠ a_τ/a_s` in all conventions, `κ_t/κ_s=4` countermodel, `κ_t=κ_s` circular | **PASS=34 FAIL=0** |

**Per-route runners (verified, recomputed this cycle):**

| runner (absolute path) | route / clause | PASS/FAIL |
|---|---|---|
| `/Users/jonBridger/tp-audit-bridge-20260620/scripts/single_clock_n5_functional_calculus_one_clock_2026_06_20.py` | R-FC-N5 / N5 functional calculus + degeneracy | **PASS=50 FAIL=0** |
| `/Users/jonBridger/tp-audit-bridge-20260620/scripts/single_clock_count_label_free_n4_2026_06_20.py` | R-COUNT-N4 / N4 label-free count | **PASS=16 FAIL=0** |
| `/Users/jonBridger/tp-audit-bridge-20260620/scripts/single_clock_n5_integrability_dichotomy_2026_06_20.py` | R-DICHOTOMY-N5 / N5 integrability | **PASS=37 FAIL=0** |
| `/Users/jonBridger/tp-audit-bridge-20260620/scripts/single_clock_kinform_spacing_bridge_n2b_2026_06_20.py` | R-KINFORM-N2b / N2b form↔spacing | **PASS=16 FAIL=0** |
| `/Users/jonBridger/tp-audit-bridge-20260620/scripts/single_clock_definability_independence_2026_06_20.py` | R-DEFINABILITY / N2b+N4+N5 independence | **PASS=24 FAIL=0** |

**Aggregate of the five per-route runners: PASS=143 FAIL=0, cracks=0.**

**Route section sources (this campaign):**
`.claude/science/physics-loops/single-clock-baxis-wall/block05_section_{R-FC-N5,R-COUNT-N4,R-DICHOTOMY-N5,R-KINFORM-N2b,R-DEFINABILITY}.md`.

**Exercise packet (cited):**
`.claude/science/exercises/baxis-wall-break/{EXERCISE.md,ATTACK_VECTORS.md,ASSUMPTIONS_TABLE.md,LITERATURE_SEARCH.md,MATH_SECTOR_SEARCH.md,REFRAMING.md}`.

**Corrected artifact (additive correction section appended):**
`docs/SINGLE_CLOCK_BAXIS_OBSTRUCTION_UNIFIED_NO_GO_NOTE_2026-06-20.md`
(§ CORRECTION (2026-06-20, block05 exercise reassessment)).

---

## 7. Status discipline

Branch-local source artifact for
`physics-loop/single-clock-baxis-wall-block05-20260620`. Adds NO framework
axiom, introduces NO primitive, sets / updates NO audit status, edits NO audit /
publication / effective-status surface. Branch-local status vocabulary only; no
bare "retained"/"promoted" in any status line. Cited upstream statuses
(`retained_no_go`, `exact-support`, `audited_conditional`) are quoted from their
source notes, not reasserted here. `proposal_allowed=false`;
`bare_retained_allowed=false`; `audit_required_before_effective_retained=true`.
The independent audit lane is the sole status authority.
