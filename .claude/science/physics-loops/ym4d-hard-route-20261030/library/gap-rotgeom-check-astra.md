# Repo search

Check of FINISH row 963 at `e3ee1bdba5fb6982daa83f8a2d1728748ab16937`, by OpenAI Codex (dispatch: gpt-6-astra xhigh; exact runtime variant and effort are not independently exposed here). Research text, not an audit; grants no status.

The target-specific `prior/gap-rotgeom-check-astra.md` is absent. The lead's
`prior/repo-search-2026-11-08.md` covers earlier RG targets, not this rotation
check. Its mass-gap hit is a one-step plaquette correlation, not a sector or
diagonal-transfer comparison. The source note identifies closer prior work:
`am1-port.md` and `lg1.md` for diagonal reflection positivity; row 892 for
centre SPLIT; rows 960 and 962 for geometry and projected seeds. These are
inputs to check, not new results of this lane. A targeted registry search for
rotgeom, vargeom, LSI-J-seed, SEED-FP and diagonal reflection found no match.
I fetched PR 10114 at `f76f6c649cff7dffbab664d8976e680e8f287fe9` and read
`MASS_GAP_LOCAL_BLOCK_ASTRA.md:106–149` at the digest's soft-route path.
That hit supplies none of the present comparisons. On main,
`8b11ae2bb95e641494fe75ed83d108ee712fa3a9`,
`research/ym4d/library/lg1.md` is byte-identical to the local file. Its
explicit qualification of Lemma S was checked with `git show`. These are
targeted checks of the lead's hits, not a new exhaustive search of all PRs.
This lane does not attack the projected engine or the seed suppliers.

## Scope and sources

The source has 544 lines. Verdicts below use HOLDS, HOLDS AFTER CORRECTION,
and FAILS, as requested. A passing GUIDE calculation establishes only its
model and arithmetic. No run discharges a proof. Credit for the account and
its reflection argument belongs to Ethan Sussman and Levent Alpoge, with
Claude and Codex as authors of their text. The repository ports retain their
printed provenance.

Sources downloaded once to `/tmp/sa-gap-rotgeom-check-astra.4fCPzV/`:
`sa_ym4.tex` (32,992 lines) and `sa_ca_I.tex` (166,711 lines), revision
`31a47c543775`. Main's workflow now points to RULES, SETTINGS and the check
procedure; those were read. User-specific output path and verdict vocabulary
govern this record.

CA-III was also downloaded once to that scratch directory. Its structural
index does not index the relevant remarks. Source reads were CA-III
79931–79990 and 108546–108567: the quotations are faithful, but neither
passage exhibits a negative reflection form on a straight torus.
The SA-index README, neighbouring chunk-03 rows and obligations led to
SA 2729–2883, 3271–3305 and 3380–3396. The last passage already constructs
the infinite-volume positive diagonal step. No CA-I passage was needed.
Recalled older literature remains recalled; no Balaban paper was used.

The source note's SHA-256 is
`530d54b1e8bdfaf6cc6caf76d74a3f06fad7ac4ba00e9590dc6ed29c6f30ee12`.
Its GUIDE script and log are pinned by the same checkout revision.

The material defects, ranked by what they break, are: (1) the finite-seed
identity and blanket obstruction; (2) adaptation confused with existence
of a coordinate mirror/channel; (3) the finite-torus OS domain; (4) the
missing diagonal recursion; (5) universal sector fact tests; (6) R5's
unrestricted representation; (7) unproved spectral and energy comparisons;
(8) thermal coefficients and approximate series; (9) the projection-grid
error claim. The arguments and repairs below cover these nine groups.

## Algebra, frozen sectors and reflection

- **R1–R3: HOLDS**, given the stated Wilson transfer input and its admissible
  time lengths. Moving commuting symmetry operators through the transfer
  factors leaves their ordered product. Taking the trace of the composed
  kernel gives the mapping-torus seam. Kernel positivity gives a positive
  twisted trace; the trace norm gives its untwisted upper bound.
