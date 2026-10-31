# WITNESS — a common-algebra witness contract

## Owner-decision summary

**Recommendation (ARGUED): choose `(A_e, F1, AF-e)`**, where `A_e` is the
separated, centred clover-field OS test hierarchy with `Z(a)=1`, `F1` means
all Hermitian scalar finite Wick polynomials, with finitely many derivatives,
in finitely many canonical free fields, and `AF-e` is the two-sided
short-distance property (E1) below. This excludes every assignment in that
specified class, including canonical free Yang–Mills energy observables.
The comparator theorem is **PROVEN**; its Yang–Mills application is **OPEN**.
The complete obligations are E-ALG, E-SEQ, E-TR and E-TS in §5, with
`PL-1L` a sufficient producer of E-TS. This is not unrestricted free-net
exclusion, non-Gaussianity, or a mass-gap theorem.

**Owner decisions remain decisions.** OWN-alg must accept this separated
hierarchy and its reconstructed scalar field; OWN-free must accept exactly
F1, rather than F2 or F3. In addition, N5 must accept the countable asymptotic
criterion in place of its present continuous **finite-moment** witness.
This note recommends that change; it does not silently make it. No existing
source or theorem statement is edited. If finite-moment N5 is immutable,
the recommended route does not yet satisfy it.

**Do not select the magnetic two-scale test as a whole-class separator.**
It has a PROVEN comparator inequality for the **marked canonical-curvature
class** `F_B^curv`, even with arbitrary positive matrix spectral measure.
That is a useful alternative contract, but a proper restriction of the
free assignments asked about here. `F17-WINS-B(2)` reduces its upper-bound
cost; it cannot repair its class or common-algebra gap.

| Candidate and whole free class | Decision for the proposed witness | Exact reason / missing input |
|---|---|---|
| Separated e, F1 | **OPEN for YM; PROVEN conditional separation** | §2 proves `AF-e => outside F1`. E-ALG/SEQ/TR/TS are required; PL-1L remains OPEN. |
| Separated e, F2 | **PROVEN counterexample to AF-e separation** | The scalar Gaussian field q in §3 has positive KL density `s²/log²(e+s)` and satisfies AF-e. A scalar member already defeats exclusion of a class that also allows tensors. |
| Separated e, F3 | **PROVEN counterexample to AF-e separation** | The same q is Gaussian on this very e hierarchy. Its connected functions of order greater than two vanish. |
| Time-zero B, F1 | **PROVEN counterexample to unmarked two-scale separation** | The assignments (B4) and (B5) are realized in a canonical free scalar theory on the B hierarchy of §1. They have a strictly positive magnetic-test value. |
| Time-zero B, F2 | **PROVEN counterexample to unmarked two-scale separation** | A canonical free scalar is a GFF with atomic KL measure. (B4) also works as an affine Gaussian B family. Arbitrary tensor GFFs are not all canonical Bianchi-curvature fields. |
| Time-zero B, F3 | **PROVEN counterexample to two-scale separation** | (B4) is an affine Gaussian state with deterministic B coordinates and arbitrary positive prescribed means, on the same hierarchy. |

Here “counterexample” refutes a **class-wide witness implication**, not an
assertion about the unknown actual YM state. No row claims unconditional
YM separation. The broad B rows refer to all compatible free assignments
on the explicitly specified unmarked hierarchy; the narrower marked reading
and its OPEN YM estimates are treated separately in §4. All statuses are
research statements under PROCESS_LIGHT, not audit or retained status.

## 1. Freeze the objects before comparing states

**The separated algebra.** Use
`A_e = direct_sum_n ^0S((R^4)^n)`, with tests flat on all collisions,
the ordered positive-time cone, scalar Euclidean action, and only the
products permitted by this separated test hierarchy. Reconstruction and
its extension/domain estimates are an explicit obligation, not a theorem
in this note. In particular `e(f)^2` on an arbitrary coincident test is not
adjoined by notation. This is the domain in W_T0 §6.1 and NONFREE55 §10.

Fix real nonnegative nonzero `f` supported compactly in `x_0>1`, and
`g(x)=f(theta x)`. Their supports have distance between fixed `d>0` and
`D<infinity`. Put `lambda_m=L^(-m)`, `f_lambda=lambda^(-4)f(x/lambda)`
and similarly for g. The connected two-point value

    C_m = S_2^T(g_lambda_m tensor f_lambda_m),
    V_m = lambda_m^8 C_m

is an actual OS pairing: for the centred reconstructed field it is the
squared norm of `[e(f_lambda_m)]`. Each m is fixed before any cutoff limit.
Thus these values use neither collision counterterms nor a flowed
Euclidean representative. A field-preserving equivalence preserves them.

