# Classical permanent records with quantum gauge memory

Date: 2026-09-22. Status: personal provisional construction and proofs;
independent check pending. This is an explicitly enlarged model, not a native
derivation from the framework axioms and not a photon or TOE identification.

## 1. Question and supplied model

The earlier coherent charge-conjugation examples mix different record-charge
configurations. They do not by themselves exhibit definite record contents
coexisting with readable quantum gauge information. Here record contents are
classical throughout and gauge information occupies an explicitly supplied
quantum fiber. This change is a separate model, not an interpretation adopted
for the axiom memo.

Let G=(V,E) be a finite connected oriented graph. A record configuration c
assigns either vacancy or a permanent charge q=+1 or -1 to each vertex; a
later variant also assigns a permanent readout bit b=+1 or -1. A record moves
only by swapping with a neighboring vacancy, and its entire content moves
with it. Formation creates a charge-neutral pair at two vacant endpoints.
Thus existing contents are never changed and at most one record occupies a
vertex. Occupation increases by two at a birth and is unchanged by a hop.

Supply a Z_m electric link, m>=3, with basis e_l in Z_m, unitary shift
U_l|e_l>=|e_l+1>, and incidence matrix D with +1 at an edge's tail and -1 at
its head. Define

    K_c = span{|e>: D e = Q(c) mod m}.

For net charge zero mod m, dim K_c=m^(|E|-|V|+1): fixing a spanning tree
solves its |V|-1 edge variables uniquely from the other edge variables and
the vertex equations. No charged constraint is imposed on the readout bit.
The actual histories considered start at integer net charge zero and keep
it zero, a subset of the possible modular sectors.

The state space here is the direct sum of matrix algebras on these fibers:

    rho = direct_sum_c rho_c,       rho_c>=0, sum_c Tr rho_c=1.

This declares c to be classical; no off-diagonal coherence between different
record configurations is assumed. The gauge fiber, orthogonal record
register, clock, generator, and maps below are supplied additional structure.
In particular the finite content alphabet is not an asserted realization of
the complete one-site M_2(C) possibility domain. Readability of vacancy is not
used as an observable; occupation variables specify the dynamics.

## 2. Whole-fiber unitary transport and a closed classical clock

If a charge q moves from the tail x to the head y of l, Q changes by -q D_l,
so U_l^(-q) maps K_c unitarily onto K_d. Reversing the spatial hop reverses
the exponent. Formation of q at x and -q at y uses U_l^q and also maps the
whole source fiber unitarily to the target fiber. Denote these maps U_dc.

Give each marked allowed transition c->d a rate r_dc independent of the
quantum field state, and each fiber a Hermitian H_c. Repeated edges or
transition labels can be summed; they need not be identified. The equation

    dot rho_d = -i[H_d,rho_d]
                + sum_c r_dc U_dc rho_c U_dc^dagger
                - r_out(d) rho_d                                      (1)

is a completely positive trace-preserving finite-dimensional semigroup on
the direct-sum algebra: embed its jumps as sqrt(r_dc)|d><c| tensor U_dc.
Taking traces proves the exact Markov equation

    dot p_d = sum_c r_dc p_c - r_out(d) p_d.                            (2)

In particular, choose hop rates k_l>0 in each spatial direction, independent
of q and b, and total birth rate beta_l>0 per vacant edge, with orientation
charges chosen equally. The occupation marginal is exactly the exclusion
walk with neutral pair insertion, independently of every H_c and every
initial conditional gauge density. This is strong lumpability by occupation:
the total rate from a source configuration to each destination occupation
pattern depends only on its source occupation pattern.

On a connected graph with an even number of vacancies, every nonfull
occupation sector has a finite sequence of allowed swaps leading to an
adjacent vacancy pair. To see this, choose two vacancies at minimal graph
distance; the internal vertices of a shortest path are occupied. Successive
swaps move one vacancy toward the other. A birth then reduces the vacancy
number by two. Every step has positive rate. A finite Markov chain therefore
has no closed communicating class outside full occupation. Full occupation
is reached with probability one, with an exponentially bounded tail and
finite mean for each fixed graph and fixed positive rates. This is not a
volume-uniform bound and does not address odd vacancy number.

## 3. What retained trajectories do and do not protect

Fix an initial record configuration. For a complete marked jump trajectory h
(including jump times and destinations), the unnormalized conditional field
map of (1) is p(h) V_h rho V_h^dagger, where V_h is the ordered product of
the inter-event field unitaries and U_dc. Its scalar path density p(h) is the
classical Markov path density, independent of rho, including when rho is
entangled with an inert reference. The no-jump factors are scalar exponential
survival factors times exp(-i H_c t).

