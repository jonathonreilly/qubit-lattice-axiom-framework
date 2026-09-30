# The physical four-particle periodic band

This is current supporting proof for the canonical four-particle threshold
note, under exactly its supplied Hamiltonian and positive parameters. It has
no separate claim classification or runner. The owner note binds this proof
as a primary-runner input. All Hilbert spaces below retain physical hard-core
occupation configurations.

Fix R>=14 and a cubic torus of side L>=10(R+4), V=L^3. Put

    a=min(tau,mu/12), C_B=28000322,
    C_R=4+15 C_B(R+4)^3,
    Delta_L=a/[C_B R^3+C_R L^2],
    delta_L=(2R+9)^3/V,
    s_R=(2R+9)^3-(2R-7)^3,
    theta_L=120 max(mu,2tau)s_R/[V(1-delta_L)].           (1)

Assume delta_L<1. We construct a rank-fifteen physical isometry V_L such
that H_4,L>=Delta_L(I-V_L V_L^*) and V_L^*H_4,L V_L<=theta_L I.
At fixed R, theta_L/Delta_L=O(L^-1).

## A local occupation estimate and isolation

For a free rectangular grid C with longest side at most twice its shortest,
and f(p)=0 at any vertex, the elementary pinned estimate is

    sum_C |f|^2<=448 |C| sum_(edges in C)|delta f|^2.     (2)

Here is a proof fixing its volume dependence. Normalized Neumann cosine
modes have squared value at most8/|C| and eigenvalue at least4|n|^2/smax^2.
The squared difference between a mode at x and p is at most32/|C|.
For the point-difference inverse sum, group modes by max coordinate r:
there are at most7r^2 in that shell. The resulting bound is at most
56smax^3/|C|<=448. Cauchy in the mode expansion, followed by summation in x,
proves(2). Constant modes cancel in a point difference. The estimate works
componentwise and for a cyclic rectangle with one cut in each coordinate.

Let B be an inner box, C its one-site enlargement as distinct torus sites,
and use the fifteen centered bare pair words of the canonical note. Fix an
annihilation output eta meeting B at y. A bare word with endpoint offsets
u,v has amplitude f_eta(x)=<eta|B_t(x)psi>, with literal pin f_eta(y-u)=0.
That point lies in C. Applying(2) and summing only those output eta gives

    sum_(t,x in C, eta intersects B)|f_eta(x)|^2
                                  <=448 |C| Egrad15_C. (3)

The output restriction is independent of the center x and is dropped only
after summing positive gradients. No occupation projector is moved through
an annihilator. On configurations with at least three particles in B,
removing any graph edge incident to B leaves a particle in B. Such an edge
has a bare representation centered in C. The directed neighbor count counts
each physical edge at most twice, while the bare words count it at least
once. Combining this fact with1<=(m-1)(m-2)/2+m yields

    <N_B 1_(N_B>=3)><=<D_B>+896 |C| Egrad15_C.          (4)

D_B keeps the original full-torus neighbors of its centers. This is positive
row restriction and counting, not a deletion or redefinition of neighbors.

Let F_R count occupied x whose Chebyshev radius-R cube contains at least
three occupied sites. Partition the coordinate circles into intervals with
lengths between R and2R, enlarge each product box B by R to C and by one
more site to C+. Then F_R<=sum_B N_C 1_(N_C>=3). The rectangles C+ have
aspect ratio at most two, volume at most125R^3 and overlap at most125 for
each site or free edge. In one dimension at most five expanded intervals
can meet a point, which proves the overlap bound. Applying(4) gives

    <F_R><=125<D>+14000000 R^3 Egrad15.                 (5)

A graph edge is R-isolated when every other occupied site is farther than
R from either endpoint. Let B_R count particles outside these edges. At
N=4, on a nonmatching configuration B_R<=4<=4D. On a matching configuration
choose any perfect matching. If its two edges are mutually R-isolated then
B_R=0. Otherwise there is a close cross pair from the two edges. Each of
those two endpoints has its own partner and the other endpoint in its
R-cube, so F_R>=2 and B_R<=4<=2F_R. Thus, pointwise,

    B_R<=4D+2F_R.

The simultaneous H>=mu D+a Egrad15 and(5) imply the deliberately loose
bound used here,

                       <B_R><=C_B R^3 <H>/a.            (6)

The same argument holds with R replaced by R+4. This proof is confined to
N=4 and the N<=2 outputs required below; it supplies no all-N phase statement.

## A bookkeeping isometry retaining the residual particles

For an occupation S, let A_R(S) be its selected isolated graph edges and
E_R(S) the remaining occupied sites. They are unique and disjoint. Map

    I_R|S>=|A_R(S)>_edge Fock tensor |E_R(S)>_environment. (7)

The auxiliary Fock factors have occupation zero or one on each selected
edge; their image is constrained by separation and compatibility with the
environment. Recovering S by the union proves that I_R is an isometry.
It asserts no physical bosonic pair commutator.

Removing a selected edge cannot change isolation of the remaining edges or
create a new edge inside its distant environment. Therefore, for the actual
guarded annihilator

    c_e=B_e product_(z not in e, dist(z,e)<=R)(1-n_z),

one has I_R c_e=a_e I_R, and likewise for successive removals. The maps on
N=4 and its N=2,0 outputs are used in this identity. Guarded annihilation
correlations and their positive quadratic rows consequently agree exactly
with those in the auxiliary image. The environment has particle number B_R.

Use the nine forward bond fields and put J=Egrad9+S/mu. For a fixed output
eta, guarding multiplies f_eta(e)=<eta|B_e psi> by
q_R(e;eta)=1_(dist(eta,e)>R). Each positive J row is sum_e l_e f_e. Picking
one edge e0 gives

 |sum l_e q_e f_e|^2<=2|sum l_e f_e|^2
                +2||l||^2 sum_e |q_e-q_0| |f_e|^2.     (8)

