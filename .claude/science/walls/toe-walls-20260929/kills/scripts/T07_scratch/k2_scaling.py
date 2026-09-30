"""K2: does the noise rate needed to fix a shifted start scale with packet width?  Single walker, ring L, H = sin k sigma_z.
Wave: coin (cos a, sin a), Gaussian amplitude width w.  Bell minimal rates + Metropolis noise gamma.
Wrong start: Born marginal P_0 shifted by 1.9 prob-widths (attacker's start 3).  Read at T = 8 w."""
import numpy as np, scipy.sparse as sp, sys, json
from scipy.integrate import solve_ivp
SZ = np.array([1.0, -1.0])

def setup(L, w, alpha, centre):
    H = np.zeros((2 * L, 2 * L), complex)
    for x in range(L):
        y = (x + 1) % L
        for c in range(2):
            H[2 * x + c, 2 * y + c] += SZ[c] / (2j); H[2 * y + c, 2 * x + c] += np.conj(SZ[c] / (2j))
    E, V = np.linalg.eigh(H)
    x = np.arange(L)
    d = (x - centre + L / 2) % L - L / 2
    g = np.exp(-d ** 2 / (2 * w ** 2))
    psi0 = (g[:, None] * np.array([np.cos(alpha), np.sin(alpha)])[None, :]).astype(complex).reshape(-1)
    psi0 /= np.linalg.norm(psi0)
    return E, V, psi0

def run(L, w, alpha, gamma, shift_pw=1.9, Tfac=8.0, rtol=1e-8):
    centre = L // 2
    E, V, psi0 = setup(L, w, alpha, centre)
    c0 = V.conj().T @ psi0
    wave = lambda t: ((V * np.exp(-1j * E * t)) @ c0).reshape(L, 2)
    def gen(t):
        psi = wave(t); P = (np.abs(psi) ** 2).sum(1)
        T = np.real((np.roll(psi, -1, axis=0).conj() * SZ[None, :] * psi).sum(1))   # flow x -> x+1
        Pinv = np.where(P > 1e-300, 1 / np.maximum(P, 1e-300), 0.0)
        rp = np.minimum(np.maximum(T, 0) * Pinv, 1e5); rm = np.minimum(np.maximum(-np.roll(T, 1), 0) * Pinv, 1e5)
        if gamma > 0:
            rp = rp + gamma * np.minimum(1, np.roll(P, -1) * Pinv); rm = rm + gamma * np.minimum(1, np.roll(P, 1) * Pinv)
        idx = np.arange(L)
        rows = np.concatenate([(idx + 1) % L, (idx - 1) % L, idx]); cols = np.concatenate([idx, idx, idx])
        vals = np.concatenate([rp, rm, -(rp + rm)])
        return P, sp.csc_matrix((vals, (rows, cols)), shape=(L, L))
    P0 = gen(0.0)[0]
    x = np.arange(L)
    # shifted start: interpolate P0 shifted by s = shift_pw * prob-width (prob-width = w/sqrt2) using fractional shift by linear interpolation
    s = shift_pw * w / np.sqrt(2)
    xs = (x - s)
    r0 = np.interp(xs, np.concatenate([x - L, x, x + L]), np.concatenate([P0, P0, P0])); r0 /= r0.sum()
    T = Tfac * w
    f = lambda t, y: gen(t)[1] @ y; jac = lambda t, y: gen(t)[1]
    sol = solve_ivp(f, (0, T), r0, method='Radau', jac=jac, t_eval=[0, T], rtol=rtol, atol=1e-14)
    assert sol.success
    rT = sol.y[:, -1]; PT = gen(T)[0]
    tv = lambda a, b: 0.5 * np.abs(a - b).sum()
    # branch weight: mass right of centre
    right = (x >= centre)
    return dict(L=L, w=w, gamma=gamma, T=T, TV0=tv(r0, P0), TVT=tv(rT, PT), ratio=tv(rT, PT) / tv(r0, P0),
                right_rec=float(rT[right].sum()), right_born=float(PT[right].sum()))

if __name__ == '__main__':
    alpha = 1.0     # cos^2 = 0.29 left..., asymmetric coin
    out = []
    for w in [1.5, 3.0, 6.0]:
        L = int(max(120, 40 * w + 2 * 8 * w * 2))
        for g in [0.0, 1.0, 3.0, 7.0, 10.0, 15.0, 30.0, 60.0, 120.0]:
            r = run(L, w, alpha, g); out.append(r)
            print(f"w={w:4.1f} L={L:4d} gamma={g:6.1f}  TV0={r['TV0']:.3f} TVT={r['TVT']:.4f} ratio={r['ratio']:.3f}  right: rec={r['right_rec']:.4f} born={r['right_born']:.4f}", flush=True)
    json.dump(out, open('k2_results.json', 'w'), indent=1)
