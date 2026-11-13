# Frozen Gaussian producers at a fixed nonidentity terminal background

Conditional author derivation, 2026-11-09, at
`97fc90828ab071b5813d1c9b6c8a952dc042509b`. Use the provisional compact
mode and the regional compensation premises pinned in §6. This supplies
the frozen Gaussian and the action and source vertices of the chart law.

## 1. Centered action and exact physical prefactor

Fix odd L>=3, kappa>0, m>=3 and u>=1. Use the actual two-layer seven-edge
deleted marginal, with adjacent elementary terminal plaquettes defining J
and with all allowed internal trees of the terminal-root fine forest.
Write O=E2\J and fix V on O with sup_c |V_c-I|<=epsilon_*, reducing the
uniform epsilon_* from the mode premise as needed. Use the actual paired
path means, every non-tree fine link and every intermediate link. Let
a* be the supplied stationary Haar-energy mode for this fixed V,u, and
write a_e=a*_e q_e, q_e=exp(b_e), for real quaternion logarithms b_e in
a common injective chart. The center and chart are frozen for all source
variations below.

Let Q_J(V) be the density of the surviving terminal field relative to its
probability Haar reference, that is, the integral of q_u times every
level-zero and every O terminal kernel over the hidden fields. Use
q_u=Z_fine(u)^(-1) exp[-u sum_p W_p] in the same Wilson convention as the
old producer. Root-fixed orbit Haar integrates to one in this quotient.
Put t=kappa u and H_Z(t)=exp(t)/Z(t), where Z(s)=integral exp(s w(Q)) dQ
under probability Haar. Each surviving kernel equals H_Z(t) times its
exponential of minus u times the full energy Phi_u in the mode note §1.
There are

    K_surv=|E1|+|O|=4 L^4 m^4+4m^4-7

such kernels. In particular the count excludes both numerator and radial
normalizer of each deleted kernel.

For each whole factor f let h_f be its complete energy, either W_p or
Phi_u, and S_f its distinct hidden readers. Use the regional note's
compensation (its equation (3)),

    ell_f,e = D_(b_e) h_f(a* exp(b);V)|_(b=0),
    hbar_f(q) = h_f(a*q;V)-h_f(a*;V)
                      -sum_(e in S_f) ell_f,e dot Im(q_e).     (1)

In the chart hbar_f(Exp(b)) has value and differential zero at b=0,
because D Im(exp(b_e)) at zero is the identity. For every e, stationarity
of E_u=sum_f h_f at a* gives sum_(f:e in S_f) ell_f,e=0. Hence on the
entire compact q-product the compensators cancel and sum_f hbar_f(q)
equals E_u(a*q;V)-E_u(a*;V). Every factor still reads only its own
hidden readers. A factor with empty S_f has hbar_f=0 and contributes its
constant only through E_u(a*;V). The count K_surv is unchanged by this.

The product Haar reference is preserved by multiplication by a*. Thus
the exact normalized quotient law in q variables is

    d rho_J(q;V) = D(V,u) exp[-u sum_f hbar_f(q)] product_e dq_e,
    D(V,u) = H_Z(t)^K_surv exp[-u E_u(a*;V)]/[Q_J(V) Z_fine(u)],  (2)

where each dq_e is probability Haar. This follows by multiplying the
original physical factors and then applying (1). It retains the center
energy and every normalized kernel at V.

Put n=m^4(3L^8+1+4L^4), N_s=3n, k=3(3L^8+1+4L^4) and sigma=u^(-1/2).
The Haar volume factor for exp(b_e) is (2pi^2)^(-1) j(b_e) with
j(b_e)=(sin|b_e|/|b_e|)^2, continuously extended at zero. The exact
negative log Lebesgue density S(b) on the chart therefore has the form

    exp[-S(0)] = D(V,u) (2pi^2)^(-n),
    S(b)-S(0) = sum_f u hbar_f(exp(b)) - sum_e log j(b_e).     (3)

