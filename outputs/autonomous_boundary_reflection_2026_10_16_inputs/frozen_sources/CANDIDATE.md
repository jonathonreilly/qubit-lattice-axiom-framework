# Static boundary reflection for the fixed old-pair gate

Provisional root derivation, 2026-10-16. Not independently checked, retained,
or a native hardware result. This is an alternative conditional apparatus for
the target of PR9657, not an autonomous implementation of its four-qubit
mediator or its prescribed ramps. Those two source qubits may be retained as
uncoupled |00> spectators if that output register is desired.

## Target, sources and added premises

Keep the literal old pair K=2I+Z1 Z2 and the target

    W=((9+12i)I+(-16+12i)X1 X2)/25
      =exp(i theta) exp(i theta X1 X2), theta=atan(4/3).

Both W and X1 X2 commute with K. The exact source is PR9657 head
c86e61caf46c848fe8cee57ecbea6e6fdad7a4bc, with note SHA
b25d812dc1a4cdad2959f003ddd36346f2de0058292c74c7d0e07c9c5e395a4d.
The existing native half-line clock note at that head, SHA
87d8c6f4b98563cd827f0d8264ec2575c689ec4d7ac018fe5b87d89006181ed3,
already supplies the general outgoing-tail strategy, positive one-hot clock
extension and finite-horizon versus infinite-apparatus distinction. This
proposal does not claim those ideas as new. Scattering gates are also prior
literature: Childs, arXiv:0806.1972, sections I-II (background mechanism, no
theorem from that paper is required below).

New conditional resources are a half-line of clock qubits, one independently
prepared incoming one-head packet, positive clock hopping, and one positive
three-qubit boundary block. That three-body block has not been derived from
the two-body controls of PR9657. It has fixed support, rather than a sequence
of supplied target-unitary hopping bonds. Infinite blank sites remain an
infinite resource. A finite approximation has a finite horizon only.

## 1. Hamiltonian and conditional boundary scattering

On the one-head clock space l2(N0), let J>0 and

    h0=2J I-J sum(n>=0)(|n+1><n|+|n><n+1|),
    Pminus=(I-X1 X2)/2, Pplus=I-Pminus,
    H=K tensor I + I tensor h0 + w Pminus tensor |0><0|.       (1)

Nominally w=4J/3. Permit the explicit fault family J<=w<=5J/3;
there are no other faults in this theorem. K remains literally present with
its original coefficients. K commutes with all added terms. There is no
externally timed intervention during evolution.

In the Pplus old sector the clock is h0. In Pminus it is hw=h0+w|0><0|.
Put E(k)=2J(1-cos k), 0<k<pi. Direct substitution at n=0 and in the bulk gives

    phi_w(k,n)=(exp(-ikn)+r_w(k)exp(ikn))/sqrt(2pi),
    r_w(k)=-(w+J exp(ik))/(w+J exp(-ik)).                       (2)

These are bounded generalized eigenfunctions with energy E(k). In particular
r_0(k)=-exp(2ik). For real w, |r_w(k)|=1 on this open band. At k0=pi/2,

    r_0(k0)=1,
    r_(4J/3)(k0)=(-7-24i)/25=exp(-2i theta),
    R=Pplus+exp(-2i theta)Pminus=exp(-2i theta)W.               (3)

The scalar exp(-2i theta) is retained in the full isometry comparison.
Replacing the incident momentum by its opposite or silently conjugating the
reflection coefficient changes the operation.

For w>J there is also a bound state, proportional to (-J/w)^n, with energy
2J+w+J^2/w above the band. It is not omitted by assuming the physical input
has zero overlap with it: the initial comparison below bounds the complete
physical input's deviation from an exact continuum solution, hence also its
bound-state component. No completeness assertion excluding a bound state is
used.

## 2. Packet and an elementary uniform escape estimate

Take 0<sigma<=pi/6, k0=pi/2, and

    f(k)=sqrt(15)/(4 sqrt(sigma)) [1-((k-k0)/sigma)^2]
         for |k-k0|<=sigma, and zero elsewhere.

It is continuous, absolutely continuous on its support with zero endpoint
values, and L2-normalized. Its exact norms are

    F0=||f||_1=sqrt(15 sigma)/3,
    F1=||f'||_1=sqrt(15)/(2 sqrt(sigma)).                       (4)

For real s define clock vectors on n>=0 by

    a_s(n)=(2pi)^(-1/2) integral f(k) exp(-ikn-iE(k)s) dk,
    b_s^w(n)=(2pi)^(-1/2) integral f(k)r_w(k)exp(ikn-iE(k)s) dk,
    psi_s^w=a_s+b_s^w.                                       (5)

