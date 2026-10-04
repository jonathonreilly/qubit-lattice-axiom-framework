"""A53 lz24: two-pass Lanczos for the lowest flip-even (S even) state of a wrapped A51 rule on the 24-site tilted
cluster, checkpointed in batches (each run <= ~250 s of matvecs).  Pass 1: three-term recurrence (with local
re-orthogonalization) until the lowest Ritz value is converged (residual estimate beta_m |y_m| < tol); pass 2: the
same recurrence recomputed (deterministic; alphas checked) accumulating the Ritz vector.  Saves gs24_<tag>.npy.
Usage: lz24.py L KEY START   (START = rand | parton)"""
import sys, signal, time, os, numpy as np
from scipy.linalg import eigh_tridiagonal
signal.alarm(288)
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from a53lib import *
from a53lib import _rank
t0 = time.time(); L, key, start = int(sys.argv[1]), sys.argv[2], sys.argv[3]; BUDGET = 245.; TOL = 1e-6; MAXM = 300 if sys.argv[3] != 'parton' else 220
once = len(sys.argv) > 4 and sys.argv[4] == "once"
tag = f"L{L}_{key}_{start}" + ("_once" if once else ""); ck = f"lzck_{tag}.npz"
if os.path.exists(f"gs24_{tag}.npy"): print(f"[{tag}] already done"); sys.exit()
cl = Cluster(np.array([[2, 0, 2], [-2, 2, 2], [0, -2, 2]])); N = cl.N; X = [np.array(s) for s in cl.sites]; f = periodic_index(cl)
ks, J, c4 = load_rule(L, key); H = Ham(X, f, ks, J, c4, once=once); S = Sector(N, flip=True); mv = make_mv(H, S)
def v0():
    v = np.load("parton24.npy") if start == "parton" else np.random.default_rng(20261004).standard_normal(S.D)
    return v / np.linalg.norm(v)
if os.path.exists(ck):
    Z = np.load(ck); phase = str(Z["phase"]); j = int(Z["j"]); al = list(Z["al"]); be = list(Z["be"])
    vp, v = Z["vp"], Z["v"]; psi = Z["psi"] if phase == "p2" else None; y = Z["y"] if phase == "p2" else None; m = int(Z["m"])
    if phase == "done": print("already done"); sys.exit()
else:
    phase, j, al, be, vp, v, psi, y, m = "p1", 0, [], [0.], np.zeros(S.D), v0(), None, None, 0
print(f"[{tag}] resume phase {phase} at step {j}; setup {time.time()-t0:.1f}s", flush=True)
@nb.njit(cache=True)
def _papply(x, confs, perm, offset, idxlo, h, lomask, flip, top, full):
    y = np.empty_like(x)
    for k in range(len(confs)):
        c = confs[k]; c2 = 0
        for i in range(len(perm)): c2 |= ((c >> i) & 1) << perm[i]
        y[k] = x[_rank(c2, offset, idxlo, h, lomask, flip, top, full)]
    return y
PERMS = []
if start == "parton":                      # (2 + T + T^-1)/4 per unit translation: identity on T = +1, kills T = -1
    for a in range(3):
        pf = np.array([f(X[i] + np.eye(3, dtype=int)[a]) for i in range(N)], np.int64); pb = np.argsort(pf).astype(np.int64)
        PERMS.append((pf, pb))
def symm(w):
    for pf, pb in PERMS:
        w = (2 * w + _papply(w, S.confs, pf, S.offset, S.idxlo, S.h, S.lomask, S.flip, S.top, S.full)
             + _papply(w, S.confs, pb, S.offset, S.idxlo, S.h, S.lomask, S.flip, S.top, S.full)) / 4
    return w
def step(vp, v, bj):
    w = symm(mv(v)) - bj * vp; a = w @ v; w -= a * v
    w -= (w @ v) * v                                   # local re-orthogonalization (deterministic)
    b = np.linalg.norm(w); return a, b, w / b
while time.time() - t0 < BUDGET:
    if phase == "p1":
        a, b, w = step(vp, v, be[j]); al.append(a); be.append(b); vp, v = v, w; j += 1
        if j % 5 == 0 or j >= MAXM:
            th, U = eigh_tridiagonal(np.array(al), np.array(be[1:j]), select='i', select_range=(0, 1))
            res = be[j] * abs(U[-1, 0])
            print(f"  p1 step {j}: E0/N {th[0]/N:+.10f}  E1/N {th[1]/N:+.10f}  resid est {res:.2e}  [{time.time()-t0:.0f}s]", flush=True)
            if res < TOL or j >= MAXM:
                m = j; th, U = eigh_tridiagonal(np.array(al), np.array(be[1:m]), select='i', select_range=(0, 2)); y = U[:, 0]
                print(f"  pass 1 done: m = {m}, E0/N {th[0]/N:+.10f}, next Ritz {th[1]/N:+.10f} {th[2]/N:+.10f}; "
                      f"|<v0|Ritz0>|^2 = y_0^2 = {y[0]**2:.6e}, |<v0|Ritz1>|^2 = {U[0,1]**2:.3e}", flush=True)
                if start == "parton":
                    np.save(f"gs24_{tag}_summary.npy", np.r_[th / N, U[0, :] ** 2]); os.remove(ck) if os.path.exists(ck) else None
                    np.save(f"gs24_{tag}.npy", np.zeros(1)); print(f"DONE {tag} (pass 1 only)"); sys.exit()
                phase, j, vp, v, psi = "p2", 0, np.zeros(S.D), v0(), np.zeros(S.D)
    elif phase == "p2":
        psi += y[j] * v
        if j == m - 1:
            phase = "done"; break
        a, b, w = step(vp, v, be[j])
        assert abs(a - al[j]) < 1e-9 * max(1, abs(al[j])), f"p2 alpha mismatch at {j}: {a} vs {al[j]}"
        vp, v = v, w; j += 1
if phase == "done":
    psi /= np.linalg.norm(psi); Hp = mv(psi); E = psi @ Hp; r = np.linalg.norm(Hp - E * psi)
    np.save(f"gs24_{tag}.npy", psi); os.remove(ck) if os.path.exists(ck) else None
    print(f"DONE {tag}: m = {m}; <psi|H|psi>/N {E/N:+.10f}; residual |Hpsi - E psi| {r:.2e}  [{time.time()-t0:.0f}s]")
else:
    np.savez(ck, phase=phase, j=j, al=np.array(al), be=np.array(be), vp=vp, v=v, psi=psi if psi is not None else 0,
             y=y if y is not None else 0, m=m)
    print(f"  checkpoint: phase {phase} step {j}  [{time.time()-t0:.0f}s]")