Each term on the right has value and differential zero at the origin,
including each Haar term. In particular DS(0)=0. This is stationarity of
the exact chart action at zero.

## 2. Uniform precision in the translated log chart

Write H=u^(-1)D² S(0). Differentiating (3) gives exactly

    H = D_b² E_u(a* exp(b);V)|_(b=0) + (2/(3u)) Id.          (4)

Indeed (1) cancels on summation, and D²[-log j](0)=(2/3)Id by
sin r/r=1-r²/6+O(r⁴). In particular the energy Hessian in (4) is
that of the full normalized kernel sum, including every radial
normalizer. A compensation has no quadratic term, since Im exp(b)
is odd. Equation (4) uses the translated group chart at the fixed
center, with no substitution of the identity-background Hessian.

The supplied mode lower bound is, in squared chord units,
E_u(a*q;V)-E_u(a*;V)>=c_* sum_e |q_e-I|² with c_*>0 uniform.
For q=exp(sb), divide this inequality by s²/2 and let s tend to zero.
The differential vanishes and |exp(sb_e)-I|²/s² tends to |b_e|².
It follows from (4) that H>=g Id with g=2c_*. If the premise is
written with 1-w(q_e) and coefficient c, use g=c.

For the derivative bounds take a common fixed small b-chart.
Smallness of V and the supplied |a*_e-I|<=C epsilon_* imply that
all translated arguments a*_e exp(b_e) stay inside the common
all-reader identity chart after reducing epsilon_* and the chart
radius. Word telescoping then gives |M|>=1/2. The mode note §2 gives
|h^(j)(s)|<=C_j(1+s)^(-j), j=1,2,3, for h(s)=log Z(s)-s. In
Phi_u the radial correction is [h(t|M|)-h(t)]/u. Each positive-order
chain-rule term from h(t|M|) contains t^j h^(j)(t|M|), bounded by
2^j C_j. The leading terms, path means, and change to the translated
chart have bounded derivatives through order three on their fixed
local domains. Thus each h_f(a* exp(b);V) has uniform second and
third derivative bounds. The ell_f,e in (1) are uniformly bounded
by the corresponding first derivative estimates. The imaginary
quaternion compensator, smooth multiplication and -log j have
bounded derivatives on the chart, so the local terms s_f and s_e^H
in (3) satisfy

    s_f(b)=u hbar_f(exp(b)),     s_e^H(b)=-log j(b_e),
    sup ||D³ s_v|| <= C u                                          (5)

for v of either type. No derivative bound at a zero mean is used.

Every translated factor has exactly the same bounded syntactic
reader geometry as its original factor, including the intermediate
output and all radial-normalizer readers when present. Uniform
arity and anchor incidence, including multiplicity from repeated
word occurrences and periodic projection, give an absolute row
bound for H by (4)-(5) and the second derivative bounds. Let d be
periodic axial nearest-neighbor cell distance and X(i) the owner
cell of scalar coordinate i. If the model range is supplied in
periodic l-infinity distance, multiply it by four to bound the
range in d. In particular the regional note's one-cell l-infinity
collar yields range at most four: take A to be one of two reader
cells of a common factor. We may take any common larger integer R.
With M large enough and K_H finite,

    g Id<=H<=M Id,    sup_i sum_j |H_ij|<=K_H,
    H_ij=0 if d(X(i),X(j))>R.                                (6)

The upper spectral bound follows from the row bound and symmetry.
All constants depend only on L,kappa and the supplied uniform mode
constants. These estimates hold for u>=1, regardless of m, tree
choices, V in the prescribed cap, and position or orientation of J.

## 3. Positive finite-range covariance core and symmetric paths

Apply the finite-matrix estimates of the old producer §2 with (6)
in place of its identity-background precision bounds. To record the
hypothesis match, choose M'>M, rho=1-g/M' and gamma=-log(rho)/R. For
C=H^(-1), the lth power in its Neumann series in Id-H/M' has range
at most lR and operator norm at most rho^l. Thus

    |C_ij|<=g^(-1) exp[-gamma d(X(i),X(j))].                  (7)

