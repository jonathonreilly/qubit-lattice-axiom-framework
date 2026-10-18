"""Block C5b shared tools (own implementation; imports nothing from C5).

Conventions (fixed once, used everywhere; see NOTE.md section 0):
  * quasienergy E of an eigenvector: U psi = exp(-i E) psi.
  * level eps: F_eps = {k : exp(-i eps) in spec U(k)}.
  * W3[U] = (1/24 pi^2) int_{[0,2pi)^3} sum eps_abc tr(A_a A_b A_c) d^3k, A_a = U^{-1} d_a U
    (same convention as C5; positive control V_2 has W3 = -1).
  * Ch(P) on an oriented closed surface = (i/2pi) int tr(P dP ^ dP); computed here by
    the Fukui-Hatsugai-Suzuki lattice method, sign-calibrated in s0 against the
    analytic integral.
  * Weyl chirality chi_p = sign det v, where near p the two touching bands obey
    H_eff = E_p + sum_ij v_ij dk_i sigma_j (+ tilt), i.e. U ~ exp(-i H_eff) on the
    two-dimensional degenerate space.

Localization theorem (NOTE.md Thm L): for disjoint boxes B_i whose union contains F_eps
in its interior,  W3[U] = - sum_i Ch(P_<|dB_i)   (dB_i oriented outward),
P_< = spectral projector onto eigenvectors with quasienergy in the local window
(phi - 2pi, eps), phi a quasienergy absent on the whole box.
"""
import itertools
import numpy as np

S0 = np.eye(2, dtype=complex)
SX = np.array([[0, 1], [1, 0]], complex)
SY = np.array([[0, -1j], [1j, 0]], complex)
SZ = np.array([[1, 0], [0, -1]], complex)
PAULI = [SX, SY, SZ]


class Checker:
    def __init__(self):
        self.p = self.f = 0

    def check(self, name, ok, tag='numerical'):
        ok = bool(ok)
        self.p += ok
        self.f += (not ok)
        print(('PASS' if ok else 'FAIL') + f' [{tag}] ' + name, flush=True)

    def total(self):
        print(f'TOTAL: PASS={self.p} FAIL={self.f}', flush=True)


# ---------------------------------------------------------------- walks
class Laurent:
    """U(k) = sum_n A_n exp(i n.k), n in Z^3."""

    def __init__(self, coeffs, name=''):
        self.c = {tuple(int(x) for x in n): np.asarray(M, complex) for n, M in coeffs.items()}
        self.c = {n: M for n, M in self.c.items() if np.abs(M).max() > 1e-14}
        self.n = next(iter(self.c.values())).shape[0]
        self.name = name
        # ||U(k)-U(k')|| <= L ||k-k'||_inf
        self.L = sum(np.linalg.norm(M, 2) * sum(abs(x) for x in n) for n, M in self.c.items())
        self.range = max(max(abs(x) for x in n) for n in self.c)

    def __call__(self, K):
        K = np.asarray(K, float)
        out = np.zeros(K.shape[:-1] + (self.n, self.n), complex)
        for n, M in self.c.items():
            ph = np.exp(1j * (K @ np.array(n, float)))
            out += ph[..., None, None] * M
        return out

    def deriv(self, K):
        K = np.asarray(K, float)
        outs = [np.zeros(K.shape[:-1] + (self.n, self.n), complex) for _ in range(3)]
        for n, M in self.c.items():
            ph = np.exp(1j * (K @ np.array(n, float)))
            for a in range(3):
                outs[a] += (1j * n[a] * ph)[..., None, None] * M
        return outs


def lmul(A, B):
    out = {}
    for na, Ma in A.c.items():
        for nb, Mb in B.c.items():
            n = tuple(x + y for x, y in zip(na, nb))
            out[n] = out.get(n, 0) + Ma @ Mb
    return Laurent(out, A.name + '*' + B.name)


def lconst(M, name='C'):
    return Laurent({(0, 0, 0): M}, name)


def lshift(P, a, name='S'):
    d = P.shape[0]
    out = {tuple(a): P.astype(complex)}
    out[(0, 0, 0)] = out.get((0, 0, 0), 0) + (np.eye(d) - P)
    return Laurent(out, name)


