---
claim_id: excluded_walk_quantitative_memory_transfer_bounded_theorem_note_2026-10-11
claim_type: bounded_theorem
runner: scripts/excluded_walk_quantitative_memory_transfer_2026_10_11.py
claim_scope: "For the supplied antisymmetric excluded Weyl pair, prove an inverse-edge moment and an explicit mean-survival rate for its fixed effective dressing, then a quantitative time-averaged fixed-transverse-projection occupation for one globally normalized actual positive-free-band packet family."
upstream_dependencies:
  - excluded_walk_memory_current_bounded_theorem_note_2026-10-11
  - excluded_walk_projected_free_band_canonical_current_bounded_theorem_note_2026-10-11
  - excluded_walk_low_energy_energy_current_bounded_theorem_note_2026-10-11
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: upstream_support
reachability_to_target: supports
target_claim_id: null
target_blocker_text: "Construct controlled links from microscopic dynamics to macroscopic transport."
source_of_blocker_text: user_goal
artifact_role: theorem
next_trace_action: "Use the explicit occupation estimate in further supplied-model current and many-body tests; retain separate independent audit before effective retained status."
conditional_surface_status: "Exact estimates for the supplied effective generator and the specified actual free-band preparation."
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# Quantitative effective memory and time-averaged transverse occupation

**Date:** 2026-10-11

**Type:** bounded_theorem

**Status:** proposed_retained

Current surface status: conditional-support. The exact edge and occupation
source arguments have received the selective mathematical checks identified
below. The complete combined note also received a scoped composition check;
root authored the occupation source and does not independently recertify it.
The distinct source reviews supply that coverage. Final source and delivery
checks are recorded below. No independent retained-status audit is claimed.

For every nonzero kappa, put b=|kappa|. The normalized dressing spectral
measure of the supplied effective generator has the inverse moment
`integral dnu(E)/(b^2-E^2)<=12I0/b^2`. Its actual combined-edge mass is
at most `12I0[2delta/b-(delta/b)^2]`. Together with the inherited interior
density estimate, this gives the explicit mean-survival bound

    (1/T)integral_0^T |a(t)|^2dt
      <=min{1,D0(bT)^(-4/5)},
    D0=24^(6/5)(327680pi)^(4/5)I0^2.                    (A1 = S20)

For the actual excluded walk, use the constructed free positive-band packet
with band parameter 0<lambda<=1/16, total-momentum center lambda^3(1,1,1),
radius lambda^5, and one global contact projection and normalization.
For the fixed transverse projection F its time-averaged probability obeys

    H_lambda=lambda^(-59/18),
    (1/(lambda H_lambda))integral_0^H_lambda
                  <Psi_lambda(t),F Psi_lambda(t)>dt
       =1/(8pi^2 I0)+O(lambda^(2/9)).                   (A9)

The finite error and every scale domain appear below. This is an order-lambda
occupation of a specified subspace for a constructed family. It neither
describes most of the entire normalized packet nor supplies a convergence
rate for the weighted canonical current.

## 1. Supplied model, exact dependencies, and proof organization

All relative-torus and total-momentum integrals use dq/(2pi)^3 and
dK/(2pi)^3 respectively. Inner products are linear in the second argument.
On the fixed antisymmetric pair fiber, the singlet coefficient is even in q
and the Cartesian triplet coefficients are odd. The supplied free symbol,
contact exclusion, and bounded physical generator are

    H0(K,q)=sigma_1·sin(K/2+q)+sigma_2·sin(K/2-q),
    P=I-|c><c|,
    H_D(K)=P H0(K)P restricted to ran P,

where c is the constant normalized spin singlet. The full operator H_D is
the measurable direct integral of these bounded fibers. The auxiliary c in
the zero extension is not a physical state. Coordinates, lattice and clock
units, this continuous generator, exclusion rule, Hilbert space and
preparation are supplied-model premises. No physical primitive or empirical
clock calibration is selected here.

The Cartesian triplets are T_j=sigma_(1,j)c. On the full physical fiber,
F is zero on the singlet block and is the pointwise I-nn^T projection on
the triplet block, with n=sin(q)/|sin(q)|. Its direct integral is the same
fixed observable in every total-momentum fiber.

This note is self-contained for the new S4–S21 and A1–A9 implications given
the following explicitly imported theorems. Their upstream proofs remain in:

- [Projected positive-free-band canonical current](EXCLUDED_WALK_PROJECTED_FREE_BAND_CANONICAL_CURRENT_BOUNDED_THEOREM_NOTE_2026-10-11.md):
  the physical zero-space identification, cone integrals, L6–L8 band measure,
  Q12–Q16 finite comparison and the actual nonzero-K preparation. Q16 is used
  as an all-finite-T inequality, not merely at its later 1/20 specialization.
