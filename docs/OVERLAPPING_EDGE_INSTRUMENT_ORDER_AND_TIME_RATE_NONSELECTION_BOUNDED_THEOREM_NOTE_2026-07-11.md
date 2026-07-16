---
claim_id: overlapping_edge_instrument_order_and_time_rate_nonselection_bounded_theorem_note_2026-07-11
claim_type: bounded_theorem
claim_scope: "Exact finite schedule fork for identical normalized five-outcome instruments on two overlapping qubit edges: raw layered and first-nonempty priority schedules are separately CPTP but define different channels. Disjoint support, identity-no-record, q=0, symmetrized-schedule, and clock-rescaling controls isolate composition semantics, overlap order, stopping priority, and metric rate as distinct coordinates. A six-matching proper-cubic family is exhibited for even torus side L>=4, but no layer schedule, global QCA, framework-Record realization, or physical clock is selected."
upstream_dependencies:
  - minimal_axioms
  - autonomous_intermittent_record_instrument_calibration_nonselection_bounded_theorem_note_2026-07-11
runner: scripts/overlapping_edge_instrument_order_time_rate_nonselection_2026_07_11.py
---

# Overlapping Edge Instruments: Order, Stopping, And Time/Rate Nonselection

**Date:** 2026-07-11

**Type:** bounded theorem

**Status authority:** independent audit only. This note changes no axiom,
approved primitive, framework rule, or audit verdict.

**Primary runner:**
[`scripts/overlapping_edge_instrument_order_time_rate_nonselection_2026_07_11.py`](../scripts/overlapping_edge_instrument_order_time_rate_nonselection_2026_07_11.py)

**Cached output:**
[`logs/runner-cache/overlapping_edge_instrument_order_time_rate_nonselection_2026_07_11.txt`](../logs/runner-cache/overlapping_edge_instrument_order_time_rate_nonselection_2026_07_11.txt)

## Question

The single-carrier normal form leaves the no-record channel and event gate
open. What happens when the same normalized edge rule is available on two
overlapping supports? Does separate edge-instrument normalization select a unique global event
order, stopping priority, clock, or rate?

No. This note proves the finite schedule fork exactly and separates three
layers:

```text
overlap composition/order
  -> optional first-nonempty stopping priority
  -> optional clock map and physical rate.
```

## Existing-science reading gate

The actual order/time stack and its runners were read before this attack.

- The approved
  [`minimal axioms`](MINIMAL_AXIOMS_2026-06-29.md) supply generic Record
  occurrence, locking, permanence, readability, and finite scalar additivity,
  but no transition relation, overlap composition, scheduler, clock, rate,
  arrow, Markov law, or IID law.
- The preceding
  [`finite-carrier instrument normal form`](AUTONOMOUS_INTERMITTENT_RECORD_INSTRUMENT_CALIBRATION_NONSELECTION_BOUNDED_THEOREM_NOTE_2026-07-11.md)
  exposes the empty channel and event efficiencies but does not compose
  overlapping cells.
- The history-order, clock/rate, count-arrow, Markov-embeddability, finite-reset,
  IID, and clock-axis rows all give narrow finite route pruning or conditional
  interfaces. On the current validation surface the directly relevant rows are
  mostly unaudited; none is used as proof authority here.
- The formation-arrow model is still in audit processing and conditions on a
  finite broadcast model plus a low-record boundary; it does not select an
  overlap schedule.
- The classical record-composition note concerns convolution of named weight
  kernels, not composition of overlapping CP instruments.
The finite CP/Kraus mathematics below is recomputed directly. Current-main
Kraus--Choi authority supplies only the general representation convention.

## 1. One normalized full-edge rule

Supply the bounded tensor carrier `H=(C^2)^(tensor n)` for `n=3` or `4`, embed
each edge operator by the identity on spectator factors, and use ordinary
finite tensor/matrix composition. These are explicit conditional inputs: the
one-site axiom does not itself supply multisite tensor generation or local
tomography. On a two-qubit edge `e`, let

```text
P_xy=|xy><xy|,                   xy in {00,01,10,11},
K_empty^e=sqrt(q) S_e,
K_xy^e=sqrt(1-q) P_xy,           0<q<1,                    (1)
```

