# Block 106 — control and findings (2026-09-23)

1. **Provenance.** Workers j5c0d and j152a are Claude Opus 5.5. Their Grok referees (jc358, jf88c) confirmed the commutator, the weights and the zero mean, and the bond form, the sublattice counterexample, the upwind cancellation and the first-order no-go. The supervisor ported the exact checks, keeping the arithmetic machinery verbatim.
2. **A vacuous check, caught by the census.** On a 4³ torus the two-step difference u(x+2e) − u(x−2e) vanishes identically, so the reach-three plane-wave check was empty. It was moved to 8³, and a nonvanishing force is now required.
3. **Prior art placed.**
   - Blocks 54 and 66 as landed on main (c3f8c47a58: block 54's exact packet force withdrawn; block 66's lattice force at leading order), 63, 64, 69, 72 and 73, and #8644.
   - New: the general zero-mean theorem, the exact bond form, the rate-carrying member, the equal-content no-go, and the two-step bond form.
