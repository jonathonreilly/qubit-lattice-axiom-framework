# Full-physical live-bank transfer, conditional clean reset, and recurrent physical update — Cycle 800

Date: 2026-07-30

Authority: none

Audit: unset

Status: bounded constructive theorem on a supplied clean-output genesis domain

Claim type: bounded_theorem

Runner: [`frontier_cycle800_full_physical_coherent_live_transfer_reset_2026_07_30.py`](../scripts/frontier_cycle800_full_physical_coherent_live_transfer_reset_2026_07_30.py)

Supplemental, non-load-bearing integration regression:

- [`frontier_cycle800_full_physical_integration_replay_2026_07_30.py`](../scripts/frontier_cycle800_full_physical_integration_replay_2026_07_30.py)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status. Its gate layers, route slots, coframe, and program order are supplied
finite circuit structure. They are not physical time, duration, cadence,
rate, energy, occurrence, Record, or Born weight.

## Result up front

The independently companion-encoded physical `L` bank can be transferred
exactly into the landed recurrent output bank `O` without an EPR resource,
Bell-syndrome bank, character measurement, parity service, or gauge-conditioned
correction. On the supplied domain with `O` clean,

\[
  \bigotimes_s \operatorname{SWAP}(O_s,L_s)
  \left(|0\rangle_O\otimes|\psi\rangle_L\right)
  = |\psi\rangle_O\otimes|0\rangle_L
\]

for every full physical-bank state `|psi>`, including states entangled across
slots or with an external reference. The clean `L` output is exactly the
supplied clean `O` input moved by SWAP; it is not erasure or renewal. Because
corresponding `O/L` physical M2
sites carry the same landed companion-code coordinates, this is a complete
physical-state transfer, not only equality of selected even-CAR characters.

Each nonadjacent endpoint SWAP has a literal nearest-neighbour implementation:
walk adjacent SWAPs from one endpoint to the other, then reverse every edge
except the last. All intermediate states are restored exactly; no clean route
corridor is required. On the landed palettes this uses per coarse cell:

- `18` persistent `O/L` M2 plus the already supplied `3` coframe M2;
- `51` M2 in the union of transient route supports;
- nine fixed local route slots;
- maximum route distance `14`;
- `435` CNOTs when every adjacent SWAP is decomposed into three CNOTs; and
- a conservative fixed padded depth of `729` CNOT microsteps.

Those values are constant through the held `6x5x4` box of `120` cells. Route,
return, collision, coframe-intersection, proper-cubic frame, and all `576`
ordered-frame-product failures are zero.

The transferred output occupies exactly the `O` coordinates consumed by the
landed Cycle-720 recurrent physical update. The canonical runner reconstructs
that public interface independently and matches frozen two- and three-cell
coordinate digests exactly. The cited Cycle-720 theorem gives zero coordinate,
gauge, parity, and recurrent-induction failures through powers `1,2,3,5,8`
where applicable. Its one-particle mass residual is
`5.551115123125783e-17`; the checked contact vacuum/one-particle and double-
occupation phase residuals are both zero. No fresh encoder environment is
called after genesis. The supplemental regression replays those dependency
checks, but the new Cycle-800 claim needs only the typed theorem composition.

This bypasses creating an EPR, Bell-syndrome bank, or dirty Bell-work state in
this one-time live-bank initialization. It does not derive a clean `O` genesis,
an independently companion-encoded `L` bank from raw six-mode matter, the
coframe, or occurrence of the finite transfer word.

## Direct scientific dependencies

- the landed [Cycle-720 recurrent companion physical update](./RECURRENT_COMPANION_PHYSICAL_M2_UPDATE_LOCAL_CHOI_PREPARATION_CYCLE720_BOUNDED_THEOREM_NOTE_2026-07-27.md), which supplies the physical `O` palette and factorwise recurrent-
  `G` intertwiner; and
- the landed [Cycle-789 three-register physical schedule](./THREE_REGISTER_COMPANION_INPUT_CIRCUIT_CYCLE789_BOUNDED_THEOREM_NOTE_2026-07-30.md), used only for its public corresponding `O/I/L` palettes, coframe, and
  returned-route grammar.

The landed Cycle-794 literal prefix plus recurrent update is a comparison
surface, not an extra algebraic premise: it previously
proved postcomposition through the larger character/Bell prefix. Cycle 800
replaces that prefix on the stronger supplied clean-`O`/encoded-`L` domain.
All dependencies remain premise bounds until independent audit says
otherwise.

