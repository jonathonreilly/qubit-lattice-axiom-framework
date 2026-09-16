"""Control, block 27: (1) sign lemma by series: coefficients of (kappa/2) sinh 2kappa + kappa^2 - 2 sinh^2 kappa are >= 0 (exact);
(2) identities: Var(w) = A'(kappa); E[((s - A u).d)^2] = A/k + (1 - 3A/k - A^2)(u.d)^2 (symbolic); (3) TV(K_V, K_V') <= |V - V'|/(2 sqrt3)
against quadrature at random pairs; (4) simulation of m_t at beta = 0.3, 0.5 against (sqrt3 beta)^t and beta^t."""
import sympy as sp, numpy as np
from fractions import Fraction as F
k, w, c = sp.symbols("kappa w c", positive=True)
lhs = sp.series(2*sp.sinh(k)**2, k, 0, 16).removeO(); rhs = sp.series(k/2*sp.sinh(2*k) + k**2, k, 0, 16).removeO()
diff = sp.expand(rhs - lhs)
print("(1) coefficients of RHS - LHS:", [diff.coeff(k, 2*m) for m in range(1, 8)], " (m/2 - 1 pattern:", [sp.Rational(2**(2*m), sp.factorial(2*m))*(sp.Rational(m,2)-1) for m in range(1,8)], ")")
A = sp.coth(k) - 1/k
Z = sp.integrate(sp.exp(k*w), (w, -1, 1)); Ew = sp.integrate(w*sp.exp(k*w), (w,-1,1))/Z; Ew2 = sp.integrate(w**2*sp.exp(k*w), (w,-1,1))/Z
print("(2) Var(w) - A'(k) =", sp.simplify((Ew2 - Ew**2 - sp.diff(A, k)).rewrite(sp.exp)))
# directional second moment: E[((s - A u).d)^2] with E[s s^T] = (A/k) I + (1 - 3A/k) u u^T, E[s] = A u, d unit, u.d = c
M = (A/k)*sp.eye(3) + (1 - 3*A/k)*sp.Matrix([[1,0,0],[0,0,0],[0,0,0]])   # u = e_1
d = sp.Matrix([c, sp.sqrt(1-c**2), 0])
expr = (d.T*M*d)[0] - 2*A*c*(A*c) + A**2*c**2
print("(2) E[((s-Au).d)^2] - [A/k + (1 - 3A/k - A^2) c^2] =", sp.simplify(expr - (A/k + (1 - 3*A/k - A**2)*c**2)))
# (3) TV quadrature
rng = np.random.default_rng(5)
def Af(x): return 1/np.tanh(x) - 1/x
nth, nph = 300, 300
th = (np.arange(nth)+0.5)*np.pi/nth; ph = (np.arange(nph)+0.5)*2*np.pi/nph
TH, PH = np.meshgrid(th, ph, indexing="ij"); Wt = np.sin(TH)*(np.pi/nth)*(2*np.pi/nph)
pts = np.stack([np.sin(TH)*np.cos(PH), np.sin(TH)*np.sin(PH), np.cos(TH)], -1)
def dens(V):
    n = np.linalg.norm(V); return (n/(4*np.pi*np.sinh(n)))*np.exp(pts@V) if n > 1e-9 else np.full(TH.shape, 1/(4*np.pi))
worst = 0
for trial in range(300):
    V = rng.normal(size=3)*rng.choice([0.1, 0.5, 1, 2, 5]); Vp = V + rng.normal(size=3)*rng.choice([0.05, 0.3, 1, 3])
    tv = 0.5*(np.abs(dens(V)-dens(Vp))*Wt).sum(); worst = max(worst, tv/np.linalg.norm(V-Vp))
print(f"(3) max TV/|V - V'| over 300 random pairs = {worst:.4f}; bound 1/(2 sqrt3) = {1/(2*np.sqrt(3)):.4f}; the small-|V| value 1/4")
# (4) simulation
def run(beta, L, T, seed):
    rng2 = np.random.default_rng(seed); s = np.zeros((L,L,3)); s[...,2] = 1; out = []
    for t in range(1, T+1):
        Sv = s + np.roll(s,1,0) + np.roll(s,1,1); n = np.linalg.norm(Sv, axis=2); u = Sv/n[...,None]; kap = beta*n
        U = rng2.random((L,L)); wv = np.clip(1 + np.log(U + (1-U)*np.exp(-2*kap))/kap, -1, 1); phv = 2*np.pi*rng2.random((L,L))
        a = np.where((np.abs(u[...,0])<0.9)[...,None], np.array([1.0,0,0]), np.array([0,1.0,0])); e1 = a - (a*u).sum(-1)[...,None]*u; e1 /= np.linalg.norm(e1,axis=2)[...,None]; e2 = np.cross(u, e1)
        r = np.sqrt(np.clip(1-wv*wv,0,1)); s = wv[...,None]*u + r[...,None]*(np.cos(phv)[...,None]*e1 + np.sin(phv)[...,None]*e2)
        out.append(s[...,2].mean())
    return out
for beta in (0.3, 0.5):
    m = run(beta, 256, 12, 1)
    print(f"(4) beta={beta}: m_t = {[round(x,4) for x in m[:8]]}; (sqrt3 beta)^t = {[round((np.sqrt(3)*beta)**t,4) for t in range(1,9)]}; beta^t = {[round(beta**t,4) for t in range(1,9)]}; A(3beta) = {Af(3*beta):.4f}")
