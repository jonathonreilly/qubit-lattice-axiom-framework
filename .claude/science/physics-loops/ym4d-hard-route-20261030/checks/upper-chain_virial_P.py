#!/usr/bin/env python3
"""Exact linear-algebra check of the operator P' of Theorem 18.3, and of Lemma 18.5.

Model: lattice of the map of hard-core--independent in d = 2, odd L, N blocks per side, torus side N L.
Straight contour Q_str with tri weights (Lemma 4.5a there), optional frames R_l in SO(3) on the links
(colour 3 per link), standing in for the Ad of a background. Form H = d^T d at level 0, with frames.

Criteria, fixed before running. All are exact identities up to rounding, tolerance 1e-9, except P5, P6.
 P1  Q P' b = 0 for b in X := ker Q (P' maps X to X), every block.
 P2  sum over blocks of P' = 1 on X.
 P3  Tr_X P' = N', the count of free coordinates of the block, for every block and for frames R = 1
     and for random frames: the same number. FAIL if it depends on the frames.
 P4  Virial: E <P' b, A b> / g^2 = Tr_X P' under the Gaussian with form A on X, at g = 1.
 P5  Naive diagonal cut-off, the orthogonal P_o := Pi_X phi Pi_X: Tr depends on the frames. This is the
     reason for P'. Reported, and PASS if the spread is above 1e-3 for the random frames.
     First run: FAIL, spread 1e-14, but that test was vacuous: a frame per link is a link-wise rotation,
     under which the trace of a link-diagonal cut-off cannot change. In the map the frame belongs to a
     pair (link, bond), since an interior link lies in two bonds with different paths. P5 and P3 for
     random frames are re-registered with frames per (link, bond), criteria unchanged, before this rerun.
     The form H stays flat in that rerun; it enters only P4, which holds for any A.
 P6  Lemma 18.5, frames = 1: max |CC_inf - CC_c|(x, x') at L = 3, 5, 7, curvature covariance on the
     fibre against the unconstrained one. Reported with L^2 max; PASS if L^2 max is bounded,
     non-increasing from L = 5 to L = 7, which is what the lemma claims (it claims no more).
 P7  Gauge term, frames = 1: tau E |rho|^2_{c'} / g^2 = L^d - 1 for every block.

Usage: upper-chain_virial_P.py
"""
import os
import resource
import sys

os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
import numpy as np

RSS_LIMIT_KB = 2 * 1024 * 1024


def check_rss():
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if sys.platform == "darwin":
        rss = rss // 1024
    if rss > RSS_LIMIT_KB:
        sys.exit("RSS limit exceeded")


