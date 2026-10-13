"""R19-23 (a)/(b), part 1: which polarizations are isolated from every other component (and from every
gauge/Stueckelberg direction) by the little group of q, for ANY O_h x T invariant kernel (Ward-satisfying or not)."""
import numpy as np, sys
sys.path.insert(0, '.')
from kernels import *
rng2 = np.random.default_rng(11)
print('s_EH =', s_EH)
# controls: EH Ward; TT block normalization
for nm, n, e in NAMED:
    for (w, q) in [(0.3, 0.7), (0.9, 0.2)]:
        p = np.concatenate([[w], q*n])
        v = np.einsum('ij,ijkl,kl->', e, s_EH*kernel(0*Ab[0], Beh, p), e)
        print('control %-6s  e.(sK_EH).e at (w,q)=(%.1f,%.1f): %.12f  vs w^2-q^2 = %.12f' % (nm, w, q, v, w*w-q*q))
_res = 0.
for _ in range(10):
    _w = rng2.normal(); _q = rng2.normal(size=3)
    _res = max(_res, np.abs(mat(kernel(0*Ab[0], Beh, np.r_[_w, _q])) @ gauge_dirs(_w, _q)).max())
print('EH gauge residual |K_EH . (p xi + xi p)| (max over 10 random p, all xi): %.2e' % _res)
# generic invariant kernel (all 32 directions)
def rand_kernel():
    return combA(rng2.normal(size=len(Ab))), combB(rng2.normal(size=len(Bb)))
print('\nIsolation test: generic kernel (all 6+26 invariant directions, random), 20 draws x random (omega, |q|).')
for nm, n, e in NAMED:
    u = vec(e)/np.sqrt(2)
    worst_mix = 0.; worst_g = 0.
    for _ in range(20):
        A, B = rand_kernel()
        w, q = rng2.uniform(-1, 1), rng2.uniform(0.05, 1)
        Q = Qmat(A, B, w, q*n, 0.37)
        r = Q @ u - (u @ Q @ u)*u
        worst_mix = max(worst_mix, np.abs(r).max())
        worst_g = max(worst_g, np.abs(u @ gauge_dirs(w, q*n)).max())
    print('  %-6s (q along %s): max |Q u - (uQu) u| = %.2e ; max |u . gauge dirs| = %.2e' % (nm, np.round(n, 3), worst_mix, worst_g))
# which components does face1 couple to?
A, B = rand_kernel(); n = fd3; w, q = 0.31, 0.53
Q = Qmat(A, B, w, q*n, 0.37)
# basis adapted to face-diagonal frame (n, a, b)
nv = np.r_[0, fd3]; av = np.r_[0, a3]; bv = np.r_[0, b3]; tv = t4
def sym(x, y): return (np.outer(x, y) + np.outer(y, x))/2
frame = {'h00': sym(tv, tv), 'h0n': sym(tv, nv), 'h0a': sym(tv, av), 'h0b': sym(tv, bv), 'hnn': sym(nv, nv),
         'haa': sym(av, av), 'hbb': sym(bv, bv), 'hna': sym(nv, av), 'hnb': sym(nv, bv), 'hab': sym(av, bv)}
names = list(frame); V = np.array([vec(frame[k]) for k in names]).T
V = V/np.linalg.norm(V, axis=0)
Qf = V.T @ Q @ V
print('\nFace-diagonal q, generic kernel: nonzero couplings (|entry| > 1e-12) in the (n, a, b) frame:')
for i, ki in enumerate(names):
    print('  %-4s couples to: %s' % (ki, [kj for j, kj in enumerate(names) if j != i and abs(Qf[i, j]) > 1e-12]))
n = z3
Q = Qmat(A, B, w, q*n, 0.37)
nv = np.r_[0, z3]; av = np.r_[0, 1., 0, 0]; bv = np.r_[0, 0, 1., 0]
frame = {'h00': sym(tv, tv), 'h0z': sym(tv, nv), 'h0x': sym(tv, av), 'h0y': sym(tv, bv), 'hzz': sym(nv, nv),
         'hxx+yy': sym(av, av)+sym(bv, bv), 'hxx-yy': sym(av, av)-sym(bv, bv), 'hzx': sym(nv, av), 'hzy': sym(nv, bv), 'hxy': sym(av, bv)}
names = list(frame); V = np.array([vec(frame[k]) for k in names]).T; V = V/np.linalg.norm(V, axis=0)
Qf = V.T @ Q @ V
print('\nAxis q (z), generic kernel: nonzero couplings:')
for i, ki in enumerate(names):
    print('  %-7s couples to: %s' % (ki, [kj for j, kj in enumerate(names) if j != i and abs(Qf[i, j]) > 1e-12]))
