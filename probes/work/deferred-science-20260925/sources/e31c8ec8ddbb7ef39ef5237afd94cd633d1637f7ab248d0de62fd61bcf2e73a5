# First-birth charge and the separated flat magnetic threshold

Personal root derivation, 25 September 2026. Conditional mathematics in the
supplied model; not yet independently checked at this seal. No particle or
measured-charge identification. The question is whether the already known
first-birth spectral minimum also supplies a physical charged excitation.

## 1. Sources, model and precise limits

Use the full original matter/rotor formation model of the local-pair and common
compensation parents, together with the native-ground publication in PR9199,
head d3dfdff92b6eb9e422da3691d13af4c249b7c4e9. Exact source identities accompany
this note. PR9199 is open, not retained or merged. Its finite-graph weak-coupling
spectral comparison is an imported conditional theorem.

On an even cubic torus let n=L^3/2=|A|=|B|. All A vertices are occupied on P;
Gauss law is div E=q-1_A. The first postbirth number sector has N=n+2 and,
since total q=n, precisely one negative color among m=n+2 occupied vertices.
The full common Hamiltonian remains h=KD+delta H4 with the original vacancy-
gated D. Here Q=-H4 at a flat magnetic connection uses coefficient TWO per
unordered overlapping A-pair Gram. This is the root33 convention. It is twice
the unordered Q used when writing h=KD-2delta Q in the common-law convention.

The parent establishes that the bottom of the full colored flat H4 has the
same value as the occupancy comparison -Q_occ. The embedding is

  U|X> = m^(-1/2) sum_(z in A union X) |X; minus at z>,   X={b,c} subset B.

It is a spectral comparison and intertwining for the flat magnetic operator.
It does not delete colors, identify a physically selected state, or replace
the actual initial field by flat angle. In particular, zero electric winding
has harmonic-angle Haar measure; it is not a zero-angle state.

For L>=6 the flat empty-B scalar is q0=321 L^3. Put R_L=Q_occ-q0 I. The
parent's fixed-finite-L limit is

  Delta_L := lim_(g->0) g^2 tau [inf h_(n+2)(g)-inf h_n(g)]
           = -lambda_max(R_L)/4.                                  (1)

K=g^2/(2tau), delta=1/(4tau g^2), tau=a/c are supplied parameter relations,
not calibration to measured charge or mass. The cyclic spectral-edge statement
for actual births in that parent is not an energy atom, mean or concentration
statement. All finite-g field/color dynamics and original jumps remain in force.

## 2. A local definition and the separated contribution

For each unordered overlapping A pair {a,c}, let P_ac be the list of ordered
paths (u,v) with u adjacent to a, v adjacent to c, u!=v. Duplicate unordered
targets have multiplicity t_ac(d). On an occupancy X, outward paths must avoid
X. The corresponding exact matrix contribution is 2 S_ac* S_ac. Its row is
obtained by creating u,v and returning any permitted ordered pair from the
intermediate occupancy. Subtract the empty-B diagonal scalar
2 sum_d t_ac(d)^2 for that local pair.

If X misses N(a) union N(c), this difference vanishes. Thus only overlapping
star unions touching X are included in R. This defines a finite-range bounded
real symmetric operator on the infinite unordered-pair configuration space;
no subtraction of two divergent infinite-volume operators is performed.
Uniformly finitely many paths meet each X, so the absolute row sums are bounded.
All off-diagonal entries are nonnegative.

The B vertices in any one star union have lattice distance at most4. When the
two records are more than4 apart, no contributing union touches both. The row
then splits into two translated one-occupancy algebraic contributions. The
auxiliary one-occupancy kernel, classified by absolute displacement, is

| Displacement class | Multiplicity | Coefficient for each displacement |
|---|---:|---:|
|000|1|-1284|
|002|6|220|
|011|12|424|
|004|6|2|
|013|24|8|
|022|12|12|
|112|24|24|

