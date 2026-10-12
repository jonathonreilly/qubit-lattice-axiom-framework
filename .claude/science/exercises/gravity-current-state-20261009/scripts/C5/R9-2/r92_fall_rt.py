"""C5 R9-2 (c), real-time check (d = 1, L = 512): evolve bound-state packets under the lapse Hamiltonian
H_g = H + g D1 by RK4 and read the fall directly, without the commutator identities.
  D1 = K   (interacting stress: binding energy gravitates)      -> expect d<P>/dt = -g<H>,  Xddot_E = -g
  D1 = K0  (comparator: only free energy gravitates)            -> expect d<P>/dt = -g<H0>
Observables: <P>(t) (lattice momentum), X_E(t) = <D1>/<H> (centre of energy).  Quadratic fits on t in [0, T].
"""
import numpy as np, sys, time
sys.argv = [sys.argv[0], '512']
exec(open('r92_fall_d1.py').read().split("T0 = time.time()")[0])
g = 2e-3; dt = 0.025; NT = 160
out2 = []
def pr2(*a):
    line = ' '.join(str(x) for x in a); print(line, flush=True); out2.append(line)
T0 = time.time()
pr2('real-time lapse evolution, L = %d, g = %.0e, dt = %.3f, T = %.1f (RK4)' % (L, g, dt, dt*NT))
for MU_B in ([float(a) for a in __import__("os").environ.get("MUB","0.85,0.95").split(",")]):
    lam, Kr, blocks = build(MU_B)
    H, H0, Pp, K, K0 = ops(blocks)
    for D1name in ['K', 'K0']:
        D1 = K if D1name == 'K' else K0
        Hg = lambda p: H(p) + g*D1(p)
        p = packet(Kr, MU_B, 0.0, 0.06, 'bound')
        ts, Ps, Xs, Hs, H0s = [], [], [], [], []
        for it in range(NT + 1):
            if it % 8 == 0:
                Hp = H(p); eH = ip(p, Hp).real
                ts.append(it*dt); Ps.append(ip(p, Pp(p)).real); Xs.append(ip(p, D1(p)).real/eH); Hs.append(eH); H0s.append(ip(p, H0(p)).real)
            if it == NT: break
            k1 = -1j*Hg(p); k2 = -1j*Hg(p + 0.5*dt*k1); k3 = -1j*Hg(p + 0.5*dt*k2); k4 = -1j*Hg(p + dt*k3)
            p = p + dt/6*(k1 + 2*k2 + 2*k3 + k4)
        ts = np.array(ts); Ps = np.array(Ps); Xs = np.array(Xs)
        cfP = np.polyfit(ts, Ps, 2); cfX = np.polyfit(ts, Xs, 3)
        slope = cfP[1]; acc = 2*cfX[1]
        pr2('  M_b = %.2f, D1 = %-2s: d<P>/dt|0 = %+.9e ; -g<H> = %+.9e ; -g<H0> = %+.9e ; ratio slope/(-g<H>) = %.9f ; Xddot_E/g = %+.6f ; norm drift %.1e  [%.0fs]'
            % (MU_B, D1name, slope, -g*Hs[0], -g*H0s[0], slope/(-g*Hs[0]), acc/g, abs(nrm(p) - 1), time.time() - T0))
with open('r92_fall_rt_%s.out' % __import__('os').environ.get('MUB','all'), 'w') as fh: fh.write('\n'.join(out2) + '\n')