- [Effective memory and canonical current](EXCLUDED_WALK_MEMORY_CURRENT_BOUNDED_THEOREM_NOTE_2026-10-11.md):
  E20–E23 give absolute continuity, symmetry and the interior density bound;
  E25–E26 give the earlier finite-horizon split; G5 gives the stated growing
  interval substitution. Its weighted/outgoing/current conclusions remain
  separate results and are not needed to infer this fixed-F probability.
- [Low-energy energy current](EXCLUDED_WALK_LOW_ENERGY_ENERGY_CURRENT_BOUNDED_THEOREM_NOTE_2026-10-11.md):
  the inherited supplied-model and physical-space provenance used by those
  two notes. No canonical-current formula is required by the new proof.

The exact source revisions and corresponding current repository-note
identities are in the reconstruction map and receipt. These dependency
references do not assert that a pending PR has landed or been audited.

The effective compression below uses the inherited `ker H_D(0)=Z` and
`1/12<=I0<=9/8`. The effective density assumptions are stated in Section 7;
the complete band/preparation hypotheses and finite comparison are restated
in Sections 10–13. Thus the composition exposes every imported estimate used
by its new steps. It makes no new inference from finite-control counts.

In Sections 3–9 delta denotes an edge width. In Sections 10–13 it denotes
the weak total-momentum scale lambda^3. The scalar compression coefficient
is written c_edge to distinguish it from the contact singlet c.

## 2. Fixed physical effective space

Work in the Hilbert space of odd square-integrable complex triplet fields on
the three-torus, with normalized measure `dmu=dq/(2pi)^3`. Inner products
are linear in the second slot. Put

    s_j=sin q_j,  epsilon=|s|,  n=s/epsilon,
    I0=integral (4epsilon^2)^(-1) dmu,
    zeta=n/(2epsilon sqrt(I0)),
    F={odd u in L2: n·u=0 almost everywhere},
    Z=F direct-sum span{zeta},  Pi=F+|zeta><zeta|.          (S1)

The same letter F denotes the orthogonal projection onto that closed
subspace. Cone points form a null set. The source proves
`1/12<=I0<=9/8` and `||zeta||=1`; its inverse-radius singularities are
square-integrable. Z is the full physical zero space. The auxiliary
constant singlet is not in Z and is not added to the calculation.

For fixed `kappa in R^3`, define

    b=|kappa|,  d_j=kappa_j cos q_j,
    Bv=i d cross v,  A=Pi B Pi restricted to Z,
    w(q)=sum_j kappa_j^2 sin^2 q_j,
    C=b^2 I_Z-A^2.                                       (S2)

B is bounded self-adjoint, preserves odd parity, and has norm at most b.
A is bounded self-adjoint on all Z, with norm at most b. All multipliers
and compressions used below are bounded. No derivative of zeta or inverse
of the gapless Hamiltonian is used. Let nu be A's probability spectral
measure at zeta. It is supported in `[-b,b]`. The source's block generator
gives

    exp(-itA)zeta=(u(t),a(t)),
    a(t)=integral exp(-itE) dnu(E),
    ||u(t)||^2=1-|a(t)|^2.                               (S3)

For `b=0`, A is zero and `a(t)=1`. All subsequent estimates assume `b>0`.
They hold for every direction of kappa, including `kappa=k(1,1,1)` with
nonzero k. The supplied walk, exclusion rule, pair Hilbert space, chosen
preparation, torus normalization and effective clock remain premises.
No approved primitive is being reclassified, and none supplies these
model choices or a physical identification of S3.

## 3. A rank-one lower bound for the spectral defect

Pointwise, the cross-product square is

    B^2=|d|^2 I-dd^T,
    b^2 I-B^2=w I+dd^T.                                 (S4)

The real vector d makes `dd^T` a positive Hermitian multiplication
operator, also on complex fields. Keep the positive compression defect:
on Z,

    C=Pi(b^2 I-B^2)Pi+Pi B(I-Pi)B Pi
     =Pi w Pi+Pi dd^T Pi+R*R,
    R=(I-Pi)B Pi.                                       (S5)

For `z=u+alpha zeta in Z`, u is pointwise transverse and zeta is
pointwise longitudinal. Multiplication by the scalar w preserves that
orthogonality, so

    <z,w z>=<u,w u>+|alpha|^2<zeta,w zeta>.

The dressing coefficient is exact. Coordinate permutation invariance
of the normalized torus measure and
`sum_j sin^2(q_j)/epsilon^2=1` almost everywhere give

    integral sin^2(q_j)/epsilon^2 dmu=1/3,
    <zeta,w zeta>=(1/(4I0))sum_j kappa_j^2/3
                 =b^2/(12I0)=:c_edge>0.                     (S6)

