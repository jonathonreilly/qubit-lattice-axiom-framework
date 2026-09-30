# Independent reconstruction of native density coercivity

No blocking mathematical error was found in the frozen proof. For the stated
physical-qubit Hamiltonian on every cubic torus `L>=5`, the argument establishes

`Hmob >= c N(N-2)/V`,
`c=min(tau,mu/12)/99090432`, `V=L^3`, `mu,tau>0`.

Its finite-volume kernel is exactly the vacuum and the five uniform pair
states. The residual-configuration pin, localization inequality, box overlap,
and numerical constants have been reconstructed below. The already frozen
independent pulse check may consequently be combined with this bound within
the same supplied model. This is a focused independent check, not a formal
audit/PASS, framework-law selection, or claim about a tensor phase.

The checked author report is `native-coercivity-route/REPORT.md`, SHA256
`27c9aee46d3d34c3fe7949f0774cd4de93c7b14df7f26461f4e615d3c1ad0811`.
The complete report was read. Its native stability input is SHA256
`7eba7d0092eb4990f5ae1a46825e015c6edc18692c09cab69ad5cd3ed4d24ca9`;
the actual hard-core definitions and operator positivity were reconstructed
again during the preceding density check, whose frozen report is SHA256
`c297675dfa1e3d119bcc8b02dd249c0d906a3d75706acbb3efb8d4a0b1eb10d8`.
The source inventories are bound separately with explicit coverage limits.
No author code was imported or executed. This check does not inherit a proof
of coercivity merely from either predecessor.

## Fixed full-carrier operator and gradient control

The actual model has one qubit at each site, `b_x^2=0`, `n_x=b_x^dagger b_x`,
and commuting operators at different sites. At each center, there are three
opposite bare pairs `d_i` and twelve signed orthogonal bare pairs `v_ij^st`.
The five `Q_A` are the two normalized E combinations and the normalized
four-word sum in each of the three T planes. All have exactly two annihilation
operators. Both Hmob and the asserted lower bound conserve total N.

The supplied completion of squares is an unrestricted operator identity:

`Hmob=A_E+A_T+mu D+W_tau`,
`D=(1/2)sum_x n_x(m_x-1)(m_x-2)>=0`,

where `m_x` counts the eighteen distinct neighbors `+/-2ei,+/-ei+/-ej`.
The nonnegative polynomial uses the integer spectrum of `m_x`; it is not a
function of an occupation mean. Its origin and center multiplicities were
checked in the preceding report from the literal pair operators.

For an arbitrary state vector, regard each bare annihilator applied to it
as a vector in the residual-particle Hilbert space. The E doublet plus
`D0/sqrt(3)` is an orthonormal change of the three opposite amplitudes. The
singlet has coefficient `2mu` in A_E. In a T plane, expansion gives

`(1/4)sum_(a<b)(v_a-v_b)^dagger(v_a-v_b)`
`=sum_a v_a^dagger v_a-Q_T^dagger Q_T`.

Thus the three complementary internal directions have coefficient `mu`
in A_T. These are algebraic changes of amplitude coordinates, not new
physical oscillators. They preserve the sum of squared spatial differences
as well as the sum of squared amplitudes.

For any vector-valued torus function,

`sum_(x,k)||f(x+ek)-f(x)||^2<=12 sum_x||f(x)||^2`.

Indeed each squared difference is at most twice the two endpoint norms,
and there are three positive coordinate directions. Define `Ebare` to be
the gradient sum of all fifteen bare types. Applying this estimate only to
the complementary internal components gives

`Ebare <=(6/mu)<A_E>+(12/mu)<A_T>+(1/tau)<W_tau>`.

For `a=min(tau,mu/12)`, this implies the simultaneous bound

`<Hmob> >=mu<D>+a Ebare`.

The factor twelve and the factors two/four in the internal normalization are
correct. The unused half of A_E causes no problem; all estimates have the
inequality in the required direction.

## Point pin on a three-dimensional box

For completeness I recomputed the numerical Poincare estimate. On a free
rectangular grid of side lengths `s_i`, let `s=max s_i` and assume
`s<=2 min s_i`. The normalized cosine eigenvectors of the free-path product
Laplacian have squared pointwise amplitude at most `8/|C|`. For a nonzero
multi-index n their eigenvalue is

