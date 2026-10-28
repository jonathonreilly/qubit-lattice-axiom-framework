#!/usr/bin/env python3
"""Check c18c (session 7, [R56-fix] binding): Lemma A1-NA(1) tested IN its own regime.
Pre-registered criteria: checks/c18c_criteria.md (written before this script). SU(2), S4' (diagonal order pairing),
L = 3; d = 2 coarse side 5 and d = 3 coarse side 3; small phi; near-extremal long-wavelength field; principal-branch logs;
HS norms. R_ab is computed independently from the abelian linearised S4' (linear sums of link logs along the same paths).
Finite instances only.
"""
import os
os.environ.update(OMP_NUM_THREADS="1", OPENBLAS_NUM_THREADS="1", MKL_NUM_THREADS="1")
import time, itertools as it, numpy as np
AUDIT_TIMEOUT_SEC = 600
T0 = time.time(); NP = NF = 0
def check(n, ok, s=""):
    global NP, NF
    NP += bool(ok); NF += not ok; print(("PASS " if ok else "FAIL ") + n + (" | " + s if s else ""))
Lb = 3
dag = lambda M: np.conj(np.swapaxes(M, -1, -2))
GEN = np.array([[[0, 1], [1, 0]], [[0, -1j], [1j, 0]], [[1, 0], [0, -1]]], complex) / 2
def su2_exp(a):
    H = np.einsum("...a,aij->...ij", a, GEN); w, V = np.linalg.eigh(H); return V @ (np.exp(1j * w)[..., None] * dag(V))
def plog(Z):  # principal log of unitary matrices: eigen-angles in (-pi, pi]
    w, V = np.linalg.eig(Z); ang = np.angle(w); ang = np.where(ang <= -np.pi, ang + 2 * np.pi, ang)
    return V @ ((1j * ang)[..., None] * np.linalg.inv(V))
