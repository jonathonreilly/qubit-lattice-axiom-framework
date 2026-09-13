# Spatial truncation of native energy dressing with a retained battery

Author derivation, 2026-09-13. Conditional-support; small exact author checks
cover the native/Fourier core and capped algebra; independent review remains
pending. This answers a specified approximation question
in the current-main ambient native generator. It does not derive a physical
bath, one-qubit-per-site apparatus, formation clock, or renewed blank sites.

## 1. Exact source and proposed change

Use the current-main ambient construction at base
cda8b1445e21b3908a0a520710e0dae57b7bc3a3:

- NATIVE_EDGE_RECORD_AMBIENT_GENERATOR_ERASURE_BOUNDED_THEOREM_NOTE_2026-09-07.md;
- NATIVE_EDGE_RECORD_OCCUPATION_FEEDBACK_SHARED_BATTERY_BOUNDED_THEOREM_NOTE_2026-09-07.md;
- NATIVE_EDGE_RECORD_MATTER_INSTRUMENT_AND_ENERGY_LEDGER_BOUNDED_THEOREM_NOTE_2026-09-05.md.

Their ordinary-composition native edge carrier, initial legal codes, fuel,
one-head preparation, hopping coefficients, energy gap, continuous coherent
battery and irreversible GKSL law remain supplied. They are not additional
framework axioms. In particular, grouping the source's co-located native and
fuel registers into finite-dimensional metric cells is a mathematical way to
apply locality estimates; it is not a derivation of a one-M2(C)-per-site
physical resource layout.

On a finite virtual nearest-neighbor graph of maximum degree d<=6, write

    A = sum_e q_e (h_e + Delta I),  ||h_e||<=J_*,
    h_e = a_e T_e,  |a_e|<=J_*.

Here q_e is live fuel, f_e lowers it, M_vw moves the one head from v to w,
Q_ez=(I+zZ_e)/2 is the physical native Record projector, and
J_vw=T_e n_v(1-n_w) is the native directed particle hop, of norm<=1.
The complete and feedback seeds respectively are

    B_(vw,z) = M_vw f_e Q_ez q_e,
    B^fb_(vw,z) = M_vw f_e Q_ez J_vw q_e.           (1)

Use one common battery L2(R,dE) throughout. In the unitary Fourier convention
exp(+i tau E), battery energy is -i partial_tau and its energy translation by
u is multiplication by exp(i tau u). The source energy lift is the multiplier

    Y_B(tau) = exp(-i tau A) B exp(i tau A).         (2)

The full-line generator has common free Hamiltonian H=A+E_B and jumps
L_B=sqrt(gamma) Y_B, with the actual sign-summed anticommutator. In feedback
this rate is not a scalar degree hazard. Full-line is a mathematical
comparison domain; the source's physical energy cap is addressed in Section8.

For each seed let X contain its physical metric support. Set
Omega_R={x:dist(x,X)<=R}, and let A_R contain exactly the interaction terms
of A whose full supports lie in Omega_R. Define the changed jump by

    Y_(B,R)(tau)=exp(-i tau A_R) B exp(i tau A_R).   (3)

Keep the same full free Hamiltonian H in the changed generator. Equation (3)
depends on a finite matter/fuel/head neighborhood and on the same battery.
No fresh battery is introduced at a jump. The battery still needs a physical
spatial placement/routing and a finite-dimensional approximation; these are
not consequences of finite matter support.

## 2. Exact algebra preserved by the truncation

On the invariant one-head subspace, E_vw=n_v^head q_e. Since A and every A_R
commute with all head and fuel projectors, the complete law obeys

    sum_z Y_(B,R)^dagger Y_(B,R) = E_vw.            (4)

For feedback the exact expression is instead

    exp(-i tau A_R) E_vw n_v(1-n_w) exp(i tau A_R), (5)

bounded between 0 and E_vw. Thus complete-law eligibility/rates remain exact.
Each individual feedback edge effect is a unitary conjugate of its bare
effect and has the same rank. Different edges use different A_R, so the
kernel of the TOTAL changed hazard and its dark probabilities must be
recomputed; neither is claimed unchanged. No identity-rate completion is
inserted into that feedback law.

