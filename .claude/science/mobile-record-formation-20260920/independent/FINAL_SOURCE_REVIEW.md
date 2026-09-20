# Final candidate source review

Date: 2026-09-20. Scope: scientific scrutiny of the complete candidate note
`docs/MOBILE_RECORDS_RARE_FORMATION_EVENT_LAW_AND_SIX_SITE_WITNESS_BOUNDED_THEOREM_NOTE_2026-09-20.md`
and complete runner
`scripts/mobile_records_rare_formation_event_law_2026_09_20.py`.
This is not a landing decision, audit, or effective-retention verdict.

**Source-bound conclusion:** the final candidate sources identified below are
scientifically confirmed within this review's scope. No unresolved
mathematical or executable-claim defect was found. This conclusion is based
on the complete source read, the independent derivation and computation,
and same-session review of the complete correction diff.

The independent calculation in `REPORT.md` was completed and sealed before
these primary artifacts were first read. `INITIAL_SEAL.json` records that
report's SHA-256 as
`3d31d272951642dc36812dec7a5404f5150f51bd084a947e937ae1f4846aeb44`.
No primary `probe.py`, `probe.json`, or `CHECKPOINT.md` was read in this task.

## Findings and disposition

The complete mathematical argument and numerical claims agree with the
independent calculation. Two precision corrections were requested on the
first reviewed source:

1. Equation (5) gives off-diagonal class jump rates; it should explicitly
   restrict to distinct classes and specify the diagonal as minus the total
   exit rate, with zero generator row at full absorbing classes. The initial
   all-pairs display would otherwise give diagonal zero because an insertion
   cannot remain in the same motion class.
2. The probability `p_N` in equation (8) should be explicitly defined as the
   limiting birth-indexed count law as epsilon tends to zero. The initial
   wording simply called it the law after the Nth birth, which can read as an
   exact finite-epsilon claim. The note's own finite-rate result distinguishes
   these two laws. The proof already establishes the intended limiting law.

I also recommended putting the slow-time scaling `tau=epsilon t` directly
in the machine-readable claim scope so it matches the theorem's proof.
All corrections are present in the final note. Equation (5) now states
`D != C`, gives diagonal `-bar B_C`, and declares full rows zero. Equation
(8) is explicitly the limiting count law at fixed graph and motion rates.
The claim scope states the slow time and off-diagonal rates; the menu is
now explicitly nonempty in both the scope and model. I inspected the
complete diff against the fully read first version. No other note content
changed, and the runner is byte-for-byte unchanged. These findings are
resolved; no additional mathematical obstruction was found.

## Mathematical coverage

* **Model and motion classes.** Positive symmetric weights and symmetric
  positive edge rates give exact detailed balance with the product weight
  restricted to each motion component. Counts are conserved, while distinct
  components may share a count vector. Births are supplied model conditions,
  permanent and content-preserving, rather than derived axiom consequences.
* **Next-birth resolvent.** The non-full finite component has strictly
  positive minimum birth hazard, ensuring convergence of the killed
  semigroup integral. The normalized occupation identities (2) establish
  boundedness and identify every subsequential limit uniquely. No premise
  that event sampling is stationary is assumed in this argument.
* **Waiting time and marks.** Inserting `h epsilon` into the resolvent is
  exactly the Laplace transform in scaled waiting time. Its limit factors
  into the transform of an exponential time and the stated event mark law.
  Finiteness makes convergence uniform over entry states; linearity extends
  it to arbitrary entrance distributions. The strong Markov property and
  the finite number of births justify iteration through absorption.
* **Event/time distinction.** The pre-birth law is `pi_C B/E_pi_C B`;
  the embedded class chain normalizes averaged rates separately in each
  source component. The covariance and total-variation identities follow
  immediately. The note distinguishes third-birth and fixed-time ensembles
  and makes no uniform-in-volume inference.
* **Count partition identity.** The insertion/deletion bijection gives
  multiplicity `n_a+1`. Using an entire count sector requires its stated
  source-sector connectivity hypothesis. Destination-sector connectivity
  is unnecessary for the one-step count identity, but every subsequently
  used source sector must again satisfy the hypothesis.
* **Third-birth witness.** The 28 source sectors and 577 states through two
  births are sufficient for this observable. My independent breadth-first
  search also checked all 56 sectors at level three. Pair partitions,
  wedge counts, the three-site edge profile, and forest leaf sums all agree.
  The exact rare result is `2701/53880`; static is `73/1440`; their signed
  difference is `-73/129312`. The full microscopic and count total-variation
  values coincide here at `811/387936`: for any final count vector, deletion
  multiplicities make the post-birth microscopic law proportional to the
  static weight within that sector.
* **Finite-rate witness.** The second-birth law is exactly static for every
  epsilon in this example because the single-record entrance is stationary
  and the total hazard is constant at 30. Therefore the 15-state
  identical-pair absorption calculation is the correct finite-epsilon
  reduction, rather than a rare-event approximation at the entrance.
