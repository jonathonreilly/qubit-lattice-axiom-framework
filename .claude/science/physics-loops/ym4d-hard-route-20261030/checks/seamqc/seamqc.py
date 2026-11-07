#!/usr/bin/env python3
"""seam-quadratic-c: identity checks and the B-uniformity kill test.

Guidance only. No statement of library/seam-quadratic-c.md rests on a run:
the proof there is written by hand. A failed identity or a growing ratio
would refute; a bounded ratio proves nothing.

Lattice conventions (match Sections 2-5 of the note):
  1D fine circle of N = M*B sites, B = 2m+1 odd; coarse sites y_j = j*B;
  block I(y) = [y-m, y+m]; fine bond x = (x, x+1); coarse bond j = (y_j, y_{j+1}).
  R0 = block average, R1 = block average of line sums of B bonds (tent / B),
  T0 = kernels zeta, T1 = kernels eta, h = 1D homotopy.
  4D forms: dict comp -> array, comp a sorted tuple of axes.
"""
import sys, json, time, resource, itertools
import numpy as np

def rss_gb():
    r = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return r / 1e9 if sys.platform == "darwin" else r / 1e6

def guard():
    if rss_gb() > 2.0:
        print("RSS above 2 GB; stopping", flush=True)
        sys.exit(3)

# ---------------------------------------------------------------- 1D
def beta_fn(t, B):
    m = (B - 1) // 2
    return (B / (m + 1)) * max(0.0, 1.0 - abs(t) / (m + 1))

def lam_fn(t, B):
    return max(0.0, 1.0 - abs(t) / B)

def g1_of(B):
    m = (B - 1) // 2
    return m * (m + 1) / (2.0 * B * B)

def zeta_fn(t, B):
    g1 = g1_of(B)
    return lam_fn(t, B) + 2 * g1 * beta_fn(t, B) - g1 * (beta_fn(t - B, B) + beta_fn(t + B, B))

def eta_fn(t, B):
    g1 = g1_of(B)
    db = lambda s: beta_fn(s + 1, B) - beta_fn(s, B)
    box = 1.0 / B if 0 <= t <= B - 1 else 0.0
    return box + g1 * (db(t - B) - db(t))

def tau_fn(t, B):
    m = (B - 1) // 2
    return sum(1 for a in range(-m, m + 1) if a <= t <= a + B - 1)

def ops1d(B, M):
    m = (B - 1) // 2
    N = M * B
    R0 = np.zeros((M, N)); R1 = np.zeros((M, N))
    T0 = np.zeros((N, M)); T1 = np.zeros((N, M))
    for j in range(M):
        y = j * B
        for t in range(-m, m + 1):
            R0[j, (y + t) % N] += 1.0 / B
        for t in range(-m, m + B):
            R1[j, (y + t) % N] += tau_fn(t, B) / B
        for t in range(-(B + m), B + m + 1):
            T0[(y + t) % N, j] += zeta_fn(t, B)
        for t in range(-m - 1, B + m + 1):
            T1[(y + t) % N, j] += eta_fn(t, B)
    d = np.zeros((N, N)); dc = np.zeros((M, M))
    for x in range(N):
        d[x, x] -= 1; d[x, (x + 1) % N] += 1
    for j in range(M):
        dc[j, j] -= 1; dc[j, (j + 1) % M] += 1
    h = np.zeros((N, N))
    for x in range(N):
        jlo = int(np.floor((x - (B + m)) / B)) - 1
        jhi = int(np.ceil((x + (B + m)) / B)) + 1
        for jj in range(jlo, jhi + 1):
            y = jj * B
            z = zeta_fn(x - y, B)
            if z == 0.0:
                continue
            for xpp in range(y - m, y + m + 1):
                if xpp <= x:
                    for xp in range(xpp, x):
                        h[x, xp % N] += z / B
                else:
                    for xp in range(x, xpp):
                        h[x, xp % N] -= z / B
    P0 = T0 @ R0; P1 = T1 @ R1
    return dict(B=B, M=M, N=N, R0=R0, R1=R1, T0=T0, T1=T1, d=d, dc=dc, h=h, P0=P0, P1=P1)