Thus `Pi w Pi=F w F+c_edge|zeta><zeta|` on Z. Combining the three positive
terms in S5 proves the bounded quadratic-form inequality

    C >= c_edge |zeta><zeta|,     c_edge=b^2/(12I0).               (S7)

This estimate is about the dressing direction. It is not a positive
uniform lower bound on C. Indeed `||A||=b`: the transverse compression
`D=FBF` acts as `D u=i(d·n)n cross u`, hence `|Du|=|d·n||u|` for
transverse u. Along `q=r kappa/b` as positive r tends to zero,
`d·n->b`. For every positive tolerance, continuity away from the cone
gives a positive-measure small neighborhood on which `|d·n|` is within
that tolerance of b. A normalized transverse field supported there and
its negative, extended oddly, belongs to F and has D norm arbitrarily
close to b. The F component of A on this vector is D, so `||A||>=b`.
Together with S2 this gives equality. S7 therefore cannot be replaced by
a positive operator-norm spectral gap.

## 4. Actual combined-edge mass

For `0<delta<b`, write `chi=delta/b`, and use the spectral projection

    P_delta=1_{|A|>=b-delta},
    m_delta=<zeta,P_delta zeta>
           =nu({E: |E|>=b-delta}).

For `z=P_delta zeta`, both `||z||^2` and `<zeta,z>` equal m_delta.
On the range of this projection, `0<=C<=h_delta I`, where
`h_delta=2b delta-delta^2`. Consequently S7 gives

    c_edge m_delta^2 <=<z,Cz><=h_delta m_delta,
    m_delta<=min{1,12I0(2chi-chi^2)}.                    (S8)

If m_delta is zero there is nothing to divide; otherwise division by
`c_edge m_delta` proves the estimate. Both spectral edges are already inside
P_delta. There is no additional doubling in S8. This is a bound for the
actual spectral mass; it does not identify that mass with the Poisson
quantity used by the memory note.

## 5. A regulated inverse-form estimate

The useful stronger fact is

    integral_[−b,b] dnu(E)/(b^2-E^2) <=12I0/b^2.         (S9)

Here an infinite integrand at an endpoint is interpreted in the
nonnegative extended-integral sense. To prove S9 without assuming a
bounded inverse of C, take `eta>0` and define

    x_eta=(C+eta I_Z)^(-1)zeta,
    t_eta=<zeta,(C+eta I_Z)^(-1)zeta> >0.

The regulator makes the inverse bounded everywhere. Since
`(C+eta I)x_eta=zeta`, S7 gives

    c_edge t_eta^2 <=<x_eta,Cx_eta>
              =t_eta-eta||x_eta||^2 <=t_eta,
    t_eta<=1/c_edge.                                         (S10)

By bounded spectral calculus,
`t_eta=integral (b^2-E^2+eta)^(-1)dnu(E)`. Let eta decrease to zero and
apply monotone convergence. This proves S9, and also excludes dressing
atoms at both endpoints. Equivalently, zeta belongs to the domain of
the spectral inverse square root `C^(-1/2)` and its squared norm is at
most `1/c_edge`. No bounded `C^(-1)` on all Z is asserted.

S9 also reproves S8: on its edge set, `1/(b^2-E^2)>=1/h_delta`.
The direct projection proof was retained to expose the squared overlap
and the combined-edge normalization.

## 6. The source's Poisson edge term

The memory note defines the scalar resolvent and its computable edge
upper bound by

    M(z)=<zeta,(z-A)^(-1)zeta>,
    e_delta=min{1,4delta[-Im M(b+i delta)]}.             (S11)

That note proves symmetry of nu, for example from
`M(-conjugate(z))=-conjugate(M(z))`. It also proves absolute continuity,
so using strict or non-strict finite endpoints in m_delta has the same
value. In particular `m_delta<=e_delta`: on the upper edge the Poisson
factor `delta^2/((b-E)^2+delta^2)` is at least one half, and symmetry
accounts for the second edge.

For every `x>0`, elementary completion of a square gives

    delta/(2x)-delta^2/(x^2+delta^2)
       =delta(x-delta)^2/[2x(x^2+delta^2)]>=0.

S9 makes both `1/(b-E)` and `1/(b+E)` integrable: each is at most
`2b/(b^2-E^2)`. Symmetry then gives

    integral dnu(E)/(b-E)
       =b integral dnu(E)/(b^2-E^2)<=12I0/b.

Apply the scalar inequality with `x=b-E`, integrate, and retain the
factor four in S11. The result is

    e_delta<=min{1,24I0 chi}.                            (S12)

Endpoint absence handles the null exceptional point E=b. The actual mass
bound in S8 is slightly stronger than this bound on e_delta. The two
quantities remain distinct: e_delta includes a Poisson contribution from
energies outside the edge region.

