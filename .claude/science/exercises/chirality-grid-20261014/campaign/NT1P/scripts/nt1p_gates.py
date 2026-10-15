"""NT-1' gates G-LEG (b1), (b1-W), (d), G1, G5-G7 on joined configurations from the W-matched pool P-B; charge-set check C0;
quadrature node counts and timing (no kernel numbers).  usage: python3 nt1p_gates.py"""
import numpy as np, time
from nt1p_lib import *
from lat2d import Geom, rand_half, nodes, wrap
from k2b_lib import admissible

Lx, T = 4, 4; S = Strip(Lx, T); G = Geom(Lx, T, False, -1); t00 = time.time()


def wmatched_pool(seed, k, margin, s0=0.25):
    rng = np.random.default_rng(seed); U = []
    while len(U) < k:
        u = rand_half(rng, G, s0, margin); v = {'x': u['x'] - u['x'][0].sum() / Lx, 't': u['t'].copy()}
        if admissible(G, v, margin): U.append(v)
    return U


U = wmatched_pool(2504, 10, 0.55)
np.savez('pool_NT1P_PB_random_Lx4_Lt8_seed2504.npz', ux=np.array([u['x'] for u in U]), ut=np.array([u['t'] for u in U]))
print(f"# NT-1' gates Lx={Lx} Lt={2*T}; pool P-B (10 random W-matched, seed 2504) saved; max|W1| {max(abs(u['x'][0].sum()) for u in U):.1e}", flush=True)
for n in (2, 3, 4, 5):
    ph, w = nodes(G, U[0], U[1], 0.6, n, 'hard'); print(f"Duffy n={n}: {len(w)} crossing nodes per entry (entry 0,1), weight sum {w.sum():.10f}")
rng = np.random.default_rng(7); J = []
for (a, b) in [(0, 1), (2, 5), (7, 9)]:
    ph, w = nodes(G, U[a], U[b], 0.6, 3, 'hard'); idx = rng.choice(len(w), 2, replace=False); J.append(S.joined(U[a], U[b], ph[idx]))
J = np.concatenate(J); print(f"gate configurations: {len(J)} joined fields (3 pool pairs x 2 quadrature nodes)")

M = Measure(S, '11112', Ns=8, sk=+1)
# ---- (b1-W): Ward identity of the NON-canonical ray measure, fixes s_k ----
lower = (S.site_t < 1).astype(float)
Om = [np.repeat((0.3 * lower)[None], len(J), 0), rng.normal(0, 0.3, (len(J), S.ns)), rng.normal(0, 2.0, (len(J), S.ns))]
for sk in (+1, -1):
    M.sk = sk; line = []
    for Ns in (4, 8, 16):
        W1, _, _ = M.logrho(J, Ns=Ns, canon=False); v = 0.0
        for om in Om:
            Wg, _, _ = M.logrho(S.gauge(J, om), Ns=Ns, canon=False); d = Wg - W1
            v = max(v, np.abs(d.real).max(), np.abs(np.angle(np.exp(1j * d.imag))).max())
        line.append(v)
    print(f"(b1-W) s_k={sk:+d}: non-canonical Ward residual max|d ln rho| at transport R(2), R(4), R(8): " + " ".join(f"{v:.2e}" for v in line), flush=True)
    if sk == +1: wp = line
    else: wm = line
SK = +1 if wp[-1] < wm[-1] else -1; M.sk = SK
other = (wm if SK == +1 else wp)[-1]; mine = (wp if SK == +1 else wm)[-1]
print(f"(b1-W) s_k = {SK:+d}; other sign / chosen at R(8) = {other/mine:.1e} (registered: > 100)", flush=True)
# L1 Ward residual without the Q correction (descriptive) and with it
for model, uq in (('L1', False), ('L1', True), ('11112', False)):
    ML = Measure(S, model, Ns=8, sk=SK, use_Q=uq); line = []
    for Ns in (4, 8, 16):
        W1, _, _ = ML.logrho(J, Ns=Ns, canon=False); v = 0.0
        for om in Om:
            Wg, _, _ = ML.logrho(S.gauge(J, om), Ns=Ns, canon=False); d = Wg - W1
            v = max(v, np.abs(np.angle(np.exp(1j * d.imag))).max())
        line.append(v)
    print(f"(b1-W, descriptive) {model} use_Q={uq}: Ward phase residual at R(2), R(4), R(8): " + " ".join(f"{v:.2e}" for v in line), flush=True)
