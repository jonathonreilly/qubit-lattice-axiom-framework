"""R2-5 check 4 (route P2): records that carry a direction label, 1+1, whole-law square symmetry.
Site values: 0 blank, or a record with label d in {U(+t), D(-t), R(+x), Lf(-x)}.
Hard rule (range 1, covariant under the square's rotations, invariant under t -> -t, which maps
U <-> D): a record with label d at site y requires a record with the SAME label at y + d.
Weight w per record.  Blank bottom row (low-record boundary), free top row, x periodic (L).
Exact transfer matrix over 5^L row states.  Reported: record density, formation and
un-formation per site per step split by label, and P(any U-record ever un-forms) (must be 0),
P(any record ever un-forms).
"""
import itertools
import numpy as np

B, U, D, R, LF = 0, 1, 2, 3, 4

def row_ok(row):
    L = len(row)
    for x, v in enumerate(row):
        if v == R and row[(x + 1) % L] != R: return False
        if v == LF and row[(x - 1) % L] != LF: return False
    return True

def run(L, w, T):
    rows = [r for r in itertools.product(range(5), repeat=L) if row_ok(r)]
    n = len(rows)
    A = np.array(rows)
    nrec = (A != B).sum(1)
    Rw = w ** nrec.astype(float)
    # vertical compatibility: U at (x,t) needs U at (x,t+1); D at (x,t+1) needs D at (x,t)
    Wm = np.ones((n, n))
    for i in range(n):
        a = A[i]
        bad = ((a[None, :] == U) & (A != U)).any(1) | ((A == D) & (a[None, :] != D)).any(1)
        Wm[i, bad] = 0.0
    blank = [i for i in range(n) if (A[i] == B).all()][0]
    def forward_backward(Wmat):
        alpha = []; a = np.zeros(n); a[blank] = 1.0; alpha.append(a); logs = 0.0
        for t in range(1, T + 1):
            a = (alpha[-1] @ Wmat) * Rw; s = a.sum(); logs += np.log(s); alpha.append(a / s)
        beta = [None] * (T + 1); beta[T] = np.ones(n)
        for t in range(T - 1, -1, -1):
            b = Wmat @ (Rw * beta[t + 1]); beta[t] = b / b.sum()
        return alpha, beta, logs
    alpha, beta, logZ = forward_backward(Wm)
    # un-formation by label: site record at t (label l) and blank at t+1
    unf = {l: np.zeros(T) for l in (U, D, R, LF)}; form = np.zeros(T); dens = np.zeros(T + 1)
    for t in range(T):
        P = alpha[t][:, None] * Wm * (Rw * beta[t + 1])[None, :]; P /= P.sum()
        for l in (U, D, R, LF):
            M = ((A[:, None, :] == l) & (A[None, :, :] == B)).sum(2)
            unf[l][t] = (P * M).sum() / L
        Mf = ((A[:, None, :] == B) & (A[None, :, :] != B)).sum(2)
        form[t] = (P * Mf).sum() / L
    for t in range(T + 1):
        p = alpha[t] * beta[t]; p /= p.sum(); dens[t] = p @ nrec / L
    # P(no un-formation of any record anywhere)
    noU = Wm * (~(((A[:, None, :] != B) & (A[None, :, :] == B)).any(2)))
    _, _, logZ2 = forward_backward(noU)
    return n, dens, form, unf, np.exp(logZ2 - logZ)

if __name__ == "__main__":
    T = 40
    for L in (3, 4):
        for w in (0.5, 1.0, 1.2, 3.0):
            n, dens, form, unf, pno = run(L, w, T)
            print(f"L={L} w={w}: row states={n}; density(t=1,5,T/2)={dens[1]:.3f},{dens[5]:.3f},{dens[T//2]:.3f}; "
                  f"formation/site/step(t=0,1,T/2)={form[0]:.3e},{form[1]:.3e},{form[T//2]:.3e}")
            print(f"      un-formation per site per step summed over t<T: U={unf[U].sum():.1e} D={unf[D].sum():.1e} "
                  f"R={unf[R].sum():.3e} L={unf[LF].sum():.3e};  P(no record ever un-forms)={pno:.3e}")
