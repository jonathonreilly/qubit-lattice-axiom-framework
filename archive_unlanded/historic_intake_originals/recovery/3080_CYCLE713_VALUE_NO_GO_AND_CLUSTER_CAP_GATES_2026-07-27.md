# Cycle 713 — Value Gate, No-Go Discipline Gate, and Cluster-Cap Evaluation

**Date:** 2026-07-27
**Block:** `poisson-self-bound-source`
**Parent row:** `self_consistency_forces_poisson_note` (`criticality: critical`,
`direct_in_degree: 17`, `transitive_descendants: 783`,
`load_bearing_score: 18.115`)
**Runner:** [`scripts/physical_poisson_self_bound_source_exists_cycle713_2026_07_27.py`](../scripts/physical_poisson_self_bound_source_exists_cycle713_2026_07_27.py)

These answers are a pre-PR self-review record. They are not an audit
certificate and predict no audit verdict.

---

## Part 1 — V1-V5 Promotion Value Gate

### V1 — What specific verdict-identified obstruction does this PR close?

Quoted from the parent row's `verdict_rationale`:

> "the attraction comparison uses the same negative source with operators of
> different sign definiteness, making the Poisson-versus-biharmonic/local/random
> sign discriminator convention-dependent; ... a response-kernel bridge is still
> missing."

and from `notes_for_re_audit_if_any`:

> "normalize alternative-operator source signs consistently, and revise the note
> to the resulting finite numerical scope before re-audit."

Three distinct obstructions, addressed as follows.

1. *Convention-dependent sign discriminator.* Row R0 fixes the source sign per
   operator, once, from the sign of the first iterate, so that every operator
   produces an attractive well. No operator is handed a repulsive self-potential
   and then scored unphysical.
2. *Missing response-kernel bridge.* Row R10 supplies one in the form the
   rationale asks for: the converged self-consistent field is compared, outside
   the source, against the matched point-source kernel of the **same operator
   under the same boundary condition**. Median ratio within ~1% of unity at
   every box. Both sides carry the same wall and the same image, so no boundary
   correction is applied and no exponent is fitted.
3. *Revise to the resulting finite numerical scope.* Rows R3-R14 replace the
   note's convention-dependent comparison with a criterion that has no sign
   convention in it — whether the self-consistent binding energy has a
   box-independent limit — and state the resulting scope explicitly.

The upstream is not merely unratified; these are named derivation gaps.

### V2 — What new derivation does this PR contain, and what repo search establishes that?

The new content is a **two-condition criterion for a self-bound source, and the
demonstration that the second condition is the one that separates the operator
family**. At fixed coupling with the box growing, a source is self-bound when
(1) its extent converges and (2) the depth of the self-consistent well
converges. Condition 2 is load-bearing: a state whose extent stops growing can
still be held by a well that deepens without bound, which is box-squeezing by a
kernel with no decaying far field. Measured across the parent note's own family,
unscreened Poisson and screened Poisson satisfy both, biharmonic satisfies (1)
but not (2), and `local` has no single branch. Rows R6/R7 then isolate the
mechanism from the nonlinear fixed point entirely: with a prescribed source of
fixed extent and no self-consistency, biharmonic's peak potential still grows
linearly with the box on Dirichlet **and** on a boundary-free torus out to
`N = 96`, so the divergence is a property of the kernel.

Prior-art search, recorded in full with hits and classifications in
`.claude/science/physics-loops/poisson-self-bound-source/ROUTE_PORTFOLIO.md`.
Searched commit `9ce38a06db`, refreshed immediately before the sweep. Commands:

```bash
git grep -l -iE "self.?bound|soliton|schr(o|ö)dinger.?newton|choquard" origin/main -- 'docs/*.md'
git grep -l -iE "(self.?consistent.*(ground state|eigen)|nonlinear eigen|hartree)" origin/main -- 'docs/*.md'
git grep -l -i "biharmonic" origin/main -- 'docs/*.md'
git ls-tree -r --name-only origin/main -- docs/ | grep -iE "SOURCE|LOCALIZ|SOLITON|BOUND_STATE"
git grep -l -iE "(box.?independen|lattice.?size.?independen|size.?independent.*(width|extent|radius))" origin/main -- 'docs/*.md'
git grep -l -iE "(asymptotically free|confining potential|kernel (decays|grows)|potential (depth )?(grows|scales) with (the )?box)" origin/main -- 'docs/*.md'
git grep -l -iE "hartree|frozen_star|self_focusing" origin/main -- 'docs/audit/data/ledger/'
```

