# PRE reconstruction: compensated cube energy accounting

Independent source-bound reconstruction, 2026-09-24. This packet stops before
comparison with the high-flux-energy author or any prior independent attempt.
It supplies a conditional operator calculation and exact controls, not retained
status, an audit, or an autonomous reservoir construction.

## Contract, sources and exact scope

The input sources, their complete snapshots and hashes are in
`SOURCE_BINDINGS.json` and `sources/`. The raw checkout is
`/Users/jonreilly/Documents/Codex/mobile-record-formation-20260920` at
`f82e21b82f209871f84d671bfc020cea0116e693`. Current-main science workflow was
verified against `61fa847f032d25c90bca2c1273b7edb5713fe160`; planning instructions
were read at `eb1f1ca8338848cf2046582e13aef372d8540937`. No git mutation,
network action, landing, audit or source comparison was performed.

Accepted model premises are exactly the supplied cube, hard-core charges,
Gauss sector, normalized shifts, formation instruments and added gated
compensation. The earlier parent note supplies the actual hop and birth
operators. The general target note is read with its explicit correction:
self-adjointness applies to the two Hamiltonian coefficients, not all displayed
operators. The reconstruction does not re-prove the microscopic approximation.

Edges are ordered by smaller endpoint and satisfy `i xor j` in `{1,2,4}`.
The A sites are `{0,3,5,6}`, the B sites `{1,2,4,7}`. Write `g_n` for the
normalized electric basis vector with all A charges plus, all B vacant, and

    E01=n, E13=n, E23=-n, E02=-n, all other E=0, n an integer.

This is a divergence-free field and hence an allowed Gauss state. It is a
normalizable vector, not an electric-plane-wave generalized eigenvector.

The first-output statements below mean the normalized actual jump vector
`B_j g_n / ||B_j g_n||`, with the specified mark. They are the conditional
immediate output from this input. At a later first-event time, the no-event
Hamiltonian has evolved the input, and the output is instead the jump applied
to that evolved vector. No time-independent claim about that later output
field distribution is implicit here.

## Operators retained throughout

A hop of charge c from the lower edge endpoint to the upper shifts E by -c;
the reverse direction shifts by +c. A resolved birth with charge c at the
lower endpoint shifts E by +c and creates the opposite charge at the upper.
The physical birth operator annihilates occupied-edge inputs. With the
negative hopping convention of the source,

    A = Pi1 T P, M=A* A, Z=Pi2 T Pi1 T P, B_j=-P j Pi1 T P.

On the cube the compensation is zero on every sector with W>=1. On P,

    C0=M+D/C, C1=0, C=S(S+1),
    H4_S^C = -{M_S,D}/(2C) - Z_S*Z_S/2.                 (1)

For unit rotors the first term vanishes and

    H4 = -Z*Z/2,    h=K D+delta H4.                    (2)

The electric multiplication operator is

    D(q,E)=sum_(a in A,b~a,q_b=0) E_ab(E_ab+k_ab(q_a)),

with k=-q_a for a lower endpoint and +q_a for an upper endpoint. Every term
is nonnegative on integer fields. In particular `D(g_n)=4n^2`.

The effective energy generator form at the input is

    G_h(g)=kappa [sum_j <B_j g,h B_j g> -Re <R g,h g>],
    R=sum_j B_j*B_j.                                  (3)

The Hamiltonian commutator makes no contribution to its own energy. Its
expectation for D and H4 separately also vanishes at g_n because g_n is a D
eigenvector. This is an unbounded-observable quadratic form on the specified finite-support input;
it is not asserted to be a bounded Heisenberg observable on all densities.

## Resolved mark edge (0,1), plus at 0 and minus at 1

The virtual old plus at 0 must first hop to 2 or 4; hopping to 1 prevents
birth on the selected edge and is excluded by the actual hard-core operator.
Both legal rotor amplitudes are +1 in B_j. Denote the two orthogonal outputs
by v2 and v4:

| output | occupied B charges | field shifts relative to g_n | D |
|---|---|---|---|
| v2 | q1=-1, q2=+1 | E01 +=1, E02 -=1 | 0 |
| v4 | q1=-1, q4=+1 | E01 +=1, E04 -=1 | 2n^2 |

