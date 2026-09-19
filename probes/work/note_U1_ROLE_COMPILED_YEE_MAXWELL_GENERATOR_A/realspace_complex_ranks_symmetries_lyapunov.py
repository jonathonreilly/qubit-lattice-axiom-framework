#!/usr/bin/env python3
"""Probe: U1_ROLE_COMPILED_YEE_MAXWELL_GENERATOR_AND_TIME_SELECTION_FORK_BOUNDED_THEOREM_NOTE_2026-09-03.

Falsifier checks in REAL SPACE, beyond the runner's single L=3 real-space block,
with machinery disjoint from the runner (own lattice builder from the note's
section 1 text; exact integer sparse products; exact ranks over GF(p);
real-space signed-permutation action of the cubic group; a real-space
Lyapunov solve for the Gaussian sampler; mpmath for the phase maps):

 R1  chain identities C d0 = 0, d2 C = 0 (exact integers) and physical
     nearest-neighbour locality of every d0, C, d2 entry, on cubic tori
     L = 2..8, 10 and anisotropic tori (2,3,4), (3,4,5), (2,5,7), (4,6,8).
 R2  exact ranks over GF(p), two primes: rank d0 = N-1, rank C = 2N-2,
     rank d2 = N-1, rank [C; d0^T] = 3N-3 (three harmonic one-forms, no other
     transverse zero mode = no doublers), and the missing-yz-face control
     rank 2(N - Ly Lz) + (Ly Lz - 1).
 R3  full real-space spectra: C^T C and the Yee generator i G against the
     multiset {0, |s|^2, |s|^2} resp. {+-|s| twice, 0 twice} per momentum.
 R4  all 48 signed permutations of the physical cube act on the complex; the
     24 proper ones (and the 24 improper, reported) must fix d0, C, d2.
 R5  energy and both Gauss rows under numerical evolution exp(tG) (expm_multiply).
 R6  Ornstein-Uhlenbeck sampler on the mean-zero transverse space H, real
     space: Lyapunov covariance against (1/kappa)(C^T C|_H)^{-1}; spectrum of
     kappa*Sigma against 1/|s|^2; harmonic zero modes and their removal.
 R7  unit speed with reciprocal coefficients; two-reflection block exactness;
     whole-zone gap between the matched spectral lift and the direct law.

Prints SUMMARY: lines; HIT: only when a falsifier of the note fires.
"""
import itertools
import math
import sys
import time

import numpy as np
import scipy.sparse as sps
import scipy.linalg as sla
from scipy.sparse.linalg import expm_multiply
import mpmath as mp

HITS = []


def hit(msg):
    HITS.append(msg)
    print("HIT: " + msg)


def summary(msg):
    print("SUMMARY: " + msg)


# ---------------------------------------------------------------------------
# lattice builder (section 1 of the note, written from the text)
# ---------------------------------------------------------------------------
def build_complex(Ls):
    """Physical torus of side 2*L_i per axis.  Role by parity pattern:
    vertex = all even, edge = one odd coordinate (axis = odd one), face = two
    odd (plane = odd pair), cube = all odd.  Returns index maps and sparse
    integer d0 (E x V), C (F x E), d2 (Q x F), plus position lists."""
    n = tuple(2 * L for L in Ls)
    pts = list(itertools.product(*(range(k) for k in n)))
    V, E, F, Q = [], [], [], []
    for p in pts:
        odd = tuple(i for i in range(3) if p[i] % 2 == 1)
        (V, E, F, Q)[len(odd)].append(p)
    vi = {p: t for t, p in enumerate(V)}
    ei = {p: t for t, p in enumerate(E)}
    fi = {p: t for t, p in enumerate(F)}

    def shift(p, axis, step):
        q = list(p)
        q[axis] = (q[axis] + step) % n[axis]
        return tuple(q)

    def mk(rows, cols, vals, shape):
        return sps.csr_matrix((np.array(vals, dtype=np.int64), (rows, cols)), shape=shape)

    r, c, v = [], [], []
    for p, t in ei.items():
        i = [a for a in range(3) if p[a] % 2 == 1][0]
        r += [t, t]
        c += [vi[shift(p, i, -1)], vi[shift(p, i, +1)]]
        v += [-1, +1]
    d0 = mk(r, c, v, (len(E), len(V)))
    r, c, v = [], [], []
    for p, t in fi.items():
        i, j = [a for a in range(3) if p[a] % 2 == 1]
        # the four edge sites x-e_j, x+e_i, x+e_j, x-e_i with signs (+,+,-,-)
        for q, sg in ((shift(p, j, -1), 1), (shift(p, i, +1), 1), (shift(p, j, +1), -1), (shift(p, i, -1), -1)):
            r.append(t)
            c.append(ei[q])
            v.append(sg)
    C = mk(r, c, v, (len(F), len(E)))
    C.sum_duplicates()
    r, c, v = [], [], []
    for t, p in enumerate(Q):
        for nrm in range(3):
            i, j = [a for a in range(3) if a != nrm]
            eps = levi(i, j, nrm)
            r += [t, t]
            c += [fi[shift(p, nrm, +1)], fi[shift(p, nrm, -1)]]
            v += [eps, -eps]
    d2 = mk(r, c, v, (len(Q), len(F)))
    d2.sum_duplicates()
    return dict(n=n, V=V, E=E, F=F, Q=Q, vi=vi, ei=ei, fi=fi, d0=d0, C=C, d2=d2)


