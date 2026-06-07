# Staggered Anticommutation Filter: Multi-Loop Cocycle Consistency Does Not Force CAR

**Date:** 2026-06-07
**Claim type:** no_go
**Actual current-surface status:** no-go source-note proposal; independent
audit required before any effective retained_no_go status.
**Trace class:** negative_route_pruning
**Reachability to target:** prunes
**Primary runner:** [`scripts/frontier_staggered_anticommutation_filter_cocycle_no_go_2026_06_07.py`](../scripts/frontier_staggered_anticommutation_filter_cocycle_no_go_2026_06_07.py)
**Cached runner output:** [`logs/runner-cache/frontier_staggered_anticommutation_filter_cocycle_no_go_2026_06_07.txt`](../logs/runner-cache/frontier_staggered_anticommutation_filter_cocycle_no_go_2026_06_07.txt)

## Role

This note attacks the first live route named by the spin-statistics exercise:
the possibility that **multi-loop graded-net cocycle consistency** forces the
cross-site fermion sign.  If that route worked, it could supply the CAR /
graded-locality premise that would then feed the staggered anticommutation
filter `{D,gamma5}=0`; the existing staggered chirality selector enumerator
would force `epsilon(x)` up to global sign after that filter is present.

The route does not work.  Multi-loop exchange consistency forces only a uniform
exchange character.  It leaves both global values alive:

```text
q = +1  hard-core-boson / trivial exchange character
q = -1  CAR / fermion sign character
```

Therefore this route cannot retire the chirality selector admission.  It is a
route-local no-go, not a no-go against fermions or against a future retained
spin-statistics theorem.

## Setup

Use the type-A Coxeter presentation for adjacent exchange generators
`s_i` of `S_n`:

```text
s_i^2 = e
s_i s_j = s_j s_i                 for |i-j| > 1
s_i s_{i+1} s_i = s_{i+1} s_i s_{i+1}
```

Reduce to the one-dimensional `Z_2` exchange-character question:
`chi(s_i) in {+1,-1}`.  This is exactly the finite sign data that a
single-valued abelian exchange cocycle can see.

## Result

The runner enumerates all `Z_2` sign assignments for `S_n`, `n = 3,4,5,6`,
and checks the involution, distant-commutation, and adjacent-braid loop
relations.

It verifies:

- adjacent braid relations force `chi(s_i) = chi(s_{i+1})`, so the exchange
  sign is uniform across adjacent generators;
- the uniform value remains unconstrained;
- `q = +1` and `q = -1` both satisfy every checked loop relation;
- imposing `chi(s_1) = -1` selects CAR uniquely, but that predicate is exactly
  the missing selector;
- imposing `chi(s_1) = +1` selects the hard-core-boson frame just as uniquely.

So the multi-loop route improves the boundary from "many local sign choices"
to "one global statistics sign", but it does **not** derive the fermion sign.

## Consequence For The Chirality Lane

The existing
[`STAGGERED_CHIRALITY_SELECTOR_ENUMERATOR_NARROW_THEOREM_NOTE_2026-06-06.md`](STAGGERED_CHIRALITY_SELECTOR_ENUMERATOR_NARROW_THEOREM_NOTE_2026-06-06.md)
locates the chirality residual:

```text
epsilon forced  <=>  chiral anticommutation {D,gamma5}=0 is required
```

This note shows that the multi-loop graded-net route cannot supply that
requirement by itself.  The hard-core-boson exchange character survives the same
finite loop consistency checks as the CAR character.  A later retained theorem
would need an additional physical principle: graded locality, spin-statistics
reconstruction, positive-energy microcausality, a supplied fermion-parity
superselection rule, or another genuinely native selector.

## No-Go Discipline Gate

### Alternative Route Enumeration

| Route | Attempted forcing step | Result |
|---|---|---|
| Adjacent braid consistency | Use `s_i s_{i+1} s_i = s_{i+1} s_i s_{i+1}` to force the sign. | Forces uniformity only. |
| Many-loop consistency | Add several linked adjacent exchange loops. | Still leaves `q = +1` and `q = -1`. |
| Single-valued exchange character | Require a one-dimensional `Z_2` cocycle. | Both trivial and sign characters are single-valued. |
| CAR predicate | Add `chi(s_1)=-1`. | Selects CAR, but the predicate is the missing selector. |
| Hard-core predicate | Add `chi(s_1)=+1`. | Selects the hard-core-boson frame just as coherently. |

### Wall Independence

The collapsed wall is one wall: the global exchange sign.  Multi-loop
consistency can identify that the sign is global, but cannot choose it.

### Hidden-Wall Scan

The only framework premises are the `Lattice`, `Quantum`, and `Record` baseline
recorded in
[`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md).  The runner uses
finite group-presentation algebra and exact `Z_2` sign enumeration.  It does
not import a continuum spin-statistics theorem, a Lorentzian time direction,
microcausality, a fermion measure, or a physical source/action.

### Residual Matching

The residual is cross-site CAR/graded-locality selection as a possible upstream
source for `{D,gamma5}=0`.  This note does not attack the conditional fact that
`{D,gamma5}=0` forces the staggered `epsilon`; it attacks one proposed source of
that condition.

### Rhetoric Audit

"No-go" here means no-go for deriving CAR from the tested multi-loop
exchange-cocycle consistency route.  It does not claim CAR is impossible, and
it does not claim all spin-statistics or reconstruction routes are closed.

### Partial-Closure Path

The next route should not keep repeating loop-consistency tests.  It should
attack a different selector:

- a future retained graded-locality/spin-statistics reconstruction theorem;
- a canonical orientation/source-section theorem;
- or an eta/spectral-flow boundary filter.

## Reprove-And-Cite Ledger

- Reproven here: type-A exchange-character enumeration; uniformity under
  adjacent braid relations; survival of both `q = +1` and `q = -1`; failure of
  the multi-loop route to select CAR.
- Cited for downstream context:
  [`SPIN_STATISTICS_FS_ADMISSION_LOCATED_EXERCISE_NOTE_2026-06-06.md`](SPIN_STATISTICS_FS_ADMISSION_LOCATED_EXERCISE_NOTE_2026-06-06.md),
  [`STAGGERED_CHIRALITY_SELECTOR_ENUMERATOR_NARROW_THEOREM_NOTE_2026-06-06.md`](STAGGERED_CHIRALITY_SELECTOR_ENUMERATOR_NARROW_THEOREM_NOTE_2026-06-06.md),
  [`STAGGERED_DIRAC_EXERCISE_HONEST_REASSESSMENT_NOTE_2026-06-06.md`](STAGGERED_DIRAC_EXERCISE_HONEST_REASSESSMENT_NOTE_2026-06-06.md),
  [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md).

No new axiom, no fitted input, no observed target, and no audit verdict are
introduced by this packet.
