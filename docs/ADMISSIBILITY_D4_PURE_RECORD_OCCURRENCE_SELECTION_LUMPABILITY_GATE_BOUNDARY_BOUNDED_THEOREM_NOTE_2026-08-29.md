---
claim_id: admissibility_d4_pure_record_occurrence_selection_lumpability_gate_boundary_bounded_theorem_note_2026-08-29
claim_type: bounded_theorem
claim_scope: "Within the invariant seven-state sector and the declared bounded range-one one-site Markov pure-Record ansatz, two complete finite/local-infinite processes use the same supplied six-mark conditional kernel but have clock-independent local first-Record probabilities 1/2 and 2/3. The frozen premise set therefore underselects these two processes modulo one common positive rescaling. This is not a full-M2, non-Markov, compound-event, global-jump-chain, gravity, or axiom result."
preregistration_commit: 54f1d5c5e0
support_correction_commit: 5dd5f77522
origin_main_observed: 3cc632921c36aa90266c5c62e56816577ce59a0a
minimal_axioms_blob: bc23300becfe4e4db57153c0e94cfcdf2338da71
verdict: PURE-RECORD-HARRIS-PROCESSES-EXIST-DIMENSIONLESS-GENERATOR-UNDERSELECTED
primary_runner_sha256: c1f7e00b8f42111d677fc5e53ced6f6a25a4871325671270f3984670d5f7b799
independent_runner_sha256: de91d8a726d44bd16536753d8fe7789eec1ac87915f4c3d3de40b926964e8d8f
state_sector: blank_plus_six_rho_f
full_m2_process: false
global_jump_chain: false
gravity_no_go: false
axiom_amendment: false
obligation_retirement: 0
toe_percentage_movement: 0
---

# Pure-Record Occurrence Selection and Lumpability Gate

**Date:** 2026-08-29

**Campaign block:** Source/Eta 18

**Standing:** author-side bounded theorem; audit status remains unset

Primary certificate:
[`admissibility_d4_pure_record_occurrence_selection_lumpability_gate_2026_08_29.py`](../scripts/admissibility_d4_pure_record_occurrence_selection_lumpability_gate_2026_08_29.py).

Independent certificate:
[`independent_admissibility_d4_pure_record_occurrence_selection_lumpability_gate_2026_08_29.py`](../scripts/independent_admissibility_d4_pure_record_occurrence_selection_lumpability_gate_2026_08_29.py).

Frozen target and support correction:
[`GOAL.md`](../.claude/science/physics-loops/toe-source-eta-ownership-block18-pure-record-occurrence-selection-lumpability-20260829/GOAL.md)
and
[`PREFLIGHT_SUPPORT_CORRECTION.md`](../.claude/science/physics-loops/toe-source-eta-ownership-block18-pure-record-occurrence-selection-lumpability-20260829/PREFLIGHT_SUPPORT_CORRECTION.md).

No-Go Discipline packet:
[`NO_GO_DISCIPLINE_CHECKLIST.md`](../.claude/science/physics-loops/toe-source-eta-ownership-block18-pure-record-occurrence-selection-lumpability-20260829/NO_GO_DISCIPLINE_CHECKLIST.md).

## 1. Result

The bounded seven-state process sector earns

```text
PURE-RECORD-HARRIS-PROCESSES-EXIST-DIMENSIONLESS-GENERATOR-UNDERSELECTED.
```

Fix the supplied six-mark conditional kernel below and the declared bounded,
range-one, one-site, continuous-time Markov pure-Record ansatz. Two processes
on exactly that state sector satisfy the same finite-history, local-infinite
Harris, covariance, formation, and permanence requirements. Their hazards are

```text
lambda_x^(0)(R) = alpha,
lambda_x^(1)(R) = alpha(1+n_x(R)/6)
```

at a blank site, and zero after that site records. Here `alpha>0` is a common
rate scale, not the registered lattice scale. A local readable-Record race has
winner probabilities `1/2` and `2/3`; the common scale cancels. Since
`lambda^(1)/lambda^(0)` ranges from `1` to `2` as the recorded-neighbor count
runs from zero to six, no one state-independent rescaling identifies the two
generators.

