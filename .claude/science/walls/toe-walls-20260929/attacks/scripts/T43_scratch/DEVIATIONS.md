# Deviations from PREREG.md (recorded honestly)

1. First construction of the offset-averaged spin-taste singlet omitted the Kogut-Susskind phase correction at odd hypercube
   corners. It gave exactly zero determinant phase for the "singlet" and mismatched the 07-02 note's Gamma_f (dev 0.5). The P0
   comparison caught it; the correction (Gamma_A -> (-1)^{rho_s(A)} Gamma_A, rho_s(A)=sum_mu A_mu sum_{nu<mu} s_nu) was added to
   stag.py, after which the operator equals Gamma_f exactly (2D, flux and free) and equals (-1)^{x1+x3} sym prod C_mu (4D).
   All reported numbers are from the corrected code; the pre-fix output files were overwritten.
2. P2 coefficient criterion (1 +- 0.25 of 2 Q arctan(m5/m)) FAILED at the pre-registered m = 0.5 (c = 0.69). A follow-up m and L
   scan (p2b_mscan.py, added after seeing the failure) shows c -> 0.98 at m = 0.05, L = 16 (2D) and c increasing with L in 4D
   (0.63 at L=4, 0.81 at L=6, m = 0.1). This is post hoc, not pre-registered. Structural criteria (proportional to Q, odd in Q,
   zero at Q = 0, linear in arctan) passed.
3. P3 (4D) coefficient criterion (1 +- 0.3) passes only at L = 6, m = 0.1; fails at L = 4 and at m = 0.5.
4. An expectation written in my working notes (singlet phase odd under U -> U*) was wrong: on SU(3) hot 4^4 the phase is EVEN
   under U -> U* (C-even, P-odd like theta Q) and odd in m5. Not pre-registered; reported as measured.
