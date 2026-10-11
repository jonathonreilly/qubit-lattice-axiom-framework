"""W2 gap N7: the ultralocal ('gradient') representative.  Anomaly {C_c[xi],C_s[N]} = int xi_c N v_c with
v_c = d_c A_c a background vector (WKB: constant over the wavelength; take v = b e_x).
Anomalous variation: dS = b int [ (d_x B) eps - (d_x chi) Phi ].  Check WZ consistency, solve a WZ ansatz,
and get the scalar spectrum for k parallel to v (x) and k at 45 degrees."""
import sympy as sp, numpy as np
t, x, y, z = sp.symbols('t x y z', real=True); X = (x, y, z)
b, M = sp.symbols('b M_p2', real=True)
F = lambda n: sp.Function(n)(t, x, y, z)
Phi, B, Psi, E, pi_, zeta, eps, chi = [F(n) for n in ('Phi', 'B', 'Psi', 'E', 'pi', 'zeta', 'eps', 'chi')]
grad = lambda f: [sp.diff(f, v) for v in X]; dot = lambda u, v: sum(p*q for p, q in zip(u, v))
lap = lambda f: sum(sp.diff(f, v, 2) for v in X)
def vary(L, subs):
    s = sp.symbols('s'); return sp.expand(sp.diff(L.subs({f: f + s*d for f, d in subs.items()}, simultaneous=True), s).subs(s, 0))
def EL_all(expr, flds):
    out = []
    for f in flds:
        r = sp.euler_equations(expr, [f], [t, x, y, z]); el = sp.expand(r[0].lhs if r else 0)
        if el != 0: out.append(el)
    return out
gauge = {Phi: sp.diff(eps, t), B: -eps + sp.diff(chi, t), E: chi, Psi: sp.Integer(0), pi_: -eps, zeta: -chi}
anom = b*(sp.diff(B, x)*eps - sp.diff(chi, x)*Phi)
e1, e2, c1, c2 = F('e1'), F('e2'), F('c1'), F('c2')
A1 = b*(sp.diff(B, x)*e1 - sp.diff(c1, x)*Phi); A2 = b*(sp.diff(B, x)*e2 - sp.diff(c2, x)*Phi)
cons = sp.expand(vary(A1, {Phi: sp.diff(e2, t), B: -e2 + sp.diff(c2, t)}) - vary(A2, {Phi: sp.diff(e1, t), B: -e1 + sp.diff(c1, t)}))
print("WZ consistency (Euler residuals):", EL_all(cons, [e1, e2, c1, c2]) == [])
cs = sp.symbols('k1:13')
ansatz = [sp.diff(B, x)*pi_, sp.diff(zeta, x)*Phi, sp.diff(zeta, t, x)*pi_, pi_*sp.diff(pi_, x),
          sp.diff(E, x)*pi_, sp.diff(zeta, x)*Psi, pi_*sp.diff(Psi, x), B*sp.diff(pi_, x),
          zeta*sp.diff(Phi, x), sp.diff(zeta, t)*sp.diff(pi_, x), pi_*sp.diff(pi_, t), zeta*sp.diff(zeta, x)]
SWZ = b*sum(c*a_ for c, a_ in zip(cs, ansatz))
total = sp.expand(vary(SWZ, gauge) + anom)
eqs = []
for el in EL_all(total, [Phi, B, Psi, E, pi_, zeta, eps, chi]):
    ders = sorted(el.atoms(sp.Derivative).union({a_ for a_ in el.atoms(sp.Function) if a_.args == (t, x, y, z)}), key=str)
    eqs += sp.Poly(el, *ders).coeffs()
sol = sp.solve(eqs, cs, dict=True); print("WZ solutions:", sol)
if not sol:
    print("RESULT: the ultralocal representative with a constant background gradient is NOT Wess-Zumino consistent")
    print("        (the eps-eps term b(eps2 d_x eps1 - eps1 d_x eps2) is not a total derivative), and no local WZ term")
    print("        in the 12-term ansatz exists.  It cannot stand alone as a c-number cocycle of the abelian linearized")
    print("        gauge group; any completion producing it must also deform {C_s,C_s}.  Use C3's Killing representative.")
    raise SystemExit(0)
