# Immutable context exchange with an acoustic sector at every interior density

Primary construction, 2026-09-21. This is a supplied stochastic rule, not
an implication of the repository axioms. A separate reconstruction completed
before seeing this source confirms the current, all-density spectrum and
applicability of the smooth-profile proof. A further separate proof establishes
the stationary Fourier-fluctuation limit under its explicit hypotheses.
Reports: `independent_axis_balanced_context/REPORT.md` (SHA
b9cedcafccb48dfcd2503e5f00569a547288d4dcef0fb7dfca832565aec8f7cf) and
`independent_context_fluctuations/REPORT.md` (SHA
772046745ac814c32adcd8f36e3c8415ddf4a3a4b37435e8992441c6c8d5be68).
All report/checker content and sealed identities have been inspected. These
are separate mathematical checks, not an independent audit or retention.

## 1. General polarized context rule

On Z^d or a cubic torus whose periods are at least four, take vacancy 0 and
2d immutable occupied labels with v_a=+/-e_j. Write n_a=1 for occupied
labels, n_0=0, f_i(a)=v_(a,i), and q_i(a)=v_(a,i)^2. For an i-edge with
four-site string (l,a,b,r), let

`s_i(a)=2 n_a-d q_i(a)`.

This feature is 0 at vacancy, 2-d on a label parallel to the edge, and 2
on a transverse label. It does not change a record. Define

`h_i(l,a,b,r)=(alpha/2) { [f_i(a)-f_i(b)] [s_i(l)+s_i(r)]`

`                       +[s_i(a)-s_i(b)] [f_i(l)+f_i(r)] }`,     (1)

and actual exchange rate

`c_i=kappa0+max(h_i,0)`, `kappa0>0`.                            (2)

Alternatively choose a constant K with `K>max|h_i|/2` and use c_i=K+h_i/2.
These are bounded positive nearest-neighbor swaps with a four-site context.
Alpha is a fixed real scale; alpha!=0 is needed for nonzero acoustic speed.
In d=3, max|h_i|=4|alpha|, so K>2|alpha| suffices. The positive-part choice
has rate ceiling kappa0+4|alpha|. Complete local enumeration checks this
sharp bound; the generic bounded finite-alphabet argument already suffices
for a strictly positive floor.

The polarized telescoping identity used earlier holds for *any* two
single-site functions f,s:

`sum_x [(f_x-f_(x+1))(s_(x-1)+s_(x+2))`

`       +(s_x-s_(x+1))(f_(x-1)+f_(x+2))]=0`.

It proves pointwise global balance and hence invariance of every homogeneous
product law for (1)-(2). The new scalar feature transforms with the edge
axis under signed cubic coordinate permutations. Reversing the edge reverses
f and the four-site order, leaving the physical exchange rate unchanged.
Thus the rule remains cubic covariant. Every actual update swaps complete
records or a record and a vacancy; no occupied label is redrawn.

## 2. Exact product currents and flux potential

Let p_a denote the 2d occupied probabilities, p_0=1-rho,

`rho=sum_a p_a`, `g_i=sum_a p_a f_i(a)`,

`q_i=sum_a p_a q_i(a)`, `S_i=2rho-d q_i`.

The actual product current is

`J_a^i=alpha p_a [S_i f_i(a)+(s_i(a)-2S_i) g_i]`.               (3)

The vacancy current is `J_0^i=-2alpha p_0 S_i g_i`, so summing all 2d+1
species currents gives zero. As before, the symmetric part of the rate
does not contribute to these product means. Direct averaging of h/2 times
the endpoint indicator difference gives (3).

In chemical coordinates mu_a=log(p_a/p_0), the exact flux potential is

`Psi_i(mu)=alpha S_i(mu) g_i(mu)`.

Since `partial_mu_a S_i=p_a[s_i(a)-S_i]` and
`partial_mu_a g_i=p_a[f_i(a)-g_i]`, its derivative is (3). Therefore
`A_i C=C A_i^T`, where A_i=partial J_i/partial p and C=diag(p)-p p^T.
The positive categorical entropy Hessian symmetrizes the nonlinear current
law at every full-support composition. This is an exact algebraic identity,
not itself a microscopic hydrodynamic theorem.

The exact number, vector and axis-occupation currents are

`J_rho^i=2alpha p_0 S_i g_i`,                                  (4)

`J_(g_j)^i=alpha [delta_ij S_i q_i`

`                   +(2-d delta_ij-2S_i)g_i g_j]`,              (5)

`J_(q_j)^i=alpha g_i [delta_ij S_i`

`                   +(2-d delta_ij-2S_i)q_j]`.                 (6)

For the pressure term, writing r_i=q_i-rho/d yields the exact identity

`S_i q_i=rho^2/d-d r_i^2`.                                    (7)

This cancels the term linear in axis-quadrupole imbalance without requiring
rho to take a particular value.

## 3. Isotropic acoustic linearization for every 0<rho<1

At any isotropic product p_a=rho/(2d), g=0 and q_i=rho/d, so S_i=rho.
Linearizing the current-conservation equation at that fixed background gives

`partial_t delta rho+2alpha rho(1-rho) div delta g=0`,            (8)

`partial_t delta g+(2alpha rho/d) grad delta rho=0`,              (9)

`partial_t delta r_i=0`, `sum_i delta r_i=0`.                    (10)

To see (9) directly, differentiate S_i q_i:
`delta(S_i q_i)=(rho/d)(2delta rho-d delta q_i)+rho delta q_i`
`=2rho delta rho/d`.
For (10), (6) has linear coefficient 2alpha rho(1-rho)/d multiplying
delta g_i for every j, exactly one d-th of (4), so the traceless difference
cancels.

