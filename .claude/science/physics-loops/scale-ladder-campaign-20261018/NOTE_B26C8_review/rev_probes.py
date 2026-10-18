"""Reviewer probes for the B26/C8 note. Execs the runner (default mode) read-only, then tests statements it does not test."""
import sys, io, contextlib
import numpy as np
RUNNER = "/home/user/wt-lanes/scripts/corner_fermion_symmetric_shift_letter_classification_2026_10_18.py"
src = open(RUNNER).read().replace("sys.exit(0 if FAIL == 0 else 1)", "")
ns = {"__name__": "runner"}
sys.argv = [RUNNER]
buf = io.StringIO()
with contextlib.redirect_stdout(buf): exec(compile(src, RUNNER, "exec"), ns)
print("runner (exec'd):", buf.getvalue().strip().splitlines()[-1])
g = ns
ok_all = True
def rep(name, ok, det=""):
    global ok_all; ok_all &= bool(ok); print(f"[{'PASS' if ok else 'FAIL'}] {name} {det}")
# P1: gauge-change law of the lifts: lam' = lam + mu + R^T mu, tau'(c) = tau(c) + eps(c) + eps(Rc) + const (no mu-terms in tau)
rng = np.random.default_rng(7)
ok = True; nt = 0
for trial in range(5):
    mu = rng.integers(0, 2, 3); eps = rng.integers(0, 2, 12)
    u2 = np.array([g['u'][t] ^ (int(np.dot(mu, np.array(s) % 2)) % 2) ^ eps[i1] ^ eps[i2] for (i1, i2, s), t in g['ET'].items()], np.uint8)
    for G in g['PSG']:
        x, _ = g['psg'](G['M'], u2); lam2 = x[:3].astype(int); tau2 = x[3:].astype(int)
        ok &= np.array_equal(lam2 % 2, (G['lam'] + mu + G['M'].T @ mu) % 2)
        d = (tau2 - G['tau'] - eps - eps[G['RC']]) % 2
        ok &= len(set(d)) == 1; nt += 1
rep("P1 gauge change (-1)^{mu.v+eps(c)}: lam' = lam + mu + R^T mu and tau'(c) = tau(c) + eps(c) + eps(Rc) + global const, "
    "so tau_h(c)+tau_h(-c) changes by 2eps(c)+2eps(-c) (+2 const), with no mu-terms", ok, f"({nt} lifts)")
# P2: the hygienic() filter is local: a 6-letter word that passes it but reduces to the E-free -i S
w = ['E+', 'Si', 'Rt', 'S', 'E+', 'S']
q = rng.uniform(-np.pi, np.pi, 3)
rep("P2 hygienic(E+ S^-1 Rt S E+ S) is True although the word equals -i S (E-free)",
    g['hygienic'](w) and np.allclose(g['Wt'](w, q), -1j * g['Sk'](q, 1)))
# P3: (A0 R_L)^2 = -Rt R_L is not a scalar, so z A0 R_L, z R_L A0 are not involutions (P R_L P^-1 is +-R_L or +-Rt)
X = g['mul'](g['A0D'], g['RL']); X2 = g['mul'](X, X)
rep("P3 (A0 R_L)^2 = -Rt R_L and it is not a scalar", g['bl_eq'](X2, g['scal'](-1, g['mul'](g['RTX'], g['RL'])))
    and not any(g['bl_eq'](X2, g['scal'](z, g['ONE'])) for z in (1, -1, 1j, -1j)) and set(X2) != {(0, 0, 0)})
# P4: Hermitian involution R_L P + (1-P) needs [R_L, P] = 0: M - M^dag = (R_L - 1)P - P(R_L - 1)
P = g['PH'][2]; M = {a: B @ P for a, B in g['RL'].items()}; M[(0, 0, 0)] = M.get((0, 0, 0), 0) + np.eye(12) - P
rep("P4 for the H_on = 2 projector P, M = R_L P + (1-P) is not Hermitian (so not a Hermitian involution)",
    g['bl_dist'](M, g['dag'](M)) > 0.1, f"|M - M^dag| = {g['bl_dist'](M, g['dag'](M)):.2f}")
print("REVIEWER PROBES:", "ALL PASS" if ok_all else "SOME FAIL")
