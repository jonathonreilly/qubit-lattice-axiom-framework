"""Test A: pointer + free-fermion environment on an open chain. Sea vs beam; exact Holevo info of windows.
Usage: python3 beam_vs_sea.py MODE L NB G COUPLING  [T]
  MODE = sea | beam ; COUPLING = proj | sym ; NB = number of packets (beam) ; T = final time
Output: one JSON line to stdout and appended to results.jsonl
"""
import json
import sys
import time

import numpy as np
from gauss import holevo

MMAX = 8


def chain_h(L):
    h = np.zeros((L, L))
    for i in range(L - 1):
        h[i, i + 1] = h[i + 1, i] = -1.0
    return h


def evolve(h, j0, V, Phi0, T):
    hs = h.copy()
    hs[j0, j0] += V
    e, U = np.linalg.eigh(hs)
    Ut = (U * np.exp(-1j * e * T)[None, :]) @ U.conj().T
    return Ut @ Phi0


def packets(L, j0, NB, sigma=1.5, k0=np.pi / 2, spacing=10, first=12):
    x = np.arange(L)
    cols = []
    for j in range(NB):
        xc = j0 - first - spacing * j
        cols.append(np.exp(-(x - xc) ** 2 / (4 * sigma ** 2)) * np.exp(1j * k0 * x))
    Phi = np.array(cols).T
    Q, _ = np.linalg.qr(Phi)
    return Q


def corr(Phi):
    return Phi.conj() @ Phi.T  # D[x,y] = sum_k conj(phi_k(x)) phi_k(y)


def scan(Du, Dd, lo, hi, mmax=MMAX, eps=1e-7):
    """chi for all contiguous windows [i, i+m) inside [lo, hi)."""
    tab = {}
    for i in range(lo, hi):
        for m in range(1, mmax + 1):
            if i + m > hi:
                break
            a = Du[i:i + m, i:i + m]
            b = Dd[i:i + m, i:i + m]
            if np.linalg.norm(a - b) < eps:
                tab[(i, m)] = 0.0
            else:
                tab[(i, m)] = holevo(a, b)
    return tab


def disjoint_count(tab, thr):
    ws = [(i + m - 1, i, m) for (i, m), c in tab.items() if c >= thr]
    ws.sort()
    last = -10 ** 9
    chosen = []
    for end, i, m in ws:
        if i > last:
            chosen.append((i, m, tab[(i, m)]))
            last = end
    return chosen


def run(mode, L, NB, g, coup, T=None):
    h = chain_h(L)
    j0 = L // 2 if mode == "sea" else 110
    if coup == "proj":
        Vu, Vd = g, 0.0
    else:
        Vu, Vd = g, -g
    if mode == "sea":
        e, U = np.linalg.eigh(h)
        Phi0 = U[:, : L // 2]
        if T is None:
            T = L / 8
    else:
        Phi0 = packets(L, j0, NB)
        if T is None:
            T = 45.0
    Pu = evolve(h, j0, Vu, Phi0, T)
    Pd = evolve(h, j0, Vd, Phi0, T)
    Du, Dd = corr(Pu), corr(Pd)
    ov = float(np.prod(np.linalg.svd(Pu.conj().T @ Pd, compute_uv=False)))
    if mode == "sea":
        r = int(2 * T + 14)
        lo, hi = max(0, j0 - r), min(L, j0 + r)
    else:
        lo, hi = 1, L - 1
    t0 = time.time()
    tab = scan(Du, Dd, lo, hi)
    out = {
        "mode": mode, "L": L, "NB": NB, "g": g, "coup": coup, "T": T, "j0": j0,
        "overlap": ov, "secs": round(time.time() - t0, 1),
    }
    for thr in (0.9, 0.5, 0.2):
        ch = disjoint_count(tab, thr)
        out[f"R{thr}"] = len(ch)
        out[f"win{thr}"] = [(i - j0, m, round(c, 3)) for i, m, c in ch]
    contact = {k: v for k, v in tab.items() if k[0] <= j0 < k[0] + k[1]}
    away = {k: v for k, v in tab.items() if not (k[0] <= j0 < k[0] + k[1])}
    out["max_chi_contact"] = max(contact.values()) if contact else None
    out["max_chi_away"] = max(away.values()) if away else None
    # farthest window (centre distance from j0) with chi >= 0.2
    far = [abs(i + m / 2 - j0) for (i, m), c in tab.items() if c >= 0.2]
    out["far_reach_0.2"] = max(far) if far else 0
    return out


if __name__ == "__main__":
    mode = sys.argv[1]
    L = int(sys.argv[2])
    NB = int(sys.argv[3])
    g = float(sys.argv[4])
    coup = sys.argv[5]
    T = float(sys.argv[6]) if len(sys.argv) > 6 else None
    o = run(mode, L, NB, g, coup, T)
    line = json.dumps(o)
    print(line, flush=True)
    with open("results.jsonl", "a") as f:
        f.write(line + "\n")
