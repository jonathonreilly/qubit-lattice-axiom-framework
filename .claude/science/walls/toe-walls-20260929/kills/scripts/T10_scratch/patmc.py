"""Lower bound on Holevo chi of a window: classical mutual information between branch s (equal priors) and the full
site-occupation pattern of the window (a valid measurement).  Gaussian fermion state, kernel K=D^T: exact pattern
probability P(A)=|det(K - I_{A^c})|; exact sequential sampling from prefix determinants; Monte-Carlo estimate of
I = E_{s, n~p_s} log2 p_s(n)/pbar(n)."""
import numpy as np

def prefix_prob(K, n):
    k = len(n)
    M = K[:k, :k] - np.diag(1.0 - np.asarray(n, float))
    return abs(np.linalg.det(M))

def sample(K, rng):
    m = K.shape[0]; n = []; pprev = 1.0
    for i in range(m):
        p1 = prefix_prob(K, n + [1])
        p0 = prefix_prob(K, n + [0])
        s = p1 + p0
        b = 1 if rng.random() < p1 / s else 0
        n.append(b)
    return n

def logp(K, n):
    return np.log2(max(prefix_prob(K, n), 1e-300))

def mi_pattern(Du, Dd, nsamp, rng):
    Ku, Kd = Du.T, Dd.T
    tot = 0.0; tot2 = 0.0
    for K, Ko in ((Ku, Kd), (Kd, Ku)):
        vals = []
        for _ in range(nsamp):
            n = sample(K, rng)
            lp = logp(K, n); lo = logp(Ko, n)
            lbar = np.logaddexp2(lp, lo) - 1.0
            vals.append(lp - lbar)
        v = np.array(vals); tot += v.mean() / 2; tot2 += v.var() / (nsamp * 4)
    return tot, np.sqrt(tot2)
