"""R17-13 c4check: small-r expansion mu_T2^F = r^4 C4(b, m) + O(r^5) on D1 (mirror-symmetric Wilson class), with
C4 = (Nc/2) < A_x A_y (-1/E0^3 + 3 m^2/E0^5) + (A_x B_y + A_y B_x)(1/E0 - m^2/E0^3) + m^2 B_x B_y / E0 >,
A_j = w_j w'_j f_j, B_j = w'_j^2, f = s s', w = W/r, E0^2 = m^2 + sum s^2.  Checks C4 against mu_T2^F/r^4 at r -> 0, and the sign
pieces: cross <A_x B_y/E0> < 0, <A_x A_y/E0^3> > 0 (mirror lemma)."""
import sys, numpy as np
sys.path.insert(0, '.')
import lib13 as L
def C4(b, m, npan=6, ngl=16, Nc=4):
    law = L.D1law(b, 1.0)
    kx, wx = L.gl_panels([b, np.pi-b], 2*npan, ngl); kz, wz = L.gl_panels([0, b, np.pi-b, np.pi], npan, ngl)
    sx, spx, Wx, Wpx, _ = law.tab(kx); sz = law.tab(kz)[0]
    A = Wx*Wpx*sx*spx; B = Wpx**2
    S2 = sx[:, None]**2 + sx[None, :]**2; wxy = wx[:, None]*wx[None, :]
    parts = np.zeros(3)
    for iz in range(len(kz)):
        E0 = np.sqrt(m*m + S2 + sz[iz]**2)
        parts += wz[iz]*np.array([np.sum(wxy*A[:, None]*A[None, :]*(-1/E0**3 + 3*m*m/E0**5)),
                                  np.sum(wxy*(A[:, None]*B[None, :] + A[None, :]*B[:, None])*(1/E0 - m*m/E0**3)),
                                  np.sum(wxy*m*m*B[:, None]*B[None, :]/E0)])
    parts *= (Nc/2)/np.pi**3
    return parts.sum(), parts
for b in (0.15, 0.385, 0.9, 1.4):
    for m in (0.0, 0.001, 0.01, 0.3):
        c, p = C4(b, m)
        rat = [L.muT2(L.D1law(b, r), m, 6, 16)/r**4 for r in (0.04, 0.02, 0.01)]
        print('b=%.3f m=%.3g: C4 = %+.6e  [AA %+.3e, AB %+.3e, BB %+.3e] | mu_T2/r^4 at r=0.04,0.02,0.01: %s' % (b, m, c, *p, ' '.join('%+.6e' % x for x in rat)), flush=True)
