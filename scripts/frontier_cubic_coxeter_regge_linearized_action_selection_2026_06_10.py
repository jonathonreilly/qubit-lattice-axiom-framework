"""Linearized action-selection certificate on the 3+1 cubic-Coxeter complex.

Embedding-inertness plus declared locality put the leading metric-sector
quadratic form in the background-metric Einstein-Hilbert class.

THE QUESTION (the named-open "action selection" item of the Regge second-variation rows): WHY S_R?
What singles out the Regge action among local edge-length functionals? This runner proves and
demonstrates the LINEARIZED-LEVEL answer on the framework's own complex (Z^3 x Z_tau, the tick
extension of the retained six-tetrahedra chain; 3D+1 framing: space = Z^3 by the Lattice axiom, time =
the emergent record tick; c_t = c_s per the kinetic_isotropy_primitive, structural grant only;
Euclidean = the OS0 surface).

SELECTION HYPOTHESIS (framework-native, but not derived here): the Lattice axiom
supplies ADJACENCY, not an embedding; vertex positions are not part of the
axiom data. This runner studies the added embedding-inertness hypothesis that
flat-space vertex displacements are exact zero modes at every momentum.
Locality = the declared finite stencil.

THE THEOREM (runner-verified):
  Continuum nullspace (no isotropy assumed): the space of quadratic forms M(k) on the 10
      metric components, entries quadratic in k with ARBITRARY (cubic-anisotropy-allowing) constant
      coefficients, satisfying the gauge annihilation M(k) hvec(k o xi) = 0 for all (k, xi), is
      ten-dimensional by exact polynomial-coefficient rank, containing the linearized EH form.
  Background-metric identification: the ten-dimensional space is the background-metric EH class -- one
      linearized EH form per constant flat background metric g (GL(4) covariance: h -> L^T h L maps
      gauge families to gauge families, so the pullbacks F_L(k) = T_L^T M_EH(L^T k) T_L are all
      gauge-annihilating; their span has rank 10 and coincides with the continuum nullspace). Within
      this declared O(k^2) ansatz, the only leading freedom beyond one overall constant is WHICH
      flat background metric (anisotropy/units data); mass terms are excluded.
  Lattice bridge (embedding-inertness + locality => the continuum nullspace applies): (a) the hypothesis
      implies the flatness
      zero modes -- expanding Q'(k) Gamma(k) = 0 at O(k), the small-k gauge family spans the constant-h
      metric image, forcing Q'(0) M(0) = 0 (verified on every constructed H-form); (b) the exact
      line-averaged metric map satisfies M(k) h_gauge = Gamma(k) xi EXACTLY (the line-average lemma),
      so the direct metric pullback P(k) of any embedding-inert form annihilates the continuum gauge
      family exactly at every k; its O(k^2) coefficient is therefore in the background-metric EH class.
  Declared-stencil family probe: construct the sampled local lattice
      quadratic forms with stencil {0, +-e_mu, +-(e_mu+e_nu)} satisfying H (nullspace of the sampled
      constraint system), draw random elements, and verify EVERY one's P_2 is fit by a SINGLE element
      of the ten-dimensional EH class across all test directions simultaneously.
  Regge instantiation: the Regge action S_R is one embedding-inert form; its direct P_2 = -1/2 x EH at the isotropic
      background g = delta -- the complex's own flat metric (lengths {1,sqrt2,sqrt3,2} realize delta;
      the tick enters on equal footing per the kinetic-isotropy primitive) -- in tick, space, AND a
      previously untested mixed direction. The geometric action selects the background the complex is
      built on; the constant matches the textbook delta^2 S_R = (1/2) delta^2 int sqrt(g) R.
  Higher-order freedom witness: the DEFICIT-SQUARED form (the discrete curvature-squared
      term) is local, exactly gauge-annihilating, nonzero, and has ZERO leading content -- the
      higher-curvature lattice freedom starts at O(k^4); the selection is leading-order only.
  Mass-term control: a mass-term form violates the embedding-inertness hypothesis (O(1) gauge
      residual) -- the hypothesis is load-bearing.

NET: "why S_R" at the linearized level = ANY local edge-length action that respects the Lattice
axiom's adjacency-only character by satisfying the embedding-inertness hypothesis has EH-class
leading-order linearized physics; the leading freedom is {one overall constant} + {the flat background
metric}. The complex's own flat geometry + the kinetic-isotropy primitive fix the background to the
isotropic delta for the Regge instantiation, and the Regge action realizes it with c = -1/2. The
remaining action-selection gap is: the constant's
orientation+magnitude (the located sign residual + the registered scale reference), the O(k^4) tail,
and the nonlinear completion. Machinery inlined from the landed 3+1 tick-extension runner. No
PDG/fitted value.
"""
from __future__ import annotations
import itertools
import numpy as np
import sympy as sp

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


