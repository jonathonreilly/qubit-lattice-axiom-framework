# Goal

Source/Eta Block 19 executes the post-Block18 panel's 4-1 choice:
classify one bounded microscopic QND repeated-interaction family before moving
to the action/transfer selector. The independent preregistration attack found
that the first packet's arbitrary orbit-controlled hazard family made
nonuniqueness true by definition. That family is now only an outer control.
The terminal-bearing target is the finite relation-factor Hamiltonian grammar
below.

No Block19 target runner or cache existed or executed before this corrected
support packet was committed. The committed initial packet remains provenance;
this file and PREFLIGHT_SUPPORT_CORRECTION.md supersede its conflicting
family, finite-collision, QND, and product-limit language.

## Exact target contract

| field | corrected frozen contract |
|---|---|
| Positive construction target | PAIR-FACTOR-QND-WEAK-COLLISION-REALIZES-PERMANENT-RECORD-GENERATOR |
| Conditional algebraic result | MATCHING-FACTOR-ANSATZ-REALIZES-SUPPLIED-KERNEL-WITH-HAZARD-PROPORTIONAL-TO-Z |
| Eligible narrow terminal | PAIR-FACTOR-QND-WEAK-COLLISION-REALIZES-MARK-KERNEL-RECORDED-NEIGHBOR-GAIN-UNDERSELECTED |
| State carrier | At every site, an auxiliary orthogonal seven-state pointer with one blank state and six states labeled by D={+-e_1,+-e_2,+-e_3}. It is not identified with the physical strict one-qubit M_2(C) carrier. |
| Condition carrier | Six nearest-neighbor pointer observables, read through their commuting label projectors. QND means conservation of those projectors and diagonal labels, not identity of an arbitrary coherent neighbor marginal. |
| Supplied conditional law | p_f(r)=2^(m_f(r))/Z(r), Z(r)=sum_g 2^(m_g(r)). The ratio and its factor of two are downstream inputs, not derived axiom content. |
| Core microscopic grammar | One common positive real triple (g,a,b); one identical three-relation factor per neighbor (blank, same label, other recorded label); one fresh seven-state vacuum ancilla; one target plus six controls; Hermitian star Hamiltonian; no profile/orbit lookup coefficient, higher-body profile gate, postselection, or simultaneous overlapping-unitary claim. |
| Classification variable | beta=b^2 after the supplied mark law fixes (a/b)^2=2; g^2 is one common rate scale. The blank relation coefficient is fixed to one as factorization gauge. |
| Equivalence relation | Only multiplication of every generator intensity by one state-independent positive constant. A factor depending on profile, occupancy, label, site, or history is not a clock-unit quotient. |
| Collision protocol | At each finite-volume mesh sweep, every site is visited once in an arbitrary permutation and receives a fresh vacuum ancilla; permutations may vary between sweeps. Ancilla preparation, disposal, cadence, and the weak scaling U_delta=exp(-i sqrt(delta)H) are declared imports. |
| Required bridge | Exact local unitary and fresh-vacuum Kraus channel; exact pointer-label QND and target lock on the physical input sector; conditional mark law at finite delta; first-order quantum and diagonal generators; arbitrary-order finite-volume product limit; finite and local-infinite pure-Record dynamics; a clock-free local Record-order discriminator. |
| Outer control | Arbitrary proper-cubic orbit-controlled h(r) rotations may be classified only as a structural dilation control. Their many free coefficients cannot be used as evidence that the core pair-factor grammar is underselected. |
| Forbidden conclusions | No strict-M_2 encoder, autonomous bath, physical clock, compound-event selector, gravity source, full instrument uniqueness, axiom edit, audit verdict, obligation retirement, or TOE percentage movement. |

The family is selected as a bounded physics ansatz; Block19 does not derive the
ansatz from the minimal axioms. The campaign asks what the ansatz actually
fixes once the conditional mark kernel is supplied.

## Pointer profiles and supplied mark kernel

Let

~~~
P_y^rec = sum_(g in D) P_(y,g),
P_(y,other(f)) = P_y^rec - P_(y,f).
~~~

For a classical neighbor profile r, define

~~~
n(r)   = number of recorded neighbors,
m_f(r) = number of neighbors carrying label f,
w_f(r) = 2^(m_f(r)),
Z(r)   = sum_g w_g(r),
p_f(r) = w_f(r)/Z(r).                                   (1)
~~~

There are 7^6=117,649 ordered profiles. Proper-cubic covariance rotates the
six neighbor slots and the six nonblank labels simultaneously.

## Frozen relation-factor Hamiltonian grammar

For target site x, fresh ancilla a_x, and candidate label f, define

~~~
D_(x,f)(a,b)
  = product_(y nearest x)
      [P_(y,bottom) + a P_(y,f) + b P_(y,other(f))],

