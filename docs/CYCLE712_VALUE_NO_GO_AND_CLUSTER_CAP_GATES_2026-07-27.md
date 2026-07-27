# Cycle 712 — V1–V5, N1–N8, and the Cluster-Cap Evaluation

Block: `physics-loop/poisson-far-field-protocol-repair-20260727`
Deliverable: `docs/POISSON_OPERATOR_PREFERENCE_IS_CORRECT_AND_ITS_OWN_DIAGNOSTIC_IS_INVERTED_REPAIR_NOTE_2026-07-27.md`
Runner: `scripts/physical_poisson_far_field_protocol_repair_cycle712_2026_07_27.py` (10 PASS / 0 FAIL)

This is the **3rd PR** in the `self_consistency_forces_poisson_note` parent-row
family this campaign, after #5656 and #5662. **The judgment-based cluster-cap
evaluator therefore triggers and is run below, before the PR is opened.**

## Cluster-cap evaluation (mandatory at N ≥ 3)

Run locally under the skill's own conditional — the active tool policy does not
permit a separate evaluator agent, and the skill directs the loop agent to apply
the same brief locally in that case. All inputs the brief requires are available:
the deliverable note, the paired runner output (10 PASS / 0 FAIL), and both prior
cluster PRs. So the fail-closed default does not apply.

**Criterion 1 — new load-bearing premise not present in the prior 2 PRs?**
Yes, four of them:
- **U2**: a window whose radii scale with the box converges to a *wrong* value on
  a boundary-free lattice (`beta ≈ 1.66`, `4πrG ≈ 0.65`, stable to `<0.02` across
  three sizes). Neither prior PR contains a protocol result.
- **U4**: under the parent note's own window on its own Dirichlet operators, the
  biharmonic rival scores `beta = 1.005` while Poisson scores `1.796` — the
  ranking is *inverted* relative to the true far field. This is a new structural
  finding and it explains the central anomaly of both prior PRs.
- **U5–U7**: the rival far-field exponents (biharmonic → 0, `1/r^2` → exactly 2,
  screened monotone `1.68 → 9.74`). The prior-art sweep found these nowhere in the
  repo; only the parent note mentions biharmonic at all.
- **U9**: the un-normalized propagator branch diverges (total mass `4.19e6 →
  1.38e20`). #5662 measured only the normalized branch.

**Criterion 2 — distinct claim type, or another instance of the same kind?**
Distinct. **This is the first positive artifact in the cluster.** #5656 and #5662
are both demotion packets; this is a `bounded_theorem` that *recovers* the parent
note's Bounded Claim 1 conclusion on a different diagnostic. It reverses the
direction of the arc rather than extending it.

**Criterion 3 — independently reviewable on its own merits?**
Yes. The runner imports the parent construction directly and verifies in U0 that
its Fourier symbol is the symbol of the parent runner's own stencil, so it does
not inherit trust from the prior PRs. It cites #5656 R1/R13/R16 and #5662 S5 for
context but re-derives nothing from them and does not depend on their files. Based
on `main`, not stacked.

**Criterion 4 — marginal review value against per-PR review effort?**
High, and higher than either predecessor. After #5656 and #5662 a reviewer would
reasonably conclude the parent row should be demoted wholesale. This cycle shows
the conclusion is *correct* and specifies exactly which evidence to substitute for
it, which materially changes what the audit lane should do with a `critical` root
row carrying 727 descendants. It also **audits its own predecessor**: U5 confirms
#5656's R16 was right to refuse naming a rival as better, and had R16 taken the
stronger reading this cycle would have refuted it. That check has value precisely
because it is a separate artifact rather than self-certification inside #5656.

**Anti-pattern check.** Not "apply theorem X to label Y"; not "same matrix
structure, different interpretation"; not a sympy re-verification of an existing
runner; not a narrow rescope of an algebraic core. The computation, the protocol,
and the lattice sizes are all new.

**Approve-pattern check.** Matches two of the skill's listed approve patterns
directly: "a no-go theorem that retires a route the prior PRs assumed" — it
retires the assumption, shared by both prior PRs, that the parent `beta`
diagnostic can rank operators at all; and "a numerical artifact (NEW computation)
under a different action / geometry / coupling" — periodic geometry, fixed window,
sizes to N=192.

### `VERDICT: OPEN`

