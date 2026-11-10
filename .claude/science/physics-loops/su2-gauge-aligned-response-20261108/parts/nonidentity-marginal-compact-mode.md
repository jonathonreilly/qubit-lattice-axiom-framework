# Complete normalized seven-edge marginal at small terminal background

Author proof, 2026-11-09. Conditional finite-model mathematics at
`97fc90828ab071b5813d1c9b6c8a952dc042509b`. The inputs and checking scope
are in §6.

## 1. Exact model and theorem

Fix odd L>=3 and kappa>0. Use the supplied two-layer SU(2) model on the
periodic fine lattice of side L²m, m>=3, with its actual positively
weighted paired-root path means and centered terminal-root fine forest.
Internal trees may be any allowed ones. The hidden coordinates are the
non-tree fine links and all intermediate links, owned by the terminal
cells containing their tails. Let J be the seven independent positive
terminal edges bounding two distinct elementary terminal plaquettes that
share one edge. Fix the surviving terminal values V=(V_c) on O=E2\J.
Use zero sources and probability Haar on the hidden forest slice. Write
I for the group identity, w for the real part of a unit quaternion,
and d(A,B)=|A-B| for the chord distance.

For a hidden interior owned by a set R of terminal cells, select every
fine plaquette and every whole surviving kernel with a hidden reader
owned by R. Count each factor once. The exterior collar B_R consists
of all exterior hidden readers of the selected factors, including every
reader of a radial normalizer. Write z for their fixed values, a for the
interior hidden field, and H_R for the set of interior hidden links.
No selected factor uses a deleted terminal kernel. For full R use the
empty collar. The reader convention and exact Haar quotient are supplied
model premises. They apply also at fixed small nonidentity terminal V
by the exact density in the nonlinear-chart source §1. In the original
compact coordinates, freezing V in the actual density keeps every
surviving kernel exp(t<v,M>)/Z(t|M|). Passing from those coordinates to
a local chart would additionally introduce the Haar Jacobian.

Put t=kappa u, u>=1, Z(s)=integral exp(s w(Q)) dQ under probability
Haar, and define the complete energy of one kernel by

    Phi_u(v,M)=kappa(1-<v,M>)+[log Z(t|M|)-log Z(t)]/u.     (1)

The two kernel types have v=U1,c and v=V_c respectively. Each fine factor
is W_p=1-w(U0,p). Denote the full sum by E_u(a;V) and the selected sum by
E_R,u(a;V,z). For any finite u the exact regional density with respect to
product Haar is proportional to exp[-u E_R,u(a;V,z)], since

    exp(t<v,M>)/Z(t|M|)=[exp(t)/Z(t)] exp[-u Phi_u(v,M)].

Unselected factors are independent of a and cancel on conditioning. The
formula defines the positive continuous conditional density at every
collar, and Z(0)=1 covers a vanishing mean.

**Theorem.** There are epsilon_*, alpha, C, c>0 depending only on L,kappa
such that, for every specified volume, J, allowed forest and u>=1:

1. If sup_c d(V_c,I)<=epsilon_*, the full density has a unique mode a*_u(V)
   relative to product Haar. In the principal log coordinates,
   sup_e |log a*_e|<=C sup_c d(V_c,I). For every compact q (componentwise
   product a*q), the full energy increment satisfies
   `c sum_e d(q_e,I)^2 <= E_u(a*q;V)-E_u(a*;V) <= C sum_e d(q_e,I)^2`.
2. If eta=sup_(e in B_R) d(z_e,a*_e(V))<=epsilon_*, the corresponding
   conditional has a unique Haar mode a*_(R,u)(V,z) and the same
   two-sided compact bound with E_R,u and the sum over H_R. Moreover

       |log a*_(R,u),e(V,z)-log a*_u,e(V)|
          <= C eta exp[-alpha dist(owner(e),R^c)]        (2)

   for proper nonempty R. A collar identical to the global restriction
   gives the global mode restricted to R. For full R the mode is the
   global mode. Empty R gives the empty field and trivial energy bound.
