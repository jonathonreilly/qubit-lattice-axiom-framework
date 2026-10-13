"""R18-9 (b): Jacobian of the four rows in the declared knobs (b_s, b_f, r, a) at a root (argv[1] .npy), photon coefficients
parsed from argv[2] (a solve4k_*.out header). Reports J, singular values, det, and the knob shift per unit residual."""
import sys, re, numpy as np, lib9 as L
z = np.load(sys.argv[1]); x = z[:4]; fr, m = z[4], z[7]
line = open(sys.argv[2]).readline()
g = [float(v) for v in re.match(r'photon gGw\(([\d.]+), w=([\d.]+)\) N=(\d+): T \(([^ ]+) ([^ ]+) ([^)]+)\) E \(([^ ]+) ([^ ]+) ([^)]+)\) muE ([^ ]+)', line).groups()]
T, E, Vmu = np.array(g[3:6]), np.array(g[6:9]), g[9]
def rows(x):
    bs, bf, r, a = x; S = L.scal(bs, fr, m); F = L.dirac(bf, r, m=m, q=(4, 10))
    V = np.array([T[0] + T[1]*a + T[2]*a*a, E[0] + E[1]*a + E[2]*a*a, Vmu])
    t = L.NS*S[:3] + L.ND*F[:3] + L.NV*V
    return np.array([t[0], t[1], t[2], L.ND*F[3]])
h = np.array([1e-5, 1e-6, 1e-6, 1e-6]); J = np.empty((4, 4))
for j in range(4):
    dx = np.zeros(4); dx[j] = h[j]; J[:, j] = (rows(x + dx) - rows(x - dx))/(2*h[j])
np.set_printoptions(precision=4)
print('J (rows T2g, Eg, muE, muT2; cols b_s, b_f, r, a):\n', J)
print('singular values', np.linalg.svd(J, compute_uv=False), 'det %.4e' % np.linalg.det(J))
print('knob response to a unit residual in each row (columns of J^-1):\n', np.linalg.inv(J))
