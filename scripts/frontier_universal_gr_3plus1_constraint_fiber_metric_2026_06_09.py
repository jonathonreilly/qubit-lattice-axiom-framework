"""3+1 constraint/multiplier structure of the linearized EH target operator: the derived
non-degenerate (lambda-one) kinetic fiber metric, the derived comparator potential signs, and the
discretization-robust multiplier structure on the symmetric Z^3 x Z_tau lattice.

ENGAGES THE ACTUAL NO-GOS (read in full, quoted at their stated scope):
  - UNIVERSAL_GR_DEGENERATE_SUPERMETRIC_GRAVITON_SIGN_NO_GO (#3220 row): given (1) a degenerate
    trace=shear supermetric, (2) the DERIVED gluing law omega^2=V/G, (3) SUPPLIED opposite-signed
    comparator potentials, both channel signs cannot be healthy. Its own N1/N6 name the open bypass:
    "a derived non-degenerate fiber metric" (the GR lambda=1 control passes its T3 inside the same law).
  - UNIVERSAL_GR_QUADRATIC_MODE_GLUING_DERIVATION: omega^2=V/G holds for "a diagonal bounded channel
    with quadratic Lagrangian L = (1/2)G qdot^2 - (1/2)V q^2" -- i.e. an UNCONSTRAINED free channel.
  - UNIVERSAL_GR_SUPERMETRIC_NORMAL_FORM (retained): the records-route Hessian -Tr(D^-1 h D^-1 k) is
    ALL-NEGATIVE and trace=shear DEGENERATE (lapse -a^-2, shift -(ab)^-1, trace -b^-2, shear -b^-2);
    its own open item is the "Einstein/Regge glue ... using the route-2 slice dynamics".
  - R3_GEOMETRIC_REGGE_LINEARIZATION (landed): target-operator certificate only (gauge zero modes,
    G_lin(h_TT)=+k^2/2 h_TT at the spacelike frame, trace acted differently); explicitly does NOT supply
    the 3+1 kinetic/multiplier split -- which is what THIS runner adds.

WHAT THIS RUNNER DERIVES (sympy, from the metric/curvature definitions only -- math, not import):
  A1  anchor: the linearized Einstein operator built here reproduces the landed R3 facts identically in
      (omega,k): gauge modes are EXACT zero modes (all xi, symbolically), and on the TT sample
      G(h_TT) = (1/2)(k^2-omega^2) h_TT  (at omega=0: the landed +k^2/2; dispersion omega^2=k^2).
  A2  MULTIPLIER STRUCTURE, SCHEME-INDEPENDENT: writing every second derivative d_mu d_nu as a FORMAL
      symbol S(mu,nu), the constraint rows G^{00}, G^{0i} have ZERO coefficient on S(0,0) (no qddot
      anywhere in them; G^{00} has no time derivatives at all after the trace-reversal cancellation).
      Because the statement is "the S(0,0) coefficient is the zero polynomial", it survives ANY stencil
      substitution: the lapse/shift multiplier structure is DISCRETIZATION-ROBUST (structural).
  A3  THE DERIVED NON-DEGENERATE FIBER METRIC (the no-go's named bypass): the kinetic matrix
      K = -coeff(G^{ij}, S(0,0)) on spatial channels has the lambda-one DeWitt pattern:
      K_trace : K_TT = -2 : +1 (trace NEGATIVE, shear POSITIVE -- indefinite, NON-degenerate), and the
      lapse/shift kinetic weights are ZERO. This is a DIFFERENT object from the retained records-route
      supermetric (all-negative, degenerate) -- derived from the geometric target operator itself.
  A4  THE DERIVED COMPARATOR POTENTIAL SIGNS: at omega=0 the same operator gives
      V_TT = +k^2/2 > 0 and V_trace < 0 (transverse-trace channel) -- the no-go's SUPPLIED pair
      (V_trace=-k^2/2, V_TT=+k^2/2) is now derived from the target operator.
  A5  GLUING WITH BOTH HALVES DERIVED: omega^2_TT = V_TT/K_TT = +k^2 (healthy) and
      omega^2_trace = V_trace/K_trace = (neg)/(neg) > 0 -- the no-go's own lambda-one control (its T3)
      is reproduced with DERIVED inputs: the degenerate-supermetric obstruction is BYPASSED exactly
      through the route its N1/N6 left open.
  A6  THE CONSTRAINT CONTENT: G^{00} is proportional to k^2 x (transverse spatial trace) -- the
      linearized Hamiltonian constraint. In vacuum at k != 0 it forces that channel to zero: the trace
      is NOT a free "diagonal bounded channel", so the gluing theorem's hypothesis does not apply to it
      in the constrained 3+1 system (it is eliminated, not glued).
  A7  DOF COUNT (exact rank algebra at rational points): at generic omega^2 the kernel of the full
      10x10 operator is EXACTLY the 4-parameter gauge family; at omega^2 = k^2 it is 4+2: precisely TWO
      propagating physical modes, both TT, healthy dispersion.
  A8  DISCRETE TRANSCRIPTION (kinetic-isotropy primitive c_t = c_s; declared symmetrized stencils:
      S(mu,mu) = -(2 sin(p_mu/2))^2, S(mu!=nu) = -sin(p_mu) sin(p_nu)): the multiplier structure holds
      VERBATIM (A2 is S-formal); the discrete TT dispersion is 4 sin^2(omega/2) = 4 sin^2(k/2), i.e.
      omega = +-k EXACTLY across the BZ (healthy, no extra branch); the kinetic/potential channel
      weights keep the lambda-one pattern; the gauge-mode residual is nonzero at finite k (the measured
      lattice diffeomorphism-breaking) with the measured order in k reported.
  A9  TIE-IN: with the RETAINED records-supermetric weights (degenerate trace=shear) the no-go's
      negative product is reproduced; with the DERIVED geometric fiber metric it is positive: the no-go
      binds the records-Hessian gluing specifically, and the geometric target operator carries its own
      healthy gluing -- the division of labor sharpened.

WHAT THIS RUNNER DOES NOT CLAIM: it does not derive the geometric ACTION from the framework (the
Einstein/Regge glue, edge-length degrees of freedom, and action selection remain open -- the retained
supermetric note's own frontier and the R3 note's guardrails); it does not compute the cubic-Coxeter
Regge second variation; the discrete part is a declared-stencil transcription of the target operator;
linearized/abelian-gauge scope only (nonlinear constraint closure on discrete time is known-open,
cited as context). No PDG/fitted value.
"""
from __future__ import annotations
import itertools
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


