# T66 scratch: files

Author: Claude Sonnet 5.5 (same family as the supervisor; same-family checks, unrefereed). Repository never edited.

Pre-registration: `PREREG.md` (written before the degree-2 solve).

Engine (exact rational, sparse polynomials of translation-summed local functionals, Poisson bracket):
- `engine.py`, `model.py`, `solve.py`, `solve2.py`, `match.py`, `refs.py` : planar sector S1 = {h_xx,h_yy,h_zz}(x), 1D.
- `engine2.py`, `model2.py`, `solve2d.py`, `group2d.py`, `solve2d_sym.py`, `match2d.py`, `refs2d.py`, `refs2d_frame.py`, `cont2d.py`,
  `solve2d_matched.py`, `run_frame.py` : 2D sector {h_xx,h_yy,h_zz (sites), h_xy (faces)}(x,y), D4-symmetrised unknowns.

Controls (all run):
- `s1_controls.py`  : degree-1 bracket = G1[xi0] (block 112 T1) at c=1/2; fails at c=0,1/3 (planar).
- `s7_controls2d.py`: same in 2D with face timing; my real-space R2 is exactly gauge invariant; planar reduction of 2D R2 = 1D R2.
- `s0_continuum_expansion.py`, `s4b_exact.py`, `s5b_numeric.py`, `cont2d.py`: continuum ADM identity {C[N],C[M]} = G[xi], xi = (K/4a) q^{jk}(d_kN M - N d_kM),
  verified exactly (1D, random jets) and to degree 2 (2D, random jets) -- the reference pieces T3, V2, G-Lie, xi1 used for matching.
- `s11_planar_sensitivity.py`: wrong targets make the matched planar system inconsistent (matching rows are not vacuous).
- `group2d.py` self-test in `s7`/inline: C1, T2, R2, G1[xi0] are invariant under the 8-element dihedral group.

Results (logs): `planar_final.json`, `run_R2_identity.log`, `run_R2_adm.log`, `run_R2_frame.log`, `s12_exact_R1_2d` output in report.

Superseded scripts (do not use): `s4_continuum_identity.py`, `s5_cont_pieces.py` (1D truncated-identity bookkeeping failed at degree 2 for a reason I did not
track down; the exact 1D identity `s4b_exact.py` and the numeric-jet check `s5b_numeric.py` hold). `cont2d.py` had G1[xi1] at the wrong degree in its first version; fixed, and the 2D identity then holds.
