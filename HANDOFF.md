# HANDOFF — toe-retention-source-action-20260725

Campaign 2026-07-25, 14:09 onward, physics-loop campaign mode.

## Landed

| commit | content |
|---|---|
| `a89337f0bd` | `PROPER_CUBIC_FINITE_SUPPORT_LINEAR_KERNEL_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-07-25` — invariant kernels on a rotation-closed support set are the functions constant on proper-octahedral orbits; dimension = orbit count; at range 1, `span{I, Δ}`, with the Laplacian line as the constant-annihilating sublocus. Salvaged from a rejected block. |
| `a17b5e74a8` | Cycles 698 and 699. Strict Record additivity kills every two-body coefficient; the minimal position-carrying extension is one constant at range 1; the field is the marginal readout cost of a test record; carrying qubit content gives `96 → 6 → 5` couplings with an exhibited basis (isotropic, bond-axis, chiral). |

Also landed via review seats this session, from other authors' branches:
`#5605` (cl3_pauli N1 certificate), `#5597` (direction-set covariance), `#5611`
(the prior-art sweep, now part of the physics-loop skill), `#5598` (cycle 696).

## Corrections to my own earlier statements in this campaign

Recorded because both entered planning surfaces before being checked.

1. **"The gravity panel and the AC R-eta obligation name the same missing
   object."** Checked and false on the readout side: gravity needs a
   position-dependent readout, AC R-eta an intensive one, and cycle 699's
   landed L4 shows neither repair supplies the other. They share only the
   source-action object.
2. **"Both AC routes terminate at the same object, a selected reference."**
   False. `|b|/a_act` is a coupling magnitude over an activation probability —
   the occurrence and probability surfaces — not a readout reference. No
   readout convention reaches it.
3. **"The normalization residuals are provably independent."** Also false, or
   at least unproven. Symbol-disjointness in separately transcribed equations
   is true by construction. Withdrawn.

## The corrected picture of the normalization residuals

This is the useful residue of the reference-pricing attempt. It is a reading of
landed sources, not a proved claim, and points 3 and 4 were each got wrong once
before being fixed.

1. **Two distinct objects are written `w`.** The C2 note's `w` weights a
   two-cell **readout**: `I_w(x_A,x_B) = x_A + w·x_B`. The Koide flow note's
   `w` is a **formation** weight. The bijection `kappa = 2w/(1-w)`,
   `r = (1-w)/(2w)` belongs to the **formation** weight under that note's named
   conditional identifications — *not* to the readout weighting. Any argument
   that slides between them is wrong; I made that slide twice.
2. **`kappa_EW` and `w` are conditionally linked in landed work.** The C2 note
   records verbatim: *"if the `kappa_EW` wall is restricted to this two-cell
   rational content-determined C2 class, then the missing
   'weighting/readout-bridge rule' is exactly the missing choice of the single
   parameter `w` or a rule that fixes it."* This is a link to build on, not a
   gap.
3. **`a_act` sits on a different surface.** It is an activation probability,
   with `|b|` slaved to it by the AC target at `delta = 2/9`. No search found a
   landed note linking it to any weighting parameter — but note that my
   searching in this campaign was demonstrably imperfect, so treat that as
   "not found" rather than "not there".
4. **`alpha` is a unit choice on the gauge algebra.** Tracelessness fixes the
   ratio `+1 : -3` exactly and leaves the whole line free; only the convention
   that the trivial block reads unit charge selects `1/3`.

**Planning consequence.** There is no landed basis for one convention
discharging all of these. The `kappa_EW`–`w` conditional correspondence is the
one real linkage found, and it is the natural place to push: closing it would
connect the electroweak weighting to the readout class, which is more than any
of the other pairs currently offer.

## The dimensionless debt ledger (was: the priced decision surface)

**Owner standard, stated 2026-07-25:** Planck is the single CORE unit import —
one dimensionful anchor — and every other value should be *built off it*. So the
framework's target is **one dimensionful import and zero dimensionless imports**,
which is also what the scale primitive's "zero dimensionless content" clause
says when read as an aspiration rather than a limitation.

Under that standard the entries below are **derivation debt, not prices**. A
convention is not payment. An earlier version of this section framed them as
conventions to purchase; that frame is withdrawn.

Verified by per-source reading, at `origin/main` `a17b5e74a8`.