- **R4: HOLDS.** On each isotypic summand the transfer operator acts on the
  multiplicity factor. This gives the character divided by its dimension
  in the trace formula. The vacuum subtraction is valid for the geometric
  and centre actions, which fix the positive vacuum. For an arbitrary
  commuting unitary representation that last hypothesis must be stated.
- **R5: HOLDS AFTER CORRECTION.** Its generator inequalities follow from
  `kappa (1-P_1) <= sum_s (1-Re V_s) <= 2 |Sigma| (1-P_1)` and the individual
  upper bounds. The additional bound `Z_1 >= Z/|G|` requires nonnegative
  twisted traces. It holds for the geometric actions of R1, not every
  commuting unitary representation in R4. Counterexample to the latter
  reading: on four points set `T=alpha I+J`, where every entry of `J` is one,
  and let the nonidentity element of `Z_2` act as +1 on constants and -1 on
  their orthogonal complement. The kernel is strictly positive, its top is
  simple, and the vacuum is invariant. Take `alpha=12` and time three.
  Then `Z_1=16^3`, `Z=16^3+3*12^3`, and `Z_1/Z=64/145<1/2`.
  The geometric/positivity hypothesis repairs this without changing SPLIT.
- **Section 3.1: HOLDS.** Direct classification of commuting triples gives
  92 and 244 flat classes. Centre flips leave 22 and 34 orbits. Signed
  permutations leave 10 and 7. Thus the stated trivial-sector residuals
  are 9 and 6. In Step 6 the remaining 2T vectors must be **237**, not 236.
  A Burnside cross-check gives `(2*176+6*64)/8=92` for Q_8, and
  `(2*1008+6*64+16*216)/24=244` for 2T. Here 176 and 1008 count ordered
  commuting triples before conjugation; the remaining terms use cyclic
  centralizers. After centre and spatial actions, canonical representatives
  have k identical noncentral entries, `k=1,2,3`. Q_8 has three order-four
  families; 2T has one order-four and one order-six family. Including the
  central orbit gives 10 and 7. Fixed-class counts 12 and 4 give exactly
  `(1-12/92)/2=10/23` and `(1-4/244)/2=30/61`.
- **Sections 4.1–4.2: HOLDS** for the local crossing argument and the cited
  split-torus setting, including its large-period restriction. Index
  chunk-03 rows 2775–2883 and obligations 2805–2809 lead to the source read
  SA 2729–2883. Its two paths have the same endpoints; the Wilson factor is
  a positive quaternion Gram series. This is Sussman–Alpoge's existing
  argument, faithfully checked here, not a new proof of this lane.
- **Section 4.3: HOLDS** as a non-separation statement for the stated
  straight torus, `N>=3`. It does not prove a negative reflection form.
  Step 8's stronger wording, “fails ... because the mirror does not
  separate”, must retain that distinction.
- **Section 4.4: FAILS** at “no coordinate mirror ... so the axis transfer
  operators ... do not exist”. For `L/2=M=b`, the lattice generated by
  `b(e_1+e_2), b(e_1-e_2)` is preserved by the coordinate reflection
  `x_1 -> -x_1`, which exchanges the two generators up to sign. It is not
  *adapted* to that coordinate normal. D2 itself gives an axis transfer
  representation with a twist. `am1-port.md` Section 1 and `lg1.md:417–423`
  explicitly limit Lemma S to simultaneous adaptation.