def ldirect(A, B):
    n1, n2 = A.n, B.n
    out = {}
    for n, M in A.c.items():
        Z = out.setdefault(n, np.zeros((n1 + n2, n1 + n2), complex))
        Z[:n1, :n1] += M
    for n, M in B.c.items():
        Z = out.setdefault(n, np.zeros((n1 + n2, n1 + n2), complex))
        Z[n1:, n1:] += M
    return Laurent(out, A.name + '+' + B.name)


class Func:
    """Generic (possibly infinite-range) walk given by a vectorised callable and a
    rigorous Lipschitz constant L for ||U(k)-U(k')|| <= L ||k-k'||_inf."""

    def __init__(self, f, n, L, name='', dfun=None):
        self.f, self.n, self.L, self.name, self.dfun = f, n, L, name, dfun
        self.range = None

    def __call__(self, K):
        return self.f(np.asarray(K, float))

    def deriv(self, K, h=1e-5):
        if self.dfun is not None:
            return self.dfun(K)
        K = np.asarray(K, float)
        outs = []
        for a in range(3):
            e = np.zeros(3); e[a] = h
            outs.append((self.f(K + e) - self.f(K - e)) / (2 * h))
        return outs


# ---------------------------------------------------------------- W3 integral
def w3_grid(W, N, offset=0.0):
    k = 2 * np.pi * (np.arange(N) + offset) / N
    K = np.stack(np.meshgrid(k, k, k, indexing='ij'), -1)
    U = W(K)
    dU = W.deriv(K)
    Ui = np.linalg.inv(U)
    A = [Ui @ d for d in dU]
    t = np.trace(A[0] @ A[1] @ A[2] - A[0] @ A[2] @ A[1], axis1=-2, axis2=-1)
    # sum eps tr(AaAbAc) = 3 [tr(A1A2A3) - tr(A1A3A2)]
    val = 3 * t.sum() * (2 * np.pi / N) ** 3 / (24 * np.pi ** 2)
    return val


# ---------------------------------------------------------------- spectra
def gapfun(U, eps):
    """s(k) = min_j |lambda_j - exp(-i eps)| (U normal => smallest singular value of U - z)."""
    lam = np.linalg.eigvals(U)
    return np.min(np.abs(lam - np.exp(-1j * eps)), axis=-1)


def quasi(U):
    """quasienergies E in (-pi, pi], sorted, U psi = e^{-iE} psi."""
    lam = np.linalg.eigvals(U)
    return np.sort(-np.angle(lam), axis=-1)


# ---------------------------------------------------------------- level-set certification
def certify_level(W, eps, N0=24, depth=4, exclude=None, batch=200000):
    """Rigorous (up to float rounding) certificate that s(k) > 0 on every closed coarse
    cell of an N0^3 periodic grid except those returned as 'bad'.  A cell of half-width h
    (sup-norm) with centre c is certified if s(c) > L h (Lipschitz).  Uncertified cells are
    split into 8 up to `depth` times.  Returns (bad_coarse_cells:set of index triples,
    min certified margin)."""
    L = W.L
    h0 = np.pi / N0
    cells = np.array(list(itertools.product(range(N0), repeat=3)))
    if exclude is not None:
        cells = np.array([c for c in cells if tuple(c) not in exclude])
    bad = set()
    # entries: coarse index, centre, half-width
    centres = (cells + 0.5) * (2 * np.pi / N0)
    owner = cells.copy()
    h = h0
    minmargin = np.inf
    for lev in range(depth + 1):
        s = np.empty(len(centres))
        for i in range(0, len(centres), batch):
            s[i:i + batch] = gapfun(W(centres[i:i + batch]), eps)
        ok = s > L * h * (1 + 1e-9) + 1e-12
        if ok.any():
            minmargin = min(minmargin, np.min(s[ok] - L * h))
        fail = ~ok
        if lev == depth or not fail.any():
            for o in owner[fail]:
                bad.add(tuple(o))
            break
        c = centres[fail]; o = owner[fail]
        h = h / 2
        offs = np.array(list(itertools.product((-1, 1), repeat=3))) * h
        centres = (c[:, None, :] + offs[None]).reshape(-1, 3)
        owner = np.repeat(o, 8, axis=0)
        if len(centres) > 4e6:   # too many: give up on refinement, report all as bad
            for oo in np.unique(owner, axis=0):
                bad.add(tuple(oo))
            break
    return bad, minmargin


