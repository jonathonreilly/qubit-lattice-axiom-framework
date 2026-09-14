# Causal cubic wires and a permanent likelihood protocol

Personal proof and author checks, 2026-09-14. This is a supplied downstream
program. No independently retained claim, native action/law selection,
physical quantum state, or axiom amendment is asserted.

## Input and output of the geometric construction

Supply finitely many gate types h=0,...,H-1, each with one complex payload,
and directed edge types e from (n,h_left) to (n+delta_e,h_right), n in Z^3.
Let ||delta_e||_infinity<=R. The total incident degree at every gate type
is at most four. Supply integer stages s_h such that s_left<s_right for
every edge. This is stronger than merely acyclic behavior on one finite
cover: the same type-level DAG works on every cover.

The construction produces periodic, vertex-disjoint nearest-neighbor wires,
meeting only at their true gate endpoints. Each internal vertex stores a
single complex copy. The number of sites and the maximum wire length per
coarse cell are finite constants fixed by the input graph, independent of
the number of coarse cells. This is an existence/resource bound, not an
efficient architecture. All initial program conditions remain supplied.

## A periodic immersion with only isolated transverse crossings

Here are the coordinates, stated again so the mathematical argument does not
depend on the prior static Gaussian compiler's provisional theorem.
Set P=2R+2, C=P^3, q=ceil(sqrt(CH)), z0=8 and

    M=max(20q+20, z0+16+E C)+16.

For coarse n, let cid(n)=((n_x mod P)P+(n_y mod P))P+(n_z mod P),
j=H cid(n)+h, and put the gate at

    home(n,h)=Mn+(10+20(j mod q), 10+20 floor(j/q), z0).

Assign incident half-edges distinct directions from +x,-x,+y,-y. From a
home, its arm goes one step in that direction, one step in -z, then three
further steps in its horizontal direction. This ends at a port column
home+4 direction-e_z. Distinct arms meet only at the home. Home neighborhoods
are separated by at least twenty before scaling, including coarse seams;
port column coordinates are consequently distinct modulo M.

For e starting at n and ending at n+delta_e, join the two port columns at

    plane=max(n_z,(n+delta_e)_z)M+z0+8+e C+cid(n).

The path ascends the left column, goes in x then y on this plane, descends
the right column and reverses the right terminal arm. The plane is above
BOTH endpoints. The original path length L is bounded by

    L <= (3R+4)M+16.

Horizontal planes never equal a terminal arm/home level: their residues
modulo M lie in [z0+8,z0+8+EC-1], while terminal levels have residues z0-1
or z0. Equal main planes identify edge type, source color and maximum
endpoint coarse height. For fixed edge type and source color this fixes
source n_z. Distinct such occurrences are separated by PM horizontally;
their horizontal boxes have span less than (R+1)M<PM, so they do not meet.

Port column XY residues identify their home color, gate type and port. Two
occurrences using the same column XY are separated vertically by PM; each
vertical interval has length less than (R+1)M, so they do not meet. Finite
terminal arms in separated home neighborhoods have no foreign intersection.
No path crosses a foreign home or its terminal first step.

Thus every remaining foreign crossing consists of one straight vertical
column interior and one horizontal straight segment or x/y corner. There
are no overlapping horizontal intervals or overlapping vertical intervals,
no foreign endpoint crossings, and no three-strand crossings. Quotient
covers with each coarse side a multiple of P inherit this classification:
the span bounds exclude self-aliasing, and crossings across seams are the
images of the same infinite periodic construction.

## Scale-ten detours remove all foreign intersections

Scale the entire immersion by ten. At each foreign crossing center c leave
the horizontal wire unchanged. Suppose its vertical wire is traversed in
direction d e_z, d=+1 or -1. Replace the vertical interval from c-2d e_z
to c+2d e_z with

    c-2d e_z,
    c-2d e_z+e_x,
    c-2d e_z+e_x+e_y,
    c+2d e_z+e_x+e_y,
    c+2d e_z+e_x,
    c+2d e_z.

Each displayed axis segment is filled with unit copy sites. At the crossing
height, the vertical detour lies at horizontal offset (1,1); the other wire
lies on the x/y axes through c, even at a corner. The detour's horizontal
steps occur at heights c_z+-2, where there is no original horizontal wire.
All original columns and plane heights are on the ten-grid. Detour boxes
at different crossings are therefore disjoint: distinct columns differ by
at least ten in a horizontal coordinate, or crossings on one column differ
by at least ten vertically. No detour meets an original unrelated wire.

The crossing is strictly interior to its vertical column. The distance to
its endpoints is at least ten, so the four-unit replacement is available.
Each detour increases length by exactly four. A path with original length
L has at most L-1 foreign crossings, hence final length

    L' = 10L+4(number of its detours) <= 14L.