def rel(a, b):
    na = max(np.linalg.norm(a), np.linalg.norm(b), 1e-300)
    return float(np.linalg.norm(a - b) / na)

def check1d(o):
    I_M = np.eye(o["M"]); I_N = np.eye(o["N"])
    out = {
        "R0T0=I": rel(o["R0"] @ o["T0"], I_M),
        "R1T1=I": rel(o["R1"] @ o["T1"], I_M),
        "R1d=dcR0": rel(o["R1"] @ o["d"], o["dc"] @ o["R0"]),
        "dT0=T1dc": rel(o["d"] @ o["T0"], o["T1"] @ o["dc"]),
        "hd=I-P0": rel(o["h"] @ o["d"], I_N - o["P0"]),
        "dh=I-P1": rel(o["d"] @ o["h"], I_N - o["P1"]),
        "R0h=0": float(np.abs(o["R0"] @ o["h"]).max()),
        "T0 1 = 1": rel(o["T0"] @ np.ones(o["M"]), np.ones(o["N"])),
    }
    # operator norms (guidance for the constants of Section 3)
    B = o["B"]
    out["|T0|^2/B"] = float(np.linalg.norm(o["T0"], 2) ** 2 / B)
    out["|T1|^2*B"] = float(np.linalg.norm(o["T1"], 2) ** 2 * B)
    out["|P0|"] = float(np.linalg.norm(o["P0"], 2))
    out["|P1|"] = float(np.linalg.norm(o["P1"], 2))
    out["|h|/B"] = float(np.linalg.norm(o["h"], 2) / B)
    return out

def check_composite1d(L, M2):
    """R^{(L)} o R^{(L)} = R^{(L^2)} for the 1D factors of the path average."""
    lo = ops1d(L, L * M2)   # level 0 -> 1
    hi = ops1d(L, M2)       # level 1 -> 2
    big = ops1d(L * L, M2)  # one step of side L^2
    return {"R0 comp": rel(hi["R0"] @ lo["R0"], big["R0"]),
            "R1 comp": rel(hi["R1"] @ lo["R1"], big["R1"])}

# ---------------------------------------------------------------- 4D
PAIRS = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
TRIPLES = [(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)]

def ax_apply(mat, arr, axis):
    out = np.tensordot(mat, arr, axes=([1], [axis]))
    return np.moveaxis(out, 0, axis)

def tens(arr, mats):
    for ax in range(4):
        if mats[ax] is not None:
            arr = ax_apply(mats[ax], arr, ax)
    return arr