The directional current matrix has one acoustic pair

`omega=+/-c_s(rho)|k|`,

`c_s(rho)^2=4alpha^2 rho^2(1-rho)/d`,                           (11)

and 2d-2 zero modes: d-1 transverse vector modes and d-1 axis-quadrupole
modes. The pair is nonzero for alpha!=0 and every 0<rho<1. In d=3 with
alpha=1, speeds at rho=1/4,1/2,3/4 are respectively 1/4, 1/sqrt(6),
and sqrt(3)/4. All physical parameters are held fixed as rho varies.

This is an exact all-direction current statement throughout the interior,
not a fit. The separate stationary-fluctuation proof now connects this
spectrum to microscopic two-time correlations for fixed interior products,
fixed Fourier modes, fixed finite time and a fixed positive swap floor.
The smooth-profile proof applies under its given smooth-interior-solution
hypothesis. Neither result is a finite-wave-number damping calculation.

## 4. Selection within the polarized bilinear context family

The construction can be located within a small explicit rate family. Let
the antisymmetric difference be a constant endpoint term u(f_a-f_b) plus
a polarized context of the form (1) with a general scalar feature

`s_i=a n+b q_i`,

and prefactor E. Its product flux potential is

`Psi_i=u g_i+2E(a rho+b q_i)g_i`.

Write r_i=q_i-rho/d. The coefficient multiplying g_i is

`F(rho)+2E b r_i`, `F(rho)=u+2E(a+b/d)rho`.

At an isotropic state, the coupling between the vector mode and a traceless
axis-occupation mode is proportional to

`F(rho)+2E b rho/d = u+2E(a+2b/d)rho`.                         (12)

It vanishes at every interior rho iff u=0 and a+2b/d=0, assuming E!=0.
The nontrivial choice is therefore proportional to a=2,b=-d, which is (1).
This is an all-density decoupling criterion within the stated polarized
bilinear family. The full directional calculation strengthens it in d=3.
Let `L=u+2E(a+2b/3)rho`, `T=u+4E(a+b/3)rho`, and `R=(1-rho)T^2>=0`.
The generic linearized field equations have coefficients

`delta rho_t+(1-rho)T div delta g=0`,
`delta g_i,t+(T/3)partial_i delta rho+L partial_i delta r_i=0`,
`delta r_j,t+L[partial_j delta g_j-(1/3)div delta g]=0`.

In a unit axis direction the only possibly nonzero squared speed is
`(2L^2+R)/3`; in a unit body-diagonal direction the squared speeds are
`L^2/3,L^2/3,R/3`. A common nonzero speed requires L=0: equality with R/3
forces L=0, while equality with L^2/3 requires L^2+R=0 and gives zero.
When L=0 and T!=0, the density/vector equations provide the isotropic pair
in every direction and the four extra modes have zero speed. Requiring
this at every interior rho therefore forces u=0 and a+2b/3=0, with a
nontrivial overall scale. The exact symbolic field matrix and both
directional characteristic polynomials are checked in the primary runner.

This is necessity and sufficiency within the stated d=3 polarized bilinear
family. It is not a classification of all local rates or a proof that the
repository axioms impose the all-density isotropy criterion. The d=3
necessity argument is not asserted unchanged in dimensions one or two.

## 5. Continuing formation on a changing product background

Uniform births, each occupied label at rate epsilon per vacant site, still
preserve the homogeneous product family exactly, with

`p_0(t)=p_0(0) exp(-2d epsilon t)`,

`p_a(t)=p_a(0)+p_0(0)[1-exp(-2d epsilon t)]/(2d)`.

An isotropic product background remains isotropic while rho increases.
Unlike the occupation-only context family, this rule stays on its isotropic
acoustic current sector at every interior point of that trajectory.

For microscopic birth rate beta/N and macroscopic time tau=t/N, the formal
linearized reaction-conservation equation about that background is

`delta rho'=-2alpha rho p_0 div delta g-2d beta delta rho`,

`delta g'=-(2alpha rho/d) grad delta rho`,

`delta r_i'=0`,

`rho'=2d beta p_0`.

This is a time-dependent acoustic system with a birth source, not a
stationary wave equation with one constant speed. Even the linear mean
response still requires a justified limiting procedure. The density speed
tends to zero as full occupancy is approached; all-density isotropy does
not provide persistent finite-speed density waves after vacancies vanish.
Occupied records can nevertheless continue exchanging.

## 6. Required checks and physical scope

The primary runner `axis_balanced_context_check.py` completes 19 grouped
checks: sharp rates, endpoint reversal, 345744 local signed-cubic transforms,
pointwise periodic balance, 24 direct four-site product-current cases with
seven species each, nonlinear entropy compatibility, the complete symbolic
all-direction field matrix, and the generic family classification above.
Its full results and source identity are preserved in
`AXIS_BALANCED_CONTEXT_RESULTS.json`. These are primary checks, not independent
evidence. The separate derivations recorded above have now checked the
change of feature, the all-density result and the stated limiting hypotheses. If tested numerically,
use a newly identified simulator and exact finite-generator calibration;
do not silently modify the running occupation-only simulations.

The supplied scalar feature and a uniform exchange floor remain extra
dynamical assumptions. Alpha sets a microscopic time scale. This construction
addresses a particular obstruction to isotropic collective transport during
formation; it does not derive quantum mechanics, gravity, a selected physical
clock or the microscopic generator from the minimal axioms.
