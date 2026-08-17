---
claim_id: support_drop_body_reverse_vs_k_b16_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Body-diagonal reverse versus integer scale k under the named support-drop hop-cost on B_16(0) is reported for k=1..5. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/support_drop_body_reverse_vs_k_b16_2026_08_15.py
---

# Body-Diagonal Reverse Versus Integer Scale k Under The Support-Drop Hop-Cost On B_16(0)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one directed Dijkstra on the nearest-neighbor graph of the
ball $B_{16}(0)=\{v\in\mathbb{Z}^3:|v|_1\le 16\}$ for the named support-drop
hop-cost $\nu$. Body-diagonal reverse versus integer scale $k$ is reported
for $k=1,\ldots,5$. Displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/support_drop_body_reverse_vs_k_b16_2026_08_15.py`](../scripts/support_drop_body_reverse_vs_k_b16_2026_08_15.py)
**Cache:** none. `cache_write: false`.

## Result Up Front

The same named support-drop hop-cost $\nu$ already scored on $B_{12}(0)$ for
$k=1,\ldots,4$ (bits yes/yes/no/no) is scored here independently on
$B_{16}(0)$ against integer scale $k$ for every pair $((2k,0,0),(k,k,k))$
with $k=1,\ldots,5$. The five bits are not leftover of the $B_{12}(0)$
body-versus-$k$ table: the site $(5,5,5)$ has $|v|_1=15$ and therefore lies
outside $B_{12}(0)$. The $k=5$ times are independent Dijkstra outputs on
$B_{16}(0)$. A larger ball cheapens some axis arrivals — the same one
Dijkstra returns $t(12,0,0)=18$, not the $B_{12}(0)$ wall value $20$ — but
that cheapening does not change the $k=1,\ldots,4$ body-reverse bits.

Let $\sigma_v=\{i\in\{1,2,3\}:v_i\neq 0\}$ and write $|\sigma_v|$ for its
cardinality. On every nearest-neighbor hop $v\to w$ that remains inside
$B_{16}(0)=\{v\in\mathbb{Z}^3:|v|_1\le 16\}$, the named support-drop hop-cost is

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
t(2,0,0)=6,\qquad t(4,0,0)=10,\qquad t(6,0,0)=12,\qquad t(8,0,0)=14,\qquad t(10,0,0)=16,
$$
$$
t(1,1,1)=5,\qquad t(2,2,2)=8,\qquad t(3,3,3)=11,\qquad t(4,4,4)=14,\qquad t(5,5,5)=17.
$$

For each $k=1,\ldots,5$, reverse means the displayed comparison

$$
12\,t(2k,0,0)^2>16\,t(k,k,k)^2
$$

holds, equivalently $t(2k,0,0)^2/(4k^2)>t(k,k,k)^2/(3k^2)$. The bit is
displayed, not adopted.

| $k$ | pair | axis $t^2/|v|_2^2$ | body $t^2/|v|_2^2$ | reverse |
|---|---|---|---|---|
| $1$ | $((2,0,0),(1,1,1))$ | $36/4=9$ | $25/3$ | yes |
| $2$ | $((4,0,0),(2,2,2))$ | $100/16=25/4$ | $64/12=16/3$ | yes |
| $3$ | $((6,0,0),(3,3,3))$ | $144/36=4$ | $121/27$ | no |
| $4$ | $((8,0,0),(4,4,4))$ | $196/64=49/16$ | $196/48=49/12$ | no |
| $5$ | $((10,0,0),(5,5,5))$ | $256/100=64/25$ | $289/75$ | no |

Exact integer comparisons:

- $12\,t(2,0,0)^2=432>400=16\,t(1,1,1)^2$
- $12\,t(4,0,0)^2=1200>1024=16\,t(2,2,2)^2$
- $12\,t(6,0,0)^2=1728<1936=16\,t(3,3,3)^2$
- $12\,t(8,0,0)^2=2352<3136=16\,t(4,4,4)^2$
- $12\,t(10,0,0)^2=3072<4624=16\,t(5,5,5)^2$

The reverse bit is therefore not the same for every $k=1,\ldots,5$. Reverse
holds at $k=1,2$ and fails at $k=3,4,5$. The first four bits match the
$B_{12}(0)$ body-versus-$k$ table. The $k=5$ fail is new: $(5,5,5)$ is not
in $B_{12}(0)$. These five bits are not leftover of the $B_{12}(0)$ table.
The score is displayed, not adopted. Do not attach L1.

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
graph of $B_{16}(0)$. It is not written into Admissibility. It is not attached to L1.
It supplies no time metric, no Record formation rule, and no physical hop law.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Arrival times and five body-versus-axis reverse bits versus integer scale k on B_16(0) are finite exact Dijkstra values for a named hop-cost; the hop-cost is displayed, not adopted."
trace_class: upstream_support
target_claim_id: support_drop_body_reverse_vs_k_b16_bounded_theorem_note_2026-08-15
target_blocker_text: "the named hop-cost is displayed, not adopted, and is not Admissibility content"
source_of_blocker_text: this note
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Keep the body-versus-axis reverse bits versus k as a displayed B_16(0) score; do not write nu into Admissibility."
conditional_surface_status: "exact for the named support-drop hop-cost on B_16(0); not adopted as a law"
hypothetical_axiom_status: no edit
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Write $0=(0,0,0)$ and $B_{16}(0)=\{v\in\mathbb{Z}^3:|v|_1\le 16\}$. This set has
$6017$ sites, of which $6016$ are nonzero. The directed graph is the
nearest-neighbor graph of $\mathbb{Z}^3$ induced on $B_{16}(0)$: from $v$ there
is an edge to $w=v\pm e_i$ exactly when $w\in B_{16}(0)$.

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
$k=1,\ldots,5$ the ordered pair is $((2k,0,0),(k,k,k))$. The second site is
the more-diagonal site (strictly more nonzero coordinates). The pair is
reverse when

$$
12\,t(2k,0,0)^2>16\,t(k,k,k)^2,
$$

which is the same comparison as $t(2k,0,0)^2/(4k^2)>t(k,k,k)^2/(3k^2)$.

The $B_{12}(0)$ body-versus-$k$ table covers only $k=1,\ldots,4$. It does not
contain $(5,5,5)$. The $k=1,\ldots,5$ table is therefore not leftover of the
$B_{12}(0)$ body-versus-$k$ bits.

## Theorem 1 — Named Arrival Times At Each Scale

On $B_{16}(0)$ under $\nu$, for each $k=1,\ldots,5$,

$$
\begin{align*}
t(2,0,0)&=6,& t(1,1,1)&=5,\\
t(4,0,0)&=10,& t(2,2,2)&=8,\\
t(6,0,0)&=12,& t(3,3,3)&=11,\\
t(8,0,0)&=14,& t(4,4,4)&=14,\\
t(10,0,0)&=16,& t(5,5,5)&=17.
\end{align*}
$$

These ten values are Dijkstra outputs, not fitted scalars.

Witnessing paths of those $\nu$-costs exist. The walk

$0\to(1,0,0)\to(2,0,0)$

has hop-costs $3,3$ and sum $6$. The walk

$0\to(1,0,0)\to(1,1,0)\to(1,1,1)$

has hop-costs $3,1,1$ and sum $5$. The walk

$0\to(1,0,0)\to(1,1,0)\to(2,1,0)\to(3,1,0)\to(4,1,0)\to(4,0,0)$

has hop-costs $3,1,1,1,1,3$ and sum $10$. The walk

$0\to(1,0,0)\to(1,1,0)\to(1,1,1)\to(2,1,1)\to(2,2,1)\to(2,2,2)$

has hop-costs $3,1,1,1,1,1$ and sum $8$. The walk

$0\to(1,0,0)\to(1,1,0)\to(2,1,0)\to(3,1,0)\to(4,1,0)\to(5,1,0)\to(6,1,0)\to(6,0,0)$

has hop-costs $3,1,1,1,1,1,1,3$ and sum $12$. The walk

$0\to(1,0,0)\to(1,1,0)\to(1,1,1)\to(2,1,1)\to(2,2,1)\to(2,2,2)\to(3,2,2)\to(3,3,2)\to(3,3,3)$

has hop-costs $3,1,1,1,1,1,1,1,1$ and sum $11$. The walk

$0\to(1,0,0)\to(1,1,0)\to(2,1,0)\to(3,1,0)\to(4,1,0)\to(5,1,0)\to(6,1,0)\to(7,1,0)\to(8,1,0)\to(8,0,0)$

has hop-costs $3,1,1,1,1,1,1,1,1,3$ and sum $14$. The walk

$0\to(1,0,0)\to(1,1,0)\to(1,1,1)\to(2,1,1)\to(2,2,1)\to(2,2,2)\to(3,2,2)\to(3,3,2)\to(3,3,3)\to(4,3,3)\to(4,4,3)\to(4,4,4)$

has hop-costs $3,1,1,1,1,1,1,1,1,1,1,1$ and sum $14$. The walk

$0\to(1,0,0)\to(1,1,0)\to(2,1,0)\to(3,1,0)\to(4,1,0)\to(5,1,0)\to(6,1,0)\to(7,1,0)\to(8,1,0)\to(9,1,0)\to(10,1,0)\to(10,0,0)$

has hop-costs $3,1,1,1,1,1,1,1,1,1,1,3$ and sum $16$. The walk

$0\to(1,0,0)\to(1,1,0)\to(1,1,1)\to(2,1,1)\to(2,2,1)\to(2,2,2)\to(3,2,2)\to(3,3,2)\to(3,3,3)\to(4,3,3)\to(4,4,3)\to(4,4,4)\to(5,4,4)\to(5,5,4)\to(5,5,5)$

has hop-costs $3,1,1,1,1,1,1,1,1,1,1,1,1,1,1$ and sum $17$.

The site $(5,5,5)$ is not in $B_{12}(0)$.

## Theorem 2 — Reverse Bit Versus Integer Scale k

For each $k=1,\ldots,5$ the displayed comparison is whether
$12\,t(2k,0,0)^2>16\,t(k,k,k)^2$. The five bits are:

- $k=1$: $t(1,1,1)^2/|(1,1,1)|_2^2=25/3<9=t(2,0,0)^2/|(2,0,0)|_2^2$ (yes)
- $k=2$: $t(2,2,2)^2/|(2,2,2)|_2^2=16/3<25/4=t(4,0,0)^2/|(4,0,0)|_2^2$ (yes)
- $k=3$: $t(3,3,3)^2/|(3,3,3)|_2^2=121/27\not<4=t(6,0,0)^2/|(6,0,0)|_2^2$ (no)
- $k=4$: $t(4,4,4)^2/|(4,4,4)|_2^2=49/12\not<49/16=t(8,0,0)^2/|(8,0,0)|_2^2$ (no)
- $k=5$: $t(5,5,5)^2/|(5,5,5)|_2^2=289/75\not<64/25=t(10,0,0)^2/|(10,0,0)|_2^2$ (no)

Reverse holds at $k=1,2$ and fails at $k=3,4,5$. The $B_{12}(0)$ table does
not determine the $k=5$ fail on this ball.

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
- Body-diagonal reverse versus $k$ is not claimed outside $B_{16}(0)$ and is
  not claimed for any hop-cost other than the named $\nu$.
- L1 is not adopted and is not attached to Admissibility.
- The $B_{12}(0)$ body-versus-$k$ table is not reused as a substitute for
  the five-scale Dijkstra table on $B_{16}(0)$.

## claim_scope

Body-diagonal reverse versus integer scale k under the named support-drop hop-cost on B_16(0) is reported for k=1..5. Displayed, not adopted.
