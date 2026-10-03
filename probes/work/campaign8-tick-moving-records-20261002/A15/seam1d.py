#!/usr/bin/env python3
"""A15 task 1 (1D): phase-mismatch seams for the A10 alternating-pairing cycle, one excitation.

Supplied toy (nothing adopted). Sites 0..N-1. Gate on a pair = exp(-i th SWAP); relative to the empty pair its
one-excitation block is u = e^{i th}(cos th - i sin th sigma_x); an idle site is the identity.
Rigid local clocks: site x has a fixed schedule phase phi(x) in Z_2; at sub-step t it selects partner
x+1 if (t+phi(x)) = x (mod 2), else x-1  (phase 0: even layer first, as in A10).
Region A = x < s has phi = 0; region B = x >= s has phi = 1 (offset by one sub-step).
Seam rules (all act identically away from the seam):
  H   handshake: a pair acts iff both sites' clocks select it
  K   conflict-skip: candidate pairs = selected by >= 1 site; candidates sharing a site with another are skipped
  P   request-priority: a one-sided request wins over the agreed pair it conflicts with
  Smu sequential: agreed pairs, then one-sided requests (two gates on the seam site in one sub-step)
  Sum sequential: one-sided requests, then agreed pairs
  R   random arbitration: H or P with odds 1/2 each (density-matrix average)
Measured: transmitted / reflected / seam-stuck weight of a right-moving packet sent from A (and a left-moving
packet from B), and the maximum one-sub-step jump (strict-cone check)."""
import os, signal
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[_v] = "1"
signal.alarm(55)
import numpy as np

def ublock(th):
    c, s = np.cos(th), np.sin(th)
    return np.exp(1j * th) * np.array([[c, -1j * s], [-1j * s, c]])

def selections(N, phi, t):
    sel = np.empty(N, int)
    for x in range(N):
        if (t + phi[x]) % 2 == x % 2:
            sel[x] = x + 1 if x + 1 < N else -1
        else:
            sel[x] = x - 1 if x - 1 >= 0 else -1
    return sel

def pairs_for(N, phi, t, rule):
    """Return list of (prob, [layer, layer, ...]); a layer is a list of disjoint bonds (x, x+1)."""
    sel = selections(N, phi, t)
    mutual, onesided = [], []
    for x in range(N - 1):
        a, b = sel[x] == x + 1, sel[x + 1] == x
        if a and b:
            mutual.append((x, x + 1))
        elif a or b:
            onesided.append((x, x + 1))
    def sites(bs):
        out = {}
        for (x, y) in bs:
            out[x] = out.get(x, 0) + 1
            out[y] = out.get(y, 0) + 1
        return out
    if rule == 'H':
        return [(1.0, [mutual])]
    if rule == 'K':
        cand = mutual + onesided
        cnt = sites(cand)
        return [(1.0, [[b for b in cand if cnt[b[0]] == 1 and cnt[b[1]] == 1]])]
    if rule == 'P':
        busy = set()
        for (x, y) in onesided:
            busy |= {x, y}
        return [(1.0, [onesided + [b for b in mutual if b[0] not in busy and b[1] not in busy]])]
    if rule == 'Smu':
        return [(1.0, [mutual, onesided])]
    if rule == 'Sum':
        return [(1.0, [onesided, mutual])]
    if rule == 'R':
        return [(0.5, pairs_for(N, phi, t, 'H')[0][1]), (0.5, pairs_for(N, phi, t, 'P')[0][1])]
    raise ValueError(rule)

def compile_layers(layers):
    out = []
    for layer in layers:
        if layer:
            xs = np.array([b[0] for b in layer]); ys = np.array([b[1] for b in layer])
            out.append((xs, ys))
    return out

def apply(layers, u, A, conj=False):
    """apply the layers to the rows of A (vector or matrix); conj=True applies to columns as A U^dagger."""
    A = A.copy()
    for xs, ys in layers:
        if not conj:
            ax, ay = A[xs].copy(), A[ys].copy()
            A[xs] = u[0, 0] * ax + u[0, 1] * ay
            A[ys] = u[1, 0] * ax + u[1, 1] * ay
        else:
            ax, ay = A[:, xs].copy(), A[:, ys].copy()
            uc = u.conj()
            A[:, xs] = uc[0, 0] * ax + uc[0, 1] * ay
            A[:, ys] = uc[1, 0] * ax + uc[1, 1] * ay
    return A

def maxjump_of(layers):
    # reach of one sub-step: a site touched by k sequential gates can move up to k sites
    reach = {}
    for xs, ys in layers:
        for x, y in zip(xs, ys):
            r = max(reach.get(x, 0), reach.get(y, 0)) + 1
            reach[x] = reach[y] = r
    return max(reach.values()) if reach else 0

