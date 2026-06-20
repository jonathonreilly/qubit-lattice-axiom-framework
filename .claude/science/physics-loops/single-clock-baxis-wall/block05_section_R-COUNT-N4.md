# Block05 §R-COUNT-N4 — the count `d_t ≤ 1` is label-free; N4-as-label is over-specified for the consumer

**Route:** R-COUNT-N4 (clause N4, over-specification test)
**Branch:** `physics-loop/single-clock-baxis-wall-block05-20260620`
**Runner:** `scripts/single_clock_count_label_free_n4_2026_06_20.py`
**Cache:** `logs/runner-cache/single_clock_count_label_free_n4_2026_06_20.txt`
**Result:** `TOTAL: PASS=16 FAIL=0`
**Outcome:** `corrects_overclaim` (shrinks the N4 wall for the 959 cone; does NOT close N4 from A_min, does NOT touch N2b/N5).

---

## 1. What was tested

The keystone's **only** consumer is `docs/ANOMALY_FORCES_TIME_THEOREM.md`
(premise row SC, downstream fanout 959). Verified verbatim (runner `[VERB]`,
recomputed in-tree, not inherited):

- Non-circularity §2, item 2: *"The anomaly argument here never selects a
  direction. Steps 1-3 below constrain only the \*count\* `d_t` (parity and
  positivity), **not which axis is temporal**."* (lines 140–142)
- Upper bound / proof Step 4: *"given B-AXIS, there is one admitted clock
  factor, so `d_t <= 1`."* (lines 239, 245)
- The conclusion is the **signature `(3,1)`** — a pure count (3 space + 1
  time), never a label of which lattice axis is time.

