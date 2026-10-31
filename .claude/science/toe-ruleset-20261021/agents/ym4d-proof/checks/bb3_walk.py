"""bb3: algebra of BFT_B.md Theorem RW^nabla_k / Construction BB-bond_k on a model local operator.

Criteria: checks/bb3_criteria.md (written before this script).  d = 2 torus, scalar site fields,
L = -Laplacian + mu^2.  Tests identities, supports and class splitting only (no k-uniformity, no lane-A norm).
"""
import sys
import time
import numpy as np

T0 = time.time()


def lap_matrix(n, mu2):
    """Dense -Delta + mu2 on the n x n torus (5-point), site index x*n + y."""
    N = n * n
    A = np.zeros((N, N))
    for x in range(n):
        for y in range(n):
            i = x * n + y
            A[i, i] = 4.0 + mu2
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                j = ((x + dx) % n) * n + (y + dy) % n
                A[i, j] -= 1.0
    return A


def circ_dist(t, a, length, n):
    """l-infinity (1D) distance on the circle of n from site t to the interval [a, a+length)."""
    off = (t - a) % n
    if off < length:
        return 0
    return min(n - off, off - (length - 1))


def partition_1d(n, length, weights):
    """Normalised 1D partition of unity: intervals [a, a+length), weight weights[d] at distance d (0 beyond)."""
    starts = list(range(0, n, length))
    W = np.zeros((len(starts), n))
    for k, a in enumerate(starts):
        for t in range(n):
            d = circ_dist(t, a, length, n)
            if d < len(weights):
                W[k, t] = weights[d]
    W /= W.sum(axis=0, keepdims=True)
    return starts, W


def psi_1d(n, a, length, R):
    out = np.zeros(n)
    for t in range(n):
        d = circ_dist(t, a, length, n)
        out[t] = min(1.0, max(0.0, (R - d) / (R / 2.0)))
    return out


