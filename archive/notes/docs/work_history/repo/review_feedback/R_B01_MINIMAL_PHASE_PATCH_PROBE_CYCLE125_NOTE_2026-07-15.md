# R_B01 minimal phase patch probe — Cycle 125

Date: 2026-07-15

Authority: none

Disposition: bounded negative for one named patch; constructive residual remains

Write scope: runner + review note only

Companion runner:

```text
scripts/r_b01_minimal_phase_patch_probe_cycle125_2026_07_15.py
```

No predecessor, foundation, axiom, primitive, registry, queue, policy, audit,
or git state is edited here. No commit, push, or PR is made.

## Exact result

Cycle 125 tests the bounded object

```text
R_B01_MINIMAL_PHASE_PATCH_PROBE
```

at proper-cubic orientation 20 of the Cycle-121 geometry, mapped from the old
`R_B00` port onto the fresh Cycle-124 `R_B01` port. The target word is

```text
R_B01 = 10010001.
```

The patch makes two minimal intended-order changes:

1. D5 moves before D4, so its H0 record sits beside D4 before the two H0
   branches can expose the live two-perpendicular-H0 -> H1 orbit.
2. The final join changes from `R_C00` to `R_C01`, distinguishing the new
   `R_B01` completion from the already-live `R_B00` completion row.

In the displayed append order, those changes work. All fourteen transformed
sites are open; the eight records decode `10010001`; the inherited H1 cage
still fires; the candidate table is single-valued; and the completion local
maps to `R_B01` rather than colliding with `R_B00`.

The all-schedules result fails immediately. The translated TAIL site has no
neighbouring support when its row is introduced. Covariant closure therefore
turns it into the empty rule

```text
() -> R_B41.
```

The candidate also contributes 30 unary raw signatures. Compiling every local
subset exposes 130 unexpected targets. Exact asynchronous exhaustion stops at
the source with one bad `R_B41` transition before any intended write:

```text
explicit intended rows                      13
rotation-quotient canonical rows            12
candidate raw signatures                   159
complete raw union                       8,903
unexpected compiled targets                130
reachable states                             1
append edges                                  0
terminal histories                            0
intended candidate records reached            0
```

This closes only the named minimal patch.
It is **not a no-go against an R_B01 writer** and **not a no-go against recurrence**. The failure is useful
because it identifies what “phase-labelled” must mean at bare metal: a label
cannot be chosen as a role name alone; it needs local provenance that prevents
empty and unary rules from existing in the covariant table.

## Exact next repair target

The next target is a

```text
rail-attached provenance cage
```

or an equivalently specific local phase chain. It must do both jobs before
either H0 branch forms:

- give the prospective guard a nonempty, history-specific local signature;
- make at least one H0 branch causally depend on that guard, so delaying an
  enabled guard cannot expose the forbidden bare two-H0 local.

The best current concrete route is orientation 13. The transformed join site
`G0=(5,1,-3)` is open but sees the fixed local `L6+L6`. A candidate phase
chain can then run

```text
G0=(5,1,-3)
 -> G1=(6,1,-3)
 -> G2=(7,1,-3)
 -> G3=(7,2,-3)
 -> G4=(7,3,-3).
```

`G1` and `G3` neighbour the prospective D4 at `(6,2,-3)`; `G4` neighbours D1
at `(6,3,-3)`. Requiring `G4` in D1 would make the whole phase chain, including
the D4 guards, exist before D1/D2 can expose the bare two-H0 local. The next
probe must choose low-alias phase roles, close all proper-cubic images, and
exhaust the full graph; this note does not assert that the route lands.

**No axiom addition follows** from this bounded failure. It is a candidate-law
engineering result, not evidence that a reader, clock, global counter, or new
formation primitive is required.

## N1–N8 no-go-discipline gate

Status: **PASS only for the bounded negative against the orientation-20
D5-early/R_C01 patch; FAIL for a universal writer no-go, recurrence no-go,
role minimum, or axiom-need claim.** The current `origin/main`
no-go-discipline body governs this note.

### N1 — Alternative routes

