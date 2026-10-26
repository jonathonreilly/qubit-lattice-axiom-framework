#!/usr/bin/env python3
"""
check.py  --  J:derive:review-20260929-finite-spin-incompressible-tensor:a1

Own machinery (numpy, scipy, sympy, mpmath, fractions only).  Nothing is imported from
the source branch or from any repository script.  Every finite claim that can be exact
is exact (sympy rationals / Fractions); floating point is used only where a spectrum
is irrational and is labelled "numerical".

What is checked (numbering follows ATTEMPT.md):
  S2   tensor stencil rebuilt from its formula: integer kernel on 3^3 and 4^3 boxes has
       zero zeroth and first moments (re-verification of a landed lemma, not new)
  S3   a +-1 (qubit) kernel move found by MILP; exact G m = 0; exact quadrupole (second
       moment) tensor and its TT components; series link |w(q)|^2 = q^4 |M|^2/4 + ...
  S4   exact operator identity [O^dag,[T,O]] = -|w|^2 T on spin 1/2 and spin 1 slots
  S5   Q-projected (whole ground eigenspace removed) spectral moments: f-sum identity,
       T3-type bound and moment chain on a ring (numerical), and an exact
       degenerate-ground-space example where mean-only subtraction breaks S <= m1/omega
  S6   Born-structure-factor lemma: finite and algebraic examples, exact/high-precision
  S7   spin-1/2 diagonal quadratic forms: exact commutation vs harmonic shift invariance
  S8   harmonic (Gaussian) comparator has chi = 1/U >= 1/(sum |u|)
  S9   the window arithmetic (chi>=kappa q^2, omega_min>=c q  =>  S>=c kappa q^3/2,
       m1>=c^2 kappa q^4/2) on exact rational spectral measures
"""
import itertools
import random
import sys
import time
from fractions import Fraction

import numpy as np
import sympy as sp
from sympy.polys.matrices import DomainMatrix
import mpmath as mp

T0 = time.time()
PASS = 0
FAIL = 0
LINES = []


def check(name, ok, extra=""):
    global PASS, FAIL
    if ok:
        PASS += 1
        print("PASS " + name + (("  [" + extra + "]") if extra else ""))
    else:
        FAIL += 1
        print("FAIL " + name + (("  [" + extra + "]") if extra else ""))
    sys.stdout.flush()


# ----------------------------------------------------------------------------------
# S2 / S3 : tensor stencil, kernel, moments, qubit move
# ----------------------------------------------------------------------------------
EV = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
TYPES = [("d", 0), ("d", 1), ("d", 2), ("f", (0, 1)), ("f", (0, 2)), ("f", (1, 2))]


def vadd(a, b, s=1):
    return tuple(a[k] + s * b[k] for k in range(3))


def face(i, j):
    return ("f", (min(i, j), max(i, j)))


def build_box(n):
    """columns = slots inside an n^3 box; rows = every (j,x) whose stencil touches the box.
    (G p)_j(x) = p_jj(x+e_j) - p_jj(x) + sum_{i!=j} [p_ij(x) - p_ij(x-e_i)]."""
    cols = {}
    for x in itertools.product(range(n), repeat=3):
        for t in TYPES:
            cols[(t, x)] = len(cols)
    rows = {}
    for j in range(3):
        for x in itertools.product(range(-1, n + 1), repeat=3):
            ent = {}

            def put(t, y, v):
                if (t, y) in cols:
                    ent[(t, y)] = ent.get((t, y), 0) + v

            put(("d", j), vadd(x, EV[j]), 1)
            put(("d", j), x, -1)
            for i in range(3):
                if i == j:
                    continue
                put(face(i, j), x, 1)
                put(face(i, j), vadd(x, EV[i], -1), -1)
            if ent:
                rows[(j, x)] = ent
    return cols, rows


def doubled_pos(t, x):
    p = [2 * x[k] for k in range(3)]
    if t[0] == "f":
        i, j = t[1]
        p[i] += 1
        p[j] += 1
    return tuple(p)


def moments_of(vec_by_col, inv):
    """per-type zeroth moments and per-type first moments (doubled coordinates)."""
    z = {t: 0 for t in TYPES}
    f = {(t, l): 0 for t in TYPES for l in range(3)}
    for c, v in vec_by_col.items():
        if v == 0:
            continue
        t, x = inv[c]
        p = doubled_pos(t, x)
        z[t] += v
        for l in range(3):
            f[(t, l)] += v * p[l]
    return z, f