Every whole h_e, each J_vw and every Q_ez commutes with the original total
particle number. Their truncated sums therefore do too. A spent fuel makes
its own seed vanish. Every remaining h_f and J_f commutes with Z_e at an
already spent/recorded edge e. The old guarded Record sectors and one-head
subspace remain invariant under (3).

Legal native code invariance includes loss terms. Each individual surviving
h_f preserves the source cycle code. The seed gives the correct target code,
including bridge parity and the order Q after J. In the target fuel block,
the selected q_e=0 removes h_e from A_R; all remaining terms commute Z_e.
Summing the two Q signs in Y_R^dagger Y_R therefore gives (4) or (5), each
preserving the source code. This proves both recycling and anticommutator
invariance. Individual unsummed losses need not preserve that code.

These statements hold for the full-line changed generator. They do not
identify its event probabilities with a nearest-neighbor Record-content law.

## 3. A finite-range locality estimate with explicit hypotheses

For a finite tensor system with interaction Phi_Z, assume diameter(Z)<=D
and define, for mu>0,

    J_mu = sup_x sum_(Z contains x)
                   |Z| ||Phi_Z|| exp(mu diameter(Z)) < infinity,
    v = 2 J_mu.

The bound is uniform under deleting interaction terms or restricting the
finite volume. Cell dimensions do not enter it. For disjoint supports X,Y,

    ||[alpha_t(B_X),C_Y]||
       <= 2||B||||C|| |X| exp[-mu dist(X,Y)]
                       (exp(v|t|)-1).             (6)

For clarity, the needed general estimate can be derived without assigning
unknown numerical constants. The norm-preserving commutator differential
equation gives the recursive inequality

    C_C(X,t) <= C_C(X,0)
        +2 sum_(Z intersects X) ||Phi_Z||
                           integral_0^|t| C_C(Z,s) ds,

where C_C(X,t) is the supremum of ||[alpha_t(B),C]||/||B|| over B supported
on X. Iteration produces interaction chains, each consecutive pair of
supports intersecting. Set K_xy=sum_(Z contains x,y)||Phi_Z||. Selecting an
intersection point at each link overcounts every chain positively, so the
chain sum at order n is bounded by sum_(x in X,y in Y)(K^n)_xy. The weighted
row norm of K is at most J_mu; the triangle inequality for distance then
bounds that sum by |X| exp[-mu dist(X,Y)] J_mu^n. Summing the factorial
time series from n=1 proves (6). This argument also applies to non-Hermitian
seeds and tensoring an arbitrary reference.