class Model:
    def __init__(self, n, mu2, R, need_cube=True):
        self.n, self.mu2, self.R = n, mu2, R
        self.M = 2 * R
        assert n % self.M == 0
        self.Wt = 3 * R + 8                      # local torus side T_W
        self.o = R + 4                           # local position of the box corner
        self.L = lap_matrix(n, mu2)
        Lloc = lap_matrix(self.Wt, mu2)
        self.Lloc = Lloc
        self.Gloc = np.linalg.inv(Lloc)
        bstarts, chi1 = partition_1d(n, R, [1.0, 0.5])
        self.bstarts = bstarts
        nb = len(bstarts)
        self.boxes = []
        Nn = n * n
        P = np.zeros((Nn, Nn))
        Rm = np.zeros((Nn, Nn))
        W = self.Wt
        for bi, ax in enumerate(bstarts):
            for bj, ay in enumerate(bstarts):
                chi = np.outer(chi1[bi], chi1[bj]).ravel()
                psi = np.outer(psi_1d(n, ax, R, R), psi_1d(n, ay, R, R)).ravel()
                # window: global sites with local coords in [0, W)
                gl = np.full(W * W, -1, dtype=int)
                for lx in range(W):
                    for ly in range(W):
                        gx = (lx - self.o + ax) % n
                        gy = (ly - self.o + ay) % n
                        gl[lx * W + ly] = gx * n + gy
                assert len(set(gl.tolist())) == W * W
                chi_loc = chi[gl]
                psi_loc = psi[gl]
                # supports must lie in the window (check against the global profiles)
                assert abs(chi_loc.sum() - chi.sum()) < 1e-12 and abs(psi_loc.sum() - psi.sum()) < 1e-12
                cols = np.nonzero(chi_loc)[0]
                rowsP = np.nonzero(psi_loc)[0]
                Gc = self.Gloc[:, cols] * chi_loc[cols][None, :]
                Pb = psi_loc[rowsP][:, None] * Gc[rowsP, :]
                Comm = Lloc * psi_loc[None, :] - psi_loc[:, None] * Lloc   # [L, psi] on the local torus
                Rfull = -(Comm @ Gc)
                rowsR = np.nonzero(np.abs(Rfull).sum(axis=1) > 0)[0]
                Rb = Rfull[rowsR, :]
                gP, gR, gc = gl[rowsP], gl[rowsR], gl[cols]
                P[np.ix_(gP, gc)] += Pb
                Rm[np.ix_(gR, gc)] += Rb
                q = (ax // self.M, ay // self.M)
                self.boxes.append(dict(cols=gc, rowsP=gP, rowsR=gR, Pb=Pb, Rb=Rb, cube=q, corner=(ax, ay),
                                       rowsR_local=rowsR))
        self.P, self.Rm = P, Rm
        if need_cube:
            cstarts, eta1 = partition_1d(n, self.M, [1.0, 2.0 / 3.0, 1.0 / 3.0])
            nc = len(cstarts)
            self.nc = nc
            self.cubes = [(ci, cj) for ci in range(nc) for cj in range(nc)]
            self.cid = {q: k for k, q in enumerate(self.cubes)}
            self.eta = np.array([np.outer(eta1[ci], eta1[cj]).ravel() for (ci, cj) in self.cubes])
            assert np.allclose(self.eta.sum(axis=0), 1.0)
            # cube membership of sites
            self.site_cube = np.array([self.cid[((i // n) // self.M, (i % n) // self.M)] for i in range(Nn)])
            # Q^{(2)} masks
            self.cube_mask2 = np.zeros((nc * nc, Nn), dtype=bool)
            for k, (ci, cj) in enumerate(self.cubes):
                for i in range(Nn):
                    x, y = divmod(i, n)
                    if circ_dist(x, ci * self.M, self.M, n) <= 2 and circ_dist(y, cj * self.M, self.M, n) <= 2:
                        self.cube_mask2[k, i] = True

    def adjacent(self, q1, q2):
        nc = self.nc
        dx = min((q1[0] - q2[0]) % nc, (q2[0] - q1[0]) % nc)
        dy = min((q1[1] - q2[1]) % nc, (q2[1] - q1[1]) % nc)
        return max(dx, dy) <= 1

    def smatrix(self, bondval):
        """bondval: dict frozenset({k1,k2}) -> complex for *-adjacent distinct cubes."""
        nq = len(self.cubes)
        S = np.zeros((nq, nq), dtype=complex)
        for k in range(nq):
            S[k, k] = 1.0
        for b, v in bondval.items():
            k1, k2 = tuple(b)
            S[k1, k2] = v
            S[k2, k1] = v
        return S

    def bonds(self):
        out = []
        nq = len(self.cubes)
        for k1 in range(nq):
            for k2 in range(k1 + 1, nq):
                if self.adjacent(self.cubes[k1], self.cubes[k2]):
                    out.append(frozenset((k1, k2)))
        return out

    # cube-weighted operators
    def opI(self, S, ycub):
        return S @ ycub

    def opR(self, S, z):
        out = np.zeros_like(z)
        for b in self.boxes:
            qb = self.cid[b['cube']]
            v = b['Rb'] @ z[qb, b['cols']]
            for qp in np.nonzero(S[:, qb])[0]:
                out[qp, b['rowsR']] += S[qp, qb] * v
        return out

    def opP(self, S, z):
        out = np.zeros_like(z)
        for b in self.boxes:
            qb = self.cid[b['cube']]
            v = b['Pb'] @ z[qb, b['cols']]
            for qp in np.nonzero(S[:, qb])[0]:
                out[qp, b['rowsP']] += S[qp, qb] * v
        return out * self.eta

    def opK(self, S, ycub, maxit=2000):
        z0 = self.opI(S, ycub)
        tot = z0.copy()
        term = z0
        scale = max(np.abs(z0).max(), 1e-300)
        for it in range(maxit):
            term = self.opR(S, term)
            tot += term
            if np.abs(term).max() <= 1e-15 * scale:
                return self.opP(S, tot), it + 1, True
        return self.opP(S, tot), maxit, False


def main():
    out = []

    def say(s):
        out.append(s)
        print(s)
        sys.stdout.flush()

    rng = np.random.default_rng(1)
    n, mu2, R, c = 48, 2.0, 4, 1.0
    m = Model(n, mu2, R)
    Nn = n * n
    say(f"bb3 model: n={n} mu2={mu2} R={R} M_c={m.M} T_W={m.Wt} boxes={len(m.boxes)} cubes={len(m.cubes)} "
        f"setup {time.time() - T0:.1f}s")
    # B3-1
    I = np.eye(Nn)
    d1 = np.abs(m.L @ m.P - (I - m.Rm)).max()
    say(f"B3-1 max|L P - (I - R)| = {d1:.3e}  -> {'PASS' if d1 <= 1e-12 else 'FAIL'}")
    # B3-2
    Linv = np.linalg.inv(m.L)
    Rnorm = np.abs(m.Rm).sum(axis=1).max()
    Kexp = m.P @ np.linalg.inv(I - m.Rm)
    d2 = np.abs(Kexp - Linv).max() / np.abs(Linv).max()
    ok2 = (d2 <= 1e-10) and (Rnorm < 1)
    say(f"B3-2 rel max|P(I-R)^-1 - L^-1| = {d2:.3e}, ||R||_inf = {Rnorm:.4f}  -> {'PASS' if ok2 else 'FAIL'}")
    # B3-3
    nq = len(m.cubes)
    S1 = m.smatrix({b: 1.0 for b in m.bonds()})
    ycub = (rng.standard_normal((nq, Nn)) + 1j * rng.standard_normal((nq, Nn))) * m.cube_mask2
    Ky, its, conv = m.opK(S1, ycub)
    ref = Linv @ ycub.sum(axis=0)
    d3 = np.abs(Ky.sum(axis=0) - ref).max() / np.abs(ref).max()
    ok3 = conv and d3 <= 1e-10
    say(f"B3-3 s=1 identity rel err = {d3:.3e} (Neumann its {its}, converged {conv})  -> {'PASS' if ok3 else 'FAIL'}")
    # B3-4
    classA = [k for k, q in enumerate(m.cubes) if q[0] in (0, 1, 2)]
    inA = np.zeros(nq, dtype=bool)
    inA[classA] = True
    ssp = min(1.5, 0.5 / Rnorm)
    bonds = m.bonds()

    def rand_s(scale):
        r = scale * np.sqrt(rng.uniform(0, 1))
        return r * np.exp(2j * np.pi * rng.uniform())

    bv = {}
    for b in bonds:
        k1, k2 = tuple(b)
        bv[b] = rand_s(ssp) if inA[k1] == inA[k2] else 0.0
    Ssp = m.smatrix(bv)
    K0, i0, c0 = m.opK(Ssp, ycub)
    y2 = ycub.copy()
    fresh = (rng.standard_normal((nq, Nn)) + 1j * rng.standard_normal((nq, Nn))) * m.cube_mask2
    y2[~inA] = fresh[~inA]
    K1, i1, c1 = m.opK(Ssp, y2)
    bv2 = dict(bv)
    for b in bonds:
        k1, k2 = tuple(b)
        if (not inA[k1]) and (not inA[k2]):
            bv2[b] = rand_s(ssp)
    K2, i2, c2 = m.opK(m.smatrix(bv2), ycub)
    scaleA = np.abs(K0[inA]).max()
    chA1 = np.abs(K1[inA] - K0[inA]).max() / scaleA
    chA2 = np.abs(K2[inA] - K0[inA]).max() / scaleA
    chB1 = np.abs(K1[~inA] - K0[~inA]).max() / np.abs(K0[~inA]).max()
    ok4 = c0 and c1 and c2 and chA1 <= 1e-12 and chA2 <= 1e-12 and chB1 >= 1e-6
    say(f"B3-4 split (s_sp={ssp:.3f}): class-A change (i) {chA1:.3e}, (ii) {chA2:.3e}; control class-B change "
        f"{chB1:.3e}  -> {'PASS' if ok4 else 'FAIL'}")
    # nonlinear model
    g = np.random.default_rng(0).uniform(-0.05, 0.05, Nn)   # data source, seed 0 (criteria)

    def Nl(x):
        return c * x ** 3

    x = np.zeros(Nn)
    for it in range(200):
        xn = -Linv @ (g + Nl(x))
        inc = np.abs(xn - x).max()
        x = xn
        if inc <= 1e-15 * max(np.abs(x).max(), 1e-300):
            break

    def enlarged_fp(S, gcopies):
        A = np.zeros((nq, Nn), dtype=complex)
        for it in range(200):
            V = S @ A
            ycur = m.eta * (gcopies + Nl(V))
            KA, _, cv = m.opK(S, ycur)
            An = -KA
            inc = np.abs(An - A).max()
            A = An
            if not cv:
                return A, False
            if inc <= 1e-15 * max(np.abs(A).max(), 1e-300):
                return A, True
        return A, False

    gc = np.tile(g, (nq, 1)).astype(complex)
    A1, cvA = enlarged_fp(S1, gc)
    d5 = np.abs(A1.sum(axis=0) - x).max() / np.abs(x).max()
    ok5 = cvA and d5 <= 1e-10
    say(f"B3-5 enlarged fixed point vs global: rel err = {d5:.3e} (converged {cvA})  -> {'PASS' if ok5 else 'FAIL'}")

    def Dfun(i, u, gvec):
        Lu_i = m.L[i] @ u
        return 0.5 * u[i] * Lu_i + gvec[i] * u[i] + 0.25 * c * u[i] ** 4

    def gradD_dot(i, u, gvec):
        # grad D_i(u) . u, from d/du_j [1/2 u_i (Lu)_i] = 1/2 (delta_ij (Lu)_i + u_i L_ij)
        Lu_i = m.L[i] @ u
        return 0.5 * Lu_i * u[i] + 0.5 * u[i] * (m.L[i] @ u) + gvec[i] * u[i] + c * u[i] ** 4

    def trap_defect(i, u, gvec):
        zero = np.zeros_like(u)
        return Dfun(i, u, gvec) - Dfun(i, zero, gvec) - 0.5 * (gvec[i] * u[i] + gradD_dot(i, u, gvec))

    def cube_energy(S, A, gcopies):
        V = S @ A
        Es = np.zeros(nq, dtype=complex)
        for k in range(nq):
            v = V[k]
            gk = gcopies[k]
            e = 0.5 * np.sum(m.eta[k] * gk * v)
            for i in np.nonzero(m.site_cube == k)[0]:
                e += trap_defect(i, v, gk)
            Es[k] = e
        return Es

    E1 = cube_energy(S1, A1, gc)
    Ex = 0.5 * x @ (m.L @ x) + g @ x + 0.25 * c * np.sum(x ** 4)
    d6 = abs(E1.sum() - Ex) / abs(Ex)
    say(f"B3-6 energy identity: sum_Q E_Q(1) = {E1.sum().real:.12e}, E(x)-E(0) = {Ex:.12e}, rel {d6:.3e}  -> "
        f"{'PASS' if d6 <= 1e-10 else 'FAIL'}")
    # B3-7
    As, cvs = enlarged_fp(Ssp, gc)
    Es0 = cube_energy(Ssp, As, gc)
    gp = np.random.default_rng(7).uniform(-0.05, 0.05, Nn)
    gc2 = gc.copy()
    gc2[~inA] = gp
    As2, cvs2 = enlarged_fp(Ssp, gc2)
    Es1 = cube_energy(Ssp, As2, gc2)
    As3, cvs3 = enlarged_fp(m.smatrix(bv2), gc)
    Es2 = cube_energy(m.smatrix(bv2), As3, gc)
    EA0 = Es0[inA].sum()
    c71 = abs(Es1[inA].sum() - EA0) / abs(EA0)
    c72 = abs(Es2[inA].sum() - EA0) / abs(EA0)
    cB = abs(Es1[~inA].sum() - Es0[~inA].sum()) / abs(Es0[~inA].sum())
    ok7 = cvs and cvs2 and cvs3 and c71 <= 1e-12 and c72 <= 1e-12 and cB >= 1e-8
    say(f"B3-7 energy split: class-A change (i) {c71:.3e}, (ii) {c72:.3e}; control class-B change {cB:.3e}  -> "
        f"{'PASS' if ok7 else 'FAIL'}")
    say("VERDICT: " + ("ALL PASS" if all([d1 <= 1e-12, ok2, ok3, ok4, ok5, d6 <= 1e-10, ok7]) else "SOME FAIL"))
    say(f"time after verdicts {time.time() - T0:.1f}s")
    # informational
    for mu2i in (1.0, 2.0):
        for Ri in (4, 6, 8):
            mi = Model(48, mu2i, Ri, need_cube=False)
            rn = np.abs(mi.Rm).sum(axis=1).max()
            say(f"INFO mu2={mu2i} R={Ri}: ||R||_inf = {rn:.4e}, R*||R||_inf = {Ri * rn:.4e}")
    say(f"total time {time.time() - T0:.1f}s")


if __name__ == "__main__":
    main()
