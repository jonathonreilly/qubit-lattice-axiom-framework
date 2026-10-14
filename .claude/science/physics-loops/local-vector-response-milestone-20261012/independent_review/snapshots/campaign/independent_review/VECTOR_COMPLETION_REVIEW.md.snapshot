# Independent check of the constant-coefficient vector completion

2026-10-12. Focused mathematical/source check, not a formal audit, empirical
acceptance, or retained verdict. Parent supplied the construction and runner.
I read the complete protocol, note, runner and result receipt, together with
the complete earlier constrained-dynamics note. I did not import the author
runner, fit data, calculate galaxy fields, edit author files, or broaden the
candidate into a nonlinear theory.

**Disposition:** no mathematical correction is needed for the stated model.
The action has positive field energy and three unconstrained configuration
modes, its full retarded tensor has finite support speed c_L, and its static
scalar susceptibility is exactly the declared homogeneous target. The result
depends on supplied constant coefficients, a supplied unit direction and full
vector initial data. It does not inherit nonlinear fits or a matter/metric
completion. The stated restrictions are consequential and correctly retained.

## Exact reviewed inputs

| File | SHA-256 |
|---|---|
| PROTOCOL.md | `66c7ddb452e4385e64dec9d749b1fd76c28cdde131a446099d38293d564b678b` |
| DIRECT_VECTOR_COMPLETION.md | `0fb24c2072b5fcac16b991d8a29b6999531edfb6bc1041b73afb1cd377685ca8` |
| direct_vector_check.py | `6205aa512256262fc1d10e6b854773d2a20f177825a82459fb1b2bde63189ce1` |
| evidence_v1/RESULTS.json | `d3210caf5904bcdf4997b04156645745444b413590b3264d5bccd5cd68cd123c` |
| Prior DIRECT_DYNAMICS.md | `6fbaf6b91561d3ce5a51b154a364e98d1fafedd1b94119f725df8df4219648d8` |

Every file is copied exactly in `snapshots/`; the parent receipt's three
source identities match. The earlier note has the same bytes as the earlier
independent check. Its restricted two-scalar result does not quantify over
the new vector action.

## Action, signs, dimensions and degrees of freedom

Write mu=1/N and beta=1/D-1/N, with 0<D<=N and alpha>0. As usual the
gravitational constant G is positive. With grad u indexed by
`H_ij=partial_i u_j`, direct differentiation of the stated Lagrangian gives

`partial L/partial u_j = -rho e_j`,

`partial L/partial u_t,j = alpha u_t,j/(4 pi G)`,

`partial L/partial H_ij = -(mu H_ij+beta delta_ij tr H)/(4 pi G)`.

The Euler equation is therefore exactly

`alpha u_tt - mu Delta u - beta grad div u = -4 pi G rho e`.

The kinetic Hessian is `alpha I/(4 pi G)`, invertible and positive. There is
no primary auxiliary constraint or gauge reduction. At nonzero k the spectrum
contains two transverse modes and one longitudinal mode, not merely two total
degrees of freedom. A source along e excites only the relevant combinations;
an unsourced orthogonal polarization still exists as a free degree of freedom.
The k=0 limit is free uniform motion, not an additional unstable propagating
oscillator; compact/decaying finite-energy data fix the appropriate spatial
representative.

For u in gravitational-potential units, N and D are dimensionless and alpha
has inverse-speed-squared units. Every field term and rho e.u then has energy
density units. The Hamiltonian is the positive field term plus the interaction
rho e.u. The note correctly does not claim positivity of the complete
matter-plus-interaction system.

The Fourier stiffness `B=mu k² I+beta k k^T` has eigenvalues k²/N twice and
k²/D once. Thus c_T²=1/(alpha N), c_L²=1/(alpha D), with positive kinetic
residues and c_L>=c_T. The two scalar readout weights are the squared
projections `e.P_T.e=sin²(theta)` and `e.P_L.e=cos²(theta)`. This does not
identify either branch with tensor radiation or light.

## Local energy and a sharp domain of dependence

Define `Q(H)=mu |H|²+beta (tr H)²` and
`T_n=mu partial_n u+beta n div u`. Multiplying the Euler equation by
u_t/(4 pi G) gives

`partial_t energy + div S = -rho phi_t`,

where `S_i=-[mu u_t.partial_i u+beta u_t,i div u]/(4 pi G)`.
Both the flux sign and the stated work term are correct.