All A charges remain plus. For v2 every initially nonzero face edge terminates
at an occupied B site, so none contributes to D. For v4 the surviving face
contributions are `(-n)(-n-1)+(-n)(-n+1)=2n^2`. The shifts on the birth and
old-hop edges lie at occupied B sites and do not enter D after the event.

Thus `B_01,+ g_n=v2+v4`, the mark intensity is `2 kappa`, and

    Pr(D=0)=1/2, Pr(D=2n^2)=1/2,
    E[D]=n^2, Var(D)=n^4.                              (4)

At n=0 the two D values coincide and their probabilities combine.
The output is a coherent two-route vector, not an incoherent path mixture.
Equation (4) describes its D measurement; it does not license dropping its
coherence when computing H4.

For the other resolved sign on this edge, call the two vectors u2,u4. Here
q0=-1,q1=+1, the birth shift is E01 -=1, and the same old-hop alternatives
occur. Their D values are 0 and `2n(n-1)`, respectively. The coherent-per-edge
instrument has actual output `v2+v4+u2+u4` and squared norm 4. Its rotor D
measure is

    (1/2) point_mass_0 +(1/4) point_mass_(2n^2)
                          +(1/4) point_mass_(2n(n-1)),
    E[D]=n(2n-1)/2,
    Var(D)=n^2(4n^2-4n+3)/4.                           (5)

Coincident eigenvalues are again combined. The coherent and resolved
instruments need not have the same conditional state or later statistics.

## Fourth-order calculation from Z, including path interference

For g_n, an unordered pair of outward hops must use distinct A sites and
distinct B destinations. There are

    binomial(12,2)-4 binomial(3,2)-4 binomial(3,2)=42

such pairs. Their two orders have equal amplitude, and different edge-pair
sets give different final electric basis states even if some matter words
coincide. Therefore

    ||Z g_n||^2=4*42=168, <g_n,H4 g_n>=-84.            (6)

For each single six-record output basis state, only two B sites are empty.
Each has three A neighbors and the two share two A neighbors. Hence there
are `3*3-2=7` legal unordered outward-hop pairs and

    ||Z v2||^2=||Z v4||^2=||Z u2||^2=||Z u4||^2=28.

For the plus-at-A mark, the images of v2 and v4 overlap. Both empty A0 by
moving its plus to the alternative old destination and empty one of the
three A neighbors of B7 by moving that plus to B7. There are three common
states, each with amplitude 2 in each Z image. Consequently

    <Z v2,Z v4>=3*4=12,
    ||Z(v2+v4)||^2=56+24=80,
    <H4>_(resolved plus)=-20.                          (7)

For the minus-at-A mark the analogous moves leave the minus at different B
sites, so the images are orthogonal and

    ||Z(u2+u4)||^2=56, <H4>_(resolved minus)=-14.        (8)

The plus/minus branches also have orthogonal Z images: the birth B endpoint
is occupied throughout these outward hops, and its charge differs between
branches. Thus the coherent mark has norm squared 4, Z norm squared 136,
and normalized H4 expectation -17.

These are expectations of an operator with nontrivial off-diagonal action.
Neither g_n nor its output has been assumed to diagonalize H4. In particular,
dephasing v2,v4 before applying Z would replace the correct unnormalized H4
gain -40 by -28. The second exact control intentionally makes this wrong
replacement and detects the discrepancy.

It follows that the actual selected rotor system-energy means are

    input:                 4K n^2-84 delta,
    resolved plus output:  K n^2-20 delta,
    coherent 01 output:    K n(2n-1)/2-17 delta.        (9)

The resolved-plus conditional mean change is `-3K n^2+64 delta`.
These output D measures are not the spectral distribution of h, since D and
H4 need not commute. Nevertheless boundedness of H4 gives

    |sd(h)-K sd(D)| <= delta ||H4||.                  (10)

Thus the resolved-plus h standard deviation grows as `K n^2+O(1)`. The
coherent output has the same leading growth. This inference does not confuse
a spread in D with two sharp total-energy eigenvalues.

## All-mark intensity and rotor energy drift

