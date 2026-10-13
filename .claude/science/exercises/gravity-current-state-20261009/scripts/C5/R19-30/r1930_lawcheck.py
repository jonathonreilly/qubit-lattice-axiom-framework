"""R19-30: analytic laws (lib1930) against the archived tabulated laws (R18-5 dirac.D1, R16-3 zz.ZLaw)."""
import sys, os, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, 'r195copy'))
from lib1930 import Scalar, Dirac
from dirac import D1
sys.path.insert(0, '/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/R19-5/arch18_5')
from zz import ZLaw
k = np.linspace(-np.pi, np.pi, 4001)[1:-1]   # open zone: sigma itself is a sawtooth at +-pi (f, g are smooth)
D = Dirac(); A = D1(0.909103707957, 0.555604225797)
print('Dirac: max|S-S_arch| %.1e |S\'-S\'_arch| %.1e |W-W_arch| %.1e |W\'-W\'_arch| %.1e  W_pi %.12f vs %.12f'
      % (np.abs(D.S(k)-A.S(k)).max(), np.abs(D.dS(k)-A.dS(k)).max(), np.abs(D.W(k)-A.W(k)).max(), np.abs(D.dW(k)-A.dW(k)).max(), D.Wpi, A.Wpi))
S = Scalar(); bs = 2.5261508; wA = np.pi - bs; Z = ZLaw([1.0, 0.0], [bs + wA/2], wA)
a = np.abs(k); sZ = np.sign(k)*np.interp(a, Z.k, Z.sig); spZ = np.interp(a, Z.k, Z.sp)
print('scalar: max|sigma - sigma_arch| %.1e  |sigma\' - sigma\'_arch| %.1e' % (np.abs(S.sig(k)-sZ).max(), np.abs(S.sigp(k)-spZ).max()))
print('scalar f = sigma sigma\' at +-pi: %.1e %.1e (flat zero)' % tuple(S.f(np.array([np.pi, -np.pi]))))
