"""C5 R4-2 (1): exact algebraic inputs of Theorem S and Lemma G.

Lattice coordinates n in Z^4, Q7(n) = -7 n0^2 + n1^2 + n2^2 + n3^2, Gram G7 = diag(-7,1,1,1).
Gamma acts on n by integer matrices g with g^T G7 g = G7; on dual (momentum/charge
coefficient) coordinates by g^{-T}.

(a) gamma1 = [[8,3],[21,8]] on (n0,n1) is in Gamma; eigenvalues 8 +- 3 sqrt 7.
    Its conjugates by cubic rotations (in Gamma) act on (n0,n2), (n0,n3).
(b) The expanding and contracting eigenvectors of gamma1, gamma2, gamma3, both in the
    vector action g and in the dual action g^{-T}, span R^4 (rank 4).  This is the
    only group-specific input of Theorem S's recurrence step.
(c) Gamma-invariant Hermitian forms C on C^4 (vector rep): g^* C g = C for the
    generators -> C = c*G7 (indefinite), so the only positive-semidefinite one is 0.
    Same for the dual rep.  (Lemma G(i): site fields carrying a Lorentz vector index
    with finite variance have zero one-particle content.)
(d) Unipotent check: gamma1 is semisimple (distinct eigenvalues), so bounded-orbit
    vectors of gamma1 are exactly the eigenvalue-1 subspace span(e2,e3).
"""
import sympy as sp

G7 = sp.diag(-7, 1, 1, 1)


def emb(a, b, c, d, i, j):
    """2x2 block [[a,b],[c,d]] acting on coordinates (i,j), identity elsewhere."""
    M = sp.eye(4)
    M[i, i], M[i, j], M[j, i], M[j, j] = a, b, c, d
    return M


g1 = emb(8, 3, 21, 8, 0, 1)
g2 = emb(8, 3, 21, 8, 0, 2)
g3 = emb(8, 3, 21, 8, 0, 3)
# cubic rotation taking axis 1 -> axis 2 (in Gamma: integral, preserves G7, det 1)
Rz = sp.Matrix([[1, 0, 0, 0], [0, 0, -1, 0], [0, 1, 0, 0], [0, 0, 0, 1]])
for name, M in [("g1", g1), ("g2", g2), ("g3", g3), ("Rz", Rz)]:
    assert M.T * G7 * M == G7, name
    assert M.det() == 1, name
print("(a) g1,g2,g3,Rz preserve G7 exactly, det 1:", True)
conj = Rz * g1 * Rz.inv()
print("    Rz g1 Rz^-1 =", conj.tolist(), " in Gamma:", conj.T * G7 * conj == G7,
      "; it is a pure boost on (n0,n2) like g2 (same eigenvalues):", conj.eigenvals() == g2.eigenvals())
ev = g1.eigenvals()
print("    eigenvalues of g1:", ev)

vecs = []
for name, M in [("g1", g1), ("g2", g2), ("g3", g3)]:
    for rep, A in [("vector", M), ("dual", (M.inv()).T)]:
        for lam, mult, vs in A.eigenvects():
            if sp.simplify(sp.Abs(lam) - 1) != 0:
                vecs.append((name, rep, sp.nsimplify(lam), vs[0]))
vec_only = [v for (_, r, _, v) in vecs if r == "vector"]
dual_only = [v for (_, r, _, v) in vecs if r == "dual"]
print("(b) # expanding/contracting eigenvectors found:", len(vecs))
print("    rank of their span (vector action):", sp.Matrix.hstack(*vec_only).rank())
print("    rank of their span (dual action):  ", sp.Matrix.hstack(*dual_only).rank())
print("    rank of span(e_+,e_-) of g1 alone (vector):",
      sp.Matrix.hstack(*[v for (n, r, _, v) in vecs if n == "g1" and r == "vector"]).rank())

# (c) invariant Hermitian forms on C^4 under g1 and Rz (and a second rotation)
Rx = sp.Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, -1], [0, 0, 1, 0]])
syms = sp.symbols("c0:16")
C = sp.Matrix(4, 4, syms)
eqs = []
for M in [g1, Rz, Rx]:
    eqs += list(M.T * C * M - C)
    Md = M.inv().T
    # dual rep handled separately below
sol = sp.solve(eqs + list(C - C.T), syms, dict=True)
Csol = C.subs(sol[0])
print("(c) general real symmetric form invariant under g1,Rz,Rx (vector rep):")
print("   ", Csol)
free = sorted(Csol.free_symbols, key=str)
print("    free parameters:", free, "-> proportional to G7 = diag(-7,1,1,1):",
      sp.simplify(Csol - Csol[1, 1] * G7) == sp.zeros(4))
print("    G7 indefinite (eigenvalues):", G7.eigenvals(), "=> only psd invariant form is 0")
eqs = []
for M in [g1, Rz, Rx]:
    Md = M.inv().T
    eqs += list(Md.T * C * Md - C)
sol = sp.solve(eqs + list(C - C.T), syms, dict=True)
Csol = C.subs(sol[0])
print("    dual rep invariant forms:", Csol, " (prop. to G7^{-1}, indefinite)")
# antisymmetric part (imaginary part of a Hermitian form) invariant?
eqs = []
for M in [g1, Rz, Rx]:
    eqs += list(M.T * C * M - C)
sol = sp.solve(eqs + list(C + C.T), syms, dict=True)
print("    invariant antisymmetric forms (imag. part of Hermitian):", C.subs(sol[0]))

# (d) bounded-orbit subspace of g1: eigenvalue-1 eigenspace dimension
ker = (g1 - sp.eye(4)).nullspace()
print("(d) dim ker(g1 - 1) =", len(ker), " basis:", [list(v) for v in ker])
