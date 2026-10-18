

# ------------------------------------------------------------------ curvature-squared term, masses, readings
def R2(C, k):
    """sum over hinge classes of delta_h(-k) delta_h(k): the quadratic form of sum_h delta_h^2."""
    k = np.asarray(k, complex); M = np.zeros((C.E, C.E), complex)
    for a, d in C.terms:
        rp = np.zeros(C.E, complex); np.add.at(rp, d[0], d[2] * np.exp(1j * (d[1] @ k)))
        rm = np.zeros(C.E, complex); np.add.at(rm, d[0], d[2] * np.exp(-1j * (d[1] @ k)))
        M += np.outer(rm, rp)
    return M


def lumped_mass(C):
    tix = {t: i for i, t in enumerate(C.types)}; w = np.zeros(len(C.types))
    for vs in C.simp:
        P = np.array([C.pos(v) for v in vs]); vol = abs(np.linalg.det(P[1:] - P[0])) / 24
        for v in vs: w[tix[v[1]]] += vol / 5
    return np.diag(w)


def consistent_mass(C, k):
    k = np.asarray(k, complex); tix = {t: i for i, t in enumerate(C.types)}; M = np.zeros((len(C.types),) * 2, complex)
    for vs in C.simp:
        P = np.array([C.pos(v) for v in vs]); vol = abs(np.linalg.det(P[1:] - P[0])) / 24
        for i in range(5):
            for j in range(5):
                M[tix[vs[i][1]], tix[vs[j][1]]] += vol * (2 if i == j else 1) / 30 * np.exp(1j * k @ (np.array(vs[j][0], float) - np.array(vs[i][0], float)))
    return M


def comp_inv(Q, G, J):
    """solve Q x = J on the orthogonal complement of the exact null directions G."""
    Pq, _ = np.linalg.qr(G); n = Q.shape[0]
    Pc = np.linalg.svd(np.eye(n) - Pq @ Pq.conj().T)[0][:, :n - G.shape[1]]
    return Pc @ np.linalg.solve(Pc.conj().T @ Q @ Pc, Pc.conj().T @ J)


def face_metric(C, k):
    """D4 cone: site-cell metric from axis edges and both face diagonals, each read through the deep hole it crosses."""
    pairs = list(itertools.combinations(range(4), 2)); E = np.eye(4, dtype=int); Z = (0, 0, 0, 0)
    k = np.asarray(k, complex); Lm = np.zeros((10, C.E), complex)
    def add(row, v1, v2, coef):
        key, anc = _key_pair(v1, v2); Lm[row, C.ekey[key]] += coef * np.exp(1j * k @ np.array(anc, float))
    for mu in range(4): add(HC.index((mu, mu)), (Z, 0), (tuple(E[mu]), 0), 2.0)
    for h, (m, n) in enumerate(pairs):
        row = HC.index((m, n)); hv = (Z, 2 + h); r2 = np.sqrt(2) / 2
        add(row, (Z, 0), hv, r2); add(row, hv, (tuple(E[m] + E[n]), 0), r2)
        add(row, (tuple(E[n]), 0), hv, -r2); add(row, hv, (tuple(E[m]), 0), -r2)
    return Lm


def kuhn_reading(K, k, relative=True):
    """Kuhn complex: least-squares metric from the 15 edge classes (relative or plain strains)."""
    l = np.array([np.linalg.norm(K.evec[c]) for c in range(K.E)]); M = K.line_map(k)
    W = np.diag(1 / l ** 2) if relative else np.eye(K.E)
    return np.linalg.pinv(W @ M) @ W