# ================= machinery inlined from frontier_cubic_coxeter_regge_second_variation_3plus1
# (the landed 3+1 tick-extension runner) =================
PAIRS5 = [(i, j) for i in range(5) for j in range(5) if i < j]


def build_theta_funcs():
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
            return dot(wi, wj, p) - (G22 * ai1 * aj1 - G12 * (ai1 * aj2 + ai2 * aj1) + G11 * ai2 * aj2) / det

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
_A = sp.sqrt((2 * _qa * _qb + 2 * _qa * _qc + 2 * _qb * _qc - _qa ** 2 - _qb ** 2 - _qc ** 2) / 16)
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
STARS = {}
for tri in TRI_CLASSES:
    tset = {tri[0], tri[1], tri[2]}
    st = []
    for off in itertools.product([-1, 0, 1], repeat=4):
        for vs in cell_simplices(off):
            if tset <= set(vs):
                st.append(vs)
    STARS[tri] = st


def tri_rows(tri, kvec):
    a_row = np.zeros(15, complex)
    d_row = np.zeros(15, complex)
    vts = [np.array(tri[0]), np.array(tri[1]), np.array(tri[2])]
    qvals = []
    einfo = []
    for (i, j) in [(0, 1), (0, 2), (1, 2)]:
        cls, anc = edge_class(tuple(vts[i]), tuple(vts[j]))
        v = np.array(DIRS15[cls])
        qvals.append(float(v @ v))
        einfo.append((cls, anc, np.sqrt(float(v @ v))))
    Aout = AREA(*qvals)
    for n, (cls, anc, ell) in enumerate(einfo):
        a_row[cls] += 2 * ell * float(Aout[1 + n]) * np.exp(1j * np.dot(kvec, anc))
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
            edata.append((cls, anc, np.sqrt(float(v @ v))))
        out = THETA[miss](*qv)
        for n, (cls, anc, ell) in enumerate(edata):
            d_row[cls] -= 2 * ell * float(out[1 + n]) * np.exp(1j * np.dot(kvec, anc))
    return a_row, d_row


def bloch_Q_regge(kvec):
    Q = np.zeros((15, 15), complex)
    for tri in TRI_CLASSES:
        a_row, d_row = tri_rows(tri, kvec)
        Q += 0.5 * (np.outer(np.conj(a_row), d_row) + np.outer(np.conj(d_row), a_row))
    return Q


def gauge_map(kvec):
    Gm = np.zeros((15, 4), complex)
    for ci, v in enumerate(DIRS15):
        vv = np.array(v, float)
        ell = np.linalg.norm(vv)
        Gm[ci, :] = (np.exp(1j * np.dot(kvec, vv)) - 1.0) * vv / ell
    return Gm


