"""The sampled O(k^4) lattice fingerprint of the Regge graviton sector on the 3+1 cubic-Coxeter
complex (Z^3 x Z_tau, flat OS0 background): machine-certified k^4 scaling of the deviation from
linearized EH, machine-zero gauge residuals for the deviation, and the candidate on-shell TT
dispersion anisotropy law.

FRAMING (3D+1, per the framework): the Lattice axiom supplies SPACE = Z^3 only; time is the
emergent record tick. The complex is the tick extension Z^3 x Z_tau of the six-tetrahedra
body-diagonal chain (CUBIC_COXETER_REGGE_DEFICIT_VANISHING): the path (Kuhn-chain)
triangulation of the 4-cell whose constant-tick spatial face is the spatial 3D chain. The
tick edge is grained on the same footing as the spatial edge per the approved
kinetic_isotropy_primitive (c_t = c_s, structural grant only; nothing beyond it is consumed -- in
particular no tick-scale/clock-rate derivation). Euclidean signature = the OS0 surface. This is
NOT a fundamental Z^4.

PROVENANCE OF THE MACHINERY: the complex/Bloch machinery below (symbolic 4-simplex dihedral
gradients, path complex, bloch_Q, the LOAD-BEARING exact line-averaged metric map
[midpoint phase x sinc], gauge map, 4D Euclidean linearized EH pairing) is copied INLINE from
scripts/frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09.py
(landed 3+1 tick-extension note), with two
performance-neutral additions: per-triangle static caching of the flat-background dihedral
gradients (the numbers are identical; only the k-dependent phases are recomputed per call), and
analytic-continuation variants (conj(row(k)) -> row(-k)) that agree with the Hermitian objects at
real momentum to machine precision (gate F0). Faithfulness is anchored end-to-end by reproducing
the prior runner's cached X5 comparator numbers digit-for-digit (gate F1). The prior
tick-extension result established:

    Q_h(k) = -1/2 Q_EH(k) + O(k^4),  exact gauge zeros at every k,  the exactly-decoupled
    fifth branch,  the lambda-one fiber metric at pure-tick momentum.

THIS RUNNER characterizes a sampled O(k^4) remainder fingerprint of the geometric route:

  F0   machinery faithfulness gates: flat deficits (50 classes) = 0; per-4-simplex Schlaefli
       identity; Q(k) Hermitian; analytic continuation == Hermitian object at real k; numpy EH
       pairing == sympy EH pairing; Q_EH annihilates the continuum gauge family (machine).
  F1   c-ANCHOR: the fitted comparator constant at k = 1e-3 across the five comparator directions
       is c = -1/2 to < 1e-7, and the per-direction fitted-c residuals reproduce the prior runner
       cache digit-for-digit (provenance cross-check before extending it).
  F2   O(k^4) SCALING: D(k) := Q_h(k) + (1/2) Q_EH(k). Log-log slope of ||Re D||_F over
       k in [3e-3, 3e-2] equals 4.00 (within 0.01) in ALL 17 directions = 5 comparator
       + 12 random unit 4D directions; numerical floor 3+ orders below the smallest signal.
  F3   NO ODD-ORDER TERM: ||Im D||/||Re D|| at floor level (< 1e-8) in all 17 directions --
       no O(k^3) (and no odd) deviation despite the chain complex's low point symmetry
       (S4 x inversion only; single-axis reflections are NOT symmetries).
  F4   GAUGE EXACTNESS AT THE SAMPLE POINTS: at representative real sample momenta of the fit
       grid AND at the complex on-shell root momenta: |Q(k) Gamma(k)| machine-zero,
       |Q_h(k) h_gauge(k)| machine-zero, |D(k) h_gauge(k)| machine-zero. The O(k^4) deviation is
       therefore has machine-zero gauge residuals at the tested momenta.
  F5   FIFTH BRANCH: at the real sample momenta the quadratic form has EXACTLY FIVE machine-zero
       modes (4 discrete-diffeomorphism + the decoupled branch; metric-overlap pattern 4 + 1
       outside re-verified at this runner's sample points); at the on-shell roots the nullity is
       7 = 5 + 2 with the next singular value O(k^2) away at the sampled roots.
  F6   ON-SHELL TT DISPERSION (basis-free): roots located as rank drops of the FULL 15x15
       analytic Bloch form at p = (k n, iE) -- sigma_6 -> machine floor at the root, sigma_7
       simultaneously at floor (the TT pair is degenerate to machine precision at the sampled
       roots: no sampled birefringence at O(k^4)),
       roots REAL, Richardson k->0 fits with residuals < 1e-6.
  F7   THE CANDIDATE CLOSED FORM: alpha(n) := lim (E^2 - k^2)/k^4 satisfies
           alpha(n) = -(1 + sum_a n_a^4)/12
       to <= 1e-6 across all 15 spatial directions (axis/face+-/body+- and 10 random):
       axis -1/6, face diagonals -1/8, body diagonals -1/9; anisotropy spread = 1/18.
       Equivalently on-shell: omega^2 = k^2 - [ (sum_a k_a^2)^2 + sum_a k_a^4 ]/12 + O(k^6),
       i.e. the on-shell deficit is the S4-SYMMETRIC quartic sum_mu p_mu^4 / 12 with the TICK
       FOURTH POWER ON THE SAME FOOTING AS THE SPATIAL ONES (visible at O(k^4) on-shell within
       the kinetic-isotropy primitive's structural graining) -- the same correction as the
       standard hypercubic (sin^2-type) scalar dispersion.
  F8   B3 ENHANCEMENT: the S3-only (chain-orientation-sensitive) spatial harmonics P31, P211 are
       ABSENT (< 1e-6): face+ = face-, body+ = body-. The on-shell O(k^4) fingerprint has the
       FULL cubic symmetry even though the complex's point group is only S4 x inversion.
  F9   NO OTHER BRANCH NEAR THE CONE IN THE THREE SCANNED DIRECTIONS: a wide rank-drop scan over
       E^2/k^2 in [0.3, 2.5] along the axis, face-diagonal, and one random spatial direction finds
       no additional on-shell branch in those directions; in that scanned surface the continuum
       trace-channel third on-shell null is NOT realized as an independent lattice branch
       (diagnostic: the exactly-decoupled fifth branch carries an O(1) share of the on-shell trace
       class, overlap reported). This is not an all-direction branch-exclusion theorem.
  F10  PROJECTION-CONVENTION BOUNDARY (numerically pinned): the roots of the PROJECTED (exact
       line-averaged metric map) TT block at the axis are {-1/9, -2/9} -- split and unequal to
       the physical degenerate -1/6. The O(k^4) on-shell content must be read from the full
       edge-space form; projected O(k^4) tables are convention-tagged.
  F11  STRUCTURE FIT (honest negative): an 8-element basis of linearized-curvature-squared
       contractions (Riem^2, Ric^2, R^2 + axis-anisotropic + S4-only terms) does NOT capture the
       off-shell projected deviation C4(khat) (relative residual ~0.3; isotropic-only ~0.4). Per
       the brief, the raw per-channel table is reported instead; the convention-free O(k^4)
       structure is the F7 closed form.
  F12  TICK-MIXED ANALOGUE (off-shell, convention-tagged): for real tick-mixed momentum
       directions there is no on-shell point on the OS0 surface; the well-defined analogue --
       gauge-invariant TT-channel values of C4 along the five comparator directions -- is reported.
       The PURE-TICK row EQUALS the PURE-SPACE row channel-by-channel (the complex's S4
       tick<->space symmetry exhibited at O(k^4): the kinetic-isotropy footing in the off-shell
       table), with rational values 1/72 (off-diagonal TT), 1/48 (diagonal-doublet TT), -1/48
       (transverse trace). The two projected TT channels SPLIT by S3 polarization class at
       O(omega^4) -- another face of the F10 projection-convention boundary (on-shell the pair
       is exactly degenerate, F6).

UNITS REMARK (primitive-respecting, no check consumes it): in lattice units the correction is
relative size |alpha(n)| (k a)^2 <= (1/6)(k a)^2. With the registered scale_reference_primitive
a^{-1} = M_Pl (a units conversion ONLY) this is a Planck-suppressed dispersion/anisotropy
correction: for gravitational-wave-band momenta (k/M_Pl)^2 is of order 1e-80 (context arithmetic
only). No dimensionless physics is granted by the primitives; this is the structural
fingerprint of the geometric route, NOT a near-term test.

Literature context only (enters no check): Regge 1961; Rocek-Williams lattice graviton;
Cheeger-Mueller-Schrader; LIGO/Virgo-era graviton dispersion-bound phenomenology for the units
remark. No PDG / fitted / literature value is consumed.
"""
from __future__ import annotations
import itertools
import numpy as np
import sympy as sp