The burden at N ≥ 3 is on the proposed PR to demonstrate non-churn content. It
does: a new protocol result, an inversion finding that reinterprets both
predecessors, the first positive claim in the cluster, and rival measurements the
repo does not have. Backlogging it would leave the parent row demoted on evidence
this cycle shows is the wrong diagnostic.

## V1–V5 Promotion Value Gate

**V1 — specific verdict-identified obstruction closed?** The parent row's
`notes_for_re_audit_if_any`, quoted verbatim in the note, asks for the operator
comparison to be put on a correct footing and the note revised "to the resulting
finite numerical scope". #5662's handoff named this measurement as the successor.
This is a derivation-gap obstruction on the parent row itself. **PASS.**

**V2 — new derivation not already in the audit lane?** Yes: U2, U4, U5–U7, U9 as
enumerated under cluster criterion 1. Explicitly **not** new: Poisson's own
`1/(4 pi r)` asymptotic, which is landed repo content
(`LATTICE_GREENS_1_OVER_R_...`, `GRAVITY_LEADING_LATTICE_CORRECTION_...`). U1 is
labelled a control in the runner, in the note, and in its ledger row. **PASS.**

**V3 — could the audit lane already complete this from retained primitives plus
standard machinery?** No. The Fourier diagonalization is standard and is not the
new part; the new part is measuring the parent note's operator family on a
far-field protocol and discovering that the parent diagnostic orders them
backwards. That is an output of this specific construction and diagnostic, not of
general machinery. No framework axiom or primitive is load-bearing. **PASS.**

**V4 — marginal content non-trivial?** Yes. The strongest item is U4: the parent
diagnostic assigns `beta = 1.005` to the operator whose potential is
asymptotically constant. A diagnostic that is *inverted* rather than noisy is a
qualitatively different finding from "the numbers are unreliable", and it retro-
actively explains both prior cycles. **PASS.**

**V5 — one-step variant of an already-landed campaign cycle?** No. Closest are
#5656 and #5662 on the same row. Structural distinctions: different diagnostic
(far-field fixed window vs self-consistent scaling window), different geometry
(periodic for the separation rows), opposite sign of result (positive vs
demotion), and it functions as a check on #5656 R16 rather than an application of
it. **PASS.**

**Gate result: PASS on all five.**

## N1–N8 No-Go Discipline Gate

Applies to the negative half: the parent diagnostic is inverted (U4); the
biharmonic far field is flat (U5); a scaling window cannot be rescued by larger
lattices (U2); the self-consistent construction cannot supply a localized source
(U9).

**N1 — Alternative route enumeration.**

| # | Route | What it would attempt | Outcome |
|---|---|---|---|
| 1 | Boundary condition | The separation is a periodic-lattice artifact; Dirichlet would differ | **PARTIALLY ATTEMPTED, and declared.** U4 is Dirichlet and shows the inversion there. The far-field separation is periodic, declared in the status block, the thesis hypotheses, and the objection section. The Dirichlet fixed-window series I measured (`2.633, 1.695, 1.466` at N=24/32/40) descends in the same direction but converges too slowly at reachable sizes — that is a limitation of the measurement, stated as such. |
| 2 | Window choice | Radii 4..10 is arbitrary; another fixed window gives another answer | **ATTEMPTED (U2 vs U1, and the P3 exploration).** Two fixed sub-windows (4..8 and 8..16) on the biharmonic Green's function both drift toward 0 with N, and the scaling window is what produces a stable wrong value. The result is a property of fixed-vs-scaling, not of the specific endpoints. |
| 3 | Zero-mode handling | Removing the `k=0` mode on the torus biases the profile | **ATTEMPTED implicitly by U1.** If zero-mode removal biased the fixed-window profile, Poisson would not converge to the landed `4πrG → 1`. It does, which is exactly what makes U1 a usable control. |
| 4 | Stencil mismatch | The Fourier symbol is not the parent operator's | **ATTEMPTED (U0).** The parent Laplacian is verified to be a `-6` diagonal with unit nearest-neighbour couplings, whose symbol is the one used. |
| 5 | Source shape | A point source is not the parent note's spread source | **ATTEMPTED, and it is the point.** #5662 established the parent source is scale-locked and the fit window sits inside it. A point source is the fixed-extent source the successor called for. U9 then shows the parent loop cannot produce one. |
| 6 | Fit estimator | The log-log slope is the wrong estimator | **RULED OUT BY PRIOR.** The estimator is the parent note's own (`check_field_physics`), used deliberately so the comparison is apples-to-apples; #5662 S4 already recorded that its fit quality degrades on the parent construction. Here the fixed-window `R^2` reaches `0.99997`, so the estimator is not the limitation. |
| 7 | Larger `mu^2` or other operator families | The screened sweep or family is too narrow | **NOT ATTEMPTED beyond the parent note's six `mu^2` values and four operators — declared.** The note states explicitly that this is not a uniqueness theorem over all local operators and that the parent note's own finite-family caveat remains correct. |

