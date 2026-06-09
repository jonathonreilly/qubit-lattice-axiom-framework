# The Staggered-Gate Closure Assembly: What Is Actually Left of the AC_φλ Admission

**Date:** 2026-06-09
**Claim type:** assembly/support (live-ledger statuses + the phase campaign's in-review results; no new theorem)
**Type:** open_gate (assembly)
**Status authority:** independent audit lane only. This source note does not set
or predict an audit outcome, and the Tier-A registry is not edited.
**Primary runner:**
[`scripts/frontier_staggered_gate_closure_assembly_2026_06_09.py`](../scripts/frontier_staggered_gate_closure_assembly_2026_06_09.py)
(SCORECARD: PASS=17, FAIL=0; cached:
[`logs/runner-cache/frontier_staggered_gate_closure_assembly_2026_06_09.txt`](../logs/runner-cache/frontier_staggered_gate_closure_assembly_2026_06_09.txt))

---

## The assembly (every status read live from the ledger, every source read)

| component of the AC_φλ admission | status |
|---|---|
| fermionic (not bosonic) matter — substep-1 | `retained_bounded` |
| Kähler–Dirac equivalence — substep-2 | `retained_bounded` |
| BZ-corner `1+3+3+1` Hamming combinatorics — substep-3 | **`retained`** |
| AC_λ simultaneous diagonalization — substep-4 | **`retained`** |
| the scheme itself (staggered unique from one-qubit + Locality) | `unaudited` note, 20/20; **core re-verified here** (Fock dim 2 = qubit; Wilson/naive = 16 = four qubits; overlap/DW nonlocal) |
| generation algebra on `hw=1` is exact, irreducible, **and admits no quotient/rooting/reduction** | **`retained`** (the three-generation observable theorem — a retained anti-rooting theorem) |
| generation count = 3, no proper quotient, Burnside companion | **`retained`** |
| the physical three-generation surface | **`retained_bounded`** (`THREE_GENERATION_STRUCTURE_NOTE`) |
| orientation / species naming / labeling | conventions (stripped) |
| `r = 1/2`, `|δ| = 2/9` | computed (the campaign; PRs #3415/#3420/#3423, in review) |

## The two selector gates, examined against what the framework consumes

- **(a) rooting:** scoped to the selector note's own import (the non-equivariant
  single-fermion Fukaya framing). The framework's `|δ|` chain consumes the
  **equivariant** retained arithmetic, which contains no rooting step
  (grep-verified) — and the **retained** observable theorem now states
  positively that *no quotient/rooting/reduction exists* on the framework
  surface. What remains in (a)'s place is the PL/ABSS global bridge already
  named open by the retained arithmetic note — a transformation, recorded
  honestly, not a vacating by fiat.
- **(c) edge-as-carrier:** is the species reading — substep-3's own boundary
  routes it to the three-generation rows (grep-verified). It is the gate's
  *existing* content; **the phase campaign added zero new conditions.**

## The surviving irreducible

```text
R1b  the semantic matter anchor: "the hw=1 triplet is the physical
     charged-lepton generation sector" — carried by the retained_bounded
     structure note; imports NO number, NO phase, NO knob (the matter
     analogue of "the qubit is physical reality")
R2   the PL/ABSS equivariant global bridge (the retained arithmetic's
     own named open)
R3   audit ratifications: the in-review campaign package + the
     scheme-forcing note
```

**No number, no phase, no orientation, and no scheme choice survives as an
input.** The admission's *derivation-target* character is exhausted: what
remains is one semantic identification (already at `retained_bounded` on its
carrier surface), one named geometric bridge, and ratification work. A next
counterfactual is flagged (not claimed): why `hw=1` rather than `hw=2` — a
uniqueness question on the retained Hamming grading that would reduce R1b
further.

## What this note does NOT claim

- **Not** a registry edit or a retirement declaration (audit-lane authority);
  **not** a closure of R2 or of the ratification queue.
- The scheme-forcing and selector notes are unaudited (cores independently
  re-verified here and in the campaign runners).
- Sets no audit status; consumes no comparator.

## Dependencies

- [STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md](STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md) — the gate.
- [STAGGERED_SCHEME_FORCED_BY_ONE_QUBIT_PER_SITE_LOCALITY_NARROW_THEOREM_NOTE_2026-06-06.md](STAGGERED_SCHEME_FORCED_BY_ONE_QUBIT_PER_SITE_LOCALITY_NARROW_THEOREM_NOTE_2026-06-06.md) — the scheme forcing (core re-verified).
- [STAGGERED_DIRAC_SUBSTEP3_BZ_CORNER_HAMMING_ORBIT_NARROW_THEOREM_NOTE_2026-05-17.md](STAGGERED_DIRAC_SUBSTEP3_BZ_CORNER_HAMMING_ORBIT_NARROW_THEOREM_NOTE_2026-05-17.md) — the routing of the species reading.
- [THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md](THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md) — the retained algebraic/anti-rooting theorem.
- [KOIDE_APS_C3_FIXED_LOCUS_WEIGHTS_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md](KOIDE_APS_C3_FIXED_LOCUS_WEIGHTS_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md) — the retained equivariant arithmetic (R2's home).
- [KOIDE_DELTA_RANK2_SELECTOR_IS_THE_CLIFFORD_CHIRALITY_DOMAIN_WALL_EDGE_BOUNDED_NOTE_2026-06-05.md](KOIDE_DELTA_RANK2_SELECTOR_IS_THE_CLIFFORD_CHIRALITY_DOMAIN_WALL_EDGE_BOUNDED_NOTE_2026-06-05.md) — the selector and its gates.

**No-promotion statement:** this note does not promote, demote, or set the audit
status of any dependency. The independent audit lane is the only status authority.
