# Frozen independent derivation before author comparison

This derivation and the accompanying coefficient matrices were produced before
reading the author's native-interaction packet. Only its anticipated freeze
timing was received. The actual native-stability operators and earlier
independent native/pulse checks are the inputs. This is a mathematical
discriminator for a specified variational family, not an effective scattering
amplitude, condensate, many-body phase, or formal audit/PASS.

The first independent sparse calculation finished at approximately
2026-09-30T01:28 UTC. Its full complex coefficient file has SHA256
`4d4ac9e32d0d2cf80d3153ae01e8a1a49c8728c7bfeab68a50551e1d39fc8c69`.
No author code or interim output was read or imported.

## Exact hard-core pulse expansion

Let `C=sum_(x,A) zeta_A Q_A(x)^dagger`, `v=C Omega`, `w=C^2 Omega`, and
`s=||v||^2`. The actual state is the normalized full-carrier vector

`psi(t)=exp[t(C-C^dagger)]Omega`.

There is no normalization denominator and no truncation in its definition.
The first three powers of the anti-Hermitian generator applied to the vacuum
are

`(C-C^dagger)Omega=v`,
`(C-C^dagger)^2 Omega=w-s Omega`,
`(C-C^dagger)^3 Omega=C^3 Omega-C^dagger w-s v`.

The previously reconstructed uniform-pair identities give `Hmob Omega=0`
and `Hmob v=0` for every complex zeta. Number conservation and `Nv=2v`,
`Nw=4w` then give the exact Taylor coefficients

`<Hmob>_t = (t^4/4)<w,Hmob w>+O(t^6)`,
`<N>_t =2s t^2+(||w||^2-2s^2)t^4/3+O(t^6)`.

For number, the order-four contributions are `||w||^2` from the squared
order-two state and `-(2/3)(||w||^2+s^2)` from the order-one/order-three
cross term. This explicitly checks the hard-core normalization subtraction.
The number phase `exp(i pi N/2)` reverses the pulse generator while fixing
both observables and the vacuum, so the expectations are even in t.

These remainders can be made uniform per volume. A local pulse summand has
support on six sites, each site occurs in six translated supports, and one
nonzero nested step adds at most five sites. For example take
`k_*=4 sum_A |zeta_A|`, a valid local Hermitian-generator norm bound because
`||Q_A||<=2`. Then

`||ad_K^r O|| <=(12k_*)^r product_(j=0,...,r-1)(s_O+5j)||O||`,

where `K=i(C-C^dagger)`. Use `s_O=25`, `||h_x||<=182mu+240tau` for energy
and `s_O=1`, `||n_x||=1` for number. The sixth-order integral Taylor remainder
is bounded by the resulting sixth-commutator constant times `V |t|^6/720`.
Thus no condition `Vt^2<<1` is needed. This bound is deliberately loose.

## Physical edge coefficients and pair normalization

Collect the uniform creator into physical unordered edges:

`C=sum_(unordered {u,v}) c_(v-u) b_u^dagger b_v^dagger`, `c_d=c_(-d)`.

Use five complex variables `(a,b,p,q,r)` and set `d=(a,b,-a-b)`.
The actual nonzero coefficients are

`c_(+/-2ei)=d_i`,
`c_(s ei+t ej)=-s t t_ij`, with `(t12,t13,t23)=(p,q,r)`.

The first formula follows from the E definitions. The second includes BOTH
shell centers of an orthogonal physical pair; omitting this multiplicity
would give a wrong T normalization. In the original source coordinates,

`a=zeta_E1/sqrt(2)+zeta_E2/sqrt(6)`,
`b=-zeta_E1/sqrt(2)+zeta_E2/sqrt(6)`,
`(p,q,r)=(zeta_T12,zeta_T13,zeta_T23)`.

The pair norm per volume is therefore

`g=s/V=sum_i |d_i|^2+2(|p|^2+|q|^2+|r|^2)`.

For four distinct physical vertices S, the coefficient in `w` is

`w(S)=2[c_12 c_34+c_13 c_24+c_14 c_23]`.

