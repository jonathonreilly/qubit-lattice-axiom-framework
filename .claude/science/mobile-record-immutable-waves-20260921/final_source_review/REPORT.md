# Immutable-wave publication source review

Date: 2026-09-21. This is scientific source scrutiny, not an audit, retention,
landing, or axiom-adoption decision. The complete 482-line note and complete
218-line runner were read. The four prior independent capsules were verified
and their applicable arguments compared with the publication proofs.

**Result:** one narrow summary-scope correction is required. No unresolved
mathematical defect was found in the body theorems under their stated
hypotheses. In particular, the changed reverse-current Euler proof and the
single-current canonical projection used for fluctuations are valid; neither
requires assuming that a locally frozen context generator is reversible or
canonical-stationary.

## 1. Reviewed identities and the required correction

The frozen sources reviewed are:

| Source | SHA-256 |
|---|---|
| `docs/MOBILE_RECORDS_IMMUTABLE_CONTEXT_EXCHANGE_ACOUSTIC_LIMITS_BOUNDED_THEOREM_NOTE_2026-09-21.md` | `7b0ca5ba4add0790151beac085dee85c922f02db2b2f053b2b2421ac09d71b42` |
| `scripts/mobile_records_immutable_context_exchange_acoustic_limits_2026_09_21.py` | `bc0ec7d702f46f862464cbfc3f915fa77201878858ee9984620ede10b669cb8d` |

**Finding F1, note line 4, nonzero-pair hypothesis.** The machine-readable
`claim_scope` says the displayed feature "has one nonzero direction-independent
acoustic pair at every isotropic interior density". The supplied model permits
alpha=0; with that parameter and any positive floor all rates remain valid,
but J=0, A(k)=0 and all six Euler speeds are zero. The body correctly supplies
`alpha!=0` at lines 167-171. Carry that condition into the summary:

> ... has, for fixed alpha!=0, one nonzero direction-independent acoustic pair
> at every isotropic interior density, with four zero-speed modes.

The introductory prose at lines 19-22 should make the same condition explicit
if it is meant as a universal assertion about the parameter family. Keeping
alpha=0 as a valid degenerate control in the model and in the remaining
theorems is fine. No equation, proof, or runner implementation needs to change
for this correction. The independent checker includes the exact rank-zero
counterexample. This finding remains open for the reviewed source identity;
this report does not silently treat a proposed edit as already applied.

## 2. Generator, currents, spectrum and scope

The publication specializes the sealed general family to
`u=0, E=alpha/2, A=2, B=-3`. On an axis, the pair of single-site values (f,s)
is (0,0) at vacancy, (+/-1,-1) at the axial labels, and (0,2) at the other
occupied labels. The sealed sharp context bound is 8 before multiplication
by alpha/2. Thus |h|<=4|alpha|, and both rate floors in the note are sufficient.
The cubic torus N>=4 has distinct four-site footprints. Equal-label events
are null; unequal occupied labels really can swap. This latter assumption
is essential to the canonical count-sector connectivity used later.

Central exchange sends h to -h. The two implementations have c-c^edge=h.
Writing T(y,z)=f_y s_z+s_y f_z, which is symmetric in its arguments, the
periodic context sum reduces to translations of
T(x,x-1)+T(x,x+2)-T(x+1,x-1)-T(x+1,x+2), and vanishes pointwise.
Every homogeneous product is invariant, including boundary products as
finite-volume laws. This is global balance, not detailed balance. Joint
signed coordinate transformations preserve h: a reversed coordinate uses
the reversed word (Rr,Rb,Ra,Rl), reversing both the directed f and endpoint
difference signs. The stated larger signed-coordinate covariance is correct.

Under a product, endpoint symmetry cancels the exchange-symmetric part of
c in the mean current. The remaining h/2 gives

    J_a^i = alpha p_a [S_i f_i(a)+(s_i(a)-2S_i)g_i],
    J_0^i = -2 alpha p_0 S_i g_i,

with S_i=2rho-3q_i. This agrees with the sealed current after the parameter
substitution, for either sign of alpha and either rate implementation.
Summing the seven currents gives zero. Taking the appropriate six linear
combinations gives both vector and axis-occupation expressions in (2).
The use of product expectations is explicit and does not assume a closed
microscopic first-moment equation for an inhomogeneous law.

