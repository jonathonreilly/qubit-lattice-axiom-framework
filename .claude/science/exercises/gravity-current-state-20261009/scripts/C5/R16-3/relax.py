"""Relaxed (Young-measure) problem: |sigma'| = 1 a.e. (fast zigzag), so f^2 = g pointwise.
Half-zone level measure: Lebesgue on [0,H] (first rise = box) + atoms c_i at levels x_i (fast zigzags), sum c_i = pi - H.
Xi_{M,T2g} = Xi_{U,T2g} in this limit (f^2 = g). Quadrature: 1D level grid."""
import numpy as np, sys; sys.path.insert(0, '.')
from zz import xi_all
def relaxed_gf(H, atoms, n=1 << 14):
    # emulate as a 'sample list' with weights: build sample points whose mean reproduces the measure
    # first rise: n1 points uniform on [0,H]; atoms: replicated points; total weight pi
    n1 = int(n*H/np.pi); x1 = (np.arange(n1)+0.5)*H/n1
    xs = [x1]
    for (x, c) in atoms:
        xs.append(np.full(int(round(n*c/np.pi)), x))
    x = np.concatenate(xs)
    return x*x, x   # g, f (|f| = x)
if __name__ == '__main__':
    for m in [1.0, 0.3, 0.1]:
        print('== m = %.2f' % m)
        best = None
        for H in [0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.8, 2.2, 2.6, 3.0]:
            row = []
            for x0 in [0.1, 0.2, 0.3, 0.5, 0.7, 1.0, 1.4, 2.0, 2.6]:
                if x0 > H: row.append('   ---   '); continue
                g, f = relaxed_gf(H, [(x0, np.pi - H)])
                X = xi_all(g, f, m, nu=800)
                row.append('%+.2e' % X['M,T2g'])
                if best is None or X['M,T2g'] > best[0]: best = (X['M,T2g'], H, x0, X)
            print('H=%.1f ' % H + ' '.join(row))
        print('best', best)
