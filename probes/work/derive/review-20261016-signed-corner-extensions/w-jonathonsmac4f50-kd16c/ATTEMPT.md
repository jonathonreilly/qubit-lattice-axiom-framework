# J:derive:review-20261016-signed-corner-extensions:a1 -- attempt (same-family, unrefereed)

Worker: Claude Sonnet 5.5. Not adopted science, not an audit verdict, no PR. Nothing here infers generations.

## Plain-language summary

The source notes rotate a 2x2x2 block of sites about its centre and let each corner pick up a sign. They found
several sign patterns and said one of them is "the spinorial class" (a binary octahedral lift, 2O).
I enumerated all 65536 sign choices exactly and classified them. Result: the sign patterns realise
each of the four possible central extensions of the cube rotation group by {+1,-1} exactly once
(up to flipping signs of corners). Two are spinorial: 2O (the prescribed one) and GL(2,3), which the
runner's trace key does not separate from 2O (the B7 check does name it). I give exact matrices and the exact induced character for the GL(2,3)
class. The two spinorial classes are not equivalent as groups of matrices, but they become equivalent
if odd rotations (quarter turns, edge half-turns) may be multiplied by +-i and the corners rephased.
Covariance statements of the form W(Rk) = D W D^dagger do not see that phase, so the sources' moving
walk carries over to the GL(2,3) class unchanged. The count of eleven nearest-site covariant
coefficients is the same in all four classes. The sources' own class counts (three, four, five) are consistent
with one another once the level of identification is named; I list them.

## Read first (stated)

- Read in full: `docs/MINIMAL_AXIOMS_2026-06-29.md` (233 lines, current main) and
  `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` (130 lines). Approved primitives
  (scale reference, kinetic isotropy, realized state) are not used. No premise below comes from the axioms
  beyond Lattice (Z^3, proper cubic rotations) and the single-amplitude reading of Qubit.
- Source branch `claude/toe-campaign-24h-20261015`, frozen commit
  `b0178fa585cad5ac9e02e70dff2175593dbc5dab`: commit present, all six listed objects match their
  sha256 (`RECOVERY_STATUS.json`). I read all six in full (README, blockrep.py, both notes, both runners).
  I also read the independent check `.claude/science/physics-loops/toe-campaign-20261015/independent_check_B7/`
  (README, common.py, part1_classify.py, part1_decompose.py, classes.json) on current main, and the
  main-landed Majorana note
  `docs/MAJORANA_PER_DIRECTION_CUBIC_FERMION_CODE_HAS_ONE_SPECIES_COVARIANT_UNDER_ALL_CUBIC_ROTATIONS_BOUNDED_THEOREM_NOTE_2026-10-17.md:4`
  and `.claude/science/physics-loops/toe-campaign-20261017/c8_rotation_action/independent_check/grouptheory/REPORT.txt`.
- Open-PR search (`gh pr list`, "signed corner", "GL(2,3)"): none open. PR 9658 is closed unmerged.
  The task catalog (`probes/work/review-science-20261016/PR9658_FOLLOWUP.md`) routes "signed conventions" here
  and the nearest-site prime closure to a separate task; I do not touch the latter.

## Setting and premises

- A1 (ASSUMED, supplied): one complex amplitude per site (single-amplitude reading of the Qubit axiom).
- A2 (ASSUMED, supplied, not an axiom): sites are grouped in 2x2x2 blocks; each proper cubic rotation R acts
  about the block centre by permuting the 8 corners. Nothing in the four axioms selects a block origin
  (the Lattice axiom speaks of rotations about each site). Source: staggered note, Premises.
- A3 (ASSUMED, supplied): the action is monomial with entries +-1: D(R) = diag(s) P(R) (sign on target, as in
  `blockrep.py`) or P(R) diag(s) (sign on source, as in B7 `common.py`).
- A4 (ASSUMED, my scoping of "action"): the operators for the 24 rotations generate a group G whose diagonal
  kernel K = G cap {diagonal sign matrices} is contained in {+I,-I}, so that G is a (central) extension of O
  by K, i.e. a projective representation of O. (If K contains a non-scalar diagonal sign d, then d implements
  "no rotation" and covariance at R = id forces [W,d] = 0: the walk splits into d-sectors. I do not classify
  those; see "Not shown".)
- Notation. O = cube rotation group ~ S4. P(R) = corner permutation. V = {+-1}^8 (diagonal signs).
  Invariants of a group G of signed permutation matrices that contains -I: a(G) = 1 iff lifts of axis
  half-turns square to -I; e(G) = 1 iff lifts of edge half-turns square to -I; kappa(G) = the commutator of
  lifts of two perpendicular axis half-turns, +-I.
