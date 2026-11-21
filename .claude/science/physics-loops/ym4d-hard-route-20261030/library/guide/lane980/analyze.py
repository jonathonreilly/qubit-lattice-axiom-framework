"""analyze.py -- FINISH row 980 (gap-pinsheet-guide). GUIDE only.
Reads pinsheet output files (one or more chains of one side and mode), drops nothing further
(thermalisation is already excluded by pinsheet), and reports for each column the mean, the
16-block standard error, and the integrated autocorrelation time (Sokal window, c = 6).
Usage: python3 -I analyze.py mode file1  (mode 1 = P1 SU(2), 2 = P2 U(1), 3 = P3)
 [file2 ...]
Several files = independent chains: block errors are computed per chain (16 blocks each) and pooled.
"""
import sys
import gzip
import numpy as np

NB = 16


def tau_int(x, c=6.0):
    x = np.asarray(x, float) - np.mean(x)
    n = len(x)
    f = np.fft.rfft(x, 2 * n)
    ac = np.fft.irfft(f * np.conj(f))[:n] / np.arange(n, 0, -1)
    ac /= ac[0]
    t = 0.5
    for w in range(1, n):
        t += ac[w]
        if w >= c * t:
            break
    return t


def blocks(x, nb=NB):
    n = len(x) // nb * nb
    return np.asarray(x[:n], float).reshape(nb, -1).mean(1)


def header(f):
    return (gzip.open(f, 'rt') if f.endswith('.gz') else open(f)).readline()


def main():
    mode = int(sys.argv[1])
    files = sys.argv[2:]
    names = {1: ["R", "Gp1", "tau", "a0sq"], 2: ["R", "Gp1", "tau", "c0sq"], 3: ["R0", "q0", "R4", "G0p1", "tau"]}[mode]
    ncomp = {1: 4, 2: 2, 3: 1}[mode]
    chains = [np.loadtxt(f, comments="#") for f in files]
    out = {}
    for j, nm in enumerate(names):
        bl = np.concatenate([blocks(c[:, 1 + j]) for c in chains])
        ti = np.mean([tau_int(c[:, 1 + j]) for c in chains])
        blen = min(len(c) for c in chains) // NB
        out[nm] = (bl.mean(), bl.std(ddof=1) / np.sqrt(len(bl)), ti, blen, bl)
        flag = "UNDER-SAMPLED" if ti > blen / 20 else "ok"
        print(f"{nm:5s} mean {bl.mean():.6f} err {bl.std(ddof=1) / np.sqrt(len(bl)):.6f} tau_int {ti:.1f} block_len {blen} {flag}")
    pl = np.concatenate([c[c[:, -1] >= 0, -1] for c in chains])
    print(f"plaq  mean {pl.mean():.6f} (n={len(pl)})")
    S = int(header(files[0]).split("S=")[1].split()[0])
    beta = float(header(files[0]).split("beta=")[1].split()[0])
    # stationarity: first half against second half of each chain, first observable
    for c in chains:
        h = len(c) // 16 * 8
        a, b = c[:h, 1], c[h:2 * h, 1]
        ea = a.reshape(8, -1).mean(1).std(ddof=1) / np.sqrt(8)
        eb = b.reshape(8, -1).mean(1).std(ddof=1) / np.sqrt(8)
        print(f"halves {names[0]}: {a.mean():.5f} +- {ea:.5f} | {b.mean():.5f} +- {eb:.5f}  diff/sigma {(b.mean() - a.mean()) / np.hypot(ea, eb):.2f}")
    # infrared bound of row 977 5.3 / 9.1(d) at the lowest momentum, per component
    Ep1 = 1 - np.cos(2 * np.pi / S)
    irb = 1 / (2 * beta * Ep1)
    if mode in (1, 2):
        g = out["Gp1"][0] / ncomp
        print(f"IRB  Ghat^e(p1) = {g:.5f} +- {out['Gp1'][1] / ncomp:.5f}  <=  1/(2 beta E(p1)) = {irb:.5f} : {'holds' if g <= irb else 'VIOLATED'}")
    if mode == 3:
        g = out["G0p1"][0]
        print(f"IRB  Ghat^0(p1) = {g:.5f} +- {out['G0p1'][1]:.5f}  <=  1/(2 beta E(p1)) = {irb:.5f} : {'holds' if g <= irb else 'VIOLATED'}")
    if mode in (1, 2):
        # second-moment correlation length from block means of R (= 4 Ghat(0)) and Gp1 (same normalisation)
        bR, bG = out["R"][4], out["Gp1"][4]
        ratio = bR.mean() / bG.mean()
        xi = np.sqrt(max(ratio - 1, 0)) / (2 * np.sin(np.pi / S))
        # jackknife over blocks
        n = len(bR)
        js = []
        for i in range(n):
            r = np.delete(bR, i).mean() / np.delete(bG, i).mean()
            js.append(np.sqrt(max(r - 1, 0)) / (2 * np.sin(np.pi / S)))
        js = np.array(js)
        print(f"xi2nd {xi:.4f} err {np.sqrt((n - 1) * np.var(js)):.4f}  (xi/S = {xi / S:.3f})")


if __name__ == "__main__":
    main()
