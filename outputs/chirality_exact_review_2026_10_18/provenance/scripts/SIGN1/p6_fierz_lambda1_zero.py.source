"""SIGN-1: the lambda1 = 0 point (Q = -sum_a (B^a B^a + h.c.)) as an exact Fierz identity in U(1)_c-neutral
pairing channels: sum_a B^a B^a = sum_f alpha_f sum_{e in f} Z_e Z_e, Z_e = X_e + i Y_e (neutral pairings).
Solve for alpha_f by least squares on 3000 + fresh 20000 sampled 4-index components; check signs vs Theta-parity."""
import numpy as np, sys, io, contextlib
sys.path.insert(0, __file__.rsplit("/", 1)[0])
buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    import pair_kramers_u1c as pk
def P(*a): print(*a); sys.stdout.flush()
fams = [("sing", "8v"), ("trip", "8v"), ("sing", "56v"), ("trip", "56v")]
for cols, q2, lab in ((pk.cols, pk.q2, "sample 3000"), (pk.fcols, pk.fq2, "fresh 20000")):
    # Q(lambda1=0, lambda2=-1) = -q2 ;  channel quartic: -(1/4) [g_Re A_Re + g_Im A_Im] with g_Im = -g_Re
    A = np.array([cols[f"pair:{s}:{y}:Re"] - cols[f"pair:{s}:{y}:Im"] for s, y in fams]).T * (-0.25)
    g, *_ = np.linalg.lstsq(A, -q2, rcond=None)
    rel = np.abs(A @ g + q2).max() / np.abs(q2).max()
    P(f"{lab}: g_Re (= -g_Im) per family {dict(zip([f'{s}:{y}' for s, y in fams], np.round(g, 10)))}; max relative residual {rel:.1e}")
for s, y in fams:
    P(f"  pair:{s}:{y}: Re parity {pk.parity(f'pair:{s}:{y}:Re')}, Im parity {pk.parity(f'pair:{s}:{y}:Im')}")
P("sign-free iff each family has g_Re <= 0 when Re is even (and then g_Im = -g_Re >= 0 on the odd Im), or g_Re >= 0 when Re is odd.")
# kernel of the 4-family ansatz and the sign-correct segment
A = np.array([pk.fcols[f"pair:{s}:{y}:Re"] - pk.fcols[f"pair:{s}:{y}:Im"] for s, y in fams]).T * (-0.25)
u_, sv, vt = np.linalg.svd(A, full_matrices=False)
P(f"singular values of the ansatz map: {sv}")
ker = vt[sv < 1e-10 * sv[0]]
P(f"kernel dimension {len(ker)}; kernel vector(s): {np.round(ker, 6).tolist()}")
g0, *_ = np.linalg.lstsq(A, -pk.fq2, rcond=None)
need = np.array([-1, +1, -1, +1])   # required sign of g_Re: sing:8v (Re even) <= 0, trip:8v (Re odd) >= 0, sing:56v <= 0, trip:56v >= 0
if len(ker) == 1:
    v = ker[0]; lo, hi = -np.inf, np.inf
    for i in range(4):
        # need[i] * (g0[i] + t v[i]) >= 0
        a, b = need[i] * v[i], need[i] * g0[i]
        if abs(a) < 1e-14:
            if b < 0: lo, hi = 1, 0
        elif a > 0: lo = max(lo, -b / a)
        else: hi = min(hi, -b / a)
    P(f"sign-correct t-interval: [{lo:.6f}, {hi:.6f}]")
    if lo <= hi:
        tm = (lo + hi) / 2 if np.isfinite(lo) and np.isfinite(hi) else (lo + 1 if np.isfinite(lo) else hi - 1)
        g = g0 + tm * v
        P(f"interior point t = {tm:.6f}: g_Re = {np.round(g, 6).tolist()}, min margin {np.min(need * g):.4f}, residual {np.abs(A @ g + pk.fq2).max() / np.abs(pk.fq2).max():.1e}")
from scipy.optimize import linprog
K2 = ker.T                                            # 4 x 2
# maximise m subject to need_i (g0 + K2 x)_i >= m, |x| <= 100
c = np.array([0, 0, -1.0]); Aub = []; bub = []
for i in range(4):
    Aub.append(np.concatenate([-need[i] * K2[i], [1.0]])); bub.append(need[i] * g0[i])
res = linprog(c, A_ub=np.array(Aub), b_ub=bub, bounds=[(-100, 100), (-100, 100), (None, None)], method="highs")
x = res.x[:2]; g = g0 + K2 @ x
P(f"max-margin sign-correct Fierz point: g_Re = {np.round(g, 6).tolist()}, margin {res.x[2]:.4f}, residual {np.abs(A @ g + pk.fq2).max() / np.abs(pk.fq2).max():.1e}")
# rational-looking point check: try g = (-a, +b, -c, +d) with small integers