- Three notions of "gauge": G1 = conjugation by diagonal sign matrices; G3 = conjugation by diagonal
  U(1) matrices together with a scalar factor lambda(R) on each D(R) (what covariance D W D^dagger cannot see).

## What the sources say / supply / proved

- Source claims (staggered note claim_scope, B7 README, cubic-cell note, runner): "signed corner actions fall into three
  classes by trace data", exactly one spinorial; B7: "four diagonal gauge classes, H^2(S4,Z2), two spinorial,
  gauge-equivalent to each other, each two copies of spin 3/2"; runner docstring: "five classes, two spinorial".
  Cubic-cell note: induced from the C6 character, spinorial corners = 2H.
- Lane-supplied: block, corner action, signs, the two-qubit Dirac walk.
- Proved/checked by them: the numerical 2^16 scan and numerical intertwiner null spaces.
  They did not give invariants, cocycles, exhaustiveness arguments, or exact data for the second spinorial class.

## Steps

### Part I -- exhaustive classification of the signed corner lifts

1. [CHECKED, S1a-c] All 65536 raw sign pairs for generators (quarter turn RZ, quarter turn RX) generate a group
   of order 24 (128 pairs), 48 (896 pairs) or more than 48 (64512 pairs); no other order. The same counts and the same
   set of 384 generated groups arise (i) with the sign on the source corner instead of the target corner and (ii) with the
   generator pair (RZ, threefold about (1,1,1)). So the target/source convention and the generator pair do not affect
   the classification. (This reconciles the two "signed-generator conventions".)
2. [PROVED] |G| = 24|K| because G maps onto O with kernel K. K is a subgroup of diagonal signs normalised by O,
   which permutes corners transitively; the only O-fixed sign vectors are +-I. Hence |G| <= 48 iff K <= {+-I}
   (central). [CHECKED, S1d] 128 groups with K = 1, 256 groups with K = {+-I}.
3. [PROVED, Shapiro] V = F2[O/C3] is a coinduced module, so H^n(O,V) = H^n(C3,F2) = 0 for n >= 1 (C3 has odd order).
   Projective central lifts are homomorphic sections O -> (V/F2) x| O, i.e. Z^1(O,V/F2); diagonal sign conjugation is B^1.
   From 0 -> F2 -> V -> V/F2 -> 0: H^1(O,V/F2) ~ H^2(O,F2) (connecting map, bijective since H^1(O,V) = H^2(O,V) = 0). So
   diagonal-sign gauge classes of central projective lifts correspond one to one with central extensions of O by Z2,
   with |B^1| = 128/2 = 64 lifts per class. [CHECKED, S3a] dim H^2(O,F2) = 2 by F2 linear algebra on 24x24 cochains
   (dim Z^2 = 24, dim B^2 = 22). [CHECKED, S2a-b] 256 = 4 x 64 projective lifts, each class one orbit, stabiliser {+-I, +-diag(v_eps)}.
4. [CHECKED, S2a, S2d, S2f, S4b] The four classes, by the pair (a,e):

   | (a,e) | group | element orders | spinorial |
   |---|---|---|---|
   | (0,0) | S4 x C2 | 1:1, 2:19, 3:8, 4:12, 6:8 (matches S4 x C2 computed from permutations) | no |
   | (0,1) | A4 x| C4 (name from the Majorana note; here identified by (a,e) and orders) | 1:1, 2:7, 3:8, 4:24, 6:8 | no |
   | (1,0) | GL(2,3) (explicit isomorphism to GL(2,F3), S4b) | 1:1, 2:13, 3:8, 4:6, 6:8, 8:12 | yes |
   | (1,1) | binary octahedral 2O (unique involution -I) | 1:1, 2:1, 3:8, 4:18, 6:8, 8:12 | yes |

   Each of the four central extensions of O by Z2 is realised by a signed corner action, exactly once up to G1.
   The 128 honest (K = 1) lifts are one G1-orbit and lie in (0,0) once -I is adjoined (S2c). So there are 5 classes of generated
   matrix groups, 4 classes of projective actions, and 3 trace-data classes (S2e). [CHECKED, S3b-c] the four section
   cocycles are cocycles, only (0,0) is a coboundary, and (a,e) -> [omega] is a group isomorphism onto H^2(O,F2).
