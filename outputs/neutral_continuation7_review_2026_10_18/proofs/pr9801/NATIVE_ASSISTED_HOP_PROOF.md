<!-- Original PR9801 source SHA256 2c39a5db6e3ca82a9d4e7c4634b274ecb2634b12c2e394b47de3aa7c404df006. -->
**Source boundary:** Complete mathematical source follows. Historical verdicts, replay narratives and workflow instructions are provenance only. Mathematical identities and constructive arguments retain their explicit hypotheses; an old status supplies no current certification. Earlier exploratory statements must be read with the later corrections in this unit.

# Native background-changing motion and a prepared neutral vertex

Status: bounded-support. One physical qubit per site, supplied Hamiltonian
H=-J sum(ZZ_z+lambda XX_x+lambda YY_y), longitudinal period four. There is
no additional interaction. This is coefficient mathematics and exposed
model development, not an observed scalar or gravitational coupling.

## 1. Complete nearest-hop operator

Use the singleton/background basis of NATIVE_PROBE_LOOP_PROOF.md and the
canonical degenerate N=2 Schrieffer-Wolff gauge. Write X_i,Y_i,Z_i for logical
column Pauli operators, with Z_i the majority sign. Fix the singleton layer;
its exact plane parities prevent its change. For nearest columns i,j,
the complete matrix block between their particle positions is, at fixed R,

 Hji/J = -lambda I +lambda³(I/8-X_i X_j/4)+O_R(lambda^4),    x edge,
 Hji/J = -lambda Z_i Z_j
          +lambda³(Z_i Z_j/8-Y_i Y_j/4)+O_R(lambda^4),      y edge. (1)

The displayed Pauli operators act on the background, not extra qubits.
The order-two nearest block is zero. The explicit x-edge term is a native
vertex into precisely the column-pair operator of the neutral coefficient
Hamiltonian K=-4P-5E. It is not merely a chosen fluctuating hopping strength.
The formula is gauge-specific; physical uses require matching dressed
preparations and readouts, not a gauge-independent interpretation of an
isolated effective coefficient.

## 2. Complementary-layer process

Start with a singleton at layer z of column i over signs s_i,s_j. Apply the
same transverse edge at each of the other three layers. The endpoint has
column i fully reversed and column j with a length-three interval: it is
a singleton at j,z over a background with BOTH i and j reversed.

The six orders have two denominator pairs (-4,-4) and four pairs
(-4,-8) or (-8,-4), since the intermediate wall numbers are four or six.
Their denominator sum is 2/16+4/32=1/4. Three XX insertions give product -1;
three YY insertions give s_i s_j. The amplitudes are consequently -1/4 on
x and s_i s_j/4 on y. In logical notation the latter is
Z_i Z_j X_i X_j/4=-Y_i Y_j/4.

These six changed physical sites exhaust the three insertions. No different
edge geometry reaches that endpoint. Canonical folded terms cannot reach
it: both the first-order singleton hop and the two-insertion operator
PVQ R² QVP preserve the majority background. Half-column states have the
wrong exact parity. Thus this term survives the canonical subtraction.

## 3. Ordinary-background paths and exact cancellation

Let P project onto the full N=2 cluster, Q=1-P, V be the dimensionless
transverse interaction, and R=Q(4-H0/J)^-1 Q. The canonical third coefficient is

 D3=PV R V R VP - (1/2){PV R² VP,PVP}.                       (2)

For the ordinary nearest x endpoint, write B=8R² for the number of physical
transverse bonds at height four, and P_+,P_- for the two adjacent background
plaquettes. Exact local enumeration gives

 raw=-(B+11)I/64+(P_++P_-)/64,
 folded=-(B+19)I/64+(P_++P_-)/64.

Their difference is I/8. The ordinary y expressions have the common
factor Z_i Z_j; their difference is Z_i Z_j/8. Thus possible background
plaquette terms cancel here, rather than being omitted from the vertex.

The source-bound symbolic replay enumerates physical first and last bonds,
joins their intermediate states by a possible middle bond, excludes N=2
intermediates, and accumulates exact rational coefficients of arbitrary
background-sign monomials. It computes the folded operator independently.
R=6 and R=7 controls have different B and identical final local coefficients.
An independent ordered-three-word enumeration gives the same result.

