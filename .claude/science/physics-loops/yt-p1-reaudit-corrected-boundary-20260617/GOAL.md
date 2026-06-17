# Goal

Repair the YT P1 I_S restricted-packet verifier so it checks the corrected
2026-06-16 boundary instead of the invalidated native-candidate arithmetic.

The branch preserves:

- the conditional literature-bracket arithmetic as conditional context;
- the corrected BZ fallout (`I_v_scalar ~= 32.435`, positive O(50%) `Delta_R`
  diagnostic);
- the explicit statement that the corrected diagnostic is not a controlled
  retained replacement or precision prediction.

It does not run audit, retag the ledger, or land anything to main.