## 7. From the inverse moment to an L^(5/3) density

The memory theorem E20–E23 supplies
`dnu(E)=rho(E)dE`, with rho nonnegative, integral one and support in
`[-b,b]`. Its uniform strip-resolvent proof gives, for each `0<delta<b`,

    rho(E)<=32768 pi I0 b^(1/2) delta^(-3/2)
             for almost every |E|<=b-delta.             (S13)

This is an inherited, source-bound conditional result, not an inference
from the finite controls in this packet. The frozen memory review checked
its cone-measure, Poisson domination and endpoint argument. That review
does not independently certify this new composition.

Set `K=32768 pi I0` and `d(E)=b-|E|`. Choose a single full-measure set
on which S13 holds for every rational delta in `(0,b)`. At any E in
that set, let rational delta increase to d(E), including d(E)=b if
E=0. This proves the usable pointwise envelope

    rho(E)<=K b^(1/2) d(E)^(-3/2),   |E|<b.             (S14)

There is no uncountable union of exceptional null sets. Raising only the
extra `2/3` density power in S14 gives

    rho(E)^(5/3)
       <=K^(2/3)b^(1/3) rho(E)/d(E).

Also `1/d(E)=(b+|E|)/(b^2-E^2)<=2b/(b^2-E^2)`.
After integration, S9 therefore yields

    integral rho(E)^(5/3)dE
       <=24I0 K^(2/3)b^(-2/3)=:R_b<infinity.            (S15)

In particular `||rho||_(5/3)^2<=R_b^(6/5)`. The unweighted envelope
S14 is not integrable at the edges; it is the weighted moment S9 that
makes S15 possible. A linear bound on cumulative edge mass by itself
would not supply the same finite inverse moment.

## 8. Direct convolution proof and the mean-survival rate

Here is the required special Young inequality, proved rather than
imported. Let f,g be nonnegative functions in `L^(5/3)(R)`, and put
`U=integral f^(5/3)`, `V=integral g^(5/3)`. At each x write

    f(x-y)g(y)
       =[f(x-y)^(5/3)g(y)^(5/3)]^(1/5)
          f(x-y)^(2/3)g(y)^(2/3).

Hölder in y with exponents `5,5/2,5/2` gives

    (f*g)(x)^5
       <=[f^(5/3)*g^(5/3)](x) U^2 V^2.

Integrating in x and using Tonelli gives
`integral(f*g)^5<=U^3 V^3`. One may first truncate f,g to bounded
compactly supported functions and then use monotone convergence. Thus

    ||f*g||_5<=||f||_(5/3)||g||_(5/3).                   (S16)

Extend rho by zero and set `tilde-rho(E)=rho(-E)` and
`h=rho*tilde-rho`. This difference density is nonnegative, even,
integrable with total mass one, and by S15–S16 satisfies
`||h||_5<=R_b^(6/5)`. For `T>0`, Fubini against the finite product
probability measure and exchange of the two energies give exactly

    Q(T):=(1/T)integral_0^T |a(t)|^2 dt
         =integral h(x) sinc(Tx) dx,
    sinc(v)=sin(v)/v,  sinc(0)=1.                       (S17)

The imaginary part cancels under exchanging the energies. No symmetry
of the original probability measure is needed for that cancellation,
and sinc is not assumed nonnegative. Its absolute value is at most

    K_T(x)=min{1,1/(T|x|)},  K_T(0)=1.

The exact whole-line norm is

    integral K_T(x)^(5/4)dx
       =2/T+2T^(-5/4)integral_(1/T)^infinity x^(-5/4)dx
       =10/T,
    ||K_T||_(5/4)=(10/T)^(4/5).                         (S18)

Hölder with exponents 5 and 5/4 now proves

    Q(T)<=||h||_5 ||K_T||_(5/4)
          <=R_b^(6/5)(10/T)^(4/5).                     (S19)

Substitution of S15, with `tau=bT`, gives the explicit statement

    D0=24^(6/5)(327680 pi)^(4/5) I0^2,
    Q(T)<=min{1,D0 tau^(-4/5)},
    (1/T)integral_0^T ||u(t)||^2dt
          >=max{0,1-D0 tau^(-4/5)},  T>0.              (S20)

All constants are independent of the direction of kappa. The large
constant is a conservative consequence of the inherited cone estimate;
no optimal exponent or prefactor is claimed. The result controls a mean
of the survival probability. It does not imply a pointwise `t^(-2/5)`
amplitude bound, a monotone transfer law, or weighted-current convergence.

## 9. Preserved earlier mean bound

