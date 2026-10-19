<!-- Original PR9793 source SHA256 c50312841b1822f7053e2831d74b8e1a48a57a8067620f20a410f61e69bc2419. -->
**Source boundary:** Complete mathematical argument follows. Historical verdicts, execution narratives and provisional instructions are provenance only. Exact identities and conditional mathematical implications remain live; no audit status or additional physical premise is conferred. Earlier exploratory statements are read with their explicit later corrections.

# A native extended defect and its derived local environment

Status: bounded-support. Supplied Hamiltonian H=-J sum(ZZ_z+lambda XX_x+
lambda YY_y), J>0, one physical qubit per site, longitudinal period four,
even transverse periods R. The geometry, anisotropy, ground-state question,
and identification of lattice units remain premises. No new interaction,
external environment potential, or scalar coupling is introduced. All
controls are exposed model development, not observations or fits.

## 1. Statement and limits

Let R be an even integer comparable to lambda^-1, lambda tending to zero.
Let Eg be the actual microscopic ground energy and E2 the bottom of its
isolated two-vertical-wall cluster, continuously identified by the finite
local normal form below. Then

 E2-Eg = 4J-4Jlambda+O(Jlambda^(5/2)).                         (1)

A variational family realizing the upper bound has an altered column
background on an ell-square patch, ell comparable to lambda^-3/4, containing
Theta(ell²) physical spins at fixed height. This is a derived permissible
large dressing family, not a proof of an exact state's radius or shape.
For near-minimal two-wall states, a dressed particle-conditioned local
bad-plaquette weight F obeys F=O(lambda^(3/2)). This establishes backreaction
near the mobile defect; it does not identify its entire environment with
the vacuum background or construct a universal matter/scalar coupling.

## 2. Finite local reduction and basis embedding

Use the finite local native SW construction of
MICROSCOPIC_GROUND_WINDOW_PROOF.md and FEATURE_INTERACTION_PROOF.md, now at
fixed height four and order four. Its integer wall-energy denominators,
local N filtering and linked commutators give

 UHU†=J(B4+R4), B4=2N+sum_(j=1)^4 lambda^j Dj,
 [Dj,N]=0, ||R4||<=C Vlambda^5, V=4R².                       (2)

There is no all-order convergence assumption. Height-four winding terms
are local in the transverse plane and are retained, not discarded as they
would be in a growing-height proper-local construction. Fixed-order local
bounds are uniform in transverse R. The unitary preserves plane symmetries
and total physical Z parity.

An N=2 column has twelve physical configurations: eight are a singleton
at one of four layers relative to either majority column sign; four are
half-column intervals. Choose two representatives of the complementary
half-interval pairs, with the background sign accounting for complements.
Thus the entire cluster is position times six internal labels times the
aligned-column background Hilbert space. This is a basis identification,
not a factorization assumption on the actual state. Length-three intervals
are already counted as singleton states over their opposite majority sign.

Let Hb be the complete N=0 block of JB4, including its scalar. Its first
nonconstant coefficient is Jlambda^4 K/128, K=-4P-5E, with P the sum of
column plaquettes and E the sum of nearest column-X pairs; see
FOUR_LAYER_COLLECTIVE_PROOF.md. Terms below order four are scalar on N=0.

A fixed-order local term whose enlarged support avoids the occupied column
acts on its background exactly as in Hb. The difference from Hb therefore
has support meeting that column. The number of translated terms and of
outgoing position blocks is bounded independently of R; each is a bounded
operator on the background space. Hermiticity gives the same incoming bound.
The operator-valued Schur estimate gives a uniform norm for this defect
remainder, without multiplying by the background Hilbert-space dimension.
In the singleton block this yields

 Hs =4J+I tensor Hb+Jlambda T+Jlambda² D2+O(Jlambda³),         (3)

after subtracting the shared second-order scalar. In the half block the
first-order term vanishes and the second-order defect operator is bounded.
Exact Z parity prevents singleton/half mixing at every order. Plane parities
also track the singleton layer. The background in (3) can be entangled with
the particle and need not minimize Hb separately.

