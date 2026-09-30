import numpy as np, glob, sys, json, re

def load(fn):
    P = []; W = []; hdr = ''
    for l in open(fn):
        if l.startswith('#'):
            if 'L=' in l: hdr = l.strip()
            continue
        t = l.split()
        if len(t) < 2 or not l.endswith('\n'): continue
        if len(t) > 2 and len(t) != 18: continue
        try: float(t[1])
        except: continue
        P.append(float(t[1]))
        if len(t) > 2:
            W.append([float(x) for x in t[2:18]])
        else:
            W.append(None)
    return np.array(P), W, hdr

def tau_int(x, c=5.0):
    x = np.asarray(x) - np.mean(x); n = len(x)
    f = np.fft.rfft(x, 2 * n); acf = np.fft.irfft(f * np.conj(f))[:n]; acf /= acf[0]
    tau = 0.5
    for w in range(1, n):
        tau = 0.5 + np.sum(acf[1:w + 1])
        if w >= c * tau: break
    return tau

def stat(x, nblock=None):
    x = np.asarray(x); n = len(x)
    t = tau_int(x)
    naive = np.std(x, ddof=1) / np.sqrt(n) * np.sqrt(2 * t)
    bl = max(int(np.ceil(4 * t)), 1)
    nb = n // bl
    if nb >= 8:
        bm = x[:nb * bl].reshape(nb, bl).mean(1)
        jk = np.sqrt((nb - 1) / nb * np.sum((np.array([np.mean(np.delete(bm, i)) for i in range(nb)]) - bm.mean()) ** 2))
    else:
        jk = naive
    return np.mean(x), max(naive, jk), t

def summarize(fn, ncut=0):
    P, W, hdr = load(fn)
    P = P[ncut:]
    m, e, t = stat(P)
    return m, e, t, len(P), hdr

if __name__ == '__main__':
    for fn in sys.argv[1:]:
        m, e, t, n, hdr = summarize(fn)
        print(f"{fn}: P={m:.6f} +/- {e:.6f} tau={t:.2f} n={n}  {hdr}")