These integers follow by the finite path enumeration above, reproduced without
an imported scientific helper in the accompanying standalone program. The row
sum is6048 and sum_d t(d)d_i d_j=7392 delta_ij. Its Fourier symbol is therefore
6048-3696|k|^2+O(|k|^4), with the remainder bounded by its finite fourth moment.
This kernel is an algebraic contribution, not a physical odd-number sector:
N=n+1 would have the wrong parity to satisfy total q=n on the torus. In
particular, this curvature is not an electron mass or an assigned inertial mass.

The separated pair row sum is lambda=12096. For the six near classes, the
deviations from this value and their multiplicities are

  002: -196 (6); 011: -584 (12); 004: +26 (6);
  013: +72 (24); 022: +92 (12); 112: +152 (24).       (2)

Their total over all nonzero near displacements is -1548. Row sums above12096
occur, so a bound by the maximum unweighted row sum does not give the separated
threshold. A positive nonconstant supersolution is necessary for the argument
given here.

## 3. An exact positive supersolution

Let d(X) be the sorted absolute displacement and set v(X)=1-x(d(X)), with x=0
outside distance6. The thirteen deficits have common denominator10^9. The last
column is the numerator, at that same denominator, of (Rv-12096v)(X).

| Class | Deficit numerator | Residual numerator |
|---|---:|---:|
|002|30355481|-10002520|
|004|0|-9999140|
|006|82543|-10004780|
|011|62454728|-16736738424|
|013|592565|-9991656|
|015|257096|-10000960|
|022|1564788|-9994872|
|024|501938|-10006332|
|033|0|-10221152344|
|112|2988879|-10003268|
|114|733404|-10001320|
|123|1227493|-10005992|
|222|0|-27847107864|

Every deficit is in [0,1), so 0.937545272<=v<=1. The exact integer grouped rows
used for these residuals are all retained in the result. Cubic symmetry and
even translation give all inputs of distance<=6. For any other input, v(X)=1,
the row sum is12096, and v(Y)<=1 with R_XY>=0 for Y!=X. Therefore

  (Rv)(X)-12096 = sum_(Y!=X) R_XY[v(Y)-1] <=0.       (3)

This proves the tail, without checking a finite cutoff and extrapolating. The
program additionally reconstructs all37 classes through distance10 and finds
their exact nonpositive residuals. Floating linear programming was used only
to propose the rational trial. Neither this inequality nor its proof depends
on the accuracy or optimality of that solve.

For finitely supported complex psi the exact ground-state-transform identity is

  <psi,(lambda-R)psi>
  = (1/2) sum_(X!=Y) R_XY v_X v_Y |psi_X/v_X-psi_Y/v_Y|^2
    +sum_X [lambda-(Rv)_X/v_X]|psi_X|^2.              (4)

All terms on the right are nonnegative. Boundedness extends R<=12096 I from
the finitely supported core to the full unordered-pair Hilbert space.

For the reverse spectral bound, take constant normalized amplitudes on pairs
with one point in each of two large disjoint B-sublattice boxes, separated by
more than the interaction range. In the bulk each row has sum12096. Only a
fixed-thickness boundary of either box loses hopping terms, with bounded total
weight per row. Boundary/volume is O(1/box size), so these Rayleigh quotients
tend to12096. Hence

  sup spec R_infinite = 12096.                         (5)

This is the separated flat occupancy threshold. There is no state of this
operator with energy -R below -12096. It does not exclude binding at finite g,
identify a bound particle, establish threshold eigenvectors, or prove scattering
completeness. The full infinite-volume rotor model is not constructed here.

## 4. Conservative periodic extension and ordered energy limit