Consequently, if this entire classical trajectory is separately retained and
available, applying V_h^dagger recovers the original field state exactly.
This is an instance of environment-assisted correction of random-unitary
channels, not a new correction principle. The complete trajectory and its
event times are **additional data**: permanent record contents at the final
time need not contain them. No recovery from final contents alone is claimed.
The same factorization also means that these scalar-rate trajectory data
alone reveal no information about the initial field conditional on the fixed
initial record configuration. Readable field dependence requires an actual
instrument, such as the one below.

## 4. Field-sensitive permanent contents with the same occupation law

Let z be an oriented integer cycle, Dz=0, and supply the unitary Wilson shift

    W=product_l U_l^(z_l).

It preserves every Gauss fiber. All U_l commute, so its restrictions obey
W_d U_dc=U_dc W_c. To avoid selecting an orientation for Re W, set

    K_(b,eta) = (I+b W^eta)/(2 sqrt(2)),    b,eta in {+1,-1}.            (3)

The orientation eta is not retained. Direct multiplication gives

    sum_(b,eta) K_(b,eta)^dagger K_(b,eta)=I,
    E_b=sum_eta K_(b,eta)^dagger K_(b,eta)
       = (I+b Re W)/2,     Re W=(W+W^dagger)/2.                        (4)

Replacing W by W^dagger merely permutes eta and leaves the coarse b
instrument unchanged, not only its probabilities. A birth on l now creates
records (q,b) at x and (-q,b) at y, with jumps on its vacant source block

    J_(q,b,eta) = sqrt(beta_l/2) U_l^q K_(b,eta),                      (5)

where q=+1,-1 and the target block includes both new, matching permanent b
contents. The two orientation charges and two readout bits are distinct
record contents. The eta alternatives are coarse-grained. Equations (4)-(5)
give total loss beta_l I per vacant edge. Thus the occupation process and
the completion conclusion of Section 2 hold **unchanged**, even though the
new b contents depend on the conditional gauge state:

    Pr(b | this birth, current field rho)=(1+b Re Tr(W rho))/2.         (6)

The charge orientation q is uniform. Existing contents are never overwritten;
new b values are readable from new records and remain attached when they
move. The input rho in (6) is the normalized conditional density immediately
before that event. Future b outcomes can be correlated through the evolving
field. No independent-draw claim is made.

The field-only channel for a birth after its known unitary transport is

    M(rho)=rho/2+(W rho W^dagger+W^dagger rho W)/4.                     (7)

It preserves every observable commuting with W, in particular every function
of W. The conditioned K's also commute with W: this measures Re W without
changing its spectral values. It does not preserve an arbitrary quantum
state or imply error-free binary outcomes for a general W eigenvalue.
If H_c also commutes with W_c, these Wilson spectral values are unchanged
between events. Electric energy H_c need not satisfy that extra premise.
For W=W^dagger, the coarse instrument reduces to the two projectors
(I+bW)/2; repeated outcomes then agree provided the intervening dynamics
preserves W. For m>=3 the ordinary loop shift is generally not Hermitian.

## 5. Boundaries and relation to prior work

The instrument in (3) is the usual controlled-unitary/Hadamard-test algebra.
Ancilla Wilson-loop readout is established technology; this note's bounded
contribution is its placement in permanent pair formation with exact
Gauss preservation and an unchanged exclusion/formation clock. This is not
a claim to discover quantum gauge measurement or trajectory correction.

The following dependencies remain explicit: the chosen graph and links,
finite cyclic gauge carrier, orthogonal classical record algebra, additional
permanent b contents, supplied rates/Hamiltonians, Born instrument law,
multi-link measurement support, and resources for irreversible fresh record
creation. A cycle instrument supported away from the birth pair is not a
nearest-neighbor microscopic implementation. Local ancilla transport could
be investigated separately; no such compiler is supplied here. Neither the
modular model nor a formal rotor replacement proves a physical Coulomb
phase, emergent Lorentz invariance, Maxwell dynamics, or a native axiom bridge.

Sources checked for context: Gregoratti and Werner, quant-ph/0403092v1,
abstract/introduction and Propositions 1-2 (random-unitary trajectory
correction); Brennen et al., arXiv:1512.06565v2, Supplement III.A
(controlled Wilson-loop readout). The finite identities above are derived
directly and do not import an unchecked theorem from those sources.