`lambda_n=4 sum_i sin^2(pi n_i/(2s_i)) >=4|n|^2/s^2`.

The inequality uses `sin(pi u/2)>=u` for `0<=u<=1`. By Cauchy-Schwarz in the
nonconstant eigenmodes, the point-to-point squared difference is at most
the ordinary undirected-edge Dirichlet energy times

`sum_(n!=0)|phi_n(x)-phi_n(p)|^2/lambda_n`.

The numerator is at most `32/|C|`: this factor includes the difference of
the two mode values. Grouping nonnegative indices by `r=max n_i>=1`, each
shell has at most `3r^2+3r+1<=7r^2` modes and `|n|^2>=r^2`. Therefore

`sum_(n!=0)1/|n|^2 <=7s`,
`sum_(n!=0)|phi_n(x)-phi_n(p)|^2/lambda_n`
`<=56s^3/|C|<=448`.

For a function pinned by `f(p)=0`, summing the pointwise estimate gives

`sum_(x in C)|f(x)|^2 <=448 |C| E_C(f)`.

This uses each undirected free edge once, the same convention as the positive-
direction torus gradient. A side of length one is harmless; if the whole box
is one site, its pinned function is zero. For cyclic interval subsets, choose
their free path order and discard the closing edge. The entire torus is
handled by one cut in each coordinate. All retained edges are actual torus
edges. This proves the stated constant independently of finite resistance
experiments, and explains why the dimensional hypothesis is material.

## Residual occupation words give legitimate pins

Work in an arbitrary fixed N sector, without assuming translation invariance
of the state. For a fixed output occupation configuration eta, define

`f_eta^t(x)=<eta|B_t(x)|psi>`.

If eta occupies site y and the fixed bare type has an endpoint offset u,
the amplitude at `x=y-u` is zero. The annihilator removes the particle at
y, so its output cannot still occupy y. This conclusion is exact for
coherent states as well as occupation basis states.

Let B be an inner box and C its one-site enlargement in every coordinate.
Restrict eta to configurations with at least one particle in B. Choosing
any such y places the pin at `y-u` inside C because every endpoint offset
is a signed unit vector. The pin can depend on eta and the type, but the
Poincare constant does not depend on its location.

Crucially, the set of allowed eta is chosen once from B; it is independent
of the variable center x. Apply the pinned bound to each complete function
`x -> f_eta^t(x)` on C, then sum over these eta and t. Only after this step
drop the restriction from the positive gradient sum. Parseval then yields

`M_C^(B,+) <=448 |C| Ebare_C`.

There is no projection moved through an annihilator and no assumption that
many pins have additive electrical capacity. A single suitable pin per
residual configuration is sufficient.

## The local occupation inequality, including pair multiplicities

For each integer `m=0,...,18`,

`1 <=(m-1)(m-2)/2+m`.

On an input occupation configuration S with `N_B>=3`, sum this inequality
over its occupied sites in B. Every occupied pair incident to B leaves at
least one particle of B after it is removed. Thus its residual eta is in
the fixed allowed set used above.

Each graph edge incident to a site z in B has a bare-pair center in C.
For an axial edge, the center is the midpoint one lattice step from z. For
an orthogonal edge, either of its two centers is one lattice step from z.
The oriented quantity `sum_(z in B)n_z m_z` counts each physical edge at most
twice, whereas the bare-word sum in C counts it at least once. The full
torus multiplicities are one for axial edges and two for orthogonal edges;
the signed word has the same sign at the latter two centers. Signs disappear
from its individual squared norm.

For a fixed bare word and residual eta, the contributing input configuration
is unique: it is eta together with that word's two endpoints, if disjoint.
Consequently `M_C^(B,+)` is a diagonal weighted occupation count. There is
no interference term in this quantity. The configuration inequality therefore
extends immediately to the expectation in any coherent state:

`<N_B 1_(N_B>=3)> <=<D_B>+2 M_C^(B,+)`
`<=<D_B>+896 |C| Ebare_C`.