def levi(a, b, c):
    perm = (a, b, c)
    if len(set(perm)) < 3:
        return 0
    inv = sum(1 for x in range(3) for y in range(x + 1, 3) if perm[x] > perm[y])
    return -1 if inv % 2 else 1


def tor_dist(p, q, n):
    return sum(min((p[i] - q[i]) % n[i], (q[i] - p[i]) % n[i]) for i in range(3))


def rank_mod_p(M, p):
    A = np.array(M, dtype=np.int64) % p
    rows, cols = A.shape
    r = 0
    for c in range(cols):
        if r == rows:
            break
        piv = np.nonzero(A[r:, c])[0]
        if len(piv) == 0:
            continue
        pr = r + piv[0]
        if pr != r:
            A[[r, pr]] = A[[pr, r]]
        inv = pow(int(A[r, c]), p - 2, p)
        A[r] = (A[r] * inv) % p
        nz = np.nonzero(A[:, c])[0]
        nz = nz[nz != r]
        if len(nz):
            A[nz] = (A[nz] - np.outer(A[nz, c], A[r]) % p) % p
        r += 1
    return r


def s2_multiset(Ls):
    """|s(k)|^2 = sum_i 4 sin^2(pi m_i / L_i) over the coarse momentum grid."""
    grids = [np.array([4 * math.sin(math.pi * m / L) ** 2 for m in range(L)]) for L in Ls]
    tot = (grids[0][:, None, None] + grids[1][None, :, None] + grids[2][None, None, :]).ravel()
    return tot


PRIMES = (2147483647, 1000000007)