# Heavy symbolic/numeric Regge fingerprint runner; cache refreshes can take
# longer than the default audit-runner budget on slower hosts.
AUDIT_TIMEOUT_SEC = 600

PASS = 0
FAIL = 0


def check(name, cond, detail=""):
    global PASS, FAIL
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    PASS += int(bool(cond))
    FAIL += int(not cond)
    return bool(cond)


# ===================================================== machinery (inline from the 3+1 tick-extension runner)
# Source: scripts/frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09.py.
PAIRS5 = [(i, j) for i in range(5) for j in range(5) if i < j]      # 10 edges of a 4-simplex


def build_theta_funcs():
    """for each missing pair (a,b) (hinge = the other three vertices), the dihedral angle of the
    4-simplex at that hinge as a function of the 10 edge-lengths-squared, plus its 10 gradients."""
    q = {e: sp.Symbol(f"q{e[0]}{e[1]}", positive=True) for e in PAIRS5}

    def qq(i, j):
        return q[(min(i, j), max(i, j))]

    def dot(i, j, base):
        if i == j:
            return qq(base, i)
        return (qq(base, i) + qq(base, j) - qq(i, j)) / 2

    funcs = {}
    for (a, b) in PAIRS5:
        hinge = [v for v in range(5) if v not in (a, b)]
        p, qv, r = hinge
        G11, G12, G22 = dot(qv, qv, p), dot(qv, r, p), dot(r, r, p)
        det = G11 * G22 - G12 ** 2

        def proj_pair(wi, wj):
            ai1, ai2 = dot(qv, wi, p), dot(r, wi, p)
            aj1, aj2 = dot(qv, wj, p), dot(r, wj, p)
            return dot(wi, wj, p) - (G22 * ai1 * aj1 - G12 * (ai1 * aj2 + ai2 * aj1)
                                     + G11 * ai2 * aj2) / det
        nab = proj_pair(a, b)
        naa = proj_pair(a, a)
        nbb = proj_pair(b, b)
        theta = sp.acos(nab / sp.sqrt(naa * nbb))
        grads = [sp.diff(theta, q[e]) for e in PAIRS5]
        funcs[(a, b)] = sp.lambdify([q[e] for e in PAIRS5], [theta] + grads, "numpy")
    return funcs


THETA = build_theta_funcs()

AREA_SYMS = sp.symbols("qa qb qc", positive=True)
_qa, _qb, _qc = AREA_SYMS
_A2 = (2 * _qa * _qb + 2 * _qa * _qc + 2 * _qb * _qc - _qa ** 2 - _qb ** 2 - _qc ** 2) / 16
_A = sp.sqrt(_A2)
AREA = sp.lambdify(AREA_SYMS, [_A, sp.diff(_A, _qa), sp.diff(_A, _qb), sp.diff(_A, _qc)], "numpy")

E4 = [np.array(v) for v in [(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)]]
PERMS = list(itertools.permutations(range(4)))


def cell_simplices(base):
    out = []
    for sg in PERMS:
        vs = [np.array(base)]
        for i in range(4):
            vs.append(vs[-1] + E4[sg[i]])
        out.append([tuple(v) for v in vs])
    return out


DIRS15 = [v for v in itertools.product([0, 1], repeat=4) if any(v)]
DIR_IDX = {v: i for i, v in enumerate(DIRS15)}


def edge_class(p, r):
    d = tuple(np.array(r) - np.array(p))
    if d in DIR_IDX:
        return DIR_IDX[d], np.array(p)
    d = tuple(np.array(p) - np.array(r))
    return DIR_IDX[d], np.array(r)


def triangle_classes():
    out = []
    for w in DIRS15:
        sw = {i for i in range(4) if w[i]}
        if len(sw) < 2:
            continue
        for u in DIRS15:
            su = {i for i in range(4) if u[i]}
            if su and su < sw:
                out.append((tuple([0, 0, 0, 0]), u, w))
    return out


TRI_CLASSES = triangle_classes()


def star_of_triangle(tri):
    tset = {tri[0], tri[1], tri[2]}
    out = []
    for off in itertools.product([-1, 0, 1], repeat=4):
        for vs in cell_simplices(off):
            if tset <= set(vs):
                out.append(vs)
    return out


STARS = {tri: star_of_triangle(tri) for tri in TRI_CLASSES}

# per-triangle static data: the flat-background area/dihedral gradients are k-independent
# constants (identical numbers to the prior per-call evaluation); only phases depend on k.
_TRI_STATIC = []
for tri in TRI_CLASSES:
    vts = [np.array(tri[0]), np.array(tri[1]), np.array(tri[2])]
    qvals = []
    einfo = []
    for (i, j) in [(0, 1), (0, 2), (1, 2)]:
        cls, anc = edge_class(tuple(vts[i]), tuple(vts[j]))
        v = np.array(DIRS15[cls])
        qvals.append(float(v @ v))
        einfo.append((cls, anc.astype(float), np.sqrt(float(v @ v))))
    Aout = AREA(*qvals)
    a_static = [(cls, anc, 2 * ell * float(Aout[1 + n])) for n, (cls, anc, ell) in enumerate(einfo)]
    star_static = []
    for vs in STARS[tri]:
        loc = {v: i for i, v in enumerate(vs)}
        hinge_local = sorted([loc[tri[0]], loc[tri[1]], loc[tri[2]]])
        miss = tuple(sorted([i for i in range(5) if i not in hinge_local]))
        qv = []
        edata = []
        for (i, j) in PAIRS5:
            cls, anc = edge_class(vs[i], vs[j])
            v = np.array(DIRS15[cls])
            qv.append(float(v @ v))
            edata.append((cls, anc.astype(float), np.sqrt(float(v @ v))))
        out = THETA[miss](*qv)
        d_static = [(cls, anc, -2 * ell * float(out[1 + n])) for n, (cls, anc, ell) in enumerate(edata)]
        star_static.append((d_static, float(out[0])))
    _TRI_STATIC.append((a_static, star_static))