This formula is exact for commuting distinct-site qubits: two ordered
disjoint creation words give each perfect matching, while an overlapping
creation vanishes. It is not Wick's theorem for bosons.

## Independent connected energy assembly

Use the actual positive decomposition `Hmob=A_E+A_T+mu D+W_tau`. Each
annihilator R appearing in an energy square has finite pair-word expansion
`R=sum_e r_e b_e` and obeys `sum_e r_e c_e=0` for every uniform pair direction.
This is the full five-variable identity, not a check at one chosen direction.

For a residual pair eta=`{x,y}`, the coefficient of `Rw/2` can be written

`F_R(eta)=-c_eta sum_(e intersects eta) r_e c_e`
` +sum_(e={u,v} disjoint eta) r_e(c_(x-u)c_(y-v)+c_(y-u)c_(x-v))`.

It follows by removing the disconnected term with the null identity above.
This is a quadratic polynomial in the five variables. If it is nonzero,
both residual vertices lie in the finite union `U=S_R union (S_R+Dgraph)`.
The first term requires an overlap and a graph edge to the other residual
vertex; the second requires both residual vertices to be graph-neighbors of
the annihilator support. Thus the entire infinite-lattice sum is finite,
without enumerating the disconnected volume-squared part of `w`.

The contribution to the order-four energy density is the sum of the actual
square weights times `sum_eta |F_R(eta)|^2`:

* one opposite singlet, weight `2mu/3`;
* eighteen signed plane differences, each weight `mu/4`;
* fifteen pair-gradient combinations, weights `tau/2,tau/6,tau/4` for their
  unnormalized E1, E2, and T words respectively.

The remaining diagonal D term has an especially small support at N=4.
Every nonzero `w(S)` already gives every occupied site a graph partner. With
only three other particles, its integer diagonal polynomial is nonzero
only when all three are graph neighbors of the chosen occupied site.
Therefore its order-four density contribution is

`mu sum_({x,y,z} subset Dgraph) |c_0x c_yz+c_0y c_xz+c_0z c_xy|^2`.

There are exactly `binom(18,3)=816` such stars. This handles the full diagonal
operator, not merely the nominal three-body term.

The implementation consequently uses 34 local residual-pair rows, 67,420
candidate residual pairs, 390,882 pair-word iterations, and these 816 stars.
The largest residual-site set has 88 sites. All energy coefficients are
computed as rational Gram matrices of quadratic monomials. No large
many-body state or eigensolver is used.

## Independent closed-walk number formula

The number coefficient has a second, different connected representation.
Let `M_uv=c_(v-u)` with zero diagonal. Counting matching cross terms on each
four-site set gives, for a general finite symmetric hard-core creator,

`||w||^2-2s^2 =tr[(M M^dagger)^2]`
` -4 sum_u (sum_v |M_uv|^2)^2+4 sum_(u<v)|M_uv|^4`.

This identity was additionally tested by literal four-site occupation words
on a nontranslation-invariant seven-site complex coupling matrix. It is
useful because it exposes every disconnected cancellation.

For the translation convolution, put
`ell_h=sum_d c_d conjugate(c_(d-h))` and
`u4=(1/2)sum_d |c_d|^4`. Its extensive coefficient is

`n4=(1/3)[sum_h |ell_h|^2-16g^2+4u4]`,
`<N>_t/V=2g t^2+n4 t^4+O(t^6)`.

The closed-walk sum is finite. A separate direct complex-convolution check
agrees with the stored quartic matrix, including its conjugation ordering.

## Complete coefficient data and real-direction simplification

`quartic_matrices.json` gives the general complex result without imposing a
real pulse. Let m be the fifteen monomials `z_i z_j`, `i<=j`, in its stated
order. Then

`e4=m^dagger (mu G_mu+tau G_tau)m/12`,
`n4=m^dagger G_N m/3`,
`<Hmob>_t/V=e4 t^4+O(t^6)`.