In chemical coordinates, J_i=partial_theta Psi_i and Psi_i=alpha S_i g_i.
Since partial_theta p=C, differentiating once more gives A_i C symmetric;
equivalently H A_i is symmetric, with H=C^{-1}>0 in the interior. This
verifies the nonlinear entropy identity needed by the Euler proof, rather
than inferring it merely from a balanced-state spectrum.

Putting r_i=q_i-rho/3 yields S_i q_i=rho^2/3-3r_i^2. Linearizing the full
six-field current at p_a=rho/6 therefore gives (3), including the two
independent r fields. For k!=0 and alpha!=0, the rank is two and

    c_s^2 = 4 alpha^2 rho^2(1-rho)/3,

with two longitudinal eigenvalues +/-c_s|k| and four semisimple zeros.
The two vector directions transverse to k and two trace-free axis-occupation
directions account for all four. Entropy symmetry excludes hidden Jordan
blocks in the stated interior. The three listed numerical speeds are correct.
At alpha=0 there are six zero eigenvalues; rho=0,1 are outside the interior
theorems. The exact nonlinear vector current on q_i=rho/3 contains
-3 alpha diag(g_i^2), so the stated nonlinear anisotropy limitation is correct.

The supplied alphabet, clocks, rates and formation scaling are consistently
declared additional assumptions. No quantum interpretation or derivation of
the framework's nearest-neighbor formation odds is smuggled into these
mathematical statements.

## 3. Reconstruction of the publication's Euler proof

The theorem fixes the rate floor and parameters, assumes a given C^2 periodic
solution on a finite interval with all seven probabilities uniformly positive,
and starts at relative entropy o(N^3). It proves entropy per volume uniformly
in time and empirical convergence at fixed times. The latter is weaker than,
and consistent with, the stronger smooth-test consequence in the sealed
independent report. No solution-existence or post-shock theorem is asserted.

The uniform seven-state product is exchange-invariant. The elementary jump
entropy inequality and floor yield the exchange dissipation in (7). For
each site the birth adjoint applied to 1 contributes beta at an occupied
state and -6beta at vacancy, so its upper bound is beta V, not 6beta V.
The resulting integrated dissipation budget is valid without assuming that
the evolving law is translation invariant or product. Zero probabilities
in the evolving law can be handled by positive-density regularization of
this finite-state inequality; the reference laws stay strictly positive.

For sufficiently large fixed blocks containing the footprint (l>=2 is
enough), internal unit adjacent transpositions connect every fixed-count
sector. Finite canonical Poincare constants therefore exist even though the
actual context generator with a frozen exterior need not preserve a
canonical law. The floor controls the unit-swap form; marginalization
contracts that form. Sectorwise Hellinger comparison gives the displayed
L1 estimate with its conservative factor, and translated-block overlaps
count each edge at most M times. Canonical sampling without replacement
has O(1/M) error for a fixed footprint. Disjoint current supports have
O(1/M) canonical covariance, and only O(M) pairs overlap. Normalization by
the number of valid anchors gives mean -J(q)+O(1/M) and variance O(1/M).
Combining these facts with the budget proves (8). Its constants may depend
on the fixed rates and profile, while the block constant is held fixed as
N first tends to infinity. No bound on the growth of that finite constant
is needed for the iterated limit.

The publication uses the adjoint route (9), whereas the earlier independent
Euler proof used a forward-current entropy route. I reconstructed the changed
step. With psi=dnu/dpi, the exact exchange adjoint is

    L*psi/psi = sum_e [c(eta^e) psi(eta^e)/psi(eta)-c(eta)].

Pointwise global balance cancels sum_e[c(eta^e)-c(eta)]. The swap ratio is
exp[(theta_y-theta_x).(xi_x-xi_y)], so its first-order term has the
**positive reverse current** c(eta^e)(xi_x-xi_y). Its homogeneous product
mean is **-J**. Thus the sign in the subsequent entropy cancellation is
correct. The accumulated Taylor error is O(V/N) after multiplying by N.
This identity was additionally checked exactly on all 2,401 configurations
of an inhomogeneous four-cycle, with nonzero adjoint values in 2,394 cases.

