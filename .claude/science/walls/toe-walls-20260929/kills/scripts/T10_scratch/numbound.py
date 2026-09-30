"""Independent lower bound on the Holevo information of a window: classical mutual information between the
branch label s (equal priors) and the particle NUMBER in the window.  For a fermionic Gaussian state with
one-body matrix D_F the number is Poisson-binomial with parameters = eigenvalues of D_F.  Any measurement's
classical information <= chi (Holevo), so this is a rigorous LOWER bound on chi_F.  Independent of gauss.py."""
import numpy as np

def pb_pmf(nu):
    p = np.array([1.0])
    for v in nu:
        p = np.convolve(p, [1 - v, v])
    return p

def H(p):
    p = p[p > 1e-15]
    return float(-(p * np.log2(p)).sum())

def num_info(Da, Db):
    na = np.clip(np.linalg.eigvalsh((Da + Da.conj().T) / 2), 0, 1)
    nb = np.clip(np.linalg.eigvalsh((Db + Db.conj().T) / 2), 0, 1)
    pa, pb = pb_pmf(na), pb_pmf(nb)
    n = max(len(pa), len(pb))
    pa = np.pad(pa, (0, n - len(pa))); pb = np.pad(pb, (0, n - len(pb)))
    return H(0.5 * (pa + pb)) - 0.5 * (H(pa) + H(pb))

def scan_num(Du, Dd, lo, hi, mmax):
    tab = {}
    for i in range(lo, hi):
        for m in range(1, mmax + 1):
            if i + m > hi: break
            tab[(i, m)] = num_info(Du[i:i+m, i:i+m], Dd[i:i+m, i:i+m])
    return tab

def disjoint(tab, thr):
    ws = sorted((i + m - 1, i, m) for (i, m), c in tab.items() if c >= thr)
    last = -10**9; ch = []
    for end, i, m in ws:
        if i > last:
            ch.append((i, m, round(tab[(i, m)], 3))); last = end
    return ch
