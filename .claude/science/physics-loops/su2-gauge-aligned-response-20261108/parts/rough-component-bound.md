# Full compact rough-component bound at two steps

2026-11-08. Research proof. The quantified relative-energy supplier below
is proved in `local-relative-coercivity.md`; its application here and both
arguments are checked in `../gates/relative-component-check.md`. The earlier
absolute coercivity alone is insufficient. No mass-gap, connected-log activity
norm, covariance-decay conclusion, or formal retained status is claimed.
The exact compact quotient and all radial normalizers are those of
`local-conditional-tail.md`. No existing file is modified.

## 1. Exact hypothesis required and its quantifiers

Fix L,kappa and the same two-step periodic SU(2) model with terminal V=I.
Terminal-cell distance is shortest periodic l-infinity distance. Ownership
of a retained coordinate is its tail's terminal cell. Each cell owns
m=3L^8+1+4L^4 coordinates. For R let J_R be all owned coordinates and
P_R,C_R the WHOLE factors reading J_R, with output readers and every
normalizer retained. Write n=m|R|, k_R=|C_R|<=9m|R| and

    density_R(a|z) = D_R^-1 exp[-u E_R(a,z)] product_(c in C_R)H_u(r_c).

Here H_u(r)=exp(kappa u r)/Z(kappa u r). Outside factors cancel exactly.
The following sufficient supplier is proved in the companion relative-energy
note and is used explicitly as a dependency here:

(H) There are constants delta0>0, C_*, alpha>0, c_*>0, C_Q<infinity and
rho_Q>0 independent of volume, R and exterior such that, whenever every
exterior reader coordinate has chord distance <=delta0 from I, there is
a measurable choice a*=a*(R,z) with

    d(a*_e,I)<=|log a*_e|<=C_*delta0 exp[-alpha dist(owner(e),R^c)],
    E_R(a*q,z)-E_R(a*,z)>=c_* sum_(e in J_R)[1-w(q_e)]     for ALL q,
    E_R(a*q,z)-E_R(a*,z)<=C_Q sum_e d(q_e,I)^2             (H)

in the last line whenever max_e d(q_e,I)<=rho_Q. Products a*q are
coordinatewise. The chosen logarithm in the first line is merely the
supplier's smallness assertion; all integrations and tail estimates below
are on the full compact group. The distance to the empty exterior is
infinity. Stationarity of a* can be included in H but is not used separately.
The first line may use any stronger boundary-dependent amplitude. The proof
below only uses the stated delta0 amplitude.

The supplier `local-relative-coercivity.md` uses nearest-neighbor
terminal-cell distance. That distance to R^c is at least the l-infinity
distance used here, so its exponential bound implies the first line of (H).
Its contraction construction gives a measurable choice, and its equation (9)
gives the required uniform cap upper bound. This exact premise match is included
in the independent mathematical check of both notes.

This quantitative quadratic upper bound is needed: a qualitative claim
of being quadratic near a* without a volume-uniform constant is insufficient.
Existence without measurability suffices for pointwise bounds, but measurable
selection is convenient for conditional notation. All final upper bounds
are uniform in the choice, so they do not otherwise depend on that selection.

Shrink delta0 if needed so p Cbar delta0<=1/4, where p=5L and
Cbar=max(C_*,1). Such shrinking is permitted only if H is supplied uniformly
on the smaller exterior class with the same constants. Choose
0<b<=min(1,rho_Q,1/(4p)). Work at u>=1.

## 2. Rough components and the actual exterior event

Fix 0<delta<=delta0. A terminal cell is rough iff at least one of its owned
retained links satisfies d(a_e,I)>=delta. Choose an integer h>=0 such that

    C_*delta0 exp[-alpha(h+1)]<=delta/4.                 (1)

Let the rough-component graph join distinct cells at periodic l-infinity
distance <=D, where D=2h+4. Its maximum degree is at most
Delta=(2D+1)^4-1, independent of the torus size. Components refer to the
induced graph on rough cells, with this precise fixed adjacency.

For any nonempty cell set S put R=N_h(S). If R is not the whole torus,
dist(x,R^c)>=h+1 for x in S. Also |R|<=B_h|S| with B_h=(2h+1)^4;
periodic coincidences only reduce this count. Thus (H),(1) put a* within
delta/4 on every coordinate owned by S.

