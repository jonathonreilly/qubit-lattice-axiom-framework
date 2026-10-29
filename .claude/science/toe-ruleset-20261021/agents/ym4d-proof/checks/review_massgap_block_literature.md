# Primary-literature applicability register — local physical mass-gap unit

Read on 29 October 2026 by the independent same-family reviewer. This is a
bounded theorem/import screen, not a literature-completeness or whole-paper
verification claim. The [review](../REVIEW_MASS_GAP_LOCAL_BLOCK_ASTRA.md) binds
the actual source unit. Broader continuum OS/covariance/nontriviality literature
is being handled separately by the coordinator.

## Established inputs and exact scope

**Lüscher, DESY 76/54; CMP 54 (1977), 283–292.** The
[primary scan](https://bib-pubdb1.desy.de/record/396349/files/7611148.pdf)
was read through the temporal-gauge setup, time-zero space, Proposition 1 and
its proof, and Proposition 2's statement (PDF pages 3–8; scan pages 1–11).
Proposition 1 gives bounded self-adjoint, gauge-invariant, strictly positive
finite-volume transfer. Its one-link character argument uses positive
multiplicities in fundamental/conjugate tensor powers. This directly supports
the finite-transfer/Peter–Weyl ingredient of the predecessor. The quark hopping
restriction belongs to the fermionic part; this unit is pure gauge. No
volume-uniform physical gap, infinite-volume injectivity, or continuum
construction follows just from this proposition. The review independently
retains the magnetic half-factors, the \(c_R/d_R\) convolution multiplier and the
physical gauge projection; it does not import an unprojected operator as the
physical operator on all functions. [Published DOI](https://doi.org/10.1007/BF01614090).

**Shen–Zhu–Zhu, arXiv:2204.12737v1.** Read equations (1.1)–(1.6),
Assumption 1.1, Theorems 1.2 and 1.4, Corollary 1.6 and its surrounding
definitions/remarks, PDF pages 3–8, from the
[primary PDF](https://arxiv.org/pdf/2204.12737v1).
Their density is \(\exp[N\beta_S\sum_p\operatorname{Re}\operatorname{Tr}U_p]\)
and the SU(N) hypothesis is \(|\beta_S|<1/[16(d-1)]\).
Theorem 1.2 gives the unique infinite Langevin invariant state and convergence
of the finite Gibbs measures. Theorem 1.4 is a Langevin Dirichlet-form
inequality. Separately, Corollary 1.6 gives exponentially decaying covariance
for smooth local cylinders with disjoint supports, with a common positive
rate and support-dependent constants. It admits products/functions of loops.
Our normalization gives \(\beta_W=N^2\beta_S\), hence in four dimensions
\(\beta_W<N^2/48\), containing the reviewed range for every \(N\ge2\).
Together with the reviewed lattice OS/density argument this is an alternative
fixed-spacing physical-gap input. The stochastic gap alone is insufficient;
neither result supplies the needed cutoff-uniform physical-scale bridge.
[Publication DOI](https://doi.org/10.1007/s00220-022-04609-1).

**Rebeschini–van Handel, arXiv:1308.4117v1.** Read §§2.1–2.4, in
particular Definitions 2.2–2.3, Theorem 2.4 and Corollaries 2.6/2.8, in the
[primary PDF](https://arxiv.org/pdf/1308.4117v1).
For quasilocal single-site kernels, the trivial metric gives precisely total
variation with the half-\(L^1\) convention. Corollary 2.6 bounds expectation
differences by \(\sum_{ij}\delta_i f D_{ij}b_j\), where
\(D=\sum_{n\ge0}C^n\); a row bound below one supplies the required decay.
Compact SU(N), finite-range Wilson conditionals and bounded local functions
fit these hypotheses. The generalized block theorem is a useful prospective
replacement for single-link comparison, but its coupled block kernels and
weighted influence condition must be proved for the actual gauge model.
It does not establish them at weak coupling. This is a reusable comparison
theorem, not an imported numerical contraction constant or physical-time gap.

**Chatterjee, arXiv:2006.16229v5; CMP 385 (2021).** Read §2.1,
Definitions 2.1/2.3 and Theorems 2.2/2.4, plus the opening of §12, in the
[primary PDF](https://arxiv.org/pdf/2006.16229v5).
Theorem 2.4 requires exponential correlation decay uniformly over every cube
and every boundary configuration, for bounded local functions, with fixed
group/coupling/dimension. It yields center symmetry and an area law for
irreducible representations acting nontrivially on the center. Its action
uses \(\beta_C\operatorname{Re}\operatorname{Tr}\), so here
\(\beta_W=N\beta_C\). This is a conditional confinement criterion at fixed
spacing. It neither derives the required boundary-uniform mixing at arbitrary
coupling nor identifies a continuum limit. The reviewed small-coupling
four-dimensional Dobrushin argument is compatible with its mixing hypothesis;
using it for an additional confinement claim would require a separate explicit
hypothesis match. [DOI](https://doi.org/10.1007/s00220-021-04086-y).

## Proposed bridges screened, not imported

**Faizal–Shabir, arXiv:2606.19362v1.** The
[593-page primary aggregate](https://arxiv.org/pdf/2606.19362v1) includes
the four companion papers. Read main Theorems 10.4, 10.8 and 11.1 with the
displayed proof passages, and Part 4's standing hypotheses (aggregate PDF
pages 110, 115–119, 127–131, 560–562). Main (11.1)/(11.3) assume
\(T'\ge\Pi T\Pi-R\), but (11.5) infers an upper bound. With
\(\Pi=I,R=0,T=\mathrm{diag}(1,1/2),T'=\mathrm{diag}(1,99/100)\), the
premise holds and the claimed consequence fails. Moreover, summable defects
need not have total size smaller than the initial gap; (11.7)'s asserted
uniform bound on \(e^{a_k\Delta_k}/a_{k+1}\) requires additional control.
Part 4 explicitly assumes scale-uniform clustering and continuum OS limits
with a gap. These passages cannot supply the missing bridge. This is a
specific failed inference, not a verdict on every argument in the aggregate.
The [exact independent check](review_massgap_block_literature_exact.py),
[predeclared criteria](review_massgap_block_literature_criteria.md) and
[results](review_massgap_block_literature_results.json) preserve the witness
and a correctly oriented comparison control (8/8 predicates).

**Kirk, Zenodo v4 (2 August 2026).** The
[v3 record](https://zenodo.org/records/21479499) points to
[v4](https://zenodo.org/records/21765806), which expands the claimed group
scope beyond SU(2). Read Theorem 1.1 and the stated proofs of 6.4–6.6,
6.10–6.13, 6.20–6.23 and 6.39–6.44 in the 118-page PDF. Its conclusion
concerns a directed continuum local curvature-jet theory. The bridge requires
uniform control of the complete reference, regular and irregular terms for
every exterior and weak depth; a finite one-pivot log-oscillation; exponentially
small separated multipivot interactions; and a joint Haar/optical forest
admission bound. These are new model-specific claims with substantial
upstream dependencies. Reading their statements and displayed proofs does
not validate that dependency chain. No identification with the lane's exact
soft-block source law was established. Consequently no theorem from this
manuscript is adopted here. The downloaded version is bound by SHA256
`b91c6c2b9ba7cd4d5476aa6a2e823569507682c24cf103933ff9f97c73260bed`;
it and its extracted text are research caches, not requested publication
attachments. They are kept outside the worktree in the local-only research
directory recorded in the relocation metadata.

**Ito–Seiler, arXiv:0901.4246v1.** Read the complete five-page
[primary discussion](https://arxiv.org/pdf/0901.4246v1).
Its §4 separates two obligations in a Migdal–Kadanoff-type route: actual flow
to strong coupling and a common interpolation parameter controlling twisted
and untwisted partition functions. The local implicit-function argument alone
does not give global continuation; the displayed scalar example terminates
before the desired endpoint. This is a useful warning when screening a
proposed bridge, not a no-go theorem for all RG mechanisms. I did not audit
the original Tomboulis construction or independently reproduce the paper's
decimation numerics; no current-global-status conclusion is based on them.

**Faria da Veiga–O'Carroll, arXiv:2509.03513v1.** Read the abstract,
introductory scope and action/Hilbert-space setup through §2 in the
[primary text](https://arxiv.org/html/2509.03513v1).
This is a fixed-lattice charge-conjugation/correlation analysis. Its action
convention gives \(\beta_W=2N\beta_{paper}\). The scanned introductory
claims do not constitute a continuum construction or a proved replacement
for the full physical Hilbert-space argument here. No theorem is imported;
the later spectral arguments and their cited constructive predecessors were
not independently audited in this pass.

## Search coverage and remaining proof obligations

The [literature bridge protocol](../../../../../../docs/ai_methodology/skills/physics-loop/references/literature-bridge-protocol.md)
was read at the pinned methodology revision. The coordinator restricted this
reviewer's writes to review-owned outputs, so this table is the scoped import
register; shared `ASSUMPTIONS_AND_IMPORTS.md` and `LITERATURE_BRIDGES.md` are
not edited.

| Source | Exact item | Role / import class | Affected claim | Derivation impact |
|---|---|---|---|---|
| Lüscher | Proposition 1 | Finite-transfer comparison; `literature theorem` | Finite positivity | Applicable comparison; no continuum closure. |
| Shen–Zhu–Zhu | Assumption 1.1, Corollary 1.6 | Alternative endpoint; `literature theorem` | Fixed-spacing local correlation gap | Applicable after convention/OS match; no continuum closure. |
| Rebeschini–van Handel | Theorem 2.4, Corollary 2.6 | Comparison machinery; `literature theorem` | Conditional sensitivity | Model-specific influence estimates remain required. |
| Chatterjee | Definition 2.3, Theorem 2.4 | Conditional confinement criterion; `literature theorem` | Optional fixed-spacing consequence | Not adopted as a new claim here. |
| Faizal–Shabir | Main (11.1)–(11.8), Part 4 H1–H5 | Failed import screen; `background context` | Proposed crossover | No derivation closure. |
| Kirk v4 | Selected §6 bridge statements/proofs | Unvalidated import candidate; `background context` | Proposed crossover | No derivation closure. |
| Ito–Seiler | §4 | Comparison-route caution; `background context` | Proposed crossover | No route-wide negative conclusion. |
| Faria da Veiga–O'Carroll | Introductory scope/setup | Comparator; `background context` | Fixed-spacing spectrum | No theorem adopted. |
| Osterwalder–Seiler; Seiler book | Bibliographic records only | Historical context; `background context` | Prior art | Unread theorem statements supply no closure. |

The established items are used as mathematical comparisons and do not provide
derivation closure for the continuum target. The screened proposals are used
as background context and do not provide derivation closure for the missing
physical-scale bridge. No empirical parameter or selector is imported.

The actual queries included the following families; this records search
coverage, not success at finding or validating a theorem for every phrase.

| Key block | Search terms / selected primary result | Disposition |
|---|---|---|
| Physical transfer, normalized Haar, all irreps | Lüscher; Osterwalder–Seiler; lattice spin-network/Peter–Weyl transfer | Lüscher finite theorem read; local normalization independently derived. |
| Local Perron ratio and rank-one covariance witness | “lattice Yang Mills ground state local ratio Perron eigenfunction covariance lower bound rank one operator” | No exact matching theorem established by this bounded query; the unit's direct proof remains load-bearing. No novelty claim follows. |
| Conditional TV, covariance and possible blocks | Dobrushin comparison, covariance oscillation, Rebeschini–van Handel | Exact single-site comparison hypotheses fit; general block theorem is a tool with unproved model-specific inputs. |
| Thermodynamic lattice gap | Shen–Zhu–Zhu, strong coupling, lattice physical-time mass gap | Established smooth-local correlation theorem applies after normalization; physical OS interpretation must be supplied separately. |
| Infinite-volume injectivity | “lattice gauge theory infinite volume transfer matrix injective strictly positive local finite energy Peter Weyl” | No substitute theorem validated; the supplement's all-boundary tilt/Fubini/martingale proof is required. |
| Continuum, crossover, exact RG | uniform/block/crossover queries; Faizal–Shabir, Kirk, Tomboulis/Ito–Seiler | No usable theorem was validated that discharges this lane's actual bridge. This is not a claim that every route or publication has been exhausted. |

Osterwalder–Seiler, [Annals of Physics 110 (1978), 440–471](https://doi.org/10.1016/0003-4916(78)90039-8),
was located on the publisher site, but only its abstract/bibliography was
available in this pass. Seiler's
[Lecture Notes in Physics 159](https://doi.org/10.1007/3-540-11559-5)
was identified bibliographically, not read. Neither supplies an exact theorem
import in this report. Lüscher and the fully stated SZZ result give the
applicable transfer/strong-coupling comparisons without pretending that these
unread sources were checked.

The still-needed physical estimate concerns the **same** continuum existence
hierarchy and complete source algebra: a common positive rate in physical
time, cutoff/volume-independent prefactors and onset, and nonzero finite-energy
spectral content. A fixed-spacing theorem, a stochastic mixing inequality,
or a source-free effective action cannot by itself provide these. A block
approach must control actual physical transition kernels on blocks of fixed
physical size, retaining all boundary sectors and all conditional source
terms. A coarse Wilson-looking action is not an identity with the actual
soft-block output.

## Retrieval limitations and preserved evidence

The arXiv HTML endpoints for 2204.12737v3 and 2606.19362v1 returned 404;
the PDFs were readable. Two initially guessed Project Euclid URLs with the
wrong identifier `1103900989` failed; the original DESY scan was then found
through its primary catalogue. The Hasselt Part 4 record returned 503, but
its relevant text was read in the arXiv aggregate. The Zenodo PDF URL produced
a web-tool Unicode-decoding error. Python's first direct retrieval failed
certificate verification before creating a file; ordinary `curl` with its
normal certificate verification retrieved the exact file successfully. Text
was extracted with `pypdf` because `pdftotext` was absent. These are retrieval
limitations, not failed mathematical claims. The manifest records the local
PDF/text hashes and the precise selected reading coverage.

A later hash-capture retrieval of the DESY URL returned a 248-byte HTML
challenge despite HTTP success; its bytes are preserved and explicitly
classified as a failed PDF capture. The Lüscher reading above used the
web tool's readable original scan, not that HTML response. Five versioned
arXiv PDFs were captured and validated as PDFs in the same hash-capture pass.
