#!/usr/bin/env python3
"""C9 fresh-context check, part (b): the ruler model  du_x = xi_x (1 + (Delta u)_x).

New code; imports nothing from the C9 runner.  Two independent routes:
  R-pos : position space, concrete rational Delta (central difference), symbolic u,
          brackets from my own Jacobian-based vector-field engine; structure functions
          obtained by SOLVING the frame equation (not by plugging in C9's formula), then
          compared with C9's formula.
  R-mom : Fourier coordinates, where the model is V_a = d_a + sum_k lam_k u_k d_(a+k)
          (derived by hand, see report), with a FULLY SYMBOLIC symbol lam_k (lam_0 = 0).
          The first-order structure functions come from C = B F^{-1} expanded to O(u).
Everything exact (sympy rationals / polynomials; cyclotomic arithmetic via Phi_L remainders).
"""
import random, sys, itertools
import sympy as sp

PASS = FAIL = 0
def check(name, ok, detail=""):
    global PASS, FAIL
    if ok: PASS += 1
    else: FAIL += 1
    print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}")
    sys.stdout.flush()

def nbar(n, L):
    n %= L
    return n - L if n > L // 2 else n

# ---------------------------------------------------------------- R-pos
def central(L):
    D = sp.zeros(L, L)
    for x in range(L):
        D[x, (x + 1) % L] += sp.Rational(1, 2)
        D[x, (x - 1) % L] -= sp.Rational(1, 2)
    return D

def bracket(V, W, xs):
    # [V,W]^i = V(W^i) - W(V^i)
    n = len(xs)
    return [sp.expand(sum(V[j] * sp.diff(W[i], xs[j]) - W[j] * sp.diff(V[i], xs[j]) for j in range(n)))
            for i in range(n)]

def r_pos(L):
    u = sp.symbols(f"u0:{L}")
    D = central(L)
    g = [1 + sum(D[x, y] * u[y] for y in range(L)) for x in range(L)]
    V = [[g[i] if k == i else 0 for k in range(L)] for i in range(L)]   # V_i = g_i d_i (xi = delta_i)
    ok_formula = True; fielddep = False
    Csol = {}
    for i in range(L):
        for j in range(L):
            B = bracket(V[i], V[j], u)
            # solve B = sum_e C^e V_e ; V diagonal frame -> C^e = B^e / g_e  (on {g != 0})
            C = [sp.cancel(B[e] / g[e]) for e in range(L)]
            Csol[(i, j)] = C
            for e in range(L):
                if e == j and i != j:
                    pred = D[j, i] * g[i] / g[j]
                elif e == i and i != j:
                    pred = -D[i, j] * g[j] / g[i]
                else:
                    pred = 0
                if sp.simplify(C[e] - pred) != 0:
                    ok_formula = False
                if any(sp.diff(C[e], v) != 0 for v in u):
                    fielddep = True
    check(f"Rpos_closure_formula_L{L}",
          ok_formula and fielddep,
          "frame solve gives C_ij^j = D_ji g_i/g_j, C_ij^i = -D_ij g_j/g_i, field-dependent")
    # full Jacobi identity with derivative term, sign convention: sum_cyc (C_ab^d C_dc^e - V_c(C_ab^e)) = 0
    if L <= 5:
        rnd = random.Random(7 + L)
        pt = {v: sp.Rational(rnd.randint(-5, 5), rnd.randint(7, 13)) for v in u}
        Cpt = {k: [sp.nsimplify(c.subs(pt)) for c in v] for k, v in Csol.items()}
        def Vder(c, f):  # V_c(f) at pt
            return sum((V[c][j] * sp.diff(f, u[j])).subs(pt) for j in range(L))
        ok_plus = True; ok_minus = True
        for a, b, c in itertools.product(range(L), repeat=3):
            for e in range(L):
                s_quad = 0; s_der = 0
                for (x, y, z) in [(a, b, c), (b, c, a), (c, a, b)]:
                    s_quad += sum(Cpt[(x, y)][d] * Cpt[(d, z)][e] for d in range(L))
                    s_der += Vder(z, Csol[(x, y)][e])
                if sp.simplify(s_quad - s_der) != 0: ok_plus = False
                if sp.simplify(s_quad + s_der) != 0: ok_minus = False
        check(f"Rpos_JacobiSign_L{L}", ok_plus and not ok_minus,
              "sum_cyc C C = +sum_cyc V_c(C) at a random rational point (and the '-' sign fails)")

