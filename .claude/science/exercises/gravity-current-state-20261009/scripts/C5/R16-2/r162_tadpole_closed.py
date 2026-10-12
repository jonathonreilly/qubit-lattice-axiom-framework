"""R16-2 Lemma T check: Dirac tadpole at m -> 0 equals (1/2)<(s'(q_x) - 1)/(d_x^2 W)> x16pi^2 (S-part; the Wilson part is O(m)).
Compare with the runner's tadpole column at m = 0.1, 0.05 (linear extrapolation to 0). D1(1.0, 1/sqrt3), naive photon, lam = 0.05."""
import numpy as np, sys
sys.path.insert(0, '.')
from r162_laws import D1Law
from r85_box_qed_copy import kgrid1, deriv
from r162_dirac_scan import ce2
U = 16*np.pi**2; lam = 0.05; N = 128
L = D1Law(1.0, 1/np.sqrt(3), None, None, 0.1)
q = kgrid1(N); QX, QY, QZ = np.meshgrid(q, q, q, indexing='ij')
W = np.sqrt(L.d(QX)**2 + L.d(QY)**2 + L.d(QZ)**2 + lam**2)
sp = L.A.ds(QX)
closed = np.mean((sp - 1)/(L.d(QX)**2*W))/2*U
t = {m: ce2(D1Law(1.0, 1/np.sqrt(3), None, None, m), N, lam, 0.02)[1] for m in (0.1, 0.05)}
print('closed S-part tadpole (m->0) %+9.4f | runner tadpole m=0.1 %+9.4f, m=0.05 %+9.4f, linear extrap to 0 %+9.4f | max s\' = %.3f'
      % (closed, t[0.1], t[0.05], 2*t[0.05] - t[0.1], sp.max()))