The one closely matching hit is `docs/FROZEN_STARS_RIGOROUS_NOTE.md` with
`scripts/frontier_frozen_stars_rigorous.py`, which builds a self-consistent
Hartree ground state and measures an RMS width. It is cited, imported, and run,
not reinvented — rows F1/F2 execute that landed runner directly. It cannot
address the question here, because its self-potential is a hand-imposed
`-G sum(rho/r)` Coulomb sum rather than a solve of `Op phi = rho`, so no
operator comparison is possible in it; and it tests condition (1) only. Its own
3D table (`L=6..14`, widths `2.52..5.08`) shows the width still growing at its
largest box, and its "What is needed next" section concedes the 3D width is not
converged. No hit anywhere states, for any operator, whether the self-consistent
extent or the self-consistent binding energy is box-independent. Target state:
**open after the matched-hit review**.

### V3 — Could the audit lane already complete this from retained primitives plus standard machinery?

**No.** One ingredient is standard: that a `1/r` kernel gives a bounded
potential from a bounded source while a kernel growing like `r` does not is
elementary. What is not available from standard machinery is the rest:

- that the *self-consistent* problem — a nonlinear eigenproblem with no closed
  form — has a fixed point at all on the parent's finite Dirichlet lattice, on
  which branch, and over what coupling range (row R13 locates the extended
  branch and the collapse that ends it);
- that the width-only criterion is insufficient. This is not a hypothetical
  concern. It is the criterion a landed repo note used, and rows F1/F2 measure
  that its 3D result is within 87-95% of the free box ground state at its own
  parameters, so its reported lattice-size independence is not established by
  its own construction;
- the quantitative separation itself, which is a measurement.

### V4 — Is the marginal content non-trivial?

**Yes.** The claim that survives is not "1/r decays and r does not". It is that
across the parent note's family the discriminating quantity is the binding
energy rather than any fitted decay exponent — after PR #5656 showed the note's
sign discriminator is empty and PR #5693 showed its exponent discriminator is
inverted, this is the third candidate discriminator and the first that does not
collapse under its own controls. Row R14 further narrows it: the biharmonic
potential *difference* across a fixed window is bounded, so the failure is
specifically of the binding energy and not of local forces.

### V5 — Is this a one-step variant of an already-landed cycle, or of anything on `origin/main`?

**No.** Refreshed `origin/main` at `9ce38a06db`.

| Prior | What it did | Structural distinction |
|---|---|---|
| PR #5656 (cycle 710) | The note's two operator discriminators are empty | Negative; no self-consistent state is constructed |
| PR #5662 (cycle 711) | The `beta` diagnostic has no far field to extrapolate | Negative; diagnoses the source's scale-locking without repairing it |
| PR #5693 (cycle 712) | Repaired protocol on a **prescribed** external source | The source there is imposed by hand and is not self-consistent, so it cannot answer the parent note's question. Here the source is a fixed point of the field it generates. |
| `FROZEN_STARS_RIGOROUS_NOTE` (landed 2026-04-12) | Self-consistent Hartree width, one hand-imposed kernel | No operator family, no binding-energy test, width-only criterion, and its 3D claim is measured here rather than assumed |

The construction differs (eigenproblem vs propagator), the criterion differs
(binding energy vs fitted exponent), and the direction differs (this is the
first positive selection result in the family).

**V1-V5: PASS.**

---

## Part 2 — N1-N8 No-Go Discipline Gate

Negative claims made in this block:

- **NG-A** biharmonic admits no box-independent binding energy on this surface;
- **NG-B** `local` has no single self-consistent branch from a zero start;
- **NG-C** the landed frozen-stars 3D lattice-size-independence is not
  established by its own construction at its own parameters.

### N1 — Alternative route enumeration against NG-A