The result is a graph subdivision with distinct physical vertices on
distinct wires, except for true shared gates. Every home has the unused
neighbor home-e_z in the scaled geometry, available as an initial control.
It lies on no wire. The formula and crossing classification are periodic;
therefore the complete finite role map repeats with physical period 10MP.

The private runner first checks all original unit vertices, then uses a
different inclusive-integer-segment intersection calculation for the final
geometry. It rejects positive interval overlaps, foreign intersections and
control collisions, and checks each wire for repeated vertices. The doubled
cover additionally compares the complete compressed route coordinates
relative to their coarse origins against the smaller cover's role roster.
These finite challenges support the proof; their counts are not the proof.

## Causality is preserved at physical sites

Let Lmax bound every final wire length. Give a gate the integer level
s_h Lmax. On an edge beginning at stage s_left, give its j-th internal
copy the level s_left Lmax+j. Its first copy is later than its source and
its last copy is earlier than its destination, since s_right>=s_left+1
and j<L'<=Lmax. Distinct wires share no internal site, so there is no new
physical dependency from a crossing. The physical dependency graph is a
DAG on every cover, with depth at most (max s-min s)Lmax.

Attach an independent innovation to each stochastic root/observation gate;
copy/scale/sum gates are deterministic. For any fixed coherent program,
the acyclic recursion determines all written values as functions of these
innovations. Every fair causal schedule yields this same final law, even
if it chooses among currently enabled gates based on already written data.
No future innovation may be read, and fairness/completion remains assumed.
No write updates an existing record. A nearest-neighbor rule reads only
the declared parent records and may ignore other present neighbors.

For the infinite periodic type DAG, every finite set has a finite ancestor
set. Independent innovations therefore also define the infinite forward law
directly; sufficiently large covers agree on an unwrapped ancestor set.
At fixed graph depth it has finite dependence range, because disjoint
innovation ancestor sets give independent outputs. A long-range Gaussian
posterior obtained after conditioning is a different law; no uniform
postselection/infinite-volume interchange is asserted.

## A single covariant rule and readable matrix carriers

For each finite role r and proper-cubic frame R use

    M=z I+(8r+1)(R(1,2,3)).sigma.

Trace decodes the one complex value. The traceless vector has norm
(8r+1)sqrt(14), which decodes r; the free orbit decodes R. These are
disjoint closed affine complex planes in M2(C). Proper rotations act by
ordinary Pauli conjugation; coordinates and the supplied frame co-rotate.
The codec chooses a downstream instruction representation, not a privileged
physical spinor or selected action.

A role contains its outgoing direction/next-role table, required incoming
roles, and its finite gate instruction. In a valid program neighborhood,
the parent tags identify one target role and frame; the rule requires all
its parents and evaluates that instruction. Gaussian gates push the specified
one-complex Gaussian into its role plane; deterministic gates use a point
mass there. Other neighbors are irrelevant data. On conflicting/unrecognized
neighborhoods the rule can use a fixed proper-rotation-invariant default
distribution. This defines one answer on every neighborhood; along the
supplied causal program only the stated instruction cases are exercised.
Translations and proper rotations commute with the decoder and these tables.

Initial controls, coefficients, Gaussian parameters and a causal formation
schedule are presently supplied. A finite auxiliary bootstrap can make the
initial controls themselves supported formation outcomes: at an empty
neighborhood let the default law draw uniformly from the finite control
roles and all 24 frames, with complex payload zero. Control sites are
pairwise nonadjacent, so they may form first with independent draws. Any
specified coherent finite control pattern has positive probability, a
product of the corresponding atom probabilities. Conditioning on that
pattern gives the protocol used above. This adds a disclosed rare-program
conditioning cost; it does not select a typical program, initial state or
formation schedule from the axioms. No infinite coherent-program event is
assigned a nonzero probability by this finite observation.

## Application to the supplied DK likelihood circuit

The actual finite linear map L has a common union roster of 208 coefficient
positions across all four arms and both c choices. Keep a scale gate even
when its coefficient is zero. Binary fanout and sum trees then give the same
768-node, 848-edge, degree-three, depth-nine circuit in every case. The
runner checks the topology digest independently of the coefficient digest
and reproduces every row of L exactly.

Any finite circuit is a special case of the geometric input: make each gate
a separate type, let all displacements be zero and replicate the whole
circuit on coarse cells. Its type stages give the required DAG. The universal
coordinate proof therefore applies, with finite constants depending on this
supplied circuit. The full DK physical coordinate roster has not yet been
instantiated by the finite geometry runner; its tested graphs are smaller
three-axis DAGs. This distinction must stay explicit unless that additional
certificate is built.

Combining this construction with BLOCK5_DK_POSTERIOR_DERIVATION.md gives a
conditional local permanent likelihood protocol for the supplied source,
with a proper-prior perturbation and explicit positive-window accuracy and
acceptance costs. It does not reproduce the earlier native Record-star
experiment or derive its local formation weights, and it does not turn the
source determinant into an unconditioned physical Born law.