There are 4 choices of A center, 3 birth neighbors, 2 distinct old-record
destinations, and 2 resolved birth charge signs: 48 orthogonal marked route
contributions. For each fixed mark, reversing its birth and old hop uniquely
recovers the input. Cross signs in its coherent loss are orthogonal. Thus

    R g_n=48 g_n, intensity=48 kappa                    (11)

for either instrument. On the entire initially vacant-B sector the loss is
indeed scalar, giving a rotor first waiting time exponential with this rate;
that statement does not freeze the conditional field.

For clarity the D gain can also be counted without the path program. A given
B site is empty in 24 of the 48 contributions. A surviving edge retains its
original field because the two shifted edges both terminate at filled B
sites. For an edge attached to A site a, among those 24 events the center is
a in four; its two birth signs cancel in the linear term. The other twenty
have q_a=+1. Hence

    sum_j <B_j g_n,D B_j g_n>
       =24 sum_e E_e^2+20 sum_e k_e(+) E_e=96n^2,

where the last linear sum vanishes by Gauss. Subtracting the initial electric
loss `48*4n^2` gives `-96n^2`.

Cube symmetry makes twelve resolved marks plus-at-A and twelve minus-at-A.
Equations (7)-(8) give total H4 gain `12*(-40-28)=-816`; the initial loss is
`48*(-84)=-4032`. Therefore, for both instruments,

    G_D(g_n)/kappa=-96n^2,
    G_H4(g_n)/kappa=3216,
    G_h(g_n)=kappa[-96K n^2+3216 delta].               (12)

The drift is negative for `n^2>(67/2) delta/K`, zero at equality if an integer
n realizes it, and positive below. Per first-event averaging gives total
energy change `-2K n^2+67 delta`. This is the instantaneous all-mark mean
balance on the supplied input, not a heat theorem.

Translation by the integer divergence-free face circulation is a unitary
on the physical rotor Hilbert space. It commutes with each rotor hop, birth,
P, Z, B_j and H4. Thus the route amplitudes, overlaps and H4 matrix elements
above are independent of n for a structural reason. D transforms according
to its charge- and vacancy-dependent quadratic polynomial, giving (4)-(5)
and (12) for every integer n. The full h evolution is not covariant under
this translation because D is not invariant.

## Exact finite-spin target and moving high flux

Let `C=S(S+1)` and

    p=1-n(n+1)/C, q=1-n(n-1)/C.

The exact normalized shift is
`|E> -> sqrt(1-E(E+k)/C)|E+k>`, with zero at a forbidden boundary step.
For the selected resolved-plus mark the two squared amplitudes are p^2 at
D=0 and p at D=2n^2. Consequently, whenever the mark has nonzero weight,

    weight=p(1+p),
    Pr(D=0)=p/(1+p), Pr(D=2n^2)=1/(1+p),
    E[D]=2n^2/(1+p), Var(D)=4n^4 p/(1+p)^2.            (13)

For the resolved-minus mark the weights are pq,q and the second D value is
`2n(n-1)`. Its total weight is `q(1+p)` and the same conditional probabilities
apply to the two routes. For the coherent mark the total weight is
`(p+q)(1+p)` and its unnormalized D measure is

    p(p+q) point_mass_0 + p point_mass_(2n^2)
                           + q point_mass_(2n(n-1)).  (14)

The physical mark intensities are kappa times these weights. A zero-weight
mark has no normalized output; for example the plus mark is blocked at n=S.
The asymptotic regime below stays strictly inside that boundary.

Direct expansion of all 48 route weights and their D values gives, for either
instrument, putting `u=n^2/C`,

    R g_n=r_S g_n, r_S=8(6-4u+u^2),
    G_D(g_n)/kappa=-16n^2(6-6u+2u^2+1/C).             (15)

For example the two A vertices on the circulation face each have outward
weights p,q,1 and summed birth-sign weights 2(1-u),2(1-u),2; summing distinct
old/birth neighbors gives `12-16u+4u^2` at each. The other two centers each
contribute 12, proving the rate formula without asymptotic replacement.
The D formula is the exact polynomial expansion of the same finite route sum;
the symbolic control retains each mark and full charge/electric endpoint.