Thus the frozen premise set does not select between these two executed laws
modulo a common positive change of time unit. This is an existence-plus-
underselection theorem inside the displayed process sector. It is not a
theorem that occurrence laws do not exist, not a uniqueness result over other
process classes, and not authorization for a foundation change.

The minimal-axiom boundary is exact. Admissibility assigns a probability
distribution to possible Record content conditional on formation, while
explicitly not supplying the formation site, probability, or rate
(`docs/MINIMAL_AXIOMS_2026-06-29.md:63-73`). Record supplies formation,
uniqueness, readability, and permanence, but no process generator
(`docs/MINIMAL_AXIOMS_2026-06-29.md:75-83`). The kernel and Markov/Harris
composition below are downstream witness inputs. Their role is to construct
two compatible completions, not to rename either completion as axiom content.

## 2. Exact state sector and conditional mark kernel

Let

```text
D = {+-e_1,+-e_2,+-e_3},
rho_f = (I-(143/256) f dot sigma)/2,
X = {bottom} union {rho_f : f in D}.
```

The process state is `R in X^(Z^3)` or its finite-torus analogue. A blank site
may append one mark and a recorded site never changes. This readable blank/
Record split, the six-mark support, instantaneous one-site jumps, and the
Markov clock are declared downstream model inputs.

For every signed axis `f`, `rho_f` is Hermitian and has trace one. With
`b=143/256`,

```text
det rho_f = (1-b^2)/4 = 45087/262144,
spec(rho_f) = {(1-b)/2,(1+b)/2} = {113/512,399/512}.
```

Both eigenvalues are positive, so all six marks are valid one-site `M_2(C)`
possibilities. They do not exhaust that domain.

For a blank candidate `x`, let `m_x(f;R)` count nearest neighbors carrying the
exact mark `rho_f`. The supplied conditional kernel is

```text
w_x(f;R) = 2^(m_x(f;R)),
p_x(rho_f|R) = w_x(f;R) / sum_(g in D) w_x(g;R).
```

Every weight is positive and the probabilities sum to one. There are
`7^6=117,649` ordered neighbor profiles. The primary exhausts all profiles
under all `24` determinant-`+1` signed-axis rotations; the independent checker
reconstructs `5,075` rotation orbits and checks `2,823,576` profile/rotation
pairs. In a blank neighborhood the row is `(1/6,...,1/6)`. With one neighbor
carrying `rho_f`, its entry is `2/7` and the other five entries are `1/7`.

The kernel assigns no “no event” mark. Waiting belongs to the activation
hazard. With

```text
q_x(f|R) = lambda_x(R) p_x(rho_f|R),
```

both implementations verify exactly that `sum_f q_x(f|R)=lambda_x(R)` on
every local profile.

## 3. Finite generators and normalized histories

On `Lambda_L=(Z/LZ)^3`, `L>=3`, define

```text
Q_L(R,R^(x,f)) = q_x(f|R),
Q_L(R,R) = -Lambda(R),
Lambda(R) = sum_(x:R_x=bottom) lambda_x(R),
```

with every other entry zero. For either hazard, every legal off-diagonal entry
is positive, the row sum is zero, and each accepted transition removes one
blank site. A path therefore has at most the number of blanks in its initial
state, hence at most `L^3` jumps. Fully recorded states are absorbing and no
transition overwrites a Record. “Monotone” here means only this append-only
occupancy property; no colored attractiveness statement is made.

Fix `R_0`, `T>0`, and a marked history
`gamma=((x_i,f_i,t_i))_(i=1)^k` with `t_0=0` and
`0<t_1<...<t_k<T`. Relative to counting measure on sites and marks and
Lebesgue measure on the ordered time simplex, its conditional density is

```text
 [product_(i=1)^k
    exp(-Lambda(R_(i-1))(t_i-t_(i-1)))
    q_(x_i)(f_i|R_(i-1))]
 exp(-Lambda(R_k)(T-t_k)).
```

