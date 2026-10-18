#!/usr/bin/env python3
"""C4b second code path (no kernel engine): one-particle OPERATOR identities in position space, applied to a generic
test spinor psi = (f(x,y,z), g(x,y,z)) with sympy Function lapses, vector fields and strains.

For bilinears F_A = int chibar A chi with {chi, chibar} = -i:  {F_A, F_B} = -i int chibar [A, B] chi, and F_A = F_B for all
chi iff A = B as operators.  With G_f[xi] = lam_f int chibar (i L_xi) chi:
    {C_f[N], G_f[xi]} = lam_f int chibar [h_N, L_xi] chi,
    {C_f^(1)[N], lam1 G1[xi]} = C_f^(1)[N] with h -> lam1 (d_i xi_j + d_j xi_i)      (G1 = int P (d xi + d xi^T)).
Checks (each an exact operator identity on the test spinor):
  O1  [h_N, h_M] = i... : {C_f[N], C_f[M]} = v^2 int chibar i L^K_w chi, w = N dM - M dN, Kosmann spin term +i/4 curl w.sigma
  O2  lam_f [h_N, L^K_xi] + h^(1)_N[h -> lam1 2 sym d xi] = h_{N'}  iff  a_s lam1 = lam_f, N' = -lam_f xi.dN, solved for
      a_s, s1, s2 and the Kosmann spin coefficient
  O3  antisymmetric frame: h_N[1 + A] - h_N[1] = -i [h_N, (i/2) theta.sigma]... + N div(theta)/2 (walker's rotation defect)
"""
import sympy as sp

x = sp.symbols("x0:3", real=True)
I = sp.I
sig = [sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -I], [I, 0]]), sp.Matrix([[1, 0], [0, -1]])]
one = sp.eye(2)
f, g = sp.Function("f")(*x), sp.Function("g")(*x)
psi = sp.Matrix([f, g])
Nf, Mf = sp.Function("N")(*x), sp.Function("M")(*x)
xi = [sp.Function(f"xi{k}")(*x) for k in range(3)]
th = [sp.Function(f"th{k}")(*x) for k in range(3)]
hm = sp.Matrix(3, 3, lambda i, j: sp.Function(f"h{min(i, j)}{max(i, j)}")(*x))
RES = {"pass": 0, "fail": 0}


def check(tag, ok, msg):
    RES["pass" if ok else "fail"] += 1
    print(("PASS" if ok else "FAIL") + f": {tag} {msg}", flush=True)


def d(e, k):
    return e.applyfunc(lambda z: sp.diff(z, x[k])) if isinstance(e, sp.MatrixBase) else sp.diff(e, x[k])


def hN(Lp, E, ps, v=1):
    """h_N psi = 1/2 {Lp E_aj sigma_a, p_j} psi, p = -i d."""
    out = sp.zeros(2, 1)
    for a in range(3):
        for j in range(3):
            c = Lp * E[a, j]
            out += v * (-I / 2) * (c * sig[a] * d(ps, j) + d(c * sig[a] * ps, j))
    return out.applyfunc(sp.expand)


def LK(vec, ps, spin):
    """Kosmann-class transport on half-densities: (vec.d + div vec / 2 + spin * i curl vec . sigma) psi."""
    div = sum(sp.diff(vec[k], x[k]) for k in range(3))
    curl = [sum(sp.LeviCivita(c, k, j) * sp.diff(vec[j], x[k]) for k in range(3) for j in range(3)) for c in range(3)]
    out = sum((vec[k] * d(ps, k) for k in range(3)), sp.zeros(2, 1)) + div / 2 * ps
    out += spin * I * sum((curl[c] * sig[c] for c in range(3)), sp.zeros(2, 2)) * ps
    return out.applyfunc(sp.expand)


def zero(m):
    return all(sp.expand(z) == 0 for z in m)


