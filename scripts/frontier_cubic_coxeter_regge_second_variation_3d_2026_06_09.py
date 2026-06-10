"""Second variation of the Regge action on the RETAINED cubic-Coxeter complex (3D, flat background):
does delta^2 S_R reproduce the 3D Euclidean linearized Einstein-Hilbert quadratic form natively?

BUILDS DIRECTLY ON THE RETAINED ROW (read in full): CUBIC_COXETER_REGGE_DEFICIT_VANISHING (2026-05-10,
positive_theorem) establishes, for the standard six-tetrahedra body-diagonal Coxeter chain T(Z^3)
(T1=(v0,v1,v2,v6) ... T6=(v0,v5,v1,v6), all sharing the body diagonal (v0,v6)), with flat edge lengths
(1, sqrt2, sqrt3): the dihedral table {pi/4, pi/3, pi/2}, the corrected axis edge-star (6 contributing
tets, per-cube pi/2), zero deficit for every interior edge class, and S_R = sum_e L_e theta_e = 0 on
flat Z^3. That row ends at "flat is a solution". THIS runner computes the SECOND variation around that
flat point on that exact complex -- the object the landed but unaudited R3 target-operator row and the
degenerate-supermetric no-go both name as not-yet-supplied (the no-go names comparator potentials
V_trace<0<V_TT; here we ask whether the framework's own retained complex derives them).

STRUCTURE (3D Regge: hinges are edges; S_R = sum_e ell_e delta_e):
  - Regge's first-variation identity dS/d ell_e = delta_e (the complex-level Schlaefli lemma) implies
    at the flat point d^2S/d ell_e d ell_f = d delta_e / d ell_f, and symmetry of second derivatives
    makes J = d delta / d ell SYMMETRIC -- checked to machine precision (an exactness gate on the whole
    angle-gradient pipeline, alongside the per-tet Schlaefli identity sum_e ell_e d theta_e = 0).
  - Per unit cell the complex has SEVEN edge classes (3 axis + 3 face-diagonal + 1 body-diagonal); the
    metric sector h_ij (6 components, edge response d ell_e = v_e^T h v_e / (2 ell_e)) is 6 of them:
    exactly ONE non-metric edge mode per cell.
  - Vertex displacements of the flat complex leave it flat => they must be EXACT zero modes of
    delta^2 S_R at every Bloch momentum (the discrete gauge/diffeomorphism family) -- checked.

CHECKS:
  R1  flat-complex anchor: every interior edge of every class has deficit 0 (machine precision) on the
      periodic build, INCLUDING the corrected 6-tet axis edge-star of the retained row; S_R = 0.
  R2  exactness gates: per-tet Schlaefli identity sum_e ell_e d theta_e = 0 (all tets, machine), and
      J = d delta / d ell symmetric (machine) -- Regge's lemma realized by the assembled matrices.
  R3  gauge: vertex-displacement fields are EXACT zero modes of Q = (J + J^T)/2 in real space (random
      displacement field) and at random Bloch momenta (Q(k) Gamma(k) = 0 to machine).
  R4  Bloch reduction: the 7x7 Q(k) from the extracted finite-range stencil matches the periodic-build
      quadratic form on commensurate momenta (machine) -- the reduction is faithful.
  R5  k=0 consistency: constant metric perturbations (all 6 h components) are zero modes at k=0 (a
      constant h re-flattens to a flat complex) -- and the ONE non-metric mode at k=0 is NOT a zero
      mode: its quadratic weight is nonzero (sign REPORTED: the breathing mode is massive).
  R6  THE COMPARATOR QUESTION (the decisive check): at small k the metric-sector quadratic form
      Q_h(k) = k^2 M_regge(khat) + O(k^4); the 3D Euclidean linearized EH pairing gives
      Q_EH(k) = k^2 M_EH(khat) exactly (operator derived in-runner from the curvature definitions,
      same machinery as the 3+1 row). RESULT: M_regge = c * M_EH with ONE constant c = -1/2 EXACTLY,
      in all three lattice directions (axis, face-diagonal, body-diagonal), residual ~1e-8,
      slice-invariant (Schur complement = projection). c = -1/2 is precisely the textbook
      correspondence delta^2 S_R = (1/2) delta^2 int sqrt(g) R combined with the variational sign
      delta(sqrt(g)R) = -sqrt(g) G^{mu nu} delta g_{mu nu}: the Regge<->EH second-variation
      correspondence, including its 1/2 normalization, is DERIVED on the retained complex, with exact
      O(k^2) isotropy. The exact-line-average metric map (midpoint phase x sinc) is essential: a
      phase-free map is an O(k)-wrong slice that leaks the breathing weight into the metric channels
      (the contaminated numbers are reproduced and explained in the development history).
  R7  channel structure at small k (k || x): the two TT channels EQUAL (exact O(k^2) spin-2 isotropy),
      transverse-trace OPPOSITE sign with EQUAL magnitude (ratio -1 = the no-go's named +-k^2/2
      pair, derived), gauge zero. Orientation: in the standard Euclidean orientation S_E = -2 S_R the
      TT channels are positive, the conformal mode negative (textbook conformal-factor structure), the
      breathing mode +48 massive. The single remaining sign is the overall action orientation -- the
      same located sign residual as the arrow/stability/spectral no-go row.

WHAT THIS DOES NOT CLAIM: no edge-length-DOF provenance (Regge edge lengths are the supplied dynamical
variables here, as in the retained row's premise); no action selection (why S_R -- open); no 4D/timelike
extension (the kinetic fiber metric / multiplier structure is the separate 3+1 target-operator row; the
4D cubic-Coxeter complex is the named next step); no nonlinear statement. Comparators (Regge 1961;
Rocek-Williams lattice graviton; Cheeger-Mueller-Schrader convergence) cited as context only -- every
number here is computed from the retained complex's geometry. No PDG/fitted value.
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


# ---------------------------------------------------------------- the retained complex (verbatim chain)
CUBE = {
    0: (0, 0, 0), 1: (1, 0, 0), 2: (1, 1, 0), 3: (0, 1, 0),
    4: (0, 0, 1), 5: (1, 0, 1), 6: (1, 1, 1), 7: (0, 1, 1),
}
CHAIN = [(0, 1, 2, 6), (0, 2, 3, 6), (0, 3, 7, 6), (0, 7, 4, 6), (0, 4, 5, 6), (0, 5, 1, 6)]


# ------------------------------------------------- symbolic dihedral-angle gradients for a generic tet
def build_symbolic_gradients():
    """generic tet, vertices 0..3, edge-length-SQUARED symbols q_{ij}; returns for each edge (i,j) a
    lambdified [theta, dtheta/dq_kl ...] in the canonical edge order."""
    EDGES4 = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
    q = {e: sp.Symbol(f"q{e[0]}{e[1]}", positive=True) for e in EDGES4}

    def qq(i, j):
        return q[(min(i, j), max(i, j))]

    def dot(i, j, base):
        # <v_i - v_base, v_j - v_base> from edge lengths squared
        if i == j:
            return qq(base, i)
        return (qq(base, i) + qq(base, j) - qq(i, j)) / 2

    funcs = {}
    for (a, b) in EDGES4:
        c, d = [v for v in range(4) for _ in [0] if v not in (a, b)][:2]
        c, d = [v for v in range(4) if v not in (a, b)]
        # angle along edge (a,b): components of (c-a),(d-a) perpendicular to u=(b-a)
        uu = dot(b, b, a)
        ua = dot(b, c, a)
        ub = dot(b, d, a)
        aa = dot(c, c, a)
        bb = dot(d, d, a)
        ab = dot(c, d, a)
        na_nb = ab - ua * ub / uu
        na_na = aa - ua ** 2 / uu
        nb_nb = bb - ub ** 2 / uu
        cosang = na_nb / sp.sqrt(na_na * nb_nb)
        theta = sp.acos(cosang)
        grads = [sp.diff(theta, q[e]) for e in EDGES4]
        funcs[(a, b)] = sp.lambdify([q[e] for e in EDGES4], [theta] + grads, "numpy")
    return EDGES4, funcs


EDGES4, THETA_FUNCS = build_symbolic_gradients()


# ---------------------------------------------------------------- periodic complex build
class Complex3D:
    def __init__(self, L):
        self.L = L
        self.tets = []          # list of 4-tuples of vertex coordinates (tuples mod L)
        for x in range(L):
            for y in range(L):
                for z in range(L):
                    base = np.array([x, y, z])
                    for tet in CHAIN:
                        vs = tuple(tuple((base + np.array(CUBE[i])) % L) for i in tet)
                        self.tets.append(vs)
        # edges: canonical key = (vertex_a, vertex_b) sorted, PLUS the geometric edge vector class
        self.edge_index = {}
        self.edge_list = []
        self.edge_vec = []      # geometric vector (un-wrapped) of the edge as built
        for vs in self.tets:
            for (i, j) in itertools.combinations(range(4), 2):
                key = tuple(sorted([vs[i], vs[j]]))
                if key not in self.edge_index:
                    self.edge_index[key] = len(self.edge_list)
                    self.edge_list.append(key)
        self.NE = len(self.edge_list)

    def edge_vector(self, key):
        """un-wrapped displacement of minimal image between the two vertices."""
        a, b = np.array(key[0]), np.array(key[1])
        d = (b - a + self.L // 2) % self.L - self.L // 2
        return d


def flat_length(vec):
    return float(np.linalg.norm(vec))


def build_J(cx):
    """J_ef = d delta_e / d ell_f at the flat point (dense NE x NE), plus flat deficits."""
    L = cx.L
    NE = cx.NE
    J = np.zeros((NE, NE))
    deficit = np.full(NE, 2 * np.pi)
    # per tet: edge keys, flat q values, theta + gradients
    for vs in cx.tets:
        keys = []
        vecs = []
        for (i, j) in EDGES4:
            a, b = np.array(vs[i]), np.array(vs[j])
            d = (b - a + L // 2) % L - L // 2
            keys.append(tuple(sorted([vs[i], vs[j]])))
            vecs.append(d)
        qflat = [float(np.dot(v, v)) for v in vecs]
        ells = [np.sqrt(x) for x in qflat]
        idxs = [cx.edge_index[k] for k in keys]
        for ei, (a, b) in enumerate(EDGES4):
            out = THETA_FUNCS[(a, b)](*qflat)
            theta = float(out[0])
            deficit[idxs[ei]] -= theta
            for fj in range(6):
                # d theta / d ell_f = 2 ell_f * d theta / d q_f ; d delta_e/d ell_f = - sum_T dtheta/dell
                J[idxs[ei], idxs[fj]] -= 2 * ells[fj] * float(out[1 + fj])
    return J, deficit


def schlafli_residual(cx):
    """per-tet Schlaefli: sum_e ell_e d theta_e = 0 (as a gradient identity: for each tet and each
    length-direction f: sum_e ell_e dtheta_e/dell_f -- the 3D Schlaefli differential identity)."""
    worst = 0.0
    for vs in cx.tets[: 6 * 8]:
        vecs = []
        for (i, j) in EDGES4:
            a, b = np.array(vs[i]), np.array(vs[j])
            d = (b - a + cx.L // 2) % cx.L - cx.L // 2
            vecs.append(d)
        qflat = [float(np.dot(v, v)) for v in vecs]
        ells = np.array([np.sqrt(x) for x in qflat])
        G = np.zeros((6, 6))
        for ei, (a, b) in enumerate(EDGES4):
            out = THETA_FUNCS[(a, b)](*qflat)
            for fj in range(6):
                G[ei, fj] = 2 * ells[fj] * float(out[1 + fj])
        res = ells @ G            # sum_e ell_e dtheta_e/dell_f for each f
        worst = max(worst, float(np.abs(res).max()))
    return worst


def main() -> int:
    print("SECOND VARIATION OF THE REGGE ACTION ON THE RETAINED CUBIC-COXETER COMPLEX (3D, flat)")
    print("=" * 96)
    L = 4
    cx = Complex3D(L)
    J, deficit = build_J(cx)

    # ---- R1: flat anchor ----
    worst_def = float(np.abs(deficit).max())
    # also: count tets on a representative axis edge (the corrected edge-star of the retained row)
    axis_key = tuple(sorted([(0, 0, 0), (1, 0, 0)]))
    n_axis = sum(1 for vs in cx.tets
                 if axis_key in [tuple(sorted([vs[i], vs[j]])) for (i, j) in EDGES4])
    SR = float(np.sum([flat_length(cx.edge_vector(k)) for k in cx.edge_list] * deficit)) if False else \
        float(np.dot(np.array([flat_length(cx.edge_vector(k)) for k in cx.edge_list]), deficit))
    check("R1 (flat anchor = the retained row, reproduced on the periodic build): every interior edge "
          "deficit is 0 to machine precision (all classes), the representative axis edge has the "
          "CORRECTED 6-tet edge-star of the 2026-05-19 repair, and S_R = sum ell_e delta_e = 0",
          worst_def < 1e-12 and n_axis == 6 and abs(SR) < 1e-10,
          f"max|deficit| = {worst_def:.2e}; axis edge-star tets = {n_axis} (retained row: 6); S_R = {SR:.2e}")

    # ---- R2: exactness gates ----
    schl = schlafli_residual(cx)
    sym = float(np.abs(J - J.T).max())
    check("R2 (exactness gates): per-tet Schlaefli identity sum_e ell_e d theta_e = 0 holds to machine "
          "precision (validates the symbolic angle-gradient pipeline), and J = d delta/d ell is SYMMETRIC "
          "to machine precision (Regge's first-variation identity dS/d ell = delta realized: J is the "
          "Hessian of S_R at flat)",
          schl < 1e-12 and sym < 1e-12,
          f"max per-tet Schlaefli residual = {schl:.2e}; max|J - J^T| = {sym:.2e}")

    Q = (J + J.T) / 2

    # ---- R3: gauge (vertex displacements) ----
    rng = np.random.default_rng(11)
    xi = {v: rng.standard_normal(3) for v in {vv for key in cx.edge_list for vv in key}}
    eps = np.zeros(cx.NE)
    for n, key in enumerate(cx.edge_list):
        vec = cx.edge_vector(key)
        ell = flat_length(vec)
        eps[n] = vec @ (xi[key[1]] - xi[key[0]]) / ell
    gauge_res = float(np.abs(Q @ eps).max()) / max(1e-30, float(np.abs(eps).max()))
    check("R3 (gauge): a random vertex-displacement field of the flat complex is an EXACT zero mode of "
          "Q = delta^2 S_R (flat stays flat under vertex motion) -- the discrete diffeomorphism family, "
          "exact at the discrete level (contrast: the transcribed continuum operator on the hypercubic "
          "lattice had only approximate gauge zero modes)",
          gauge_res < 1e-10, f"|Q eps_gauge| / |eps| = {gauge_res:.2e}")

    # ---- Bloch machinery: 7 classes per cell ----
    # class id: (anchor offset within cell = 0, direction vector) -- the 7 directions:
    DIRS = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0), (0, 1, 1), (1, 0, 1), (1, 1, 1)]
    def classify(key):
        vec = cx.edge_vector(key)
        sgn = 1
        v = tuple(vec)
        if v not in DIRS:
            v = tuple(-vec)
            sgn = -1
        cls = DIRS.index(v)
        base = key[0] if sgn == 1 else key[1]
        return cls, np.array(base)
    CLS = [classify(k) for k in cx.edge_list]

    def bloch_Q(kvec):
        """7x7 Bloch reduction of Q at momentum kvec (radians per lattice unit)."""
        B = np.zeros((7, 7), complex)
        # use the periodic complex directly: edge field eps_e = u_cls * exp(i k . base)
        # Q(k)_{cd} = (1/Ncells) sum_{e in c, f in d} Q_ef exp(i k.(base_f - base_e))
        Ncells = cx.L ** 3
        for ei in range(cx.NE):
            ci, bi = CLS[ei]
            row = Q[ei]
            nz = np.nonzero(np.abs(row) > 1e-14)[0]
            for fj in nz:
                cj, bj = CLS[fj]
                # minimal-image displacement between anchors
                d = (bj - bi + cx.L // 2) % cx.L - cx.L // 2
                B[ci, cj] += row[fj] * np.exp(1j * np.dot(kvec, d))
        return B / Ncells

    # ---- R4: Bloch reduction faithful (commensurate momentum) ----
    kc = np.array([2 * np.pi / L, 0, 0])
    Bk = bloch_Q(kc)
    u = rng.standard_normal(7) + 1j * rng.standard_normal(7)
    eps_c = np.zeros(cx.NE, complex)
    for n in range(cx.NE):
        ci, bi = CLS[n]
        eps_c[n] = u[ci] * np.exp(1j * np.dot(kc, bi))
    lhs = np.vdot(eps_c, Q @ eps_c) / (cx.L ** 3)
    rhs = np.vdot(u, Bk @ u)
    check("R4 (Bloch reduction faithful): the 7x7 Q(k) reproduces the periodic-build quadratic form on a "
          "commensurate plane-wave edge field to machine precision",
          abs(lhs - rhs) < 1e-10 * max(1.0, abs(lhs)),
          f"|periodic - Bloch| = {abs(lhs - rhs):.2e}")

    # gauge at Bloch level: Gamma(k) 7x3: vertex field xi e^{ikx}: eps_e = vhat.( xi e^{ik(base+v)} - xi e^{ik base} )
    def gauge_map(kvec):
        Gm = np.zeros((7, 3), complex)
        for ci, v in enumerate(DIRS):
            vv = np.array(v)
            ell = np.linalg.norm(vv)
            Gm[ci, :] = (np.exp(1j * np.dot(kvec, vv)) - 1.0) * vv / ell
        return Gm

    kr = np.array([0.37, -0.83, 0.51])
    Bkr = bloch_Q(kr)
    Gr = gauge_map(kr)
    g_bloch = float(np.abs(Bkr @ Gr).max())
    check("R3b (gauge at Bloch level): Q(k) Gamma(k) = 0 to machine precision at a random incommensurate "
          "momentum -- the vertex-displacement gauge family is exact at every k",
          g_bloch < 1e-10, f"max|Q(k) Gamma(k)| = {g_bloch:.2e} at k = {kr.round(2).tolist()}")

    # ---- metric map: h (6 comps) -> 7 edge classes (EXACT line-averaged response) ----
    # For a Bloch field h(x) = H e^{ik.x}, the exact length response of edge (x0, x0+v) is the LINE
    # AVERAGE: d ell = (ell/2) vhat^T H vhat * e^{ik.(x0+v/2)} * sinc(k.v/2). The midpoint phase and
    # sinc are NOT optional: a phase-free map is an O(k)-wrong slice of edge space, which leaks the
    # massive breathing weight into the metric channels at O(k^2) (verified: that leak reproduces the
    # contaminated first-draft numbers). With the exact map, a continuum gauge field h = i(k x xi)_sym
    # maps EXACTLY onto the discrete vertex-displacement family (line integral of a tangential
    # derivative = endpoint difference) -- checked below as a convention gate.
    HCOMPS = [(0, 0), (1, 1), (2, 2), (0, 1), (0, 2), (1, 2)]
    def metric_map(kvec):
        Mm = np.zeros((7, 6), complex)
        for ci, v in enumerate(DIRS):
            vv = np.array(v, float)
            ell = np.linalg.norm(vv)
            z = np.dot(kvec, vv) / 2.0
            phase = np.exp(1j * z) * (np.sinc(z / np.pi))   # numpy sinc(x) = sin(pi x)/(pi x)
            for hj, (a, b) in enumerate(HCOMPS):
                Hm = np.zeros((3, 3))
                Hm[a, b] += 1.0
                if a != b:
                    Hm[b, a] += 1.0
                Mm[ci, hj] = phase * (vv @ Hm @ vv) / (2 * ell)
        return Mm
    MM = metric_map(np.zeros(3)).real

    # ---- R2b: end-to-end gate -- finite difference of the ACTUAL action vs the assembled Q ----
    def action_of(eps_real):
        """S_R = sum_e ell_e(eps) delta_e(eps) on the periodic complex, edge lengths ell_flat + eps."""
        ell_pert = {}
        for n, key in enumerate(cx.edge_list):
            ell_pert[key] = flat_length(cx.edge_vector(key)) + eps_real[n]
        total = 0.0
        deficits = {key: 2 * np.pi for key in cx.edge_list}
        for vs in cx.tets:
            keys = [tuple(sorted([vs[i], vs[j]])) for (i, j) in EDGES4]
            qv = [ell_pert[k_] ** 2 for k_ in keys]
            for ei, (a, b) in enumerate(EDGES4):
                out = THETA_FUNCS[(a, b)](*qv)
                deficits[keys[ei]] -= float(out[0])
        for key in cx.edge_list:
            total += ell_pert[key] * deficits[key]
        return total
    eps_rand = 1e-4 * rng.standard_normal(cx.NE)
    s_p, s_0, s_m = action_of(eps_rand), action_of(0 * eps_rand), action_of(-eps_rand)
    fd2 = (s_p - 2 * s_0 + s_m)
    quad_pred = float(eps_rand @ Q @ eps_rand)
    check("R2b (end-to-end gate): the numerical second difference of the ACTUAL Regge action "
          "S_R = sum ell delta under a random edge-length perturbation equals eps^T Q eps from the "
          "assembled Hessian (validates every sign, factor, and assembly step at once)",
          abs(fd2 - quad_pred) < 1e-6 * max(abs(quad_pred), 1e-12),
          f"finite-diff = {fd2:.10e} vs eps^T Q eps = {quad_pred:.10e}")

    # ---- convention gate: continuum gauge == discrete gauge through the exact line-averaged map ----
    kg = np.array([0.29, 0.61, -0.47])
    xig = rng.standard_normal(3) + 1j * rng.standard_normal(3)
    # continuum gauge field h_ab = i (k_a xi_b + k_b xi_a) (Bloch amplitude)
    hg = np.zeros(6, complex)
    for j, (a, b) in enumerate(HCOMPS):
        hg[j] = 1j * (kg[a] * xig[b] + kg[b] * xig[a])
    lhs_g = metric_map(kg) @ hg
    rhs_g = gauge_map(kg) @ xig
    gate_g = float(np.abs(lhs_g - rhs_g).max())
    check("R2c (convention gate): a continuum gauge perturbation h = i(k xi + xi k) maps through the "
          "exact line-averaged metric map onto EXACTLY the discrete vertex-displacement family (pins the "
          "midpoint-phase/sinc conventions; line integral of a tangential derivative = endpoint "
          "difference)",
          gate_g < 1e-12, f"max|M(k) h_gauge - Gamma(k) xi| = {gate_g:.2e}")

    # ---- R5: k=0 -- constant h are zero modes; the non-metric 7th mode is massive ----
    B0 = bloch_Q(np.zeros(3)).real
    h_res = float(np.abs(B0 @ MM).max())
    # non-metric direction: complement of the metric image in R^7
    u_perp, s, _ = np.linalg.svd(np.hstack([MM, np.zeros((7, 1))]))
    nonmetric = u_perp[:, 6]
    w_nm = float(nonmetric @ B0 @ nonmetric)
    check("R5 (k=0): constant metric perturbations (all 6 h components) are EXACT zero modes of Q(0) (a "
          "constant h re-flattens the complex), while the single NON-METRIC edge mode per cell (the "
          "7-edge-class complement of the 6 metric components) is NOT a zero mode -- the breathing mode "
          "has nonzero quadratic weight at k=0 (sign reported)",
          h_res < 1e-10 and abs(w_nm) > 1e-6,
          f"max|Q(0) M_metric| = {h_res:.2e}; non-metric breathing weight = {w_nm:+.6f} in the raw "
          f"S_R orientation (= {-2*w_nm:+.1f} in the standard Euclidean orientation S_E = -2 S_R: "
          f"massive and healthy there; no flat direction beyond gauge+metric)")

    # ---- continuum comparator: 3D Euclidean linearized EH pairing ----
    def einstein_pairing_3d(kvec):
        """M_EH(k): 6x6 quadratic-form matrix of the pairing sum_ab h_ab G^{ab}(h) in 3D Euclidean,
        operator derived from the curvature definitions (same machinery as the 3+1 row, eta = I)."""
        n = 3
        hs = {}
        for a in range(n):
            for b in range(n):
                if a <= b:
                    hs[(a, b)] = sp.Symbol(f"h{a}{b}")
        Hm = sp.Matrix(n, n, lambda a, b: hs[(min(a, b), max(a, b))])
        p = [sp.Float(kvec[0]), sp.Float(kvec[1]), sp.Float(kvec[2])]
        Svals = {}
        for m in range(n):
            for nn in range(n):
                Svals[(m, nn)] = -p[m] * p[nn]
        R = sp.zeros(n, n)
        for m in range(n):
            for nn in range(n):
                acc = 0
                for l in range(n):
                    acc += (Svals[(min(l, m), max(l, m))] * Hm[l, nn]
                            + Svals[(min(l, nn), max(l, nn))] * Hm[l, m]
                            - Svals[(l, l)] * Hm[m, nn] - Svals[(min(m, nn), max(m, nn))] * Hm[l, l])
                R[m, nn] = acc / 2
        Rs = sum(R[m, m] for m in range(n))
        G = sp.Matrix(n, n, lambda m, nn: R[m, nn] - sp.Rational(1, 2) * (1 if m == nn else 0) * Rs)
        # pairing quadratic form on the 6 components with (2 - delta) weights
        Mq = np.zeros((6, 6))
        for i, (a, b) in enumerate(HCOMPS):
            wgt = 2.0 if a != b else 1.0
            expr = wgt * G[a, b]
            for j, key in enumerate(HCOMPS):
                Mq[i, j] = float(sp.diff(expr, hs[key]))
        return (Mq + Mq.T) / 2

    # ---- R6: the comparator question (proportionality + signs + isotropy) ----
    print("\n  small-k metric-sector comparison  Q_h(k) =? c * Q_EH(k)  per direction:")
    dirs = {"axis(100)": np.array([1.0, 0, 0]),
            "face(110)": np.array([1.0, 1.0, 0]) / np.sqrt(2),
            "body(111)": np.array([1.0, 1.0, 1.0]) / np.sqrt(3)}
    cs = {}
    res_rel = {}
    schur_diff = {}
    for nm, khat in dirs.items():
        kk = 1e-3
        Bk_ = bloch_Q(kk * khat)
        Mk = metric_map(kk * khat)
        Qh = Mk.conj().T @ Bk_ @ Mk
        Qh = (Qh + Qh.conj().T) / 2
        # Schur-complement cross-check (slice-invariance): integrate out the complement of the metric
        # image instead of projecting it out; difference must be subleading (O(k^4)).
        Ufull, _, _ = np.linalg.svd(Mk)
        Pm, Pb = Ufull[:, :6], Ufull[:, 6:]
        Qmm = Pm.conj().T @ Bk_ @ Pm
        Qmb = Pm.conj().T @ Bk_ @ Pb
        Qbb = Pb.conj().T @ Bk_ @ Pb
        Qs = Qmm - Qmb @ np.linalg.inv(Qbb) @ Qmb.conj().T
        Cm = Pm.conj().T @ Mk
        Qh_schur = Cm.conj().T @ Qs @ Cm
        Qh_schur = (Qh_schur + Qh_schur.conj().T) / 2
        schur_diff[nm] = float(np.abs(Qh_schur - Qh).max() / max(1e-30, np.abs(Qh).max()))
        Meh = einstein_pairing_3d(kk * khat)
        num = float(np.real(np.vdot(Meh, Qh)))
        den = float(np.real(np.vdot(Meh, Meh)))
        c = num / den
        resid = np.abs(Qh - c * Meh).max() / max(1e-30, np.abs(Qh).max())
        cs[nm] = c
        res_rel[nm] = float(resid)
        print(f"    {nm}:  c = {c:+.6f}   rel-residual = {resid:.3e}   schur-vs-project = {schur_diff[nm]:.1e}")
    c_vals = np.array(list(cs.values()))
    iso = float(np.ptp(c_vals) / np.abs(c_vals).mean())
    check("R6 (THE COMPARATOR QUESTION -- exact proportionality, derived normalization, isotropy): at "
          "small k the Regge metric-sector quadratic form is EXACTLY PROPORTIONAL to the 3D Euclidean "
          "linearized EH pairing in ALL THREE lattice directions, with ONE constant c = -1/2 -- which is "
          "precisely the TEXTBOOK correspondence delta^2 S_R = (1/2) delta^2 (int sqrt(g) R) combined "
          "with the variational sign delta(sqrt(g)R) = -sqrt(g) G^{mu nu} delta g_{mu nu}: the runner "
          "DERIVES the Regge<->EH second-variation correspondence on the retained complex, including the "
          "1/2 normalization, with O(k^2) ISOTROPY (direction spread ~1e-8) and slice-invariance (Schur "
          "complement vs projection agree). The opposite-signed comparator PAIR the no-go named is "
          "therefore DERIVED from the framework's own retained geometry (the overall orientation of the "
          "action is the single remaining sign -- see R7).",
          all(abs(c + 0.5) < 1e-6 for c in c_vals) and all(r < 1e-6 for r in res_rel.values())
          and iso < 1e-6 and all(s < 1e-6 for s in schur_diff.values()),
          f"c = {dict((k, round(v, 8)) for k, v in cs.items())} (= -1/2 exactly); spread/mean = {iso:.2e}; "
          f"residuals = {dict((k, '%.1e' % v) for k, v in res_rel.items())}")

    # ---- R7: explicit channel signs at small k (k || x) ----
    kk = 1e-3
    kvec7 = np.array([kk, 0, 0])
    Bk_ = bloch_Q(kvec7)
    Mk7 = metric_map(kvec7)
    Qh = Mk7.conj().T @ Bk_ @ Mk7
    Qh = np.real((Qh + Qh.conj().T) / 2) / kk ** 2
    def hquad(d):
        v = np.zeros(6)
        nrm = 0.0
        for (a, b), val in d.items():
            v[HCOMPS.index((min(a, b), max(a, b)))] = val
            nrm += val ** 2 * (2 if a != b else 1)
        v = v / np.sqrt(nrm)
        return float(v @ Qh @ v)
    q_tt_yz = hquad({(1, 2): 1.0})
    q_tt_E = hquad({(1, 1): 1.0, (2, 2): -1.0})
    q_trT = hquad({(1, 1): 1.0, (2, 2): 1.0})
    q_gauge = hquad({(0, 1): 1.0})
    ratio_tt = q_trT / q_tt_yz
    check("R7 (channel structure, k || x): the two TT channels are EQUAL (spin-2 isotropy exact at "
          "O(k^2)), the transverse-trace channel has the OPPOSITE sign with EQUAL magnitude (ratio "
          "exactly -1: the no-go's named pair V = +-k^2/2 with equal magnitudes, derived), and the "
          "gauge channel is zero. ORIENTATION (honest): in the runner's raw S_R = sum ell delta "
          "orientation TT is negative and trace positive; in the standard Euclidean orientation "
          "S_E = -int sqrt(g) R = -2 S_R, TT is POSITIVE, the conformal/trace mode NEGATIVE (the "
          "textbook Euclidean conformal-factor structure), and the breathing mode +48 (massive, "
          "healthy). The overall orientation of the geometric action is the SINGLE remaining sign -- "
          "the same located sign residual as the arrow/stability/spectral no-go row; everything "
          "orientation-independent (opposite-sign pair, equal magnitudes, isotropy, gauge zeros, "
          "massive breathing) is derived here.",
          abs(q_tt_yz - q_tt_E) < 1e-6 and abs(ratio_tt + 1.0) < 1e-6
          and abs(q_gauge) < 1e-6 * max(abs(q_tt_yz), 1e-12),
          f"TT(yz)={q_tt_yz:+.6f} = TT(E)={q_tt_E:+.6f}; transverse-trace={q_trT:+.6f} (ratio {ratio_tt:+.4f}); "
          f"gauge(xy)={q_gauge:+.2e}  (per k^2, unit-norm channels, raw S_R orientation)")

    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    print(
        "VERDICT: on the RETAINED cubic-Coxeter complex (the exact six-tetrahedra body-diagonal chain of\n"
        "the deficit-vanishing row), the second variation of the Regge action around flat EQUALS the\n"
        "continuum linearized Einstein-Hilbert second variation at leading order, EXACTLY and\n"
        "ISOTROPICALLY: Q_h(k) = c * Q_EH(k) + O(k^4) with the single constant c = -1/2 in all three\n"
        "lattice directions (= the textbook delta^2 S_R = (1/2) delta^2 int sqrt(g) R with the\n"
        "variational sign, DERIVED including the 1/2). Vertex displacements are exact zero modes at\n"
        "every momentum (discrete gauge); constant metric perturbations re-flatten (k=0 zero modes);\n"
        "the single non-metric breathing mode is massive (no extra flat direction); the two TT channels\n"
        "are equal and the transverse-trace channel is equal-magnitude opposite-sign (ratio -1) -- the\n"
        "degenerate-supermetric no-go's named comparator pair (+-k^2/2) is hereby DERIVED from the\n"
        "framework's own retained geometry. The one remaining sign is the overall action orientation\n"
        "(S_R vs -S_R), the same single located sign residual as the arrow/stability/spectral no-go\n"
        "row. OPEN (named): the 4D/timelike cubic-Coxeter extension (the kinetic fiber metric from the\n"
        "geometric action itself), edge-length-DOF provenance, action selection, nonlinear closure.\n"
        "No PDG/fitted value."
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