# ---------------------------------------------------------------- linearized Einstein operator, S-formal
ETA = sp.diag(-1, 1, 1, 1)
IDX = list(range(4))

# formal second-derivative symbols S[mu][nu] (symmetric): d_mu d_nu h_ab  ->  S(mu,nu) * h_ab
S = [[sp.Symbol(f"S{min(m,n)}{max(m,n)}") for n in IDX] for m in IDX]

# 10 independent metric perturbation symbols
hsym = {}
for a in IDX:
    for b in IDX:
        if a <= b:
            hsym[(a, b)] = sp.Symbol(f"h{a}{b}")
H = sp.Matrix(4, 4, lambda a, b: hsym[(min(a, b), max(a, b))])
HVARS = [hsym[k] for k in sorted(hsym)]          # canonical order of the 10 components


def ricci_lin(Hm):
    """linearized Ricci with d_mu d_nu -> S[mu][nu]:
    R_mn = (1/2) eta^{lr} [ S(l,m) h_rn + S(l,n) h_rm - S(l,r) h_mn - S(m,n) h_lr ]."""
    R = sp.zeros(4, 4)
    for m in IDX:
        for n in IDX:
            acc = 0
            for l in IDX:
                acc += ETA[l, l] * (S[l][m] * Hm[l, n] + S[l][n] * Hm[l, m]
                                    - S[l][l] * Hm[m, n] - S[m][n] * Hm[l, l])
            R[m, n] = sp.Rational(1, 2) * acc
    return R


