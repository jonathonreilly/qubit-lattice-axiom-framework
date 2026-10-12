"""R16-10: the zero curve G*(b) on D1(b, 1/sqrt3) and on literal(2,3); dF/dG and dF/dm at the zero (N = 64, 96)."""
import numpy as np, time
from r1610_eval import *
from r1610_laws import *
t0 = time.time()
def F(G, mat, N, m=1e-6):
    d = photon('R85', 1.0, 2.0, G)
    matter = dirac_D1(mat[1], mat[2]) if mat[0] == 'D1' else dirac_lit(mat[1], mat[2])
    return K[0.5] + lattice_part(0.5, N, m, 0.0, matter, d, 0.25, 0.7, 0.02)[0]
for mat in [('D1', 1.4, 1/np.sqrt(3)), ('D1', 1.2, 1/np.sqrt(3)), ('D1', 1.0, 1/np.sqrt(3)), ('D1', 1.4, 0.2), ('lit', 2.0, 3.0)]:
    for N in (64, 96):
        a, b = 2.5, 4.0; Fa = F(a, mat, N)
        for it in range(14):
            c = 0.5*(a + b); Fc = F(c, mat, N)
            if np.sign(Fc) == np.sign(Fa): a, Fa = c, Fc
            else: b = c
        Gs = 0.5*(a + b)
        dFdG = (F(Gs + 0.02, mat, N) - F(Gs - 0.02, mat, N))/0.04
        dFdm = (F(Gs, mat, N, m=0.02) - F(Gs, mat, N, m=0.01))/0.01
        print('%-28s N=%3d  G* = %.4f  dF/dG = %+.4f  dF/dm(0.01-0.02) = %+.4f' % (str((mat[0], mat[1], round(mat[2], 4))), N, Gs, dFdG, dFdm), flush=True)
print('elapsed %.1fs' % (time.time() - t0))
