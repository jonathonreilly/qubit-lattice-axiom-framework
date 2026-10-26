#!/usr/bin/env python3
"""check.py for J:derive:review-20260929-wall-horizon-and-entropy-checks:a1

Obligation chosen: the exact thermal structure of the half-filled hopping-chain vacuum on a
wedge, with respect to nearest-neighbour ("clocked walker") Hamiltonians.  This is the test-A
setting of wall T75 (toe-walls-20260929 attacks/kills T75): vacuum
    C_ij = sin(pi (i-j)/2) / (pi (i-j)),  C_ii = 1/2,
wedge = sites 1..infinity (or 1..N), clocked hopping H = -sum_j h_j (c_j^+ c_{j+1} + h.c.).

Machinery here is disjoint from the sources' scripts: exact Fractions/sympy commutation
algebra, Meixner-Pollaczek orthogonal polynomials with mpmath quadrature, exact rational
null spaces, and a determinantal-process enumeration.  No eigen-fit of beta is used anywhere.

Each check prints one PASS/FAIL line.  Run:  python3 check.py
"""
import sys
import time
from fractions import Fraction
from itertools import product

import numpy as np
import sympy as sp
import mpmath as mp

T0 = time.time()
RESULTS = []


def report(name, ok, detail=""):
    RESULTS.append(bool(ok))
    print(("PASS " if ok else "FAIL ") + name + (" :: " + detail if detail else ""))


# ----------------------------------------------------------------------------------------
# exact building blocks
# ----------------------------------------------------------------------------------------
def sigma(d):
    """sigma(d) = sin(pi d/2)/d for d != 0, sigma(0)=0 (so C = 1/2 + S/pi, S_ij = sigma(i-j))."""
    d = int(d)
    if d == 0 or d % 2 == 0:
        return Fraction(0)
    m = (abs(d) - 1) // 2
    sgn = -1 if m % 2 else 1
    val = Fraction(sgn, abs(d))
    return val if d > 0 else val  # sigma is even: sin(-x)/(-d) = sin(x)/d


def S_matrix(N):
    return [[sigma(i - j) for j in range(1, N + 1)] for i in range(1, N + 1)]


def tri_matrix(N, hop, diag=None):
    """symmetric tridiagonal, hop(j) joins sites j and j+1 (1-indexed), j=1..N-1."""
    M = [[Fraction(0)] * N for _ in range(N)]
    for j in range(1, N):
        M[j - 1][j] = hop(j)
        M[j][j - 1] = hop(j)
    if diag is not None:
        for j in range(1, N + 1):
            M[j - 1][j - 1] = diag(j)
    return M


