# Independent occupation completion and birth-backaction check

This packet was derived and executed from the neutral supplied definitions,
before reading either new author note, either author checker, their outputs,
or the campaign checkpoint. `READ_BOUNDARY.json` records that boundary.
The model has vacancies and occupied internal states; it does **not** impose
permanent partner adjacency after a pair birth.

**Main results.** For finite-dimensional occupied content, the monitored
completion conjecture is true under the stated connected-hopping and
positive-birth hypotheses. It has a model-dependent exponential survival
bound and finite mean. This does not imply a unique stationary internal
state. With H0=0, the square dark-state completion mean is

    1/d + 3/(2 beta) + 1/(beta+d) + 1/[2(beta+2d)]
      + (beta+2d)/(16 kappa^2).                          (1)

Without monitoring the specified N4 torus amplitude is dark, and a nonzero
dark component is accessible from the all-vacant state when births are
positive on the displayed finite matching (in particular on all nearest
neighbor edges). Finally the three-state clock mean from A is

    2/beta + beta/(4 kappa^2).                           (2)

All exact computational controls passed on their first execution. Scope and
the difference between dark-state existence and accessibility are important
parts of these conclusions.

## 1. Finite-model statement and conventions

Let G=(V,E) be a finite connected simple graph. At each vertex use
`C|0> direct-sum K`, with **1<=dim K<infinity** for the finite-model theorem
proved here. Set q_x=|0><0|, n_x=I-q_x. The Hamiltonian is

    H=H0+sum_{xy in E} kappa_xy sum_a
                 (|0,a><a,0|+|a,0><0,a|),

where kappa_xy are finite real nonzero numbers and H0 is Hermitian with
[H0,n_x]=0 for every x. The sum over a is an orthonormal basis of K; its
value is the content-preserving vacancy swap and is basis independent.

Use the Lindblad convention

    L(rho)=-i[H,rho]+sum_j [J_j rho J_j^dagger
                             -(1/2){J_j^dagger J_j,rho}].

Monitoring jumps are sqrt(d_x)n_x, with 0<d_x<infinity. Birth channels on a
nonempty F subset E are

    J_(e,alpha)=sqrt(beta_(e,alpha)) |b_(e,alpha)><00|,

acting as identity off e. Each b is a unit vector in K tensor K, including
arbitrary entangled vectors. Require nonnegative channel rates with finite
positive total `0<beta_e=sum_alpha beta_(e,alpha)<infinity` for e in F.
The finite-dimensional birth CP map can equivalently use finitely many
Kraus operators. No locality of H0 beyond occupation preservation is needed
for this finite-graph argument.

Let P be the all-occupied projector, restricted to the invariant even-vacancy
sector, and let Q be its complement within that sector. For any initial
density supported there define

    S_rho(t)=Tr Q rho(t).

P is absorbing for the occupation dynamics: hops vanish on it, H0 preserves
it, monitoring restricts to scalars, and birth jumps annihilate it.
Moreover `d Tr P rho(t)/dt=sum_j Tr J_j^dagger P J_j rho(t)>=0`.
The nonfull block evolves by a completely positive trace-nonincreasing
semigroup T_t, independently of initial full/nonfull coherences:

    Q rho(t) Q=T_t(Q rho(0) Q).

Thus S is a genuine absorption survival function. Its integral is the mean
absorption time. If a trajectory description is wanted for initial
coherences between different even vacancy counts, an initial measurement of
the total count leaves these occupation statistics unchanged; trajectories
then have definite counts, and each birth lowers vacancy count by two.

For every fixed t0>0 there is a model-dependent number 0<r(t0)<1 such that

    S_rho(t) <= r(t0)^floor(t/t0) S_rho(0),
    integral_0^infinity S_rho(t) dt
                         <= t0 S_rho(0)/(1-r(t0)).       (3)

In particular this supplies an exponential bound with exponent
`-log r(t0)/t0` and prefactor `r(t0)^-1 S_rho(0)`. There is no claim that
these constants are uniform over volume, detunings, monitoring strength,
birth intensity or graph families.

