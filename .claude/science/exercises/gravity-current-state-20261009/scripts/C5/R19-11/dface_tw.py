"""R19-11 P-R19-11c: twisted-mass version of R18-13's archived dface.xi_dirac (source read and patched in memory; archive untouched):
M -> W_tot (no m), c -> (S_x, S_y, S_z, W_tot, m), G/c'/c'' get a zero fifth component. At m = 0 it must equal the archived rows."""
import os, sys, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); A13 = os.path.join(HERE, '..', 'arch18_13')
sys.path.insert(0, A13); sys.path.insert(1, os.path.join(HERE, '..', 'arch18'))
import dface
src = open(os.path.join(A13, 'dface.py')).read()
fn = src[src.index('def xi_dirac'):src.index('def relation')]
rep = [('M = m + Wx + Wy + Wz', 'M = Wx + Wy + Wz'), ('c = [Sx + 0*M, Sy, Sz, M]', 'c = [Sx + 0*M, Sy, Sz, M, m + 0*M]'),
       ('G = [0*M, 0*M, 0*M, 0*M]', 'G = [0*M, 0*M, 0*M, 0*M, 0*M]'),
       ('n[0]*wp_[0] + n[1]*wp_[1] + n[2]*wp_[2]]', 'n[0]*wp_[0] + n[1]*wp_[1] + n[2]*wp_[2], 0*M]'),
       ('n[0]**2*wpp_[0] + n[1]**2*wpp_[1] + n[2]**2*wpp_[2]]', 'n[0]**2*wpp_[0] + n[1]**2*wpp_[1] + n[2]**2*wpp_[2], 0*M]'),
       ('def xi_dirac(', 'def xi_dirac_tw(')]
for a, b in rep:
    assert fn.count(a) == 1, a; fn = fn.replace(a, b)
ns = dict(dface.__dict__); exec(fn, ns); xi_tw = ns['xi_dirac_tw']
if __name__ == '__main__':
    from content3 import D1q
    z = np.load(os.path.join(HERE, 'root0_final.npy')); law = D1q(z[1], z[2]); rows = ('T2g', 'Eg', 'face1', 'face2')
    X0 = dface.xi_dirac(law, 0.0, rows=rows, npan=4, ngl=10); T0 = xi_tw(law, 0.0, rows=rows, npan=4, ngl=10)
    print('validation m=0 archived %s | twisted %s' % ([X0[r] for r in rows], [T0[r] for r in rows]), flush=True)
    for m in (5e-4, 1e-3, 2e-3, 4e-3):
        Tm = xi_tw(law, m, rows=rows, npan=4, ngl=10)
        print('m=%-6g twisted %s ; (row - row0)/m^2 %s' % (m, ['%+.9e' % Tm[r] for r in rows], ['%+.4e' % ((Tm[r] - T0[r])/m**2) for r in rows]), flush=True)
