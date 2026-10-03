"""A44 vmc: variational Monte Carlo for Gutzwiller-projected parton states (supplied toys).
Usage: vmc.py CLUSTER NSWEEP STATE [STATE ...]
  CLUSTER = L (cube L^3, APBC fermions) or fcc16 (validation against exact enumeration)
  STATE   = sold:<theta_deg> (hop t=cos th, lam=sin th) | pi (KS pi-flux scalar hop)
Moves: single spin flips (determinant ratio, Sherman-Morrison) + flips of both spins of a random bond
(exchange or pair flip; rank-2 Woodbury).  The pair flip is needed: the soldered state conserves the
twisted magnetisation sum_x (-1)^(x1+x2) s^z_x, so single flips are never accepted (validation, fcc16).  Measurement every sweep: per-bond <s^a_x s^b_y> local estimators from one N^3 product;
inverse recomputed from scratch each sweep (drift reported).  Errors by binning (plateau)."""
import sys, time, signal, numpy as np
signal.alarm(int(sys.argv[4]) if len(sys.argv) > 4 and sys.argv[4].isdigit() else 280)
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from a44lib import *


def binerr(x):
    x = np.asarray(x); n = len(x); out = []
    B = 1
    while n // B >= 16:
        m = x[:(n // B) * B].reshape(-1, B).mean(1)
        out.append((B, m.std(ddof=1) / np.sqrt(len(m))))
        B *= 2
    return x.mean(), max(e for _, e in out), out


def vmc(cl, t, lam, kind, nsweep, ntherm, seed, tlimit):
    N = cl.N; rng = np.random.default_rng(seed)
    Phi, gap, lev = mf_orbitals(cl, t, lam, kind=kind)
    conserve = (kind == "pi") or abs(lam) < 1e-12
    rows0 = 2 * np.arange(N)
    for _ in range(200):
        s = rng.permutation(np.r_[np.zeros(N // 2, int), np.ones(N - N // 2, int)]) if conserve else rng.integers(0, 2, N)
        M = Phi[rows0 + s]
        if abs(np.linalg.slogdet(M)[0]) > 0 and np.linalg.cond(M) < 1e10:
            break
    Q = np.linalg.inv(M)
    bi, bj, ba = cl.bi, cl.bj, cl.ba
    eye = np.eye(N)
    acc = [0, 0, 0, 0]; samples = []; drift = 0.; t0 = time.time()
    for sw in range(ntherm + nsweep):
        for _ in range(N):
            if (not conserve) and rng.random() < 0.5:
                i = rng.integers(N); v = Phi[2 * i + 1 - s[i]]
                R = v @ Q[:, i]; acc[1] += 1
                if rng.random() < abs(R) ** 2:
                    u = v @ Q; u[i] -= 1.
                    Q -= np.outer(Q[:, i], u) / R
                    s[i] = 1 - s[i]; acc[0] += 1
            else:
                b = rng.integers(len(bi)); i, j = bi[b], bj[b]     # flip both spins of a bond:
                vi, vj = Phi[2 * i + 1 - s[i]], Phi[2 * j + 1 - s[j]]  # exchange if antiparallel, pair flip if parallel
                Qc = Q[:, [i, j]]
                Rm = np.array([[vi @ Qc[:, 0], vi @ Qc[:, 1]], [vj @ Qc[:, 0], vj @ Qc[:, 1]]])
                R = Rm[0, 0] * Rm[1, 1] - Rm[0, 1] * Rm[1, 0]; acc[3] += 1
                if rng.random() < abs(R) ** 2:
                    U = np.vstack([vi @ Q, vj @ Q]); U[0, i] -= 1.; U[1, j] -= 1.
                    Q -= Qc @ np.linalg.solve(Rm, U)
                    s[i], s[j] = 1 - s[i], 1 - s[j]; acc[2] += 1
        Qf = np.linalg.inv(Phi[rows0 + s])
        drift = max(drift, np.abs(Q - Qf).max() / np.abs(Qf).max()); Q = Qf
        if sw < ntherm:
            continue
        a = rows0 + 1 - s
        G = Phi[a] @ Q                                 # G[i, j] = phi(flip_i) . Q[:, j]
        R1 = np.diag(G).copy()
        R2 = R1[bi] * R1[bj] - G[bi, bj] * G[bj, bi]
        z = 1. - 2. * s
        c = lambda al, zz: np.ones_like(zz, dtype=complex) if al == 0 else (-1j * zz if al == 1 else zz.astype(complex))
        C = np.empty((3, 3, len(bi)), complex)
        for al in range(3):
            for be in range(3):
                if al < 2 and be < 2: r = R2
                elif al < 2: r = R1[bi]
                elif be < 2: r = R1[bj]
                else: r = 1.
                C[al, be] = c(al, z[bi]) * c(be, z[bj]) * r
        eJ = (C[0, 0] + C[1, 1] + C[2, 2]).mean()
        eK = C[ba, ba, np.arange(len(bi))].mean()
        bb = np.array([1, 2, 0])[ba]; cc = np.array([2, 0, 1])[ba]; ar = np.arange(len(bi))
        eD = (C[bb, cc, ar] - C[cc, bb, ar]).mean()
        mag = [(R1).mean(), (-1j * z * R1).mean(), z.mean()]
        # per-direction 3x3 correlation (bond-averaged) for diagnostics
        Cd = np.array([[C[al, be][ba == d].mean() for al in range(3) for be in range(3)] for d in range(3)])
        samples.append(np.r_[eJ, eK, eD, mag, Cd.ravel()])
        if time.time() - t0 > tlimit:
            break
    S = np.array(samples)
    return dict(S=S, gap=gap, drift=drift, acc=acc, nsw=len(samples), secs=time.time() - t0)


if __name__ == "__main__":
    cname, nsweep = sys.argv[1], int(sys.argv[2])
    states = sys.argv[3].split(",")
    cl = Cluster([[2, 2, 0], [2, 0, 2], [0, 2, 2]]) if cname == "fcc16" else cube(int(cname))
    budget = 270. / len(states)
    print(f"cluster {cname}: N={cl.N}, oriented bonds {len(cl.bonds)}; states {states}; nsweep {nsweep}; budget/state {budget:.0f}s", flush=True)
    for st in states:
        if st == "pi":
            t, lam, kind, lab = 1.0, 0.0, "pi", "KS pi-flux"
        else:
            th = np.radians(float(st.split(":")[1])); t, lam, kind = np.cos(th), np.sin(th), "sold"
            lab = f"th={float(st.split(':')[1]):.1f}deg (t={t:+.3f}, lam={lam:+.3f})"
        Phi, gap, lev = mf_orbitals(cl, t, lam, kind=kind)
        if gap < 1e-8:
            print(f"{lab}: open shell (gap {gap:.1e}), skipped", flush=True); continue
        r = vmc(cl, t, lam, kind, nsweep, ntherm=max(50, nsweep // 10), seed=4400 + len(st), tlimit=budget * 0.85)
        S = r["S"]; n = len(S)
        out = []
        for k, nm in enumerate(["e_J", "e_K", "e_D"]):
            m, e, tab = binerr(S[:, k].real)
            h1, h2 = S[: n // 2, k].real.mean(), S[n // 2:, k].real.mean()
            out.append(f"{nm} = {m:+.5f} +- {e:.5f} (halves {h1:+.5f}/{h2:+.5f}; |Im| {abs(S[:, k].imag.mean()):.1e})")
        magm = np.abs(S[:, 3:6].mean(0))
        Cd = S[:, 6:].real.mean(0).reshape(3, 3, 3)
        print(f"{lab}: MF gap {gap:.3f}; sweeps {n} in {r['secs']:.0f}s; acc flip {r['acc'][0]}/{r['acc'][1]} exch {r['acc'][2]}/{r['acc'][3]}; "
              f"inverse drift {r['drift']:.1e}", flush=True)
        for o in out:
            print("   " + o)
        print(f"   |<s^a>| site-avg = {np.round(magm, 4)}; diag corr per direction (xx,yy,zz): "
              + "; ".join(f"e{d}: {np.round([Cd[d, 0, 0], Cd[d, 1, 1], Cd[d, 2, 2]], 4)}" for d in range(3)), flush=True)
        np.save(f"vmc_{cname}_{st.replace(':', '')}.npy", S)