Edges in a row have Hausdorff distance at most four. An unequal guard thus
requires e to be(R-4)-isolated but not(R+4)-isolated. Such edges are disjoint,
and each consumes two particles counted by B_(R+4). The weighted incidence
sum of ||l||^2 over rows containing one forward edge is at most15: six
gradient rows contribute 12; an axial singlet contributes2; a plane edge
occurs at two centers, each with three difference rows of squared norm1/2,
contributing 3. Summing(8), using J<=2H/a and(6), proves

                    J_guard<=C_R H/a.                  (9)

All sums resolve actual annihilation outputs. This bound preserves shared
physical amplitudes and does not independently minimize removal fibers.

## The five soft modes and the physical compression gap

The one-body space of unique edges has nine orientations per anchor. Its
five constant normalized vectors are the real matrix U defined in the owner
note. For a periodic field f=m+q, with q of mean zero, the first positive
nearest-neighbor gradient eigenvalue is4sin^2(pi/L)>=16/L^2. The S form has
norm at most2mu, and S(m)=2mu V||P_high m||^2, P_high=I-UU^T. The squared
triangle estimate gives

    V||P_high m||^2<=S(f)/mu+2||q||^2,
    dist(f,constant U)^2<=3||q||^2+S(f)/mu<=L^2 J(f).    (10)

The same bounds apply to Hilbert-space-valued annihilation outputs. In the
auxiliary image, let N_exc count edge particles outside the constant U
subspace. Equations(9)-(10) give N_exc<=C_R L^2 H/a in expectation.
Let P_aux select empty environment and two particles in those five modes.
On the fixed physical N=4 image, every orthogonal auxiliary component has
at least one environment particle or one excited edge particle. Hence

    I-P_aux<=B_R+N_exc,
    H>=Delta_L[I-I_R^*P_aux I_R].                        (11)

Let W_2 embed Sym^2 C^5 into the constant auxiliary edge modes with empty
environment, and T_L=I_R^*W_2. For a fixed bond orientation the anchors
excluded by proximity to a second edge number at most(2R+9)^3. Summing the
ordered uniform-pair norm, with all internal entanglement retained, gives

    (1-delta_L)I<=G_L=T_L^*T_L<=I.                       (12)

The literal physical coefficient of T_L[A] on separated edges is
sqrt2(UAU^T)_(d,e)/V, since each normalized auxiliary pair mode has its
V^-1/2 factor. In the normalized translation-orbit basis that coefficient
is sqrt2(UAU^T)_(d,e)/sqrt V. Thus V_L=T_L G_L^-1/2 is an isometry of rank15. The positive contraction
I_R^*P_aux I_R=T_L T_L^* has range P_L=V_L V_L^* and is at most P_L.
Equation(11) proves H>=Delta_L Q_L, Q_L=I-P_L. This is a full physical
operator inequality, including every momentum sector.

## Uniform trial energy and finite Schur matrix

All inputs in T_L have two separated graph edges, so D=0. Also
S+W<=max(mu,2tau)J, since the collective definitions give W<=2tau Egrad9.
For a residual selected edge eta, the unguarded annihilation amplitude is
V^-1/2(Uv_eta)_d, independent of its anchor, and sum_eta||v_eta||^2=2.
This follows directly by annihilating one particle in the normalized
auxiliary symmetric tensor. A physical graph annihilator removes an entire
selected edge because R>2; these are all its outputs.

Every J row annihilates an unguarded constant U vector. Its guarded row is
therefore bounded by||l||^2 sum_e|q_e-q_0||(Uv_eta)_d|^2/V. An unequal guard
places a removed endpoint in a shell of radii R-4 and R+4 about a residual
site. For each orientation, the union has at most4s_R anchors. Using the
incidence bound 15 and then sum_eta||v_eta||^2=2 gives

    T_L^*H T_L<=120 max(mu,2tau)s_R/V I,
    V_L^*H V_L<=theta_L I.                              (13)

The shell is embedded without wrapping alias under the stated L condition.
This is a matrix inequality on all fifteen channels, not just coherent ones.

On Q_L, C_L=Q_L H Q_L>=Delta_L is invertible. Define

 S_L=V_L^*H V_L-V_L^*H Q_L C_L^-1 Q_L H V_L.             (14)

Completing the square proves0<=S_L<=theta_L and identifies<A,S_L A> as the
minimum of<Psi,H Psi> subject to V_L^*Psi=A. The complement minimizer is
unique. Since H and V_L are translation invariant, it lies at momentum zero.

For theta_L<Delta_L, min-max yields exactly15 eigenvalues below Delta_L;
all others are at least Delta_L. On0<=lambda<=theta_L,

 0<=(C_L-lambda)^-1-C_L^-1
                    <=[lambda/(Delta_L-lambda)]C_L^-1.

The zero-energy Schur subtraction is at most V_L^*H V_L<=theta_L. Comparing
inertia after block Gaussian congruence, with continuity at degeneracies,
gives for the ordered low physical eigenvalues lambda_j and Schur values s_j

    lambda_j<=s_j<=[1+theta_L/(Delta_L-theta_L)]lambda_j. (15)

The other momentum sectors are orthogonal to the invariant frame and have
energy at least Delta_L. Thus all 15 low levels lie at momentum zero.
The rescaled eigenvalue error in(15) is O(L^-1), because s_j=O(L^-3).
This proves the finite-band input to the owner's threshold limit. It neither
evaluates S_L nor replaces a large system's physical boundaries by cell seams.