* **Vacancy bound.** If `w_min<1`, any local product with at most `d`
  neighbors is at least `w_min^d`; if `w_min>=1`, it is at least 1. Thus
  `B(s)>=q min(1,w_min^d) V(s)`. Hops leave the vacancy count fixed and
  every birth reduces it by one, giving `L V=-epsilon B`. Dynkin's formula
  and Gronwall give the expectation bound; `1_(V_t>0)<=V_t` gives the
  completion-time tail bound. This uses the stated finite closed graph,
  positive time-independent rates, and no export/removal.

The generic proof covers a larger finite-model family than the runner,
whose checks instantiate the stated six-site example and a two-state
symbolic test. This is an appropriate division of proof and computation;
the finite runner does not independently certify all finite graphs.

## Independent finite-epsilon evidence

The independently derived six-orbit absorption system in `REPORT.md` gives
the following exact probability for every positive epsilon `e`:

```
P(e) = [95366160000 e^5 + 41898708000 e^4 + 6758339400 e^3
        + 498976260 e^2 + 16928359 e + 210678]
       / [1905120000000 e^5 + 836593920000 e^4 + 134896320000 e^3
          + 9957002400 e^2 + 337738320 e + 4202640].
```

Substitution at `e=1/1000` independently gives exactly
`2851401694918427/56880888215238000`, the candidate's finite-rate value.
Its absolute error from the rare limit is
`14631226274927/25539518808641862000 = 5.728857455989422e-7`, below `6e-7`.
The exact harmonic residual vanishes symbolically. The zero-motion control
is `14717/294000`; constant-weight controls `W=1` and `W=2` both give
all-identical probability `1/36`. Those controls were computed before
reading the primary sources.

## Executable checks

The frozen primary runner executed successfully with `TOTAL: PASS=15 FAIL=0`
and exit code 0. Full output is in `PRIMARY_RUN.log`. All seven advertised
mutations exited 1 and failed their declared families, as recorded in
`MUTATION_REVIEW.json` and `mutation_logs/`:

| Mutation | Observed failed families |
|---|---|
| `motion_flat` | motion |
| `birth_normalized` | content_law, event_sampling, insertion |
| `drop_multiplicity` | insertion |
| `merge_sectors` | content_law |
| `unbiased_events` | event_sampling |
| `killing_flat` | resolvent |
| `allow_removal` | vacancies |

The primary source was read in full, including the mutation behavior and
the scope of the finite checks. Its component traversal stays within the
supplied complete count sectors because hops preserve counts. The pair
generator has at most one hop to any distinct occupied pair, so assigning
rather than accumulating each off-diagonal entry is valid for that helper.
The finite-rate birth vector correctly includes the equal-content term,
opposite-content term, and four neutral-content terms at each empty site.

## Source identities and limits

The first complete read was frozen under `review_sources/` with these
SHA-256 hashes:

* Candidate note:
  `6231fdc8cd1d989323472feb0c953b153c31fcf5b8c54123aa3b074b74190ed7`.
* Candidate runner:
  `1f64e0a8d83c872abb6fb87d11da1c3c14d5a87416ff96404a286645afa71c4d`.

The **final confirmed source identities**, read directly from the current
workspace after correction, are:

* `docs/MOBILE_RECORDS_RARE_FORMATION_EVENT_LAW_AND_SIX_SITE_WITNESS_BOUNDED_THEOREM_NOTE_2026-09-20.md`:
  `8cc06519d7f3acc088b1e450c151f0870ab21d2987ef2b0224d40ba6a5e7e4e2`.
* `scripts/mobile_records_rare_formation_event_law_2026_09_20.py`:
  `1f64e0a8d83c872abb6fb87d11da1c3c14d5a87416ff96404a286645afa71c4d`.

The final source copies and complete correction diff are preserved under
`review_sources/final/`. `FINAL_REVIEW_SEAL.json` records the final source,
review report, and execution-log hashes. The initial independent seal was
rechecked and is unchanged. The earlier primary-runner execution evidence
applies to the final runner because its bytes are unchanged; its mathematical
input parameters also remain unchanged in the corrected note.

The initial pinned base is `5d784d8ccda5268f2b7c056fcdf0d81fdb703319`.
The separate independent report and manifest preserve the original parent
note's source identity and the instruction revisions read for this task.

I did not independently repeat the author's search of 66 open PRs or check
the bibliographic novelty survey. Those are provenance/background statements,
not load-bearing steps in the local finite-model proof. No literature theorem
or numerical constant is needed for this verification. The canonical runner
cache, repository-wide lint, audit tooling, and downstream physics claims are
outside this scientific check. No files outside the assigned independent
output directory were edited, and no audit/retention status was applied.
