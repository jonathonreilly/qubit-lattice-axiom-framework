# DM Selector Shifted-Relative-Action Recovered-Packet Closure Theorem

**Date:** 2026-04-21
**Status:** bounded conditional algebra on a supplied objective and recovered packet
**Claim type:** bounded_theorem
**Primary runner:** `scripts/frontier_dm_selector_shifted_relative_action_recovered_packet_closure_2026_04_21.py`

## Statement

The supplied shifted-relative-action objective has a unique minimizer on the
**current recovered comparison packet**. This is conditional algebra, not a
physical selector closure.

Supply the same scalar objective used by the conditional off-seed calculator,

```text
S_rel(H || H_seed)
  = Tr(H_seed^(-1) H) - log det(H_seed^(-1) H) - 3,
```

and transport it to the common positive comparison windows

```text
A_mu(H) = H + mu I.
```

This gives the shifted same-law packet

```text
S_mu(H || H_seed)
  = Tr(A_mu(H_seed)^(-1) A_mu(H))
    - log det(A_mu(H_seed)^(-1) A_mu(H)) - 3.
```

Then on the current recovered bank of five lifts:

- for every checked common positive shift in the packet, the preferred
  recovered lift `0` is the **unique** minimizer of `S_mu`,
- on a dense admissible stress range from the positivity edge to large shifts,
  the same unique minimizer persists,
- and that same lift `0` is exactly the unique recovered point with
  `Im(K_Z3[1,2]) > 0`.

So the same supplied scalar objective picks one recovered lift throughout the
tested packet. No physical source-selection rule is derived.

## Prior branch state

Four earlier same-day results are integrated here.

1. `docs/DM_LEPTOGENESIS_PMNS_RELATIVE_ACTION_CONDITIONAL_CALCULATOR_NOTE_2026-07-12.md`
   evaluates the supplied scalar objective on the fixed `N_e` seed
   parameterization.
2. `docs/DM_SELECTOR_RELATIVE_ACTION_RECOVERED_BRANCH_SEPARATION_SUPPORT_THEOREM_NOTE_2026-04-21.md`
   shows that the supplied candidate does **not** itself land on the recovered
   comparison branch.
3. `docs/DM_SELECTOR_RELATIVE_ACTION_RECOVERED_PROJECTION_SUPPORT_THEOREM_NOTE_2026-04-21.md`
   shows that the same supplied candidate is nearest to the preferred recovered
   lift `0` in the checked metric packet.
4. `docs/DM_SELECTOR_SHIFTED_DOUBLET_IMAG_SIGN_SUPPORT_THEOREM_NOTE_2026-04-21.md`
   shows that among recovered lifts only the preferred lift `0` lies on the
   positive side of the canonical odd doublet boundary
   `Im(K_Z3[1,2]) = 0`.

Those results still left one live current-package burden:

- justify the recovered selector law itself, rather than only a projection
  toward it.

## Bounded packet result

### 1. The same scalar logdet law extends naturally to the common positive windows

The raw seed-relative action is not defined on the whole recovered bank, since
some recovered lifts leave the seed-positive branch.

But the exact scalar grammar is unchanged by passing to any common positive
window

```text
A_mu(H) = H + mu I,
```

with `mu > mu_floor`, where

```text
mu_floor = max_i repair(H_i).
```

This is the natural SPD-cone continuation of the same LogDet/Bregman law on
the recovered packet.

### 2. Every checked common positive shift has the same packet minimizer

For the branch-local checked shift family

```text
mu = mu_floor + s,  s in SHIFT_OFFSETS,
```

the shifted relative action `S_mu(H_i || H_seed)` has the same unique
minimizer on the whole recovered bank:

- lift `0` is always the unique minimizer,
- the worst checked uniqueness gap is still strictly positive.

So the selector is not a one-window accident.

### 3. The same minimizer survives dense admissible stress

On a dense stress sweep from immediately above the positivity threshold out to
large shifts, the same unique minimizer persists.

So the branch-local packet does not show any minimizer swap within the
admissible shifted family:

```text
argmin_i S_mu(H_i || H_seed) = 0
```

throughout the checked stress range.

### 4. The same exact law activates the positive odd doublet side

The shifted-imaginary sign theorem already showed:

- lift `0`: `Im(K_Z3[1,2]) > 0`
- lifts `1,2,3,4`: `Im(K_Z3[1,2]) < 0`.

Therefore the shifted same-law minimizer is not just the preferred recovered
lift abstractly. It is exactly the unique recovered point on the positive side
of the canonical odd doublet boundary.

### 5. Consequence

On the supplied recovered comparison packet, the relative-action objective,
its recovered image, the breakpoint candidate `tau_b,min`, and the positive
shifted-imaginary doublet side all identify lift `0`.

## What this does and does not close

The bounded result is only finite-packet minimizer agreement for a supplied
objective. It does not close a physical point-selection law, the DM flagship
lane, a source-chart/sign law, or the derivation of the PMNS target surface.
Those remain separate open obligations.

## Reproduction

```bash
PYTHONPATH=scripts python3 scripts/frontier_dm_selector_shifted_relative_action_recovered_packet_closure_2026_04_21.py
```

Expected:

```text
SUMMARY: PASS=13 FAIL=0
```

## Audit dependency repair links

This graph-bookkeeping section records explicit dependency links named by a prior conditional audit so the audit citation graph can track them. It does not promote this note or change the audited claim scope.

- [dm_leptogenesis_pmns_relative_action_conditional_calculator_note_2026-07-12](DM_LEPTOGENESIS_PMNS_RELATIVE_ACTION_CONDITIONAL_CALCULATOR_NOTE_2026-07-12.md)
- [dm_selector_relative_action_recovered_branch_separation_support_theorem_note_2026-04-21](DM_SELECTOR_RELATIVE_ACTION_RECOVERED_BRANCH_SEPARATION_SUPPORT_THEOREM_NOTE_2026-04-21.md)
- [dm_selector_relative_action_recovered_projection_support_theorem_note_2026-04-21](DM_SELECTOR_RELATIVE_ACTION_RECOVERED_PROJECTION_SUPPORT_THEOREM_NOTE_2026-04-21.md)
- [dm_selector_shifted_doublet_imag_sign_support_theorem_note_2026-04-21](DM_SELECTOR_SHIFTED_DOUBLET_IMAG_SIGN_SUPPORT_THEOREM_NOTE_2026-04-21.md)