- **D1: HOLDS AFTER CORRECTION** on the infinite lattice; remove its
  finite-torus OS construction. A closed slab in a finite torus is not
  preserved by forward translation, so the displayed assignment on its
  whole half-algebra is not defined as claimed. A separate transfer-kernel
  construction and trace identity remain needed there, as D3 acknowledges.
  The omitted infinite-volume contraction step is already in SA
  3271–3305 and 3380–3396: iterated Cauchy–Schwarz bounds
  `||T F|| <= ||F||^(1-2^-j) ||T^(2^j) F||^(2^-j)`; the last norm is
  bounded by the local representative's supremum norm. Taking the limit
  proves contraction and null preservation. Complex tests require the
  antilinear reflection throughout.

  A precise replacement for the one-height suggestion is available in this
  same unbounded-normal setting. Write `S_i[F]=[tau_(e_i) F]`. Reflection
  sends `e_1` to `-e_2`, so translation invariance gives `S_1^*=S_2` on
  local tests. Consequently `S_1^* S_1=T_n` and
  `||S_1 F||^2=<F,T_n F><=||F||^2`; this proves null preservation and
  bounded extension. The commuting translations make S_1 normal. Its
  polar factorization is `S_1=U T_n^(1/2)`, with
  `U^2=U_(n')` on the support of T_n, since `2e_1=n+n'`.
  This supplies no general positivity of S_1. Identifying U with the
  source's particular geometric glide would require additional bookkeeping.

## Diagonal comparisons

**D2: HOLDS** for the period lattice displayed in its statement. Its index
in the (1,2) plane is `LM`; its second-coordinate subgroup is `g Z`, so its
horizontal period is `LM/g`. For `L/2=M=b`, the half-shift gives exactly
`Z_even-Z_odd`. This identifies two readings of **one partition function**.
It does not identify their vacuum normalizers or their thermal seeds.
The title's “every adapted” must be restricted to that displayed family;
a general tangential period lattice need not yield the straight `B'` used
there.

**D3: HOLDS AFTER CORRECTION.** The pairing-preserving group has order eight,
and the named simultaneous exchanges are correct. The full four-direction
engine also needs the recursion compatibility which the body expressly
leaves OPEN. The final summary drops this third missing input. Thus the
statement is conditional on the trace formula, the simple top **and** an
admissible enlargement recursion, not only on the trace formula.

**D4: HOLDS** for the same infinite-volume state, given the two OS
constructions and the vacuum-complement definition of gap. Tangential
translations are unitary, so the correlation bound's constant is uniform
in the tangential displacement. Place the fixed local supports on opposite
sides by a fixed preliminary translation. For even `k`,
`k e_1=(k/2)n+(k/2)n'` gives axis decay with exponent `m_n/2`.
Conversely `k n=k e_1+k e_2` gives diagonal decay with exponent `m_1`.
Apply these bounds to reflected autocorrelations. Positivity of their
spectral measures and density of local vectors give
`m_1 <= m_n <= 2 m_1`. Fixed support offsets alter constants only.
This compares neither different DLR states nor different finite-torus seeds.

**Step 5(a),(c), Step 8 and the final blanket conclusion: FAILS** as an
obstruction. The same measure on a different period lattice need not have
the same finite thermal sum. Equality of a partition function in D2 does
not equate `Z/lambda_axis^g` and `Z/lambda_diagonal^alpha`.
The common bulk pressure discards precisely the finite-size and spectral
information needed by a seed. Lemma S excludes simultaneous adaptation,
not all possible inequalities or comparison arguments. Main's
`research/ym4d/library/lg1.md:417–423` says this explicitly; its blob is
identical to the local file. A correct conclusion is: **row 963 establishes
no sufficient replacement for the full seed.** It does not prove that
rotated geometry can never help.

The blanket “at most one positive channel” claim also fails. Total twist
equal to the identity gives an ordinary torus with four axis channels.
A gluing reflecting one spatial coordinate leaves two other spatial
coordinates as product directions, each with a positive transfer channel.
The claim must specify a nonidentity proper rotation and justify the
channel restriction separately.

**Lemma M: HOLDS.** The integers `2 n_i^2/|n|^2` lie in `{0,1,2}` and sum
to two. Primitivity leaves one unit entry, or two entries of absolute
value one. The translation part gives exactly the stated mirror heights.
This excludes a hyperplane reflection with normal `(1,1,1,1)`, not every
possible positive-operator construction along that displacement. D1's
one-height glide factorization remains unproved as written.

