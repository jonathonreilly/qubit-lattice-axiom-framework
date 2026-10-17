# GEN-2 PREREG (written before any run; time stamped below)

Written 2026-10-17, clock read as 21:11Z (`date -u`). Deadline 21:30Z, so this is a short, symmetry-level pass.

Fixed readings: TESTS.md GEN-2 entry and GEN-2 amendment (binding): the generation label is the orientation a in {x,y,z} of an extended fermion cell (COL-1 rods). Cubic rotations permute generations as they permute axes; translations do not act on the label. Items c1-c6 as fixed; DIR-GAIN / DIR-PRICE / DIR-FAIL / OPEN as fixed; c6 failure reads DIR-PRICE if a floating translation-covariant cell law (or another allowed period) avoids it.

Model class: X2' (GEN-1) with the generation index carried by rod orientation. Little group of a rod along a is D4h; generation representation P = permutation rep of O_h on axes = A1g + Eg.

Planned checks (one script, gen2_symm.py, through capped.sh, cap 0.4 GB):
- S1 (c3, c4): character-table multiplicities under O_h of A1g in End(P) and in End(P) x Sym2(R3); decomposition of End(P).
- S2 (c3): circulant matrices = A1/A2 part of End(P); numerical check that zero E-projection <=> circulant, and that two circulants commute (CKM trivial). So nontrivial CKM needs an E component.
- S3 (c3): first-order eigenvalue response to an Eg perturbation: zero for a nondegenerate circulant (OBS-1 lemma), generically nonzero once Y has an E component.
- S4 (c2): Z3 (C3 about 111) and transposition charges of the three generations; Z3 anomaly sums Sum q, Sum q^3 times 16 modulo 3 and 9; Spin(10)^2-Z3 mixed sum.
- S5 (c6): which of the 8 corners fold onto Gamma under residual translations cZ^3 for c = 2..8; chiral index of the folded Gamma sector (X2': +3 at Gamma, net -3 at the 7 corners).

Decision rules: c3 clock-row size is taken from OBS-1's branch rates rescaled linearly by (GEN-2 coefficient)/(X2 coefficient); if the GEN-2 coefficient is not computed, the c3 size is labelled suggested and the reading uses it only if the conclusion holds for every coefficient >= 1e-2. c4: n counted as GEN-1 does (counterterms beyond the cubic-covariant per-field ones); any required non-cubic-covariant structure counts toward n.


## Follow-up 21:13Z (2026-10-17)
- gen2_symm.py ran once (peak 23 MB). No deviation in S1-S5.
- The GEN-2 tree-level strain coefficient was not computed (time). Per the decision rule, the c3 size is labelled suggested.
