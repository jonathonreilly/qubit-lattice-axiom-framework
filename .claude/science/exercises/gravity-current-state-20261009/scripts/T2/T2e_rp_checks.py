#!/usr/bin/env python3
"""T2e: reflection-positivity checks for every family (per axis and full kernel).

For a translation-invariant Gaussian field, OS positivity for reflections in the time direction holds iff, at EVERY
spatial momentum k, the time correlator G_k(n) = (1/2pi) int dq0 cos(q0 n)/D(q0,k) gives PSD Hankel matrices:
  site  [G(i+j)],  link  [G(i+j+1)],  Hausdorff  [G(i+j) - G(i+j+1)]   (i, j = 0..T).
site+link (+Hausdorff) <=> G(n) = int lambda^|n| dm, m >= 0 on [0,1]  (positive transfer matrix; Lemma N's class).
'Per axis' = k = 0 (time axis; spatial axes identical at g = 1 by hypercubic symmetry).
'Full kernel' = all k on a 12^3 grid including 0 and pi.  Done at g = 1 and at finite shear eps = 0.3.
Mass m^2 = 0.09 (a constant shift; does not change the Nevanlinna property).  Pass if min eig/max eig > -1e-10.
"""
import numpy as np
from scipy.linalg import expm
from t2_core import CHANNELS, V_matrix
import T2b_kl_proper_distance as KLm
from T2c_perfect_action import B_tables

M2 = 0.09
NT = 512
LS = 12
T = 10
q0 = 2 * np.pi * (np.arange(NT) + 0.5) / NT - np.pi
ks = 2 * np.pi * np.arange(LS) / LS
ks = np.where(ks > np.pi, ks - 2 * np.pi, ks)
K1, K2, K3 = np.meshgrid(ks, ks, ks, indexing="ij")
COS = np.cos(np.outer(np.arange(2 * T + 2), q0))  # (2T+2, NT)


def hankel_report(Sq):
    """Sq: propagator on (NT, LS, LS, LS). Returns worst (site, link, hausdorff) eigen-ratios and at k = 0."""
    G = np.einsum("nj,j...->n...", COS, Sq) / NT  # (2T+2, LS,LS,LS)
    G = G.reshape(2 * T + 2, -1)
    idx = np.add.outer(np.arange(T + 1), np.arange(T + 1))
    worst = np.array([np.inf, np.inf, np.inf]); at0 = None
    for c in range(G.shape[1]):
        g = G[:, c]
        Hs = g[idx]; Hl = g[idx + 1]; Hh = Hs - Hl
        r = []
        for H in (Hs, Hl, Hh):
            ev = np.linalg.eigvalsh(H)
            r.append(ev.min() / ev.max())
        worst = np.minimum(worst, r)
        if c == 0:
            at0 = np.array(r)
    return at0, worst


def fmt(name, at0, worst):
    flag = "PASS" if worst.min() > -1e-10 else "VIOLATED"
    print(f" {name:44s} k=0 (site,link,haus) {at0[0]:+.1e} {at0[1]:+.1e} {at0[2]:+.1e} | all k worst {worst[0]:+.1e} {worst[1]:+.1e} {worst[2]:+.1e}  {flag}")


def g3(X, eps):
    return np.eye(3) if X is None else expm(eps * X)


def carrier_S(gsp):
    gi = np.linalg.inv(gsp)
    V = V_matrix(K1, K2, K3)
    return sum(gi[i, j] * V[i][j] for i in range(3) for j in range(3))


def famA(a, r, gsp):
    Ssp = carrier_S(gsp)
    S = (2 - 2 * np.cos(q0))[:, None, None, None] + Ssp[None]
    F = sum(ak * S / (1 + rk * S) for ak, rk in zip(a, r))
    return 1 / (M2 + F)


def famD(r, gsp):
    w, U = np.linalg.eigh(gsp)
    gmh = U @ np.diag(w ** -0.5) @ U.T
    V = np.array(V_matrix(K1, K2, K3), dtype=object)
    Vm = np.empty((3, 3) + K1.shape)
    for i in range(3):
        for j in range(3):
            Vm[i, j] = V[i][j]
    Mm = np.einsum("ij,jk...,kl->il...", gmh, Vm, gmh)
    h = lambda x: x / (1 + r * x)
    Dsp = sum(h(Mm[i, i]) for i in range(3))
    return 1 / (M2 + h(2 - 2 * np.cos(q0))[:, None, None, None] + Dsp[None])


