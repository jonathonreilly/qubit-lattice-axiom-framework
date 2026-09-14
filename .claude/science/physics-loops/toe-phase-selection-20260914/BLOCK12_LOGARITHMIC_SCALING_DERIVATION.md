# Logarithmic finite-clock scaling and the global defect-removal boundary

Personal proof draft, 2026-09-14. Independent review pending. Builds on the
integer geometry and model definitions in the direct Maxwell/Wilson source
at commit44faa4d4ce09b8634726cef62a84146f940eb233 (PR8130), explicitly
provisional. No affine-covariance theorem premise. No fixed-law phase or
axiom contradiction is asserted.

## 1. Target and leverage

Replace the sufficient beta=64L^4,N=8beta family by beta of order log V and
N=8beta, where V=L^4 on equal even four-tori. Preserve Gaussian scaling of
actual bounded score fields and relative Wilson loops. Diagnose why this
GLOBAL defect-removal method cannot prove a fixed-coupling phase.

Definitions: K=d_1 Z^E is saturated in S=im d_1; M=K+NZ^P;
sigma=N^2/(4pi^2 beta); X=z/sqrt(sigma) for z in M with centered Gaussian
weight exp(-|z|^2/(2sigma)). The exact positive lift has z=da-Nk and
X=sqrt(beta)(dtheta-2pi k). Conditional on the clock angles, all integer
image labels k_p are independent discrete Gaussians.

Write P_e for projection on S, and P_h for the six harmonic plaquette
modes. There are 4V edges,6V faces,4V elementary three-cubes.

## 2. Centered Gaussian domination and local defect tails

Completing the square for the full-rank lattice M gives

 E exp(<h,X>) = exp(|h|^2/2) Z_M(-sqrt(sigma)h)/Z_M(0)
              <= exp(|h|^2/2).

The last inequality is the centered theta maximum: Poisson summation has
positive Gaussian Fourier coefficients, so the real shifted theta is at
most its value at zero. This is valid for every real h, with no covariance
or phase premise. Hence for any real vector v and u>=0,

 Pr(|<v,X>|>=u) <= 2 exp(-u^2/(2|v|^2)).

For one oriented three-cube c, dX_c=-2pi sqrt(beta) (dk)_c. The incidence
vector d_2^*1_c has exactly six coefficients +/-1 and squared norm6.
Thus

 Pr((dk)_c !=0) <= 2 exp(-pi^2 beta/3),
 Pr(dk !=0) <= 8V exp(-pi^2 beta/3).                     (2.1)

If dk=0, integer periods of k are six integers kappa_{mu nu}. On equal
four-tori the unit harmonic form h_{mu nu} has value L^-2 on every face
of its orientation, so <k,h_{mu nu}>=kappa_{mu nu}. The exact part dtheta
has zero harmonic projection. Therefore

 Pr(dk=0 and P_h X !=0) <= 12 exp(-2pi^2 beta).          (2.2)

If both dk and the harmonic periods vanish, X is real exact and the
saturation of K makes z an element of K. Conversely z in K implies these
conditions. Consequently

 p_bad := Pr(z not in K)
 <= min(1,8V exp(-pi^2 beta/3)+12 exp(-2pi^2 beta)).      (2.3)

This uses local integer defect quantization instead of packing the entire
perpendicular lattice in dimension3V+3. It retains harmonic sectors.

## 3. Integer-current theta bound

For w in K^* subset S, a=d_1^*w is in Z^E: <a,e>=<w,d_1 e> is an integer
for every unit edge. The map is injective, because a=0 with w in im d_1
forces w=0. In Fourier coordinates ||d_1||<=4, hence |a|<=4|w|.
Thus for t>0,

 sum_{w in K^*,w!=0} exp(-t|w|^2)
 <= theta_1(t/16)^(4V)-1,
 theta_1(u)=sum_{n in Z} exp(-u n^2).                  (3.1)

The right side overcounts many currents, but is explicit. For u>=1,

 theta_1(u)-1 <= 2 exp(-u)/(1-exp(-3u)) <= 3exp(-u).