The original edge worker used the source's central/edge split before
the L^(5/3) improvement was proposed. That route remains valid and its
helper and logs remain unchanged. For `tau=bT>=1/2`, put
`L=1+log(2tau)`. Combining source E25–E26 with S12 gives

    Q(T)^(1/2)
       <=24I0 chi+256sqrt(pi I0 L/tau) chi^(-3/4).

For

    Q0=64pi L/(I0 tau)<1,
    chi=Q0^(2/7),

the right side is `56I0 chi`, by direct differentiation or substitution.
Consequently

    Q(T)<=min{1,3136 I0^2 Q0^(4/7)}.                    (S21)

For example `tau>=2^16` guarantees Q0<1. Indeed L/tau decreases for
tau>=1/2; at `2^16`, use `I0>=1/12`, `pi<22/7`, and `L<18` to get
`Q0<297/448`. S21 is the earlier logarithmic estimate. S20 has a stronger
asymptotic power and removes this cutoff restriction. Either bound can
be used where numerically useful. The earlier briefly considered cone
cutoff gave only an O(sqrt(delta)) edge estimate; it was superseded by
the exact coefficient S6, not disproved by a counterexample.

## 10. Imported band preparation and the reused mean bound

The estimate A1 is now S20 proved above, with C_edge=D0; it is no longer an
unproved dependency within this note. It still depends on the supplied-model
memory theorem stated in Section 7. Set kappa0=(1,1,1), so b=sqrt(3), and
take 0<lambda<=1/16. Define the actual central free slice and projection by

    I_lambda=[5lambda/4,7lambda/4],
    Gamma_lambda=1_I_lambda(H0(0)),
    w_lambda=||Gamma_lambda zeta||^2,
    phi_lambda=Gamma_lambda zeta/sqrt(w_lambda),
    beta_lambda=<c,phi_lambda>, n_lambda=sqrt(1-beta_lambda^2),
    chi_lambda=P phi_lambda/n_lambda,
    A_lambda=<zeta,chi_lambda>=sqrt(w_lambda)/n_lambda.

This beta_lambda is real and nonnegative for the specified slice. The exact
positive contact density (distinct from the effective rho(E) in S13) and
band mass are, for 0<E<2,

    rho(0,E)=E^2/(16pi^3) integral_(S^2)
                product_j(1-E^2 n_j^2/4)^(-1/2)dOmega,
    E^2/(4pi^2)<=rho(0,E)
                  <=E^2/[4pi^2(1-E^2/4)^(3/2)],
    w_lambda=I0^(-1)integral_I_lambda rho(0,E)/E^2 dE.

The inherited finite bounds used below are

    F chi_lambda=0, Pi chi_lambda=A_lambda zeta,
    n_lambda>=1/2, 0<=beta_lambda<=1/2,
    sqrt(lambda)/12<=A_lambda<=2sqrt(lambda), A_lambda<=1,
    C_lambda=2/[(5/4)lambda n_lambda]
                        +beta_lambda sqrt(I0)/n_lambda<=4/lambda.

These are the L6–L8/Q12–Q15 statements of the prior current note. They use
the normalized torus measure, not a fitted low-energy density. The weaker
lower constant 1/12 follows from the source's 1/(3pi) bound.

## 11. A finite band-weight remainder

Fix kappa0=(1,1,1), b=sqrt(3), and 0<lambda<=1/16. Use the actual normalized
free spectral slice phi_lambda of zeta on [5lambda/4,7lambda/4], its physical
projection chi_lambda=P phi_lambda/n_lambda, and
A_lambda=sqrt(w_lambda)/n_lambda. Put c_A=1/(8pi^2 I0).

The L7-L9 measure bounds imply

    c_A <= w_lambda/lambda
        <= c_A F_lambda,
    F_lambda=(1-49lambda^2/64)^(-3/2).

Cauchy-Schwarz against the free contact spectral projection gives
beta_lambda^2=|<c,phi_lambda>|^2<=integral_I rho(0,E)dE. Hence

    beta_lambda^2 <=49lambda^3 F_lambda/(128pi^2)
                   <=lambda^3/3.                         (A2)

For x<=1/16 the derivative of (1-x)^(-3/2) is below 2. Therefore
F_lambda<=1+2lambda^2. With pi^2>9 and I0>=1/12 we have c_A<=1/6, and

    0<=A_lambda^2/lambda-c_A
       <=c_A [(1+2lambda^2)/(1-lambda^3/3)-1]
       <=lambda^2.                                      (A3)

For the last inequality it suffices to use lambda<=1/16 and
2+lambda/3 <= 6(1-lambda^3/3). This also checks the denominator is positive.
Thus the band asymptotic used below has a finite uniform error bound.
The previously checked bounds F chi_lambda=0 and A_lambda<=2sqrt(lambda)
remain in force.

## 12. The central fiber on a growing time interval

