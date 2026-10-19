# B24 check

Provenance: a fresh-context checker of the same model family. Lattice and letter checks use `B7_check/chk_core.py` (its own gauge and PSG) with Hermite-normal-form enumeration. Witness checks use its own builder, finite-difference cone diagnosis over 303 directions, and its own Λ₀ and point typing, on B18_check primitives. Saved by the supervisor from the hand-back.

| Script | Result |
|---|---|
| `chk1_lattices` | 12/0 |
| `chk2_letters` | 13/0 (first-run gauge-finder bug logged) |
| `chk3_witnesses` | 10/0 |
| `chk3b`, `chk4_pairs` | diagnostics |

## Verdicts

1. **Classification: confirmed, with one listing error.**
   - Exactly 10 lattices: sc 2π, π, π/2, π/4; fcc π, π/2, π/4; bcc 2π, π, π/2. bcc(π/4) is not in (π/4)Z³; B24's log and JSON are right, only the prose was wrong.
   - Bad-class counts are confirmed: 6/8, 6/10, 9/10.
   - No bad point is C3-fixed. All C2-pair points lie on (π/8)Z³.
2. **Scale-free theorem: confirmed.**
   - Every O-invariant lattice between 2πZ³ and (2π/N)Z³, N = 1–16 (including non-dyadic scales), is sc, fcc or bcc, with the same counts.
   - The witnesses are exact.
   - "Any scale" covers every taste group, because a closed O-invariant subgroup containing 2πZ³ is either a lattice or all of R³ (a flat spectrum).
3. **Letter identities and commutant: confirmed.**
   - S moves each corner by +f_c; R_L hops preserve the corner position.
   - The commutant of the Z_i is span{1, P}, and of {Z_i, Y} the scalars.
4. **Witnesses: 3 of 3 reproduced.** The logged minimum speeds are upper bounds, because only 43 directions were sampled.
5. **Route closure: true geometrically, overstated about pinning.**
   - **Non-rotation symmetries cannot rescue isotropy.** An irreducible linear little group lies in O_h and contains C3.
   - **The gap.** Pinning needs a unitary symmetry, while isotropy needs only spectral invariance, and B24's Λ₀ is spectral.
     - In S²·L101·S²·H13, Λ₀ = bcc(π/2), but its (π/4)(1,1,1) taste exists only as a transpose (antiunitary-type) taste. At 24 of 36 bad classes all levels are simple, so nothing is pinned there.
     - Across survivors, the odd-level bad classes are exactly those relying on such tastes.
   - **The real condition** is: C2-pair points mod Λ_u ⊆ T-fixed points mod Λ_sp.
     - It fails in all 10 cases with Λ_u = Λ_sp (B24's theorem).
     - It **holds in 29 of 42 strictly nested dyadic pairs** (`chk4_pairs`), e.g. Λ_u = 2πZ³ with Λ_sp = πZ³.
   - **So the route stays open where the spectral taste lattice strictly exceeds the unitary one.** Examples are antiunitary or transpose tastes, or tastes with nontrivial linear part.
   - Pinning at every C2-pair point of Λ_u is observed, not proved.