## 2. Why occupation monitoring gives completion

The monitoring dissipator has the exact alternative form

    d_x [n_x rho n_x-(1/2){n_x,rho}]
      =(d_x/2)[n_x rho n_x+q_x rho q_x-rho].              (4)

It therefore has an unraveling consisting of occupation measurements with
outcomes n_x and q_x, at positive Poisson rate d_x/2. This does not replace
finite monitoring by an infinite-measurement or classical-hopping limit.
It is an exact representation of the same Lindblad generator.

For a vacancy set A define its occupation projector

    P_A=product_(x in A) q_x product_(x notin A) n_x.

Products of the allowed measurement outcomes give P_A. They resolve vacancy
patterns but act as identity on the internal color space of every occupied
site. Thus this argument allows arbitrary internal entanglement, including
entanglement correlated with the vacancy pattern; it does not replace
internal states by classical labels.

If A and A' differ by exchanging a vacant and an occupied endpoint of one
edge e, then

    P_A' H P_A=kappa_e U_(A',A),                        (5)

where U is a unitary identification of the two occupied-content fibers.
There is only one graph edge producing this change, so no cancellation of
different edge amplitudes occurs. H0 contributes no off-pattern term.
Consequently a short coherent interval followed by occupation measurements
can move any nonzero internal state from A to A' with positive probability.
More explicitly, for the no-jump propagator exp(Kt), whose extra loss terms
are occupation diagonal,

    P_A' exp(Kt) P_A=-i t kappa_e U_(A',A)+O(t^2).

The leading term is injective on the internal fiber, irrespective of its
state or entanglement.

On a connected graph the graph of h-element vacancy sets under these moves
is connected whenever 0<h<|V|. One elementary proof is that edge
transpositions on a connected graph generate all vertex permutations; their
action on h-subsets is transitive, and transpositions of equal occupations
can simply be ignored. No bipartite or perfect-matching hypothesis is used.

Fix one birth edge e0 in F and one positive channel on it. Any h>=2 vacancy
pattern can be moved to a pattern containing both endpoints of e0. If all
sites are vacant this is already true. On that fiber the birth jump is an
injective map of norm factor sqrt(beta_(e0,alpha)): it tensors the unchanged
remaining internal state with the normalized, possibly entangled born pair.
It lowers h by two. Repeating this argument gives a finite sequence of
occupation projections, nonzero coherent hops and births leading to P from
every nonzero even nonfull state.

The formal zero-waiting products used to identify this sequence are not
assigned a positive probability themselves. Instead their nonzero leading
Taylor coefficients show that the corresponding quantum-trajectory Kraus
product is nonzero on an open set of small **positive** waiting times.
All selected monitor and birth channels have positive rates. The sequence
can be fitted inside any prescribed t0>0, so every initial nonfull density
has strictly positive absorption probability by t0. This also proves that
there is no nonzero nonfull invariant support under all the occupation
measurements, hopping and birth maps.

Finally the normalized density matrices on the finite-dimensional Q space
form a compact set, and survival is continuous and linear in the initial
density. Therefore

    r(t0)=max_(rho>=0,Tr rho=1,supp rho subset Q) Tr T_t0(rho)
         =||T_t0^*(I_Q)||_op < 1.

The semigroup property proves (3). This supplies the missing uniformity over
all internal states at a fixed finite model; a pointwise accessibility
argument alone would not justify that uniform bound in an infinite state
space.

## 3. Hypotheses, exceptions and internal-state scope

- **Parity matters.** Pair births remove two vacancies, and the other terms
  preserve the count. Odd-vacancy states cannot reach full occupation. An
  all-vacant initial state is in the theorem only when |V| is even.
- **Connectivity is that of nonzero vacancy hopping.** Disconnected hopping
  components, zero indispensable couplings, or birth-free inaccessible
  components can trap vacancies. All nonzero edge amplitudes and connected G
  are convenient sufficient hypotheses, rather than a classification of
  every weaker connectivity condition.