This formula is normalized, rather than merely sampled. Induct on the number
of blanks. At a state with total rate `Lambda`, if every successor's remaining
history mass is one, the no-jump history and all possible first jumps have
total mass

```text
exp(-Lambda T)
 + integral_0^T exp(-Lambda s) sum_(x,f) q_x(f|R) ds
= exp(-Lambda T) + integral_0^T Lambda exp(-Lambda s) ds
= 1.
```

The absorbing state is the induction base and the append-only graph is finite
and acyclic. Summing and integrating over
`k=0,...,#blanks(R_0)` therefore gives one. A random initial state with Borel
law `mu` on `X^(Lambda_L)` is handled by mixing this conditional law against
`mu`.

The density is zero for a site occupied in `R_0`, a repeated site, an illegal
site or mark, a recursively inconsistent transition, or non-strict time
ordering. Both runners test exact positive histories and all named invalid
classes.

## 4. Local infinite-volume Harris processes

There is no finite global proposal rate on `Z^3` when infinitely many sites
are blank. The infinite processes are defined on finite spacetime cylinders,
not by a global next-event clock.

Start from any deterministic configuration in the seven-state sector, or
sample a Borel initial law `mu` on that product space independently of the
proposal and key field.

Independently at each site place a rate-`2 alpha` Poisson proposal process.
Give each proposal an independent uniform key `U` and six independent
unit-rate exponential keys `E_f`. At a proposal:

1. reject the proposal if the site is already recorded;
2. otherwise accept iff `U<=lambda_x(R)/(2 alpha)`; and
3. on acceptance choose the unique minimizer of
   `E_f/2^(m_x(f;R))`.

If `E_f` has rate one, `E_f/w_f` has exponential rate `w_f`. The probability
that label `f` wins the race is therefore

```text
integral_0^infinity w_f exp(-s sum_g w_g) ds
= w_f / sum_g w_g
= p_x(rho_f|R).
```

Multiplying the proposal rate, acceptance probability, and race probability
gives exactly `q_x(f|R)`. Continuous keys tie with probability zero; the exact
fixtures also reject tied and fixed-label mutations.

### Finite backward clans and measurability

For a finite observation set `A` and time horizon `T`, trace the required
proposal decisions backward. One predecessor step queries at most the site
and its six neighbors. The proposal rate is `2 alpha`, and the ordered volume
of `k` proposal times is `T^k/k!`. Consequently

```text
P(ancestor radius >= m)
 <= |A| sum_(k>=m) (14 alpha T)^k/k! -> 0.
```

For finite `z=14 alpha T`, once `m+1>z`, successive terms have ratio at most
`z/(m+1)<1`; taking `m` beyond `2z` gives a geometric ratio at most `1/2`.
The factorial tail therefore vanishes. The primary exact regression at `z=1`
gives bounds `5/48`, `1/17920`, and `13/2874009600` for
`m=4,8,12`; the independent regression extends two rational query times and
clan radii.

The ancestor radius is thus finite almost surely. Its finite cubic bounding
box contains finitely many rate-`2 alpha` Poisson points in finite time almost
surely. Ordering those finitely many points and applying the local acceptance
and mark maps gives a finite composition of Borel comparisons and minima.
This defines a measurable sample map simultaneously on the countable family
of rational finite-set queries. Each coordinate changes at most once, so the
map extends locally to a cadlag path.

Use the same proposal/uniform/key field for the infinite process,
fixed-exterior boxes, and periodic boxes. If the backward clan and its initial
data avoid a box boundary, every decision relevant to the query is identical
in all three realizations. The disagreement probability is bounded by the
probability that the clan reaches the boundary, hence tends to zero with box
size. This proves shared-field local-cylinder convergence, not exact
projective consistency.

### Covariance, initial laws, formation, and permanence

For a translation or proper cubic rotation `g`, relabel sites and marks and
set