For any fixed 0<gamma<1/2 set

    delta=lambda^3, sigma=lambda^2, T_lambda=lambda^(-gamma),
    p=1/2-gamma, E_lambda=275lambda^p.

The inherited all-T Q16 gives the following finite estimate. Put
H_*=H_D(0), U_delta(tau)=exp[-i tau H_D(delta kappa0)/delta] and
r_delta=delta b^2/4+delta^2 b^3/24. For T>0 and
0<sigma<=min(1/2,5lambda/8),

    e_perp=sup_(|tau|<=T)||F U_delta(tau)chi_lambda-A_lambda u(tau)||
      <=delta[A_lambda(2b+2Tb^2)+(2b+Tb^2)]/sigma
        +A_lambda[4+(7/2)b^2T^2]sqrt(sigma)/sqrt(I0)
        +2sigma C_lambda+(A_lambda+1)T r_delta.            (Q16, imported)

This estimate already annihilates the fast complementary evolution with F;
no infinite-time or arbitrary-vector approximation is asserted. At the
stated scales sigma=lambda^2 is in its domain. Also delta<=1, b=sqrt(3),
r_delta<=delta and T_lambda>=1. Dividing its four terms by A_lambda gives

    e_perp/A_lambda
       <=108delta T_lambda/[sigma sqrt(lambda)]
          +58T_lambda^2 sqrt(sigma)+96sigma/lambda^(3/2)
          +13T_lambda delta/sqrt(lambda)
       =108lambda^p+58lambda^(2p)+96lambda^(1/2)
                                      +13lambda^(2+p)
       <=275lambda^p=E_lambda.                            (G5, imported)

For the first coefficient use b<2, T>=1 and
1/A_lambda<=12/sqrt(lambda):
`(4+8T)+(4+4T)/A_lambda<=108T/sqrt(lambda)`.
For the second use `I0^(-1/2)<4` and `16+42T^2<=58T^2`.
The last two use C_lambda<=4/lambda, A_lambda<=1 and the same lower bound
on A_lambda. All four powers are at least p because 0<gamma<1/2.
This is the complete finite specialization already proved as G5.

Write psi_c(tau)=exp[-i tau H_D(delta kappa0)/delta]chi_lambda and
(u(tau),a(tau))=exp(-i tau A)zeta. The finite G5 estimate gives

    sup_(0<=tau<=T_lambda)
      ||F psi_c(tau)-A_lambda u(tau)||<=A_lambda E_lambda.

Since ||u(tau)||<=1, the difference of squared norms is bounded by
A_lambda^2(2E_lambda+E_lambda^2). Dividing by lambda and averaging yields

    |(1/(lambda T_lambda)) integral_0^T_lambda
           ||F psi_c(tau)||^2 dtau
       -(A_lambda^2/lambda)
           [1-(1/T_lambda)integral_0^T_lambda |a(tau)|^2 dtau]|
        <=8E_lambda+4E_lambda^2.                          (A4)

This uses a vector comparison for the actual evolving state. No norm limit
uniform over arbitrary initial vectors or uncontrolled infinite-time
substitution occurs. Combining A1,A3,A4 gives the finite conditional bound

    |(1/(lambda T_lambda)) integral_0^T_lambda
          ||F psi_c(tau)||^2 dtau-c_A|
       <=8E_lambda+4E_lambda^2+lambda^2
          +4 min(1,C_edge (sqrt(3)T_lambda)^(-4/5)).      (A5)

## 13. A packet with positive momentum volume

For |K|<=lambda/16 use the actual positive projector and define

    phi_(lambda,K)=Pi_++(K)phi_lambda/||Pi_++(K)phi_lambda||,
    n_(lambda,K)=||P phi_(lambda,K)||,
    chi_(lambda,K)=P phi_(lambda,K)/n_(lambda,K).          (B18-B19, imported)

Each positive one-particle projector is (I+ahat.sigma)/2. On the original
support, 5lambda/8<=epsilon<=7lambda/8, and each sine vector changes by at
most |K|/2. The unit-direction inequality
|a/|a|-b/|b||<=2|a-b|/|b| bounds each projector change by
4|K|/(5lambda). Their product therefore changes by at most
8|K|/(5lambda)<=2|K|/lambda. It respects pair antisymmetry.

Its action on phi_lambda is nonzero. Normalizing costs at most twice the
unnormalized distance, so ||phi_(lambda,K)-phi_lambda||<=4|K|/lambda.
The unchanged q support has epsilon<=7lambda/8 and normalized volume at
most lambda^3/3 by the inherited cone-volume bound. Cauchy-Schwarz against the constant singlet gives
n_(lambda,K)^2>=1-lambda^3/3. Both physical projection norms are at least
1/2; the map u -> Pu/||Pu|| is then Lipschitz with constant four on these
unit vectors. Consequently

    ||chi_(lambda,K)-chi_lambda||<=16|K|/lambda.

