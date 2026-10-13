"""R17-1 s6 (written before running). E_g-channel (diagonal polarization) version of the s2 windows, using the
weight-8 F2-invariant pattern mu8 (s1, contains diagonal slots). Diagonal components carry no orientation sign,
so E_g probes are covariant under the Z2 permutation action (s4 (1)). k along x, eps = (yy - zz)/sqrt2.
 (A') CSS: m1 = K sum_R sum_{s in R mu8} |c_s|^2 (needs <X_s X_t> = 0: GF(2) check as in s2)
 (B') dipole hop R mu8_x -> R mu8_{x+a}: symbol slope.
"""
import numpy as np, itertools, importlib.util, sys
spec = importlib.util.spec_from_file_location("s2", "s2_exact_symbols.py")
src = open("s2_exact_symbols.py").read().split("# exact symbols")[0]
src = src.split("# (A) X_s X_t in X-stabilizer group?")[0]
ns = {}; exec(src, ns)
TYPES, rotate, Rs, Gof, pos, canon = ns['TYPES'], ns['rotate'], ns['Rs'], ns['Gof'], ns['pos'], ns['canon']
mu8 = [((0,1,1),5,1),((0,1,2),2,1),((0,1,2),5,1),((1,1,1),0,1),((1,1,1),5,1),((1,1,2),5,1),((1,1,3),0,1),((2,1,2),2,1)]
mu8 = [((x, t), v) for x, t, v in mu8]
orb = {}
for R in Rs:
    r = rotate(mu8, R); orb.setdefault(canon(r), r)
orb = list(orb.values())
print("mu8: all rotations F2-invariant:", all(all(v % 2 == 0 for v in Gof(p).values()) for p in orb), "; distinct copies:", len(orb))
def chat(supp, k, eps):
    tot = 0j
    for (x, t), v in supp:
        i, j = TYPES[t]; c = eps[i, j] if i == j else 2*eps[i, j]
        tot += np.exp(1j*k @ pos(x, t))*c*v
    return tot
eps = np.zeros((3,3)); eps[1,1] = 1/np.sqrt(2); eps[2,2] = -1/np.sqrt(2)
d = np.array([1.0, 0, 0]); ks = np.array([1e-3, 3e-3, 1e-2, 3e-2, 1e-1, 3e-1])
A = [sum(abs(eps[TYPES[t][0], TYPES[t][1]] if TYPES[t][0] == TYPES[t][1] else 2*eps[TYPES[t][0], TYPES[t][1]])**2 for p in orb for (x, t), v in p) for kk in ks]
B = [sum(abs(chat(p, kk*d, eps))**2*abs(1 - np.exp(1j*kk*d @ a))**2 for p in orb for a in np.eye(3)) for kk in ks]
for name, vals in [("(A') CSS mu8, E_g pol, k||x", A), ("(B') dipole hop mu8, E_g pol, k||x", B)]:
    vals = np.array(vals); sl = np.diff(np.log(vals))/np.diff(np.log(ks))
    print("%s: m1(1e-3) = %.4e ; m1/k^2 = %.4e ; slopes %s" % (name, vals[0], vals[0]/ks[0]**2, np.round(sl, 3)))
