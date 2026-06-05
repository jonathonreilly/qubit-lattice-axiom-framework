# Born Rule From Envariance Is Conditional On State-Functional Probability

**Date:** 2026-06-05
**Claim type:** conditional / support (with a sharpened negative core)
**Status authority:** independent audit lane only. This source note does not set,
predict, or assert an audit verdict and does not claim "retained" or "promoted"
standing.
**Primary runner:**
[`scripts/frontier_born_from_envariance_2026_06_05.py`](../scripts/frontier_born_from_envariance_2026_06_05.py)
with cache
[`logs/runner-cache/frontier_born_from_envariance_2026_06_05.txt`](../logs/runner-cache/frontier_born_from_envariance_2026_06_05.txt)
(PASS=44, FAIL=0).

---

## Scope and honesty (read first)

This note tests whether the Born rule `p_k = |a_k|^2` can be **derived** from the
framework axioms {Quantum, Record} on the record state by the route the narrow
additivity no-go
([`OBSERVABLE_PRINCIPLE_RECORD_SCALAR_MAP_NO_GO_NOTE_2026-06-05.md`](OBSERVABLE_PRINCIPLE_RECORD_SCALAR_MAP_NO_GO_NOTE_2026-06-05.md))
does not block: Zurek-style envariance (state symmetry), with a Gleason/Busch
backstop. The honest result is **conditional**, with a sharpened negative core:

- The envariance value-equality (`equal amplitudes => equal probability`) is
  **derived, not assumed** — the runner exhibits the exact state-symmetry that
  forces it and verifies that the symmetry **fails** for unequal amplitudes, so
  equal-amplitude is the genuine hinge, not a smuggled premise.
