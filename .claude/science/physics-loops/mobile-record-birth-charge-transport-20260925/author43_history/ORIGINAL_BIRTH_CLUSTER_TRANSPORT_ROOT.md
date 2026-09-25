# Full dynamics of the smallest original birth charge grouping

Personal root derivation, 25 September 2026. Conditional mathematics in the
supplied common matter/rotor model. This author packet is not independently
checked at its creation and is not an audit disposition or an observed particle
prediction. The exact result below concerns one specified preparation and a
bounded charge projector. It does not exclude larger or approximately stable
charged objects.

The original formation map produces an exactly unit-negative charge grouping
at birth. This note tests whether the union of all such nearest-neighbor
groupings is preserved by the full subsequent law. It is not: an explicit
actual birth output has positive quadratic probability of leaving that union.
The original formation channels remain active in this calculation.

## 1. Premises, provenance, and the diagnostic

Use an even periodic cubic graph with equal side L >= 4, A the even sublattice,
B the odd sublattice, and n=|A|. Each simple edge is oriented A to B. Matter is
the parent's unsigned tensor hard-core matter, not a fermionic replacement.
All integer electric configurations satisfying

    div E = q - 1_A

are retained. On P, every A site is occupied. Write the full common generator as

    h = K D + delta H4,
    H4 = -2 sum_{unordered overlapping {x,y}} S_xy^* S_xy,
    S_xy = F_y F_x P,
    D = sum_{x->z, q_z=0} E_xz (E_xz - q_x).

Here K >= 0, delta > 0, kappa >= 0, and the original resolved jumps are
L_xz,sigma=sqrt(kappa) P j_xz,sigma F_x P. Alternatively, use the stipulated
unnormalized coherent sign sum at each separate edge. In both cases

    Gamma = sum L^* L = 2 kappa sum_x P F_x^* G_x F_x P,

where G_x counts empty B neighbors after F_x. In the coherent alternative,
j_+^* j_-=j_-^* j_+=0, so this is the same loss operator. No vacancy gate,
electric sector, color degree of freedom, or later original jump is removed.
The factor -2 belongs to the unordered-pair convention used here.

The total occupied-site number N commutes with h and Gamma. Every original
jump increases N by two. In the sector N=n+2 with total charge n, exactly two B
sites are occupied and exactly one occupied site carries the minus label.
Let Pi_2 denote this sector. Define P_nn as the diagonal orthogonal projector
onto the following union of charge words, with all compatible electric fields:

* The minus label is at B; both A charges and the other occupied B charge are
  plus. Include the word.
* The minus label is at an A site d. Include the word if at least one of the
  two occupied positive B sites is adjacent to d.

The second case pairs the A defect -2 relative to the intrinsic background
with an adjacent +1, making a unit-negative charge sum. The other +1 remains.
The projector allows every choice of which positive B charge is paired with d;
it is not tied to the original mark edge. Let C=Pi_2-P_nn. This is a test of
the smallest birth grouping, not a new primitive or a definition of all matter.

The original birth formula, personally derived in candidate42, is

    Delta q_a = sigma-1, q_b=-sigma, q_c=+1,
    Delta E = sigma e_ab - e_ac,       c in N(a) except b.

Every such first-birth output belongs to P_nn. The root sealed candidate42
before reading the independent charge-force PRE. The latter was then read and
its explicit H4 path showing that one selected charge word is not invariant
helped motivate the stronger question in this note. That conceptual input is
credited; this is not a claim of fresh blindness to the PRE. The present
question concerns the union P_nn, normalized actual birth states, and the full
Lindblad evolution. The computation reuses the root's own candidate42 geometry
helper byte for byte, with this reuse declared.

## 2. A specified normal actual-birth preparation

Supply the immediately pre-mark vector |Omega,0>, with every A plus, every B
empty, and all electric fields zero. It satisfies Gauss law and is normal.
Fix a=0 and the marked edge b=-e_x. Define

    psi_- = B_ab,- |Omega,0> / sqrt(5),
    psi_+ = B_ab,+ |Omega,0> / sqrt(5),
    psi_coh = (B_ab,+ + B_ab,-) |Omega,0> / sqrt(10).

The denominators follow from the five distinct outgoing matter words for each
sign and orthogonality of the signs. Each primitive electric translation has
unit coefficient. For resolved formation the physical post-mark alternatives
are psi_- and psi_+. The coherent model has psi_coh. An equal mixture of the
resolved states is a third state, distinct from psi_coh.

This is an actual output of the original Kraus map on a supplied input. It is
not claimed to be the typical field state at a random first event after
starting the autonomous dynamics at |Omega,0>. The pre-event Hamiltonian can
change that field. No field-state selection or preparation mechanism is proved
here. In particular, this result must not be conflated with candidate42's
field-independent static charge probabilities at an actual first event.