**The magnetic hierarchy.** `A_B` means W_T0 §6.3's proposed common local
core containing the e-tests and local regularizations of positive B labels,
with their bounded truncations, permitted mixed products, and a boundary /
spatial completion containing `B_n(t;x)`. The label action is
`alpha_(R,b) B_n(t;x)=B_(Rn)(t;Rx+b)`. Time reflection, positivity and
unit/product relations are retained. In this unmarked hierarchy there is
no asserted identity reconstructing B from e, no underlying curvature
generator, and no identity fixing B's image in another theory. Imposing
such additional identities is an additional algebra/identification contract.
The counterexamples below are representations of this stated hierarchy,
not representations of an unspecified stronger quotient.

**F1.** On `A_e` take exactly the finite-polynomial class in the summary:
finite species, fixed finite masses/spins, finite derivatives and Wick
degree; include all coefficients and finite tensor products. Its defining
free propagators are finite matrix differential polynomials in scalar
mass-shell propagators. Do not import a classification of *all* local
fields or nets into this definition. On `A_B`, a free realization is a
representation of its permitted operations in such a finite free theory,
including the spatial completion. In particular constants are degree-zero
Wick polynomials; different t labels may have different scalar coefficients.
The nonlocal B label cannot be required to be a point-local Wick polynomial
while still admitting W_T0's own heat-smeared free comparator.

**F2.** On `A_e`, include elementary scalar/tensor GFF hierarchies with any
positive tempered KL measure on their appropriate separated domains. If
“free realization” also permits Wick composites of GFFs, the class is
larger still, and the AF-e counterexample remains valid. On `A_B`, an
unmarked GFF realization likewise does not prescribe the B assignment.
If instead the intended F2 is exclusively a Bianchi-curvature GFF together
with its canonical magnetic square, its name here is `F_B^curv`, not the
unrestricted F2 of the table.

**F3.** Gaussian / quasi-free on the chosen generators means Wick pairing
after centring: connected functions of order at least three vanish.
Means may be nonzero, and a covariance may be degenerate. This includes
affine Gaussian states, as “all Gaussian states” requires. For a convention
in which “quasi-free” means strictly centred, say so separately: a mean test
would then exclude states just by centring convention. A free quadratic
composite is usually not Gaussian on the composite generators. F1 and F3
therefore must not be identified.

There is no general inclusion “canonical free composites are Gaussian on
e.” All comparisons are on the same named generators and their allowed
operations. A map `O -> (1/2)D²O(1)[A,A]` does not qualify: for a quadratic
leading term q, `(q²)^natural=0` but `(q^natural)²` need not vanish. This
rebuilds the ID-natural product obstruction without using it as an input.

## 2. Library E-CAN: why AF-e separates all of F1

The proposed property is

    V_m -> 0, and lambda_m^(-eta) V_m -> +infinity
    for every eta>0.                                      (E1: AF-e)

Only `eta=1/2` in the second clause is needed for the F1 contradiction.
Retaining the familiar AF-e name does not demand a stronger YM producer:
the bounds in §5 yield all eta simultaneously.

**PROVEN free-side lemma.** A nonnull centred scalar finite Wick
polynomial in F1 has, at separated distance r,

    S_2^T(r)=C r^(-gamma)|log r|^j(1+o(1)),
    gamma an integer, j a nonnegative integer, C>0.         (E2)

Here is a rebuild of the needed analytic step. With mass squared s,

    G_s(r)=(16 pi²)^(-1) integral_0^infinity
                  tau^(-2) exp(-r²/(4tau)-s tau) d tau.    (E3)

This follows by integrating the Fourier Gaussian for
`1/(p²+s)=integral_0^infinity exp[-tau(p²+s)]d tau`; at s=0 it gives
`1/(4pi²r²)` by `v=r²/(4tau)`. Differentiation shows that for s=m²>0
`h=G_s` solves `h''+3h'/r-m²h=0` off zero. With `z=mr`,
`Y=4pi²r² h`, this is `z²Y''-zY'-z²Y=0`.

Construct its solutions as
`Y=a_0+sum_(n>=1)(a_n+b_n log z)z^(2n)`. Equating coefficients gives

    b_1=a_0/2;
    4n(n-1)b_n=b_(n-1),
    4n(n-1)a_n+(4n-2)b_n=a_(n-1)  (n>=2).                 (E4)

The coefficient a_1 is free. The recurrence has factorial denominators;
`b_n=a_0/[2^(2n-1)(n-1)!n!]`, and variation of the a recurrence adds
at most a harmonic factor. Both series and all derivatives converge on
compact punctured intervals. The two choices `(a_0,a_1)=(1,0),(0,1)`
give independent solutions (one tends to 1, one starts at z²); their
Wronskian is nonzero. Uniqueness for this ordinary differential equation
on any interval away from zero therefore spans every solution, including
(E3). No decay condition selecting a particular a_1 is needed for the
log-structure assertion. Finite derivatives have integer powers of r and
log degree at most one. This also avoids mistaking an ODE coefficient
check for identification of a unique Bessel function.