For even L>=24 use the minimal-image displacement in v. If its distance is<=6,
choose the unique short lift. The union of the radius4 neighborhoods of the two
input B sites has coordinate span at most14<L-1, so all contributing primitive
stars and their adjacency relations lift without a periodic alias. A nonzero
transition changes only one record by distance<=4, unless both are returned
through the same star union; in that case the output separation is<=4. Thus
every relevant output difference has coordinates of absolute value<=10<L/2.
Its trial value agrees with the unwrapped row. The thirteen inequalities hold.

At distance>6 no star union touches both records. Each local one-record patch
has its unwrapped row sum, giving12096 even across a periodic boundary. With
v(X)=1, the same off-diagonal argument (3) applies. Equation (4) therefore gives
lambda_max(R_L)<=12096 on every such finite torus. The use of L>=24 is
conservative, not a claim of an optimal minimum size. Actual modular primitive
controls at L24 and26, including translated boundary inputs and antipodal
separations, provide checks of the lifting argument; they do not replace it.

The normalized constant pair vector has Rayleigh quotient
12096-1548/(n-1). To see the factor, average first over ordered pairs: each of
the n-1 nonzero B displacements is represented equally. Symmetrization to
unordered pairs changes neither quotient. The near corrections are (2), and
there are no other corrections. Consequently

  12096-1548/(n-1) <= lambda_max(R_L) <=12096,
  -3024 <= Delta_L <= -3024+387/(n-1),  L even>=24.    (6)

It follows in the stated order that

  lim_(L->infinity) lim_(g->0) g^2 tau
       [inf h_(n+2)(g)-inf h_n(g)] = -3024.           (7)

No joint limit, uniform finite-g remainder, finite-density ground gap, mass,
typical birth energy or physical stability conclusion follows from (7).

## 5. Charge observables in the spectral comparison

For fixed occupancy X={b,c}, the uniform-minus state has m=n+2 equally likely
minus locations. For each occupied vertex, U* q_x U=(1-2/m)n_x. Relative to
the original all-A-plus background, its mean charge is -2/m at every A site
and 1-2/m at each of b,c. The probability that the minus color lies on one of
the B records is2/m; it lies on A with probability n/m. Total charge relative
to the background remains exactly zero.

For a real vertex test f define rho(f)=sum_x f_x(q_x-1_A(x)). In a fixed-X
uniform-minus state,

  rho(f) = f_b+f_c-2 f_Z,
  <rho(f)> = f_b+f_c-(2/m) sum_(z occupied) f_z,
  Var rho(f) =4[(1/m)sum_(z occupied) f_z^2
                    -((1/m)sum_(z occupied) f_z)^2].             (8)

These formulas follow from the diagonal charge eigenvalues, not a field-only
ansatz. For the rank-one color projector P_U at X,

  ||(1-P_U)rho(f)U|X>||^2 = Var rho(f).                           (9)

It is generally positive. Merely compressing charge to U* rho(f) U thus loses
its charge fluctuations and matrix elements outside that line. No extra scalar
potential is adopted here; (9) concerns an existing observable. Using such a
compression as a dynamical charged-particle theory would require an additional
decoupling/selection argument, not just the spectral-edge equality.

## 6. Compare with the original actual first birth

Start with the original all-A-plus, empty-B, zero-electric-flux basis input.
For a resolved birth mark (a->b,sigma), an outward transfer from a to another
neighbor c!=b first moves its plus color. The pair creator then places sigma
at a and -sigma at b. Each resulting occupancy X={b,c} has

  Delta q_a=sigma-1,  q_b=-sigma,  q_c=+1,
  Delta E=sigma e_(a,b)-e_(a,c).                                  (10)

The divergence of this electric shift equals exactly the listed charge change.
For sigma=+1 the two B sites carry opposite charges and A is unchanged. For
sigma=-1 both B sites are positive, while a changes from plus to minus,
carrying a charge change -2. Thus the second outcome cannot be described as
opposite charges at the two new records. Both signs occur with equal initial
resolved norm in this supplied instrument. The initial resolved ensemble has
minus-on-B probability1/2, not the uniform-minus value2/(n+2).

