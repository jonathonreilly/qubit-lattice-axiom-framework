---
claim_id: support_drop_why_face8_fails_b12_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Lex-first shortest paths to (8,0,0) and (4,4,0) under the named support-drop hop-cost on B_12(0) are named. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/support_drop_why_face8_fails_b12_2026_08_15.py
---

# Lex-First Shortest Paths For The Face-8 Reverse Failure On B_12(0)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one directed Dijkstra on the nearest-neighbor graph of the
ball $B_{12}(0)=\{v\in\mathbb{Z}^3:|v|_1\le 12\}$ for the named support-drop
hop-cost $\nu$. Lex-first shortest paths to $(8,0,0)$ and $(4,4,0)$ are
named, together with the hop that makes $t(8,0,0)=14$ and $t(4,4,0)=10$.
Displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/support_drop_why_face8_fails_b12_2026_08_15.py`](../scripts/support_drop_why_face8_fails_b12_2026_08_15.py)
**Cache:** none. `cache_write: false`.

## Result Up Front

On $B_{12}(0)$ the named support-drop hop-cost $\nu$ gives
$t(8,0,0)=14$ and $t(4,4,0)=10$. Those two integers are
not leftover of the yes/no reverse bit. This note names a lex-first
shortest path to each site and the hop that produces those times.

Let $\sigma_v=\{i\in\{1,2,3\}:v_i\neq 0\}$ and write $|\sigma_v|$ for its
cardinality. On every nearest-neighbor hop $v\to w$ that remains inside
$B_{12}(0)$, the named support-drop hop-cost is

$$
\nu(v\to w)=
\begin{cases}
3 & \text{if }|\sigma_v|=0\text{ or }(|\sigma_v|=|\sigma_w|=1)\text{ or }|\sigma_w|<|\sigma_v|,\\
1 & \text{otherwise.}
\end{cases}
$$

Arrival $t(v)$ is the least $\nu$-length of a directed path from $0$ to $v$
in the in-ball nearest-neighbor graph. Among all such least-length paths,
the lex-first path is the sequence of sites that is lexicographically least
when sites are compared as integer triples $(x,y,z)$.
Uniqueness of a shortest path is not claimed and is not required.
The lex-first representative is the order-least sequence, not a uniqueness
statement about $\nu$.

One Dijkstra from the origin returns $t(8,0,0)=14$ and $t(4,4,0)=10$. The
lex-first shortest path to $(8,0,0)$ is

$0\to(0,-1,0)\to(1,-1,0)\to(2,-1,0)\to(3,-1,0)\to(4,-1,0)\to(5,-1,0)\to(6,-1,0)\to(7,-1,0)\to(8,-1,0)\to(8,0,0)$.

Its hop-costs are $3,1,1,1,1,1,1,1,1,3$ and its running-cost sequence is
$3,4,5,6,7,8,9,10,11,14$. The last hop $(8,-1,0)\to(8,0,0)$ is a support
drop ($|\sigma|=2\to 1$), so $\nu=3$. That hop takes the running cost from
$11$ to $14$ and is the hop that makes $t(8,0,0)=14$.

The lex-first shortest path to $(4,4,0)$ is

$0\to(0,1,0)\to(1,1,0)\to(1,2,0)\to(1,3,0)\to(1,4,0)\to(2,4,0)\to(3,4,0)\to(4,4,0)$.

Its hop-costs are $3,1,1,1,1,1,1,1$ and its running-cost sequence is
$3,4,5,6,7,8,9,10$. The last hop $(3,4,0)\to(4,4,0)$ stays at $|\sigma|=2$,
so $\nu=1$. That hop takes the running cost from $9$ to $10$ and is the hop
that makes $t(4,4,0)=10$. Together these last hops give
$t(8,0,0)=t(4,4,0)=14/10$.

The displayed comparison for this pair is

$32\,t(8,0,0)^2=6272<6400=64\,t(4,4,0)^2$.

The inequality holds. It is the fail: $t^2/|v|_2^2$ is not strictly smaller
at the more-diagonal site $(4,4,0)$ than at $(8,0,0)$. The inequality is
displayed, not adopted.

The score is displayed, not adopted. Do not write $\nu$ into Admissibility.
Do not attach L1.

## Current Premise Boundary

The Lattice and Admissibility premises are quoted from
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md):

Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
adjacency, standard translations, and proper cubic rotations about each site.

There is one fixed nearest-neighbor admissibility rule, covariant under lattice
translations and proper cubic rotations.

For each site, the probability distribution over the possibilities is
determined by, and varies with, the nearest-neighbor conditions.

Admissibility is not a dynamics axiom. It does not choose a Hamiltonian or
transfer operator, supply transition-probability or weight values, select a
scalar or nonzero kinetic branch, assert a Dirac-square carrier, define a time
metric, or provide a record-production process or physical persistence
dynamics.

The current Record boundary is:

When present, a record locks exactly one admissible local possibility.

A readout value is determined by record content alone.

A site with no record cannot be read.

The named hop-cost $\nu$ is a displayed scoring rule on the nearest-neighbor
graph of $B_{12}(0)$. It is not written into Admissibility. It is not attached to L1.
It supplies no time metric, no Record formation rule, and no physical hop law.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Lex-first shortest paths and running-cost sequences to (8,0,0) and (4,4,0) on B_12(0) are finite exact Dijkstra objects for a named hop-cost; the hop-cost is displayed, not adopted."
trace_class: frontier_discovery
target_claim_id: support_drop_why_face8_fails_b12_bounded_theorem_note_2026-08-15
target_blocker_text: "the named hop-cost is displayed, not adopted, and is not Admissibility content"
source_of_blocker_text: this note
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Keep the lex-first paths as a displayed B_12(0) score; do not write nu into Admissibility."
conditional_surface_status: "exact for the named support-drop hop-cost on B_12(0); not adopted as a law"
hypothetical_axiom_status: no edit
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Write $0=(0,0,0)$ and $B_{12}(0)=\{v\in\mathbb{Z}^3:|v|_1\le 12\}$. This set has
$2625$ sites, of which $2624$ are nonzero. The directed graph is the
nearest-neighbor graph of $\mathbb{Z}^3$ induced on $B_{12}(0)$: from $v$ there
is an edge to $w=v\pm e_i$ exactly when $w\in B_{12}(0)$.

The support $\sigma_v$ and the hop-cost $\nu$ are as in Result Up Front. In
words: seed exit from the origin costs $3$; every hop that stays on a
coordinate axis costs $3$; every hop that strictly drops the number of
nonzero coordinates costs $3$; every other in-ball nearest-neighbor hop
costs $1$.

A site sequence $p=(p_0,\ldots,p_k)$ is a directed path from $0$ to $v$ when
$p_0=0$, $p_k=v$, and each $p_i\to p_{i+1}$ is an in-ball nearest-neighbor
hop. Its $\nu$-length is $\sum_{i=0}^{k-1}\nu(p_i\to p_{i+1})$. The running-cost
sequence is the partial sums of those hop-costs. The path is shortest when
its $\nu$-length equals $t(v)$. Among shortest paths, lex-first means the
least sequence in the dictionary order of integer triples.

One Dijkstra computation from the origin, with heap key
$(\text{cost},\text{path})$, produces every $t(v)$ used below and the
lex-first path to each target. No second Dijkstra is run.

## Theorem 1 — Arrivals And Lex-First Shortest Paths

On $B_{12}(0)$ under $\nu$,

$$
t(8,0,0)=14,\qquad t(4,4,0)=10.
$$

These two values are Dijkstra outputs, not fitted scalars.

A lex-first shortest path to $(8,0,0)$ is

$0\to(0,-1,0)\to(1,-1,0)\to(2,-1,0)\to(3,-1,0)\to(4,-1,0)\to(5,-1,0)\to(6,-1,0)\to(7,-1,0)\to(8,-1,0)\to(8,0,0)$.

A lex-first shortest path to $(4,4,0)$ is

$0\to(0,1,0)\to(1,1,0)\to(1,2,0)\to(1,3,0)\to(1,4,0)\to(2,4,0)\to(3,4,0)\to(4,4,0)$.

The last hop $(8,-1,0)\to(8,0,0)$ is the support-drop hop that makes
$t(8,0,0)=14$. The last hop $(3,4,0)\to(4,4,0)$ is the support-preserving
hop that makes $t(4,4,0)=10$. Those two last hops are the hop pair that
makes $t(8,0,0)=t(4,4,0)=14/10$.

## Theorem 2 — Running-Cost Sequences And The Displayed Fail

The hop-cost sequence along the lex-first path to $(8,0,0)$ is
$3,1,1,1,1,1,1,1,1,3$. The running-cost sequence is
$3,4,5,6,7,8,9,10,11,14$.

The hop-cost sequence along the lex-first path to $(4,4,0)$ is
$3,1,1,1,1,1,1,1$. The running-cost sequence is
$3,4,5,6,7,8,9,10$.

The Euclidean squared lengths are $|(8,0,0)|_2^2=64$ and $|(4,4,0)|_2^2=32$.
The displayed comparison is whether

$32\,t(8,0,0)^2<64\,t(4,4,0)^2$.

Substituting the computed times gives $32\cdot 196=6272$ and
$64\cdot 100=6400$, so

$32\,t(8,0,0)^2=6272<6400=64\,t(4,4,0)^2$.

The inequality holds. It is the fail for this pair: arrival per Euclidean
squared length is not smaller at $(4,4,0)$ than at $(8,0,0)$. The comparison
is displayed, not adopted.

## Theorem 3 — Not Admissibility, Not Attached To L1

Do not write $\nu$ into Admissibility. Admissibility names one fixed
nearest-neighbor rule for the local possibility distribution. It does not
supply hop weights, a time metric, or an arrival-time comparison.

Do not attach L1. The named hop-cost is not attached to L1 and is not
offered as a replacement for unit-cost first arrival. No uniqueness claim is
made among hop-costs. Uniqueness of a shortest path is not required.

## What This Note Does Not Claim

- $\nu$ is not an axiom, not an approved primitive, and not a derived law.
- The lex-first paths are not promoted to a continuum speed, a physical clock,
  or a Record readout.
- The fail inequality is not claimed outside $B_{12}(0)$ and is not claimed
  for any hop-cost other than the named $\nu$.
- L1 is not adopted and is not attached to Admissibility.
- The yes/no reverse bit is not reused as a substitute for the named paths.
  The residual is not leftover of the yes/no bit.
- Shortest paths are not claimed unique.

## claim_scope

Lex-first shortest paths to (8,0,0) and (4,4,0) under the named support-drop hop-cost on B_12(0) are named. Displayed, not adopted.