## Sector comparisons and fact tests

**The universal sector fact test: FAILS.** Translations act trivially on
every frozen flat class. Hence a sector with nonzero momentum contains no
frozen ground vector and has `S_rho=0` in the normalized frozen limit.
It passes any positive sector threshold. This directly refutes “every
sector form still fails” in Sections 3.4, 6 and 8. The trivial-sector
calculation remains correct and suffices for its own frozen test.

**The U(1) photon coefficient: HOLDS AFTER CORRECTION.** Row 962 explicitly
uses *three* photons to obtain about 9,100. One U(1) field has two physical
polarizations, so its continuum free-photon bulk term is
`(pi^2/45) 24^3`, about **3,032**, before finite-volume and toron terms.
The group-size logarithm at `a=30,b=720` is correctly 25.6884. This correction
does not rescue the trivial-sector seed: an invariant pair at opposite
minimal momenta already has weight approximately `exp(-pi/6)>0.3`.

**Torons: HOLDS AFTER CORRECTION.** Given the spectrum of 3.2, centre
parity and O_h orbit counting hold. The leading thermal weights are
`(12 pi)^(3/2)/g^3` and that number divided by 48: about `231.47/g^3`
and `4.8223/g^3`. These are small-g asymptotics of weighted sums, not
counts below a sharp energy threshold or uniform estimates for `g<=1`.
A hand test avoids that approximation: the orbit of flux `(2,0,0)` supplies
one invariant state with weight `exp(-g^2/12)>=11/12` for `g<=1`.

**Energy comparisons: HOLDS AFTER CORRECTION.** The momentum expansion
holds in the stated free massive scalar model. A generic opposite-momentum
pair gives the regular representation of `O_h/{1,-1}`, hence the fractions
`d_rho^2/24`. Special shells do not: the minimal axial shell has only three
unordered pairs, so cannot contain every even irrep. Odd pairs of one
scalar species are absent. Literal “no energy margin” is too strong:
a nontrivial zero-momentum even irrep has no one-particle scalar and needs
at least two particles. No adequate **SU(2) aggregate sector bound** is
supplied by this observation or by the free model.

The quarter-turn bulk factor `1/256` holds as a massless continuum
free-gas asymptotic. Length-four momentum cycles contribute one quarter
of the thermal log at time `4a`; its momentum integral contributes
another `1/4^3`. The axis term is lower-dimensional. Equal sector weights
require smallness of all nonidentity twisted traces, not just one quarter
turn. The exact geometric-symmetry bound
`abs(Tr(V_g T^a)/lambda_0^a-1)<=S` does follow from R4.

**Section 3.4(i),(iii): HOLDS AFTER CORRECTION.** Identifying the lightest
SU(2) excitation as centre-even `0++` is an additional spectral premise.
A zero-momentum projection loses the localized correlations read by the
current consumer. But the exact target is the Hilbert space generated by
`tr F^2` (`gap-finishline-opus.md:152–169`), not every sector of an enlarged
Hilbert space. The full seed is sufficient for the current engine, not
proved necessary for every possible engine. Row 962 Section 7.4 already
owns the projected-engine question.

SMALL-BOX's scalar level is RECALLED. `gap-phys-seed.md:98–113` attributes
the `g^(2/3)/b` law to Lüscher, Münster, Koller and van Baal through van
Baal's review, and labels the seed reading GUIDE. Given this trivial-sector
level, its weight tends to one. That supports this sector's obstruction,
not every sector's. K7's critical/coexistence physics is also RECALLED
in `gap-mid-max.md:44–68`. The diagonal table's K7 entry is conditional
on that physics, the diagonal engine and the required state comparison;
it is not a newly verified computation.

## GUIDE verification