# ------------------------------------------------------------------ OS reflection positivity of Gaussian fields
def rp_vertex(Qfun, offs_t, ks, Nt, t0):
    kts = 2 * np.pi * np.arange(Nt) / Nt
    inv = [np.linalg.inv(Qfun(np.array([*ks, kt]))) for kt in kts]
    G = lambda dbt: sum(Ki * np.exp(1j * kt * dbt) for Ki, kt in zip(inv, kts)) / Nt
    half = [(bt, tau, bt + ot) for bt in range(-1, Nt // 2 + 1) for tau, ot in enumerate(offs_t)
            if t0 - 1e-9 <= bt + ot <= t0 + Nt / 2 + 1e-9]
    R = np.zeros((len(half),) * 2, complex)
    for a, (bt1, ta, _) in enumerate(half):
        for b, (bt2, tb, t2) in enumerate(half):
            R[a, b] = G(bt1 - int(round(2 * t0 - t2 - offs_t[tb])))[ta, tb]
    return R


def rp_forms(F, k, Qfun, ks, Nt, t0):
    C = F.C; kts = 2 * np.pi * np.arange(Nt) / Nt
    inv = [np.linalg.inv(Qfun(np.array([*ks, kt]))) for kt in kts]
    G = lambda dbt: sum(Ki * np.exp(1j * kt * dbt) for Ki, kt in zip(inv, kts)) / Nt
    reps = sorted((ci, [(np.array(b, float), t) for t, b in key]) for key, ci in F.cls[k].items())
    half = []
    for bt in range(-2, Nt // 2 + 2):
        for ci, verts in reps:
            ts = [bt + v[0][3] + C.OFF[v[1]][3] for v in verts]
            if min(ts) >= t0 - 1e-9 and max(ts) <= t0 + Nt / 2 + 1e-9:
                half.append((bt, ci, [(tuple(int(x) for x in v[0] + np.array([0, 0, 0, bt])), v[1]) for v in verts]))
    img = []
    for bt, ci, verts in half:
        rv = []
        for b, t in verts:
            p = np.array(b, float) + C.OFF[t]; p[3] = 2 * t0 - p[3]; rv.append((tuple(int(x) for x in np.round(p - C.OFF[t])), t))
        key, anc, srt = canon(rv)
        img.append((F.cls[k][key], anc, Forms._perm_sign([srt.index(v) for v in rv])))
    R = np.zeros((len(half),) * 2, complex)
    for a, (bt1, c1, _) in enumerate(half):
        for b, (c2, anc2, sg2) in enumerate(img):
            R[a, b] = sg2 * G(bt1 - anc2[3])[c1, c2] * np.exp(-1j * np.array(ks) @ np.array(anc2[:3], float))
    return R


def rel_min_eig(R):
    w = np.linalg.eigvalsh(0.5 * (R + R.conj().T)); return w.min() / abs(w).max()


def main():
    OFF, S = d4cone(); D = Complex(OFF, S); F = Forms(D)
    # ---------------- J1
    q = np.array([0.31, -0.22, 0.17, 0.4])
    d2 = max(np.abs(F.d(k + 1, q) @ F.d(k, q)).max() for k in range(3))
    minm = min(np.linalg.eigvalsh(0.5 * (F.M(k, q) + F.M(k, q).conj().T)).min() for k in range(5))
    check("J1 D4 cone Whitney complex: classes per cell 8, 72, 208, 240, 96; d^2 = 0; Euler characteristic 0; mass matrices positive",
          F.n == [8, 72, 208, 240, 96] and d2 < 1e-12 and sum((-1) ** k * F.n[k] for k in range(5)) == 0 and minm > 0,
          f"counts {F.n}; |d d| {d2:.0e}; min mass eigenvalue {minm:.2e}")
    # ---------------- J2
    kd = np.array([0.3, -0.5, 0.6, 0.55]); kd /= np.linalg.norm(kd); rows = []
    for k in range(5):
        K, M = F.hodge(k, 0.01 * kd); w = np.sort(np.real(sl.eigvals(K, M)))
        ns = int((np.abs(w) < 1e-2).sum()); rows.append((ns, np.abs(w[:ns] / 1e-4 - 1).max() if ns else 1, w[ns]))
    check("J2 Hodge Laplacians (square of the Dirac-Kahler operator): massless modes per degree = C(4,k) = 1, 4, 6, 4, 1, all at lambda = k^2, gap >= 20",
          [r[0] for r in rows] == [math.comb(4, k) for k in range(5)] and max(r[1] for r in rows) < 1e-3 and min(r[2] for r in rows) > 20,
          f"counts {[r[0] for r in rows]}; max |lambda/k^2 - 1| {max(r[1] for r in rows):.0e}; gap {min(r[2] for r in rows):.1f}")
    # ---------------- J3
    worst = 0.0; nxt = np.inf
    for n in [(1, 0, 0), (3, 1, 2)]:
        n = np.array(n, float); n /= np.linalg.norm(n); km = 0.05
        for k in range(5):
            K, M = F.hodge(k, np.array([*(km * n), 1j * km])); w = np.sort(np.abs(sl.eigvals(K, M)))
            worst = max(worst, w[math.comb(4, k) - 1] / km ** 2); nxt = min(nxt, w[math.comb(4, k)] / km ** 2)
    check("J3 on the continuum shell omega = k (|k| = 0.05; axis and generic): all 16 modes null with |lambda|/k^2 <= 1e-7 (an O(k^4) term would give ~1e-4)",
          worst < 1e-7 and nxt > 1e3, f"max |lambda|/k^2 {worst:.1e}; next {nxt:.1e}")
    # ---------------- J4
    m2 = 0.3; Nt = 6; ksl = [np.array([0.0, 0.0, 0.0]), np.array([0.7, -0.3, 0.2])]
    nn = lambda k: np.array([[np.sum(4 * np.sin(np.asarray(k) / 2) ** 2) + m2]], complex)
    hd = lambda k: np.array([[(lambda L: L + 0.5 * L * L + m2)(np.sum(4 * np.sin(np.asarray(k) / 2) ** 2))]], complex)
    offs_t = [float(o[3]) for o in D.OFF]; ML = lumped_mass(D)
    c_nn = min(rel_min_eig(rp_vertex(nn, [0.0], ks, Nt, t0)) for ks in ksl for t0 in (0.0, 0.5))
    c_hd = max(rel_min_eig(rp_vertex(hd, [0.0], ks, Nt, 0.0)) for ks in ksl)
    c_cm = max(rel_min_eig(rp_vertex(lambda k: p1_scalar(D, k) + m2 * consistent_mass(D, k), offs_t, ks, Nt, 0.0)) for ks in ksl)
    check("J4 reflection-positivity controls: NN Laplacian passes (site and link planes); higher-derivative scalar fails; D4 P1 with consistent mass fails",
          c_nn > -1e-12 and c_hd < -1e-3 and c_cm < -1e-5, f"NN min/max {c_nn:+.0e}; higher-derivative {c_hd:+.1e}; consistent-mass P1 {c_cm:+.1e}")
    # ---------------- J5
    s5 = min(rel_min_eig(rp_vertex(lambda k: p1_scalar(D, k) + m2 * ML, offs_t, ks, Nt, t0)) for ks in ksl for t0 in (0.0, 0.5))
    check("J5 D4-cone P1 scalar with lumped mass: reflection positive at the site plane t = 0 and the centre plane t = 1/2",
          s5 > -1e-12, f"min/max eigenvalue over 2 momenta x 2 planes {s5:+.1e}")
    # ---------------- J6
    Mdiag = np.diag(np.real(np.diag(F.M(1, np.zeros(4)))))
    proca = lambda q: F.d(1, -np.asarray(q, complex)).T @ F.M(2, q) @ F.d(1, q) + 0.5 * Mdiag
    procac = lambda q: F.d(1, -np.asarray(q, complex)).T @ F.M(2, q) @ F.d(1, q) + 0.5 * F.M(1, q)
    s6 = min(rel_min_eig(rp_forms(F, 1, proca, ks, Nt, t0)) for ks in ksl for t0 in (0.0, 0.5))
    c6 = rel_min_eig(rp_forms(F, 1, procac, ksl[1], Nt, 0.0))
    check("J6 D4-cone Whitney 1-form (Proca, diagonal mass): reflection positive at both planes; consistent mass fails (control)",
          s6 > -1e-12 and c6 < -1e-5, f"min/max {s6:+.1e}; control {c6:+.1e}")
    # ---------------- J7
    lam = -0.1; OFFk, Sk = kuhn(); K = Complex(OFFk, Sk); qg = np.array([0.3, -0.2, 0.25, 0.15])
    nk0 = int((np.sort(np.linalg.svd(K.Q(qg), compute_uv=False)) / np.abs(K.Q(qg)).max() < 1e-9).sum())
    sk = np.sort(np.linalg.svd(K.Q(qg) + lam * R2(K, qg), compute_uv=False)); nk = int((sk / sk[-1] < 1e-9).sum())
    Qd = D.Q(0.01 * kd) + lam * R2(D, 0.01 * kd); wd = np.linalg.eigvalsh(0.5 * (Qd + Qd.conj().T)); wd = wd[np.argsort(np.abs(wd))]
    Qd0 = D.Q(0.01 * kd); wd0 = np.linalg.eigvalsh(0.5 * (Qd0 + Qd0.conj().T)); wd0 = wd0[np.argsort(np.abs(wd0))]
    soft = int((np.abs(wd[32:]) < 1e-2).sum()); soft0 = int((np.abs(wd0[32:]) < 1e-2).sum())
    check("J7 curvature-squared term (lambda = -0.1): Kuhn nullity 5 -> 4 (vertex displacements only); D4 massless non-gauge directions 8 -> 6 (partners gapped)",
          nk0 == 5 and nk == 4 and soft0 == 8 and soft == 6, f"Kuhn {nk0} -> {nk}; D4 {soft0} -> {soft}; D4 next eigenvalue {abs(wd[32 + soft]):.2f}")
    # ---------------- J8
    def roots(C, ng, axis):
        vals = np.linspace(0.005, 3.0, 400); out = []
        def s_at(v):
            kk = np.array([0.05, 0.0, 0.0, (1j * v if axis == 'E' else v)])
            s_ = np.sort(np.linalg.svd(C.Q(kk) + lam * R2(C, kk), compute_uv=False)); return s_[ng] / s_[-1]
        f = np.array([s_at(v) for v in vals])
        return [vals[i] for i in range(1, len(vals) - 1) if f[i] < f[i - 1] and f[i] < f[i + 1] and f[i] < 1e-4]
    rk_t, rd_t = roots(K, 4, 'T'), roots(D, 32, 'T'); rk_e, rd_e = roots(K, 4, 'E'), roots(D, 32, 'E')
    check("J8 with the term: no real-k_t (tachyonic) rank drops in (0, 3) on either complex; the light-cone root omega = |k| = 0.05 is present",
          not rk_t and not rd_t and min(abs(np.array(rk_e) - 0.05)) < 0.01 and min(abs(np.array(rd_e) - 0.05)) < 0.01,
          f"Kuhn real-energy roots {np.round(rk_e, 3).tolist()}; D4 {np.round(rd_e, 3).tolist()}")
    # ---------------- J9
    itt, ixx = HC.index((3, 3)), HC.index((0, 0)); res = []
    for kk in [np.array([0, 0.02, 0, 0.0]), np.array([0, 0.012, 0.009, 0.0])]:
        T = np.zeros(10); T[itt] = 1.0; k2 = kk @ kk
        for lab, Cx, Lk in (('D4 face', D, face_metric(D, kk)), ('Kuhn rel', K, kuhn_reading(K, kk, True)), ('Kuhn plain', K, kuhn_reading(K, kk, False))):
            x = comp_inv(Cx.Q(kk) + lam * R2(Cx, kk), Cx.gauge(kk), Lk.conj().T @ T); h = Lk @ x
            res.append((lab, h[itt].real * k2, (h[ixx] / h[itt]).real))
    check("J9 with the term: static T_tt response h_tt k^2 = -2 and h_xx/h_tt = -1 for the D4 face reading and two Kuhn readings (on and off axis)",
          all(abs(r[1] + 2) < 2e-3 and abs(r[2] + 1) < 2e-3 for r in res), "; ".join(f"{r[0]} {r[1]:+.4f}/{r[2]:+.4f}" for r in res))
    # ---------------- J10
    kk = np.array([1.0, 0, 0, 0.0]); T = np.zeros(10); T[itt] = 1.0; Lk = face_metric(D, kk)
    h = (Lk @ comp_inv(D.Q(kk) + lam * R2(D, kk), D.gauge(kk), Lk.conj().T @ T))[itt].real
    nnv = 4 * np.sin(0.5) ** 2
    check("J10 the static D4 response is not an exact lattice Poisson equation: at |k| = 1, h_tt k^2 and h_tt sum 4 sin^2(k/2) both differ from -2 by > 1%",
          abs(h * 1.0 + 2) > 0.02 and abs(h * nnv + 2) > 0.02, f"h_tt k^2 {h:+.4f}; h_tt * 4 sin^2(1/2) {h * nnv:+.4f}")
    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
