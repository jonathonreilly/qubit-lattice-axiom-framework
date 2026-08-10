---
claim_id: admissibility_binary_full_conditional_compatibility_ising_action_axiom_boundary_bounded_theorem_note_2026-08-10
claim_type: bounded_theorem
claim_scope: "For strictly positive binary full-conditionals on a finite set of sites, a positive joint law exists exactly when the conditional-odds one-form has zero multiplicative curl on every two-site configuration square; the joint law is then unique and recovered by path integration. For a translation- and proper-cubic-covariant rule on the binary central M2 code whose probability depends only on the number k of occupied nearest neighbors, compatibility for all cubic edge environments is equivalent to geometric odds o_k=A B^k, hence an affine logit and a finite-volume nearest-neighbor Ising-type action. An exact normalized, full-support, monotone, code-swap-symmetric count rule satisfies the named local structural clauses but fails one square with path products 1/14 and 1/9. The result identifies a sufficient global-compatibility addition to Admissibility but proves no axiom inconsistency, global-law impossibility, dynamics, formation process, realized history, gravity identification, axiom necessity, or adoption."
upstream_dependencies:
  - minimal_axioms
  - admissibility_global_measure_menu_kernel_type_separation_bounded_theorem_note_2026-08-10
  - global_record_history_process_law_cycle30_note_2026-07-14
  - local_to_global_cubic_process_glue_cycle33_note_2026-07-14
  - source_action_bridge_pricing_cycle871_bounded_theorem_note_2026-07-28
runner: scripts/admissibility_binary_full_conditional_compatibility_ising_action_axiom_boundary_2026_08_10.py
---

# Binary Full-Conditional Compatibility, Cubic Ising Action, And The Admissibility Axiom Boundary

**Date:** 2026-08-10
**Type:** bounded theorem and axiom-consequence map
**Scope:** finite strictly positive binary sectors embedded in the existing
one-site M2(C) possibility domain, with a count-only cubic specialization.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[admissibility_binary_full_conditional_compatibility_ising_action_axiom_boundary_2026_08_10.py](../scripts/admissibility_binary_full_conditional_compatibility_ising_action_axiom_boundary_2026_08_10.py)

## Result Up Front

The August Admissibility sentence gives a normalized probability distribution
at each site as a function of its nearest-neighbor condition. Sitewise
normalization does not by itself answer a different question:

> Are those local distributions the full conditional distributions of one
> joint probability law on a collection of forming Records?

On any finite binary sector, that question has an exact answer. For each site
$i$, let $r_i(x)$ be the positive conditional odds for changing the site from
zero to one while all other bits equal $x$. A positive joint law exists if and
only if every two-site configuration square obeys

    r_i(x) r_j(x^i)=r_j(x) r_i(x^j).

When the square equations hold, multiplying odds along any path from the
all-zero configuration gives a path-independent unnormalized weight.
Normalization gives the unique joint law with the declared full conditionals.
No external representation theorem is needed.

The cubic specialization is sharper. Encode two local possibilities by the
central matrices $B_0=-I_2$ and $B_1=+I_2$. Suppose the probability of $B_1$
depends only on the number $k$ of neighboring $B_1$ Records:

    q(k)=P(B_1 | k),       k=0,...,6,
    o_k=q(k)/(1-q(k)).

For adjacent cubic sites, the other five neighbors on the two ends are
disjoint. Their occupied counts $a,b$ can therefore vary independently from
zero through five. The square equations become

    o_a o_(b+1)=o_b o_(a+1).

They hold for all environments exactly when the six successive odds ratios
are equal. Hence

    o_k=A B^k,
    q(k)=A B^k/(1+A B^k).

The resulting finite-region law is not merely representable by an action; its
action is derived up to the usual additive normalization:

    pi_Lambda(x|b)=Z_Lambda(b)^(-1)
      A^(sum_i x_i)
      B^(sum_(<ij> subset Lambda) x_i x_j + sum_i b_i x_i).

This is the binary nearest-neighbor Ising/Gibbs shape in zero-one variables.
If a separately registered code-swap symmetry also requires
$q(6-k)=1-q(k)$, it imposes $A B^3=1$ and leaves one continuous coupling
$B$. The code-swap clause is not inferred from the current axioms.