# O1 flat walker algebra: -i [h_N, h_M] must equal v^2 i L^K_w  => [h_N, h_M] = -v^2 L^K_w
E0 = sp.eye(3)
w = [sp.expand(Nf * sp.diff(Mf, x[k]) - Mf * sp.diff(Nf, x[k])) for k in range(3)]
comm = (hN(Nf, E0, hN(Mf, E0, psi)) - hN(Mf, E0, hN(Nf, E0, psi))).applyfunc(sp.expand)
res = {sg: zero(comm + LK(w, psi, sg * sp.Rational(1, 4))) for sg in (1, -1)}
check("O1", res == {1: True, -1: False}, f"[h_N, h_M] = -L^K_w with spin coefficient +i/4 curl w.sigma (i.e. -1/4 curl w.s "
      f"in the bilinear, as in c4b T0b): {res}")

# O2 order chi chi {C,G}: unknown a_s, s1, s2, spin coefficient kap; lam1, lam_f symbolic
lam1, lf = sp.symbols("lam1 lam_f", positive=True)
aS, s1, s2, kap = sp.symbols("a_s s1 s2 kap", real=True)
lhs = lf * (hN(Nf, E0, LK(xi, psi, kap)) - LK(xi, hN(Nf, E0, psi), kap))
dh = sp.Matrix(3, 3, lambda i, j: lam1 * (sp.diff(xi[j], x[i]) + sp.diff(xi[i], x[j])))
E1 = -aS * dh / 2                     # first-order part of (delta + a_s h)^(-1/2) at h -> delta h
lhs += hN(Nf, E1, psi)
Np = s1 * sum(xi[k] * sp.diff(Nf, x[k]) for k in range(3)) + s2 * Nf * sum(sp.diff(xi[k], x[k]) for k in range(3))
resid = (lhs - hN(Np, E0, psi)).applyfunc(sp.expand)
# collect coefficients of all derivative monomials of the test and parameter functions
eqs = []
for comp in resid:
    comp = sp.expand(comp)
    atoms = [a_ for a_ in comp.atoms(sp.Derivative) | {f, g, Nf} | set(xi)]
    gens = sorted(set(atoms), key=str)
    P = sp.Poly(comp, *gens)
    for _, c in P.terms():
        c = sp.expand(c)
        if c != 0:
            eqs += [sp.re(c), sp.im(c)]
eqs = [e for e in (sp.expand(e) for e in eqs) if e != 0]
sol = sp.solve(eqs, [aS, s1, s2, kap], dict=True)
check("O2", sol == [{aS: lf / lam1, s1: -lf, s2: 0, kap: sp.Rational(1, 4)}],
      f"operator route, order chi chi: lam_f [h_N, L_xi] + h^(1)_N[h -> lam1 (d xi + d xi^T)] = h_(N') iff "
      f"a_s = lam_f/lam1, s1 = -lam_f, s2 = 0 and the Kosmann spin coefficient (+i/4): {sol}")

# O3 antisymmetric frame part: h_N[A] - (-i)[h_N, (1/2)(theta.s generator)]: the bilinear bracket {C_f, 1/2 int theta.s}
#    = -i int chibar [h_N, theta.sigma/2] chi; claim  h_N[A] = -i [h_N, theta.sigma/2] + N div(theta)/2
A = sp.Matrix(3, 3, lambda a, j: sum(sp.LeviCivita(a, j, k) * th[k] for k in range(3)))
ths = sum((th[c] * sig[c] for c in range(3)), sp.zeros(2, 2)) / 2
rot = (-I * (hN(Nf, E0, ths * psi) - ths * hN(Nf, E0, psi))).applyfunc(sp.expand)
divth = sum(sp.diff(th[k], x[k]) for k in range(3))
ok3 = zero(hN(Nf, A, psi) - rot - Nf * divth / 2 * psi)
ok3b = not zero(hN(Nf, A, psi) - rot)
check("O3", ok3 and ok3b, "operator route: h_N[E = 1 + A] - h_N[1] = -i[h_N, theta.sigma/2] + N div(theta)/2 exactly; the "
      "scalar remainder is nonzero (the walker is not locally rotation covariant; c4b G1)")
print(f"TOTAL: PASS={RES['pass']} FAIL={RES['fail']}")
