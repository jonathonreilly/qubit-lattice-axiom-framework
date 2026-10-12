"""Lane RI / probe I2: readout Q-RI.  N* for the P0-level bound under stated scaling assumptions (READING).
Anomaly of a folded fine lattice with fine stencil range r: |A(K)| ~ c_r (K a/N)^(2r), c_r = 1/2, 1/6, 1/20, 1/70, 1/252
(exact leading coefficients, C3 referee).  Response quadratic in the defect (G3 design A): |A| <= sqrt(B);
linear: |A| <= B.  B = 5.7e-99 (refereed, reduced-Planck cell) and 9.0e-102 (framework convention, reading).
Loop content (all modes to the truncation edge): mode-averaged |A| = 1 for every N (sum rule) -> no finite N*.
"""
import numpy as np
out = []
def P(s=""):
    print(s); out.append(s)
cr = [0.5, 1/6, 1/20, 1/70, 1/252]
for B in (5.7e-99, 9.0e-102):
    P(f"B = {B:.1e}:  sqrt(B) = {np.sqrt(B):.3e}")
    P("   r   N*/(K a) quadratic   N*/(K a) linear     N*(K a = pi) quadratic   N*(K a = pi) linear")
    for r, c in enumerate(cr, 1):
        q = (c / np.sqrt(B))**(1 / (2 * r)); l = (c / B)**(1 / (2 * r))
        P(f"   {r}   {q:.3e}            {l:.3e}           {np.pi * q:.3e}               {np.pi * l:.3e}")
P("loop content (UV-weighted, d = 3): R_1 = -1.092, R_-1 = -0.874 for N = 2..64 (i2_fold.out): no finite N*.")
open('i2_nstar.out', 'w').write('\n'.join(out) + '\n')