An exact hostile rule shows why compatibility is real content:

    q_bad=(1/8,1/4,1/3,1/2,2/3,3/4,7/8).

It is normalized, strictly between zero and one, monotone, genuinely
neighbor-varying, code-swap symmetric, translation covariant, and invariant
under all 24 proper cubic rotations. Its odds are

    (1/7,1/3,1/2,1,2,3,7).

For one adjacent pair with $a=0,b=1$, the two orders from $00$ to $11$ give
$1/14$ and $1/9$. No positive joint law can have these sitewise kernels as
its simultaneous full conditionals.

This is not an inconsistency in the four axioms. The local rule may instead
be intended as an ordered update kernel; that reading needs an update order
or dynamics and does not imply the static action above. The result isolates
the exact axiom choice:

- keep Admissibility sitewise and require each completed model to prove its
  own local-to-global/history consistency; or
- state explicitly that the sitewise distributions are conditionals of a
  compatible, projectively consistent family of finite-region joint laws.

No canonical axiom is edited, and the fixed TOE percentages do not move.

## Machine Status And Trace

~~~yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The finite binary square-curl equivalence, path reconstruction, cubic count classification, exact action, all-24 covariance, and hostile incompatibility witness are proved; global M2 compatibility, dynamics, formation order, realized history, gravitational identification, and axiom adoption remain open."
trace_class: upstream_support
target_claim_id: admissibility_local_to_global_compatibility_and_action_bridge
target_blocker_text: "decide whether sitewise nearest-neighbor probability distributions are compatible conditionals of one global law, and identify the exact axiom-side obligation if they are not"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
campaign_native_target_reachability: advances
next_trace_action: "Test whether the selected physical M2 law supplies a compatible finite-region specification or an ordered update process; then connect the derived statistical action to a physical source/tensor response without identifying them by name alone."
conditional_surface_status: "exact finite positive binary compatibility criterion and exact count-symmetric Ising-action classification; no general continuous-M2, temporal, history, or gravity closure"
hypothetical_axiom_status: "one sufficient addition is to require the sitewise laws to be one-site full conditionals of a covariant, projectively consistent family of finite-region joint laws; this is not adopted, proved necessary, or claimed minimal"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
~~~

## Exact Target And Obligation Graph

**Exact target.** Separate a normalized distribution at every site from a
compatible joint law across sites, solve the finite binary compatibility
problem, and determine what the current cubic symmetries force after
compatibility is supplied.

| Obligation | Role | Disposition |
|---|---|---|
| normalize each binary local law | local kernel | assumed strictly positive and normalized |
| make the rule translation/proper-cubic covariant | local symmetry | exact for count-only rules |
| decide whether all kernels are full conditionals of one joint law | compatibility | square-curl theorem closes the finite binary question |
| reconstruct the joint law | global finite law | exact path integral and normalization |
| classify count-only compatible cubic rules | action shape | exact geometric-odds / affine-logit theorem |
| test whether current local clauses force compatibility | axiom boundary | exact hostile symmetric rule fails one square |
| extend to arbitrary continuous M2 laws | generality | open |
| choose formation sites/order/rate and one realized history | autonomy | open |
| identify the statistical action with gravitational source/tensor response | gravity | open |

The theorem is deliberately finite and binary. It does not use the word
global to smuggle in infinite-volume existence, an actual sample, or a
dynamics.

## 1. Typed Setup

Let $V$ be a finite set of sites and let

    Omega={0,1}^V.

The two symbols may be embedded into the current one-site domain as
$B_0=-I_2$ and $B_1=+I_2$. Both are central, so simultaneous one-site unitary
conjugation fixes them. The embedding is a test sector, not a claim that
physical Records use this code or that the entire M2(C) distribution is
binary.

For each site $i$ and each configuration $x$ with $x_i=0$, let

    q_i(x)=P(X_i=1 | X_(V\{i})=x_(V\{i})),
    0<q_i(x)<1,
    r_i(x)=q_i(x)/(1-q_i(x)).

