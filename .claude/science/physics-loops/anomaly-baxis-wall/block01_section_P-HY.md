# Block01 Section — Edge P-HY (hypercharge identification)

**Keystone:** `anomaly_forces_time_abj_inconsistency_accepted_premise_bridge_bounded_note_2026-05-26` (fanout 1105)
**Edge:** P-HY — identify the bounded left-handed abelian eigenvalue surface
`{+1/3 ×6, −1 ×2}` with the physical anomaly-relevant `U(1)_Y` consumed by the
bridge's step B1.
**Runner:** `scripts/frontier_abj_phy_identification_routes_2026_06_20.py`
**Cache:** `logs/runner-cache/frontier_abj_phy_identification_routes_2026_06_20.txt`
**Result:** `TOTAL: PASS=41 FAIL=0`
**Scope:** A_min (Lattice+Quantum+Record) + the four approved primitives. No new
axiom/primitive. Source discipline: all load-bearing facts recomputed in-tree;
nothing cited blind from the unaudited keystone.

---

## 0. Disposition

- **Arithmetic core (B1 LH anomaly traces): BANKABLE** as a deps-all-retained
  bounded theorem (SM_ANOMALY_CLOSURE precedent). Recomputed in-tree.
- **Physical identification: still walled, but the wall SHRINKS.** Two of the
  three sub-pieces the prior framing carried as load-bearing admissions
  (alpha=1/3; species naming) are shown NOT load-bearing for the anomaly test.
  The single irreducible load-bearing withheld piece is the **"is-gauged"
  predicate** on the canonical u(1) direction (Route B1).

This edge is **not** a fresh hard wall warranting an exercise-skill run: the
wall is the *same* MINIMAL_AXIOMS gauge-group-withholding wall already
established and gate-tested across the in-flight P-HY branches; this block
sharpens it (shrinks it to the gauged predicate) rather than hitting a new one.

---

## 1. ABSORBED in-flight work (cited, NOT rebuilt)

Per GROUNDING_MAP duplication_warnings:

| Branch | Path | PASS | Absorbed as |
|---|---|---|---|
| abj-phy-supplier-wiring-20260618 | `docs/ABJ_P_HY_RETAINED_BOUNDED_SUPPLIER_WIRING_NOTE_2026-06-18.md` | 26 (parent 80) | source-side supplier-edge repair (hygiene, not derivation) |
| anomaly-hy-parent-edge-20260617 | re-route HY-surface citation to `GRAPH_FIRST_SU3_INTEGRATION_NOTE.md`; demote 2026-05-23 packaging | 90 | citation-hygiene precedent; graph-first is the load-bearing HY authority |
| hypercharge-chain-boundary-firewall-20260617 | fail-closed firewall on `HYPERCHARGE_IDENTIFICATION_NOTE.md` (10 req / 3 forbidden markers) | — | source-hygiene firewall pattern |
| abj-scale-free-anomaly-core | `ABJ_SCALE_FREE_NATIVE_ABELIAN_ANOMALY_CORE_BOUNDARY_NOTE_2026-06-18` | 54 | the scale-free anomaly core (Tr[Y_a³]=−48a³ etc.) — my Part A re-derives only enough to bank B1 in-tree |
| abj-hypercharge-completion-boundary-20260617 | `ABJ_HYPERCHARGE_COMPLETION_DECOUPLING_BOUNDARY_NOTE_2026-06-17` | 47 | full-generation cancellation witness + B1/B2/B3 negative lemmas |

I did **not** re-derive any of these. My runner independently recomputes the B1
trace tuple to bank it under source discipline.

---

## 2. Arithmetic core — BANKABLE (Part A of the runner)

Recomputed in-tree on the bounded surface `Y_a = a(P_sym − 3 P_anti)`
(+a ×6 on (2,3)=Sym², −3a ×2 on (2,1)=Anti²):

- **Scale-free shape** (a ∈ {1/3, 1, −2/5, 7} all PASS): `Tr[Y]=0`,
  `Tr[Y³]=−48a³`, `Tr[SU(3)²Y]=a`, `Tr[SU(2)²Y]=0`. The absolute scale `a`
  (=alpha) is **not load-bearing for the SHAPE of the anomaly polynomial.**
- **At a=1/3 (SM normalization) — the exact keystone B1 tuple:**
  `Tr[Y]=0`, **`Tr[Y³]=−16/9`**, **`Tr[SU(3)²Y]=1/3`**, **`Tr[SU(3)³]=2`**,
  `Tr[SU(2)²Y]=0`. Three nonzero ABJ-relevant traces — matches the keystone
  B1 line exactly, recomputed (not cited blind).