We record the geometric reader radius rather than assuming a halo suffices.
The support in terminal-cell ownership of every fine plaquette has
l-infinity diameter at most one. Each level-zero paired path lies in its
two adjacent fine blocking cubes, which are nested within terminal cubes;
its hidden output has endpoints in those same terminal cubes. Each
level-one paired path lies in its two terminal blocking cubes. Assigning
a positively oriented inverse occurrence to its original tail cannot leave
these endpoint cubes. Consequently any retained coordinate in a factor
reading J_R is owned by a cell in N_1(R). This covers normalizer inputs
and hidden outputs. A terminal output is fixed and has no hidden reader.
The assumed nested centered odd-L cubes are important for this assertion.

Let Omega_ext(S) say that every cell outside R owning an exterior reader
of P_R,C_R is delta-good, meaning ALL its owned coordinates have chord
<delta. This event is measurable outside J_R. If S is an entire nonempty
rough component, Omega_ext(S) holds: every such exterior cell lies within
h+1 of some cell of S, hence within D, and a rough such cell would belong
to the same component. Thus the actual component event is contained in

    {every cell of S is rough} intersect Omega_ext(S).   (2)

No claim that these two events are independent is made. D=2h+4 is a
conservative valid radius; h+1 would suffice for this particular exterior
inclusion. The larger radius is retained as the stated component convention.
If R is the whole torus, Omega_ext is vacuous and (H) still applies.

## 3. Compact integration: matching all powers of u

There are positive constants K_H,k_H,K_G,c_cap depending only on fixed
parameters such that for u>=1,

    H_u(r)<=K_H u^(3/2)                    (0<=r<=1),
    H_u(r)>=k_H u^(3/2)                    (1/2<=r<=1),
    integral_SU(2) exp[-t(1-w(Q))]dQ<=K_G t^(-3/2)       (t>=1),
    Haar{d(Q,I)<=s}>=c_cap s³                           (0<s<=1). (3)

The first and last estimates were proved in local-conditional-tail.md.
For completeness, angular integration gives
H_u(r)^-1=(2/pi)integral_0^pi exp[-kappa u r(1-cos theta)]sin²theta dtheta.
Use 1-cos theta>=2theta²/pi², sin²theta<=theta², and extend to infinity.
The Gaussian integral is a finite constant times (kappa u r)^(-3/2),
proving the lower H bound for r>=1/2. The identical calculation proves the
third bound; by increasing its constant it holds for every t>0, since
for t<1 its right side can dominate one. These are compact Haar estimates,
not replacements of the measure by a Gaussian.

On the product cap d(q_e,I)<=b/sqrt(u), each a*_e q_e differs from I by
at most C_*delta0+b. Exterior readers differ by at most delta0. Every
mean's actual path word has length <=p; telescoping and the choices above
therefore give |M_c-I|<=p(Cbar delta0+b)<=1/2 and r_c>=1/2 for EVERY
selected kernel. This includes a selected kernel whose normalizer is
constant under conditioning. All of its exterior inputs are among the
specified readers. Consequently (H) and the lower bounds in (3) yield

    D_R >= exp[-u E_R(a*,z)-C_Q n b²]
              (c_cap b³)^n k_H^k_R u^(3(k_R-n)/2).          (4)

Let B_S be the event that every cell in S is rough. For a in B_S choose
one offending coordinate in each cell, solely to establish an inequality.
These coordinates are distinct. Since a* is within delta/4 on S,
d(q_e,I)>=3delta/4 on the chosen coordinates. Hence, without any union
bound over witnesses,

    T(q):=sum_e [1-w(q_e)] >=9delta²|S|/32.              (5)

The global lower bound in H, split into two equal parts, implies

    exp[-u(E_R-E_R(a*))] 1_BS
      <=exp[-9c_*u delta²|S|/64] exp[-(c_*u/2)T(q)].     (6)

Using upper H bounds and independent reference Haar, the remaining
integral factors. The compact Gaussian estimate in (3) gives

    numerator(B_S)<= exp[-u E_R(a*)] exp[-a u delta²|S|]
                    K_H^k_R K_0^n u^(3(k_R-n)/2),
    a=9c_*/64,

with K_0 depending only on c_*. Divide by (4). All u powers cancel for
the actual counts n and k_R, including every intermediate/final normalizer.
Thus a constant C>=1 independent of u,R,z,volume satisfies

    mu_R(B_S|z)<=min(1,C^|R| exp[-a u delta²|S|])
               <=min(1,eta(u)^|S|),
    eta(u)=C^B_h exp[-a u delta²].                      (7)