Strict positivity is load-bearing. It lets every conditional odds ratio and
every configuration path exist. Zero-support constraints require
component-by-component support analysis and are outside this theorem.

A **compatible positive joint law** is one function
$pi:Omega to (0,1)$ summing to one whose full one-site conditionals equal the
declared $q_i$.

This object is different from all of:

- one normalized measure on the one-site possibility domain;
- a temporal update kernel applied in a declared order;
- a measure on complete record histories;
- a realized member of any such measure; and
- a physical gravity action.

## 2. Finite Binary Square-Curl Theorem

### Theorem 1

The strictly positive full-conditionals $(q_i)$ admit a compatible positive
joint law if and only if, for every pair $i != j$ and every configuration $x$
with $x_i=x_j=0$,

    r_i(x) r_j(x^i)=r_j(x) r_i(x^j).          (SC)

Here $x^i$ is $x$ with bit $i$ flipped from zero to one.

When (SC) holds, the joint law is unique.

### Necessity

If $pi$ exists, then

    r_i(x)=pi(x^i)/pi(x).

Following the square first through $i$ and then $j$ gives

    pi(x^(ij))/pi(x)=r_i(x) r_j(x^i).

Following it first through $j$ and then $i$ gives

    pi(x^(ij))/pi(x)=r_j(x) r_i(x^j).

The two expressions are equal, proving (SC).

### Sufficiency

Fix the all-zero configuration $0$. For any target $x$, choose an order of
the sites where $x_i=1$ and multiply the appropriate odds along that monotone
path. Call the product $w(x)$.

Any two orders of the same finite set differ by adjacent transpositions.
Swapping two adjacent flips changes one path segment from

    r_i(y) r_j(y^i)

to

    r_j(y) r_i(y^j).

Equation (SC) makes those products equal. Therefore $w(x)$ is independent of
the chosen order. Set

    pi(x)=w(x)/sum_(z in Omega) w(z).

Every weight is positive. For any $x_i=0$, choose a path to $x$ and append
the flip at $i$. Path independence gives

    pi(x^i)/pi(x)=w(x^i)/w(x)=r_i(x).

Converting odds back to probabilities recovers $q_i(x)$. This proves
existence.

### Uniqueness

Any compatible positive law must have the same ratio
$pi(x^i)/pi(x)=r_i(x)$ on every hypercube edge. The connected configuration
hypercube therefore determines every weight relative to $pi(0)$.
Normalization fixes $pi(0)$, so the law is unique.

### Exact general fixture

The runner starts from an arbitrary positive rational four-site weight with
both one-site and cross-site terms. It:

1. derives all full-conditional odds;
2. verifies every square residual is exactly zero;
3. reconstructs all 16 weights along every monotone path;
4. normalizes and recovers the original law exactly; and
5. mutates one local odds entry, after which a square curl and a two-path
   disagreement both appear.

The finite fixture checks the construction. The proof above covers every
finite $V$.

## 3. Nearest-Neighbor Locality Reduces The Tests

Suppose $q_i$ depends only on the graph neighbors of site $i$.

If $i$ and $j$ are not adjacent, flipping $j$ does not change $r_i$, and
flipping $i$ does not change $r_j$. Their square equation holds
automatically. Only adjacent pairs need testing.

This is a useful local-to-global compression: the obstruction is a local
two-site curl, not a census over all global distributions. It is still more
than normalization at each endpoint.

## 4. Cubic Count Classification

### Count-only rule

On the cubic lattice, let the local law depend only on

    k=sum_(y~x) 1{B_1 at y},

and write $q(k)$ and $o_k=q(k)/(1-q(k))$.

Take adjacent sites $i,j$. Excluding their shared edge, the five remaining
neighbors of $i$ and the five remaining neighbors of $j$ are disjoint on
$Z^3$. Let their occupied counts be $a$ and $b$. They can be set
independently in the range zero through five.

The square condition is

    o_a o_(b+1)=o_b o_(a+1).

Dividing by the positive product $o_a o_b$ gives

    o_(a+1)/o_a=o_(b+1)/o_b.

Because $a,b$ are arbitrary, all six successive ratios equal one positive
constant $B$. With $A=o_0$,

    o_k=A B^k,
    q(k)=A B^k/(1+A B^k).