GUIDE check: a separate implementation groups one-particle momenta into
permutation cycles and uses
`prod_cycles (1-exp(-length*omega+i theta*cycle_sum))^(-1)`.
This differs from the author's fixed-point trace-power implementation.
For `K=60,M=192`, all nine selected rows of Step 7 reproduce to the saved
precision. The quarter-turn ratio at `x=0.25` is 0.0096567381. The original
model is a scalar; no SU(2) or photon estimate follows from that run.

The grid computes momentum **modulo M**, not exact momentum zero. Changing
only `M` gives the following GUIDE sensitivity, with `K=60` fixed:

| x | S_0, M=192 | S_0, M=256 | S_1, M=192 | S_1, M=256 |
|---|---:|---:|---:|---:|
| 6.5 | 783969.6900 | 747759.8905 | 16332.7036 | 15578.3328 |
| 7.0 | 95.272863 | 94.506668 | 1.985853 | 1.969891 |
| 7.5 | 0.28535358 | 0.28510165 | 0.00652938 | 0.00652413 |

At 6.5 the stated finite Bose model's per-component momentum standard
deviation is 62.0922, not at most 53. The advertised `exp(-6.6)` Gaussian
alias estimate is therefore not a justified bound. If meant as a relative
error bound for the projected trace, the 4.84 percent change already
contradicts it. This sensitivity test is not an error enclosure for M=256.
The old grid's log-linear crossings are **11.99144, 7.49514, 7.14648**.
The broad threshold conclusions and C1–C4 dispositions survive; report
the latter two as approximately 7.5 and 7.15, not certified thresholds.

The displayed hand series of Section 3.4, using its Bessel value of `s`,
evaluates to 118.6042, 0.349629, 0.00935174 and 0.000306086 at
`x=7,7.5,8,9`. Its listed 106 and 0.37 are rough estimates, not the
values of the displayed expression. The Bessel expression is a continuum
momentum integral, not the exact finite-box sum. The zero-momentum series
also uses a dilute Gaussian approximation; it must not carry an equality
sign for the exact Bose gas.

The Gaussian normalization in that heuristic also needs care. With
`D=(2 pi sigma^2)^(3/2)`, a Gaussian N-particle approximation gives
`sum_N s^N/(N! D N^(3/2))`. The simplification `D=s exp(x)` holds for
the nonrelativistic leading value of s, not its exact Bessel integral.
The latter gives `s(9)=3.56249`, rather than 3.7. These are approximation
corrections, not counterexamples to a Wilson-theory statement.

The original scalar calculation has no nontrivial centre action. Its
`S_1` is the space-group invariant projection; adding a trivially acting
centre would leave it unchanged. The finite cutoff is part of the stated
model: changing K from 60 to 80 at x=12 changes the full log from
0.2603202633 to 0.2604498296. It must not be called the untruncated sum.
No verified error tolerance for the continuum gas is claimed here.

Run record: the first lock command failed because this sparse checkout lacks
`scripts/automation_lock.py`. I supplied the unchanged module from
`origin/main` in the scratch directory and retried via `PYTHONPATH`.
The machine lock was acquired by `rotgeom964-check` at 20:38:14 UTC;
memory free was 63 percent. The single-process run used one BLAS thread,
nice 10 and a 2 GB RSS stop. It completed in 26.28 seconds, peak RSS
1,372,946,432 bytes. Script and full log are in the scratch directory as
`check_guide.py` and `check_guide.log`; supplemental arithmetic is in
`guide_arithmetic.log`. The lock was released (`lock-release.json`).
The cited `guide/lane963/run_guide.sh` is absent from the pinned tree;
the Python source and saved run log are present. All selected scientific
rows and the quarter-turn criterion were checked; unused aliased rows
at x<=6 were not rerun. No computation supplies a proof step.

## Statement-by-statement verdict map

Line numbers refer to the unchanged 544-line source. Administrative plans
and process timestamps are not scientific statements. Repeated conclusions
take the verdict of their underlying statement, not a fresh status.

