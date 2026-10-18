"""B21 core: jet calculus (unmodified copy of B19's b19_jets.py) + a Fourier-kernel zero test on jets.

Reuse/independence: the jet calculus (D, Euler operator, bracket) is B19's code COPIED (b19_jets_copy.py);
R1, R2 = [sqrt g R]^(1),(2) come from B19_check's independently built pickle (R12.pkl, copied) converted to jets.
The zero test is the B19_check idea (Fourier kernel on the momentum-conservation surface), re-implemented on jets.

Conventions (as B19 / B19_check):
  canonical pairs (h_ab, P_ab) over the 6 independent components a <= b;
  tensor momentum Pt^ij = P_ii (diagonal), P_ab/2 (off-diagonal): int Pt^ij W_ij (all i,j) = sum_comp P_ab W_ab;
  {F,G} = sum dF/dh dG/dP - dF/dP dG/dh ;  [xi,eta]^i = xi.d eta^i - eta.d xi^i ;
  G[xi] = lam1 G1[xi] + G2[xi],  G1 = int Pt^ij (d_i xi_j + d_j xi_i);
  C(N) = int N [kin0 + kin1 - K1 R1 - K2 R2].
"""
from __future__ import annotations
import itertools, os, pickle
import sympy as sp
from b19_jets_copy import J, D, euler, bracket, KEY

I = sp.I
R3 = range(3)
COMP = [(0, 0), (1, 1), (2, 2), (0, 1), (0, 2), (1, 2)]
HN = {ab: f"h{ab[0]}{ab[1]}" for ab in COMP}
PN = {ab: f"P{ab[0]}{ab[1]}" for ab in COMP}
CONJ = {HN[ab]: PN[ab] for ab in COMP}
XI = [J(f"xi{k}") for k in R3]
ETA = [J(f"eta{k}") for k in R3]
N = J("N")
M = J("M")


def h(i, j):
    return J(HN[(min(i, j), max(i, j))])


def Pt(i, j):
    ab = (min(i, j), max(i, j))
    return J(PN[ab]) if i == j else J(PN[ab]) / 2


trh = sum(h(k, k) for k in R3)
trP = sum(Pt(k, k) for k in R3)
trPP = sp.expand(sum(Pt(i, j) * Pt(j, i) for i in R3 for j in R3))
trhP = sp.expand(sum(h(i, j) * Pt(j, i) for i in R3 for j in R3))
trhPP = sp.expand(sum(h(i, j) * Pt(j, k) * Pt(k, i) for i in R3 for j in R3 for k in R3))


def d(f, k):
    return D(f, k)


def G1(xi):
    return sp.expand(sum(Pt(i, j) * (d(xi[j], i) + d(xi[i], j)) for i in R3 for j in R3))


def W_iso_terms(xi):
    """the 12-term isotropic one-derivative ansatz of B19_check's W_iso, transcribed to jets.  T1 + T2 = (L_xi h)_ij."""
    dx = lambda i, j: d(xi[j], i)            # d_i xi_j
    div = sum(dx(k, k) for k in R3)
    dh = lambda k, i, j: d(h(i, j), k)
    dtr = lambda k: d(trh, k)
    dl = lambda i, j: 1 if i == j else 0
    return [
        lambda i, j: sum(xi[k] * dh(k, i, j) for k in R3),
        lambda i, j: sum(h(i, k) * dx(j, k) + h(j, k) * dx(i, k) for k in R3),
        lambda i, j: sum(h(k, i) * dx(k, j) + h(k, j) * dx(k, i) for k in R3),
        lambda i, j: dl(i, j) * sum(h(k, l) * dx(k, l) for k in R3 for l in R3),
        lambda i, j: dl(i, j) * trh * div,
        lambda i, j: h(i, j) * div,
        lambda i, j: trh * (dx(i, j) + dx(j, i)),
        lambda i, j: dl(i, j) * sum(xi[k] * dtr(k) for k in R3),
        lambda i, j: sum(xi[k] * (dh(i, j, k) + dh(j, i, k)) for k in R3),
        lambda i, j: dl(i, j) * sum(xi[k] * dh(l, k, l) for k in R3 for l in R3),
        lambda i, j: xi[i] * dtr(j) + xi[j] * dtr(i),
        lambda i, j: sum(xi[i] * dh(k, k, j) + xi[j] * dh(k, k, i) for k in R3),
    ]


def G2_terms(xi):
    T = W_iso_terms(xi)
    return [sp.expand(sum(Pt(i, j) * T[n](i, j) for i in R3 for j in R3)) for n in range(12)]