Conversely, geometric odds make both square products
$A^2 B^(a+b+1)$, so all squares close. This proves:

> A strictly positive, count-only cubic binary rule is compatible in every
> finite edge environment exactly when its logit is affine in the neighbor
> count.

The runner also encodes the logit equations as an exact rational linear
system on seven formal values. Its rank is five, so the solution space has
dimension two, and the constant vector plus the neighbor-count vector span
it.

### Derived finite-volume action

Let $Lambda$ be finite and let $b_i$ count exterior $B_1$ neighbors at site
$i$. Define

    pi_Lambda(x|b)=Z_Lambda(b)^(-1)
      A^(sum_i x_i)
      B^(sum_(<ij> subset Lambda) x_i x_j + sum_i b_i x_i).

Flipping site $i$ from zero to one multiplies the weight by

    A B^(b_i + sum_(j~i, j in Lambda) x_j)=A B^k.

Therefore the full conditional is exactly $q(k)$. In logarithmic notation,
the action, up to its normalization constant, is

    S_Lambda(x|b)
      =-(log A) sum_i x_i
       -(log B)[sum_(<ij>) x_i x_j + sum_i b_i x_i].

The action is a theorem of compatibility plus count symmetry on this binary
sector. It is not obtained by identifying the Record scalar readout with an
action.

### Optional code-swap symmetry

If a physical symmetry independently exchanges $B_0$ and $B_1$, the count
rule must obey

    q(6-k)=1-q(k),
    o_(6-k)=1/o_k.

Substitution of $o_k=A B^k$ gives

    A B^3=1.

The field and coupling are then related and only one continuous parameter
remains. For the exact runner fixture,

    A=1/8, B=2,
    o_k=2^(k-3),
    q=(1/9,1/5,1/3,1/2,2/3,4/5,8/9).

This is the zero-field ferromagnetic Ising shape after converting
$x_i$ to spins $s_i=2x_i-1$. Neither the physical binary code nor its swap
symmetry is selected here.

## 5. Exact Covariant Incompatibility Witness

Define

    q_bad=(1/8,1/4,1/3,1/2,2/3,3/4,7/8).

Every entry lies strictly between zero and one, so the local distributions

    mu_k=(1-q_bad(k)) delta_(B_0)+q_bad(k) delta_(B_1)

are normalized and full-support on the binary code. The entries increase with
$k$, hence the distribution genuinely varies with neighbor conditions.

The rule uses only neighbor count. Applying the same formula at every site is
translation covariant, and every proper cubic rotation merely permutes the
six neighbor slots. The runner enumerates all 64 binary neighbor patterns and
all 24 proper cubic rotations and verifies exact invariance.

The rule even has the additional symmetry

    q_bad(6-k)=1-q_bad(k).

Its odds are

    o_bad=(1/7,1/3,1/2,1,2,3,7),

whose successive ratios are not constant.

Now take adjacent sites whose other-neighbor counts are $a=0$ and $b=1$.
Starting at $00$:

- flip the $a$ endpoint, then the $b$ endpoint: $(1/7)(1/2)=1/14$;
- flip the $b$ endpoint, then the $a$ endpoint: $(1/3)(1/3)=1/9$.

The endpoint configuration is the same but the inferred weight ratio is not.
Theorem 1 therefore excludes a positive joint law having these kernels as its
simultaneous full conditionals.

This witness satisfies more local symmetry than the canonical wording
requires. It does not claim to be a complete model of Record formation,
because its precise purpose is to expose the missing local-to-global typing.

## 6. The Two Honest Semantics Of The Current Sentence

The current
[minimal axiom memo](MINIMAL_AXIOMS_2026-06-29.md) says that, for each site,
the probability distribution is determined by and varies with nearest-neighbor
conditions. It also says that Admissibility is not a dynamics axiom.

There are two mathematically distinct readings.

### Full-conditional reading

The local distribution is intended to be the conditional distribution of one
simultaneous joint configuration law. Then the square equations, or an
equivalent compatibility theorem, are mandatory. The hostile rule proves
that local normalization, variation, translation covariance, and proper-cubic
covariance do not imply them.

