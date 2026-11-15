# Infrared construction attempt: the full finite-volume transfer and exact soft-loop transport

Author checkpoint, 29 October 2026. **The physical mass gap remains open.**
This unit derives an actual gap lower bound for the full finite-spatial-volume
Wilson transfer operator, including its spatial interaction and gauge
projection. Its bound loses uniformity with volume. A separate calculation
of the actual normalized soft kernel identifies precisely which fine-field
correlations survive into coarse Wilson loops. Neither calculation supplies
the missing infrared estimate on the continuum trajectory.

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
reachability_to_target: supports
conditional_surface_status: null
independent_review: pending
```

The target is [MASS_GAP_TARGET.md](MASS_GAP_TARGET.md), including its clarified
common physical rate and cutoff/volume-independent prefactor **and onset time**.
The strengthened target's SHA256 is
`105440c10b9a2fc91b2be366f439053de05fd3d3497596f8f28993b0fe42de7b`;
the original target at `9761471` remains in Git. The target group is SU(N),
N>=2. Section 2's explicit kernel filtering is restricted to SU(2); it is not
an extension to all SU(N), much less every compact simple group.

## 0. Contract, premises and source identity

The worktree baseline is `75cdf2dd1411c2d7d89c52871f84154ba0146ba4`.
Methodology and prior-art searches use current main
`ca2bc7ddf64790da96cd43d42017d000fbfe4808`, fetched by the coordinator.
The coordinator holds the cooperative lock, owns the shared proof, commits
and PR #10114. This worker writes only this note and `checks/mass_gap_construction_*`.
A manifest binds exact source bytes and the read scopes; unreviewed recent
residual-vertex and source-return continuations are not premises here.

**Allowed input.** This is constructive mathematics for the supplied Wilson
model in [PROOF.md, Setting S1-S3](PROOF.md) and the supplied normalized
soft kernel in [its Decision 4/D4-norm](PROOF.md). The normalized joint-chain
identity is also explicit in [HIST.md, sections 0 and 2](HIST.md). It is not a derivation of the action from the
repository's ontology. The physical spacing is the supplied regulator
spacing a=L^-K; it is never replaced by a fixed Planck lattice. Current-main
primitive registry and its three source notes were inspected: units, kinetic
form and pointwise realization supply none of the infrared estimates needed
here. No observed mass, fitted coupling, new axiom or primitive enters.

| Input | Role and boundary |
|---|---|
| Compact SU(N), normalized Haar measure, Wilson beta>0 | Supplied mathematical model; all finite-volume inequalities below follow from this action |
| Finite cubic spatial graph and nearest-neighbor Euclidean time, spacing a>0 | Regulator convention; not yet a continuum hierarchy |
| Compact self-adjoint spectral theorem; Peter-Weyl decomposition of L2(SU(N)) | Standard mathematical tools, with the used hypotheses checked below |
| S4' path means and D4 normalized soft kernel | Supplied exact RG kernel; its strength lambda=kappa/g_i^2 is not the Wilson beta |
| Complete reconstructed local algebra, continuum/volume limits, renormalized source bounds | Still-open target obligations; not used to prove a finite result |

**Prior-art sweep.** Searches on main used `Dobrushin`, `Doeblin`,
`strong.coupling.*cluster`, `transfer.operator.*mass.gap`, their reversed
word order, and matching filenames. The matching current-main notes read were
[constrained-fiber Dobrushin control and raw unit directions](../../../../../docs/WILSON_STAGGERED_CONSTRAINED_FIBER_DOBRUSHIN_AND_RAW_RG_UNIT_DIRECTIONS_BOUNDED_THEOREM_NOTE_2026-07-12.md),
[raw-action Hessian decay](../../../../../docs/WILSON_STAGGERED_RAW_CONSTRAINED_ACTION_HESSIAN_DECAY_BOUNDED_THEOREM_NOTE_2026-07-12.md),
[native coefficient-transfer strong-coupling gap](../../../../../docs/NATIVE_GAUGE_TRANSFER_STRONG_COUPLING_GAP_NARROW_THEOREM_NOTE_2026-06-12.md),
and [fixed-lattice gap scope](../../../../../docs/FIXED_LATTICE_GAUGE_EXISTENCE_STRONG_COUPLING_SCOPE_NOTE_2026-06-09.md).
These links locate the source notes; the manifest binds the exact main
revision inspected. They are prior-art and endpoint context, not hidden
premises supplying the present target.
The checked constrained-fiber and native-transfer ledger rows are currently
unaudited; no retained premise is imported from them. The first pair already
contains small-beta Dobrushin covariance machinery and raw-map unit directions.
The native-transfer note concerns coefficient packets and explicitly excludes
the full spatial Wilson environment. The fixed-lattice note supplies only
one-plaquette diagnostics. Their standard endpoint machinery is not claimed
as a new discovery. Section 1 instead constructs the actual finite Wilson
transfer including that environment; section 2 uses this lane's different,
normalized S4' soft kernel. No global novelty claim is made.

The primary literature check read the abstracts of
[Osterwalder–Seiler (1978)](https://doi.org/10.1016/0003-4916(78)90039-8),
[Lüscher's transfer-matrix paper](https://doi.org/10.1007/BF01614090), and
[Shen–Zhu–Zhu](https://arxiv.org/abs/2204.12737).
They establish prior art for lattice positivity and strong-coupling analysis;
only abstracts were inspected and no uninspected theorem is used as an input.
The finite derivations below are supplied explicitly.

## 1. Direct route: construct the actual finite Wilson transfer operator

### 1.1 The spatial interaction and gauge projector are retained

Let Gamma be a finite periodic three-dimensional cubic lattice with side at
least three, positive-oriented spatial edges E_s, and spatial plaquettes P_s.
Set n_s=|E_s| and X=SU(N)^(E_s), with product normalized Haar measure dU.
A spatial gauge transformation h=(h_x) acts by
`(h.V)_(xy)=h_x V_(xy) h_y^-1`. Let P be Haar averaging over all h, the
orthogonal projection onto the complete gauge-invariant Hilbert space
H_inv=L2(X)^gauge. All invariant functions are included, not only a plaquette
source sector.

Write w(W)=N^-1 Re tr W and

    A_beta(U) = exp[-(beta/2) sum_(p in P_s)(1-w(U_p))],
    k_beta(U,V) = product_(e in E_s) exp[beta w(U_e V_e^-1)],
    K_beta(U,V) = integral dh k_beta(U,h.V),
    T_beta(U,V) = A_beta(U) K_beta(U,V) A_beta(V).        (1)

Integrating the temporal link at each vertex between two adjacent slices
gives the integral in K_beta. Splitting each spatial plaquette weight equally
between the adjacent slabs gives A_beta on each side. Thus the product of
(1) around a finite time circle is exactly the Wilson integral, apart from
the field-independent exp(-beta n_s) per temporal layer omitted in k_beta.
That factor cancels from every eigenvalue ratio. No temporal gauge fixing or
Faddeev-Popov determinant is required for this derivation.

The operator with kernel k_beta commutes with simultaneous spatial gauge
transformations, since each U_e V_e^-1 is conjugated at its initial vertex.
Consequently K_beta=k_beta P=P k_beta, and T_beta=A_beta k_beta P A_beta.
A_beta is gauge invariant. K_beta and T_beta are real symmetric kernels.

**Positivity and injectivity.** On one link,

    exp[beta w(W)]
      = exp[(beta/(2N))(chi_f(W)+chi_fbar(W))]
      = sum_R c_R(beta) chi_R(W),   c_R(beta)>=0.       (2)

The exponential series consists of tensor-product characters with
nonnegative multiplicities and positive coefficients. It converges uniformly
on SU(N). Every irreducible representation occurs in a tensor power of the
fundamental or its conjugate; for beta>0, c_R(beta)>0. In the Peter-Weyl
matrix-coefficient basis, convolution by (2) has eigenvalue c_R/d_R>0.
The dimension divisor is required: c_R/c_trivial alone is not the normalized
physical convolution eigenvalue. Products of links preserve positivity and
injectivity. Since P commutes with k_beta, T_beta is positive semidefinite on
L2(X), and is injective on H_inv: for nonzero invariant f,

    <f,T_beta f> = <A_beta f,k_beta A_beta f> > 0.       (3)

A_beta is continuous and strictly positive on the finite compact X. The
continuous kernel makes T_beta compact. Moreover, since -1<=w<=1,

    exp(-beta n_s) <= K_beta(U,V) <= exp(beta n_s).     (4)

The kernel T_beta is strictly positive everywhere. Its top eigenvalue
lambda_0 is positive and simple with a continuous strictly positive
normalized eigenfunction psi_0. For completeness: compactness gives a
maximizer of the Rayleigh quotient; replacing a maximizer by its modulus
cannot lower the quotient, and strict kernel positivity excludes sign
changes at the top. Its image under T is strictly positive. Two linearly
independent top eigenfunctions could be made orthogonal, contradicting this
strict positivity. The same argument applied to phase yields simplicity
over C. Gauge covariance makes psi_0 invariant.

Thus T_beta/lambda_0 defines, on H_inv, the actual finite-spatial-volume
Hamiltonian

    H_(a,Gamma) = -a^-1 log(T_beta/lambda_0).            (5)

It is nonnegative and self-adjoint by spectral calculus. Injectivity for
beta>0 makes (5) densely defined. Multiplication of psi_0 by continuous invariant functions is dense in
H_inv, because psi_0 and its reciprocal are bounded on finite X. The finite
observable construction therefore reaches the complete invariant space. It
contains nonconstant loop functions, hence a nonzero excited sector. Compactness and
injectivity give positive non-top eigenvalues, hence finite excited energies.
At beta=0 the transfer has rank one and this last conclusion does not hold;
beta=0 is excluded from the finite-gap assertion.

### 1.2 An explicit all-sector finite-volume gap

Define Z_A=int A_beta(V)psi_0(V)dV and the probability measure

    nu(dV) = A_beta(V)psi_0(V)dV / Z_A.

The ground-state transform of the normalized transfer is the Markov operator

    (P_0 f)(U) = [lambda_0 psi_0(U)]^-1
                 int T_beta(U,V)psi_0(V)f(V)dV
               = int K_beta(U,V) f(V)nu(dV)
                   / int K_beta(U,W)nu(dW).            (6)

Its invariant reversible measure is pi(dU)=psi_0(U)^2 dU. From (4), for
every U and measurable B,

    P_0(U,B) >= epsilon_Gamma nu(B),
    epsilon_Gamma = exp(-2 beta n_s).                  (7)

This uses the full normalized denominator and the actual psi_0. It does not
assume that the vacuum is constant, ignore A_beta, or identify nu with pi.
Writing P_0=epsilon_Gamma nu+(1-epsilon_Gamma)Q_U gives, for real bounded f,

    osc(P_0 f) <= (1-epsilon_Gamma) osc(f).             (8)

Every nonzero eigenfunction phi of the compact T is continuous; psi_0 has a
positive minimum on finite X, so f=phi/psi_0 is bounded. For a non-top
eigenfunction, f is nonconstant. Its eigenvalue equation and (8) imply

    0 < lambda/lambda_0 <= 1-exp(-2 beta n_s).

Complex eigenfunctions can be replaced by real and imaginary parts because
the operator is real and self-adjoint. Its entire nonzero spectrum is covered
by eigenvectors. Therefore

    spec(H_(a,Gamma)) subset {0} union [m_(a,Gamma),infinity),
    ker H_(a,Gamma) = span{psi_0},
    m_(a,Gamma) = -a^-1 log[1-exp(-2 beta n_s)] > 0.    (9)

This is an actual bound derived from the repository's action for **every**
finite Gamma, a>0, beta>0 and N>=2. It contains the spatial magnetic factor,
temporal gauge average and all invariant Hilbert-space sectors. It is a
finite-volume construction, not MG1 on R4.

For any centered finite-volume vector v, (9) gives
`0<=<v,exp(-tH)v><=||v||^2 exp(-m_(a,Gamma)t)` for all t>=0.
For lattice time translates one uses t in a times the nonnegative integers;
the spectral semigroup defines the other t. This bound is for the ground
state (equivalently the infinite-time limit at fixed spatial volume).
Identifying it with the target's common finite-torus/continuum hierarchy,
with uniform prefactors and a common onset t_F, is a separate obligation.

### 1.3 The attempted uniformity step fails at an explicit inequality

For a cubic spatial torus with n sites per side, n_s=3n^3. The minorization
constant in (7) is exp(-6 beta n^3). At fixed beta,a>0, the right side of (9)
tends to zero as n tends to infinity. This is a statement about **this lower
bound**; it is no upper bound on the actual gap. At fixed physical spatial
size R=na, the same estimate is

    -a^-1 log[1-exp(-6 beta (R/a)^3)],                 (10)

which also tends to zero as a tends to zero for beta bounded below by a
positive constant. No claim about the unproved actual beta trajectory is
needed to see the lack of a uniform estimate.

The tempting attempted replacement, “the independent-link kinetic gap
survives multiplication by the positive magnetic factor,” is false as a
general operator inequality. Let

    k = [[1,r],[r,1]], 0<r<1,
    K = k tensor k,
    A = diag(a0,1,1,a0),  a0>1.

K is positive and has nontrivial/top ratio (1-r)/(1+r). The antisymmetric
vector on the first and last coordinates of AKA has eigenvalue
`a0^2(1-r^2)`. As a0 tends to infinity the top eigenvalue divided by a0^2
tends to 1+r^2, so the ratio tends to (1-r^2)/(1+r^2), strictly larger.
Hence the energy gap decreases under this positive multiplier. The runner
checks a finite declared a0, not only this limit. This is a finite two-spin
operator control, not an SU(N) counterexample or an argument against a
Yang–Mills mass gap.

A local, volume-independent estimate for the actual Doob kernel, or an
appropriate block comparison exploiting its Wilson magnetic factor, would
replace (7). We have not proved it. Stating that replacement as a uniform
spectral-gap inequality would merely restate the physical task and is not a
near-completion claim.

## 2. Distinct route: exact transport through the normalized S4' soft kernel

### 2.1 The SU(2) first moment has no unproved RG input

At one actual soft step, put lambda=kappa/g_i^2>0 and use
[PROOF.md, Decision 4](PROOF.md)'s exact path mean

    M_c(U) = (4! L^4)^-1 sum_(sigma,y) T_y^sigma(U),
    k_lambda(V_c;M_c)
      = exp[lambda w(V_c^-1 M_c)] / Z(lambda,M_c).      (11)

The exp(-lambda) in the printed action cancels exactly against its same
factor in the normalizer. Under the normalized joint measure
`mu_beta(dU) product_c k_lambda(V_c;M_c(U))dV_c`, the original U marginal is
exactly the Wilson law. The V_c are independent conditional on U. No
small-field indicator, selected history or restricted chart is used in (11).

For SU(2), write matrices as real quaternions. A convex mean of SU(2)
matrices has M=rW with 0<=r<=1 and W in SU(2) when r>0. At r=0, M=0.
Let

    Z(z) = integral_SU(2) exp[z w(V)]dV
         = sum_(k>=0) z^(2k)/(4^k k!(k+1)!)
         = 2 I_1(z)/z,
    b(z) = Z'(z)/Z(z) = I_2(z)/I_1(z).                (12)

The continuous values at z=0 are Z(0)=1 and b(0)=0. The series follows from
Haar SU(2)=uniform S3 and `E[w(V)^(2k)]=Catalan(k)/4^k`; odd moments vanish.
Rotational symmetry in the three vector quaternion coordinates gives

    E[V_c | U] = b(lambda r_c) W_c
               = f_lambda(r_c) M_c,
    f_lambda(r) = b(lambda r)/r,
    f_lambda(0) = lambda/4.                            (13)

The expression f_lambda(r)M is regular at M=0. No polar-frame derivative is
used. In particular

    f_lambda(r) = lambda/4 - lambda^3 r^2/96
                  + lambda^5 r^4/1536 + O(lambda^7). (14)

The quotient in (12), rather than Z' alone, is load-bearing. All displayed
series remainders are uniform for r in [0,1] and lambda in a fixed small
complex disk: for |z|<=1,
`|Z(z)-1|<=exp(1/4)-1<1`, so Z is nonzero there and Cauchy bounds apply.
Equations (12)-(13) hold for every real lambda>=0, beyond that series disk.
For a negatively oriented link and real lambda,
`E[V_c^(-1)|U]=f_lambda(r_c) M_c^dagger`. In (15)-(18) the orientation
notation means `M_c^(+)=M_c` and `M_c^(-)=M_c^dagger`, never the inverse
of the generally nonunitary mean. This includes M_c=0. In the small
complex-lambda disk the analytic continuation uses the same holomorphic
coefficient f_lambda(r_c) multiplying M_c^dagger; it does not conjugate
f_lambda or lambda. The adjoint acts only on the fixed real-field matrix M_c.

### 2.2 Exact disjoint-loop correlations expose the unclosed infrared input

For a simple oriented coarse loop C using each unoriented edge at most once,
let W_C(V)=w(product_(c in C) V_c^(orientation)). Set

    B_C(U) = [product_(c in C) f_lambda(r_c(U))]
              w(product_(c in C) M_c(U)^(orientation)).             (15)

Conditional independence and linearity of trace give

    E[W_C(V)|U] = B_C(U).                                            (16)

For two loops C,D with disjoint coarse-edge sets, the same independence gives
the exact identity for the actual Wilson prior at any finite beta and volume,

    Cov_(mu_beta K_lambda)(W_C,W_D) = Cov_mu_beta(B_C,B_D).           (17)

Disjointness is only of the coarse random links. Their fine path footprints
may overlap; that dependence is retained on the right. For simple plaquettes
P,Q define X_P(U)=w(product_(c in P) M_c(U)^(orientation)). Equations
(14)-(17) imply the exact Taylor-coefficient identity

    [lambda^8] Cov_(mu_beta K_lambda)(W_P,W_Q)
        = 4^-8 Cov_mu_beta(X_P,X_Q),                                (18)

and a uniform O(lambda^10) remainder for fixed finite loop lengths. Uniform
here means independent of volume, beta and fine separation for the bounded
coefficient calculation; it does **not** supply decay in separation.
X_P is a finite sum of fine Wilson-loop traces, with the actual S4' contour
weights and orientations. It is gauge invariant, since each M transforms at
the two coarse roots. Thus (18) identifies a concrete gauge-invariant
correlation that a proposed soft-noise crossover must actually estimate.

Small lambda suppresses its amplitude, not its separation dependence. Also,
changing the algorithmic lambda is not a proof that Wilson beta flowed to a
small effective value. The actual weak-coupling construction takes
lambda=kappa/g_i^2, generally large; (18) is a controlled endpoint probe of
the exact kernel, not extrapolation of a weak-coupling beta function.

### 2.3 Positive-noise control, all products, and the missing source term

There is a useful exact control against deriving clustering from (11) alone.
Choose two disjoint coarse plaquettes at any separation. In one center-valued
coarse background set their loop signs both +1; in another set them both -1.
Such backgrounds exist by choosing one distinct edge in each plaquette.
Mix the two configurations equally and average each over the coarse gauge
group. Both loop signs remain gauge invariant.

These inputs can be realized by an actual fine lift for the S4' path means:
put identity on every link internal to each fine block and put the chosen
coarse link V_c on every fine link crossing its corresponding block face.
Every in-block axial path is identity, and each straight segment of length L
crosses exactly that one face. Thus T_y^sigma=V_c and M_c=V_c for every c.
Averaging the lift over the full fine gauge group induces the stated
coarse-root averaging and preserves the loop signs by covariance of M_c.
This lifted prior is singular and **is not** the Wilson measure.

For this control, r_c=1 and (15) gives the two conditional plaquette means
as the common random sign times b(lambda)^4. Therefore

    Cov(W_P,W_Q) = b(lambda)^8 > 0     for every lambda>0,             (19)

independently of their separation. To see strict positivity directly, the
symmetric Haar scalar density gives
`Z'(lambda)=E[x sinh(lambda x)]>0` for lambda>0. Equation (19) refutes only
a proposed implication from normalized soft noise plus gauge covariance
alone, not a Wilson-specific RG crossover theorem. It leaves that theorem
open and identifies the correlations it must use.