A_(x,f)
  = g (|f><bottom|)_x tensor (|f><0|)_(a_x) D_(x,f)(a,b),

H_x(a,b,g) = sum_f [A_(x,f) + A_(x,f)^dagger],

U_(x,delta) = exp[-i sqrt(delta) H_x].                   (2)
~~~

The allowlist in (2) is the complete core grammar: finite sums, products, and
adjoints of the displayed target/ancilla transitions and one-neighbor
orthogonal relation projectors, with the same positive real a, b, and g at
every site and label. A hidden orbit/profile table, an extra common profile
polynomial, or a higher-body control is outside the core family.

On profile r,

~~~
c_f(r) = g a^(m_f(r)) b^(n(r)-m_f(r)),
h_(a,b)(r) = sum_f c_f(r)^2.                             (3)
~~~

Let

~~~
|B> = |bottom>_x |0>_(a_x),
|chi_r> = h_(a,b)(r)^(-1/2) sum_f c_f(r)|f>_x|f>_(a_x).
~~~

Every other neighbor label is a control. On
span\{|B>,|chi_r>\}, H_x is sqrt(h_(a,b)(r)) sigma_x,
and it annihilates the orthogonal dark space. Hence

~~~
U_(x,delta)|B>
  = cos(sqrt(delta h)) |B>
    - i sin(sqrt(delta h)) |chi_r>.                      (4)
~~~

This is the required explicit unitary, not generic Stinespring rhetoric.

## Exact fresh-vacuum channel and scope of QND

Tracing the fresh ancilla after (4) gives, on profile r,

~~~
K_0(r,delta)
  = P_rec + cos(sqrt(delta h(r))) P_bottom,

K_f(r,delta)
  = -i [c_f(r)/sqrt(h(r))]
       sin(sqrt(delta h(r))) |f><bottom|.                (5)
~~~

The exact completeness identity is

~~~
K_0^dagger K_0 + sum_f K_f^dagger K_f = I.              (6)
~~~

The exact finite-collision probabilities are

~~~
P_delta(bottom -> f | r)
  = sin^2(sqrt(delta h(r))) c_f(r)^2/h(r),

P_delta(bottom -> bottom | r)
  = cos^2(sqrt(delta h(r))).                             (7)
~~~

Thus the conditional mark law c_f^2/h is exact whenever a collision writes,
while the total write probability is sinusoidal. It is not exactly
delta h. For all-profile nonzero conditional probabilities one may take a
shared interval 0<delta h_max<pi^2; the generator limit only requires
delta -> 0.

The fresh-vacuum induced channel fixes every already recorded target:

~~~
K_0 P_rec=P_rec,       K_f P_rec=0.
~~~

The Hamiltonian commutes with every neighbor label projector, so those pointer
observables and all diagonal Record labels are nondemolished. It can entangle
different coherent profile sectors, and H_x can erase |f>_x|f>_(a_x) for a
nonvacuum ancilla. Therefore neither complete neighbor-state identity nor an
ancilla-state-independent target lock is claimed. Append-only permanence is
an exact statement about each collision boundary under the frozen fresh-vacuum
protocol.

## Weak generator

Removing the ancilla transition from (2), define system jump operators

~~~
J_(x,f) = g |f><bottom|_x D_(x,f)(a,b).                  (8)
~~~

The local quantum channel has the expansion

~~~
Phi_(x,delta) = I + delta L_x + O(delta^2),

L_x(rho)
  = sum_f [J_(x,f) rho J_(x,f)^dagger
           - (1/2){J_(x,f)^dagger J_(x,f),rho}].         (9)
~~~

There is no first-order Hamiltonian term because the fresh-vacuum expectation
of H_x vanishes. On the diagonal pointer algebra, (9) is the pure-Record
generator

~~~
(L_x F)(R)
  = 1_(R_x=bottom) sum_f q_f(r_x(R))
      [F(R^(x,f))-F(R)],

q_f(r) = g^2 a^(2m_f(r)) b^(2(n(r)-m_f(r))),
h(r)   = sum_f q_f(r).                                  (10)
~~~

Recorded targets have zero rate and never overwrite.

## Exact classification inside the core grammar

Let

~~~
kappa = (a/b)^2,       beta=b^2.
~~~

Equation (10) gives

~~~
q_f(r)=g^2 beta^(n(r)) kappa^(m_f(r)).
~~~

A profile with one recorded neighbor has same-label/nonmatching-label
intensity ratio kappa. Requiring (1) on that profile forces kappa=2.
Conversely kappa=2 reproduces (1) on every profile. Therefore all positive
real members of the core grammar that match the supplied kernel are

~~~
a=sqrt(2 beta),        b=sqrt(beta),

