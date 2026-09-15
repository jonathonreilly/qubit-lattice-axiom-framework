# Block26: fixed-clock transverse spectral concentration

Personal working derivation, 2026-09-15. This is a new conditional implication
of the proposed periodic finite-clock covariance theorem in PR8127, not an
independently checked phase theorem. No Gaussianity, isolated particle pole,
selected native law, or exact photon dispersion is assumed or concluded.

The target is quantitative information about the actual isotropic clock
model's reconstructed energy spectrum at fixed N and fixed coupling. The
method is elementary positive spectral-measure algebra. Its useful addition
to the existing gaplessness result is a band of energies proportional to
spatial momentum with two nonvanishing transverse response directions.

## 1. Exact input and provenance

The model is the four-dimensional periodic finite-clock Villain law

    theta_e in 2 pi Z/N modulo 2 pi,
    probability(theta) proportional to product_p phi_beta((d theta)_p),
    phi_beta(t)=sum_n exp(-n²/(2 beta)) exp(i n t),
    beta_d=N²/(4 pi² beta).

Fix beta,beta_d >=2000 and any local limit along equal even tori. The
substantial provisional input is the complete proposed theorem in
`docs/PERIODIC_FINITE_CLOCK_VILLAIN_COVARIANCE_AND_OBSERVABLE_MASSLESSNESS_BOUNDED_THEOREM_NOTE_2026-09-14.md`
at PR8127 head `d46526dc07fc1f4f6530c7b4d98c1d5feb8f6eee`. Its full790-line
source was reread for this block. In particular we require its all-affine
covariance argument, physical contact identity, and site/link reflection
positivity in the same infinite-volume state. Independent review is pending.

Write P_e,P_c for the infinite-volume exact/coexact two-form projections.
The input gives a bounded positive Fourier density C_n/beta with

    (1-delta(beta)) P_c <= C_n/beta
       <= P_c+delta(beta_d)P_e,     C_n/beta <= I.       (1)

Here delta(s) is exactly the upstream explicit function:

    b1=(107 log3+log4)/(4 pi²), a(s)=s/384-b1,
    q(s)=exp(-2 pi² a(s)), S_j(q)=sum_(r>=1) r^j q^r,
    delta(s)=s[8503056 S_6(q(s))+262144 S_5(q(s))]/[a(s)e].

Finite torus harmonics have already been kept and removed in the local
limit by the input. They are not discarded at finite volume here.

The physical bounded observable is Y_p=-phi_beta'/[sqrt(beta)phi_beta]
at the clock plaquette angle. Put B=(Y_23,-Y_13,Y_12). These three spatial
plaquettes are even under time reflection and live on integer time slices.
Charge conjugation of the specified periodic-limit state centers all scores.

## 2. Physical covariance is uniformly close to the exact projector

Augment the clock law by independent conditional Gaussian image integers:
X_p=sqrt(beta)((d theta)_p-2 pi m_p). Its joint marginal is a centered
Gaussian on a full-rank lattice, with covariance at most I. More strongly,
completion of the square and the nonnegative Fourier coefficients of its
theta function give E exp(h.X)<=exp(||h||²/2). This centered MGF bound uses
only finite-dimensional Poisson summation, not the all-affine input.
Explicitly, write theta=2 pi a/N with integer link representatives. The
integer field z=d a-N m ranges over M_N=N Z^P+d Z^E, and each admissible z
has the same number |ker(d mod N)| of clock/image preimages. Thus
X=z/sqrt(beta_d) has precisely the centered Gaussian law on this full-rank
lattice. Finite Poisson duality from the input gives Cov(X)=I-C_n/beta.

Conditional on theta, image integers on distinct plaquettes are independent,
Y=E[X|theta], and v_p(theta)=Var(X_p|theta)>=0. Translation and cubic
invariance give a common vbar=E v_p. Total covariance and the exact duality
just stated give

    C_Y=(1-vbar)I-C_n/beta.                            (2)

For completeness a uniform explicit bound on vbar follows from the same
centered MGF. Let v be the principal flux angle. If |X_p|<pi sqrt(beta),
then sqrt(beta)v=X_p. Otherwise their difference has magnitude at most
2|X_p|. Conditional expectation minimizes squared prediction error, so

    vbar <=4 E[X_p² 1_(|X_p|>=pi sqrt(beta))]
          <= (8 pi² beta+16) exp(-pi² beta/2)=eta(beta). (3)