- **Monitoring is occupation resolving.** Positive d_x at all sites is
  sufficient, and removing monitoring invalidates the universal statement,
  as the explicit dark examples show. It is not necessary at every vertex
  of every special graph: on a two-site graph an empty pair can fill directly
  without any monitoring. No minimal monitoring-set classification is
  claimed. Monitoring only total number would not break position-space
  interference inside a fixed-count dark state.
- **H0 must not cancel the stipulated hopping.** If local occupation
  preservation is dropped, choosing H0=-H_hop leaves a zero total Hamiltonian
  and traps separated holes despite monitoring. Commutation with total
  number alone is insufficient for the stated proof.
- **Birth positivity and normalization matter.** With no active birth edge
  there is no completion. A state-dependent birth channel that vanishes on
  some internal states is a different premise; the supplied normalized
  |b><00| channels have no such internal kernel on a vacant pair.
- **Finite-model scope is explicit.** If K is intended to be infinite
  dimensional, an arbitrary self-adjoint H0 and unspecified channel sums
  need additional well-posedness and uniform estimates. The compactness
  proof above does not establish a uniform exponential bound in that
  setting. Finite dimensionality is a sufficient route; it is not asserted
  necessary for every separately controlled infinite-dimensional model.
- **No permanent partner constraint is imposed.** Born records may separate
  under the given vacancy hopping. Importing the former perfect-matching
  requirement would change this occupation model. The exact star-graph
  control below deliberately has no perfect matching.

Completion is an occupation statement, not a unique internal equilibrium.
On full occupation the generator reduces to `-i[H0 restricted to P,rho]`.
For H0=0 every full internal density is stationary. For admissible nonzero
H0 it may keep evolving unitarily. Occupation monitoring does not directly
dephase the occupied internal space. The theorem allows arbitrary
entanglement; it does not assert that the entire evolution preserves any
particular initial entanglement measure.

The exact colored two-site control uses an entangled born pair
`(|1,1>+|2,2>)/sqrt(2)`. It verifies J^dagger J=q_0 q_1 and that monitoring
and hopping annihilate this full-state density. A local occupied-content
flip in H0 commutes with both n_x yet moves that density nontrivially, with
full-occupation probability identically one. This directly checks the
internal-state boundary.

## 4. Four-cycle dark-state mean

For this calculation take **H0=0**, one occupied color, four undirected
cycle edges, uniform hopping kappa>0, birth rate beta>0 on each edge, and
monitoring jump sqrt(d)n_x at each vertex with d>0. A different occupation
diagonal H0 generally changes the requested mean.

Use two-hole states O0={0,2}, O1={1,3}, and A_j={j,j+1} modulo four. The
hopping graph on these six states is the complete bipartite graph between
the two O states and the four A states, with matrix element kappa. Each A
state has total birth hazard beta; each O state has zero hazard. The initial
state is (O0-O1)/sqrt(2).

Write p for total O population, a for total A population, c=rho_(O0,O1),
r1=rho_(A_j,A_(j+1)), r2=rho_(A_j,A_(j+2)), and
y=Im rho_(O_i,A_j). The relevant symmetry-invariant density has O diagonal
p/2, A diagonal a/4, real c,r1,r2 and common imaginary O-to-A entry i y.
The exact killed equations are

    p'  =-16 kappa y,
    a'  = 16 kappa y-beta a,
    c'  =-8 kappa y-2d c,
    r1' = 4 kappa y-(beta+d)r1,
    r2' = 4 kappa y-(beta+2d)r2,
    y'  = kappa[p/2+c-a/4-2r1-r2]-(beta/2+d)y.           (6)

Initial data are (1,0,-1/2,0,0,0). The dephasing rates in (6) follow from
`-(d/2) sum_x [n_x(A)-n_x(B)]^2 rho_(A,B)`; no alternate factor-of-two
convention is used. A direct symbolic six-by-six density calculation in the
checker verifies this closure against the un-lumped Hamiltonian and losses.

