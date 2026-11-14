# K4CORR2 author log

Task: execute briefs_q/K4CORR2/AUTHOR.md in the supplied snapshot.
Only K4CORR2.md, this log and checks/k4corr2_* may be created or edited.
No commits, coordinator changes, audit/ledger changes or axiom changes.

## Initial grounding

Read AUTHOR.md, PROCESS_LIGHT.md, K4CORR.md, REVIEW_K4CORR.md,
K4MATCH.md, CUMUL.md and LGF.md. FLOW was indexed by headings and read
at sections 0-4, 6-10, 15 and 110, plus the first part of section 18
(lines 708-760); these contain the conventions, named hypotheses,
conditional running/tuning estimates and final unresolved hypotheses
used here. Read HANDOFF's current assignments at lines 505-560.

The working directory is a supplied source snapshot without .git, docs
or scripts at its root. No repository revision, main refresh, global
primitive-registry audit or remote-PR coverage is claimed. The local
physics-loop skill and its DISCOVERY, CLAIM_STATUS and DELIVERY references
were read. The explicitly assigned lane process/file limits control this
task; its checkpoints and claim-scope record stay within the permitted
files. No unattended campaign, PR or framework-premise judgment is made.

Prior-result search: searched the supplied Markdown for BPHZ, forest
formula, renormalized diagrams, and upper bounds on corrections. The
matching primary sources K4CORR and REVIEW_K4CORR explicitly leave the
finite coefficient unbounded. Their scalar bubble and first Taylor
subtraction estimate are prior results and are not claimed as new here.

K4CORR sections 5.1-5.2 specify formal continuum Feynman-gauge vertices,
but explicitly leave the regulator, infrared/zero-mode prescription,
subtractions and matching unspecified. There is consequently no fully
defined prior numerical regularization to reproduce. The diagnostic
regularization in K4CORR2 is declared explicitly and is not silently
identified with the Wilson law.

## Intended scientific work

Rebuild all five families and their component/pairing bounds. First
bound the truly separated finite subfamilies, then the complete bare
families at a declared cutoff, and attempt the internal subtraction step.
Keep a cutoff-dependent constant distinct from the requested uniform
renormalized Cbar. State the higher-order/original-law remainder and
denominator estimate needed for a fixed-scale positive witness.

The exact numerical criteria were created before any checker or run.
Checks will test graph counting and rational constants, not replace the
missing renormalization or original-law estimates.

## Literature and attribution