For `H'=n outer v`, the bilinear form associated with Q satisfies
`Q(H,H')=v.T_n` and `Q(H')=mu |v|²+beta(n.v)²`. Cauchy-Schwarz gives

`|v.T_n|² <= Q(H)[mu |v|²+beta(n.v)²] <= Q(H)(mu+beta)|v|²`.

Taking v=u_t and using `2 sqrt(alpha)|u_t|sqrt(Q)<=alpha|u_t|²+Q`
establishes `|S.n|<=c_L energy`. The coefficient is sharp: a longitudinal
plane-wave jet with `H=n outer n` and `u_t=c_L n` saturates it. The independent
controls confirm saturation as well as the acoustic matrix
`mu I+beta n n^T`, whose eigenvalues give the two characteristic speeds.

The shrinking-cone energy integral consequently cannot acquire energy from
outside its backward c_L cone. Starting with zero full vector data and no
source inside that cone gives zero field there. Smooth compact data suffice;
the standard finite-energy approximation retains distributional support.
The local projection phi=e.u and its spatial derivatives cannot enlarge
support. An eternal static source or noncompact full initial data is outside
this compact-data propagation assertion; static long-range fields do not
contradict it. Group-velocity samples are not being substituted for this proof.

## Static susceptibility and source normalization

The inverse is

`B^-1 = [N I+(D-N)P_L]/k² = (N P_T+D P_L)/k²`.

Contracting twice with the unit e gives

`e.B^-1.e = [N k_perp²+D k_parallel²]/k^4`.

Combined with the negative source term, this yields exactly
`phi_hat=-4 pi G rho_hat [N k_perp²+D k_parallel²]/k^4`.
Independently eliminating the prior static equations
`Delta psi=4 pi G rho`, `Delta phi=div(M grad psi)` gives the same result
for `M=N I+(D-N)e e^T`. This is equality at every nonzero wave vector, not an
axis-only match.

With `F[f](k)=integral exp(-i k.x) f(x) dx`, the distributions
`F^-1(1/k²)=1/(4 pi r)` and `F^-1(1/k^4)=-r/(8 pi)` give

`B^-1_ij(x)=[(N+D)delta_ij+(N-D)n_i n_j]/(8 pi r)`.

The contracted point potential and isotropic `-GmN/r` limit follow with the
stated sign and factors. The point source is a distributional fundamental
solution, not a finite-energy smooth-data example; its singular energy at
the origin is not covered by the finite-energy claim. No missing origin
contact term is needed in the Fourier-defined inverse.

## Retarded tensor: independent distributional derivation

For each Fourier mode the impulse solution has
`G_hat(0+)=0` and `partial_t G_hat(0+)=I/alpha`. Resolving the stiffness
eigenspaces gives the note's sine propagator, so

`(alpha partial_t² + B) G_hat = I delta(t)`.

This fixes the normalization and, with retarded support, the solution. The
frequency denominators with `(omega+i0)²` agree with the retarded convention.

To check its real-space form separately, let
`g_c=delta(t-r/c)/(4 pi c² r)` and solve `Delta h=g_L-g_T`, with zero exterior
constant. For fixed positive t each shell has spatial integral t; the delta
conversion is `delta(t-r/c)=c delta(r-c t)`. Radial integration therefore gives

`r² h'(r)=t[H(r-c_L t)-H(r-c_T t)]/(4 pi)`.

Thus h' is zero before the inner shell and after the outer shell and is
`-t/(4 pi r²)` between them. In the intervening region one may take
`h=t(1/r-1/(c_L t))/(4 pi)`. Its Hessian is
`t(3n_i n_j-delta_ij)/(4 pi r³)`.

There is a negative h' jump at r=c_T t and a positive jump at r=c_L t.
Using `delta(r-c t)=delta(t-r/c)/c` on each shell converts the jump coefficient
`t/(c r²)` to `1/(c² r)`. Adding `delta_ij g_T` then produces exactly the
transverse-front, longitudinal-front and intervening terms printed in the
note, all divided by alpha. This checks the otherwise easy-to-miss powers
of c and both surface signs.

For t<r/c_L all contributions vanish. For fixed t>0 the middle term is
away from the origin. Near the spacetime vertex it defines a locally
integrable cone-supported distribution; its radial volume integral scales
as t. The two shells have the same property. Together with the Fourier
impulse jump this fixes the distribution at the vertex without an added
instantaneous spatial tail.

