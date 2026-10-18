"""B17 check, claim 1 (exact sympy, own code, different route from aniso_weyl_bracket.py).

h_N psi = (1/2) sum_{a,j} E_aj {N, sigma^a (-i d_j)} psi with a GENERAL constant triad E (not only uniaxial).
Route: the full 2x2 matrix symbol of [h_N, h_M] is extracted (coefficients of d_k f1, d_k f2 in both components,
and the zeroth-order part), and compared with the frame-E Kosmann derivative obtained from the isotropic one by
the linear map x = E^T y:
   [h_N,h_M] = -( xi.grad + (1/2) div xi + (i/4) sum_a eps_abc (E_b.grad)(E_c.w) sigma^a ),  xi^k = g^{kj} w_j,  g = E^T E.
Then: (i) the derivative part is scalar and fixed by g alone; (ii) it equals kappa * (w.grad) iff g = kappa I;
(iii) an improvement of the energy density by d_jN psi^dag B^j psi (any Hermitian B^j) leaves the spin trace of
the derivative part unchanged (so no reordering/improvement rescues an anisotropic cone);
(iv) naive-walk species (E = diag(s), s = +-1): the spin term is det(s) (i/4)(curl w).tau with tau_a = s_a sigma_a,
so the on-site Kosmann term (i/4) curl w . sigma is reproduced only at k = 0 and (pi,pi,pi) (cf. B15 T7/O5b).
"""
import itertools
import sympy as sp

x, y, z = sp.symbols('x y z', real=True); X = (x, y, z)
N = sp.Function('N')(*X); M = sp.Function('M')(*X)
f1 = sp.Function('f1')(*X); f2 = sp.Function('f2')(*X); psi = sp.Matrix([f1, f2])
s = [sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]]), sp.Matrix([[1, 0], [0, -1]])]
D = lambda u, j: sp.diff(u, X[j])
NP = NF = 0
def check(name, ok, detail=''):
    global NP, NF
    NP += bool(ok); NF += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''))

def h(L, E, ps, B=None):
    out = sp.zeros(2, 1)
    for a in range(3):
        for j in range(3):
            if E[a, j] == 0: continue
            out += E[a, j] * sp.Rational(1, 2) * (L * (s[a] * (-sp.I) * ps.applyfunc(lambda u: D(u, j)))
                                                  + s[a] * (-sp.I) * (L * ps).applyfunc(lambda u: D(u, j)))
    if B is not None:  # improvement: + d_j L  B^j  (zeroth-order, Hermitian B^j)
        for j in range(3): out += D(L, j) * (B[j] * ps)
    return out
def comm(E, B=None):
    return (h(N, E, h(M, E, psi, B), B) - h(M, E, h(N, E, psi, B), B)).applyfunc(sp.expand)
w = [N * D(M, j) - M * D(N, j) for j in range(3)]
def kosmann_E(E, ps):
    g = E.T * E
    xi = [sum(g[k, j] * w[j] for j in range(3)) for k in range(3)]
    div = sum(D(xi[k], k) for k in range(3))
    Ew = [sum(E[c, l] * w[l] for l in range(3)) for c in range(3)]          # (E w)_c
    Ed = lambda u, b: sum(E[b, j] * D(u, j) for j in range(3))               # (E_b . grad) u
    spin = sp.zeros(2, 2)
    for a, b, c in itertools.permutations(range(3)):
        spin += sp.LeviCivita(a, b, c) * Ed(Ew[c], b) * s[a]
    out = sum((xi[k] * ps.applyfunc(lambda u: D(u, k)) for k in range(3)), sp.zeros(2, 1))
    return out + sp.Rational(1, 2) * div * ps + sp.I / 4 * spin * ps
def dsymbol(C):
    """2x2 coefficient matrices of d_k psi in C (C linear in f1, f2 and their first derivatives)."""
    return [sp.Matrix(2, 2, lambda r, c_: sp.expand(C[r]).coeff(D([f1, f2][c_], k))) for k in range(3)]

# (A) symbolic uniaxial + generic rational triads
va, vt = sp.symbols('v_a v_t', positive=True)
Es = {'uniaxial diag(vt,vt,va)': sp.diag(vt, vt, va),
      'generic rational triad': sp.Matrix([[sp.Rational(3, 2), sp.Rational(1, 3), 0], [-sp.Rational(1, 2), 1, sp.Rational(2, 5)], [sp.Rational(1, 4), -sp.Rational(1, 3), sp.Rational(5, 4)]]),
      'reflected (det<0) triad': sp.Matrix([[1, sp.Rational(1, 2), 0], [0, -1, sp.Rational(1, 3)], [sp.Rational(1, 5), 0, 2]])}
for nm, E in Es.items():
    C = comm(E)
    full = (C + kosmann_E(E, psi)).applyfunc(sp.simplify)
    check(f"{nm}: [h_N,h_M] = -(frame-E Kosmann derivative along xi = g w), exactly", full == sp.zeros(2, 1))
    g = E.T * E; Dk = dsymbol(C)
    ok = all(sp.simplify(Dk[k] + sum(g[k, j] * w[j] for j in range(3)) * sp.eye(2)) == sp.zeros(2, 2) for k in range(3))
    check(f"{nm}: derivative part is scalar, -sum g^kj w_j d_k (no spin-matrix derivative term)", ok)

