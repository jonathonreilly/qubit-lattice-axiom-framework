# YT EW Matching Rule M Current-Packet Boundary

**Date:** 2026-05-02; narrowed 2026-05-27
**Claim type:** no_go
**Script:** `scripts/frontier_yt_ew_matching_rule_m_current_packet_boundary.py`
**Historical broad runner:** `scripts/frontier_yt_ew_matching_rule_m_stretch.py`
**Status authority:** independent audit lane only

---

## Status

This row is narrowed to a current-packet boundary. It records what the present
packet does and does not supply for the EW matching rule M residual.

The row no longer claims a global theorem that matching rule M is non-exact at
finite `N_c`, and it no longer claims an exhaustive no-go over all possible
non-perturbative disconnected-current or OZI routes. Those broader statements
would require a separate retained selector/no-go proof with the full route
checklist requested by audit.

## Bounded No-Go Claim

Within the current packet:

1. The algebraic color-channel fraction is exactly
   `F_adj = (N_c^2 - 1) / N_c^2 = 8/9` at `N_c = 3`.
2. The packet does not contain a retained selector that promotes this algebraic
   fraction to the physical EW current matching rule M.
3. The packet therefore supports only the boundary:

```text
F_adj = 8/9 is available as algebraic support.
Exact physical R_conn = 8/9 for EW matching rule M is not derived by this packet.
```

That is the full proposed re-audit surface.

## Current-Packet Route Inventory

The packet considers three route labels, but only as current-packet gaps:

| Route | Current-packet status |
|---|---|
| `S1` disconnected term identically absent | not supplied by this packet |
| `S2` disconnected term assigned only to `v` | not supplied by this packet |
| `S3` exact OZI/disconnected-current selector | not supplied by this packet |

This table is not an exhaustive proof that no future route can work. It is a
finite inventory of what the current packet lacks.

## Direct Dependencies

- [`YT_EW_COLOR_PROJECTION_THEOREM.md`](YT_EW_COLOR_PROJECTION_THEOREM.md)
  supplies the retained no-go parent boundary for the YT/EW projection lane.
- [`YUKAWA_COLOR_PROJECTION_THEOREM.md`](YUKAWA_COLOR_PROJECTION_THEOREM.md)
  supplies the color-channel algebra decoration under the retained graph-first
  `SU(3)` surface.

No external OZI theorem, glueball-spectrum computation, PDG Yukawa value, Higgs
VEV value, or empirical `R_conn` value is a dependency of this repaired row.

## Explicit Non-Claims

This note does not claim:

- a physical derivation of `R_conn = 8/9`;
- an exact finite-`N_c` non-exactness theorem;
- an exhaustive no-go over all possible matching-rule selectors;
- a retained OZI or disconnected-current theorem;
- any use of observed `y_t`, `v`, `m_H`, or fitted empirical `R_conn`;
- promotion of the parent YT/EW theorem;
- an audit verdict or direct ledger retag.

## No-Go Discipline Gate

This section records the review-loop N1-N8 gate for the negative boundary.
It is source-side review evidence only; independent audit still owns status.

- **N1 alternative routes.**
  1. Direct algebraic support route: the packet supplies `F_adj = 8/9`; this
     is retained only as algebraic support and does not by itself identify the
     physical EW matching rule M.
  2. `S1` disconnected-current absence route: listed and checked as not
     supplied by the current packet.
  3. `S2` disconnected-current assignment-to-`v` route: listed and checked as
     not supplied by the current packet.
  4. `S3` exact OZI/disconnected-current selector route: listed and checked as
     not supplied by the current packet.
  5. Future non-perturbative selector route: not closed by this theorem and
     therefore explicitly excluded from scope.
- **N2 wall independence.** The three route labels are not counted as
  independent global no-go walls. They are current-packet absences; any future
  retained selector would need its own source packet and audit.
- **N3 hidden-wall scan.** No OZI theorem, glueball-spectrum computation, PDG
  Yukawa value, Higgs VEV value, or empirical `R_conn` value is used as a
  hidden input. The note states exactly what the current packet lacks.
- **N4 residual matching.** The residual being closed is only
  "not derived by this packet." It does not match, and therefore does not
  claim to close, a universal finite-`N_c` non-exactness theorem or all
  possible non-perturbative disconnected-current routes.
- **N5 rhetoric audit.** The no-go is stated at current-packet resolution. It
  does not say "matching rule M can never be exact" or "no selector can ever
  derive it."
- **N6 partial-closure path scan.** A later retained selector, convention
  ratification, or direct non-perturbative current theorem could retire this
  current-packet boundary. That route remains open outside this row.
- **N7 steelman.** A hostile reviewer could build a retained OZI or
  disconnected-current theorem that turns the `8/9` algebraic support into a
  physical EW matching rule. This note does not preclude that route; it only
  records that the present packet does not contain it.
- **N8 cross-cycle echo.** Earlier YT/EW review failures came from converting
  local support gaps into broad no-go rhetoric. This repair avoids that
  pattern by keeping the statement at current-packet scope.

## Verification

Run:

```bash
python3 scripts/frontier_yt_ew_matching_rule_m_current_packet_boundary.py
```

Expected result:

```text
YT EW matching rule M current-packet boundary: PASS
PASS=29 FAIL=0
```

The historical stretch runner remains available for context, but its stronger
finite-`N_c` language is not the repaired row's load-bearing surface.

## Audit Request

Please re-audit only the current-packet boundary above. The intended safe
outcome, if the auditor agrees, is retained no-go/bounded-boundary status for
the statement that the current packet supplies `F_adj = 8/9` algebraic support
but no retained selector deriving exact physical EW matching rule M.