def components(bad, N0):
    """26-connected periodic components of a set of coarse cells."""
    bad = set(bad); comps = []
    while bad:
        seed = bad.pop(); comp = {seed}; stack = [seed]
        while stack:
            c = stack.pop()
            for d in itertools.product((-1, 0, 1), repeat=3):
                nb = tuple((c[i] + d[i]) % N0 for i in range(3))
                if nb in bad:
                    bad.remove(nb); comp.add(nb); stack.append(nb)
        comps.append(comp)
    return comps


def comp_box(comp, N0, pad=1):
    """Box (in unwrapped coarse-index coordinates) covering a component, padded."""
    arr = np.array(sorted(comp))
    lo = []; hi = []
    for a in range(3):
        v = np.sort(np.unique(arr[:, a]))
        # choose unwrapping that minimises extent: find largest gap on circle
        if len(v) == 1:
            lo.append(v[0]); hi.append(v[0]); continue
        gaps = np.diff(np.concatenate([v, [v[0] + N0]]))
        j = np.argmax(gaps)
        start = v[(j + 1) % len(v)]
        ext = (v - start) % N0
        lo.append(start); hi.append(start + ext.max())
    lo = np.array(lo) - pad; hi = np.array(hi) + pad
    return lo, hi   # cells lo..hi inclusive (unwrapped)


def box_cells(lo, hi, N0):
    return {tuple(np.array(c) % N0) for c in itertools.product(*[range(lo[a], hi[a] + 1) for a in range(3)])}


def shell_cells(lo, hi, N0):
    s = set()
    for c in itertools.product(*[range(lo[a], hi[a] + 1) for a in range(3)]):
        if any(c[a] in (lo[a], hi[a]) for a in range(3)):
            s.add(tuple(np.array(c) % N0))
    return s


# ---------------------------------------------------------------- Chern number on box surface
def box_surface_points(lo_k, hi_k, M):
    """Six faces of the box [lo_k,hi_k], each an (M+1)x(M+1) grid with outward orientation:
    returns list of arrays (M+1,M+1,3) with (u,v) ordered so that d_u x d_v is outward."""
    faces = []
    xs = [np.linspace(lo_k[a], hi_k[a], M + 1) for a in range(3)]
    for a in range(3):
        b, c = (a + 1) % 3, (a + 2) % 3   # e_b x e_c = e_a
        for side, val in ((+1, hi_k[a]), (-1, lo_k[a])):
            if side == 1:
                u, v = b, c
            else:
                u, v = c, b
            G = np.zeros((M + 1, M + 1, 3))
            G[..., u] = xs[u][:, None]
            G[..., v] = xs[v][None, :]
            G[..., a] = val
            faces.append(G)
    return faces


def lower_frame(U, eps, phi):
    """Frames of P_<: eigenvectors whose quasienergy, mapped into (phi-2pi, phi], is < eps."""
    lam, V = np.linalg.eig(U)
    E = -np.angle(lam)
    E = phi - np.mod(phi - E, 2 * np.pi)          # into (phi-2pi, phi]
    sel = E < eps
    return V, sel


def chern_box(W, lo_k, hi_k, eps, phi, M=24):
    """Fukui-Hatsugai-Suzuki Chern number of P_< on the outward-oriented box surface.
    Returns (Ch, rank_set) ; rank must be constant on the surface."""
    faces = box_surface_points(lo_k, hi_k, M)
    total = 0.0
    ranks = set()
    for G in faces:
        U = W(G.reshape(-1, 3)).reshape(M + 1, M + 1, W.n, W.n)
        frames = np.empty((M + 1, M + 1), object)
        for i in range(M + 1):
            for j in range(M + 1):
                V, sel = lower_frame(U[i, j], eps, phi)
                Q = V[:, sel]
                Q, _ = np.linalg.qr(Q) if Q.shape[1] > 0 else (Q, None)
                frames[i, j] = Q
                ranks.add(Q.shape[1])
        if len(ranks) != 1:
            return np.nan, ranks
        r = ranks.copy().pop()
        if r == 0:
            continue

        def link(a, b):
            return np.linalg.det(a.conj().T @ b)
        for i in range(M):
            for j in range(M):
                p = (link(frames[i, j], frames[i + 1, j]) * link(frames[i + 1, j], frames[i + 1, j + 1])
                     * link(frames[i + 1, j + 1], frames[i, j + 1]) * link(frames[i, j + 1], frames[i, j]))
                total += np.angle(p)
    # sign calibrated in s0 against (i/2pi) int tr P dP dP
    return CH_SIGN * total / (2 * np.pi), ranks