```text
E'_(g f)(g x,t)=E_f(x,t)
```

with the analogous proposal and uniform relabeling. The local update map then
commutes with `g` off the null tie set. Hence

```text
g_* Law_mu = Law_(g_* mu).
```

This is covariance. The evolved law is invariant only when the initial law is
invariant. Both runners use an asymmetric point-mass initial state as the
control and reject the stronger invariance claim.

While a site is blank, both hazards are at least `alpha`. Proposals whose
uniform key is at most `1/2` form a rate-`alpha` subfield and are accepted
regardless of the surrounding profile. Therefore

```text
P(x remains blank at t) <= exp(-alpha t) -> 0.
```

Every initially blank fixed site records almost surely. Since `Z^3` is
countable, all initially blank sites eventually record on one probability-one
event. No site ever changes afterward. When infinitely many sites are initially
blank, there is no common finite completion time: for each fixed integer `T`,
infinitely many independent site proposal fields have no proposal before `T`
almost surely, so those sites are still blank. Taking the countable intersection
over integer `T` proves the claim. For the same reason there is no globally
nonexplosive jump chain; infinitely blank data have infinitely many global
events in every positive interval.

## 5. Dimensionless local Record-order discriminator

On `Lambda_7`, let `x_6=(0,0,0)` have its six neighbors permanently recorded
and let `x_0=(3,3,3)` and its six neighbors be blank. The radius-one
neighborhoods are disjoint. Marginalizing the mark in the first finite jump
gives site intensity `sum_f q_x(f|R)=lambda_x(R)`. Conditional on that jump
occurring at one of the two named sites,

```text
P(x_6 next | next site in {x_0,x_6})
 = lambda_(x_6)/(lambda_(x_0)+lambda_(x_6))
 = 1/2  for law 0,
 = 2/3  for law 1.
```

The operational infinite-volume witness uses only local readable Record
history. In the corresponding `Z^3` configuration put

```text
U = {x_0,x_6} union N(x_0),
tau_U = first new Record time in U.
```

Before `tau_U`, the hazard at `x_0` remains `r_0=alpha` under both laws: all
its nearest neighbors lie in `U` and remain blank. The hazard at `x_6` remains
`r_6=alpha` or `2 alpha`: its six neighbors were already recorded and are
permanent.

The competing sites in `N(x_0)` need not have constant hazards. Births outside
`U` can change their neighbor profiles before `tau_U`. Condition on an
exterior graphical history `H` and let `b_H(s)` be the resulting predictable
sum of competitor hazards at time `s`, on the history with no earlier birth in
`U`. The common survival factor is

```text
S_H(s) = exp(-(r_0+r_6)s - integral_0^s b_H(u) du).
```

Conditional on `H`, the density that the first Record in `U` occurs at time
`s` and at `x_i`, for `i in {0,6}`, is

```text
r_i S_H(s) ds.
```

Thus for every `T>0`, both tested probabilities contain the same factor

```text
J_H(T) = integral_0^T S_H(s) ds.
```

It cancels before or after averaging over exterior histories:

```text
P(x_6 wins | tau_U<=T, winner in {x_0,x_6})
 = r_6/(r_0+r_6)
 = 1/2  for law 0,
 = 2/3  for law 1.
```

The statistic observes only which named site records first. Multiplying every
intensity by one positive constant changes the time distribution but not
these odds. Conversely the ratio

```text
lambda^(1)/lambda^(0) = 1+n/6,  n=0,...,6,
```

is not constant, and the two observed odds differ. The two complete process
laws are therefore dimensionlessly inequivalent.

## 6. One-site and compound event arity

For a signed direction `f`, define the three-site cylinder

```text
C_(c,f) = {c-2f,c,c+f all carry rho_f}.
```

Starting with those sites blank, a bounded one-site append generator must
accept at least three target-site jumps. In the generator graph, the cylinder
is at distance three; the constant, linear, and quadratic semigroup
coefficients vanish. Hence

```text
P_single(C_(c,f) at t) = O(t^3).
```