Repeated-link products require higher conditional moments. They cannot be
obtained by multiplying (13): at lambda=0, for one link,
`E[w(V)^2]=1/4` whereas `E[w(V)]^2=0`. More generally, in real quaternion
coordinates v in S3 and m for M,

    E[v_(a1)...v_(an)|m]
      = [partial_(b_a1)...partial_(b_an) Z(|b|)] / Z(|b|)
          evaluated at b=lambda m.                                (20)

The radial Z series in (12) makes (20) regular at b=0. It computes every
finite polynomial product, including repeated links, without dividing by a
polar radius. Linkwise use of (20) supplies all such finite forward images;
density follows for continuous local functions by polynomial approximation
on compact SU(2)^E. This is **forward** transport from coarse observables to
fine functions. It is not a bounded inverse or a proof of the required
fine-to-coarse source representation.

For any bounded fine local F_1,...,F_n, the exact source-dependent weight is

    W_lambda(V;J) = integral dU exp[-S_beta(U)+sum_j J_j F_j(U)]
                           K_lambda(V|U),
    integral dV W_lambda(V;J) = Z_beta(J).                           (21)

At lambda=0, K_0=1 and W_0(V;J)=Z_beta(J), independently of V. The coarse
measure is then product Haar, but

    partial_(J_1)partial_(J_2) log W_0(V;J)|_(J=0)
         = Cov_mu_beta(F_1,F_2).                                   (22)

