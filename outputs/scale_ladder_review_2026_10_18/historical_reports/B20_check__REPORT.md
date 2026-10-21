# B20 check: all-isotropic step

Provenance: a fresh-context checker of the same model family. All code is its own (`chklib.py` on `B18_check/chk_model.py`). It read B20's pickles only to sample records and rebuilt each word. Saved by the supervisor from the hand-back.

**Totals: PASS=42 FAIL=0** (final runs). Earlier FAILs were the checker's own, and their logs are kept.

| Runner | Result |
|---|---|
| `chk1_L1_L2.py` | 11/0 |
| `chk2_W3.py` | 11/0 |
| `chk3_L4_fixed.py` | 12/0 |
| `chk4_search.py` | 6/0 |
| `chk5_dirac_screen.py` | 2/0 |

## Verdicts

1. **L1 holds.**
   - The little group at ±k* (order 96) has commutant dimension 6, with E1/2 and E5/2 each occurring once.
   - The symmetric on-site algebra is 6-dimensional and non-commutative, larger than the functions of H_on and Λ that B20 tested. L1 holds for all of it.
   - Every proof step checks: 512 doublets with worst deviation 2e−5, and Berry flux on 40.
   - **Caveats:**
     - (a) n_S = 0 gives zero velocity.
     - (b) **New:** a 4-fold D₊⊕D₋ level (λ₊ = λ₋) is an exact isotropic Dirac point. E1/2⊗T1 ∌ E5/2 kills the cross terms, leaving two untilted cones at |n_S|√2/3 of opposite chirality. B20's lemmas and screen excluded these levels.
     - (c) The 4-fold G3/2 levels are not covered.
2. **L2 holds,** for the D± doublet contributions only; a G3/2 level at E would add charge. "Words without R_L are always excluded" holds only for 2-fold doublets.
3. **L3 holds.**
   - A reflection is explicitly null-homotopic: U_s = 1 + (e^{iπs} − 1)P.
   - Hopf control: P with Hopf invariant ±1 still gives W₃[1 − 2P] = 0.
   - Additivity is exact.
   - Net chirality = W₃ agrees with the su2 control; Bessho–Sato was confirmed at abstract level.
4. **L4 holds** on (π/16)Z³. The doubler, X_r and M_r little groups are D4.
5. **Search.**
   - The r(k) test is sound.
   - 25 of 25 rejections and 24 of 24 witnesses were confirmed.
   - Some witnesses are 4-fold points labelled through a 2×2 projection, and some have zero speed; both still disqualify.
   - The census was reproduced. Its chirality convention is det M, which is minus the lattice flux.
   - The Lipschitz certificate was confirmed with Bauer–Fike.
   - **Scope gap:** B20 screened only 2-fold k* levels. The check screened Dirac levels in SKEL1 × PHL plus the two L202 taste skeletons: 1,872 Dirac levels, none passing. cliff2 and π/6 were not screened for Dirac levels.
6. **Framing.** Use "no tested step". The conditional obstruction applies to 2-fold doublets only, and Dirac levels escape it. Add PRL 121, 196401 (2018) (arXiv 1806.09296), "Three-dimensional chiral lattice fermion in Floquet systems".