The two positive free energies together move by at most |K|. Thus the
interior band [5lambda/4,7lambda/4] remains inside [lambda,2lambda], and
phi_(lambda,K) is an actual positive free-band vector. These preparation
statements do not assert free-band confinement after contact projection or
excluded evolution.

Here Pi_++(K) is the tensor product of the positive one-particle
projectors for momenta K/2+q and K/2-q. The physical generator also obeys
`||H_D(K)-H_D(K')||<=|K-K'|`; compression preserves the sine Lipschitz
bound. Bounded Duhamel therefore applies at every finite effective time.
For |kappa-kappa0|<=lambda^2 we have |kappa|<2 and
|delta kappa|<=lambda/16, so all these preparation estimates apply.

Use exactly the actual free-band family G8: eta_lambda=lambda^2,
f_lambda(kappa)=eta_lambda^(-3/2)h((kappa-kappa0)/eta_lambda), with a fixed
smooth h supported in the unit ball and nonzero on an open set, with
integral |h(y)|^2dy/(2pi)^3=1.
Let Phi_lambda(K,q)=delta^(-3/2) f_lambda(K/delta)phi_(lambda,K)(q),
and Chi_lambda=P Phi_lambda/||P Phi_lambda||. The total-momentum support
has center lambda^3 kappa0 and radius lambda^5. The free packet is in the
actual positive free [lambda,2lambda] band before contact projection.

The same bounded Duhamel estimate and B19 give, uniformly in this support,

    ||exp[-i tau H_D(delta kappa)/delta]chi_(lambda,delta kappa)
         -psi_c(tau)||
       <=32delta/lambda+|tau|eta_lambda.                 (A6)

The observable F has norm one and is a fixed fiberwise projection. For
unit vectors the difference of its expectations is at most twice their
norm difference. Thus dividing by lambda and averaging over time costs
at most 64lambda+2lambda^(1-gamma), using the uniform endpoint bound.
The exact global weights are |f_lambda|^2 n_(lambda,delta kappa)^2 /
||P Phi_lambda||^2; they are positive and integrate to one. Integrating
this uniform estimate against those weights is legitimate without
changing the preparation or its probability law.

Set Psi_lambda(t)=exp(-it H_D)Chi_lambda and
H_lambda=T_lambda/delta=lambda^(-(3+gamma)). Define the actual occupation
average over physical time by

    O_lambda=(1/(lambda H_lambda)) integral_0^H_lambda
                     <Psi_lambda(t),F Psi_lambda(t)> dt.

The substitution tau=delta t has dt=dtau/delta and 1/H_lambda=delta/T_lambda,
so both factors cancel exactly:

    (1/(lambda H_lambda))integral_0^H_lambda q(delta t)dt
       =(1/(lambda T_lambda))integral_0^T_lambda q(tau)dtau.

It gives the previous time average with its actual normalization.
Equations A5-A6 yield

    |O_lambda-c_A|
       <=8E_lambda+4E_lambda^2+lambda^2+64lambda
          +2lambda^(1-gamma)
          +4 min(1,C_edge (sqrt(3)T_lambda)^(-4/5)).      (A7)

In particular, using A1=S20,

    |O_lambda-c_A|=O(lambda^min(1/2-gamma,4gamma/5)).      (A8)

Taking gamma=5/18 balances these two error exponents and gives

    H_lambda=lambda^(-59/18),
    O_lambda=1/(8pi^2 I0)+O(lambda^(2/9)).                (A9)

This balance is optimal only for the displayed pair of error exponents
with the already chosen delta and sigma. It is not an optimality theorem
for other scales or other arguments. All constants can be read from A7.

At time zero each actual prepared fiber has F-norm at most 32lambda^2
by A6 and F chi_lambda=0. Therefore <Chi_lambda,F Chi_lambda>/lambda
<=1024lambda^3. Subtracting the initial occupation from the averaged
occupation preserves A9, with that explicit additional error. A9 describes
an O(lambda) physical probability transferred to the fixed transverse
subspace. It does not say that most of the entire normalized packet ends
there.

## 14. Evidence, attribution, and precise claim limits

This composition preserves the entire S4–S21 and A1–A9 mathematics. The
original edge worker supplied the compression/edge route, earlier S21 bound
and edge_controls.py. Root suggested the L^(5/3)/T^(-4/5) improvement. The
recovery worker completed its proof and rate_controls.py. Root then authored
the original-walk occupation implication and occupation_controls.py.