Thus a source-dependent field-independent term retains the full fine
correlation even at the exactly Haar endpoint. Only source-independent
vacuum constants may be dropped when evaluating source derivatives.
This does not allege that an existing lane dropped (22); it supplies a
specific control for an attempted infrared continuation. For lambda>0 the
corresponding exact identity is the law of total covariance,

    Cov_mu(F,G) = Cov_nu(E[F|V],E[G|V])
                    + E_nu Cov(F,G|V).                             (23)

Both pieces require control. A proof of clustering for nu alone is not a
producer for (23). The actual history-uniform return and source bounds in
[SOURCE_LOCAL_RETURN_ASTRA.md](SOURCE_LOCAL_RETURN_ASTRA.md) remain open at
their stated larger scope.

## 3. What was attempted, and the next constructive inequality

| Family | Actual attempt and result | Remaining obligation and strength |
|---|---|---|
| Full physical transfer operator | Constructed (1)-(9) from the finite Wilson action with the spatial factor and all invariant states | Replace volume-small (7) by a Wilson-specific local/block estimate; an assertion of a uniform gap alone would be target-equivalent once existence is supplied |
| Strong-coupling endpoint from direct one-link contraction | Prior-art check found existing Dobrushin bounds; the Wilson row majorant is at most 18 beta in d=4, useful only at small bare beta | Actual exact RG crossover to an endpoint with a uniform interaction norm and source remainder; this is a stronger sufficient package than a physical gap, and is not established |
| Soft-noise continuation with exact observable transport | Derived (12)-(23); computed the order-eight separated-loop coefficient and kept the source-only term | Prove physical-distance decay of actual Wilson covariances in (18)/(23), with common constants and all products; a single loop-sector estimate is weaker than the full target |

