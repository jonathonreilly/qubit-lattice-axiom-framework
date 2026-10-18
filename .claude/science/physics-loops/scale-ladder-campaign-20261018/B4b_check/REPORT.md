# B4b independent check: headline holds, reframed as a missing seagull

Provenance: a fresh-context agent of the same model family. Its own bubble implementation matches B4b's to 3e−15 (the kernel definition is shared by design). Saved by the supervisor from the hand-back.

## Findings

- **No contradiction with the repo.** The repo's telescope runner claims only exact operator identities. It lists the seagull and full Ward closure as open, and the isotropy, TT and dispersion notes disclaim the Ward bridge.
- **One repo overclaim.** `UNIVERSAL_GR_STRESS_WARD_TRANSVERSE_SEAGULL_BOUNDED_THEOREM_NOTE_2026-06-08.md` (2-component model) says "transverse to leading physical order (residual O(k³))". Its seagull is K-independent, equivalent to the Π(0) subtraction. The symbol-level ratio is 0.88: the same leading-order break.
- **Scaling.**
  - Without the Π(0) subtraction, |k̂·Π| ~ K¹.
  - With it, |k̂·Π| ~ K³.
  - The symbol Ward ratio is 0.18–0.23 depending on direction; B4b's 0.229 is the maximum.
  - It stays roughly constant as m falls (0.177 → 0.186), so it is not a heavy-mass artefact.
- **B4 symbol space.** Dimension 9, Ward map rank 8, and the one remaining invariant is EH (cosine 1.0). a_EH = 0.028815. The non-EH fraction is 0.92 (norm-dependent). E/T2 = 1.042 raw.
- **Exact identity** (to 5e−15). k̂·Π_bubble is a sum of one-propagator loops: exactly the shape a two-graviton seagull's tadpole produces.
  - Π(0) is the unique K-independent seagull, and removes only the O(K) part.
  - A local nearest-neighbour seagull S(K) = (a·EH − T)[k̂,k̂] restores the identity, with the residual falling from K³ to about K⁵ on an out-of-fit direction.
  - But no lattice diffeo fixes it: restoring Ward means tuning 8 B4 coefficients, and a_EH (the induced 1/G) stays free.
- **S vertex** is confirmed not Brillouin-zone periodic.

## Corrections to B4b

- Describe the defect as a missing or underived seagull: a contact term that a local seagull removes but no symmetry fixes. Not intrinsic.
- Quote 0.23 as the maximum over directions.
- Note the repo's 2-component "transverse seagull" note shows the same O(1) violation.
