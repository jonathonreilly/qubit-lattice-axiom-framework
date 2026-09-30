"""Test A: is the homogeneous lattice vacuum, restricted to the wedge behind a stopped
clock, thermal with respect to the framework's clocked walker H_w = Phi H Phi ?

Pre-registered in PREREG.md.  Model: half-filled tight-binding chain (hopping 1),
exact infinite-chain vacuum correlations, wedge = sites 1..M.
H_prof bond (j,j+1) = -sqrt(w_j w_{j+1})  (framework clock: hopping dressed by phi_x phi_y).
Thermal test: r(beta) = ||C - expit(-beta H)||_F / ||C - 1/2||_F on the window j <= J0.
"""
import numpy as np
from scipy.special import expit
from scipy.optimize import minimize_scalar

M = 1500
J0 = 100


def vacuum_C(M):
    i = np.arange(1, M + 1)
    d = i[:, None] - i[None, :]
    with np.errstate(divide="ignore", invalid="ignore"):
        C = np.sin(np.pi * d / 2.0) / (np.pi * d)
    C[d == 0] = 0.5
    return C


def hop_H(w):
    """w[0..M-1] are the rates at sites 1..M; hopping dressed by sqrt(w_j w_{j+1})."""
    t = np.sqrt(w[:-1] * w[1:])
    H = np.zeros((len(w), len(w)))
    idx = np.arange(len(w) - 1)
    H[idx, idx + 1] = -t
    H[idx + 1, idx] = -t
    return H


def onsite_H(a):
    H = hop_H(np.ones(M))
    H[np.arange(M), np.arange(M)] = a * np.arange(1, M + 1)
    return H


def resid(C, evals, evecs, beta, J):
    f = expit(-beta * evals)
    Vw = evecs[:J, :]
    F = (Vw * f) @ Vw.T
    Cw = C[:J, :J]
    return np.linalg.norm(Cw - F) / np.linalg.norm(Cw - 0.5 * np.eye(J))


def fit_beta(C, H, J, betas):
    ev, V = np.linalg.eigh(H)
    rs = [resid(C, ev, V, b, J) for b in betas]
    k = int(np.argmin(rs))
    lo = betas[max(k - 1, 0)]
    hi = betas[min(k + 1, len(betas) - 1)]
    res = minimize_scalar(lambda b: resid(C, ev, V, b, J), bounds=(lo, hi),
                          method="bounded", options={"xatol": 1e-6 * max(hi, 1)})
    return res.x, res.fun


def comm_norm(C, H, J):
    K = C @ H - H @ C
    return np.linalg.norm(K[:J, :J]) / (np.linalg.norm(C[:J, :J] - 0.5 * np.eye(J)) * np.linalg.norm(H[:J, :J]))


if __name__ == "__main__":
    C = vacuum_C(M)
    j = np.arange(1, M + 1, dtype=float)
    out = []
    print("Test A: kinematic KMS on the clocked walker (M=%d, window j<=%d)" % (M, J0))
    print("linear zero w_j = a j; predicted beta = pi/a (T = a/pi)\n")
    for a in (0.02, 0.05, 0.1):
        w = a * j
        H = hop_H(w)
        pred = np.pi / a
        betas = np.linspace(0.2 * pred, 3 * pred, 60)
        b, r = fit_beta(C, H, J0, betas)
        # window excluding first 4 sites
        ev, V = np.linalg.eigh(H)
        f = expit(-b * ev)
        Vw = V[4:J0, :]
        F = (Vw * f) @ Vw.T
        Cw = C[4:J0, 4:J0]
        r2 = np.linalg.norm(Cw - F) / np.linalg.norm(Cw - 0.5 * np.eye(J0 - 4))
        cn = comm_norm(C, H, J0)
        print(f"a={a:5.3f}  beta_fit={b:9.4f}  beta*a/pi={b*a/np.pi:7.4f}  resid[1..100]={r:7.4f}  resid[5..100]={r2:7.4f}  comm={cn:8.5f}")
        out.append(dict(profile="linear", a=a, beta=b, ratio=b * a / np.pi, resid=r, resid5=r2, comm=cn))

    print("\nControl C1: same slope entering as an on-site potential a j n_j")
    for a in (0.02, 0.05, 0.1):
        H = onsite_H(a)
        pred = np.pi / a
        betas = np.linspace(0.05 * pred, 5 * pred, 80)
        b, r = fit_beta(C, H, J0, betas)
        cn = comm_norm(C, H, J0)
        print(f"a={a:5.3f}  best beta*a/pi={b*a/np.pi:7.4f}  resid={r:7.4f}  comm={cn:8.5f}")
        out.append(dict(profile="onsite", a=a, beta=b, ratio=b * a / np.pi, resid=r, comm=cn))

    print("\nControl C2: double zero w_j = min((a j)^2, 1)  (stopped-ball exterior, p=2)")
    for a in (0.02, 0.05, 0.1):
        w = np.minimum((a * j) ** 2, 1.0)
        H = hop_H(w)
        # best single beta over a wide range
        betas = np.geomspace(0.05, 2000, 80)
        b, r = fit_beta(C, H, J0, betas)
        cn = comm_norm(C, H, J0)
        print(f"a={a:5.3f}  best beta={b:9.3f}  resid={r:7.4f}  comm={cn:8.5f}")
        out.append(dict(profile="double", a=a, beta=b, resid=r, comm=cn))

    # C2 variant: also test the commutator of the *linear* profile that saturates (plateau) as in a real field
    print("\nLinear zero with plateau w_j = min(a j, 1) (window inside the sloped part)")
    for a in (0.02, 0.05, 0.1):
        w = np.minimum(a * j, 1.0)
        H = hop_H(w)
        Jw = int(0.5 / a)  # window ends where the rate is 1/2
        pred = np.pi / a
        betas = np.linspace(0.2 * pred, 3 * pred, 60)
        b, r = fit_beta(C, H, max(Jw, 8), betas)
        print(f"a={a:5.3f}  window j<= {Jw:3d}  beta*a/pi={b*a/np.pi:7.4f}  resid={r:7.4f}")
        out.append(dict(profile="linear_plateau", a=a, window=Jw, ratio=b * a / np.pi, resid=r))
    import json
    json.dump(out, open("A_results.json", "w"), indent=1)