For the endpoint row, each four-dimensional link belongs to six plaquettes,
with three other links per plaquette. One changed neighboring link gives
mixed log-weight oscillation at most 4 beta per common plaquette. The
normalized likelihood-ratio bound therefore gives influence at most
tanh(beta) <= beta per incidence, and row sum at most 18 beta. This is the
existing small-beta endpoint estimate, not a new theorem. Increasing noise
alone was explicitly tried and fails to remove the unestimated Wilson
correlation. The direct transfer route is substantively different and gives
a real finite-volume gap, but compact positivity alone does not provide a
useful uniform constant. These outcomes do not rule out either route.

One useful next finite-volume statement is to prove a *local block
comparison* for the actual ground-state kernel (6), with constants tied to a
fixed physical block size ell rather than |Gamma|. The first new quantity to
estimate is the spatial dependence of the ground-state ratio in (6) when
external block data change. That ratio cannot be replaced by the bare local
Boltzmann factor. Even a conditional-mixing theorem for pi=psi_0^2 would
require a separate comparison to the physical operator P_0. Bounds for bare
single-link heat-bath dynamics concern stochastic time and do not establish
this physical-kernel estimate. We have not produced either comparison.

For the RG route, the concrete next calculation is the complete two-source
coefficient of the **actual** integrated weight at a fixed physical scale,
including the source-only contribution in (22), conditional covariance in
(23), and all history returns. A successful inequality must give, on the
same existence hierarchy,

    |C_F^(a,R)(t)| <= A_F exp(-m_* t),
    t_F <= t <= T_safe(R),