| residual | what discharging it costs | notes |
|---|---|---|
| `alpha` (hypercharge) | **a dimensionless normalization choice** — one owner decision | Cheapest of the four, but **not paid by taking Planck**. Tracelessness already fixes the ratio `+1 : -3` exactly, so only one number is at stake; the choice that the trivial block reads unit charge gives `1/3`. An earlier version of this table called this "a unit convention", which was wrong and misleading: `alpha` is a pure number, while the scale primitive supplies a *dimensionful* ruler and declares zero dimensionless content. Two different senses of "unit". |
| `w_formation` (Koide) | **a counting convention** — one owner decision | Consequences already computed in landed work: `w = 1/2` gives `r = 1/2, kappa = 2`; `w = 1/3` gives `r = 1`. |
| `kappa_EW` (electroweak) | **conditional**: a carrier/readout-context identification first, then it collapses to a counting convention | Gated by the **EW instance premise**. `CANONICAL_TWO_CELL_CONTEXT_C3_EW_INSTANCE_BOUNDED_NOTE_2026-07-02.md` states the EW identification is "a named instance premise with witnesses" and that "cardinality `8/9` is consistent with the `M_3` unit/traceless split, but **cardinality alone does not supply the Hilbert-Schmidt cell structure**." If that premise is discharged, the C2 conditional correspondence makes `kappa_EW`'s missing rule exactly a choice of `w` on that class. |
| `a_act` (AC occurrence) | **a formation or rate law** — not a convention at all | Largest commitment, and the one the axioms most explicitly withhold: every formation rule is downstream content. `|b|` is slaved to it by the AC target at `delta = 2/9`. |

### What covariance already bought

Recast as debt reduction, today's landed work did real work:

| object | before | after covariance | remaining debt |
|---|---|---|---|
| the field law | an arbitrary linear operator | `A·I + B·Delta`, with `B` factoring out | **1 number**, `A/B` |
| the source action at range 1 | an arbitrary two-body kernel | classified by octahedral orbits | **5 numbers**, with an exhibited basis |

Covariance took the law from infinite-dimensional to a single number. It cannot
take 1 to 0, and neither can source-restriction by the neighbour rule — tested
and ruled out above.

### What pins `A/B`: four mechanisms checked, all negative

The law's remaining debt is one dimensionless number. Four candidate mechanisms
have now been checked. None supplies it.

| mechanism | verdict | evidence |
|---|---|---|
| the scale primitive | **no** | declares "zero dimensionless content" in its own text; `A/B` is a pure number |
| covariance | **no** | already exhausted by the landed kernel classification, which *leaves* exactly this number |
| source restriction by the neighbour rule | **no** | tested 2026-07-25: admissible configurations span the full space (rank 27/27 on a `3^3` torus) under hard-core, exactly-one-neighbour, and at-most-one rules, so `I` and `Delta` stay independent on them |
| coarse-graining / decimation RG | **no** | landed 2026-06-12: the massless point is a fixed point of the declared Schur RG map, but an **unstable** one, at the `E=0` resolvent threshold — so RG does not select it, it must be tuned to |

The RG entry is worth stating carefully because it is easy to get backwards.
Masslessness *is* preserved by decimation — the condition "annihilates
constants" is exactly invariant, and the landed `d=3` step-1 closed form
(`diag' = mu - 6t^2/mu`, face-diagonal `-2t^2/mu`, axial `-t^2/mu`, nothing
beyond) satisfies it. But being a fixed point is not being selected: the landed
uniform-chain RG note finds the fixed set `g in {0, 1/2, -1}` with `|g| = 1/2`
— which is exactly the massless, row-sum-zero point — labelled **unstable**.
An unstable fixed point is a critical surface reached by tuning, not an
attractor reached by flowing.

**Consequence.** `A/B` is not determined by anything currently in the framework.
The remaining candidates are dynamics or a formation rule, both explicitly
withheld by the axioms, or a structural principle not yet identified. It is not
a convention-shaped gap; it is a genuine derivation debt with no current route.

### What could discharge the last numbers without an import

Not a convention, by owner standard. Two candidate classes:

1. **Dynamics or a formation rule.** Explicitly withheld by the axioms. This is
   what `a_act` needs.
2. **Self-consistency conditions.** `L^{-1} = G_0` in the gravity lane is a
   *condition*, not a supplied number: if the field's propagator must be the
   inverse of its own law operator, that could pin `A/B` with nothing imported.
   **This class was under-rated in this campaign** — T4a was declined twice as
   corollary churn, which was the wrong judgement under the one-import standard,
   because it is the only identified route that discharges a dimensionless debt
   without paying anything.

   Honest caveat: the two landed weak-field bridge notes obtain `L^{-1} = G_0`
   from a *supplied* action or *supplied* dynamics, so as currently written it is
   not free either. Whether self-consistency **alone** pins `A/B` is well posed
   and untested.

**Next target on this standard:** test whether a self-consistency condition, with
no supplied action and no supplied dynamics, constrains `A/B` within the landed
two-parameter family. That is a bounded, self-contained question.

## Planck's scope, and one mechanism tested and ruled out

**What Planck settles.** The scale-reference primitive fixes `a^{-1} = M_Pl`, a
dimensionful units conversion. That is the whole of it. By its own text it
"carries zero dimensionless content", so it settles no pure number anywhere in
the framework — not `alpha`, not `A/B`, not `w`. Any table row priced as "a unit
convention" should be checked against that distinction; one row in the pricing
table above was mislabeled and is now corrected.