The fourth-order term must retain the anticommutator in (1). The control
computes its form through

    <v,H4_S v>=-||Z_S v||^2/2
                -Re <A_S v,A_S Dv>/C.                (16)

For the input one obtains

    <H4_S>_input=-84+8u+12u^2-4n^2/C^2.

For both instruments the exact all-mark fourth-order drift is

    G_H4,S(g_n)/kappa
       =3216-2608u+456u^2+240u^3-96u^4
          +(184u-224u^2+32u^3)/C.                    (17)

The complete finite-spin energy drift is
`kappa [K*(-16n^2(6-6u+2u^2+1/C)) + delta*(the polynomial in (17))]`. The control evaluates M as A* A on the
actual outputs; it never replaces their M by the initial-sector scalar.
A second implementation applies both anticommutator orders and all four
hops in Z*Z directly, with exact square-root spin amplitudes and boundary
checks. It verifies (15)-(17), including negative and nonzero n.

Now let integer n=n(S) satisfy `n/S -> x`, `0<x<1`, and write `a=1-x^2`.
The selected resolved-plus mark has limiting weight `a(1+a)>0`; the coherent
mark has twice that weight. For either selected instrument, the leading
scaled D measure has weights `a/(1+a),1/(1+a)` at `0,2x^2`, respectively:

    E[D]/S^2 -> 2x^2/(2-x^2),
    Var(D)/S^4 -> 4x^4(1-x^2)/(2-x^2)^2.              (18)

The two coherent nonzero values differ only by order S and coalesce after
S^2 scaling. The limiting all-mark first intensity and leading total drift
are

    intensity -> 8 kappa(x^4-4x^2+6),
    G_h(g_n)/S^2 -> -32 kappa K x^2(x^4-3x^2+3).      (19)

The leading drift is strictly negative throughout 0<x<1. The fourth-order
piece has a finite limit

    G_H4,S(g_n)/kappa ->
       3216-2608x^2+456x^4+240x^6-96x^8.              (20)

It has no order-S^2 term. Uniform boundedness also follows directly: normalized
spin shifts are contractions, `||T||<=12`, `||A||<=12`, `||Z||<=144`, and
`||D/C||<=12` on physical P. Equation (1) gives the coarse sufficient bound
`||H4_S||<=12096`, independent of S. The finitely many jump norms are uniformly
bounded as well, so their H4 generator-form contribution is uniformly bounded.
The sharper exact polynomial (17) corroborates this structural bound.

Equation (10) with the uniform bound now proves an actual total-energy spread
of order S^2 on the selected output, with leading standard deviation

    2 K x^2 sqrt(1-x^2)/(2-x^2) * S^2.

The proof and symbolic formulas are valid for the interior high-flux sequence;
all relevant paths eventually lie inside the spin box. The separate direct
control enforces boundaries even in small finite-spin cases. No moving-input
rotor approximation is used to derive (18)-(20).

## Domains, convergence and the microscopic energy distinction

Finite-support physical vectors form a core for the nonnegative multiplication
operator D. Bounded H4 makes h self-adjoint on D(D). Each g_n and every finite
jump/hop image used here lies in the domain of every needed finite operator
product, so the forms and variance statements are finite. A general normalizable
rotor density need not have finite D or h moments: qualitative trace-class
semigroup existence does not supply such moment hypotheses.

For fixed integer n, the exact expressions above tend to their rotor values
as S increases. This is compatible with the source's strong trace-class
limit for fixed inputs and trace-norm convergent initial approximants. The
sequence `|g_n(S)><g_n(S)|` with n/S -> x>0 has no trace-norm limiting rotor
density: distinct integer electric basis states are orthogonal. Neither
strong operator convergence nor the fixed-input theorem supplies a uniform
approximation on this moving high-field family. Its exact rate in (19) also
differs from 48 kappa, directly displaying that distinction.

Even with a density approximation, unbounded microscopic energy moments do
not follow. The supplied microscopic Hamiltonian is

    H_epsilon,S=delta epsilon^-4 W +delta epsilon^-3 T
                                      +delta epsilon^-2 C_S,
    epsilon^2 C=delta/K.

