# B24 findings: taste-enlarged steps

Provenance: a worker of the same model family; not yet checked. Saved by the supervisor from the hand-back. The model is `b24base.py`, a copy of B23's `b23lib.py`.

| Runner | Result |
|---|---|
| `lattice_classification.py` | PASS=6 |
| `scale_free_obstruction.py` | PASS=3 |
| `letter_tastes.py` | PASS=11 |
| `b24_screen.py mix2` | PASS=5 |
| `b24_screen.py small` | PASS=5 |
| `analyse.py` | PASS=1 |

Two first-run expectation errors are logged (12 commuting C2 pairs, not 9; fcc at 2π does not contain 2πZ³). The `probe_*`, `test_tastes`, `certify` and `run_screens*` files are helpers, not evidence.

**Bottom line.**
- No translation or taste lattice, at any scale, makes every C2-pair point T-fixed (exact).
- Enlarging the taste group only moves the bad D4/D2 points to finer momenta.
- 0 of 449 classified survivors pass. The search was cut short; the gaps are listed below.

## 1. Lattice classification (exact)

- **Ten rotation-invariant lattices** satisfy 2πZ³ ≤ Λ ≤ (π/4)Z³: sc at 2π, π, π/2, π/4; fcc at π, π/2, π/4; bcc at 2π, π, π/2, π/4.
- **None makes all C2-pair classes T-fixed.** Bad classes: sc 6 of 8; fcc 6 of 10; bcc 9 of 10. Checked to (π/32)Z³.
- **Scale-free theorem.** Around k* the action is linear, q → Rq, so every invariant lattice is sc_a, fcc_a or bcc_a. Each has a witness fixed by a commuting C2 pair and by no C3, at every scale a:
  - sc: (a/2)e_x, little group D4;
  - fcc: (a/2)(0,1,1), little group D2;
  - bcc: (a/2)e_z, little group D4.
- **Enlarging only relabels.** In the sc chain the bad points move k* + πe_i → (π/2)e_i → (π/4)e_i → (π/8)e_i.
- **Scope:** rotations only (no inversion or antiunitaries), and pure translation tastes. At operator level all 42,036 defect nodes found at C2-pair points had even levels. Pinned 2-fold nodes also occur off C2-pair points.

## 2. Letters and search

- **Letter identities (exact).**
  - S^n(k+t) = S^n(k)·diag(e^{int·f_c}).
  - R_L(k+t) = D_t R_L(k) D_t⁻¹, with D_t = diag(e^{−it·f_c/2}).
- **On-site algebra.**
  - The commutant of the Z_i is span{1, PP}, so the plane letters are exactly PP + e^{iφ}(1 − PP).
  - The commutant of {Z_i, Y} is the scalars.
  - Generic Clifford letters admit only scalar gauges.
- **Gauge-chain rule** (derived by hand; facts and examples checked). The reachable level-preserving lattices form an sc/bcc chain up to sc(π/4). fcc is not reachable with these letters through letter-level diagonal gauges. A random-word census agrees.
- **Exact tastes.** For S^a·A·S^a·L202 with a = 1, 2, 4: Z_i W(k) Z_i = W(k + (π/a)e_i) and Y W Y = −W(k + (π/2a)(1,1,1)).
- **Search** (R_L excluded; the B20/B23 criterion):

  | Family | Words | Levels | Survivors | Clean |
  |---|---|---|---|---|
  | Mixed powers S·S^{2,4} × Clifford | 25,600 | 27,680 | 378 | 0 |
  | S²·S⁴, S⁴·S⁴ | 19,200 | 20,760 | 353 | not classified (time limit) |
  | Reduced taste families, plane letter × Clifford | 1,520 | 1,633 | 71 | 0 |
  | Full taste families with PHL | — | — | — | not completed |

## 3. Obstruction pattern (observed, not proved)

- **Defects:**
  - at C2-pair points: 38,040 anisotropic, 3,804 flat, 192 isotropic at another speed;
  - off C2-pair points: 18,976 anisotropic;
  - at generic points: 12,674;
  - at T-fixed points: higher-multiplicity levels (8-fold anisotropic, 10-fold flat), which the lemmas do not cover.
- **Best cases.**
  - S·H20·S²·L020: 26 defects, with anisotropic 4-fold cube-point nodes.
  - S⁴·L101·S⁴·L123 (Λ₀ = sc(π/4)): 20 defects, all at generic momenta.
- So with the largest tastes the failure moves from pinned D4 doublets to generic-point nodes at E.
- No counting claim is made for the pinning mechanism. It is a reflection E → 2E − E′ in the mixed-power family, but not universally.

## Status

- **Exact:** the lattice classification and scale-free witnesses; the letter identities and commutants.
- **Derived:** the gauge-chain rule. It is a restriction for this palette, not a general no-go.
- **Numerical:** the screen, a negative search.
- **Open:**
  - stage C for the 353 S²/S⁴ survivors;
  - the full PHL and π/6 taste families;
  - higher-multiplicity levels;
  - non-diagonal or longer-range tastes;
  - tastes with nontrivial linear part.

The route "make every pinning point T-fixed with a larger taste lattice" is closed for pure translation tastes.
