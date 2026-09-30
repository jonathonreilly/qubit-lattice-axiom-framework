#!/usr/bin/env python3
"""T36 P3 (redo with proper small-p scaling): in the supplied corner model the light (hw=0) state's
quadratic dispersion tensor is the INVERSE of the triplet mass matrix. Pre-registration: PREREGISTRATION.md."""
import numpy as np
rng = np.random.default_rng(7)
I2 = np.eye(2, dtype=complex); SX = np.array([[0,1],[1,0]],dtype=complex)
SY = np.array([[0,-1j],[1j,0]],dtype=complex); SZ = np.diag([1,-1]).astype(complex)
def kr(*ms):
    o = np.array([[1.0+0j]])
    for m in ms: o = np.kron(o, m)
    return o
XI  = [kr(SX,I2,I2), kr(SZ,SX,I2), kr(SZ,SZ,SX)]
GAM = [kr(SY,I2,I2), kr(SZ,SY,I2), kr(SZ,SZ,SY)]
HW = np.array([bin(s).count("1") for s in range(8)])
axis_state = [4, 2, 1]
def Hbloch(q):
    return sum((1+np.cos(q[a]))*XI[a] + np.sin(q[a])*GAM[a] for a in range(3))
def branch_energy(p, D):
    w, U = np.linalg.eigh(Hbloch(np.pi + np.asarray(p)) + D)
    return w[int(np.argmax(np.abs(U[0,:])**2))]
def build_D(M1, heavy=5.0):
    D = np.zeros((8,8), dtype=complex)
    for s in range(8):
        if HW[s] >= 2: D[s,s] = heavy
    for i,a in enumerate(axis_state):
        for j,b in enumerate(axis_state):
            D[a,b] = M1[i,j]
    return D
print("A) diagonal triplet masses m_a = 2 r_a, p along axis a, p = 0.01 m_a  (E0 = -p^2/m_a)")
for name, m in {"isotropic (1,1,1)": (1,1,1), "(1,1e-2,1e-4)": (1,1e-2,1e-4), "up-type-like (1, 7.4e-3, 7.5e-6)": (1,7.4e-3,7.5e-6)}.items():
    D = build_D(np.diag(m).astype(complex))
    out = []
    for a in range(3):
        p = np.zeros(3); p[a] = 0.01*m[a]
        E = branch_energy(p, D); out.append(-E/(p[a]**2/m[a]))
    print(f"  {name:34s} E0_exact / E0_pred per axis = {np.round(out,6)}")
print("\nB) generic Hermitian triplet mass matrix with hierarchical eigenvalues (random unitary frame)")
for m in [(1,0.5,0.25), (1, 7.4e-3, 7.5e-6)]:
    Q,_ = np.linalg.qr(rng.normal(size=(3,3))+1j*rng.normal(size=(3,3)))
    M1 = Q @ np.diag(m) @ Q.conj().T
    D = build_D(M1)
    worst = 0
    for _ in range(8):
        p = rng.normal(size=3); p = p/np.linalg.norm(p)*0.01*min(m)
        E = branch_energy(p, D)
        Hp = -sum(p[a]*GAM[a] for a in range(3))
        v = np.array([Hp[axis_state[a],0] for a in range(3)])
        Ep = -(v.conj() @ np.linalg.inv(M1) @ v).real
        worst = max(worst, abs(E/Ep-1))
    print(f"  masses {m}:  worst |E_exact/E_pred - 1| over 8 directions = {worst:.2e}")
    Kev = np.linalg.eigvalsh(np.linalg.inv(M1))
    print(f"     mass eigenvalues {np.linalg.eigvalsh(M1)};   light-state stiffness eigenvalues {Kev}; stiffness spread max/min = {Kev.max()/Kev.min():.3g}")