s0 = {c: sol[0].get(c, c) for c in cs}; free = [c for c in cs if s0[c] == c]
LWZ = sp.expand(SWZ.subs(s0).subs({c: 0 for c in free}))
print("L_WZ (gradient branch) =", sp.simplify(LWZ), " | free (gauge-invariant/total-derivative) coeffs set to 0:", free)
print("check:", EL_all(sp.expand(vary(LWZ, gauge) + anom), [Phi, B, Psi, E, pi_, zeta, eps, chi]) == [])
L_GR = M*(-3*sp.diff(Psi, t)**2 + dot(grad(Psi), grad(Psi)) - 2*dot(grad(Phi), grad(Psi)) - 2*sp.diff(Psi, t)*lap(B - sp.diff(E, t)))
L = sp.expand((L_GR + LWZ).subs({B: 0, E: 0}).doit())
w, kx, ky = sp.symbols('omega k_x k_y', real=True)
fields = [Phi, Psi, pi_, zeta]
def sym(fac):
    if isinstance(fac, sp.Derivative):
        m = 1
        for var, cnt in fac.variable_count:
            m *= {t: -sp.I*w, x: sp.I*kx, y: sp.I*ky, z: 0}[var]**cnt
        return fields.index(fac.expr), m
    return fields.index(fac), 1
Mq = sp.zeros(4, 4)
for term in sp.Add.make_args(L):
    coeff, facs = sp.Integer(1), []
    for fac in sp.Mul.make_args(term):
        if isinstance(fac, sp.Derivative) or (isinstance(fac, sp.Function) and fac.args == (t, x, y, z)): facs.append(fac)
        elif isinstance(fac, sp.Pow) and fac.exp == 2: facs += [fac.base, fac.base]
        else: coeff *= fac
    (ia, s1), (ib, s2) = sym(facs[0]), sym(facs[1])
    Mq[ib, ia] += coeff*s1*sp.conjugate(s2)/4; Mq[ia, ib] += coeff*sp.conjugate(s1)*s2/4
Mq = sp.simplify(Mq); print("Hermitian:", sp.simplify(Mq - Mq.H) == sp.zeros(4, 4))
det = sp.factor(sp.simplify(Mq.det())); print("det =", det)
W2 = sp.symbols('W2'); roots = sp.solve(sp.Eq(sp.simplify(det.subs(w, sp.sqrt(W2))), 0), W2); print("omega^2 roots:", roots)
P1, P2, P3, P4 = Mq[:2, :2], Mq[:2, 2:], Mq[2:, :2], Mq[2:, 2:]
S = sp.simplify(P4 - P3*P1.inv()*P2)
Sf = sp.lambdify((w, kx, ky, b, M), S, 'numpy'); dSf = sp.lambdify((w, kx, ky, b, M), sp.diff(S, w), 'numpy')
for bv in (+0.01, -0.01):
    for (kxv, kyv) in [(0.3, 0.0), (1.0, 0.0), (0.3, 0.3), (1.0, 1.0), (0.05, 0.5)]:
        out = []
        for r in roots:
            rv = complex(r.subs({kx: kxv, ky: kyv, b: bv, M: 1.0}))
            if abs(rv.imag) > 1e-12 or rv.real < 0:
                out.append(f"w2={rv.real:+.3e}{rv.imag:+.1e}j TACHYON/complex"); continue
            wv = np.sqrt(rv.real); Sv = np.array(Sf(wv, kxv, kyv, bv, 1.0), dtype=complex)
            ev, evec = np.linalg.eigh(Sv); v = evec[:, np.argmin(abs(ev))]
            En = wv*np.real(v.conj() @ np.array(dSf(wv, kxv, kyv, bv, 1.0), dtype=complex) @ v)
            out.append(f"w2={rv.real:+.3e} {'healthy' if En > 0 else 'GHOST'}")
        print(f" b={bv:+g} k=({kxv},{kyv}): " + " | ".join(out))
