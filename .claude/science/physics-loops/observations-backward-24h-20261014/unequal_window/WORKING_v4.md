# Unequal-distance scalar constraint: root working derivation

2026-10-15. Supersedes the prospective sketch only as a working argument;
neither independent confirmation nor empirical validation is implied.
Target: replace M15's ideal equal-epoch covariance history by an expectation
of a smooth weighted pair statistic, without selecting an initial covariance.
Trace: upstream_support to the revised scalar measurement bridge. The field
law, calibrated geometry, statistical homogeneity/isotropy, selection and
measurement-error identifications remain explicit supplied conditions.

## Geometry and elimination

Use physical Jordan N=ln(a), H>0, alpha=1/(aH), chi_N=-alpha. Positions are
x_i=chi_i n_i; r=|x_2-x_1| and mu=n_1.n_2. Work on a compact interior chart
of |chi_1-chi_2|<r<chi_1+chi_2, r>0, with p_1 p_2 nonzero. All N_1
derivatives below fix r and N_2, not the observed angle. Write

    p_1=(chi_2 mu-chi_1)/r, p_2=(chi_2-chi_1 mu)/r,
    C_Su=alpha_2 p_2 J, J=partial_r C_SV,
    C_uu=-alpha_1 alpha_2[p_1 p_2 R_r+(mu-p_1 p_2)R/r],
    R=partial_r C_VV.

This is direct differentiation of an isotropic covariance, not a growth-law
or initial-state model. S belongs to leg1. The supplied local law is
S_1-y V_1=a0 S+c0 V (M14: a0=(y-x-2)/2,c0=-hy-m).
Define

    gamma=(mu-p_1 p_2)/(p_1 p_2 r), P=partial_r+gamma,
    G=-C_uu/(alpha_1 alpha_2 p_1 p_2),
    T=y partial_1+c0, D=partial_1-a0, d=D J.

Then P R=G and T R=d. Let U=partial_chi1 gamma, b=y chi_1,N1,
L=U P-U_r and F=T G-P d. Since [T,P]=b U, F=b U R, hence

    H=L(T G-P D J)-b U^2 G=0.                         (1)

No division by b or U is used in (1). Thus vanishing y or U does not invalidate
necessity, though it can remove information. If bU is nonzero, additional
temporal compatibility can reconstruct R locally; (1) alone is not a
sufficiency or parameter-identifiability theorem. No PSD/full-history
converse is asserted. p_1 p_2=0 remains outside this chart.

## Removing unmeasured angular modes

Let A=chi_1,B=chi_2,delta=A^2-B^2, q_-=r^2-delta,q_+=r^2+delta.
Then p_1 p_2=(delta^2-r^4)/(4ABr^2) and

    gamma=[2r^2(A^2+B^2)-r^4-delta^2]/[r(delta^2-r^4)].

The full-sky shear inverse loses ell0,1. In the isotropic S-u correlation,
the missing terms are arbitrary a(N1,N2)+b0(N1,N2)mu. Dividing by alpha2 p2
maps these into span{r,r/q_-}. A fixed-r N1 derivative adds only r/q_-^2
to that span; arbitrary time-dependent coefficients remain arbitrary.
Thus the nuisance in H lies in span{LP r, LP(r/q_-), LP(r/q_-^2)}.

Exact rational reduction gives denominators respectively q_-^4 q_+^4,
q_-^5 q_+^4,q_-^6 q_+^4. Their numerators are even polynomials with common
r^4 and degrees at most12,8,10 respectively. Therefore with

    W=q_-^6 q_+^4/r^4, K=r partial_r,
    Z=[product_{j=0}^6(K-2j)] W,

ZH is independent of the missing angular coefficients. Multiplication W
acts first. This follows because each W LP nuisance is a polynomial in r^2
of degree at most6, which the seven Euler factors kill. This is an explicit
geometry-derived annihilator; no nuisance coefficients are fitted or supplied.
It also removes some genuine signal. Sensitivity, conditioning and arbitrary
angular masks cannot be inferred from cancellation alone.

## Weak functional in two independent distances

Use compact smooth weights w(N1,N2,r) strictly inside the chart, with measure
dN1 dN2 dr. Formal adjoints are

    Z* w=W product_{j=0}^6(-K-1-2j)w = z,
    P*=-partial_r+gamma,
    L*f=-partial_r(U f)+(U gamma-U_r)f,
    T*f=-partial_1(y f)+c0 f,
    D*f=-partial_1 f-a0 f.

For eta=1/(alpha2 p2), beta=-1/(alpha1 alpha2 p1 p2), set

    K_uu=beta[T*L*z-b U^2 z],
    K_Su=-eta D*P*L*z.                                (2)

Then integral(K_uu C_uu+K_Su C_Su)=0. All derivatives hit weights and
candidate/geometry coefficients; none hit measured correlations. Smooth
compact support removes boundary terms, including moving chart boundaries.
This is an expectation constraint, not an identity for every finite sky
realization. Finite regularity alternatives require their own boundary proof.
The coefficients can be challenged using multiple prespecified weights;
uniqueness or a useful parameter rank has not yet been proved.

For fixed kernels, a supplied pointwise correlation-error envelope gives
|delta I| <= integral(|K_uu|epsilon_uu+|K_Su|epsilon_Su).
Unknown geometry, candidate-dependent kernels and sample variance are not
automatically covered. They require their own delta-kernel/error terms.

