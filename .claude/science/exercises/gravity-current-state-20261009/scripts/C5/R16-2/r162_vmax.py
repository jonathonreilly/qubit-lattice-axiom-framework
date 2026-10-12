"""R16-2 v_max rule: axis group-velocity bound max|S'| (m -> 0) and max S' for the literal BQ edges used; D1 and G(b)
are subluminal by R14-1's theorems (|s'| <= 1 with W' = r sqrt(1 - s'^2), r <= 1/sqrt3; |grad eps_G| < 1). Also checks
max s' over D1's S(b) and A = u''/2 - 1 <= 0 for G(b) (Lemma T hypotheses)."""
import numpy as np, sys
sys.path.insert(0, '.')
from r85_box_qed_copy import Law, deriv
from sublum import SymS, SymG
kk = np.linspace(-np.pi, np.pi, 400001)
for (b1, b2) in [(1.0, 2.0), (2.0, 3.0), (0.5, 1.5), (1.0, 3.0), (2.5, 3.1)]:
    L = Law(b1, b2, 0.0, None, None, 0.1); Sp = deriv(L.S, kk)
    print('literal BQ box=(%.1f,%.1f): max S\' = %.6f, min S\' = %.3f -> axis v_max(m->0) = %.3f' % (b1, b2, Sp.max(), Sp.min(), np.abs(Sp).max()))
for b in (1.0, 1.2, 1.4):
    A = SymS(b); print('D1 symbol S(b=%.1f): max s\' = %.6f, min s\' = %.6f' % (b, A.ds(kk).max(), A.ds(kk).min()))
for b in (0.6, 1.0, 1.4, 2.0, 2.6):
    G = SymG(b); Aa = G.d2g(kk)/2 - 1
    print('G(b=%.1f): max A = %.3e, min A = %.3f, max h\' = %.6f' % (b, Aa.max(), Aa.min(), G.dh(kk).max()))