By the completion proof all six variables decay to zero. Integrating (6)
gives

    integral y=1/(16 kappa),       integral a=1/beta,
    integral c=-1/(2d),
    integral r1=1/[4(beta+d)],    integral r2=1/[4(beta+2d)].

The integrated y equation then gives (1) for `integral(p+a)`. At unit rates
the mean is 161/48. It diverges as 1/d when monitoring disappears, and also
grows at large d or beta through the Zeno terms. Positive monitoring and
positive birth therefore do not imply monotone speedup as those rates grow.

## 5. Full finite-Liouvillian and premise-removal controls

The independent checker constructs the full one-color four-site Hilbert
space of dimension 16, including both parity sectors, and its complete
256-by-256 Liouvillian. Trace preservation is checked on this full matrix.
The unit-rate matrix, with 1,337 nonzero entries, is stored in
`C4_FULL_LIOUVILLIAN.json`; this is not a simulation or a fit to (6).

For three separately chosen positive parameter triples, the two-hole mean
obtained by directly inverting the killed Liouvillian agrees exactly with
(1). The triples and answers are:

    (kappa,beta,d)=(1,1,1):             161/48,
    (2/3,5/4,7/5):                    22960943/7693056,
    (2,3/2,1/4):                      1311/224.

The checker also solves K^*(T)=-I on the complete even nonfull Hilbert space
and certifies T>0 by all exact leading principal minors. Thus it checks all
initial density matrices in that finite transient space, rather than only
the displayed dark initial state. At unit cycle rates, Tr T=323/24 and
Tr T^-1=1908131/461426. These give, for example, the explicit valid bound

    S(t) <= (Tr T)(Tr T^-1) exp[-t/(Tr T)] S(0).

Indeed V(t)=Tr T rho_Q(t) obeys V'=-S<=-V/(Tr T), while
S<=Tr(T^-1)V. The empty-cycle mean at these unit monitored rates is 7/4.

On the four-vertex star K1,3, with unit hopping/monitoring and births on only
one edge, the same exact positive-mean-operator certificate succeeds. Its
empty-state mean is 4185/376. This tests both the single-edge birth claim
and the absence of a perfect-matching requirement.

The full generator separately verifies the following stationary traps:
the square dark density with d=0; a mixture of opposite-hole states when
effective hopping is zero; and the uniform one-hole density in the odd
sector. They are premise-removal controls, not counterexamples to the
stated monitored theorem.

There is an important reachability control: on the **unmonitored** square,
the dark projector is conserved by the full adjoint Liouvillian and has zero
overlap with the all-vacant state. Each first pair birth produces an adjacent
hole state orthogonal to it. Thus this square dark state is not an
empty-start trapping witness. `reachability_control.py` verifies that exact
adjoint identity. Existence of a dark initial state alone is insufficient.

## 6. Unmonitored N4 torus: darkness and empty-start access

Here use one occupied color, H0=0, uniform real nonzero kappa, no monitoring,
and independent contact-birth Lindblad channels. The accessibility argument
below requires positive births on a particular displayed set of 31 edges;
positive rates on all nearest-neighbor edges suffice. Darkness itself does
not require all those rates.

For distinct torus vertices x,y define

    f({x,y})=sin[pi(y1-x1)/2] sin[pi(y2-x2)/2].

Both sine factors change sign upon exchange of x,y, so f is a well-defined
unordered-hole amplitude. It vanishes on every nearest-neighbor pair and
on x=y. It has 512 nonzero entries, each +-1, hence squared norm 512.

For the free two-hole hopping operator, the first two coordinate sums have
cos(pi/2)=0 and the third has cos(0)=1. Thus Hf=4 kappa f. Removing collision
terms to impose hard-core exclusion does not change this identity because
the omitted diagonal amplitudes vanish. The independent checker evaluates
all 2,016 unordered pairs and obtains an exactly zero eigen-residual.
Since every contact amplitude is zero, every pair-birth J annihilates f.
Its normalized projector is therefore a stationary dark state of this
unmonitored model, even though its Hamiltonian eigenvalue need not be zero.

