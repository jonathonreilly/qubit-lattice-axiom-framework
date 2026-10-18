#!/usr/bin/env python3
"""Fresh-context reviewer check (own code) of N1, N2, Y8, Y9 of
scripts/curvature_member_closure_spin_half_and_spin_one_common_cone_2026_10_18.py.

Different route from the runner:
 N1: no jet engine / Euler operators. A linear-in-momentum generator G[xi] = int p . V_xi(q) has
     {G[xi], G[eta]} = int p . (DV_xi[V_eta] - DV_eta[V_xi]) (convention {q, p} = +1). We compute this
     field-space commutator directly with sympy Functions for gravity V_xi(h) = L_xi h + lam1 L_xi delta
     (affine), a scalar V_xi(phi) = xi.grad phi, Maxwell V_xi(A) = L_xi A (one-form), with weights.
     Also the matrix generalisation: lam1 delta -> constant symmetric g0 (anisotropic background).
 N2: polynomial (cubic) vector fields with symbolic coefficients instead of sympy Functions; spinor
     components as generic Functions.
 Y8: direct with generic cubic fields.
 Y9: full octahedral group O_h (48 elements) and the rotation group O (24), enumerated.
"""
import itertools
import sympy as sp

X = sp.symbols("x0:3")
I = sp.I
SIG = [sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -I], [I, 0]]), sp.Matrix([[1, 0], [0, -1]])]
res = {}
_set = dict.__setitem__
class R(dict):
    def __setitem__(self, k, v):
        print(f"[{'PASS' if v else 'FAIL'}] {k}", flush=True); _set(self, k, v)
res = R()


def D(f, k):
    return sp.diff(f, X[k])


def lie_br(u, v):
    return [sum(u[k] * D(v[i], k) - v[k] * D(u[i], k) for k in range(3)) for i in range(3)]


def zero(e):
    return sp.expand(e) == 0


# ---------------------------------------------------------------- N1 (field-space commutator route)
xi = [sp.Function(f"a{k}")(*X) for k in range(3)]
et = [sp.Function(f"b{k}")(*X) for k in range(3)]
br = lie_br(xi, et)
h = [[sp.Function(f"h{min(i,j)}{max(i,j)}")(*X) for j in range(3)] for i in range(3)]
g0s = sp.Matrix(3, 3, lambda i, j: sp.Symbol(f"g{min(i,j)}{max(i,j)}"))
lam1 = sp.Symbol("lam1")


def lie_tensor(u, T):  # Lie derivative of a covariant symmetric 2-tensor (T as nested list/expr)
    return [[sum(u[k] * D(T[i][j], k) + T[k][j] * D(u[k], i) + T[i][k] * D(u[k], j) for k in range(3))
             for j in range(3)] for i in range(3)]


def V_grav(u, H, g0):  # affine: L_u H + L_u g0 (g0 constant)
    LH = lie_tensor(u, H)
    Lg = lie_tensor(u, [[g0[i, j] for j in range(3)] for i in range(3)])
    return [[LH[i][j] + Lg[i][j] for j in range(3)] for i in range(3)]


def DV_grav(u, dH):  # derivative of the affine map in direction dH (linear part only)
    return lie_tensor(u, dH)


# {G[xi],G[eta]} density coefficient of p:  DV_xi[V_eta] - DV_eta[V_xi]
for label, g0 in (("lam1*delta", lam1 * sp.eye(3)), ("constant symmetric g0", g0s)):
    Ve, Vx = V_grav(et, h, g0), V_grav(xi, h, g0)
    comm = [[DV_grav(xi, Ve)[i][j] - DV_grav(et, Vx)[i][j] for j in range(3)] for i in range(3)]
    target = V_grav(br, h, g0)
    res[f"N1 gravity affine action closes, nu = 1, for any {label}"] = all(
        zero(comm[i][j] - target[i][j]) for i in range(3) for j in range(3))
