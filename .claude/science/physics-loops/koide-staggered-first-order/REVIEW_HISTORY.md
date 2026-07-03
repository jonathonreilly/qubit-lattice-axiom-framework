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

Branch self-review disposition: **source proposal passed local pre-PR
review**. Independent audit and external review still required; the
note's status lines say so explicitly.

## 2026-06-11 block02 local self-review (pre-PR)

1. **Refinement of block01's headline made explicit, not buried:** the
   channel-general localization has TWO antiunitary tying classes
   (K-real cross-block gamma = conj beta; Hermitian in-block z zbar);
   block01's c = conj(b) line is the circulant locus where they
   coincide. The block02 note states this as a refinement of block01
   in its Role section.
2. **Universal quantifier discipline:** "every channel" is over the
   computed 24-dim commutant (dimension verified two independent ways,
   lattice realizability exhibited), with bilinear/equivariant scope
   declared as residuals — not an open-ended family claim.
3. **Stray construction removed** (unused projector split in check 16's
   setup) before commit.

Branch self-review disposition: **source proposal passed local pre-PR
review**. Independent audit still required.

Cluster-cap status: block02 is the 2nd PR in the koide parent-row family
this campaign — below the 3-PR evaluator threshold.