The last inequality integrates the Chernoff bound
Pr(|X_p|>=u)<=2 exp(-u²/2). Conditional image variances are bounded functions
of the finite clock angle, so this bound passes to every specified local
limit. We do not need to reconstruct an infinite-volume image process.

Set R=C_n/beta-P_c and

    epsilon=max(delta(beta),delta(beta_d))+eta(beta).

Equation(1) implies -delta(beta)I<=R<=delta(beta_d)I. Therefore

    ||C_Y(k)-P_e(k)||_op <= epsilon                  (4)

for almost every four-momentum k. The contact contribution -vbar I is
retained. No assumption that the score itself is a closed two-form is made.

## 3. Spatial midpoint convention and the transverse block

Fourier transform every spatial plaquette using its spatial midpoint. The
change from lattice-origin Fourier coordinates is a diagonal unitary
depending only on spatial momentum p, so it preserves positivity of the
time spectral measure. Put

    xi_i=2 sin(p_i/2), r²=sum_i xi_i², w²=4 sin(omega/2)²,
    P_T=I-xi xi^T/r², r>0.

In midpoint coordinates the coboundary symbol is exterior multiplication
by i(2 sin(omega/2),xi). Direct exterior algebra gives

    [P_e(omega,p)]_BB = r²/(r²+w²) P_T.

Let S_p(w²) be the compression of the physical B covariance density to
the two-dimensional range of P_T. Equation(4) yields

    ||S_p(z)-[r²/(r²+z)] I_T|| <= epsilon,
    z=4 sin(omega/2)².                              (5)

This holds initially for almost every (omega,p). The spectral representation
below supplies the continuous version at z>0 and the monotone value at z=0.
The longitudinal compression obeys 0<=S_L(z)<=epsilon as well. Small
longitudinal response is allowed; it is not claimed to vanish exactly.

## 4. The positive transfer spectral measure, including contact states

Use the site-reflection OS space on gauge-invariant functions supported at
times >=0. The upstream construction gives a positive self-adjoint
contraction T and commuting spatial translation unitaries. For the B
observables on time0, their reflected inner product equals their ordinary
equal-time covariance. In particular, for t>=0,

    E[B_i(0,0) B_j(t,x)] = ([B_i],T^t U_x[B_j]).       (6)

This identity has no one-time-step displacement: that displacement was
needed upstream for general slabs including temporal plaquettes. Here the
observables lie on the reflection plane and are time-even.
Time-reflection invariance makes their negative-time covariances equal to
the corresponding positive-time ones, justifying the two-sided sum below.

The joint spectral theorem for T and spatial translations produces a
positive3x3 matrix measure on [0,1] x the spatial Brillouin torus. Its
spatial marginal is the equal-time covariance, which has a bounded Fourier
density by(4). Hence the joint measure disintegrates as dnu_p(lambda) dp
with the normalized spatial Haar measure understood. Compress nu_p to the
transverse plane. All following matrix inequalities hold for almost every p.

An atom at lambda=1 would create a temporal Fourier atom at omega=0,
contradicting the bounded four-dimensional density. It has zero measure.
An atom at lambda=0 is allowed: it contributes only at t=0 and therefore
a constant Fourier density. This is an infinite-energy/contact component,
and is retained until the positive localization estimate bounds it.

For 0<lambda<1 put E=-log(lambda). Summing the two-sided geometric series
gives the Poisson kernel

    sum_(t in Z) lambda^|t| exp(i omega t)
      =(1-lambda²)/(1-2lambda cos(omega)+lambda²)
      =sinh(E)/(cosh(E)-cos(omega)).                   (7)

The kernel is nonnegative and has normalized temporal integral1. Tonelli
and uniqueness of Fourier coefficients identify its integral against nu_p
with the covariance density. The kernel is uniformly bounded for omega
separated from0, giving continuity there. Consequently(5), originally an
almost-everywhere inequality, holds at every0<z<=4 for almost every p.

Use the energy coordinate u=4 sinh(E/2)². Reweight the measure by

    dchi_p(u)=coth(E/2) dnu_p(E) for E in(0,infinity),
    chi_p({infinity})=nu_p({lambda=0}).

Then the exact Stieltjes representation is

    S_p(z)=int_[0,infinity] [u/(u+z)] dchi_p(u),       (8)