## 3. A complete Gauss-law target outside the union

Use short coordinate lifts, reduced modulo L:

    a=0, b=-e_x, c=-e_y, d=e_x+e_y, u=e_x, v=e_y.

Take the c branch of psi_-. It has q_a=-1, q_b=q_c=+1, the other A charges
plus, and E=-e_ab-e_ac. The two stars a,d have exactly the two common neighbors
u,v. These are empty. One primitive term in S_ad^* S_ad performs

| Move | Matter transported | Electric increment |
|---|---|---|
| a to u | minus | +e_au |
| d to v | plus | -e_dv |
| u to d | minus | -e_du |
| v to a | plus | +e_av |

Each move changes divergence by exactly its change in q, and each destination
is empty. The final vector chi is the complete orthonormal basis vector with
minus at d, plus at b,c, every other A plus, and

    E_chi = -e_ab-e_ac+e_au+e_av-e_du-e_dv.

Both positive B sites are at graph distance three from d for every even L>=4.
Thus chi lies in C, even after allowing reassignment of the positive charge
that dresses the A defect. Interchanging u and v in the two outward moves and
the two return choices gives a second primitive path with exactly the same
final matter AND electric word. The two electric additions commute. This
geometry does not apply to the cube L=2, where u=b is already occupied.

## 4. Exact full-Hamiltonian and loss matrix elements

The complete coefficient is computable, not just bounded by one visible path.
For any branch of psi_-, the source and target A charges differ at exactly a,d.
Only the unordered star pair {a,d} can contribute. The minus must move from a
to a common neighbor and return to d. The other outward plus must use the
other common neighbor and return to a, leaving the occupied B set unchanged.
Neither b nor c is adjacent to d. Returning an old B record would leave an
unwanted common neighbor occupied or could not restore the required b,c set.
Consequently the source branch must be the chosen c branch and the two paths
above are the only ones. Each carries coefficient -2 in H4.

In every branch of psi_+, the unique minus starts at b. To finish at d in one
S_xy^* S_xy it would have to return directly along a b-d edge. That edge does
not exist. This excludes all star pairs, including those containing d and an
A site other than a. Therefore

    <chi,H4 psi_->   = -4/sqrt(5),
    <chi,H4 psi_+>   = 0,
    <chi,H4 psi_coh> = -4/sqrt(10).

This argument uses the complete final electric word; no zero-angle or
field-only substitution is made. Unsigned primitive coefficients also give
a useful check against a spurious destructive cancellation in this preparation.
No corresponding sign assertion is made for arbitrary complex field inputs.

D is diagonal and chi is orthogonal to all the source words, so
<chi,D psi>=0 for each of the three states. A term F_x^* G_x F_x changes the A
charge at at most x. Thus it cannot connect a minus-source branch, requiring
changes at both a and d, to chi. For a plus-source branch it would have to move
the minus from b to d, again requiring the absent b-d edge. Hence

    <chi,Gamma psi_-> = <chi,Gamma psi_+>
                      = <chi,Gamma psi_coh> = 0.

These are exact statements for either specified original instrument and every
kappa>=0, not a weak-loss approximation.

## 5. Full Lindblad small-time probability and a controlled remainder

Let rho(t) be the full unconditional evolution with one of these pure initial
states. Set G=-i h-Gamma/2 and V(t)=exp(tG). Because h and Gamma preserve N,
while every original recycling term raises it, the entire Pi_2 block is

    Pi_2 rho(t) Pi_2 = V(t)|psi><psi|V(t)^*.

Once any original formation event occurs, it cannot feed this block again.
Consequently its contribution to the full, unconditioned target probability is
exactly

    p_chi(t) = <chi,rho(t)chi> = |<chi,V(t)psi>|^2.

This identity includes the original loss and accounts for recycling by sector
orthogonality. It does not assume that formation was turned off or that a
normalized no-event trajectory describes the whole state.

On a finite graph H4 and Gamma are bounded finite sums of finite electric
translations. D is diagonal. The supplied self-adjoint realization of h plus
the bounded nonnegative loss gives a contraction semigroup V. Each psi has
finite support in the complete q,E basis. Applying h or Gamma preserves finite
support, so psi belongs to D(G^2). In particular M_psi=||G^2 psi|| is finite.
The semigroup integral remainder gives, for t>=0,

    ||V(t)psi-psi-tGpsi|| <= (t^2/2) M_psi.

Let A_psi=|<chi,Gpsi>|. The proven matrix elements give

    A_- = 4 delta/sqrt(5),       A_coh = 4 delta/sqrt(10).

For these two preparations,

    p_chi(t) >= max(0, A_psi t - M_psi t^2/2)^2,
    |p_chi(t)-A_psi^2 t^2| <= A_psi M_psi t^3 + M_psi^2 t^4/4.

