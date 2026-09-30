"""Test A, second protocol (added after the wedge run showed a far-end mismatch; see report).
Segment of N sites of the infinite half-filled chain (a 'causal diamond' with a horizon at each
end).  Exact fact (Slepian 1978, DPSS): C commutes with the tridiagonal matrix T with
T_{j,j+1} = j (N-j)/2 and zero diagonal, so C = f(T) exactly.  Framework clock: site rates
w_j = (j-1/2)(N+1/2-j)/N (zero of rate at the two cuts, positive at every site),
hopping sqrt(w_j w_{j+1}).  Test: C vs expit(-beta H_w); prediction beta = pi (a = 1).
"""
import numpy as np
from scipy.special import expit
from scipy.optimize import minimize_scalar

def vacuum_C(N):
    i = np.arange(1, N + 1)
    d = i[:, None] - i[None, :]
    with np.errstate(divide="ignore", invalid="ignore"):
        C = np.sin(np.pi * d / 2.0) / (np.pi * d)
    C[d == 0] = 0.5
    return C

def tri(t):
    N = len(t) + 1
    H = np.zeros((N, N)); i = np.arange(N - 1)
    H[i, i + 1] = -t; H[i + 1, i] = -t
    return H

def fit(C, H, lo, hi):
    ev, V = np.linalg.eigh(H)
    def r(b):
        F = (V * expit(-b * ev)) @ V.T
        return np.linalg.norm(C - F) / np.linalg.norm(C - 0.5 * np.eye(len(C)))
    bs = np.linspace(lo, hi, 80)
    rs = [r(b) for b in bs]; k = int(np.argmin(rs))
    res = minimize_scalar(r, bounds=(bs[max(k-1,0)], bs[min(k+1,79)]), method="bounded",
                          options={"xatol": 1e-9})
    return res.x, res.fun

def onsite_H(N, a):
    H = tri(-np.ones(N - 1) * -1.0)  # hopping -1 -> matrix entries -1
    H = tri(np.ones(N - 1))
    H[np.arange(N), np.arange(N)] = a * np.arange(1, N + 1)
    return H

if __name__ == "__main__":
    import json
    out = []
    print("Diamond test: segment of N sites, framework clock w_j=(j-1/2)(N+1/2-j)/N, prediction beta=pi")
    print("  N   | exact-T: ||[C,T]||/(||C-.5|| ||T||) | linear clock: beta/pi  resid | double zero: best beta/pi resid | on-site: resid")
    for N in (100, 200, 400, 800):
        C = vacuum_C(N)
        j = np.arange(1, N + 1, dtype=float)
        Tex = tri(np.arange(1, N) * (N - np.arange(1, N)) / 2.0)
        cn = np.linalg.norm(C @ Tex - Tex @ C) / (np.linalg.norm(C - 0.5*np.eye(N)) * np.linalg.norm(Tex))
        w = (j - 0.5) * (N + 0.5 - j) / N
        H = tri(np.sqrt(w[:-1] * w[1:]))
        b, r = fit(C, H, 1.5, 6.0)
        # double zero, same centre value
        w2 = (N / 4.0) * (4 * (j - 0.5) * (N + 0.5 - j) / N**2) ** 2
        H2 = tri(np.sqrt(w2[:-1] * w2[1:]))
        # scan wide beta range on log scale
        ev, V = np.linalg.eigh(H2)
        best = (1e9, None)
        for bb in np.geomspace(0.05, 200, 200):
            F = (V * expit(-bb * ev)) @ V.T
            rr = np.linalg.norm(C - F) / np.linalg.norm(C - 0.5 * np.eye(N))
            if rr < best[0]: best = (rr, bb)
        # on-site: slope 1 potential ramp (lattice Rindler with potential instead of hopping)
        H3 = onsite_H(N, 1.0)
        ev3, V3 = np.linalg.eigh(H3)
        best3 = (1e9, None)
        for bb in np.geomspace(0.02, 50, 200):
            F = (V3 * expit(-bb * ev3)) @ V3.T
            rr = np.linalg.norm(C - F) / np.linalg.norm(C - 0.5 * np.eye(N))
            if rr < best3[0]: best3 = (rr, bb)
        print(f" {N:4d} |  {cn:10.2e}  | {b/np.pi:8.4f} {r:9.5f} | {best[1]/np.pi:8.3f} {best[0]:8.4f} | {best3[0]:8.4f}")
        out.append(dict(N=N, comm_exact_T=cn, beta_over_pi=b/np.pi, resid_linear=r,
                        double_best_beta_over_pi=best[1]/np.pi, resid_double=best[0], resid_onsite=best3[0]))
    json.dump(out, open("A3_results.json", "w"), indent=1)