Its norm grows at least on the scale epsilon^-4. A bare O(epsilon) trace-norm
error cannot by itself control its absolute expectation error. On the
undressed input g_n, W and the expectation of T vanish, while the expectation
of C_S is exactly 12: on the initial sector `C0=M+D/C=12 I`. Therefore

    <g_n,H_epsilon,S g_n>=12 delta epsilon^-2=12K C,   (21)

whereas the effective low-cluster Hamiltonian expectation is the distinct
`4K n^2+delta <H4_S>`. Small occupation of high-penalty clusters can carry a
large energy moment. Equation (21) is a concrete reason not to identify the
effective h balance with a converged bare microscopic energy balance.
Also every microscopic j annihilates the undressed input at time zero, so
its instantaneous microscopic dissipative energy drift initially vanishes.
The effective positive first intensity and its energy drift arise after the
fast initialization layer; convergence of finite-time densities does not imply
convergence of derivatives at time zero.

The above balance uses precisely the stipulated h (or finite-spin target h_S).
Adding a number-dependent offset, unlike an overall scalar, changes energy
transferred per formation and therefore changes physical energy accounting,
even if certain number-block-diagonal density dynamics agree.

## Physical interpretation and unresolved obligations

The large decrease in D is easy to locate: birth fills B vertices and thereby
removes their incident electric terms from the supplied vacancy-weighted D.
It does not erase all the corresponding electric fields. Bounded formation
amplitudes coexist with unbounded changes of the system's chosen energy on
this rotor family, and with order-S^2 changes on moving spin inputs.

These calculations establish an effective system-energy balance. They do not
identify it as heat, prove an autonomous energy-conserving dilation, supply a
fuel state, establish reservoir capacity, or establish a thermal/detailed-balance
law. The supplied B_j are not assumed energy-resolved eigenoperators of h;
the two D peaks are not sharp h-energy transitions. Any physical reservoir
interpretation must independently specify its Hamiltonian, coupling, initial
state and energy accounting, and demonstrate that this effective instrument
and its required energy/spread are produced in its stated domain. No global
no-go about possible reservoirs is claimed here.

The source-bound independent PRE reconstruction is complete for the requested
rotor and interior high-flux effective-spin questions. What remains open is
comparison with the withheld author, a microscopic unbounded-energy-moment
transfer theorem, and any autonomous reservoir/heat identification. No such
comparison or additional theorem has been performed in this packet.

## Evidence, failures and reproduction

`independent_exact_control.py` builds all legal paths from charge words and
edge orientations. It uses formal ladder-bond square roots; pairing equal
endpoints makes all powers even, producing exact rational polynomials in n,C.
It saves every mark and selected output in `EXACT_RESULTS.json` and full output
in `exact_control.log`. No model builder or expected energy constant is imported.

`direct_matrix_action_control.py` is a separately written control with actual
integer fields and exact SymPy square roots. It applies H4 and B adjoints as
operators, checks the complete loss action, and tests both instruments at
rotor n=0,3 and spin `(S,n)=(2,0),(2,1),(3,-2),(3,2)`. It compares against this
PRE's own symbolic results only after those were computed. Its full records
are `DIRECT_ACTION_RESULTS.json` and `direct_action_control.log`. These are
same-reconstructor cross-checks with shared model definitions, not a claim of
an additional independent human/agent review.

The initial tool-mediated file-write attempt did not create the runner, so an
initial execution failed with file-not-found. That failure is preserved as
`INITIAL_EXECUTION_FAILURE.log`; subsequent explicit writes and both runs
completed. No failed physics assertion was suppressed. Reproduce from this
directory with the specified Python executable:

    /opt/homebrew/opt/python@3.13/bin/python3.13 independent_exact_control.py
    /opt/homebrew/opt/python@3.13/bin/python3.13 direct_matrix_action_control.py

`PRE_SEAL.json` binds this note, source snapshots, full results, complete logs,
runner files and execution receipt. Its SHA256 is recorded in
`PRE_SEAL.sha256`. The seal authenticates bytes and exposure order; it does not
constitute scientific retention or prove the underlying model describes nature.
