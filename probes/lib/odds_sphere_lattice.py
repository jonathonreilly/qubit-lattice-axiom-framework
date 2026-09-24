"""Possibility's odds on the sphere menu (block 42's reading; block 103, PR #8919): the self-consistent map
pi_x(s) ~ prod_{y~x} (K1 pi_y)(s) at every unformed site of an L^3 box, records held with their own contents,
the boundary layer held at the uniform ordered sea (lean along z). Odds are stored on a product grid of the sphere
(Gauss-Legendre in t = s.z times uniform azimuth); K1 is the grid matrix of exp(beta s.b)/Z; red-black relaxation in
the log domain (omega ~ 1.6-1.7). Floating point; a research library, not a proof.

    python3 odds_sphere_lattice.py BETA L "x,y,z:sx,sy,sz;x,y,z:sx,sy,sz" [omega]

prints, per site on the axes and diagonal through the box centre, the sideways lean <s.e_x>, the lean <s.z>, and the
site's log normalizer log <prod_y g_y> (the content-averaged weight of the site, block 42 T4(b)), each against the
record-free sea. Import and call solve() for other measurements."""
import sys
import time
import numpy as np
from numpy.polynomial.legendre import leggauss


def sphere_grid(nt=20, nph=24):
    tq, wt = leggauss(nt)
    ph = 2 * np.pi * np.arange(nph) / nph
    T, PH = np.meshgrid(tq, ph, indexing="ij")
    T, PH = T.ravel(), PH.ravel()
    W = np.repeat(wt / 2, nph) / nph
    R = np.sqrt(1 - T * T)
    S = np.stack([R * np.cos(PH), R * np.sin(PH), T], axis=1)
    return S, W


def ordered_sea(beta, S, W):
    Z = np.sinh(beta) / beta
    K = np.exp(beta * S @ S.T) * W[None, :] / Z
    F = 1 + 0.4 * S[:, 2]
    for _ in range(20000):
        Fn = (K @ F) ** 6
        Fn /= W @ Fn
        if np.abs(Fn - F).max() < 1e-14:
            F = Fn
            break
        F = Fn
    return K, F


def solve(beta, L, records, omega=1.6, tol=1e-11, maxit=6000, nt=20, nph=24, verbose=True):
    """records: dict {(x,y,z): unit content vector}. Returns dict with P (normalized odds, L^3 x npts), logN (site
    log normalizers), T (sideways lean <s.e_x>), M (<s.z>), MF (sea lean), logNF (sea log normalizer), S, W."""
    S, W = sphere_grid(nt, nph)
    Z = np.sinh(beta) / beta
    K, F = ordered_sea(beta, S, W)
    GF = K @ F
    logP = np.tile(np.log(F), (L, L, L, 1))
    held = np.zeros((L, L, L), bool)
    held[0, :, :] = held[-1, :, :] = held[:, 0, :] = held[:, -1, :] = held[:, :, 0] = held[:, :, -1] = True
    rec = np.zeros((L, L, L), bool)
    for p in records:
        rec[p] = True
    ii, jj, kk = np.indices((L, L, L))
    color = (ii + jj + kk) % 2
    upd = [(~held) & (~rec) & (color == q) for q in (0, 1)]
    t0 = time.time()

    def factors(logP):
        Pn = np.exp(logP)
        Pn /= (Pn * W).sum(-1, keepdims=True)
        g = Pn @ K.T
        g[held] = GF
        for p, s0 in records.items():
            g[p] = np.exp(beta * S @ np.asarray(s0, float)) / Z
        lg = np.log(g)
        acc = np.zeros_like(lg)
        acc[1:] += lg[:-1]; acc[:-1] += lg[1:]
        acc[:, 1:] += lg[:, :-1]; acc[:, :-1] += lg[:, 1:]
        acc[:, :, 1:] += lg[:, :, :-1]; acc[:, :, :-1] += lg[:, :, 1:]
        return acc

    for it in range(maxit):
        delta = 0.0
        for q in (0, 1):
            acc = factors(logP)
            m = upd[q]
            new = acc[m]
            mx = new.max(-1, keepdims=True)
            new = new - (np.log((np.exp(new - mx) * W).sum(-1, keepdims=True)) + mx)
            old = logP[m]
            logP[m] = (1 - omega) * old + omega * new
            delta = max(delta, np.abs(new - old).max())
        if delta < tol:
            break
    acc = factors(logP)
    mx = acc.max(-1, keepdims=True)
    logN = (np.log((np.exp(acc - mx) * W).sum(-1, keepdims=True)) + mx)[..., 0]
    Pn = np.exp(logP)
    Pn /= (Pn * W).sum(-1, keepdims=True)
    logNF = np.log(W @ (GF ** 6))
    if verbose:
        print(f"beta={beta} L={L} records={len(records)}: {it + 1} sweeps, residual {delta:.1e}, {time.time() - t0:.0f} s")
    return dict(P=Pn, logN=logN, T=Pn @ (W * S[:, 0]), M=Pn @ (W * S[:, 2]), MF=W @ (F * S[:, 2]), logNF=logNF, S=S, W=W)


if __name__ == "__main__":
    beta, L = float(sys.argv[1]), int(sys.argv[2])
    recs = {}
    for item in sys.argv[3].split(";"):
        a, b = item.split(":")
        p = tuple(int(v) for v in a.split(","))
        s = np.array([float(v) for v in b.split(",")])
        recs[p] = s / np.linalg.norm(s)
    omega = float(sys.argv[4]) if len(sys.argv) > 4 else 1.6
    out = solve(beta, L, recs, omega)
    c = L // 2
    for name, pts in (("axis x", [(c + r, c, c) for r in range(-c + 1, c)]), ("axis y", [(c, c + r, c) for r in range(-c + 1, c)])):
        print(name)
        for p in pts:
            if p in recs:
                print(f"  {p}: record")
                continue
            print(f"  {p}: T={out['T'][p]:+.6e} dM={out['M'][p] - out['MF']:+.6e} dlogN={out['logN'][p] - out['logNF']:+.6e}")
    print("SUMMARY: odds solved; see the site lines")