class Lat4:
    def __init__(self, B, Ms):
        self.B = B; self.Ms = tuple(Ms)
        cache = {}
        self.o = []
        for M in Ms:
            if M not in cache:
                cache[M] = ops1d(B, M)
            self.o.append(cache[M])
        self.Ns = tuple(o["N"] for o in self.o)

    # exterior derivatives (fine: key 'd', coarse: key 'dc')
    def d0(self, f, key="d"):
        return {(mu,): ax_apply(self.o[mu][key], f, mu) for mu in range(4)}
    def d1(self, A, key="d"):
        return {(mu, nu): ax_apply(self.o[mu][key], A[(nu,)], mu) - ax_apply(self.o[nu][key], A[(mu,)], nu)
                for (mu, nu) in PAIRS}
    def d2(self, F, key="d"):
        out = {}
        for (l, mu, nu) in TRIPLES:
            out[(l, mu, nu)] = (ax_apply(self.o[l][key], F[(mu, nu)], l)
                                - ax_apply(self.o[mu][key], F[(l, nu)], mu)
                                + ax_apply(self.o[nu][key], F[(l, mu)], nu))
        return out
    def d1T(self, Y, key="d"):  # adjoint of d1
        out = {(mu,): 0.0 for mu in range(4)}
        for (mu, nu) in PAIRS:
            out[(nu,)] = out[(nu,)] + ax_apply(self.o[mu][key].T, Y[(mu, nu)], mu)
            out[(mu,)] = out[(mu,)] - ax_apply(self.o[nu][key].T, Y[(mu, nu)], nu)
        return out

    # tensor maps on forms: degree-1 matrix on axes in S, degree-0 elsewhere
    def tmap(self, F, k1, k0, transpose=False):
        out = {}
        for S, arr in F.items():
            mats = []
            for ax in range(4):
                m_ = self.o[ax][k1 if ax in S else k0]
                mats.append(m_.T if transpose else m_)
            out[S] = tens(arr, mats)
        return out
    def R(self, F): return self.tmap(F, "R1", "R0")
    def T(self, F): return self.tmap(F, "T1", "T0")
    def Pi(self, F): return self.tmap(F, "P1", "P0")
    def RT_(self, F): return self.tmap(F, "R1", "R0", transpose=True)
    def TT_(self, F): return self.tmap(F, "T1", "T0", transpose=True)

    # telescoped tensor homotopy, sign (-1)^{#{j in S: j < i}} on slot i
    def _hterms(self, S):
        terms = []
        for pos, i in enumerate(S):
            sign = (-1) ** pos
            mats = []
            for ax in range(4):
                if ax < i:
                    mats.append(self.o[ax]["P1" if ax in S else "P0"])
                elif ax == i:
                    mats.append(self.o[ax]["h"])
                else:
                    mats.append(None)
            outS = tuple(a for a in S if a != i)
            terms.append((sign, mats, outS))
        return terms
    def hmap(self, F):
        out = {}
        for S, arr in F.items():
            for sign, mats, outS in self._hterms(S):
                v = sign * tens(arr, mats)
                out[outS] = out.get(outS, 0.0) + v
        return out
    def hmapT(self, Hbar, Scomps):  # adjoint of hmap restricted to input comps Scomps
        out = {}
        for S in Scomps:
            acc = 0.0
            for sign, mats, outS in self._hterms(S):
                if outS not in Hbar:
                    continue
                matsT = [None if m_ is None else m_.T for m_ in mats]
                # adjoint of tens: apply transposes (axis order irrelevant: they commute)
                acc = acc + sign * tens(Hbar[outS], matsT)
            out[S] = acc
        return out

def fadd(a, b, s=1.0): return {k: a[k] + s * b[k] for k in a}
def fsub(a, b): return {k: a[k] - b[k] for k in a}
def fdot(a, b): return float(sum(np.vdot(a[k], b[k]).real for k in a))
def fnorm2(a): return fdot(a, a)
def frel(a, b):
    num = np.sqrt(sum(np.linalg.norm(a[k] - b[k]) ** 2 for k in a))
    den = max(np.sqrt(fnorm2(a)), np.sqrt(fnorm2(b)), 1e-300)
    return float(num / den)
def fmax(a): return float(max(np.abs(v).max() for v in a.values()))
def fscale(a, s): return {k: s * v for k, v in a.items()}
def fmul(chi, a): return {k: chi * v for k, v in a.items()}

def rand1(lat, rng): return {(mu,): rng.standard_normal(lat.Ns) for mu in range(4)}
def rand2(lat, rng): return {S: rng.standard_normal(lat.Ns) for S in PAIRS}