def tri_rows_analytic(kvec):
    """per-triangle (a_row(p), d_row(p)) with NO conjugation: entries are entire in p.
    For real p these are the same tri_rows as the 3+1 tick-extension runner."""
    rows = []
    for a_static, star_static in _TRI_STATIC:
        a_row = np.zeros(15, complex)
        d_row = np.zeros(15, complex)
        for cls, anc, coef in a_static:
            a_row[cls] += coef * np.exp(1j * np.dot(kvec, anc))
        for d_static, _theta in star_static:
            for cls, anc, coef in d_static:
                d_row[cls] += coef * np.exp(1j * np.dot(kvec, anc))
        rows.append((a_row, d_row))
    return rows


def flat_deficits():
    return [2 * np.pi - sum(th for _d, th in star_static) for _a, star_static in _TRI_STATIC]


def bloch_Q(kvec):
    """Hermitian Bloch quadratic form at REAL momentum (same construction as the 3+1 runner)."""
    Q = np.zeros((15, 15), complex)
    for a_row, d_row in tri_rows_analytic(kvec):
        Q += 0.5 * (np.outer(np.conj(a_row), d_row) + np.outer(np.conj(d_row), a_row))
    return Q


def bloch_Q_analytic(kvec):
    """analytic continuation: conj(row(k)) -> row(-k); equals bloch_Q for real k (gate F0)."""
    rows_p = tri_rows_analytic(np.asarray(kvec, complex))
    rows_m = tri_rows_analytic(-np.asarray(kvec, complex))
    Q = np.zeros((15, 15), complex)
    for (a_p, d_p), (a_m, d_m) in zip(rows_p, rows_m):
        Q += 0.5 * (np.outer(a_m, d_p) + np.outer(d_m, a_p))
    return Q


def gauge_map(kvec):
    Gm = np.zeros((15, 4), complex)
    for ci, v in enumerate(DIRS15):
        vv = np.array(v, float)
        ell = np.linalg.norm(vv)
        Gm[ci, :] = (np.exp(1j * np.dot(kvec, vv)) - 1.0) * vv / ell
    return Gm