3. The modes are jointly continuous in (u,V,z) on the indicated finite-u
   domains, and C¹ in the group parameters there by local extensions.
   If two admissible global terminal backgrounds differ only on a
   nonempty set S of surviving outputs, with owner set A_S, then

       |log a*_u,e(V')-log a*_u,e(V)|
         <= C sup_(c in S) d(V'_c,V_c)
                        exp[-alpha dist(owner(e),A_S)].  (3)

Distances use the ambient periodic terminal-cell graph. Empty suprema are
zero. In (2) and (3) the difference of logs also bounds the corresponding
chord difference up to a uniform constant. The density ratio at a*q
relative to the mode is exactly exp[-u times the energy increment]. All
estimates concern a fixed terminal background in the stated forest slice.

## 2. Uniform factor bounds and the identity comparison

The compact input from `two-plaquette-compact-coercivity.md` is

    E_J,I^lead(a)>=g sum_hidden [1-w(a_e)],  g>0,          (4)

with all geometry and constant quantifiers as in §1. Here E_J,I^lead
uses W_p and kappa(|M|-<v,M>) for the same surviving factors at V=I.
Write B(s)=(log Z)'(s). For s>=0, the symmetry of w under sign reversal
gives B(s)>=0 and w<=1 gives B(s)<=1. As H(s)=exp(s)/Z(s), one has
(log H)'=1-B>=0. With r=|M|<=1,

    Phi_u(v,M)=kappa(r-<v,M>)+[log H(t)-log H(tr)]/u
                  >=kappa(r-<v,M>)>=0.                   (5)

Every baseline factor vanishes at all-reader identity. Extend q on H_R
by I everywhere else. The unselected factors vanish on that extension at
V=I, so (4) and (5) give

    E_R,u(q;I,I)>=g sum_(e in H_R) [1-w(q_e)]
                 =(g/2) sum_(e in H_R) d(q_e,I)^2.         (6)

This uses the full compact theorem before restriction. Its recovery
paths need not stay inside R.

The factor estimates below are uniform in u, geometry and trees.
Indeed |Phi_u(v,M)-Phi_u(v',M')|<=kappa|v-v'|+2kappa|M-M'|.
The radial term satisfies the stated Lipschitz bound by |B|<=1 and
||M|-|M'||<=|M-M'|. Word telescoping with unit factors and positive
averaging transfers it to the compact reader variables, with bounded
word length. This applies even when either mean is zero. W_p has the
same type of bound. Factor values are bounded uniformly, since all
vanish at identity and the number of readers and the diameter of SU(2)
are bounded.

For local derivatives, fix a common all-reader log chart, including the
output slots, small enough that all means have |M|>=1/2. This follows
from word telescoping and bounded word lengths. On this chart, write
h(s)=log Z(s)-s. The radial contribution beyond the leading term in
(5) is [h(tr)-h(t)]/u. To check the needed orders, the Haar variable
X=1-w has density (2/pi)sqrt(x(2-x)) for 0<=x<=2. Under exp(-sX)
tilting, for s>=1 the denominator is bounded below by a fixed multiple
of s^(-3/2) by integrating on [0,1/s], and the moment numerator of
degree j is bounded above by a fixed multiple of s^(-j-3/2) by
integrating exp(-sx)x^(j+1/2) on [0,infinity). For s<=1 use X<=2.
Hence the tilted moments are O((1+s)^(-j)). Differentiating log of the
tilted integral shows h', h'', h''' are, up to signs, the first three
cumulants of X, so |h^(j)(s)|<=C_j(1+s)^(-j) for 1<=j<=3.
Each order-j chain-rule term uses t^k h^(k)(tr) with k<=j and
t^k/(1+tr)^k<=2^k. With 1/u<=1 this proves common bounds through third
order for all reader derivatives of Phi_u in the chart. Group products,
path inverses and W_p are smooth with bounded derivatives there.
Finite reader arity, incidence and cell range of the supplied templates
turn these estimates into uniform absolute derivative row sums, also
for mixed hidden, collar and terminal-output slots. Repeated
occurrences and periodic identifications retain their multiplicities.
For fixed L the internal-tree patterns in a footprint form a finite set.

Let x be the interior logs (exp(x) denotes quaternion exponential), y
the collar logs and v the terminal logs. Use Euclidean coordinate blocks
at terminal cells. Put F(x;v,y)=E_R,u(exp(x);exp(v),exp(y)) and write
H=D_x² F(0;0,0). Every baseline factor has zero first differential in
hidden directions by smoothness and its nonnegative minimum at I.
Applying (6) along exp(sx) gives H>=g Id. The row bounds and symmetry
give H<=M Id for a common finite M. This is the complete Haar-energy
Hessian, with no log-coordinate Haar term. Let r0>=1 bound the ambient
cell diameter of the full hidden reader set of each factor, so the
Hessian has cell-block range at most r0. Full R uses the same argument.

## 3. Uniform stationary construction

For H as above choose M'>M and set rho=1-g/M' in (0,1). In the
Neumann series H^(-1)=(1/M') sum_(k>=0)(Id-H/M')^k the kth power
has block range k r0 and Euclidean operator norm at most rho^k. Thus

    ||(H^(-1))_(XY)|| <= g^(-1) rho^ceil(dist(X,Y)/r0).    (7)

For any nonnegative 1-Lipschitz cell function s use the block norm
||b||_s=max_(X in R) exp(alpha s(X)) |b_X|. Since the number of cells
within radius r of any cell is at most (2r+1)^4 on the periodic graph,
choose alpha>0 with exp(alpha)rho^(1/r0)<1. Summing (7) by distance
with weight ratio at most exp(alpha dist(X,Y)) gives a common
inverse bound A in all these norms, including s=0. The range
argument uses ambient distance even if R is disconnected.

Let b=max(sup |v_c|,sup |y_e|). On a fixed small parameter and
interior log neighborhood, the finite incidence second/third
derivative bounds give, with s=0,

    ||grad_x F(0;v,y)||_0 <= B b,
    ||D_x² F(x;v,y)-H||_(0->0) <= K (||x||_0+b).           (8)

For the first inequality integrate mixed second derivatives along the
line of parameter logs from zero. For the second integrate the third
derivatives along the line from the all-zero field. An analogous
operator bound holds in every weighted norm with K replaced by
K exp(alpha r0), by the same absolute block row sums and the range
restriction. Increase B if necessary to be positive. For parameter
bound b<b_0, solve grad_x F=0 by the map

    x -> -H^(-1)[grad_x F(0;v,y)+N(x;v,y)],
    N(x;v,y)=grad_x F(x;v,y)-grad_x F(0;v,y)-H x.

For all b<=b_0 the ball of radius 2AB b is mapped into itself:
N(0)=0 and the map has Lipschitz constant at most
A K (2AB+1)b<=1/2, by integrating (8) on its segments.
Choose b_0 small enough for this and for the entire ball and all its
parameters to lie in the common log chart. This includes b=0, where
x*=0. The resulting stationary field satisfies ||x*||_0<=2AB b.
The log is a coordinate chart, so stationarity holds in group tangents.
The iterates from zero converge uniformly with constant 1/2 and are
jointly continuous at finite u, v, y. In particular the stationary field
is jointly continuous.

Further reduce b_0 so A K exp(alpha r0)(2AB+1)b_0<=1/2. At the
stationary field, K_*=D_x² F(x*;v,y) then has inverse

    K_*^(-1)=[Id+H^(-1)(K_*-H)]^(-1) H^(-1)

with norm <=2A in every weighted norm above. This follows from the
norm-convergent Neumann series for the bracketed inverse. At each
finite volume the log-parameter dependence is C¹ by the finite
dimensional implicit function theorem, since K_* is invertible
and F is smooth in the chart. The chosen solutions agree with the
local implicit branch by continuity and local uniqueness. All final
parameter domains are chosen strictly inside the b<b_0 domain.

## 4. Compact comparison and mode identification

Let f be one selected factor, with distinct interior readers S_f.
Its fixed readers include any terminal outputs in addition to any
exterior hidden links. For q on S_f write h_f(q;V,z) for its evaluation
with those fixed values. Define

    D_f(q)=h_f(a*q;V,z)-h_f(a*;V,z)-h_f(q;I,I),
    l_(f,e)=partial_(x_e at 0) D_f(exp(x)),
    p(q)=Im(q).

Here a*=exp(x*) is the stationary field from §3. One has D_f(I)=0.
All background logs in a*,V,z are O(b). The two evaluations with q
compare compact reader assignments at chord distance O(b) per
reader, since d(a*_e q_e,q_e)=d(a*_e,I). Also h_f(a*;V,z) differs
by O(b) from h_f(I;I,I)=0. The global Lipschitz bounds therefore
give |D_f(q)|<=C b for every compact q.

On a fixed small product cap for q=exp(x), interpolate the background
logs (x* on S_f, y, v) linearly from zero to their actual values.
All composed group variables exp(s x*_e) exp(x_e), and all fixed
readers along the interpolation, lie in the common all-reader chart
by decreasing b_0 and the cap radius. Mixed derivatives once in a
background log and up to twice in x are uniformly bounded. This
follows by the third derivative bounds in §2 and smooth
multiplication in the chart. Consequently the first differential of
D_f at zero and the entire Hessian on the cap are O(b) in the local
finite-dimensional norm. Taylor's formula bounds the remainder
after subtracting sum_e l_(f,e) dot x_e by C b sum_e |x_e|².
Since p(exp(x_e))=(sin|x_e|/|x_e|)x_e, its difference from x_e is
O(|x_e|³) and log/chord lengths are comparable on the cap. Therefore

    |D_f(q)-sum_(e in S_f) l_(f,e) dot p(q_e)|
                          <= C_0 b sum_(e in S_f) d(q_e,I)^2.   (9)

On the complement, at least one interior reader has chord distance
at least the fixed cap radius. The global |D_f| bound, the bound
|l_(f,e)|<=C b, bounded arity and |p(q_e)|<=1 prove (9) there as
well after enlarging C_0. In particular this argument uses no
nonvanishing of means on the complement and no log at antipodal q_e.

For each e, sum_f l_(f,e)=0. Along the path q_e=exp(tX), the sum
is the differential of the selected energy along a*_e exp(tX)
minus that of the identity-background selected energy along exp(tX).
Both differentials vanish. Crucially the same p(q_e) is used in each factor reading
e. Thus the linear terms cancel as an algebraic identity at every
compact q, including all antipodal and zero-mean configurations.
With D the maximum hidden-reader incidence, (9) gives

    |E_R,u(a*q;V,z)-E_R,u(a*;V,z)-E_R,u(q;I,I)|
                          <= D C_0 b sum_(e in H_R) d(q_e,I)^2. (10)

Reduce b_0 so D C_0 b_0<=g/4. Equation (6) now gives the lower
bound in §1 with c=g/4. For the upper bound, each identity-background
factor is bounded above by C sum_(e in S_f) d(q_e,I)^2 on the small
cap by zero differential and its uniform second derivative bound.
Off that cap, its uniform bound in value and the fixed minimum
chord distance of some reader give the same inequality with a
larger C. Sum by incidence and use (10) to get the compact upper
bound. This proof compares energy increments by a sum of local
quadratic costs, with no volume-dependent multiplicative comparison
of Gibbs densities.

The lower bound is strictly positive unless q_e=I for all e,
so the stationary field is the unique global energy minimum and
unique mode of the exact continuous Haar density. The density
ratio follows directly from the exact formula in §1. Haar is invariant
under the coordinatewise map q -> a*q, which is left multiplication
by a*_e in each coordinate. No chart Jacobian is part of that ratio.

## 5. Localization and admissible collars

For two admissible sets of parameters in the common small log
domain, interpolate their log vectors linearly. Along the segment
let a dot denote differentiation in the interpolation variable.
Differentiating stationarity gives

    K_* dot x* = -D_(v,y) grad_x F(x*;v,y)[dot v,dot y].   (11)

For a terminal-only change supported on S, the right side is zero
outside a fixed r1-neighborhood of A_S. Indeed each changed output
is a slot only in its own terminal kernel, whose hidden reader
owners are within a bounded distance of the output tail by the
actual templates. Uniform mixed second derivative row sums bound
the right side in ||.||_0 by C sup_c |dot v_c|. With
s(X)=dist(X,A_S), the weighted bound is at most
C exp(alpha r1) sup_c |dot v_c|. Apply the inverse bound in §3
and integrate (11) to get (3), using the uniform Lipschitz bound of
the principal log in chord distance on the fixed small cap.
The logarithm is smooth there as a function of the imaginary
quaternion part and has bounded derivative on its smaller
Euclidean ball. The exponential is Lipschitz on the corresponding
log ball. The proof also gives the localized differential bound
for an infinitesimal change in one terminal output.

For the regional comparison let z^0 be the collar restriction of
a*_u(V). All factors touching an interior reader are exactly the
selected ones, so the restriction of the full mode to H_R is
stationary for this conditional. It is also the unique conditional
minimum: varying a on H_R at exterior a*_u(V) changes only selected
terms, and full strict minimality then applies. It therefore equals
a*_(R,u)(V,z^0) when the collar is in the common small log domain.
Choose epsilon_* small enough that for every V and z in the theorem
both the terminal and the collar logs (for z and z^0) have norm
strictly below b_0. This is possible by the global stationary estimate
with y absent, log/chord comparability, and
d(z_e,I)<=eta+d(a*_e(V),I). The interpolated collar logs stay below
b_0 too.

Now hold V fixed and interpolate from the logs of z^0 to those
of z. The right side of (11) has interior reader support within
distance r0 of R^c, since only factors with a collar reader contribute.
Its block-sup norm is bounded by C sup_e |dot y_e|<=C' eta by
mixed second derivative row sums and the small-cap log bound. With
s(X)=dist(X,R^c), the weighted norm is bounded by C' exp(alpha r0) eta.
Apply the inverse bound and integrate to obtain (2). If B_R is
empty there is no forcing and the equality with the restriction
holds throughout. Full and empty regions were specified in §1.

## 6. Source identities and check scope

The following were read in full in the assigned worktree. Paths are
relative to this note.

| Source | SHA-256 | Use |
|---|---|---|
| `two-plaquette-compact-coercivity.md` | `b77fdb722d19c96594cddded301d9dd019c412b875721f5c28d1461415bb246e` | Supplied uniform leading-energy estimate (4) and actual geometry |
| `marginal-regional-relative-coercivity.md` | `2d142414fb4992c2a1e907d42d15ca9f7164ee6e90c892d8c3d529b39e297385` | Regional selection and identity-reference mechanism |
| `marginal-normalized-regional-coercivity.md` | `bd3fa8b5eb989c7718ad5d760a913e33166f3e9edcf52b9f17f82cbd809ca255` | Complete normalized Haar energy and identity-terminal compact comparison |
| `marginal-nonlinear-chart-estimates.md` | `b1e26baa37cf1dc47331d9a98a834afda5e7634d62f31df50600fd321fc45cb7` | Exact density at fixed V and uniform mixed-reader templates and radial derivative method |

The parent supplied the completed repo and primary-literature pass,
including the closest small-nonidentity V fixed-chart result. This
proof uses the identity-centered compact coercivity and finite-template
bounds as stated premises, then transfers the regional argument by
including terminal logs in the fixed parameters. No outside theorem
for compact nonidentity coercivity is used. The decisive comparison
is (9)-(10), and the localization uses (7) and (11). Independent
mathematical checking of this implication and its inherited premises
is separate. The conditional energy theorem supplies no rough-collar
control or volume-uniform concentration, covariance, or connected
response estimate.