CH_SIGN = -1.0   # set by s0 (calibration against the analytic Chern form); s0 re-derives it


# ---------------------------------------------------------------- nodes
def find_min(W, eps, k0, iters=200):
    """Locally minimise s(k) from k0 (Nelder-Mead); returns k, s."""
    from scipy.optimize import minimize
    f = lambda k: float(gapfun(W(k[None])[0][None], eps)[0])
    r = minimize(f, k0, method='Nelder-Mead', options=dict(xatol=1e-12, fatol=1e-15, maxiter=4000))
    return r.x, r.fun


def weyl_chirality(W, eps, p, h=1e-6):
    """chi = sign det v for the two bands touching at quasienergy eps at p.
    H_eff on the 2-dim degenerate eigenspace D of U(p): U(p+dk) ~ e^{-i eps}(1 - i dH),
    dH = i e^{i eps} D^dag dU D (first order, degenerate perturbation theory)."""
    U0 = W(p[None])[0]
    lam, V = np.linalg.eig(U0)
    d = np.abs(lam - np.exp(-1j * eps))
    idx = np.argsort(d)[:2]
    D, _ = np.linalg.qr(V[:, idx])
    dU = W.deriv(p[None])
    v = np.zeros((3, 3)); tilt = np.zeros(3)
    for a in range(3):
        Ha = 1j * np.exp(1j * eps) * (D.conj().T @ dU[a][0] @ D)
        Ha = (Ha + Ha.conj().T) / 2
        tilt[a] = np.trace(Ha).real / 2
        for j, s in enumerate(PAULI):
            v[a, j] = np.trace(Ha @ s).real / 2
    others = np.sort(d)[2:] if len(d) > 2 else np.array([])
    return int(np.sign(np.linalg.det(v))), v, tilt, others


# ---------------------------------------------------------------- level analysis pipeline
def certify_cells(W, eps, cells, N0, depth=4, batch=200000):
    """Same Lipschitz certificate as certify_level, on an explicit list of coarse cells.
    Returns set of coarse cells NOT certified (eigenvalue exp(-i eps) not excluded)."""
    L_ = W.L
    cells = np.array(sorted(cells))
    if len(cells) == 0:
        return set()
    h = np.pi / N0
    centres = (cells + 0.5) * (2 * np.pi / N0)
    owner = cells.copy()
    bad = set()
    for lev in range(depth + 1):
        s = np.empty(len(centres))
        for i in range(0, len(centres), batch):
            s[i:i + batch] = gapfun(W(centres[i:i + batch]), eps)
        fail = ~(s > L_ * h * (1 + 1e-9) + 1e-12)
        if lev == depth or not fail.any():
            bad |= {tuple(o) for o in owner[fail]}
            break
        c = centres[fail]; o = owner[fail]
        h = h / 2
        offs = np.array(list(itertools.product((-1, 1), repeat=3))) * h
        centres = (c[:, None, :] + offs[None]).reshape(-1, 3)
        owner = np.repeat(o, 8, axis=0)
        if len(centres) > 3e6:
            bad |= {tuple(x) for x in np.unique(owner, axis=0)}
            break
    return bad