def check4d(lat, rng):
    out = {}
    f = rng.standard_normal(lat.Ns)
    A = rand1(lat, rng); G = rand2(lat, rng)
    # chain maps
    out["R d1 = d1' R"] = frel(lat.R(lat.d1(A)), lat.d1(lat.R(A), key="dc"))
    a_c = {(mu,): rng.standard_normal(lat.Ms) for mu in range(4)}
    out["d1 T = T d1'"] = frel(lat.d1(lat.T(a_c)), lat.T(lat.d1(a_c, key="dc")))
    out["R T = I (1-forms)"] = frel(lat.R(lat.T(a_c)), a_c)
    # homotopy on 0-, 1-, 2-forms
    f1 = {(): f}
    lhs0 = fsub(f1, lat.Pi(f1))
    rhs0 = lat.hmap(lat.d0(f))
    out["(I-Pi) f = h d f"] = frel(lhs0, {(): rhs0[()]})
    lhs1 = fsub(A, lat.Pi(A))
    hA = lat.hmap(A)[()]
    rhs1 = fadd(lat.d0(hA), lat.hmap(lat.d1(A)))
    out["(I-Pi) A = d h A + h d A"] = frel(lhs1, rhs1)
    lhs2 = fsub(G, lat.Pi(G))
    rhs2 = fadd(lat.d1(lat.hmap(G)), lat.hmap(lat.d2(G)))
    out["(I-Pi) G = d h G + h d G"] = frel(lhs2, rhs2)
    out["R h = 0 on 2-forms (max)"] = fmax(lat.R(lat.hmap(G)))
    # adjoint test of hmap on 2-forms
    Y = rand1(lat, rng)
    out["adjoint h2"] = abs(fdot(lat.hmap(G), Y) - fdot(G, lat.hmapT(Y, PAIRS))) / (np.sqrt(fnorm2(G) * fnorm2(Y)))
    return out

# ---------------------------------------------------------------- seam
def make_chi(lat, r, offset_fine, sharp=False):
    """chi as a function of axis 0 only. D = {x0 in [off, off + N0/2)} (cyclic);
    chi = clamp(2 - 2 d(x, D^{-r}) / r, 0, 1), d in top units (sup norm reduces to axis 0)."""
    B = lat.B; N0 = lat.Ns[0]
    xs = np.arange(N0)
    inD = ((xs - offset_fine) % N0) < N0 // 2
    if sharp:
        c = inD.astype(float)
    else:
        rf = int(round(r * B))
        # D^{-r}: sites whose cyclic ball of radius rf (fine) along axis 0 lies in D
        Dm = np.array([all(inD[(x + s) % N0] for s in range(-rf, rf + 1)) for x in xs])
        idx = np.where(Dm)[0]
        dist = np.array([min(min(abs(x - i), N0 - abs(x - i)) for i in idx) if len(idx) else 10 ** 9 for x in xs]) / B
        c = np.clip(2.0 - 2.0 * dist / r, 0.0, 1.0)
    shape = [1, 1, 1, 1]; shape[0] = N0
    return c.reshape(shape) * np.ones(lat.Ns), c

def seam_R(lat, G, chi):
    H = lat.hmap(G)
    chiH = fmul(chi, H)
    alpha = lat.R(chiH)
    Z = fsub(chiH, lat.T(alpha))
    dZ = lat.d1(Z)
    Rdef = fsub(dZ, fmul(chi, G))
    return H, Z, dZ, Rdef

def seam_RT(lat, Y, chi):
    Zbar = lat.d1T(Y)
    chiHbar = fsub(Zbar, lat.RT_(lat.TT_(Zbar)))
    Hbar = fmul(chi, chiHbar)
    Gbar = lat.hmapT(Hbar, PAIRS)
    return fsub(Gbar, fmul(chi, Y))

def g0_from_A(lat, A):
    F = lat.d1(A)
    return fsub(F, lat.Pi(F))