The recursion is established mathematical machinery; it is checked against
the proof of Theorem2.1, equations2.7-2.11, in Nachtergaele, Ogata and Sims,
[Propagation of Correlations in Quantum Lattice Systems](https://arxiv.org/abs/math-ph/0603064).
The specialization and constants above are derived here. No empirical
speed or physical formation-time axiom is taken from the locality theorem.

For the supplied ambient native interaction, the whole hopping has physical
diameter4. Each native edge cell belongs to at most11 endpoint-star terms.
A generous uniform choice is

    D=4,  J_mu <=132(J_*+Delta) exp(4mu).            (7)

This overcounts the grouped finite cell supports and also bounds sparse
subgraphs. The seed support contains at most14 of the supplied registers,
within radius2 of its selected edge midpoint. These estimates are sufficient,
not optimal physical resource counts.

## 4. The actual truncated conjugation, not an arbitrary local surrogate

Let b_R be the sum of ||Phi_Z|| over supports crossing the boundary of
Omega_R. Terms wholly outside commute with the entire A_R evolution of B.
Every crossing term has dist(X,Z)>R-D. A Duhamel comparison and (6) give,
for ||B||<=1, R>D and |tau|<=T,

    ||Y_B(tau)-Y_(B,R)(tau)|| <= epsilon_R(T),
    epsilon_R(T) = min(2,
       2|X| b_R exp[-mu(R-D)]
          [(exp(vT)-1)/v-T]).                       (8)

If v=0 the bracket has its continuous value zero. A useful coarser bound is
2|X| b_R T exp[vT-mu(R-D)]. To prove (8), interpolate between the two unitary
conjugations. The derivative is a conjugate of [A-A_R,alpha_s^(A_R)(B)].
Only crossing terms survive, and integrating their bound (6) gives the
displayed bracket. The minimum by2 follows from the two contraction norms.

The boundary sum is polynomial in R on this apparatus, independently of
total finite graph size. An explicit coarse bound for integer R>D=4 is

    b_R <=11(J_*+Delta)|X|
                   sum_(k=R-D+1)^R (4k^2+2).       (9)

Indeed every cut support has a point in Omega_R at distance greater than
R-D from X. Sum interaction norms over that boundary layer and overcount
its sites by the union of |X| cubic l1 annuli. A sphere of integer radius
k>=1 in Z3 has4k^2+2 sites. This yields O(R^2), with all constants supplied
above. Grouped co-located apparatus degrees do not add lattice sites to
the sphere count. Take suprema over seed supports for a common epsilon_R.

Unlike Haar-averaging a quasi-local operator, formula(3) preserves the seed's
unitary-conjugation algebra and its correct summed effects. This is why it
can define a trace-preserving changed generator with the same guards.

## 5. The retained battery has a calculable Fourier tail

Use the source family

    beta(E)=sqrt(2/w) sin(pi(E-b)/w), b<=E<=b+w,

and zero elsewhere, with w>0. Put k=pi/w. Direct integration gives

    beta_hat(tau) = exp(i b tau) k(1+exp(i tau w))
                        /[sqrt(pi w)(k^2-tau^2)].  (10)

The apparent poles at tau=+/-k are removable. For T>=2pi/w, its normalized
Fourier probability p(tau)=|beta_hat(tau)|^2 has tail

    p_T = integral_(|tau|>T) p(tau)d tau
           <=128pi/(27 w^3 T^3).                  (11)

For |tau|>=2k, |tau^2-k^2|>=3tau^2/4, so p(tau)<=64pi/(9w^3 tau^4).
Integrating both tails proves (11). No fitted tail exponent is used.
One may replace the right side by its minimum with1. Translating b changes
only the Fourier phase, not the tail or any locality estimate.

## 6. Complete generator comparison on the one-head domain

First restrict the input Fourier support to [-T,T]. Stack all directed-edge
and sign jumps into a single column L; let L_R be the corresponding changed
column. The supplied one-head subspace is crucial for the following estimates:

    ||L||,||L_R|| <=sqrt(d gamma),
    ||L-L_R||_(|tau|<=T) <=sqrt(2d gamma) epsilon_R(T). (12)

For the first bound, (4)-(5) sum to at most gamma d I in each source-head
block. For the second, each difference retains its source-head projector,
and at a fixed source v there are at most2d edge/sign labels. Their squared
norms add in the jump column; distinct source heads are orthogonal input
blocks. Thus no factor proportional to the total number of edges is needed.
Superpositions of head locations are included within this invariant domain.

For two jump columns C,D, writing the recycling map as a partial trace gives

    ||Diss_C-Diss_D||_diamond
        <=2(||C||+||D||)||C-D||.                   (13)

The recycling difference costs (||C||+||D||)||C-D||; the difference of the
two half anticommutators costs the same. These operator-norm estimates hold
after tensoring arbitrary references. The free Hamiltonian is identical in
the two generators and cancels in their difference.

Free evolution under A-i partial_tau translates Fourier support by physical
duration s; the jump multipliers never enlarge it. At time u the interval
is [-T+u,T+u]. Duhamel comparison, trace-norm contraction and (12)-(13) give
on the input band, for any s>=0,

    ||Phi_s-Phi_(R,s)||_diamond,input-band
        <=4 sqrt(2) d gamma s epsilon_R(T+s).       (14)

Finite volume A is bounded, while E_B is self-adjoint; bounded multiplier
jumps give the usual bounded dissipative perturbation of its unitary group.
Equivalently the interaction picture proves the Duhamel estimate on trace
class without differentiating a bandlimited input in energy. Both semigroups
are CPTP and preserve the stated head domain. All no-jump, dark, reached and
trapped probability is included; no conditional renormalization occurs.

Now supply the actual pure sine battery independently of arbitrary legal
matter/fuel/head input and reference. Its normalized Fourier truncation has
trace distance2sqrt(p_T) from the original packet. Applying both channels
and the triangle inequality yields the retained-output, ready-battery bound

    delta_R(s,T) = min(2,
       4 sqrt(2) d gamma s epsilon_R(T+s)
                           +4 sqrt(p_T)).         (15)

This includes the battery in the output and does not reset it between
events. It is a diamond-norm bound for the channel with that fixed battery
preparation, not for arbitrary unrestricted battery inputs. It also bounds
any final matter/Record marginal by partial-trace contraction. A sharper
discarded-battery bound is not silently reused for this retained problem.

For fixed w,s,gamma and local interaction parameters, choose
T=mu(R-D)/(2v)-s when positive and at least2pi/w. Equations(8)-(11) imply

    delta_R = O(R^3 exp[-mu(R-D)/2]) + O(R^(-3/2)). (16)

Thus the specified full-line generator admits finite matter-neighborhood
approximations, with an explicit volume-independent error on the one-head
domain. This neither proves an infinite apparatus process nor removes its
finite fuel depletion. Constants may be conservative and large.

## 7. Approximate global mean-energy account

The changed jumps do not exactly conserve H=A+E_B. Their precise defect is

    [H,Y_(B,R)](tau) = [A-A_R,Y_(B,R)(tau)].        (17)

To check the sign, -i partial_tau Y_R=-[A_R,Y_R], which cancels the local
part of [A,Y_R]. Only cut interactions contribute. Therefore on |tau|<=T
the defect norm is at most

    g_R(T)=2|X| b_R exp[-mu(R-D)](exp(vT)-1),       (18)

and at any tau it is at most2b_R. This uniform bound is finite for every R.
It also shows the changed bounded jumps preserve the first-energy-moment
domain; the following expectation identity may be obtained first on smooth
finite-moment vectors and then by finite-moment approximation.

For any Lindblad jump family,

    G_R^*(H)=1/2 sum_l
       [L_l^dagger[H,L_l]+[L_l^dagger,H]L_l].       (19)

This is again a Fourier multiplier. In a source-head block there are at
most2d terms, giving pointwise norm at most2d gamma g_R(T) inside the band
and4d gamma b_R outside. The diagonal Fourier probability evolves purely
by translation: for every bounded smooth scalar f(tau) with bounded derivative,
G_R^*(f(tau))=f'(tau), since all jumps and A commute with f. This identifies
the translated Fourier probability measure without assuming a pure current
battery state or a pointwise density-matrix kernel. Thus an
initially independent sine battery gives, even after matter-battery
correlations develop, at most p_T probability outside the translated band.

Integrating (19) through a horizon s gives the modeled mean-energy estimate

    |<H>_(R,s)-<H>_0|
       <=2d gamma s [g_R(T+s)+2b_R p_T].           (20)

For the same choice of T as Section6, this is
O(R^2 exp[-mu(R-D)/2])+O(R^(-1)). It controls mean global energy, not the
complete energy distribution and not the norm of the energy-defect operator
on all battery states. The exact source preserves that complete distribution;
the changed finite-neighborhood generator is an approximation to it.

## 8. Finite cap: what follows and what remains

For Delta>=J_*, 0<=A<=B_max=L(Delta+J_*). A product initial battery supported
in[b,b+w] gives exact total-energy support inside[b,b+w+B_max]. Exact source
energy conservation confines its battery, at every time, to

    [b-B_max,b+w+B_max].                           (21)

Choose b>=B_max and a cap containing this interval. On the source's invariant
safe domain its capped generator equals the full-line one. Equation(15)
therefore compares the full-line changed evolution with that physical capped
source, and implies at each fixed time s

    Prob_changed(battery outside cap) <=delta_R(s,T)/2. (22)

This is a final-time leakage bound, not a probability of ever crossing the
cap and not a theorem about a repeatedly monitored boundary. It does not by
itself prove that compressing every changed jump by that cap yields the same
error: cap projection convolves Fourier variables, and feedback has a
non-scalar loss that must be preserved. Section10 supplies a separate
comparison that evaluates errors on the exact source's safe states.

The inherited battery capacity in (21) is extensive in L and continuous in
energy. The volume-independent spatial approximation (15) does not turn it
into a fixed-size resource or an indefinitely renewed formation apparatus.

## 9. Decisive checks and remaining route

The small exact native/Fourier checker passes126 predicates covering the
Fourier sign/tail constant, head-degree eligibility, native Q-after-J order,
sign-summed effects, old-Record and number guards, and genuinely changed
local conjugation coefficients. On its actual four-edge native path, the
first changed Taylor order is3 for both complete signs and2 for the allowed
feedback sign. The other feedback sign is an identically zero bridge branch;
it is retained explicitly. See BLOCK03_CHECKS.json and CHECK_NOTES.md.
The capped comparison has its distinct47-predicate finite check described
after Section10. This does not replace review of the general proof.
The proof of (6)-(22) is analytical; a finite matrix scan cannot establish
its arbitrary-volume assertions. All scientific conclusions remain
conditional and author-proposed pending independent review.

This result addresses the ambient note's named spatial-truncation step.
Remaining work includes a finite-dimensional battery realization,
physical battery routing and bath, renewed fuel and blank sites, a continuing
matter regime, and a consistent nearest-neighbor Record-content law. It does
not decide whether a global coupled-history interpretation or local messages
are the appropriate framework interface identified in Blocks1-2. No axiom
amendment is forced by this construction or by its remaining obligations.

## 10. A capped changed generator without assuming its Fourier-tail invariance

Let P be the battery cap projector onto[0,C], containing(21), and let Q be
the common total-energy projector onto[b,b+w+B_max]. Then P Q=Q. The exact
source semigroup preserves Q, and every exact lifted jump and its adjoint
preserves Q. These statements follow from exact energy intertwining, not
from the approximate construction. All initially supplied legal system
inputs with the chosen battery satisfy rho=Q rho Q.

For feedback, compress every changed jump by the same cap:

    K_l=P L_(R,l) P,

and use its ACTUAL summed loss in the GKSL generator. For the complete law,
also include, per eligible directed edge, exactly one refusal jump with
positive factor

    F_(vw,R)=sqrt(gamma E_vw-sum_z K_(vw,z)^dagger K_(vw,z)), (23)

into the source's absorbing refusal copy. This is positive because the
uncompressed changed sign column has effect gamma E_vw by(4), and E_vw
commutes with the cap and local Hamiltonian. No such complement is added
to feedback. Both changed capped generators are CPTP on the same supplied
finite-volume system and continuous bounded-energy battery.

The parent's sign-summed code argument applies with A_R in place of A:
cap projection acts only on the battery, the target local Hamiltonian omits
the consumed h_e, and its energy projectors commute with Q_ez. The summed
loss therefore preserves source code, original N and guarded old Records.
Functional calculus preserves those same invariant subspaces for(23).
Each changed capped jump/refusal depends only on the finite neighborhood,
the battery cap and the inherited active/refused flag. This is not a local
physical placement theorem for that battery or flag.

Here is the required state-dependent comparison lemma. Stack the exact
capped core jumps in L and the changed capped core jumps in K. On the
one-head domain, ||L||,||K||<=ell=sqrt(d gamma). Write Delta_col=K-L. On an
exact source state rho(u), set S=sqrt(rho(u)). Exact safe support implies

    L S=L_full S,
    Delta_col S=P (L_R-L_full) S,
    Delta_col^dagger L S
        =P (L_R-L_full)^dagger L_full S.           (24)

The P on the column output is understood componentwise. In the last identity
the intermediate cap disappears because each exact L_full maps Q into Q.
Let

    q_R(s,T)=min(2,sqrt(2 epsilon_R(T+s)^2+4p_T)),
    e=ell q_R(s,T).

The full-line differences are multipliers, so(12), the exact translated
Fourier marginal, and the global column bound2ell imply uniformly for
0<=u<=s

    ||Delta_col S||_2 <=e,
    ||Delta_col^dagger L S||_2 <=ell e.             (25)

These are Hilbert-Schmidt norms, with arbitrary reference included. They
use the Fourier marginal of the EXACT safe source state only. No claim is
made about the Fourier tail of the repeatedly capped changed state.

Expand the changed loss:

    K^dagger K-L^dagger L
      =L^dagger Delta_col+Delta_col^dagger L
                                      +Delta_col^dagger Delta_col.

Since ||Delta_col||<=2ell, equations(25) bound its product with S by4ell e.
The recycling difference on rho has trace norm at most2ell e. The two half
anticommutators together therefore cost at most4ell e. Thus the feedback
generator difference on each exact source rho(u) costs at most6ell e.
Applying Duhamel, with the changed CPTP semigroup after the difference,
gives the capped, retained-output ready-battery bound

    delta_cap^fb(s,T)=min(2,6d gamma s q_R(s,T)).    (26)

For the complete law, its total loss including refusal is exactly
gamma sum_(vw) E_vw in BOTH generators, so the anticommutators cancel
identically. The exact refusal vanishes on Q. The changed refusal mass on
an exact source state is

    sum_(vw) Tr(F_(vw,R) rho F_(vw,R)^dagger)
      =||(I-P)L_R S||_2^2
      <=||(L_R-L_full)S||_2^2 <=e^2.               (27)

Here the complete uncompressed columns have the same eligibility effect,
and exact L_full S lies inside the cap. Adding this positive output mass
to the core recycling comparison gives the stronger complete-law bound

    delta_cap^complete(s,T)
       =min(2,d gamma s[2q_R(s,T)+q_R(s,T)^2]).     (28)

All intermediate correlations, no-jump loss and refusal outcomes are retained
in(26)-(28). These bounds compare whole unconditional channels and do not
control every normalized rare trajectory. They scale as O(R^(-3/2)) plus
the exponential-boundary term under the choice of T in Section6, with no
factor growing with graph volume on the one-head domain. They solve the
cap-projection issue for the supplied finite-volume laws, while preserving
feedback's actual summed loss.

For these capped models the common modeled total energy, including the
refusal copy, lies between0 andB_max+C. Thus trace-distance comparison also
gives

    |<H>_(changed,s)-<H>_(source,s)|
        <=(B_max+C) delta_cap/2.                  (29)

This bound has an extensive resource prefactor. It does not assert exact
energy-distribution conservation of the changed model. The uncapped
volume-independent mean-energy estimate(20) is a separate statement; its
proof must not be transferred through repeated cap projections.

## 11. Exact finite cap witness and a false shortcut

The dedicated check uses an actual native two-edge path, with input
A_in=3T0+4T1+10I and output A_out=4T1+5I. Their distinct energies are
{5,10,15} and{1,5,9}. For a local subinteraction take A_inR=3T0+5I,
A_outR=0, with input energies{2,5,8}. This choice tests the cap algebra;
it is not asserted to be a metric-R>D truncation on this tiny graph.
Polynomial spectral projectors and literal shifts on a padded0..32 energy
ladder construct every operator exactly. The input is the source energy5
state with battery energy12, hence total energy17. Its exact safe battery
support lies in[2,16], inside the cap[0,16]. The discrete sharp-energy input
does not stand in for the continuous sine packet of the general bounds.

Before computation, the native two-edge algebra predicts complete-law
refusal mass9/25. It predicts feedback source, uncompressed changed and
capped changed rates1/2,17/50 and8/25. The exact check confirms all four
values, the actual refusal projector, complete output mass, loss expansion
and both state-weighted bounds used in Section10.

It also preserves a counterexample to an unwarranted shortcut in the first
checker version. In feedback the measured forward squared column error is
21/25, but the squared adjoint-on-exact-output error is1. Thus one cannot
set the theorem's common e equal to the measured forward error alone.
Equations(24)-(25) instead bound BOTH quantities from the uniform Fourier-
fiber estimate. The corrected check retains that failed stronger condition,
checks the two premises separately, and verifies the resulting loss bound.
No scientific target or event probability was changed to obtain a pass.
See BLOCK03_CAP_CHECKS.json, its log and CHECK_NOTES.md for exact evidence.
