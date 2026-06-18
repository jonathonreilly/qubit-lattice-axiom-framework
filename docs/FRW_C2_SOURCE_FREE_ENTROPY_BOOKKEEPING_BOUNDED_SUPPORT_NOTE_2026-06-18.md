# FRW C2 Source-Free Entropy Bookkeeping Bounded Support

**Date:** 2026-06-18
**Claim type:** bounded_theorem
**Type:** bounded_theorem
**Status:** bounded support for finite source-free entropy bookkeeping only.
**Status authority:** independent audit lane only. This note is not an audit
result and does not alter any row status.
**Primary runner:**
[`scripts/frontier_frw_c2_entropy_bookkeeping_2026_06_18.py`](../scripts/frontier_frw_c2_entropy_bookkeeping_2026_06_18.py)
**Cached runner output:**
[`logs/runner-cache/frontier_frw_c2_entropy_bookkeeping_2026_06_18.txt`](../logs/runner-cache/frontier_frw_c2_entropy_bookkeeping_2026_06_18.txt)

## Claim-Status Certificate Snapshot

```yaml
actual_current_surface_status: bounded-support
trace_class: direct_blocker_closure
reachability_to_target: partially_closes
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "This proves source-free entropy bookkeeping algebra only; it does not prove the real cosmological era is source-free."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Target

The parent FRW open gate's C2 premise says that, between the heavy-Majorana
leptogenesis era and the CMB-recombination era used by the eta cascade, the
comoving entropy density `s a^3` is conserved up to `g_*S(T)` step-function
bookkeeping and no additional entropy injection is admitted.

This note partially closes the bookkeeping part of C2. It proves the finite
algebra behind source-free comoving-entropy conservation, internal entropy
transfer, `g_*S T^3 a^3` step compensation, and conserved charge-over-entropy
ratios.

This is source-free entropy bookkeeping only. It does not derive that the real
cosmological era is source-free, does not derive C1, does not derive the
Standard Model g_*S table, does not derive reheating/decay absence, and does
not set audit status. No new axiom, registry premise, Tier-A admission,
observational comparator, or fitted value is introduced.

## Statement

Let a finite entropy inventory be represented by component comoving entropies

```text
S_i := s_i a^3.
```

For a finite update

```text
S_i' = S_i + Delta_i,
```

the total comoving entropy changes by

```text
S_total' - S_total = sum_i Delta_i.
```

Therefore:

1. If `sum_i Delta_i = 0`, the update is source-free at the total level and
   `S_total` is exactly conserved. Individual components may change by
   internal transfer.
2. If `sum_i Delta_i != 0`, total comoving entropy is not conserved. That is
   exactly the C2 source/injection residual.
3. In a source-free thermal step with entropy density proportional to
   `g_*S T^3`, the exact invariant is

   ```text
   g_*S(T) T^3 a^3 = const.
   ```

   When `g_*S` changes from `g_1` to `g_2`, the compensated temperature scaling
   is

   ```text
   T_2 / T_1 = (g_1 / g_2)^(1/3) (a_1 / a_2).
   ```

   Plain `T proportional to a^-1` is correct only when `g_*S` is unchanged.
4. If a conserved charge `N_B` and total comoving entropy `S_total` are both
   conserved, then `N_B / S_total` is conserved. If entropy is injected while
   `N_B` is fixed, the ratio changes.

## Proof

The finite update identity is immediate:

```text
S_total' = sum_i (S_i + Delta_i)
         = sum_i S_i + sum_i Delta_i
         = S_total + sum_i Delta_i.
```

This proves both the source-free conservation statement and the source-term
failure statement. Internal transfer is allowed because the condition is only
on the total `sum_i Delta_i`; individual `Delta_i` need not vanish.

For the `g_*S` step, the finite invariant is

```text
S = C g_*S T^3 a^3,
```

where the common constant `C` cancels in any equality check. Setting
`S_1 = S_2` gives

```text
g_1 T_1^3 a_1^3 = g_2 T_2^3 a_2^3,
```

so

```text
T_2 / T_1 = (g_1 / g_2)^(1/3) (a_1 / a_2).
```

The runner checks this with exact rational cube choices and also checks that
omitting the `g_*S` compensation fails by the ratio `g_2/g_1`.

For a conserved charge `N_B`, the ratio result follows from ordinary fraction
equality:

```text
N_B / S_start = N_B / S_end
```

when `S_start = S_end`. If `S_end != S_start`, the ratio changes unless an
equal compensating charge source is also supplied. This note supplies no such
source.

## Boundary

This bridge does not derive:

- that the actual leptogenesis-to-CMB window is source-free;
- absence of reheating, late decay, or entropy injection;
- the Standard Model `g_*S(T)` table or any numerical thermal threshold;
- C1 homogeneity/isotropy;
- the Friedmann equations;
- baryon number generation or freeze-out physics;
- `N_eff`, `Delta N_eff = 0.046`, or any observed cosmological parameter;
- an effective retained audit status.

The result is still useful because it removes the purely mathematical
bookkeeping part of C2 from the import list. What remains is the physical
premise that the relevant cosmological window is actually source-free and uses
the stated `g_*S` inventory.

## Trace

The direct blocker being partially addressed is the parent request to close or
explicitly admit C1-C3 before re-auditing the FRW backdrop. This note does not
close C2. It narrows C2 by replacing textbook entropy bookkeeping with an exact
finite source-free invariant.

The remaining C2 residual is:

- prove or explicitly admit that the actual leptogenesis-to-CMB window has no
  entropy source/injection beyond the stated internal `g_*S` transfers;
- provide retained or approved authority for the `g_*S(T)` inventory used in
  the eta cascade.

## Verification

Run:

```bash
python3 scripts/frontier_frw_c2_entropy_bookkeeping_2026_06_18.py
python3 scripts/cached_runner_output.py --refresh scripts/frontier_frw_c2_entropy_bookkeeping_2026_06_18.py
python3 scripts/cached_runner_output.py --check-only scripts/frontier_frw_c2_entropy_bookkeeping_2026_06_18.py
```

Expected result:

```text
VERDICT: bounded support passes for finite source-free entropy bookkeeping. The real no-injection cosmological era, g_*S table, C1, and audit status remain open.
```