For arbitrary sufficiently large R the connected three-bond paths near the
specified nearest edge have fixed support, with no transverse wrapping.
The only volume dependence comes from a retraced bond disconnected from
the hop. Those terms cancel against the folded normalization term, as the
B terms show. Remaining connected patterns are already enumerated locally.
Per-layer parity fixes the singleton layer. At most six changed spins and
even parity of full-column changes allow only the original background or
the two endpoint columns reversed. Thus (1) contains all nearest-endpoint
outputs, not only the selected six complementary paths.

## 4. Positive prepared neutral vertex

For even fixed R in the native coefficient vacuum, the ground g is unique
and in the all-positive row/column-X sector. In the logical-X basis its
amplitudes are positive. The amplitude-ratio bound of
BULK_SLAB_RESPONSE_PROOF.md gives, for every plaquette,

 <Pp> >= m =2h/[sqrt((16g_c)^2+4h²)+16g_c], h=4,g_c=5.

Here g_c denotes the coupling coefficient, not the state. Numerically
m=0.04987562112089027. A boundary-crossing edge operator E_e=X_iX_j
anticommutes with Pp. For anticommuting Hermitian involutions,
<E_e>²+<Pp>²<=1. Therefore

 Var_g(E_e) >=m²>0.                                       (3)

E_e preserves the all-positive sector, whose ground is unique. Its centered
weight is consequently in positive-energy neutral background states. This
is a local vertex-weight statement; it does not locate a single pole.

Let g_lambda be an actual vacuum-block ground in the matching finite-box
reduction, converging to g. Prepare a singleton at i over g_lambda and test
its x-neighbor j with the background component orthogonal to g_lambda.
The identity pieces in (1) are exactly elastic. Hence the squared norm of
the off-diagonal Hamiltonian vertex is

 ||Q_g Hji g_lambda||²
   =J²lambda^6 Var_g(E_e)/16+O_R(J²lambda^7).               (4)

It is bounded below asymptotically by J²lambda^6 m²/16. This coefficient
comes from native paths, not a fitted scalar coupling. Interpret (4) in
matching dressed channels. It is an infinitesimal prepared transition
vertex, not an independently isolated finite-time emission rate: ordinary
hopping, repeated paths and environment evolution also act at finite time.
A physical detector implementing this channel has not been derived.

## 5. The relaxed-loop limitation

The prepared background above is not the energy-minimizing heavy
background. NATIVE_DRESSED_PATCH_PROOF.md gives <F>=O(lambda^(3/2)) for
near-minimal dressed singleton states along its growing-box family, where
F=sum_i n_i sum_(p incident i)(1-Pp)/2. Define the particle-conditioned loop
sum W=sum_i n_i sum_(p incident i)Pp=4I-2F. Since 0<=F<=4,

 Var(W)<=<(W-4I)²>=4<F²><=16<F>=O(lambda^(3/2)).             (5)

For a specified one of the four relative plaquettes, its conditioned loop
W_a is an involution with 1-W_a twice that bad-flux projector, bounded by
2F. Consequently Var(W_a)<=4<F>. Thus the suppression is not cancellation
between four unsuppressed loop sums.

For a stationary eigenstate this bounds its total inelastic spectral weight;
for a near-minimal nonstationary state it is only a variance/centered-action
bound. Keep the dressed singleton projection: odd parity alone does not
exclude all higher-wall sectors. Equations (3)-(4) concern the different
operator E_e in a prepared vacuum environment. Equation (5) must not be
misused to suppress E_e, identify the original microscopic bond readout,
or prove the full relaxed feature's scalar response. That response remains
an open dynamical calculation.

## 6. Surviving assumptions

The native microscopic action, four-layer slab, small lambda, specified
state and channel preparation remain supplied. The result derives an
interaction vertex and challenges the common-environment assumption. It
does not derive Lorentz invariance, three-dimensional particle propagation,
fermionic statistics, universality of mass coupling, measurement apparatus,
or a cosmological field identification.
