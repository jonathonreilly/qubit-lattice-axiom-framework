"""Pointwise consistency (diagnostic only): reviewer's matrix-route bubble vs the author's closed-form F(k,t).
Also checks that the reviewer's U(k) reproduces the author's spectrum (f) and that H^2 = omega^2."""
import sys, os
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import r8_walk as rw
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'scripts'))
import c8_core as cc
PASS = FAIL = 0
def check(n, ok):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok); print(('PASS' if ok else 'FAIL'), n)
rng = np.random.default_rng(1)
bs = rw.bstar(); print('b* =', bs, ' author:', cc.POINTS['bstar'])
check('b* root agrees with the author constant to 1e-12', np.max(np.abs(bs - np.array(cc.POINTS['bstar']))) < 1e-12)
for name, b, th in (('bstar', bs, 0.0), ('iso', rw.B_ISO, 0.0), ('gold', rw.B_GOLD, 0.2)):
    W = rw.Walk(b, theta=th, hhat=(0.0, 1.0)); A = cc.Walk(name, theta=th, chi=np.pi/2)
    if name == 'gold':
        k0 = rng.uniform(-np.pi, np.pi, (2000, 3)); qh0, e0 = cc.tt_eps('z', 'A')
        own = rw.bubble(W, rw.vertex(W, k0, e0, 'M1'), k0 + 0.3*qh0, k0 - 0.3*qh0)
        W.Fh = cc.build_F(cc.POINTS['gold'])[1:]          # adopt the author's h-plane frame (W = 0 at b_gold)
        aut = rw.bubble(W, rw.vertex(W, k0, e0, 'M1'), k0 + 0.3*qh0, k0 - 0.3*qh0)
        print(f'  b_gold theta=0.2: pointwise F differs between h-frames by up to {np.max(np.abs(own-aut))/np.max(np.abs(aut)):.1e} (relative)')
        check('gold: the massive walk depends on the mass direction relative to the h-plane frame (chi undefined since W = 0)',
              np.max(np.abs(own - aut))/np.max(np.abs(aut)) > 1e-6)
    k = rng.uniform(-np.pi, np.pi, (2000, 3))
    om, V = W.bands(k); u, x = A.sym(k)
    check(f'{name}: |omega| = arccos f (author) to 1e-12', np.max(np.abs(np.sort(np.abs(om), 1)[:, 0] - cc.Efun(u))) < 1e-12)
    U = W.U(k); check(f'{name}: U unitary', np.max(np.abs(U @ np.conj(np.transpose(U, (0, 2, 1))) - np.eye(4))) < 1e-13)
    for qn, pol in (('z', 'A'), ('f', 'B'), ('d', 'A')):
        qh, eps = cc.tt_eps(qn, pol)
        t = 0.3
        Vm = rw.vertex(W, k, eps, 'M1')
        mine = rw.bubble(W, Vm, k + t*qh, k - t*qh)
        auth = cc.Fval(A, 'M1', eps, qh, k, t)
        check(f'{name} M1 {qn}{pol}: matrix-route bubble = author F(k,t=0.3) (rel 1e-10)', np.max(np.abs(mine - auth))/np.max(np.abs(auth)) < 1e-10)
print(f'TOTAL: PASS={PASS} FAIL={FAIL}')