The indicator on D_B was dropped using its positivity. Its `m_z` still counts
the true full-torus neighbors, not a graph truncated to B. This verifies the
load-bearing localization step in the frozen proof.

## Partition, the q=1 case, and the final constant

For `N>=4`, set `q=floor((N/4)^(1/3))`. Since `N<=L^3`, one has `1<=q<=L`.
Partition each coordinate circle into q consecutive intervals with lengths
differing by at most one. The `q^3` product boxes are disjoint and exhaust
the torus. For `q=1`, the enlarged box is exactly the whole torus, with no
repeated sites. Its Poincare proof uses the free cuts described above.

For `q>=2`, enlarge each interval by one site at each end, retaining distinct
sites and capping at L. The resulting product boxes have aspect ratio at
most two. A coordinate vertex belongs to at most its own inner interval
and the enlarged intervals containing its two immediate neighbors, hence
at most three. A three-dimensional vertex belongs to at most `27` enlarged
boxes. Every retained edge belongs to no more boxes than either endpoint,
so its multiplicity is also at most 27, regardless of free-cut choices.

The largest side of an enlarged box is at most `ceil(L/q)+2`. Since
`L/q>=1`, this is at most `4L/q`. Also `floor x>=x/2` for `x>=1`, so
`q^3>=N/32`. Therefore

`max_C |C| <=64V/q^3<=2048V/N`.

For `q=1` the same bound holds; no oversized wrapped interval is inserted.
The inner occupation count obeys, configuration by configuration,

`sum_B N_B 1_(N_B>=3) >= N-2q^3 >=N/2`.

Summing the local inequality uses `sum_B D_B=D` exactly and
`sum_C Ebare_C<=27 Ebare`. Hence

`N/2 <=<D>+B_* (V/N) Ebare`,
`B_*=896*27*2048=49545216`.

The right side is at most `B_* V <Hmob>/(aN)`. To check this last comparison,
use `<Hmob>>=mu<D>+a Ebare` and note that
`B_* mu V/(aN)>=1`, since `mu/a>=12` and `V/N>=1`. Thus for `N>=4`,

`<Hmob> >=a N^2/(99090432 V)`.

For `N=3`, every residual word has one particle and provides a pin on the
whole torus. The unlocalized occupation inequality gives

`N<=<D>+2M<=<D>+896V Ebare`,

and therefore `<Hmob>>=aN/(896V)`, stronger than the asserted result in
that sector. For `N=0,2` the claimed right side is zero; for `N=1` it is
negative, whereas the actual energy is mu. This proves
`Hmob>=a N(N-2)/(99090432 V)` in every sector. Number conservation extends
the operator inequality to arbitrary coherent superpositions of sectors.

## Exact finite-volume kernel

If the energy is zero, each positive square annihilates the state. W makes
each vector `Q_A(x)psi` constant in x on the connected torus. A_E sets the
opposite singlet to zero, so inversion of the three internal components
makes each `d_i(x)psi` constant too. The plane difference squares set the
four signed bare amplitudes equal; their sum is the constant Q_T, hence
each signed bare amplitude is constant in x.

For `N>=3`, fix any residual eta and one of its occupied sites. The hard-core
pin supplies a zero at some center for each type. Constancy then makes every
amplitude zero everywhere. Thus all bare and collective pairs annihilate the
state. In the original Hamiltonian expression its energy becomes
`mu N+V3`, strictly positive in this sector unless the state is zero. N=1
has energy mu, while N=0 contributes the vacuum.

In N=2, the diagonal D removes all configurations whose pair is outside the
eighteen-neighbor graph. Their two occupied endpoints each have m=0.
The surviving opposite-pair amplitudes are three constants with one sum
constraint, giving two degrees of freedom. Each orthogonal plane has one
constant signed amplitude, giving three more. The two-center signs agree,
so no further consistency condition appears. No other graph edge type exists.
These five solutions are exactly the uniform `Q_A^dagger Omega` states.
The E norms squared are V and the T norms squared are 2V; different channels
are orthogonal. They are nonzero on all stated even or odd tori.

Thus the full finite-volume kernel has dimension six. This proof applies
to arbitrary states, not just translation-invariant trial vectors. It does
not assert that the uniform waves are normalizable in the infinite vacuum
representation, or that the many-body spectral gap is volume independent.

