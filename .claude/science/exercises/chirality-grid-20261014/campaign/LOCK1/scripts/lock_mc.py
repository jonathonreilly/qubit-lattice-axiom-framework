"""LOCK-1: canonical Monte Carlo of the static law with vacancies (record gas).

Weight of an arrangement on the L^3 torus: prod over recorded bonds (both ends
recorded) of g * M(s, s'), M = 6*omega/(p+q+4r), omega = p, q, r for equal,
opposite, orthogonal axis contents (blocks 39/40/81/117 as landed).  Content-less
gas: p = q = r (M = 1).  g = 0 is hard-core nearest-neighbour exclusion.
Canonical: fixed number of records N = round(rho V) (block 39 T1: motion keeps N).

Moves (a sampler of the static law, not the motion clause's dynamics):
  nonlocal record-vacancy exchange carrying the content; content re-draw.
Usage: python3 lock_mc.py TASK OUTPREFIX   (TASK in C1, C2, C3, T)
"""
import sys, json, time, math
import numpy as np
from numba import njit


def build_nbr(L):
    V = L ** 3
    nbr = np.empty((V, 6), np.int32)
    par = np.empty(V, np.int8)
    for k in range(L):
        for j in range(L):
            for i in range(L):
                x = i + L * j + L * L * k
                par[x] = (i + j + k) % 2
                nbr[x, 0] = ((i + 1) % L) + L * j + L * L * k
                nbr[x, 1] = ((i - 1) % L) + L * j + L * L * k
                nbr[x, 2] = i + L * ((j + 1) % L) + L * L * k
                nbr[x, 3] = i + L * ((j - 1) % L) + L * L * k
                nbr[x, 4] = i + L * j + L * L * ((k + 1) % L)
                nbr[x, 5] = i + L * j + L * L * ((k - 1) % L)
    return nbr, par


def content_logM(p, q, r):
    lm = np.zeros((6, 6))
    tot = p + q + 4 * r
    for a in range(6):
        for b in range(6):
            if a == b:
                w = p
            elif a // 2 == b // 2:
                w = q
            else:
                w = r
            lm[a, b] = math.log(6.0 * w / tot)
    return lm


@njit(cache=True)
def seed_rng(s):
    np.random.seed(s)


@njit(cache=True)
def sweeps(nsw, occ, cont, nbr, reclist, vaclist, pos, logg, hard, lm, use_cont):
    V = occ.shape[0]
    N = reclist.shape[0]
    nv = vaclist.shape[0]
    acc = 0
    for _ in range(nsw):
        if N > 0 and nv > 0:
            for _t in range(V):
                ir = np.random.randint(N)
                iv = np.random.randint(nv)
                x = reclist[ir]
                y = vaclist[iv]
                a = cont[x]
                # before: bonds of x
                nb_b = 0
                lw_b = 0.0
                for d in range(6):
                    z = nbr[x, d]
                    if occ[z] == 1:
                        nb_b += 1
                        lw_b += lm[a, cont[z]]
                nb_a = 0
                lw_a = 0.0
                for d in range(6):
                    z = nbr[y, d]
                    if z != x and occ[z] == 1:
                        nb_a += 1
                        lw_a += lm[a, cont[z]]
                if hard:
                    if nb_a > 0:
                        continue
                    dl = lw_a - lw_b
                else:
                    dl = (nb_a - nb_b) * logg + lw_a - lw_b
                if dl >= 0.0 or np.random.random() < math.exp(dl):
                    occ[x] = 0
                    occ[y] = 1
                    cont[y] = a
                    reclist[ir] = y
                    vaclist[iv] = x
                    pos[y] = ir
                    pos[x] = iv
                    acc += 1
        if use_cont and N > 0:
            for _t in range(N):
                x = reclist[np.random.randint(N)]
                a = cont[x]
                b = np.random.randint(6)
                if b == a:
                    continue
                dl = 0.0
                for d in range(6):
                    z = nbr[x, d]
                    if occ[z] == 1:
                        dl += lm[b, cont[z]] - lm[a, cont[z]]
                if dl >= 0.0 or np.random.random() < math.exp(dl):
                    cont[x] = b
    return acc


@njit(cache=True)
def count_bonds(occ, nbr):
    B = 0
    for x in range(occ.shape[0]):
        if occ[x] == 1:
            for d in (0, 2, 4):
                if occ[nbr[x, d]] == 1:
                    B += 1
    return B


