# Independent review of the Wilson local-block physical-time unit

29 October 2026. Reviewer: separate Astra/max context, same model family as
the authors. **Bounded scientific-unit disposition: supported within the
stated finite-volume and fixed-spacing strong-coupling scope.** No unresolved
mathematical defect was found in the claims reviewed below. This is not a
whole-proof, whole-PR, landing, audit-authority or continuum verdict.

```yaml
actual_current_surface_status: bounded-support
review_scope: frozen_local_block_unit_and_injectivity_supplement
independence: same_family_separate_context
continuum_existence: open
continuum_physical_mass_gap: open
MG_rows_closed: []
global_novelty: not_claimed
route_exhaustion: not_claimed
```

## Source binding and review boundary

The mathematical source was the complete
[local-block note](MASS_GAP_LOCAL_BLOCK_ASTRA.md), originally frozen with
SHA256 `f75e8cfc6f9e4310a9ba78ce7d8d53a6c729f4cac10599b430fb9234403c8d25`,
and the complete [injectivity supplement](checks/massgap_block_injectivity.md),
SHA256 `820bceb7c30ad7a4e42eb0733018923ace7bcd57023163fe7a639b3d74a02acf`.
The original [author manifest](checks/massgap_block_manifest.json) and
[freeze receipt](checks/massgap_block_freeze.json) have SHA256
`044391102b2468b76ee9583a5d08dbc2db24c77367076e6de7c97750d698026b` and
`cd3f60bcbb654a44dbb918b9091f4aa9c491be751a08042423a021e21f310665`.
They remain valid for the original source preserved at commit
`47a916398fb58231d809695485812faf25c70ce9`.

I reported one portability defect in the original note: an installed-skill
absolute path was its reader-facing methodology link. The coordinator's
[narrow repair receipt](checks/full_proof_massgap_block_link_fix.json) records
the replacement at `1d221a0063566d5270b60cc543690d7c4d8c68ba`. I read its full
diff and confirmed that only the installed-versus-repository wording/link
changed. The present note's SHA256 is
`0cdbfd18a97f6240b07f4a6047073fe6dc2abe2949af9ccb6f6bd191498bae3d`.
The installed and portable skill hashes correctly remain distinct. No
mathematical assertion or formula was changed, so this narrow re-review
extends the scientific disposition to the repaired bytes. The supplement
was unchanged.

The actual target is [MASS_GAP_TARGET.md](MASS_GAP_TARGET.md), SHA256
`105440c10b9a2fc91b2be366f439053de05fd3d3497596f8f28993b0fe42de7b`.
I read the complete [finite-transfer predecessor](MASS_GAP_CONSTRUCTION_ASTRA.md)
and [its review](REVIEW_MASS_GAP_CONSTRUCTION_ASTRA.md), but checked the
consumed mathematics rather than inheriting a review label. The governing
methodology was read at freshly fetched main
`ca2bc7ddf64790da96cd43d42017d000fbfe4808`; the installed physics-loop and
review-loop skills were also read. Portable entries are
[physics-loop](../../../../../docs/ai_methodology/skills/physics-loop/SKILL.md)
and [review-loop](../../../../../docs/ai_methodology/skills/review-loop/SKILL.md).
The [review manifest](checks/review_massgap_block_manifest.json) gives each
exact file hash, revision and actual reading coverage. Whole-file hashes
identify bytes; they do not claim whole-file reading where the coverage is
explicitly partial.

The [falsification criteria](checks/review_massgap_block_criteria.md) were
written after reading the proposed formulas and sources, before reviewer
computation and before reading the author runners. This is precomputation
declaration, not blind review. I used no workers, made no author-file edits,
and exercised no audit or landing authority.

## Independent analytic checks

### 1. Exact finite physical transfer and local ratios

The model is the supplied pure Wilson theory, \(N\ge2\), normalized Haar,
spatial cubic tori of side at least four, spacing \(a>0\), and
\(\beta=2N/g_K^2\). With \(w=\operatorname{Re}\operatorname{tr}/N\),
\(A=\exp[-(\beta/2)\sum_{p\ {\rm spatial}}(1-w_p)]\), and
\(k(U,V)=\prod_e\exp[\beta w(U_eV_e^\dagger)]\), the physical transfer
is \(T=A k P_{\rm gauge} A\). Gauge Haar is normalized; the projection
retains every invariant representation/intertwiner sector. No selected
Wilson-loop sector replaces the invariant space.

