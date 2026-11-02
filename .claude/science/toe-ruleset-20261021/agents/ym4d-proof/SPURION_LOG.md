# SPURION author log — 2026-10-30

## Contract and source identity

Executed `briefs_q/SPURION/AUTHOR.md` under `PROCESS_LIGHT.md` in the
specified working directory. The allowed output set is `SPURION.md`,
`SPURION_LOG.md`, and `checks/spurion_*`. Existing sources are read-only;
no commit, push, audit, ledger or axiom operation is part of this lane.
The working copy is a source snapshot without `.git`. The brief's LOCOP
commit identity cannot be certified here; actual source bytes are hashed.

The generic physics-loop skill was inspected for applicability, but its
unattended campaign/loop-pack/PR workflow is not used: the explicit brief
is a bounded in-place lane with its own process, output restrictions and
no-commit rule. No source-freshness or retained-status claim is inferred
from the snapshot. No skills caused a permission question or unfinished
authorized filesystem work.

The before inventory records SHA256 for 3,976 pre-existing files under the
working folder, excluding only this lane's allowed output names. The
inventory ran with nice 20, single-thread environment, peak RSS 28,983,296
bytes. No file in that inventory is intentionally edited. Source identities
and final integrity checks are in `checks/spurion_sources.json` and
`checks/spurion_verification.json`.

## Reading and scope decisions

The source dictionary used for the mathematics is:

| Source | Material read and used |
|---|---|
| AUTHOR / PROCESS_LIGHT / HANDOFF | Complete author/process instructions; current assignments and coordinator boundaries. FR/KR/TC remain named inputs. |
| LOCOP / REVIEW_LOCOP | L1–L14, LC1–LC6, scope, review item table and independent derivations: exact covariance, local Ward test, tensor projection, relative mass diagnostic, action extraction and conditional AF bracket. |
| EXTCONT | §§1–2, fixed-sector differentiated integration, hole-cost obstruction, §5 conditional closure and §6 live alternatives. Distinguishes supplied local action from exact finite global integration. |
| REALRGA | §§1–2, RGA-L/E and H0–H6: all retained species, original labels, mixed order (6,4), complete/inactive readers, group weights and the missing actual producer. |
| BFT_A | §§7.1,8.0 and composite-gauge definitions: residuals remain gauge invariant; a gauge choice does not delete them. |
| BFT_B | §§2.4,12.2,13.6,16.11,22.12 and later scope/status caveats. CovLift covariance is separated from background regularity and unreviewed norm extensions. |
| REVIEW_BFT_B_S5 / S7 | Lift-cocycle uniqueness and KPi-off reviewed qualifications: T>=5, log/cluster margins, locality and lack of hypercubic symmetry. |
| RD3 | Positive example and its exterior inverse/reference, actual normalized transfer, complete selected species and old-mass normalization diagnostic, remaining all-history obligations. |
| MIXSMALL | MS1–MS10, actual conditional-kernel mixed groups MS15–MS20, filled-family/hole scope and H-clause carry-over. Complete reader costs survive future tilts. |
| FLOW | §36 COV-GI, proof, criticality/positivity conditions, Schur factors and noncritical remainder. No all-history derivative conclusion is drawn from Gaussian cancellation. |
| RD / SOURCE_LOCAL_HISTORY_RETURN_ASTRA | Actual R2–R8 decision tree, chart measure convention, H11 completion minimum and its proved joint covariance. These substantiate the classification of actual selectors. |

No external paper was needed as a proof input; method credit to Balaban,
Dimock, and the localization authors is preserved. No [m] fact is used.

The brief's proposed implication “surviving mixed terms must be tuned”
was tested against the exact kernel and rejected as a general inference.
The draft distinguishes determined blocking/reference coefficients from
new adjustable bare physical parameters. A separate zero physical local
mass conclusion is proved only with the stated single-field/local scope.

## New written results and residual work

1. Exact covariance of RD's actual completion/size histories follows by
   a bijection of completion sets, including cut boundaries.
2. The inventory is closed under complete-reader multiplication, Haar
   integration, sums and positive ratios/logs. It is not an assertion of
   an already convergent local expansion.
3. The actual fixed-fine kernel Hessian is kappa u; the Haar chart Hessian
   is N^2/6 in LOCOP's colour metric. Neither is an independent physical mass.
4. The exactly integrated pair of unitary-mean SU(2) kernels has the
   surviving relative Hessian in S10. It is explicitly labelled a diagnostic
   of the reader inference, not the generic actual inherited-law coefficient.
5. The complete single-field Ward identity and its differentiated-integral
   form exclude a symmetry-breaking local mass. S13/S14 explain the
   corresponding admissible Gaussian and COV-GI cancellations.