class Lat:
    def __init__(self, L, N, colour=1, seed=None, frame_size=0.0):
        self.L, self.N, self.T = L, N, L * N
        self.nl = 2 * self.T ** 2
        self.colour = colour
        rng = np.random.default_rng(seed)
        self.R = [np.eye(colour) for _ in range(self.nl)]
        self.rng = rng
        self.frame_size = 0.0 if seed is None else frame_size
        self._rb = {}

    def rb(self, l, i):
        """Frame of link l in bond i."""
        if self.frame_size == 0.0:
            return np.eye(self.colour)
        if (l, i) not in self._rb:
            w = self.frame_size * self.rng.normal(size=3)
            n = np.linalg.norm(w)
            K = np.array([[0, -w[2], w[1]], [w[2], 0, -w[0]], [-w[1], w[0], 0]])
            self._rb[(l, i)] = np.eye(3) + np.sin(n) / n * K + (1 - np.cos(n)) / n ** 2 * K @ K
        return self._rb[(l, i)]

    def link(self, x, y, mu):
        return (x % self.T + self.T * (y % self.T)) * 2 + mu

    def site(self, x, y):
        return x % self.T + self.T * (y % self.T)

    def block_of(self, x, y):
        # blocks are centred on multiples of L, x in [-(L-1)/2, (L-1)/2] around the centre
        h = (self.L - 1) // 2
        return ((x + h) // self.L) % self.N, ((y + h) // self.L) % self.N


def build(lat):
    """Return bonds with their weights: for each block (bx, by) and mu, the bond to the next block along mu."""
    L, N, T = lat.L, lat.N, lat.T
    h = (L - 1) // 2
    bonds = []
    for bx in range(N):
        for by in range(N):
            for mu in range(2):
                weights = {}
                crossing = []
                cx, cy = bx * L, by * L
                for tr in range(-h, h + 1):  # transverse line within the block section
                    for t in range(-(L - 1), L):  # t = 0 is the crossing link
                        tri = 1 - abs(t) / L
                        # link along mu with midpoint at offset t from the face between the two blocks
                        s = (h if True else 0) + t  # site below the link, measured from the first centre
                        if mu == 0:
                            l = lat.link(cx + s, cy + tr, 0)
                        else:
                            l = lat.link(cx + tr, cy + s, 1)
                        weights[l] = tri / L
                        if t == 0:
                            crossing.append(l)
                bonds.append(dict(block=(bx, by), mu=mu, w=weights, crossing=crossing))
    return bonds


def assemble_Q(lat, bonds):
    c = lat.colour
    Q = np.zeros((len(bonds) * c, lat.nl * c))
    for i, bo in enumerate(bonds):
        for l, q in bo["w"].items():
            Q[i * c : (i + 1) * c, l * c : (l + 1) * c] += q * lat.rb(l, i)
    return Q


def assemble_d(lat):
    """Curvature d on plaquettes, abelian form, on links with colour; frames rotate the variable into a common frame."""
    T, c = lat.T, lat.colour
    d = np.zeros((T * T * c, lat.nl * c))
    for x in range(T):
        for y in range(T):
            p = lat.site(x, y)
            for (l, s) in [(lat.link(x, y, 0), 1), (lat.link(x + 1, y, 1), 1), (lat.link(x, y + 1, 0), -1), (lat.link(x, y, 1), -1)]:
                d[p * c : (p + 1) * c, l * c : (l + 1) * c] += s * lat.R[l]
    return d


def assemble_grad(lat):
    T, c = lat.T, lat.colour
    G = np.zeros((lat.nl * c, T * T * c))
    for x in range(T):
        for y in range(T):
            s = lat.site(x, y)
            for mu, (xn, yn) in enumerate([(x + 1, y), (x, y + 1)]):
                l = lat.link(x, y, mu)
                G[l * c : (l + 1) * c, lat.site(xn, yn) * c : (lat.site(xn, yn) + 1) * c] += lat.R[l].T
                G[l * c : (l + 1) * c, s * c : (s + 1) * c] -= lat.R[l].T
    return G


def free_coords(lat, bonds):
    """Matrix T: free coordinates -> links, with Q T = 0, and the block of each free coordinate.

    Free coordinates: frame-rotated values of links that are not crossing, and on each bond, with its
    crossing links u, the zero-mean combinations of R_u b_u. The mean is fixed by the constraint.
    """
    c, nl = lat.colour, lat.nl
    crossing_of = {}
    for i, bo in enumerate(bonds):
        for l in bo["crossing"]:
            crossing_of[l] = i
    free = []  # (kind, data, block)
    h = (lat.L - 1) // 2
    T_ = lat.T
    for l in range(nl):
        if l in crossing_of:
            continue
        site, mu = l // 2, l % 2
        x, y = site % T_, site // T_
        free.append(("int", l, lat.block_of(x, y)))
    for i, bo in enumerate(bonds):
        n = len(bo["crossing"])
        # orthonormal zero-sum basis on the crossing links
        M = np.eye(n) - np.ones((n, n)) / n
        U, S, _ = np.linalg.svd(M)
        for k in range(n - 1):
            free.append(("cross", (i, U[:, k]), bo["block"]))
    Tm = np.zeros((nl * c, len(free) * c))
    blocks = []
    for f, (kind, data, blk) in enumerate(free):
        blocks.append(blk)
        for a in range(c):
            e = np.zeros(c)
            e[a] = 1.0
            col = np.zeros(nl * c)
            if kind == "int":
                l = data
                col[l * c : (l + 1) * c] = e  # the free coordinate is the link value
                # effect on the mean of crossing links of the bonds that use l
                for i, bo in enumerate(bonds):
                    q = bo["w"].get(l)
                    if q is None or q == 0:
                        continue
                    n = len(bo["crossing"])
                    # sum_u (1/n) R_u b_u = - sum_int q R_l b_l
                    for u in bo["crossing"]:
                        col[u * c : (u + 1) * c] += lat.rb(u, i).T @ (-q * lat.rb(l, i) @ e)
            else:
                i, vec = data
                for u, v in zip(bonds[i]["crossing"], vec):
                    col[u * c : (u + 1) * c] += lat.rb(u, i).T @ (v * e)
            Tm[:, f * c + a] = col
    return Tm, blocks


def run(L, N, colour, seed, frame_size, tol, label):
    lat = Lat(L, N, colour, seed, frame_size)
    bonds = build(lat)
    Q = assemble_Q(lat, bonds)
    Tm, blocks = free_coords(lat, bonds)
    res = np.abs(Q @ Tm).max()
    out = {"Q T residual": res}
    # coordinates on X
    Tp = np.linalg.pinv(Tm)
    uniq = sorted(set(blocks))
    c = colour
    Ps = {}
    for b in uniq:
        mask = np.zeros(Tm.shape[1])
        for f, bl in enumerate(blocks):
            if bl == b:
                mask[f * c : (f + 1) * c] = 1.0
        Ps[b] = Tm @ np.diag(mask) @ Tp
    # orthonormal basis of X
    U, S, _ = np.linalg.svd(Tm, full_matrices=False)
    Xb = U[:, S > 1e-10]
    out["dim X"] = Xb.shape[1]
    out["dim free"] = Tm.shape[1]
    P1 = max(np.abs(Q @ Ps[b] @ Xb).max() for b in uniq)
    Psum = sum(Ps.values())
    P2 = np.abs(Psum @ Xb - Xb).max()
    traces = {b: np.trace(Xb.T @ Ps[b] @ Xb) for b in uniq}
    counts = {b: c * sum(1 for bl in blocks if bl == b) for b in uniq}
    P3 = max(abs(traces[b] - counts[b]) for b in uniq)
    # form
    d = assemble_d(lat)
    G = assemble_grad(lat)
    T2 = lat.T ** 2
    # zero block average projector on sites
    Pi0 = np.eye(T2 * c)
    h = (L - 1) // 2
    site_block = {}
    for x in range(lat.T):
        for y in range(lat.T):
            site_block[lat.site(x, y)] = lat.block_of(x, y)
    for b in uniq:
        idx = [s for s, bl in site_block.items() if bl == b]
        vec = np.zeros(T2)
        vec[idx] = 1.0 / np.sqrt(len(idx))
        for a in range(c):
            v = np.zeros(T2 * c)
            v[a::c] = vec
            Pi0 -= np.outer(v, v)
    tau = 1.0
    H0 = d.T @ d + tau * G @ Pi0 @ G.T
    A = Xb.T @ H0 @ Xb
    ev = np.linalg.eigvalsh(A)
    out["lambda_min(A)"] = ev[0]
    Ainv = np.linalg.inv(A)
    # P4: E <P' b, A b> with b = Xb z, z ~ N(0, Ainv), A acting as H0
    P4 = 0.0
    for b in uniq:
        val = np.trace(Xb.T @ Ps[b].T @ H0 @ Xb @ Ainv)
        P4 = max(P4, abs(val - traces[b]))
    # P5: orthogonal cut-off, same block indicator on links
    tr_o = {}
    for b in uniq:
        link_mask = np.zeros(lat.nl * c)
        for l in range(lat.nl):
            site = l // 2
            x, y = site % lat.T, site // lat.T
            if lat.block_of(x, y) == b:
                link_mask[l * c : (l + 1) * c] = 1.0
        tr_o[b] = np.trace(Xb.T @ np.diag(link_mask) @ Xb)
    out.update(P1=P1, P2=P2, P3=P3, P4=P4)
    out["traces"] = sorted(set(round(v, 6) for v in traces.values()))
    out["orth traces"] = [round(tr_o[b], 4) for b in uniq]
    # P7
    if frame_size == 0.0:
        P7 = 0.0
        for b in uniq:
            idx = [s for s, bl in site_block.items() if bl == b]
            sel = np.zeros(T2 * c)
            for s in idx:
                sel[s * c : (s + 1) * c] = 1.0
            rho_op = np.diag(sel) @ Pi0 @ G.T
            val = tau * np.trace(Xb.T @ rho_op.T @ rho_op @ Xb @ Ainv)
            P7 = max(P7, abs(val - c * (L ** 2 - 1)))
        out["P7"] = P7
    check_rss()
    print(label, {k: (float(v) if isinstance(v, (float, np.floating)) else v) for k, v in out.items()})
    ok = P1 < tol and P2 < tol and P3 < tol and P4 < tol and (frame_size != 0.0 or out["P7"] < tol)
    return ok, tr_o


def lemma_18_5(L, N=3):
    """Curvature covariance on the fibre over W = 1 against the unconstrained one, abelian, Fourier-free."""
    lat = Lat(L, N, 1)
    T = lat.T
    d = assemble_d(lat)
    G = assemble_grad(lat)
    bonds = build(lat)
    Q = assemble_Q(lat, bonds)
    # coarse curvature Z = d' Q on the coarse torus
    nb = N * N
    def bond_index(bx, by, mu):
        return ((bx % N) + N * (by % N)) * 2 + mu
    index = {}
    for i, bo in enumerate(bonds):
        index[(bo["block"][0], bo["block"][1], bo["mu"])] = i
    dp = np.zeros((nb, len(bonds)))
    for bx in range(N):
        for by in range(N):
            p = (bx) + N * (by)
            dp[p, index[(bx, by, 0)]] += 1
            dp[p, index[((bx + 1) % N, by, 1)]] += 1
            dp[p, index[(bx, (by + 1) % N, 0)]] -= 1
            dp[p, index[(bx, by, 1)]] -= 1
    Z = dp @ Q
    H = d.T @ d + G @ G.T
    Cinf = np.linalg.pinv(H, rcond=1e-10)
    CCinf = d @ Cinf @ d.T
    G_ = Z @ Cinf @ d.T
    ZCZ = Z @ Cinf @ Z.T
    Diff = G_.T @ np.linalg.pinv(ZCZ, rcond=1e-10) @ G_
    check_rss()
    return np.abs(Diff).max(), np.abs(CCinf).max()


def main():
    results = []
    ok, tr1 = run(3, 2, 1, None, 0.0, 1e-9, "L=3 N=2 abelian")
    results.append(ok)
    ok, tr2 = run(3, 2, 3, None, 0.0, 1e-9, "L=3 N=2 colour flat")
    results.append(ok)
    ok, tr3 = run(3, 2, 3, 1, 0.4, 1e-9, "L=3 N=2 colour frames")
    results.append(ok)
    ok, tr4 = run(5, 2, 1, None, 0.0, 1e-9, "L=5 N=2 abelian")
    results.append(ok)
    spread = max(abs(tr3[b] - tr2[b]) for b in tr3)
    print("PASS-P1-P4,P7" if all(results) else "FAIL-P1-P4,P7", results)
    print("P5 spread of the orthogonal trace between frames and flat:", spread, "PASS" if spread > 1e-3 else "FAIL")
    vals = []
    for L in (3, 5, 7):
        m, base = lemma_18_5(L)
        vals.append(L * L * m)
        print(f"P6 L={L}: max|CC_inf - CC_c| = {m:.6g}, L^2 max = {L*L*m:.4g}, L^4 max = {L**4*m:.4g}, max|CC_inf| = {base:.4g}")
    print("P6", "PASS" if vals[2] <= vals[1] else "FAIL")


if __name__ == "__main__":
    main()