**A mechanism tested and ruled out.** The most direct route from neighbour
constraints to the law's coefficients: `L = A·I + B·Delta` is only ever applied
to *admissible* sources, so if admissibility forced a linear relation among
`rho` and `sum_nbr rho`, then `I` and `Delta` would be dependent there and the
two-parameter family would collapse. Tested on a `3^3` torus by enumerating
admissible configurations and taking the rank of their span:

| rule | admissible configs (<= 3 records) | span rank |
|---|---|---|
| hard-core (no occupied neighbour) | 1576 | 27/27 |
| exactly one occupied neighbour | 82 | 27/27 |
| at most one | 2953 | 27/27 |
| unconstrained | 3304 | 27/27 |

Admissible sources span the full space even under the tightest rules, so `I` and
`Delta` remain independent on them. **The neighbour rule does not pin the law's
coefficients by source-restriction.** A different mechanism would be needed.

## An attempt that failed, recorded because the reason is instructive

The scale-reference primitive fixes `a^{-1} = M_Pl` and declares it "carries
zero dimensionless content". The landed kernel classification leaves the
range-1 covariant law as `A·I + B·Delta`, whose only physical content is the
dimensionless ratio `A/B`.

The tempting inference — that since the primitive supplies nothing
dimensionless, the member needing no dimensionless number (`A = 0`) is
distinguished — **does not hold**. "Zero dimensionless content" means `A/B` is
*unsupplied*; it does not privilege the value zero. Selecting zero because it
can be written without naming a number is a naturalness or simplicity
principle, and the framework has none. The corpus uses that clause consistently
as a *blocker*; using it as a *selector* is having it both ways.

A second, independent error in the same attempt: the claim "long-ranged
precisely when `A = 0`" is false. `Dhat` ranges over `[-12, 0]`, so for
`0 < A/B <= 12` the symbol vanishes at nonzero `k` and the behaviour is
oscillatory, not screened. Verified independently after the gate flagged it.

**Consequence for planning.** Taking Planck as the scale buys units and nothing
else. It cannot pin any dimensionless content, by its own declaration, and the
law's entire physical content at this range is dimensionless. So the law's
coefficients cannot come from the scale, cannot come from covariance (which the
landed classification already exhausted), and by owner direction should not come
from a convention. What is left is that they must come from **the admissibility
rule** — the neighbour constraints — which is the one piece of framework content
not yet used and not yet specified.

That is the honest form of "we are in the business of identifying the law": the
law's coefficients are downstream of the rule, and the rule is the actual
foundational unknown. The landed
`ADMISSIBILITY_RULE_COVARIANCE_EXTENSION_CLASSIFICATION_..._2026-07-03.md`
already maps that rule space's structure — 10 orbit classes at occupancy level,
chirality requiring three condition values, and the theta-seed dichotomy. What
selects among them is the open question.

## Backlogged, with branches pushed and recovery commands

See `PR_BACKLOG.md`. Cycle 700 (admissibility closed under neither union nor
sub-collection, plus the sufficient separation condition) and cycle 701
(normalization residual map) are both proven, cold-run, pin-verified, and
un-PR'd on the cluster-cap evaluator's verdict.

Cycle 700's caveat on cycle 698's M1 is now a follow-up against landed work:
the additivity clause's domain is rule-dependent, and M1's decomposition
direction is the safe one.

## What I would do next

1. **The `kappa_EW`–`w` conditional correspondence** (point 2 above). The only
   landed cross-parameter link. Closing or sharpening it is worth more than
   another survey.
2. **T4a `L⁻¹ = G₀`** is now cheap: the landed kernel classification reduces it
   from an unsourced operator identity to two scalars within a two-parameter
   family. I declined it twice as corollary churn — "apply the theorem that
   just landed to a new label" is a named anti-pattern — but it is close to
   free for whoever wants that critical row moved.
3. **Not another cross-lane synthesis in a single session.** Today's evidence:
   self-contained exact classification landed (698, 699); cross-lane mapping
   and self-referential repair were backlogged, twice, with real errors found
   each time. The gate worked; the lesson is to give per-source reading more
   time than this session gave it.

## Method notes

- The prior-art sweep landed mid-campaign (#5611) and paid for itself three
  times: it caught the AC route-(b) duplication before any work, the
  admissibility-rule census duplication before any work, and the cubic-orbit
  Reynolds prior art on the kernel classification.
- Every runner was grepped for structurally-always-true rows before freezing.
  One tautological row survived into #5620 anyway, was flagged by the reviewer,
  and is the clearest single lesson: fix them when you see them.
- Reviewers caught two false PASSes of mine: the `5 → 4` axial counterfactual
  (actually `5 → 3`; the mixed channel dies too) and cycle 697's C9. Both were
  real.
- Every receipt-writing runner was cold-run in an isolated worktree detached at
  its own commit, with `runner_sha256` verified against the committed blob.
