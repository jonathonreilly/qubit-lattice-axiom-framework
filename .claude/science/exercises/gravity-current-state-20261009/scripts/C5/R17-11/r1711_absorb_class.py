"""R17-11 (a)/(d): what the E-sector can absorb under (S); Lagrangian alternatives; sizes (sympy + arithmetic).

C1 (absorbable class, proved, elementary).  Local orthonormal site frame n = e_0.  A site-frame stress
     S = rho_S n n + (q n + n q) + p_S h + pi   (pi spatial traceless)
   is absorbed by the E-sector under (S) iff E := -lam0 g - kappa S keeps the imposed form E_nn = lam0 (fixed law constant),
   E_ni = 0, E^TL = 0.  Result: rho_S = 0, q = 0, pi = 0, p_S free.  The grid vacuum T_v = -V g + W h splits uniquely into
   a covariant part (-V g: gravitates) and an absorbable part (W h).  Absorbing energy density instead needs lam' != 0, i.e.
   g' != 0 (Lemma C / R15-1 Lemma S) -- not available under (S).
C2 (ultralocal Lagrangian alternatives, proved).  Lattice time T as a khronon in unitary gauge, X = 1/N^2, action N sqrt(h) P(X):
   rho = 2 X P_X - P, p = P, c_s^2 = P_X/(P_X + 2 X P_XX).
   (i)  p independent of N  =>  P_X = 0  =>  W = rho + p = 0.
   (ii) rho = 0 for all N (the partner T_X = -W h)  =>  P = C sqrt(X)  =>  p = C/N: lapse-dependent (the cuscuton g/N term of
        R15-1's S_E).  So a lapse-independent pure pressure -W is not ultralocal-Lagrangian.
   (iii) rho = V for all N  =>  P = -V + C sqrt(X), W = C/N, c_s^2 = infinity (cuscuton); a conserved fluid at rest in n with
        constant rho then needs W theta_n = 0: no expansion of the site frame.
C3 (energy leg, counted once from r151_gridvac D3): fixed proper site density + W != 0 => n.div(T_v) = -W theta_n != 0 for any
   conserved completion; so an energy exchange is unavoidable; (d-i) and (d-ii) differ only in the momentum leg D_i W + W a_i.
C4 sizes: W per real scalar (R11-3 table, refereed reproduction) and R17-4's LV-tadpole values, in rho_Lambda at a = l_P.
"""
import sympy as sp

# C1 ---------------------------------------------------------------------------------
lam0, kap, rS, pS = sp.symbols('lambda_0 kappa rho_S p_S', real=True)
q = sp.symbols('q1:4', real=True)
pi = sp.Matrix(3, 3, lambda i, j: sp.Symbol(f'pi{min(i, j)}{max(i, j)}', real=True))
pi[2, 2] = -pi[0, 0] - pi[1, 1]
g = sp.diag(-1, 1, 1, 1)
S = sp.zeros(4, 4)
S[0, 0] = rS
for i in range(3):
    S[0, i+1] = S[i+1, 0] = -q[i]           # momentum flux in the n-frame (lower index sign immaterial)
    for j in range(3):
        S[i+1, j+1] = pS*(1 if i == j else 0) + pi[i, j]
E = -lam0*g - kap*S
conds = [sp.Eq(E[0, 0], lam0)] + [sp.Eq(E[0, i+1], 0) for i in range(3)]
Esp = E[1:, 1:]
tr = sum(Esp[i, i] for i in range(3))
conds += [sp.Eq(Esp[i, j] - (tr/3 if i == j else 0), 0) for i in range(3) for j in range(i, 3)]
unk = [rS, *q, pi[0, 0], pi[1, 1], pi[0, 1], pi[0, 2], pi[1, 2]]
sol = sp.solve(conds, unk, dict=True)
print("C1 absorbable site-frame stresses under (S): solution", sol, "; p_S unconstrained:", pS not in sol[0])

# C2 ---------------------------------------------------------------------------------
Xs, C, Vv = sp.symbols('X C V', positive=True)
P = sp.Function('P')
rho = 2*Xs*P(Xs).diff(Xs) - P(Xs)
# (i)
print("C2(i)  dp/dN = 0  <=>  P_X = 0  ->  W = rho + p = 2 X P_X =", sp.simplify((2*Xs*P(Xs).diff(Xs)).subs(P(Xs).diff(Xs), 0)))
# (ii)
solii = sp.dsolve(sp.Eq(rho, 0), P(Xs))
print("C2(ii) rho = 0 for all X:", solii, " -> p = P = C1*sqrt(X) = C1/N (lapse-dependent: cuscuton g/N)")
# (iii)
soliii = sp.dsolve(sp.Eq(rho, Vv), P(Xs))
Piii = soliii.rhs
Wiii = sp.simplify(2*Xs*Piii.diff(Xs))
cs2_den = sp.simplify(Piii.diff(Xs) + 2*Xs*Piii.diff(Xs, 2))
print("C2(iii) rho = V for all X:", soliii, "; W = rho + p =", Wiii, "; P_X + 2X P_XX =", cs2_den, "(c_s^2 = infinity)")
print("        conserved fluid at rest in n: rho' + theta_n W = 0 with rho' = 0  ->  theta_n * W = 0")

# C4 ---------------------------------------------------------------------------------
MP = 1.221e19          # GeV, unreduced (as vR11-3:68-73)
rhoL = 2.52e-47        # GeV^4 (as vR11-3:68-73)
unit = MP**4/rhoL
print(f"C4 1/l_P^4 = {unit:.3e} rho_Lambda")
for lab, w in (("R11-3 L m=1", 2.0683), ("R11-3 G m=1", 1.8492), ("R11-3 NN m=1", 1.3991),
               ("R17-4 M-zero m=0.01 (U)", 0.6021), ("R17-4 U-zero m=0.1 (U)", 0.6107), ("R17-4 U-zero m=0.1 (M)", 0.6331)):
    print(f"C4 W = rho+p = {w:.4f}/a^4 per real scalar ({lab}) = {w*unit:.2e} rho_Lambda")