def run_R1_R2(sizes):
    print("=" * 78)
    print("R1/R2  exact chain identities, locality, ranks over GF(p)")
    rows = []
    fails = []
    for Ls in sizes:
        X = build_complex(Ls)
        N = Ls[0] * Ls[1] * Ls[2]
        d0, C, d2 = X["d0"], X["C"], X["d2"]
        cd = (C @ d0)
        dc = (d2 @ C)
        chain_ok = cd.count_nonzero() == 0 and dc.count_nonzero() == 0
        if not chain_ok:
            hit(f"chain identity fails on torus {Ls}: nnz(C d0) = {cd.count_nonzero()}, nnz(d2 C) = {dc.count_nonzero()}")
        # locality: every nonzero at physical toroidal distance exactly 1, counts per row/col
        loc_ok = True
        for M, rl, cl in ((d0, X["E"], X["V"]), (C, X["F"], X["E"]), (d2, X["Q"], X["F"])):
            Mc = M.tocoo()
            for a, b in zip(Mc.row, Mc.col):
                if tor_dist(rl[a], cl[b], X["n"]) != 1:
                    loc_ok = False
                    break
        cnt_ok = (np.all(np.diff(C.indptr) == 4) and np.all(np.diff(C.tocsc().indptr) == 4)
                  and np.all(np.diff(d0.indptr) == 2) and np.all(np.diff(d2.indptr) == 6))
        if not loc_ok:
            hit(f"an incidence entry connects non-neighbouring physical sites on torus {Ls}")
        if not cnt_ok:
            fails.append(f"{Ls}: row/column counts differ from 2/4/4/6")
        rk = {}
        if 3 * N <= 3000:
            for p in PRIMES:
                Cd = C.toarray()
                rk.setdefault("d0", set()).add(rank_mod_p(d0.toarray(), p))
                rk.setdefault("C", set()).add(rank_mod_p(Cd, p))
                rk.setdefault("d2", set()).add(rank_mod_p(d2.toarray(), p))
                rk.setdefault("Cd0T", set()).add(rank_mod_p(np.vstack([Cd, d0.toarray().T]), p))
                # missing yz faces (plane (1,2)): delete those rows
                keep = [t for t, f in enumerate(X["F"]) if not (f[1] % 2 == 1 and f[2] % 2 == 1)]
                rk.setdefault("Cmiss", set()).add(rank_mod_p(Cd[keep], p))
            exp = {"d0": N - 1, "C": 2 * N - 2, "d2": N - 1, "Cd0T": 3 * N - 3,
                   "Cmiss": 2 * (N - Ls[1] * Ls[2]) + (Ls[1] * Ls[2] - 1)}
            for key, val in exp.items():
                got = rk[key]
                if len(got) != 1 or next(iter(got)) != val:
                    # rank over GF(p) <= rank over Q; the kernel lower bounds cap rank over Q at the
                    # expected value, so a GF(p) value equal to it is an exact rank over Q
                    if key == "C" or key == "Cd0T":
                        hit(f"rank {key} on torus {Ls}: GF(p) ranks {sorted(got)} vs expected {val} "
                            f"(transverse count / doubler statement)")
                    else:
                        fails.append(f"{Ls}: rank {key} {sorted(got)} vs {val}")
            rows.append((Ls, N, {k: next(iter(v)) for k, v in rk.items()}, exp))
            print(f"  torus {Ls}: N={N}; C d0 = 0: {cd.count_nonzero() == 0}, d2 C = 0: {dc.count_nonzero() == 0}; "
                  f"distance-1 entries only: {loc_ok}; counts 2/4/4/6: {cnt_ok}; ranks d0,C,d2,[C;d0^T],C-no-yz = "
                  f"{[next(iter(rk[k])) for k in ('d0', 'C', 'd2', 'Cd0T', 'Cmiss')]} expected "
                  f"{[exp[k] for k in ('d0', 'C', 'd2', 'Cd0T', 'Cmiss')]}")
        else:
            print(f"  torus {Ls}: N={N}; C d0 = 0: {cd.count_nonzero() == 0}, d2 C = 0: {dc.count_nonzero() == 0}; "
                  f"distance-1 entries only: {loc_ok}; counts 2/4/4/6: {cnt_ok} (ranks: see spectrum)")
    for f in fails:
        print("  note: " + f)
    return rows, fails