where the integrand at infinity is1. As z decreases to0, monotone
convergence and(5) show that chi_p is finite, with

    (1-epsilon)I_T <= chi_p(total) <= (1+epsilon)I_T.  (9)

There is no mass at E=0. Possible unbounded weight near E=0 is ruled out
by this same bound, not by assuming an energy gap. Equation(8) at z=0
means its finite monotone limit. This chi is the static susceptibility
measure; it is different from the ordinary OS spectral weight nu.

## 5. A positive two-frequency localization identity

Fix0<r<=1 and set a=r², so the two frequencies z=a and z=4a are available
on the lattice. For x>=0, including x=infinity by its limit, define

    Phi(x)=(x-1)²/[(x+1)(x+4)]
          =1/4-(4/3)x/(x+1)+(25/12)x/(x+4).          (10)

This identity is exact. Phi>=0, Phi(1)=0, Phi(infinity)=1, and

    Phi'(x)=(x-1)(7x+13)/[(x+1)²(x+4)²].

It decreases on[0,1] and increases on[1,infinity]. Substituting(8) gives

    0 <= int Phi(u/a) dchi_p(u)
      = chi_p(total)/4 -(4/3)S_p(a)+(25/12)S_p(4a)
      <= (11/3)epsilon I_T.                         (11)

The reference values1,1/2,1/5 cancel exactly. The upper bound is the sum
of three norm errors with total coefficient1/4+4/3+25/12=11/3. Positivity
comes from the integral, despite the negative coefficient in this linear
combination. No derivative or analytic continuation of noisy covariance
data is required.

For0<alpha<1<gamma let

    m(alpha,gamma)=min(Phi(alpha),Phi(gamma))>0,
    I_r=[alpha r²,gamma r²], K=11/[3m(alpha,gamma)].

Equation(11) and the monotonicity of Phi imply

    chi_p(I_r^c) <= K epsilon I_T,
    chi_p(I_r) >= [1-(K+1)epsilon] I_T.             (12)

The complement includes the contact atom at infinity. For every unit
transverse v the fraction of its static susceptibility in I_r is at least

    1-K epsilon/(1-epsilon).                        (13)

This is a statement for positive scalar compressions v*chi_p v; no quotient
of noncommuting matrices is used.

## 6. Ordinary spectral weight and two energy-response directions

Transforming I_r back to energy gives

    J_r=[2 asinh(sqrt(alpha)r/2),
         2 asinh(sqrt(gamma)r/2)].                   (14)

Because dnu=tanh(E/2)dchi, equations(9),(12) give

    sqrt(alpha)r/sqrt(alpha r²+4) [1-(K+1)epsilon]I_T
        <= nu_p(J_r)
        <= sqrt(gamma)r/sqrt(gamma r²+4)(1+epsilon)I_T. (15)

If the lower coefficient is positive, the map from a transverse source v
to its band-projected OS vector is injective. Thus the energy band has two
nonzero response directions for almost every such p. Wave packets with
measurable transverse polarizations give actual Hilbert-space vectors;
point-momentum plane waves are not claimed normalizable eigenvectors.

The interval endpoints are asymptotic to sqrt(alpha)|p| and
sqrt(gamma)|p| as p->0. Both bounds on ordinary band weight are proportional
to r. The conclusion is quantitative low-energy spectral concentration,
not merely the existence of spectral values approaching zero.

Most *static susceptibility* in the band does not imply most equal-time
OS norm there. A small contact weight of order epsilon can dominate a band
weight of order r as r->0. Equation(15) preserves this distinction.

## 7. A fixed-parameter certificate

The upstream delta bound can be sharpened using only elementary rational
inequalities, without estimating a critical coupling. For s>=2000,
log3<11/10, log4<7/5 and pi>157/50 give b1<31/10. Hence

    a(2000)>253/120, 2000/a(2000)<1000,
    2 pi² a(2000)>6236197/150000>59(7/10)>59 log2.

Thus q<2^-59, and s/a(s) decreases with s. The upstream rational identities
for S_5,S_6 imply S_j(q)<=2q for q<=1/1024. Using e>2,

    delta(s)<8765200000/2^59 <1/50000000.             (16)

Also eta(beta) decreases for beta>=2000. The bounds3<pi<4 and e>2 give
eta(beta)<256016*2^-9000 <1/50000000. Consequently the deliberately loose
choice epsilon_*=1/10000000 bounds epsilon for every admitted beta,beta_d.