5. [PROVED, standard Mackey/Frobenius] A monomial representation with transitive line permutation action is
   Ind_H^G(chi), H = stabiliser of the line e_0, chi = the character on e_0. H is the preimage of the corner C3 and
   (with -I in G) is C3 x {+-I} = C6 (extensions of C3 by Z2 split). chi(-I) = -1 and chi real force chi(generator of C6) = -1
   (the unique real odd character of C6). So within each class the signed corner action is the single induced
   representation Ind_{C6}^{G}(chi_real,odd). [CHECKED, S4d for GL(2,3)] chi is a homomorphism, Frobenius over 8 coset
   representatives reproduces tr D(g) on all 48 elements.

### Part II -- the one class classified in detail: GL(2,3), (a,e) = (1,0)

6. [CHECKED, S4a, exact] Representative (target-sign convention, corner index 4v0+2v1+v2, D = diag(s)P(R)):
   s_Z = (1,1,1,1,1,1,-1,-1), s_X = (1,1,-1,1,-1,1,-1,-1).
   As signed permutations e_i -> +-e_j (1-based, a minus sign means -e_j):
   D(RZ) = (5, 6, 1, 2, -7, -8, 3, 4), D(RX) = (-3, 1, 4, 2, -7, -5, -8, 6).
   D(RZ)^4 = D(RX)^4 = -I, both of order 8, D(RZ)D(RX) of order 6 with (D(RZ)D(RX))^3 = -I. The generated group has 48 elements,
   and the cocycle class is (a,e) = (1,0): axis half-turn lifts square to -I, edge half-turn lifts square to +I
   (13 involutions; compare 2O: both -I).
