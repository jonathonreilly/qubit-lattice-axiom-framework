"""C4 / lane RW / probe W2, part 2: Stueckelberg (Wess-Zumino) effective action for the
C3 boost anomaly, scalar sector of linearized gravity, flat background, continuum symbols
(the lattice replaces k by qhat; the IR statement is what is checked here).

Anomaly (C3, refereed, Killing sector; local representative 'rep 1'):
   {C_c[xi], C_s[N]}  contains  -a * sum_c int xi_c (d_c N)   (a = background anomaly density)
=> under the linearized gauge transformations (eps = time, chi = spatial scalar,
   dPhi = eps_dot, dB = -eps + chi_dot, dE = chi, dPsi = 0) the action varies by
   dS_anom = a int [ dB.d eps - d chi.d Phi ]          (Wess-Zumino consistent; checked)
We (i) check WZ consistency, (ii) find a local WZ term S_WZ[pi, zeta] with
   d pi = -eps, d zeta = -chi  and  delta S_WZ = -delta S_anom,
(iii) add S_GR (scalar sector, M_P^2 = 1) and find the propagating scalar spectrum,
its sign (ghost / tachyon / healthy) and mass in units of a.
"""
import sympy as sp

t = sp.symbols('t', real=True)
x, y, z = sp.symbols('x y z', real=True)
X = (x, y, z)
a, Mp2 = sp.symbols('a M_p2', real=True)


def grad(f):
    return [sp.diff(f, v) for v in X]


def dot(u, v):
    return sum(ui * vi for ui, vi in zip(u, v))


def lap(f):
    return sum(sp.diff(f, v, 2) for v in X)


F = lambda name: sp.Function(name)(t, x, y, z)
Phi, B, Psi, E, pi_, zeta = [F(n) for n in ('Phi', 'B', 'Psi', 'E', 'pi', 'zeta')]
eps, chi = F('eps'), F('chi')

# ---- variational helper: vary a Lagrangian density L under field -> field + s*delta ----
def vary(L, subs):
    s = sp.symbols('s')
    Ls = L.subs({f: f + s * d for f, d in subs.items()}, simultaneous=True)
    return sp.expand(sp.diff(Ls, s).subs(s, 0))


def is_total_derivative(expr):
    """Euler operator test: expr is a total divergence iff its Euler-Lagrange derivative
    vanishes for every field it contains (all functions of (t,x,y,z))."""
    funcs = sorted(expr.atoms(sp.Function), key=str)
    funcs = [f for f in funcs if f.args == (t, x, y, z)]
    for f in funcs:
        res = sp.euler_equations(expr, [f], [t, x, y, z])
        el = res[0].lhs if res else 0
        if sp.simplify(el) != 0:
            return False, f, sp.simplify(el)
    return True, None, None

gauge = {Phi: sp.diff(eps, t), B: -eps + sp.diff(chi, t), E: chi, Psi: sp.Integer(0),
         pi_: -eps, zeta: -chi}

# ---- (a) GR scalar sector, sigma = B - E_dot; check gauge invariance ----
sigma = B - sp.diff(E, t)
L_GR = Mp2 * (-3 * sp.diff(Psi, t)**2 + dot(grad(Psi), grad(Psi)) - 2 * dot(grad(Phi), grad(Psi))
              - 2 * sp.diff(Psi, t) * lap(sigma))
ok, f, el = is_total_derivative(vary(L_GR, gauge))
print("(a) linearized GR scalar sector gauge invariant (eps and chi):", ok)

# ---- (b) anomaly: dS_anom = a [ dB.d eps - d chi . d Phi ];  WZ consistency ----
eps1, eps2, chi1, chi2 = F('eps1'), F('eps2'), F('chi1'), F('chi2')
def A(e, c, fields):
    Bf, Phif = fields
    return a * (dot(grad(Bf), grad(e)) - dot(grad(c), grad(Phif)))