# ---------------------------------------------------------------- R-mom (symbolic symbol)
def mom_model(L, lam):
    u = sp.symbols(f"w0:{L}")      # Fourier coordinates u_k
    # V_a = d_a + sum_k lam_k u_k d_(a+k)  ; frame matrix F[a][m]
    F = sp.zeros(L, L)
    for a in range(L):
        F[a, a] += 1
        for k in range(L):
            F[a, (a + k) % L] += lam[k] * u[k]
    return u, F

def mom_check(L):
    lam = [0] + list(sp.symbols(f"l1:{L}"))
    u, F = mom_model(L, lam)
    V = [list(F.row(a)) for a in range(L)]
    # brackets B[a,b] (components), then C = B F^{-1}; to first order F^{-1} = I - N
    N = F - sp.eye(L)
    ok_c0 = True; ok_d1 = True; ok_jac = True; jac_nonzero = False
    C0 = {}; C1 = {}
    for a in range(L):
        for b in range(L):
            B = sp.Matrix([bracket(V[a], V[b], u)])
            Cfirst = sp.expand(B - B * N)          # exact through O(u)  (B is affine in u)
            c0 = Cfirst.subs({v: 0 for v in u})
            C0[(a, b)] = c0
            z0 = {v: 0 for v in u}
            C1[(a, b)] = [[sp.diff(Cfirst[e], u[c]).subs(z0) for e in range(L)] for c in range(L)]
            for e in range(L):
                pred = (lam[a] - lam[b]) if e == (a + b) % L else 0
                if sp.expand(c0[e] - pred) != 0: ok_c0 = False
            for c in range(L):
                for e in range(L):
                    d = C1[(a, b)][c][e]
                    if e == (a + b + c) % L:
                        pred = lam[c] * (lam[(a + c) % L] - lam[(b + c) % L] - lam[a] + lam[b])
                    else:
                        pred = 0
                    if sp.expand(d - pred) != 0: ok_d1 = False
    # L2: Jac(cbar)_abc = sum_cyc <dC_ab^(a+b+c)(0), V_c(0)> ; V_c(0) = d_c so contraction = d/du_c
    for a, b, c in itertools.product(range(L), repeat=3):
        e = (a + b + c) % L
        jac = sum(C0[(x, y)][(x + y) % L] * C0[((x + y) % L, z)][e] for (x, y, z) in [(a, b, c), (b, c, a), (c, a, b)])
        der = sum(C1[(x, y)][z][e] for (x, y, z) in [(a, b, c), (b, c, a), (c, a, b)])
        if sp.expand(jac - der) != 0: ok_jac = False
        if sp.expand(jac) != 0: jac_nonzero = True
    check(f"Rmom_cbar_L{L}", ok_c0, "generic symbol: C(0) graded, cbar(a,b) = lam_a - lam_b, Lam_n = -lam_n")
    check(f"Rmom_firstorder_L{L}", ok_d1, "d_c C_ab^e(0) = lam_c(lam_(a+c)-lam_(b+c)-lam_a+lam_b) delta_(e,a+b+c)")
    check(f"Rmom_L2_identity_L{L}", ok_jac and jac_nonzero,
          "Jac(cbar) = +sum_cyc <dC, V_c(0)> as polynomials in lam; Jac not identically 0")

# ---------------------------------------------------------------- spectra and Jacobiators
def jac_cbar(L, lam, reduce):
    bad = []
    for a, b, c in itertools.product(range(L), repeat=3):
        cb = lambda x, y: lam[x % L] - lam[y % L]
        j = sum(cb(x, y) * cb(x + y, z) for (x, y, z) in [(a, b, c), (b, c, a), (c, a, b)])
        if reduce(j) != 0:
            bad.append((a, b, c))
    return bad

def cyclo(L):
    w = sp.symbols("w")
    Phi = sp.cyclotomic_poly(L, w)
    def red(expr):
        num, den = sp.fraction(sp.together(sp.expand(expr)))
        r = sp.rem(sp.expand(num * w ** (4 * L)), Phi, w)  # clear negative powers
        return sp.expand(r)
    return w, Phi, red

