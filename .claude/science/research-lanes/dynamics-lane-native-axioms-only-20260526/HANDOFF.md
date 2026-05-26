# HANDOFF — Native-Only Dynamics Lane (research)

## Lane state at end of turn 5

- **Slug:** `dynamics-lane-native-axioms-only-20260526`
- **Branch:** `research/dynamics-lane-native-axioms-only-20260526` (off `origin/main`)
- **Type:** research lane / side project. NO main landings via lane wrapper.
- **Foundation:** complete (charter + dependency map + Chain 5 verification).
- **Runtime used:** ~1h of 12h target (turn-5 conversation budget).
- **Cycles:** 1 (foundation).
- **PRs from this lane:** zero (correct per the lane policy).

## What's on the branch

| File | Role |
|---|---|
| `CHARTER.md` | Strict constraints + mandate; defines what counts as "native" for this lane |
| `DEPENDENCY_MAP.md` | Every step of the existing dynamics-lane chain tagged NATIVE / RETAINED / IMPORT / DEMOTED. Five chains: kinematic shape, Bernoulli identities, PDG comparator, the δ=2/9 question, native retained dynamics. |
| `CHAIN5_VERIFICATION_2026-05-26.md` | Calibration artifact: queried `origin/main` audit ledger for each piece of native dynamics. Decoherence is `retained_bounded`; broader chain (Brannen-CH, corrected propagator, lattice growth, anomaly-forces-time) is unverified or `unaudited`. |
| `STATE.yaml` | Resume surface |
| `HANDOFF.md` | This file |

## Calibration finding (most important)

**Memory was partially stale about the native dynamics chain.** The query of
`origin/main`'s audit ledger shows:

- ✓ Decoherence (`retained_bounded`)
- ✗ Anomaly-forces-time theorem (`unaudited`)
- ✗ Brannen-Plancherel identity (`unaudited`)
- ✓ Koide-A1 physical-bridge no-go (`retained_no_go`)
- ✓ Koide-A1 radian-bridge no-go (`retained_no_go`)
- ? Corrected propagator, Brannen-CH three-gap, mirror-symmetry — not located by initial query

This **constrains** Direction α (native dynamics test of δ=V(3)) to use only the
verified retained subset. The lane MUST NOT assume the broader native dynamics
chain claimed by memory.

## Resume command

```
/physics-loop --mode resume --loop dynamics-lane-native-axioms-only-20260526
```

## Next exact action on resume

**Direction α — Native dynamics test of `δ = V(3)`, constrained to the verified
Chain 5 subset (decoherence + Cl(3) per-site + Z³ + retained Bernoulli + Brannen
circulant shape).**

Specifically:

1. State the question precisely: given (A1+A2 + Brannen circulant + Bernoulli
   identities + decoherence-action-independence + decoherence-zero-field-phase-
   equality), is `δ` determined, free, or constrained-but-not-fixed?
2. Compute (or argue from retained results) what decoherence dynamics says about
   the C₃-axis phase. The decoherence retained results say something about
   per-link phases; map this onto the C₃ generation triplet.
3. If decoherence dynamics constrains δ to a specific value (any value, not
   necessarily 2/9): that's a concrete native dynamic result.
4. If decoherence dynamics leaves δ free: that's also a concrete native result —
   it says decoherence is insufficient to determine the generation phase, and
   the gap is precisely the structural input needed.
5. Output: a research-grade analysis note (`DIRECTION_ALPHA_DECOHERENCE_PHASE_ANALYSIS_2026-05-XX.md`).
   If a clean algebraic piece falls out (e.g. "decoherence-zero-field implies δ
   modulo phase normalization is integer multiple of X"), package as a candidate
   small-PR off `origin/main`.

**Fallback if Direction α hits a wall in the resume cycle:** pivot to Direction
γ (native isolation of the π-bridge gap) — characterize exactly what new content
would close `P`, using only the retained no-go inventory + L-W. This is a
sharpened-residual statement, not a closure.

## Process commitments (carried forward)

- No source PR opens unless the piece passes "Imports: NONE" certification
  against the retained inventory.
- PR bodies (if any) quote the user's 2026-05-26 mandate verbatim and list
  Imports: NONE explicitly.
- Each PR is single-claim per the reviewer's "small PRs only" rule.
- Each negative claim runs through N1-N8 No-Go Discipline before claiming any
  no-go.
- The lane wrapper does NOT open as a PR during this campaign.
- If a clean import-free piece can't be extracted from a cycle, the cycle still
  contributes to the research artifact — it just doesn't spawn a PR.

## Stop conditions for the campaign

The lane stops when:

1. Runtime budget exhausted (12h).
2. Opportunity queue (currently 4 directions + verification work) exhausted with
   no further native-only attacks identified.
3. User redirects.

The lane does NOT stop for:

- A direction hitting a wall (pivot to next direction).
- A negative result (record as named obstruction; that's a contribution).
- Inability to spawn a PR from a cycle (cycle still contributes to research).

## Sibling artifacts

- `research/dynamics-lane-import-inventory-2026-05-26` (the import-approval
  proposal) is on hold pending user response. **The native-only lane does NOT
  depend on the import-proposal being approved** — it explicitly uses ONLY
  axioms + retained.
- The M-work branches (`claude/lattice-...`, `science/dynamics-lane-m3-*`,
  `science/pi-bridge-*`, `physics-loop/dynamics-lane-completion-block01-*`)
  remain as historical record. Not touched by this lane.

## Open verification queue (for resume cycles to address opportunistically)

- Locate corrected-propagator / `1/L^p` retained source on main if it exists.
- Locate Brannen-CH three-gap closure retained source on main if it exists.
- Locate lattice-growth-with-decoherence retained source on main.
- Resolve memory/main discrepancy: my persistent memory says these are retained;
  ledger query didn't surface them. Either (a) memory is stale, (b) notes exist
  under different names, (c) search query missed them.