def run_R3(sizes):
    print("=" * 78)
    print("R3  full real-space spectra against the per-momentum formula")
    worst_ctc = 0.0
    worst_gen = 0.0
    out = []
    for Ls in sizes:
        X = build_complex(Ls)
        C = X["C"].astype(float).toarray()
        s2 = s2_multiset(Ls)
        ev = np.sort(np.linalg.eigvalsh(C.T @ C))
        pred = np.sort(np.concatenate([np.zeros_like(s2), s2, s2]))
        dev = float(np.max(np.abs(ev - pred)))
        worst_ctc = max(worst_ctc, dev)
        msg = f"  torus {Ls}: C^T C ({C.shape[1]}x{C.shape[1]}) max |eig - formula| = {dev:.2e}"
        if 6 * np.prod(Ls) <= 2400:
            Z = np.zeros((C.shape[0], C.shape[0]))
            Z2 = np.zeros((C.shape[1], C.shape[1]))
            G = np.block([[Z2, -C.T], [C, Z]])
            evg = np.sort(np.linalg.eigvalsh(1j * G))
            sabs = np.sqrt(s2)
            predg = np.sort(np.concatenate([sabs, sabs, -sabs, -sabs, np.zeros_like(s2), np.zeros_like(s2)]))
            devg = float(np.max(np.abs(evg - predg)))
            worst_gen = max(worst_gen, devg)
            npos = int(np.sum(evg > 1e-9))
            msg += f"; Yee iG ({G.shape[0]}) max dev {devg:.2e}, positive branches {npos} = 2(N-1) = {2 * (np.prod(Ls) - 1)}"
            if npos != 2 * (np.prod(Ls) - 1):
                hit(f"torus {Ls}: {npos} positive Yee frequencies, expected two per nonzero momentum")
        print(msg)
        out.append((Ls, dev))
    if worst_ctc > 1e-9 or worst_gen > 1e-9:
        hit(f"real-space spectrum differs from two transverse branches per momentum (dev {max(worst_ctc, worst_gen):.2e})")
    return worst_ctc, worst_gen


def cubic_group():
    out = []
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product((1, -1), repeat=3):
            R = np.zeros((3, 3), dtype=int)
            for a in range(3):
                R[perm[a], a] = signs[a]
            out.append((perm, signs, int(round(np.linalg.det(R)))))
    return out


def run_R4(Lvals):
    print("=" * 78)
    print("R4  real-space action of the 48 signed permutations on d0, C, d2")
    res = []
    for L in Lvals:
        X = build_complex((L, L, L))
        n = X["n"]
        good_proper = good_improper = 0
        for perm, signs, det in cubic_group():
            def act(p):
                q = [0, 0, 0]
                for a in range(3):
                    q[perm[a]] = (signs[a] * p[a]) % n[perm[a]]
                return tuple(q)
            # vertices: no sign; edges: axis i -> perm[i], sign signs[i];
            # faces: plane (i,j) -> {perm i, perm j}, sign s_i s_j (-1 if order flips); cubes: det
            SV = sps.csr_matrix((np.ones(len(X["V"])), ([X["vi"][act(p)] for p in X["V"]], range(len(X["V"])))),
                                shape=(len(X["V"]),) * 2)
            er, es = [], []
            for p in X["E"]:
                i = [a for a in range(3) if p[a] % 2 == 1][0]
                er.append(X["ei"][act(p)])
                es.append(signs[i])
            SE = sps.csr_matrix((np.array(es, float), (er, range(len(X["E"])))), shape=(len(X["E"]),) * 2)
            fr, fs = [], []
            for p in X["F"]:
                i, j = [a for a in range(3) if p[a] % 2 == 1]
                sg = signs[i] * signs[j] * (1 if perm[i] < perm[j] else -1)
                fr.append(X["fi"][act(p)])
                fs.append(sg)
            SF = sps.csr_matrix((np.array(fs, float), (fr, range(len(X["F"])))), shape=(len(X["F"]),) * 2)
            qi = {p: t for t, p in enumerate(X["Q"])}
            SQ = sps.csr_matrix((np.full(len(X["Q"]), float(det)), ([qi[act(p)] for p in X["Q"]], range(len(X["Q"])))),
                                shape=(len(X["Q"]),) * 2)
            ok = ((SE @ X["d0"] @ SV.T - X["d0"]).count_nonzero() == 0 and
                  (SF @ X["C"] @ SE.T - X["C"]).count_nonzero() == 0 and
                  (SQ @ X["d2"] @ SF.T - X["d2"]).count_nonzero() == 0)
            if det == 1:
                good_proper += ok
                if not ok:
                    hit(f"proper rotation perm={perm} signs={signs} changes the incidence law on L={L}")
            else:
                good_improper += ok
        res.append((L, good_proper, good_improper))
        print(f"  L={L}: proper rotations fixing (d0, C, d2): {good_proper}/24; improper (2-form face signs, "
              f"cube sign det): {good_improper}/24")
    return res