For example C may be any upper bound on
[exp(C_Q b²)K_0/(c_cap b³)]^m [max(1,K_H/k_H)]^(9m),
enlarged to at least one. No factor m^|S| is needed: (5) is a direct
pointwise lower bound on the sum, and the whole product integration in
(6) remains unrestricted after extracting the event charge.

## 4. Disintegration and connected-animal tails

For fixed S, let A_S be the actual event that S is an entire rough component.
By (2), conditional expectation over J_R and (7),

    P(A_S)<=E[1_Omega_ext P(B_S|z)]<=eta(u)^|S|.         (8)

The expectation is in the ORIGINAL normalized two-step quotient law.
Nothing conditions that law on a good sector; good exterior is used only
inside an event inclusion. No independence between exterior cells, rough
cells, or distinct components is assumed.

For a fixed cell x, the number of connected sets of size j containing x
in a graph of degree at most Delta is at most Delta^(2(j-1)). One proof
chooses a deterministic rooted spanning tree for each set and performs its
depth-first traversal; this is a walk of length 2(j-1), with at most Delta
choices per step, and its visited set recovers the original set. Fixing a
neighbor ordering makes the encoding single-valued. This bound applies
also on the finite torus.

Define C(x) as the rough component containing x, empty if x is good.
If theta=Delta² eta(u)<1, summing (8) over component sets yields

    P(|C(x)|>=j)<=eta(u) theta^(j-1)/(1-theta), j>=1.    (9)

As always this may be capped at one. Any connected set of j vertices has
periodic l-infinity diameter <=D(j-1). Thus the probability that the
component containing x has diameter at least d>0 is bounded by (9) with
j=ceil(d/D)+1. A statement about some component anywhere would additionally
require a union over roots and may have a total-volume prefactor; none is
silently omitted here. The bounds are useful once u is large enough that
theta<1, with delta,h and the supplier constants fixed.

## 5. Optional finite real-source derivative for a fixed component event

Fix an event A, such as a specified A_S or the size event in (9), defined
by these fixed coordinate thresholds and independent of sources and V.
Let bounded real original observables F,G be invariant under the rooted
gauge group and independent of V. For real-source tilts of the full law,

    P_s,t(A)<=exp[2|s| ||F||infinity+2|t| ||G||infinity] P(A). (10)

This follows by bounding both the tilted numerator and its normalization.
For a real terminal-link tangent dot V_c, the full log-weight score is
A_c=kappa u <dot V_c,M_1,c>; normalizers have no V dependence. Finite compact
normalized differentiation gives exactly

    partial_s partial_t D_(V_c) P_s,t(A)
       =kappa_4,s,t(1_A,F,G,A_c),
    |partial_s partial_t D_(V_c) P_s,t(A)|
       <=26 kappa u ||dot V_c|| ||F||infinity ||G||infinity P_s,t(A). (11)

The coefficient 26 is the sum of absolute fourth-cumulant partition
coefficients 1+7+12+6. Every partition has one block containing 1_A;
its expectation retains the factor P_s,t(A). Combining (8) or (9) with
(10),(11) gives a real fixed-event derivative estimate at V=I. Varying the
event with V or sources would add terms and is excluded. Arbitrary bounded
noninvariant original sources instead require the orbit treatment of the
previous draft. This is not a complex-source norm or connected-log activity
bound, and does not imply covariance decay for arbitrary observables.

## Proof dependency and limitations

Every tail assertion (7)–(9), and its use in (11), uses (H). Global relative
energy coercivity under the specified small exterior-reader hypothesis,
an exponentially localized small minimizer, and a uniform quadratic cap
upper bound are furnished by the companion relative-energy proof. They do not
follow from the earlier absolute coercivity or identity-centered cap alone.
No absorbing collar is assumed without the exact component/exterior inclusion
above; that inclusion works only with the stated sufficiently small delta0
and the graph tied to h. No mass-gap or full nonlinear response is claimed.

Only this new file was written. No numerical, network or Git actions were
needed. Model identifier unavailable through host tools; inherited supervisor
model, launch effort medium. The fresh-context mathematical check is recorded
in the linked report; it is not a formal audit or retained-status decision.
