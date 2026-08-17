---
claim_id: support_drop_face_reverse_vs_k_b12_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Face-diagonal reverse versus integer scale k under the named support-drop hop-cost on B_12(0) is reported for k=1..6. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/support_drop_face_reverse_vs_k_b12_2026_08_15.py
---

# Face-Diagonal Reverse Versus Integer Scale k Under The Support-Drop Hop-Cost On B_12(0)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one directed Dijkstra on the nearest-neighbor graph of the
ball $B_{12}(0)=\{v\in\mathbb{Z}^3:|v|_1\le 12\}$ for the named support-drop
hop-cost $\nu$. Face-diagonal reverse versus integer scale $k$ is reported
for $k=1,\ldots,6$. Displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/support_drop_face_reverse_vs_k_b12_2026_08_15.py`](../scripts/support_drop_face_reverse_vs_k_b12_2026_08_15.py)
**Cache:** none. `cache_write: false`.

## Result Up Front

The same named support-drop hop-cost $\nu$ already scored on the four named
pairs of the $B_{12}(0)$ face-diagonal census is scored here against integer
scale $k$ for every pair $((2k,0,0),(k,k,0))$ with $k=1,\ldots,6$. The six
bits are not leftover of those four named pairs: the pairs at $k=1,3,5$ are
not among them, and the $k=5$ fail is not a restatement of the $k=4$ fail.
The $k=1,3,5$ times are independent Dijkstra outputs on $B_{12}(0)$.

Let $\sigma_v=\{i\in\{1,2,3\}:v_i\neq 0\}$ and write $|\sigma_v|$ for its
cardinality. On every nearest-neighbor hop $v\to w$ that remains inside
$B_{12}(0)=\{v\in\mathbb{Z}^3:|v|_1\le 12\}$, the named support-drop hop-cost is

$$
\nu(v\to w)=
\begin{cases}
3 & \text{if }|\sigma_v|=0\text{ or }(|\sigma_v|=|\sigma_w|=1)\text{ or }|\sigma_w|<|\sigma_v|,\\
1 & \text{otherwise.}
\end{cases}
$$

A single Dijkstra computation from the origin on this directed weighted graph
returns the arrival times

$$
t(2,0,0)=6,\qquad t(4,0,0)=10,\qquad t(6,0,0)=12,
$$
$$
t(8,0,0)=14,\qquad t(10,0,0)=16,\qquad t(12,0,0)=20,
$$
$$
t(1,1,0)=4,\qquad t(2,2,0)=6,\qquad t(3,3,0)=8,
$$
$$
t(4,4,0)=10,\qquad t(5,5,0)=12,\qquad t(6,6,0)=14.
$$

For each $k=1,\ldots,6$, reverse means the displayed comparison

$$
\frac{t(2k,0,0)^2}{4k^2}>\frac{t(k,k,0)^2}{2k^2}
$$

holds, equivalently $t(k,k,0)^2\cdot 4k^2<t(2k,0,0)^2\cdot 2k^2$. The bit is
displayed, not adopted.

| $k$ | pair | axis $t^2/|v|_2^2$ | face $t^2/|v|_2^2$ | reverse |
|---|---|---|---|---|
| $1$ | $((2,0,0),(1,1,0))$ | $36/4=9$ | $16/2=8$ | yes |
| $2$ | $((4,0,0),(2,2,0))$ | $100/16=25/4$ | $36/8=9/2$ | yes |
| $3$ | $((6,0,0),(3,3,0))$ | $144/36=4$ | $64/18=32/9$ | yes |
| $4$ | $((8,0,0),(4,4,0))$ | $196/64=49/16$ | $100/32=25/8$ | no |
| $5$ | $((10,0,0),(5,5,0))$ | $256/100=64/25$ | $144/50=72/25$ | no |
| $6$ | $((12,0,0),(6,6,0))$ | $400/144=25/9$ | $196/72=49/18$ | yes |

Exact integer comparisons:

- $4\,t(1,1,0)^2=64<72=2\,t(2,0,0)^2$
- $16\,t(2,2,0)^2=576<800=8\,t(4,0,0)^2$
- $36\,t(3,3,0)^2=2304<2592=18\,t(6,0,0)^2$
- $64\,t(4,4,0)^2=6400>6272=32\,t(8,0,0)^2$
- $100\,t(5,5,0)^2=14400>12800=50\,t(10,0,0)^2$
- $144\,t(6,6,0)^2=28224<28800=72\,t(12,0,0)^2$

The reverse bit is therefore not the same for every $k=1,\ldots,6$. The fail
is not isolated at $k=4$: reverse fails at $k=4$ and $k=5$, and holds at
$k=1,2,3,6$. These six bits are not leftover of the four named pairs. The
score is displayed, not adopted. Do not attach L1.

## Current Premise Boundary

The Lattice and Admissibility premises are quoted from
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md):

Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor adjacency, standard translations, and proper cubic rotations about each site.

There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations.

For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.

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
claim_type_reason: "Arrival times and six face-versus-axis reverse bits versus integer scale k on B_12(0) are finite exact Dijkstra values for a named hop-cost; the hop-cost is displayed, not adopted."
trace_class: upstream_support
target_claim_id: support_drop_face_reverse_vs_k_b12_bounded_theorem_note_2026-08-15
target_blocker_text: "the named hop-cost is displayed, not adopted, and is not Admissibility content"
source_of_blocker_text: this note
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Keep the face-versus-axis reverse bits versus k as a displayed B_12(0) score; do not write nu into Admissibility."
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

Arrival time $t(v)$ is the least $\nu$-length of a directed path from $0$ to
$v$ in this graph. One Dijkstra computation from the origin produces every
$t(v)$ used below.

The Euclidean squared length is $|v|_2^2=v_1^2+v_2^2+v_3^2$. The displayed
comparison density is $t(v)^2/|v|_2^2$ at $v\neq 0$. For each integer
$k=1,\ldots,6$ the ordered pair is $((2k,0,0),(k,k,0))$. The second site is
the more-diagonal site (strictly more nonzero coordinates). The pair is
reverse when

$$
t(k,k,0)^2\cdot|(2k,0,0)|_2^2 < t(2k,0,0)^2\cdot|(k,k,0)|_2^2,
$$

which is the same comparison as $t(2k,0,0)^2/(4k^2)>t(k,k,0)^2/(2k^2)$.

The four named pairs of the prior $B_{12}(0)$ face-diagonal census are
$((4,0,0),(2,2,0))$, $((8,0,0),(4,4,0))$, $((12,0,0),(6,6,0))$, and
$((4,0,0),(2,2,2))$. Those pairs cover only $k=2,4,6$ among the face pairs
and one body pair. They do not determine $t(2,0,0)$, $t(1,1,0)$, $t(6,0,0)$,
$t(3,3,0)$, $t(10,0,0)$, or $t(5,5,0)$. The $k=1,\ldots,6$ table is therefore
not leftover of the four named pairs.

## Theorem 1 — Named Arrival Times At Each Scale

On $B_{12}(0)$ under $\nu$, for each $k=1,\ldots,6$,

$$
\begin{align*}
t(2,0,0)&=6,& t(1,1,0)&=4,\\
t(4,0,0)&=10,& t(2,2,0)&=6,\\
t(6,0,0)&=12,& t(3,3,0)&=8,\\
t(8,0,0)&=14,& t(4,4,0)&=10,\\
t(10,0,0)&=16,& t(5,5,0)&=12,\\
t(12,0,0)&=20,& t(6,6,0)&=14.
\end{align*}
$$

These twelve values are Dijkstra outputs, not fitted scalars.

Witnessing paths of those $\nu$-costs exist. The walk

$0\to(1,0,0)\to(2,0,0)$

has hop-costs $3,3$ and sum $6$. The walk

$0\to(1,0,0)\to(1,1,0)$

has hop-costs $3,1$ and sum $4$. The walk

$0\to(1,0,0)\to(1,1,0)\to(2,1,0)\to(3,1,0)\to(4,1,0)\to(4,0,0)$

has hop-costs $3,1,1,1,1,3$ and sum $10$. The walk

$0\to(1,0,0)\to(1,1,0)\to(1,2,0)\to(2,2,0)$

has hop-costs $3,1,1,1$ and sum $6$. The walk

$0\to(1,0,0)\to(1,1,0)\to(2,1,0)\to(3,1,0)\to(4,1,0)\to(5,1,0)\to(6,1,0)\to(6,0,0)$

has hop-costs $3,1,1,1,1,1,1,3$ and sum $12$. The walk

$0\to(1,0,0)\to(1,1,0)\to(1,2,0)\to(1,3,0)\to(2,3,0)\to(3,3,0)$

has hop-costs $3,1,1,1,1,1$ and sum $8$. The walk

$0\to(1,0,0)\to(1,1,0)\to(2,1,0)\to(3,1,0)\to(4,1,0)\to(5,1,0)\to(6,1,0)\to(7,1,0)\to(8,1,0)\to(8,0,0)$

has hop-costs $3,1,1,1,1,1,1,1,1,3$ and sum $14$. The walk

$0\to(1,0,0)\to(1,1,0)\to(1,2,0)\to(1,3,0)\to(1,4,0)\to(2,4,0)\to(3,4,0)\to(4,4,0)$

has hop-costs $3,1,1,1,1,1,1,1$ and sum $10$. The walk

$0\to(1,0,0)\to(1,1,0)\to(2,1,0)\to(3,1,0)\to(4,1,0)\to(5,1,0)\to(6,1,0)\to(7,1,0)\to(8,1,0)\to(9,1,0)\to(10,1,0)\to(10,0,0)$

has hop-costs $3,1,1,1,1,1,1,1,1,1,1,3$ and sum $16$. The walk

$0\to(1,0,0)\to(1,1,0)\to(1,2,0)\to(1,3,0)\to(1,4,0)\to(1,5,0)\to(2,5,0)\to(3,5,0)\to(4,5,0)\to(5,5,0)$

has hop-costs $3,1,1,1,1,1,1,1,1,1$ and sum $12$. The walk

$0\to(1,0,0)\to(1,1,0)\to(2,1,0)\to(3,1,0)\to(4,1,0)\to(5,1,0)\to(6,1,0)\to(7,1,0)\to(8,1,0)\to(9,1,0)\to(10,1,0)\to(11,1,0)\to(11,0,0)\to(12,0,0)$

has hop-costs $3,1,1,1,1,1,1,1,1,1,1,1,3,3$ and sum $20$. The walk

$0\to(1,0,0)\to(1,1,0)\to(1,2,0)\to(1,3,0)\to(1,4,0)\to(1,5,0)\to(1,6,0)\to(2,6,0)\to(3,6,0)\to(4,6,0)\to(5,6,0)\to(6,6,0)$

has hop-costs $3,1,1,1,1,1,1,1,1,1,1,1$ and sum $14$.

## Theorem 2 — Reverse Bit Versus Integer Scale k

For each $k=1,\ldots,6$ the displayed comparison is whether
$t(2k,0,0)^2/(4k^2)>t(k,k,0)^2/(2k^2)$. The six bits are:

- $k=1$: $t(1,1,0)^2/|(1,1,0)|_2^2=8<9=t(2,0,0)^2/|(2,0,0)|_2^2$ (yes)
- $k=2$: $t(2,2,0)^2/|(2,2,0)|_2^2=9/2<25/4=t(4,0,0)^2/|(4,0,0)|_2^2$ (yes)
- $k=3$: $t(3,3,0)^2/|(3,3,0)|_2^2=32/9<4=t(6,0,0)^2/|(6,0,0)|_2^2$ (yes)
- $k=4$: $t(4,4,0)^2/|(4,4,0)|_2^2=25/8\not<49/16=t(8,0,0)^2/|(8,0,0)|_2^2$ (no)
- $k=5$: $t(5,5,0)^2/|(5,5,0)|_2^2=72/25\not<64/25=t(10,0,0)^2/|(10,0,0)|_2^2$ (no)
- $k=6$: $t(6,6,0)^2/|(6,6,0)|_2^2=49/18<25/9=t(12,0,0)^2/|(12,0,0)|_2^2$ (yes)

The fail is not isolated at $k=4$. The four named pairs do not determine the
$k=1,3,5$ times or the $k=5$ fail.

These reverse bits are displayed, not adopted.

## Theorem 3 — Not Admissibility, Not Attached To L1

Do not write $\nu$ into Admissibility. Admissibility names one fixed
nearest-neighbor rule for the local possibility distribution. It does not
supply hop weights, a time metric, or an arrival-time comparison.

Do not attach L1. The named hop-cost is not attached to L1 and is not
offered as a replacement for unit-cost first arrival. No uniqueness claim is
made among hop-costs.

## What This Note Does Not Claim

- $\nu$ is not an axiom, not an approved primitive, and not a derived law.
- The reverse bits are not promoted to a continuum speed, a physical clock,
  or a Record readout.
- Face-diagonal reverse versus $k$ is not claimed outside $B_{12}(0)$ and is
  not claimed for any hop-cost other than the named $\nu$.
- L1 is not adopted and is not attached to Admissibility.
- The four named pairs of the prior face-diagonal census are not reused as a
  substitute for the six-scale Dijkstra table.

## claim_scope

Face-diagonal reverse versus integer scale k under the named support-drop hop-cost on B_12(0) is reported for k=1..6. Displayed, not adopted.