def spectra():
    # central difference: lam_n = (w^n - w^-n)/2
    jac_ok = True
    for L in range(3, 13):
        w, Phi, red = cyclo(L)
        lam = [(w ** n - w ** (-n)) / 2 for n in range(L)]
        Lam = [-x for x in lam]
        ratio_ok = red(Lam[2] - (w + 1 / w) * Lam[1]) == 0
        S_ok = red(Lam[1]) != 0 and red(lam[1] - lam[L - 1]) != 0
        bad = jac_cbar(L, lam, red) if L <= 9 else None
        jz = (bad is not None and len(bad) == 0)
        if L == 3:
            jac_ok &= jz
        elif bad is not None:
            jac_ok &= (not jz)
        check(f"central_L{L}", ratio_ok and S_ok,
              f"Lam_2 = (w+1/w) Lam_1 = 2cos(2pi/L) Lam_1 in Q(w); (S) on cbar"
              + ("" if bad is None else f"; Jac(cbar) {'= 0' if jz else '!= 0 (%d triples)' % len(bad)}"))
    check("central_Jac_pattern", jac_ok, "Jac(cbar) = 0 exactly at L = 3 and != 0 at L = 4..9")
    # exact sign of 2cos(2pi/L): positive iff L >= 5 (elementary: 2pi/L < pi/2); exact zero at L = 4
    w, Phi, red = cyclo(4)
    check("central_L4_ratio_zero", red(w + 1 / w) == 0, "L = 4: Lam_2 = 0 exactly (inside the arc set {0})")
    # SLAC: lam_n proportional to nbar (overall constant i 2pi/L dropped: Jac is homogeneous)
    for L in (5, 7, 9, 11):
        lam = [nbar(n, L) for n in range(L)]
        bad = jac_cbar(L, lam, lambda x: x)
        Lam = [-x for x in lam]
        sp_ok = all(Lam[n] == nbar(n, L) * Lam[1] for n in range(L))
        check(f"SLAC_L{L}", sp_ok and lam[1] - lam[L - 1] != 0 and len(bad) > 0,
              f"Lam_n = nbar Lam_1 for all n, cbar(1,-1) = 2 lam_1 != 0, Jac(cbar) != 0 on {len(bad)} triples; "
              f"first bad triple {bad[0]}")
    # forward difference: Lam_1 + Lam_-1 = 2 - w - 1/w  != 0
    ok = True
    for L in range(3, 10):
        w, Phi, red = cyclo(L)
        ok &= red((w - 1) + (1 / w - 1)) != 0
    check("forward_step1", ok, "forward difference: Lam_1 + Lam_-1 != 0 for L = 3..9")

def injectivity_covariance():
    # V_xi(u=0) = xi, so xi -> V_xi is injective; covariance: T u_x = u_(x-1)
    L = 5
    u = sp.symbols(f"u0:{L}")
    D = central(L)
    xi = sp.symbols(f"x0:{L}")
    def Vxi(xiv, uu):
        g = [1 + sum(D[x, y] * uu[y] for y in range(L)) for x in range(L)]
        return [xiv[x] * g[x] for x in range(L)]
    Tu = [u[(x - 1) % L] for x in range(L)]
    Txi = [xi[(x - 1) % L] for x in range(L)]
    lhs = Vxi(Txi, Tu)
    rhs0 = Vxi(xi, u)
    rhs = [rhs0[(x - 1) % L] for x in range(L)]
    cov = all(sp.expand(lhs[x] - rhs[x]) == 0 for x in range(L))
    inj = all(sp.expand(Vxi(xi, [0] * L)[x] - xi[x]) == 0 for x in range(L))
    check("P1_covariance_injectivity_L5", cov and inj,
          "V_(T xi)(T u) = T_* V_xi(u) (u-translation T, background u = 0 T-fixed); V_xi(0) = xi so G injective")

if __name__ == "__main__":
    for L in range(3, 8):
        r_pos(L)
    for L in range(3, 7):
        mom_check(L)
    spectra()
    injectivity_covariance()
    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