## Energy-density and packet consequences

The variance inequality gives, for any finite-volume state,

`<Hmob>/V >=c(rho^2-2rho/V)`, `rho=<N>/V`.

For an infinite translation-invariant state, restricting to large cubes and
replacing their open interaction by the torus interaction changes the energy
by only order `L^2`. This follows from finite range and bounded local terms;
only a boundary layer of centers changes. The finite bound applies to the
reduced density matrix without a fixed-N assumption. Dividing by volume and
taking the limit gives `e>=c rho^2`. This is an energy-density statement,
not an excitation theorem.

The frozen report's independent packet construction also checks out. The
orthonormal compact E1 basis makes its normalized sine packet's exact mobile
energy the ordinary Dirichlet eigenvalue
`6tau(1-cos(pi/(R+1)))<=3pi^2 tau/(R+1)^2`. The immobile stabilized part
annihilates every superposition in this E subspace. Its physical support
lies in coordinates `0,...,R+1`; spacing `R+6` leaves coordinate distance
at least five between distinct supports, including the final periodic gap.
No term of interaction diameter at most four touches two packets. Product
expectations therefore add, with vacuum expectations zero. When L is too
small for a packet, the stated floor-count bound reduces to the vacuum bound.
Choosing the packet energy at most nu gives exactly the report's
`E0<=-nu floor(L/(R+6))^3` and corresponding density lower bound.

The later pulse construction is stronger and has now been checked separately.
It is combined here only after both checks, leaving the preceding frozen
density report's conditional wording unchanged. Define

`A=10199347200*(182mu+240tau)`, `B=3870720`,
`c=min(tau,mu/12)/99090432`.

For every ground state of `Hmob-nu N`, `nu>0`, the checked bounds are

`nu/(A+nu B) <=rho<=min(1,nu/c+2/V)`,
`-(nu+2c/V)^2/(4c) <=E0/V<=-nu^2/(A+nu B)`.

The finite two-particle trial also gives `E0<=-2nu`; one may take the better
upper bound. For thermodynamic accumulation points and `0<nu<=nu_*`,

`nu/(A+nu_* B)<=rho<=nu/c`,
`-nu^2/(4c)<=e<=-nu^2/(A+nu_* B)`.

These are volume-uniform linear-density and quadratic-energy bounds at the
zero-density onset. They rule out the predecessor's positive density jump
at nu=0 in this specific mobile law. They do not establish differentiability
of the equation of state, continuity at every nu, a condensate, Goldstone
content, two linear tensor branches, or an actual record/source/action bridge.
For negative nu, positivity and the positive number penalty leave only the
vacuum. Both strictly positive mu and tau remain hypotheses.

## Actual independent controls and coverage limits

One exact job was priced below fifteen seconds and 150 MB. It completed in
**20.671 seconds**, slightly above that time estimate, with peak RSS
**56,131,584 bytes**. BLAS/OMP threads were capped at one. No dense N=3 torus
Hilbert space, many-body eigensolver, or unmanaged worker was used.

The independent script checks the internal projectors and all nineteen
occupation values; 3,230 balanced cyclic partitions for sides 5 through 80;
distinct expanded sites, pins, aspect ratio, density-volume bounds and free
edge overlap; eleven exact grounded-Laplacian resistance cases on boxes of
at most 27 vertices; the complete L=5 pair graph multiplicities and signs;
and 1,639 occupation configurations on twelve selected physical sites,
including 254,580 residual-pin controls. Its largest observed one-dimensional
vertex overlap is three, and free-edge overlap two. The general proof keeps
the conservative bound three for both. The sparse configuration census is
a control of counting conventions, not an exhaustive many-body proof.

The proof of all volumes and all states is the operator, pinning, spectral,
and incidence argument above. No extrapolation from samples is used. No
author numerical output was used as proof, no source file was edited, and
no formal source/audit status was changed. The campaign deadline and absent
stop sentinel were checked before execution. Exact bindings and the actual
control output accompany this report. No correction to the frozen coercivity
constant or claimed kernel dimension is needed.