The tensor has support on and between the two outgoing fronts. Individual
spatial projectors are nonlocal, but the complete retarded combination is
local. Omitting the intervening term breaks the match; the independent
mutation discrepancy is .5598960738067768 in the parent's decisive example.

At fixed r>0 its time integral is ordinary and supported on a finite interval.
The middle integral is
`(3nn^T-I)(1/c_T²-1/c_L²)/(8 pi alpha r)`. Adding both front integrals yields
`[(N+D)I+(N-D)nn^T]/(8 pi r)`, precisely the static inverse above.
In Fourier space the corresponding zero-frequency integral is understood
retarded/Abel-wise; no unjustified absolute convergence of an undamped sine
integral is needed.

## Independent numerical and symbolic controls

`check_vector_independent.py` imports no author module and no spherical-Bessel
function. It uses raw Gauss-Legendre polar integration and an azimuthal rule
for all nine tensor components, with k pointing along (1,2,-2)/3. It integrates
the two delta fronts with their radial Jacobians and the middle region directly.
The target comes independently from the three Fourier oscillator modes.

- All 16 distinct parameter/wave-number/time tuples underlying the parent's
  64 scalar checks were recomputed as full tensors. Maximum tensor error was
  8.35e-15; maximum discrepancy with a saved scalar receipt was 8.51e-15.
- Three additional synthetic parameter choices, including a degenerate
  isotropic case, have maximum tensor error 1.42e-15.
- Four independent spatial-moment controls verify
  `integral G dx=t I/alpha` and all 81 components of
  `integral x_a x_b G_ij dx = t³[2mu delta_ab delta_ij +
  beta(delta_ia delta_jb+delta_ib delta_ja)]/(6alpha²)`.
  These are the impulse normalization and low-k wave-operator coefficients.
- Symbolic checks cover the full three-coordinate inverse, source/action
  derivatives, Hamiltonian, Fourier impulse jump, middle Hessian, delta
  conversion and static time integral.
- Four sharp longitudinal flux fixtures saturate the analytic bound. These
  supplement the complete quadratic-form proof; the parent's 120 random
  draws were source-inspected and their receipt count/bound checked, not
  replayed as a second independent sample set.

The independent run took .44 seconds of measured script time, used one
numerical-library thread and peaked at 86,917,120 bytes RSS. All checks passed
on the first run; source hashes remained unchanged. No observations or fitted
response arrays were opened in this check.

`check_vector_mutations.py` additionally tests seven deliberately false
formula variants without changing author files: interchanged static branch
coefficients, an extra term invisible on both distinguished axes, an inverted
radial delta Jacobian, c_T substituted for the outer flux speed, a reversed
source sign, an unmatched transverse projector branch claiming compact
support, and the omitted middle term. Each fails the corresponding independent
identity or counterexample. The incorrect delta Jacobian gives six times the
required total impulse mass in the rational fixture; the incorrect flux speed
fails by a factor two. Removing one projector branch leaves an explicit
off-cone Hessian tail. These controls target the proof's decisive assumptions
and normalization rather than simply repeating the author runner.

## Limits and final source disposition

At N=D the tensor reduces to the same scalar wave kernel times I, the middle
term vanishes, and only the e component is sourced/read out. There are still
three field components. As D tends to zero at fixed N and alpha, c_L and the
longitudinal stiffness diverge. Neither a uniformly finite propagation speed
nor a regular D=0 theory follows. The nine-source numerical D optima are
outside this strict-positive model.

For an oblique wave vector, the old constrained scalar has one branch while
this model has two readout poles. The corresponding axis branches agree, but
their dynamics are generally different. Changing the spatial action, adding
degrees of freedom and imposing a constant background direction takes this
construction outside the earlier constant two-scalar kinetic classification.
That is a legitimate constructive escape under new premises, not a refutation
of the previous restricted theorem.

The note appropriately withholds a field equation for e, nonlinear coefficient
promotion, galaxy/solar fit inheritance, quasistatic evidence for actual
sources, matter/metric coupling, light propagation, tensor-wave identification,
cosmology and quantum completion. The three-field model is a conditional local
realization of a homogeneous linear static susceptibility. It is not a physical
identification or an observationally established gravitational theory.

No source edit is requested. Detailed calculations, exact inputs and the final
identity checkpoint are preserved alongside this report. Campaign discovery
and stop guards were respected.
