# session-20 constants arithmetic (float, informational except c_D which is checked exactly)
import itertools, math
from fractions import Fraction
import numpy as np
L, d = 3, 4
# c_D: grid Laplacian on {0..L-1}^4 (internal edges), Dirichlet at the centre
sites = list(itertools.product(range(L), repeat=d)); c = (1,)*d
idx = {s: i for i, s in enumerate(s for s in sites if s != c)}
n = len(idx)
Lap = [[Fraction(0)]*n for _ in range(n)]
for s in sites:
    for mu in range(d):
        t = list(s); t[mu] += 1; t = tuple(t)
        if t[mu] >= L: continue
        for a, b in ((s, t), (t, s)):
            if a != c:
                Lap[idx[a]][idx[a]] += 1
                if b != c: Lap[idx[a]][idx[b]] -= 1
A = np.array([[float(x) for x in r] for r in Lap])
lam = np.linalg.eigvalsh(A)[0]
# rigorous: Cholesky of Lap - q I in exact arithmetic with q = rational just below lam
q = Fraction(int(lam*10**6) - 1, 10**6)
M = [[Lap[i][j] - (q if i == j else 0) for j in range(n)] for i in range(n)]
ok = True
for k in range(n):  # LDL^T
    if M[k][k] <= 0: ok = False; break
    for i in range(k+1, n):
        f = M[i][k] / M[k][k]
        if f:
            for j in range(k, n): M[i][j] -= f * M[k][j]
print(f"c_D(L=3): float {lam:.8f}; exact Cholesky certifies Lap > {q} = {float(q):.6f}: {ok}")
cD = float(q)
sM1 = math.sqrt(L**4 - 1) / L**4
Dn = 2 * math.sqrt(d)
KFP = max((2/cD)*(1 + math.sqrt(cD)/(2*Dn)), (1 + 2*Dn/math.sqrt(cD))/(sM1/2))
print(f"s_M(1) = {sM1:.6f}; K_FP (with s_M >= s_M(1)/2) = {KFP:.3f}")
coth = lambda x: 1/math.tanh(x)
pL = 5*L - 4
for lab, m, gp, Rs in (("product rule", 1.97e-18, 1.19e-8, 1.4e20), ("N5-w0", 9.66e-11, 1.19e-8, 1.7e12)):
    a = m/2
    c_coth = 8*coth(a/2)**4/(gp*0.5)
    nOm = d*((4*Rs + 1)*L)**d
    c_sqrt = 81*math.sqrt(3*nOm)/(gp*0.5)
    cinf = min(c_coth, c_sqrt)
    K1 = 1 + 36*pL*cinf
    lam_old = gp*0.5/(8*coth(m/2)**4); lam_new = gp*0.5/9
    print(f"{lab}: 8coth^4(a/2)/(g'(1-eR)) = {c_coth:.2e}; 81 sqrt(3 n_Omega)/(g'(1-eR)) = {c_sqrt:.2e}; c_inf = {cinf:.2e}; "
          f"K_1 = 1 + 36 p_L c_inf = {K1:.2e}; gap old {lam_old:.2e}, RW-l2 {lam_new:.2e}; 1/(24 c_inf^2) = {1/(24*cinf**2):.2e}")
cE = 0.004069
print(f"gamma_1/gamma_0 = 2c_E = {2*cE:.5f}; gamma_0 = {1/3.5e6*0.5/9:.4e}, gamma_1 = {1/3.5e6*cE/9:.4e} (x2 sharpened: {2/3.5e6*0.5/9:.4e}, {2/3.5e6*cE/9:.4e})")
