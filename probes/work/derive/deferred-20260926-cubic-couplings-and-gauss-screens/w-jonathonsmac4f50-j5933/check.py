#!/usr/bin/env python3
"""Proper-cubic eleven-coupling extension (Codex campaign12h) and the five-versus-eleven classification of frozen #8569,
refereed with disjoint machinery.  J:derive:deferred-20260926-cubic-couplings-and-gauss-screens:a1

K1  species-space solve: real symmetric first-order symbols S(q) on the 15-state tangent (zero row sums), covariant
    P(Q) S(q) P(Q)^T = S(Qq), form a space of dimension 11 under the 24 proper signed permutations and 5 with inversion
    (exact nullspaces over QQ; no character sums).
K2  the author's eleven explicit maps (five of #8569 plus b1, b2, b_u, b_v, d, g) are covariant in orthonormal coordinates,
    independent (rank 11) hence exhaust the space; exactly the original five are inversion covariant.
K3  closure: raw-vector closure and raw Gauss preservation for arbitrary other moments each force a1=a2=u=v=b1=b2=b_u=b_v=0;
    derivative-curl closure forces only u=v=b_u=b_v=0 (polynomial identities in q, all coefficients at once).
K4  the (t | d1,d2,w) block is as displayed, with determinant -6 sqrt3 d^2 g q1 q2 q3; K5 reversal parities; K6 rank 10 with
    m, d, g != 0; K7 #8569's K K^T formula; K8 the species-current normalisation J' = (2/15) S.
"""
import time
T0 = time.time(); FAIL = []
def check(name, ok, detail=""):
    print(f"{'PASS' if ok else 'FAIL'} {name}" + (f" :: {detail}" if detail else ""), flush=True)
    if not ok: FAIL.append(name)
import itertools, sympy as sp
from sympy.polys.matrices import DomainMatrix
# labels: vacancy, 6 polar axis e, 8 axial cube b
labels = [('v', (0, 0, 0))]
for i in range(3):
    for s in (1, -1):
        e = [0, 0, 0]; e[i] = s; labels.append(('A', tuple(e)))
for b in itertools.product((1, -1), repeat=3): labels.append(('B', b))
lidx = {l: i for i, l in enumerate(labels)}
def signed_perms():
    out = []
    for perm in itertools.permutations(range(3)):
        for sg in itertools.product((1, -1), repeat=3):
            Q = sp.zeros(3, 3)
            for i in range(3): Q[i, perm[i]] = sg[i]
            out.append(Q)
    return out
G48 = signed_perms(); G24 = [Q for Q in G48 if Q.det() == 1]
def act(Q, l):
    t, x = l
    if t == 'v': return l
    v = Q*sp.Matrix(x)
    if t == 'B': v = Q.det()*v
    return (t, tuple(int(c) for c in v))
def P(Q):
    M = sp.zeros(15, 15)
    for l, i in lidx.items(): M[lidx[act(Q, l)], i] = 1
    return M
# orthonormal tangent observables (rows = observables, columns = species values)
def obs():
    rows = []
    for i in range(3): rows.append([sp.Integer(l[1][i]) if l[0] == 'A' else 0 for l in labels])          # e_i
    E = [[x/sp.sqrt(2) for x in r] for r in rows]
    s1 = [(4 if l[0] == 'A' else (-3 if l[0] == 'B' else 0))/sp.sqrt(168) for l in labels]
    s2 = [(14 if l[0] == 'v' else -1)/sp.sqrt(210) for l in labels]
    B = [[(sp.Integer(l[1][i]) if l[0] == 'B' else 0)/sp.sqrt(8) for l in labels] for i in range(3)]
    D1 = sp.diag(1, -1, 0)/sp.sqrt(2); D2 = sp.diag(1, 1, -2)/sp.sqrt(6)
    def eDe(D): return [((sp.Matrix(l[1]).T*D*sp.Matrix(l[1]))[0] if l[0] == 'A' else 0)/sp.sqrt(2) for l in labels]
    t = [[(l[1][i]*l[1][j] if l[0] == 'B' else 0)/sp.sqrt(8) for l in labels] for i, j in ((0, 1), (0, 2), (1, 2))]
    w = [(l[1][0]*l[1][1]*l[1][2] if l[0] == 'B' else 0)/sp.sqrt(8) for l in labels]
    return sp.Matrix(E + [s1, s2] + B + [eDe(D1), eDe(D2)] + t + [w])
U = obs()
q1, q2, q3 = sp.symbols('q1 q2 q3'); qv = sp.Matrix([q1, q2, q3])
# species-space solve: S_i symmetric 15x15, zero row sums; P S_i P^T = sum_j Q_ji S_j
pairs = [(a, b) for a in range(15) for b in range(a, 15)]
nv = 3*len(pairs)
def var(i, a, b):
    if a > b: a, b = b, a
    return i*len(pairs) + pairs.index((a, b))
