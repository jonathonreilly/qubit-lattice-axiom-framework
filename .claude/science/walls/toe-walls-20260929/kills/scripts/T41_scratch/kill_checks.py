#!/usr/bin/env python3
"""Kill-check scratch for T41. Reads (never writes) the repo checkout. Sonnet 5.5, same family as attacker."""
import os, sys, math, itertools
sys.dont_write_bytecode = True
import numpy as np
import warnings; warnings.filterwarnings("ignore")
MAIN = ("/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--"
        "claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/main_wt")
sys.path.insert(0, os.path.join(MAIN, "scripts"))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import importlib.util
spec = importlib.util.spec_from_file_location("t41", os.path.join(os.path.dirname(os.path.abspath(__file__)), "rerun_t41.py"))
t41 = importlib.util.module_from_spec(spec); spec.loader.exec_module(t41)
rng = np.random.default_rng(1)
wrap = t41.wrap

print("=== K1: S3 has no failure mode. |det O| depends only on singular values of m and B; ANY unitary-rephased family passes ===")
B = t41.rand_cplx(7, 6)
m0 = t41.rand_cplx(3, 3)
spreads = []
for trial in range(5):
    U = t41.rand_unitary(3); V = t41.rand_unitary(3)
    vals = []
    for phi in np.linspace(-3, 3, 9):
        Uphi = np.diag(np.exp(1j*phi*rng.normal(size=3))) @ U
        m = Uphi @ m0 @ V          # arbitrary phi-dependent left rotation, same singular values
        # rebuild with m0's singular values: left unitary rotation keeps m m^dag spectrum
        sgn, ld = np.linalg.slogdet(t41.build_O(B, m))
        vals.append(ld)
    spreads.append(max(vals)-min(vals))
# Note left-rotation changes m m^dag by unitary conjugation only -> same spectrum; but det(mm^dag + s^2) spectrum-only
print("  max spread of log|det O| under arbitrary phi-dependent unitary rephasing of m:", max(spreads))
# control: a phase-sensitive K-even probe: cos(arg det O)
ph = []
for phi in np.linspace(-1.5, 1.5, 7):
    m = np.diag([np.exp(1j*phi),1,1]) @ (np.eye(3)*1.2)
    sgn, ld = np.linalg.slogdet(t41.build_O(B, m)); ph.append(math.cos(np.angle(sgn)))
print("  cos(arg det O) (K-even, non-multiplicative) spread:", max(ph)-min(ph), " -> excluded by the class DEFINITION (multiplicativity), not by any test")

print("=== K2: same complex flavor matrix, two couplings on the balanced 4^3 surface ===")
K, eps = t41.build_K(4, 7); N = 64
m = 0.8*(t41.rand_cplx(3,3))
op_a = np.kron(K, np.eye(3)) + np.kron(np.eye(N), m)                 # repo coupling (07-01 note): K (x) 1 + 1 (x) A
Pp = np.diag((1+eps)/2); Pm = np.diag((1-eps)/2)
op_b = np.kron(K, np.eye(3)) + np.kron(Pp, m) + np.kron(Pm, m.conj().T)   # eps-graded (m on even, m^dag on odd)
for name, op in (("repo coupling K(x)1+1(x)A, generic complex A", op_a), ("eps-graded (m,m^dag), same A", op_b)):
    s, l = np.linalg.slogdet(op); print(f"  {name}: arg det = {np.angle(s):+.4f}, arg det A = {np.angle(np.linalg.det(m)):+.4f}")
Ah = (m + m.conj().T)/2
s, l = np.linalg.slogdet(np.kron(K, np.eye(3)) + np.kron(np.eye(N), Ah)); print(f"  repo coupling, Hermitian part of A: arg det = {np.angle(s):+.2e}  (K-reality is what kills the phase in the repo's coupling)")

print("=== K3: quark carriers are Hermitian by construction; det channel is K-constant trivially; the atlas constants fix the sign bit ===")
import frontier_quark_cp_carrier_completion as qc
from frontier_quark_mass_ratio_full_solve import (C12_D, C12_U, C23_D, C23_U, R_DB, R_SB)
r_uc, r_ct = 1.688494e-3, 7.400356e-3
xi_u, xi_d = complex(0.340735, -0.063203), complex(0.078186, 0.108371)
m_u, m_c, m_t = r_uc*r_ct, r_ct, 1.0
m_d, m_s, m_b = R_DB, R_SB, 1.0
c13u = C12_U*C23_U*math.sqrt(m_u/m_t) + xi_u
c13d = C12_D*C23_D*math.sqrt(m_d/m_b) + xi_d
Mu = qc.build_nni_with_complex_13(m_u, m_c, m_t, C12_U, C23_U, c13u)
Md = qc.build_nni_with_complex_13(m_d, m_s, m_b, C12_D, C23_D, c13d)
print("  Hermitian?", np.allclose(Mu, Mu.conj().T), np.allclose(Md, Md.conj().T))
print("  det(Mu), det(conj Mu):", np.linalg.det(Mu), np.linalg.det(Mu.conj()))
print("  -> for a Hermitian block det is real, so det-channel K-constancy holds for ANY Hermitian carrier (lepton or quark); S5's gauge-relabeling test is stronger than orbit-indexing of the det channel")
print("  sign of det(Mu*Md) vs the imported constant c12_u (others fixed):")
for c12 in (0.9, 1.0, 1.2, 1.48):
    Mu_c = qc.build_nni_with_complex_13(m_u, m_c, m_t, c12, C23_U, C12_U*C23_U*math.sqrt(m_u/m_t)*0 + c12*C23_U*math.sqrt(m_u/m_t)+xi_u)
    e = np.linalg.eigvalsh(Mu_c)
    print(f"    c12_u={c12}: eig signs {np.sign(e).astype(int)}, arg det(Mu Md) = {np.angle(np.linalg.det(Mu_c)*np.linalg.det(Md)):+.3f}")
print("  -> the sign bit IS fixed by the atlas texture (an imported constant); it is invisible to |V|,J,masses only because those come from M M^dag = M^2")
print("=== K4: sign flips leave M M^dag fixed identically (algebra) ===")
ev, W_ = np.linalg.eigh(Mu)
for s in ([1,1,1],[-1,1,1],[-1,-1,1]):
    M2 = W_ @ np.diag(ev*np.array(s)) @ W_.conj().T
    print("  max|M2 M2^dag - Mu Mu^dag| =", np.max(np.abs(M2@M2.conj().T - Mu@Mu.conj().T)))