# delta_2 of A(1) - delta_1 of A(2)
s = sp.symbols('s')
A1 = A(eps1, chi1, (B, Phi)); A2 = A(eps2, chi2, (B, Phi))
d2A1 = vary(A1, {Phi: sp.diff(eps2, t), B: -eps2 + sp.diff(chi2, t)})
d1A2 = vary(A2, {Phi: sp.diff(eps1, t), B: -eps1 + sp.diff(chi1, t)})
ok, f, el = is_total_derivative(sp.expand(d2A1 - d1A2))
print("(b) Wess-Zumino consistency [d2 A1 - d1 A2 = total derivative]:", ok)

# ---- (c) WZ term: general quadratic ansatz, solve delta S_WZ + delta S_anom = total derivative ----
cs = sp.symbols('c1:10')
gp, gz = grad(pi_), grad(zeta)
ansatz = [dot(grad(B), gp), dot(gz, grad(Phi)), dot(grad(sp.diff(zeta, t)), gp), dot(gp, gp),
          dot(grad(E), gp), dot(gz, grad(Psi)), dot(gp, grad(Psi)), sp.diff(pi_, t)**2, dot(gz, gz)]
S_WZ = a * sum(c * term for c, term in zip(cs, ansatz))
anom = a * (dot(grad(B), grad(eps)) - dot(grad(chi), grad(Phi)))
total = sp.expand(vary(S_WZ, gauge) + anom)
# Euler operator must vanish for every field: collect linear equations in c's
eqs = []
for fld in [Phi, B, Psi, E, pi_, zeta, eps, chi]:
    res = sp.euler_equations(total, [fld], [t, x, y, z])
    el = sp.expand(res[0].lhs if res else 0)
    if el == 0:
        continue
    # coefficients of independent derivative monomials
    derivs = sorted(el.atoms(sp.Derivative).union(el.atoms(sp.Function)), key=str)
    poly = sp.Poly(el, *derivs) if derivs else None
    if poly is not None:
        eqs += [sp.expand(cf) for cf in poly.coeffs()]
sol = sp.solve(eqs, cs, dict=True)
print("(c) WZ coefficient solutions:", sol)
sol0 = {c: sol[0].get(c, c) for c in cs}
free = [c for c in cs if sol0[c] == c]
S_WZ_min = sp.expand(S_WZ.subs(sol0).subs({c: 0 for c in free}))
print("    minimal WZ term (free coefficients set to 0, they are separately gauge invariant):")
print("    L_WZ =", sp.simplify(S_WZ_min))
ok, f, el = is_total_derivative(sp.expand(vary(S_WZ_min, gauge) + anom))
print("    check delta(L_WZ) + delta(anomaly) = total derivative:", ok)

# ---- (d) spectrum: gauge B = E = 0 (fixes eps, chi); fields Phi, Psi, pi, zeta ----
w, k = sp.symbols('omega k', positive=True)
L = sp.expand((L_GR + S_WZ_min).subs({B: 0, E: 0}).doit())
fields = [Phi, Psi, pi_, zeta]
# plane waves along x: f -> f_hat exp(-i w t + i k x); quadratic form via second derivatives of
# the real Lagrangian evaluated on complex amplitude pairs (Hermitian matrix M with L = v^dag M v)
def sym(fac):
    """(field index, symbol on exp(i(kx - w t)))"""
    if isinstance(fac, sp.Derivative):
        mult = 1
        for var, cnt in fac.variable_count:
            if var == t: mult *= (-sp.I * w)**cnt
            elif var == x: mult *= (sp.I * k)**cnt
            else: mult *= 0
        return fields.index(fac.expr), mult
    return fields.index(fac), 1