| route | marker | result |
|---|---|---|
| orientation-20, D5 early, `R_C01` join | `ATTEMPTED / NEGATIVE` | intended order works; full subset graph fails at source through empty/unary aliases |
| orientation-13 `G0..G4` provenance chain | `LIVE / CONCRETE` | fixed `L6+L6` anchor and branch dependency are named; roles/full graph untested |
| rail-attached phase cage | `LIVE` | can import nonempty phase context from the repaired rail |
| redesign TAIL at a supported site | `LIVE` | directly removes the empty row while preserving early D5 |
| add an explicit inherited-cage row in orientation 13 | `LIVE` | may close the missing-image residual at additional row cost |
| start from a nonliteral writer geometry | `LIVE` | avoids the translated empty neighbourhoods entirely |
| branch-local completions followed by a final join | `LIVE` | alternative commit shape remains available |
| longer bridge to a less occupied region | `LIVE` | may yield richer support and fewer unary rows |

At least six materially distinct alternatives remain. The bounded failure
cannot support a universal negative.

### N2 — Residual independence

| pair | first closes second? | second closes first? | treatment |
|---|---|---|---|
| empty TAIL vs unary aliases | removing empty TAIL does not remove all unary rows | no | two related table-specific residuals |
| provenance cage vs two-H0 guard | cage can close guard only if a branch depends on it | no | one ordered repair |
| third word vs finite grammar | necessary evidence, not sufficient | grammar includes it | one downstream chain |
| finite grammar vs unbounded recurrence | necessary, not sufficient | recurrence includes grammar | one downstream chain |
| writer construction vs exact-law selection | no | no | independent residuals |

The third-word/grammar/recurrence chain is not inflated into independent
walls.

### N3 — Hidden-condition scan

The exact source, Cycle-124 terminal, orientation index, coordinate transform,
target word, D5 reorder, `R_C01` role, 13 explicit rows, 12 canonical rows,
159 raw signatures,
14 intended records, subset compilation, and append semantics are explicit.
“Intended-order success” means only that one constructed record sequence has
the desired local outputs; it does not mean the covariant asynchronous law is
valid. No scheduler is allowed to force TAIL before its aliases.

### N4 — Residual matching

| cited witness | witness residual | Cycle-125 residual | match and use |
|---|---|---|---|
| Cycle-124 literal-reuse probe | two-H0 conflict plus unary start ambiguity | D5/R_C01 minimal patch | exact local target; patched only in intended order |
| Cycle-121 provenance repair | rotated corrupt-boundary alias | empty/unary phase patch aliases | same all-schedules failure genus, not same row |
| generic `R_B01` writer | any finite append-safe word and completion | one failed orientation-20 patch | no match; not claimed closed |
| unbounded recurrence | induction over arbitrary roles | one 1-state negative graph | no match; not evidence |

Nonmatching residuals limit the conclusion.

### N5 — Resolution and rhetoric

Tested: one orientation, one D5 reorder, one join phase role, all 159 raw
signatures, every compiled local subset, and the exact asynchronous graph from
the official source. Not tested: the `G0..G4` role assignments, every phase
role, other rotations with redesigned cages, longer writers, simultaneous
apparatuses, or an infinite process. The result may be called a bounded
negative for this patch, not “R_B01 cannot be written.”

### N6 — Partial-closure paths and axiom discipline

The `G0..G4` chain is a direct constructive partial-closure path. Its fixed
`L6+L6` anchor eliminates the empty rule, and D1 dependence would enforce
guard-before-branch order. A rail-attached variant offers another source of
phase provenance. Both are candidate-law tests inside the existing local,
append-only framework. Failure of one unanchored translation does not motivate
a new primitive or formation axiom.

### N7 — Strongest hostile steelman

A hostile reviewer should say the proposed “phase label” was cosmetic: the
join role changed, but the tail had no local cause at all. The one displayed
append order silently behaved like a scheduler and hid an everywhere-enabled
empty rule plus many unary aliases. The result therefore gives no evidence for
a third writer. The only honest value is diagnostic: it forces the next probe
to carry phase as causal local structure and to pass full asynchronous
exhaustion before any compiler or recurrence language is used.

### N8 — Cross-cycle echo

Cycle 117 and Cycle 121 both required cages whose timing was enforced by local
dependencies. Cycle 121 additionally rejected a positive graph after a wrong
`VALID` rotation exposed a generic FRONT orbit. Cycle 125 repeats that lesson
more sharply: intended-order construction is not bare-metal sufficiency.
Context must eliminate every improper schedule and rotated alias. The concrete
provenance chain continues the same repair tradition; no constitutional
conclusion is warranted before it is tested.

## Verification

```text
python3 scripts/r_b01_minimal_phase_patch_probe_cycle125_2026_07_15.py
```