## 3. Arbitrary-background native second order

Write T=Tx+Ty. The x-hop amplitude is -1, the y-hop amplitude is -s_i s_j,
where s labels the majority background. Both directional operators have
norm at most two. Resolvent elimination of intermediate N not equal to two
uses denominator 4-2N_mid and gives exactly

 D2=-(Tx-Ty)²/8.                                           (4)

Here is the local sign-independent derivation, beyond the finite controls.
On the occupied layer an ordinary first hop stays in N=2 and is excluded
from the second-order resolvent. Reverse order for a two-step path creates
three singletons, with denominator -8. Axial distance-two paths therefore
give -1/8; mixed paths give the opposite product sign, +1/8 times the two
native link phases. These are precisely the off-diagonal entries of (4),
including interference between the two mixed paths in a nonflat background.
At the diagonal, the four excluded same-layer virtual bonds change the
vacuum subtraction by +1/2. The four incident bonds on each of the two
neighboring layers have denominator -4 instead of -8, contributing -1 in
total. The opposite layer has no difference. The result is -1/2, matching
(4). No other two-insertion path leaves one two-wall column: changing the
majority background while moving a singleton needs at least six spin flips.
This exhausts the local outputs with arbitrary background signs.

For the half-column block the diagonal difference is -2: all sixteen
incident bonds have denominator -4 rather than -8. Two insertions on the
occupied or complementary pair of layers of one transverse edge give eight
outputs, each -1/2. Four move the chosen half interval; four also reverse
the old background column and leave the complementary half at its neighbor.
The latter must not be lost by fixing the background. There are no other
N=2 outputs at this order. Thus its D2 is bounded below by -6 by the absolute
row sum. The whole truncated cluster is bounded below by
min(-4lambda,-6lambda²); the singleton wins for lambda<=2/3.

For the stronger singleton bound set A=Tx+2I, B=Ty+2I. Each is between zero
and 4I. Commutativity is unnecessary:

 (Tx-Ty)²=(A-B)² <=2A²+2B² <=8(A+B)=8(T+4I).

The first difference is (A+B)², positive. Therefore

 lambda T+lambda²D2 >= -4lambda I+lambda(1-lambda)(T+4I).    (5)

Flat backgrounds saturate -4lambda with their signed constant wave. The
negative D2 cannot create an order-lambda² loss in the band bottom. Adding
Hb>=Eb gives the uniform lower bound

 inf Hs-Eb >=4J-4Jlambda-CJlambda³.                         (6)

The half block lies higher by order Jlambda at sufficiently small lambda.

## 4. Extended patch upper bound

Start with any ground density matrix of Hb. Trace out a square patch plus
a fixed-width margin, and tensor its outside reduced density matrix with
an aligned logical-Z state inside. This is a legitimate mixed trial state.
Terms fully outside retain their expectation. Only O(ell²) fixed-range terms
change. All nonconstant background terms first enter at order lambda^4,
so the reset cost is at most CJlambda^4 ell². Scalar lower-order terms do
not contribute to this cost. No assumed continuum profile is used.

Put the singleton in the normalized product of Dirichlet sine waves on the
ell-square interior. Native links in the reset region have trivial flux;
choose their gauge so hopping is ordinary. Its T expectation is
-4cos(pi/(ell+1)). Extension by zero causes no extra hopping expectation.
D2 is negative semidefinite and can be omitted from an upper bound, even
though its action need not stay inside the trial support. Equation (3) then
implies

 inf Hs-Eb <=4J-4Jlambda+
   CJ[lambda/ell²+lambda^4 ell²+lambda³].                   (7)

Choosing ell comparable to lambda^-3/4 balances the two displayed costs
and gives O(Jlambda^(5/2)). It fits well inside R comparable to lambda^-1.
This proves an upper family, not minimizer-radius selection. The familiar
kinetic confinement versus environment-energy balance is not itself new;
White and Affleck's Nagaoka-polaron work (cond-mat/0011098,
doi:10.1103/PhysRevB.64.024411) is context only. No t-J Hamiltonian,
coefficients or empirical conclusions are imported.

