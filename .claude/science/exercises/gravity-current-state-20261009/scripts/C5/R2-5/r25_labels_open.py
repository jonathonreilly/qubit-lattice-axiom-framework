"""R2-5 check 4b (route P2), blank spatial walls instead of a periodic ring.
Same law as r25_labels.py (covariant, t-reflection invariant, range 1). State = blank bottom row,
blank walls at x = -1 and x = L (records do not reach spatial infinity), free top.
Then horizontally-labelled records cannot exist, D records cannot exist, and U records never
un-form.  Columns decouple: P(first record in a column at t0) proportional to w^(T - t0 + 1).
Reported: exact P(no record ever un-forms) (must be 1), density profile, the arrow length
t50 (median formation time) against the prediction ln 2 / ln w for w > 1 (T -> infinity), and for
w < 1 the fraction of formation within T/2 (-> 0 as T grows: formation is pushed to the free end).
"""
import itertools, math
import numpy as np
from r25_labels import B, U, D, R, LF

def ok_open(row):
    L = len(row)
    for x, v in enumerate(row):
        if v == R and (x + 1 >= L or row[x + 1] != R): return False
        if v == LF and (x - 1 < 0 or row[x - 1] != LF): return False
    return True

def run(L, w, T):
    rows = [r for r in itertools.product(range(5), repeat=L) if ok_open(r)]
    A = np.array(rows); n = len(rows)
    nrec = (A != B).sum(1); Rw = w ** nrec.astype(float)
    Wm = np.ones((n, n))
    for i in range(n):
        a = A[i]
        bad = ((a[None, :] == U) & (A != U)).any(1) | ((A == D) & (a[None, :] != D)).any(1)
        Wm[i, bad] = 0.0
    blank = [i for i in range(n) if (A[i] == B).all()][0]
    unf = (((A[:, None, :] != B) & (A[None, :, :] == B)).any(2))
    def logZ(Wmat):
        a = np.zeros(n); a[blank] = 1.0; ls = 0.0; dens = []
        alphas = [a]
        for t in range(1, T + 1):
            a = (a @ Wmat) * Rw; s = a.sum(); ls += math.log(s); a = a / s; alphas.append(a)
        return ls, alphas
    l1, alphas = logZ(Wm); l2, _ = logZ(Wm * (~unf))
    # density via forward-backward
    beta = [None] * (T + 1); beta[T] = np.ones(n)
    for t in range(T - 1, -1, -1):
        b = Wm @ (Rw * beta[t + 1]); beta[t] = b / b.sum()
    dens = []
    for t in range(T + 1):
        p = alphas[t] * beta[t]; p /= p.sum(); dens.append(p @ nrec / L)
    return n, math.exp(l2 - l1), np.array(dens)

if __name__ == "__main__":
    for L in (3, 4):
        for w, T in ((1.05, 200), (1.2, 100), (3.0, 60), (0.9, 100), (0.9, 200)):
            n, pno, dens = run(L, w, T)
            # median formation time from the density (fraction of columns with a record by t)
            t50 = int(np.argmax(dens >= 0.5)) if dens.max() >= 0.5 else None
            pred = (math.log(2) / math.log(w)) if w > 1 else None
            print(f"L={L} w={w} T={T}: states={n}  P(no record ever un-forms)={pno:.12f}  density(t=1,T/4,T/2,T)="
                  f"{dens[1]:.4f},{dens[T//4]:.4f},{dens[T//2]:.4f},{dens[T]:.4f}  t50={t50} pred(T->inf) ln2/ln w={pred}")