### Ordered update-kernel reading

The local distribution is applied when a site is selected to form or update,
conditional on the neighbors at that time. Any declared order can then
generate a path law even when the static full-conditionals are incompatible.
Different orders can give different laws; the $1/14$ versus $1/9$ square is
the smallest exact witness.

This reading is live. But the update order, scheduler, causal rule, and
formation rate are dynamics/history content, and the static Ising action does
not follow.

This steelman is accepted: the current sentence may be intended only as an
update-kernel contract. The theorem therefore does not call the axioms
inconsistent. It says that a static/global-law reading needs one additional
compatibility statement or a model-specific proof.

## 7. Exact Axiom-Side Residual

One sufficient candidate addition to Admissibility is:

> For every supplied finite set of Record-forming sites and exterior neighbor
> condition, there is at least one joint law on their locked possibilities
> whose one-site full conditional measures are the sitewise Admissibility
> distributions. These laws transform covariantly and belong to a
> projectively consistent family: they agree under marginal restriction of
> unfixed sites and conditional restriction by supplied exterior Records.
> This clause does not select the forming sites, their order or rate, one
> phase when several compatible families exist, or one realized member.

This is hypothetical wording only. It is not an edit, an adoption, a
recommendation, a necessity theorem, or a literal-minimality claim. Its first
sentence supplies finite full-conditional compatibility; its second supplies
the separate cross-region projectivity obligation.

On the strictly positive binary count-only sector, this clause composes with
Theorems 1 and 2 to derive:

- zero square curl;
- a unique finite joint law for each exterior condition;
- affine conditional log odds;
- a nearest-neighbor Ising-type action; and
- one action coupling if an independent code-swap symmetry is also supplied.

It does not derive:

- which M2(C) possibilities form the physical binary code;
- a global joint law for arbitrary continuous M2 kernels;
- projectivity from the current local clauses alone, rather than as the
  hypothetical addition above, or uniqueness/phase selection;
- a formation site, scheduler, order, rate, or causal time metric;
- an outcome/effect program, Born functional, or preparation quotient;
- a realized history or frequency/typicality bridge;
- a metric, curvature carrier, stress tensor, Newton coupling, or
  identification of this statistical action with gravity.

The alternative axiom policy is also honest: leave the canonical wording
sitewise and make compatibility/projective consistency an acceptance theorem
for every proposed exact law. The explicit local-to-global construction in
[Cycle 33](work_history/repo/review_feedback/LOCAL_TO_GLOBAL_CUBIC_PROCESS_GLUE_CYCLE33_NOTE_2026-07-14.md)
shows that this route can succeed architecture by architecture.

## 8. Consequence For The TOE Lanes

This block sharpens three lane boundaries without changing their fixed
scores.

| Lane | Exact consequence | Still open |
|---|---|---|
| operational quantum / records | sitewise laws and global record laws are separated; binary compatibility is decidable | physical binary code, formation process, complete protocol law |
| gravity / source / resources | a compatible count-only binary law derives an action instead of postulating action additivity | physical source/action identification, tensor response, coupling and scale |
| Born probability / realized history | one compatible spatial joint law is derivable on the declared finite binary sector | effect kernel, temporal process, realized member, frequencies |

The gravity gain is structural rather than physical: the source/action
bridge is reduced to a theorem once a compatible binary statistical sector
and its physical identification are supplied. The note does not call that
action gravity.

No current-axiom physical or autonomous obligation is retired, so the fixed
TOE percentages do not move.

## 9. Relation To Existing Sources