A declared compound jump of finite oriented rate `kappa_c(R)/6` has

```text
P_atom(C_(c,f) at t) = (kappa_c(R)/6)t + O(t^2)
```

only when it is the sole direct transition into that cylinder and the local
generator supplies the bounded `O(t^2)` remainder. With several direct
entries, the linear coefficient is their sum. This compares event arities; it
does not identify the three-site Record projection with the complete Block16
quantum/output state.

Both runners check all six directions. They also reproduce the mandatory
periodic controls:

| volume | exact nominal-fixture failure |
|---|---|
| `L=3` | `c-2f=c+f`, so there are two target sites and one-site order two; `S` gives `(q0,q1)=(2/7,1/3)` and `C` gives `(4/9,16/27)` in units of `alpha` |
| `L=4` | `y=c+2f=c-2f` is already recorded in `C`, so there is no tested append |
| `L=5` | both `c+f` and `c-2f` neighbor `y`, giving `(q0,q1)=(4/9,16/27)` in units of `alpha` |

These volumes are falsifiers for the nominal lumpability fixture, not members
of it.

## 7. Corrected strong-lumpability row

Use `Lambda_L` with `L>=6`. Let

```text
S_(c,f) = {c -> rho_f},
C_(c,f) = {c-2f,c,c+f -> rho_f},
y = c+2f,
```

Place the corresponding full states identically outside these displayed seeds
and require the five neighbors of `y` other than `c+f` to be blank in both
states. This support condition is uniform in `L`: in the integer lift,
all seed sites, `y`, and neighbors of `y` lie between offsets `-2` and `3`
along the seed axis, so distinct lifted points cannot become congruent modulo
any `L>=6`. In `S`, `y` has no recorded neighbor, so `p_y(f)=1/6`. In `C`,
its unique recorded neighbor carries `rho_f`, so `p_y(f)=2/7`; law 1 also has
`lambda_y=7 alpha/6`. The exact marked rates are

```text
             S -> y:f       C -> y:f
law 0        alpha/6        2 alpha/7
law 1        alpha/6        alpha/3.
```

For a partition that identifies the two full seed states, maps their `y:f`
successors into one common distinguishable cell `A_(y,f)`, and maps no other
outgoing transition from either representative into that cell, strong
lumpability requires

```text
sum_(R':pi(R')=A) Q(R,R')
 = sum_(R':pi(R')=A) Q(R_tilde,R').
```

Each displayed pair is unequal, so that specified partition fails the row
test for both witness processes. The conclusion is exactly this narrow. A
compensating transition mapped into `A_(y,f)` changes the complete row sum and
can equalize it; both runners reproduce that falsifier. A constant projection
is trivially lumpable, and a coarser projection that discards the future
append, a different process, or another exactly lumpable fibre remains live.

## 8. Periodic incidence and source/debit interface

Let `B_L` be the oriented incidence matrix of the connected periodic cubic
graph and let raw occupancy be
`rho_x(R)=1_(R_x!=bottom)`. Every incidence column has one `+1` and one `-1`,
so `im B_L` lies in the zero-sum vertex subspace.

For every `L>=3`, connect each nonroot vertex to a parent that lowers its first
nonzero coordinate. These `L^3-1` edges form a spanning tree. Removing the
root row gives a unimodular reduced tree-incidence matrix, proving the matching
lower bound. Therefore, over real currents,

```text
rank B_L = L^3-1,
im B_L = 1^perp.
```

The exact regressions are `26`, `63`, and `124` at `L=3,4,5`.

A one-site birth has `Delta rho=e_x` and total one. A compound birth at three
distinct sites has total three. The displayed `C_(c,f)` has three distinct
sites for `L>=4` and the lumpability fixture uses `L>=6`; a generic
three-distinct-site source also exists on `L=3`. Neither birth can satisfy

```text
Delta rho + B_L j = 0
```

because the left side has nonzero total for every edge current `j`. An
explicit source repairs the local equation,

```text
Delta rho + B_L j = sigma,
sum_x sigma_x = 1 or 3.
```

