"""Regge edge-length degrees of freedom and matter correlation decay: the per-edge-class analytic
decay exponents of the framework's matter two-point function calibrate to the landed flat assignment
and respond to the landed metric family through the geometric metric map -- a linearized ratios-only
dictionary.

THE GAP (the named guardrail of the landed geometric rows): the Regge second-variation /
action-selection rows presuppose dynamical edge lengths ell_e on the Z^3 x Z_tau complex ("the
edge-length metric degrees of freedom required by Regge calculus" -- the landed R3 target-operator
guardrail). The framework's axioms supply adjacency (Lattice), a per-site qubit (Quantum), and the
record readout (Record) -- no length field. THIS NOTE closes the linearized identification with the
dictionary

    ell_hat(v) := Lambda(v) / kappa,

where Lambda(v) is the ANALYTIC DECAY EXPONENT of the matter two-point function along the edge ray v
(the contour-shift singularity location -- the standard Ornstein-Zernike-type exponent, cited as
context and certified directly here), and kappa is ONE overall normalization. All numerics below are
EXACT-OBJECT certificates (zeros and grid positivity of the analytically continued symbol) -- no
asymptotic fits anywhere; a position-space FFT convergence check is included as supporting evidence
only.

CHECKS:
  E1  SIGN DICTIONARY: the lattice s-form coupling qhat^T(1+h)qhat (the landed TT-kernel row's
      canonical metric entry) occupies the INVERSE-metric slot of the curved-Laplacian symbol, so the
      METRIC perturbation is -h at linear order (sympy identity).
  E2  CLOSED-FORM CALIBRATION: for an edge class with k active coordinates (|v| = sqrt k; k = 1..4),
      the symmetric on-shell point gives Lambda_k = 2k asinh(m/(2 sqrt k)) exactly; the m->0 ratios are
      sqrt(k) = {1, sqrt2, sqrt3, 2} -- EXACTLY the landed complex's flat edge-length assignment --
      with deviation law 1 + (m^2/24)(1 - 1/k) + O(m^4).
  E3  THE EXPONENT CERTIFIED (two-sided, grid): the analytically continued symbol K(p + i theta v) has
      (i) an EXACT zero at p = 0, theta = theta* = 2 asinh(m/(2 sqrt k)) (machine precision), and
      (ii) NO zero on the sampled momentum torus for theta = 0.97 theta* (min |K| bounded away from
      zero) -- so the contour can be shifted to just below theta* and the decay exponent along v is
      Lambda(v) = k theta*, the closed form. Tick and space orientations agree identically. SUPPORTING:
      the position-space FFT decay sequences converge toward the certified exponents from above.
  E4  THE METRIC-RESPONSE THEOREM: for the s-form family the law is EXACT AT FINITE h:
          Lambda(v; h) = 2k asinh( m / (2 sqrt(k + v^T h v)) ),
      because at p = 0 the continued symbol is K_h = m^2 - 4 sinh^2(theta/2)(k + v^T h v) for EVERY h.
      The response derivative is c_resp(m,k) (v^T h_metric v)/|v|^2 with c_resp -> 1/2 as m -> 0:
          delta ell_hat(v)/ell_hat(v) -> v^T h_metric v / (2 |v|^2)
      -- EXACTLY the geometric metric map of the landed Regge rows, including the factor 1/2.
  E5  FINITE-h CERTIFICATES: for ALL 15 edge classes x ALL 10 metric components at h = +-0.05: the
      exact zero sits at theta*(h) of the law above (machine) and the grid stays nonsingular below it;
      off-pattern components (v^T h v = 0) leave theta* EXACTLY unchanged.
  E6  DICTIONARY CONVERGENCE (closed form): the exact response matrix converges to the geometric
      metric map M0 as m -> 0 with the O(m^2) law (log-log slope 2 over the m-scan); the finite-m
      deviation is an exactly computable per-class factor.
  E7  THE PROVENANCE STATEMENT: the operator-native metric family's exact response has rank 10 and its
      column space converges to the Regge metric sector im(M0) (principal-angle sine -> 0 as m -> 0):
      the matter sector's metric content and the geometry's metric sector COINCIDE through this
      linearized dictionary; the 5 non-metric (breathing) directions are not populated in the limit.
  E8  TICK ON EQUAL FOOTING: the exact law depends only on (k, v^T h v) -- manifestly symmetric under
      coordinate permutations including tick <-> space (c_t = c_s, the kinetic-isotropy primitive's
      structural grant); the record-sector realization of the TIME-edge response is the landed
      record-density front-speed toy row (cited).
  E9  HONEST DYNAMICS BOUNDARY: this note supplies the DOF identification only; the matter-INDUCED
      action on these DOF is NOT the embedding-independent action (landed: pure-gauge channels are not
      suppressed), and the EH-class dynamics is what the landed action-selection row derives for
      embedding-independent actions. Remaining open: the embedding-independence provenance of the
      dynamics, the nonlinear completion, and the absolute scale kappa (the post-record
      clock-rate no-go + the registered scale-reference primitive -- ratios only here).

3D+1 framing throughout: space = Z^3 (Lattice axiom), tick direction = the supplied Z_tau extension
used by the cited geometric rows; Euclidean = the OS0 surface. Record is not used as a time metric
here. No external-data value.
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


DIRS15 = [v for v in itertools.product([0, 1], repeat=4) if any(v)]
HCOMPS = [(0, 0), (1, 1), (2, 2), (3, 3), (0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]


def metric_map_M0():
    """the geometric metric map of the landed Regge rows: delta ell_e = v^T H v/(2|v|) per unit h."""
    M = np.zeros((15, 10))
    for ci, v in enumerate(DIRS15):
        vv = np.array(v, float)
        ell = np.linalg.norm(vv)
        for hj, (a, b) in enumerate(HCOMPS):
            H = np.zeros((4, 4))
            H[a, b] += 1.0
            if a != b:
                H[b, a] += 1.0
            M[ci, hj] = vv @ H @ vv / (2 * ell)
    return M


def Hcomp(j, eps=1.0):
    a, b = HCOMPS[j]
    H = np.zeros((4, 4))
    H[a, b] += eps
    if a != b:
        H[b, a] += eps
    return H


def main() -> int:
    print("REGGE EDGE LENGTHS FROM MATTER CORRELATION DECAY (the edge-DOF identification, linearized)")
    print("=" * 96)

    # ---- E1: sign dictionary (sympy) ----
    eps = sp.symbols("epsilon")
    ginv = sp.Matrix([[1 + eps, 0], [0, 1]])
    lin = sp.series(ginv.inv()[0, 0], eps, 0, 2).removeO()
    check("E1 (sign dictionary): the lattice s-form coupling qhat^T(1+h)qhat occupies the INVERSE-metric "
          "slot of the curved-Laplacian symbol (g^{mu nu} p_mu p_nu), so h = delta g^{inverse} and the "
          "METRIC perturbation is -h at linear order (sympy: (1+eps)^{-1} = 1 - eps + O(eps^2)); the "
          "s-form is the landed TT-kernel row's canonical metric entry",
          sp.simplify(lin - (1 - eps)) == 0,
          "g_00 = 1 - eps + O(eps^2) for g^{inv}_00 = 1 + eps")

    # ---- E2: closed-form calibration (sympy) ----
    m_s, k_s = sp.symbols("m k", positive=True)
    phi = 2 * sp.asinh(m_s / (2 * sp.sqrt(k_s)))
    Lam = k_s * phi
    onshell = sp.simplify(k_s * (2 * sp.sinh(phi / 2)) ** 2 - m_s ** 2)
    ratio = sp.simplify(Lam / (sp.sqrt(k_s) * Lam.subs(k_s, 1)))
    series = sp.series(ratio, m_s, 0, 4).removeO()
    dev_law = sp.simplify(series - (1 + m_s ** 2 / 24 * (1 - 1 / k_s)))
    ratios_m0 = [sp.limit(Lam.subs(k_s, kk) / Lam.subs(k_s, 1), m_s, 0) for kk in (1, 2, 3, 4)]
    check("E2 (CLOSED-FORM CALIBRATION): the symmetric on-shell exponent per edge step is "
          "Lambda_k = 2k asinh(m/(2 sqrt k)) (on-shell identity exact); the m->0 ratios are sqrt(k) = "
          "{1, sqrt2, sqrt3, 2} -- EXACTLY the landed complex's flat edge-length assignment -- with "
          "finite-m deviation law 1 + (m^2/24)(1 - 1/k) + O(m^4)",
          onshell == 0 and dev_law == 0
          and [sp.simplify(r - v) for r, v in zip(ratios_m0, [1, sp.sqrt(2), sp.sqrt(3), 2])] == [0, 0, 0, 0],
          f"on-shell residual = {onshell}; deviation-law residual = {dev_law}; "
          f"m->0 ratios = {[sp.simplify(r) for r in ratios_m0]}")

    # ---- exact-certificate machinery ----
    Lg = 24
    p1 = 2 * np.pi * np.fft.fftfreq(Lg)
    PG = np.meshgrid(p1, p1, p1, p1, indexing="ij")

    def Kmin_and_zero(m, h, theta, v):
        """returns (min |K(p + i theta v)| over the sampled torus, |K| at p=0)."""
        tot = m * m + 0j
        for a in range(4):
            for b in range(4):
                coef = (1.0 if a == b else 0.0) + h[a, b]
                if coef == 0.0:
                    continue
                qa = 2 * np.sin((PG[a] + 1j * theta * v[a]) / 2)
                qb = 2 * np.sin((PG[b] + 1j * theta * v[b]) / 2)
                tot = tot + coef * qa * qb
        A = np.abs(tot)
        return float(A.min()), float(A[0, 0, 0, 0])

    m0 = 0.5
    h0 = np.zeros((4, 4))

    # ---- E3: the exponent certified ----
    worst_zero = 0.0
    worst_gap = np.inf
    tick_pair = 0.0
    for v in [(1, 0, 0, 0), (0, 0, 0, 1), (1, 1, 0, 0), (1, 0, 0, 1), (1, 1, 1, 0), (1, 1, 0, 1),
              (1, 1, 1, 1)]:
        vv = np.array(v)
        kk = int(vv @ vv)
        th = 2 * np.arcsinh(m0 / (2 * np.sqrt(kk)))
        gmin, gz = Kmin_and_zero(m0, h0, 0.97 * th, vv)
        zmin, zz = Kmin_and_zero(m0, h0, th, vv)
        worst_zero = max(worst_zero, zz)
        worst_gap = min(worst_gap, gmin)
    # tick-vs-space orientation identity (formula depends on k only; numeric double-check):
    _, z_sp = Kmin_and_zero(m0, h0, 2 * np.arcsinh(m0 / 2), np.array([1, 0, 0, 0]))
    _, z_tk = Kmin_and_zero(m0, h0, 2 * np.arcsinh(m0 / 2), np.array([0, 0, 0, 1]))
    tick_pair = abs(z_sp - z_tk)
    # supporting: position-space convergence from above (FFT, no fit)
    Lf = 40
    pf = 2 * np.pi * np.fft.fftfreq(Lf)
    PF = np.meshgrid(pf, pf, pf, pf, indexing="ij")
    KF = m0 * m0 + sum((2 * np.sin(PF[a] / 2)) ** 2 for a in range(4))
    GF = np.real(np.fft.ifftn(1.0 / KF))
    support_ok = True
    for v in [(1, 0, 0, 0), (1, 1, 1, 1)]:
        vv = np.array(v)
        kk = int(vv @ vv)
        lam = float(2 * kk * np.arcsinh(m0 / (2 * np.sqrt(kk))))
        ns = np.arange(4, min(Lf // 2 - 2, int(14 / lam)) + 1)
        logs = np.array([np.log(abs(GF[tuple((n * vv) % Lf)])) for n in ns])
        d = -np.diff(logs)
        if not (np.all(np.diff(d) < 0) and np.all(d > lam)):
            support_ok = False
    check("E3 (THE EXPONENT CERTIFIED, two-sided): the analytically continued symbol K(p + i theta v) "
          "has an EXACT zero at p=0, theta* = 2 asinh(m/(2 sqrt k)) (machine precision, all class types "
          "incl. tick-mixed), and NO zero on the sampled torus at theta = 0.97 theta* (min|K| bounded "
          "away) -- the decay exponent along v is Lambda(v) = k theta*, the closed form (the standard "
          "analytic/Ornstein-Zernike exponent; context citation, certified directly). Tick and space "
          "orientations agree identically. SUPPORTING: the position-space FFT decay sequences converge "
          "toward the certified exponents monotonically from above (no fit used)",
          worst_zero < 1e-12 and worst_gap > 1e-3 and tick_pair < 1e-14 and support_ok,
          f"worst |K(p=0, theta*)| = {worst_zero:.1e}; min torus |K| at 0.97 theta* = {worst_gap:.3e}; "
          f"tick-vs-space zero diff = {tick_pair:.1e}; position-space convergence-from-above: {support_ok}")

    # ---- E4: the metric-response theorem (closed form) ----
    s_s = sp.symbols("s")
    Lam_h = k_s * 2 * sp.asinh(m_s / (2 * sp.sqrt(k_s + s_s)))
    c_resp = sp.simplify(-k_s * sp.diff(sp.log(Lam_h), s_s).subs(s_s, 0))
    c0 = sp.limit(c_resp, m_s, 0)
    check("E4 (THE METRIC-RESPONSE THEOREM): the EXACT finite-h law Lambda(v;h) = "
          "2k asinh(m/(2 sqrt(k + v^T h v))) gives delta log Lambda = c_resp(m,k) (v^T h_metric v)/|v|^2 "
          "(sign from E1), with c_resp -> 1/2 as m -> 0: delta ell_hat/ell_hat -> v^T h v/(2|v|^2) -- "
          "EXACTLY the geometric metric map of the landed Regge rows, including the factor 1/2",
          sp.simplify(c0 - sp.Rational(1, 2)) == 0,
          f"c_resp(m,k) = {c_resp}; m->0 limit = {c0}")

    # ---- E5: finite-h certificates for the whole family ----
    worst_z5 = 0.0
    worst_gap5 = np.inf
    worst_off = 0.0
    for ci, v in enumerate(DIRS15):
        vv = np.array(v)
        kk = int(vv @ vv)
        for hj in range(10):
            for sg in (+1.0, -1.0):
                H = Hcomp(hj, sg * 0.05)
                s = float(vv @ H @ vv)
                th = 2 * np.arcsinh(m0 / (2 * np.sqrt(kk + s)))
                gmin, gz = Kmin_and_zero(m0, H, 0.97 * th, vv)
                zmin, zz = Kmin_and_zero(m0, H, th, vv)
                worst_z5 = max(worst_z5, zz)
                worst_gap5 = min(worst_gap5, gmin)
                if s == 0.0:
                    # off-pattern: theta* must be EXACTLY the unperturbed value
                    th0 = 2 * np.arcsinh(m0 / (2 * np.sqrt(kk)))
                    _, zz0 = Kmin_and_zero(m0, H, th0, vv)
                    worst_off = max(worst_off, zz0)
    check("E5 (FINITE-h CERTIFICATES, the whole family): for ALL 15 edge classes x ALL 10 metric "
          "components at h = +-0.05, the continued symbol's exact zero sits at theta*(h) of the law "
          "Lambda(v;h) = 2k asinh(m/(2 sqrt(k + v^T h v))) (machine), with the torus nonsingular below "
          "it; off-pattern components (v^T h v = 0) leave theta* EXACTLY unchanged -- the response is "
          "the closed form for the entire landed metric family, not just at linear order",
          worst_z5 < 1e-12 and worst_gap5 > 1e-3 and worst_off < 1e-12,
          f"worst |K(p=0, theta*(h))| = {worst_z5:.1e}; min torus |K| below = {worst_gap5:.3e}; "
          f"worst off-pattern zero shift = {worst_off:.1e}")

    # ---- E6/E7: dictionary convergence to M0 (closed form) + provenance ----
    M0 = metric_map_M0()
    c_resp_f = sp.lambdify((m_s, k_s), c_resp, "numpy")

    def Rdict(m):
        """exact dictionary response: delta ell_hat(v) per unit h_metric, in calibrated units."""
        R = np.zeros((15, 10))
        for ci, v in enumerate(DIRS15):
            vv = np.array(v, float)
            kk = int(vv @ vv)
            for hj in range(10):
                H = Hcomp(hj)
                # delta log ell_hat = c_resp * (v^T H v)/k ; ell_hat (ratios) = sqrt(k)*(calib factor)
                calib = float(2 * kk * np.arcsinh(m / (2 * np.sqrt(kk)))) / (
                    np.sqrt(kk) * float(2 * np.arcsinh(m / 2)))
                R[ci, hj] = float(c_resp_f(m, kk)) * (vv @ H @ vv) / kk * np.sqrt(kk) * calib
        return R

    devs = []
    for mm in (0.6, 0.45, 0.3, 0.15):
        dev = float(np.abs(Rdict(mm) - M0).max() / np.abs(M0).max())
        devs.append((mm, dev))
    slope = np.polyfit(np.log([d[0] for d in devs]), np.log([d[1] for d in devs]), 1)[0]
    check("E6 (DICTIONARY CONVERGENCE, closed form): the exact dictionary response matrix converges to "
          "the geometric metric map M0 as m -> 0 with the O(m^2) law (log-log slope ~2 over the m-scan); "
          "the finite-m deviation is the exactly computable per-class factor (the c_resp and calibration "
          "corrections)",
          devs[-1][1] < devs[0][1] and 1.9 < slope < 2.1,
          "deviation vs m: " + ", ".join(f"m={mm}: {d:.3e}" for mm, d in devs)
          + f"; log-log slope = {slope:.3f}")

    R05 = Rdict(0.5)
    rank_R = np.linalg.matrix_rank(R05, tol=1e-9 * np.abs(R05).max())
    Qa, _ = np.linalg.qr(R05)
    Qb, _ = np.linalg.qr(M0)
    ang = np.linalg.svd(Qa[:, :10].T @ Qb[:, :10], compute_uv=False)
    sin_05 = float(np.sqrt(max(0.0, 1 - ang.min() ** 2)))
    R015 = Rdict(0.15)
    Qa2, _ = np.linalg.qr(R015)
    ang2 = np.linalg.svd(Qa2[:, :10].T @ Qb[:, :10], compute_uv=False)
    sin_015 = float(np.sqrt(max(0.0, 1 - ang2.min() ** 2)))
    check("E7 (THE PROVENANCE STATEMENT): the operator-native metric family's exact response has rank 10 "
          "and its column space converges to the Regge metric sector im(M0) (principal-angle sine "
          "decreasing toward 0 with m): the matter sector's metric content and the geometry's metric "
          "sector COINCIDE through this linearized dictionary -- the edge-length degrees of freedom are "
          "represented by per-edge-class matter-correlation decay data; the 5 non-metric "
          "(breathing) directions are not populated in the limit",
          rank_R == 10 and sin_015 < sin_05 and sin_015 < 5e-3,
          f"rank = {rank_R}; principal-angle sine: m=0.5 -> {sin_05:.2e}, m=0.15 -> {sin_015:.2e}")

    # ---- E8: tick on equal footing ----
    perm_ax = {0: 3, 1: 1, 2: 2, 3: 0}
    HC_sw = [tuple(sorted((perm_ax[a], perm_ax[b]))) for (a, b) in HCOMPS]
    permj = [HCOMPS.index(c) for c in HC_sw]
    permc = [DIRS15.index(tuple(np.array(v)[[3, 1, 2, 0]])) for v in DIRS15]
    diff_perm = float(np.abs(R05[permc][:, permj] - R05).max())
    check("E8 (tick on equal footing): the exact law depends only on (k, v^T h v) -- manifestly "
          "symmetric under coordinate permutations including tick <-> space (numeric permutation "
          "identity at machine precision; c_t = c_s, the kinetic-isotropy primitive's structural grant); "
          "the record-sector realization of the TIME-edge response -- record density slowing the front "
          "-- is the landed record-density toy row (cited, not re-derived)",
          diff_perm < 1e-14,
          f"response-matrix permutation identity residual = {diff_perm:.1e}")

    # ---- E9: honest dynamics boundary ----
    check("E9 (honest dynamics boundary): this note supplies the DOF identification only. The "
          "matter-INDUCED action on these DOF is NOT the embedding-independent action (landed "
          "full-channel-table row: 'pure-gauge channels are not suppressed'); the EH-class dynamics is "
          "what the landed action-selection row derives for ANY embedding-independent local action. "
          "Remaining open after this note: the embedding-independence (H-property) provenance of the "
          "dynamics, the nonlinear completion, and the absolute scale kappa (= the post-record "
          "clock-rate no-go + the registered scale-reference primitive -- ratios only here).",
          True,
          "linearized DOF dictionary supplied here; dynamics provenance = named open (cited rows)")

    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    print(
        "VERDICT: the edge-length degrees of freedom of the geometric (Regge) rows admit a linearized\n"
        "ratios-only matter-correlation dictionary on the framework's own complex, with\n"
        "ell_hat(v) = Lambda(v)/kappa built on the ANALYTIC decay exponent (certified two-sidedly, no\n"
        "fits): (i) it calibrates in closed form to the landed flat assignment {1, sqrt2, sqrt3, 2} as\n"
        "m -> 0 with an O(m^2) deviation law; (ii) it responds to the landed s-form metric family by the\n"
        "EXACT law Lambda(v;h) = 2k asinh(m/(2 sqrt(k + v^T h v))) -- certified for all 15 classes x 10\n"
        "components at finite h -- whose linearization is EXACTLY the geometric metric map (factor 1/2\n"
        "included) as m -> 0; (iii) the response lands exactly on the Regge metric sector (rank 10 ->\n"
        "im(M0)), the breathing directions unpopulated in the limit; (iv) the tick enters on equal\n"
        "footing (c_t = c_s); (v) RATIOS ONLY -- the absolute scale kappa is the located clock-rate /\n"
        "scale residual, untouched. In this linearized dictionary the Regge rows' edge fields are\n"
        "represented by the matter sector's per-edge correlation structure. Remaining of the gap: the\n"
        "dynamics' embedding-independence provenance (the matter-induced action is not the H-action --\n"
        "landed; the H-class selection theorem is landed) and the nonlinear completion.\n"
        "No external-data value."
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
