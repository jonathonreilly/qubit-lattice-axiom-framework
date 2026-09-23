# GOAL — block 33: a construction attaining `c = 1` with a proof — attacked as an existence statement by induction on levels (2026-09-17)

**Directive.** Owner 2026-09-17 (morning): "pick up the next in the queue and get going." After block 32 (PR #8176) the queue's first item: a construction attaining the unit budget `E ≤ 3(|S| − 1) + |A|` with a proof (worth `p ≥ 453` at `(p, 1, 2)`); the second: a count of the family that is not a union bound over sub-structures. Lens: the union bound needs only the *existence* of a tree with the budget at every realization, so the target is an existence proof — by induction on levels through the rooted value `v(z)` — with the exact programs of block 32 as oracles.

**Exact target (claim type `bounded_theorem`).**
- T1: the extension and seed lemmas for `v`; the inductive step; the reduction of the unit budget to whatever case the lemmas leave open (executed as instances by exact rooted brute force).
- T2: the extremal realizations' rooted structure (do the tight roots fall into the open case?); climbs for violations and for the open case.
- T3: the shape of optimal trees and a restricted count with exact certificates.
- T4: the restriction's admissibility, executed.

**Seat plan (supervisor-run, no subagents).** Controls: rooted values by the integer program with a level cap (`supervisor_control_block33_rooted.py`), the hard cases (`..._tight.py`), candidate lemmas (`..._lemmas.py`), climbs (`..._tightpairs.py`, `..._violate.py`), shape statistics (`..._shape.py`, `..._shape2.py`), the kind-typed count (`..._restricted_count.py`), certificates (`..._certify33.py`; the eight-variable attempt `..._kind_certs.py`, `..._diag.py`). Contract with a lens pass; primary; refuting pass (`..._refuter.py`); fold; census; gates; independent PR against `main`.

**Stop conditions.** A proof of the unit budget, or an exact reduction to a named lemma with the other cases proved; conditional regions recorded but not claimed. Never merge; layman update at the milestone.