# projector onto G_0 = {closed G with C G = 0} via FFT + small Gram correction
class ProjG0:
    def __init__(self, lat):
        self.lat = lat
        Ns = lat.Ns
        ks = np.meshgrid(*[2 * np.pi * np.fft.fftfreq(n) for n in Ns], indexing="ij")
        e = [np.exp(1j * k) - 1.0 for k in ks]  # symbol of forward difference
        # d2 symbol: 3-form comps x 2-form comps
        D = np.zeros(Ns + (4, 6), dtype=complex)
        pidx = {S: i for i, S in enumerate(PAIRS)}
        for ti, (l, mu, nu) in enumerate(TRIPLES):
            D[..., ti, pidx[(mu, nu)]] += e[l]
            D[..., ti, pidx[(l, nu)]] -= e[mu]
            D[..., ti, pidx[(l, mu)]] += e[nu]
        DD = D @ np.conj(np.swapaxes(D, -1, -2))
        pinv = np.linalg.pinv(DD, rcond=1e-10, hermitian=True)
        self.Pcl = np.eye(6) - np.conj(np.swapaxes(D, -1, -2)) @ pinv @ D
        del D, DD, pinv
        # Gram correction for the coarse constraint
        cols = []
        for S in PAIRS:
            for idx in itertools.product(*[range(M) for M in lat.Ms]):
                ec = {T: np.zeros(lat.Ms) for T in PAIRS}
                ec[S][idx] = 1.0
                cols.append(self.pcl(lat.RT_(ec)))
        self.Y = cols
        n = len(cols)
        Gm = np.array([[fdot(cols[i], cols[j]) for j in range(n)] for i in range(n)])
        self.Gpinv = np.linalg.pinv(Gm, rcond=1e-12, hermitian=True)
    def pcl(self, F):
        Fh = np.stack([np.fft.fftn(F[S]) for S in PAIRS], axis=-1)
        Fh = (self.Pcl @ Fh[..., None])[..., 0]
        return {S: np.fft.ifftn(Fh[..., i]).real for i, S in enumerate(PAIRS)}
    def __call__(self, F):
        v = self.pcl(F)
        c = np.array([fdot(y, v) for y in self.Y])
        coef = self.Gpinv @ c
        for a, y in zip(coef, self.Y):
            if a != 0.0:
                v = fadd(v, y, -a)
        return v

def shell_mask(lat, chi_line, rho_top):
    """Sites within rho_top (top units, axis 0) of the transition set {0 < chi < 1}."""
    B = lat.B; N0 = lat.Ns[0]
    tr = np.where((chi_line > 0) & (chi_line < 1))[0]
    if len(tr) == 0:
        tr = np.where(np.abs(np.diff(np.r_[chi_line, chi_line[0]])) > 0)[0]
    xs = np.arange(N0)
    dist = np.array([min(min(abs(x - i), N0 - abs(x - i)) for i in tr) for x in xs]) / B
    m = (dist <= rho_top).astype(float)
    shape = [1, 1, 1, 1]; shape[0] = N0
    return m.reshape(shape) * np.ones(lat.Ns)

def ratio(lat, G, chi, mask):
    H, Z, dZ, Rdef = seam_R(lat, G, chi)
    nR = fnorm2(Rdef); nG = fnorm2(G); nGs = fnorm2(fmul(mask, G))
    return nR / nG, (nR / nGs if nGs > 0 else float("inf")), H, Z, dZ, Rdef

