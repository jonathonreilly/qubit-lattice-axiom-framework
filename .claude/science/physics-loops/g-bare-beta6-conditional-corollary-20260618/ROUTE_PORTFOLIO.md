# Route Portfolio

1. Direct beta=6 derivation from canonical trace normalization: rejected for
   this PR because it would be circular without a separate action-coefficient
   theorem.
2. Safe source repair: keep the exact algebra but make `beta=6` an explicit
   scoped input. Implemented.
3. Future frontier route: prove a framework-native local Wilson coefficient
   theorem that supplies `beta=6` without reusing `g_bare=1`.