The complete independent spectral-edge review is
`EXCLUDED_WALK_SPECTRAL_EDGE_REVIEW.md`, SHA-256
`8a6741ea9ea890fb9fdece7a8c241fed537a1fe899dafe34f716f1211171bd40`,
with receipt `1cc248fc02fedd81a2e8d9a91d5b8d7157ad9abc18e2a4b5cfa4f8c87954e055`.
It found no mathematical repair in S4–S21. Its reviewer disclosed authorship
of inherited long-time/degenerate premises and did not independently
recertify them. The review did not cover A2–A9.

The occupation composition review is
`EXCLUDED_WALK_AVERAGED_TRANSVERSE_OCCUPATION_REVIEW.md`, SHA-256
`e4f0f730b1d14d1d444e9e22eb0f6995fdc2dab4c130375491d6b61528d2d12a`,
with receipt `4398c9bd17e25281efa1dfd2ae1d5f22eafc8415adc8b2a736a11b45c40b789d`.
It reconstructed A2–A9 before opening the author controls and found no
consequential defect conditional on S20. That reviewer authored S20 and
explicitly did not recertify it; S20's coverage is the separate edge review.
Neither review supplies final review of this new publication composition.

The matching primary is
`scripts/excluded_walk_quantitative_memory_transfer_2026_10_11.py`.
It embeds the complete unchanged edge_controls.py (20 controls),
rate_controls.py (15) and occupation_controls.py (14), verifies their exact
SHA-256 identities and executes them in three separate global namespaces.
It imports no historical helper file at runtime. Required libraries are
SymPy and mpmath. AUDIT_TIMEOUT_SEC=180 records the intended process limit;
the external execution harness enforces it. AUDIT_INPUT_PATHS names this
note and the three prior dependencies in Section 1.

The edge helper is an exact finite cubic compression/projection fixture;
the rate helper has exact Gram/kernel identities and an unrelated parabolic
continuous comparator. Its 50-digit floating comparisons have no certified
error enclosure. The occupation helper checks exact scalar and finite
normalization identities. They are author consistency controls, not torus
quadrature, proof of a continuum spectral law, or independent final review.
The separate source reviews used different controls within their stated
scope; their outcomes remain source-bound, not a substitute for this proof.

The original five edge mutations, three rate mutations and three occupation
mutations, all complete failure logs, and the first rate helper's preserved
missing-parenthesis failure remain unchanged. The successful helpers embed
only the frozen corrected versions; no failed artifact is hidden or replaced.
The reconstruction map identifies every proof-source slice, editorial change,
helper payload and current dependency-note identity. The fresh execution
record binds the exact primary, command, timeout, full log and return code.
The receipt and preservation check bind these files and the old evidence.

The recorded combined execution exited zero in about 1.15 seconds under
the 180-second timeout, with all 49 author controls completed. Its full
stdout and empty stderr are preserved. This outcome is consistency replay.

From a repository root with the stated dependencies installed, reproduce with

```text
python3 scripts/excluded_walk_quantitative_memory_transfer_2026_10_11.py
```

For this external candidate the same basename is in the research directory;
its recorded invocation uses the explicit Python executable in the receipt.
New executions must write fresh logs rather than overwrite the frozen record.

S8 controls actual combined-edge mass; S12 controls the distinct Poisson
proxy. S9 is an inverse-form domain statement, not a positive uniform gap or
a bounded inverse on the whole physical space. S20 controls a time mean;
it proves no pointwise amplitude power, monotonic loss or dissipation.
A7–A9 control the specified actual packet's fixed-F probability with the
given scales. They do not imply a weighted-current convergence rate,
generic-state theorem, stochastic process or many-body transport law.

The earlier memory/current note already establishes selected weighted
asymptotics and a joint growing-time current comparison, and states its
own selected-datum lower bound. Those results are outside the new proof's
scope. This note therefore does not call all weighted-current asymptotics
or all growing-time original-walk control globally open. A rate for the
limiting weighted current and broader preparation-uniform conclusions are
not supplied by the present estimates. No optimal exponent or prefactor,
global novelty result, Lean verification, physical primitive adoption,
publication authorization or retained/audit verdict is claimed.


## Publication evidence and complete parent dependency

The [delivery record](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/ba74c93aab9185d62a9711695dc931446f67c8ba/.claude/science/physics-loops/toe-quantitative-memory-transfer-20261011/DELIVERY_CHECKS.md)
binds the complete root composition check, distinct source reviews, exact
publication edits, canonical cache and actual primary-source mutations.
The historical edge and occupation notes, negative controls and failed
attempts remain preserved losslessly; a source replay is not a new proof.

The complete parent is regular PR #9481 at
d8480b5a6e04102ff076b3dd6f817a2d43f20252, including its parent #9479.
Parent-first or cumulative review from main
a13caa4885f547c8d206265b031ba7649e539fd9 is required before landing.
Flux/form #9480 and stochastic transport #9478 are not premises.