- **Bankability:** the arithmetic uses only the **retained** `graph_first_su3_
  integration_note` (effective_status=retained, chain_closes=True) + rational
  algebra; the L1 ratio and L2 matter-assignment notes are
  `decoration_under_graph_first_su3_integration_note` (retained as decorations
  under that parent). It does **not** route the arithmetic through the unaudited
  keystone. **=> deps-all-retained bounded-theorem candidate**, exactly the
  SM_ANOMALY_CLOSURE_RETAINED_ANCHORS_DECOUPLED move (retained_pending_chain,
  PASS=11). This is the high-value Decision-A deliverable for this edge.

**Runner caught a real arithmetic error mid-cycle** (logged): the first draft
computed `Tr[SU(3)²Y]` by summing T(fund)=1/2 over all 6 colour states
(=3a, wrong), instead of absorbing the colour trace into T(fund) and summing
over the 2 isospin components (=a, correct → 1/3 at a=1/3). Fixed; this is the
load-bearing-residual pattern (Memory: feedback_runner_load_bearing_residuals).

---

## 3. Fresh identification-route attempts (Part B)

### Route B1 — gauged-direction selection from the Record sector → **WALLED (sharpened)**

Attempt: derive the *narrowed* P-HY claim — "this nonzero native abelian
direction IS the gauged U(1) entering the anomaly test" — from Record-sector
structure (NOT full SM U(1)_Y).

- The commutant supplies a **canonical** traceless u(1) direction (retained
  `graph_first`); the DIRECTION is selected uniquely up to scale. **PASS** as a
  partial: the direction is supplied.
- But **"gauged"** (the symmetry couples as a connection whose anomaly threatens
  unitarity) is an external **dynamical predicate** A_min does not register.
  Recomputed in-tree from `MINIMAL_AXIOMS_2026-06-05.md` line 52 (Quantum axiom
  "does not supply ... gauge group, particle content") and lines 64–72 (Record
  supplies no sector-generation rule / weighting / normalization). **WALL.**
- **Counterfactual test (realized-state primitive policing):** no realized state
  makes Y "gauged"; gaugedness is a law-level structural input, not registered
  data — so it is **not rescuable as realized-state data** either (it would be a
  derivation claim, not registered data). Correctly applies exercise-lesson (3).
- **Net:** even the narrowed gauged-direction claim is not supplied. This is the
  one irreducible withheld piece that is load-bearing for the anomaly test.

### Route B2 — alpha=1/3 as pure gauge/convention → **PARTIAL WIN (admission removable for the anomaly test)**

Attempt: push the B3 rescaling hint to a clean "alpha is convention" lemma that
REMOVES the admission.

- **Lemma proven (runner B2, all PASS):** every ABJ anomaly polynomial is
  **homogeneous** in Y — degree-1 (Tr[Y], grav²Y, SU²Y) scales by λ, degree-3
  (Tr[Y³]) by λ³ — so the set {all anomalies = 0} is **invariant under
  Y→λY**. Verified at λ ∈ {2, −5, 1/7}. Therefore **within the
  anomaly-cancellation test the absolute scale alpha is a free normalization**
  (only ratios +1:(−3) and the forced RH ratios are invariant). **The alpha=1/3
  admission is HARMLESS / REMOVABLE for the keystone B1/B3 anomaly arithmetic.**
- **Wall remnant:** alpha=1/3 is NOT pure convention for the *physical electric
  charge value* (GMN `Q=T₃+Y/2` with `Q(e_L)=−1`): a rescaling changes
  `Q(e_L)`. That value-match is the alpha-bridge's admitted **P1–P4 SM
  conventions** (Anti²-as-L_L readout, GMN, T₃(e_L)=−1/2, Q(e_L)=−1).
- **In-tree ledger correction (source discipline):** the prior GROUNDING_MAP
  framing ("alpha=1/3 still conditional", "chain_closes=FALSE") is **stale**.
  On this branch base the ledger row `hypercharge_alpha_third_normalization_
  bridge_bounded_note_2026-05-25` is **retained_bounded, chain_closes=True**,
  and `hypercharge_identification_note` is **retained_bounded, chain_closes=
  True**. The bridge's own text is explicit that it "does not eliminate
  admission; it formally exposes the conditional chain" (P1–P4) — so the bridge
  is retained *as a bounded conditional packet*, with P1–P4 as named admitted
  conventions. **Carry this caveat verbatim; do not overstate to "alpha
  derived."** But for the ANOMALY arithmetic specifically, alpha is provably
  not load-bearing (the B2 lemma).

### Route B3 — L2 matter assignment from Cl(3) rep theory WITHOUT importing target labels → **HALF MET**

Attempt: the never-met 2026-05-02 audit repair target — construct the physical
map from the C⁸ taste sectors to SU(3) rep content without importing the target
labels.