def run_R5(L=6, t=5.0, alpha=0.37, beta=1 / 0.37):
    print("=" * 78)
    print("R5  energy and Gauss rows under exp(tG), real space")
    X = build_complex((L, L, L))
    C = X["C"].astype(float)
    E0 = C.shape[1]
    F0 = C.shape[0]
    G = sps.bmat([[None, -beta * C.T], [alpha * C, None]]).tocsr()
    rng = np.random.default_rng(3)
    y0 = rng.standard_normal(E0 + F0)
    y = expm_multiply(G, y0, start=0, stop=t, num=6, endpoint=True)
    Hs = [0.5 * alpha * np.dot(v[:E0], v[:E0]) + 0.5 * beta * np.dot(v[E0:], v[E0:]) for v in y]
    gE = [np.linalg.norm(X["d0"].T.astype(float) @ v[:E0] - X["d0"].T.astype(float) @ y0[:E0]) for v in y]
    gB = [np.linalg.norm(X["d2"].astype(float) @ v[E0:] - X["d2"].astype(float) @ y0[E0:]) for v in y]
    drift = max(abs(h - Hs[0]) / Hs[0] for h in Hs)
    print(f"  L={L}, alpha={alpha}, beta=1/alpha, t in [0,{t}]: relative energy drift {drift:.2e}; "
          f"electric Gauss change {max(gE):.2e}; magnetic Gauss change {max(gB):.2e}")
    if drift > 1e-9 or max(gE) > 1e-9 or max(gB) > 1e-9:
        hit(f"energy or Gauss row changes under the generator (drift {drift:.2e}, {max(gE):.2e}, {max(gB):.2e})")
    return drift, max(gE), max(gB)


def run_R6(Lvals=(4, 5), kappas=(0.37, 1.0, 2.9, 11.0)):
    print("=" * 78)
    print("R6  OU sampler on the mean-zero transverse space, real-space Lyapunov")
    worst = 0.0
    worst_spec = 0.0
    zero_counts = []
    for L in Lvals:
        X = build_complex((L, L, L))
        N = L ** 3
        C = X["C"].astype(float).toarray()
        d0 = X["d0"].astype(float).toarray()
        K = C.T @ C
        # axis-sum rows
        J = np.zeros((3, 3 * N))
        for t, p in enumerate(X["E"]):
            i = [a for a in range(3) if p[a] % 2 == 1][0]
            J[i, t] = 1.0
        Qg = sla.null_space(d0.T)                 # d0^T A = 0 (gauge fixed)
        QH = sla.null_space(np.vstack([d0.T, J]))  # mean-zero transverse space H
        zg = int(np.sum(np.abs(np.linalg.eigvalsh(Qg.T @ K @ Qg)) < 1e-9))
        zH = int(np.sum(np.abs(np.linalg.eigvalsh(QH.T @ K @ QH)) < 1e-9))
        zero_counts.append((L, Qg.shape[1], zg, QH.shape[1], zH))
        print(f"  L={L}: dim ker d0^T = {Qg.shape[1]} with {zg} zero modes of C^T C (harmonic); "
              f"dim H = {QH.shape[1]} (2N-2 = {2 * N - 2}) with {zH} zero modes")
        if zg != 3 or zH != 0 or QH.shape[1] != 2 * N - 2:
            hit(f"L={L}: harmonic/transverse zero-mode count {zg}/{zH}, dim H {QH.shape[1]}")
        MH = 0.25 * QH.T @ K @ QH
        s2 = s2_multiset((L, L, L))
        nz = np.sort(np.concatenate([s2[s2 > 1e-12], s2[s2 > 1e-12]]))
        for kap in kappas:
            DD = (1.0 / (2 * kap)) * np.eye(QH.shape[1])
            Sig = sla.solve_continuous_lyapunov(MH, DD)
            target = (1.0 / kap) * np.linalg.inv(QH.T @ K @ QH)
            dev = float(np.max(np.abs(Sig - target)) / np.max(np.abs(target)))
            worst = max(worst, dev)
            spec = np.sort(np.linalg.eigvalsh(kap * (Sig + Sig.T) / 2))
            pred = np.sort(1.0 / nz)
            ds = float(np.max(np.abs(spec - pred) / pred))
            worst_spec = max(worst_spec, ds)
        print(f"  L={L}: Lyapunov Sigma vs (1/kappa)(C^T C|_H)^-1 over kappa={kappas}: max rel dev {worst:.2e}; "
              f"spectrum of kappa*Sigma vs 1/|s|^2 (two per nonzero k): max rel dev {worst_spec:.2e}")
    if worst > 1e-8 or worst_spec > 1e-8:
        hit(f"projected Gaussian sampler variance differs from 1/(kappa |s|^2) (rel dev {max(worst, worst_spec):.2e})")
    return worst, worst_spec, zero_counts


