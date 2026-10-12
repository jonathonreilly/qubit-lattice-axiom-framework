"""C5 R12-6, script 6: symbolic operator check of the equivariant supercharge on a minimal gauged toy (Schroedinger rep).
Toy: two link coordinates a1,a2 (gauge shift v = (1,1)), one charged site phi = (f1,f2) (v = e J phi, J = [[0,-1],[1,0]]),
complex sigma (s, sb as Wirtinger-independent coordinates), fermions psi_{a1}, psi_{a2}, psi_{f1}, psi_{f2}, eta (32-dim Fock).
W = (g/2)(a1-a2)^2 + h (a1-a2)(f1^2+f2^2) + (mu/2)(f1^2+f2^2)  (gauge invariant: v.dW = 0).
  Q   = sum_a psi_a^+ (p_a - i d_aW) + i s (v.psi) + c eta pi_sb,      p = -i d,  pi_sb = -i d_sb,  pi_s = -i d_s
  Q^+ = sum_a psi_a (p_a + i d_aW) - i sb (v.psi^+) + c eta^+ pi_s       (c real)
Checks on generic test states (undefined functions of all six coordinates in several Fock components):
  (1) Q^2 = i s L,   L = v.p - i sum_ab psi_a^+ (d_a v_b) psi_b        [hand algebra, report 3.1 step 1]
  (2) {Q,Q^+} = p^2 + |dW|^2 + 2 psi^+ HessW psi - tr HessW + |s|^2 |v|^2 ... compared term by term with the expected
      operator H2 := {Q,Q^+} computed from the listed pieces (report 3.1 step 3), including the eta hopping c (v.psi^+) eta + h.c.
      and the sigma pairing -sb sum (d_a v_b) psi_a^+ psi_b^+ + h.c.  (here pi_s pi_sb kinetic: c^2 pi_sb pi_s).
"""
import sympy as sp, itertools, random
a1, a2, f1, f2, s, sb, e, g, h, mu, c = sp.symbols('a1 a2 f1 f2 s sb e g h mu c')
X = [a1, a2, f1, f2]
W = g / 2 * (a1 - a2) ** 2 + h * (a1 - a2) * (f1 ** 2 + f2 ** 2) + mu / 2 * (f1 ** 2 + f2 ** 2)
v = [sp.Integer(1), sp.Integer(1), -e * f2, e * f1]
assert sp.simplify(sum(v[i] * sp.diff(W, X[i]) for i in range(4))) == 0
NF = 5  # fermion modes: 0..3 = psi_x, 4 = eta
I = sp.I

# states: dict bitstring(tuple) -> expr
def add(st, key, val):
    st[key] = st.get(key, 0) + val
def cdag(mode, st):
    out = {}
    for key, val in st.items():
        if key[mode] == 1:
            continue
        sign = (-1) ** sum(key[:mode])
        nk = list(key); nk[mode] = 1
        add(out, tuple(nk), sign * val)
    return out
def ann(mode, st):
    out = {}
    for key, val in st.items():
        if key[mode] == 0:
            continue
        sign = (-1) ** sum(key[:mode])
        nk = list(key); nk[mode] = 0
        add(out, tuple(nk), sign * val)
    return out
def mul(fn, st):  # bosonic operator fn: expr -> expr, applied componentwise
    return {k: fn(vv) for k, vv in st.items()}
def plus(*sts):
    out = {}
    for st in sts:
        for k, vv in st.items():
            add(out, k, vv)
    return out
def scal(a, st):
    return {k: a * vv for k, vv in st.items()}
p = lambda x: (lambda f: -I * sp.diff(f, x))

def Qop(st):
    terms = []
    for i, x in enumerate(X):
        Gi = lambda f, x=x: -I * sp.diff(f, x) - I * sp.diff(W, x) * f
        terms.append(cdag(i, mul(Gi, st)))
    terms.append(scal(I * s, plus(*[mul(lambda f, i=i: v[i] * f, ann(i, st)) for i in range(4)])))
    terms.append(scal(c, ann(4, mul(lambda f: -I * sp.diff(f, sb), st))))
    return plus(*terms)

def Qdag(st):
    terms = []
    for i, x in enumerate(X):
        Gi = lambda f, x=x: -I * sp.diff(f, x) + I * sp.diff(W, x) * f
        terms.append(ann(i, mul(Gi, st)))
    terms.append(scal(-I * sb, plus(*[mul(lambda f, i=i: v[i] * f, cdag(i, st)) for i in range(4)])))
    terms.append(scal(c, cdag(4, mul(lambda f: -I * sp.diff(f, s), st))))
    return plus(*terms)