## Exact state-transfer identity

For one physical site, order registers as `O,I,L`. The eight-layer coherent
Bell route

```text
H(O); CNOT(O,I); CNOT(L,I); H(L);
CNOT(I,O); CZ(L,O); H(L); H(I)
```

satisfies

```text
|0>_O |0>_I |psi>_L  ->  |psi>_O |0>_I |0>_L
```

with isometry residual `4.732681091546602e-16`. Every gate deletion is active;
the weakest residual is `1.0823922002923938`, and reversing the two correction
gates gives residual `1.414213562373095`.

On this clean domain the complete eight-layer word equals direct
`SWAP(O,L)` with residual `4.732681091546602e-16`. The direct SWAP itself has
zero isometry residual and leaves `I` unused. A two-slot Bell input transfers
with residual `6.297190057159811e-16`; entanglement with an external reference
transfers with residual `3.1569827355773645e-16`. These tests make the full
tensor and reference-preserving content active rather than inferring it from
computational-basis population alone.

The coherent route remains a valid literal fallback on all held boxes: `27`
persistent `O/I/L` M2, `132` route-support M2 per cell, maximum route `14`, and
`1,290` expanded `H/CNOT/CZ` gates per cell, with zero route and covariance
failures. It is not the strongest construction under the same clean-`O`
supply because direct SWAP uses no `I` bank and fewer gates.

## Literal returned endpoint SWAP

Let a Manhattan path have vertices `v_0,...,v_d`. Apply

```text
SWAP(v_0,v_1), ..., SWAP(v_{d-1},v_d),
SWAP(v_{d-2},v_{d-1}), ..., SWAP(v_0,v_1).
```

The endpoint labels exchange and every intermediate label returns. This is a
permutation identity on the entire route Hilbert space, so it remains valid
for arbitrary dirty or entangled intermediate states. An independent random
five-site state gives endpoint-SWAP residual zero. Deleting one reverse SWAP
gives residual `0.9206126451685925`, and every literal held path leaves at
least two incorrect labels under the corresponding deletion. The standard
three-CNOT adjacent-SWAP decomposition has residual zero.

All cells execute the same local slot in parallel and different local slots
sequentially. Same-slot route supports in distinct cells are disjoint on every
declared box. Transporting the supplied coframe transports endpoints, paths,
and gate directions together. Nearest-neighbour failures are zero in all `24`
proper-cubic frames and `192` frame/origin contexts per fixture; coordinate
composition failures are zero in all `576` ordered frame products. This is
covariance of supplied coframe data, not derivation of a preferred coframe.

## Recurrent physical-update composition

Write `T_{OL}` for the tensor product of the nine endpoint-SWAP words per cell
and `E_L` for the supplied companion encoding into `L`. On the clean-`O` code
domain,

\[
T_{OL}\bigl(|0\rangle_O\!\otimes E_L\bigr)
= E_O\!\otimes |0\rangle_L,
\]
\[
(G_O\!\otimes I_L)T_{OL}\bigl(|0\rangle_O\!\otimes E_L\bigr)
= (E_O G_{logical})\!\otimes |0\rangle_L.
\]

The first equality is full physical-state identity plus exact coordinate
matching. The second is linear postcomposition by the cited landed Cycle-720
intertwiner. The canonical runner reconstructs the Cycle-789/Cycle-720 `O`
coordinate formula without importing either runner and matches the frozen
parent digests on both declared boxes. The supplemental regression also
replays the dependency runner and its `I/L/coframe` collision firewall, but no
new Cycle-800 lemma relies exclusively on that large regression closure.
Transfer routes finish before recurrent `G` begins; their layer indices are
not a time variable.

## Active controls

- every gate deletion in the coherent fallback is detected;
- hostile coherent correction order is detected;
- dirty `O` and dirty `I` inputs lie outside the stated coherent clean domain
  and each gives residual approximately `2`;
- a direct second load with `O=|1>` misses a clean `L` output by
  `1.4142135623730951`, making the no-erasure/no-renewal boundary executable;
- deleting a returned endpoint-SWAP edge is detected both algebraically and
  on every literal path;
- same-slot intercell collisions, path self-intersections, non-nearest-
  neighbour steps, and coframe intersections are required to remain zero;