def section_kernel():
    for n in (3, 4):
        cols, rows = build_box(n)
        inv = {v: k for k, v in cols.items()}
        rl = list(rows)
        M = [[0] * len(cols) for _ in rl]
        for r, k in enumerate(rl):
            for c, v in rows[k].items():
                M[r][cols[c]] = int(v)
        dm = DomainMatrix([[sp.QQ(v, 1) for v in row] for row in M], (len(rl), len(cols)), sp.QQ)
        ns = dm.nullspace().to_Matrix()
        bad = 0
        for r in range(ns.rows):
            vec = {c: ns[r, c] for c in range(ns.cols)}
            z, f = moments_of(vec, inv)
            if any(v != 0 for v in z.values()) or any(v != 0 for v in f.values()):
                bad += 1
        check("S2.kernel_moments_box%d" % n, ns.rows > 0 and bad == 0,
              "dim ker=%d, vectors with a nonzero zeroth/first moment=%d" % (ns.rows, bad))


def find_qubit_move(n=4, tl=120.0):
    from scipy.optimize import milp, LinearConstraint, Bounds
    from scipy.sparse import lil_matrix, hstack, identity
    cols, rows = build_box(n)
    m = len(cols)
    A = lil_matrix((len(rows), m))
    for r, k in enumerate(rows):
        for c, v in rows[k].items():
            A[r, cols[c]] = v
    A = A.tocsr()
    Aeq = hstack([A, -A]).tocsr()
    S = hstack([identity(m), identity(m)]).tocsr()
    cons = [LinearConstraint(Aeq, 0, 0), LinearConstraint(S, 0, 1),
            LinearConstraint(np.ones((1, 2 * m)), 1, np.inf)]
    res = milp(np.ones(2 * m), constraints=cons, integrality=np.ones(2 * m),
               bounds=Bounds(0, 1), options={"time_limit": tl, "disp": False})
    inv = {v: k for k, v in cols.items()}
    x = np.round(res.x[:m] - res.x[m:]).astype(int)
    move = {inv[i]: int(x[i]) for i in range(m) if x[i] != 0}
    return move, res.status


def section_move():
    move, status = find_qubit_move()
    supp = len(move)
    check("S3.milp_move_found_support20", status == 0 and supp == 20 and set(move.values()) <= {1, -1},
          "status=%s support=%d (optimal in the 4^3 box)" % (status, supp))
    # exact integer verification G m = 0 on an enlarged lattice (independent of the box rows)
    full = {}
    for (t, x), v in move.items():
        full[(t, x)] = v
    ok = True
    xs = [x for (_, x) in move]
    lo = min(min(c) for c in xs) - 2
    hi = max(max(c) for c in xs) + 2
    for j in range(3):
        for x in itertools.product(range(lo, hi + 1), repeat=3):
            val = full.get((("d", j), vadd(x, EV[j])), 0) - full.get((("d", j), x), 0)
            for i in range(3):
                if i == j:
                    continue
                val += full.get((face(i, j), x), 0) - full.get((face(i, j), vadd(x, EV[i], -1)), 0)
            if val != 0:
                ok = False
    check("S3.move_in_kernel_exact_all_rows", ok, "G m = 0 at every row of an enlarged window")
    # moments, exact
    inv_like = {("k", i): (t, x) for i, ((t, x), v) in enumerate(move.items())}
    vec = {("k", i): v for i, (_, v) in enumerate(move.items())}
    z, f = moments_of(vec, inv_like)
    check("S3.move_zero_zeroth_and_first_moments",
          all(v == 0 for v in z.values()) and all(v == 0 for v in f.values()))
    # quadrupole tensor per slot type, physical positions r = doubled/2
    Q = {t: sp.zeros(3, 3) for t in TYPES}
    for (t, x), v in move.items():
        p = [sp.Rational(c, 2) for c in doubled_pos(t, x)]
        for a in range(3):
            for b in range(3):
                Q[t][a, b] += v * p[a] * p[b]
    # TT amplitudes for q-hat along axis k: M_plus = Q_aa - Q_bb (unnormalised, a,b transverse), M_cross = Q_ab-slot
    amp = {}
    for k in range(3):
        a, b = [i for i in range(3) if i != k]
        mp_ = sum(vv * 0 for vv in [0])
        Mplus = Q[("d", a)][k, k] - Q[("d", b)][k, k]
        Mcross = Q[face(a, b)][k, k]
        amp[k] = (Mplus, Mcross)
    nonzero = any(amp[k][0] != 0 or amp[k][1] != 0 for k in range(3))
    check("S3.move_has_nonzero_TT_quadrupole", nonzero,
          "(M_plus,M_cross) along x,y,z = %s" % ([(str(amp[k][0]), str(amp[k][1])) for k in range(3)],))
    # series link: w(t q-hat) = -(M/2) t^2 + O(t^3) for both TT polarisations along each axis,
    # hence |w|^2 = M^2 t^4 / 4 + O(t^5)
    t = sp.symbols("t", real=True)
    good = True
    for k in range(3):
        a, b = [i for i in range(3) if i != k]
        for pol in ("plus", "cross"):
            w = 0
            for (ty, x), v in move.items():
                p = [sp.Rational(c, 2) for c in doubled_pos(ty, x)]
                if pol == "plus":
                    eps = 1 if ty == ("d", a) else (-1 if ty == ("d", b) else 0)
                else:
                    eps = 1 if ty == face(a, b) else 0
                if eps:
                    w += eps * v * sp.exp(sp.I * t * p[k])
            ser = sp.series(w, t, 0, 3).removeO()
            Mval = amp[k][0] if pol == "plus" else amp[k][1]
            if not (sp.simplify(ser.coeff(t, 0)) == 0 and sp.simplify(ser.coeff(t, 1)) == 0
                    and sp.simplify(ser.coeff(t, 2) + Mval / 2) == 0):
                good = False
    check("S3.series_w_equals_minus_M_over_2_t2", good,
          "w(t q-hat)= -(M/2) t^2 + O(t^3), exact, three axes x two TT polarisations")
    # explicit window constant for H = -J sum (T + T^dag) over translates of this one move:
    # K(q) <= 2 J |w|^2 = (J M^2 / 2) q^4  =>  kappa c^2 <= J M^2 (axis x, cross polarisation)
    Mx = amp[0][1]
    check("S3.single_move_window_constant", Mx != 0 and Mx ** 2 == 4,
          "for H=-J sum(T+T^dag), q along x, cross polarisation: M=%s, so kappa c^2 <= J M^2 = %s J (this move family only)" % (Mx, Mx ** 2))
    return move, amp