| # | Route | Marker | Outcome |
|---|---|---|---|
| 1 | Different coupling — maybe `g = 10` is special | **ATTEMPTED** | `g = 10` and `g = 100` both give linear depth growth. The `g = 100` runs fail to converge at `N >= 20`, so the scored row uses `g = 10`, where every box converges. |
| 2 | Different boundary condition — maybe the Dirichlet wall creates it | **ATTEMPTED** | Row R7: boundary-free torus, zero mode removed, growth persists to `N = 96`. |
| 3 | Remove self-consistency — maybe it is an artifact of the nonlinear fixed point | **ATTEMPTED** | Row R6: prescribed source of fixed extent, same linear growth. |
| 4 | Different source extent | **ATTEMPTED** | The prescribed Gaussian (width 1.0) and the self-consistent state (rms ~2.7) both show it. |
| 5 | Sign convention — maybe biharmonic is being penalized by the parent runner's defect | **ATTEMPTED** | Row R0: biharmonic is given an attractive well by construction. |
| 6 | Rescale the operator — `Delta^2 / c` for some constant `c` | **RULED OUT BY ARGUMENT** | A positive rescaling is absorbed into `g`; it maps the linear family to itself and cannot make an unbounded sequence bounded. |
| 7 | Reference the potential to a fixed radius rather than the well bottom | **ATTEMPTED, AND IT SUCCEEDS** | Row R14. The difference across the fixed window IS bounded for biharmonic. NG-A is therefore narrowed to the binding energy and makes no claim about local field differences. |
| 8 | Larger boxes might reveal saturation | **ATTEMPTED** | The torus row reaches `N = 96` with increments still constant. |

Eight routes, seven attempted. Route 7 succeeded and the claim was narrowed
rather than defended.

### N2 — Wall independence

| Wall | Follows from another? |
|---|---|
| W1 four-member family, not all local operators | No |
| W2 single particle, no Pauli pressure | No |
| W3 finite box sizes; the limit is a fit, not a proof | No |
| W4 the extended branch exists only below the collapse coupling | Partly scope, not a wall: W4 bounds where the rows are taken, and every box-independence row is taken inside it (row R13) |

W1-W3 are independent. W4 is recorded as scope.

### N3 — Hidden-wall scan

Scanned the note and runner for `we assume`, `by construction`, `naturally`,
`standard`, `registered`, `canonical`, `bridge context`.

- "by construction" appears in R0's description of the sign normalization. This
  is a **cited, explicit condition**, stated in the runner docstring, the
  imports ledger, and the note — not hidden.
- "the source sign is fixed once, from the first iterate" is a real condition:
  a different rule could in principle select a different branch. Promoted to an
  explicit scope line in the note.
- No other hit is load-bearing.

One condition promoted; none left implicit.

### N4 — Residual matching

| Cited witness | Its residual | Matches? |
|---|---|---|
| PR #5693 row U9 | "the self-consistent construction cannot supply a localized source" — measured **for the propagator density only**, both branches | **Yes**, and this cycle takes the escape U9 itself names |
| PR #5662 | fit window inside the source, enclosed fraction rising | **Yes** — condition (1) is the direct repair |
| PR #5656 R16 | "the `beta` comparison establishes no operator as best" | **Yes** — leaves operator selection open, which is what admits a positive result here |
| `MATTER_SELF_FOCUSING_NOTE` | self-focusing on the **propagator density** fails to restore equivalence | **Yes** as prior-art evidence for leaving that source; **not** cited as a wall against self-consistency |

No citation dropped.

### N5 — Rhetoric audit

The phrase "biharmonic has no box-independent binding energy" is checked at:
per-coupling (`g = 10`, `g = 100`), per-geometry (Dirichlet, torus),
per-construction (self-consistent fixed point, prescribed source), and
per-reference (well bottom vs fixed radius — where it does **not** hold, R14).
It is **not** checked at: other lattices, other dimensions, other source
profiles beyond the two run, or multi-particle sources. The note states the
claim at exactly the tested resolutions and no wider.

### N6 — Partial-closure path scan

Is there a convention or definition refactor that closes the wall without a new
axiom? Two were found and both are recorded:

- *Reference the potential to a fixed radius.* Found by N8's echo check, run as
  R14, and it **does** rescue biharmonic's local field differences. The claim was
  narrowed to the binding energy rather than asserting "new axiom required".
- *Make the operator box-dependent (normalize by `N`).* This leaves the class of
  local operators the parent note's family is drawn from, so it is out of scope
  rather than a closure path; recorded as such, not as an axiom demand.

Nothing here calls for a new axiom or a new primitive, and the note does not say
one is required.

### N7 — Steelman

> The criterion is rigged. Demanding that the binding energy have a
> box-independent limit is demanding that the kernel be asymptotically free,
> which is a Newtonian property. Of course the Newtonian operator wins a test
> built from a Newtonian premise. A biharmonic "gravity" is confining, and for a
> confining theory a binding energy set by the size of the universe is the
> expected behaviour, not a defect. Worse, row R14 concedes that biharmonic's
> local field differences are perfectly box-independent — so the only thing that
> fails is a global quantity the test elevated by choice.

**This steelman largely lands, and the block is demoted in response.** The
criterion does encode a substantive requirement — that an isolated object have a
binding energy that is a property of the object rather than of the box — and
that requirement is a stated condition, not a neutral measurement. The result is
therefore recorded as a **bounded theorem conditional on that named condition**,
not as an unconditional no-go against biharmonic, and the note says in its own
thesis row that under a different choice biharmonic is not excluded. What
survives the steelman is narrower and still non-trivial: *given* the isolation
condition, the parent note's family separates, and it separates on a quantity
with no sign convention in it — unlike the discriminator the ledger row calls
convention-dependent.

### N8 — Cross-cycle echo

Structurally similar prior wall: cycle 712's "the diagnostic has no far field",
retired by fixing the measurement window in absolute units instead of box units.
Applying the analogous move here — fix the *reference radius* instead of using
the well bottom — is what produced row R14 and the narrowing above. The
mechanism that retired the earlier wall was considered and applied, not skipped.

**N1-N8: PASS, with the claim demoted at N7 from an unconditional no-go to a
bounded theorem under a named isolation condition, and narrowed at N1/N6/N8 from
the field to the binding energy.**

---

## Part 3 — Cluster-Cap Evaluation

This is the **4th** PR in the `self_consistency_forces_poisson_note` family
(#5656, #5662, #5693, this one), so the cluster-cap evaluator triggers. The
active tool policy forbids spawning a separate evaluator agent, so per the
skill's own conditional — "otherwise the loop agent applies the same evaluator
brief locally" — it was run locally against the deliverable note and the paired
runner output.

**1. New load-bearing premise.** Yes. The two-condition self-binding criterion,
with the binding energy as the load-bearing half, appears in none of the prior
three. #5656 is about sign conventions and kernel correlation, #5662 about
extrapolation of a fitted exponent, #5693 about a fixed window on a prescribed
source. None constructs a self-consistent state or measures a binding energy.

**2. Distinct claim type.** Yes, and this is the sharpest distinction. #5656 and
#5662 are demotions. #5693 is a bounded theorem plus a no-go, both about a
prescribed source. This is the first **positive** result on the self-consistent
problem the parent note is actually about, and the first to answer a successor
the cluster itself named.

**3. Independent reviewability.** Yes. The runner is self-contained, imports two
committed parent modules and verifies both blobs, and every row is computed. A
reviewer who has read none of the prior three can check R0-R14 on their own
terms. Its dependence on the cluster is one citation in the thesis row.

**4. Marginal review value.** High relative to cost. The cluster's first three
PRs left the parent row's headline claim unsupported but not refuted, with an
explicit open successor. Folding this into a combined PR is not available —
the prior three are already open, and this result partly reverses the arc's
direction, which a reviewer should see as its own artifact rather than as an
amendment. It also surfaces an independent finding against a second landed note
(F1/F2), which a combined PR would bury.

**VERDICT: `OPEN`.**

The counter-consideration is real and is recorded: four open PRs against one
parent row is a heavy review load, and if the audit lane wants them batched, the
branch is self-contained and can be restacked. That is a reviewer's call, not a
reason to withhold the artifact.
