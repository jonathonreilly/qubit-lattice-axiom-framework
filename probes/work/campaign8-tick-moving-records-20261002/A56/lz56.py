"""A56 lz56: EXACT S = 0 ground-state energy of the restricted rule on a 24-site open block (line3 = 2x2x6, L3 = three
cubes in an L), by two-pass Lanczos in the flip-even S^z = 0 sector, checkpointed (each call <= ~240 s of matvecs).
Start = cube product + 0.3 * random singlet (both exact S = 0; the random part is generic in every spatial sector),
so the Krylov space is S = 0 up to round-off.  Pass 1: three-term recurrence with local re-orthogonalization until
the residual estimate beta_m |y_m| < TOL; pass 2 recomputes (alphas checked) and accumulates the Ritz vector, then
reports the true residual, sum <s.s> (S check), the cube-product overlap and inter-cube bond correlations.
Usage: lz56.py KEY BLOCK"""
import sys, signal, time, os, numpy as np
from scipy.linalg import eigh_tridiagonal
signal.alarm(285)
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from a56lib import *
t0 = time.time(); key, name = sys.argv[1], sys.argv[2]; L = 6; BUDGET = 235.; TOL = 1e-7; MAXM = 400
tag = f"{key}_{name}"; ck = f"lzck_{tag}.npz"
if os.path.exists(f"gs_{tag}.npy"): print(f"[{tag}] already done"); sys.exit()
X, cid, pairs, fours = block_terms(name, L, key); n = len(X); ncube = n // 8
S = Sector(n, flip=True); H = TabHam(pairs, fours, n); mv = make_mv_tab(H, S)
gsd, wc, sing, Ec = cube_gs(L, key)
def v0():
    p = cube_product(S, ncube, gsd); r = random_singlet(S); v = p + 0.3 * r
    return v / np.linalg.norm(v)
if os.path.exists(ck):
    Z = np.load(ck); phase = str(Z["phase"]); j = int(Z["j"]); al = list(Z["al"]); be = list(Z["be"])
    vp, v = Z["vp"], Z["v"]; psi = Z["psi"] if phase == "p2" else None; y = Z["y"] if phase == "p2" else None; m = int(Z["m"])
else:
    phase, j, al, be, vp, v, psi, y, m = "p1", 0, [], [0.], np.zeros(S.D), v0(), None, None, 0
    print(f"[{tag}] start: <v0|H|v0> {v@mv(v):+.6f}; {ncube} E_cube {ncube*Ec:+.6f}", flush=True)
print(f"[{tag}] n={n} D={S.D} pairs {len(H.pm)} four-sets {len(H.fm)}; resume phase {phase} at step {j}; setup {time.time()-t0:.1f}s", flush=True)
def step(vp, v, bj):
    w = mv(v) - bj * vp; a = w @ v; w -= a * v
    w -= (w @ v) * v
    b = np.linalg.norm(w); return a, b, w / b
while time.time() - t0 < BUDGET:
    if phase == "p1":
        a, b, w = step(vp, v, be[j]); al.append(a); be.append(b); vp, v = v, w; j += 1
        if j % 5 == 0 or j >= MAXM:
            th, U = eigh_tridiagonal(np.array(al), np.array(be[1:j]), select='i', select_range=(0, 1))
            res = be[j] * abs(U[-1, 0])
            print(f"  p1 step {j}: E0 {th[0]:+.12f}  E1 {th[1]:+.12f}  resid est {res:.2e}  [{time.time()-t0:.0f}s]", flush=True)
            if res < TOL or j >= MAXM:
                m = j; th, U = eigh_tridiagonal(np.array(al), np.array(be[1:m]), select='i', select_range=(0, 2)); y = U[:, 0]
                print(f"  pass 1 done: m = {m}, E0 {th[0]:+.12f} (E0/N {th[0]/n:+.8f}), next Ritz {th[1]:+.8f} {th[2]:+.8f}; "
                      f"|<v0|Ritz0>|^2 {y[0]**2:.4f}", flush=True)
                np.save(f"p1_{tag}.npy", np.r_[th, m, res])
                if len(sys.argv) > 3 and sys.argv[3] == 'p1':
                    os.remove(ck) if os.path.exists(ck) else None; np.save(f"gs_{tag}.npy", np.zeros(1)); print(f"DONE {tag} (pass 1 only)"); sys.exit()
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
    C = paircorr(psi, S); p = cube_product(S, ncube, gsd); ov = (p @ psi) ** 2
    np.save(f"gs_{tag}.npy", psi); os.remove(ck) if os.path.exists(ck) else None
    print(f"DONE {tag}: m = {m}; E = <psi|H|psi> {E:+.12f} (E/N {E/n:+.8f}); residual |H psi - E psi| {r:.2e}; "
          f"sum<s.s> {C.sum():.1e}; |<cube product|psi>|^2 {ov:.4f}  [{time.time()-t0:.0f}s]")
    E2 = {}
    for (i, k), Jv in pairs.items():
        cc = tuple(sorted((cid[i], cid[k]))); E2[cc] = E2.get(cc, 0.) + Jv * C[i, k]
    print("  two-place energy by cube pair: " + ", ".join(f"{a}-{b}: {v:+.4f}" for (a, b), v in sorted(E2.items())))
    cl = {}
    for (i, k), Jv in pairs.items():
        if cid[i] != cid[k] and Jv > 0.3:
            c = tuple(sorted(abs(int(t)) for t in X[i] - X[k])); cc = tuple(sorted((cid[i], cid[k])))
            cl.setdefault((cc, c), []).append(C[i, k])
    print("  inter-cube bonds with J > 0.3, mean <s.s> [count]: " +
          "; ".join(f"{a}-{b} {''.join(map(str,c))}: {np.mean(v):+.3f} [{len(v)}]" for ((a, b), c), v in sorted(cl.items())))
else:
    np.savez(ck, phase=phase, j=j, al=np.array(al), be=np.array(be), vp=vp, v=v, psi=psi if psi is not None else 0,
             y=y if y is not None else 0, m=m)
    print(f"  checkpoint: phase {phase} step {j}  [{time.time()-t0:.0f}s]")