where `S_e` swaps the two edge qubits. Then

```text
(K_empty^e)^dag K_empty^e=qI,
sum_xy (K_xy^e)^dag K_xy^e=(1-q)I,                         (2)
```

so every edge carries the same complete five-outcome CPTP instrument. Each
nonempty branch locks the two-qubit edge output to the matching computational
possibility; the spectator sites remain untouched. Equation (1) is the
`d=4`, menu-neutral specialization of the preceding intermittent normal form.

The terminal outcome names used below are mathematical labels. This note does
not identify terminal labels as framework Records.

## 2. Raw overlapping-layer order

On the three-site path use edges

```text
A=(1,2),       B=(2,3).                                      (3)
```

The raw `A then B` schedule has the 25 Kraus products
`{K_b^B K_a^A}`; the reverse schedule has `{K_a^A K_b^B}`. Nested
completeness proves that both are CPTP:

```text
sum_(a,b) (K_b^B K_a^A)^dag(K_b^B K_a^A)
 = sum_a (K_a^A)^dag I K_a^A=I,                            (4)
```

and likewise in reverse.

They are not the same channel. At `q=1/3`, on `rho=|100><100|`, in the basis
`|000>,...,|111>`,

```text
diag Phi_(A then B)(rho)
  = (0,1/9,2/9,0,2/3,0,0,0),
diag Phi_(B then A)(rho)
  = (0,0,1/3,0,2/3,0,0,0).                                (5)
```

The cause is already present in the double-empty coherent blocks:

```text
[S_B,S_A] has rank 4,
S_B S_A |100> = |001>,
S_A S_B |100> = |010>.                                    (6)
```

Thus identical edge rules plus separate edge completeness do not select overlapping
sublayer order.

For two maps, schedule independence on all inputs is exactly the interchange
condition

```text
Phi_B Phi_A = Phi_A Phi_B.                                 (7)
```

More generally, assign channels to a finite dependency DAG. If channels at
incomparable vertices commute as superoperators, every linear extension gives
the same global channel: any two linear extensions are connected by adjacent
swaps of incomparable vertices, and each swap leaves the product unchanged.
This is the positive schedule-independence theorem. Disjoint tensor supports
are its exact simplest case.

## 3. First-nonempty stopping is a separate priority

If the process stops at the first nonempty edge outcome, `A` priority has the
nine terminal Kraus operators

```text
{K_xy^A} union {K_b^B K_empty^A : b=empty,00,01,10,11}.    (8)
```

`B` priority is the reverse construction. Each is CPTP because

```text
(1-q)I + (K_empty)^dag I K_empty = I.                       (9)
```

For arbitrary `q`, the same input `|100>` gives

```text
diag Phi_stop_(A then B)
 = (0,q^2,q(1-q),0,1-q,0,0,0),
diag Phi_stop_(B then A)
 = (0,0,q^2,0,1-q^2,0,0,0).                              (10)
```

At `q=1/3` these become

```text
(0,1/9,2/9,0,2/3,0,0,0),
(0,0,1/9,0,8/9,0,0,0).                                   (11)
```

The two stage-weight multisets agree,

```text
{1-q, q(1-q), q^2},                                       (12)
```

but they attach those weights to different edge/label histories and different
system outputs. A supplied priority resolves the process even when the local
maps do not commute; it does not derive that priority.

Stopping priority is distinct from coherent overlap order. Replacing the
no-record SWAP by identity makes the raw overlapping channels commute, yet
first-nonempty schedules can still differ on coherence because the first edge
is offered the first writing opportunity. Conversely, a diagonal input can
hide that difference. Disjoint supports guarantee raw/tensor commutation but
do not address a separately imposed first-nonempty stopping policy.

## 4. Controls and alternative composition rules

The runner supplies four exact controls. For the first three, it checks channel
equality on every matrix unit, not only on the displayed coherent fixtures:

1. raw instruments on disjoint edges commute on a coherent four-qubit input;
2. identity no-record branches remove the raw overlapping order difference;
3. at `q=0`, the overlapping computational projective channels commute;
4. corrupting one Kraus weight breaks completeness.