M = sp.zeros(4, 4)
for term in sp.Add.make_args(L):
    coeff, facs = sp.Integer(1), []
    for fac in sp.Mul.make_args(term):
        if isinstance(fac, sp.Derivative) or (isinstance(fac, sp.Function) and fac.args == (t, x, y, z)):
            facs.append(fac)
        elif isinstance(fac, sp.Pow) and fac.exp == 2 and (isinstance(fac.base, sp.Derivative) or isinstance(fac.base, sp.Function)):
            facs += [fac.base, fac.base]
        else:
            coeff *= fac
    if len(facs) != 2:
        continue  # terms with y,z derivatives vanish for k along x
    (ia, s1), (ib, s2) = sym(facs[0]), sym(facs[1])
    # period average of Re(A_a s1 e) Re(A_b s2 e) = 1/2 Re[s1 A_a conj(s2 A_b)]; write as v^dag M v
    M[ib, ia] += coeff * s1 * sp.conjugate(s2) / 4
    M[ia, ib] += coeff * sp.conjugate(s1) * s2 / 4
M = sp.simplify(M)
print("\n(d) Fourier quadratic form v^dag M v (fields Phi, Psi, pi, zeta; gauge B = E = 0, k along x):")
sp.pprint(M)
print("    Hermitian:", sp.simplify(M - M.H) == sp.zeros(4, 4))
det = sp.factor(sp.simplify(M.det()))
print("    det M(omega,k) =", det)
W2s = sp.symbols('W2', real=True)
print("    omega^2 roots:", sp.solve(sp.Eq(sp.simplify(det.subs(w, sp.sqrt(W2s))), 0), W2s))
# reduced action of the propagating mode: eliminate Phi (Lagrange multiplier) and Psi, keep (pi, zeta)
Mr = M
# Schur complement onto (pi, zeta) after eliminating Phi, Psi (non-dynamical in this gauge?)
P1 = Mr[:2, :2]; P2 = Mr[:2, 2:]; P3 = Mr[2:, :2]; P4 = Mr[2:, 2:]
print("    det of (Phi,Psi) block:", sp.factor(sp.simplify(P1.det())))
if sp.simplify(P1.det()) != 0:
    S = sp.simplify(P4 - P3 * P1.inv() * P2)
    print("    Schur complement on (pi, zeta):"); sp.pprint(sp.simplify(S))
    print("    det Schur:", sp.factor(sp.simplify(S.det())))

# ---- (e) Krein signature (energy sign) of the extra mode, both signs of a ----
# For L = v^dag S(omega) v, the on-shell mode energy is E = omega * v^dag (dS/domega) v (S v = 0).
import numpy as np
Sfun = sp.lambdify((w, k, a, Mp2), sp.simplify(P4 - P3 * P1.inv() * P2), 'numpy')
dSfun = sp.lambdify((w, k, a, Mp2), sp.diff(sp.simplify(P4 - P3 * P1.inv() * P2), w), 'numpy')
print("\n(e) extra scalar: omega^2 = a k^2/(3a - 2 Mp2 k^2);  mu^2 := a/(2 Mp2)")
for aval in (+1.0, -1.0):
    for kval in (0.3, 1.0, 3.0, 10.0):
        Mval = 1.0
        w2 = aval * kval**2 / (3 * aval - 2 * Mval * kval**2)
        if w2 <= 0:
            print(f"   a={aval:+.0f} k={kval:5.1f}: omega^2 = {w2:+.4f}  -> imaginary frequency (tachyon), growth rate {np.sqrt(-w2):.4f}")
            continue
        wv = np.sqrt(w2)
        S = np.array(Sfun(wv, kval, aval, Mval), dtype=complex)
        ev, evec = np.linalg.eigh(S)
        v = evec[:, np.argmin(abs(ev))]
        dS = np.array(dSfun(wv, kval, aval, Mval), dtype=complex)
        Emode = wv * np.real(v.conj() @ dS @ v)
        print(f"   a={aval:+.0f} k={kval:5.1f}: omega^2 = {w2:+.4f}, |min eig S| = {min(abs(ev)):.1e}, mode energy sign = {np.sign(Emode):+.0f} ({'healthy' if Emode > 0 else 'GHOST'})")
print("   large-k limit: omega^2 -> -a/(2 Mp2) = -mu^2 ;  small-k limit: omega^2 -> k^2/3")
