"""C5 R18-8 (A): degree-2 asymptotic Killing charges of free separable lattice matter, Vlasov (leading-order) form.

Charges (integrated against the Wigner density f(x,k); every identity below is a pointwise symbol identity,
so it holds for every f):
  H = eps(k),  P_c = d_c(eps^2/2) = eps v_c (current-aligned, R16-8 Lemma P),  K_b = x_b eps,  J_ab = x_a P_b - x_b P_a.
Bracket {A,B} = dA/dx . dB/dk - dA/dk . dB/dx  (so {x_b, k_c} = delta_bc).
Generic separable band: eps^2 = m^2 + u1(k1) + u2(k2) + u3(k3), u_i arbitrary smooth functions.
Defect density Delta_cb = eps (d_b P_c - delta_bc)  (diagonal for separable bands).
Prints each bracket minus its Poincare value, simplified; expected: 0, or the stated defect expression.
"""
import os
os.environ.setdefault("OMP_NUM_THREADS", "2")
import sympy as sp

x = sp.symbols('x1:4', real=True); k = sp.symbols('k1:4', real=True); m = sp.symbols('m', positive=True)
u = [sp.Function('u%d' % (i + 1))(k[i]) for i in range(3)]
eps = sp.sqrt(m**2 + sum(u))
P = [sp.diff(eps**2 / 2, k[c]) for c in range(3)]
v = [sp.diff(eps, k[c]) for c in range(3)]
H = eps
K = [x[b] * eps for b in range(3)]
J = [[x[a] * P[b] - x[b] * P[a] for b in range(3)] for a in range(3)]
Delta = [[eps * (sp.diff(P[c], k[b]) - (1 if b == c else 0)) for b in range(3)] for c in range(3)]

def br(A, B):
    return sum(sp.diff(A, x[i]) * sp.diff(B, k[i]) - sp.diff(A, k[i]) * sp.diff(B, x[i]) for i in range(3))

def z(e):
    return sp.simplify(sp.expand(e)) == 0

lines = []
def pr(s):
    print(s); lines.append(s)

d = lambda a, b: 1 if a == b else 0
pr("(A) Vlasov symbol identities, generic separable band, current-aligned P = d(eps^2/2):")
pr("  {K_b,H} - P_b = 0 for all b: %s" % all(z(br(K[b], H) - P[b]) for b in range(3)))
pr("  {P_c,H} = 0, {P_c,P_d} = 0: %s" % all(z(br(P[c], H)) and z(br(P[c], P[dd])) for c in range(3) for dd in range(3)))
pr("  {K_a,K_b} + J_ab = 0 for all a,b: %s" % all(z(br(K[a], K[b]) + J[a][b]) for a in range(3) for b in range(3)))
pr("  {J_ab,H} = 0: %s" % all(z(br(J[a][b], H)) for a in range(3) for b in range(3)))
pr("  {K_b,P_c} - delta_bc H - Delta_cb = 0 for all b,c: %s" %
   all(z(br(K[b], P[c]) - d(b, c) * H - Delta[c][b]) for b in range(3) for c in range(3)))
pr("  Delta off-diagonal = 0 (separable): %s" % all(z(Delta[c][b]) for c in range(3) for b in range(3) if b != c))
# rotation sector: Poincare values {J_ab,P_c} = delta_ac P_b - delta_bc P_a ; {J_ab,K_c} = delta_ac K_b - delta_bc K_a
okJP = all(z(br(J[a][b], P[c]) - (d(a, c) * P[b] - d(b, c) * P[a]) - (v[b] * Delta[c][a] - v[a] * Delta[c][b]))
           for a in range(3) for b in range(3) for c in range(3))
pr("  {J_ab,P_c} - [delta_ac P_b - delta_bc P_a] = v_b Delta_ca - v_a Delta_cb: %s" % okJP)
okJK = all(z(br(J[a][b], K[c]) - (d(a, c) * K[b] - d(b, c) * K[a]) + (x[a] * Delta[b][c] - x[b] * Delta[a][c]))
           for a in range(3) for b in range(3) for c in range(3))
pr("  {J_ab,K_c} - [delta_ac K_b - delta_bc K_a] = -(x_a Delta_bc - x_b Delta_ac): %s" % okJK)
# {J,J}: Poincare value {J_ab,J_cd} = d_ac J_bd ... ; compute residual and check it is a defect expression
def Jstd(a, b, c, dd):
    return d(a, c) * J[b][dd] - d(a, dd) * J[b][c] - d(b, c) * J[a][dd] + d(b, dd) * J[a][c]
def Jdef(a, b, c, dd):
    # from {x_a P_b, x_c P_d} = x_c P_b d_a P_d - x_a P_d d_c P_b, defect part replaces d_a P_d -> Delta/eps
    t = lambda a, b, c, dd: x[c] * v[b] * Delta[dd][a] - x[a] * v[dd] * Delta[b][c]
    return t(a, b, c, dd) - t(b, a, c, dd) - t(a, b, dd, c) + t(b, a, dd, c)
okJJ = all(z(br(J[a][b], J[c][dd]) - Jstd(a, b, c, dd) - Jdef(a, b, c, dd))
           for (a, b) in [(0, 1), (0, 2), (1, 2)] for (c, dd) in [(0, 1), (0, 2), (1, 2)])
pr("  {J_ab,J_cd} - [Poincare] = defect bilinear in (x, v, Delta): %s" % okJJ)
# continuum control: u_i = k_i^2 => Delta = 0 and all brackets are Poincare
sub = {u[i]: k[i]**2 for i in range(3)}
ctl = all(z(sp.simplify(Delta[c][c].subs(sub).doit())) for c in range(3))
pr("  NEGATIVE controls (must be False): {K_b,P_b} - H == 0: %s; {K_1,P_2}+{J_12,P_1} sign-flipped == 0: %s; {J_12,P_1} - P_2 == 0: %s" % (
    z(br(K[0], P[0]) - H), z(br(J[0][1], P[0]) + (P[1])), z(br(J[0][1], P[0]) - P[1])))
pr("  continuum control u_i = k_i^2: Delta == 0: %s" % ctl)
# zone mean: for any continuous periodic P_c(k_c), int_{-pi}^{pi} (dP_c/dk_c - 1) dk_c = -2 pi  (proved: P periodic)
pr("  zone-mean root (SUMMARY s17): int (P_c' - 1) dk_c = [P_c]_{-pi}^{pi} - 2pi = -2pi for continuous periodic P_c")
open(os.path.splitext(os.path.abspath(__file__))[0] + ".out", "w").write("\n".join(lines) + "\n")