## 5. Actual microscopic cluster separation

Along this box family the global remainder in (2) is O(Jlambda³), small
enough to preserve (6)-(7). The N=0 nonconstant bandwidth is
O(Jlambda^4 R²)=O(Jlambda²), so that entire block remains near its scalar.
One must not use the extensive first-order norm to separate other sectors.
Instead subtract the shared scalar at orders one through three from grouped
local linked-word coefficients. Order-two wall-free returns retrace one edge
and are sign independent; order three has no nontrivial wall-free return.
This is not an assertion about an arbitrary decomposition into local terms.
A number-preserving local term then vanishes on its wall-free neighborhood:
nontrivial height-four column winding first occurs at order four. Including
incident vertical bonds in its support makes this statement local. Bounded
local wall projectors and bounded overlaps give a form bound CJlambda N.
At order four conservatively retain the full norm CJlambda^4 V. Hence all
N>=4 sectors obey, relative to the common scalar,

 energy >=2JN-CJlambda N-CJlambda^4 V.

They stay near or above 8J, whereas the N=2 block stays near 4J and N=0 near
zero. Spectral perturbation by the global remainder shifts the separated
band bottoms by O(Jlambda³). This proves (1) for the actual Hamiltonian.
It does not imply a thermodynamic fixed-lambda isolated pole or a selected
individual eigenvector. Constants are finite-order asymptotic constants,
not a laboratory error tolerance.

## 6. Particle-conditioned flux backreaction

For singleton background-valued components psi_i, let Uij be the native
diagonal link signs, so the hopping entry is -Uij. Then

 <T+4>=sum_edges ||psi_i-Uij psi_j||².

Unitary transport around a plaquette p has product Pp. Telescoping at any
of its four roots gives

 ||(I-Pp)psi_i||² <=4 sum_edges_p ||gradient||².

Because Pp²=I, the bad-flux probability at that root is one quarter of the
left side. Summing the four roots, each edge belonging to two plaquettes,
proves the exact inequality

 F=sum_i,p incident i <psi_i|(I-Pp)/2|psi_i> <=8<T+4>.       (8)

For a state whose energy is at most the upper bound (7) plus O(Jlambda^(5/2)),
positivity of Hb-Eb and (5) imply <T+4>=O(lambda^(3/2)), hence
F=O(lambda^(3/2)). The O(Jlambda³) error gives only O(lambda²) after dividing
by Jlambda. The half-sector weight is at most O(lambda^(3/2)) because that
sector is separated from the singleton minimum by order Jlambda; alternatively
work in the exactly odd physical-Z sector where it is absent. Define F to
vanish on the half block before normalization. Mixed states follow by linearity.

For states restricted to the actual isolated microscopic two-wall spectral
cluster, first apply U and project into the separated N=2 block. Its leakage
is O(lambda³) by the order-one cluster separation. A low energy expectation
alone does not imply this leakage bound. Centering by the shared scalar,
the actual cluster has bounded spectral width; its approximate eigenvalue
equation controls projected energy without a factor from the global ||H||;
F has bounded norm (at most four), so this leakage is negligible. Equation
(8) concerns the resulting dressed observable/state. It is not an identity
for an undressed local microscopic measurement. Local flattening conditional
on particle position does not prove a flat region of deterministic radius.

## 7. What remains

This supplies an extended dressing construction, controlled heavy gap, and
local environment backreaction within one native Hamiltonian. It does not
supply an observed scalar, universal mass coupling, a cosmological state,
fermionic statistics, emergent Lorentz invariance, or three-dimensional
motion. Fixed longitudinal plane charge still restricts the singleton's
motion. The relaxed background differs from the prepared-vacuum probe of
NATIVE_PROBE_LOOP_PROOF.md; its dynamical response remains to be derived.