def solve_space(gens):
    rows = []
    for Q in gens:
        Pm = P(Q)
        perm = [int(sp.Matrix(Pm.col(c)).T.tolist()[0].index(1)) for c in range(15)]   # species c -> perm[c]
        for i in range(3):
            for a in range(15):
                for b in range(a, 15):
                    # (P S_i P^T)[perm a, perm b] = S_i[a, b]  must equal sum_j Q[j, i] S_j[perm a, perm b]
                    r = {}
                    r[var(i, a, b)] = r.get(var(i, a, b), 0) + 1
                    for j in range(3):
                        c = Q[j, i]
                        if c: r[var(j, perm[a], perm[b])] = r.get(var(j, perm[a], perm[b]), 0) - c
                    rows.append(r)
    for i in range(3):
        for a in range(15):
            r = {}
            for b in range(15): r[var(i, a, b)] = r.get(var(i, a, b), 0) + 1
            rows.append(r)
    M = DomainMatrix([[sp.QQ(int(r.get(k, 0))) for k in range(nv)] for r in rows], (len(rows), nv), sp.QQ)
    ns = M.nullspace().to_Matrix()
    return ns
def to_S(vec):
    Ss = []
    for i in range(3):
        Sm = sp.zeros(15, 15)
        for a in range(15):
            for b in range(15): Sm[a, b] = vec[var(i, a, b)]
        Ss.append(Sm)
    return Ss
Rz = sp.Matrix([[0, -1, 0], [1, 0, 0], [0, 0, 1]]); Rx = sp.Matrix([[1, 0, 0], [0, 0, -1], [0, 1, 0]]); Inv = -sp.eye(3)
# author's maps in orthonormal coordinates: E 0-2, s1 3, s2 4, B 5-7, d1 8, d2 9, t12 10, t13 11, t23 12, w 13
iE = [0, 1, 2]; iB = [5, 6, 7]; is1, is2, id1, id2, iw = 3, 4, 8, 9, 13; it = [10, 11, 12]
D1 = sp.diag(1, -1, 0)/sp.sqrt(2); D2 = sp.diag(1, 1, -2)/sp.sqrt(6)
def Qm(i, j):
    M = sp.zeros(3, 3); M[i, j] = M[j, i] = 1/sp.sqrt(2); return M
Qs = [Qm(0, 1), Qm(0, 2), Qm(1, 2)]
def cross(q): return sp.Matrix([[0, -q[2], q[1]], [q[2], 0, -q[0]], [-q[1], q[0], 0]])
def put(A, rows, col_or_cols, block):
    """place block (rows x cols) and its transpose"""
    cols = col_or_cols if isinstance(col_or_cols, list) else [col_or_cols]
    B = sp.Matrix(block).reshape(len(rows), len(cols))
    for a, r in enumerate(rows):
        for b, c in enumerate(cols):
            A[r, c] += B[a, b]; A[c, r] += B[a, b]
    return A
def author_maps(q):
    C = cross(q); maps = {}
    Z = lambda: sp.zeros(14, 14)
    maps['a1'] = put(Z(), iE, is1, q); maps['a2'] = put(Z(), iE, is2, q)
    maps['m'] = put(Z(), iE, iB, C)
    A = Z(); put(A, iE, id1, D1*q); put(A, iE, id2, D2*q); maps['u'] = A
    A = Z()
    for k in range(3): put(A, iE, it[k], Qs[k]*q)
    maps['v'] = A
    maps['b1'] = put(Z(), iB, is1, q); maps['b2'] = put(Z(), iB, is2, q)
    A = Z(); put(A, iB, id1, D1*q); put(A, iB, id2, D2*q); maps['bu'] = A
    A = Z()
    for k in range(3): put(A, iB, it[k], Qs[k]*q)
    maps['bv'] = A
    A = Z()
    for k in range(3):
        for al, Dm in ((id1, D1), (id2, D2)):
            val = (Qs[k]*(C*Dm - Dm*C)).trace()
            A[it[k], al] += val; A[al, it[k]] += val
    maps['d'] = A
    A = Z()
    for k, comp in zip(range(3), (q[2], q[1], q[0])): A[it[k], iw] += comp; A[iw, it[k]] += comp
    maps['g'] = A
    return maps
def R(Q): return (U*P(Q)*U.T).applyfunc(sp.nsimplify)

