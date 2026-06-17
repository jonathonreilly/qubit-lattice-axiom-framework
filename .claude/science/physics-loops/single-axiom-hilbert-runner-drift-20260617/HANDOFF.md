# Handoff

This PR repairs a high-load audited-renaming source drift:

- the note no longer says Test 4 has monotone distance decay;
- the runner no longer prints "single axiom reduction" closure language;
- the cache now records the scope-narrowed output;
- Test 4 preserves the false monotone-gradient diagnostic and uses only the
  spread/localization contrast as bounded support.

Remaining blocker: a clean positive theorem would still need a retained
derivation of the local Hamiltonian, locality restriction, Born readout, and
support-as-edges rule from the actual framework surface. This PR does not
attempt that.