# ----------------------------------------------------------------------------------
# S4 : exact operator identity
# ----------------------------------------------------------------------------------
def shift_op(dims, m, fval):
    """T = sum_E fval(E) |E+m><E| over allowed E (E_s in {-d_s..d_s} integer steps; half-integers allowed)."""
    # dims: list of lists of allowed E values per site
    states = list(itertools.product(*dims))
    index = {s: i for i, s in enumerate(states)}
    N = len(states)
    T = sp.zeros(N, N)
    for s in states:
        s2 = tuple(s[k] + m[k] for k in range(len(m)))
        if s2 in index:
            T[index[s2], index[s]] = fval(s)
    return states, T


def section_identity():
    rnd = random.Random(7)
    for label, vals, m in [("spin1/2", [sp.Rational(-1, 2), sp.Rational(1, 2)], (1, -1, -1)),
                           ("spin1", [-1, 0, 1], (1, -1, 0))]:
        dims = [vals] * 3
        coef = {}

        def fval(s, coef=coef):
            if s not in coef:
                coef[s] = sp.Rational(rnd.randint(-5, 5), rnd.randint(1, 4)) + sp.I * sp.Rational(rnd.randint(-5, 5), rnd.randint(1, 4))
            return coef[s]

        states, T = shift_op(dims, m, fval)
        fs = [sp.Rational(rnd.randint(-4, 4), rnd.randint(1, 3)) + sp.I * sp.Rational(rnd.randint(-4, 4), rnd.randint(1, 3)) for _ in range(3)]
        N = len(states)
        O = sp.zeros(N, N)
        for i, s in enumerate(states):
            O[i, i] = sum(fs[k] * s[k] for k in range(3))
        Od = O.H
        lhs = Od * (T * O - O * T) - (T * O - O * T) * Od
        w = sum(fs[k] * m[k] for k in range(3))
        rhs = -(w * sp.conjugate(w)) * T
        d = sp.simplify(lhs - rhs)
        check("S4.double_commutator_identity_%s" % label, d == sp.zeros(N, N),
              "[O^dag,[T,O]] = -|w|^2 T exactly, |w|^2=%s, E-dependent complex prefactor" % sp.simplify(w * sp.conjugate(w)))