- **Rep-content half — DERIVED label-free (runner B3, all PASS):** from the
  τ=SWAP eigendecomposition, Sym²-block dim=3, Anti²-block dim=1 (no labels);
  su(3) acts non-trivially on the 3-dim block ([λ₁,λ₂]=2iλ₃ verified) ⇒
  **fundamental (3)**; su(3) on the 1-dim block is forced trivial ⇒ **singlet
  (1)**. This is exactly `LHCM_MATTER_ASSIGNMENT_FROM_SU3_REPRESENTATION_NOTE_
  2026-05-02` (ledger=`decoration_under_graph_first_su3_integration_note`,
  retained). **This half of the repair target IS met.**
- **Wall remnant:** the repair target also asked for the **physical map to "SM
  left-handed fermion representations"** — i.e. *naming* the SU(3)-fundamental
  Weyl the physical quark doublet. "color-charged ≡ quark" is a **definitional
  SM convention**, not derivable from A_min (line 52: no species
  identification). **BUT** for the anomaly test only the **rep content (3 vs 1)
  and the hypercharge values** enter — the species **name** is not load-bearing
  in the anomaly polynomial. Applied exercise-lesson (2): membership tested in
  the rep-theoretic structure {generator}'' (su(3) action), not a label import.

---

## 4. Algebra correctness (exercise lessons applied)

- Lesson (1): loaded the four approved primitives — Route B1 explicitly tested
  the **Record** axiom and the **realized_state** primitive, not bare 3-axioms.
- Lesson (2): Route B3 tests membership in the rep-theoretic structure (su(3)
  action on Sym²/Anti²), the functional/representation algebra, not a linear
  span or a label.
- Lesson (3): Route B1 ran the counterfactual clause — gaugedness is not
  realized-state data, so cannot be laundered as registered data.
- Lesson (4): no new hard wall ⇒ no exercise-skill run requested for this edge.

---

## 5. Load-bearing wall (post-block)

**The single load-bearing wall for P-HY's anomaly role is the "is-gauged"
predicate** on the canonical (already supplied) traceless u(1) direction —
MINIMAL_AXIOMS withholds the gauge group / which-symmetry-is-gauged. This is
strictly narrower than the prior "physical U(1)_Y identification" wall:

- alpha=1/3 — NOT load-bearing for the anomaly test (B2 homogeneity lemma);
  retained_bounded bridge supplies it for the value-match with named P1–P4.
- species naming — NOT load-bearing for the anomaly polynomial (B3); rep content
  is derived label-free.
- → only "is-gauged" remains, and it funnels to the same MINIMAL_AXIOMS
  gauge-group-withholding gate as P-COMP (content) and the P-REC/P-ABJ walls.

---

## 6. Carry to block02 / owner packet

1. **BANK** the B1 arithmetic core as a deps-all-retained bounded theorem (the
   keystone B1 tuple {Tr[Y]=0, Tr[Y³]=−16/9, Tr[SU3²Y]=1/3, Tr[SU3³]=2,
   Tr[SU2²Y]=0}, scale-free), citing graph_first (retained) — Decision A.
2. **NEW LEMMA to register** (Decision H opportunity): "alpha is pure
   convention for the anomaly test" (B2 homogeneity/rescaling-invariance) —
   this REMOVES the alpha admission from the anomaly arithmetic (it remains only
   for the GMN value-match, which is the retained alpha-bridge's named P1–P4).
3. **CORRECTION to adopt:** the stale "alpha still conditional / chain_closes=
   FALSE" framing is wrong on this branch base — the alpha bridge and the
   identification note are both retained_bounded / chain_closes=True. Carry the
   bridge's own "does not eliminate admission, formally exposes P1–P4" caveat.
4. **WALL to ship (held until N1≥5 + N7 per the gate):** P-HY identification
   wall = the "is-gauged" predicate only. Route inventory now: B1 gauged-
   direction (fresh, walled+sharpened), B2 alpha-convention (fresh, partial
   win), B3 L2-label-free (fresh, half met) + the absorbed reprove-full-
   hypercharge (rejected) and add-new-primitive (rejected) = **5 attacked
   routes**, satisfying N1≥5 for this edge; N7 steelman = "a richer Record/
   readout context supplies the gauged predicate" → attacked: Record supplies
   no sector-generation/coupling rule, so the steelman fails.
5. **RE-EXPOSE** P-HY as an explicit premise edge (do NOT inherit the
   dep-reroute "consumed retained-bounded content" laundering).

---

## 7. One line

P-HY: arithmetic core is a deps-all-retained bankable bounded theorem (keystone
B1 traces recomputed in-tree, PASS=41); the identification wall SHRINKS to the
single "is-gauged" predicate — alpha (homogeneity lemma) and species-naming
(label-free rep content) are proven NOT load-bearing for the anomaly test.
