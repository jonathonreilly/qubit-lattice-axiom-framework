# Review History — koide-staggered-first-order block01

## 2026-06-11 local self-review (pre-PR)

Findings and fixes applied before commit:

1. **Orientation check was vacuous as first written** (any 3-cycle is
   permutation-conjugate to any other, so "conjugate to the same shift"
   proved nothing). Fixed: both triplet blocks are now pinned in
   canonical axis-index bases and required to EQUAL the explicit shift
   matrix; exact equality verified (check 10).
2. **"Vanishes off the K-real line" was coded as a derivative by an
   absent symbol** (trivially zero). Fixed: replaced with the
   harmonicity criterion — Laplacian over (Re b, Im b) is 0 with c
   independent and -12a on the K-real line (check 15).
3. **Grassmann engine sign convention was n-parity-dependent** in the
   first implementation (global reorder). Fixed: principled nested
   single-generator Berezin left-integration; first-power identity now
   verified uniformly (checks 6-7).

Disposition: **pass** (local). Independent audit and external review
still required; the note's status lines say so explicitly.
