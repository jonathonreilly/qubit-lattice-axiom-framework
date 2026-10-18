"""Claim 3 (letter level): constant-V tastes V X(k) V^-1 = w X(k + pi e), own model; joint tastes with an INDEPENDENT w per letter."""
import sys, itertools, time
sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
from mymodel import *
P = F = 0
def check(n, ok, d=""):
    global P, F; P += bool(ok); F += (not ok); print(f"[{'PASS' if ok else 'FAIL'}] {n}  {d}", flush=True)
t0 = time.time(); rng = np.random.default_rng(5); KS = rng.uniform(-np.pi, np.pi, (5, 3))
ES = [e for e in itertools.product((0, 1), repeat=3) if any(e)]
WS = [np.exp(1j * np.pi * j / 4) for j in range(8)]
def rows_for(Xf, e, w):
    R = []
    for k in KS:
        X1 = Xf(k); X2 = Xf(k + np.pi * np.array(e))
        R.append(np.kron(np.eye(12), X1.T) - w * np.kron(X2, np.eye(12)))    # row-major vec: vec(V X1) - w vec(X2 V)
    return R
def invertible_in_null(R):
    A = np.vstack(R); _, sv, Vh = np.linalg.svd(A); null = Vh[np.sum(sv > 1e-8):].conj()
    if len(null) == 0: return 0, False
    c = rng.normal(size=len(null)) + 1j * rng.normal(size=len(null)); V = (c @ null).reshape(12, 12)
    s = np.linalg.svd(V, compute_uv=False); return len(null), bool(s.min() > 1e-8 * s.max())
def table(Xfs):
    """for each e: list of (w-index tuple) admitting an invertible V, one independent w per letter"""
    out = {}
    pre = {(i, e, j): rows_for(Xf, e, WS[j]) for i, Xf in enumerate(Xfs) for e in ES for j in range(8)}
    for e in ES:
        out[e] = [js for js in itertools.product(range(8), repeat=len(Xfs))
                  if invertible_in_null(sum((pre[(i, e, j)] for i, j in enumerate(js)), []))[1]]
    return out
Aa = lambda a: (lambda k: A0m @ Sk(k, a))
S = lambda k: Sk(k, 1); Hon = lambda k: HON0.astype(complex); RLk = lambda k: bloch(RL, k); RTk = lambda k: bloch(RTX, k)
for a in (0, 1, 2):
    t = table([Aa(a)])
    check(f"A_{a} alone: invertible taste for every e, exactly with w = +-1", all(sorted(t[e]) == [(0,), (4,)] for e in ES), str({e: t[e] for e in ES[:2]}))
tS = table([S])
check("S alone: invertible taste only for e = (1,1,1), w = 1 (S(k + pi(1,1,1)) = S(k); k* -> -k*)",
      all(tS[e] == [] for e in ES if e != (1, 1, 1)) and tS[(1, 1, 1)] == [(0,)])
tSA = table([S, Aa(1)])
check("joint (S, A_1), independent w's: only e = (1,1,1)", all(tSA[e] == [] for e in ES if e != (1, 1, 1)), str(tSA[(1, 1, 1)]))
tHA = table([Hon, Aa(1)])
check("joint (H_on, A_1), independent w's: only e = (1,1,1)", all(tHA[e] == [] for e in ES if e != (1, 1, 1)), str(tHA[(1, 1, 1)]))
tRA = table([RLk, Aa(1)])
check("joint (R_L, A_1), independent w's: some taste for every e", all(tRA[e] for e in ES), str({e: tRA[e] for e in ES[:1]}))
tRt = table([RTk])
check("Rt alone has tastes for every e (like R_L)", all(tRt[e] for e in ES), str(tRt[ES[0]]))
print(f"\nTOTAL: PASS={P} FAIL={F}   [{time.time() - t0:.1f}s]")
