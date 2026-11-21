# The public Lean release of the OpenAI Yang-Mills construction (read 2026-11-11)

Status: a reading record by the lead (Claude Fable 5.2). It is not a check of the
proof. Nothing was built. The Lean sources below the top level were not read.

## Sources (GitHub organisation `yang-mills-group`, public since 2026-11-11 about 04:05 UTC)

- `OpenAI-YM-20261028`: one commit, 3456e5e75 (2026-11-05), "Import original October 28
  OpenAI Yang-Mills submission"; 9508 files; Apache-2.0. Read whole by the lead:
  `README.md`, `ChallengeSpec.lean`, `Challenge.lean`, `Solution.lean`, `ConcreteSU2.lean`.
- `YM`: one commit, 55ba9fc36 (2026-11-10), the working group's results repository;
  Apache-2.0. Read whole by the lead: `README.md`, `docs/README.md`,
  `submissions/openai-20261028/README.md`, `submissions/openai-20261028/docs/checks.md`,
  `checks/RemainingObligations.lean`, `checks/CompleteOS.lean`. Read in part:
  `checks/AcceptanceSpec.lean` (lines 1-12, 150-175),
  `checks/TwoPointPhysicalObservable.lean` (lines 1-12, 100-160).
- `.github`: the organisation profile, a members file and three statement PDFs. Not read.
- NOT read: `docs/assessment-1.pdf` (the group's assessment, 2026-11-10, 658 kB; a download
  needs the owner's OK); `PublicWilson.lean` and `PublicTheory.lean` (the definitions of
  `GaugeGroup`, `IsSimple`, `WilsonFamily`, `Converges`, `WightmanTheory.Axioms`); every
  file under `YM/`.

## What the theorem says

`YangMills.jointExistence : YangMills.JointExistence` (`Solution.lean`; the statement is in
`ChallengeSpec.lean`, the last definition). In words: for every gauge group `g` with
`g.IsSimple` there is one Wilson lattice family `C` with `WilsonRegularity C`, and for every
strictly increasing sequence of volumes there is a subsequence and one hierarchy `T` with
four properties.

1. `wilson`: the correlations of `T` are the limit of the Wilson lattice moments of `C`
   (mesh limit at fixed volume, then the volume limit along the subsequence).
   `WilsonRegularity.running` says: beta divided by log(1/mesh) tends to a positive slope.
2. `reconstruction`: a Wightman theory (`T.theory.Axioms`), faithful fields, and analytic
   continuation that joins the Euclidean correlations of one SELECTED phase to the
   Wightman vacuum moments. The hierarchy carries a compact space of phases
   (`Character`) with a probability measure of full support; the Wilson limit is the
   integral over the phases (`mixture`).
3. `ope`: an operator product expansion at separated points, to every order, with one
   system of coefficients for all phases.
4. `nonfree`: the centred trace field of grade four has a two-point function with
   short-distance law r^-8 log^-2(1/r) times 3 dim(g)/pi^4, and it is not a finite sum of
   the stated mass-shell Wick profiles.

`ConcreteSU2.lean` gives the SU(2) case. The points are in four Euclidean dimensions.

## What it does not say (their own words, paraphrased; places given)

- `OpenAI-YM-20261028/README.md`, the paragraph before "Verification": the volume limit
  allows refinement (a subsequence); the spectral conclusions are the spectrum condition
  and the uniqueness of the vacuum; a positive mass gap, a general exclusion of
  generalized free fields with continuous mass, and all-orders MS-bar matching are
  outside the scope.
- `YM/README.md`, first paragraph: the group's opinion is that the submission proves that
  a Wightman theory can be constructed as a scaling limit of the four-dimensional Wilson
  theory for any simple compact gauge group; it does not prove that the infinite-volume
  limit is unique, and it does not prove a mass gap.
- `docs/checks.md`: the combined theorem asserts no uniqueness of the large-volume limit,
  no mass gap, no confinement, no all-orders perturbative matching; no unique phase is
  inferred. Row A5: the scale and the positive lattice probe do not establish a nonzero
  intrinsic continuum reference mass.
- `checks/TwoPointPhysicalObservable.lean`, `MassLimit` (line 133): a fixed separated
  two-point probe has a positive finite limit after a root is taken. The comment says that
  no intrinsic scale and no spectral gap is asserted. It is a nonzero-correlation
  statement. It is not a decay statement.
- `checks/CompleteOS.lean`: the group proves the Osterwalder-Schrader axioms E0-E4 and the
  growth condition E0' for the scalar family of the centred stress trace of the selected
  phase. E4 is clustering with no rate (`E4_cluster_norm`, by contradiction from a
  sequence statement). There is no exponential rate anywhere in the files read.

## Verification as the READMEs state it (not repeated by us)

Lean 4.32.0; the kernel replayed 100,168 project declarations for 17 advertised results;
axioms: propositional extensionality, classical choice, quotient soundness; the standalone
Comparator executable was not run in the submission; the group ran Comparator on macOS
without Linux isolation. The group's table lists a second submission, "OpenAI, 4 November
2026", as work in progress; `docs/checks.md` says it has additional perturbative matching
claims.

## What it means for this lane

- The mass gap is outside the submission and outside the group's assessment. So is the
  uniqueness of the infinite-volume limit. Track B aims at statements that nobody has
  published a proof of.
- The crux of Track B agrees with the shape of their result. They take the volume limit
  along a subsequence and get clustering with no rate. A bound uniform in the volume
  (our finite-box statement, row 691) is the kind of input that would give both a rate
  and one limit on the lattice. This is an observation, not a result.
- The sources are Apache-2.0. We may read them and build on them in the open. Places to
  read next for the gap (not read yet): the modules behind `Extraction` (how the volume
  limit is taken), the phase decomposition (`Character`, `mixture`), and the effective
  action at the scale where the renormalisation steps end.
- Credit: the construction builds on Tadeusz Balaban's renormalisation-group programme.
  The `NOTICE` files were not read; read them before any public statement about sources.
- Submission route: the group takes proposals by email and promises no reply. This lane
  publishes in the open and does not plan around that route.