- The **single residual admission** is `A3`: that a probability measure over
  outcomes **exists and is a function of the (record/quantum) state**. The Record
  axiom as written
  ([`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md)) supplies a
  discrete realized alphabet (K/CPT orbits of central sectors) and finite
  **additivity** of a scalar readout `I` over disjoint records — explicitly **no**
  weighting, normalization, or probability. So `A3` is **not** contained in
  {Quantum, Record}. This is exactly the premise the Schlosshauer–Fine (2005) and
  Barnum (2003) critiques of envariance point to.

**Verdict.** Envariance gives a **genuine, non-circular** derivation of
`p_k = |a_k|^2` **conditional on `A3`**. It does not derive Born from
{Quantum, Record} alone, because those axioms do not supply `A3`. Both
foundational routes leave a value-fixing admission that the timeless additive
Record readout does not provide.

---

## What the runner verifies (exact `numpy` + `sympy`, PASS=44 FAIL=0)

### Route 1 — envariance on the record state

1. **Record state.** `|psi> = a_0|0>_S|00>_E + a_1|1>_S|11>_E` (GHZ-type): the
   environment records `{|00>,|11>}` are orthonormal and redundant. Verified.
2. **Equal-case envariance.** With `a_0=a_1=1/sqrt2`, the system swap `U_S` (the
   X relabel `|0>_S<->|1>_S`) alone moves `|psi>`, the environment swap `U_E`
   (`|00><->|11>`) alone moves `|psi>`, but the composite is invariant:
   `(U_S ⊗ U_E)|psi> = |psi>` (verified to machine precision **and** exactly in
   `sympy`). The reduced system state is `I/2` and is `U_S`-invariant; the
   environment-only `U_E` cannot change it.
3. **General case by fine-graining.** For `|a_0|^2=2/3, |a_1|^2=1/3`, an ancilla
   splits each coarse branch into `N_0:N_1 = 2:1` orthonormal, **equiprobable**
   fine-grained sub-records (all carrying amplitude `sqrt(1/3)`). Equal-case
   envariance applies to all three; counting + Record additivity over the
   disjoint coarse unions gives `p(s_0)=2/3, p(s_1)=1/3 = |a_k|^2`. The same
   recipe is checked for `(3/4,1/4)` and `(2/5,3/5)`.
4. **Hinge contrast.** Swapping the **unequal** coarse branches is **not** a state
   symmetry (verified exactly): equal-amplitude is the actual hinge, so
   `equal amp => equal prob` is derived, not an input.

### Route 2 — Gleason/Busch backstop (the theorem route)

5. The framework's records form a PVM (orthogonal, commuting, sum to `I`).
   Gleason's hypothesis (`dim>=3`) is met on `|Lambda|>=2` regions
   (`dim=2^|Lambda|>=4`); Busch's (`dim>=2`) is met on the single qubit. Both
   force the measure **form** `m(.) = Tr(rho .)` (uniqueness of `rho` verified).
   This sits **outside** the additivity no-go: it is additivity over **orthogonal
   projectors** of one measurement (a frame function), not the multiplicative
   independent-branch homomorphism `(R_+,x)->(R,+)` the no-go bars. The runner
   contrasts the two composition laws explicitly. The Born **value** still rides
   on the conditional `rho`-identification (pre-record reference `= I/d`; an open
   admission per
   [`PRE_RECORD_REFERENCE_STATE_TRACIAL_DERIVATION_NOTE_2026-05-20.md`](PRE_RECORD_REFERENCE_STATE_TRACIAL_DERIVATION_NOTE_2026-05-20.md)).

---

## The circularity-assumption ledger

| Premise | Tag | In {Quantum, Record}? |
|---|---|---|
| A1 unitary invariance `(U_S⊗U_E)|psi>=|psi>` (equal case) | physical | yes (linear algebra) |
| A2 locality of the undo (`U_E` acts only on `E`) | physical | yes |
| A3 a probability measure **exists and is state-functional** | **admission** | **NO** |
| A4 symmetry ⇒ equal probability | `= A1+A2+A3` | derived, not independent |
| A5 additivity over disjoint records (coarse = sum of sub-records) | Record axiom | yes |
| A6 fine-graining is a physical unitary embedding | physical | yes |

The only premise not contained in {Quantum, Record} is **A3**. Everything else is
physical invariance (A1, A2, A6) or the Record additivity axiom (A5); A4 is not an
independent smuggle — it is forced by A1+A2 **once A3 is granted**. Crucially, A3
is **not** the strong "equal amplitudes ⇒ equal probability" assumption (that is
derived); it is the weaker-looking but still-extra "a state-functional probability
exists."

---

## What this note establishes / does not establish

**Establishes.**
- Equal-case envariance holds exactly on the framework's record state, and the
  general rational case reduces to it by fine-graining + Record additivity,
  recovering `p_k=|a_k|^2`.
- The envariance derivation is non-circular about the **value** (the
  equal-amplitude hinge is derived; the unequal contrast is verified).
- The exact residual admission is `A3` (state-functional probability exists),
  which {Quantum, Record} do not contain — pinning the Schlosshauer–Fine /
  Barnum critique to a single, named premise for **this** framework.
- The Gleason/Busch route's hypotheses are met and it sits outside the additivity
  no-go; it forces the measure **form** `Tr(rho .)`.

**Does not establish.**
- An **unconditional** Born `= |amplitude|^2` from {Quantum, Record} alone. Route 1
  is conditional on A3; Route 2's value is conditional on the `rho`-identification.
- Any enlargement of the Record axiom. The axiom stays a timeless additive scalar
  readout with no probability; A3 is recorded as an admission, not folded into it.
- Any contradiction of the narrow additivity no-go. That no-go bars only
  "Record additivity alone ⇒ the branch measure" via the multiplicative→additive
  branch homomorphism; neither route uses that step, so the no-go stands intact.
- Any numerical-prediction change.

## Relation to the additivity no-go (no contradiction)

The no-go is narrow: it forecloses deriving the **branch** measure from the
`(R_+,x)->(R,+)` homomorphism on independent branches (yielding `-c log p`, not
which measure). This note goes **around** it: Route 1 uses a **state symmetry**
plus additivity over **disjoint** records (+ A3); Route 2 uses frame-function
additivity over **orthogonal projectors**. Both are different structures from the
barred homomorphism. The no-go is unaffected.

## Forbidden-imports check

- No PDG observed values, literature numerical comparators, or fitted selectors
  consumed.
- Gleason 1957 and Busch 2003 are cited as named standard mathematical-physics
  content (the framework-scoped applications already exist in
  [`GLEASON_ON_QUBIT_LATTICE_PROJECTION_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md`](GLEASON_ON_QUBIT_LATTICE_PROJECTION_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md)
  and
  [`BUSCH_POVM_EXTENSION_ON_QUBIT_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md`](BUSCH_POVM_EXTENSION_ON_QUBIT_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md));
  they are not re-proved here.
- No new axiom is introduced; the Record axiom is used only as written, and A3 is
  recorded as an admission outside it.
