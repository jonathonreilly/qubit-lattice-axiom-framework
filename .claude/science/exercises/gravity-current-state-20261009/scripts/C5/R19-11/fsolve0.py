"""R19-11 (b): off-axis rows at the m->0+ axial root and the two own-direction data (w_d, w_o) of the 12 vectors (R18-13's
Lemma O route: face rows linear in (w_d, w_o), triangular Jacobian, det = E0 T0/16 > 0). Inputs: scalar off-axis rows at
m = 1e-5 (mscan_s_root0.out), Dirac off-axis rows at m = 0 (mscan_d_root0_GL4_10.out), photon rows at the root's a (photface0_N224.npy)."""
import re, numpy as np
def grab(fn, mval, key):
    for line in open(fn):
        if line.startswith('m=%s ' % mval) or line.startswith('m=%-10s' % mval):
            off = line.split('| off:')[1]; return float(re.findall(r'%s ([+-]\d\.\d+e[+-]\d+)' % key, off)[0])
    raise KeyError((fn, mval, key))
NS, ND, NV = 4.0, 22.5, 12.0
s1, s2 = grab('mscan_s_root0.out', '1e-05', 'face1'), grab('mscan_s_root0.out', '1e-05', 'face2')
d1, d2 = grab('mscan_d_root0_GL4_10.out', '0', 'face1'), grab('mscan_d_root0_GL4_10.out', '0', 'face2')
P = np.load('photface0_N224.npy'); a = P[0]; F1, F2 = P[1:4], P[4:7]
tot1 = NS*s1 + ND*d1 + NV*F1[0]; tot2 = NS*s2 + ND*d2 + NV*F2[0]
J = NV*np.array([[F1[1]-F1[0], F1[2]-F1[0]], [F2[1]-F2[0], F2[2]-F2[0]]]); w = np.linalg.solve(J, -np.array([tot1, tot2]))
print('m->0+ root, a = %.10f: per scalar face1 %+.6e face2 %+.6e | per Dirac (m=0) face1 %+.6e face2 %+.6e | per vector face1 %+.8e face2 %+.8e' % (a, s1, s2, d1, d2, F1[0], F2[0]))
print('totals at (w_d, w_o) = (0, 0): face1 %+.6e face2 %+.6e' % (tot1, tot2))
print('Jacobian (12 vectors) %s det %+.5e -> (w_d, w_o) = (%+.8f, %+.8f)   [R18-13 at m = 0.01, N = 224: (-1.17155412, -0.19541845)]' % (J.tolist(), np.linalg.det(J), *w))
print('linear-model totals after solve: %+.2e %+.2e (Lemma O: exactly linear in (w_d, w_o) up to the grid artefact)' % tuple(np.array([tot1, tot2]) + J@w))
