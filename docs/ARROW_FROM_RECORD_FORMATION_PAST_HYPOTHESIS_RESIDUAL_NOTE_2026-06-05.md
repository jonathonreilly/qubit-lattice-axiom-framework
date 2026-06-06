# Arrow Of Time From Record Formation, Modulo The Past Hypothesis (Bounded)

**Date:** 2026-06-05
**Claim type:** bounded_theorem
**Claim boundary:** boundary-condition / structural result; honest pinning,
**not** a from-nothing derivation of the arrow.
**Status authority:** independent audit lane only. This source note does not set,
predict, or estimate any audit verdict. Effective status is pipeline-derived
after independent audit and dependency closure.
**Primary runner:**
[`scripts/frontier_arrow_from_record_formation_2026_06_05.py`](../scripts/frontier_arrow_from_record_formation_2026_06_05.py)
**Cached log:**
[`logs/runner-cache/frontier_arrow_from_record_formation_2026_06_05.txt`](../logs/runner-cache/frontier_arrow_from_record_formation_2026_06_05.txt)
(PASS=20 FAIL=0)

## Gate Attacked

`MINIMAL_AXIOMS_2026-06-05.md` lists "arrow, measurement, decoherence,
record-production dynamics" as gates **outside** the three axioms (Lattice,
Quantum, Record). The framework carried **zero** past-hypothesis notes. This
note attacks the arrow-of-time gate on a fully explicit small system and pins
the irreducible residual.

## What Is Claimed (narrow)

On an explicit `1 system qubit + nfrag environment-fragment` system (here
`nfrag = 5`, total 6 qubits, exact numpy density matrices), with the #2701
record-forming dynamics realized as redundant pointer broadcast:

1. **(M) The microdynamics is time-symmetric.** Each record-write generator
   `H_k = (pi/2) |1><1|_sys (x) X_k` is real and symmetric, so the #2701
   transfer operator `T_k = e^{-H_k}` is self-adjoint **and** `T_k = T_k^T`
   (no preferred direction), and the unitary step `U_k = e^{-iH_k}` satisfies
   the time-reversal identity `Theta U_k Theta = U_k^{-1}` with `Theta = K`
   (complex conjugation). The arrow is **not** in the map.

2. **(1) Record monotonicity is a candidate arrow.** From a **low-record**
   initial state (system in pointer superposition `|+>`, all fragments blank
   `|0>`), the record functionals increase monotonically under forward
   evolution: redundancy `R_red = [0,1,2,3,4,5]`, total imprinted record
   `R_tot = [0,1,2,3,4,5]` bits, while the system pointer entropy saturates at
   1 bit. This is record proliferation / Quantum Darwinism.

3. **(2) The arrow is in the initial condition, not the dynamics.** Running the
   **same** operator set `{U_k}` (equivalently the same self-adjoint `{T_k}`):
   - from the **time-reversed high-record** state `Theta rho_M Theta`, the
     record **decreases** monotonically, `R_red = [5,4,3,2,1,0]` — the arrow
     **reverses**;
   - from an **independently built GHZ record** (constructed from scratch, not
     by conjugating the forward orbit), the record likewise decreases
     `R_red = [5,...,0]` — so the reversal is **not** an artifact of the
     construction;
   - from the **`I/d` equilibrium** (max-entropy) state, `R_red` is exactly
     **flat** (`[0,0,0,0,0,0]`); `I/d` is invariant — equilibrium has no arrow;
   - from a **generic high-entropy** state, no redundant records form and
     `R_tot` **fluctuates** non-monotonically — the arrow vanishes.

   The sign of the candidate arrow is therefore an **output** fixed entirely by
   the initial condition, with the dynamics held fixed.

4. **(3) Residual = the past hypothesis (universal-floor).** Record formation
   derives the arrow's **direction** = "away from the low-record boundary". The
   irreducible open input is the **existence of a low-record (low-entropy)
   initial condition**, i.e. the **past hypothesis** (Boltzmann/Penrose). The
   three axioms supply registration (Record), a carrier (Quantum), and a site
   set (Lattice) but **no** preferred low-entropy boundary. This open input is
   **universal-floor**: every theory with time-symmetric microdynamics (CM, QM,
   QFT, GR) needs the same boundary input for a thermodynamic arrow. It is
   **not** a framework-specific gap.