| Source lines | Statement | Verdict and exact scope |
|---|---|---|
| 40–72 | Prior-work and source inventory | **HOLDS AFTER CORRECTION**: the named local results exist; the brief grep is not an exhaustive repo search, and Lemma S has the narrower scope above. |
| 76–94 | Setting R and R1(a)–(c) | **HOLDS**, given (TM), for the geometric and centre actions. |
| 95–103 | R2, ordered total twist and conjugacy | **HOLDS**, including the quarter-turn schedule with `4` dividing the time length. |
| 104–113 | R3, mapping torus and inverse twist | **HOLDS** from the composed kernel; inverse twists have equal real traces. |
| 114–125 | R4(i)–(iii), characters and projectors | **HOLDS** for a finite commuting unitary representation. |
| 126–132 | Nonnegative sector seeds; twisted seed | **HOLDS AFTER CORRECTION**: assume invariant vacuum; character weights can be complex (the geometric traces are real). The twisted operator is not generally positive; the identity twist is an exception. |
| 134–150 | R5 and recovery of centre SPLIT | **HOLDS AFTER CORRECTION**: require invariant vacuum and nonnegative twisted traces for its additional lower bound; exclude the trivial-group empty-generator convention. The centre specialization holds. |
| 151–155 | Translation and point-group constants | **HOLDS**: for the cubic translation generators `kappa=4 sin^2(pi/b)`; equal directional deficits give `3 q_tau/sin^2(pi/b)`. A fixed generating set of O_h has a fixed positive constant. |
| 159–184 | Group action; frozen Q_8 and 2T counts | **HOLDS** for the normalized frozen model. These are not finite-coupling degeneracy claims. |
| 186–198 | U(1) toron sectors and their count | **HOLDS AFTER CORRECTION**, conditional on the stated spectrum; weighted small-g asymptotics and the exact one-orbit test are distinguished above. |
| 199–203 | Photon sectors, pair weight and entropy | **HOLDS AFTER CORRECTION**: one U(1) photon gives about 3,032, not 9,100; the invariant pair survives. The finite-group lower bound needs the R5 hypotheses. |
| 205–218 | Momentum and angular energy comparisons | **HOLDS AFTER CORRECTION** as model statements. Generic-orbit fractions are not low-shell multiplicities; no universal absence of an energy margin is proved. |
| 219–223 | Quarter-turn free-energy deficit and small-S bound | **HOLDS AFTER CORRECTION**: the former is a free-gas asymptotic; the latter is an exact character bound. Sector equidistribution needs all twisted traces. |
| 225–227 | SU(2) lightest `0++` in the trivial sector | **HOLDS AFTER CORRECTION** only as an added spectral premise. It is not derived here. |
| 228–239 | Dilute scalar count and projected thresholds | **HOLDS AFTER CORRECTION**: integral and Gaussian approximation, with the corrected arithmetic above; not exact finite-box Fock identities. |
| 240–245 | Full trace in the present engine; target sectors | **HOLDS AFTER CORRECTION**: current full-trace consumer confirmed by row 962; no necessity theorem for all possible consumers. |
| 246–248 | Every sector form fails all rivals | **FAILS**: nonzero-momentum frozen sectors are empty. The stated trivial-sector tests survive conditionally. |
| 252–269 | Diagonal-RP sources and recalled literature | **HOLDS** as source attribution; the stronger straight-torus failure sentence remains a source assertion, not the non-separation proof's conclusion. |
| 271–284 | Crossing-plaquette path orientation and Gram sum | **HOLDS** by the written two-path calculation. |
| 286–301 | Straight-torus complement connected; no split | **HOLDS** for `N>=3`; no negative form was constructed. |
| 303–306 | RP on split diagonal tori | **HOLDS**, retaining the source's large-period/no-quotient-ambiguity conditions. |
| 307–309 | No coordinate mirrors or axis operators | **FAILS**: explicit invariant period lattice and D2's twisted axis channel. |
| 313–325 | Admissible heights and D1 | **HOLDS AFTER CORRECTION**: infinite-volume reconstruction only; finite-torus trace construction remains open. |
| 326–327 | One-height glide/positive-part description | **HOLDS AFTER CORRECTION**: use the explicit polar factorization above. The particular geometric glide identification remains unproved; the absence of half-height lattice mirrors holds. |
| 329–341 | D2 and half-shift identity | **HOLDS** for the displayed period lattice; general tangential lattices require a more general spatial quotient. |
| 342–345 | Positive diagonal trace reading of D2 | **HOLDS AFTER CORRECTION**, conditional on the still-missing finite transfer and trace construction. |
| 347–360 | D3 symmetry and full diagonal engine | **HOLDS AFTER CORRECTION**: symmetry calculation holds; full engine also needs recursion compatibility. |
| 362–375 | D4 and physical-unit factors | **HOLDS** for one state under LG1 and both OS constructions. |
| 377–389 | Same finite thermal sum; only bulk-pressure bridge | **FAILS**. Same-state gap comparison and the missing comparison between limit families remain valid limited observations. |
| 394–410 | Fact-test table | **HOLDS AFTER CORRECTION** as a table restricted to the specified trivial sectors and conditional diagonal inputs. The universal-sector row, 236 count, and one-channel claim fail as stated; the half-shift and D4 rows hold. K7 was not numerically tested. |
| 412–415 | Every seed form passes the fact-test filter | **FAILS**, by the frozen nonzero-momentum example. |
| 419–427 | Scalar determinant, projections and alias estimate | **HOLDS AFTER CORRECTION**: exact cycle/Fock identities; finite grid projects modulo 192, with no supplied exact-zero-momentum error bound. |
| 429–438 | C1–C4 criteria | **HOLDS** as the recorded comparison criteria, not proofs or fresh predictions by this checker. |
| 443–470 | Three-part “buys nothing” verdict | **FAILS** as stated; replace by “no sufficient replacement is established here”. |
| 472–484 | Reopening conditions and by-products | **HOLDS AFTER CORRECTION** with the R5, D1–D3 and scope qualifications above. The projected engine remains owned by row 962. |
| 488–503 | Lemma M and excluded light-cone mirror | **HOLDS** for lattice hyperplane reflections; other positivity constructions are not excluded. |
| 507–521 | Saved run receipt and selected numerical rows | **HOLDS** as recorded GUIDE arithmetic; all selected rows reproduced. The shell wrapper is absent, so its command/environment history was not independently reconstructed. |
| 523–526 | Interpolation, quarter-turn ratios and asymptotic reading | **HOLDS AFTER CORRECTION**: the grid crossings are 11.99144, 7.49514, 7.14648; cutoff and aliasing remain model limits. |
| 528–534 | C1 PASS, C2 FAIL, C3 FAIL, C4 PASS | **HOLDS** for the stated truncated/grid model and broad intervals. |
| 536–540 | Easier projected scalar numbers; correction to row 962 | **HOLDS AFTER CORRECTION** as GUIDE only: the improvement is about 4.5–4.85 in x; the quoted hand-series values need the corrections above. |
| 544 | Final result | **FAILS** as a blanket obstruction; the surviving algebra and properly conditional comparisons are listed above. |

No source note, registry, ledger or status file was changed. This check
does not supply (LSI-J-seed), (SEED-FP), a diagonal finite-torus transfer
construction, an admissible diagonal recursion, shape independence, or a
projected seed consumer. Work is local on
`codex/gap-rotgeom-check-astra-e3ee1bdba`; no commit or push was made.

RESULT: Row 964 — FAILS as written: row 963 does not prove that rotated or diagonal geometry buys nothing. R1–R4, the frozen trivial-sector counts, the local diagonal-RP argument, straight-torus non-separation, Lemma M, displayed-family D2 and same-state conditional D4 hold; R5, D1, D3 and the sector comparisons need the stated corrections. Selected GUIDE arithmetic reproduces for its finite scalar model, with projection-grid and asymptotic corrections. No seed obligation is closed and no scientific status is granted.