A scalar reservoir debit `-1` or `-3` restores global balance, but it is not a
local current until an enlarged reservoir incidence is supplied. Open-boundary
flux, neutral paired events, signed content, and worldline-transition decoders
also remain live. This theorem applies only to a downstream join that elects
to identify raw cumulative Record occupancy with a conserved density. It is
not a gravity no-go.

## 9. Execution evidence and hostile controls

The frozen primary cache is
[`admissibility_d4_pure_record_occurrence_selection_lumpability_gate_2026_08_29.txt`](../logs/runner-cache/admissibility_d4_pure_record_occurrence_selection_lumpability_gate_2026_08_29.txt):

```text
runner SHA-256: c1f7e00b8f42111d677fc5e53ced6f6a25a4871325671270f3984670d5f7b799
cache SHA-256:  31653b583ee0cc3c6b3aabccacbddd59227627a692932e4161f23bf09c04ca44
exit:          0
checks:        PASS=12 FAIL=0
mutants:       rejected 18/18
stdout:        3,133 bytes
```

The frozen independent cache is
[`independent_admissibility_d4_pure_record_occurrence_selection_lumpability_gate_2026_08_29.txt`](../logs/runner-cache/independent_admissibility_d4_pure_record_occurrence_selection_lumpability_gate_2026_08_29.txt):

```text
runner SHA-256: de91d8a726d44bd16536753d8fe7789eec1ac87915f4c3d3de40b926964e8d8f
cache SHA-256:  2f2120b0106bac4123f69daad63915df4c1bc494a6739c41acfa79a66e854265
exit:          0
checks:        PASS=17 FAIL=0
mutants:       detected 18/18
```

The independent checker does not import the primary. It reconstructs the
profile orbit census, finite generator and exact history, two rational Harris
query times, two clan radii, six `L=6` seed directions, the three hostile
small volumes, and the all-`L` incidence proof with different data structures.

The mutation battery rejects Record overwrite, mark subnormalization and
covariance breaking, asymmetric-initial-law/invariance confusion, fixed or
tied mark keys, a hidden no-event mark, excessive or nonlocal rates, zero
blank hazard, positive density for invalid histories, use of the small-torus
lumpability fixture, removed or compensated fibres, a hidden direct triple
entry, pure global rescaling, source suppression, the wrong graph type, a
global jump-chain upgrade, and a full-`M_2(C)` scope upgrade.

## 10. Exact scope, live exits, and accounting

The result uses one supplied conditional mark kernel. It does not claim that
the minimal premises select that kernel. The state sector is the invariant
blank-plus-six-`rho_f` sector. A common extension that preserves arbitrary
pre-existing `M_2(C)` contents, counts exact `rho_f` matches, and appends only
the six supported marks remains a live technical completion; it was not
executed here.

The following routes also remain live:

- an action, detailed-balance condition, DLR law, or reconstruction theorem
  that derives a unique generator under an explicitly enlarged hypothesis
  set;
- a microscopic QND repeated-interaction dilation that derives occurrence
  rather than stipulating a hazard;
- a compound, non-Markov, correlated, or other event-arity law;
- a different future-preserving lumpable process or quotient;
- an explicit local source/reservoir incidence, boundary flux, signed decoder,
  or worldline source map; and
- an absolute physical clock calibration.

An added-condition selector would be a separately scoped positive theorem; it
would not erase the two-process result under the smaller frozen premise set.
Conversely, this note does not establish that any additional premise belongs
in the foundation.

The linked No-Go Discipline packet must resolve its post-execution N1--N8
gate and land with the cached five-resolution evidence before this bounded
negative terminal can ship. This source note does not set that gate or any
audit verdict.

```text
minimal-axiom amendment: false
obligation retirement: 0
TOE percentage movement: 0
audit verdict: unset
```

The scientific next step is a microscopic QND or action-derived selector that
produces a dimensionless hazard ratio under a clearly stated hypothesis set.
No foundation, gravity, or audit change is made here.
