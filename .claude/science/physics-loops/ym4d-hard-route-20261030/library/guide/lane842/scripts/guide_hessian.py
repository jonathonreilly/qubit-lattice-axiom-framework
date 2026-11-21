# GUIDE only (row 842). Pass criteria written before the run:
# (1) D1 D0 = 0 for SU(2) (each colour) and U(1) on (Z/n)^2 x (Z/M)^2, periodic base.
# (2) SU(2): least eigenvalue of Delta_1 = D1^T D1 + D0 D0^T and of Delta_0 equals mu_n = (2 sin(pi/2n))^2.
# (3) U(1) at U*: gradient sum_p sin(phi*_p) D1[p,:] = 0; transverse Hessian D1^T C D1 restricted to
#     ker D0^T has >= 4 zero eigenvalues and least positive eigenvalue <= 4 sin^2(pi/M) + 1e-9.
import numpy as np, itertools, sys
def build(n, M, twisted, colour):
    sites = list(itertools.product(range(n), range(n), range(M), range(M)))
    idx = {s: i for i, s in enumerate(sites)}
    size = [n, n, M, M]
    def sh(s, mu): t = list(s); t[mu] = (t[mu] + 1) % size[mu]; return tuple(t)
    links = [(s, mu) for s in sites for mu in range(4)]
    lid = {l: i for i, l in enumerate(links)}
    def sign(s, mu):
        if not twisted: return 1.0
        if mu == 0 and s[0] == n - 1 and colour in (1, 2): return -1.0
        if mu == 1 and s[1] == n - 1 and colour in (0, 2): return -1.0
        return 1.0
    D0 = np.zeros((len(links), len(sites)))
    for (s, mu), i in lid.items():
        D0[i, idx[sh(s, mu)]] += 1.0; D0[i, idx[s]] -= sign(s, mu)
    plaqs = [(s, mu, nu) for s in sites for mu in range(4) for nu in range(mu + 1, 4)]
    D1 = np.zeros((len(plaqs), len(links)))
    for k, (s, mu, nu) in enumerate(plaqs):
        D1[k, lid[(s, mu)]] += sign(sh(s, mu), nu)
        D1[k, lid[(sh(s, mu), nu)]] += 1.0
        D1[k, lid[(sh(s, nu), mu)]] -= 1.0
        D1[k, lid[(s, nu)]] -= sign(sh(s, nu), mu)
    return D0, D1, plaqs
ok = True
for n, M in [(2, 4), (2, 6), (3, 4)]:
    mu_n = (2 * np.sin(np.pi / (2 * n))) ** 2
    for c in range(3):
        D0, D1, _ = build(n, M, True, c)
        e1 = np.linalg.eigvalsh(D1.T @ D1 + D0 @ D0.T).min(); e0 = np.linalg.eigvalsh(D0.T @ D0).min()
        z = np.abs(D1 @ D0).max()
        good = z < 1e-12 and abs(e1 - mu_n) < 1e-9 and abs(e0 - mu_n) < 1e-9
        ok &= good
        print(f"SU2 n={n} M={M} c={c}: |D1D0|={z:.1e} minDelta1={e1:.6f} minDelta0={e0:.6f} mu_n={mu_n:.6f} {'PASS' if good else 'FAIL'}")
for n, M in [(2, 8), (3, 6)]:
    D0, D1, plaqs = build(n, M, False, 0)
    phi = np.array([np.pi / n**2 if (mu, nu) == (0, 1) else 0.0 for (s, mu, nu) in plaqs])
    grad = np.abs(np.sin(phi) @ D1).max()
    H = D1.T @ np.diag(np.cos(phi)) @ D1
    u, sv, vt = np.linalg.svd(D0.T); rank = (sv > 1e-9).sum(); Q = vt[rank:].T  # basis of ker D0^T
    ev = np.linalg.eigvalsh(Q.T @ H @ Q)
    nz = (np.abs(ev) < 1e-9).sum(); pos = ev[ev > 1e-9].min(); bound = 4 * np.sin(np.pi / M) ** 2
    good = np.abs(D1 @ D0).max() < 1e-12 and grad < 1e-12 and nz >= 4 and pos <= bound + 1e-9
    ok &= good
    print(f"U1 n={n} M={M}: grad={grad:.1e} zero modes={nz} least positive={pos:.6f} 4sin^2(pi/M)={bound:.6f} {'PASS' if good else 'FAIL'}")
print("ALL PASS" if ok else "SOME FAIL")