def analyze_level(W, eps, N0=32, depth=4, M=32, maxcomp=4000, verbose=True, allow_sheets=False):
    """Certified decomposition of level eps.  Returns dict with keys
    clean(bool), boxes(list of dict), sumCh, reason."""
    allc = set(itertools.product(range(N0), repeat=3))
    bad = certify_cells(W, eps, allc, N0, depth)
    comps = components(bad, N0)
    out = dict(eps=eps, N0=N0, nbad=len(bad), ncomp=len(comps), boxes=[], clean=True, reason='')
    big = [c for c in comps if len(c) > maxcomp]
    out['sheets'] = [len(c) for c in big]
    bigcells = set().union(*big) if big else set()
    if big and allow_sheets:
        comps = [c for c in comps if len(c) <= maxcomp]
        out['clean'] = False
        out['reason'] = f'sheet component(s) of size {[len(c) for c in big]} coarse cells kept out of boxes'
    elif big:
        out['clean'] = False
        out['reason'] = f'component(s) of size {[len(c) for c in big]} coarse cells: Fermi sheet(s) at this level'
        return out
    boxes = []
    for comp in comps:
        pad = 1
        while True:
            lo, hi = comp_box(comp, N0, pad)
            if box_cells(lo, hi, N0) & bigcells:
                out['clean'] = False; out['reason'] = 'node box meets a sheet component'; return out
            if (hi - lo + 1).max() >= N0:
                out['clean'] = False; out['reason'] = 'box would wrap the torus'; return out
            sh = shell_cells(lo, hi, N0)
            if not (sh & bad):
                break
            pad += 1
            if pad > 4:
                out['clean'] = False; out['reason'] = 'cannot isolate component'; return out
        boxes.append(dict(lo=lo, hi=hi, cells=box_cells(lo, hi, N0), comp=comp))
    # merge overlapping boxes is not attempted: require disjointness
    for i in range(len(boxes)):
        for j in range(i + 1, len(boxes)):
            if boxes[i]['cells'] & boxes[j]['cells']:
                out['clean'] = False; out['reason'] = 'boxes overlap'; return out
    tot = 0
    for b in boxes:
        lo_k = b['lo'] * 2 * np.pi / N0; hi_k = (b['hi'] + 1) * 2 * np.pi / N0
        # choose local cut phi from sampled quasienergies on the box
        g = np.stack(np.meshgrid(*[np.linspace(lo_k[a], hi_k[a], 9) for a in range(3)], indexing='ij'), -1).reshape(-1, 3)
        E = quasi(W(g)).ravel()
        cand = np.linspace(-np.pi, np.pi, 721)[:-1]
        dist = np.array([np.min(np.abs(np.angle(np.exp(1j * (E - c))))) for c in cand])
        dist_eps = np.abs(np.angle(np.exp(1j * (cand - eps))))
        dist[dist_eps < 0.05] = -1
        phi_ok = None
        for c in cand[np.argsort(-dist)][:6]:
            if not certify_cells(W, c, b['cells'], N0, depth):
                phi_ok = c; break
        if phi_ok is None:
            out['clean'] = False; out['reason'] = 'no certified local cut phi'; return out
        phi = eps + np.mod(phi_ok - eps, 2 * np.pi)   # phi in (eps, eps+2pi)
        ch1, r1 = chern_box(W, lo_k, hi_k, eps, phi, M)
        ch2, r2 = chern_box(W, lo_k, hi_k, eps, phi, M + 8)
        b.update(lo_k=lo_k, hi_k=hi_k, phi=phi, ch=ch1, ch2=ch2, rank=r1)
        # nodes inside
        nodes = []
        for c in list(b['comp'])[:60]:
            k0 = (np.array(c) + 0.5) * 2 * np.pi / N0
            kk, s = find_min(W, eps, k0)
            lam = np.linalg.eigvals(W(kk[None])[0])
            dd = np.sort(np.abs(lam - np.exp(-1j * eps)))
            degenerate = len(dd) > 1 and dd[1] < 1e-6
            if s < 1e-7 and degenerate and not any(np.max(np.abs(np.angle(np.exp(1j * (kk - q['k']))))) < 1e-5 for q in nodes):
                chi, v, tilt, oth = weyl_chirality(W, eps, kk)
                nodes.append(dict(k=np.mod(kk, 2 * np.pi), s=s, chi=chi, tilt=tilt, v=v,
                                  gap_others=(oth.min() if len(oth) else np.inf)))
        b['nodes'] = nodes
        # a box is a 'pocket' box if eigenvalue exp(-i eps) occurs there at non-degenerate points
        b['pocket'] = any((lambda kk_s: kk_s[1] < 1e-7 and np.sort(np.abs(np.linalg.eigvals(W(kk_s[0][None])[0]) - np.exp(-1j*eps)))[1] > 1e-4)(find_min(W, eps, (np.array(c) + 0.5) * 2 * np.pi / N0)) for c in list(b['comp'])[:12])
        tot += ch1
        if verbose:
            print(f'    box {np.round(lo_k,3)}..{np.round(hi_k,3)}: phi={phi:.3f} rank(P_<)={r1} Ch={ch1:+.6f} (M+8: {ch2:+.6f});'
                  f' pocket={b["pocket"]} nodes at eps: ' + '; '.join(f"k={np.round(q['k'],5)} chi={q['chi']:+d} |s|={q['s']:.1e} sep_others={q['gap_others']:.2f}" for q in nodes))
    out['boxes'] = boxes
    out['sumCh'] = tot
    return out