def einstein_lin(Hm):
    R = ricci_lin(Hm)
    Rs = sum(ETA[m, m] * R[m, m] for m in IDX)
    G = sp.zeros(4, 4)
    for m in IDX:
        for n in IDX:
            G[m, n] = R[m, n] - sp.Rational(1, 2) * ETA[m, n] * Rs
    # raise both indices: G^{mn} = eta^{ma} eta^{nb} G_ab (eta diagonal)
    Gup = sp.zeros(4, 4)
    for m in IDX:
        for n in IDX:
            Gup[m, n] = ETA[m, m] * ETA[n, n] * G[m, n]
    return Gup


G_FORMAL = einstein_lin(H)                       # 4x4, entries linear in h, linear in the S symbols

w, k = sp.symbols("omega kk", real=True)

CONT = {S[m][n]: -([w, k, 0, 0][m]) * ([w, k, 0, 0][n]) for m in IDX for n in IDX if m <= n}
# declared symmetrized lattice stencils, c_t = c_s (kinetic-isotropy primitive):
def lat_sym(m, n):
    p = [w, k, 0, 0]
    if m == n:
        return -(2 * sp.sin(p[m] / 2)) ** 2
    return -sp.sin(p[m]) * sp.sin(p[n])
LATT = {S[m][n]: lat_sym(m, n) for m in IDX for n in IDX if m <= n}


def subs_scheme(expr, scheme):
    return sp.expand(expr.subs(scheme))


def op_matrix(scheme):
    """10x10 matrix of G^{ab} (rows: (a<=b) pairs canonical order) acting on HVARS."""
    rows = []
    for a in IDX:
        for b in IDX:
            if a <= b:
                e = subs_scheme(G_FORMAL[a, b], scheme)
                rows.append([sp.expand(sp.diff(e, v)) for v in HVARS])
    return sp.Matrix(rows)


def hmat(d):
    M = sp.zeros(4, 4)
    for (a, b), v in d.items():
        M[a, b] += v
        if a != b:
            M[b, a] += v
    return M


def hvec(M):
    return sp.Matrix([M[a, b] for a in IDX for b in IDX if a <= b])


