"""R18-9: 4-knob solve (b_s, b_f, r, a) at a FIXED photon edge whose VWa coefficients are parsed from a solve4k_*.out header line
(argv[1]); m, fr, start x, tag from argv. Identical rows to solve4k.py. Also reports the photon-grid sensitivity when two headers are given."""
import sys, re, time, numpy as np, lib9 as L
def parse(fn):
    line = open(fn).readline()
    m = re.match(r'photon gGw\(([\d.]+), w=([\d.]+)\) N=(\d+): T \(([^ ]+) ([^ ]+) ([^)]+)\) E \(([^ ]+) ([^ ]+) ([^)]+)\) muE ([^ ]+)', line)
    g = [float(v) for v in m.groups()]
    return g[0], g[1], int(g[2]), np.array(g[3:6]), np.array(g[6:9]), g[9]
bg, w, N, T, E, Vmu = parse(sys.argv[1]); m = float(sys.argv[2]); fr = float(sys.argv[3])
x = np.array([float(v) for v in sys.argv[4].split(',')]); tag = sys.argv[5]; q = (4, 10)
print('photon gGw(%.6f, w=%.6f) N=%d (parsed from %s); m = %g; scalar fr = %.3f' % (bg, w, N, sys.argv[1], m, fr))
def parts(x):
    bs, bf, r, a = x
    S = L.scal(bs, fr, m); F = L.dirac(bf, r, m=m, q=q)
    V = np.array([T[0] + T[1]*a + T[2]*a*a, E[0] + E[1]*a + E[2]*a*a, Vmu, 0.0])
    return S, F, V
def rows(x):
    S, F, V = parts(x); t = L.NS*S[:3] + L.ND*F[:3] + L.NV*V[:3]
    return np.array([t[0], t[1], t[2], L.ND*F[3]])
h = np.array([1e-5, 1e-6, 1e-6, 1e-6])
for it in range(8):
    f = rows(x); J = np.empty((4, 4))
    for j in range(4):
        dx = np.zeros(4); dx[j] = h[j]; J[:, j] = (rows(x + dx) - rows(x - dx))/(2*h[j])
    print('it %d x=(b_s %.9f, b_f %.9f, r %.9f, a %.9f) |rows|=%.2e detJ %.3e' % (it, *x, np.abs(f).max(), np.linalg.det(J)), flush=True)
    if np.abs(f).max() < 1e-13: break
    x = x - np.linalg.solve(J, f)
S, F, V = parts(x)
print('ROOT (b_s, b_f, r, a) = (%.10f, %.10f, %.10f, %.10f); rows %s; detJ %.4e; r<1/sqrt3 %s' % (*x, rows(x), np.linalg.det(J), x[2] < 1/np.sqrt(3)))
print('per real scalar (T,E,muE) %+.6e %+.6e %+.6e | per Dirac (T,E,muE,muT2) %+.6e %+.6e %+.6e %+.6e | per vector (T,E,muE) %+.6e %+.6e %+.6e' % (*S[:3], *F, *V[:3]))
np.save('root4c_%s.npy' % tag, np.r_[x, fr, bg, w/(np.pi-bg), m])