def run_R7():
    print("=" * 78)
    print("R7  unit speed, two-reflection block, whole-zone comparison")
    mp.mp.dps = 40
    # reciprocal coefficients: omega = sqrt(alpha beta) |s| -> speed 1 in every direction
    rows = []
    for L in (256, 1024, 4096):
        for direc in ((1, 0, 0), (1, 1, 1), (1, 2, 3)):
            k = [2 * mp.pi * d / L for d in direc]
            om = mp.sqrt(sum(4 * mp.sin(ki / 2) ** 2 for ki in k))
            kk = mp.sqrt(sum(ki ** 2 for ki in k))
            rows.append((L, direc, om / kk))
    for kap in (mp.mpf("0.37"), mp.mpf(3), mp.mpf(19)):
        if abs(mp.sqrt((1 / kap) * kap) - 1) > mp.mpf(10) ** -35:
            hit("reciprocal coefficients do not give speed one")
    last = [r for r in rows if r[0] == 4096]
    print("  omega/|k| at L=4096 along (100),(111),(123): " + ", ".join(mp.nstr(r[2], 12) for r in last))
    if any(abs(r[2] - 1) > 1e-6 for r in last):
        hit("reciprocal Yee speed differs from one at long wavelength")
    # two-reflection block: exact rotation by 2 arccos(lambda) at many lambda
    wdev = 0
    for num in range(0, 201):
        lam = mp.mpf(num) / 200
        a = 2 * mp.acos(lam)
        c = 2 * lam ** 2 - 1
        s = 2 * lam * mp.sqrt(1 - lam ** 2)
        W = mp.matrix([[c, -s], [s, c]])
        WtW = W.T * W
        wdev = max(wdev, abs(WtW[0, 0] - 1), abs(WtW[1, 1] - 1), abs(WtW[0, 1]), abs(c - mp.cos(a)), abs(s - mp.sin(a)))
    print(f"  two-reflection block, 201 lambdas in [0,1]: max |W^T W - I|, |cos,sin - (2 arccos)| = {mp.nstr(wdev, 3)}")
    if wdev > mp.mpf(10) ** -30:
        hit("two-reflection block not unitary or phase not 2 arccos lambda")
    # infrared: Omega = 2 arccos(exp(-tau |s|^2/4)) at tau=1/2 -> |s| - |s|^3/48 + ...
    cf = []
    for sv in (mp.mpf("0.1"), mp.mpf("0.01"), mp.mpf("0.001")):
        Om = 2 * mp.acos(mp.e ** (-sv ** 2 / 8))
        cf.append((sv - Om) / sv ** 3)
    print("  (|s| - Omega)/|s|^3 at |s| = 0.1, 0.01, 0.001: " + ", ".join(mp.nstr(x, 10) for x in cf) + " (1/48 = 0.0208333)")
    # whole zone, L = 16 grid
    L = 16
    s2 = s2_multiset((L, L, L))
    om = np.sqrt(s2)
    Om = 2 * np.arccos(np.exp(-s2 / 8))
    gap = np.abs(Om - om)
    frac = float(np.mean(gap[s2 > 0] > 1e-3))
    imax = int(np.argmax(gap))
    print(f"  L=16 zone: max |Omega - omega| = {gap.max():.6f} at |s|^2 = {s2[imax]:.4f} (corner: omega = "
          f"{math.sqrt(12):.6f}, Omega = {2 * math.acos(math.exp(-1.5)):.6f}); fraction of nonzero momenta with "
          f"gap > 1e-3: {frac:.4f}")
    if gap.max() < 1e-6:
        hit("direct Yee and matched spectral lift coincide across the zone")
    # tick dependence: speed sqrt(2 tau)
    sp = []
    for tau in (mp.mpf("0.125"), mp.mpf("0.5"), mp.mpf(2)):
        sv = mp.mpf("1e-6")
        sp.append(2 * mp.acos(mp.e ** (-tau * sv ** 2 / 4)) / sv)
    print("  lift speed at tau = 1/8, 1/2, 2: " + ", ".join(mp.nstr(x, 10) for x in sp))
    return rows, wdev, cf, gap.max(), frac, sp


