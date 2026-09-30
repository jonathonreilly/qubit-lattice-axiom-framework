"""T38 test 5 (added after Test 4, not pre-registered as a pass/fail gate): what a C3-covariant dynamics can and cannot
supply for the sector weights nu = (nu_s, nu_d), with r = nu_d/(2 nu_s) (the supplied 'energy shares ~ sector weight' map).
Scope: Weyl-Heisenberg (Pauli) covariant channels and classical detailed-balance generators on the C-eigenlines.
Run: python3 t38_dynamics.py"""
import numpy as np
rng = np.random.default_rng(20260929)
w = np.exp(2j*np.pi/3)
C = np.array([[0,0,1],[1,0,0],[0,1,0]], dtype=complex)
D = np.diag([1, w, w**2])
def Wop(m, n): return np.linalg.matrix_power(C, m) @ np.linalg.matrix_power(D, n)
# Fourier eigenbasis of C, ordered so C v_k = w^k v_k
V = np.array([[w**(-k*j) for k in range(3)] for j in range(3)])/np.sqrt(3)
ev = [np.argmin([abs(np.vdot(V[:,kk], C@V[:,kk]) - w**k) for kk in range(3)]) for k in range(3)]
V = V[:, ev]
P = [np.outer(V[:,k], V[:,k].conj()) for k in range(3)]     # character projectors
Pi_s, Pi_d = P[0], P[1]+P[2]                                  # singlet, doublet central projectors

def channel_fixed_points(probs):
    # Pauli channel Phi(rho) = sum p_mn W_mn rho W_mn^dag ; superoperator on vec(rho)
    S = np.zeros((9,9), dtype=complex)
    for (m,n),p in probs.items():
        W = Wop(m,n); S += p*np.kron(W, W.conj())
    vals, vecs = np.linalg.eig(S)
    idx = np.where(abs(vals-1) < 1e-9)[0]
    return len(idx), vecs[:, idx]

print("== (1) unital covariant channel with D-type Kraus operators (mixes Fourier lines): unique fixed point I/3")
probs1 = {(0,0):0.4, (0,1):0.3, (1,0):0.2, (0,2):0.1}
nfix, fp = channel_fixed_points(probs1)
rho = fp[:,0].reshape(3,3); rho = rho/np.trace(rho)
ns, nd = np.trace(Pi_s@rho).real, np.trace(Pi_d@rho).real
print(f"   fixed-point multiplicity {nfix}; sector weights (singlet, doublet) = ({ns:.4f},{nd:.4f}); r = nd/(2 ns) = {nd/(2*ns):.4f}")
ok1 = nfix == 1 and abs(ns-1/3) < 1e-9 and abs(nd-2/3) < 1e-9

print("== (2) same but Kraus operators diagonal in the Fourier basis only (C-powers): charge conserved, fixed points = all sector-diagonal states")
probs2 = {(0,0):0.5, (1,0):0.3, (2,0):0.2}
nfix2, fp2 = channel_fixed_points(probs2)
print(f"   fixed-point multiplicity {nfix2} (= number of conserved character projectors): sector weights are initial data (any (q0,q1,q2))")
ok2 = nfix2 == 3

print("== (3) classical detailed-balance generator on the C-eigenlines (non-unital), E_1 = E_2 = E_0 + Delta")
def stationary(Delta, beta=1.0):
    E = np.array([0.0, Delta, Delta]); wts = np.exp(-beta*E)
    # Metropolis rates between all pairs
    Wm = np.zeros((3,3))
    for i in range(3):
        for j in range(3):
            if i != j: Wm[j,i] = min(1.0, wts[j]/wts[i])
    Wm -= np.diag(Wm.sum(0))
    vals, vecs = np.linalg.eig(Wm)
    q = np.real(vecs[:, np.argmin(abs(vals))]); return q/q.sum()
for Delta in (0.0, np.log(2), 1.0, 2.0):
    q = stationary(Delta)
    nu_s, nu_d = q[0], q[1]+q[2]
    print(f"   beta*Delta = {Delta:5.3f}: stationary q = {np.round(q,4)}; sector weights ({nu_s:.4f},{nu_d:.4f}); r = {nu_d/(2*nu_s):.4f}  [= exp(-beta Delta) = {np.exp(-Delta):.4f}]")
q = stationary(np.log(2))
ok3 = abs((q[1]+q[2])/(2*q[0]) - 0.5) < 1e-9
print("   -> r = 1/2 needs beta*Delta = ln 2: a tuned free parameter of the dynamics (or the initial charge populations), not an output.")
print("   -> Delta = 0 (no preferred sector, unital) returns r = 1.")

print(f"\nchecks: unital-ergodic => (1/3,2/3), r=1: {ok1};  charge-conserving => populations free: {ok2};  thermal r = exp(-beta Delta): {ok3}")