| Source location | Exact residual used | Use here | Not borrowed |
|---|---|---|---|
| [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) | one sitewise nearest-neighbor distribution; no dynamics | exact current wording under test | no global compatibility or action inferred |
| [Global-measure/menu separation](ADMISSIBILITY_GLOBAL_MEASURE_MENU_KERNEL_TYPE_SEPARATION_BOUNDED_THEOREM_NOTE_2026-08-10.md) | types the current object as a measure on one local M2 possibility domain | prevents confusing local-domain normalization with a lattice joint law | no Born kernel or global law borrowed |
| [Global history process law, Cycle 30](work_history/repo/review_feedback/GLOBAL_RECORD_HISTORY_PROCESS_LAW_CYCLE30_NOTE_2026-07-14.md) | projective consistency remains explicit for complete histories | preserves temporal/history boundary | no history law supplied |
| [Local-to-global cubic glue, Cycle 33](work_history/repo/review_feedback/LOCAL_TO_GLOBAL_CUBIC_PROCESS_GLUE_CYCLE33_NOTE_2026-07-14.md) | one exact architecture derives its global family by contraction | positive architecture-specific alternative | no generic compatibility theorem borrowed |
| [Source-action pricing, Cycle 871](SOURCE_ACTION_BRIDGE_PRICING_CYCLE871_BOUNDED_THEOREM_NOTE_2026-07-28.md) | readout-to-action/source-action identification is open | compares the derived binary action with the gravity wall | no physical gravity identity borrowed |
| [Finite sharp-record source intervention](SOURCE_MEASURE_RECORD_INTERVENTION_THEOREM_NOTE_2026-05-30.md) | a supplied finite record law has an RN action/score | positive statistical-action precedent | no continuous or global law borrowed |

The theorem and classification are proved here from finite odds algebra. No
literature theorem, observed value, fitted parameter, or external PR artifact
is load-bearing.

## 10. No-Go Discipline Gate

The bounded negative claim is only:

> Local normalization, neighbor-count variation, translation covariance,
> proper-cubic covariance, strict positivity, monotonicity, and even a
> code-swap symmetry do not force a count-only binary rule to be compatible
> full conditionals of one static positive joint law.

No axiom inconsistency, global-law impossibility, or gravity no-go is claimed.

### N1 — Materially Distinct Routes

| Route | Exact attack | Result | Marker |
|---|---|---|---|
| direct positive joint law | derive conditionals from arbitrary rational four-site weights | every square closes and path reconstruction returns the law | ATTEMPTED |
| square-curl reconstruction | impose all two-site squares and integrate odds | succeeds generally on every finite binary configuration hypercube | ATTEMPTED |
| count-only cubic classification | use independently variable endpoint environments | succeeds exactly; compatible odds are geometric | ATTEMPTED |
| highly symmetric hostile rule | add positivity, monotonicity and code-swap symmetry | still fails with $1/14 != 1/9$ | ATTEMPTED |
| ordered update process | interpret kernels temporally rather than as full conditionals | remains live; needs order/dynamics and may be order dependent | ATTEMPTED |
| architecture-specific process contraction | use a supplied CP/process rule and boundary | Cycle 33 remains a positive route | ATTEMPTED |
| direct global history law | supply one projectively consistent law first | remains live; compatibility is then a theorem/check on its conditionals | ATTEMPTED |
| multi-state/continuous specification | replace the binary test sector by full M2 kernels | open; no global negative is exported from the binary witness | ATTEMPTED |

### N2 — Wall Independence And Collapse

| Pair | First closes second? | Second closes first? | Disposition |
|---|---:|---:|---|
| finite full-conditional compatibility / finite-region restriction consistency | no: each boundary can be compatible while cross-volume marginals disagree | no: projective marginals need not expose declared full conditionals | distinct global-law checks |
| joint law / ordered formation dynamics | no: a static law supplies no scheduler | no: an ordered process need not have the declared static full conditionals | independent semantics |
| joint law / realized history | no: a measure does not select one member | no: one history does not identify all conditional weights | independent |
| statistical action / gravitational identification | no: minus log weight is not curvature or stress | no: a gravity name does not prove compatibility | independent |

The square theorem collapses all finite binary path-order checks to the local
two-site curl. It does not multiply the remaining walls.

### N3 — Hidden-Wall Scan

Load-bearing scope restrictions are explicit:

- finite site set;
- binary atomic subalphabet inside M2(C);
- strict positivity;
- full-conditional, not merely update-kernel, semantics;
- supplied exterior neighbor condition;
- count-only symmetry for the cubic classification; and
- no infinite-volume, temporal, actual-member, or gravity identification.

The primitive-registry scan used the current approved primitive list:
scale reference, kinetic isotropy, and realized-state reference. None supplies
joint-law compatibility, an update order, an action identification, or a
realized history value.