with m_*>0 physical, A_F and t_F independent of a,R, and T_safe(R) tending
to infinity. This is the target to derive, not an added assumption in this
note. The beta-flow continuation through the intermediate regime is also
unproved; the perturbative coefficient cannot be extended there by fiat.

No claim is made that the named open conditions are pairwise independent.
The endpoint crossover and source control can overlap in an eventual joint
construction. The current unit closes no MG0-MG5 target row.

## 4. Checks, scope controls and author disposition

Pre-stated criteria are in
[checks/mass_gap_construction_criteria.md](checks/mass_gap_construction_criteria.md).
The [runner](checks/mass_gap_construction_exact.py) and its
[preserved output](checks/mass_gap_construction_results.json) check exact SU(2) series, normalized
moments, the order-eight coefficient, oriented products, repeated-link
failure, the source-only term, finite Doob identities, and a finite-cycle
transfer implementation. They also test deliberate errors in normalization,
representation dimension, Perron factors, link count and electric-gap
inheritance. Neither finite quadrature nor a truncated character matrix is
used as proof of an infinite-volume assertion. The written arguments carry
the finite general statements. Independent review remains pending. The original frozen run passes 45 checks,
including 11 deliberate negative controls, with empty stderr.
Review found that two implementation mutations still passed those checks.
The [repaired run](checks/mass_gap_construction_results_v2.json) adds an
independently assembled coordinate-space Haar transfer comparison, passing
47 predicates with empty stderr. Both formerly surviving mutations now fail
the actual spectral-ratio and leading-eigenvalue comparisons; the
[repair record](checks/full_proof_massgap_checker_fix.json) preserves their
exact scripts and outputs. These remain finite implementation checks.
The first run
and its exact script are also preserved; the subsequent change evaluates
the very small minorization with `1-ratio > exp(-8 beta)` to avoid subtracting
exp(-64) from one in binary floating point. No scientific criterion changed.

