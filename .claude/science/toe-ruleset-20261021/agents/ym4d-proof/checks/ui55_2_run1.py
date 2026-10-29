# ui55_2 -- exact control of the leading coefficient (UIR55.md section 4). Criteria: checks/ui55_2_criteria.md.
# sympy exact arithmetic only; no floats in any verdict.
import sympy as sp

res = {}
def rep(name, ok, extra=""):
    res[name] = bool(ok)
    print(f"{name}: {'PASS' if ok else 'FAIL'} {extra}")

# ---------- P1: S^3 moments ----------
def dfact(m):
    r = sp.Integer(1)
    while m > 1:
        r *= m; m -= 2
    return r
def moment(exps):
    if any(e % 2 for e in exps): return sp.Integer(0)
    a = [e // 2 for e in exps]; num = sp.Integer(1)
    for ai in a: num *= dfact(2 * ai - 1)
    den = sp.Integer(1)
    for j in range(sum(a)): den *= (4 + 2 * j)
    return num / den
psi, th, ph = sp.symbols('psi theta phi', real=True)
nh = [sp.cos(psi), sp.sin(psi) * sp.cos(th), sp.sin(psi) * sp.sin(th) * sp.cos(ph), sp.sin(psi) * sp.sin(th) * sp.sin(ph)]
meas = sp.sin(psi) ** 2 * sp.sin(th)
def sphere_avg(expr):
    I = sp.integrate(sp.integrate(sp.integrate(expr * meas, (ph, 0, 2 * sp.pi)), (th, 0, sp.pi)), (psi, 0, sp.pi))
    return sp.simplify(I / (2 * sp.pi ** 2))
okP1 = True
for ex, e in [((2, 0, 0, 0), nh[0] ** 2), ((4, 0, 0, 0), nh[0] ** 4), ((2, 2, 0, 0), nh[0] ** 2 * nh[1] ** 2)]:
    direct = sphere_avg(e); formula = moment(ex)
    print(f"  moment {ex}: formula {formula}, direct {direct}")
    okP1 = okP1 and sp.simplify(direct - formula) == 0
rep("P1 (S^3 moments: formula = direct integration)", okP1)
n1, n2 = sp.symbols('n1 n2', real=True)
def sphere_mean(poly_expr, m22=None):
    P = sp.Poly(sp.expand(poly_expr), n1, n2); tot = sp.Integer(0)
    for (e1, e2), c in P.terms():
        mom = moment((e1, e2, 0, 0))
        if m22 is not None and (e1, e2) == (2, 2): mom = m22
        tot += c * mom
    return sp.nsimplify(tot)

# ---------- P2: vertices derived from the operator ----------
# Plane wave u e^{ik.x}; background a(x2) = (eps/2)(W Z + 1/(W Z)), Z := e^{i p x2}, W := e^{i vartheta}.
x = sp.symbols('x1:5', real=True); k = sp.symbols('k1:5', real=True)
p, eps, q = sp.symbols('p epsilon q', real=True)
Z, W, Asym = sp.symbols('Z W A')
plane = sp.exp(sp.I * sum(ki * xi for ki, xi in zip(k, x)))
def orbital_symbol():
    # (sum_mu (-i d_mu - q A delta_{mu,1})^2) acting on the plane wave; A depends only on x2, and only d_1 multiplies it,
    # so A may be treated as x-independent here (exact).
    out = 0; phi = plane
    for mu in range(4):
        Amu = Asym if mu == 0 else 0
        t1 = -sp.I * sp.diff(phi, x[mu]) - q * Amu * phi
        out += -sp.I * sp.diff(t1, x[mu]) - q * Amu * t1
    return sp.expand(sp.simplify(out / plane))
orb = orbital_symbol()
a_expr = eps / 2 * (W * Z + 1 / (W * Z))
da_dx2 = eps / 2 * (sp.I * p * W * Z - sp.I * p / (W * Z))   # d/dx2 of e^{+-i p x2} = +-i p e^{+-i p x2}
def operator_symbol(dim, s):
    M = sp.zeros(dim, dim)
    for i in range(dim): M[i, i] = orb.subs(Asym, a_expr)
    if dim == 4:
        F = sp.zeros(4, 4); F[1, 0] = da_dx2; F[0, 1] = -da_dx2   # F_{mn} = d_m a_n - d_n a_m, a = a(x2) e_1
        M = M + s * sp.I * q * F
    return M
def vertices(dim, s):
    M = operator_symbol(dim, s)
    O0 = sp.zeros(dim, dim); Vp = sp.zeros(dim, dim); Vm = sp.zeros(dim, dim); O2 = sp.zeros(dim, dim)
    for i in range(dim):
        for j in range(dim):
            P = sp.Poly(sp.expand(M[i, j] * Z ** 2 * W ** 2), Z, W, eps)
            c = lambda zp, wp, ep: P.coeff_monomial(Z ** (zp + 2) * W ** (wp + 2) * eps ** ep)
            O0[i, j] = c(0, 0, 0); Vp[i, j] = c(1, 1, 1); Vm[i, j] = c(-1, -1, 1); O2[i, j] = c(0, 0, 2)
    return O0, Vp, Vm, O2
ksq = sum(ki ** 2 for ki in k)
for dim, s, lab in [(1, 0, "scalar"), (4, 2, "vector s=2")]:
    O0, Vp, Vm, O2 = vertices(dim, s)
    print(f"  {lab}: O0 = {sp.factor(O0[0, 0])}*1 ; V+ = {Vp.tolist()} ; V- = {Vm.tolist()} ; O2 = {O2.tolist()}")
O0s, Vps, Vms, O2s = vertices(1, 0)
rep("P2 (scalar: O0 = k^2, V+ = V- = -q k1, O2 = q^2/2)",
    sp.expand(O0s[0, 0] - ksq) == 0 and sp.expand(Vps[0, 0] + q * k[0]) == 0 and sp.expand(Vms[0, 0] + q * k[0]) == 0
    and sp.expand(O2s[0, 0] - q ** 2 / 2) == 0)

# ---------- P3/P4: integrand, large-|k| expansion with |n| = 1, residues ----------
R, t = sp.symbols('R t', positive=True)
def residue(dim, s, m22=None, show=False):
    O0, Vp, Vm, O2 = vertices(dim, s)
    O0_should = ksq * sp.eye(dim)
    assert (O0 - O0_should).applyfunc(sp.expand) == sp.zeros(dim, dim)
    def shift(Mx, sgn): return Mx.subs(k[1], k[1] + sgn * p)
    tp = (shift(Vm, +1) * Vp).trace()          # V_-(k + p e2) V_+(k)
    tm = (shift(Vp, -1) * Vm).trace()          # V_+(k - p e2) V_-(k)
    sub = {k[0]: R * n1, k[1]: R * n2}
    kk = R ** 2                                 # |k|^2 with |n| = 1
    kp = R ** 2 + 2 * R * n2 * p + p ** 2; km = R ** 2 - 2 * R * n2 * p + p ** 2
    f = O2.trace() / kk - sp.Rational(1, 2) * (tp.subs(sub) / (kk * kp) + tm.subs(sub) / (kk * km))
    diff = (f.subs(p, 1) - f.subs(p, 0)).subs(R, 1 / t)
    ser = sp.series(sp.together(diff), t, 0, 5).removeO()
    c3 = sp.expand(ser.coeff(t, 3)); c4 = sp.expand(ser.coeff(t, 4))
    if show: print(f"    t^3 coeff c3 = {sp.factor(c3)} ; t^4 coeff h = {sp.factor(c4)}")
    return sphere_mean(c3, m22), sphere_mean(c4, m22)
c3S, hS = residue(1, 0, show=True)
c3V, hV = residue(4, 2, show=True)
print(f"  <c3_S> = {c3S}, <h_S> = {hS};  <c3_V> = {c3V}, <h_V> = {hV}")
rep("L0 (<c3> = 0, scalar and vector)", c3S == 0 and c3V == 0)
rep("L1 (<h_S> = 1/12, i.e. C_S = q^2/(96 pi^2) = q^2 c_g)", hS == sp.Rational(1, 12))
rep("L2 (<h_V>/<h_S> = -20)", sp.simplify(hV / hS) == -20, f"[ratio = {sp.simplify(hV / hS)}]")
cg = sp.Rational(1, 96) / sp.pi ** 2
CS = q ** 2 * hS / (8 * sp.pi ** 2); CV = q ** 2 * hV / (8 * sp.pi ** 2)
rep("L3 (per root: transverse -21 q^2 c_g, full -22 q^2 c_g, ratio 21/22)",
    sp.simplify(CV - CS + 21 * q ** 2 * cg) == 0 and sp.simplify(CV - 2 * CS + 22 * q ** 2 * cg) == 0
    and sp.simplify((CV - CS) / (CV - 2 * CS) - sp.Rational(21, 22)) == 0)
ok4 = True
for Nn in (2, 3, 4):
    h = sp.symbols(f'h1:{Nn + 1}', real=True)
    ok4 = ok4 and sp.expand(sum((h[i] - h[j]) ** 2 for i in range(Nn) for j in range(i + 1, Nn))
                            - (Nn * sum(hi ** 2 for hi in h) - sum(h) ** 2)) == 0
rep("L4 (sum_{i<j}(h_i-h_j)^2 = N sum h^2 - (sum h)^2, hence N^2 under sum h = 0, sum h^2 = N)", ok4)
N = sp.symbols('N', positive=True)
b0 = 11 * N / (48 * sp.pi ** 2); beta0 = 2 * N * 2 * b0
slope_T = 4 * (-21) * cg * N ** 2; slope_gh = 4 * (-1) * cg * N ** 2
rep("L5 (u-units: transverse -84 N^2 c_g = -(21/22) beta0 = -7N^2/(8 pi^2); ghost -(1/22) beta0; sum -beta0; beta0 = 11N^2/(12 pi^2))",
    sp.simplify(slope_T + 7 * N ** 2 / (8 * sp.pi ** 2)) == 0 and sp.simplify(slope_gh + N ** 2 / (24 * sp.pi ** 2)) == 0
    and sp.simplify(slope_T + slope_gh + beta0) == 0 and sp.simplify(slope_T / beta0 + sp.Rational(21, 22)) == 0
    and sp.simplify(beta0 - 11 * N ** 2 / (12 * sp.pi ** 2)) == 0)
_, hV1 = residue(4, 1)
rep("Lc1 control (spin coupling 1) must FIRE", sp.simplify(hV1 / hS) != -20, f"[ratio = {sp.simplify(hV1 / hS)}]")
_, hS_bad = residue(1, 0, m22=sp.Rational(1, 16))
rep("Lc2 control (product-of-marginals moment) must FIRE", hS_bad != sp.Rational(1, 12), f"[<h_S> = {hS_bad}]")
rep("Lc3 control (FN-1 slip 2N b0) must FIRE", sp.simplify(88 * N ** 2 * cg - 2 * N * b0) != 0)
print(f"OVERALL: {'PASS' if all(res.values()) else 'FAIL'} ({sum(res.values())}/{len(res)} items true; controls count as true when they fire)")
