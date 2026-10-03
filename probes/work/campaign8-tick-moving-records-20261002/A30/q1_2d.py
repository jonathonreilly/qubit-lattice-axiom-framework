"""A30 q1_2d: 2D recorded disk with a capture channel on its gate-open surface (supplied toy).

Square lattice 128x128, periodic, hopping -t.  Recorded sites are removed (compression ->
walls).  Capture sites = unrecorded sites with >= 1 recorded neighbour (gated formation),
each with rate Gam (no-record branch: -i Gam/2).  Stationary scattering of a plane wave
e^{i k x} (k = 2 pi m / 128, periodic-compatible); the scattered part is absorbed by a
quadratic absorbing frame of width 36 (numerical device only).
  sigma_abs = sum_capture Gam |psi|^2 / (2 t sin k)        (2D cross-section = a length)
compared with the geometric width 2a (and the lattice disk's actual width).
Modes:  flat   -- full-height recorded column: checks the solver against the exact 1D law
        disk   -- disk radius a, Gam in {0.5, 2, 8}
        porous -- disk radius a + random shell of width d with density falling outward
Usage: python3 q1_2d.py MODE
"""
import signal
import sys
import numpy as np
import scipy.sparse as sp
from scipy.sparse.linalg import splu

signal.alarm(55)
t = 1.0
N = 128
W = 36          # absorbing frame width (validated: flat-face law to <=0.2% for k in [0.39, 2.75])
Wmax = 1.5      # frame strength (max -i Wmax/2 ... applied as -i w/2)
mode = sys.argv[1] if len(sys.argv) > 1 else 'disk'

X, Y = np.meshgrid(np.arange(N), np.arange(N), indexing='ij')
idx_all = X * N + Y


def frame_profile():
    dx = np.minimum(X, N - 1 - X)
    dy = np.minimum(Y, N - 1 - Y)
    d = np.minimum(dx, dy)                   # distance from the box edge
    w = np.where(d < W, Wmax * ((W - d) / W) ** 2, 0.0)
    return w


def frame_x_only():
    dx = np.minimum(X, N - 1 - X)
    return np.where(dx < W, Wmax * ((W - dx) / W) ** 2, 0.0)


def solve(rec, Gam, k, ky=0.0, frame=None):
    """rec: bool NxN recorded mask. Returns sigma_abs, sigma_frame (flux into frame / incident)."""
    if frame is None:
        frame = frame_profile()
    free = ~rec
    nfree = int(free.sum())
    lab = -np.ones((N, N), dtype=np.int64)
    lab[free] = np.arange(nfree)
    E = -2 * t * (np.cos(k) + np.cos(ky))
    phi = np.exp(1j * (k * X + ky * Y))
    # neighbours
    rows, cols = [], []
    nrec = np.zeros((N, N), dtype=np.int64)
    src = np.zeros((N, N), dtype=complex)
    for (ddx, ddy) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        Xn = (X + ddx) % N
        Yn = (Y + ddy) % N
        m = free & free[Xn, Yn]
        rows.append(lab[m]); cols.append(lab[Xn[m], Yn[m]])
        mr = free & rec[Xn, Yn]
        nrec += mr
        src[mr] += t * phi[Xn[mr], Yn[mr]]
    rows = np.concatenate(rows); cols = np.concatenate(cols)
    H = sp.csr_matrix((-t * np.ones(len(rows)), (rows, cols)), shape=(nfree, nfree))
    cap = free & (nrec > 0)
    gam = np.where(cap, Gam, 0.0)
    V = -0.5j * gam
    src = src + V * phi
    diag = E - V[free] + 0.5j * frame[free]
    A = sp.diags(diag) - H
    lu = splu(A.tocsc())
    s = lu.solve(src[free])
    psi = phi[free] + s
    P_abs = np.sum(gam[free] * np.abs(psi) ** 2)
    P_frame = np.sum(frame[free] * np.abs(s) ** 2)
    v = 2 * t * np.sin(k)
    return P_abs / v, P_frame / v, int(cap.sum())