def main() -> int:
    print("3+1 CONSTRAINT STRUCTURE OF THE LINEARIZED EH TARGET OPERATOR (derived fiber metric)")
    print("=" * 96)

    # ---- A1: anchor to the landed R3 target-operator facts ----
    xi = [sp.Symbol(f"xi{m}") for m in IDX]
    p4 = [w, k, 0, 0]
    h_gauge = hmat({(a, b): p4[a] * xi[b] + p4[b] * xi[a] if a <= b else 0
                    for a in IDX for b in IDX if a <= b})
    # careful: build properly symmetric gauge mode h_ab = p_a xi_b + p_b xi_a
    h_gauge = sp.Matrix(4, 4, lambda a, b: p4[a] * xi[b] + p4[b] * xi[a])
    Gg = einstein_lin(h_gauge).subs(CONT)
    gauge_zero = all(sp.simplify(Gg[a, b]) == 0 for a in IDX for b in IDX)
    h_tt = sp.Matrix(4, 4, lambda a, b: 1 if {a, b} == {2, 3} else 0)   # yz polarization, k || x
    Gtt = einstein_lin(h_tt).subs(CONT)
    tt_fact = sp.simplify(Gtt[2, 3] - sp.Rational(1, 2) * (k ** 2 - w ** 2) * 1)
    tt_others = all(sp.simplify(Gtt[a, b]) == 0 for a in IDX for b in IDX if {a, b} != {2, 3})
    check("A1 (anchor to the landed R3 target-operator certificate): gauge modes h = p (x) xi + xi (x) p "
          "are EXACT zero modes symbolically (all xi, all omega,k), and the yz TT sample gives "
          "G(h_TT) = (1/2)(k^2 - omega^2) h_TT -- at omega=0 the landed +k^2/2, dispersion omega^2=k^2",
          gauge_zero and tt_fact == 0 and tt_others,
          "gauge zero modes exact; G_23(h_TT) = (k^2-omega^2)/2; all other components zero")

    # ---- A2: multiplier structure, S-formal (scheme-independent) ----
    s00 = S[0][0]
    bad = []
    for (a, b) in [(0, 0), (0, 1), (0, 2), (0, 3)]:
        c = sp.expand(sp.diff(G_FORMAL[a, b], s00))
        if sp.simplify(c) != 0:
            bad.append((a, b, c))
    # G^{00} stronger: no time derivatives AT ALL (no S(0,mu) of any kind)
    no_t_at_all = all(sp.simplify(sp.diff(G_FORMAL[0, 0], S[0][m])) == 0 for m in IDX)
    check("A2 (MULTIPLIER STRUCTURE, scheme-independent): with every second derivative a FORMAL symbol "
          "S(mu,nu), the constraint rows G^{00}, G^{0i} have ZERO coefficient on S(0,0) (no qddot in any "
          "constraint row -- the trace-reversal cancels them), and G^{00} contains NO time-derivative "
          "symbol S(0,mu) at all. A zero polynomial stays zero under ANY stencil substitution: the "
          "lapse/shift multiplier structure is DISCRETIZATION-ROBUST (structural).",
          not bad and no_t_at_all,
          "coeff(G^{00},S00)=coeff(G^{0i},S00)=0 identically; G^{00} free of S(0,mu) entirely")

    # ---- A3: the derived non-degenerate (lambda-one) kinetic fiber metric ----
    # EOM rows carry c2 * S00 with S00 <-> -omega^2 (continuum), so the gluing kinetic coefficient is
    # c2 = +coeff(G^{ab}, S00). The quadratic-form pairing over tensors is Q(h) = sum_ab h_ab G^{ab}(h)
    # = sum_{a<=b} (2 - delta_ab) h_ab G^{ab}(h)  (off-diagonal components appear twice in the tensor sum).
    pairs = [(a, b) for a in IDX for b in IDX if a <= b]
    PAIRW = sp.Matrix([2 - (1 if a == b else 0) for (a, b) in pairs])
    Kmat = sp.Matrix(10, 10, lambda i, j: 0)
    for i, (a, b) in enumerate(pairs):
        e = sp.expand(sp.diff(G_FORMAL[a, b], s00))
        for j, v in enumerate(HVARS):
            Kmat[i, j] = sp.diff(e, v)
    def chan(d):
        v = hvec(hmat(d))
        n = sp.sqrt(sum(x ** 2 for x in hmat(d)))    # Frobenius norm of the tensor
        return v / n
    e_tr = chan({(1, 1): 1, (2, 2): 1, (3, 3): 1})                  # spatial trace /sqrt3
    e_yz = chan({(2, 3): 1})                                          # TT yz /sqrt2
    e_E = chan({(2, 2): 1, (3, 3): -1})                               # TT E /sqrt2
    e_lapse = chan({(0, 0): 1})
    e_shift = chan({(0, 2): 1})
    def quad(M, u, v=None):
        v = u if v is None else v
        Mv = M * v
        return sp.simplify(sum(PAIRW[i] * u[i] * Mv[i] for i in range(10)))
    K_tr, K_yz, K_E = quad(Kmat, e_tr), quad(Kmat, e_yz), quad(Kmat, e_E)
    K_lapse, K_shift = quad(Kmat, e_lapse), quad(Kmat, e_shift)
    ratio = sp.simplify(K_tr / K_yz)
    check("A3 (THE DERIVED NON-DEGENERATE FIBER METRIC -- the no-go's named bypass): the kinetic "
          "coefficient c2 = +coeff(G^{ij},S00) in the tensor pairing has the lambda-one DeWitt pattern on "
          "spatial channels: K_trace NEGATIVE, K_TT POSITIVE, ratio K_trace:K_TT = -2:+1 (indefinite, "
          "NON-degenerate; both TT channels equal), and the lapse/shift kinetic weights are ZERO -- a "
          "DIFFERENT object from the retained records-route supermetric (all-negative, trace=shear "
          "degenerate)",
          K_tr < 0 and K_yz > 0 and ratio == -2 and sp.simplify(K_yz - K_E) == 0
          and K_lapse == 0 and K_shift == 0,
          f"K_trace={K_tr}, K_TT(yz)={K_yz}, K_TT(E)={K_E} (ratio {ratio}); K_lapse={K_lapse}, K_shift={K_shift}")

    # ---- A4: the derived comparator potential signs ----
    M0 = op_matrix(CONT).subs(w, 0)                                   # omega=0: the potential block
    e_trT = chan({(2, 2): 1, (3, 3): 1})                              # transverse trace (k || x)
    V_yz = quad(M0, e_yz)
    V_trT = quad(M0, e_trT)
    check("A4 (THE DERIVED COMPARATOR POTENTIAL SIGNS): at omega=0 the SAME operator gives "
          "V_TT = +k^2/2 > 0 and V_trace(transverse) < 0 -- the no-go's SUPPLIED pair "
          "(V_TT=+k^2/2, V_trace=-k^2/2) is now derived from the target operator",
          sp.simplify(V_yz - k ** 2 / 2) == 0 and sp.simplify(V_trT + k ** 2 / 2) == 0,
          f"V_TT(yz)={V_yz}; V_trace(transverse)={V_trT}")

    # ---- A5: gluing with both halves derived ----
    # glue per the no-go's own law omega^2 = V/G with the DERIVED channel pairs:
    # TT: (G,V) = (K_yz, V_yz); trace: (G,V) = (K on the transverse-trace channel, V_trT)
    om2_tt = sp.simplify(V_yz / K_yz)
    K_trT = quad(Kmat, e_trT)
    om2_tr = sp.simplify(V_trT / K_trT)
    check("A5 (GLUING WITH BOTH HALVES DERIVED): omega^2_TT = V_TT/K_TT = +k^2 (healthy) and "
          "omega^2_trace = V_trace/K_trace = (neg)/(neg) > 0 -- the no-go's lambda-one control (its T3) "
          "reproduced with DERIVED inputs: the degenerate-supermetric obstruction is BYPASSED exactly "
          "through the 'derived non-degenerate fiber metric' route its N1/N6 left open",
          sp.simplify(om2_tt - k ** 2) == 0 and K_trT < 0 and V_trT.subs(k, 1) < 0 and
          sp.simplify(om2_tr).subs(k, 1) > 0,
          f"omega^2_TT={om2_tt}; K_trace(transverse)={K_trT}, V_trace={V_trT} -> omega^2_trace={om2_tr} > 0")

    # ---- A6: the constraint content (the gluing hypothesis fails for the trace) ----
    G00 = subs_scheme(G_FORMAL[0, 0], CONT)
    # expect G^{00} = +(1/2) k^2 (h22+h33) exactly (k || x; all other components drop)
    c22 = sp.simplify(sp.diff(G00, hsym[(2, 2)]))
    c33 = sp.simplify(sp.diff(G00, hsym[(3, 3)]))
    others = [v for key, v in hsym.items() if key not in ((2, 2), (3, 3))
              and sp.simplify(sp.diff(G00, v)) != 0]
    check("A6 (CONSTRAINT CONTENT): G^{00} = +(k^2/2)(h_yy+h_zz) exactly (k || x) -- the linearized "
          "Hamiltonian constraint is k^2 x (transverse trace), with every other component absent. In "
          "vacuum at k != 0 it forces that channel to ZERO: the trace is NOT a free 'diagonal bounded "
          "channel with L = (1/2)G qdot^2 - (1/2)V q^2', so the derived gluing law's hypothesis does not "
          "apply to it in the constrained 3+1 system (the channel is eliminated by the constraint, not "
          "glued)",
          sp.simplify(c22 - k ** 2 / 2) == 0 and sp.simplify(c33 - k ** 2 / 2) == 0 and not others,
          f"dG00/dh_yy={c22}, dG00/dh_zz={c33}, all other h-coefficients zero")

    # ---- A7: DOF count (exact ranks at rational points) ----
    M = op_matrix(CONT)
    def kern_dim(wv, kv):
        return 10 - M.subs({w: wv, k: kv}).rank()
    generic = kern_dim(sp.Rational(3, 7), sp.Rational(2, 5))
    onshell = kern_dim(sp.Rational(2, 5), sp.Rational(2, 5))
    check("A7 (DOF COUNT, exact rank algebra): at generic omega^2 != k^2 the kernel of the full 10x10 "
          "operator is EXACTLY the 4-parameter gauge family; at omega^2 = k^2 it is 4+2 -- precisely TWO "
          "propagating physical modes, both TT, healthy dispersion omega^2 = k^2",
          generic == 4 and onshell == 6,
          f"kernel dim: generic (omega=3/7,k=2/5) = {generic} (gauge only); on-shell (omega=k=2/5) = {onshell} (gauge + 2 TT)")

    # ---- A8: discrete transcription (kinetic-isotropy primitive c_t=c_s) ----
    # (i) multiplier structure: A2 is S-formal => holds verbatim (re-assert via the lattice matrix):
    # G^{00} row is omega-INDEPENDENT entirely; G^{0i} rows are ODD in omega (only the S(0,j) ~
    # sin(omega) sin(k_j) mixing terms -- an even 4sin^2(omega/2) kinetic term would violate parity).
    MLat = op_matrix(LATT)
    rowidx = {pp: i for i, pp in enumerate(pairs)}
    g00_free = all(sp.simplify(MLat[rowidx[(0, 0)], j].diff(w)) == 0 for j in range(10))
    no_w2 = True
    for pp in [(0, 1), (0, 2), (0, 3)]:
        for j in range(10):
            e = MLat[rowidx[pp], j]
            even_part = sp.simplify((e + e.subs(w, -w)) / 2)
            # the even-in-omega part must be omega-INDEPENDENT (pure spatial terms are allowed; an
            # even omega-dependence would be a 4sin^2(omega/2) kinetic term -- forbidden by A2)
            if sp.simplify(even_part.diff(w)) != 0:
                no_w2 = False
    # (ii) discrete TT dispersion: 4 sin^2(w/2) = 4 sin^2(k/2)  => omega = +-k exactly in the BZ
    h_tt_v = hvec(h_tt)
    Gtt_lat = MLat * h_tt_v
    yz_idx = rowidx[(2, 3)]
    disp = sp.simplify(Gtt_lat[yz_idx])
    disp_expect = sp.simplify(sp.Rational(1, 2) * ((2 * sp.sin(k / 2)) ** 2 - (2 * sp.sin(w / 2)) ** 2) * 1)
    tt_disp_ok = sp.simplify(disp - disp_expect) == 0
    # (iii) gauge-mode residual at finite k: measure order
    xi_y = sp.Matrix(4, 4, lambda a, b: (p4[a] if b == 2 else 0) + (p4[b] if a == 2 else 0))
    # lattice gauge mode (continuum form transcribed): h = p (x) xi + xi (x) p with xi = e_y
    res = einstein_lin(xi_y).subs(LATT)
    res_norm = sum(sp.expand_trig(sp.simplify(res[a, b])) ** 2 for a in IDX for b in IDX)
    r1 = float(sp.sqrt(res_norm.subs({w: 0.20, k: 0.20})))
    r2 = float(sp.sqrt(res_norm.subs({w: 0.10, k: 0.10})))
    order = (sp.log(sp.Float(r1) / sp.Float(r2)) / sp.log(2)).evalf()
    check("A8 (DISCRETE, kinetic-isotropy primitive c_t=c_s; declared symmetrized stencils): the "
          "multiplier structure holds VERBATIM on the lattice (G^{00} row free of omega entirely; no "
          "4sin^2(omega/2) in any constraint row -- the S-formal theorem); the discrete TT dispersion is "
          "4sin^2(omega/2) = 4sin^2(k/2), i.e. omega = +-k EXACTLY across the BZ (healthy, no extra "
          "branch); the continuum-form gauge mode has a NONZERO lattice residual at finite k (the "
          "measured lattice diffeomorphism-breaking), vanishing as k -> 0 with the reported order",
          no_w2 and g00_free and tt_disp_ok and r1 > 1e-12 and r2 < r1,
          f"G00 row omega-free; TT: G_23 = (4sin^2(k/2)-4sin^2(omega/2))/2; gauge residual "
          f"|G(h_gauge)| = {r1:.3e} at w=k=0.20 vs {r2:.3e} at 0.10 (order ~ 2^{order:.2f} per halving)")

    # ---- A9: tie-in -- the no-go binds the records-Hessian gluing; the geometric operator is healthy ----
    # records-route retained supermetric weights (normal form, b=1): trace=-1, shear=-1 (degenerate)
    om2_tt_rec = sp.simplify(V_yz / sp.Integer(-1))
    om2_tr_rec = sp.simplify(V_trT / sp.Integer(-1))
    prod_rec = sp.simplify(om2_tt_rec * om2_tr_rec).subs(k, 1)
    prod_geo = sp.simplify(om2_tt * om2_tr).subs(k, 1)
    check("A9 (tie-in, both landed rows respected): gluing the DERIVED potentials with the RETAINED "
          "records-route supermetric weights (trace=shear=-1, degenerate) reproduces the no-go's negative "
          "product (one channel unhealthy -- the no-go BINDS that gluing); gluing with the DERIVED "
          "geometric fiber metric gives a positive product (both healthy). The no-go is therefore a "
          "correct boundary on the records-Hessian gluing specifically; the geometric target operator "
          "carries its own healthy non-degenerate gluing.",
          prod_rec < 0 and prod_geo > 0,
          f"records-supermetric gluing: omega^2 product = {prod_rec} < 0 (no-go reproduced); "
          f"derived geometric fiber metric: product = {prod_geo} > 0 (bypass)")

    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    print(
        "VERDICT: the no-go's own named bypass ('a derived non-degenerate fiber metric') EXISTS and is\n"
        "now exhibited: the 3+1 kinetic fiber metric of the linearized EH target operator is the\n"
        "indefinite lambda-one DeWitt form (K_trace:K_TT = -2:+1, derived), the comparator potential\n"
        "signs (V_TT>0, V_trace<0) are derived from the same operator, and the gluing law with both\n"
        "halves derived gives BOTH channels healthy -- while the trace channel is in fact CONSTRAINED\n"
        "(G^{00} = +(k^2/2)(transverse trace): not a free diagonal channel, eliminated not glued), the\n"
        "lapse/shift multiplier structure is scheme-independent (S-formal zero polynomial => holds for\n"
        "ANY stencil, including the symmetric Z^3 x Z_tau with c_t=c_s), the exact DOF count is 2 TT,\n"
        "and the discrete TT dispersion is omega=+-k across the BZ. The degenerate-supermetric no-go\n"
        "remains correct at its stated scope: it binds the RECORDS-route Hessian gluing (reproduced\n"
        "here); the geometric target operator bypasses it. OPEN (unchanged): deriving the geometric\n"
        "action itself from the framework (Einstein/Regge glue, edge-length DOF, action selection),\n"
        "the cubic-Coxeter Regge second variation, nonlinear constraint closure on discrete time.\n"
        "No PDG/fitted value."
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