def main():
    t0 = time.time()
    rank_sizes = [(2, 2, 2), (3, 3, 3), (4, 4, 4), (5, 5, 5), (6, 6, 6), (2, 3, 4), (3, 4, 5), (2, 5, 7),
                  (7, 7, 7), (8, 8, 8), (4, 6, 8), (10, 10, 10)]
    rows, fails = run_R1_R2(rank_sizes)
    summary("R1/R2 exact: C d0 = 0 and d2 C = 0 with distance-1 entries only (counts 2/4/4/6) on tori "
            + ", ".join(str(s) for s in rank_sizes) + "; GF(p) ranks (two primes) "
            + "; ".join(f"{Ls}: d0 {r['d0']}, C {r['C']}, d2 {r['d2']}, [C;d0^T] {r['Cd0T']}, C-without-yz {r['Cmiss']}"
                        for Ls, N, r, e in rows)
            + f" all equal N-1, 2N-2, N-1, 3N-3, 2(N-LyLz)+LyLz-1: {all(r == e for _, _, r, e in rows)}")
    spec_sizes = [(3, 3, 3), (4, 4, 4), (5, 5, 5), (6, 6, 6), (7, 7, 7), (8, 8, 8), (2, 3, 4), (3, 4, 5), (2, 5, 7)]
    wc, wg = run_R3(spec_sizes)
    summary(f"R3 real-space spectra on {len(spec_sizes)} tori up to 8^3 (C^T C 1536x1536): max |eig - "
            f"{{0,|s|^2,|s|^2}}| = {wc:.1e}; Yee iG up to 6^3 (1296x1296) max dev {wg:.1e}, positive branches 2(N-1)")
    r4 = run_R4((2, 3, 4, 5))
    summary("R4 real-space cubic action: " + "; ".join(f"L={L}: proper {a}/24, improper {b}/24 fix (d0,C,d2)"
                                                   for L, a, b in r4))
    drift, gE, gB = run_R5()
    summary(f"R5 exp(tG) on 6^3 (1296 fields), t<=5: energy drift {drift:.1e}, Gauss changes {gE:.1e}/{gB:.1e}")
    w, ws, zc = run_R6()
    summary(f"R6 OU on H (real space, L=4,5; kappa 0.37,1,2.9,11): Lyapunov vs (1/kappa)(C^TC|_H)^-1 rel dev {w:.1e}; "
            f"kappa*Sigma spectrum vs 1/|s|^2 rel dev {ws:.1e}; harmonic zero modes "
            + ", ".join(f"L={L}: {zg} in ker d0^T (dim {dg}), {zH} in H (dim {dH})" for L, dg, zg, dH, zH in zc))
    rows7, wdev, cf, gmax, frac, sp = run_R7()
    summary(f"R7 omega/|k| at L=4096 (100,111,123) = {', '.join(mp.nstr(r[2], 10) for r in rows7 if r[0] == 4096)}; "
            f"two-reflection block exact to {mp.nstr(wdev, 2)}; (|s|-Omega)/|s|^3 -> {mp.nstr(cf[-1], 8)} (1/48); "
            f"L=16 zone max |Omega - omega| = {gmax:.6f}, fraction gap>1e-3 = {frac:.4f}; lift speed at tau 1/8,1/2,2 = "
            f"{', '.join(mp.nstr(x, 8) for x in sp)}")
    print("=" * 78)
    if fails:
        summary("non-falsifier count notes: " + "; ".join(fails))
    summary(f"hits={len(HITS)}; runtime {time.time() - t0:.0f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