q_f^(beta)(r)=g^2 beta^(n(r)) 2^(m_f(r)),
h_beta(r)=g^2 beta^(n(r)) Z(r),          beta>0.         (11)
~~~

The beta=1 member is the matching-only identity

~~~
q_f=g^2 2^(m_f),       h=g^2 Z.
~~~

It is unique modulo g^2 only after the syntax fixes the other-recorded gain
equal to the blank gain. This is a simple realization of the supplied ratio,
not physical selection of that ratio or of beta=1.

For beta' != beta,

~~~
h_(beta')(r)/h_beta(r)=(beta'/beta)^(n(r)),
~~~

which is not one constant on the full profile space. The freedom cannot be
absorbed into g^2.

## Same-premise dimensionless discriminator

Use the same carrier, ancilla, protocol, g, and core grammar for:

~~~
law A: beta=1,   b=1,       a=sqrt(2),
law B: beta=2,   b=sqrt(2), a=2.                         (12)
~~~

Choose two blank targets with disjoint radius-one neighborhoods:

~~~
x_2: n=2, both recorded neighbors have the same label,
     Z=2^2+5=9;

x_3: n=3, three recorded neighbors have three distinct labels,
     Z=3*2+3=9.                                          (13)
~~~

Their hazard ratio is

~~~
h_beta(x_3)/h_beta(x_2)=beta.
~~~

Conditional on the next tested Record occurring at one of the two sites,

~~~
P_beta(x_3 first)=beta/(1+beta)
                 =1/2  at beta=1,
                 =2/3  at beta=2.                       (14)
~~~

The common scale g^2 and the equal raw sum Z=9 cancel. In the local-infinite
reading, put both targets and all of their blank neighbors in the observation
region. Conditional on exterior graphical history, other candidate sites
contribute one common predictable survival functional to the two target
densities; it cancels in their conditional ratio exactly as in Block18. No
constant-rate assumption is made for those competitors.

The n=0 versus n=6 Block18 fixture is a hostile control here, not an oracle:
for one of each of the six labels its Z values are 6 and 12, and the
x_6 odds are 2 beta^6/(1+2 beta^6).

## Finite-volume ordered-product bridge

Fix Lambda_L=(Z/LZ)^3, L>=3, with M=L^3. One mesh sweep:

1. chooses any permutation containing every site exactly once;
2. applies each local fresh-vacuum channel (5) in that order; and
3. discards every used ancilla.

Permutations may vary from sweep to sweep. This is a regulator, not a physical
scheduler. No simultaneous product of overlapping local unitaries is claimed.

On the diagonal pointer algebra, write the local Markov operator as

~~~
T_(x,delta)F
  = F + sin^2(sqrt(delta h_x))
      [sum_f p_f F(R^(x,f))-F].
~~~

For delta h_max<=1,

~~~
0 <= delta h-sin^2(sqrt(delta h))
   <= (delta h)^2/3,

||L_x||_infinity <= 2 h_max,

||T_(x,delta)-I-delta L_x||_infinity
   <= (2/3) delta^2 h_max^2.                             (15)
~~~

For any sweep permutation pi, with A=sum_x L_x,

~~~
||T_(delta,pi)-I-delta A||_infinity
 <= (2/3)M delta^2 h_max^2
    + exp(2 delta M h_max)-1-2 delta M h_max.            (16)
~~~

The right side is O_L(delta^2) and is uniform over the finitely many
permutations. Markov contractions plus a telescoping comparison with
exp(delta A) then give, for any sequence of sweep permutations,

~~~
T_(t/N,pi_N) ... T_(t/N,pi_1)
  -> exp(t A)                                             (17)
~~~

on the finite diagonal algebra. The bound is not uniform in volume and proves
neither a global infinite-lattice collision unitary nor a physical clock.

An exact adjacent-site finite-step control must show that scan order can
change probabilities at O(delta^2) while leaving (10) unchanged at first
order. It must not report that regulator artifact as physical selection.

## Finite and local-infinite process gate

For the executed pair (12), set alpha=6g^2. Exhaustive profile bounds must
rederive

~~~
alpha <= h_beta(r) <= 736 alpha,       beta in {1,2}.     (18)
~~~

Finite-volume generators are conservative pure-birth generators and their
ordered-history laws normalize by the append-only finite DAG argument.

For local-infinite existence, a common rate-736 alpha proposal field,
uniform acceptance key, and exponential mark race realize both generators.
A backward query step exposes at most seven sites, giving the explicit
factorial-tail domination

~~~
P(ancestor radius >= m)
 <= |A| sum_(k>=m) (5152 alpha T)^k/k! -> 0.             (19)
~~~

