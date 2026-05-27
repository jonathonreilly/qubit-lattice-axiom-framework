# Assumptions And Imports

## Direct Authorities

- `ew_current_fierz_channel_decomposition_note_2026-05-01` supplies the exact
  SU(N_c) channel fraction `F_adj = (N_c^2 - 1)/N_c^2`.
- `ew_current_matching_rule_open_gate_note_2026-05-03` supplies the retained
  no-go that the current packet does not derive `kappa_EW = 0`.
- `rconn_derived_note` is retained as bounded context for the older R_conn
  route, but the repaired row does not use it to derive the physical selector.

## Local Algebra

- `F_singlet = 1/N_c^2`.
- `Pi_EW^phys(kappa_EW) = F_adj + kappa_EW F_singlet`.
- `K_EW(kappa_EW) = 1/(F_adj + kappa_EW F_singlet)`.
- At `N_c = 3`, `K_EW(kappa_EW) = 1/(8/9 + kappa_EW/9)`.

## Firewalls

- No physical connected-trace selector is derived.
- No exact unconditional `9/8` EW coefficient is derived.
- No new axiom or convention is introduced.
- Independent audit remains required.