For any absolutely continuous g vanishing at the band endpoints, either
nonstationary phase kn+E(k)t or its negative has derivative magnitude at
least n+v t, where v=sqrt(3)J. Integration by parts gives, for t>0,

    |(2pi)^(-1/2) integral g(k)exp(i[kn+E(k)t]) dk|
      <= [||g'||_1+(2J/v)||g||_1]/[sqrt(2pi)(n+v t)].          (6)

Indeed |E''|<=2J and t/(n+vt)<=1/v; no monotonicity of E'' is needed.
For vt>=1, sum(n>=0)(n+vt)^(-2)<=1/(vt)^2+1/(vt)<=2/(vt).
Consequently the norm of this vector on n>=0 is at most

    [||g'||_1+(2/sqrt(3))||g||_1]/sqrt(pi v t).                (7)

This estimate holds for every t satisfying vt>=1, not only an asymptotic
sequence or time average.

For w in [J,5J/3] and k in [pi/3,2pi/3], the denominator
D=w^2+J^2+2wJ cos k is at least J^2. Differentiation of (2) gives

    |r_w'(k)|=2J |J+w cos k|/D <=11/3.                       (8)

For w=0 the derivative magnitude is2 and satisfies the same upper bound.
Define

    CA=F1+(2/sqrt(3))F0,
    CB=F1+(11/3+2/sqrt(3))F0.                                (9)

Then for every s,T with vs,vT>=1,

    ||a_s||<=CA/sqrt(pi v s),
    ||b_-T^w||<=CB/sqrt(pi v T),                              (10)

uniformly over the nominal plus sector w=0 and the admitted minus-sector
range [J,5J/3]. The norm in (10) is the entire half-line clock norm.

## 3. Normalization and exact dynamics without a spectral-completeness import

The synthesis map in (5) is bounded from L2 on the band to l2(N0), by
restriction of the two full-integer Fourier maps. E(k) is bounded. Thus
psi_s^w is norm differentiable and the directly checked eigenfunction
identity implies i d_s psi_s^w=hw psi_s^w. Since hw is bounded selfadjoint,

    psi_s^w=exp[-i(s-r)hw]psi_r^w.                            (11)

Its norm is constant. On the full integer line, Parseval gives ||a_-T||=1.
The part with n<0 tends to zero as T tends to infinity: write n=-m, m>=1,
and use (6)-(7) on phase mk+E(k)T. Therefore ||a_-T|| on n>=0 tends to1.
Equation (10) gives ||b_-T^w|| tending to0. It follows that

    ||psi_s^w||=1 for every real s.                           (12)

This argument establishes the needed normalized solutions without asserting
that their continuum span contains every physical clock state.

Fix T with vT>=1 and define the same ready clock for both old sectors,

    A_T=||a_-T||, chi=a_-T/A_T.                               (13)

Whenever CB/sqrt(pi vT)<1, A_T>=1-CB/sqrt(pi vT)>0 by (12).
The initial joint product state chi is independent of the old input. From
the reverse triangle inequality and (12),

    ||chi-psi_-T^w||<=2||b_-T^w||.                            (14)

The state on the left is the actually prepared input, including any bound
state overlap. Both compared vectors evolve under the same hw; this error
does not accumulate with elapsed time.

## 4. Complete output for every later time and static coefficient error

Let q_w(k)=r_w(k)/r_0(k). By (8), |q_w'(k)|<=17/3 throughout the band.
At fixed k, differentiation in w yields

    |partial_w r_w(k)|=2J sin k/D<=2/J                       (15)

for w in [J,5J/3]. Therefore, writing delta_w=w-4J/3,

    sup_band |q_w(k)-exp(-2i theta)|
       <=(17/3)sigma+2|delta_w|/J=:Delta.                    (16)

The w=0 sector is exactly q_0=1. Parseval followed by half-line restriction
shows ||b_s^w-exp(-2i theta)b_s^0||<=Delta. For s>=T, set

    B_s=||b_s^0||, beta_s=b_s^0/B_s.                          (17)

If CA/sqrt(pi vT)<1, then B_s>=1-||a_s||>0. Its scalar normalization is
positive real; beta_s retains the entire Fourier phase exp[-iE(k)s] and
reflection phase r_0(k). The reverse triangle inequality with (12) gives
|B_s-1|<=||a_s||. Combining (10), (14), (16) and (17),

    ||exp[-i(T+s)hw]chi-exp(-2i theta)beta_s||
      <=2CB/sqrt(pi vT)+2CA/sqrt(pi vs)+Delta                (18)

in the minus sector. In the plus sector replace the target scalar by1;
the same right hand side bounds it. Orthogonality of Pplus and Pminus now
gives the operator norm bound on the complete ready-input isometry,

    || exp[-itH](I_old tensor |chi>)
       - exp(-2i theta) exp(-itK)W tensor |beta_(t-T)> ||
       <= 2(CA+CB)/sqrt(pi vT)+(17/3)sigma+2|delta_w|/J,       (19)
    for every t>=2T.

Tensoring an arbitrary passive reference leaves this bound unchanged. For
any joint old/reference density, the trace norm error of the complete old,
clock and reference output is at most twice the right hand side, capped at2.
No subsystem is discarded. Uncoupled |00> source spectators can be tensored
onto both sides with zero change. This is persistent approximate completion
in the free-old interaction picture, with an escaping clock. It is not a
stationary total state, exact capture, selected Record, or apparatus reset.

An explicit sufficient choice for isometry error epsilon, 0<epsilon<=1, is

    sigma=3epsilon/68,
    |delta_w|<=J epsilon/8,
    T>=max{1/v, 16(CA+CB)^2/(pi v epsilon^2)}.               (20)

Then the three terms in (19) are at most epsilon/2, epsilon/4 and
epsilon/4. This also ensures the strict positive normalization conditions
above; each of CA/sqrt(pi vT), CB/sqrt(pi vT) is at most epsilon/4.
The band condition holds since sigma<=3/68<pi/6. The admitted fault lies
in [J,5J/3]. Nominal w needs no finite coefficient approximation when J is
chosen below. The packet width and incoming travel time still grow with
accuracy: CA+CB=O(epsilon^(-1/2)), hence T=O(J^(-1)epsilon^(-3)).
The coefficient tolerance in (20) is independent of how late t is read.
This conclusion is restricted to this one static boundary-strength fault,
not arbitrary clock disorder, old-K error, multi-head leakage or noise.

## 5. Positive qubit realization and actual local costs

For clock qubits c_n, write a_n=|0><1|_n and n_n=a_n^dagger a_n. Install

    H_clock=J n_0 + sum(n>=0) J[n_n+n_(n+1)
                               -a_(n+1)^dagger a_n-a_n^dagger a_(n+1)],
    H_boundary=w n_0 Pminus.                                (21)

Each hopping bond is positive, has norm2J, and has two-clock-qubit support.
The boundary term is positive with normw and support c_0, old1, old2.
Number is conserved. On the one-head sector (21) gives exactly (1).
On each finite-number sector H_clock is bounded by4J N; the orthogonal
direct sum of those bounded positive selfadjoint restrictions defines a
nonnegative selfadjoint operator. Adding bounded positive H_boundary and
bounded positive K preserves selfadjointness and nonnegativity. This is the
vacuum finite-excitation representation, not an infinite-density thermal
representation. The input is one-head; arbitrary clock input is not covered.

Each interior clock site has incident-block load4J. Clock0 has3J+w.
Each old site has added loadw, in addition to the unchanged literal K block
of norm3. A chain old1-old2-clock0-clock1-... embeds the support in Z3;
the boundary is a connected triple of diameter2, not an ordinary nearest-
neighbor two-body interaction. No unspecified gadget is included.

For the nominal dyadic choice J=3/16, w=1/4, the largest added load is
13/16 at clock0; old added load is1/4 and interior clock load3/4. The
boundary block is (I-Zc0)(I-X1 X2)/16. It is a single positive three-qubit
block, not four separately positive Pauli summands. All coefficients are
fixed dyadic values, independent of the desired accuracy. Under the admitted
fault range the boundary-site load remains<=7/8 and old added load<=5/16.
These added-load bounds do not include the old norm3 in an artificial cap1.

In the one-head sector, 0<=h_clock<=4J and 0<=H_boundary<=w, so
1<=H<=3+4J+w. For the nominal dyadic choice this is [1,4]. Static total
mean energy and variance are conserved; K is separately conserved. Clock
free energy and boundary energy need not separately be conserved. This
bounded modeled excitation energy does not price preparation, fabrication,
cooling, an infinite blank lattice or a physical identification of energy.

## 6. Readiness, limits and next checks

The ready vector (13) has infinite support but is a normal one-head state.
For every rho>0 it can be replaced by a normalized finite-support vector
within rho in norm. Exact unitary propagation then adds at most rho to
(19), uniformly for every later time. This existence statement is simply
density of finite-support vectors; it does not yet provide a finite
preparation algorithm or an explicit truncation size. Infinite blank tail
sites are still needed for the all-future construction. A fixed finite chain
can reflect the outgoing packet and is not covered by (19) at unbounded time.

The next independent checks must verify the incoming/outgoing convention,
the half-line boundary equation, normalization argument including the bound
state, full-output phase and old aging, tail constants and fault uniformity,
and the full-qubit positivity/load statement. A numerical finite-chain
experiment can falsify wrong formulas and test finite wavepackets; it cannot
certify the all-future or infinite-volume theorem. Strict two-body boundary
hardware, native incoming-packet preparation, arbitrary noise, finite reuse
and physical energy/Record identifications remain open.