Within the parent flat color representation a resolved mark has one minus
location for every distinct X, so its squared projection onto the uniform-minus
line is exactly1/m of its norm. This remains true for a chosen standard Gauss
fiber identification extended over the angle variables: each X still has one
nonzero color component, and its unit-modulus reference-flow phase drops out
of this ratio. This is a statement about that specified comparison projector,
not a canonically selected observable or an energy-window projection.

For the stipulated unnormalized coherent sum of the two signs, the two color
components for each X are orthogonal. At the flat connection with both path
phases one, the ratio is2/m. For arbitrary relative phases the projection ratio
is at most2/m, by Cauchy-Schwarz; equality cannot be assumed for an actual angle
distribution or arbitrary reference-flow convention. The resolved instrument
and its coherent alternative therefore remain separately stated. No normalized
coherent jump is silently substituted.

These overlap statements are not probabilities of lying near the spectral
minimum. A rank-one color comparison line is not the full energy projector,
and the electric term at finite g does not generally preserve it. A nonzero
birth cyclic edge and small color-line overlap can coexist. The original
formation law also continues after birth; neither comparison removes it.

## 7. Controls, failures and the observation obligation

The standalone standard-library program reconstructs37 complete integer grouped
rows,68 modular periodic controls,43 exact reciprocal entries and all85 entries
of the auxiliary kernel. Its37 rows agree exactly with the earlier independently
expressed personal helper calculation; that is root crosschecking, not an
independent agent review. It directly checks8448 resolved primitive charge/flux
outputs over the degree-three cube and L4/L6 tori, all1704 resolved edge/sign
marks,852 flat coherent edge controls and15 complete test-charge moment rows.
No six-site second birth is used. Actual execution took3.166498542 seconds,
exit0, empty stderr. Full rows, source, stdout and receipt are preserved.

The support-distance2 and4 positive-deficit ansatz searches were infeasible.
Those are failures of chosen numerical ansatzes, not impossibility theorems.
Distance6 produced the exact rational proposal. The shorter deficit vector
was proposed by a saved result from a here-document calculation; its full shell
source was not saved. The final standalone program reconstructs all decisive
rows and checks the proposed rational values without that exploratory code or
any scientific import. No failed execution is erased or called confirmation.

The next observational obligation is to identify an actual dynamically selected
charged preparation, its current/force response and its controlled parameter
scale. The energy edge, the initial signed charge pattern and the uniform-color
comparison are three distinct facts. No measured electron mass, fine-structure
constant, Coulomb law from another supplied model, or photon calibration is
inserted to equate them. No fit to observations or empirical prediction is
claimed by this conditional unit.

## 8. Scope stress test for the narrow threshold exclusion

N1 Alternative routes: finite-g binding, other number sectors and other physical
preparations remain open; a flat two-occupancy upper bound excludes none of them.
N2 Wall independence: (5) is a local operator theorem. Its use in (7) separately
imports the parent's finite-L weak-g energy limit, not experimental calibration.
N3 Hidden walls: unsigned hard-core amplitudes, full overlapping stars, cubic
degree6, one-minus sector and the order of limits are explicit. Smaller tori
with extra coincidences are excluded from (6), not swept into the same count.
N4 Residual matching: exact integer path rows verify the rational supersolution;
the infinite tail follows (3), and finite-volume lifting is proved separately.
N5 Rhetoric: no no-go for charged matter, QED, the full rotor law or a TOE is made.
N6 Partial routes: full charge/current matrix elements, finite-g color/field
mixing and measured-scale identification remain available research directions.
N7 Steelman: perturbations may bind even when a leading flat operator does not;
no uniform error small compared with such a binding energy has been supplied.
N8 Earlier-cycle check: PR9199 established finite-graph cyclic edges, not this
separated threshold or a typical particle. The present bound sharpens only
that specified leading comparison and preserves the earlier limitations.