For an irrep \(R\), the one-link convolution multiplier is \(c_R/d_R\),
not \(c_R\). Expanding the exponential in fundamental and conjugate tensor
powers gives \(c_R>0\) for every \(R\) when \(\beta>0\). Thus unprojected
\(\widehat T=A k A\) is positive and injective at finite volume; it agrees
with \(T\) on invariant functions, while the projected operator annihilates
gauge-variant directions. The continuous strictly positive kernel gives a
simple positive Perron vector \(\psi\), which is invariant. Normalize
\(\int\psi^2=1\), and set \(u=A\psi\).

Changing a block \(B\) of \(b\) links affects exactly the touching magnetic
plaquettes. Pointwise comparison of the actual Perron equation gives

\[
 \left|\log\frac{(\psi/A)(U')}{(\psi/A)(U)}\right|\le2\beta b,
 \qquad
 \left|\log\frac{u(U')}{u(U)}\right|\le D_B:=2\beta(p_B+b).
\]

Consequently the \(\pi=\psi^2\) conditional density on \(B\), relative to
product Haar, lies between \(e^{-L_B}\) and \(e^{L_B}\), where
\(L_B=2\beta p_B+4\beta b\). These bounds are independent of spatial
volume and valid for each finite \(\beta>0\). They are local finite-energy
comparisons, not spatial decay estimates.

### 2. The centered one-step witness uses two different kinds of positivity

Let \(W\) be the normalized real trace of a simple loop supported on \(B\),
\(F=W-\pi W\), and \(v_N=\int W^2dU_B\). Schur orthogonality gives
\(v_2=1/4\); for \(N\ge3\), fundamental and conjugate are inequivalent,
so \(v_N=1/(2N^2)\). The normalized one-link multiplier is
\(r_f=c_f/(Nc_0)>0\), and \(\bar k_B W=\rho W\), with
\(\rho=r_f^b\). Since \(F\) contains only its constant and fundamental
loop components, the inverse needed here is well-defined on that finite
spectral span, even though the full inverse operator is unbounded.

Writing \(m=\pi W\), Cauchy–Schwarz in the \(\bar k_B\) quadratic form
gives

\[
 \bar k_B\succeq\frac{|F\rangle\langle F|}{m^2+v_N/\rho}
 \succeq\frac{|F\rangle\langle F|}{1+v_N/\rho}.
\]

This is an **operator** inequality. Its kernel remainder need not be
pointwise nonnegative. Tensoring with the positive exterior operator is
legitimate. In the resulting form the block integral is
\(b_F(Z)=\int u(U_B,Z)F(U_B)^2dU_B\ge v_N u_{\min}(Z)\).
Only at this later step does pointwise positivity of the exterior kernel
permit comparison with \(u_{\min}\). The denominator is at most
\(e^{2D_B}\langle u_{\min},\bar k_{B^c}u_{\min}\rangle\).
The common exterior factor cancels exactly, yielding

\[
 \langle F,P_0F\rangle_\pi
 =\frac{\langle uF,\bar k uF\rangle}{\langle u,\bar k u\rangle}
 \ge\frac{v_N^2 e^{-4\beta(p_B+b)}}{1+v_N/r_f^b}.
\]

For an elementary spatial plaquette, \(b=4\) and \(p_B=13\): four links
have sixteen touching-plaquette incidences, and the common plaquette was
counted four times. Thus the claimed exponent is exactly \(-68\beta\).
No full-volume minimum of \(u\) or \(k\) enters the result. Centering under
\(\psi^2\), rather than \(A\psi\), is essential. The all-beta statement
at this point is finite-volume with a volume-independent lower bound.

### 3. Open slabs, ground-state ratios and oscillation constants

Open temporal gauge is fixed recursively from the bottom slice. Haar
invariance and normalized gauge integrations leave the same Wilson
expectations on the invariant observable algebra. Spatial holonomies remain;
no periodic-time holonomy is erased. The exact slab weights are \(A\) at
both ends, \(A^2\) in the interior and \(k\) between consecutive slices.
Since \(A\) and \(1\) are invariant, \(T^n1=\widehat T^n1\). The finite-volume
Perron limit is uniform after one continuous-kernel smoothing step.

For \(R_n=\psi_n/A\), a bottom-link change introduces exactly one source
on the corresponding first-layer link,
\(H_e(V)=\beta[w(U'_eV_e^\dagger)-w(U_eV_e^\dagger)]\).
Its absolute size is at most \(2\beta\), but its **full oscillation** is
at most \(4\beta\). Integrating the two source derivatives gives the
mixed log-ratio as the double integral of \(\operatorname{Cov}(H_e,H_f)\)
in the actual interpolated slab.

For full oscillations and TV equal to half the \(L^1\) distance, a
log-likelihood range \(L\) gives TV at most \(\tanh(L/4)\le L/4\).
Normalization is included. The covariance bound is
\(|\operatorname{Cov}(f,g)|\le\frac14\sum_{ij}\delta_i f D_{ij}\delta_jg\).
The source proves this with an auxiliary single-site heat-bath generator and
integrates its oscillation semigroup. The auxiliary time is only a device
for a static covariance estimate; it is never equated with physical time.

The half-slab comparison matrix has spatial row sum \(12\beta\) and at
most two temporal neighbors of weight \(\beta\), hence \(14\beta\).
The resulting ground-state mixed ratio is bounded by
\(2\beta m_{ef}+4\beta^2D^+_{(e,1),(f,1)}\).
The actual unprojected Doob output conditional has density proportional to

\[
 A(V)\psi(V)\exp\!\left[\beta\sum_{e\in B}w(U_eV_e^\dagger)\right].
\]

Both the magnetic factor and the Perron factor must remain. The output
influence row is at most
\(q=12\beta+\beta^2/(1-14\beta)\), and a changed input link contributes
TV defect at most \(\beta\) at that same output link. Therefore one
**physical** transition contracts the summed link oscillation by

\[
 r=\frac{\beta}{1-12\beta-\beta^2/(1-14\beta)}.
\]

At \(\beta=1/32\), independently reduced rational values are
\(14\beta=7/16\), \(q=217/576\) and \(r=18/359\). The expressions are
increasing on the claimed interval, so \(0<r\le18/359<1\). Although the
unprojected kernel is useful for comparison, only its restriction to
invariants is identified with the physical \(P_0\).

### 4. Thermodynamic limit, full observable space and physical spectrum

The original four-dimensional Wilson specification has comparison row
\(18\beta<1\) throughout the claimed range. Finite-range comparison yields
boundary-uniform convergence of local marginals and a unique infinite-volume
Gibbs state. This includes spatial-torus/open-slab limits; the estimates do
not require choosing a favorable exterior field.

The local observable algebra includes arbitrary bounded gauge-invariant
local functions, intersecting loops, products and spin networks. It also
includes local observables containing temporal links. Finite matrix
coefficients are uniformly dense in each continuous cylinder algebra;
averaging over its incident gauge vertices preserves its finite support.
Cylinder approximation followed by gauge averaging gives density in the
entire invariant \(L^2(\pi)\), not only in a selected loop subspace.

Conditioning on a spatial slice separates the past and future nearest-time
interactions. Half-space uniqueness identifies their conditional laws and
gives a stationary reversible Markov transition. Positivity of the finite
transfer passes to invariant local cylinders and then to their \(L^2\)
closure. For every centered cylinder, the physical-time covariance bound
has an \(n\)-independent prefactor and rate \(r^n\). The spectral theorem,
nonnegative transfer spectrum and density therefore exclude spectral mass
in \((r,1)\) on the entire centered invariant space. This is not an inference
from a single Wilson-loop correlator.

For reflection through a temporal link, conditional expectation of a bounded
positive-half-space observable onto its first slice gives an invariant
\(f\in L^2(\pi)\), possibly nonlocal. The reflected form is
\(\langle f,P_\infty f\rangle\), and the OS map is \(f\mapsto\sqrt{P_\infty}f\).
Boundary cylinders are dense. Temporal-link observables inside a half-space
are included before conditioning; translating the reflection plane covers
any finite local support. The injectivity proof below makes the range of
\(\sqrt{P_\infty}\) dense in the full invariant slice space. No physical
observable sector is silently removed to make the Hamiltonian exist.

### 5. Supplement: infinite-volume injectivity

The finite-volume strict positivity theorem is insufficient by itself. I
checked each additional limiting step in the supplement:

1. The temporal-gauge half-space specification has row bound \(14\beta<1\)
   for **every** bottom field \(U\). Uniform comparison constructs a canonical
   half-space probability and its first-slice kernel \(Q_U\), with measurable
   boundary dependence. Stationarity, reversibility and positivity pass from
   the finite unprojected system. \(Q\) and the projected physical transfer
   agree only on invariants.
2. Changing finitely many bottom links \(B\) changes the half-space energy
   only by the bounded first-layer source \(H\). DLR plus uniqueness gives
   the exact identity
   \(Q_{U'}=e^H Q_U/(Q_Ue^H)\) for every such pair of boundary fields.
   Since \(|H|\le2\beta b\), the Radon–Nikodym ratio lies between
   \(e^{-4\beta b}\) and \(e^{4\beta b}\). The normalizer is essential.
3. The finite-block conditional Haar lower/upper bounds for \(\pi\) pass
   through finite-volume integral inequalities against nonnegative local
   tests, then through monotone classes/disintegration. They do not require
   a global density of \(\pi\) relative to infinite product Haar.
4. For \(F\in L^2(\pi)\) with \(QF=0\), stationarity supplies
   \(Q_U|F|<\infty\) almost everywhere. For a countable exhausting sequence
   \(B_j\), disintegration and the local Haar lower bound turn each exceptional
   \(\pi\)-null set into a Haar-null set of block modifications for almost
   every exterior. A **countable** intersection gives one common full-measure
   set. The proof never intersects null sets over all boundary fields.
5. At a fixed boundary in this common set, bounded tilt extends integrability
   to every block modification. Define the finite complex signed measure
   \(\alpha_B(dV_B)=e^{-\beta\sum_Bw(U_eV_e^\dagger)}
   E_{Q_U}[F\mid V_B]Q_U(dV_B)\). Its convolution with the product Wilson
   kernel vanishes Haar-almost everywhere and hence everywhere by continuity.
   Every tensor Peter–Weyl multiplier is nonzero. Uniform density of finite
   matrix coefficients then implies \(\alpha_B=0\), hence
   \(E_{Q_U}[F\mid V_B]=0\).
6. Martingale exhaustion under this fixed probability \(Q_U\) gives \(F=0\),
   \(Q_U\)-almost surely. Stationarity integrates that assertion to \(F=0\),
   \(\pi\)-almost surely. This proves injectivity on the full unprojected
   \(L^2\) and therefore on its invariant restriction. The argument does not
   claim a bounded inverse or a positive uniform lower spectral edge for \(P\).

The exclusion of \(\beta=0\) is real: the one-link kernel then has zero
nontrivial Fourier multipliers. Infinite-volume injectivity is established
analytically by this argument, not by the finite diagnostic matrices.

### 6. Exactly what the endpoint proves

At fixed \(a>0\), \(N\ge2\), \(0<\beta\le1/32\), define
\(H=-a^{-1}\log P_\infty\) on the full physical slice space. Positivity
and injectivity make this a densely defined self-adjoint Hamiltonian. Its
vacuum is unique. The one-step witness survives the local two-slice limit.
Because \(\operatorname{Var}_\pi W\le1\), its spectral measure has nonzero
mass at finite positive transfer spectrum. Thus the nonvacuum spectral
threshold is finite and satisfies

\[
 0<\frac{-\log r}{a}
 \le\inf\sigma(H|_{1^\perp})
 \le\frac{-\log\eta}{a}<\infty,
 \quad
 \eta=\frac{v_N^2e^{-68\beta}}{1+v_N/r_f^4}.
\]

This constructs continuous Hamiltonian time by functional calculus. It does
not restore continuum spatial rotations or establish a four-dimensional
continuum field theory. At fixed \(\beta\), the bounds scale as \(1/a\).
The witness is at shrinking time \(a\). The target requires a common physical
rate, uniform prefactor **and onset**, a complete common limiting source
hierarchy, and nonzero finite-energy continuum spectral content. No such
continuum conclusion follows from this endpoint.

## Independent computational evidence and all failed attempts

The [reviewer implementation](checks/review_massgap_block_independent.py)
was built separately around the non-Abelian quaternion group \(Q_8\), with
two vertices, three parallel links, three interacting two-link magnetic
loops, 512 link configurations and all 64 vertex-gauge transformations.
This is explicitly a finite analogue, not an SU(N) lattice approximation.
Its raw slab, full projector, magnetic Perron transform and exterior
interaction differ from the author's Z2/SU2-cycle diagnostics. It also
enumerates actual cubic-lattice incidences and checks rational endpoint
constants. The SU(N) variance identities are analytically derived above;
their rational substitutions in the code are not independent group integration.

The final [attempt 03 output](checks/review_massgap_block_attempt03.stdout.json)
records **112/112 predicates**, including **13 mutation predicates killed**.
Those 13 predicates represent eleven changed-formula/operator families; the
missing \(A\) and missing \(\psi\) changes each have both conditional and
stationarity checks, and the bad exterior matrix is a separate control.
The implementation was written before the author runners were read; the
last fixture repair described below occurred after that reading.

The mutations actually remove the magnetic weight, square the terminal
half-factor, halve the source oscillation, omit the tilt normalizer, use the
gauge projection as the all-boundary \(Q\), omit \(A\) or \(\psi\) from the
Doob output, change the centering law, replace the input sensitivity
\(\beta\) by \(\beta^2\), reduce the covariance factor from \(1/4\) to
\(1/16\), or replace the pointwise-positive exterior kernel by a PSD matrix
with negative entries. That last control explicitly separates operator
positivity from pointwise monotonicity.

| Attempt | Outcome | Interpretation |
|---|---|---|
| [01 source](checks/review_massgap_block_attempt01.py), [stderr](checks/review_massgap_block_attempt01.stderr.txt) | Parser rejected an unmatched bracket; no scientific checks ran. | Reviewer coding error, preserved before correction. |
| [02 source](checks/review_massgap_block_attempt02.py), [output](checks/review_massgap_block_attempt02.stdout.json) | 111/112; omitted-normalizer mutation survived at roundoff size. | The chosen bottom fields were gauge equivalent, so the true normalizer was one. This was a degenerate negative-control fixture, not a false tilt identity. |
| [03 source](checks/review_massgap_block_attempt03.py), [receipt](checks/review_massgap_block_attempt03.receipt.json) | 112/112; all 13 mutation predicates killed. | Changed the boundary pair from `((1,i,j),(-1,i,j))` to `((1,1,i),(-1,1,i))`, changing a loop invariant. The omitted-normalizer discrepancy became about 0.05435. No formula or tolerance was relaxed. |

The main residual tolerance was \(5\times10^{-11}\), PSD tolerance
\(10^{-10}\), and mutation threshold \(10^{-7}\), declared in the runner
before first execution. The inverse/recovery checks had their own declared
\(10^{-6}\) and \(5\times10^{-8}\) thresholds. Runtime and exact hashes
are preserved in each attempt receipt. These finite calculations cannot
certify SU(N) for all \(N\), thermodynamic limits, disintegration, martingale
convergence or continuum reconstruction.

I read both author runners and their criteria after writing the independent
implementation. The author's 108 main and 23 supplementary checks remain
author diagnostics; the coordinator owns their replay. Their reported count
is not added to the independent count or used as proof of a limit.

## Literature, procedural limits and open interface

The [primary-literature register](checks/review_massgap_block_literature.md)
records exact theorem statements/hypotheses read, action conversions,
retrieval failures and applicability. It identifies established finite
transfer, Gibbs comparison and strong-coupling correlation results; it also
screens proposed crossover imports with a separate exact falsification
check. No unread abstract is used as an established theorem. The literature
screen did not validate a theorem that supplies this lane's complete
cutoff-uniform physical-time/source bridge. This is a bounded search result,
not a global absence or route-exhaustion claim.

The [primitive registry](../../../../../docs/audit/data/axiom_premise_nodes.json),
[minimal axioms](../../../../../docs/MINIMAL_AXIOMS_2026-06-29.md),
[registry check](../../../../../docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md), and the
registered scale, kinetic-isotropy and realized-state notes were read at
the pinned governance revision. None is used to assume the missing
infrared dynamics. Here the Wilson action is an explicit mathematical model
hypothesis; no derivation of that model from ontology is asserted.

The source's two constructive mechanisms do not constitute the five-family
packet discussed in [no-go discipline](../../../../../docs/ai_methodology/skills/no-go-discipline/SKILL.md).
This review neither invents additional routes to satisfy a count nor
certifies a no-go/landing packet. Existing bounded repository notes were
read for exact overlap/scope, not treated as transitive proofs of their
unread dependencies.

The next unresolved mathematical consumer is an actual physical transition
comparison at fixed physical block size, or an exact RG transport into an
applicable endpoint class. Either route must retain every boundary sector
and the full conditional fine-source terms in the predecessor. A
source-free action, auxiliary heat-bath gap, finite-volume Perron gap, or
single nonzero witness does not discharge that consumer. **No MG0–MG5 row
closes from this unit.**

The [manifest](checks/review_massgap_block_manifest.json) and
[final receipt](checks/review_massgap_block_receipt.json) bind this review,
the successful and failed checker versions, source snapshots and read
coverage. Review files are frozen after final delivery.
