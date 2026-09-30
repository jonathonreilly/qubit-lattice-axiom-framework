# Actual fixed-time infinite rank from the empty-sector plaquette obstruction

This continues the same actual-input reachability attack. The claimed
result concerns one fixed graph and the specified original preparation and
source labels. It uses no numerical evidence and does not prove full
phase-fiber or closed-subspace faithfulness at fixed time.

## 1. Inputs and exact target

Keep all definitions of COHERENT_SEPARATION_PROOF809a5838: L divisible by4,
L>=8, n=L^3/2,4<=b<=n/4, the complete original b-label word, supplied
positive K,delta,kappa, the actual no-event generators L_j, and the fixed
source T at h=(4,2,0). Its dark physical words Xi_w have electric norm
2b+3+wL. The first-hop words Theta_w have norm2b+1+wL. Write m_w=wL/4.
The orthonormal first-hop-range vectors are eta_w=P_M Theta_w/c, with
the actual physical range projection and c>=1/sqrt(3) proved there.

For d>=1 put

    X_d=span{Xi_1,...,Xi_d},     Y_d=span{eta_1,...,eta_d}.

There exists a dense-G_delta full-Lebesgue-measure E subset(0,infinity)
such that, for every s in E and every finite d,

    P_Xd T rho_b(s)T* P_Xd is strictly positive on X_d,
    P_Yd A_h rho_b(s)A_h* P_Yd is strictly positive on Y_d. (1)

In particular the actual source, its actual dark compression and the
actual first-hop output all have infinite rank at those SAME positive
times. All parameters, graph, b and original labels are kept fixed when
intersecting over d. No fixed-time faithfulness on the closed infinite
spans X or Y is asserted.

## 2. Literal final electric support has no four-cycle

Only edges with NONZERO final electric field are used in this argument;
an occupied B site does not make every incident link a nonzero field edge.
For Xi_w these edges are:

1. The whole x ring at y=z=0, of length L. The first birth's old outward
   edge (0,0,0)->(1,0,0) lies on it with the same sign.
2. The first birth's marked edge to(0,1,0).
3. For the distinct chosen grid A centers a with y=0 modulo4, a!=a0,
   the two edges a->a-e_y and a->a+e_y.
4. The two special z-birth edges from a_z=(4,2,L-2) to a_z-e_z and a_z+e_z.
5. The three source edges h->h+e_x, h->h-e_x and h->h+e_z.

The grid centers include a_minus=(4,0,0) and a_plus=(4,4,0). Their B
endpoints have y=1 or3 modulo4. Distinct grid centers have distinct such
B endpoints: equality forces identical x,z and y, since a separation2
in y cannot occur between centers both0 modulo4. Periodicity causes no
exception because L is divisible by4 and L>=8. The excluded a0 is the
only grid center whose marked B endpoint could equal(0,1,0).

Thus each grid pair is a two-edge tree. It meets the x ring only when its
A root itself lies on that ring; neither of its B leaves lies on it.
Trees at other roots are disconnected from the ring and from one another
in this electric-support graph. The special z pair lies at y=2, with
B z-coordinates L-3 and L-1. The source B endpoints lie at y=2 with
z=0 or1. For L>=8 these are disjoint from the special pair and all grid
B endpoints; the source A center is distinct from every preparation A.
These components are therefore separate two- and three-edge stars.

The only cycle of this graph is the long x ring. In particular it contains
no four-cycle. The first-hop word Theta_w simply replaces the three source
edges in item5 by the single edge h->h+e_x, so its support also has no
four-cycle. This checks every allowed choice of remaining grid births.

The three already occupied B neighbors h-e_y,h+e_y,h-e_z receive their
preparation fields from a_minus,a_plus,a_z respectively. Their zero-field
links from h are NOT in the literal support above. This distinction avoids
confusing the full occupied star with the actual electric support.

## 3. Why initial waiting cannot occur in the leading coefficient

In the NB=0 physical sector total charge n and all A occupancy force every
A charge to be+. The landed pair-form theorem gives, on every allowed
divergence-free field in this sector,

    Q_0=c I+2 sum_p (W_p+W_p*),                         (2)

where p are the ordinary four-cycles. The value of c is irrelevant here.
Each off-diagonal summand shifts one plaquette circulation with electric
l1 norm4; the diagonal part shifts no field. This is the actual empty-B
sector of the supplied Hamiltonian, not a new independent-link model.

Consider a complete history amplitude tested against Xi_w. Any Taylor
term of total generator degree j has field l1 support at most2b+3+4j.
Thus all degrees below m_w vanish. At degree m_w the bound is saturated.
Every generator must be i delta Q, since R has band at most2 and D band0.
Expand one contributing term into its literal bounded hop paths. There
are at most2b+3+4m_w individual unit field shifts in it. Equality with
the final norm implies that, on each edge, all shifts have the final sign;
no shift on a zero final-field edge and no subsequent cancellation is
possible. This is equality in the l1 triangle inequality, not a choice
of a favorable path after cancellations.

If any generator factor occurs in the initial no-birth gap g0, the first
chronological one acts on Omega in sector NB=0. Its scalar part in (2)
loses four units of the required field budget. Its off-diagonal part is
a four-cycle shift. All four of its edges would have to lie in the final
electric support, which section2 forbids. Therefore every such term is
zero. This applies to the complete Q sum and all original coherent birth
branches; it requires no claim about fixed signed flux of those branches.