So the consumer reads exactly one thing from B-AXIS for its upper bound: the
codim-1 **COUNT** cap `d_t ≤ 1`. The axis **LABEL** ("which of the 4 Euclidean
directions is time", = B-AXIS.2 = N4) is *carried* in the premise stack but is
never read by the argument or the conclusion.

The route tests whether that count is **label-free** (S₄-invariant): conjugate
the whole codim-1 RP/transfer construction by every `g ∈ G_bare` (the signed
hyperoctahedral group B₄, 384 elements) and count inequivalent constructions
modulo S₄.

## 2. Method (finite-dim exact linear algebra; deterministic; same retained surface)

Built on the **same** retained even cubic-symmetric staggered-Dirac surface as
the campaign's R-N4-AUT runner (R-RP2/R-SC2/R-CL3 object), reusing its
`build_staggered` and `G_bare` (solved-sign-field B₄) construction.

- `[SURF]` Recompute the standing N4 LABEL wall: `|G_bare| = 384`, axis image =
  all of S₄ acting **transitively** (orbit of axis 0 = {0,1,2,3}). The axis
  label is not derivable, only declarable. (3 PASS.)
- `[COUNT-INV]` G_bare is **equivariant** on the per-axis hop sectors: every
  `g` maps the axis-`a` construction `D_a` exactly onto `±D_{π(a)}` (all 384×4
  checked, resid 0). The four per-axis hop sectors are unitarily equivalent
  (identical spectra, max diff 1.3e-14). Hence every axis-invariant count
  functional — including the admitted-clock-factor count — is axis-uniform.
- `[ORBIT]` The four per-axis codim-1 constructions form **exactly one**
  inequivalence class modulo S₄ (one orbit; class reps = [0]); every axis lies
  in that single orbit. So `d_t ≤ 1` is a single-S₄-orbit, label-free statement.
- `[CAP]` The cap value (one admitted clock factor → `d_t ≤ 1`) is identical for
  every axis label.
- `[SEP]` The precise over-specification statement: BEFORE the quotient the
  axis-0 and axis-1 constructions are **distinct** operators (`‖D_0−D_1‖=16`,
  `‖D_0+D_1‖=16`) — so N4-as-a-label is genuine, non-vacuous data; AFTER the
  quotient the signed exchange `W_{0,1}∈G_bare` carries one exactly onto the
  other (resid 0). **Label ≠ count.** The label is real data the count
  quotients away; the consumer reads only the count.
- `[SCOPE]` Even-extent guard (odd-L falsifier, `‖W M Wᵀ−M‖=6.0`) inherited from
  the no_go. **Honesty/sharper leg:** on the ODD block the per-axis hop spectra
  are *still* axis-uniform (max diff 5.2e-15), so the COUNT cap is axis-uniform
  even where the exact signed-exchange LABEL transport `W` fails. The count the
  consumer reads is robust beyond the even-extent W-transport scope to which the
  no_go's LABEL wall is bounded.

## 3. Outcome — corrects an over-claim in the block02 framing

Block02's unified no_go (`SINGLE_CLOCK_BAXIS_OBSTRUCTION_UNIFIED_NO_GO_NOTE_2026-06-20.md`)
correctly establishes that the axis **label** (N4) is **not derivable** from
A_min (S₄-transitive transport). That negative-derivation result is **not
disturbed** by this route.

What the block02 framing **over-claims** is the *consumer relevance* of N4. Its
§2 table lists N4 as an "open (declared premise)" load-bearing wall, and its §9
consumer firewall demotes every downstream consumer to consume B-AXIS — N2/N4/N5
— as **one opaque premise** (the firewall coverage runner
`single_clock_baxis_consumer_firewall_coverage_2026_06_20.py` checks only that
each consumer carries a single B-AXIS marker; it does not split count from
label). For the **only** consumer of the 959-fanout keystone
(ANOMALY_FORCES_TIME), the load-bearing content of N4 is the **count** (one
admitted clock factor), which:
1. is **already supplied** (one declared construction), and
2. is **S₄-invariant / label-free** (this runner: one orbit, [ORBIT]),

while the **label** portion of N4 is **over-specified** — it supplies
information the consumer's count cap never reads. The block02 N4 §5.3 item 4
already names the "count-not-label firewall," but only as a reason the *anomaly*
cannot **supply** the label; this route makes the dual, stronger statement that
the consumer does not **need** the label.

### Precise corrected scope (what should replace the block02 wording)

> N4 splits into a **count** part and a **label** part. The count part ("one
> admitted clock factor", which gives `d_t ≤ 1`) is the only N4 content the
> 959-fanout consumer (ANOMALY_FORCES_TIME) reads; it is supplied and is an
> S₄-invariant (label-free) statement (one inequivalent codim-1 construction
> modulo S₄). The **label** part ("which of the four Euclidean axes is time") is
> non-derivable from A_min (S₄-transitive — the genuine wall), but is
> **over-specified for this consumer**: no step of the consumer, nor its
> `(3,1)`-signature conclusion, reads the label. For the 959 cone, N4 functions
> as a *count* premise, not a *label* premise; the "A_min cannot derive the axis
> label" obstruction does not block this cone.

## 4. Honest limits (what this route does NOT do)

- It does **not** close N4 from A_min. The label remains non-derivable; the
  S₄-transitivity wall stands (recomputed here, [SURF]).
- It does **not** touch N2b or N5. **N5 is the count cap itself** (≤1 commuting
  clock factor → `d_t ≤ 1`); it remains a genuine, undischarged wall (the
  consumer's count cap is exactly the thing N5 must supply). **N2b** (the
  absolute unit) is untouched. Only the over-specified **label** portion of N4
  dissolves for the count-only consumer.
- The dissolution is **consumer-relative**. If any downstream note in the cone
  read the axis label for a *directional* claim, N4-as-label would be
  load-bearing there. None in this cone does (the conclusion is a pure count /
  signature). This is a scope correction, not a framework-wide closure.

## 5. Boundary flags

`B_AXIS_DERIVED = FALSE`; `N4_LABEL_DERIVED = FALSE`;
`N4_LABEL_OVERSPECIFIED_FOR_959_CONSUMER = TRUE`;
`N4_COUNT_SUPPLIED_AND_S4_INVARIANT = TRUE`; `N5_STILL_OPEN = TRUE`;
`N2B_STILL_OPEN = TRUE`; `NEW_AXIOM_ADDED = FALSE`; `AUDIT_VERDICT_APPLIED = FALSE`.
No new axiom or primitive. Independent audit lane is the sole status authority.
```
TOTAL: PASS=16 FAIL=0
```