For method orientation, inspected the abstracts of Steffen Pottel,
[A BPHZ Theorem in Configuration Space](https://arxiv.org/abs/1706.06762)
and [Normal Products and Zimmermann Identities in Configuration Space
BPHZ Renormalization](https://arxiv.org/abs/1708.04115). No theorem,
constant or gauge-theory matching claim is imported from them. Taylor
subtractions used here are proved directly. Credit Bogoliubov, Parasiuk,
Hepp and Zimmermann for the subtraction/forest method, Isserlis and Wick
for Gaussian contractions, and Balaban and Dimock for constructive RG.
No memory-only [m] item carries weight.

## Derivation and attempted routes

1. **Separated finite graph families.** Expanded the action-density vertices
   into elementary A and derivative-A fields, proved coefficient majorants
   from the trace normalization, and enumerated the connected pairings.
   The external-only no-self sub-sums and the four-support quartic bulk
   star admit uniform constants C_ext and C_star. Their sum bounds only
   the stated subset, not the full coefficient.
2. **Complete bare cutoff calculation.** Defined the heat-kernel ultraviolet
   cutoff and a compact interaction region, and bounded every bare family
   with its full connected count, derivative power and integration volume.
   Proved lower bounds on its own free coefficients before dividing.
   This gives explicit C_bare(delta,R) and a positive window for its
   truncated formal ratio. The attempt to use that constant uniformly
   **fails**: it contains a positive delta^-24 term and grows with volume.
3. **Renormalized position-space route.** Worked out the tadpole remainder,
   differentiated ghost bubble and insertion-collision regions. Rebuilt
   Taylor subtraction estimates through degree two with exact constants.
   The compatible overlapping subtractions, finite local matching and full
   IR limit are not bounded. This remains a live, uncompleted route, not
   a no-go claim. The missing complement C_rem is not assigned a number.
4. **Original-law transfer.** Specified a uniform relative higher-order and
   nonperturbative remainder plus a separate denominator lower estimate.
   Proved their fixed-scale polynomial cumulant margin and conditional
   connection with K4CORR's FLOW rate. None of these original-law estimates
   is supplied by the free diagram calculations.

No observed YM value, exact two-loop beta coefficient, flowed observable,
or coordinator-lane assertion was used as a hidden premise. The partial
graph bounds support REVIEW_K4CORR B1 but do not discharge it. The remainder
package is a sufficient version of K4MATCH lower matching, not a new proof
of that matching.

## Exact verification

The first and only numerical run started at 2026-10-30T05:30:42Z.
It passed 97 exact assertions, including all ten connected degree-list
counts checked both by explicit pairings and partition/Mobius inversion.
Scalar polynomial controls independently expanded normalized moments and
formed their cumulants, recovering all five families for n=2 and n=4.
The deliberately wrong repeated-cubic factor is detected in both controls.
They are algebra controls and are not proxy values of the YM coefficient.

Command, from the assigned working folder:

```sh
env OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 NUMEXPR_NUM_THREADS=1 /usr/bin/nice -n 10 python3 -I -B checks/k4corr2_run.py 01
```

The runner preserves attempt-specific outputs and refuses overwrites.
Evidence: checks/k4corr2_attempt01_results.json,
checks/k4corr2_attempt01_stderr.txt (empty), and
checks/k4corr2_attempt01_run.json. Nice was 20, all five thread limits
were one, five numerical locks were held, memory free was 52%, all load
averages were below 2, and combined peak RSS was 37,584,896 bytes.
There were no pools, RLIMIT_AS calls, failed numerical runs or float-based
scientific acceptance decisions. The output separately records the uniform
renormalized coefficient and positive original-YM window as OPEN / NOT PASSED.

The initial inventory records SHA-256 for 3,729 pre-existing lane files,
excluding the new K4CORR2 outputs. It was taken after the own criteria,
log and checker had been created; no pre-existing file was edited before
that snapshot. Ten primary-source hashes are recorded separately.

## Independent review

A fresh, separate-context Codex reviewer performed the PROCESS_LIGHT review.
This is same-family review. The reviewer created only
[checks/k4corr2_review.md](checks/k4corr2_review.md), preserving the AUTHOR
brief's file whitelist; the separate REVIEW brief's suggested top-level
output is outside that whitelist and was not created.

**VERDICT: HOLD for completion.** The reviewer found no mathematical defect
in the stated partial results. All 97 registered assertions reproduced in
memory. A third implementation, using weighted multigraph adjacency matrices,
independently verified all 20 connected/no-self counts. Its integer weight
formula and results are printed in review R3. The review rerun used nice 20,
all five thread limits one, all five locks read-only/exclusive, 53% free
memory, load averages below 2.781 and combined peak RSS 43,548,672 bytes.
No additional numerical output files were written and no run failed.

B1 is the substantive missing uniform renormalized coefficient enclosure
and its instantiated coupling window. It cannot be repaired by changing a
label or substituting the finite bare constant. B2 is expressly downstream:
the present brief asks to name, not prove, the original-law remainder, and
the reviewer accepts that input formulation. There are no editorial or
algebraic binding fixes to apply. The sole post-review manuscript change is
an appended review-link/disclosure paragraph. No audit status is inferred.

The reviewer then verified that the original 559 manuscript lines were
byte-for-byte unchanged and that the appended disclosure accurately
summarizes the review. Its final-version note binds the 568-line manuscript
SHA-256 `f7af21719921a45f7ada8f82ab8a8f2bd1db5d37f86ba282d6b725a452323b25`
and retains HOLD. No numerical rerun was needed for this provenance-only edit.

Final integrity, local-link and file-whitelist checks are recorded in
[checks/k4corr2_verification.json](checks/k4corr2_verification.json).
No pre-existing file was changed. Only the permitted author, log and
checks/k4corr2_* artifacts were created; no commits were made.