## Pullback to measured shear and radial velocities

Use chi1,chi2,mu coordinates. The absolute volume factor is
Jgeom=chi1 chi2/(alpha1 alpha2 r). Put k=Jgeom K for both terms.
Because the nuisance cancellation holds for arbitrary time coefficients,
k_Su has zero angular moments against1 and mu at each chi1,chi2.

On each observable ell>=2 Born mode,
psi_lm(s)=integral_0^s(1/chi-1/s)S_lm(chi)dchi and
S_lm=partial_s(s^2 partial_s psi_lm)=D_s psi_lm. Require the
corresponding integrability near the observer. No finite or known observer
monopole/dipole lensing potential is required or reconstructed. D_s is self-adjoint in ds on
these compact weights. Move it onto k_Su at fixed angular directions, after the coordinate change.
Next use the full-sky spin-2
map gamma_lm=h_l psi_lm, h_l=1/2 sqrt[(l-1)l(l+1)(l+2)], l>=2.
The scalar weight has no l0,1, so its adjoint inverse is well-defined:
divide its harmonic coefficients by h_l and use spin-2 harmonics. Pair the
result with shear by Re(q* gamma). This moves the entire inverse onto a
known smooth weight. It does not reconstruct individual missing modes.
The angular inverse generally destroys compact angular support: full-sky
coverage, or a separately proved masked inverse, is still a condition.

Statistical isotropy converts integral dmu k C into
(1/(8pi^2)) integral dOmega1 dOmega2 k(n1.n2) E[signal1 signal2].
Both source distances stay independent. Unlike an equal-epoch diagonal,
the resulting pair weight contains no delta(chi1-chi2).

## Finite sampling and the remaining physical assumptions

For independent catalogue draws from known positive p_s(chi,n),p_v(chi,n)
with respect to dchi dOmega,
positions independent of the latent field, and measurements conditionally
unbiased and with zero cross-object/cross-channel noise products conditional
on the latent fields and all sampled positions (or with those conditional
products supplied and subtracted), the cross-pair
average of Re(q* e_i) v_j/(p_s p_v) and the ordered distinct velocity-pair
average of k_uu v_i v_j/(8pi^2 p_v p_v) estimate the two integrals above.
q includes D_s and the 1/(8pi^2) angular factor. Their sum has zero ensemble
expectation under the conditional field law. Pair averages use n_s n_v and
n_v(n_v-1), respectively. Integrability must hold; no finite variance or
observational error bar follows from unbiasedness alone.

This is a conditional mathematical supplier for a finite statistic, not a
claim that galaxy positions are field-independent or selection functions,
shear calibration, true distances and peculiar velocities are already known.
Density-biased tracers, correlated noise, intrinsic alignments, redshift
mapping and survey masks require explicit treatment. More pairs do not erase
cosmic variance in a fixed survey. A fixed finite grid cannot exactly integrate
arbitrary smooth correlation functions: a bump between sample points gives
a direct counterexample. Random sampling targets an expectation instead.

Next: exact rational geometry/annihilator controls, nonzero sensitivity
witness, independent weak/pullback checks and finite-sample expectation tests.
The first root geometry check is separate from the independent weak/pullback
check. A reviewer identified the need to condition the noise-product premise
on fields and sampled positions; that qualification is explicit above.
No empirical dataset has been opened for this block. Do not call this result
an observed scalar signal, derived initial state/action/scale or completed TOE.

## Nonvacuity on a positive covariance family

Let g(x)=sqrt(2) cos(k.x+theta), theta uniform and k~N(0,2lambda I),
lambda>0 independent. This bounded homogeneous/isotropic ensemble has
C_g(r)=exp(-lambda r^2), so positivity is established by an explicit random
field rather than an arbitrary radial function. Take V=e^N g and
S=[(y+c0)/(1-a0)]e^N g with constant y,a0,c0, a0!=1. The supplied local law
holds. For example y=2/5,a0=-83/100,c0=-3/5 with alpha=1,h=-1 corresponds
to x=3/50,q=3/20,m=1 at the coefficient level. No full gravity/background
solution is asserted; this is a kinematic field-law witness.

Changing only the tested c0 by dc changes the final constraint by
dc Z L P R, where R=-2lambda r exp(-lambda r^2)e^(N1+N2). After removing
the positive time factor and Gaussian, WLP R is an even polynomial of degree16
in r, with leading coefficient32 chi1 lambda^3. Applying the seven Euler
factors gives degree30 with leading coefficient -4096 chi1 lambda^10.
Thus the operator does not vanish on this positive-covariance family.
The checked interior point chi1=2,chi2=3,r=5/2,lambda=1/2 has nonzero response.
A compact sign-consistent weight in a sufficiently small neighborhood then
has nonzero expectation for that wrong candidate. This proves existence of
a discriminator, not parameter uniqueness, useful signal/noise, full-solution
embedding or success on an observed survey.

Root geometry v3 has43 passing controls, including this witness. Geometry v2
was terminated after172seconds of expensive expanded symbolic algebra; no
assertion failed and no result file was produced. The same Gaussian witness
was recomputed with exact conjugated polynomial operators, preserving v2.
Root weak/sampling v1 has30 passing exact controls; v2 additionally checks
full-sky spin normalization through explicit Legendre integrals. These are
mathematical tests, not independent observations.
