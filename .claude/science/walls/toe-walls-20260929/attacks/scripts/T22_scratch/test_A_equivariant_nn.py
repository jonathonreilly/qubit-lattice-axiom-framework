"""T22 test A: G-equivariant Nielsen-Ninomiya check + epsilon(x) swap check.

A1: H(k) = [doublet block: h_D(k) (x) 1_2] + [singlet block: h_S(k)], h = d0 + d.sigma with d
    a random range-1 trigonometric polynomial. SU(2) acts on the isospin factor (doublet) and
    trivially on the singlet block, and commutes with H by construction. Node = zero of d.
    Chirality = sign det(dd/dk). Report the total chirality per isotypic block.
A2: for the campaign walker d = (sin k1, sin k2, sin k3): eps(x)=(-1)^(x+y+z) is k -> k+Pi;
    check eps H eps = -H and that it maps chirality chi -> -chi.
A3: intertwiner count Hom_SU(2)(doublet, singlet) = 0 (a hop from a doublet site to a singlet
    site cannot be invariant without a doublet link field).
"""
import numpy as np
from scipy.optimize import root
rng = np.random.default_rng(20260929)

def make_d():
    a = rng.normal(size=(3,3)); b = rng.normal(size=(3,3)); c = rng.normal(size=3)
    # d_i(k) = c_i + sum_j a_ij sin k_j + b_ij cos k_j ; scale constants so zeros exist
    def d(k):
        return c*0.6 + a@np.sin(k) + b@np.cos(k)
    def J(k):
        return a*np.cos(k)[None,:] - b*np.sin(k)[None,:]
    return d, J

def nodes(d, J, ntry=600):
    found = []
    for _ in range(ntry):
        k0 = rng.uniform(-np.pi, np.pi, 3)
        s = root(d, k0, jac=J, tol=1e-13)
        if not s.success or np.linalg.norm(d(s.x)) > 1e-9: continue
        k = (s.x + np.pi) % (2*np.pi) - np.pi
        if any(np.linalg.norm(((k-f+np.pi) % (2*np.pi))-np.pi) < 1e-6 for f,_ in found): continue
        chi = int(np.sign(np.linalg.det(J(k))))
        found.append((k, chi))
    return found

bad = 0
rows = []
for draw in range(40):
    dD, JD = make_d(); dS, JS = make_d()
    nD = nodes(dD, JD); nS = nodes(dS, JS)
    # isospin multiplicity: doublet block nodes are doubled (both isospin components)
    chiD = 2*sum(c for _,c in nD); chiS = sum(c for _,c in nS)
    rows.append((len(nD), chiD, len(nS), chiS))
    if chiD != 0 or chiS != 0: bad += 1
print("A1: draws=40  (n_nodes_doublet, net_chi_doublet_states, n_nodes_singlet, net_chi_singlet)")
print("    nonzero-node draws:", sum(1 for r in rows if r[0]>0 or r[2]>0))
print("    first 8:", rows[:8])
print("    draws with nonzero isotype chirality:", bad)

# A2 walker
def d_w(k): return np.sin(k)
def J_w(k): return np.diag(np.cos(k))
corners = [np.array(k, float)*np.pi for k in np.ndindex(2,2,2)]
chi = {tuple(k): int(np.sign(np.linalg.det(J_w(k)))) for k in corners}
pi3 = np.array([np.pi,np.pi,np.pi])
ok_swap = all(chi[tuple(k)] == -chi[tuple(((k+pi3)%(2*np.pi)))] for k in corners)
print("A2: walker nodes: R =", sum(1 for v in chi.values() if v>0), " L =", sum(1 for v in chi.values() if v<0))
print("    eps H eps = -H exactly (sin(k+pi) = -sin k):", np.allclose(d_w(pi3+0.3), -d_w(np.array([0.3]*3))))
print("    eps maps node chirality chi -> -chi at every corner:", ok_swap)

# A3: intertwiners Hom_SU(2)(1/2 , 0): solve T = 0 constraint [rho(J_a) T - T*0] i.e. T (1 x 2) with J_a^T? use generators
s = [np.array([[0,1],[1,0]])/2, np.array([[0,-1j],[1j,0]])/2, np.array([[1,0],[0,-1]])/2]
# T: C^1 <- C^2 (row vector t), invariance: t @ s_a = 0 for all a
A = np.vstack([np.kron(np.eye(1), s[a].T) for a in range(3)])  # constraints on t
print("A3: dim Hom_SU(2)(doublet -> singlet) =", 2 - np.linalg.matrix_rank(A))