Take alpha=9/10 and gamma=11/10. Then

    m=1/1071, K=3927,
    chi_p(I_r)> (1-3928/10000000)I_T,
    [v*chi_p(I_r)v]/[v*chi_p(total)v]>0.9996 for every v!=0. (17)

The last line is the scalar ratio in(13) on the transverse plane.
Over99.96 percent of each transverse static susceptibility is therefore
in the energy band(14). As momentum tends to0 its lower and upper slopes
are3/sqrt(10) and sqrt(11/10), approximately0.94868 and1.04881 in the
supplied isotropic units. The example beta=2000,N=16384 remains a fixed
finite clock model satisfying the required dual inequality.

The constants are sufficient bounds for this particular model. They are
not measured speeds, a selected physical normalization, or transition
estimates. Exact E=|p| is not inferred from a narrow interval.

## 8. What this still permits

A positive spectral distribution spread continuously through J_r can meet
the same bounds. The argument does not force a spectral atom, stable
one-particle states, Gaussian joint laws, exactly two total polarizations,
a unique infinite-volume phase, or a local continuous-time Hamiltonian.
It does not bound a group velocity or prove coherent wave-packet transport.
It does identify two robust transverse directions with linear energy scale
in the actual isotropic OS state, conditional on the stated covariance input.

The finite-clock Gaussian limit with both defect species remains open. So
does the selected N=3 penalty-Hamiltonian phase, and the framework's native
law/observable identification. No axiom change is requested or forced.

A precise control preserving the distinction from a pole takes chi uniform
on u in[a(1-h),a(1+h)], with0<h<1. For z>=0 its Stieltjes function is

    S(z)=1-z/(2ah) log[(a(1+h)+z)/(a(1-h)+z)],
    S(0)=1.

Put b=ah/(a+z). Expanding atanh(b)/b shows

    0<=a/(a+z)-S(z)
      =z/(a+z)[atanh(b)/b-1]
      <= z a² h²/[3(a+z)^3(1-h²)]
      <=4h²/[81(1-h²)].

The last step maximizes x/(1+x)^3 at x=1/2. At h=1/1000 this is below
1/10000000 for every z, but the energy measure has no atom. This is an
abstract positive spectral control, not a claimed alternative realization
of the full four-dimensional clock law. Likewise a Gaussian scale mixture
with equiprobable squared amplitudes1/2 and3/2 has unit variance and fourth
moment15/4. Two-point data do not establish its Gaussianity. Neither control
is used as an axiom obstruction or an assertion about the clock's actual
higher-point functions.

## 9. Reading and intended falsifiers

The covariance source above was read completely. Its companion varying-law
Gaussian source was inspected for the exact image/MGF/score bounds and
reconstruction scope; no fixed-law Gaussian result is imported from it.
Hao Shen, arXiv1311.2305v2, opening through Proposition1 was read as a
possible RG route. It concerns a scalar-gradient dipole model; no theorem
is imported into the clock model here.

Kouta Usui, arXiv1201.3415v3, opening through Theorem2.1 and the initial
reconstruction section was read as primary spectral-representation context.
Section3.3 was also read in full: adding site positivity to the author's
link-based reconstruction gives a positive transfer at every integer time.
That theorem's link-only statement concerns odd time separations. Here
both site and link positivity are explicit, and the time0 identity(6) is
derived for spatial plaquettes. A source-scope check is required before any
stronger literature import; none is used for the concentration estimate.

Eight finite families check these distinctions in the companion private
runner. Sixteen actual source faults are caught. The one-plaquette image
and Fourier score comparison initially exceeded a1e-13 tolerance because
of double-precision cancellation. Its source and failure are preserved in
review/BLOCK26_INITIAL_CONTACT_CHECKER.py.txt and
review/BLOCK26_INITIAL_CONTACT_FAILURE.json. The same comparison at65-digit
precision agrees below1.5e-62; its final tolerance is1e-55. No tolerance
was relaxed. These are finite truncated sums, not certified infinite-series
error bounds, and no phase simulation is claimed.

Finite checks supplement this analytic implication; they do not validate
the arbitrary-volume upstream covariance proof. No independent review has
occurred. This draft remains private pending the complete author cold read
and a decision on whether the new implication warrants a public milestone.