To establish accessibility from all vacancies, begin with the z-directed
perfect matching pairing z=0 with z=1 and z=2 with z=3 in each column.
Along the alternating path

    000 -- 001 -- 011 -- 010 -- 110 -- 111

delete its three matching edges and insert its two intervening edges. The
result is a 31-edge matching covering all vertices except 000 and 111.
All its edges are nearest-neighbor edges. The checker records the full edge
list and verifies disjointness and coverage. The remaining basis hole state
has f=1, so its squared overlap with the normalized dark state is 1/512.
Choosing opposite-parity holes here avoids an unjustified near-perfect
matching claim for a same-parity pair.

Perform births on these 31 distinct edges in a prescribed order. In the
zero-waiting limit their bare jump product maps the empty state to exactly
that basis hole state. The actual proof uses small positive intervals, not
events of zero waiting time. To make it quantitative, let

    R=sum_e beta_e q_x q_y,
    K=-iH-R/2,
    M=192 |kappa|+(1/2)sum_e beta_e.

Then ||K||<=M and exp(Kt) is contractive. For the ordered sequence of m=31
bare jumps, each of norm one, with successive waiting times in (0,delta),
the vector differs from its zero-waiting limit by at most
`m M delta exp(M delta)`. Choose

    delta=1/[4 m e M sqrt(512)].

Its dark amplitude is then at least 1/[2 sqrt(512)], after factoring out
the product of square roots of the 31 birth rates. These trajectory-time
intervals have positive measure. On the two-hole sector the dark projection
is preserved by the subsequent no-birth propagator, up to its phase.
Consequently

    Prob_empty(no eventual completion)
       >= delta^31 (product_(selected edges) beta_e)/(4*512) > 0. (7)

This deliberately crude lower bound establishes access to a **component**
of the dark subspace. It does not claim exact deterministic preparation of
the pure dark vector. It uses the specified separate contact-birth channels,
not a different coherently summed birth operator. It makes no claim of
accessibility for an arbitrary single active birth edge or arbitrary
multicolor pair states. The one-color, all-positive-contact case is already
a countercontrol to removing monitoring from the universal completion claim.

As an additional exact check, unit occupation monitoring initially decreases
this dark state's self-overlap at rate 31/16: its vacancy marginal at each
site is 1/32. Monitoring therefore does not preserve this dark density.

## 7. The three-state coherent first-birth clock

Take H=kappa(|A><B|+|B><A|), J=sqrt(beta)|F><B|, initial A, and no other
channels. On the unabsorbed A,B subspace put p=rho_AA, q=rho_BB and
y=Im rho_AB. The exact equations are

    p'=-2 kappa y,
    q'= 2 kappa y-beta q,
    y'=kappa(p-q)-(beta/2)y.

For beta>0 and kappa!=0 the state is absorbed. Integrating gives
`integral y=1/(2 kappa)`, `integral q=1/beta`, and
`integral p=1/beta+beta/(4 kappa^2)`, yielding (2). A separately assembled
complete three-state Liouvillian and its killed block verify the expression
symbolically. At unit rates it is 9/4. If beta=0 or kappa=0, the first-birth
time from A has infinite mean. The strong-birth term is a Zeno delay, so the
mean is not obtained by assigning a constant effective vacancy hazard.

## Evidence and read limits

`check.py`, `color_control.py` and `reachability_control.py` are independently
written. Their complete results, stdout, stderr and timestamped command
receipts are preserved. The latter control explicitly reuses only the
first independent checker's finite generator constructor, with its hash in
the receipt. All three executions passed first time; no failed attempt was
discarded. No author code, result or current campaign checkpoint was read.
No external theorem was imported; the completion proof uses finite operator
algebra, a quantum-trajectory expansion and compactness, with its hypotheses
stated above. The initial task definitions and read boundary, rather than an
unopened author source, are the source of this pre-comparison calculation.

This report establishes the bounded supplied-model results above. It does
not assign a physical microscopic interpretation, select the dynamics from
axioms, provide a volume-uniform completion bound, or confer publication or
formal audit status. Author-source comparison remains a separate next step.
