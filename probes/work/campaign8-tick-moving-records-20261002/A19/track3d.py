#!/usr/bin/env python3
"""A19 3D brief (supplied toy): record tracks of one excitation on the A10 signed time-symmetric cycle
(strang-9 word, Kogut-Susskind signs, theta = 0.6: isotropic massless cone at K* = (pi,pi,pi), speed 2 sin(theta)
sites per cycle), registered with chance g per cycle by a sharp site cut or a Gaussian (unsharp) cut.
Real-space layer code adapted from A10 t7_real.py (checked there against Bloch form to 6e-15; re-checked here).

usage: track3d.py CUT G [L B T q0]   CUT in {none, site, gS}
"""
import sys, time
import numpy as np

PI = np.pi


# ---------------- A10 Bloch builder (vcyc.layers_U), signed strang-9 word
def _pairs(axis):
    out = []
    for pz in (0, 1):
        for py in (0, 1):
            for px in (0, 1):
                p = [px, py, pz]
                if p[axis] != 0:
                    continue
                q = list(p); q[axis] = 1
                i0 = p[0] + 2 * p[1] + 4 * p[2]; i1 = q[0] + 2 * q[1] + 4 * q[2]
                e = 1.0 if axis == 0 else ((-1.0) ** p[0] if axis == 1 else (-1.0) ** (p[0] + p[1]))
                out.append((i0, i1, e))
    return out


PAIRS = {a: _pairs(a) for a in range(3)}


def strang9(th):
    out = []
    for a in (0, 1, 2):
        out += [(a, 0, th / 2), (a, 1, th), (a, 0, th / 2)]
    return out


def layers_U(K, layers):
    K = np.atleast_2d(K); N = K.shape[0]
    U = np.broadcast_to(np.eye(8, dtype=complex), (N, 8, 8)).copy()
    for (a, par, th) in layers:
        c, s = np.cos(th), np.sin(th)
        Lm = np.zeros((N, 8, 8), complex)
        for (i0, i1, e) in PAIRS[a]:
            Lm[:, i0, i0] = c; Lm[:, i1, i1] = c
            if par == 0:
                Lm[:, i0, i1] = -1j * e * s; Lm[:, i1, i0] = -1j * e * s
            else:
                Lm[:, i1, i0] = -1j * e * s * np.exp(1j * K[:, a]); Lm[:, i0, i1] = -1j * e * s * np.exp(-1j * K[:, a])
        U = np.exp(1j * th) * (Lm @ U)
    return U


# ---------------- real-space layers on a batch (B, L, L, L)
def make_eta(L):
    x = np.arange(L)
    return {0: None, 1: ((-1.0) ** x)[:, None, None], 2: ((-1.0) ** (x[:, None] + x[None, :]))[:, :, None]}


def apply_layer(psi, axis, par, th, ETA):
    L = psi.shape[1]
    c, s = np.cos(th), np.sin(th)
    ax = axis + 1
    eta = ETA[axis]
    ps = np.roll(psi, -par, axis=ax)
    sl0 = [slice(None)] * 4; sl1 = [slice(None)] * 4
    sl0[ax] = slice(0, L, 2); sl1[ax] = slice(1, L, 2)
    a, b = ps[tuple(sl0)].copy(), ps[tuple(sl1)].copy()
    if eta is None:
        e = 1.0
    else:
        et = np.roll(np.broadcast_to(eta, (L, L, L)), -par, axis=axis)
        sle = [slice(None)] * 3; sle[axis] = slice(0, L, 2)
        e = et[tuple(sle)][None]
    ps[tuple(sl0)] = np.exp(1j * th) * (c * a - 1j * e * s * b)
    ps[tuple(sl1)] = np.exp(1j * th) * (-1j * e * s * a + c * b)
    return np.roll(ps, par, axis=ax)


def run_cycle(psi, lay, ETA):
    for (a, p, th) in lay:
        psi = apply_layer(psi, a, p, th, ETA)
    return psi


def gauss1(sig):
    if sig <= 0:
        return np.array([0]), np.array([1.0])
    R = int(np.ceil(5 * sig)); z = np.arange(-R, R + 1)
    w = np.exp(-z ** 2 / (2 * sig ** 2)); return z, w / w.sum()