print("== K1 exact classification by nullspace")
n24 = solve_space([Rz, Rx]); n48 = solve_space([Rz, Rx, Inv])
check("K0 alphabet: 15 labels (vacancy, 6 polar axis, 8 axial cube), 24 proper and 48 signed permutations; the note's 14 observables "
      "are orthonormal and orthogonal to the constant (tangent)", len(labels) == 15 and len(G24) == 24 and len(G48) == 48
      and sp.simplify(U*U.T - sp.eye(14)) == sp.zeros(14, 14) and sp.simplify(U*sp.ones(15, 1)) == sp.zeros(14, 1))
check("K1 covariant symmetric first-order symbols: dimension 11 for the proper group (generators 90-degree rotations about z and "
      "x), 5 with inversion added (exact nullspace, species space, rational)", n24.rows == 11 and n48.rows == 5, f"{n24.rows}, {n48.rows}")
print("== K2 the author's eleven maps")
maps = author_maps(qv); names = list(maps)
Rs = {'Rz': R(Rz), 'Rx': R(Rx), 'Inv': R(Inv)}
def covariant(A, Q, RQ):
    lhs = RQ*A*RQ.T; rhs = A.subs({q1: (Q*qv)[0], q2: (Q*qv)[1], q3: (Q*qv)[2]}, simultaneous=True)
    return sp.simplify(lhs - rhs) == sp.zeros(14, 14)
cov24 = all(covariant(maps[n], Rz, Rs['Rz']) and covariant(maps[n], Rx, Rs['Rx']) for n in names)
inv = {n: covariant(maps[n], Inv, Rs['Inv']) for n in names}
vecs = []
for n in names:
    v = []
    for qq in (q1, q2, q3): v += list(maps[n].diff(qq))
    vecs.append(v)
rk = sp.Matrix(vecs).rank(simplify=True)
check("K2 all eleven maps are proper-covariant (R(Q) = U P(Q) U^T), independent (rank 11), so they span the 11-dimensional space; "
      "inversion covariance holds exactly for a1, a2, m, u, v", cov24 and rk == 11 and [n for n in names if inv[n]] == ['a1', 'a2', 'm', 'u', 'v'],
      f"rank {rk}")
print("== K3 closure conditions")
cs = sp.symbols('a1 a2 m u v b1 b2 bu bv d g'); cd = dict(zip(names, cs))
A = sum((cd[n]*maps[n] for n in names), sp.zeros(14, 14))
vec = iE + iB; nonvec = [3, 4, 8, 9, 10, 11, 12, 13]
def coeff_eqs(exprs):
    eqs = []
    for e in exprs:
        e = sp.expand(e)
        if e != 0: eqs += list(sp.Poly(e, q1, q2, q3).coeffs())
    return eqs
eight = {cd[n]: 0 for n in ('a1', 'a2', 'u', 'v', 'b1', 'b2', 'bu', 'bv')}
sol1 = sp.solve(coeff_eqs([A[r, c] for r in vec for c in nonvec]), cs, dict=True)
x = sp.symbols('x0:14'); xv = sp.Matrix(x); eq2 = []
for blk in (iE, iB):
    expr = ((qv.T*A.extract(blk, list(range(14))))*xv)[0]
    num = sp.numer(sp.together(sp.expand(expr.subs({x[0]: -(q2*x[1] + q3*x[2])/q1, x[5]: -(q2*x[6] + q3*x[7])/q1}))))
    eq2 += list(sp.Poly(sp.expand(num), *x, q1, q2, q3).coeffs())
sol2 = sp.solve(eq2, cs, dict=True)
Cq = cross(qv); eq3 = []
for blk in (iE, iB):
    Arow = A.extract(blk, list(range(14)))
    eq3 += coeff_eqs(list(Cq*Arow.extract([0, 1, 2], nonvec)))
    eq3 += coeff_eqs(list(Cq*Arow.extract([0, 1, 2], iE)*qv)) + coeff_eqs(list(Cq*Arow.extract([0, 1, 2], iB)*qv))
sol3 = sp.solve(eq3, cs, dict=True)
check("K3a closure of the six raw-vector observables for arbitrary other moments (vector rows vanish on all nonvector columns, "
      "every q) holds iff a1=a2=u=v=b1=b2=b_u=b_v=0; m, d, g stay free", sol1 == [eight], str(sol1))
check("K3b preservation of q.E = q.B = 0 for arbitrary remaining moments (on the constraint subspace, every q) gives the same eight "
      "conditions", sol2 == [eight], str(sol2))
check("K3c derivative-curl closure ([q]x of the vector rows kills nonvector columns and longitudinal E, B inputs) holds iff "
      "u=v=b_u=b_v=0; the four scalar couplings and m, d, g stay free", sol3 == [{cd['u']: 0, cd['v']: 0, cd['bu']: 0, cd['bv']: 0}], str(sol3))