Expanding the Gaussian generating function `exp(J C J/2)` (or the
Grassmann exponential for fermions) gives Wick pairings. For a finite Wick
polynomial, its connected two-point function is a finite sum of finite
products of the differentiated propagator entries. Hence it has a
convergent power/log series with integer powers bounded below and a
finite maximum log degree. Scalar covariance makes it radial. After all
cancellations the first nonzero power and the highest log degree at that
power give (E2). If every coefficient vanishes, the separated analytic
kernel is identically zero and fails (E1)'s lower clause. Finally RP,
applied to the centred field near a point at positive time and its
reflection, gives `S_2^T(r)>=0`, so the nonzero leading coefficient is
positive in the `|log r|` convention. Masses can determine both C and the
surviving power; they are **not** assumed to occur only subleadingly.

Because the smearing distances lie in `[d,D]`, the expansion is uniform
there and

    C_m=C I_gamma lambda_m^(-gamma)|log lambda_m|^j(1+o(1)),
    I_gamma=integral f(x)g(y)|x-y|^(-gamma) dx dy >0.

If `gamma>=8`, the first clause of (E1) fails. If `gamma<=7`,
`lambda_m^(15/2) C_m ->0`, contradicting its second clause at `eta=1/2`.
This proves F1 exclusion for every permitted assignment, including arbitrary
finite normalization changes. It is the repaired NONFREE55 FS/SEP-e
argument; CODEX_REVIEW_NONFREE R3/R10 identify the mass correction.

**Optional enlargement, not needed for the recommendation.** The same
proof covers finite mixtures and NONFREE55's uniformly enveloped mixtures.
For component means mu_alpha, the connected kernel is
`integral C_alpha dnu + Var_nu(mu_alpha)`, not just the integral. Assume
these terms are finite and each component has the common ENV bound
`C_alpha(r)<=B r^(-gamma_alpha)|log r|^J` for `r<=r_0<1`.
Nonnegativity and Fatou force `gamma_alpha<=7` almost everywhere from
the first clause of (E1). ENV then bounds the average by
`B'lambda^(-7)(|log lambda|+c)^J`; the finite variance term is O(1).
Both contradict the lower clause. No claim covers arbitrary mixtures
without that envelope or variance assumption.

**The finite-moment interface remains different.** AF-e is an asymptotic
property of a countable family, not a continuous function of finitely
many values with a uniform gap. Truncating a positive KL measure to compact
mass intervals and replacing it by finite positive atomic sums approximates
any fixed finite list of separated two-point tests: the kernels are
continuous in mass on a compact interval and their large-mass tails are
integrable on these separated supports. Each atomic sum is a linear
combination of finitely many canonical free scalars. In particular this
applies to q below. A continuous separator using just those finitely many
two-point values cannot distinguish q from that closure. This does not
prove a no-go for every higher-moment witness. Nor do we assume all OS
two-point functions have a mass-shell-only representation: a random
spacetime-constant Gaussian mode is an additional permitted invariant
sector when clustering is absent (CODEX_REVIEW_NONFREE R4/R16).

## 3. Library E-GAUSS: a common-algebra counterexample for F2 and F3

Take the centred scalar GFF q with

    rho(ds)=s²/[log(e+s)]² ds,  s>=0,
    C_q(r)=integral rho(ds)G_s(r),  r>0.                   (E5)

We construct a legitimate Gaussian OS covariance, rather than use a
formal divergent Euclidean integral. For `u=p²>=0` put

    C_hat(u)=integral rho(ds)
                  (1-u)²/[(1+s)²(u+s)].                  (E6)

The integral is finite, nonnegative and polynomially bounded. At large s
its integrand is bounded by a constant times `1/(s log²s)` for fixed u;
near s=0, even u=0 is integrable. In fact the integral after removal of
`(1-u)²` is bounded by its finite value at u=0. For a finite mass cutoff,

    (1-u)²/[(1+s)²(u+s)]
      =1/(u+s)-1/(1+s)-(1-u)/(1+s)².

The last two terms are contact distributions. Thus away from coincidence
(E6) has exactly (E5). On reflected positive-time supports the contacts
vanish, and each mass-shell cross form is

    integral d³p/[(2pi)³ 2sqrt(|p|²+s)]
      |integral_(t>0) exp[-t sqrt(|p|²+s)] f_hat(t,p)dt|² >=0.