It follows that

    p_chi^-(t)   = (16/5) delta^2 t^2 + O(t^3),
    p_chi^coh(t) =  (8/5) delta^2 t^2 + O(t^3).

For psi_+ the same estimate has A_+=0, so p_chi^+(t)=O(t^4).
The equal resolved-sign mixture has coefficient (8/5)delta^2 by linearity;
this equality of one leading probability does not equate the quantum states.
Since Tr(C rho(t))>=p_chi(t), P_nn is not invariant under the full original
generator when delta>0. This is also an explicit failure of exact closure for
this smallest grouping applied to the specified actual birth preparations.

M_psi has not been numerically evaluated or bounded uniformly in volume or the
parameters. The assertion is a fixed-graph, fixed-parameter small-time result
with the displayed finite remainder quantity. It is not a lifetime estimate at
t of order delta^-1, a typical escape probability, or a uniform scaling limit.
The supplied relations K=g^2/(2 tau), delta=1/(4 tau g^2), tau=a/c do not supply
a physical calibration or a measured decay rate.

## 6. Deterministic controls and read coverage

cluster_escape_controls.py reconstructs the original primitive birth words
and four-hop Gram terms on L=4 and L=6, retaining full integer fields. The
helper birth_geometry.py is the exact personally authored candidate42 helper,
SHA256 4b1b273bb5046fab5e4f6dc307c650d9be9cba8df25b584020fcaadaa0d5ce6e.
It is declared reuse, not an independent implementation. The control excludes
irrelevant star pairs only by the necessary changed-A-charge condition, then
enumerates every legal outward and return choice of each remaining pair.

The saved result contains all 80 relevant L=4 rows, all 95 relevant L=6 rows,
and all four matched primitive paths across the two graphs. Every full matched
intermediate state satisfies Gauss law. The exact unnormalized H4 numerators
are -4 for the minus sign and zero for the plus sign; the loss numerators are
zero for both. Both target distances are three. The root read every relevant
row and all matched paths in a lossless sparse rendering after the full source
review. These finite controls support the analytic all-L proof; two graph
sizes alone would not establish it.

Attempt01 succeeded with exit0 and empty stderr. External elapsed time was
0.1268903750460595 seconds and internal elapsed time 0.081492875 seconds.
The scratch WORKING_DERIVATION.md retains the earlier one-path lower bounds
4/5 and 2/5 in units of delta^2. Those are valid weaker bounds, superseded by
the exact two-path coefficients 16/5 and 8/5 proved here. No failed scientific
run is hidden. No finite-time propagation or experimental fit was performed.

## 7. Narrow negative-claim stress test

N1, alternatives: Larger dressings, radius-three or larger charge groupings,
moving collective packets, different complex field preparations, different
parameter regimes, and controlled approximate projections remain available.
Even a packet defined by a local charge sum need not remain in P_nn.

N2, independent restrictions: Radius one defines the tested projector; the
supplied input fixes the demonstrated matrix element; and the original law
fixes its motion. Failing this projector's exact invariance does not select a
preparation or show that every alternative shares that failure.

N3, hidden restrictions: Full integer Gauss fields, both original signs and
the unnormalized coherent alternative are retained. No fermionic signs,
field-only postbirth limit, selected flat connection, or tiny-volume
extrapolation is inserted. The graph hypothesis L>=4 is explicit.

N4, residual matching: The target is the complete same-N q,E basis vector
outside the union after allowing charge reassignment. Its exact full-generator
matrix element is evaluated on normalized actual Kraus outputs. The measured
mathematical quantity is this target probability, not global formation count,
energy loss, photon absorption, or a normalized survival fraction.

N5, rhetoric: The conclusion is failure of exact P_nn invariance for this
supplied law and preparation. It is not absence of particles, exclusion of the
framework, an observed instability, or TOE closure.

N6, partial closure: An approximate low-energy description or a larger dressed
packet could still be stable on useful times. It would require an explicit
preparation, transport/readout definition, and quantitative error estimate.

N7, strongest alternative: Observed particles need not be instantaneous
radius-one charge clusters. A dynamical collective state can dress and move.
This result leaves that route open and identifies the exact assumption that
cannot simply be taken from the birth charge label.

N8, relation to prior work: Candidate40's uniform-minus comparison was not an
actual birth state; candidate41's fixed-word noninvariance did not cover the
whole union P_nn. This note strengthens the relevant dynamical test but credits
the latter motivation. Candidate42's static charge identities remain intact;
they never asserted subsequent persistence. None of these results supplies a
physical detector, charge unit, mass, or force law.

Next observation obligation: identify a prepared or selected full-state packet
and test its charged current, spatial transport and interaction on a controlled
time scale, with a route to physical units and readout. A birth charge sum
alone cannot fulfill that obligation.