The first inequality uses n^2>=1+3(n-1) for n>=1; the second is strict
already at u=1. Therefore define

 eta_sigma := theta_1(pi^2 sigma/16)^(4V)-1
 <= exp(12V exp(-pi^2 sigma/16))-1                      (3.2)

when pi^2 sigma/16>=1. The exponential in the written finite sum is
controlled analytically; numerical truncation is not a tail proof.

## 4. Uniform shifted relative characteristic estimates

For b in S the affine discrete Gaussian on b+K, normalized with variance
sigma, has characteristic C_b(h), for h_e=P_e h. Poisson summation gives

 C_b(h)/G(h)
 = [1+sum_{w!=0} exp(-2pi^2 sigma|w|^2
                +2pi sqrt(sigma)<w,h_e>) exp(2pi i<w,b>)]
   /[1+sum_{w!=0} exp(-2pi^2 sigma|w|^2) exp(2pi i<w,b>)],
 G(h)=exp(-|h_e|^2/2).                                 (4.1)

Changing w to -w reverses the source and phase signs together. Reversing
only one generally changes the answer; the source term is REAL.
Two alternative sufficient source conditions control the numerator tail:

(A) |h_e|<=pi sqrt(sigma)/8. Since each nonzero w has length>=1/4,
    2pi sqrt(sigma)|<w,h_e>|<=pi^2 sigma|w|^2.

(B) Put psi=(d_1^*d_1)^+ d_1^*h. Then <w,h_e>=<a,psi>. If
    ||psi||_infinity<=pi sqrt(sigma)/32, integrality gives
    |a|_1<=|a|^2, and

 -2pi^2 sigma|w|^2+2pi sqrt(sigma)<a,psi>
 <= -pi^2 sigma|a|^2/8+pi^2 sigma|a|_1/16
 <= -pi^2 sigma|a|^2/16.

In either case the numerator tail is at most eta_sigma; so is the
denominator tail. If eta_sigma<1 then, uniformly in every b,

 |C_b(h)/G(h)-1| <= 2eta_sigma/(1-eta_sigma).            (4.2)

The full M law is a positive mixture of these affine K laws with fixed
perpendicular representatives. Its exact coset has no perpendicular
source phase, and the other phases have unit modulus. Hence

 |E exp(i<h,X>)/G(h)-1|
 <= 2p_bad+2eta_sigma/(1-eta_sigma).                    (4.3)

This bound controls a relative error even if G(h) tends to zero. The
perpendicular-source contribution is bounded by2p_bad rather than by an
absolute error subsequently divided by a small Gaussian expectation.

## 5. Logarithmic sequence and actual local fields

For V=L^4 and even L>=4 take

 beta=ceil(4 log(2V)), N=8beta, sigma=16beta/pi^2.       (5.1)

These are finite clock alphabets, varying only logarithmically with V.
Here pi^2 sigma/16=beta and

 eta_sigma <= exp(3/(4V^3))-1,
 p_bad <= 8V(2V)^(-4pi^2/3)+12(2V)^(-8pi^2).

Both vanish. Any bounded-L2 source family satisfies(A) eventually. With
spacing a->0 and physical side aL->infinity, cell-average sources
(J_a f)_p=a^-2 integral_{cell(p)}f satisfy ||J_a f||<=||f||. The precise
midpoint Hodge/Riemann-sum argument in PR8130 yields

 <J_a f,P_e J_a g> -> <f,P_Maxwell g>.

The bounded physical score Y=-phi_beta'(dtheta)/(sqrt(beta)phi_beta(dtheta))
is E[X|theta]. The conditional independent Gaussian images give

 E|<h,X-Y>|^2 <= (8pi^2 beta+16)exp(-pi^2 beta/2)||h||^2.

Thus the characteristic limit in(4.3) transfers to Y. Conditional Jensen
also gives E exp(<h,Y>)<=exp(||h||^2/2), uniformly in V. These real MGF
bounds give uniform integrability of every fixed smeared moment. The score
field converges with all joint moments to the same Gaussian Maxwell field.
Uniform test variance and the local Sobolev trace/compact embedding argument
in PR8130 give convergence as local H^-s random distributions for s>2.

For the principal-flux field R=sqrt(beta)principal(dtheta), R=X whenever
all |X_p|<pi sqrt(beta). The exceptional probability is

 p_wrap <= 12V exp(-pi^2 beta/2).                       (5.2)