**Negative-claim discipline.** This is a stretch attempt with an honest
residual, not a global no-go packet. N1 has three real families above, not
five, so the five-family packet gate is incomplete and no packet PASS is
claimed. N2 records no independent-wall count. N3's assumption scan leaves
the supplied Wilson action, soft kernel, finite geometry and mathematical
spectral tools explicit. N4 uses no previous no-go as a nonmatching witness.
N5's runner reports the actual resolution classes and marks the continuum
estimate unexecuted. N6's registry check finds no relevant convention that
supplies a dynamical decay bound. N7's strongest counter-route is a
Wilson-specific, gauge-invariant block comparison or exact RG crossover with
joint source transport; neither is ruled out. N8's closest prior raw-map
unit-direction result is on a different hard constraint and does not block
a rescaled soft action. The exact controls (19) and the two-spin matrix only
refute their explicitly stated universal inference, not Yang–Mills.

**Value/trace check.** The added content is the actual full finite Wilson
transfer bound, an explicit normalized SU(2) S4' loop-image formula, and the
specific source coefficient/term that a noise-based infrared argument would
otherwise lose. This is upstream support for MG1/MG2 and an attempted route
to their producer. It does not retire the uniform infrared input, promote
existence, or establish a continuum mass. A new spectral implication or a
new name for the terminal gap would add no further progress. After freezing
this unit, independent review should challenge the actual slab identity,
gauge projection, injectivity, minorization constant, SU(2) normalization,
source direction, and the limits of each control before further reuse.