Fix 0<beta<gamma, an integer R0>=1, and split symmetrically

    P_ij=C_ij 1_(d(X(i),X(j))<=R0),    E=C-P.

At most (2t'+1)^4 cells lie at axial distance t' from a given cell,
including when the torus wraps. With
M_beta(E)=sup_i sum_j exp(beta d(X(i),X(j))) |E_ij|, (7) gives

    M_beta(E)<= (k/g) sum_(t'>R0) (2t'+1)^4
                                  exp[-(gamma-beta)t'].      (8)

Take R0 large enough that M_0(E)<=1/(2M). Symmetry gives
||E||<=M_0(E), hence P>=p0 Id with p0=1/(2M) and
P<=U Id with U=1/g+1/(2M). This is the positive range-R0 core in
(F1). The remainder E is a symmetric matrix used in the forest,
with no covariance positivity requirement.

For each unordered scalar pair choose one shortest axial path
between its owner cells by a fixed tie rule. Use its cell set
Gamma_ij=Gamma_ji in both orientations, including one cell if
the owners coincide. Set e_ij=exp(beta |Gamma_ij|)|E_ij|, with
|Gamma_ij|=d(X(i),X(j))+1. The row and pinned sums of (F2) obey

    e=sup_i sum_j e_ij <= exp(beta) M_beta(E),
    B_pin=sup_x sum_(i,j:x in Gamma_ij) e_ij
       <= exp(beta) (k²/g) sum_(t'>R0) (2t'+1)^8
                                  exp[-(gamma-beta)t'].      (9)

For the second bound, a pinned path of length t' has both endpoints
in the t'-ball of the pin. Count ordered scalar endpoints, using
at most k² choices per cell pair. Increase the common R0 until
e<=p0/4. The same enlargement can meet any prescribed positive
bound on B_pin, uniformly in the parameters of (6).

If a principal covariance inverse is needed, P[I]>=p0 Id for any
scalar subset I and C[I]>=M^(-1) Id. For the diagonal weight
W_ii=exp(theta d(X(i),X_*)), the absolute row and column bounds
on W P[I] W^(-1)-P[I], and likewise for C[I], are at most

    (k/g) sum_(t'>=0) (2t'+1)^4 exp(-gamma t')
                                         (exp(theta t')-1).

Choose theta>0 so this is <=p0/2. The inverse perturbation bound
then gives absolute inverse entries at most
2 p0^(-1) exp[-theta d(X(i),X(j))] by taking X_*=X(j).
The corresponding row sums are finite uniformly. These are
inverses of principal covariance matrices. The marginal Gaussian
on I uses C[I] itself.

All of C, P, E and their paths are frozen at V,u in each calculation.
Their spatial range and tail estimates are in the hidden coordinate
indices. No assertion about local dependence on a varied terminal
background is used in the forest hypothesis match.

## 4. Whole-cell chart vertices and fixed sources

Choose A>5/2 and p=[log(2+u)]^A. Write b=sigma x, sigma=u^(-1/2),
and Box_p={x: |x_i|<p for every scalar i}. There is a common
u_dagger such that for u>=u_dagger, |b_i|<=sigma p lies in the
fixed chart from §2, and sigma p³ is smaller than any fixed
prescribed positive threshold. This is the same per-link cube
of logs relative to a* as in the regional note §3.

For each local action s_v of (5), let D_v contain the complete
scalar bodies of all its reader cells, including scalars unused
numerically. Empty-reader compensated factors are identically zero
and are omitted as vertices. Fix a connected cell envelope T_v of
the reader cells of each other vertex, of uniformly bounded size
and diameter. For example, join them by shortest axial paths to
one reader cell. Define on the reader cube

    R_v(x)=s_v(sigma x)-(sigma²/2) D²s_v(0)[x,x].

Every s_v has s_v(0)=Ds_v(0)=0 by (3), and by (5) and the
uniform arity,

    |R_v(x)|<=C u sigma³ p³=C sigma p³.

On the whole real space use the bounded extension

    W_v(x)=1_(Box_p on D_v) [exp(-R_v(x))-1].                 (10)

The bracket is evaluated only in its indicated domain. Its uniform
bound is C' sigma p³ for u>=u_dagger after enlarging that threshold.
On Box_p, product_v(1+W_v)=exp[-sum_v R_v] exactly, and the total
quadratic contribution is x^T H x/2 by (3)-(4). In particular no
linear term of size sigma^(-1) has been hidden in a weak vertex.

Use the four marks X_1=F, X_2=G, X_3=A_c, X_4=A_d for fixed bounded
local quotient observables F,G with uniformly bounded reader sizes
and diameters, and distinct c,d in O. At fixed base V use unit
terminal tangents dot V_c and dot V_d and the insertions

    A_c(q)=kappa u <dot V_c,M_1,c(a*q)>,
    A_d(q)=kappa u <dot V_d,M_1,d(a*q)>.                      (11)

These are derivatives of the surviving physical log factors,
since the radial normalizer is independent of its output.
There is no deleted output mark. If differentiating the normalized
log density in V_c itself, the score includes the scalar
- D_c log Q_J(V); (11) are the insertions for the fixed-law
source generating function. Such scalars cancel from cumulants
of order at least two. For a fixed-base distinct-label terminal
jet no derivative of a*, the chart or H is taken. Varying
the terminal outputs in the original factors at fixed chart
coordinates gives precisely the separate first-order insertions
in (11). The assertion here is for quotient marks; an orbit-dependent
source is outside this vertex contract without a separate realization.

Choose ell_l>=||X_l||inf positive for each nonzero mark, with
ell_c=ell_d=kappa u available since |M_1|<=1. Put f_l=X_l/ell_l
and zeta_l=ell_l t_l so the physical coupling t_l X_l equals
zeta_l f_l. Any zero mark may be dropped. With D_l the complete
bodies of its reader cells, and a fixed connected envelope T_l,
the whole-space source vertex is

    W_l^src(x;zeta_l)=1_(Box_p on D_l)
                [exp(zeta_l f_l(a* exp(sigma x)))-1].         (12)

Here f_l is written as a function on the original hidden field.
For a score this notation means exactly (11) at q=exp(sigma x)
after normalization by ell_l. The chart integrals use the actual
retained quotient functions, including any pullback readers.
The bound is sup|W_l^src|<=exp(r)-1<=exp(1)r for |zeta_l|<r<=1,
with holomorphy in zeta and bounded measurability in x. The
whole-cell indicators are included even if some components are
unused. Empty-support constant sources are carried once in
V_vac(zeta)=sum_(empty-support l) zeta_l f_l instead. Constants
with a declared nonempty reader can instead be priced by (12).
The pure Gaussian reference is centered by construction. The
interacting chart law need not have zero mean x.

## 5. Exact chart identity and forest base contract

The log change b=sigma x contributes sigma^N_s to Lebesgue
measure. The real Gaussian of covariance C=H^(-1) has
density (2pi)^(-N_s/2)(det H)^(1/2) exp(-x^T H x/2) relative
to dx. Inserting (3), (10), (12) and this Gaussian density gives

    integral_chart exp(sum_l t_l X_l) d rho_J
       = B(V,u) exp(V_vac(zeta))
           E_gamma_C[1_Box_p product_v(1+W_v)
                                 product_l(1+W_l^src)],     (13)
    B(V,u) = [Q_J(V) Z_fine(u)]^(-1)
             H_Z(kappa u)^K_surv exp[-u E_u(a*;V)]
             (2pi²)^(-n) sigma^N_s
             (2pi)^(N_s/2) (det H)^(-1/2).                  (14)

The source product excludes labels included in V_vac. This is
pointwise substitution in the chart, also valid for complex
source couplings. There is no integration over the compact
complement in (13). The prefactor (14) is source independent
at the fixed base and applies to the original normalized
quotient density, restricted to the chart. Multiplying it
by Q_J(V) gives the marginal numerator convention; dividing
(13) by its zero-source value gives the chart-conditioned
generating function. In particular the prefactor keeps
the full energy at a*, the surviving kernel count, fine
normalization, probability Haar volume and Gaussian determinant.

For (F1)-(F2) use (6)-(9) and B=B_pin in the forest notation.
At each action or source vertex take the base S_o=N_R0(T_o)
in axial distance. At a bad cell X take S_bad=N_R0({X}).
These are connected, nonempty, include the activated and source
reader cells, and are uniformly bounded in size. If bases are
disjoint then no pair of readers in them has distance <=R0,
so the cross entry of P is zero. Equations (10), (12) and
(13) give precisely the whole-cell base factors and physical
realization of Z_a in (F3).

Use c=p0/2, G=U+p0, a=1/G, b=1/c, D0=b²/a+b/2,
L_f=max(1,sqrt(2 exp(1) D0)) and K_g=max(1,sqrt(4/(a c)))
from (F4). These are uniform constants after R0 is fixed.
The (F5)-(F6) beta-weighted rooted sums satisfy

    h_weak<=C_weak sigma p³,   h_bad<=C_bad exp(-a p²/8),
    h_src<=C_src r.                                          (15)

Indeed one weak vertex contributes at most
exp(beta |S_o|) K_g^(k |reader_cells(o)|) C' sigma p³.
A root cell sees only a fixed bounded number of action bases:
their readers, connected envelopes and collars all stay
within fixed radius of a factor anchor, and the model has
bounded anchor density and incidence. The Haar terms have one
link as their anchor and are also bounded in number per cell.
A bad-cell term uses a fixed R0 neighborhood and cost
K_g^k exp(-a p²/8). The at most four source bases have
uniform sizes with a constant allowed to depend on the
stated reader sizes and diameters of F,G. This bounds the
source sum even for coincident reader locations. Full-cell
costs in (15) pay for every scalar in the body. V_vac is the
separate exact constant source normalization, not a primitive.

For the threshold H_f of (F7) at fixed beta,k,L_f,e,B_pin,
first choose r>0 small enough for the source bound in (15)
to be <=H_f/4, then increase u_dagger so the sum of the first
two bounds is <=H_f/4. In a uniform use of the contract use
the prescribed upper bounds on e and B_pin from (9) in the
positive majorants defining H_f. This gives h_base<=H_f/2
uniformly. The compact h_comp bound and exact Z_* realization
are additional consumer obligations. Equations (13)-(15)
supply the chart half only.

## 6. Source identities and verification scope

Paths are relative to the respective worktrees' pack parts directories.

| Source | Coverage | SHA-256 |
|---|---|---|
| `nonidentity-marginal-compact-mode.md` | Full, stationary center, relative coercivity and full radial C³ as provisional inputs | `3ef73e9715111804f7ddc135e7bed62bbaaf36278f459e8d71d8fc15e127f83d` |
| `nonidentity-centered-regional-estimates.md` | Full, supervisor worktree read-only, compensated factors, product cube and score convention | `b125f4b80bb0143c4269024d426476deb118bc7b30030c15d31e5fbb0a98b9bc` |
| `marginal-frozen-gaussian-producers.md` | Full, identity-background inverse, paths, counts and chart method | `598af873a6b9da46a94dafe94de05ebef6cc165b2420b32f46cd2983f31dcff6` |
| `zero-shift-marked-density-forest.md` | Abstract (F1)-(F7) contract and explicit threshold (F16) | `d44adc900daf7ac665e502ac950230a8739b120d1a2be4940fd292ea9a09087f` |

The exact law and reader templates are model inputs. The mode and
compensation notes remain conditional premises for this producer, with
independent checking separate. This note neither certifies the forest
theorem nor obtains a compact expansion, connected response estimate
or physical gap. The inherited repo and primary-literature search
and workflow selections are as recorded in the supervisor's checkpoint.
Only this new note was written. No Git state or previously authored
note was changed.