print("== K4-K8")
blk = sp.Matrix([[A[it[k], c] for c in (id1, id2, iw)] for k in range(3)])
note = sp.Matrix([[2*cd['d']*q3, 0, cd['g']*q3], [-cd['d']*q2, -sp.sqrt(3)*cd['d']*q2, cd['g']*q2], [-cd['d']*q1, sp.sqrt(3)*cd['d']*q1, cd['g']*q1]])
check("K4 the d,g block t-versus-(d1,d2,w) is exactly the displayed matrix, with determinant -6 sqrt3 d^2 g q1 q2 q3",
      sp.simplify(blk - note) == sp.zeros(3, 3) and sp.simplify(blk.det() + 6*sp.sqrt(3)*cd['d']**2*cd['g']*q1*q2*q3) == 0)
Tm = sp.diag(-1, -1, -1, *([1]*11))
odd = [n for n in names if sp.simplify(Tm*maps[n]*Tm + maps[n]) == sp.zeros(14, 14)]
even = [n for n in names if sp.simplify(Tm*maps[n]*Tm - maps[n]) == sp.zeros(14, 14)]
check("K5 the internal reversal T = diag(-I3, I11) is odd exactly on the original five and even on the six added maps, so "
      "T A T = -A for every q iff b1=b2=b_u=b_v=d=g=0", odd == ['a1', 'a2', 'm', 'u', 'v'] and even == ['b1', 'b2', 'bu', 'bv', 'd', 'g'])
Ag = A.subs({cd[n]: 0 for n in names if n not in ('m', 'd', 'g')}).subs({cd['m']: 2, cd['d']: 3, cd['g']: 5, q1: 1, q2: 2, q3: 3})
check("K6 with only m, d, g nonzero (closed-vector case) at the generic q = (1,2,3) the symbol has rank 10: ten nonzero speeds, four "
      "zeros", Ag.rank() == 10)
a1, a2, m, u, v = [cd[n] for n in ('a1', 'a2', 'm', 'u', 'v')]
K = A.extract(iE, [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]).subs({cd[n]: 0 for n in ('b1', 'b2', 'bu', 'bv', 'd', 'g')})
KK = sp.expand(K*K.T)
formula = (m**2 + v**2/2)*(q1**2 + q2**2 + q3**2)*sp.eye(3) + (a1**2 + a2**2 - m**2 - u**2/3 + v**2/2)*qv*qv.T + (u**2 - v**2)*sp.diag(q1**2, q2**2, q3**2)
check("K7 #8569's Gram formula K K^T = (m^2+v^2/2)|q|^2 I + (a1^2+a2^2-m^2-u^2/3+v^2/2) q q^T + (u^2-v^2) diag(q_i^2)",
      sp.simplify(KK - sp.expand(formula)) == sp.zeros(3, 3))
pv = sp.symbols('p0:15'); Ssym = sp.Matrix(15, 15, lambda i, j: sp.Symbol(f's{min(i, j)}_{max(i, j)}'))
# impose zero row sums by construction on a random rational symmetric tangent matrix
import random
rg = random.Random(5); Sr = sp.zeros(15, 15)
for i in range(15):
    for j in range(i + 1, 15):
        val = sp.Rational(rg.randint(-9, 9), rg.randint(1, 5)); Sr[i, j] = Sr[j, i] = val
for i in range(15): Sr[i, i] = -sum(Sr[i, j] for j in range(15) if j != i)
p = sp.Matrix(pv)
J = sp.Matrix([2*p[a]*((Sr*p)[a] - (p.T*Sr*p)[0]) for a in range(15)])
Jac = J.jacobian(p).subs({pv[i]: sp.Rational(1, 15) for i in range(15)})
check("K8 the species current J_a = 2 p_a[(S p)_a - p^T S p] has, at the uniform law and for S 1 = 0 symmetric, tangent derivative "
      "(2/15) S (so S = (15/2) U A U^T realises A)", sp.simplify(Jac - sp.Rational(2, 15)*Sr) == sp.zeros(15, 15))
print(f"== done in {time.time()-T0:.0f}s")
if FAIL:
    print("SUMMARY: ROUTE FAILS AT " + ", ".join(FAIL))
else:
    print("SUMMARY: PROVED (cross-family reproduction, no defect found) - the proper-cubic eleven-coupling extension and #8569's "
          "five-versus-eleven classification hold: exact species-space nullspaces give 11 proper and 5 full covariant symbols; "
          "the author's eleven maps are covariant, independent and exhaustive; raw-vector closure and raw Gauss preservation each "
          "force the eight conditions a1=a2=u=v=b1=b2=b_u=b_v=0 (curl m and the non-vector d, g survive), derivative-curl closure "
          "only u=v=b_u=b_v=0; the d,g block determinant, reversal parities, rank 10, #8569's Gram formula and the 15/2 "
          "normalisation reproduce")
