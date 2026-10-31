"""ba5 (BFT lane A, session 5): checks of BFT_A §21 (Lemma PC, Lemma LD, Lemma DUAL, Theorem Y / CO-0R numerics).

Matrix-free linear chain at the trivial background: L = 3, kappa = 1, d = 4, c26 axial template (read-only import of
checks/c26_led.py), general depth k. Energy 1/2|d x_0|^2 + sum_j 1/2|Q_j x_j - x_{j+1}|^2 - sources, x_k = data.
Criteria: checks/ba5_criteria.md (written before this file).  Usage: python3 ba5_y.py PART   (PART in P1 P2 P4 B1)
"""
import itertools
import resource
import sys
import time

import numpy as np

sys.path.insert(0, "/Users/jonreilly/Projects/Physics/.claude/worktrees/peaceful-heisenberg-e2d2a0/.claude/science/"
                   "toe-ruleset-20261021/agents/ym4d-proof/checks")
import c26_led as c26  # noqa: E402

L = c26.L; H = (L - 1) // 2
PLANES = list(itertools.combinations(range(4), 2))
T0 = time.time()


def rss():
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6


TM = []
for _mu in range(4):
    ent = []
    for (z, nu), wv in c26.template(4, _mu).items():
        o = [H + zi for zi in z]
        ent.append((nu, tuple(oi % L for oi in o), tuple(oi // L for oi in o), wv))
    TM.append(ent)


def view8(a, Tc):
    return a.reshape(Tc, L, Tc, L, Tc, L, Tc, L)


def sl(rem):
    return (slice(None), rem[0], slice(None), rem[1], slice(None), rem[2], slice(None), rem[3])


def Qop(x, Tc):
    out = [np.zeros((Tc,) * 4) for _ in range(4)]
    v = [view8(a, Tc) for a in x]
    for mu in range(4):
        acc = out[mu]
        for (nu, rem, q, wv) in TM[mu]:
            acc += wv * np.roll(v[nu][sl(rem)], tuple(-qi for qi in q), axis=(0, 1, 2, 3))
    return out


def QTop(y, Tc):
    M = Tc * L
    out = [np.zeros((M,) * 4) for _ in range(4)]
    v = [view8(a, Tc) for a in out]
    for mu in range(4):
        for (nu, rem, q, wv) in TM[mu]:
            v[nu][sl(rem)] += wv * np.roll(y[mu], q, axis=(0, 1, 2, 3))
    return out


def fwd(f, mu):
    return np.roll(f, -1, axis=mu) - f


def bwd(g, mu):
    return np.roll(g, 1, axis=mu) - g


def dform(A):
    return [fwd(A[n], m) - fwd(A[m], n) for (m, n) in PLANES]


def dT(F):
    out = [np.zeros_like(F[0]) for _ in range(4)]
    for p, (m, n) in enumerate(PLANES):
        out[n] += bwd(F[p], m); out[m] -= bwd(F[p], n)
    return out


def dot(a, b):
    return sum(float(np.vdot(x, y)) for x, y in zip(a, b))


def axpy(al, x, y):
    return [yi + al * xi for xi, yi in zip(x, y)]


def mx(a):
    return max(float(np.max(np.abs(x))) for x in a)


def l1(a):
    return sum(float(np.sum(np.abs(x))) for x in a)


def cg(op, rhs, tol=1e-12, maxit=40000):
    x = [np.zeros_like(r) for r in rhs]; r = [a.copy() for a in rhs]; p = [a.copy() for a in rhs]
    rr = dot(r, r); nb = np.sqrt(rr); it = 0
    if nb == 0:
        return x, 0.0, 0
    for it in range(maxit):
        Ap = op(p); al = rr / dot(p, Ap)
        x = axpy(al, p, x); r = axpy(-al, Ap, r); rn = dot(r, r)
        if np.sqrt(rn) <= tol * nb:
            break
        p = axpy(rn / rr, p, r); rr = rn
    res = axpy(-1.0, op(x), rhs)
    return x, np.sqrt(dot(res, res)) / nb, it + 1


def nus(M):
    p = 2 * np.pi * np.fft.fftfreq(M); out = []
    for mu in range(4):
        sh = [1, 1, 1, 1]; sh[mu] = M
        out.append((np.exp(1j * p) - 1).reshape(sh))
    return out


def psi_of(M):
    nu = nus(M)
    return np.broadcast_to(sum(np.abs(n) ** 2 for n in nu), (M,) * 4).copy()


def lap_inv(a):
    M = a.shape[0]; ps = psi_of(M); ps[0, 0, 0, 0] = np.inf
    return np.real(np.fft.ifftn(np.fft.fftn(a) / ps))


def coulomb(Ap):
    """co-closed projection (constants kept)."""
    M = Ap[0].shape[0]; nu = nus(M)
    hat = [np.fft.fftn(a) for a in Ap]
    ps = psi_of(M); ps[0, 0, 0, 0] = 1.0
    div = sum(np.conj(nu[m]) * hat[m] for m in range(4))
    return [np.real(np.fft.ifftn(hat[m] - nu[m] * div / ps)) for m in range(4)]


def flux(A, Tc, s):
    """flux coarse-graining F^{(0->m)} with block side s, coarse side Tc."""
    out = []
    for nu in range(4):
        a = A[nu].reshape(Tc, s, Tc, s, Tc, s, Tc, s)
        idx = [slice(None)] * 8; idx[2 * nu + 1] = s - 1
        a = a[tuple(idx)]
        pos = 0; sax = []
        for j in range(4):
            if j == nu:
                pos += 1
            else:
                sax.append(pos + 1); pos += 2
        out.append(a.sum(axis=tuple(sax)))
    return out


class Chain:
    def __init__(self, k, T):
        self.k = k; self.T = T; self.S = [T * L ** (k - j) for j in range(k + 1)]

    def zero(self, j):
        return [np.zeros((self.S[j],) * 4) for _ in range(4)]

    def lev(self, X, j):
        return X[4 * j:4 * j + 4]

    def res(self, X, B=None):
        k = self.k; out = []
        for j in range(k):
            nxt = self.lev(X, j + 1) if j + 1 < k else (B if B is not None else self.zero(k))
            out.append(axpy(-1.0, nxt, Qop(self.lev(X, j), self.S[j + 1])))
        return out

    def op(self, X):
        k = self.k; r = self.res(X); out = []
        for j in range(k):
            o = Qtop = QTop(r[j], self.S[j + 1])
            if j == 0:
                o = axpy(1.0, dT(dform(self.lev(X, 0))), Qtop)
            else:
                o = axpy(-1.0, r[j - 1], Qtop)
            out += o
        return out

    def rhs(self, cur=None, B=None, resid=None):
        """cur: dict level -> 1-form current; B: data; resid: dict i -> level-(i+1) residual source s_i."""
        b = []
        for j in range(self.k):
            b += self.zero(j)
        if cur:
            for j, c in cur.items():
                for m in range(4):
                    b[4 * j + m] += c[m]
        if B is not None:
            t = QTop(B, self.S[self.k])
            for m in range(4):
                b[4 * (self.k - 1) + m] += t[m]
        if resid:
            for i, s in resid.items():
                t = QTop(s, self.S[i + 1])
                for m in range(4):
                    b[4 * i + m] += t[m]
                if i + 1 < self.k:
                    for m in range(4):
                        b[4 * (i + 1) + m] -= s[m]
        return b

    def solve(self, b):
        return cg(self.op, b)

    def outs(self, X, B=None):
        return dform(self.lev(X, 0)), self.res(X, B)


def delta_p(M):
    F = [np.zeros((M,) * 4) for _ in range(6)]; F[0][0, 0, 0, 0] = 1.0
    return F


def smoothstep_phi(t):
    a = np.abs(t); u = np.clip(2 * a - 1, 0.0, 1.0)
    S = 35 * u ** 4 - 84 * u ** 5 + 70 * u ** 6 - 20 * u ** 7
    return np.where(a <= 0.5, 1.0, np.where(a >= 1.0, 0.0, 1.0 - S))


def disp(M):
    y = np.arange(M); return np.where(y <= M // 2, y, y - M)


def cutoff(M, r):
    dv = disp(M).astype(float); f = smoothstep_phi(dv / r)
    return f[:, None, None, None] * f[None, :, None, None] * f[None, None, :, None] * f[None, None, None, :]


def ld_pieces(M, r):
    """g_0 = d^T(chi omega), current j' = d^T delta_p - d^T d g_0 (Lemma LD)."""
    dp = delta_p(M); V = float(M ** 4)
    om0 = lap_inv(dp[0] - 1.0 / V)
    chi = np.ones((M,) * 4) if r is None else cutoff(M, r)
    om = [np.zeros((M,) * 4) for _ in range(6)]; om[0] = chi * om0
    g0 = dT(om)
    jp = axpy(-1.0, dT(dform(g0)), dT(dp))
    if r is None:   # Lemma LD: G' = 0 exactly; report the roundoff, then use the exact zero (fix after the 08:33Z stall)
        print(f"    r = inf: max|d^T d g_0 - d^T delta_p| = {mx(jp):.1e} (set to 0)", flush=True)
        jp = [np.zeros_like(a) for a in jp]
    return g0, jp


def Qchain(ch, g0, upto):
    out = [g0]
    for j in range(upto):
        out.append(Qop(out[-1], ch.S[j + 1]))
    return out


def QTchain(ch, J, frm):
    """(Q^{(frm -> k)})^T J for a level-k form J."""
    v = J
    for j in range(ch.k - 1, frm - 1, -1):
        v = QTop(v, ch.S[j + 1])
    return v


def reldiff(a_list, b_list, scale):
    return max(mx(axpy(-1.0, a, b)) for a, b in zip(a_list, b_list)) / scale


# ---------------------------------------------------------------- P1
def pc(e, axes):
    """Lemma PC construction on a zero-padded box: returns {(a, b): G_ab} with d^T G = e."""
    if len(axes) == 1:
        return {}
    a0 = axes[0]; rest = axes[1:]
    Q = e[rest[0]].shape[0]
    nzidx = [i for i in range(Q) if any(np.any(np.take(e[nu], i, axis=a0) != 0) for nu in rest)]
    b = max(nzidx) if nzidx else 0
    G = {}; sub = {}
    ind_shape = [1, 1, 1, 1]; ind_shape[a0] = Q
    ind = (np.arange(Q) >= b).astype(float).reshape(ind_shape)
    for nu in rest:
        cs = np.cumsum(e[nu], axis=a0)
        W = np.take(cs, Q - 1, axis=a0)
        Wb = np.expand_dims(W, a0)
        G[(a0, nu)] = -cs + ind * Wb
        s = np.zeros_like(e[nu]); idx = [slice(None)] * 4; idx[a0] = b; s[tuple(idx)] = W
        sub[nu] = s
    G.update(pc(sub, rest))
    return G


def G_to_planes(G, shape):
    F = [np.zeros(shape) for _ in range(6)]
    for (a, b), g in G.items():
        if a < b:
            F[PLANES.index((a, b))] += g
        else:
            F[PLANES.index((b, a))] -= g
    return F


def part_P1():
    rng = np.random.default_rng(5)
    print("P1 (Lemma PC): random compact co-closed e = d^T F", flush=True)
    ok = True
    for case, q in enumerate([3, 3, 5, 5]):
        Qb = q + 8; sh = (Qb,) * 4
        F = [np.zeros(sh) for _ in range(6)]
        for p in range(6):
            F[p][3:3 + q - 1, 3:3 + q - 1, 3:3 + q - 1, 3:3 + q - 1] = rng.standard_normal((q - 1,) * 4)
        e = dT(F)
        nz = np.zeros(sh, bool)
        for a in e:
            nz |= np.abs(a) > 0
        ext = [np.where(np.any(nz, axis=tuple(j for j in range(4) if j != i)))[0] for i in range(4)]
        qq = max(int(x.max() - x.min() + 1) for x in ext)
        G = pc({m: e[m] for m in range(4)}, [0, 1, 2, 3])
        GF = G_to_planes(G, sh)
        err = mx(axpy(-1.0, e, dT(GF))) / mx(e)
        lo = [int(x.min()) for x in ext]; hi = [int(x.max()) for x in ext]
        outside = 0.0
        for g in GF:
            m = np.ones(sh, bool)
            m[lo[0]:hi[0] + 1, lo[1]:hi[1] + 1, lo[2]:hi[2] + 1, lo[3]:hi[3] + 1] = False
            outside = max(outside, float(np.max(np.abs(g[m]))))
        ratio = l1(GF) / (qq * l1(e))
        ok &= (err <= 1e-12) and (outside == 0.0)
        print(f"  case {case}: cube side q = {qq}; max|d^T G - e|/max|e| = {err:.1e}; max|G| outside cube = {outside:.1e}; "
              f"sum|G|/(q sum|e|) = {ratio:.4f}", flush=True)
    print(f"P1 {'PASS' if ok else 'FAIL'}  ({time.time() - T0:.1f} s, RSS {rss():.0f} MB)", flush=True)


# ---------------------------------------------------------------- P2
def part_P2():
    print("P2 (Lemma LD): Y^p = g-chain + Z;  Z = Z' + x(e)", flush=True)
    okA = okB = True
    for (k, T) in [(1, 4), (2, 2)]:
        ch = Chain(k, T); M = ch.S[0]
        dp = delta_p(M)
        Y, resY, itY = ch.solve(ch.rhs(cur={0: dT(dp)}))
        dY0, rY = ch.outs(Y)
        sc = mx(dY0)
        for r in [2, 3, None]:
            g0, jp = ld_pieces(M, r)
            gch = Qchain(ch, g0, k)                      # g_0, Q g_0, ..., Q^{(0->k)} g_0
            beta = [-a for a in gch[k]]
            Z, resZ, _ = ch.solve(ch.rhs(cur={0: jp}, B=beta))
            dZ0, rZ = ch.outs(Z, beta)
            dA = reldiff(dY0, axpy(1.0, dform(g0), dZ0), sc)
            dR = max(reldiff(a, b, sc) for a, b in zip(rY, rZ))
            okA &= max(dA, dR) <= 1e-8
            # second identity
            J = flux(jp, T, L ** k)
            jQ = QTchain(ch, J, 0)
            e = axpy(-1.0, jQ, jp)
            resid = {i: QTchain(ch, J, i + 1) for i in range(k)}
            Zp, _, _ = ch.solve(ch.rhs(B=beta, resid=resid))
            Xe, _, _ = ch.solve(ch.rhs(cur={0: e}))
            dZp0, rZp = ch.outs(Zp, beta); dXe0, rXe = ch.outs(Xe)
            dB_ = reldiff(dZ0, axpy(1.0, dZp0, dXe0), sc)
            rB_ = max(reldiff(a, axpy(1.0, b, c), sc) for a, b, c in zip(rZ, rZp, rXe))
            okB &= max(dB_, rB_) <= 1e-8
            print(f"  k={k} T={T} r={'inf' if r is None else r}: |dY0 - (dg0 + dZ0)| {dA:.1e}, |r(Y) - r(Z)| {dR:.1e}; "
                  f"|Z - Z' - x(e)| {max(dB_, rB_):.1e}; sum|j'| {l1(jp):.3e}, sum|e| {l1(e):.3e}; CG res {resY:.0e}/{resZ:.0e} "
                  f"({time.time() - T0:.0f} s, RSS {rss():.0f} MB)", flush=True)
    print(f"P2a {'PASS' if okA else 'FAIL'};  P2b {'PASS' if okB else 'FAIL'}", flush=True)


# ---------------------------------------------------------------- P4/P3/P5
def P_R_factory(ch, l):
    Tc = ch.S[l + 1]

    def P_R(v):
        v = coulomb(v)
        rhs = coulomb(Qop(v, Tc))
        opc = lambda u: coulomb(Qop(QTop(coulomb(u), Tc), Tc))
        z, rc, _ = cg(opc, rhs, tol=1e-12)
        s = QTop(coulomb(z), Tc)
        return axpy(-1.0, s, v), rc
    return P_R


def tsign(u):
    m = mx(u)
    return [np.where(np.abs(a) > 1e-12 * m, np.sign(a), 0.0) for a in u]


def part_P4(k, Ts):
    print(f"P4/P3/P5 (Theorem Y, Lemma DUAL, CO-0R sup): k = {k}", flush=True)
    for T in Ts:
        ch = Chain(k, T); M = ch.S[0]
        Y, resY, itY = ch.solve(ch.rhs(cur={0: dT(delta_p(M))}))
        for l in range(k):
            Yl = ch.lev(Y, l)
            P_R = P_R_factory(ch, l)
            u, rc1 = P_R(Yl)
            U = L ** (2 * l) * l1(u)
            w, rc2 = P_R(tsign(u))
            aw = mx(w)
            pair = dot(w, Yl)
            D = L ** (2 * l) * abs(pair) / aw
            X, resX, itX = ch.solve(ch.rhs(cur={l: w}))
            f0 = dform(ch.lev(X, 0))
            dual = abs(f0[0][0, 0, 0, 0] - pair) / max(abs(f0[0][0, 0, 0, 0]), 1e-30)
            S = L ** (2 * l) * mx(f0) / ((k - l + 1) * aw)
            print(f"  k={k} T={T} l={l}: D {D:.4f} (Dhat {D / (k - l + 1):.4f}), U {U:.4f}; DUAL rel {dual:.1e}; "
                  f"S {S:.4f}; CG res {resY:.0e}/{resX:.0e} ({itY}/{itX} it), coarse {rc1:.0e}/{rc2:.0e} "
                  f"({time.time() - T0:.0f} s, RSS {rss():.0f} MB)", flush=True)
            del u, w, X, f0


# ---------------------------------------------------------------- B1
def part_B1():
    print("B1 (bootstrap proxy): k = 1, T = 12", flush=True)
    k, T = 1, 12; ch = Chain(k, T); M = ch.S[0]
    dv = np.abs(disp(M))
    vals = []
    for r in [3, 4, 6, 9]:
        g0, jp = ld_pieces(M, r)
        J = flux(jp, T, L)
        e = axpy(-1.0, QTop(J, T), jp)
        nz = np.zeros((M,) * 4, bool)
        for a in e:
            nz |= np.abs(a) > 1e-14 * mx(e)
        ds = disp(M)
        q = max(int(ds[np.any(nz, axis=tuple(j for j in range(4) if j != i))].max()
                    - ds[np.any(nz, axis=tuple(j for j in range(4) if j != i))].min()) + 1 for i in range(4))
        dmax = np.maximum(np.maximum(dv[:, None, None, None], dv[None, :, None, None]),
                          np.maximum(dv[None, None, :, None], dv[None, None, None, :]))
        core = dmax <= r / 2 - 3
        jcore = max(float(np.max(np.abs(a[core]))) if core.any() else 0.0 for a in jp)
        vals.append(q * l1(e))
        print(f"  r={r}: sum|j'| {l1(jp):.4e}, max|j'| on core (d <= r/2-3) {jcore:.1e} (rel {jcore / mx(jp):.1e}), "
              f"sum|e| {l1(e):.4e}, q {q}, q*sum|e| {q * l1(e):.4e} ({time.time() - T0:.0f} s, RSS {rss():.0f} MB)",
              flush=True)
    dec = all(vals[i + 1] < vals[i] for i in range(len(vals) - 1))
    print(f"B1 {'PASS' if dec else 'FAIL'}", flush=True)


if __name__ == "__main__":
    part = sys.argv[1]
    if part == "P1":
        part_P1()
    elif part == "P2":
        part_P2()
    elif part == "P4a":
        part_P4(1, [2, 3, 4, 5, 6])
    elif part == "P4b":
        part_P4(2, [2, 3, 4])
    elif part == "B1":
        part_B1()