- held-size resource counts must equal the one-cell counts exactly;
- the direct routes and coherent fallback are independently transported
  through all proper-cubic frames and products; and
- the cited recurrent theorem remains an explicit conditional premise; the
  supplemental replay confirms its coordinate, gauge, parity, induction,
  route-return, mass, and contact interfaces without becoming the canonical
  proof packet.

The controls establish the declared positive domain. They are not promoted to
a minimum-content or impossibility statement.

## Prior-art and novelty boundary

Coherent teleportation, SWAP networks, and the three-CNOT decomposition are
standard quantum-information constructions; no general novelty is claimed
for them. The framework-specific result is that the landed companion input
interface admits a stronger full-state physical bypass on its actual M2
palettes: the complete Bell-character machinery and its work bank are not
needed to insert an already companion-encoded live state into the exact
recurrent output coordinates. The bounded literal routing, resource census,
proper-cubic covariance, clean output conditional on supplied clean `O`, and
typed recurrent-`G` theorem composition are the new integration result.

## Supplied / derived / open

### Supplied

- clean physical `O` endpoint M2 at the one-time transfer genesis;
- an independent, already companion-encoded full physical `L` bank;
- the fixed parity/center/gauge code sector of that bank;
- the finite cell chart, boundary, transported coframe, corresponding `O/L`
  slots, local route order, and fixed transfer-before-`G` program order; and
- the landed Cycle-720 local factor dictionary, routed recurrent placement,
  code domain, and Cycle-230 parameter fixture.

### Derived

- exact full-state and external-entanglement-preserving `L -> O` transfer;
- exact clean `L` output conditional on the supplied clean `O` input, with no
  `I` or Bell-syndrome bank;
- a constant-overhead nearest-neighbour returned endpoint-SWAP program with
  arbitrary intermediate-state restoration;
- zero held-size route, collision, leakage-by-coordinate, and proper-cubic
  covariance failures through `120` cells and all `576` frame products;
- exact output-coordinate identity with the recurrent physical `O` bank;
- recurrent-`G` postcomposition by the cited Cycle-720 theorem through its
  declared power ladder without a fresh encoder environment; and
- preservation of the landed one-particle mass and checked contact fixtures.

### Open

- autonomous non-postselected clean-`O` genesis and enforcement;
- a bounded local encoder from a bare/raw six-mode matter state into the
  independent companion-coded `L` bank;
- derivation rather than supply of the parity/center/gauge and coframe sector;
- autonomous occurrence/admission of the one-time transfer word and recurrent
  physical law instead of a supplied finite program;
- fault-tolerant realization of the elementary gates; and
- causal time, source/gravity/resources, permanent Record, Born/history, and
  no-refit prediction bridges.

The clean `L` output avoids Bell-work cleanup after this initialization. It
does not erase a dirty `O`, renew clean `O`, or by itself renew a clean `L`
bank for indefinite same-bank independent-input recycling. It also does not
generate the first lawful `L` state or cause the program to occur.

## Dependency-ledger consequence

- `C_ref`: unchanged; no physical reference/Record selection is derived.
- `C_num`: narrowed only at the transfer interface; the companion-coded live
  bank and lawful code sector remain supplied.
- `C_wrap`: unchanged; gate layers are not physical time.
- `C_int`: the landed free/seam/contact update is preserved under exact state
  transfer, while interaction selection/rate/protection remain open.
- `C_local`: materially narrowed; EPR, Bell-syndrome, character-correction,
  and Bell-work cleanup are unnecessary for this one-time full-state transfer.
  Clean genesis, raw encoding, coframe, and occurrence remain.
- `C_source`: unchanged.

## No-go discipline

No impossibility, minimum-content, shared-obstruction, or axiom-pressure claim
is made. The positive direct-SWAP route is itself an escape from a previously
larger implementation. The coherent Bell route also remains a positive
fallback. N1's universal-negative gate is therefore deliberately unsatisfied.

## Exact claim boundary

This is a universal one-time state-transfer identity on supplied clean `O`
plus a bounded literal physical placement and a conditional composition with
the landed recurrent update. It is not erasure, clean-`O` renewal, repeated
independent-input bank recycling, an autonomous genesis theorem, raw-state
encoder, translation-invariant
occurrence law, physical time law, source/gravity law, permanent Record law,
Born law, prediction, minimum, no-go, or axiom-pressure result.