### N4 — Residual Matching

The source residual is the gap between a normalized distribution on each
one-site possibility domain and a compatible law across sites/histories.
The exact residual produced here is the nonzero square curl. These are the
same type boundary: a family of local conditionals is not yet one global law.

The gravity residual remains source/action identification. This note reduces
the action-shape side only on a declared compatible binary sector; it does not
claim to close the physical identification.

### N5 — Rhetoric Audit

The following stronger sentences are rejected:

- the four axioms are inconsistent;
- no global law can realize Admissibility;
- every covariant local rule is incompatible;
- compatibility forces an Ising action on the full M2 domain;
- the derived statistical action is gravity;
- a global measure selects its actual history; or
- the candidate wording is a necessary axiom.

The only shipped negative is witnessed by one exact count rule and the exact
$1/14$ versus $1/9$ square.

### N6 — Partial-Closure Scan

Positive content retained before the residual:

1. a necessary and sufficient finite binary compatibility theorem;
2. constructive recovery and uniqueness of the joint law;
3. reduction of local-to-global checking to adjacent squares;
4. a complete cubic count-only classification;
5. an explicit derived finite-region action;
6. a one-parameter reduction under separately supplied code-swap symmetry;
7. an exact compatible fixture; and
8. an exact hostile covariant fixture.

These results remain useful whether compatibility is placed in an axiom or
proved per model.

### N7 — Steelman

The strongest objection is:

> The phrase one fixed nearest-neighbor admissibility rule is naturally an
> update rule, not a declaration of simultaneous full conditionals. A
> sequential stochastic process always has a path law, so the hostile square
> does not refute the intended semantics.

This steelman is accepted. Under the update-kernel reading, the rule needs a
site-selection order, causal scheduler, and formation law. The two square
paths show that those choices can matter. The present theorem then becomes a
criterion for when order dependence disappears and a static action exists;
it is not an objection to the update interpretation.

### N8 — Cross-Cycle Echo

Earlier repo work repeatedly retires global-law content only after an exact
composition theorem:

- Cycle 30 keeps projective consistency explicit for history laws;
- Cycle 33 derives it for one supplied cubic process;
- Cycle 21 requires a consistent stationary corpus before Birkhoff applies;
- the source-measure packet derives RN actions only after a probability law
  exists.

The present result follows the same pattern at the site-conditional layer.
It does not turn the recurrence of this pattern into a universal no-go.

### Gate Result

PASS for the narrow finite binary statement and the displayed hostile rule.

FAIL / DO NOT SHIP for any claim of axiom inconsistency, universal
non-derivability, full-M2 Gibbs classification, autonomous dynamics,
realized-history selection, or gravity closure.

## 11. Verification

Run:

    python3 scripts/admissibility_binary_full_conditional_compatibility_ising_action_axiom_boundary_2026_08_10.py

The runner checks:

- the source-bound canonical and predecessor wording;
- exact general joint-to-conditionals square closure;
- path reconstruction and normalized uniqueness;
- a live one-entry mutation and path-order failure;
- rank five of the seven-logit constraint system;
- compatible geometric odds and code-swap symmetry;
- the hostile rational rule and $1/14$ versus $1/9$ mismatch;
- all 24 proper cubic rotations on all 64 neighbor patterns;
- exact finite-action conditional recovery; and
- governance, trace, axiom-nonmutation, and N1--N8 needles.

Expected final line:

    TOTAL: PASS=... FAIL=0

## Boundary Verdict

The finite binary local-to-global seam is solved mathematically:

    compatible full conditionals
      iff zero square curl
      iff path-independent joint weights.

On the cubic count-only sector:

    compatibility
      iff geometric conditional odds
      iff affine logit
      iff nearest-neighbor Ising-type finite action.

The current axiom memo states the local kernels but does not explicitly choose
between full-conditional compatibility and an ordered update process. The
candidate compatibility sentence above is sufficient if the owner wants the
former semantics at foundation level. Otherwise every exact physical law
must prove the corresponding global consistency itself.

No canonical axiom is edited. No percentage moves.