Hence the finite-dimensional limit also transfers to R. For its local
Sobolev tightness, use |R_p|<=|X_p| and Gaussian moment bounds to obtain

 E|<h,X-R>|^k <= C_k (6V)^(k/2)||h||^k sqrt(p_wrap).     (5.3)

At k=2 the right side tends to zero along(5.1), giving uniform test
variance and the same local H^-s tightness. This deliberately does NOT
claim all principal-flux moments from(5.3): at coefficient4 that bound
only proves convergence of total-degree k moments when k+1<2pi^2, in
particular integers k<=18. All score moments do converge. For a prescribed
finite K, replacing4 by any C>max(1,2(K+1)/pi^2) proves principal moments
through degree K by the same argument. A single beta growing faster than
log V, such as ceil(log(2V)^2), makes(5.3) vanish for every fixed k, but
is a different specified family.

The explicit positive-time Gaussian Gram/Wick construction of PR8130
therefore applies to the limiting field, with two transverse linear modes
and energy |p|. No statement about fixed-parameter photon dispersion follows.

## 6. Thin Wilson loops: bounded current potential

Condition(A) alone does not cover every allowed continuum sequence. For a
nondegenerate fixed rectangle, nonzero g and polynomially growing boxes,
for example L of order a^-2, the source h=qS/sqrt(beta) satisfies

 |P_e h|^2=(q^2/beta)<j,G_L*j> >= (q^2/(16beta))|j|^2,

because the nonzero lattice Laplacian eigenvalues are at most16. The loop
has |j|^2 of order a^-1, while sigma is only of order log(1/a), so(A)
eventually fails. On much faster-growing boxes(A) might hold; no universal
failure is claimed. Condition(B) covers the required loops for every
allowed a->0,aL->infinity sequence.

Let G_L be the zero-mode-subtracted scalar inverse Laplacian. The heat
kernel bounds derived in PR8130 extend uniformly to the torus as

 |G_L(n)| <= C/(1+dist_L(n,0)^2)+C/L^2.                 (6.1)

For dist<=L/4, use the infinite-kernel bound plus O(L^-2) comparison already
derived there. For dist>L/4, split the heat integral at L^2: the small-time
image sum has off-diagonal distance of order L and integrates to O(L^-2),
the subtracted zero mode on that interval is L^-2, and the large-time
nonzero Fourier modes integrate to O(L^-2). Thus no divergent sum of Green
images is taken.

For any straight axis segment with at most L distinct edges, summing the
first term in(6.1) along that segment is at most the convergent circle-line
sum sum_{r in Z} C/(1+r^2), with at most a fixed multiplicity. The second
term contributes at most C/L. Therefore

 sup_x sum_{y in segment}|G_L(x-y)| <= C_line,          (6.2)

with C_line independent of L and segment length. This controls the near
self singularity; it does not require two loops to be separated.

For a contractible rectilinear loop j=d_1^*S with at most J straight
segments and integer charge q, h=qS/sqrt(beta) has

 psi=(d_1^*d_1)^+ d_1^*h=(q/sqrt(beta))G_L*j,
 ||psi||_infinity <= C_line J |q|/sqrt(beta).           (6.3)

The scalar Green identity uses divergence-free and harmonic-free j; it is
not valid for arbitrary edge currents. Rounding q to g sqrt(beta) keeps the
right side bounded for each supplied finite g. A fixed finite collection
of such loops also has bounded total source potential. Since sigma->infinity,
condition(B) eventually holds for all individual and joint sources.

The exact integer character W_q(C)=exp(iq<j,theta>)=exp(i<h,X>) and the
surface-independent pairing <P_e S_i,P_e S_j>=<j_i,G_L*j_j> are unchanged.
Using(4.3) before dividing expectations controls their ratios even as the
self expectations vanish. For separated loops with positive physical gap,
the off-diagonal Green limit of PR8130 and ordinary edge Riemann sums give

 E(W_1 W_2)/(E W_1 E W_2)
 -> exp[-g_1 g_2 integral_{C_1}dx_mu integral_{C_2}dy_mu
                     /(4pi^2 |x-y|^2)].               (6.4)