if mode == 'flat':
    # recorded column at x = 80, full height (periodic in y). Incident from the left.
    rec = np.zeros((N, N), dtype=bool)
    rec[80:82, :] = True
    fr = frame_x_only()
    print("flat face (full-height recorded column, periodic y): absorption per row vs exact 1D law")
    for (k, ky, Gam) in [(np.pi / 2, 0.0, 2.0), (0.6, 0.0, 2.0), (0.4, 0.0, 2.0), (2.2, 0.0, 0.5), (2.75, 0.0, 2.0), (1.0, 2 * np.pi * 10 / N, 2.0)]:
        k = 2 * np.pi * round(k * N / (2 * np.pi)) / N
        sa, sf, nc = solve(rec, Gam, k, ky, frame=fr)
        V = -0.5j * Gam
        R = -(t + V * np.exp(-1j * k)) / (t + V * np.exp(1j * k))
        print(f"k={k:.4f} ky={ky:.3f} Gam={Gam}: A_row(solver)={sa/N:.6f}  A_1D(exact)={1-abs(R)**2:.6f}  "
              f"reflected (into frame)/row={sf/N:.6f}  sum={sa/N+sf/N:.6f}")

elif mode == 'disk':
    xc, yc = N // 2, N // 2
    dist = np.sqrt((X - xc) ** 2 + (Y - yc) ** 2)
    print("disk: sigma_abs / (2a); sigma_frame = scattered flux / incident flux density (both lengths)")
    alist = [int(sys.argv[2])] if len(sys.argv) > 2 else [4, 8, 16]
    for a in alist:
        rec = dist <= a
        width = int(rec[:, yc].sum())     # actual lattice width across
        for Gam in [0.5, 2.0, 8.0]:
            line = []
            for m in [8, 12, 16, 24, 32, 40, 48, 56]:
                k = 2 * np.pi * m / N
                sa, sf, nc = solve(rec, Gam, k)
                line.append(f"k={k:.2f}(ka={k*a:5.1f}): {sa/(2*a):.3f}/{sf/(2*a):.2f}")
            print(f"a={a:2d} (lattice width {width}, capture sites {nc}) Gam={Gam}:")
            print("   " + " | ".join(line))

elif mode == 'porous':
    xc, yc = N // 2, N // 2
    dist = np.sqrt((X - xc) ** 2 + (Y - yc) ** 2)
    rng = np.random.default_rng(20261003)
    print("porous shell: core radius a, shell a<r<=a+d with record density 1-(r-a)/(d+1); 3 seeds")
    a, d = 8, 8
    Glist = [float(sys.argv[2])] if len(sys.argv) > 2 else [2.0]
    for Gam in Glist:
        for m in [8, 12, 20, 32, 44, 56]:
            k = 2 * np.pi * m / N
            vals = []
            for seed in range(3):
                rng = np.random.default_rng(1000 + seed)
                p = np.clip(1 - (dist - a) / (d + 1), 0, 1)
                rec = (dist <= a) | ((dist > a) & (dist <= a + d) & (rng.random((N, N)) < p))
                sa, sf, nc = solve(rec, Gam, k)
                vals.append(sa)
            sm = np.mean(vals)
            # compare with smooth disk of radius a and radius a+d/2
            s1, _, _ = solve(dist <= a, Gam, k)
            s2, _, _ = solve(dist <= a + d / 2, Gam, k)
            s3, _, _ = solve(dist <= a + d, Gam, k)
            nrec_p = int(((dist <= a) | ((dist > a) & (dist <= a + d) & (np.random.default_rng(1000).random((N, N)) < np.clip(1 - (dist - a) / (d + 1), 0, 1)))).sum())
            print(f"Gam={Gam} k={k:.3f}: porous sigma={sm:6.2f} (seeds {vals[0]:.2f},{vals[1]:.2f},{vals[2]:.2f}; records {nrec_p})  "
                  f"smooth a={a}: {s1:6.2f}  a={a+d//2}: {s2:6.2f}  a={a+d}: {s3:6.2f} (records {int((dist <= a + d).sum())})  "
                  f"porous/2(a+d)={sm/(2*(a+d)):.3f}  smooth(a+d)/2(a+d)={s3/(2*(a+d)):.3f}")