The reference derivative generated by uniform births is exactly beta p_0/p_a
at occupied a and -6beta at vacancy. This agrees pointwise with R*psi/psi,
so the reaction portion cancels without a reaction closure assumption.
The independent full four-cycle check also confirms this identity exactly.
For transport, theta_t=-sum_i A_i^T partial_i theta follows from H A_i
symmetry and the PDE. The block current's constant term is a periodic
derivative of Psi_i; its linear term cancels; bounded polynomial Hessians
leave the stated quadratic count error.

The Hoeffding tail with six components has the claimed factor 12 and
exponent -z/3. A coloring using O(M) colors followed by Holder gives a
fixed small exponential coefficient, independent of l, in (10). The
overlap factor cancels the M in the individual block tail. The local profile
variation contributes O(V l^2/N^2). The entropy inequality and Gronwall
then close with N first and l second. These estimates supply a genuine
local-equilibrium argument for the actual context rates, rather than importing
an endpoint-only theorem. The birth scaling beta/N in microscopic time is
essential and is stated consistently.

## 4. Reconstruction of the stationary fluctuation proof

Here beta=0, p is fixed and full support, the torus starts in the stationary
product, and T and each integer Fourier mode are fixed before N grows.
Equation (11) puts the supremum outside expectation. The joint claim is for
finitely many modes and times; it is not an assertion of path-space or
infinite-dimensional convergence. These quantifiers match the sealed proof.

For the actual nonreversible exchange process, S=(L+L*)/2 controls the
unit-swap Dirichlet form with the stated floor. Its kernel is precisely the
functions of global color counts. If F is centered in each sector, solving
-S u=F and adding the forward and time-reversed stationary martingales gives
2N integral F. Each martingale has second moment 2Nt D_S(u). The inequality
|M+Mhat|^2<=2|M|^2+2|Mhat|^2 gives the factor 2t/N in (14).
The martingales need not be independent and no strong sector condition is
being assumed. The displayed inverse-form variational normalization is correct.

The publication projects a **single** local current onto counts of a large
containing block instead of first spatially averaging currents as in the
sealed report. This simplification is valid. Its conditional residual is
bounded and centered when conditioning on the outside and block counts,
hence orthogonal to all global count functions. Conditional Poincare,
Cauchy-Schwarz over translates and an overlap count give (15). The size
of the block can be held fixed while N grows, making the resulting integrated
second moment O(A_l M/N) vanish.

For the slow conditional mean, uniform without-replacement comparison gives
hat j=J(q)+O(1/M). After subtracting J(p)+DJ(p)(q-p), the residual W has
**exact** mean zero and squared norm O(1/M^2): E hat j=J(p), E q=p,
and the fourth multinomial moment is O(1/M^2). At each stationary time,
residuals in disjoint blocks are independent and only O(M) translates overlap.
The normalized spatial residual thus has variance O(1/M). Time
Cauchy-Schwarz requires no temporal independence. The Fourier transform of
the block count field is an exact filter times Y_N, and its error is
O_K(l/N). Together these facts prove (16). This avoids the invalid
uniform-in-configuration spatial averaging bound at fluctuation scale.

Conservation with exp(-iK.x/N) gives N[exp(-iK_i/N)-1], with the negative
imaginary sign in (17). Exchange jumps have size O(1/(N sqrt V)) and total
rate O(NV), yielding a martingale bracket O(1/N). Variation of constants and
integration by parts against the cumulative current error turn (16) into
(11); only L2 bounds with the supremum outside the norm are used. Product
Lindeberg and Cauchy-Schwarz then give the finite-dimensional Gaussian and
two-time covariance statements. Conjugated modes pair equal integer modes,
nonconjugated modes pair opposite ones, with no fixed-mode aliasing for
sufficiently large N. A_i C=C A_i^T implies U C U*=C. The longitudinal
block has initial density variance rho(1-rho), vector variance rho/3 and
zero cross covariance, giving the coefficient and cosine in (13).

A fresh 24-state canonical generator check used the actual positive-part
rates, not a symmetric template. Its centered current has inverse-form
norm 10117279/40296960. At N=4 and t=2/7 the integrated-current second moment
computed from the complete matrix is approximately 0.01686645826975418,
below (2t/N)||F||_{-1}^2 = 0.03586686368968208. The generator, stationarity,
nonreversibility and inverse-form identity were checked in exact arithmetic;
only the matrix exponential for this finite-time comparison is numerical.
This is a finite control of normalization, not a proof by numerical examples.

## 5. Formation, executable coverage and evidence identities