def test_fields(lat, rng, face_fine):
    B = lat.B; Ns = lat.Ns
    x0 = np.arange(Ns[0]).reshape(-1, 1, 1, 1)
    x2 = np.arange(Ns[2]).reshape(1, 1, -1, 1)
    out = {}
    for name, w_top, kk in [("face mode, top-scale transverse", 0.5, 1),
                            ("face mode, fine transverse", 0.5, (Ns[2] - 1) // 2),
                            ("face mode, narrow", 0.15, 1)]:
        dd = ((x0 - face_fine + Ns[0] / 2) % Ns[0] - Ns[0] / 2) / B
        prof = np.exp(-(dd / w_top) ** 2) * np.cos(2 * np.pi * kk * x2 / Ns[2])
        A = {(mu,): np.zeros(Ns) for mu in range(4)}
        A[(1,)] = prof * np.ones(Ns)      # transverse component, crosses the face along axis 0
        out[name] = g0_from_A(lat, A)
    out["white noise"] = g0_from_A(lat, rand1(lat, rng))
    sm = {}
    for mu in range(4):
        a = rng.standard_normal(Ns)
        ah = np.fft.fftn(a)
        ks = np.meshgrid(*[np.fft.fftfreq(n) * n / B for n in Ns], indexing="ij")
        ah *= np.exp(-0.5 * sum(k ** 2 for k in ks) / 1.0 ** 2)
        sm[(mu,)] = np.fft.ifftn(ah).real
    out["smooth noise"] = g0_from_A(lat, sm)
    return out

def power_iter(lat, chi, P0, rng, iters=40):
    G = P0(rand2(lat, rng))
    lam = 0.0
    for it in range(iters):
        guard()
        _, _, _, Rd = seam_R(lat, G, chi)
        W = P0(seam_RT(lat, Rd, chi))
        lam = fdot(G, W) / fnorm2(G)
        G = fscale(W, 1.0 / np.sqrt(fnorm2(W)))
    return lam, G

# ---------------------------------------------------------------- contours
def contour_steps(delta):
    steps = []
    pos = [0, 0, 0, 0]
    for ax in range(4):
        n = delta[ax]
        for _ in range(abs(n)):
            if n > 0:
                steps.append((tuple(pos), ax, +1)); pos[ax] += 1
            else:
                pos[ax] -= 1; steps.append((tuple(pos), ax, -1))
    return steps

def shift(arr, pos):
    return np.roll(arr, shift=tuple(-p for p in pos), axis=(0, 1, 2, 3))

def balaban_Q(theta, L):
    """One linearized Balaban step with axial-staircase contours (axes in order 0..3),
    computed from the definition: avg over x in B(y) of
    theta(Gamma_{y,x}) + theta([x, x+L e_mu]) - theta(Gamma_{y+L e_mu, x+L e_mu})."""
    m = (L - 1) // 2
    N = theta[(0,)].shape
    offs = list(itertools.product(range(-m, m + 1), repeat=4))
    cont = {}
    for dlt in offs:
        acc = np.zeros(N)
        for (pos, ax, sg) in contour_steps(dlt):
            acc += sg * shift(theta[(ax,)], pos)
        cont[dlt] = acc            # cont[dlt][y] = theta(Gamma_{y, y+dlt})
    out = {}
    for mu in range(4):
        e = [0, 0, 0, 0]; e[mu] = L
        acc = np.zeros(N)
        for dlt in offs:
            line = np.zeros(N)
            for s in range(L):
                p = list(dlt); p[mu] += s
                line += shift(theta[(mu,)], p)
            acc += cont[dlt] + line - shift(cont[dlt], e)
        acc /= len(offs)
        out[(mu,)] = acc[::L, ::L, ::L, ::L]
    return out

def coarse_d1(Ms, a):
    out = {}
    for (mu, nu) in PAIRS:
        out[(mu, nu)] = (np.roll(a[(nu,)], -1, axis=mu) - a[(nu,)]) - (np.roll(a[(mu,)], -1, axis=nu) - a[(mu,)])
    return out

def contour_checks(rng, L=3, M2=2):
    B = L * L
    N = (B * M2,) * 4
    lat9 = Lat4(B, (M2,) * 4)
    theta = {(mu,): rng.standard_normal(N) for mu in range(4)}
    q1 = balaban_Q(theta, L)
    q2 = balaban_Q(q1, L)
    out = {}
    # curvature form of the composite constraint: d' Q_2 = C_9 d
    out["d'Q_2 = C_B d (B=9)"] = frel(coarse_d1((M2,) * 4, q2), lat9.R(lat9.d1(theta)))
    # gauge covariance Q_2 d = d' r_2
    lam = rng.standard_normal(N)
    g = lat9.d0(lam)
    q2g = balaban_Q(balaban_Q(g, L), L)
    r2 = lam[::B, ::B, ::B, ::B]
    dr2 = {(mu,): np.roll(r2, -1, axis=mu) - r2 for mu in range(4)}
    out["Q_2 d = d' r_2"] = frel(q2g, dr2)
    # Q_2 - Q_path^(9) is a coarse gradient: curl free and holonomy free
    qp = lat9.R(theta)
    diff = fsub(q2, qp)
    out["curl(Q_2 - Q_path) max"] = fmax(coarse_d1((M2,) * 4, diff))
    hol = max(float(np.abs(diff[(mu,)].sum(axis=mu)).max()) for mu in range(4))
    out["holonomy(Q_2 - Q_path) max"] = hol
    # end-to-end: seam competitor built from B=9 tensor operators has the exact
    # composite parent after a pure-gauge correction (A_* = 0, v = 0 here)
    A = rand1(lat9, rng)
    G = g0_from_A(lat9, A)
    chi_full, _ = make_chi(lat9, 0.5, 0, sharp=False)
    H, Z, dZ, Rdef = seam_R(lat9, G, chi_full)
    w = balaban_Q(balaban_Q(Z, L), L)       # = -d' Phi_2(Z)
    out["Q_path Z = 0 (max)"] = fmax(lat9.R(Z))
    out["curl Q_2 Z max"] = fmax(coarse_d1((M2,) * 4, w))
    # integrate -w on the coarse torus along axial paths to get psi with d'psi = -w
    Mc = M2
    psi = np.zeros((Mc,) * 4)
    for idx in itertools.product(range(Mc), repeat=4):
        s = 0.0; pos = [0, 0, 0, 0]
        for ax in range(4):
            for _ in range(idx[ax]):
                s -= w[(ax,)][tuple(pos)]; pos[ax] += 1
        psi[idx] = s
    lamf = np.zeros(N)
    lamf[::B, ::B, ::B, ::B] = psi
    X = fadd(Z, lat9.d0(lamf))
    qX = balaban_Q(balaban_Q(X, L), L)
    out["Q_2 (Z + d E psi) = 0 (max)"] = fmax(qX)
    out["d(Z + d E psi) = dZ"] = frel(lat9.d1(X), dZ)
    out["dZ in G_0: C dZ max"] = fmax(lat9.R(dZ))
    return out

# ---------------------------------------------------------------- main
def quick():
    rng = np.random.default_rng(1)
    print({k: f"{v:.2e}" for k, v in check1d(ops1d(5, 2)).items()}, flush=True)
    print(check_composite1d(3, 2), flush=True)
    print({k: f"{v:.2e}" for k, v in check4d(Lat4(3, (3, 2, 2, 2)), rng).items()}, flush=True)
    print("RSS GB", round(rss_gb(), 3), flush=True)

def rscan(path):
    """Worst-case ratio (power iteration on G_0) against the cutoff radius r."""
    rng = np.random.default_rng(7)
    out = {}
    for B in [5, 9]:
        lat = Lat4(B, (12, 1, 1, 1))
        P0 = ProjG0(lat)
        m = (B - 1) // 2
        for r in [0.5, 1.0, 2.0]:
            chi, chi_line = make_chi(lat, r, m + 1, sharp=False)
            lam, Gst = power_iter(lat, chi, P0, rng, iters=60)
            out[f"B={B},r={r}"] = {"sup |R|^2/|G|^2": lam, "times r^2": lam * r * r}
            print(B, r, round(lam, 4), round(lam * r * r, 4), "RSS GB", round(rss_gb(), 3), flush=True)
            guard()
        del P0
    with open(path, "w") as fh:
        json.dump(out, fh, indent=1)

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "quick":
        return quick()
    if len(sys.argv) > 2 and sys.argv[1] == "rscan":
        return rscan(sys.argv[2])
    rng = np.random.default_rng(20261102)
    res = {"commit": "ba5277f05", "time": time.strftime("%Y-%m-%dT%H:%MZ", time.gmtime())}
    t0 = time.time()
    res["1d"] = {}
    for B in [3, 5, 7, 9, 11, 13, 21, 41]:
        for M in [1, 2, 5]:
            res["1d"][f"B={B},M={M}"] = check1d(ops1d(B, M))
    res["composite1d"] = {f"L={L},M2={M2}": check_composite1d(L, M2) for L in [3, 5] for M2 in [1, 2, 3]}
    print("1D done", round(time.time() - t0, 1), "s; RSS GB", round(rss_gb(), 3), flush=True)
    guard()
    res["4d"] = {}
    for B, Ms in [(3, (3, 2, 2, 2)), (5, (2, 1, 2, 1)), (9, (2, 1, 1, 1))]:
        res["4d"][f"B={B},Ms={Ms}"] = check4d(Lat4(B, Ms), rng)
        guard()
    print("4D identities done", round(time.time() - t0, 1), "s; RSS GB", round(rss_gb(), 3), flush=True)
    res["contours"] = contour_checks(rng, L=3, M2=2)
    guard()
    print("contours done", round(time.time() - t0, 1), "s; RSS GB", round(rss_gb(), 3), flush=True)
    # B-uniformity kill test
    res["ratios"] = {}
    M1 = 8; r = 1.0
    for B in [3, 5, 7, 9, 11, 13]:
        for Mt in ([1, 2] if B <= 7 else [1]):
            lat = Lat4(B, (M1, Mt, Mt, Mt))
            m = (B - 1) // 2
            for align, off in [("face at block face", m + 1), ("face at block centre", 0)]:
                for sharp in [False, True]:
                    chi, chi_line = make_chi(lat, r, off, sharp=sharp)
                    mask = shell_mask(lat, chi_line, 4.0)
                    fields = test_fields(lat, rng, off)
                    row = {}
                    for name, G in fields.items():
                        a, b, H, Z, dZ, Rdef = ratio(lat, G, chi, mask)
                        row[name] = {"full": a, "shell": b}
                        if name == "white noise":
                            row["check dH=G"] = frel(lat.d1(H), G)
                            row["check Q_path H = 0 (max)"] = fmax(lat.R(H))
                            row["check C dZ = 0 (max)"] = fmax(lat.R(dZ))
                            # R = [d,chi]H - T_2 d' Q_path(chi H)
                            chiH = fmul(chi, H)
                            alt = fsub(fsub(lat.d1(chiH), fmul(chi, G)), lat.T(lat.d1(lat.R(chiH), key="dc")))
                            row["check R formula"] = frel(Rdef, alt)
                        guard()
                    if not sharp and Mt == 1 and align == "face at block face":
                        P0 = ProjG0(lat)
                        v = rand2(lat, rng); pv = P0(v)
                        row["check P0: d2 P0 v (max)"] = fmax(lat.d2(pv))
                        row["check P0: C P0 v (max)"] = fmax(lat.R(pv))
                        row["check P0 idempotent"] = frel(P0(pv), pv)
                        Yr = rand2(lat, rng)
                        _, _, _, Rv = seam_R(lat, v, chi)
                        row["check adjoint seam"] = abs(fdot(Rv, Yr) - fdot(v, seam_RT(lat, Yr, chi))) / np.sqrt(fnorm2(v) * fnorm2(Yr))
                        lam, Gst = power_iter(lat, chi, P0, rng, iters=40)
                        _, b, *_ = ratio(lat, Gst, chi, mask)
                        row["power iteration"] = {"full": lam, "shell": b}
                        del P0
                    res["ratios"][f"B={B},Mt={Mt},{align},{'sharp' if sharp else 'smooth'}"] = row
                    print(f"B={B} Mt={Mt} {align} {'sharp' if sharp else 'smooth'}:",
                          {k: (round(v['full'], 4) if isinstance(v, dict) else v) for k, v in row.items()},
                          "RSS GB", round(rss_gb(), 3), flush=True)
    res["runtime_s"] = round(time.time() - t0, 1)
    with open(sys.argv[1] if len(sys.argv) > 1 else "seamqc_results.json", "w") as fh:
        json.dump(res, fh, indent=1, default=float)
    print("done", res["runtime_s"], "s", flush=True)

if __name__ == "__main__":
    main()