Integrating against rho preserves RP. Positivity of `C_hat` defines a
Gaussian hierarchy by the generating functional
`exp[-(1/2)<f,C f>]`. Its positive-time Gaussian reflection kernel is,
up to positive one-sided factors, `exp(<theta f,C g>)`; expanding the
exponential gives nonnegative tensor-power Gram forms. This proves RP
for polynomial Gaussian observables too. Temperedness, Euclidean symmetry
and Gaussian moment bounds follow from the polynomial covariance bound
and Wick pairings. Restriction to `A_e` uses precisely its separated data.
Equivalently its reconstructed one-particle space is the mass-shell
direct integral in the displayed positive form, and symmetric tensor
powers give the Gaussian vacuum. No sharp-time restriction of q is needed.

Here is a direct bound sufficient for AF-e; no spectral asymptotic theorem
is imported. For small r split the s integral at `r^(-1)`. Since
`G_s<=G_0`, the low part is at most `C r^(-5)`. In the high part
`log(e+s)>=log(1/r)`, while (E3) and two integrations give

    integral_0^infinity s² G_s(r)ds
      = (8pi²)^(-1) integral_0^infinity tau^(-5)
                         exp[-r²/(4tau)]d tau
      =192/(pi² r^8).

For a lower bound restrict to `r^(-2)<=s<=2r^(-2)` and
`r²<=tau<=2r²` in (E3). All exponentials are bounded positively below,
so `G_s(r)>=c r^(-2)` and `rho` on that mass window has total mass at
least `c' r^(-6)/log²(1/r)`. Consequently, with fixed positive constants,

    c r^(-8)/log²(1/r) <= C_q(r)
      <= C r^(-5)+C' r^(-8)/log²(1/r).                    (E7)

The same bounds hold after our positive separated smearing, with changed
constants. They imply both clauses of AF-e. All connected higher functions
of q vanish exactly. This is a PROVEN counterexample even to the proposed
implication “AF-e implies non-Gaussian.” Multiplying (E5) by a positive
constant can adjust its two-point coefficient; a coefficient alone cannot
rescue the implication. The example follows CODEX_REVIEW_NONFREE R7,
with the construction and estimates rebuilt here. The mass variable s is
mass **squared** throughout.

This does not conflict with NONFREE55 E2/R12: its tensor obstruction assumes
the positive **Bianchi curvature** spectral numerator. A scalar field of
this spectral dimension does not have that numerator. Allowing arbitrary
tensor-valued GFFs cannot remove a scalar member from the whole class.

## 4. Library B-CURV and the failure of unrestricted B assignments

On the **marked** class `F_B^curv` specify the reconstructed observable

    B_n(t;x)=(t²/4) sum_(i,j tangent to n)
                       (K_t^3*F_ij)^T M(K_t^3*F_ij),
    M>=0,

and the canonical equal-time curvature covariance with numerator
`T_ij,kl=p_i p_k delta_jl-p_i p_l delta_jk-p_j p_k delta_il+p_j p_l delta_ik`
and denominator `2sqrt(|p|²+s)`, integrated against a positive matrix
measure rho. Write `rho_M=Tr(M rho)` and require
`integral min(1,s^(-1/2))rho_M(ds)<infinity`, with weight 1 at s=0.
This is a definition of the comparator, not a classification theorem for
all tensor GFFs or all free representations of `A_B`.

The ordered spatial trace is `sum_ij T_ij,ij=4|p|²`. Angular integration
and `v=sqrt(t)|p|` give

    b_mu(t)=(4pi²)^(-1) integral rho_M(ds) J(ts),
    J(sigma)=integral_0^infinity v^4 exp(-2v²)/sqrt(v²+sigma)dv,
    J(0)=1/8.                                             (B1)

The integrand decreases in sigma. For sigma at most 1 the integral is
bounded above and positively below; above 1 it is comparable to
`sigma^(-1/2)` by restricting v to `[1,2]` for the lower bound. These
observations prove the domain condition and `b_mu(t_0)<=b_mu(t_1)` for
`t_1<t_0`. For the finite Gaussian vector entering the square, Wick
expansion gives `E B²=(Tr AQ)²+2Tr[(Q^(1/2)AQ^(1/2))²]<=3(E B)²`.
Thus these are finite vacuum vectors, not just formal means. Mixtures
preserve the inequality when all required moments are finite. Infinite
mean/domain failure cannot masquerade as matching a finite YM vector.

It follows, **conditionally on the YM estimates and common OS bridge**,
that

    W_B=[b(t_0)-b(t_1)]_+,
    b_YM(t_0)>=A>0, b_YM(t_1)<=A/2
      => W_B(YM)>=A/2, W_B(mu)=0 for mu in F_B^curv.        (B2)

Moreover the maximum discrepancy in the two means is at least `A/4`:
subtract the two differences and apply the triangle inequality. The
witness is Lipschitz in these two mean coordinates. Arbitrary masses,
normalizations, and positive matrix KL measures do not defeat (B2)
**with the prescribed curvature composite**.