def main():
    cut = sys.argv[1]; g = float(sys.argv[2])
    L = int(sys.argv[3]) if len(sys.argv) > 3 else 48
    B = int(sys.argv[4]) if len(sys.argv) > 4 else 16
    T = int(sys.argv[5]) if len(sys.argv) > 5 else 20
    q0 = float(sys.argv[6]) if len(sys.argv) > 6 else 0.8
    th = 0.6
    lay = strang9(th)
    ETA = make_eta(L)
    rng = np.random.default_rng(2024)
    sig = float(cut[1:]) if cut.startswith("g") else 0.0
    zk, wk = gauss1(sig); cwk = np.cumsum(wk); swk = np.sqrt(wk)

    # (0) real-space vs Bloch plane-wave check (small L)
    Lc = 8; ETAc = make_eta(Lc)
    K = 2 * PI * rng.integers(0, Lc // 2, 3) / (Lc // 2)
    phi = rng.normal(size=8) + 1j * rng.normal(size=8)
    X, Y, Z = np.meshgrid(np.arange(Lc), np.arange(Lc), np.arange(Lc), indexing="ij")
    ncell = np.stack([X // 2, Y // 2, Z // 2], -1); pidx = (X % 2) + 2 * (Y % 2) + 4 * (Z % 2)
    psi = (np.exp(1j * (ncell @ K)) * phi[pidx])[None]
    out = run_cycle(psi, lay, ETAc)[0]
    ref = np.exp(1j * (ncell @ K)) * (layers_U(K[None], lay)[0] @ phi)[pidx]
    print(f"real-space vs Bloch, signed strang-9: {np.abs(out - ref).max():.1e}")

    # (1) packet in the upper cone near K* + q0 n
    nhat = np.array([1.0, 0.55, 0.25]); nhat /= np.linalg.norm(nhat)
    Kp = np.array([PI, PI, PI]) + q0 * nhat
    U0 = layers_U(np.array([[PI, PI, PI]]), lay)[0]
    ref0 = np.exp(1j * np.angle(np.linalg.eigvals(U0)[0]))
    w_, v_ = np.linalg.eig(layers_U(Kp[None], lay)[0])
    ph = np.angle(w_ * np.conj(ref0))
    phi = v_[:, np.argmin(ph)]          # eigenphase = -quasi-energy: argmin = upper (positive-energy) cone, v parallel to q
    X, Y, Z = np.meshgrid(np.arange(L), np.arange(L), np.arange(L), indexing="ij")
    ncell = np.stack([X // 2, Y // 2, Z // 2], -1); pidx = (X % 2) + 2 * (Y % 2) + 4 * (Z % 2)
    c0 = np.array([L // 4, L // 4, L // 4]) // 1
    wcell = 4.0
    # pure upper-cone packet built in Bloch space (bands are 2-fold degenerate, so a single eigenvector times an
    # envelope leaks into backward-moving bands): phi(K) = P_up(K) phi * Gaussian(K - Kp) * e^{-i K.c}
    Nc = L // 2
    kg = 2 * PI * np.arange(Nc) / Nc
    KK = np.array(np.meshgrid(kg, kg, kg, indexing="ij")).reshape(3, -1).T
    UK = layers_U(KK, lay)
    wK, vK = np.linalg.eig(UK)
    phK = np.angle(wK * np.conj(ref0))
    sel = (phK < 0).astype(float)                                     # upper cone: negative relative eigenphase
    proj = np.einsum("nij,nj,njk->nik", vK, sel, np.linalg.inv(vK))   # spectral projector (valid if V non-unitary)
    dK = ((KK - Kp + PI) % (2 * PI)) - PI
    gK = np.exp(-(dK ** 2).sum(1) * wcell ** 2) * np.exp(-1j * KK @ (c0 / 2.0))
    phiK = np.einsum("nij,j->ni", proj, phi) * gK[:, None]
    phiK = phiK.reshape(Nc, Nc, Nc, 8)
    psi0 = np.zeros((L, L, L), complex)
    for p in range(8):
        px, py, pz = p & 1, (p >> 1) & 1, (p >> 2) & 1
        psi0[px::2, py::2, pz::2] = np.fft.ifftn(phiK[..., p])
    psi0 /= np.linalg.norm(psi0)
    P0 = np.abs(psi0) ** 2
    start = np.array([np.sum(P0 * C) for C in (X, Y, Z)])
    vexp = 2 * np.sin(th)                       # sites per cycle (A10 S9)
    print(f"L={L} B={B} T={T} cycles, theta={th}, q0={q0} along n={np.round(nhat,3)}, cut={cut}, g={g}/cycle; "
          f"cone speed 2 sin(theta) = {vexp:.4f} sites/cycle")
    EXP = [np.exp(2j * PI * C / L) for C in (X, Y, Z)]

    def centroid(Pb):                           # circular mean per axis, (b, 3)
        return np.stack([np.angle(np.einsum("bxyz,xyz->b", Pb, E)) * L / (2 * PI) for E in EXP], -1)

    def mi(d):                                  # minimal image
        return ((d + L / 2) % L) - L / 2

    tracks, cen_tracks = [], []
    t0 = time.time()
    Bb = 8                                      # mini-batch (memory budget)
    for b0 in range(0, B, Bb):
        nb = min(Bb, B - b0)
        psi = np.repeat(psi0[None], nb, 0)
        cen_raw = np.repeat(start[None], nb, 0); cen_unw = cen_raw.copy()
        trk = [[(0, start.copy())] for _ in range(nb)]
        for t in range(1, T + 1):
            psi = run_cycle(psi, lay, ETA)
            c = centroid(np.abs(psi) ** 2)
            cen_unw = cen_unw + mi(c - cen_raw); cen_raw = c
            if cut == "none":
                continue
            for i in np.nonzero(rng.random(nb) < g)[0]:
                P = np.abs(psi[i]).ravel() ** 2
                P /= P.sum()
                k = min(np.searchsorted(np.cumsum(P), rng.random()), P.size - 1)
                x = np.array(np.unravel_index(k, (L, L, L)))
                xi = np.array([zk[min(np.searchsorted(cwk, rng.random()), zk.size - 1)] for _ in range(3)])
                y = (x + xi) % L
                if sig <= 0:
                    new = np.zeros((L, L, L), complex); new[tuple(y)] = psi[i][tuple(y)]
                else:
                    fac = []
                    for ax in range(3):
                        d = mi(np.arange(L) - y[ax]).astype(int)
                        f = np.zeros(L); ok = np.abs(d) <= zk[-1]
                        f[ok] = swk[d[ok] + zk[-1]]
                        fac.append(f)
                    new = psi[i] * fac[0][:, None, None] * fac[1][None, :, None] * fac[2][None, None, :]
                psi[i] = new / np.linalg.norm(new)
                y_unw = cen_unw[i] + mi(y - cen_raw[i])          # record unwrapped against the mover's centroid
                trk[i].append((t, y_unw.copy()))
                cnew = centroid((np.abs(psi[i]) ** 2)[None])[0]
                cen_unw[i] = y_unw + mi(cnew - y); cen_raw[i] = cnew
        tracks += trk
        cen_tracks += list(cen_unw)
    el = time.time() - t0
    cen_tracks = np.array(cen_tracks)
    dc = cen_tracks - start
    cosc = dc @ nhat / np.linalg.norm(dc, axis=1)
    if cut == "none":
        v = dc[0] / T
        print(f"no registration: centroid velocity {np.round(v,4)} |v| = {np.linalg.norm(v):.4f} sites/cycle, "
              f"cos(v,n) = {v @ nhat / np.linalg.norm(v):.4f}   ({el:.1f} s)")
        return
    pcacos, straight, vpar, perp, nrec = [], [], [], [], []
    for tr in tracks:
        pts = np.array([p[1] for p in tr]); tt = np.array([p[0] for p in tr], float)
        nrec.append(len(tr) - 1)
        if len(tr) < 3:
            continue
        disp = pts[-1] - pts[0]
        cpts = pts - pts.mean(0)
        ev, evec = np.linalg.eigh(cpts.T @ cpts)
        straight.append(ev[-1] / ev.sum())
        axv = evec[:, -1] * (np.sign(evec[:, -1] @ disp) or 1.0)
        pcacos.append(axv @ nhat)
        proj = (pts - pts[0]) @ nhat
        vpar.append(np.polyfit(tt, proj, 1)[0])
        tr_perp = (pts - pts[0]) - np.outer(proj, nhat)
        perp.append(np.sqrt(np.mean(np.sum(tr_perp ** 2, 1))))
    pcacos, straight, vpar, perp = map(np.array, (pcacos, straight, vpar, perp))
    print(f"records per track {np.mean(nrec):.1f}; tracks with >= 2 records {pcacos.size}/{B}")
    print(f"  record track: principal axis (time-oriented) mean cos(axis, n) = {pcacos.mean():+.3f} (sd {pcacos.std():.3f}), "
          f"fraction > 0.9 = {np.mean(pcacos > 0.9):.2f}; straightness lambda1/sum = {straight.mean():.3f} (line 1, cloud 1/3)")
    print(f"  speed along n (LS slope of record projection) = {vpar.mean():.3f} +- {vpar.std()/np.sqrt(vpar.size):.3f} sites/cycle "
          f"(cone {vexp:.3f}); transverse rms of records {perp.mean():.2f} sites")
    print(f"  [unreadable cross-check] mover centroid: mean cos(displacement, n) = {cosc.mean():+.3f}, "
          f"mean |displacement|/T = {np.mean(np.linalg.norm(dc, axis=1))/T:.3f}   ({el:.1f} s)")


if __name__ == "__main__":
    main()