def matmul(A, B):
    n = len(A)
    return [[sum(A[i][k] * B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]


def comm(A, B):
    AB, BA = matmul(A, B), matmul(B, A)
    return [[AB[i][j] - BA[i][j] for j in range(len(A))] for i in range(len(A))]


def is_zero(M):
    return all(x == 0 for row in M for x in row)


def local_comm_entry(i, k, h):
    """[S, H]_{ik} for zero-diagonal tridiagonal H with hops h(j) (h(0)=0), half-line S."""
    def hh(j):
        return Fraction(0) if j < 1 else h(j)
    return (sigma(i - k + 1) * hh(k - 1) + sigma(i - k - 1) * hh(k)
            - hh(i - 1) * sigma(i - 1 - k) - hh(i) * sigma(i + 1 - k))


# ----------------------------------------------------------------------------------------
# 1. exact commuting tridiagonal operators (Slepian / Gruenbaum at half filling)
# ----------------------------------------------------------------------------------------
def check_finite_commutation():
    bad = []
    for N in range(2, 41):
        S = S_matrix(N)
        T = tri_matrix(N, lambda j, N=N: Fraction(j * (N - j), 2))
        if not is_zero(comm(S, T)):
            bad.append(N)
    report("1a exact [S_N,T_N]=0 with T_N hops j(N-j)/2, zero diagonal, N=2..40 (Fractions)",
           not bad, "bad N: %s" % bad)


def check_halfline_commutation():
    K = 80
    # the local formula must reproduce a literal matrix product on a padded window
    Npad = 30
    S = S_matrix(Npad)
    H = tri_matrix(Npad, lambda j: Fraction(j))
    Cm = comm(S, H)
    agree = all(Cm[i - 1][k - 1] == local_comm_entry(i, k, lambda j: Fraction(j))
                for i in range(1, Npad - 1) for k in range(1, Npad - 1))
    report("1b local commutator formula equals literal matrix product (window interior, N=30)", agree)
    bad = [(i, k) for i in range(1, K + 1) for k in range(1, K + 1)
           if local_comm_entry(i, k, lambda j: Fraction(j)) != 0]
    report("1c exact [S,J]=0 entrywise on the half-line for h_j=j, all i,k<=80 (Fractions)",
           not bad, "first bad %s" % (bad[:3],))
    # symbolic proof of the identity: entry = -(d+1)(d-1)... collapses by sin(a+pi/2)+sin(a-pi/2)=0
    d = sp.symbols('d', integer=True)
    expr = sp.sin(sp.pi * (d + 1) / 2) + sp.sin(sp.pi * (d - 1) / 2)
    report("1d sympy: (d+1)sigma(d+1)+(d-1)sigma(d-1) = sin(pi(d+1)/2)+sin(pi(d-1)/2) = 0 for all integer d",
           sp.simplify(sp.expand_trig(expr)) == 0 and all(
               sp.simplify(expr.subs(d, v)) == 0 for v in range(-12, 13)))


# ----------------------------------------------------------------------------------------
# 2. uniqueness among nearest-neighbour Hamiltonians
# ----------------------------------------------------------------------------------------
def nullspace_dim_finite(N):
    """dimension of {tridiagonal symmetric H (diag + hops) on N sites : [S_N,H]=0}, exact."""
    nh = N - 1
    nd = N
    unknowns = nh + nd
    S = S_matrix(N)
    rows = []
    # build linear map H -> [S,H] by basis matrices
    basis = []
    for j in range(1, N):
        B = [[Fraction(0)] * N for _ in range(N)]
        B[j - 1][j] = Fraction(1)
        B[j][j - 1] = Fraction(1)
        basis.append(B)
    for j in range(1, N + 1):
        B = [[Fraction(0)] * N for _ in range(N)]
        B[j - 1][j - 1] = Fraction(1)
        basis.append(B)
    cols = []
    for B in basis:
        Cm = comm(S, B)
        cols.append([Cm[i][j] for i in range(N) for j in range(N)])
    M = sp.Matrix([[cols[c][r] for c in range(unknowns)] for r in range(N * N)])
    ns = M.nullspace()
    return len(ns), ns


def check_uniqueness_finite():
    ok = True
    dets = []
    for N in range(3, 11):
        dim, ns = nullspace_dim_finite(N)
        ok = ok and dim == 2
        dets.append((N, dim))
    report("2a exact: tridiagonal H with [S_N,H]=0 form a 2-dim space {alpha T_N + gamma I}, N=3..10",
           ok, str(dets))
    # that the 2 dim space is spanned by T_N and I
    N = 8
    dim, ns = nullspace_dim_finite(N)
    T = [Fraction(j * (N - j), 2) for j in range(1, N)]
    span_ok = False
    # solve for coefficients: each null vector v = a*T_hops + g*I_diag
    vecs = [list(v) for v in ns]
    Tvec = sp.Matrix(T + [0] * N)
    Ivec = sp.Matrix([0] * (N - 1) + [1] * N)
    A = sp.Matrix.hstack(*[sp.Matrix(v) for v in vecs])
    span_ok = sp.Matrix.hstack(A, Tvec, Ivec).rank() == 2
    report("2b exact: that null space is span{T_N, I} (N=8)", span_ok)


def check_uniqueness_halfline():
    # (i) J (h_j=j) and Q (h_j=j(j-1)/2) both satisfy every local commutation equation
    Kc = 80
    bad = [(i, k) for i in range(1, Kc + 1) for k in range(1, Kc + 1)
           if local_comm_entry(i, k, lambda j: Fraction(j * (j - 1), 2)) != 0]
    report("2c exact: the quadratic hop sequence Q_j=j(j-1)/2 also satisfies [S,Q]=0 entrywise (i,k<=80)", not bad)
    # (ii) recurrences from rows i=1 (k odd) and i=2 (k even) with symbolic hops
    ok = True
    for k in range(3, 41):
        hk1, hk, h1, h2 = sp.symbols('hk1 hk h1 h2')
        if k % 2 == 1:
            e = (sp.Rational(sigma(1 - k + 1)) * hk1 + sp.Rational(sigma(1 - k - 1)) * hk
                 - 0 - h1 * sp.Rational(sigma(1 + 1 - k)))
            target = sp.Rational(k, k - 2) * (hk1 - h1)
        else:
            if k < 4:
                continue
            e = (sp.Rational(sigma(2 - k + 1)) * hk1 + sp.Rational(sigma(2 - k - 1)) * hk
                 - h1 * sp.Rational(sigma(2 - 1 - k)) - h2 * sp.Rational(sigma(2 + 1 - k)))
            target = h1 + sp.Rational(k - 1, k - 3) * (hk1 - h2)
        sol = sp.solve(e, hk)
        ok = ok and len(sol) == 1 and sp.simplify(sol[0] - target) == 0
    report("2d exact: local equations (1,k) k odd and (2,k) k even give h_k=k/(k-2)(h_{k-1}-h_1) resp. h_1+(k-1)/(k-3)(h_{k-1}-h_2) (k<=40): h_1,h_2 determine all hops, so the solution space is exactly span{J,Q}",
           ok)
    # (iii) cross-check by exact null space of the truncated system, rows i<=3, k<=36
    K = 36
    hs = sp.symbols('h1:%d' % (K + 1))

    def hh(j):
        return sp.Integer(0) if j < 1 else hs[j - 1]

    eqs = []
    for i in range(1, 4):
        for k in range(i, K + 1):
            e = (sp.Rational(sigma(i - k + 1)) * hh(k - 1) + sp.Rational(sigma(i - k - 1)) * hh(k)
                 - hh(i - 1) * sp.Rational(sigma(i - 1 - k)) - hh(i) * sp.Rational(sigma(i + 1 - k)))
            if e != 0:
                eqs.append(e)
    M, _ = sp.linear_eq_to_matrix(eqs, list(hs))
    ns = M.nullspace()
    Jv = sp.Matrix([j for j in range(1, K + 1)])
    Qv = sp.Matrix([sp.Rational(j * (j - 1), 2) for j in range(1, K + 1)])
    A = sp.Matrix.hstack(*ns)
    inspan = sp.Matrix.hstack(A, Jv, Qv).rank() == 2
    report("2e exact null space of rows i<=3, k<=36 (36 unknown hops) is 2-dim and equals span{J,Q}",
           len(ns) == 2 and inspan, "dim=%d" % len(ns))
    # Carleman: sum 1/j diverges (J essentially self-adjoint), sum 1/(j(j-1)/2) converges (not covered)
    n = sp.symbols('n', integer=True, positive=True)
    div = sp.summation(1 / n, (n, 1, sp.oo)) == sp.oo
    conv = sp.summation(2 / (n * (n + 1)), (n, 1, sp.oo)) == 2
    report("2f Carleman test: sum 1/j = oo (J is a limit-point Jacobi operator); the quadratic member has sum 1/h_j < oo (outside the test)", div and conv)
    # diagonal potentials: [S,V]_{ik}=S_ik (V_k - V_i); odd-distance pairs force V constant
    Kd = 24
    Vs = sp.symbols('v1:%d' % (Kd + 1))
    eqs = []
    for i in range(1, Kd + 1):
        for k in range(i + 1, Kd + 1):
            s = sp.Rational(sigma(i - k))
            if s != 0:
                eqs.append(s * (Vs[k - 1] - Vs[i - 1]))
    Md, _ = sp.linear_eq_to_matrix(eqs, list(Vs))
    nsd = Md.nullspace()
    report("2g exact: on-site potentials commuting with S are constant (1-dim), 24 sites",
           len(nsd) == 1 and all(x == nsd[0][0] for x in nsd[0]))


# ----------------------------------------------------------------------------------------
# 3. the exact thermal identity  C = expit(pi J)  on the half-line
# ----------------------------------------------------------------------------------------
mp.mp.dps = 40


def P_list(x, nmax):
    P = [mp.mpf(1), 2 * x]
    for n in range(1, nmax):
        P.append((2 * x * P[n] - n * P[n - 1]) / (n + 1))
    return P


def expit(z):
    return 1 / (1 + mp.e ** (-z))


def C_exact(i, k):
    d = i - k
    if d == 0:
        return mp.mpf(1) / 2
    return mp.sin(mp.pi * d / 2) / (mp.pi * d)


def check_polynomials():
    # three-term recurrence <-> J psi = 2x psi, with psi_j = P_{j-1}(x)
    x = mp.mpf('0.37')
    P = P_list(x, 12)
    ok = True
    for j in range(2, 11):  # (J psi)_j = (j-1) psi_{j-1} + j psi_{j+1}
        lhs = (j - 1) * P[j - 2] + j * P[j]
        ok = ok and abs(lhs - 2 * x * P[j - 1]) < mp.mpf(10) ** -30
    ok = ok and abs(P[1] - 2 * x) < 1e-30  # (J psi)_1 = 1*psi_2 = 2x psi_1
    report("3a recurrence: J psi = 2x psi for psi_j = P_{j-1}(x), P_n Meixner-Pollaczek lambda=1/2, phi=pi/2", ok)
    f = lambda x, m, n: (lambda P: P[m] * P[n] / mp.cosh(mp.pi * x))(P_list(x, max(m, n) + 1))
    worst = 0
    for m in range(0, 5):
        for n in range(0, 5):
            val = mp.quad(lambda x: f(x, m, n), [-mp.inf, -4, 0, 4, mp.inf])
            worst = max(worst, abs(val - (1 if m == n else 0)))
    report("3b orthonormality  int P_m P_n sech(pi x) dx = delta_mn (m,n<=4), residual <1e-20", worst < mp.mpf(10) ** -20,
           "worst=%s" % mp.nstr(worst, 3))


def check_first_row():
    worst = 0
    for n in range(0, 14):
        val = mp.quad(lambda x: expit(2 * mp.pi * x) * P_list(x, n + 1)[n] / mp.cosh(mp.pi * x),
                      [-mp.inf, -6, -2, 0, 2, 6, mp.inf])
        worst = max(worst, abs(val - C_exact(1, n + 1)))
    report("3c first row: <e_1|expit(pi J)|e_{n+1}> = int expit(2 pi x) P_n sech(pi x) dx = C_{1,n+1}, n=0..13, residual <1e-20",
           worst < mp.mpf(10) ** -20, "worst=%s" % mp.nstr(worst, 3))


def check_generating_function():
    # F(t) = int expit(2 pi x) sech(pi x) G(t,x) dx = 1/2 + arctan(t)/pi  (|t|<1), the closed form used in the proof
    worst = 0
    for t in [mp.mpf('0.3'), mp.mpf('-0.55'), mp.mpf('0.8'), mp.mpc('0.2', '0.3'), mp.mpc('-0.4', '0.1')]:
        G = lambda x: (1 - 1j * t) ** (-mp.mpf(1) / 2 + 1j * x) * (1 + 1j * t) ** (-mp.mpf(1) / 2 - 1j * x)
        val = mp.quad(lambda x: expit(2 * mp.pi * x) * G(x) / mp.cosh(mp.pi * x), [-mp.inf, -8, -3, 0, 3, 8, mp.inf])
        worst = max(worst, abs(val - (mp.mpf(1) / 2 + mp.atan(t) / mp.pi)))
    report("3d generating function: int expit(2 pi x) sech(pi x) G(t,x) dx = 1/2 + arctan(t)/pi at 5 points |t|<1, residual <1e-15",
           worst < mp.mpf(10) ** -15, "worst=%s" % mp.nstr(worst, 3))
    # Fourier ingredients: int e^{i w x} sech(pi x) dx = 1/cosh(w/2)  and  cosh(L/2)=1/sqrt(1+t^2)
    w = mp.mpf('0.9')
    ft = mp.quad(lambda x: mp.cos(w * x) / mp.cosh(mp.pi * x), [-mp.inf, 0, mp.inf])
    t = mp.mpf('0.6')
    L = mp.log((1 - 1j * t) / (1 + 1j * t))
    ok = abs(ft - 1 / mp.cosh(w / 2)) < mp.mpf(10) ** -25 and abs(mp.cosh(L / 2) - 1 / mp.sqrt(1 + t * t)) < mp.mpf(10) ** -30
    report("3e Fourier transform of sech and cosh(L/2)=(1+t^2)^(-1/2), L=ln((1-it)/(1+it))", ok)
    # arctan series coefficients equal C_{1,n+1} exactly
    t = sp.symbols('t')
    ser = sp.series(sp.atan(t), t, 0, 40).removeO()
    ok = True
    for n in range(1, 40):
        coef = ser.coeff(t, n)
        ok = ok and (sp.Rational(coef) == sp.Rational(sigma(n).numerator, sigma(n).denominator))
    report("3f exact: Taylor coefficient of arctan(t) at t^n equals sigma(n) = pi*C_{1,n+1}, n=1..39 (sympy)", ok)


def check_full_matrix():
    nmax = 9
    worst = 0
    pts = [-mp.inf, -8, -4, -2, 0, 2, 4, 8, mp.inf]
    for i in range(1, nmax):
        for k in range(i, nmax):
            val = mp.quad(lambda x: expit(2 * mp.pi * x) * P_list(x, nmax)[i - 1] * P_list(x, nmax)[k - 1]
                          / mp.cosh(mp.pi * x), pts)
            worst = max(worst, abs(val - C_exact(i, k)))
    report("3g full block: <e_i|expit(pi J)|e_k> = C_ik for all 1<=i<=k<=8, residual <1e-18", worst < mp.mpf(10) ** -18,
           "worst=%s" % mp.nstr(worst, 3))
    # check the sign: expit(-beta H) with H=-J, beta = pi.  <e_1|.|e_1> = 1/2 and <e_1|.|e_2> = +1/pi
    v = mp.quad(lambda x: expit(2 * mp.pi * x) * 2 * x / mp.cosh(mp.pi * x), [-mp.inf, 0, mp.inf])
    report("3h sign/scale: <e_1|expit(pi J)|e_2> = +1/pi (so beta*a = pi for hops a*j; opposite sign would give -1/pi)",
           abs(v - 1 / mp.pi) < mp.mpf(10) ** -25)
    # local light speed at the Fermi point for hopping t: E=-2t cos k, v = 2 t sin(pi/2) = 2t ; kappa = d v/dx = 2a ; T = a/pi = kappa/(2 pi)
    k, tt = sp.symbols('k t', positive=True)
    v = sp.diff(-2 * tt * sp.cos(k), k).subs(k, sp.pi / 2)
    a = sp.symbols('a', positive=True)
    kappa = sp.diff(v.subs(tt, a * sp.Symbol('x')), sp.Symbol('x'))
    report("3i bookkeeping: v_F = 2t, kappa = dv/dx = 2a, so T = 1/beta = a/pi equals kappa/(2 pi)",
           sp.simplify(v - 2 * tt) == 0 and sp.simplify(kappa / (2 * sp.pi) - a / sp.pi) == 0)


# ----------------------------------------------------------------------------------------
# 4. what is NOT exactly thermal
# ----------------------------------------------------------------------------------------
def check_framework_profile():
    # clocked walker with rate w_j = a (j - x0) : hop = a sqrt(w_j w_{j+1}) ; test-A used x0=0
    j = sp.symbols('j', positive=True)
    h1 = lambda n: sp.sqrt(sp.Integer(n) * (n + 1))
    D = lambda n: h1(n) - n
    entry = sp.simplify(D(2) - D(3) / 3 - D(1))
    # [S,H_fw]_{13} = sigma(-1) h_2 + sigma(-3) h_3 - h_1 sigma(-1)  (h_0=0)
    e13 = sp.simplify(1 * h1(2) + sp.Rational(-1, 3) * h1(3) - h1(1))
    num = sp.N(e13, 50)
    report("4a exact counterexample: [S,H_fw]_{13} = sqrt6 - sqrt12/3 - sqrt2 != 0 for hops sqrt(j(j+1)) (value %s)" % sp.N(e13, 12),
           abs(num) > sp.Rational(1, 100) and sp.simplify(e13 - entry) == 0)
    # symbolic nonexistence of x0 giving exactly linear bonds
    x0, c, d, a = sp.symbols('x0 c d a', real=True)
    n = sp.symbols('n', integer=True)
    poly = sp.expand(((n - x0) * (n + 1 - x0)) * a ** 2 - (c * n + d) ** 2)
    coeffs = sp.Poly(poly, n).all_coeffs()
    sol = sp.solve(coeffs, [c, d, x0], dict=True)
    sol = [s for s in sol if s.get(c, 1) != 0]
    report("4b exact: no x0 makes the bonds a*sqrt((j-x0)(j+1-x0)) equal to a linear sequence c*j+d (coefficient system inconsistent)",
           sol == [])
    # also general: any profile with hops h_j=a*j-type is forced; smooth phi_j phi_{j+1}=a j alternates
    # phi_{j+1} = a j / phi_j  => phi_{j+2}/phi_j = (j+1)/j, product telescopes
    ph = [sp.Rational(1)]
    for jj in range(1, 12):
        ph.append(sp.Rational(jj) / ph[-1])
    ratios = [ph[m + 2] / ph[m] for m in range(len(ph) - 2)]
    report("4c exact: the unique clock with phi_j phi_{j+1}=j (phi_1=1) is staggered: phi_{j+2}/phi_j=(j+1)/j, not a smooth profile",
           all(ratios[m] == sp.Rational(m + 2, m + 1) for m in range(len(ratios))) and ph[1] != ph[2] != ph[3])
    # size of the mismatch: D_j -> 1/2 - 1/(8 j) : the framework bond is the exact bond plus a uniform 1/2 hopping
    jj = sp.symbols('jj', positive=True)
    ser = sp.series(sp.sqrt(jj * (jj + 1)) - jj, jj, sp.oo, 3)
    report("4d asymptotics: sqrt(j(j+1)) - j = 1/2 - 1/(8j) + O(j^-2) (a half-site displacement of the zero of the lapse)",
           sp.simplify(sp.limit(jj * (sp.sqrt(jj * (jj + 1)) - jj - sp.Rational(1, 2)), jj, sp.oo) + sp.Rational(1, 8)) == 0)


def eigh_mp(A):
    return mp.eigsy(A)


def check_finite_wedge_not_gibbs():
    mp.mp.dps = 60
    rows = []
    allbad = True
    for N in range(4, 13):
        Cm = mp.matrix(N, N)
        for i in range(1, N + 1):
            for k in range(1, N + 1):
                Cm[i - 1, k - 1] = C_exact(i, k)
        Tm = mp.matrix(N, N)
        for j in range(1, N):
            Tm[j - 1, j] = Tm[j, j - 1] = mp.mpf(j * (N - j)) / 2
        tau, V = mp.eigsy(Tm)
        eps = []
        for l in range(N):
            v = V[:, l]
            nu = (v.T * Cm * v)[0]
            eps.append(mp.log((1 - nu) / nu))
        # off-diagonal of V^T C V must vanish (common eigenbasis)
        W = V.T * Cm * V
        offd = max(abs(W[a, b]) for a in range(N) for b in range(N) if a != b)
        ratios = [eps[l] / tau[l] for l in range(N) if abs(tau[l]) > mp.mpf('1e-30')]
        spread = (max(ratios) - min(ratios)) / abs(sum(ratios) / len(ratios))
        rows.append((N, float(offd), float(spread)))
        allbad = allbad and spread > mp.mpf('1e-3') and offd < mp.mpf(10) ** -40
    report("4e finite wedge N=4..12: eigenvectors of C_N are those of T_N (offdiag<1e-40) but eps_l/tau_l is NOT constant (rel. spread>1e-3) => by 2a no nearest-neighbour H has C_N as an exact Gibbs state",
           allbad, "(N, offdiag, spread) = %s" % [(a, "%.1e" % b, "%.3f" % c) for a, b, c in rows[:3]] + " ...")
    # N=4 explicit numbers
    N = 4
    Cm = mp.matrix(N, N)
    for i in range(1, N + 1):
        for k in range(1, N + 1):
            Cm[i - 1, k - 1] = C_exact(i, k)
    Tm = mp.matrix(N, N)
    for j in range(1, N):
        Tm[j - 1, j] = Tm[j, j - 1] = mp.mpf(j * (N - j)) / 2
    tau, V = mp.eigsy(Tm)
    eps = [mp.log((1 - (V[:, l].T * Cm * V[:, l])[0]) / (V[:, l].T * Cm * V[:, l])[0]) for l in range(N)]
    pos = sorted([(tau[l], eps[l]) for l in range(N) if tau[l] > 0])
    r = [e / t for t, e in pos]
    report("4f N=4: the two positive levels have eps/tau = %s and %s (different) " % (mp.nstr(r[0], 12), mp.nstr(r[1], 12)),
           abs(r[0] - r[1]) > mp.mpf('1e-3'))
    mp.mp.dps = 40


# ----------------------------------------------------------------------------------------
# 5. process / classical / quantum: three different entropies for the same vacuum
# ----------------------------------------------------------------------------------------
def det_pattern_probs(C):
    """P(n) for the number-conserving Gaussian state with correlation matrix C (determinantal)."""
    N = C.shape[0]
    probs = np.zeros(2 ** N)
    I = np.eye(N)
    for idx, n in enumerate(product([0, 1], repeat=N)):
        M = np.array([C[i] if n[i] else I[i] - C[i] for i in range(N)])
        probs[idx] = np.linalg.det(M)
    return probs


def H2(p):
    p = np.clip(p, 1e-300, 1)
    return -np.sum(p * np.log(p))


def check_three_entropies():
    def Cnum(N, shift=0):
        i = np.arange(N)[:, None]
        j = np.arange(N)[None, :]
        d = i - j
        with np.errstate(divide="ignore", invalid="ignore"):
            C = np.sin(np.pi * d / 2) / (np.pi * d)
        C[d == 0] = 0.5
        return C

    rows = []
    ok_sum = True
    ok_dp = True
    for N in (4, 6, 8, 10, 12, 14):
        C = Cnum(N)
        p = det_pattern_probs(C)
        ok_sum = ok_sum and abs(p.sum() - 1) < 1e-10 and p.min() > -1e-12
        S_shannon = H2(np.maximum(p, 0))
        nu = np.linalg.eigvalsh(C)
        nu = np.clip(nu, 1e-300, 1 - 1e-16)
        S_ent = float(-np.sum(nu * np.log(nu) + (1 - nu) * np.log(1 - nu)))
        # classical vs quantum mutual information of the two halves of the block
        h = N // 2
        pa = p.reshape([2] * N)
        pA = pa.sum(axis=tuple(range(h, N))).reshape(-1)
        pB = pa.sum(axis=tuple(range(0, h))).reshape(-1)
        I_cl = H2(pA) + H2(pB) - H2(p)
        def Sq(Cs):
            v = np.linalg.eigvalsh(Cs)
            v = np.clip(v, 1e-300, 1 - 1e-16)
            return float(-np.sum(v * np.log(v) + (1 - v) * np.log(1 - v)))
        I_q = Sq(C[:h, :h]) + Sq(C[h:, h:]) - Sq(C)
        ok_dp = ok_dp and I_cl <= I_q + 1e-9
        rows.append((N, S_shannon, S_ent, I_cl, I_q))
    report("5a occupation patterns of the N-site wedge form a probability distribution (determinantal formula), N=4..14", ok_sum)
    sl = [(rows[m + 1][1] - rows[m][1]) / 2 for m in range(len(rows) - 1)]
    ent_inc = [(rows[m + 1][2] - rows[m][2]) / 2 for m in range(len(rows) - 1)]
    report("5b Shannon (classical occupation) entropy of the wedge grows linearly in N (slope per site %.3f..%.3f), quantum entanglement entropy S_ent increments %.3f..%.3f per site (decreasing, log-like)"
           % (min(sl), max(sl), min(ent_inc), max(ent_inc)),
           min(sl) > 0.4 and ent_inc[-1] < 0.5 * ent_inc[0] and min(sl) > 3 * max(ent_inc[-2:]))
    report("5c classical mutual information of occupations I_cl <= quantum mutual information I_Q (data processing), N=4..14: last row I_cl=%.4f I_Q=%.4f" % (rows[-1][3], rows[-1][4]),
           ok_dp and rows[-1][4] > 1.2 * rows[-1][3])


# ----------------------------------------------------------------------------------------
if __name__ == "__main__":
    check_finite_commutation()
    check_halfline_commutation()
    check_uniqueness_finite()
    check_uniqueness_halfline()
    check_polynomials()
    check_first_row()
    check_generating_function()
    check_full_matrix()
    check_framework_profile()
    check_finite_wedge_not_gibbs()
    check_three_entropies()
    npass = sum(RESULTS)
    nfail = len(RESULTS) - npass
    print("TOTAL: PASS=%d FAIL=%d" % (npass, nfail))
    if nfail == 0:
        print("HIT: scoped result (1D, half-filled chain, supplied homogeneous vacuum). On the half-line the vacuum is EXACTLY the Fermi-Gibbs state expit(-pi H) of H=-sum_j j(c_j^+ c_{j+1}+h.c.) (beta*a=pi, T=kappa/2pi with kappa=2a), and this is the only nearest-neighbour Hamiltonian of at-most-linear hop growth (up to scale and constant) with that property; the T75 test-A profile a*sqrt(j(j+1)) fails exactly (entry [S,H]_13 = sqrt6-sqrt12/3-sqrt2 != 0), as does every finite wedge N=4..12 checked, so any kappa/2pi fit for those is approximate by construction and the exact target is now known.")
    print("SUMMARY: exact lattice Bisognano-Wichmann on the half-line (C = expit(pi J), J with hops j) follows from commutation with J plus a Meixner-Pollaczek generating-function integral, is unique among linear-growth nearest-neighbour Hamiltonians, and fails exactly for the sqrt(j(j+1)) clocked profile and for finite wedges N=4..12; runtime %.0fs" % (time.time() - T0))
    sys.exit(0 if nfail == 0 else 1)