The same subsequent long-time rectangular and return-charge limits give
Coulomb interaction g_1 g_2/(4pi R) for the external charges. Limit order,
integer charge condition and positive separation remain essential. This
constructs neither dynamical charged states nor a native matter law.

## 7. A lower bound on defects and the limit of this method

For a single image label conditioned on theta, write t=dtheta_p/(2pi).
Its mass at k is proportional to exp[-2pi^2 beta(k-t)^2]. A nearest integer
k_0 is a mode. One of its adjacent integers has relative weight at least
q_beta=exp(-2pi^2 beta): choose the neighbor towards t, including either
when t=k_0. Thus every atom has mass at most

 m_beta = 1/(1+q_beta), eta_beta=1-m_beta>0.            (7.1)

Take the V/16 three-cubes of orientation(0,1,2) whose four base coordinates
are all even. Their face supports are disjoint. Choose one special face
in each. Conditional on theta and all other k labels, the special labels
remain independent. Vanishing dk at a selected cube fixes its special
integer to at most one value. Hence

 Pr(dk=0) <= m_beta^(V/16),
 Pr(z in K) <= m_beta^(V/16).                          (7.2)

Moreover the count D of defective selected cubes stochastically dominates
Binomial(V/16,eta_beta), by conditioning the independent Bernoulli indicators
and using their uniformly lower-bounded success probabilities. In particular

 E D >= eta_beta V/16,
 Pr(D<=eta_beta V/32) <= exp(-eta_beta V/128).          (7.3)

The latter is the elementary multiplicative Chernoff estimate with deficit
one half. No unconditional independence of defects is asserted.

For every FIXED beta>0,N>=2 the global exact-sector probability therefore
tends to zero exponentially in V. More generally it tends to zero whenever
V exp(-2pi^2 beta(V))->infinity. If that global probability is bounded
away from zero, (7.2) forces beta(V)>=log V/(2pi^2)-O(1).
This is a necessary scale for GLOBAL defect exclusion, not a necessary
scale for a massless phase or Maxwell infrared limit.

There is a parallel bound for the chosen uniform theta-smallness strategy.
Choose V/16 plaquettes of one orientation with all base coordinates even.
Their edge boundaries are disjoint. For any integer coefficients n_j,
w=P_e sum_j n_j 1_{p_j} is in K^*, and the map from coefficients is
injective because d_1^*w=d_1^*sum_j n_j1_{p_j} has disjoint nonzero
boundaries. Orthogonal projection gives |w|^2<=sum_j n_j^2. Therefore

 sum_{w in K^*} exp(-2pi^2 sigma|w|^2)
 >= theta_1(2pi^2 sigma)^(V/16).                       (7.4)

At fixed sigma this theta sum grows exponentially. Making its nonzero tail
tend to zero requires V exp(-2pi^2 sigma)->0. Thus sigma must also grow
at least logarithmically for this particular uniform small-tail method.
With sigma=N^2/(4pi^2 beta), simultaneous global requirements imply
N at least of logarithmic order. Equation(5.1) supplies a sufficient
logarithmic-order family with deliberately loose constants.

These lower bounds do not refute fixed-law Gaussianity. An infrared
limit can average a positive dilute defect density and acquire a
renormalized stiffness. A local connected-correlation, Ward-identity,
homogenization or multiscale argument would have to replace global defect
exclusion. Which of these applies to the selected finite-clock model
remains open; no exhaustion or independent-wall claim is made.

## 8. Pending checks and primary comparison

Need challenge local cube norms and disjoint supports, conditional atom
bound, injected integer-current maps, source-potential constants, shifted
complex Poisson identity and logarithmic parameter arithmetic. Compare
thin-loop source norms and potentials across refinements. Preserve a
principal-moment boundary test so all-moment transfer is not accidentally
claimed. This is analytic proof work, not a numerical phase simulation.

A primary search found Driver, Commun.Math.Phys.110(1987)479-501, on a
fixed-coupling compact U(1) current-sector scaling limit. Only its abstract
has been read so far. Its continuous group and current-sector observable
hypotheses cannot be transferred to the finite-clock field by title alone.