A one-scale version is false even in that marked class. With n observed
colors and `M=I`, take

    rho(ds)=(32pi² y/n) I_n delta_0(ds).                    (B3)

Then `b_mu(t_0)=y` for any desired positive y. No uniform positive
one-point gap survives this free normalization choice.

**PROVEN unrestricted counterexample.** On `A_B` map

    e -> a centred canonical free scalar phi,
    B_n(t;x) -> h(t) 1,   h(t)=c t, c>0.                  (B4)

This is a unital product-preserving representation: define every allowed
mixed product by the same scalar substitution, every bounded truncation
by `min(h(t),M)1`, and every local regularization by that same constant.
It respects translations, rotations of n and x, reflection and B positivity.
It is supported in every region, so the localization error is zero.
The boundary vector is `h(t)Omega`, and its normal-time translate is
identical, giving the strong sharp-time limit and finite second moment.
All mixed OS properties reduce to those of phi. The joint generating
functional is an affine Gaussian one with deterministic B coordinates;
after centring B its covariance is zero. Yet
`W_B=c(t_0-t_1)>0` and `h(t)->0` as `t->0`. More generally any nonnegative
profile h satisfying the chosen label regularity has this representation;
values on finitely many witness times admit a nonnegative smooth interpolation.
This refutes a mean-profile separator for the broad F1, F2 and F3 readings
on this **same** hierarchy. It is not an identification of actual YM with
that state. Additional algebraic identities forbidding this substitution
would require a new, proved class-coverage theorem, not a better TS bound.

The issue is not limited to deterministic fields. A nonconstant free
canonical realization, also admitted by the GFF-realization reading, is

    B_n^sc(t;x)=M_0² t² (K_t^3*phi|_(H_n))(x)²,
    b_sc(t)=M_0² t/(16pi²),  M_0>0.                        (B5)

Indeed the equal-time massless scalar variance is
`integral d³p/(2pi)³ exp(-2t|p|²)/(2|p|)=1/(16pi²t)`.
Its square has second moment three times its squared mean. Spatial
smearing makes these canonical vacuum vectors well-defined; truncating
the Gaussian kernel gives their spatial local approximations, and time
translation gives the sharp-time limit by dominated convergence in
`d³p/(2|p|)`. Rotating the hyperplane gives the covariant family.
It has the same sign in (B2) as the proposed YM profile. This is a
quadratic free-field observable, not Gaussian on B generators; (B4),
not (B5), is the F3 counterexample. B5 is not a magnetic curvature square.

These examples delineate the choices: a fixed **marked** curvature family
has theorem (B2); an unrestricted free family has counterexamples; a
stronger proposed common algebra whose relations have not been supplied
has an **OPEN identification obligation**. They do not prove an
impossibility theorem about every possible magnetic witness.

### Exact YM obligations for the marked alternative (all OPEN here)

1. **B-ALG / SEQ.** Construct W_T0 §6.3's common cutoff maps and mixed
   regularity bounds, continuous Euclidean action and mixed invariance,
   support-compatible RP and permutations, and local approximations
   converging in the controlled norm to B. Take all joint limits on one
   sequence with the e theory. Full-slice B has spatial tails; a tilted
   full slice cannot enter the original positive-half cone merely because
   its center is positive. Mixed bounds are not supplied by e-only OS0.
2. **B-TR and coarse lower bound.** For the same bare law and fixed nonzero
   reference coupling, `0<U_-(m)<=u_(K-m)<=U_+(m)` with
   `U_±(m)=g_ref^(-2)+beta_± m log L ± R_F`, `beta_->0`.
   Prove `(TS-low)^B: E B(t_0)>=c_-/u_(K-m_0)` uniformly; set
   `A=c_-/U_+(m_0)>0`.
3. **Minimal upper bound.** Choose one fixed `m_1>m_0` before either
   limit. On the actual normalized RG history law specify a nonnegative
   partition `chi_reg+sum_(j,x)chi_(j,x)=1`, independent of the value of B,
   retaining returned failures and normalizers. Define
   `S=E[B(t_1)chi_reg]`,
   `M_r=sum_x E[B(t_1)chi_(K-m_1-r,x)]`.
   Prove F17-SF-B, `S<=C_sf/u_(K-m_1)`, and F17-WINS-B(2),

       limsup_sequence sum_r M_r
          <= A/2-C_sf/U_-(m_1),  right side >=0.            (B6)

   Then `limsup E B(t_1)<=A/2` exactly. The stronger
   `M_r<=H(u_(K-m))w_r`, `sum w_r<infinity`, with nonincreasing `H(v)->0`,
   supplies such an m_1. Only this stronger all-grid version gives the
   further ultraviolet conclusion at all labels. No necessity of a
   strict instanton-strength probability exponent is asserted.
