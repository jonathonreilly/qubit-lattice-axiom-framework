# Chain 5 Verification — What's Actually Retained on `origin/main`

**Date:** 2026-05-26
**Method:** queried `docs/audit/data/audit_ledger.json` on `origin/main` for each
piece of native dynamics named in the dependency map's Chain 5.
**Status:** verification artifact for the research lane; not a theorem note.

## Per-piece verification

| Piece | Source | effective_status | claim_type | Usable in this lane? |
|---|---|---|---|---|
| Decoherence action independence | `DECOHERENCE_ACTION_INDEPENDENCE_NOTE.md` | **retained_bounded** | bounded_theorem | **YES** (bounded) |
| Decoherence zero-field per-link phase equality | `DECOHERENCE_ACTION_ZERO_FIELD_PER_LINK_PHASE_EQUALITY_NARROW_THEOREM_NOTE_2026-05-17.md` | **retained_bounded** | bounded_theorem | **YES** (bounded) |
| Anomaly-forces-time theorem | `anomaly_forces_time_theorem` (multiple notes) | **unaudited** | bounded_theorem | **NO** (not yet retained) |
| Brannen-Plancherel identity support | `KOIDE_A1_BRANNEN_PLANCHEREL_IDENTITY_SUPPORT_NOTE_2026-04-25.md` | **unaudited** | positive_theorem | **NO** (not yet retained) |
| Koide-A1 physical-bridge attempt | `koide_a1_physical_bridge_attempt_2026-04-22` | **retained_no_go** | no_go | **YES** (as obstruction) |
| Koide-A1 radian-bridge irreducibility | `KOIDE_A1_RADIAN_BRIDGE_IRREDUCIBILITY_AUDIT_NOTE_2026-04-24.md` | **retained_no_go** | no_go | **YES** (as obstruction) |
| Koide-A1 loop final status | `koide_a1_loop_final_status_2026-04-22` | **audited_conditional** | bounded_theorem | partial (bounded) |
| Corrected propagator `1/L^p` | (not located by initial grep) | (status TBD) | — | UNVERIFIED — defer until located |
| Brannen CH three-gap closure | (not located by initial grep; memory says 2026-04-22, runner 16/16) | (status TBD) | — | UNVERIFIED — defer until located |
| Lattice-growth dynamics (mirror DAGs) | (not located by initial grep; memory says retained) | (status TBD) | — | UNVERIFIED — defer until located |

## Result vs memory

| Memory claim | Actual `origin/main` status |
|---|---|
| "Axiom chain closure: Full chain from local growth to physics on 4D grown graphs; gravity 2.0 SE + decoherence" | Decoherence pieces ARE retained_bounded; the "full chain" is bounded, not bare-retained. |
| "Mirror symmetry breakthrough: Z₂ DAGs..." | UNVERIFIED on main by this query; defer. |
| "Brannen CH three-gap closure (2026-04-22, runner 16/16)" | UNVERIFIED on main by this query; the related Brannen-Plancherel support note is **unaudited**. The "three-gap closure" memory may have been a branch-local claim. |
| "Corrected propagator: 1/L^p attenuation enables gravitational attraction" | UNVERIFIED on main by this query; defer. |

**Calibration:** memory is partially stale. Decoherence is solid (retained_bounded);
the broader "full native dynamics chain" claimed by memory is mostly unverified or
unaudited on `origin/main`. **The lane cannot safely assume the broader chain.**

## Implications for the research lane

What is actually solid for native attacks:

1. **Kinematic surface (Chain 1) — fully usable.** Brannen circulant formula
   `cos(δ + 2πk/3)` derived from C₃ + Cl(3) is retained.
2. **Bernoulli identities (Chain 2) — usable.** `V(N) = (N-1)/N²` and the four
   CKM `2/9` readouts are retained (bounded).
3. **Decoherence dynamics (a slice of Chain 5) — usable as bounded retained.**
   Specifically the "action independence" and "zero-field per-link phase
   equality" results.
4. **Retained no-gos as obstructions — usable.** The physical-bridge and
   radian-bridge no-gos define the wall structure for any native attack on δ.
5. **NOT usable:** anomaly-forces-time theorem, Brannen-Plancherel, the broader
   "axiom chain closure" claimed by memory — all unaudited or unverified.

## Concrete next step (updated)

Original plan was Direction α (native dynamics test of δ=V(3)) using Chain 5
native dynamics. Given the calibration:

- Direction α is **constrained** to use only the decoherence-bounded subset of
  Chain 5 + the kinematic surface (Chain 1) + the Bernoulli family (Chain 2).
- The "broader" native dynamics (anomaly-forces-time, Brannen CH closure,
  corrected propagator) cannot be assumed; they would themselves be open
  attack targets if needed.
- This may MAKE Direction α MORE rigorous: a δ-derivation that uses only
  decoherence + C₃ kinematics would be substantially more constrained than
  one that imports broader Chain-5 content.

## Open verification (next cycle)

To complete Chain 5 verification:

- [ ] Locate corrected-propagator / `1/L^p` retained source (if any) on main.
- [ ] Locate Brannen CH three-gap closure retained source (if any) on main.
- [ ] Locate lattice-growth-with-decoherence retained source on main.
- [ ] Resolve the apparent disagreement between memory (which says these are
  retained) and the audit ledger (which doesn't surface them in this search).
  Possibilities: (a) memory is stale; (b) the notes exist on main under
  different names; (c) the search query missed them.