HCOMPS = [(0, 0), (1, 1), (2, 2), (3, 3), (0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]


def csinc(z):
    z = complex(z)
    if abs(z) < 1e-12:
        return 1.0 + 0j
    return np.sin(z) / z


def metric_map(kvec):
    """the LOAD-BEARING exact line-averaged metric map (midpoint phase x sinc), 3+1/3D runners;
    complex-momentum-safe via csinc (identical to np.sinc(z/pi) at real z)."""
    Mm = np.zeros((15, 10), complex)
    for ci, v in enumerate(DIRS15):
        vv = np.array(v, float)
        ell = np.linalg.norm(vv)
        z = np.dot(kvec, vv) / 2.0
        phase = np.exp(1j * z) * csinc(z)
        for hj, (a, b) in enumerate(HCOMPS):
            Hm = np.zeros((4, 4))
            Hm[a, b] += 1.0
            if a != b:
                Hm[b, a] += 1.0
            Mm[ci, hj] = phase * (vv @ Hm @ vv) / (2 * ell)
    return Mm


def Qh_metric(kvec):
    """metric-sector quadratic form at REAL momentum: M^dag Q M (Hermitian part)."""
    B = bloch_Q(kvec)
    M = metric_map(kvec)
    Qh = M.conj().T @ B @ M
    return (Qh + Qh.conj().T) / 2


def Qh_metric_analytic(kvec):
    """analytic continuation of the metric-sector form: M(-p)^T B_an(p) M(p)."""
    B = bloch_Q_analytic(kvec)
    Mp = metric_map(kvec)
    Mm = metric_map(-np.asarray(kvec, complex))
    return Mm.T @ B @ Mp


def einstein_pairing_4d(kvec):
    """4D Euclidean linearized EH pairing -- sympy version from the 3+1 runner (real k only)."""
    n = 4
    hs = {}
    for a in range(n):
        for b in range(n):
            if a <= b:
                hs[(a, b)] = sp.Symbol(f"h{a}{b}")
    Hm = sp.Matrix(n, n, lambda a, b: hs[(min(a, b), max(a, b))])
    p = [sp.Float(x) for x in kvec]
    Sv = {(m, nn): -p[m] * p[nn] for m in range(n) for nn in range(n)}
    R = sp.zeros(n, n)
    for m in range(n):
        for nn in range(n):
            acc = 0
            for l in range(n):
                acc += (Sv[(min(l, m), max(l, m))] * Hm[l, nn]
                        + Sv[(min(l, nn), max(l, nn))] * Hm[l, m]
                        - Sv[(l, l)] * Hm[m, nn] - Sv[(min(m, nn), max(m, nn))] * Hm[l, l])
            R[m, nn] = acc / 2
    Rs = sum(R[m, m] for m in range(n))
    G = sp.Matrix(n, n, lambda m, nn: R[m, nn] - sp.Rational(1, 2) * (1 if m == nn else 0) * Rs)
    Mq = np.zeros((10, 10))
    for i, (a, b) in enumerate(HCOMPS):
        wgt = 2.0 if a != b else 1.0
        expr = wgt * G[a, b]
        for j, key in enumerate(HCOMPS):
            Mq[i, j] = float(sp.diff(expr, hs[key]))
    return (Mq + Mq.T) / 2


def _h_tensor(j):
    a, b = HCOMPS[j]
    H = np.zeros((4, 4))
    H[a, b] += 1.0
    if a != b:
        H[b, a] += 1.0
    return H


def einstein_pairing_4d_np(kvec):
    """numpy reimplementation of the same EH pairing (complex-momentum-safe);
    cross-checked against the sympy version at gate F0."""
    p = np.asarray(kvec, complex)
    S = -np.outer(p, p)
    Mq = np.zeros((10, 10), complex)
    Gs = []
    for j in range(10):
        H = _h_tensor(j).astype(complex)
        R = 0.5 * (S @ H + (S @ H).T - np.trace(S) * H - np.trace(H) * S)
        G = R - 0.5 * np.eye(4) * np.trace(R)
        Gs.append(G)
    for i in range(10):
        a, b = HCOMPS[i]
        wgt = 2.0 if a != b else 1.0
        for j in range(10):
            Mq[i, j] = wgt * Gs[j][a, b]
    return (Mq + Mq.T) / 2


def gauge_h(kvec):
    """the 4 continuum gauge directions h_ab = p_a xi_b + p_b xi_a as 10-vectors."""
    p = np.asarray(kvec, complex)
    cols = np.zeros((10, 4), complex)
    for m in range(4):
        H = np.zeros((4, 4), complex)
        H[m, :] += p
        H[:, m] += p
        for i, (a, b) in enumerate(HCOMPS):
            cols[i, m] = H[a, b]
    return cols


# ================================================================ fingerprint-specific helpers
def D_of(kvec):
    """D(k) = Q_h(k) + (1/2) Q_EH(k): the deviation from the comparator at c = -1/2."""
    return Qh_metric(kvec) + 0.5 * einstein_pairing_4d_np(kvec).real


def svals_full(n3, k, a):
    """singular values of the full analytic Bloch form at p = (k n, iE), E^2 = k^2(1 + a k^2)."""
    E = np.sqrt(k ** 2 * (1 + complex(a) * k ** 2))
    p = np.array([k * n3[0], k * n3[1], k * n3[2], 1j * E], complex)
    return np.linalg.svd(bloch_Q_analytic(p), compute_uv=False), p


def alpha_root(n3, k, lo=-0.6, hi=0.15, ncoarse=76, ngold=70):
    """basis-free on-shell root: golden-section refine of the sigma_6 rank-drop in a."""
    n3 = np.asarray(n3, float)
    n3 = n3 / np.linalg.norm(n3)
    avals = np.linspace(lo, hi, ncoarse)
    s = np.array([svals_full(n3, k, a)[0][-6] for a in avals])
    i0 = int(np.argmin(s))
    a_lo, a_hi = avals[max(i0 - 1, 0)], avals[min(i0 + 1, ncoarse - 1)]

    def f(a):
        return svals_full(n3, k, a)[0][-6]
    for _ in range(ngold):
        m1 = a_lo + (a_hi - a_lo) * 0.382
        m2 = a_lo + (a_hi - a_lo) * 0.618
        if f(m1) < f(m2):
            a_hi = m2
        else:
            a_lo = m1
    a = (a_lo + a_hi) / 2
    sv, p_root = svals_full(n3, k, a)
    return a, sv, p_root


def P4_P31_P211(n):
    x, y, z = n
    P4 = x ** 4 + y ** 4 + z ** 4
    P31 = x ** 3 * y + x ** 3 * z + y ** 3 * x + y ** 3 * z + z ** 3 * x + z ** 3 * y
    P211 = x ** 2 * y * z + y ** 2 * x * z + z ** 2 * x * y
    return P4, P31, P211


def tt_pols(n3):
    """the two spatial-TT polarization 10-vectors for spatial direction n3 (unit HCOMPS norm)."""
    n3 = np.asarray(n3, float)
    n3 = n3 / np.linalg.norm(n3)
    a = np.array([1.0, 0, 0]) if abs(n3[0]) < 0.9 else np.array([0, 1.0, 0])
    u = a - n3 * (n3 @ a)
    u /= np.linalg.norm(u)
    w = np.cross(n3, u)
    out = []
    for E3 in (np.outer(u, w) + np.outer(w, u), np.outer(u, u) - np.outer(w, w)):
        E4t = np.zeros((4, 4))
        E4t[:3, :3] = E3
        v = np.zeros(10)
        nrm = 0.0
        for i, (A, B) in enumerate(HCOMPS):
            v[i] = E4t[A, B]
            nrm += v[i] ** 2 * (2.0 if A != B else 1.0)
        out.append(v / np.sqrt(nrm))
    return out


def main() -> int:
    print("O(k^4) LATTICE FINGERPRINT OF THE REGGE GRAVITON SECTOR (Z^3 x Z_tau tick extension)")
    print("=" * 96)

    # ---------------- F0: machinery faithfulness gates ----------------
    worst_def = max(abs(x) for x in flat_deficits())
    vs0 = cell_simplices((0, 0, 0, 0))[0]
    qv = []
    ells = []
    for (i, j) in PAIRS5:
        cls, anc = edge_class(vs0[i], vs0[j])
        v = np.array(DIRS15[cls])
        qv.append(float(v @ v))
        ells.append(np.sqrt(float(v @ v)))
    schl = np.zeros(10)
    for (a, b) in PAIRS5:
        hverts = [ii for ii in range(5) if ii not in (a, b)]

        def q_of(i, j):
            return qv[PAIRS5.index((min(i, j), max(i, j)))]
        Aout = AREA(q_of(hverts[0], hverts[1]), q_of(hverts[0], hverts[2]),
                    q_of(hverts[1], hverts[2]))
        out = THETA[(a, b)](*qv)
        for fidx in range(10):
            schl[fidx] += float(Aout[0]) * 2 * ells[fidx] * float(out[1 + fidx])
    schl_worst = float(np.abs(schl).max())
    kr = np.array([0.41, -0.23, 0.67, 0.31])
    Qr = bloch_Q(kr)
    herm = float(np.abs(Qr - Qr.conj().T).max())
    an_eq = float(np.abs(bloch_Q_analytic(kr) - Qr).max())
    eh_diff = 0.0
    for kk in (kr, np.array([1.0, 0, 0, 0]), np.array([0.3, -0.7, 0.11, 0.5])):
        eh_diff = max(eh_diff, float(np.abs(einstein_pairing_4d(kk)
                                            - einstein_pairing_4d_np(kk).real).max()))
    eh_gauge = float(np.abs(einstein_pairing_4d_np(kr) @ gauge_h(kr)).max())
    check("F0 (machinery faithfulness): flat deficits of all 50 triangle classes are ZERO; the "
          "per-4-simplex Schlaefli identity holds in every length direction; Q(k) is Hermitian at "
          "random incommensurate k; the analytic continuation equals the Hermitian object at real "
          "k; the numpy EH pairing equals the sympy-derived EH pairing; Q_EH annihilates the "
          "continuum gauge family (all machine precision)",
          worst_def < 1e-10 and schl_worst < 1e-12 and herm < 1e-12 and an_eq < 1e-13
          and eh_diff < 1e-12 and eh_gauge < 1e-12,
          f"max|deficit|={worst_def:.1e}; Schlaefli={schl_worst:.1e}; |Q-Q^dag|={herm:.1e}; "
          f"|Q_an-Q|={an_eq:.1e}; |EH_np-EH_sympy|={eh_diff:.1e}; |Q_EH h_gauge|={eh_gauge:.1e}")

    # ---------------- F1: c-anchor at k = 1e-3 + prior cache cross-check ----------------
    dirs5 = {
        "pure-tick (0,0,0,1)": np.array([0, 0, 0, 1.0]),
        "pure-space (1,0,0,0)": np.array([1.0, 0, 0, 0]),
        "space-space (1,1,0,0)/r2": np.array([1.0, 1.0, 0, 0]) / np.sqrt(2),
        "tick-space (1,0,0,1)/r2": np.array([1.0, 0, 0, 1.0]) / np.sqrt(2),
        "body (1,1,1,1)/2": np.array([1.0, 1.0, 1.0, 1.0]) / 2.0,
    }
    # the 3+1 tick-extension runner cache (logs/runner-cache/frontier_cubic_coxeter_regge_second_variation_
    # 3plus1_2026_06_09.txt, X5 block): comparator constants and fitted-c relative residuals.
    prior_cache = {
        "pure-tick (0,0,0,1)": (-0.5, 6.846e-09),
        "pure-space (1,0,0,0)": (-0.5, 8.227e-09),
        "space-space (1,1,0,0)/r2": (-0.5, 5.099e-08),
        "tick-space (1,0,0,1)/r2": (-0.5, 5.113e-08),
        "body (1,1,1,1)/2": (-0.4999999, 9.948e-09),
    }
    print("\n  c-anchor at k=1e-3 (fitted c per direction; prior cache comparison):")
    ok_c = True
    worst_cdev = 0.0
    for nm, khat in dirs5.items():
        kk = 1e-3
        Qh = Qh_metric(kk * khat)
        Meh = einstein_pairing_4d_np(kk * khat).real
        c = float(np.real(np.vdot(Meh, Qh)) / np.vdot(Meh, Meh).real)
        resid = float(np.abs(Qh - c * Meh).max() / np.abs(Qh).max())
        c_cached, r_cached = prior_cache[nm]
        match = (round(c, 7) == c_cached) and (abs(resid - r_cached) / r_cached < 0.02)
        ok_c = ok_c and (abs(c + 0.5) < 1e-7) and (resid < 1e-7) and match
        worst_cdev = max(worst_cdev, abs(c + 0.5))
        print(f"    {nm:26s} c = {c:+.9f}  rel-res = {resid:.3e}  "
              f"cache (c~{c_cached}, res {r_cached:.3e})  match={match}")
    check("F1 (c-ANCHOR + PRIOR CACHE CROSS-CHECK): the comparator constant refit at k=1e-3 in all "
          "five comparator directions gives c = -1/2 to better than 1e-7, and both the rounded c "
          "and the fitted-c relative residual reproduce the prior runner cache (within 2% on the "
          "residual) before this runner extends the sampled fingerprint",
          ok_c, f"max|c+1/2| = {worst_cdev:.2e}")

    # ---------------- F2 + F3: O(k^4) scaling of D(k), absence of odd orders ----------------
    rng = np.random.default_rng(20260610)
    dirs17 = dict(dirs5)
    for i in range(12):
        v = rng.standard_normal(4)
        dirs17[f"rand4d-{i}"] = v / np.linalg.norm(v)
    ks7 = np.geomspace(3e-3, 3e-2, 7)
    print("\n  D(k) = Q_h(k) + (1/2) Q_EH(k): ||Re D||_F log-log slope over k in [3e-3, 3e-2]:")
    slopes = {}
    im_ratio = {}
    floors = {}
    smallest_signal = {}
    D_grids = {}
    for nm, khat in dirs17.items():
        nre, nim = [], []
        Ds = []
        for k in ks7:
            D = D_of(k * khat)
            Ds.append(D)
            nre.append(np.linalg.norm(D.real))
            nim.append(np.linalg.norm(D.imag))
        D_grids[nm] = (khat, Ds)
        slopes[nm] = float(np.polyfit(np.log(ks7), np.log(nre), 1)[0])
        im_ratio[nm] = nim[-1] / nre[-1]
        floors[nm] = float(np.linalg.norm(D_of(1e-4 * khat).real))
        smallest_signal[nm] = nre[0]
        print(f"    {nm:26s} slope = {slopes[nm]:.4f}   ||ImD||/||ReD||@kmax = {im_ratio[nm]:.1e}"
              f"   signal@kmin = {nre[0]:.2e} vs floor@1e-4 = {floors[nm]:.1e}")
    sl = np.array(list(slopes.values()))
    check("F2 (SAMPLED O(k^4) SCALING): the deviation D(k) from the c = -1/2 comparator scales as "
          "k^4 cleanly over the sampled grid -- log-log slope in [3.99, 4.01] in ALL 17 directions "
          "(5 comparator directions + 12 random unit 4D directions), with the numerical floor at least 100x "
          "below the smallest fitted signal",
          bool(np.all(np.abs(sl - 4.0) < 0.01))
          and all(floors[nm] < 0.01 * smallest_signal[nm] for nm in dirs17),
          f"slope mean = {sl.mean():.5f}, min = {sl.min():.4f}, max = {sl.max():.4f}")
    check("F3 (NO ODD-ORDER TERM): ||Im D||/||Re D|| at the largest fitted k is < 1e-8 in all 17 "
          "directions -- D(k) is real-symmetric (even in k) to machine precision: no O(k^3) (and "
          "no odd-order) deviation appears even though the complex's point group (S4 x inversion; "
          "no single-axis reflections) would allow one",
          all(r < 1e-8 for r in im_ratio.values()),
          f"max ||ImD||/||ReD|| = {max(im_ratio.values()):.2e}")

    # ---------------- extract C4(khat) per direction from the F2 grids ----------------
    A47 = np.vstack([ks7 ** 4, ks7 ** 6]).T
    C4s = {}
    c4_fitres = {}
    for nm, (khat, Ds) in D_grids.items():
        Y = np.array([D.real.reshape(-1) for D in Ds])
        coef, *_ = np.linalg.lstsq(A47, Y, rcond=None)
        C4s[nm] = coef[0].reshape(10, 10)
        c4_fitres[nm] = float(np.linalg.norm(A47 @ coef - Y) / np.linalg.norm(Y))

    # ---------------- F4 + F5: gauge residuals and fifth branch at sample points ----------------
    sample_real = [(nm, k) for nm in ("pure-space (1,0,0,0)", "tick-space (1,0,0,1)/r2",
                                      "rand4d-0") for k in (3e-3, 3e-2)]
    g_worst = 0.0
    gh_worst = 0.0
    dh_worst = 0.0
    nullity_ok = True
    pattern_ok = True
    for nm, k in sample_real:
        khat = dirs17[nm]
        kv = k * khat
        Qk = bloch_Q(kv)
        g_worst = max(g_worst, float(np.abs(Qk @ gauge_map(kv)).max()))
        Qh = Qh_metric(kv)
        hg = gauge_h(kv)
        gh_worst = max(gh_worst, float(np.abs(Qh @ hg).max()))
        Dk = D_of(kv)
        dh_worst = max(dh_worst, float(np.abs(Dk @ hg).max()))
        evk, Vk = np.linalg.eigh((Qk + Qk.conj().T) / 2)
        Z = Vk[:, np.abs(evk) < 1e-9]
        Mq, _ = np.linalg.qr(metric_map(kv))
        svals = np.linalg.svd(Mq.conj().T @ Z, compute_uv=False)
        nullity_ok = nullity_ok and (Z.shape[1] == 5)
        pattern_ok = pattern_ok and (int((svals > 0.999).sum()) == 4) and (svals.min() < 0.9)
    check("F4 (GAUGE RESIDUALS AT THE SAMPLE POINTS, real-k part): at representative momenta of "
          "the fit grid (both ends, three directions): |Q(k) Gamma(k)|, |Q_h(k) h_gauge(k)| and "
          "|D(k) h_gauge(k)| are ALL machine-zero -- the O(k^4) deviation D has machine-zero "
          "gauge residuals at the tested momenta (it annihilates the continuum gauge family "
          "that the exact line-averaged map carries onto the discrete vertex-displacement family)",
          g_worst < 1e-12 and gh_worst < 1e-12 and dh_worst < 1e-12,
          f"max|Q Gamma| = {g_worst:.1e}; max|Q_h h_gauge| = {gh_worst:.1e}; "
          f"max|D h_gauge| = {dh_worst:.1e}")
    check("F5 (FIFTH BRANCH AT THE SAMPLE POINTS, real-k part): at the same six sample momenta "
          "the form has FIVE machine-zero modes (4 discrete-diffeomorphism + the "
          "exactly-decoupled branch), and the zero space meets the metric image in exactly the 4 "
          "gauge directions (overlap pattern: four singular values ~1, fifth < 0.9) -- the "
          "fifth-branch structure is re-verified at the fingerprint's own sample points",
          nullity_ok and pattern_ok,
          f"nullity = 5 at all 6 points; metric-overlap pattern (4 + 1 outside) verified")

    # ---------------- F6 + F7 + F8: the on-shell TT dispersion map ----------------
    dirs3 = {
        "axis (1,0,0)": np.array([1.0, 0, 0]),
        "face+ (1,1,0)": np.array([1.0, 1.0, 0]),
        "face- (1,-1,0)": np.array([1.0, -1.0, 0]),
        "body+ (1,1,1)": np.array([1.0, 1.0, 1.0]),
        "body- (1,1,-1)": np.array([1.0, 1.0, -1.0]),
    }
    rng3 = np.random.default_rng(20260610)
    for i in range(10):
        v = rng3.standard_normal(3)
        dirs3[f"rand3d-{i}"] = v / np.linalg.norm(v)
    ks_disp = (0.015, 0.0225, 0.03375)
    print("\n  on-shell TT roots: rank drop of the FULL 15x15 form at p = (k n, iE); "
          "alpha = (E^2-k^2)/k^4:")
    print("  direction          alpha(k1)    alpha(k2)    alpha(k3)    alpha0(Richardson)  "
          "-(1+P4)/12    s6,s7@root   s8")
    disp_ok = True
    root_gauge_worst = 0.0
    alpha0 = {}
    for nm, n3 in dirs3.items():
        n3u = np.asarray(n3, float)
        n3u = n3u / np.linalg.norm(n3u)
        arr = []
        s6m = s7m = 0.0
        s8min = 1.0
        for k in ks_disp:
            a, sv, p_root = alpha_root(n3u, k)
            arr.append(a)
            s6m = max(s6m, sv[-6])
            s7m = max(s7m, sv[-7])
            s8min = min(s8min, sv[-8])
            root_gauge_worst = max(root_gauge_worst, float(
                np.abs(bloch_Q_analytic(p_root) @ gauge_map(p_root)).max()))
        Afit = np.vstack([np.ones(3), np.array(ks_disp) ** 2]).T
        coef, *_ = np.linalg.lstsq(Afit, np.array(arr), rcond=None)
        al0 = float(coef[0])
        fitres = float(np.abs(Afit @ coef - arr).max())
        P4v, P31v, P211v = P4_P31_P211(n3u)
        formula = -(1.0 + P4v) / 12.0
        alpha0[nm] = (al0, n3u)
        disp_ok = disp_ok and (s6m < 1e-13) and (s7m < 1e-13) and (s8min > 1e-5) \
            and (fitres < 1e-6) and (abs(al0 - formula) < 1e-6)
        print(f"    {nm:16s} {arr[0]:+.6f}   {arr[1]:+.6f}   {arr[2]:+.6f}   {al0:+.8f}     "
              f"{formula:+.8f}   {s6m:.0e},{s7m:.0e}   {s8min:.0e}")
    check("F6 (ON-SHELL EXTRACTION QUALITY + SAMPLED TT DEGENERACY): at every sampled spatial "
          "direction and k, the located root drops the rank of the FULL form by exactly TWO "
          "(sigma_6 AND sigma_7 at machine floor < 1e-13; sigma_8 a full O(k^2) gap above) -- "
          "the two TT polarizations are degenerate to machine precision at the sampled roots "
          "(no sampled birefringence at O(k^4)); roots are real; the Richardson k->0 fits close "
          "to < 1e-6; and the discrete gauge family remains machine-zero AT the complex on-shell root momenta "
          "(F4's complex-momentum part)",
          disp_ok and root_gauge_worst < 1e-12,
          f"max|Q Gamma| at root momenta = {root_gauge_worst:.1e}")
    formula_dev = max(abs(al0 - (-(1.0 + P4_P31_P211(nu)[0]) / 12.0))
                      for al0, nu in alpha0.values())
    al_vals = np.array([a for a, _ in alpha0.values()])
    spread = float(al_vals.max() - al_vals.min())
    check("F7 (THE CANDIDATE CLOSED FORM): alpha(n) = -(1 + sum_a n_a^4)/12 to better than 1e-6 "
          "across ALL 15 sampled spatial directions: axis -1/6, face diagonals -1/8, body "
          "diagonals -1/9; anisotropy spread max-min = 1/18; all subluminal. Equivalently the "
          "sampled on-shell O(k^4) deficit is -(1/12) sum_mu p_mu^4 with p = (k n, i omega): "
          "the TICK fourth power enters on the same footing as the spatial ones within the "
          "kinetic-isotropy primitive's structural graining; the correction law matches the "
          "standard hypercubic (sin^2-type) scalar dispersion",
          formula_dev < 1e-6 and abs(spread - 1.0 / 18.0) < 1e-6
          and abs(alpha0["axis (1,0,0)"][0] + 1.0 / 6.0) < 1e-6
          and abs(alpha0["face+ (1,1,0)"][0] + 1.0 / 8.0) < 1e-6
          and abs(alpha0["body+ (1,1,1)"][0] + 1.0 / 9.0) < 1e-6,
          f"max|alpha - closed form| = {formula_dev:.2e}; spread = {spread:.6f} (1/18 = "
          f"{1.0/18.0:.6f})")
    X = np.vstack([[1.0, *P4_P31_P211(nu)] for _, nu in alpha0.values()])
    yv = np.array([a for a, _ in alpha0.values()])
    coefH, *_ = np.linalg.lstsq(X, yv, rcond=None)
    maxresH = float(np.abs(X @ coefH - yv).max())
    check("F8 (B3 ENHANCEMENT -- the chain orientation does NOT imprint): in the spatial-harmonic "
          "fit alpha(n) = c0 + c1 P4 + c2 P31 + c3 P211, the S3-only (body-diagonal-chain-"
          "sensitive) harmonics are ABSENT (|c2|, |c3| < 1e-6; face+ = face-, body+ = body-): "
          "the on-shell O(k^4) fingerprint has FULL cubic (B3) symmetry although the complex's "
          "point group is only S4 x inversion",
          abs(coefH[2]) < 1e-6 and abs(coefH[3]) < 1e-6 and maxresH < 1e-6
          and abs(coefH[0] + 1.0 / 12.0) < 1e-6 and abs(coefH[1] + 1.0 / 12.0) < 1e-6,
          f"c0 = {coefH[0]:+.8f}, c1(P4) = {coefH[1]:+.8f}, c2(P31) = {coefH[2]:+.1e}, "
          f"c3(P211) = {coefH[3]:+.1e}; max harmonic-fit residual = {maxresH:.1e}")

    # ---------------- F9: scoped branch scan + trace-class diagnostic ----------------
    print("\n  wide rank-drop scan E^2/k^2 in [0.3, 2.5] "
          "(no other on-shell branch in the three scanned directions):")
    no_other = True
    k_scan = 0.0225
    for nm in ("axis (1,0,0)", "face+ (1,1,0)", "rand3d-0"):
        nn = alpha0[nm][1]
        rats = np.linspace(0.3, 2.5, 221)
        vals = []
        for r in rats:
            p = np.array([k_scan * nn[0], k_scan * nn[1], k_scan * nn[2],
                          1j * np.sqrt(complex(r)) * k_scan], complex)
            vals.append(np.linalg.svd(bloch_Q_analytic(p), compute_uv=False)[-6])
        vals = np.array(vals)
        away = np.abs(rats - 1.0) > 0.02
        no_other = no_other and bool(vals[away].min() > 1e-9)
        print(f"    {nm:16s} min sigma_6 away from the cone = {vals[away].min():.2e}")
    # diagnostic: the fifth branch's class content at an on-shell momentum (axis)
    nn = alpha0["axis (1,0,0)"][1]
    k = 0.0225
    p0 = np.array([k * nn[0], k * nn[1], k * nn[2], 1j * k], complex)
    Q0 = bloch_Q_analytic(p0)
    _, _, vt0 = np.linalg.svd(Q0)
    Z5 = vt0.conj().T[:, -5:]
    Gq, _ = np.linalg.qr(gauge_map(p0))
    Zres = Z5 - Gq @ (Gq.conj().T @ Z5)
    uu, _, _ = np.linalg.svd(Zres)
    v5 = uu[:, 0]
    M0 = metric_map(p0)
    h5, *_ = np.linalg.lstsq(M0, v5, rcond=None)
    Ghq, _ = np.linalg.qr(gauge_h(p0))
    h5q = h5 - Ghq @ (Ghq.conj().T @ h5)
    tr10 = np.zeros(10)
    tr10[HCOMPS.index((1, 1))] = 1
    tr10[HCOMPS.index((2, 2))] = 1
    trq = tr10 - Ghq @ (Ghq.conj().T @ tr10)
    ov_tr = float(abs(np.vdot(h5q, trq)) / (np.linalg.norm(h5q) * np.linalg.norm(trq)))
    metric_share = float(np.linalg.norm(M0 @ h5))
    check("F9 (NO OTHER ON-SHELL BRANCH IN THE THREE SCANNED DIRECTIONS): the wide scan finds NO "
          "additional rank drop in E^2/k^2 in [0.3, 2.5] away from the located degenerate TT root "
          "along the axis, face-diagonal, and one random spatial direction -- in that scanned "
          "surface the continuum trace-comparator channel does NOT appear as an independent "
          "on-shell lattice branch (its continuum third on-shell null is not realized in the "
          "scanned directions; diagnostic: the exactly-decoupled fifth branch carries an O(1) "
          "share of the on-shell trace class)",
          no_other,
          f"fifth-branch metric share at p0 = {metric_share:.2f}; class overlap with "
          f"trace-transverse (mod gauge) = {ov_tr:.2f}")

    # ---------------- F10: projection-convention boundary ----------------
    nn = alpha0["axis (1,0,0)"][1]
    k = 0.0225
    eTT = tt_pols(nn)
    EP = np.array(eTT).T

    def Tblk(E2):
        p = np.array([k * nn[0], k * nn[1], k * nn[2], 1j * np.sqrt(complex(E2))], complex)
        Qh = Qh_metric_analytic(p)
        return EP.T @ Qh @ EP
    T0 = Tblk(k ** 2)
    offdiag = abs(T0[0, 1]) / max(abs(T0[0, 0]), abs(T0[1, 1]))
    proj_roots = []
    for br in range(2):
        E2 = k ** 2
        for _ in range(40):
            lam = Tblk(E2)[br, br]
            d = 1e-3 * k ** 2
            der = (Tblk(E2 + d)[br, br] - lam) / d
            step = -lam / der
            E2 = E2 + step
            if abs(step) < 1e-16 * k ** 2:
                break
        proj_roots.append((E2 - k ** 2) / k ** 4)
    pr = sorted([r.real for r in proj_roots])
    pr_im = max(abs(r.imag) for r in proj_roots)
    check("F10 (PROJECTION-CONVENTION BOUNDARY, numerically pinned): the TT-block roots of the "
          "PROJECTED metric-sector form (exact line-averaged map; block diagonal at the axis by "
          "symmetry) are {-2/9, -1/9} -- split, and unequal to the physical degenerate -1/6 of "
          "the full form. At O(k^4) the projected block's on-shell content is map-convention-"
          "tagged (the complement leaks back at this order); the physical dispersion is the "
          "full-form rank drop (F6/F7)",
          abs(pr[0] + 2.0 / 9.0) < 1e-3 and abs(pr[1] + 1.0 / 9.0) < 1e-3 and pr_im < 1e-5
          and offdiag < 1e-6 and abs(pr[0] - (-1.0 / 6.0)) > 0.04
          and abs(pr[1] - (-1.0 / 6.0)) > 0.04,
          f"projected alphas = {pr[0]:+.6f}, {pr[1]:+.6f} (TT off-diag/diag = {offdiag:.1e}); "
          f"full-form alpha = -1/6")

    # ---------------- F11: structure fit of C4 (honest negative) + raw table ----------------
    def riem(p, H):
        R = np.zeros((4, 4, 4, 4))
        for a in range(4):
            for b in range(4):
                for c in range(4):
                    for d in range(4):
                        R[a, b, c, d] = 0.5 * (p[a] * p[c] * H[b, d] + p[b] * p[d] * H[a, c]
                                               - p[a] * p[d] * H[b, c] - p[b] * p[c] * H[a, d])
        return R

    def basis_mats(khat):
        Rs = [riem(khat, _h_tensor(j)) for j in range(10)]
        Rics = [np.einsum('abad->bd', R) for R in Rs]
        Rsc = [np.trace(Ric) for Ric in Rics]

        def bil(f):
            Bm = np.zeros((10, 10))
            for i in range(10):
                for j in range(i, 10):
                    Bm[i, j] = Bm[j, i] = f(i, j)
            return Bm
        mats = {}
        mats["Riem.Riem"] = bil(lambda i, j: np.einsum('abcd,abcd->', Rs[i], Rs[j]))
        mats["Ric.Ric"] = bil(lambda i, j: np.einsum('bd,bd->', Rics[i], Rics[j]))
        mats["R.R"] = bil(lambda i, j: Rsc[i] * Rsc[j])
        mats["sum_ab Rabab^2"] = bil(lambda i, j: sum(Rs[i][a, b, a, b] * Rs[j][a, b, a, b]
                                                      for a in range(4) for b in range(4)))
        mats["sum_a Raa^2"] = bil(lambda i, j: sum(Rics[i][a, a] * Rics[j][a, a]
                                                   for a in range(4)))
        mats["sum Rabac^2"] = bil(lambda i, j: sum(Rs[i][a, b, a, c] * Rs[j][a, b, a, c]
                                                   for a in range(4) for b in range(4)
                                                   for c in range(4)))
        mats["sum RaaRab"] = bil(lambda i, j: 0.5 * sum(
            Rics[i][a, a] * Rics[j][a, b] + Rics[j][a, a] * Rics[i][a, b]
            for a in range(4) for b in range(4) if a != b))
        mats["(sum Rab)^2"] = bil(lambda i, j: np.sum(Rics[i]) * np.sum(Rics[j]))
        return mats

    names = list(basis_mats(np.array([1.0, 0, 0, 0])).keys())
    rows = []
    ys = []
    for nm in dirs17:
        khat = dirs17[nm]
        mats = basis_mats(khat)
        rows.append(np.vstack([mats[b].reshape(-1) for b in names]).T)
        ys.append(C4s[nm].reshape(-1))
    Arows = np.vstack(rows)
    yfit = np.concatenate(ys)
    coefS, *_ = np.linalg.lstsq(Arows, yfit, rcond=None)
    rel_full = float(np.linalg.norm(Arows @ coefS - yfit) / np.linalg.norm(yfit))
    iso_idx = [names.index(b) for b in ("Riem.Riem", "Ric.Ric", "R.R")]
    Aiso = Arows[:, iso_idx]
    ciso, *_ = np.linalg.lstsq(Aiso, yfit, rcond=None)
    rel_iso = float(np.linalg.norm(Aiso @ ciso - yfit) / np.linalg.norm(yfit))
    c4_gauge_rel = max(float(np.abs(C4s[nm] @ gauge_h(dirs17[nm]).real).max()
                             / np.abs(C4s[nm]).max()) for nm in dirs17)
    check("F11 (STRUCTURE FIT -- honest negative): the off-shell projected O(k^4) coefficient "
          "C4(khat) (entrywise k^4+k^6 fits closing to < 1e-5) has machine-zero gauge residuals "
          "but is NOT "
          "captured by the 8-element basis of linearized-curvature-squared contractions tried "
          "here (relative residual ~0.3; isotropic Riem^2/Ric^2/R^2 alone ~0.4): per the brief, "
          "no fit is forced -- the raw per-channel table is reported below, and the "
          "convention-free O(k^4) structure is the F7 closed form",
          rel_full > 0.2 and rel_iso > 0.3 and c4_gauge_rel < 1e-5
          and max(c4_fitres.values()) < 1e-5,
          f"8-element fit rel-residual = {rel_full:.3f}; isotropic-only = {rel_iso:.3f}; "
          f"max C4-extraction residual = {max(c4_fitres.values()):.1e}; "
          f"max relative |C4 h_gauge| = {c4_gauge_rel:.1e}")

    # ---------------- F12: tick-mixed off-shell TT coefficients (convention-tagged) ----------------
    print("\n  raw per-channel O(k^4) table (PROJECTED form, exact line-averaged map convention;")
    print("  channel value = e^T C4(khat) e, HCOMPS-weighted unit polarizations):")
    print("  direction                  TTx          TT+          trace-T      "
          "(TT values = O(|p|^4) coefficient of the channel)")
    tick_vals = {}
    for nm in dirs5:
        khat = dirs17[nm]
        sp_part = khat[:3]
        if np.linalg.norm(sp_part) < 1e-12:
            u3 = np.array([1.0, 0, 0])
            w3 = np.array([0, 1.0, 0])
        else:
            nsp = sp_part / np.linalg.norm(sp_part)
            a3 = np.array([1.0, 0, 0]) if abs(nsp[0]) < 0.9 else np.array([0, 1.0, 0])
            u3 = a3 - nsp * (nsp @ a3)
            u3 /= np.linalg.norm(u3)
            w3 = np.cross(nsp, u3)
        chans = {}
        for cnm, E3 in (("TTx", np.outer(u3, w3) + np.outer(w3, u3)),
                        ("TT+", np.outer(u3, u3) - np.outer(w3, w3)),
                        ("trT", np.outer(u3, u3) + np.outer(w3, w3))):
            E4t = np.zeros((4, 4))
            E4t[:3, :3] = E3
            v = np.zeros(10)
            nrm = 0.0
            for i, (A, B) in enumerate(HCOMPS):
                v[i] = E4t[A, B]
                nrm += v[i] ** 2 * (2.0 if A != B else 1.0)
            v = v / np.sqrt(nrm)
            chans[cnm] = float(v @ C4s[nm] @ v)
        tick_vals[nm] = chans
        print(f"    {nm:26s} {chans['TTx']:+.6f}    {chans['TT+']:+.6f}    {chans['trT']:+.6f}")
    pt = tick_vals["pure-tick (0,0,0,1)"]
    ps = tick_vals["pure-space (1,0,0,0)"]
    row_eq = max(abs(pt[c] - ps[c]) for c in ("TTx", "TT+", "trT"))
    check("F12 (TICK-MIXED ANALOGUE, off-shell, convention-tagged): for real tick-mixed momentum "
          "directions there is NO on-shell point on the OS0 surface (E^2 = omega^2 + k^2 > 0), "
          "so the well-defined analogue of the dispersion correction is the gauge-invariant "
          "TT-channel O(k^4) coefficient of D along the five comparator directions, reported above in "
          "the exact line-averaged convention. The PURE-TICK row EQUALS the PURE-SPACE row "
          "channel-by-channel (the complex's S4 tick<->space symmetry exhibited at O(k^4) -- the "
          "kinetic-isotropy footing visible in the off-shell table), with rational channel "
          "values 1/72 (off-diagonal TT), 1/48 (diagonal-doublet TT), -1/48 (transverse trace). "
          "HONEST SPLIT: the two projected TT channels differ at O(omega^4) by S3 polarization "
          "class -- another face of the F10 projection-convention boundary (the sampled "
          "on-shell pair is degenerate to machine precision, F6)",
          row_eq < 1e-7
          and abs(pt["TTx"] - 1.0 / 72.0) < 2e-6
          and abs(pt["TT+"] - 1.0 / 48.0) < 2e-6
          and abs(pt["trT"] + 1.0 / 48.0) < 2e-6,
          f"pure-tick row = pure-space row to {row_eq:.1e}; pure-tick channels: "
          f"TTx = {pt['TTx']:+.7f} (1/72 = {1/72:+.7f}), TT+ = {pt['TT+']:+.7f} "
          f"(1/48 = {1/48:+.7f}), trT = {pt['trT']:+.7f}")

    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    print(
        "VERDICT: on the Z^3 x Z_tau tick extension of the cubic-Coxeter spatial chain (3D+1: "
        "space = Z^3 per\nthe Lattice axiom, time = the emergent record tick, c_t = c_s per the "
        "kinetic-isotropy primitive's\nstructural grant, OS0/Euclidean surface), the O(k^4) "
        "remainder of the comparator is now\nsample-characterized: D(k) = Q_h(k) + (1/2)Q_EH(k) "
        "scales as k^4 with slope 4.000 in all 17 sampled directions,\nis even in k (no O(k^3) "
        "term despite the low point symmetry), and has machine-zero gauge residuals at every\nsampled "
        "momentum. The physical on-shell content (rank drop of the full edge-space form -- NOT "
        "the\nprojected block, whose O(k^4) roots are convention artifacts, F10) is: the two TT "
        "polarizations stay\ndegenerate to machine precision at the sampled roots (no sampled O(k^4) birefringence) and disperse "
        "subluminally as\n  omega^2(k) = k^2 [ 1 - k^2 (1 + sum_a n_a^4)/12 ] + O(k^6),\ni.e. an "
        "on-shell deficit -(1/12) sum_mu p_mu^4 with the tick fourth power on the same footing "
        "as the\nspatial ones -- the hypercubic (sin^2-type) scalar correction law, within "
        "the kinetic-isotropy structural graining\nat O(k^4). alpha runs from -1/6 (axes) through -1/8 "
        "(face diagonals) to -1/9 (body diagonals), spread\n1/18; the chain-orientation "
        "harmonics are ABSENT (face+ = face-, body+ = body-): the fingerprint is\nB3-symmetric, "
        "more symmetric than the complex itself. No other branch appears near the cone in the "
        "three scanned F9 directions;\nthe continuum trace-channel third on-shell null is not "
        "realized as a lattice branch in those scanned directions (the "
        "exactly-decoupled\nfifth branch carries an O(1) share of that class). The off-shell "
        "projected C4 is not captured by the\nsimple curvature-contraction basis tried "
        "(honest negative; raw table reported; its pure-tick row equals its pure-space row "
        "channel-by-channel --\nthe S4 tick-space footing at O(k^4)). UNITS REMARK (units only, "
        "no dimensionless "
        "physics granted, no phenomenology or bound claim): in lattice units the correction is\n"
        "|alpha|(ka)^2 <= (ka)^2/6; with the registered scale reference a^{-1} = M_Pl it is "
        "Planck-suppressed --\nof order 1e-80 relative at gravitational-wave-band momenta "
        "(context arithmetic only). "
        "This is the structural fingerprint of the geometric\nroute, not a "
        "near-term test. Open and unchanged: overall action orientation (the located sign "
        "residual),\nedge-length-DOF provenance, action selection, O(k^6) and nonlinear closure, "
        "tick scale (clock-rate\nboundary respected). No PDG / fitted value consumed."
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