The homogeneous product trajectory in Section 5 is exact: the conservative
generator annihilates every homogeneous product, and the independent births
move such a product along the displayed one-site trajectory. An initially
isotropic product remains isotropic, but the coefficients vary with density.
The reaction derivative is -beta 11^T in species coordinates and -6beta
on total-density perturbations. The note properly keeps that formal linear
response and the smooth-profile theorem separate from the stationary
fluctuation theorem, which excludes births. Fixed microscopic epsilon,
vanishing floors, growing time/mode lists and boundary densities are correctly
excluded from the asserted fixed-parameter limits. I did not access the
unrelated primary growing, native-formation, pressure-design or transverse
construction sources.

The complete runner was inspected, including its integer-scaled floor test,
both exact rate implementations, 24 seven-species product-current cases,
arbitrary-density symbolic entropy algebra, the full field transformation,
Fourier sign and slow-birth test. The floor-test integers are twentieths;
their reported physical floors are accurate. The symbolic Jacobian is
constructed from the species current before comparison with the acoustic
matrix, so the principal matrix check is not merely comparison of the target
with itself. The later characteristic-polynomial gate uses that already
checked matrix. The direct product-current gate includes a biased product,
which is necessary to expose the mean-subtraction mutation.

The cached 49-control baseline and seven mutations are source-bound to the
reviewed note and runner. Their full stdout/stderr records were read and
authenticated without repeating the full computations for additional PASS
counts. The mutation failures correspond to:

| Mutation | Checked failure |
|---|---|
| wrong_axis_feature | full all-density field matrix |
| drop_polarized_cross_term | periodic pointwise balance |
| omit_current_mean_subtraction | first biased product-current case |
| wrong_acoustic_dimension | full field matrix |
| discard_zero_modes | degree-six characteristic polynomial |
| reverse_fourier_sign | configuration/current Fourier drift identity |
| fast_birth_scaling | accelerated single-site birth generator |

The cross-term mutation has an empty assertion message in the cached log,
but its source location and failure are unambiguous. The new independent
checker supplies a decisive explicit witness: on the four-cycle
(vacancy,vacancy,+e1,-e1), deleting that term gives sum h=1 instead of zero.
More descriptive diagnostics would be useful maintenance, but no correctness
change is required for this already documented control. These finite gates
do not mechanically test the entropy proof or the fluctuation replacement
theorem, and the note correctly says so.

The four capsule report hashes are:

| Independent report | SHA-256 |
|---|---|
| context exchange | `277ba40b64842d128a2e46ca7bd468a7efc7c4d401e629648d440588e7784713` |
| context Euler | `60aaef142f97aea228be967a711880c5272328e5173d6c8df8c033176605a1e3` |
| axis-balanced context | `b9cedcafccb48dfcd2503e5f00569a547288d4dcef0fb7dfca832565aec8f7cf` |
| stationary fluctuations | `772046745ac814c32adcd8f36e3c8415ddf4a3a4b37435e8992441c6c8d5be68` |

Running the supplied read-only `verify_capsules.py` returned **four capsules,
41 sealed artifacts and 15 dependency links verified**. Its SHA-256 is
`5530dab3defe1ea5738c25223b6529a08ff8398337df5ba6fbe5581f998ebedb`.
The standalone readable report copies match their archives. Earlier raw
failures and interrupted attempts remain inside the unchanged capsules.

Reproduction within this directory:

    OPENBLAS_NUM_THREADS=1 python3 selective_check.py > RUN.log 2>&1

The selective run completed once without failures; all raw output is in
`RUN.log`, byte-identical to `RESULTS.json`. There are six exact mathematical
controls, one numerical complete-generator comparison, and ten cached-evidence
identity/coverage controls. The supplied capsule verifier output is preserved
separately in `CAPSULE_VERIFICATION.log`. The selective checker additionally
uses SciPy for its matrix exponential; Python and library versions are in
the full log. An initially truncated display of
prior report excerpts was repaired with targeted complete reads; no truncated
display was treated as verification. No full baseline or mutation rerun was
needed, and no new literature theorem was imported. The cited literature
remains methodological background rather than a substitute for these proofs.

The adjacent seal records complete hashes for all review artifacts and the
reviewed sources, capsule archives, provenance/cache records and relevant
instruction snapshots. Only this review directory was written. No note,
runner, graph, earlier evidence, prompt, Git state, PR, or audit status changed.