4. **MOM2-B and SHARP-B separately.** At the two witness labels require
   uniform second moments for their actual cutoff approximants and joint
   law convergence; retain all other moment/continuity estimates needed
   by the chosen common hierarchy. Uniform second moments give convergence
   of means by `E[X 1_(X>M)]<=E X²/M`, but not convergence of second
   moments. SHARP-B must identify the boundary truncation vector with the
   strong normal-time limit **in the common reconstructed theory**.
   A finite mean or an external random variable attached to H_e is
   insufficient. With these identifications the means in (B2) are
   `<Omega,b_t>`, as required.
5. **Target match.** Accept the marked composite rule and the completion,
   or prove the missing coverage/locality theorem. Strict compact locality
   needs approximation uniform enough over the comparator class to keep
   the gap; YM-only localization does not give that. Non-freeness of the
   enlarged theory does not imply non-freeness of its e-only cyclic part.

F17-WINS-B(2) and MOM2-B cannot supply item 5. F17 controls a first moment;
it cannot supply item 4 either. Coordinator-owned source radius, kernel
remainder and original-law coercivity/tails are named dependencies, not
estimates established by this note.

## 5. The recommended contract: full list of YM obligations

The following formulation fixes one flat Wilson trajectory. A sphere
version would need its own common maps, uniform estimates and diagonal;
no transfer is inferred here.

**E-ALG — OPEN reconstruction/common-domain input.** The field is exactly

    e_a(x)=(4a^4)^(-1) sum_(mu!=nu) sum_(p in clover_mu,nu(x))
                            [1-Re tr(U_p)/N],
    ehat_a=e_a-E e_a,       Z(a)=1.

Use the separated hierarchy `A_e` and its ordered positive cone, with
continuous uniform test-space extension bounds and the hypotheses of the
actual reconstruction theorem: regularity and growth at all required
orders, E(4) invariance, reflection positivity and permutations/reality.
Prove that its reconstructed e has these separated values. This obligation
includes the unresolved reconstruction interfaces; two-point convergence
alone does not construct an OS theory. No arbitrary rescaling tending to
zero or infinity is permitted. Fixed nonzero rescaling would preserve
the class and AF-e but is not silently substituted for this normalization.

**E-SEQ — OPEN common-limit input.** One sequence `(K_j,R_j)`, with
`K_j,R_j->infinity`, carries that whole determining hierarchy and every
`g_lambda_m tensor f_lambda_m`. Uniform extension estimates pass convergence
from its countable dense tests to these exact tests. In particular

    lambda_m^8 Cov_(K_j,R_j)(O_a(g_lambda_m),O_a(f_lambda_m))
                         -> V_m,   O_a(f)=sum_x a^4 f(x)e_a(x).

There is no ordinary coincident e-moment assumption. The sequence is
common, not chosen anew for each inequality.

**E-TR — OPEN tuned-trajectory input.** Fix `N>=2`, odd `L>=3`,
`a=L^(-K)` and one nonzero `g_ref` in the admissible regime. The original
Wilson law has action `u_0 sum_p[1-Re tr U_p/N]`, with
`u_i=g_i^(-2)=2N/g_std,i²` the actual chain couplings. Require uniformly

    0<U_-(m)<=u_(K-m)<=U_+(m),
    U_±(m)=g_ref^(-2)+beta_± m log L ± R_F, beta_->0.         (E8)

These are inherited F-tune obligations, not proved coupling flow. In the
PL-1L production route also require FLOW-pw for every `0<=j<=n<=K`:
`b_-(n-j)-R_F<=u_j-u_n<=b_+(n-j)+R_F`, `b_±=beta_± log L`, together
with its fixed small-coupling lower bound on u and terminal TR-7.
An exact numerical one-loop slope is not needed.