# scalar (weight 0) and Maxwell one-form
phi = sp.Function("phi")(*X)
Vs = lambda u, f: sum(u[k] * D(f, k) for k in range(3))
res["N1 scalar: [V_xi, V_eta] = V_[xi,eta]"] = zero(Vs(xi, Vs(et, phi)) - Vs(et, Vs(xi, phi)) - Vs(br, phi))
A = [sp.Function(f"A{k}")(*X) for k in range(3)]
Vm = lambda u, a: [sum(u[k] * D(a[i], k) + a[k] * D(u[k], i) for k in range(3)) for i in range(3)]
res["N1 Maxwell one-form: [V_xi, V_eta] = V_[xi,eta]"] = all(
    zero(Vm(xi, Vm(et, A))[i] - Vm(et, Vm(xi, A))[i] - Vm(br, A)[i]) for i in range(3))
# Weighted total: sectors are independent fields, so {G,G} = lam1 G1[[.,.]] + G2[[.,.]] + lm^2 Gm + la^2 GA.
# Requiring = G[nu [xi,eta]] for one nu: G2 coefficient gives nu = 1, G1 coefficient lam1 = nu lam1 (free),
# matter lm^2 = nu lm -> lm in {0,1}. (Solve this tiny system.)
lm, la, nu = sp.symbols("lm la nu")
sol = sp.solve([1 - nu, lam1 - nu * lam1, lm ** 2 - nu * lm, la ** 2 - nu * la], [nu, lm, la], dict=True)
res["N1 weights: lam_m, lam_A in {0,1}, nu = 1, lam1 free"] = (
    len(sol) == 4 and all(s[nu] == 1 and s[lm] in (0, 1) and s[la] in (0, 1) for s in sol))

# ---------------------------------------------------------------- N2 (polynomial vector fields)
cx = sp.symbols("p0:30")
ce = sp.symbols("q0:30")
monos = [m for d in range(4) for m in itertools.combinations_with_replacement(X, d)]
monos = [sp.Mul(*m) for m in monos][:10]  # 1, x, xx (generic 2-jets: the identity involves at most second derivatives of xi, eta)
xp = [sum(cx[10 * i + k] * monos[k] for k in range(10)) for i in range(3)]
ep = [sum(ce[10 * i + k] * monos[k] for k in range(10)) for i in range(3)]
psi = sp.Matrix([sp.Function("u1")(*X), sp.Function("u2")(*X)])


def curl(u):
    return [D(u[2], 1) - D(u[1], 2), D(u[0], 2) - D(u[2], 0), D(u[1], 0) - D(u[0], 1)]


def Kos(u, ps):
    dv = sum(D(u[k], k) for k in range(3))
    cu = curl(u)
    out = sp.zeros(2, 1)
    for k in range(3):
        out += u[k] * ps.diff(X[k])
    out += dv / 2 * ps
    for k in range(3):
        out += I / 4 * cu[k] * (SIG[k] * ps)
    return out


brp = lie_br(xp, ep)
rem = (Kos(xp, Kos(ep, psi)) - Kos(ep, Kos(xp, psi)) - Kos(brp, psi)).applyfunc(sp.expand)
Sx = sp.Matrix(3, 3, lambda i, j: (D(xp[j], i) + D(xp[i], j)) / 2)
Se = sp.Matrix(3, 3, lambda i, j: (D(ep[j], i) + D(ep[i], j)) / 2)
P = Sx * Se
om = [sum(sp.LeviCivita(k, i, j) * P[i, j] for i in range(3) for j in range(3)) for k in range(3)]
pred = (-I / 2) * sum((om[k] * SIG[k] for k in range(3)), sp.zeros(2, 2)) * psi
res["N2 [L_xi,L_eta] - L_[xi,eta] = -(i/2) eps_kij (S_xi S_eta)_ij sigma_k (generic quadratic polynomial fields)"] = (
    (rem - pred).applyfunc(sp.expand) == sp.zeros(2, 1))
# sign control: the opposite sign must fail
res["N2 sign control (+i/2 fails)"] = (rem + pred).applyfunc(sp.expand) != sp.zeros(2, 1)
# remainder has no derivative of psi (on-site) and vanishes for conformal Killing xi
res["N2 remainder is on-site (no d psi)"] = all(sp.expand(rem[r]).coeff(sp.Derivative(psi[c], X[k])) == 0
                                             for r in range(2) for c in range(2) for k in range(3))
