"""R13-4 (i) Theorem NL, fermion-algebra part, checked in an explicit Fock space at a fixed boson point.
Sites x, y (and a spectator link fermion); matter phi_x, phi_y in R^n (n = 4 and 6), J block complex structure.
Modes: link fermion psi_A (1) + n at x + n at y.  u_x = (-1, eJphi_x, 0), u_y = (+1, 0, eJphi_y); iota_s = u_s . psi.
N_x = number operator on W_x = span(phi_x, J phi_x)^perp.  X_t = i sum T_t^{ab} psi_a psi_b (T_t = eJ at t).
Checks: [N_x, iota_s] = [N_x, iota_s^dag] = 0;  [[S, N_x], N_y] = -4 g^-1_xy (X_x^W dag X_y^W + h.c.)
for S = sum_st X_s^dag g^-1_st X_t;  ||X^W dag |0>||^2 = 4 e^2 (n-2)/2."""
import numpy as np
import scipy.sparse as sps
rng = np.random.default_rng(7)

def jw(nm):
    I2, Z = sps.identity(2, format='csr'), sps.diags([1., -1.]).tocsr(); a = sps.csr_matrix(np.array([[0., 1.], [0., 0.]]))
    ops = []
    for j in range(nm):
        m = sps.csr_matrix(np.array([[1.]]))
        for k in range(nm):
            m = sps.kron(m, Z if k < j else (a if k == j else I2), format='csr')
        ops.append(m.astype(complex))
    return ops   # annihilators

def Jmat(n):
    J = np.zeros((n, n))
    for b in range(n//2):
        J[2*b, 2*b+1] = -1; J[2*b+1, 2*b] = 1
    return J

out = []
def pr(*a):
    s = " ".join(str(x) for x in a); print(s); out.append(s)

e = 0.7
for n in [4, 6]:
    nm = 1 + 2*n
    c = jw(nm); cd = [m.conj().T.tocsr() for m in c]
    J = Jmat(n)
    phx, phy = rng.normal(size=n), rng.normal(size=n)
    ux = np.concatenate([[-1.], e*J@phx, np.zeros(n)])
    uy = np.concatenate([[1.], np.zeros(n), e*J@phy])
    g = np.array([[ux@ux, ux@uy], [uy@ux, uy@uy]]); gi = np.linalg.inv(g)
    def lin(v, ops): return sum(v[a]*ops[a] for a in range(nm) if v[a] != 0)
    iota = [lin(ux, c), lin(uy, c)]
    def Wproj(ph):
        B = np.stack([ph/np.linalg.norm(ph), J@ph/np.linalg.norm(ph)], 1)
        return np.eye(n) - B@B.T
    Px, Py = Wproj(phx), Wproj(phy)
    def number(P, off):
        return sum(P[a, b]*cd[off+a]@c[off+b] for a in range(n) for b in range(n) if abs(P[a, b]) > 1e-15)
    Nx, Ny = number(Px, 1), number(Py, 1+n)
    def Xop(T, off):   # i sum T_ab psi_a psi_b
        return 1j*sum(T[a, b]*c[off+a]@c[off+b] for a in range(n) for b in range(n) if T[a, b] != 0)
    Xx, Xy = Xop(e*J, 1), Xop(e*J, 1+n)
    XxW, XyW = Xop(e*Px@J@Px, 1), Xop(e*Py@J@Py, 1+n)
    S = sum(gi[s, t]*[Xx, Xy][s].conj().T@[Xx, Xy][t] for s in range(2) for t in range(2))
    comm = lambda A, B: A@B - B@A
    c1 = max(abs(comm(Nx, io)).max() for io in iota + [m.conj().T for m in iota])
    lhs = comm(comm(S, Nx), Ny)
    rhs = -4*gi[0, 1]*(XxW.conj().T@XyW + XyW.conj().T@XxW)
    vac = np.zeros(2**nm); vac[0] = 1.0   # all modes empty (JW basis state 0 = |0...0> with a=[[0,1],[0,0]] acting on index 1)
    vac = np.zeros(2**nm); vac[-1] = 0;
    # find the Fock vacuum: state annihilated by all c
    Ntot = sum(cd[j]@c[j] for j in range(nm)); dg = Ntot.diagonal().real; v0 = np.zeros(2**nm, complex); v0[np.argmin(dg)] = 1
    nrm2 = np.linalg.norm(XxW.conj().T@v0)**2
    pr(f"n={n}: max|[N_x, iota_s^(dag)]| = {c1:.1e};  |[[S,N_x],N_y] - (-4 g^-1_xy)(X_x^W+ X_y^W + h.c.)| = "
       f"{abs(lhs - rhs).max():.1e} (scale {abs(lhs).max():.3f});  g^-1_xy = {gi[0,1]:.4f};  "
       f"||X^W+|0>||^2 = {nrm2:.4f} vs 4e^2(n-2)/2 = {4*e*e*(n-2)/2:.4f}")
pr("For R12-3's matter (n = 16): ||X^W+|0>||^2 = 4 e^2 * 7 = 28 e^2, so the matrix element of 2 g^-1 (X^W+X^W + h.c.) is 56 e^2 g^-1_xy.")
with open(__file__.replace('.py', '.out'), 'w') as f:
    f.write("\n".join(out) + "\n")
