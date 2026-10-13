"""R19-33 (c)+(d) part 1: split the Euclidean linearized-GR source response into
spatial-TT exchange + an instantaneous ('constraint bridge') remainder.

Euclidean conserved source J_{mu nu} (mu=1..4, 4 = time), p = (q, p4), p.J = 0.
GR response (de Donder/any gauge; gauge invariant on conserved J):
    W_GR(J,J) = (J:J - 1/2 (tr J)^2) / p^2          [R2-4 G4, K7a symbol]
Spatial-TT exchange:  W_TT = J^TT_ij J^TT_ij / p^2   (J^TT = spatial TT part of J_ij w.r.t. q)
Remainder W_inst = W_GR - W_TT.  Claim to check: W_inst has NO pole at p^2 = 0 and, written in
the canonical sources (rho := J_44, P_i := J_4i, A := transverse trace of J_ij), contains no p4,
i.e. it is instantaneous (local in time, non-local in space).
The lattice FP symbol of K7a is O(4)-covariant in s_mu = 2 sin(k_mu/2) with the staggered
placement, so the same algebra holds on Z^4 with p -> s (statement checked numerically in
r1933_d_lattice.py).
"""
import sympy as sp
q1, q2, q3, p4 = sp.symbols('q1 q2 q3 p4', real=True)
q = sp.Matrix([q1, q2, q3]); Q2 = q1**2 + q2**2 + q3**2; P2 = Q2 + p4**2
# free spatial components J_ij (6), then conservation fixes J_4j and J_44 (p4 != 0)
Jij = sp.Matrix(3, 3, lambda i, j: sp.Symbol('j%d%d' % (min(i, j)+1, max(i, j)+1)))
J4 = -(Jij * q) / p4                    # p4 J_4j + q_i J_ij = 0
J44 = -(q.T * J4)[0] / p4               # p4 J_44 + q_i J_i4 = 0
J = sp.zeros(4, 4)
J[:3, :3] = Jij; J[:3, 3] = J4; J[3, :3] = J4.T; J[3, 3] = J44
p = sp.Matrix([q1, q2, q3, p4])
assert sp.simplify(J * p) == sp.zeros(4, 1)
JJ = sum(J[a, b]**2 for a in range(4) for b in range(4)); trJ = J.trace()
W_GR = (JJ - sp.Rational(1, 2) * trJ**2) / P2
# spatial TT projector
th = sp.eye(3) - q * q.T / Q2
def PTT(M):
    return th * M * th - sp.Rational(1, 2) * th * (th * M).trace()
JTT = PTT(Jij)
W_TT = sum(JTT[i, j]**2 for i in range(3) for j in range(3)) / P2
W_inst = sp.together(sp.simplify(W_GR - W_TT))
num, den = sp.fraction(W_inst)
print("den(W_inst) factored:", sp.factor(den))
print("residue at p^2=0: (W_inst*p^2) at p4^2=-q^2 ->", sp.simplify((sp.cancel(W_inst*P2)).subs(p4, sp.I*sp.sqrt(Q2))))
# express in canonical sources: rho=J44, P=J4 (vector), A = tr(th J th) (transverse trace),
# and check W_inst = a rho^2/q^2 + b rho*A/q^2 + c |P_perp|^2/q^2 + ... with constant coefficients
rho, A, Pp2, PL, cA2 = sp.symbols('rho A Pperp2 PL cA2')
A_expr = (th * Jij).trace()
Pperp = th * J4; Pperp2_expr = sum(x**2 for x in Pperp)
PL_expr = (q.T * J4)[0] / sp.sqrt(Q2)
a, b, c, d, e, f = sp.symbols('a b c d e f')
ansatz = (a * J44**2 + b * J44 * A_expr + c * Pperp2_expr + d * A_expr**2 + e * PL_expr**2) / Q2
diff = sp.together(sp.simplify(W_inst - ansatz))
numd = sp.numer(diff)
coeffs = sp.Poly(sp.expand(numd), *(list(Jij.free_symbols) + [q1, q2, q3, p4])).coeffs()
sol = sp.solve(coeffs, [a, b, c, d, e], dict=True)
print("instantaneous form W_inst = (a rho^2 + b rho A + c |P_perp|^2 + d A^2 + e P_L^2)/q^2 with:", sol)
# numerical spot check at a random rational point
import random
random.seed(1)
for trial in range(3):
    vals = {s: sp.Rational(random.randint(-9, 9), random.randint(1, 5)) for s in Jij.free_symbols}
    vals.update({q1: sp.Rational(3, 7), q2: sp.Rational(-2, 5), q3: sp.Rational(1, 3), p4: sp.Rational(5, 11)})
    lhs = W_inst.subs(vals); rhs = ansatz.subs(sol[0]).subs(vals)
    print("  spot check W_inst - ansatz =", sp.simplify(lhs - rhs))
# signature of the instantaneous form in (rho, A, P_perp, P_L) at fixed q (each enters /q^2)
S = sol[0]
M = sp.Matrix([[S[a], S[b] / 2, 0, 0], [S[b] / 2, S[d], 0, 0], [0, 0, S[c], 0], [0, 0, 0, S[e]]])
print("quadratic form in (rho, A, |P_perp|, P_L) (times 1/q^2):"); sp.pprint(M)
print("eigenvalues:", [sp.nsimplify(x) for x in M.eigenvals().keys()])
# Static point mass rho' and probe: cross response W(J,J') = rho' * (2a rho + b A)/q^2 for the probe
print("\n== static responses (Euclidean J_44 = rho; Minkowski T^00 = -J_44, T^ii = J_ii) ==")
print("dust-dust (A=0,P=0): W = a rho rho'/q^2, a =", S[a], " -> log Z gains +a rho rho'/q^2: ATTRACTIVE iff a>0")
print("light probe: traceless 4D => J_44 + J_ii = 0 ... (Euclidean trace J_44 + J_ii = 0); a light ray along x:")
# light along x: Minkowski T^00 = T^11 = E, so Euclidean J_44 = -E (T_44 = -T^00), J_11 = E
# for static mass source at q perpendicular to x (impact-parameter geometry), A = J_11 (transverse) = E
E, m = sp.symbols('E m')
Wlight = (2 * S[a] * (-E) * (-m) + S[b] * E * (-m)) / 2   # cross term coefficient between probe and mass (mass: J44=-m)
Wdust = (2 * S[a] * (-E) * (-m)) / 2
print("  light/(dust of equal energy) cross-response ratio = 1+gamma =", sp.simplify(Wlight / Wdust))
