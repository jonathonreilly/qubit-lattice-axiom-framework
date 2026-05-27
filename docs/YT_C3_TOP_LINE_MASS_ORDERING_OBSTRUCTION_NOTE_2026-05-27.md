---
claim_id: yt_c3_top_line_mass_ordering_obstruction_note_2026-05-27
claim_type: no_go
actual_current_surface_status: no-go
trace_class: negative_route_pruning
reachability_to_target: prunes
proposal_allowed: false
bare_retained_allowed: false
audit_required_before_effective_retained: true
---

# Y_T C3 Top-Line Mass-Ordering Obstruction

**Date:** 2026-05-27
**Status:** exact route-pruning no-go for the current C3 line-assignment
shortcut. This note does not claim retained or proposed-retained `Y_T`
closure.
**Runner:** `scripts/frontier_yt_c3_top_line_mass_ordering_obstruction.py`
**Output:** `outputs/yt_c3_top_line_mass_ordering_obstruction_2026-05-27.json`

## Question

After normalized RN/Fisher source semantics remove the identity direction and
real finite-record source semantics remove the imaginary/reflection-odd
direction, the C3 source tangent is

```text
B_x = (C + C^2) / sqrt(6)
```

up to sign.  Can the remaining phrase "the physical top row is a nontrivial
C3 character line" be treated as an ordinary top-label convention rather than
a new physical premise?

## Answer

No.  The ordinary top-label convention available without new dynamics is mass
ordering: in the up-type sector, `top` names the heaviest up-type pole.  On the
`B_x` source tangent, the C3 spectral responses are

```text
P_0       ->  2/sqrt(6)
P_omega   -> -1/sqrt(6)
P_omega2  -> -1/sqrt(6).
```

If the source response is used as the mass/Yukawa ordering proxy, then the
largest absolute response is the C3 singlet `P_0`, not either nontrivial
character line.  The two nontrivial lines give the desired magnitude
`1/sqrt(6)`, but choosing one of them as the physical top line is then an
extra top-line/source law. It is not a consequence of mass ordering, LSP
projective readout, retained C3 projectors, or the real-record source theorem.

## Finite Witness

Let `omega = exp(2 pi i / 3)` and let

```text
P_k = (I + omega^{-k} C + omega^{-2k} C^2) / 3,
```

for `k in {0,1,2}`.  Direct trace evaluation gives:

```text
Tr(P_0 B_x)      =  2/sqrt(6)
Tr(P_omega B_x)  = -1/sqrt(6)
Tr(P_omega2 B_x) = -1/sqrt(6).
```

Therefore:

```text
argmax_k |Tr(P_k B_x)| = P_0.
```

So the route splits:

```text
mass-ordering top convention  -> top = P_0       -> 2/sqrt(6)
target coefficient convention -> top nontrivial  -> 1/sqrt(6)
```

The second line is useful exact support, but it is not a retained physical
top-Yukawa derivation unless a same-surface theorem explains why the physical
top pole is not the C3 singlet.

## Relation To Existing No-Gos

This is narrower than the substep-4 species-labeling no-go.  The old no-go
blocks a canonical bijection from the `hw=1` triplet to named physical labels
such as `{u,c,t}` without a convention, C3-breaking dynamics, or empirical
matching.

This note tests a weaker attempted escape:

```text
Do not name all generations; only require top to be a nontrivial C3 line.
```

That weaker shortcut still fails under the only convention that has a standard
physical meaning for `top`, namely mass ordering.  Mass ordering picks the
singlet for the `B_x` response.  Nontrivial-line selection must therefore be a
new physical law or strict pole-row result, not a convention-free conclusion.

## What This Prunes

This prunes:

```text
B_x source direction
  + retained C3 spectral projectors
  + ordinary top mass-ordering convention
  => y_t coefficient 1/sqrt(6).
```

The implication is false on the finite witness above.  The same inputs select
the singlet as the largest-response line.

## What Remains Open

Positive closure still has two honest routes:

1. derive a same-surface physical law that identifies the top pole with a
   nontrivial C3 character line despite the mass-ordering witness; or
2. bypass the line-label question by producing strict same-source top/W
   pole-response rows with coefficient-bearing `dM_t/dh` and `dM_W/dh`.

The first route is now very constrained: it cannot be "top means heaviest" and
it cannot be just "choose the line that gives the target coefficient."

## Non-Claims

This note does not:

- claim retained or proposed-retained `Y_T` closure;
- derive `m_t`, `v = 246 GeV`, physical-scale `g_2`, or numerical `y_t(v)`;
- prove that `P_0` is the physical top pole; it only shows mass-ordering would
  pick `P_0` on this candidate source tangent;
- rule out a future same-surface theorem that gives a different physical
  top-line law;
- rule out strict same-source top/W pole-response evidence;
- use `H_unit`, `yt_ward_identity`, `y_t_bare`, observed W/Z/top masses, PDG
  values, `alpha_LM`, plaquette/u0, Planck, alpha_s, or a fitted selector as
  proof inputs.

## Claim-Status Certificate

```yaml
actual_current_surface_status: no-go
trace_class: negative_route_pruning
reachability_to_target: prunes
route_pruned: B_x plus mass-ordering convention selects target 1/sqrt(6)
proposal_allowed: false
proposal_allowed_reason: |
  The B_x source direction is now derived as exact support, but ordinary
  top mass-ordering selects the C3 singlet response 2/sqrt(6), not the
  nontrivial-line response 1/sqrt(6). A nontrivial top-line law or strict
  top/W pole rows remain required.
bare_retained_allowed: false
audit_required_before_effective_retained: true
next_action: strict same-source top/W pole-response evidence, or a new
  same-surface top-line law that is not mass-ordering and not target selection
```

## Verification

Run:

```text
python3 scripts/frontier_yt_c3_top_line_mass_ordering_obstruction.py
```

Expected result:

```text
SUMMARY: PASS=... FAIL=0
```