def famB(M, gsp, R=7):
    G4 = np.eye(4); G4[1:, 1:] = gsp
    G4i = np.linalg.inv(G4)
    lam = np.linalg.eigvalsh(G4i).min()
    rr = np.arange(-R, R + 1)
    n = np.array(np.meshgrid(rr, rr, rr, rr, indexing="ij")).reshape(4, -1).T
    n = n[np.any(n != 0, axis=1)]
    u = np.einsum("ni,ij,nj->n", n, G4, n)
    Js = KLm.Js_derivs(u, M * M, jmax=0)[0]
    tot = Js.sum()
    pos = np.full((NT, LS, LS, LS), tot)
    for n0 in range(-R, R + 1):
        sel = n[:, 0] == n0
        arr = np.zeros((LS, LS, LS), complex)
        nn = n[sel, 1:]
        np.add.at(arr, (nn[:, 0] % LS, nn[:, 1] % LS, nn[:, 2] % LS), Js[sel])
        W = np.fft.ifftn(arr) * LS ** 3
        pos -= (np.exp(1j * q0 * n0)[:, None, None, None] * W[None]).real
    # images
    r4 = range(-3, 4)
    imgs = []
    for l in np.array(np.meshgrid(r4, r4, r4, r4, indexing="ij")).reshape(4, -1).T:
        mn = sum((np.pi * (2 * abs(x) - 1)) ** 2 for x in l if x != 0)
        if lam * mn * KLm.TC <= 40:
            imgs.append(l)
    D = pos.copy()
    for l in imgs:
        kk0 = 2 * np.pi * l
        v0 = kk0 @ G4i @ kk0
        if np.all(l == 0):
            D += np.exp(-M * M * KLm.TC) / (M * M)
        else:
            D += KLm.f_derivs(v0, M * M)[0]
        k4 = [(q0 + 2 * np.pi * l[0])[:, None, None, None], (K1 + 2 * np.pi * l[1])[None], (K2 + 2 * np.pi * l[2])[None], (K3 + 2 * np.pi * l[3])[None]]
        v = sum(G4i[i, j] * k4[i] * k4[j] for i in range(4) for j in range(4) if G4i[i, j] != 0)
        D -= KLm.f_derivs(v, M * M)[0]
    return 1 / (M2 + D * M ** 4)


def T0_tab(q, t):
    B = B_tables(np.where(q == 0, 1.0, q), t)
    s2 = 4 * np.sin(q / 2) ** 2
    T0 = s2 * B[-2]
    return np.where(q == 0, 1.0, T0)


def famC(s2, cdiag=(1, 1, 1), smin=-18, ds=0.04):
    """perfect action propagator with diagonal spatial metric g^-1 = diag(cdiag), mass M2 (Schwinger)."""
    smax = np.log(45 / M2) + 1
    S = np.full((NT, LS, LS, LS), s2, float)
    sg = np.arange(smin, smax + ds / 2, ds)
    for i, s in enumerate(sg):
        t = np.exp(s); w = ds * t * (0.5 if i in (0, len(sg) - 1) else 1.0) * np.exp(-t * M2)
        a0 = T0_tab(q0, t)
        a = [T0_tab(ks, c * t) for c in cdiag]
        S += w * a0[:, None, None, None] * np.multiply.outer(np.multiply.outer(a[0], a[1]), a[2])[None]
    return S


def gauss_control(sig, R=None):
    R = R or int(7 * sig) + 1
    rr = np.arange(-R, R + 1)
    n = np.array(np.meshgrid(rr, rr, rr, rr, indexing="ij")).reshape(4, -1).T
    n = n[np.any(n != 0, axis=1)]
    w = np.exp(-(n ** 2).sum(1) / (2 * sig ** 2))
    w = w / (0.5 * (w * n[:, 0] ** 2).sum())
    D = np.full((NT, LS, LS, LS), w.sum())
    for n0 in range(-R, R + 1):
        sel = n[:, 0] == n0
        arr = np.zeros((LS, LS, LS), complex)
        nn = n[sel, 1:]
        np.add.at(arr, (nn[:, 0] % LS, nn[:, 1] % LS, nn[:, 2] % LS), w[sel])
        W = np.fft.ifftn(arr) * LS ** 3
        D -= (np.exp(1j * q0 * n0)[:, None, None, None] * W[None]).real
    return 1 / (M2 + D)


if __name__ == "__main__":
    print(f"== T2e: Hankel RP tests, T = {T}, NT = {NT}, spatial grid {LS}^3 (incl. 0, pi), m^2 = {M2} ==")
    eps = 0.3
    shears = [("g=1", None), ("E_g eps=0.3", CHANNELS["E_g"]), ("T_2g eps=0.3", CHANNELS["T_2g"])]
    rA = (16 - 1 / 3) / 4
    for lab, X in shears:
        g = g3(X, eps)
        fmt(f"A single pole sigma_N=4 [{lab}]", *hankel_report(famA([1.0], [rA], g)))
        fmt(f"A 3-pole (a=.2,.5,.3; r=.5,3,10) [{lab}]", *hankel_report(famA([.2, .5, .3], [.5, 3., 10.], g)))
        fmt(f"D per-axis single pole sigma_N=4 [{lab}]", *hankel_report(famD(rA, g)))
        fmt(f"B KL M=0.5 (sigma_N=4) [{lab}]", *hankel_report(famB(0.5, g)))
        fmt(f"B KL M=0.25 (sigma_N=8) [{lab}]", *hankel_report(famB(0.25, g)))
    for s2 in (0.0, 1 / 12, 1 / 6, 1 / 3, 4.0):
        fmt(f"C perfect action s^2={s2:.4f} [g=1]", *hankel_report(famC(s2)))
    a = np.exp(eps / np.sqrt(2))
    for s2 in (1 / 6, 4.0):
        fmt(f"C perfect action s^2={s2:.4f} [E_g eps=0.3]", *hankel_report(famC(s2, cdiag=(1 / a, a, 1))))
    fmt("control: 4D Gaussian proper-distance sigma=2 [g=1]", *hankel_report(gauss_control(2.0)))
    fmt("control: 4D Gaussian proper-distance sigma=1 [g=1]", *hankel_report(gauss_control(1.0)))