# ---- (b1) exact gauge invariance of the canonical measure ----
W1, r1, Ac = M.logrho(J, parts=True); v = 0.0
for om in Om:
    Wg, _, _ = M.logrho(S.gauge(J, om)); d = Wg - W1; v = max(v, np.abs(d.real).max(), np.abs(np.angle(np.exp(1j * d.imag))).max())
print(f"(b1) canonical measure: max|ln rho(U^Lambda) - ln rho(U)| = {v:.2e} -> {'PASS' if v <= 1e-10 else 'FAIL'} (<= 1e-10); "
      f"|div kbb - Abar| {np.abs(S.div(r1['kbb']) - r1['Abar']).max():.1e}", flush=True)
# ---- G5-G7 on the gate configurations ----
print(f"G5 min|eig H_W(U^e)| over ray points {r1['gmin']:.3f}; G6 index 0 {r1['idx_ok']}; G7 |sum Abar| {r1['sumA']:.1e}; max|W_t| of canonical reps {np.abs(S.FW(Ac)[1]).max():.3f}")
# ---- G1 factorization ----
g1 = 0.0
for e in (1, 2):
    w, V = eig_H(S, e * J); n = S.N // 2; rp = np.where(S.g5 > 0)[0]; rm = np.where(S.g5 < 0)[0]
    _, l1 = np.linalg.slogdet(V[:, rp][:, :, n:]); _, l2 = np.linalg.slogdet(V[:, rm][:, :, :n])
    ld, _ = vec_logdet(S, e * J, m=0.0); g1 = max(g1, np.abs(l1 + l2 + 2 * n * np.log(2) - ld.real).max())
print(f"G1 |det M_L||det M_R| = |det D_ov|: max |log difference| {g1:.1e} -> {'PASS' if g1 < 1e-10 else 'FAIL'}")
# ---- (d) reflection condition ----
for Ns in (8, 16):
    Wf, _, _ = M.logrho(J, Ns=Ns); Wr, _, _ = M.logrho(S.theta(J), Ns=Ns)
    c = Wr - np.conj(Wf); cph = np.angle(np.exp(1j * (c.imag - c.imag[0])))
    print(f"(d) Ns={Ns}: c = ln rho(theta U) - conj ln rho(U): Re spread {np.ptp(c.real):.2e}, Im c[0] {c.imag[0]:+.6f}, Im spread (mod 2pi) {np.abs(cph).max():.2e}", flush=True)
    if Ns == 8: c8 = c
    else: c16 = c
tc = np.abs(c16 - c8).max(); spread = max(np.ptp(c8.real), np.abs(np.angle(np.exp(1j * (c8.imag - c8.imag[0])))).max())
print(f"(d) spread {spread:.2e}; transport change R(4)->R(8) of c {tc:.2e}; threshold max(1e-6, 10x) = {max(1e-6, 10*tc):.1e} -> {'PASS' if spread <= max(1e-6, 10*tc) else 'FAIL'}")
# modulus-only reflection (descriptive): Re c should be 0 if |rho| is theta-even
# ---- C0: charge set 3-4-5-0 admissibility ----
for delta, margin, pool in ((0.6, 0.55, U), (0.3, 0.275, wmatched_pool(2505, 4, 0.275))):
    gm = {3: np.inf, 4: np.inf, 5: np.inf, 1: np.inf, 2: np.inf}
    for (a, b) in [(0, 1), (1, 2), (2, 3)]:
        ph, w = nodes(G, pool[a], pool[b], delta, 3, 'hard'); A = S.canon(S.joined(pool[a], pool[b], ph))
        for t in np.arange(1, 9) / 8:
            for e in gm:
                for c in range(0, len(A), 64):
                    ww, _ = np.linalg.eigh(S.H(t * e * A[c:c+64])); gm[e] = min(gm[e], np.abs(ww).min())
    print(f"C0 delta={delta} (margin {margin}): min|eig H_W(U^e)| along rays, e=1..5: " + " ".join(f"e{e}:{gm[e]:.3f}" for e in sorted(gm)), flush=True)
# ---- timing: one entry, full chiral measure at n = 3 ----
ph, w = nodes(G, U[0], U[1], 0.6, 3, 'hard'); A = S.joined(U[0], U[1], ph); t0 = time.time()
for c in range(0, len(A), 48): M.logrho(A[c:c+48])
print(f"timing: one entry n=3 ({len(w)} nodes): {time.time()-t0:.1f}s; done [{time.time()-t00:.0f}s]")
