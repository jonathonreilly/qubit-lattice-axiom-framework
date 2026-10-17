# Scalar three-source local-amplitude stability

ROOT authored candidate, not independently checked. This supplies a time-uniform comparison of ALL THREE source-site amplitudes of the isolated scalar Jacobi chain, including detunings. It does not assert actual attached-device escape or complete robustness.

Use the exact nominal and perturbed scalar source of three_site_source_robustness/PROPOSAL.md (32456b0b5c99ad1acfcdc9a770d022ffcc14069dee157981c715177cfa6a7eb6), qualified by ROOT review ba06cef2ddf0aae45eeaf5f5c8740258babe21d2a8206fbf6c1eb7b3b33f97ad. Its finite-band, no-atom, normalized density and complex coefficient ratio remain conditional inputs. Nominal source a89025dafcb588459e88c14fa802e9e9ce2e5184aa42d9d22f6521a1dadb4823 with review c161daea2f3a126ad84baaa63d975b5d80fd3243f11ca3b1075673f62530245b supplies the exact reference and all-three-site decay. Source geometry/background unchanged is not sufficient to transfer this isolated result.

Write a=a1,0=lambda/sqrt(3), b=a2,0=lambda*sqrt(8/3). Perturbed a1=a sqrt(1+e1), a2=b sqrt(1+e2), |ei|<=epsilon, |di|<=epsilon lambda. Retain lambda/j<=1/16 and chi=[20epsilon+16epsilon^2+4epsilon^3]/(1-3lambda/j)<1, implying epsilon<.05. Define L=[(1+epsilon)^(3/2)-1+chi]/(1-chi) from the checked complex spectral ratio. No centers or phases are fitted.

On delta in [-2j,2j], the density ratio is rho_e/rho_0=|F_e/F_0|^2. Therefore

 |rho_e/rho_0-1| <= D_rho=2L+L^2.

Both measures have mass one and no residual point/singular component, by the qualified scalar result. For the negative-hopping Jacobi operator centered at 2j, the first three orthonormal polynomials are

 p0_e=1,
 p1_e=-(delta-d0)/a1,
 p2_e=((delta-d0)(delta-d1)-a1^2)/(a1 a2).

They follow by applying the spectral transform to the site0 and site1 eigenvalue equations; site2 detuning and the last bond enter the density, not these first two polynomials. Thus the three-site amplitude vector from seed0 is exactly

 v_e(t)=exp(-i2jt) integral exp(-it delta) (1,p1_e,p2_e)^T rho_e(delta) ddelta.

This statement is about scalar source amplitudes, not probability density alone. The common carrier is retained; any identical old-energy/global carrier can multiply both sides later. No unknown input is conjugated.

In the nominal measure rho_0 the three polynomials are orthonormal, so each has L2 norm one and integral ||(1,p1_0,p2_0)||^2 rho_0=3. This can also be checked directly from the spectral theorem and the orthonormal site vectors. In particular integral delta^2 rho_0=a^2=lambda^2/3. All integrals here are over the exact finite band, not a Markov surrogate with divergent moments.

Put alpha=a/a1 and beta=ab/(a1a2). Algebra gives

 p1_e-p1_0=(alpha-1)p1_0+d0/a1,
 p2_e-p2_0=(beta-1)p2_0
              +beta[-delta(d0+d1)+d0d1-a^2 e1]/(ab).

Hence their L2(rho_0) differences have upper bounds

 B1=(1/sqrt(1-epsilon)-1)+sqrt(3)*epsilon/sqrt(1-epsilon),
 B2=[epsilon+(sqrt(3/2)+1/sqrt(8))*epsilon
                                      +(3/sqrt(8))*epsilon^2]/(1-epsilon).

For B1 use |alpha-1|<=1/sqrt(1-epsilon)-1. For B2 use |beta-1|<=epsilon/(1-epsilon), beta<=1/(1-epsilon), ||delta||=lambda/sqrt(3), ab=(2sqrt(2)/3)lambda^2 and |d0+d1|<=2epsilon lambda. This retains linear and quadratic detuning terms. Define Bpol=sqrt(B1^2+B2^2). The vector polynomial difference has L2 norm at most Bpol, and L1 norm at most Bpol because rho_0 has mass one.

Now subtract the exact vector spectral representations in the order

 p_e rho_e-p_0 rho_0=(p_e-p_0)rho_0+p_e(rho_e-rho_0).

Triangle inequality, the pointwise density ratio and Cauchy-Schwarz give, for every real t,

 ||v_e(t)-v_0(t)|| <= Bpol+D_rho*(sqrt(3)+Bpol) = E_local.

The trivial norm bound 2 may replace E_local when smaller. This controls a projection of the scalar evolved state; it is not a full scalar-state or actual attached-state estimate. It is time uniform because all time dependence in this spectral comparison has modulus one. Detuning-dependent resonant phases remain inside the exact density and polynomial expression.

Consequently for t>=0,

 ||v_e(t)|| <= min(1, F(lambda*t)+Evec+E_local),
 F(x)=exp(-x)*sqrt((1+x+x^2/3)^2+(x+x^2)^2/3+2*x^4/9),

using the qualified nominal exact finite-band comparison Evec. No new bound on Evec or numerical tolerance is chosen here. The reference result contains all three source sites, including intermediary population. This is useful even when the perturbed poles split: no individual pole perturbation or critical degeneracy is assumed.

For a later actual-source proof one must still compare the perturbed installed resolvent with this perturbed scalar reference, control full complementary channels, charge a reference truncation and one global actual omitted-state term, and separately handle background/traveling/normalization/finite cut. The actual moment f32b28aba669d09933c9c22052b2abce4d68339f43faa5beac8f3dc4d8ee978d is currently a candidate under distinct checking; it is not used to prove this scalar lemma. No complete output, success probability, useful coefficient tolerance, permanent halt or native supplier follows here.

Exposure: ROOT derived this lemma after reading the full scalar robustness and perturbed-attachment sources and re-reading nominal local escape. The scalar robustness review was ROOT's own earlier work; this new polynomial/density argument requires a distinct reader. No numerical integration, dynamics, sweep, Git/PR, prompt/axiom/model change was performed. Only this candidate file was written.