def G2(xi, m):
    return sp.expand(sum(m[n] * t for n, t in enumerate(G2_terms(xi))))


def lie_vec(xi, eta):
    return [sp.expand(sum(xi[k] * d(eta[i], k) - eta[k] * d(xi[i], k) for k in R3)) for i in R3]


# ------------------------------------------------------------------ sqrt g R from B19_check's pickle, converted to jets
def _fun2jet(expr):
    X = sp.symbols("x0 x1 x2", real=True)

    def rep(dv):
        f = dv.expr.func.__name__
        al = [0, 0, 0]
        for v, n in dv.variable_count:
            al[X.index(v)] += n
        return J(f, tuple(al))
    e = sp.expand(expr).replace(lambda a: isinstance(a, sp.Derivative), rep)
    e = e.replace(lambda a: isinstance(a, sp.core.function.AppliedUndef), lambda a: J(a.func.__name__))
    return sp.expand(e)


def load_R12_jets(path=os.path.join(os.path.dirname(os.path.abspath(__file__)), "R12_jets.pkl")):
    if os.path.exists(path):
        out = pickle.load(open(path, "rb"))
        # re-register the unpickled jet symbols with the jet calculus (KEY is per-process)
        for ex in out:
            for s in ex.free_symbols:
                f, a = str(s).rsplit("_", 1)
                assert J(f, tuple(int(c) for c in a)) == s
        return out
    import grav_common
    here = os.path.dirname(os.path.abspath(__file__))
    R1f, R2f = grav_common.load_R12(os.path.join(here, "R12.pkl"))
    out = (_fun2jet(R1f), _fun2jet(R2f))
    pickle.dump(out, open(path, "wb"))
    return out


# ------------------------------------------------------------------ Fourier-kernel zero test on jets
def kernel(expr, slots):
    """slots: list of (name, [field names], mult).  Returns the polarised Fourier kernel of int expr restricted to the
    exact degree pattern (mult fields from each slot), on the momentum-conservation surface (last copy of last slot
    carries minus the sum).  Same-slot factors are summed over all assignments to the copies (polarisation)."""
    f2s = {f: s for s, (nm, fs, mu) in enumerate(slots) for f in fs}
    copies = [(s, r) for s, (nm, fs, mu) in enumerate(slots) for r in range(mu)]
    K = {c: sp.symbols(f"k_{slots[c[0]][0]}{c[1]}_0:3") for c in copies}
    A = {}

    def amp(f, r):
        if (f, r) not in A:
            A[(f, r)] = sp.Symbol(f"A_{f}_{r}")
        return A[(f, r)]
    out = []
    for term in sp.Add.make_args(sp.expand(expr)):
        coeff = 1
        facs = {s: [] for s in range(len(slots))}
        ok = True
        for b, e in term.as_powers_dict().items():
            if b in KEY:
                f, al = KEY[b]
                if f not in f2s:
                    ok = False
                    break
                facs[f2s[f]] += [(f, al)] * int(e)
            else:
                coeff *= b ** e
        if not ok or any(len(facs[s]) != slots[s][2] for s in facs):
            continue
        perslot = []
        for s in range(len(slots)):
            opts = []
            for perm in itertools.permutations(range(slots[s][2])):
                v = 1
                for (f, al), r in zip(facs[s], perm):
                    k = K[(s, r)]
                    v *= amp(f, r) * sp.Mul(*[(I * k[j]) ** al[j] for j in R3])
                opts.append(v)
            perslot.append(sp.Add(*opts))
        out.append(coeff * sp.Mul(*perslot))
    e = sp.expand(sp.Add(*out))
    last = K[copies[-1]]
    tot = [sum(K[c][j] for c in copies[:-1]) for j in R3]
    e = sp.expand(e.xreplace({last[j]: -tot[j] for j in R3}))
    gens = [x for c in copies[:-1] for x in K[c]] + list(A.values())
    return e, gens


def kernel_eqs(expr, slots):
    e, gens = kernel(expr, slots)
    if e == 0:
        return []
    return [sp.expand(c) for c in sp.Poly(e, *gens).coeffs() if sp.expand(c) != 0]


def is_zero(expr, slots):
    return len(kernel_eqs(expr, slots)) == 0


HS = ("h", list(HN.values()), 1)
HS2 = ("h", list(HN.values()), 2)
PS = ("P", list(PN.values()), 1)
PS2 = ("P", list(PN.values()), 2)
NS = ("N", ["N"], 1)
MS = ("M", ["M"], 1)
XS = ("xi", [f"xi{k}" for k in R3], 1)
ES = ("eta", [f"eta{k}" for k in R3], 1)