def bloch_W(K, u):
    we = u
    wo = np.array([[u[1, 1], u[1, 0] * np.exp(-1j * K)], [u[0, 1] * np.exp(1j * K), u[0, 0]]])
    return wo @ we

def branch(K, u, sign):
    """eigenvector of W(K) on the branch whose group velocity has the given sign; W v = e^{-i w} v."""
    dK = 1e-5
    def eig(KK):
        ev, V = np.linalg.eig(bloch_W(KK, u))
        w = -np.angle(ev)
        return w, V
    w0, V0 = eig(K)
    w1, _ = eig(K + dK)
    out = []
    for i in range(2):
        j = np.argmin(np.abs(np.angle(np.exp(1j * (w1 - w0[i])))))
        vg = np.angle(np.exp(1j * (w1[j] - w0[i]))) / dK
        out.append((vg, w0[i], V0[:, i]))
    out.sort(key=lambda z: z[0])
    vg, w, v = out[-1] if sign > 0 else out[0]
    ph = v[0] if abs(v[0]) > 1e-8 else v[1]
    return vg, w, v * np.conj(ph) / abs(ph)

def packet(N, center, K0, sigma, u, sign, cell_offset=0):
    M = 512
    Ks = K0 + np.linspace(-4 / sigma, 4 / sigma, M)
    psi = np.zeros(N, complex)
    ncell = N // 2
    n = np.arange(ncell)
    for K in Ks:
        _, _, v = branch(K, u, sign)
        g = np.exp(-(K - K0) ** 2 * sigma ** 2 / 2)
        ph = np.exp(1j * K * (n - center))
        psi[0::2] += g * ph * v[0]
        psi[1::2] += g * ph * v[1]
    return psi / np.linalg.norm(psi)

def run(rule, th, K0, side, N=520, s=260, T=None, sigma=12.0):
    u = ublock(th)
    phi = np.array([0] * s + [1] * (N - s))
    vg, _, _ = branch(K0, u, +1 if side == 'A' else -1)
    # packet in the region's own Bloch frame: region B with phase 1 = region A's pattern shifted by one site
    if side == 'A':
        psi = packet(N, (s // 2) - (4 * sigma + 10), K0, sigma, u, +1)
        psi[s:] = 0
    else:
        # build in B's frame: B at phase 1 equals phase-0 pattern on sites shifted by one
        tmp = packet(N + 2, (s // 2) + (4 * sigma + 10), K0, sigma, u, -1)
        psi = tmp[1:N + 1].copy()   # site x of B frame = site x+1 of phase-0 frame
        psi[:s] = 0
    psi /= np.linalg.norm(psi)
    if T is None:
        T = int(2 * (2 * (4 * sigma + 10)) / max(abs(vg), 0.05)) + 20
        T += T % 2
    cache = {}
    rho = None
    if rule == 'R':
        rho = np.outer(psi, psi.conj())
    maxjump = 0.0
    for t in range(T):
        key = t % 2
        if key not in cache:
            branches = pairs_for(N, phi, t, rule)
            cache[key] = [(p, compile_layers(layers)) for p, layers in branches]
            for p, cl in cache[key]:
                maxjump = max(maxjump, maxjump_of(cl))
        if rule == 'R':
            rho = sum(p * apply(cl, u, apply(cl, u, rho), conj=True) for p, cl in cache[key])
        else:
            psi = apply(cache[key][0][1], u, psi)
    prob = np.real(np.diag(rho)) if rule == 'R' else np.abs(psi) ** 2
    left, right = prob[:s].sum(), prob[s:].sum()
    near = prob[max(0, s - 4):s + 4].sum()
    purity = np.real(np.trace(rho @ rho)) if rule == 'R' else 1.0
    trans = right if side == 'A' else left
    refl = left if side == 'A' else right
    return trans, refl, near, maxjump, T, purity, vg

if __name__ == '__main__':
    print("1D A10 cycle, rigid clocks, phase offset 1 at seam bond (s-1,s), s even (odd seam bond)")
    print("rule  theta   K0    side   T(trans)  R(refl)  stuck(+-4)  maxjump  steps  purity  vg(cells/cycle)")
    for rule in ('H', 'K', 'P', 'Smu', 'Sum', 'R'):
        for th in (np.pi / 2, np.pi / 4, 0.3):
            for K0 in (np.pi / 2 + 0.6, np.pi - 0.4) if th < np.pi / 2 else (np.pi / 2,):
                for side in ('A', 'B'):
                    tr, rf, nr, mj, T, pur, vg = run(rule, th, K0, side)
                    print("%-4s  %.3f  %.3f   %s    %.6f  %.6f  %.2e    %d      %4d   %.3f   %+.3f" %
                          (rule, th, K0, side, tr, rf, nr, mj, T, pur, vg))