dv = [[sp.diff(v[b], X[a]) for b in range(4)] for a in range(4)]   # dv[a][b] = d_a v_b
def Lop(st):
    t1 = plus(*[mul(lambda f, i=i: v[i] * (-I) * sp.diff(f, X[i]), st) for i in range(4)])
    t2 = {}
    for a in range(4):
        for b in range(4):
            if dv[a][b] != 0:
                t2 = plus(t2, scal(-I * dv[a][b], cdag(a, ann(b, st))))
    return plus(t1, t2)

def is_zero(st):
    return all(sp.expand(vv) == 0 for vv in st.values())

random.seed(5)
keys = list(itertools.product((0, 1), repeat=NF))
test = {}
for kk in random.sample(keys, 6):
    test[kk] = sp.Function('F%s' % ''.join(map(str, kk)))(a1, a2, f1, f2, s, sb)
QQ = Qop(Qop(test))
diff1 = plus(QQ, scal(-I * s, Lop(test)))
print('(1) Q^2 - i s L on a generic 6-component test state: identically zero ->', is_zero(diff1))

# (2) expected {Q,Q^+} from the listed pieces
def Hexp(st):
    terms = []
    for i, x in enumerate(X):
        terms.append(mul(lambda f, x=x: -sp.diff(f, x, 2) + sp.diff(W, x) ** 2 * f, st))
    Hess = [[sp.diff(W, X[a], X[b]) for b in range(4)] for a in range(4)]
    for a in range(4):
        for b in range(4):
            if Hess[a][b] != 0:
                terms.append(scal(2 * Hess[a][b], cdag(a, ann(b, st))))
    terms.append(scal(-sum(Hess[a][a] for a in range(4)), st))
    vv = sum(v[i] ** 2 for i in range(4))
    terms.append(mul(lambda f: s * sb * vv * f, st))                                   # |sigma|^2 |v|^2
    terms.append(scal(c ** 2, mul(lambda f: -sp.diff(f, s, sb), st)))                  # c^2 pi_sb pi_s
    # eta hopping: c (v.psi^+) eta + c eta^+ (v.psi)
    terms.append(scal(c, plus(*[mul(lambda f, i=i: v[i] * f, cdag(i, ann(4, st))) for i in range(4)])))
    terms.append(scal(c, plus(*[mul(lambda f, i=i: v[i] * f, cdag(4, ann(i, st))) for i in range(4)])))
    # sigma pairing: -sb sum_ab (d_a v_b) psi_a^+ psi_b^+  and  -s sum_ab (d_a v_b) psi_b psi_a
    for a in range(4):
        for b in range(4):
            if dv[a][b] != 0:
                terms.append(scal(-sb * dv[a][b], cdag(a, cdag(b, st))))
                terms.append(scal(-s * dv[a][b], ann(b, ann(a, st))))
    return plus(*terms)

anti = plus(Qop(Qdag(test)), Qdag(Qop(test)))
diff2 = plus(anti, scal(-1, Hexp(test)))
print('(2) {Q,Q^+} - (listed H pieces x 2) on the same test state: identically zero ->', is_zero(diff2))
if not is_zero(diff2):
    for k, vv in diff2.items():
        ex = sp.simplify(vv)
        if ex != 0:
            print('   residual in component', k, ':', ex)

# ---- negative controls (must FAIL): wrong eta-hopping coefficient; Q without the sigma term; sizes of the states
print('    sizes: test components %d, Q^2 components %d, {Q,Q+} components %d' % (len(test), len(QQ), len(anti)))
bad = plus(anti, scal(-1, Hexp(test)), scal(sp.Rational(1, 2) * c, plus(*[mul(lambda f, i=i: v[i] * f, cdag(i, ann(4, test))) for i in range(4)])))
print('    control A (eta hopping coefficient off by c/2) gives zero? ->', is_zero(bad))
def Qnos(st):
    return plus(Qop(st), scal(-1, scal(I * s, plus(*[mul(lambda f, i=i: v[i] * f, ann(i, st)) for i in range(4)]))))
print('    control B (Q without the i s v.psi term): Q^2 - i s L zero? ->', is_zero(plus(Qnos(Qnos(test)), scal(-I * s, Lop(test)))),
      '; Q^2 itself zero? ->', is_zero(Qnos(Qnos(test))))