def init_state(L, N, par, nbr, start, hard, rng):
    V = L ** 3
    occ = np.zeros(V, np.int8)
    if start == "board":
        A = np.flatnonzero(par == 0)
        Bs = np.flatnonzero(par == 1)
        if N <= A.size:
            occ[rng.choice(A, N, replace=False)] = 1
        else:
            occ[A] = 1
            occ[rng.choice(Bs, N - A.size, replace=False)] = 1
    else:
        if hard:
            # random sequential addition with nearest-neighbour exclusion
            order = rng.permutation(V)
            n = 0
            for x in order:
                if n >= N:
                    break
                if occ[nbr[x]].sum() == 0:
                    occ[x] = 1
                    n += 1
            if n < N:
                return None
        else:
            occ[rng.choice(V, N, replace=False)] = 1
    cont = rng.integers(0, 6, V).astype(np.int8)
    reclist = np.flatnonzero(occ == 1).astype(np.int32)
    vaclist = np.flatnonzero(occ == 0).astype(np.int32)
    pos = np.zeros(V, np.int32)
    pos[reclist] = np.arange(reclist.size)
    pos[vaclist] = np.arange(vaclist.size)
    return occ, cont, reclist, vaclist, pos


SVEC = np.array([[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]], float)


def run_point(L, rho, g, pqr, start, seed, neq=2000, nmeas=4000, every=5, nblk=10):
    nbr, par = build_nbr(L)
    V = L ** 3
    N = int(round(rho * V))
    hard = (g == 0.0)
    logg = 0.0 if hard else math.log(g)
    use_cont = pqr is not None and not (pqr[0] == pqr[1] == pqr[2])
    lm = content_logM(*pqr) if use_cont else np.zeros((6, 6))
    rng = np.random.default_rng(seed)
    st = init_state(L, N, par, nbr, start, hard, rng)
    if st is None:
        st = init_state(L, N, par, nbr, "board", hard, rng)
        start = "board(rsa-jammed)"
    occ, cont, reclist, vaclist, pos = st
    seed_rng(seed)
    stag = np.where(par == 0, 1.0, -1.0)
    t0 = time.time()
    sweeps(neq, occ, cont, nbr, reclist, vaclist, pos, logg, hard, lm, use_cont)
    nm = nmeas // every
    per = nm // nblk
    nm = per * nblk
    ms = np.empty(nm)
    smin = np.empty(nm)
    cu = np.empty(nm)
    cs = np.empty(nm)
    bonds = np.empty(nm)
    Sblk = np.zeros((nblk, L, L, L))
    acc = 0
    for m in range(nm):
        acc += sweeps(every, occ, cont, nbr, reclist, vaclist, pos, logg, hard, lm, use_cont)
        n = occ.astype(float)
        ms[m] = (n * stag).sum() / V
        nk = np.fft.fftn(n.reshape(L, L, L))  # array axes (k, j, i)
        Sk = (nk.real ** 2 + nk.imag ** 2) / V
        Sblk[m // per] += Sk
        smin[m] = (Sk[1, 0, 0] + Sk[0, 1, 0] + Sk[0, 0, 1]) / 3.0
        if use_cont:
            sv = SVEC[cont] * n[:, None]
            cu[m] = (sv.sum(0) ** 2).sum() / max(N, 1) ** 2
            cs[m] = ((sv * stag[:, None]).sum(0) ** 2).sum() / max(N, 1) ** 2
        else:
            cu[m] = 0.0
            cs[m] = 0.0
        bonds[m] = count_bonds(occ, nbr)
    Sblk /= per
    Smean = Sblk.mean(0)
    Smean[0, 0, 0] = 0.0
    kmax = np.unravel_index(np.argmax(Smean), Smean.shape)
    Sk_max = Smean[kmax]
    Q = (L // 2, L // 2, L // 2)
    SQ_blk = Sblk[:, Q[0], Q[1], Q[2]]
    Smax_blk = np.array([b[kmax] for b in Sblk])
    m2 = (ms ** 2).mean()
    m4 = (ms ** 4).mean()
    U = 1.0 - m4 / (3.0 * m2 ** 2) if m2 > 0 else 0.0

    def se(a):
        b = a[: per * nblk].reshape(nblk, -1).mean(1) if a.ndim == 1 and a.size == nm else a
        return float(b.std(ddof=1) / math.sqrt(nblk))

    # Binder error by blocks
    Ub = []
    for b in range(nblk):
        x = ms[b * per:(b + 1) * per]
        mm2 = (x ** 2).mean()
        Ub.append(1.0 - (x ** 4).mean() / (3.0 * mm2 ** 2) if mm2 > 0 else 0.0)
    Ub = np.array(Ub)
    res = dict(L=L, rho=rho, N=N, g=g, pqr=list(pqr) if pqr else None, start=start, seed=seed,
               neq=neq, nmeas=nmeas, accept=acc / (nm * every * V),
               ms2=float(m2), ms2_se=se(ms ** 2), U=float(U), U_se=float(Ub.std(ddof=1) / math.sqrt(nblk)),
               SQ_over_V=float(SQ_blk.mean() / V), SQ_over_V_se=float(SQ_blk.std(ddof=1) / math.sqrt(nblk) / V),
               kmax=[int(kmax[2]), int(kmax[1]), int(kmax[0])], Smax=float(Sk_max),
               Smax_over_V=float(Sk_max / V), Smax_over_V_se=float(Smax_blk.std(ddof=1) / math.sqrt(nblk) / V),
               Smin_over_V=float(smin.mean() / V), Smin_over_V_se=se(smin) / V,
               cont_uni=float(cu.mean()), cont_stag=float(cs.mean()),
               bonds_per_rec=float(bonds.mean() / max(N, 1)), secs=time.time() - t0)
    return res, Smean


GRIDS = {
    "T": dict(Ls=[24], rhos=[0.25], gs=[0.0, 0.3], pqrs=[None, (3, 1, 2)], starts=["rand"], neq=200, nmeas=400),
    "C1": dict(Ls=[8, 12, 16, 24], rhos=[0.125, 0.25, 0.375, 0.5],
               gs=[0.0, 0.02, 0.1, 0.2, 0.3, 0.35, 0.4, 0.45, 0.5, 1.0, 2.0, 4.0, 8.0], pqrs=[None], starts=["rand"]),
    "C2": dict(Ls=[12, 16], rhos=[0.125, 0.25, 0.5], gs=[1e-5, 0.25, 1.0, 4.0],
               pqrs=[(3, 1, 2), (12, 1, 2)], starts=["rand"]),
    "C3": dict(Ls=[12, 16, 24], rhos=[0.16, 0.18, 0.20, 0.21, 0.22, 0.24], gs=[0.0], pqrs=[None], starts=["rand"]),
    "F1": dict(Ls=[24], rhos=[0.5], gs=[0.02, 0.1], pqrs=[None], starts=["board", "rand"], neq=20000, nmeas=4000),
    "F2": dict(Ls=[12, 16, 24], rhos=[0.25], gs=[0.12, 0.14, 0.16, 0.18], pqrs=[None], starts=["rand"]),
    "F3": dict(Ls=[12, 16, 24], rhos=[0.375], gs=[0.36, 0.37, 0.38, 0.39], pqrs=[None], starts=["rand"]),
    "F4": dict(Ls=[12, 16, 24], rhos=[0.5], gs=[0.40, 0.41, 0.42, 0.43], pqrs=[None], starts=["rand"]),
    "F5": dict(Ls=[16], rhos=[0.5], gs=[1e-5], pqrs=[(3, 1, 2), (12, 1, 2)], starts=["board", "rand"], neq=20000, nmeas=4000),
    "H": dict(Ls=[16], rhos=[0.25, 0.375, 0.5], gs=[0.0, 0.2, 0.35, 0.45, 2.0, 4.0], pqrs=[None], starts=["rand", "board"]),
}


def main():
    task, outp = sys.argv[1], sys.argv[2]
    G = GRIDS[task]
    neq = G.get("neq", 2000)
    nmeas = G.get("nmeas", 4000)
    out = open(outp + ".jsonl", "a")
    Ssave = {}
    seed = 1000
    for pqr in G["pqrs"]:
        for L in G["Ls"]:
            for rho in G["rhos"]:
                for g in G["gs"]:
                    for start in G["starts"]:
                        seed += 1
                        res, Smean = run_point(L, rho, g, pqr, start, seed, neq=neq, nmeas=nmeas)
                        res["task"] = task
                        out.write(json.dumps(res) + "\n")
                        out.flush()
                        key = f"{task}_L{L}_r{rho}_g{g}_{'cl' if pqr is None else ''.join(map(str, pqr))}_{start}"
                        if L <= 16:
                            Ssave[key] = Smean.astype(np.float32)
                        print(f"{key} U={res['U']:.3f} SQ/V={res['SQ_over_V']:.4f} Smax/V={res['Smax_over_V']:.4f}@{res['kmax']} "
                              f"Smin/V={res['Smin_over_V']:.4f} cu={res['cont_uni']:.3f} cs={res['cont_stag']:.3f} "
                              f"acc={res['accept']:.3f} t={res['secs']:.1f}s", flush=True)
    np.savez_compressed(outp + "_Sk.npz", **Ssave)


if __name__ == "__main__":
    main()