hs2 = lambda X: np.real(np.einsum("...ij,...ij->...", np.conj(X), X))
def run(d, Tc, seeds):
    S = Lb * Tc; E = np.eye(d, dtype=int); ORD = list(it.permutations(range(d))); idx = lambda x: tuple(np.asarray(x) % S)
    def path_links(a, b, order):
        cur = np.array(a); out = []
        for m in order:
            while cur[m] != b[m]:
                sg = 1 if b[m] > cur[m] else -1
                out.append((idx(cur), m, 1) if sg > 0 else (idx(cur - E[m]), m, -1)); cur[m] += sg
        return out
    straight = lambda y, m: [(idx(np.array(y) + j * E[m]), m, 1) for j in range(Lb)]
    KEYS = [(X, m) for X in it.product(range(Tc), repeat=d) for m in range(d)]; GEOM = {}
    for (X, m) in KEYS:
        cX = np.array(X) * Lb + (Lb - 1) // 2; cY = cX + Lb * E[m]; Zs = []
        for o in ORD:
            for off in it.product(range(Lb), repeat=d):
                y = np.array(X) * Lb + np.array(off)
                Zs.append((path_links(cX, y, o) + straight(y, m), path_links(cY, y + Lb * E[m], o)))
        GEOM[(X, m)] = (straight(cX, m), Zs)
    NL = d * S ** d; lid = lambda x, m: int(np.ravel_multi_index((m,) + tuple(x), (d,) + (S,) * d))
    def enc(links, pad):
        out = [lid(x, m) + (0 if s > 0 else NL) for (x, m, s) in links]; return out + [2 * NL] * (pad - len(out))
    PF = max(len(f) for k in KEYS for f, b in GEOM[k][1]); PB = max(len(b) for k in KEYS for f, b in GEOM[k][1])
    IF = np.array([enc(f, PF) for k in KEYS for f, b in GEOM[k][1]]); IB = np.array([enc(b, PB) for k in KEYS for f, b in GEOM[k][1]])
    IS = np.array([enc(GEOM[k][0], Lb) for k in KEYS]); NZ = len(GEOM[KEYS[0]][1])
    def bprod(bank, I):
        P = np.broadcast_to(np.eye(2, dtype=complex), (I.shape[0], 2, 2)).copy()
        for j in range(I.shape[1]): P = P @ bank[I[:, j]]
        return P
    def coarse(U):
        flat = U.reshape(NL, 2, 2); bank = np.concatenate([flat, dag(flat), np.eye(2, dtype=complex)[None]], axis=0)
        Sm = bprod(bank, IS); Z = np.repeat(dag(Sm), NZ, axis=0) @ bprod(bank, IF) @ dag(bprod(bank, IB))
        Xb = plog(Z).reshape(len(KEYS), NZ, 2, 2).mean(axis=1); Xb = (Xb - dag(Xb)) / 2
        Xb = Xb - (np.trace(Xb, axis1=-2, axis2=-1) / 2)[:, None, None] * np.eye(2)
        w, Vv = np.linalg.eigh(-1j * Xb); Ex = Vv @ (np.exp(1j * w)[..., None] * dag(Vv))
        V = np.empty((d,) + (Tc,) * d + (2, 2), complex)
        for i, (X, m) in enumerate(KEYS): V[(m,) + X] = Sm[i] @ Ex[i]
        return V
    def coarse_ab(a):  # abelian linearised S4' on Lie-algebra components: A'(X,m) = avg (sum fwd - sum back)
        flat = a.reshape(NL, 3); bank = np.concatenate([flat, -flat, np.zeros((1, 3))], axis=0)
        lin = bank[IF].sum(axis=1) - bank[IB].sum(axis=1)
        Ap = lin.reshape(len(KEYS), NZ, 3).mean(axis=1); A = np.empty((d,) + (Tc,) * d + (3,))
        for i, (X, m) in enumerate(KEYS): A[(m,) + X] = Ap[i]
        return A
    def plaqs(U):
        out = []
        for mu in range(d):
            for nu in range(mu + 1, d):
                out.append(U[mu] @ np.roll(U[nu], -1, axis=mu) @ dag(np.roll(U[mu], -1, axis=nu)) @ dag(U[nu]))
        return np.stack(out)
    def dflux(A):
        out = []
        for mu in range(d):
            for nu in range(mu + 1, d):
                out.append(A[mu] + np.roll(A[nu], -1, axis=mu) - np.roll(A[mu], -1, axis=nu) - A[nu])
        return np.stack(out)
    xs = np.indices((S,) * d); k = 2 * np.pi / S
    for seed in seeds:
        r = np.random.default_rng(seed); H = np.zeros((d,) + (S,) * d + (3,))
        H[0][..., 2] = np.cos(k * xs[1]); H[1][..., 2] = np.cos(k * xs[0] + 0.3)
        for mu in range(d):  # smooth non-abelian part, relative size 0.3, lowest modes
            for nu in range(d):
                if nu == mu: continue
                c = r.normal(size=2); ph = r.uniform(0, 2 * np.pi)
                H[mu][..., 0] += 0.3 * c[0] * np.cos(k * xs[nu] + ph); H[mu][..., 1] += 0.3 * c[1] * np.sin(k * xs[nu] + ph)
        Fa = dflux(H); Fc = dflux(coarse_ab(H)); R_ab = np.sum(Fc ** 2) / np.sum(Fa ** 2); Lp = Lb ** (4 - d)
        print(f"d={d} coarse side {Tc} seed {seed}: R_ab={R_ab:.6f}  L^(4-d)={Lp}  R_ab/L^(4-d)={R_ab / Lp:.4f}")
        check(f"(a) d={d} seed {seed} near-extremal R_ab/L^(4-d) >= 0.5", R_ab / Lp >= 0.5, f"{R_ab / Lp:.4f}")
        check(f"(b) d={d} seed {seed} A1 on the field R_ab <= L^(4-d)", R_ab <= Lp * (1 + 1e-9), f"{R_ab:.6f}")
        rows = []; inreg = True
        for t in (0.0025, 0.005, 0.01, 0.02):
            U = su2_exp(t * H); Xf = plog(plaqs(U)); V = coarse(U); Xc = plog(plaqs(V))
            phi = float(np.sqrt(hs2(Xf).max())); phic = float(np.sqrt(hs2(Xc).max())); inreg &= phi <= 0.25 and phic <= 0.25
            Rl = hs2(Xc).sum() / hs2(Xf).sum()
            sU = 1 - np.real(np.trace(plaqs(U), axis1=-2, axis2=-1)) / 2; sV = 1 - np.real(np.trace(plaqs(V), axis1=-2, axis2=-1)) / 2
            Rs = sV.sum() / sU.sum(); rows.append((t, phi, phic, Rl, Rs, abs(Rl - R_ab) / phi))
            print(f"  t={t:<7g} phi={phi:.3e} coarse={phic:.3e} R_log={Rl:.8f} R_s={Rs:.8f} D={abs(Rl - R_ab) / phi:.4e} |R_s-R_log|={abs(Rs - Rl):.2e}")
        Ds = [x[5] for x in rows]; okc = all(Ds[i] <= 1.5 * Ds[i + 1] + 1e-9 for i in range(len(Ds) - 1))
        check(f"(c) d={d} seed {seed} D(t) does not grow as t decreases", okc, " ".join(f"{x:.3e}" for x in Ds))
        check(f"(d) d={d} seed {seed} in regime (phi, coarse <= 0.25; side >= 3)", inreg and Tc >= 3)
        Crep = max(max(x[3] / Lp - 1, x[4] / Lp - 1, 0) / x[1] for x in rows)
        print(f"  (e) reported C_rep = {Crep:.4f}")
run(2, 5, (11, 12))
run(3, 3, (13, 14))
print(f"runtime {time.time() - T0:.1f} s")
print(f"TOTAL: PASS={NP} FAIL={NF}")
