"""R2-1: d=2 version of check (N2) to larger range R: does the best odd finite-range charge that
equals k_1 on the soft ball keep a finite collision residual, or does it fall to zero with R?
(An exact invariant is excluded analytically; this tests whether APPROXIMATE ones improve with range.)
Also the same with the residual restricted to non-umklapp rows and to umklapp rows."""
import numpy as np
exec(open('r21_collision.py').read().split("S = sample(3000)")[0].replace("d = 3", "d = 2"))
S = sample(4000)
umv = np.array([um for _, um in S])
print("d=2, m=%.2f, %d shell samples, umklapp sampler fraction %.2f" % (m, len(S), umv.mean()))
ball = rng.uniform(-0.5, 0.5, (4000, d)); ball = ball[np.linalg.norm(ball, axis=1) < 0.5]
print("   R  #basis  local fit RMS   collision RMS (all)  (non-umklapp)  (umklapp)   ||tau||_RMS on BZ")
grid = rng.uniform(-np.pi, np.pi, (4000, d))
for R in [1, 2, 3, 4, 6, 8, 10]:
    ns = odd_basis(R)
    f = lambda k, ns=ns: np.sin(ns @ k)
    A = rows(S, f) / np.sqrt(len(S))
    Bm = np.sin(ball @ ns.T) / np.sqrt(len(ball))
    mu = 1e3
    M = np.vstack([A, mu * Bm]); y = np.concatenate([np.zeros(len(A)), mu * ball[:, 0] / np.sqrt(len(ball))])
    c, *_ = np.linalg.lstsq(M, y, rcond=None)
    loc = np.sqrt(np.mean((np.sin(ball @ ns.T) @ c - ball[:, 0]) ** 2))
    rr = rows(S, f) @ c
    tn = np.sqrt(np.mean((np.sin(grid @ ns.T) @ c) ** 2))
    print("  %2d  %5d   %.3e       %.4f              %.4f         %.4f      %.3f" % (R, len(ns), loc, np.sqrt(np.mean(rr ** 2)),
          np.sqrt(np.mean(rr[~umv] ** 2)), np.sqrt(np.mean(rr[umv] ** 2)), tn))