6. Local Haar averaging makes supplied additive activities invariant with
   no new readers and no group-jet norm cost on an invariant domain.
   A tree-cycle degree-four projector provides a finite mixed-chart
   construction with explicit conditional scope and coordinate norm factors.
7. Full LC1 remains OPEN: actual local logs, stable selected domains,
   uniform graph/chart/reader costs and coefficient budgets are not supplied.
   LC2–LC6, the AF antecedents and physical continuum existence remain OPEN.

These are scoped results, not an exhaustion/no-go claim about RG. The
next concrete target is the complete mixed log of the RD3 hole-adjacent
return, with its normalizer, exterior inverse, original labels and selector
derivatives, before applying the new conditional averaging/projectors.

## Numerical preregistration and run

The criteria file contains statements and thresholds only. Recorded local
file birth times (UTC) and execution receipts give the order:

- `checks/spurion_criteria.md`: 2026-10-30 10:27:13.370600.
- `checks/spurion_check.py`: 2026-10-30 10:29:59.964274.
- First and only run: 2026-10-30 10:30:07.

The result receipt also records the exact criteria and runner hashes.
There were no exploratory numerical probes or later numerical amendments.
Written proofs were not preregistered, as PROCESS_LIGHT requires
preregistration for numerics only.

The command used all six BLAS/OpenMP thread variables equal to one and
`nice -n 20 python3 checks/spurion_check.py`. The runner holds a nonblocking
exclusive lane lock and samples macOS memory pressure, all three load
averages, niceness and its own RSS before and between groups. No pools or
RLIMIT_AS were used. The launch and every guard succeeded.

| Group | Result and measured evidence |
|---|---|
| Joint covariance and frozen-field control | PASS: max error 2.22e-16; changing one field only changes the trace by 0.0119571. |
| Haar reader survival | PASS: refinement error 2.49e-14; exact-formula Hessian 0.863208697637; centered-difference relative error 4.55e-8; reader integral 2.321964276848, different from one. |
| Gaussian Schur control | PASS in exact rationals: output diag(0,15/8), frozen-input gauge Hessian 3, positive-mass mutation 6/5. |
| Tree/projector algebra | PASS: reconstruction error 5.55e-17; exact polynomial idempotence and retained degree-five remainder control. |
| Complete readers/partition | PASS in exact rationals: unread normalization 1; reader integral 7/2; selected contributions 1/2 and 3. |

Peak run RSS: 22,380,544 bytes; maximum sampled load: 2.232421875; free
memory: 49%; nice: 20. All numerical criteria PASS. These are finite
algebra/quadrature controls, not all-history analytic estimates or a
numerical proof of covariance of Haar integrals. No failed check is hidden.

## Fresh hostile review

PROCESS_LIGHT §3 explicitly requires a fresh hostile reviewer. A fresh-context
review agent was therefore launched after the complete draft was written.
This is same-family Codex review, not cross-family verification. The reviewer
did not inherit the author conversation, was asked to reconstruct the
arguments, and may write only the new `checks/spurion_review.md` and any
new `checks/spurion_review_*` evidence. The author remains responsible for
fixes and final scope.

The fresh [hostile review](checks/spurion_review.md) ends with
**VERDICT: LAND**, restricted to the finite algebra, local mass statement
and conditional localization results. It leaves full LC1, uniform
coefficient/AF estimates, continuum existence and physical mass gap OPEN.

The reviewer required two narrow statement clarifications, both applied
in place and independently rechecked:

1. S9 now specifies an orbit-invariant open domain and a cycle-log chart
   after tree gauge fixing, rather than suggesting a global link-log chart.
2. S21 now specifies positive cycle radii with interior margins, those same
   radii as coordinate derivative units, the species factorials, field/source
   orders and placement of the supremum required for constants 16 and 17.

Initial draft SHA256:
`58b73b364a5a511955bc95d59699d8d05a197c09c589fe78935a9d19043970ca`.
Final reviewed source SHA256:
`8474bec9faca8b0d9a1318846088e26cf47a06f89748236c8d440bc0ab046667`.
No commits were made for these fixes, as required by the brief. The reviewer
confirmed that these were the only changes to the reviewed draft. The author
read the complete final review; no unresolved binding issue remains.
Neither the reviewer nor the author reran numerics after these prose fixes.

## Final verification

The final mechanical check compares every pre-existing path/hash against
`checks/spurion_inventory_before.json`, rejects added files outside the
allowed output names, parses the numerical runner without creating bytecode,
checks the saved criteria/runner receipt hashes, confirms the reviewed
SPURION hash and LAND ending, and resolves local Markdown links. Its receipt
is `checks/spurion_verification.json`. All 3,976 pre-existing files remain
unchanged and all authored outputs are in the authorized set. Only the
named finite mathematical claims and conditional interfaces are delivered;
the open all-history obligations are not represented as completed science.
