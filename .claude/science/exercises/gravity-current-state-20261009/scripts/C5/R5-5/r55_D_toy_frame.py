"""R5-5 (D): toy check of the frame-superposition identities (finite frame set; exact linear algebra).
Frames u_i, i=1..NF, equally spaced on the 1+1 analog's quotient circle (length eta0 = ln(8+3 sqrt7)); orthonormal labels |u_i>.
Matter: a two-arm interferometer (modes |1>,|2>), branch Hamiltonian diag(w1(u), w2(u)), w_a(u) = wbar_a + s_a * eps(u),
eps(u) = cos(2 pi u/eta0) (lowest quotient mode; R4-1's deviation is a sum of such modes).
(1) frame-diagonal coupling, any frame phases: matter reduced state == classical mixture over frames (Q1 Thm A analog);
(2) visibility == |E_u exp(-i (w1-w2)(u) T)|; frame coherence <u|rho_F|u'> multiplied by the matter overlap D(u,u');
(3) adding a frame Hamiltonian H_F = E_F (1 - |c><c|) with |c> the uniform (invariant) state: for E_F >> coupling the matter
    sees the MEAN law (adiabatic elimination) and the frame stays in |c>; for E_F = 0 (what Poincare covariance forces on the
    orientation sector, Lemma P0) the visibility decays.
"""
import numpy as np
from scipy.linalg import expm
eta0 = np.log(8 + 3*np.sqrt(7)); NF = 64
u = (np.arange(NF) + 0.5)*eta0/NF; eps = np.cos(2*np.pi*u/eta0)
rng = np.random.default_rng(1)
s1, s2 = 1.0, -0.6           # sensitivities of the two arms to the frame (arbitrary, unequal)
w1bar, w2bar = 0.3, 0.0
def run(EF, T, phases='random'):
    psiF = np.exp(1j*(rng.uniform(0, 2*np.pi, NF) if phases == 'random' else np.zeros(NF)))/np.sqrt(NF)
    c = np.ones(NF)/np.sqrt(NF)
    HF = EF*(np.eye(NF) - np.outer(c, c))
    Hint = np.zeros((2*NF, 2*NF))
    for i in range(NF):
        Hint[2*i, 2*i] = w1bar + s1*eps[i]; Hint[2*i+1, 2*i+1] = w2bar + s2*eps[i]
    H = np.kron(HF, np.eye(2)) + Hint
    chi = np.array([1, 1])/np.sqrt(2)
    Psi = expm(-1j*H*T) @ np.kron(psiF, chi)
    Psi = Psi.reshape(NF, 2)
    rhoM = Psi.T @ Psi.conj()            # matter reduced state
    rhoF = Psi @ Psi.conj().T            # frame reduced state
    return psiF, rhoM, rhoF, c
print("(1)+(2) EF = 0 (frame-diagonal, no frame dynamics):")
for T in (0.5, 2.0, 8.0, 32.0):
    psiF, rhoM, rhoF, c = run(0.0, T)
    mix = np.zeros((2, 2), complex)
    for i in range(NF):
        U = np.diag(np.exp(-1j*np.array([w1bar + s1*eps[i], w2bar + s2*eps[i]])*T)); chi = np.array([1, 1])/np.sqrt(2)
        mix += abs(psiF[i])**2*np.outer(U @ chi, (U @ chi).conj())
    V = 2*abs(rhoM[0, 1]); Vpred = abs(np.mean(np.exp(-1j*((w1bar-w2bar) + (s1-s2)*eps)*T)))
    # frame coherence between u_0 and u_k vs matter overlap
    i, k = 0, NF//4
    Dpred = abs(0.5*(np.exp(1j*(s1*(eps[i]-eps[k]))*T) + np.exp(1j*(s2*(eps[i]-eps[k]))*T)))
    Dnum = abs(rhoF[i, k])/(abs(psiF[i])*abs(psiF[k]))
    print(f"  T={T:5.1f}: |rhoM - mixture| = {np.abs(rhoM-mix).max():.1e};  visibility {V:.6f}  vs |E exp(-i dw T)| {Vpred:.6f};"
          f"  frame coherence |rhoF(u0,u16)|/|psi psi| = {Dnum:.6f} vs matter overlap {Dpred:.6f}")
print("\n(3) gapped frame Hamiltonian EF (NOT available under Poincare covariance, Lemma P0), T = 32:")
for EF in (0.0, 0.3, 1.0, 3.0, 10.0, 30.0):
    psiF, rhoM, rhoF, c = run(EF, 32.0, phases='none')
    V = 2*abs(rhoM[0, 1]); phase = -np.angle(rhoM[0, 1])
    meanphase = ((w1bar - w2bar) + (s1 - s2)*eps.mean())*32.0
    corr = -(s1**2 - s2**2)*eps.var()*32.0/EF if EF > 0 else 0.0   # 2nd-order (virtual frame excitation) shift
    print(f"  EF={EF:5.1f}: visibility {V:.4f};  frame fidelity with invariant |c> {np.real(c @ rhoF @ c):.4f};  "
          f"relative phase {np.mod(phase, 2*np.pi):.4f} vs mean-law {np.mod(meanphase, 2*np.pi):.4f}"
          f" (+2nd-order shift: {np.mod(meanphase + corr, 2*np.pi):.4f})")