**E-TS — OPEN observable estimate, direct sufficient form.** There are
fixed `m_0,d_0,R_0,c_->0,C_+<infinity` and finite
`0<kappa<=kappa'` such that for every `m>=m_0`, `K>=m+d_0`, `R>=R_0`,
on this same law and for this same fixed test pair,

    c_- u_(K-m)^(-kappa') <= V_m^(K,R)
                          <= C_+ u_(K-m)^(-kappa),
    V_m^(K,R)=lambda_m^8 Cov_(K,R)(O_a(g_lambda_m),O_a(f_lambda_m)). (E9)

For each fixed m pass (E9) along E-SEQ. Then
`0<=V_m<=C_+ U_-(m)^(-kappa)->0` and
`lambda_m^(-eta)V_m>=c_- L^(eta m) U_+(m)^(-kappa')->infinity`.
Only **after** those fixed-m limits is m sent to infinity. §2 proves
F1 exclusion. This is the complete conditional witness proof. E-TS at
one coarse scale, reflection positivity alone, or an upper bound alone
does not suffice. This argument proves no estimate for YM by itself.

### Named sufficient producer: PL-1L, with its exact remaining costs

The minimal named sufficient replacement for E-TS is the summed PL-1L
error below, together with the free-slice estimates and FLOW-pw. Define
`G_i=E[O_a(f_lambda)|U_i]`, `H_i=E[O_a(g_lambda)|U_i]` using the **actual
normalized chain**, and set

    D_i=lambda^8 E Cov(G_i,H_i|U_(i+1))  (i<K),
    D_K=lambda^8 Cov(G_K,H_K).

The decreasing conditional-expectation increments are orthogonal, so
`V_m^(K,R)=sum_(i=0)^K D_i`, including the terminal covariance. Let
`K_i` now denote the **free curvature covariance slices** of TSE55 §2.2
(not the RG probability kernels); to avoid that collision below write
them `mathcal K_i`. Their exact sum is `mathcal G^F=P_ex`.
With `a_i=mathcal K_i/u_i`, `mathcal G^run=sum_i a_i`, the explicitly
defined Gaussian one-loop contributions are

    Lambda_i=lambda^8(N²-1) sum_(p,q) w_f(p)w_g(q)
                    [4a_i(p,q) sum_(j>i)a_j(p,q)+2a_i(p,q)²]. (E10)

This includes `i=K` with empty cross sum. The weights are the fixed
quadratic clover-source weights in TSE55 §2.1; they carry no fitted
matching coefficient. Expanding `(sum a_i)²` proves
`sum_i Lambda_i=2lambda^8(N²-1)sum w_f w_g (mathcal G^run)²`.
Individual Lambda_i can have either sign or vanish.

**PL-1L_Sigma — OPEN:** for some fixed `theta>0`, uniformly in the E-TS
domain,

    |sum_i(D_i-Lambda_i)|<=C_err u_k^(-2-theta), k=K-m.     (E11)

The producer-facing, stronger PL-1L in TSE55 §5.2 is

    |D_i-Lambda_i|<=A_1 u_(max(i,k))^(-2-theta) p_i(k),
    p_i(k)=L^(4(k-i)) exp[-mu_1 d L^(k-i)]       (i<k),
    p_i(k)=L^(-8(i-k))                         (i>=k).       (E12)

This is an absolute error relative to a positive envelope, **not** division
by Lambda_i. FLOW-pw sums the envelope: before a coarse displacement of
order `u_k/(2b_+)`, the coarse u remains at least `u_k/2`; beyond it,
the geometric factor beats every fixed inverse power. The fine weights
are summable independently of k. Hence (E12) gives (E11).

The additional free input **K-dec** is the uniform coupling-one bound
`|mathcal K_i(p,q)|<=M L^(-4i)exp[-mu |x_p-x_q|_1/L^i]` for `i<K`,
and `|mathcal K_K|<=M L^(-4K)`. Its underlying linear response/coercivity
results retain their stated scopes; no interacting estimate is inferred.
Splitting coarse scales as above and using
`|1/u_i-1/u_k|<= (b_+|i-k|+R_F)/(u_i u_k)` gives a kernel error
`O(L^(-4k)u_k^(-2))`, hence a bubble error `C_AF u_k^(-3)`.

**LGF is supplied at the scalar/free library scope.** Its positive graph
Laplacian is `Delta=sum_j(2I-S_j-S_j^(-1))`, counting mean-zero torus
inverse, and `Phi=1/(4pi²r²)`. Equations (37)–(41) yield
`mathcal G^F=d Delta_1^(-1)d*` and the needed curvature error
`O(r^(-5))+O(T^(-4))` for `1<=r<=T/4`, `T=R/a`. The squared error is
`O(r^(-9)+r^(-4)T^(-4))`. These are the order-two estimates consumed
here. Orders zero and one have torus errors `T^(-2)` and `T^(-3)`, not
`T^(-4)`. No unregularized image sum is used.

The separated Riemann sums then give
`B_0/2<=L_free<=3B_0/2`, where
`B_0=c_bub I_8>0`, `c_bub=12(N²-1)/pi^4`. To fix this normalization:
the six-component continuum curvature covariance is
`Lambda²(I-2xx^T/r²)/(pi²r^4)`. The matrix is orthogonal, so its squared
entry sum is `6/(pi^4r^8)`; the two Wick contractions and `N²-1` colors
give c_bub. The clover's quadratic source and the Wilson convention in
E-ALG/E-TR are those used by these weights (TSE55 §2.1–§2.4).

Take all depth/radius thresholds to be maxima of the producer thresholds.
For sufficiently large fixed m_0 the two errors
`C_AF/u_k³` and `C_err/u_k^(2+theta)` are each at most
`B_0/(8u_k²)`, uniformly by (E8). Therefore

    B_0/(4u_k²)<=V_m^(K,R)<=7B_0/(4u_k²).                 (E13)

Thus E-TS follows with `kappa=kappa'=2`. This rebuilds TSE55's conditional
assembly; it does **not** prove PL-1L. In particular LGF supplies the
free kernel, not the quantum source matching or a positive YM lower bound.

Producing PL-1L still requires the six distinct items in TSE55 §6.4/E5:
source-dependent Gaussian dominance, background covariance control,
quantum image normalization tending to **one** as well as its decay,
coarse linear covariance matching, summed two-insertion large-field
errors including all coarse levels, and matching the running coupling
of that Gaussian part to u_i. CODEX_REVIEW_TSE R4/R12 correctly prevent
replacing these by a first-image upper bound such as LOC-e. The claimed
P1–P6 implication is only **ARGUED** until its remainders are written and
bounded. E11/E12, rather than this proposed production mechanism, is the
precise OPEN estimate used by the contract.

No MOM2-B, SHARP-B or F17-WINS-B is required for this separated-e
contract. This is an interface comparison, not a proof that its remaining
large-field work is easier. Existing coordinator outputs remain named
inputs wherever their source/normalization estimates are needed.

## 6. If the owner requires the broader classes

For **elementary** GFF hierarchies and Gaussian states on e, there is a
different conditional finite-moment witness. Choose four real tests with
pairwise separated supports on the common OS hierarchy. With centred e,

    K4=S4(f1,f2,f3,f4)
        -S2(f1,f2)S2(f3,f4)-S2(f1,f3)S2(f2,f4)
        -S2(f1,f4)S2(f2,f3),       W4=|K4|.                (E14)

Every Gaussian hierarchy, including arbitrary tensor KL covariance and
degenerate covariance, has `K4=0` by expanding its generating function.
Thus the exact missing YM input **C4-sep (OPEN)** is: fixed tests and
`delta>0` such that `liminf_j |K4_j|>=delta` on the common sequence,
together with convergence of all moments in (E14). This gives
`W4(YM)>=delta`, a continuous finite-coordinate separator. No moving
tests, contact products or sharp-time fields are needed. PL-1L, a
two-point estimate, does not supply C4-sep.

This excludes elementary F2 and F3 on those generators; it does **not**
exclude all Wick-composite realizations in canonical or generalized free
fields. Already a square of a nondegenerate Gaussian variable has
nonzero connected fourth moment: expanding the Gaussian generating
function gives `kappa_4(X²)=48(Var X)^4`. Separated free-field squares
likewise have connected cycle contractions. Free-Maxwell e has nonzero
separated four-point values (CODEX_REVIEW_NONFREE R8). Therefore do not
combine (E14) and AF-e and call the result exclusion of every GFF
composite; that stronger comparator theorem and its required YM
multi-point/tensor estimates remain **OPEN**. The known scalar
counterexamples do not constitute a no-go for those future witnesses.

## 7. Disposition and provenance

The six decisions and the target recommendation are complete at the
brief's requested scope. Actual non-freeness of the reconstructed YM
state remains OPEN. The recommendation uses the existing separated
field and needs its two-sided estimates at every short scale. The marked
B alternative uses only two witness means but adds a common extension,
sharp-time, moment, locality and free-assignment contract. A shorter
list of scalar inequalities alone does not make that alternative a
whole-class solution.

Primary local sources: ASSEMBLY55 N0/N5/N6/N15/F1; W_T0 §§1–6;
F17 §§1–2,5,7; NONFREE55 §§1–3,8,10 and CODEX_REVIEW_NONFREE
R2–R12/R16; HINT2_55 R1.9–R1.10; TSE55 §§2–3,5–7 and
CODEX_REVIEW_TSE R4/R9/R12; LGF §§1,8–10. Sources and verification
records are in [WITNESS_LOG](WITNESS_LOG.md). Independent review is
recorded in [checks/witness_review.md](checks/witness_review.md).

Attribution: Wick and Isserlis for Gaussian pairings; Källén and Lehmann
for the spectral framework; Osterwalder and Schrader for reconstruction;
Balaban and Dimock for the upstream gauge RG methods. The power/log
method agrees with the classical Bessel expansion attributed to Watson
and Olver in [NIST DLMF §10.31](https://dlmf.nist.gov/10.31), consulted
for attribution and comparison; (E3)–(E4) rebuild the fact consumed here.
No recalled `[m]` assertion carries any argument. No new numerical
experiment, audit verdict, axiom, commit or public consolidated proof
is produced by this author lane.