This supplies finite backward clans, a measurable local cadlag process,
fixed/periodic local-cylinder convergence, and translation/proper-cubic
covariance after the runner proves the displayed premises. The lower bound
in (18) gives

~~~
P(x remains blank at t)<=exp(-alpha t).
~~~

Every fixed initially blank site records almost surely and then remains
locked. There is no global next-event chain for infinitely blank data and no
common finite completion time.

This is a new microscopic membership proof for two pure-Record generators; it
reuses the Block18 Harris method only after the generator, sector, rate bound,
initial law, and local-cylinder contract are matched explicitly.

## Outer orbit-controlled structural control

The original exact engineered Kraus family with an arbitrary positive bounded
proper-cubic-invariant h(r) remains useful only to classify a broad
structural dilation. It contains one free coefficient per simultaneous
slot-and-label profile orbit, so it cannot test physical one-ray selection.
The held-out desk census is 5,075 orbits (5,074 dimensions modulo scale);
the count-only cone has seven coordinates (6 modulo scale). Both runners
must rederive those values without using them as pass oracles.

The exact engineered linear-in-delta Kraus family and the exponential
Hamiltonian family (2) are different finite-collision realizations that share
a first-order generator when their h agrees. They must never be printed as
one exact map.

## Provenance boundary

- Block02 supplies an orthogonal-writer precedent only. It does not supply
  this one-site carrier, collision, attachment, rate, or history.
- Blocks09 and 10 do not supply the six-mark kernel or the auxiliary
  seven-state pointer used here. Their direction/corner and joint-carrier
  results remain separate upstream work.
- Block11's strict-M_2 no-information-without-disturbance boundary is
  preserved. Block19 takes the explicitly named orthogonal-pointer exit and
  derives no strict-M_2 encoder or causal preparation.
- Block18 supplies the pure-Record process target and Harris proof method, not
  the pair-factor Hamiltonian or a selector.
- Fresh bath fragments, vacuum preparation, trace/disposal, weak scaling, and
  mesh cadence are downstream protocol inputs.

## Required test battery

The primary runner must:

1. generate the six directions and 24 proper cubic rotations;
2. exhaust all 7^6 profiles and rotate slots and labels together;
3. derive the relation-factor coefficients, star spectrum, exact sine/cosine
   Kraus channel, CP/TP, fresh-vacuum target lock, pointer-projector QND,
   range-one support, and covariance;
4. derive the quantum weak generator and its diagonal jump intensities from
   the exact unitary rather than inserting (10) as an oracle;
5. prove that the supplied conditional kernel forces (a/b)^2=2 and classify
   the surviving beta family modulo g^2;
6. execute beta=1 and beta=2 under one membership contract and reconstruct
   the same-Z 1/2 versus 2/3 local Record-order discriminator;
7. prove (15)--(17), including varying scan orders and an exact O(delta^2)
   order-dependence control;
8. prove finite histories and the local-infinite construction at the exact
   scope of (18)--(19);
9. independently derive the outer orbit census and demote it to a structural
   control;
10. bind the exact Block18 provenance and reject strict-M_2, autonomous-bath,
    compound-event, clock, gravity, axiom, audit, and TOE upgrades;
11. reject hostile mutations and print substantive per_element:,
    per_site:, per_mode:, per_block:, and lattice_wide: lines, ending
    in TOTAL: PASS=n FAIL=n with stdout below 6000 bytes.

The independent checker must reconstruct the same claims without importing
the primary implementation or treating the anticipated terminal, witness
fractions, orbit count, or hazard bounds as test oracles.

If an underselection terminal is observed, a post-execution N1--N8 No-Go
Discipline checklist with five honest N5 resolution lines is mandatory. The
preregistration attack is not that release certificate.

## Stop rule and terminal matrix

| observed result | permitted disposition |
|---|---|
| pair-factor grammar, QND quantifier, protocol, or equivalence remains ambiguous | stop before target execution |
| exact star unitary, CP/TP, lock, QND, locality, covariance, or common protocol fails | first named construction failure only |
| no controlled finite-volume diagonal limit | scaling/protocol failure only |
| matching-only beta=1 lift passes but the extended grammar is not classified | conditional realization identity only; classification inconclusive |
| two same-premise beta values survive but differ only by global scale | no underselection; classification remains open |
| beta=1,2 survive every gate and give different local Record-order odds | narrow pair-factor hazard underselection becomes eligible after N1--N8 |
| the complete corrected grammar is independently proved one ray modulo global scale | positive generator-selection theorem inside the imported grammar |

No result in this author-side block changes formal TOE percentages, audit
status, or axiom text. If the narrow terminal survives, the next campaign is
the action/transfer generator-cone audit: determine whether the retained
action structure fixes beta or supplies an equivalent positive history
measure.