HCOMPS = [(0, 0), (1, 1), (2, 2), (3, 3), (0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]


def metric_map(kvec):
    Mm = np.zeros((15, 10), complex)
    for ci, v in enumerate(DIRS15):
        vv = np.array(v, float)
        ell = np.linalg.norm(vv)
        z = np.dot(kvec, vv) / 2.0
        phase = np.exp(1j * z) * np.sinc(z / np.pi)
        for hj, (a, b) in enumerate(HCOMPS):
            Hm = np.zeros((4, 4))
            Hm[a, b] += 1.0
            if a != b:
                Hm[b, a] += 1.0
            Mm[ci, hj] = phase * (vv @ Hm @ vv) / (2 * ell)
    return Mm


def einstein_pairing_4d(kvec):
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
# ================= end inlined machinery =================


def hvec_of(H4):
    return np.array([H4[a, b] for (a, b) in HCOMPS])


def gauge_h(kv, xi):
    H4 = np.outer(kv, xi) + np.outer(xi, kv)
    return hvec_of(H4)


# ---------------------------------------------------------------- continuum classification
KP = [(e, f) for e in range(4) for f in range(4) if e <= f]          # 10 k-monomials
NPAR_PAIRS = [(i, j) for i in range(10) for j in range(i, 10)]       # 55 symmetric (i,j)
NP_S1 = len(NPAR_PAIRS) * len(KP)                                    # 550


def s1_exact_coefficient_rank():
    """Exact rank of the polynomial coefficient equations for M(k) h_gauge(k, xi)=0."""
    degree3 = []
    for a in range(4):
        for b in range(a, 4):
            for c in range(b, 4):
                exp = [0] * 4
                exp[a] += 1
                exp[b] += 1
                exp[c] += 1
                degree3.append(tuple(exp))

    row_index = {
        (out, xi, mono): idx
        for idx, (out, xi, mono) in enumerate(
            (out, xi, mono)
            for out in range(10)
            for xi in range(4)
            for mono in degree3
        )
    }
    entries = {}

    def add_k(base, kidx):
        exp = list(base)
        exp[kidx] += 1
        return tuple(exp)

    for pi, (a, b) in enumerate(NPAR_PAIRS):
        for m, (e, f) in enumerate(KP):
            base = [0] * 4
            base[e] += 1
            base[f] += 1
            col = pi * len(KP) + m
            out_js = [(a, b)] if a == b else [(a, b), (b, a)]
            for out, j in out_js:
                p, q = HCOMPS[j]
                terms = [(p, p, 2)] if p == q else [(p, q, 1), (q, p, 1)]
                for kidx, xiidx, coef in terms:
                    row = row_index[(out, xiidx, add_k(base, kidx))]
                    entries[(row, col)] = entries.get((row, col), 0) + coef

    mat = sp.SparseMatrix(len(row_index), NP_S1, entries)
    rank = int(mat.rank())
    return rank, NP_S1 - rank, mat.shape


def eval_T_form(T, kv):
    """evaluate a 550-parameter T-vector as the 10x10 form M(k)."""
    km = np.array([kv[e] * kv[f] for (e, f) in KP])
    M = np.zeros((10, 10))
    for pi, (a, b) in enumerate(NPAR_PAIRS):
        val = float(km @ T[pi * len(KP):(pi + 1) * len(KP)])
        M[a, b] += val
        if a != b:
            M[b, a] += val
    return M


def TL_rep(L):
    """10x10 representation of h -> L^T h L on the metric components."""
    T = np.zeros((10, 10))
    for j, (c, d) in enumerate(HCOMPS):
        Hm = np.zeros((4, 4))
        Hm[c, d] += 1.0
        if c != d:
            Hm[d, c] += 1.0
        Ht = L.T @ Hm @ L
        for i, (a, b) in enumerate(HCOMPS):
            T[i, j] = Ht[a, b]
    return T


def s1_continuum_uniqueness():
    npar_pairs = NPAR_PAIRS
    NP = NP_S1
    rng = np.random.default_rng(3)
    rows = []
    for _ in range(220):
        kv = rng.standard_normal(4)
        xi = rng.standard_normal(4)
        w = gauge_h(kv, xi)                                           # 10-vector
        km = np.array([kv[e] * kv[f] for (e, f) in KP])               # 10 monomials
        # condition rows: for each i: sum_j M_ij w_j = 0, M_ij = sum_m T[(i,j),m] km[m]
        for i in range(10):
            row = np.zeros(NP)
            for pi, (a, b) in enumerate(npar_pairs):
                if a == i or b == i:
                    j = b if a == i else a
                    fac = 1.0
                    row[pi * len(KP):(pi + 1) * len(KP)] += fac * w[j] * km
            rows.append(row)
    Acon = np.array(rows)
    _, sv, Vt = np.linalg.svd(Acon, full_matrices=True)
    svf = np.concatenate([sv, np.zeros(NP - len(sv))])
    cand = Vt[svf < 1e-6 * sv[0]].T          # generous candidate set, then STRICT fresh-sample filter
    true_cols = []
    for c in range(cand.shape[1]):
        T = cand[:, c]
        worst = 0.0
        for _ in range(60):
            kv = rng.standard_normal(4)
            xi = rng.standard_normal(4)
            w = gauge_h(kv, xi)
            km = np.array([kv[e] * kv[f] for (e, f) in KP])
            for i in range(10):
                val = 0.0
                for pi, (a, b) in enumerate(npar_pairs):
                    if a == i or b == i:
                        j = b if a == i else a
                        val += w[j] * float(km @ T[pi * len(KP):(pi + 1) * len(KP)])
                worst = max(worst, abs(val))
        if worst < 1e-9:
            true_cols.append(cand[:, c])
    null_dim = len(true_cols)
    null_basis = (np.stack(true_cols, axis=1) if true_cols else np.zeros((NP, 0)))
    if null_basis.shape[1] > 0:
        null_basis, _ = np.linalg.qr(null_basis)
    # embed EH: extract its T-coefficients by evaluating M_EH(k) at monomial-separating k samples
    # (simpler: verify EH is IN the nullspace by checking its gauge annihilation + projecting onto basis)
    # build EH's parameter vector by least squares: M_EH(k)_{ij} = sum_m T km
    ks = [rng.standard_normal(4) for _ in range(30)]
    rowsE = []
    rhsE = []
    for kv in ks:
        ME = einstein_pairing_4d(kv)
        km = np.array([kv[e] * kv[f] for (e, f) in KP])
        for pi, (a, b) in enumerate(npar_pairs):
            pass
        for i in range(10):
            for j in range(i, 10):
                pi = npar_pairs.index((i, j))
                r = np.zeros(NP)
                r[pi * len(KP):(pi + 1) * len(KP)] = km
                rowsE.append(r)
                rhsE.append(ME[i, j])
    T_EH, res, _, _ = np.linalg.lstsq(np.array(rowsE), np.array(rhsE), rcond=None)
    fit_res = float(np.sqrt(np.sum((np.array(rowsE) @ T_EH - np.array(rhsE)) ** 2)))
    # is T_EH in the nullspace? residual of constraints:
    eh_con = float(np.abs(Acon @ T_EH).max())
    # projection onto nullspace basis:
    proj = null_basis @ (null_basis.T @ T_EH)
    in_null = float(np.linalg.norm(T_EH - proj) / np.linalg.norm(T_EH))
    return null_dim, eh_con, in_null, fit_res, null_basis


# ---------------------------------------------------------------- lattice embedding-inert family construction
HALF_OFFSETS = ([np.array(o) for o in [(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)]]
                + [np.array(E4[m]) + np.array(E4[nn]) for m in range(4) for nn in range(m + 1, 4)])


def family_Q(theta_params, kvec):
    """Q'(k) = C0 + sum_half [C_D e^{ik.D} + C_D^T e^{-ik.D}]; params packed [C0_sym(120), C_D(225)x10]."""
    idx = 0
    C0 = np.zeros((15, 15))
    iu = np.triu_indices(15)
    C0[iu] = theta_params[:120]
    C0 = C0 + np.triu(C0, 1).T
    idx = 120
    Q = C0.astype(complex)
    for D in HALF_OFFSETS:
        CD = theta_params[idx:idx + 225].reshape(15, 15)
        idx += 225
        ph = np.exp(1j * np.dot(kvec, D))
        Q = Q + CD * ph + CD.T * np.conj(ph)
    return Q


NPAR_LAT = 120 + 225 * len(HALF_OFFSETS)


def s2_build_family(n_samples=900, seed=7):
    rng = np.random.default_rng(seed)
    # accumulate normal equations for the linear constraints Q'(k) Gamma(k) = 0 (re+im)
    N = np.zeros((NPAR_LAT, NPAR_LAT))
    for s in range(n_samples):
        kv = rng.uniform(-np.pi, np.pi, 4)
        G = gauge_map(kv)                       # 15x4
        # constraint rows: [Q'(k) G]_{c,d} = sum over params of (coef) -- build coefficient tensor
        # row for (c,d): contributions: C0[c,:] G[:,d]; CD[c,:]G[:,d] ph + CD^T[c,:]G[:,d] conj(ph)
        # vectorized assembly:
        rowsR = np.zeros((60, NPAR_LAT))
        rowsI = np.zeros((60, NPAR_LAT))
        rc = 0
        Gd = G                                  # (15,4)
        for c in range(15):
            for d in range(4):
                rr = np.zeros(NPAR_LAT, complex)
                # C0 part: C0[c,j] G[j,d]; C0 symmetric packed on triu
                v = np.zeros((15, 15), complex)
                v[c, :] += Gd[:, d]
                vs = v + v.T - np.diag(np.diag(v))   # map full coefficient to sym-packed convention
                rr[:120] = vs[np.triu_indices(15)]
                idx = 120
                for D in HALF_OFFSETS:
                    ph = np.exp(1j * np.dot(kv, D))
                    block = np.zeros((15, 15), complex)
                    block[c, :] += Gd[:, d] * ph          # CD e^{ikD} term: CD[c,j]
                    block[:, c] += Gd[:, d] * np.conj(ph)  # CD^T term: CD[j,c]
                    rr[idx:idx + 225] = block.reshape(-1)
                    idx += 225
                rowsR[rc] = rr.real
                rowsI[rc] = rr.imag
                rc += 1
        A = np.vstack([rowsR, rowsI])
        N += A.T @ A
    return N


def extract_P2(Qfun, khat, kk=1e-3):
    """DIRECT metric-sector pullback P(k)/k^2 with the exact line-averaged map. This is the
    theorem-clean object: by the line-average lemma M(k) h_gauge = Gamma(k) xi exactly, so for any
    embedding-inert form P(k) h_gauge(k) = 0 identically in k; hence the O(k^2) coefficient satisfies
    the continuum gauge condition and lies in the continuum nullspace. (A Schur reduction over the non-metric complement is a
    slice-scheme variant; for the Regge form the two were measured to agree at generic momenta in the
    second-variation rows. A naive pseudo-inverse Schur is UNRELIABLE here because the exactly
    decoupled fifth branch leaks an O(k^2) eigenvalue into the complement, which fakes an O(1) shift
    in special directions -- a diagnosed numerical artifact, excluded from the claims.)"""
    kv = kk * khat
    Qk = Qfun(kv)
    Mk = metric_map(kv)
    P = Mk.conj().T @ Qk @ Mk
    return np.real((P + P.conj().T) / 2) / kk ** 2


def main() -> int:
    print("LINEARIZED ACTION SELECTION ON THE 3+1 CUBIC-COXETER COMPLEX (Z^3 x Z_tau)")
    print("=" * 96)
    rng = np.random.default_rng(42)

    # ---- Continuum classification ----
    exact_rank, exact_nullity, exact_shape = s1_exact_coefficient_rank()
    null_dim, eh_con, in_null, fit_res, NULLB = s1_continuum_uniqueness()
    check("continuum coefficient rank: the exact polynomial equations for M(k) h_gauge(k,xi)=0 "
          "on the 550-parameter O(k^2) ansatz have nullity ten",
          exact_shape == (800, 550) and exact_rank == 540 and exact_nullity == 10,
          f"coefficient matrix shape = {exact_shape}; exact rank = {exact_rank}; nullity = {exact_nullity}")
    check("continuum nullspace check (no isotropy assumed): among ALL quadratic forms on the 10 "
          "metric components with entries quadratic in k and arbitrary constant coefficients (550 "
          "parameters, cubic-anisotropic structures included), the gauge-annihilation condition "
          "M(k) h_gauge(k,xi) = 0 for all (k,xi) leaves a TEN-dimensional family (strictly "
          "filtered against fresh samples), containing the in-runner-derived linearized EH pairing",
          exact_nullity == 10 and null_dim == 10 and eh_con < 1e-8 and in_null < 1e-8 and fit_res < 1e-10,
          f"nullspace dim = {null_dim}; EH gauge-residual = {eh_con:.1e}; EH outside-nullspace fraction = "
          f"{in_null:.1e}; EH T-fit residual = {fit_res:.1e}")

    # ---- Background-metric identification ----
    # GL(4) covariance: under h -> L^T h L the gauge family at wavevector k maps to the gauge family at
    # L^T k (verified inline), so F_L(k) := T_L^T M_EH(L^T k) T_L is gauge-annihilating for every
    # invertible L -- one linearized-EH form per constant flat background metric g = L^T L (10
    # parameters). Span test: the GL-pullback family spans exactly the ten-dimensional continuum space.
    probes = [rng.standard_normal(4) for _ in range(12)]
    def feature_of_func(Mfun):
        return np.concatenate([Mfun(kp).ravel() for kp in probes])
    feats_null = np.stack([feature_of_func(lambda kv, T=NULLB[:, j]: eval_T_form(T, kv))
                           for j in range(NULLB.shape[1])])
    feats_g = []
    worst_gauge_FL = 0.0
    for _ in range(40):
        L = np.eye(4) + 0.5 * rng.standard_normal((4, 4))
        TL = TL_rep(L)
        def FL(kv, L=L, TL=TL):
            return TL.T @ einstein_pairing_4d(L.T @ kv) @ TL
        # fresh gauge check for this pullback form
        kv = rng.standard_normal(4)
        xi = rng.standard_normal(4)
        worst_gauge_FL = max(worst_gauge_FL, float(np.abs(FL(kv) @ gauge_h(kv, xi)).max()))
        feats_g.append(feature_of_func(FL))
    feats_g = np.stack(feats_g)
    r_null = np.linalg.matrix_rank(feats_null, tol=1e-8 * np.linalg.norm(feats_null))
    r_g = np.linalg.matrix_rank(feats_g, tol=1e-8 * np.linalg.norm(feats_g))
    r_joint = np.linalg.matrix_rank(np.vstack([feats_null, feats_g]),
                                    tol=1e-8 * np.linalg.norm(feats_null))
    check("background-metric identification: every GL(4) pullback "
          "F_L(k) = T_L^T M_EH(L^T k) T_L is gauge-annihilating (h -> L^T h L maps gauge families to "
          "gauge families, fresh-sample verified), i.e. one linearized EH form per constant flat "
          "background metric g = L^T L; the span of random pullbacks has rank 10 and COINCIDES with the "
          "continuum nullspace (joint rank still 10). Within this declared O(k^2) ansatz, gauge "
          "annihilation + locality admit the EH class -- the only leading-order freedom beyond one "
          "overall constant is WHICH constant flat background metric (= anisotropy/units data). Mass "
          "terms are excluded because the family is O(k^2) by construction and the lattice bridge covers k=0.",
          worst_gauge_FL < 1e-9 and r_null == 10 and r_g == 10 and r_joint == 10,
          f"pullback gauge-residual = {worst_gauge_FL:.1e}; rank(nullspace feats) = {r_null}, "
          f"rank(pullback feats) = {r_g}, joint rank = {r_joint}")

    # ---- Lattice embedding-inert family ----
    print("  building the sampled embedding-inert lattice family (stencil {0, +-e_mu, +-(e_mu+e_nu)}, "
          f"{NPAR_LAT} parameters)...")
    Nmat = s2_build_family()
    evals, evecs = np.linalg.eigh(Nmat)
    tolN = max(1e-10 * evals[-1], 1e-12)
    null_mask = evals < tolN
    fam_dim = int(null_mask.sum())
    FAM = evecs[:, null_mask]
    check("declared-stencil lattice family is nonempty and finite-dimensional: the sampled space of local lattice "
          "quadratic forms on the 15 edge classes (declared stencil) whose vertex-displacement family "
          "consists of exact zero modes at sampled momenta has the reported dimension (constraint system "
          "sampled at 900 random momenta, 60 complex conditions each; nullspace by eigendecomposition)",
          fam_dim >= 2,
          f"family dimension = {fam_dim} (of {NPAR_LAT} parameters)")

    # ---- Lattice flatness bridge ----
    M0 = metric_map(np.zeros(4)).real
    worst_flat = 0.0
    for t in range(min(8, fam_dim)):
        th = FAM @ rng.standard_normal(fam_dim)
        Q0 = family_Q(th, np.zeros(4)).real
        worst_flat = max(worst_flat, float(np.abs(Q0 @ M0).max() / max(1e-30, np.abs(Q0).max())))
    check("lattice flatness bridge: for random elements of the embedding-inert family, constant "
          "metric perturbations are automatically zero modes at k=0 (Q'(0) M(0) = 0) -- the O(k) "
          "expansion of the gauge condition spans the constant-h metric image, so no separate flatness "
          "hypothesis is needed on the metric sector",
          worst_flat < 1e-6,
          f"max relative |Q'(0) M_metric| over samples = {worst_flat:.1e}")

    # ---- Direct metric-sector pullback ----
    DIRS_TEST = [np.array([0, 0, 0, 1.0]), np.array([1.0, 0, 0, 0]),
                 np.array([1.0, 1.0, 0, 1.0]) / np.sqrt(3)]
    MEH = {tuple(d): einstein_pairing_4d(1e-3 * d) / 1e-6 for d in DIRS_TEST}
    # membership test: one continuum-family element must reproduce P_2 across all test directions at once
    basis_eval = np.stack([np.concatenate([eval_T_form(NULLB[:, j], 1e-3 * d).ravel() / 1e-6
                                           for d in DIRS_TEST])
                           for j in range(NULLB.shape[1])], axis=1)
    worst_member = 0.0
    norms = []
    for t in range(10):
        th = FAM @ rng.standard_normal(fam_dim)
        th = th / np.linalg.norm(th)
        target = np.concatenate([extract_P2(lambda kv: family_Q(th, kv), d).ravel()
                                 for d in DIRS_TEST])
        nrm = float(np.linalg.norm(target))
        norms.append(nrm)
        if nrm < 1e-9:
            continue
        coef, _, _, _ = np.linalg.lstsq(basis_eval, target, rcond=None)
        resid = float(np.linalg.norm(basis_eval @ coef - target) / nrm)
        worst_member = max(worst_member, resid)
    check("declared-stencil family probe: for random elements of the sampled embedding-inert lattice "
          "family, the DIRECT metric-sector O(k^2) form P_2 (gauge-exact at every k by the "
          "line-average lemma, hence continuum-nullspace constrained) is fit by a SINGLE element of the ten-dimensional "
          "background-metric EH class ACROSS ALL THREE test directions simultaneously -- every local "
          "embedding-inert lattice action in this declared family has EH-class leading physics; the only "
          "leading freedom is the constant and the background metric within this scope",
          worst_member < 1e-3,
          f"worst across-direction EH-class fit residual = {worst_member:.1e} "
          f"(target norms {[round(n, 4) for n in norms[:5]]})")

    # ---- Regge action instantiation ----
    cs_regge = []
    for d in DIRS_TEST:
        P2 = extract_P2(bloch_Q_regge, d)
        ME = MEH[tuple(d)]
        cs_regge.append(float(np.vdot(ME, P2).real / np.vdot(ME, ME).real))
    check("Regge instantiation: the Regge action S_R is an embedding-inert form (its gauge zeros are exact -- the "
          "second-variation rows) and its direct P_2 = c x EH with c = -1/2 in the tick, space, AND a "
          "previously untested tick-space-space mixed direction -- the measured Regge<->EH "
          "correspondence is the continuum-plus-bridge theorem applied to the one embedding-inert form the geometric complex "
          "supplies natively",
          all(abs(c + 0.5) < 1e-5 for c in cs_regge),
          f"c(S_R) per direction (tick, space, mixed (1,1,0,1)/sqrt3) = {[round(c, 7) for c in cs_regge]}")

    # ---- Higher-order freedom witness ----
    def bloch_Q_defsq(kvec):
        Q = np.zeros((15, 15), complex)
        for tri in TRI_CLASSES:
            _, d_row = tri_rows(tri, kvec)
            Q += np.outer(np.conj(d_row), d_row)
        return Q
    kv = np.array([0.7, -0.3, 0.5, 0.2])
    gz = float(np.abs(bloch_Q_defsq(kv) @ gauge_map(kv)).max())
    nonzero = float(np.abs(bloch_Q_defsq(kv)).max())
    p2max = max(np.abs(extract_P2(bloch_Q_defsq, d)).max() for d in DIRS_TEST)
    check("higher-order freedom witness: the DEFICIT-SQUARED form sum_t |delta delta_t|^2 "
          "-- the discrete curvature-squared term, built from the same hinge data as S_R -- is local, "
          "EXACTLY gauge-annihilating at every momentum (deficits are inert under flat re-embeddings), "
          "nonzero at finite k, and has ZERO leading metric-sector content (pure O(k^4)): "
          "higher-curvature lattice terms exist, so the selection theorem fixes the LEADING order only, "
          "exactly as Lovelock's theorem does in the continuum (context only); the O(k^4) freedom is the "
          "lattice-fingerprint sector",
          gz < 1e-10 and nonzero > 1e-3 and p2max < 1e-7 * nonzero,
          f"gauge residual = {gz:.1e}; |Q_defsq(k_finite)| = {nonzero:.2f}; max|P_2| = {p2max:.1e} "
          f"(relative {p2max/nonzero:.1e} -- pure O(k^4))")

    # ---- Mass-term control ----
    th_mass = np.zeros(NPAR_LAT)
    th_mass[:120] = np.eye(15)[np.triu_indices(15)]
    kv = np.array([0.7, -0.3, 0.5, 0.2])
    viol = float(np.abs(family_Q(th_mass, kv) @ gauge_map(kv)).max())
    check("mass-term control: the edge-length mass term (C0 = identity, a "
          "perfectly local functional) violates embedding-inertness -- its gauge residual is O(1) -- so it is excluded by "
          "the embedding-independence requirement, not by fiat; the theorem is not vacuous",
          viol > 0.1,
          f"|Q'_mass(k) Gamma(k)| = {viol:.3f} (O(1) violation)")

    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    print(
        "VERDICT: at the linearized level the action-selection question is answered on the framework's\n"
        "own 3+1 complex. Gauge annihilation + locality at O(k^2) admit the\n"
        "background-metric EH class (ten-dimensional: one linearized EH form per constant flat metric;\n"
        "identified via GL(4) pullbacks); mass terms are excluded, and the\n"
        "only freedom beyond one overall constant is WHICH flat background (anisotropy/units data).\n"
        "The bridge applies to exact embedding-inert local lattice forms; the sampled declared-stencil\n"
        "family probe verifies representative random elements have leading metric physics in that class.\n"
        "The Regge action is one such form and realizes the ISOTROPIC background g = delta -- the\n"
        "complex's own flat metric, with the tick on equal footing per the kinetic-isotropy primitive --\n"
        "with c = -1/2 (the textbook normalization), including a previously untested mixed direction.\n"
        "The freedom beyond the constant and the background starts at O(k^4) (the deficit-squared\n"
        "discrete curvature-squared term, exhibited: gauge-exact, nonzero, zero leading content) -- the\n"
        "lattice analogue of Lovelock's theorem at quadratic order. The hypothesis is load-bearing\n"
        "(a mass term violates it at O(1)). The action-selection gap REDUCES to: the single leading\n"
        "constant's orientation and magnitude (the located sign residual + the registered scale\n"
        "reference), the background-metric choice (fixed by the complex's flat geometry + the\n"
        "kinetic-isotropy primitive), the O(k^4) tail, and the nonlinear completion. No PDG/fitted value."
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