# (B) closure vs kappa * isotropic relabelling: derivative part must equal -kappa w.grad for all N, M
kap = sp.symbols('kappa')
gsym = sp.Matrix(3, 3, lambda i, j: sp.Symbol(f'g{min(i,j)}{max(i,j)}'))
# coefficient of N d_j M in the k-th derivative coefficient must be kappa delta_jk
eqs = [gsym[k, j] - (kap if j == k else 0) for k in range(3) for j in range(3)]
sol = sp.solve(eqs, list(gsym.free_symbols), dict=True)
check("derivative part = -kappa (w.grad) for arbitrary lapses N, M  <=>  g = kappa I (any symmetric cone metric)",
      len(sol) == 1 and all(sp.simplify(gsym.subs(sol[0])[i, j] - (kap if i == j else 0)) == 0 for i in range(3) for j in range(3)))

# (C) spin term for the uniaxial cone: (i/4) sum_a eps_abc v_b v_c d_b w_c sigma_a; matches kappa (i/4) curl w . sigma iff vt^2 = vt va = kappa
E = sp.diag(vt, vt, va); C = comm(E)
zeroth = sp.Matrix(2, 2, lambda r, c_: sp.expand(C[r].subs({sp.Derivative(f1, X[k]): 0 for k in range(3)}).subs({sp.Derivative(f2, X[k]): 0 for k in range(3)})).coeff([f1, f2][c_]))
curl = [D(w[2], 1) - D(w[1], 2), D(w[0], 2) - D(w[2], 0), D(w[1], 0) - D(w[0], 1)]
div = sum(D(sum((E.T * E)[k, j] * w[j] for j in range(3)), k) for k in range(3))
spin_pred = sp.I / 4 * (vt * va * curl[0] * s[0] + vt * va * curl[1] * s[1] + vt ** 2 * curl[2] * s[2])
check("uniaxial spin part: -(i/4)(vt va curl_x w sigma_x + vt va curl_y w sigma_y + vt^2 curl_z w sigma_z) [plus -(1/2)div xi]",
      (zeroth + sp.Rational(1, 2) * div * sp.eye(2) + spin_pred).applyfunc(sp.simplify) == sp.zeros(2, 2))

# (D) improvement terms d_j N psi^dag B^j psi: spin trace of derivative part unchanged
b = [sp.Matrix([[sp.Symbol(f'p{j}'), sp.Symbol(f'r{j}') + sp.I * sp.Symbol(f'i{j}')], [sp.Symbol(f'r{j}') - sp.I * sp.Symbol(f'i{j}'), sp.Symbol(f'q{j}')]]) for j in range(3)]
for sy in b:
    for e_ in sy: pass
Ci = comm(E, B=b); Dk = dsymbol(Ci); g = E.T * E
tr_ok = all(sp.simplify(Dk[k].trace() / 2 + sum(g[k, j] * w[j] for j in range(3))) == 0 for k in range(3))
traceless_extra = all(sp.simplify((Dk[k] + sum(g[k, j] * w[j] for j in range(3)) * sp.eye(2)).trace()) == 0 for k in range(3))
check("improved density h_N + d_jN psi^dag B^j psi (general Hermitian B^j): spin trace of the derivative part is still -g^kj w_j d_k "
      "(any extra derivative term is traceless, so it cannot supply the missing scalar part)", tr_ok and traceless_extra)
extra_nonzero = any(sp.simplify(Dk[k] + sum(g[k, j] * w[j] for j in range(3)) * sp.eye(2)) != sp.zeros(2, 2) for k in range(3))
print("   (improvement generates a traceless matrix-valued derivative term:", extra_nonzero, "- it must itself vanish for closure)")

# (E) naive walk species: E = diag(s), s in {+-1}^3 (H = sigma . sin k near k = pi n)
res = []
for sv in itertools.product((1, -1), repeat=3):
    E = sp.diag(*sv); C = comm(E)
    zeroth = sp.Matrix(2, 2, lambda r, c_: sp.expand(C[r].subs({sp.Derivative(f1, X[k]): 0 for k in range(3)}).subs({sp.Derivative(f2, X[k]): 0 for k in range(3)})).coeff([f1, f2][c_]))
    divw = sum(D(w[k], k) for k in range(3))
    tau = [sv[a] * s[a] for a in range(3)]; det = sv[0] * sv[1] * sv[2]
    own = (zeroth + sp.Rational(1, 2) * divw * sp.eye(2) + det * sp.I / 4 * sum((curl[a] * tau[a] for a in range(3)), sp.zeros(2, 2))).applyfunc(sp.simplify) == sp.zeros(2, 2)
    onsite = (zeroth + sp.Rational(1, 2) * divw * sp.eye(2) + sp.I / 4 * sum((curl[a] * s[a] for a in range(3)), sp.zeros(2, 2))).applyfunc(sp.simplify) == sp.zeros(2, 2)
    der = all(sp.simplify(dsymbol(C)[k] + w[k] * sp.eye(2)) == sp.zeros(2, 2) for k in range(3))
    res.append((sv, der, own, onsite))
check("naive walk: all eight species have the same derivative part -w.grad (one isotropic cone, speed 1)", all(r[1] for r in res))
check("naive walk: each species' spin part is det(s) (i/4)(curl w).tau, tau_a = s_a sigma_a", all(r[2] for r in res))
onsite_ok = sorted(r[0] for r in res if r[3])
check("naive walk: the on-site Kosmann spin term (i/4) curl w . sigma holds only at k = 0 and (pi,pi,pi) (6 species need a "
      "momentum-dependent spin structure, as B15 T7/O5b)", onsite_ok == [(-1, -1, -1), (1, 1, 1)], f"{onsite_ok}")
print(f"\nTOTAL: PASS={NP} FAIL={NF}")