All three stored numerator matrices are real symmetric integer matrices.
Their construction is exact; the two energy matrices are sums of positive
weighted polynomial Gram matrices. Twenty-four proper cubic transformations
on a general complex direction preserve all three functionals exactly.

For REAL variables the matrices reduce to a compact invariant expression.
Define

`D2=a^2+b^2+(a+b)^2`, `U=p^2+q^2+r^2`,
`V4=p^4+q^4+r^4`,
`W=(a+b)^2 p^2+b^2 q^2+a^2 r^2`.

Then

`e4_mu=52 D2^2+(512/3)D2 U+(202/3)W+(772/3)U^2-(124/3)V4`,
`e4_tau=120 D2^2+592 D2 U-4W+704 U^2-80V4`,
`n4=-(5/3)D2^2-(40/3)D2 U+16W+(8/3)U^2-(28/3)V4`.

Here `e4=mu e4_mu+tau e4_tau`. These real formulas must not be extended to
complex variables just by inserting absolute values; the full complex
matrices are the applicable artifact.

## A named tensor comparison, not an implicit rotation axiom

Use the explicitly supplied real symmetric traceless matrix

`T=[[a,p,q],[p,b,r],[q,r,-a-b]]`.

Its Frobenius norm squared equals the actual pair norm g. This provides a
Gram-compatible continuous-tensor identification extending the cubic action.
Under it, a 45-degree rotation of `diag(1,-1,0)` becomes the off-diagonal
matrix with `p=1` (up to an immaterial sign). At normalized pair norm `g=1`,
the corresponding pulses are `sum Q_E1^dagger` and
`sum Q_T12^dagger/sqrt(2)`. The exact coefficients are

| Direction, g=1 | e4 | n4 |
|---|---|---|
| E1 | `52mu+120tau` | `-5/3` |
| T12 divided by sqrt(2) | `54mu+156tau` | `-5/3` |

The energy difference is `2mu+36tau>0` for the specified positive couplings.
The number expansions agree through fourth order in this comparison.
At fixed small density along the two pulse curves, the leading coefficients
of energy density divided by rho squared differ by `mu/2+9tau`.

Cubic E and T representations alone do not select a unique relative scale
for an extension to continuous rotations. The comparison above explicitly
selects the one whose metric agrees with the physical uniform-pair Gram.
For example the literal relative-momentum form of the creator has symbol
`2 sum_i d_i cos(2k_i)+4 sum_(i<j)t_ij sin(k_i)sin(k_j)`; interpreting THAT
quadratic form as a continuum tensor chooses a different off-diagonal scale.
Neither convention is an axiom or an actual continuous symmetry of the
lattice law. The checked discrepancy concerns the named physical pulse
family and tensor identification. It is not an embedding-independent
obstruction to an emergent rotational phase or scattering theory.

## Support, finite-volume scope, and execution

The calculation uses unrestricted integer coordinates. For every energy
annihilator, each coordinate span of its support is at most three. Enlarging
by the graph displacements gives span at most seven. Comparing two points
against a possible graph displacement can involve a difference of magnitude
at most nine. Thus `L>=10` suffices to avoid both vertex identification and
spurious wrapped graph edges in this connected computation. The number
closed walks have four displacements of coordinate size at most two;
`L>8` prevents nonzero winding from folding onto the constant coefficient.
The conservative common scope is therefore **every torus L>=10**, as well
as the infinite-lattice connected coefficient. No claim is made here that
these exact numerical coefficients also hold on every L=5,...,9 torus.
The exact pulse/Taylor identities themselves hold on all the stated tori;
their coefficients can receive winding corrections in smaller volumes.

One sparse job was priced below thirty seconds and 150 MB; actual runtime
was **2.830 seconds**, peak RSS **17,973,248 bytes**, with BLAS/OMP capped at
one. Deadline and stop-sentinel checks were clear before execution. The
matrices and directional values use integer/Fraction arithmetic. Auxiliary
complex covariance controls use Gaussian-integer arithmetic represented in
binary floats, with an explicit bound placing every intermediate integer
strictly below `2^53`; no numerical tolerance is used. No author comparison
has yet been made in this frozen document.