**N2 — Wall-independence audit.** Walls: (a) scaling windows converge to wrong
values; (b) the parent diagnostic inverts the ranking; (c) biharmonic's field is
flat; (d) the loop cannot supply a localized source. (a) and (b) are **not
independent** — (b) is (a) instantiated on the parent's window plus (c); the note
presents them in that order and says so. (c) and (d) are independent of each other
and of (a)/(b). No wall is presented as independent where it follows from another.

**N3 — Hidden-wall scan.** Grepped for "we assume", "by construction",
"naturally", "standard", "registered", "canonical". Hits: "by construction" in U6
(the `1/r^2` kernel returning its own defining exponent — that is the point, and
the row says so) and in U9's description of the box-filling source (the finding).
Conditions promoted to explicit `[supplied]` tags: periodic boundaries, the fixed
window endpoints, the point source, the tested family being the parent note's
rather than all operators, the `mu^2` grid, and the landed asymptotic's status as
control rather than result.

**N4 — Residual matching.** Witnesses: the parent note's Bounded Claim 1 and
Caveat 1 (quoted verbatim); the two landed Green's-function notes (cited for the
control target, matching exactly); #5656 R1, R13, R16 and #5662 S5 (each used for
a specific prior result, each matching). Nothing dropped.

**N5 — Rhetoric audit.** Checked at the resolutions tested:
- "the diagnostic is inverted" — verified per-size at five Dirichlet sizes; the
  ledger row scopes it to those sizes and to the parent window.
- "biharmonic's far field is flat" — verified at six periodic sizes with `beta·N`
  roughly constant; the row does not claim a closed form.
- "uniquely gives the Newtonian exponent" — narrowed in U8's row to the parent
  note's tested family, and the note repeats the parent's own finite-family caveat
  rather than removing it.
- "cannot be obtained self-consistently" — verified at five sizes for both
  branches; the row does not claim no propagator modification could localize it.

**N6 — Partial-closure path scan.** This cycle *is* the partial-closure path: it
repairs the parent note's claim by substituting the diagnostic rather than
retiring the physics, and the proposed revision keeps Bounded Claim 1's conclusion
while replacing its evidence. No "new axiom required" language appears; no axiom
or primitive is involved.

**N7 — Steelman.** Written in full in the note. *"You measured the rivals
periodically and the parent note is Dirichlet, so your headline separation is not
about the parent construction."* Correct, and it is why the claim is split: U4 is
Dirichlet and refutes the evidence on its own; U1/U5–U8 are periodic and supply
the far fields. A reader who rejects the periodic rows keeps the refutation and
loses only the recovery. **Not demoted for N7**, and the steelman is carried into
the deliverable along with the honest statement that Dirichlet convergence is too
slow at reachable sizes.

**N8 — Cross-cycle echo.** Structurally similar prior wall: #5656 R16, where a
ranking that looked decisive was shown to sit inside an error budget, and the
claim was weakened. Same pattern completed here — the ranking was not merely
uncertain, it was backwards. In both cases the resolution came from measuring the
diagnostic rather than trusting it. No structurally similar wall was found that
has since been retired by a mechanism not considered here.

**Gate result: no failure condition hit. Route 1 (Dirichlet far field) is declared
as measured-but-not-converged; route 7 (wider operator families) is declared
unattempted and the parent note's finite-family caveat is explicitly preserved.**

## Open routes this cycle does not close

1. **Dirichlet far field at converged sizes.** The fixed-window Dirichlet series
   descends correctly but needs lattices well beyond N=48 to converge, because the
   boundary must recede far past the window. Not run.
2. **Operator families beyond the parent note's four plus the screened sweep.** The
   finite-family caveat stands.
3. **The successor, which is no longer on this row.** U9 shows the self-consistent
   construction cannot supply a localized source: with the per-layer normalization
   the source is scale-locked, without it the amplitude diverges by 14 orders of
   magnitude. Any future self-consistency claim in this lane needs a source term
   that is not the normalized propagator density. That is the next target, and it
   belongs to the self-consistency framing rather than to the operator question.