# ----------------------------------------------------------------------------------
# S5 : whole-ground-eigenspace moments
# ----------------------------------------------------------------------------------
def ring_model(L, J, V, W):
    states = [s for s in range(1 << L) if bin(s).count("1") == L // 2]
    idx = {s: i for i, s in enumerate(states)}
    N = len(states)
    H = np.zeros((N, N))
    Ez = np.zeros((N, L))
    for s in states:
        i = idx[s]
        for x in range(L):
            Ez[i, x] = 0.5 if (s >> x) & 1 else -0.5
        # diagonal
        H[i, i] += V * sum(Ez[i, x] * Ez[i, (x + 1) % L] for x in range(L)) + W * sum(Ez[i, x] * Ez[i, (x + 2) % L] for x in range(L))
        for x in range(L):
            xs = [(x + k) % L for k in range(4)]
            pat = [(s >> p) & 1 for p in xs]
            if pat == [0, 1, 1, 0]:
                t = s
                for p, b in zip(xs, [1, 0, 0, 1]):
                    t = (t & ~(1 << p)) | (b << p)
                H[idx[t], i] += -J
                H[i, idx[t]] += -J
    return states, H, Ez


def section_ring():
    L = 8
    J, V, W = 1.0, 0.45, -0.2
    states, H, Ez = ring_model(L, J, V, W)
    w_, U = np.linalg.eigh(H)
    E0 = w_[0]
    p0 = np.where(w_ - E0 < 1e-9)[0]
    check("S5.ring_ground_space_found", len(p0) >= 1, "dim of ground eigenspace in sector = %d, gap=%.4f" % (len(p0), w_[len(p0)] - E0))
    psi0 = U[:, p0[0]]
    Q = np.array([i for i in range(len(w_)) if i not in set(p0)])
    mhat = lambda q: abs(1 - np.exp(1j * q) - np.exp(2j * q) + np.exp(3j * q))
    allok_f = True
    allok_T3 = True
    allok_chain = True
    rows = []
    for n in range(1, L // 2 + 1):
        q = 2 * np.pi * n / L
        O = np.diag(sum(np.exp(1j * q * x) * Ez[:, x] for x in range(L)) / np.sqrt(L))
        Od = O.conj().T
        comm = lambda A, B: A @ B - B @ A
        K = np.vdot(psi0, comm(Od, comm(H, O)) @ psi0).real
        # moments with the whole ground eigenspace removed
        amp = U.conj().T @ (O @ psi0)
        ampd = U.conj().T @ (Od @ psi0)
        om = w_ - E0
        m_ = lambda a, j: float(np.sum(om[Q] ** j * np.abs(a[Q]) ** 2))
        m1, m1d = m_(amp, 1), m_(ampd, 1)
        m0, mm1 = m_(amp, 0), m_(amp, -1)
        if abs(K - (m1 + m1d)) > 1e-9:
            allok_f = False
        if K > 2 * J * mhat(q) ** 2 + 1e-9 or m1 > 2 * J * mhat(q) ** 2 + 1e-9:
            allok_T3 = False
        if m0 > 1e-12:
            wts = np.abs(amp[Q]) ** 2
            omega_min = float(np.min(om[Q][wts > 1e-14]))
            tol = 1e-9
            if not (omega_min <= m0 / mm1 + tol and m0 / mm1 <= np.sqrt(m1 / mm1) + tol and np.sqrt(m1 / mm1) <= m1 / m0 + tol):
                allok_chain = False
            rows.append((n, q, m0, 2 * mm1, omega_min))
    check("S5.ring_fsum_identity_Q_projected", allok_f, "<[O^dag,[H,O]]> = m1(O)+m1(O^dag) with the whole ground eigenspace removed (numerical)")
    check("S5.ring_T3_bound_exact_finite_q", allok_T3, "K(q) <= 2 J |m_hat(q)|^2 at all ring momenta (numerical)")
    check("S5.ring_moment_chain_Q_projected", allok_chain and len(rows) > 0, "omega_min <= m0/m_-1 <= sqrt(m1/m_-1) <= m1/m0 (numerical)")

    # exact degenerate-ground-space example, rational arithmetic:  block sites 0..3 move, sites 4,5 spectators
    vals = [sp.Rational(-1, 2), sp.Rational(1, 2)]
    sts = list(itertools.product(vals, repeat=6))
    idx = {s: i for i, s in enumerate(sts)}
    NN = len(sts)
    Tm = sp.zeros(NN, NN)
    m = (1, -1, -1, 1, 0, 0)
    for s in sts:
        s2 = tuple(s[k] + m[k] for k in range(6))
        if s2 in idx:
            Tm[idx[s2], idx[s]] = 1
    Hm = -(Tm + Tm.T)
    # ground eigenspace: psi_+ (x) any spectator config, energy -1, 4-fold
    a = sts.index((sp.Rational(-1, 2), sp.Rational(1, 2), sp.Rational(1, 2), sp.Rational(-1, 2), vals[0], vals[0]))
    # build exactly
    gs = []
    for e4 in vals:
        for e5 in vals:
            A_ = idx[(sp.Rational(-1, 2), sp.Rational(1, 2), sp.Rational(1, 2), sp.Rational(-1, 2), e4, e5)]
            B_ = idx[(sp.Rational(1, 2), sp.Rational(-1, 2), sp.Rational(-1, 2), sp.Rational(1, 2), e4, e5)]
            v = sp.zeros(NN, 1)
            v[A_] = 1
            v[B_] = 1
            gs.append(v / sp.sqrt(2))
    eig_ok = all(sp.simplify(Hm * v + v) == sp.zeros(NN, 1) for v in gs)
    # is -1 the lowest eigenvalue with exactly this multiplicity?
    ev = Hm.eigenvals()
    low = min(ev.keys())
    check("S5.exact_degenerate_ground_space", eig_ok and low == -1 and ev[low] == 4,
          "ground energy -1 with multiplicity 4 (block ground state x 4 spectator configs), exact")
    # state |0> = psi_+ (x) uniform over spectators (a cat across the degenerate manifold)
    psi = sum(gs, sp.zeros(NN, 1)) / 2
    f = [sp.Rational(1, 3), sp.Rational(-2, 5), sp.Rational(1, 7), sp.Rational(3, 4), sp.Rational(5, 6), sp.Rational(-1, 2)]
    O = sp.diag(*[sum(f[k] * s[k] for k in range(6)) for s in sts])
    Op = O * psi
    P0 = sp.zeros(NN, NN)
    for v in gs:
        P0 += v * v.T
    mean = (psi.T * Op)[0]
    Sfull = (Op.T * Op)[0]
    Sel = (Op.T * P0 * Op)[0]
    Smean = Sfull - mean ** 2           # "mean-only" structure factor
    SQ = Sfull - Sel                    # whole ground eigenspace removed
    # inelastic spectral data: only the block excited state at energy +1 (gap 2) is reachable
    m1 = sp.Integer(0)
    # m1 = sum (E_n-E_0)|<n|O|0>|^2 via the commutator formula (exact)
    Hc = Hm
    com = lambda A_, B_: A_ * B_ - B_ * A_
    K = (psi.T * com(O, com(Hc, O)) * psi)[0]   # O real so O^dag = O
    m1 = K / 2                                   # m1(O) = m1(O^dag) for real diagonal O
    gap = 2
    check("S5.exact_Q_weight_is_what_the_fsum_sees", sp.simplify(m1 - gap * SQ) == 0,
          "m1 = gap * S_Q (single level, gap 2): S_Q=%s, m1=%s" % (SQ, sp.nsimplify(m1)))
    check("S5.exact_mean_only_breaks_S_le_m1_over_omega", Smean > m1 / gap and Sel > mean ** 2,
          "S_mean-only=%s > m1/omega_min=%s ; elastic weight=%s > mean^2=%s ; Q-version S_Q=%s = m1/omega_min"
          % (Smean, m1 / gap, Sel, mean ** 2, SQ))


# ----------------------------------------------------------------------------------
# S6 : Born structure-factor lemma
# ----------------------------------------------------------------------------------
def section_born():
    q = sp.symbols("q", positive=True)
    # finite-support symmetric correlation with vanishing 0th and 2nd cosine moments: fourth difference
    c = {0: 6, 1: -4, 2: 1}   # c(-r)=c(r); sum over Z: 6 - 8 + 2 = 0 ; sum c r^2 = -8 + 8 = 0
    S = sum((c[r] if r == 0 else 2 * c[r] * sp.cos(r * q)) for r in c)
    ser = sp.series(S, q, 0, 6).removeO()
    sumc = sum(c[0:1] if False else [c[0]]) + 2 * (c[1] + c[2])
    sum2 = 2 * (c[1] * 1 + c[2] * 4)
    check("S6.finite_support_zero_moments_gives_q4",
          sumc == 0 and sum2 == 0 and sp.simplify(ser.coeff(q, 3)) == 0 and sp.simplify(ser.coeff(q, 2)) == 0
          and sp.simplify(ser.coeff(q, 4)) == 1,
          "S(q)=16 sin^4(q/2): q^2 and q^3 coefficients vanish, q^4 coefficient=%s" % sp.simplify(ser.coeff(q, 4)))
    mp.mp.dps = 40
    # algebraic tail c(r)=r^-4: closed form (Bernoulli polynomial B4) for 0<=q<=2pi
    maxerr = mp.mpf(0)
    for qq in [mp.mpf(1) / 10, mp.mpf(1) / 3, mp.mpf(1), mp.mpf(2), mp.mpf(3)]:
        series = mp.nsum(lambda r: mp.cos(qq * r) / r ** 4, [1, mp.inf])
        closed = mp.pi ** 4 / 90 - mp.pi ** 2 * qq ** 2 / 12 + mp.pi * qq ** 3 / 12 - qq ** 4 / 48
        maxerr = max(maxerr, abs(series - closed))
    check("S6.algebraic_tail_r^-4_has_odd_cubic_term", maxerr < mp.mpf(10) ** -25,
          "sum_{r>=1} cos(qr)/r^4 = pi^4/90 - pi^2 q^2/12 + pi q^3/12 - q^4/48 on [0,2pi] (|err|<1e-25)")
    # build a distribution realising S ~ (pi/6) q^3 : c(r)=r^-4 (r!=0), c(+-1) += b, c(0) = -pi^4/45 - 2b, b=-pi^2/6
    b = -mp.pi ** 2 / 6
    def Salg(qq):
        core = 2 * (mp.pi ** 4 / 90 - mp.pi ** 2 * qq ** 2 / 12 + mp.pi * qq ** 3 / 12 - qq ** 4 / 48)
        return core + (-mp.pi ** 4 / 45 - 2 * b) + 2 * b * mp.cos(qq)
    ratios = [Salg(mp.mpf(10) ** -k) / mp.mpf(10) ** (-3 * k) for k in (1, 2, 3, 4)]
    check("S6.algebraic_tail_realises_S_sim_q3_with_divergent_third_moment",
          abs(ratios[-1] - mp.pi / 6) < mp.mpf(10) ** -3 and abs(ratios[-1] - ratios[-2]) < mp.mpf(10) ** -3,
          "S(q)/q^3 -> pi/6 = %s ; partial sums of sum |r|^3 |c(r)| grow like log R (checked below)" % mp.nstr(ratios[-1], 8))
    ps = [sum(mp.mpf(r) ** 3 * mp.mpf(r) ** -4 for r in range(1, R)) for R in (10, 100, 1000, 10000)]
    check("S6.third_moment_of_algebraic_tail_diverges", ps[3] - ps[2] > mp.mpf(2) and ps[2] - ps[1] > mp.mpf(2),
          "partial sums %s" % [mp.nstr(p, 6) for p in ps])
    # exponentially decaying c: S(q)/q^3 -> 0 once S(0)=0 and S''(0)=0 are imposed
    # c(r) = e^{-|r|} a_r with a chosen so that sum c = 0 and sum c r^2 = 0 using three free values
    r_vals = list(range(-60, 61))
    base = {r: mp.e ** (-abs(r)) for r in r_vals}
    # corrections on r=0,1,2: solve for (d0,d1,d2) with c(+-r) += d_r
    A = mp.matrix([[1, 2, 2], [0, 2, 8], [0, 0, 0]])
    s0 = sum(base.values())
    s2 = sum(base[r] * r * r for r in r_vals)
    # unknowns d0,d1,d2 : s0 + d0 + 2 d1 + 2 d2 = 0 ; s2 + 2 d1 + 8 d2 = 0 ; choose d2 = 0 -> d1 = -s2/2, d0 = -s0 - 2 d1
    d2 = mp.mpf(0)
    d1 = -s2 / 2
    d0 = -s0 - 2 * d1
    cc = dict(base)
    cc[0] += d0
    cc[1] += d1
    cc[-1] += d1
    def Sexp(qq):
        return sum(cc[r] * mp.cos(qq * r) for r in r_vals)
    rr = [Sexp(mp.mpf(10) ** -k) / mp.mpf(10) ** (-3 * k) for k in (1, 2, 3)]
    check("S6.short_range_with_S0_and_S2_removed_is_o_q3", abs(rr[2]) < abs(rr[0]) / 50 and abs(rr[2]) < mp.mpf(10) ** -1,
          "S(q)/q^3 at q=0.1,0.01,0.001: %s" % [mp.nstr(x, 5) for x in rr])


# ----------------------------------------------------------------------------------
# S7 : spin-1/2 quadratic forms: exact commutation vs harmonic shift invariance
# ----------------------------------------------------------------------------------
def section_quadratic():
    nS = 6
    m = [1, -1, -1, 1, 0, 0]
    supp = [0, 1, 2, 3]
    pairs = [(s, t) for s in range(nS) for t in range(s + 1, nS)]
    a = sp.symbols("a0:%d" % len(pairs))
    d = sp.symbols("d0:%d" % nS)
    # exact commutation of Q = sum a_st E_s E_t with the product-flip T_m on spin-1/2 slots
    eqs = []
    for e4 in (sp.Rational(-1, 2), sp.Rational(1, 2)):
        for e5 in (sp.Rational(-1, 2), sp.Rational(1, 2)):
            Ea = [sp.Rational(-1, 2), sp.Rational(1, 2), sp.Rational(1, 2), sp.Rational(-1, 2), e4, e5]
            Eb = [Ea[k] + m[k] for k in range(nS)]
            Qa = sum(a[i] * Ea[s] * Ea[t] for i, (s, t) in enumerate(pairs))
            Qb = sum(a[i] * Eb[s] * Eb[t] for i, (s, t) in enumerate(pairs))
            eqs.append(sp.expand(Qa - Qb))
    # exact space of commuting a's
    Mx = sp.Matrix([[sp.diff(e, ai) for ai in a] for e in eqs])
    exact_dim = len(a) - Mx.rank()
    # harmonic shift invariance X m = 0 with X symmetric, off-diagonals a_st/2, diagonal d_s free
    X = sp.zeros(nS, nS)
    for i, (s, t) in enumerate(pairs):
        X[s, t] = X[t, s] = a[i] / 2
    for s in range(nS):
        X[s, s] = d[s]
    hm = X * sp.Matrix(m)
    unk = list(a) + list(d)
    Hm_ = sp.Matrix([[sp.diff(e, u) for u in unk] for e in hm])
    harm_total = len(unk) - Hm_.rank()
    # projection of the harmonic solution space onto the cross-term variables a
    ns = Hm_.nullspace()
    proj = sp.Matrix([[v[i] for i in range(len(a))] for v in ns])
    harm_proj_dim = proj.rank()
    # harmonic invariance with the diagonal removed (d=0), i.e. what survives if the squares are dropped
    Hm0 = sp.Matrix([[sp.diff(e, ai) for ai in a] for e in hm.subs({dd: 0 for dd in d})])
    harm_nodiag = len(a) - Hm0.rank()
    check("S7.exact_commutation_space_equals_projected_harmonic_space", exact_dim == harm_proj_dim and exact_dim > harm_nodiag,
          "dim{cross terms commuting with T_m}=%d ; dim of their projection from {X m=0, diagonal free}=%d ; dim{X m=0, diagonal=0}=%d"
          % (exact_dim, harm_proj_dim, harm_nodiag))
    # which cross terms are forced to vanish? exactly those joining an outside slot to the support with nonzero m-weight
    off = []
    for t_ in (4, 5):
        row = sum(a[pairs.index((min(s, t_), max(s, t_)))] * m[s] for s in supp)
        off.append(row)
    ns_exact = Mx.nullspace()
    cond_ok = True
    for v in ns_exact:
        sub = {a[i]: v[i] for i in range(len(a))}
        if any(sp.simplify(o.subs(sub)) != 0 for o in off):
            cond_ok = False
    check("S7.exact_commutation_iff_outside_rows_annihilate_m", cond_ok and (len(a) - Mx.rank()) == len(a) - sp.Matrix([[sp.diff(o, ai) for ai in a] for o in off]).rank(),
          "commuting cross terms = {sum_{s in supp} a_st m_s = 0 for every outside slot t}; support-row harmonic equations impose nothing")
    # linear Gauss grading for contrast: G = sum g_s E_s commutes with T_m iff g.m = 0 (one linear condition)
    g = sp.symbols("g0:6")
    check("S7.linear_gauss_condition_is_g_dot_m", sp.expand(sum(g[k] * m[k] for k in range(6)) - (g[0] - g[1] - g[2] + g[3])) == 0,
          "[G,T_m] = (g.m) T_m : a linear grading, not a polynomial shift invariance")


# ----------------------------------------------------------------------------------
# S8 : harmonic comparators cannot be incompressible
# ----------------------------------------------------------------------------------
def section_harmonic():
    Uu, K, hbar = sp.symbols("U K hbar", positive=True)
    # H = U E^2/2 + K th^2/2, [E,th] = i : E^2 expectation in the ground state, omega = sqrt(UK)
    omega = sp.sqrt(Uu * K)
    E2 = sp.sqrt(K / Uu) / 2          # <E^2> = (1/2) sqrt(K/U)
    m0 = E2
    mm1 = m0 / omega                  # single level
    chi = sp.simplify(2 * mm1)
    check("S8.oscillator_chi_equals_1_over_U", sp.simplify(chi - 1 / Uu) == 0, "chi = 2 m_-1 = 1/U independent of K")
    # lattice quadratic form: eigenvalues of a finite-range symmetric U(q) are bounded by sum |u|
    rnd = np.random.default_rng(3)
    ok = True
    for _ in range(200):
        nsl = 6
        R = 2
        u = rnd.normal(size=(2 * R + 1, nsl, nsl))
        u = (u + u.transpose(0, 2, 1)) / 2
        # make it Hermitian-symmetric in displacement: u(-d) = u(d)^T
        for d in range(1, R + 1):
            u[R - d] = u[R + d].T
        q = rnd.uniform(-np.pi, np.pi)
        Uq = sum(u[R + d] * np.exp(1j * q * d) for d in range(-R, R + 1))
        lam = np.max(np.linalg.eigvalsh((Uq + Uq.conj().T) / 2))
        bound = np.max(np.sum(np.abs(u), axis=0).sum(axis=1)) * 1.0
        # Gershgorin / row-sum bound: ||U(q)|| <= max_row sum_d,t |u_{st}(d)|
        if lam > bound + 1e-9:
            ok = False
    check("S8.local_quadratic_form_norm_bounded_by_row_sum", ok, "so chi_harmonic >= 1/row-sum > 0 as q->0 for every local quadratic electric energy (numerical, 200 random stencils)")


# ----------------------------------------------------------------------------------
# S9 : window arithmetic on exact rational spectral measures
# ----------------------------------------------------------------------------------
def section_window():
    rnd = random.Random(11)
    bad = 0
    tested = 0
    for _ in range(2000):
        n = rnd.randint(1, 6)
        om = [Fraction(rnd.randint(1, 40), rnd.randint(1, 8)) for _ in range(n)]
        w = [Fraction(rnd.randint(1, 20), rnd.randint(1, 9)) for _ in range(n)]
        omin = min(om)
        m0 = sum(w)
        mm1 = sum(wi / oi for wi, oi in zip(w, om))
        m1 = sum(wi * oi for wi, oi in zip(w, om))
        chi = 2 * mm1
        # c and kappa realised by the measure itself at one wavenumber (q=1): any c<=omin, kappa<=chi
        c, kappa = omin, chi
        tested += 1
        if not (m0 >= c * kappa / 2 and m1 >= c * c * kappa / 2 and m0 <= m1 / omin and chi <= 2 * m0 / omin):
            bad += 1
    check("S9.window_implications_exact_rational", bad == 0 and tested == 2000,
          "S >= c kappa/2, m1 >= c^2 kappa/2, S <= m1/omega_min, chi <= 2S/omega_min on 2000 exact random measures")
    # the window is non-empty: one mode omega = c q, weight w = kappa c q^3 / 2
    q, c, kap, C = sp.symbols("q c kappa C", positive=True)
    omg = c * q
    w = kap * c * q ** 3 / 2
    chi = sp.simplify(2 * w / omg)
    m1 = sp.simplify(w * omg)
    S = w
    ok = sp.simplify(chi - kap * q ** 2) == 0 and sp.simplify(m1 - kap * c ** 2 * q ** 4 / 2) == 0 \
        and sp.simplify(S - kap * c * q ** 3 / 2) == 0
    check("S9.single_mode_realises_the_window_at_the_sum_rule_saturation", ok,
          "chi=kappa q^2, S=kappa c q^3/2, m1=kappa c^2 q^4/2 <= C q^4 iff kappa c^2 <= 2C : consistent, nothing excluded at moment level")


def main():
    section_kernel()
    section_move()
    section_identity()
    section_ring()
    section_born()
    section_quadratic()
    section_harmonic()
    section_window()
    print("INFO runtime %.1fs" % (time.time() - T0))
    if FAIL == 0:
        print("HIT: scoped, conditional, same-family result -- necessary conditions (S_in = Theta(|q|^3) so non-analytic algebraic Born correlations; kappa c^2 <= 2 C_H; kinetic-quadrupole lower bound) for any finite-spin exact-rule state with chi_in = Omega(q^2) and a linear lowest weighted mode, plus an exact example that mean-only ground-space subtraction breaks the S <= m1/omega_min bound; no such state is built.")
    print("TOTAL: PASS=%d FAIL=%d" % (PASS, FAIL))
    print("SUMMARY: PARTIAL -- no state is built; checked here (proofs in ATTEMPT.md): in the exact-rule finite-spin class, chi_in >= kappa q^2 with a lowest weighted mode omega_min >= c q outside the WHOLE ground eigenspace forces S_in = Theta(|q|^3), kappa c^2 <= 2 C_H and a sign-definite local kinetic-quadrupole sum, hence non-summable cubic Born correlations; harmonic (chi >= const), flat and short-range candidates fail, and mean-only ground-state subtraction exactly breaks S <= m1/omega_min.")
    sys.exit(0 if FAIL == 0 else 1)


if __name__ == "__main__":
    main()