7. [CHECKED, S4b] Explicit isomorphism with GL(2,F3): D(RZ) -> [[0,1],[1,1]], D(RX) -> [[0,1],[1,2]] (mod 3), bijective on all 48 matrices.
8. [CHECKED, S4c, exact] Induced character chi_rho = trace of the 8x8 matrix, on the 8 conjugacy classes of G
   (size, order, value): (1,1,8), (1,2,-8) [= -I], (12,2,0) [non-central involutions = edge half-turn lifts], (8,3,2), (6,4,0) [axis half-turn lifts],
   (8,6,-2), (6,8,0), (6,8,0) [two classes of quarter-turn lifts]. Equivalently: chi = 0 off the preimage of the corner C3.
   <chi,chi> = 4. The same class function (as a function of the rotation and the lift's sign) occurs in all four classes (S4g), only the group differs.
9. [CHECKED, S4e, exact over Q] The commutant of the 8-dim representation has dimension 4 and centre dimension 1, hence is M_2(C):
   rho = V (x) C^2, V irreducible of dimension 4 with character chi/2 = (4,-4,0,1,0,-1,0,0) on the classes of step 8, <chi_V,chi_V> = 1.
   So the GL(2,3) class is two copies of the faithful 4-dim irrep of GL(2,3). For 2O the same computation gives V = spin 3/2 (H).
   [CHECKED, S4f] For the integer classes the commutant is commutative of dimension 4 (four inequivalent constituents).
10. [CHECKED, S5] Phased versions (chi(-I) = -1, chi(c3) = w^j): exact <chi,chi> is 3 for j = +-1 in every class
    (three inequivalent constituents; for 2O this is the source table E1/2 + E5/2 + H). Their decomposition for the other classes is not worked out.

### Part III -- how the classes are related

11. [PROVED + CHECKED, S3d] Let eps be the sign character of O = S4. If G is a group of matrices containing -I, then
    G' = G_even cup i G_odd is again a group, and (i g)^2 = -g^2 for odd g. Axis half-turns are even (a unchanged),
    edge half-turns are odd (e flips). In H^2(O,F2): [omega_(a,1-e)] = [omega_(a,e)] + eps U eps, checked exactly for all four classes.
    So the i-twist exchanges 2O <-> GL(2,3) and S4xC2 <-> A4x|C4.
12. [CHECKED, S4h exact] There are exactly 2 diagonal gauges g in {1,i,-1,-i}^8 (g_0 = 1) with g D_GL(R) g^dagger = lambda D_2O(R) for both
    generators, lambda = -i (resp. +i) on both (both are odd). So 2O and GL(2,3) are equivalent in G3, not in G1 (step 4: distinct invariants).
    The integer pair (0,0), (0,1) is equivalent in G3 as well (S4i).
13. [PROVED] kappa is invariant under D -> lambda U D U^dagger (scalars cancel in a commutator). kappa = -1 iff a = 1 (CHECKED S3e). So no U(1) gauge
    relates a spinorial class to an integer class: under G3 there are exactly two classes (H^2(S4,U(1)) = Z2), matching steps 11-12.
14. [PROVED + CHECKED, S6] Diagonal conjugation preserves hop positions, ranges and unitarity. If A_t is covariant for D_2O then g^dagger A_t g is covariant for D_GL
    (matrix identity of step 12). Checked exactly on the 11 independent nearest-site arrays. Hence the sources' moving covariant block walk
    W = T (U_2q (x) 1_E) T^dagger, built for the 2O representative, yields a covariant unitary walk with the same spectrum for the GL(2,3) class. [READING] This
    is why the sources' covariance and spectrum statements do not depend on which spinorial class is meant. It does not make the operator-level group law the same.
15. [PROVED + CHECKED, S4j] Nearest-site covariant family (hops of at most one site per axis, 8 x 27 = 216 coefficients): the dimension of the space
    of A with A_Rt = D A_t D^T is 11 in all four classes. Proof: every hop fixed by a rotation R has sign product s_R(v') s_R(v) = +1 (the fixed corners of a C3 lift
    carry the sign +1 on the order-3 lift and -1 on the order-6 lift, same sign at both fixed corners), so the dimension is the number of O-orbits on the 216 hops. So an
    eleven-dimensional count is not specific to either spinorial class. Whether it is the same family of unitaries is not claimed. The prime closure (are all unitary members flat?) is a separate task.

### Part IV -- reconciliation of the sources' class counts (CHECKED)

16. Layers of identification: 5 generated group types (runner docstring: "five classes, two spinorial"); 4 projective classes mod -I, diagonal sign gauge (B7: H^2(S4,Z2) = Z2^2);
    3 trace-data keys, because the key merges (0,0) with (0,1) and (1,0) with (1,1) (runner check message and note claim_scope: "three classes ... one spinorial"); 2 classes up to
    phases (integer / spinorial). "Gauge-equivalent" in B7 holds in G3 (step 12), not in G1 (step 4).
17. [CHECKED, S2g] The runner keeps one spinorial representative per trace key, and its first hit in loop order is the 2O class. The GL(2,3) class is therefore never tested separately by that runner;
    steps 12 and 14 cover it. No numerical result of the sources is contradicted. One scope point: the staggered note's "exactly one class is spinorial" holds for the trace-data key and up to phases, but at the level of generated groups there are two spinorial classes (GL(2,3) and 2O). The runner docstring's "five classes" and the check message's "3 classes" refer to different identifications.

## What is NEW relative to the sources

Not new: the four H^2 classes and "two spinorial, each two copies of spin 3/2" (B7 and the staggered note), the 2O induced-character table (cubic-cell note), the observation that the Majorana per-direction
code has the same four extensions (in a different model).
New (same-family, unrefereed): (i) the exhaustiveness argument (steps 2-3) plus the exact enumeration under both sign conventions and both generator pairs; (ii) the invariant pair (a,e) and the
identification of the four classes as S4xC2, A4x|C4, GL(2,3), 2O with cocycle checks; (iii) the exact classification of the GL(2,3) class: representatives, explicit isomorphism, character, rho = 2V; (iv) the precise
relation of the two spinorial classes (i-twist plus a diagonal Gaussian gauge; distinct central extensions) and the exact transfer of covariant arrays; (v) class independence of the 11-dimensional nearest-site count with proof;
(vi) the layering that reconciles "three/four/five/two" classes.

## Not shown, first unresolved step

- First unresolved step: step 0/A2-A3, the premise gap. The axioms do not select the block, the block-centre action, the monomial form or an extension class; I classified only inside that supplied family.
  Within the family, the first unfinished classification is the non-central case (64512 of 65536 raw pairs, kernel K with a non-scalar diagonal sign): I did not classify these lifts (they are subgroups of V x| O
  mapping onto O, i.e. H^1(O,V/K) for O-submodules K of V), nor whether any admits a covariant moving walk that does not decouple into K-sectors.
- Not shown: any action on other cells (face centres, edge midpoints, larger blocks), non-monomial actions, a physical selection between 2O and GL(2,3) (nothing here prefers either), decomposition of the phased
  GL/S4xC2/A4x|C4 cases, and any claim about generations, masses or the nearest-site prime closure. A4x|C4 is identified by invariants and orders, not by an explicit isomorphism.
- Not claimed: that the i-twist is a physical gauge freedom; it is an equivalence only for statements insensitive to per-rotation phases (covariance of W under conjugation).

## Disjoint check

`check.py` (pure integer / Fraction / sympy arithmetic, no imports from the sources): 29 checks, `TOTAL: PASS=29 FAIL=0`, about 30 s, under 100 MB. It re-derives everything by enumeration and F2/rational linear algebra; the argument in steps 3, 5, 13, 15 is
by cohomology and induction, which the enumeration does not use.
