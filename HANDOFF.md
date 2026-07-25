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