5. **(4) Collapse check — distinct from `I/d` and from typicality.** The past
   hypothesis (total vN entropy `0` bits, **ordered**, the source of the arrow)
   and the maximal-symmetry pre-record reference `rho = I/d` (total vN entropy
   `6` bits, **max**, the no-arrow fixed point) are **opposite extremes** of the
   same entropy axis — a local max-entropy reference state is **not** the global
   low-entropy initial. Born "typicality" (operational `omega = frequency`) is a
   **weight/measure** statement on within-sector outcomes and does **not** name
   a global initial condition. So the past hypothesis is a distinct, third kind
   of admission: a **boundary state-selection**, orthogonal to both the
   `I/d` reference and the outcome-frequency weight.

## What Is NOT Claimed

- **Not** a from-nothing derivation of the arrow. The arrow's *existence* still
	  requires the supplied low-entropy boundary; only its *direction* (given that
  boundary) is record-formation-derived.
- **Not** a derivation of record-production dynamics from the axioms. The
  redundant-broadcast generator is a concrete model realizing #2701's
  pointer-non-demolition + redundant-broadcast description on a small system;
  the axioms do not supply it (see `MINIMAL_AXIOMS_2026-06-05.md`).
- **Not** a derivation of a preferred initial state, a cosmological boundary
	  condition, or any selection principle that would *remove* the past-hypothesis
	  residual.
- **Not** a statement about all possible record dynamics; it is the explicit
  redundant-broadcast model. The structural conclusion (symmetric map ⇒ arrow
  sign comes from the boundary) is, however, generic to any time-symmetric
  microdynamics.

## Reconciliation With The Time-Symmetry Of T (#2701)

There is no contradiction. #2701 establishes `T = e^{-H}` is time-symmetric, and
this note confirms that on the explicit system and shows that the time-symmetry
is exactly **why** the arrow cannot live in the map. The same `T` (and the same
unitary `U`) produces monotone record increase, monotone decrease, or a flat
profile depending **only** on the initial condition. The arrow is the *direction
of monotone record accumulation*, and that monotonicity is supplied by the
low-record boundary, not by `T`.

## Residual Ledger (one line)

> **Arrow direction:** record-formation-derived (away from the low-record
> boundary). **Irreducible residual:** existence of a low-record/low-entropy
> initial = the **past hypothesis** = a **universal-floor** open input, distinct
> from `rho = I/d` (opposite, max-entropy extreme) and from Born typicality (a
> weight, not a boundary).

## Relation To Existing Notes (plain-text, non-load-bearing)

- `MINIMAL_AXIOMS_2026-06-05.md` — lists arrow/measurement/decoherence/
  record-production dynamics as gates outside the three axioms; this note pins
  the arrow gate's residual.
- `ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md` — the central admitted-
  input registry; the past hypothesis sits with the universal-floor admissions
  (scale reference / strong-CP-style shared problems), not the framework-specific
  Tier A-1 derivation targets (AC_phi_lambda, theta). This note does not add a
  row to any audit-lane data file.
- `AXIOM_FIRST_GENERALIZED_SECOND_LAW_THEOREM_NOTE_2026-05-01.md` — its "matter
  second law `delta S_matter >= 0` under unital evolution" step is precisely the
  direction-relative statement this note grounds: entropy non-decrease holds
  *relative to* the low-entropy initial; the same symmetric map run from a
  high-entropy/time-reversed state shows the opposite sign.
- `FLAVOR_RECORD_DYNAMICS_SHARPENS_ARROW_STABILIZER_FAILS_2026-06-02.md` —
  closes a *different* route (thermalizing-arrow stabilizer cannot force the
  Koide value); this note is about the arrow's direction and its boundary
  residual, not a flavor value.

## Runner Self-Check

The runner verifies all of (M), (1), (2a), (2a' GHZ control), (2b), (2c), the
residual-ledger self-check, and the collapse check, emitting `PASS=20 FAIL=0`.
Peak RSS ~51 MB. No empirical value, fitted selector, or comparator is consumed;
the arrow sign is read off the redundancy functional as an output of the fixed
dynamics.