# conformal Killing: xi = b x - (x.x) b/... use special conformal  xi = 2 (b.x) x - (x.x) b,  and dilation, rotation
bv = sp.symbols("c0:3")
xx = sum(X[k] ** 2 for k in range(3))
bx = sum(bv[k] * X[k] for k in range(3))
sct = [2 * bx * X[k] - xx * bv[k] for k in range(3)]
remc = (Kos(sct, Kos(ep, psi)) - Kos(ep, Kos(sct, psi)) - Kos(lie_br(sct, ep), psi)).applyfunc(sp.expand)
res["N2 remainder vanishes also for a (non-Killing) conformal Killing field (special conformal)"] = remc == sp.zeros(2, 1)
dil = list(X)
remd = (Kos(dil, Kos(ep, psi)) - Kos(ep, Kos(dil, psi)) - Kos(lie_br(dil, ep), psi)).applyfunc(sp.expand)
res["N2 remainder vanishes for dilation"] = remd == sp.zeros(2, 1)
res["N2 remainder nonzero in general"] = rem != sp.zeros(2, 1)

# ---------------------------------------------------------------- Y8
Am = sp.Matrix(3, 3, lambda i, j: sp.Symbol(f"A{i}{j}"))
Ax, Ae = list(Am * sp.Matrix(xp)), list(Am * sp.Matrix(ep))
lhs = lie_br(Ax, Ae)
inner = [sum(Ax[k] * D(ep[i], k) - Ae[k] * D(xp[i], k) for k in range(3)) for i in range(3)]
rhs = list(Am * sp.Matrix(inner))
res["Y8 [A xi, A eta] = A((A xi).grad eta - (A eta).grad xi)"] = all(zero(lhs[i] - rhs[i]) for i in range(3))
# closure with gravity's structure [xi,eta]: need [A xi, A eta] = A [xi, eta] (gravity fixes the structure constant 1)
xl = [sum(cx[10 * i + k] * monos[k] for k in range(4)) for i in range(3)]
el = [sum(ce[10 * i + k] * monos[k] for k in range(4)) for i in range(3)]
lhsl = lie_br(list(Am * sp.Matrix(xl)), list(Am * sp.Matrix(el)))
rhsl = list(Am * sp.Matrix(lie_br(xl, el)))
eqs = []
for i in range(3):
    eqs += sp.Poly(sp.expand(lhsl[i] - rhsl[i]), *(list(X) + list(cx) + list(ce))).coeffs()
solA = sp.solve(eqs, list(Am), dict=True)
res["Y8 solutions of [A xi, A eta] = A[xi,eta]: A = 0 or A = I"] = sorted(str(sp.Matrix(3, 3, lambda i, j: Am[i, j].subs(s))) for s in solA) == sorted([str(sp.zeros(3, 3)), str(sp.eye(3))])

# ---------------------------------------------------------------- Y9 (enumerate O_h)
S = sp.Matrix(3, 3, lambda i, j: sp.Symbol(f"t{min(i,j)}{max(i,j)}"))
group = []
for perm in itertools.permutations(range(3)):
    for sg in itertools.product((1, -1), repeat=3):
        R = sp.zeros(3, 3)
        for i in range(3):
            R[i, perm[i]] = sg[i]
        group.append(R)
for name, G in (("O_h", group), ("O (det=+1)", [R for R in group if R.det() == 1])):
    eqs = []
    for R in G:
        eqs += list(R * S * R.T - S)
    sol = sp.solve(eqs, list(S.free_symbols), dict=True)
    Ss = S.subs(sol[0])
    res[f"Y9 {name} ({len(G)} elements): invariant symmetric 2-tensor is t*delta"] = Ss.is_diagonal() and Ss[0, 0] == Ss[1, 1] == Ss[2, 2] and len(Ss.free_symbols) == 1

npass = sum(bool(v) for v in res.values())
print(f"TOTAL {npass}/{len(res)}")