Analytically, disjoint edge maps commute because their Kraus operators act on
distinct tensor factors. With identity no-record branches, each overlapping
channel is a scalar identity contribution plus computational-basis pinchings,
which commute; at `q=0` only those commuting pinchings remain. The full
matrix-unit checks certify these channel identities on the finite fixtures.

The runner also constructs the equal symmetrized schedule

```text
Phi_sym = (Phi_(A then B)+Phi_(B then A))/2,                (13)
```

which is CPTP but differs from either ordered raw channel. Symmetrization is a
valid extra composition rule, not a consequence of separate edge normalization.

The exact finite fork is therefore:

```text
derive overlap interchange/commutation,
or supply a composition semantics plus dependency/priority schedule,
or supply a randomized/symmetrized rule,
or construct one simultaneous global channel.             (14)
```

## 5. Proper-cubic matching family, not an ordering

On cubic `Z^3` finite tori of even side `L>=4`, define six edge matchings

```text
M_(mu,p)
 = {{x,x+e_mu}: x_mu = p mod 2},
mu in {1,2,3}, p in {0,1}.                                 (15)
```

Each `M_(mu,p)` is conflict-free: along a fixed axis and parity every vertex is
incident to exactly one selected bond. For even `L>=4`, the two endpoints of an
undirected axis bond have distinct start parities, so the parity matchings are
disjoint and exhaust the bonds; the six matchings therefore partition all
nearest-neighbor edges. (At `L=2`, opposite periodic bonds coincide, so this
undirected statement is deliberately excluded.) Unit translations exchange
the two parities, and proper cubic rotations permute the three axes, making the
orbit of any one layer the full six-layer family. The construction therefore
exhibits a symmetry-stable family but no first layer or layer ordering. When overlapping
layer channels fail (7), an ordering is physical process content.

Equation (15) is only a finite combinatorial schedule family. This note does
not construct or classify a simultaneous cubic QCA; that is the next coherent
tick campaign.

## 6. Event order still does not supply time or rate

Once a discrete order is supplied, the same two-layer history embeds in both

```text
tau_fast=(0,1,2),       tau_slow=(0,2,4).                  (16)
```

The order is identical, while the total event rates are `1` and `1/2` in the
chosen units. Likewise, interpreting the per-attempt empty weight through a
Poisson clock gives

```text
q=exp(-lambda Delta t).                                    (17)
```

Only `lambda Delta t=-log q` is fixed. For `q=1/3`, both
`(lambda,Delta t)=(log 3,1)` and `(log 3/2,2)` produce the same instrument.
Thus the discrete event rule does not select a physical clock or rate.

This does not deny that a separately derived clocked process can define rates.
It proves only the exact rescaling freedom left by the instrument and order.

## 7. Physical residuals and boundaries

- The edge Kraus family, computational rank-one menu, overlapping-support
  schedules, first-nonempty stopping rule, and clock maps are explicit
  conditional inputs.
- The multisite tensor carrier, spectator-identity embeddings, and ordinary
  tensor/matrix composition are explicit finite-model inputs, not consequences
  of the one-site axiom.
- CP/Kraus mathematics is not identified with physical outcome probability or
  realization semantics.
- The terminal labels and priority histories are external mathematical
  objects; the theorem does not identify terminal labels as framework Records.
- The three-site path and finite even-side-`L>=4` tori are bounded carriers, not a derived
  translation-covariant infinite-lattice law.
- The theorem does not classify all overlapping instruments, schedules,
  dependency DAGs, randomizations, common dilations, or colorings.
- It does not select a physical clock or rate, Markov generator, IID/reset
  protocol, arrow, clock axis, Hamiltonian, action, or probability rule.
- It does not provide a strict-QCA verdict or a continuum limit.
- It does not establish that the axioms require amendment. Commuting overlap,
  a supplied/derived dependency relation, common dilation, symmetrized rule,
  or simultaneous global channel remain live closure routes.

## Reproduction

```bash
python3 scripts/overlapping_edge_instrument_order_time_rate_nonselection_2026_07_11.py
```
