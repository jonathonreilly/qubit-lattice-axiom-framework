"""T02 script B: Connes-Rovelli thermal time as a dynamics selector (outside route).
Two adjacent unrecorded qubits x,y with fields h_x,h_y from fixed neighbouring records and the
Heisenberg bond J s_x.s_y (the landed compressed generator).  Modular Hamiltonian K = -log rho.
(a) rho = product of the one-site marginals (all the Admissibility odds supply per site)
(b) rho = joint Gibbs state exp(-beta H)/Z (what the dynamics clause would supply)
Question: does (a) select any interaction?  Measure: operator Schmidt rank of exp(-iKt),
and the two-body Pauli content of K."""
import numpy as np, scipy.linalg as sl
rng = np.random.default_rng(7)
sx=np.array([[0,1],[1,0]],complex); sy=np.array([[0,-1j],[1j,0]]); sz=np.array([[1,0],[0,-1]],complex); I2=np.eye(2)
S=[sx,sy,sz]
def kron(a,b): return np.kron(a,b)
def ptrace(rho, keep):
    r = rho.reshape(2,2,2,2)
    return np.einsum('abcb->ac', r) if keep==0 else np.einsum('abad->bd', r)
def opschmidt(U, tol=1e-9):
    M = U.reshape(2,2,2,2).transpose(0,2,1,3).reshape(4,4)
    s = np.linalg.svd(M, compute_uv=False)
    return int(np.sum(s>tol*s[0])), s
def pauli_coeffs(K):
    out = {}
    P = [I2]+S
    for a in range(4):
        for b in range(4):
            out[(a,b)] = np.trace(kron(P[a],P[b]).conj().T @ K).real/4
    return out
for J in (1.0, -1.0):
    hx = rng.normal(size=3); hy = rng.normal(size=3)
    H = J*sum(kron(S[a],S[a]) for a in range(3)) + kron(sum(hx[a]*S[a] for a in range(3)), I2) + kron(I2, sum(hy[a]*S[a] for a in range(3)))
    beta = 0.9
    rho = sl.expm(-beta*H); rho /= np.trace(rho)
    rx, ry = ptrace(rho,0), ptrace(rho,1)
    rprod = kron(rx, ry)
    Kp = -sl.logm(rprod); Kj = -sl.logm(rho)
    t = 0.7
    rk_p, sp = opschmidt(sl.expm(-1j*Kp*t)); rk_j, sj = opschmidt(sl.expm(-1j*Kj*t))
    cp, cj = pauli_coeffs(Kp), pauli_coeffs(Kj)
    two_p = max(abs(cp[(a,b)]) for a in range(1,4) for b in range(1,4))
    two_j = [cj[(a,a)] for a in range(1,4)]
    print(f"J={J:+.0f}: op-Schmidt rank product-of-marginals flow = {rk_p} (sv {np.round(sp,3)}), joint-Gibbs flow = {rk_j}")
    print(f"      max two-body Pauli coefficient in K(product of marginals) = {two_p:.2e};  K(joint) diagonal two-body = {np.round(two_j,4)}, beta*J = {beta*J:+.4f}")
    # correlations: does the product state's flow change the entanglement of a product input? (rank 1 => no)
print("Reading: product-of-marginals flow is a product of one-site precessions (rank 1); the coupling J is returned only by the joint Gibbs state, i.e. by the dynamics it was meant to select.")