The identical argument for Theta_w uses2b+1+4j and the first-hop map
A_h=F_h P_(h,3), whose projection is diagonal and whose hop has band1.

Let the complete source history at gaps g=(g0,...,gb) be v_T(g). Its first
nonzero homogeneous coefficient against Xi_w is consequently

    <Xi_w,v_T(g)>=-(i delta)^(m_w) P_w(g1,...,gb)
                                      +O(s^(m_w+1)),    (3)

where s=sum g_i. P_w has degree m_w, nonnegative real coefficients and

    P_w(g1,...,gb)>=2^(m_w) gb^(m_w)/m_w!.              (4)

This is the complete polynomial from the checked winding proof, now with
the g0-independence proved. The fixed-order remainder and derivatives are
legitimate on finite-field Omega by that proof's weighted-domain bounds.
For each finite collection of fixed positive gap ratios the remainder is
uniform as s decreases to0. No uniformity in w or d is required.

For first-hop testing against Theta_w there is a polynomial Q_w with the
same properties and positive leading phase +(i delta)^(m_w). Testing
against eta_w divides it by c, since every first-hop history lies in M_h.

## 4. Exact finite determinant at small positive time

Choose fixed beta_i>0, i=1,...,b, with sum beta_i=1; beta_i=1/b suffices.
For each finite d choose distinct0<a_1<...<a_d<1, for example a_j=j/(d+1).
For column j use the legal interior history ratios

    u0^(j)=1-a_j,       ui^(j)=a_j beta_i, i>=1.         (5)

All original labels are the same fixed string in every column. The total
time is s for every column, and no gap is zero. Define the d by d matrix

    F_d(s)_(w,j)=<Xi_w,v_T(s u^(j))>,   1<=w,j<=d.

Homogeneity and (3) give

    F_d(s)_(w,j)=c_w s^(m_w) a_j^(m_w)+O(s^(m_w+1)),
    c_w=-(i delta)^(m_w)P_w(beta)!=0.                  (6)

After dividing each row by c_w s^(m_w), the matrix tends as s decreases
to0 to [a_j^(m_w)]. Put x_j=a_j^(L/4). Its determinant is exactly

    det[x_j^w]_(w,j=1)^d=(product_j x_j)
                                  product_(i<j)(x_j-x_i)!=0. (7)

Thus det F_d(s)!=0 for every sufficiently small positive s, with the
threshold allowed to depend on d and all supplied parameters. The same
construction for eta_w and the first-hop histories gives a matrix
G_d(s) with nonzero determinant at sufficiently small positive s.

If det F_d(s)!=0, each nonzero vector in X_d has a nonzero pairing with
at least one of the d complete histories at the interior points (5).
Strong continuity gives a neighborhood of positive simplex measure where
that pairing remains nonzero. The actual original-history expansion has
positive weight kappa^b on this same label string. Integrating its squared
pairing therefore proves strict positivity of the actual compression in
(1). The other label strings and all other histories add positive terms.
The same argument applies to G_d and Y_d. Point evaluations here certify
an open positive-measure contribution; they are not assigned probability
as isolated exact event times.

## 5. One common full-measure set of fixed times

Each entry F_d(z) is the complete bounded-source history evaluated at
fixed positive ratios, so the lower-half-plane Dyson construction in
frozen proof10eb8ccd applies. In the fourth quadrant each entry obeys
|F_d(x-iy)_(w,j)|<=C exp(My), with C independent of x,y and M the maximum
bounded-perturbation norm over sectors0,...,b. Hence det F_d is holomorphic,
continuous to positive real times, and bounded by d!C^d exp(dMy). It is
not identically zero by section4.

Multiplying by exp(-i d M z) gives a bounded nonzero holomorphic function
in that quadrant. The boundary uniqueness/measure-zero-zero-set argument
already proved in frozen section5 applies. Therefore

    E_d^T={s>0:det F_d(s)!=0}

is open, dense and full measure. The identical conclusion holds for
E_d^A from det G_d. Taking the countable intersection over d of both sets
gives a dense-G_delta full-measure set E, and proves (1) simultaneously
for all d at every s in E. This is a legitimate countable intersection
of determinants, each controlling all vectors of one finite-dimensional
space; it is not an uncountable intersection of scalar tests.

An operator of finite rank r cannot have a positive-definite compression
to an (r+1)-dimensional subspace. Equation(1) therefore proves the stated
infinite-rank claims. Every Xi_w is dark, so the dark-compressed source has
the same finite compressions. No propagation of dark states under the
fast Hamiltonian is assumed.

## 6. Remaining reachability and physical limitations

Positive definiteness of every finite compression does NOT imply
faithfulness on the full closed infinite-dimensional span. A positive
trace-class operator can have a kernel vector with infinitely many nonzero
coordinates while all its finite coordinate compressions are positive
definite. Thus this proof leaves possible infinite-support coherent
annihilators at individual times, as well as the much larger actual
first-hop/fiber density question, open.

There is no time-independent positive lower weight, no estimate uniform
in d, w, graph size or spin cutoff, and no lower energy-tail or mean-age
bound. Exceptional individual times have not been excluded. The result
is a fixed-graph rotor statement about the actual derived source of the
supplied original mark process. It adds no observed instrument, proxy
preparation, permanent-record interpretation, physical clock or law
selection. It is part of the same hard reachability attack, not a separate
delivery milestone, formal review, audit or retained claim.
