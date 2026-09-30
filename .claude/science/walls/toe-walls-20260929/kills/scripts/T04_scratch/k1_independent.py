#!/usr/bin/env python3
"""Kill-check T04, script k1. Independent extraction of the effective 4-state
distinguishable Hamiltonian by exact diagonalisation (des Cloizeaux/Loewdin), not
by the attacker's Schrieffer-Wolff formulas. Uses the attacker's model definitions
(sites, hops, energies) only.
Checks: (i) a1, a2, cex from ED vs attack SW values; (ii) distinguishable low-space
spectrum = union of boson and fermion spectra (exchange P commutes with H);
(iii) interference of the four distinguishable states (cex nonzero => the two
'final arrangements' are not incoherent)."""
import sys, numpy as np
sys.path.insert(0, '/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/walls/attacks/T04_scratch')
import ring_flip_identity as R

def eff_ED(H, Pidx):
    """des Cloizeaux effective Hamiltonian on the model space Pidx from the lowest len(Pidx) eigenvectors."""
    w, U = np.linalg.eigh(H)
    m = len(Pidx)
    Uk = U[:, :m]
    C = Uk[Pidx, :]                       # projection of eigvecs on model space (m x m)
    # Loewdin orthonormalisation of projected eigenvectors
    S = C.T @ C
    ev, evec = np.linalg.eigh(S)
    Sm12 = evec @ np.diag(ev ** -0.5) @ evec.T
    Ct = C @ Sm12                          # orthonormal columns (rotation)
    return Ct @ np.diag(w[:m]) @ Ct.T      # H_eff in model-space basis

def run(model, Dv, Dc, U, t):
    R.MODEL = model
    Bd, ixd, H0d, Vd = R.build_dist(t, Dv, Dc, U)
    Pd = R.low_indices(Bd, 'D')
    lab = [Bd[i] for i in Pd]
    H = H0d + Vd
    Heff = eff_ED(H, Pd)
    # remove the (identical) 2nd-order scalar: use the diagonal average
    scal = np.trace(Heff) / len(Pd)
    Hs = Heff - scal * np.eye(len(Pd))
    def el(dst, src): return Hs[lab.index(dst), lab.index(src)] / t ** 4
    a1 = el(('l', 't'), ('b', 'r')); a2 = el(('t', 'l'), ('b', 'r')); cex = el(('r', 'b'), ('b', 'r'))
    cexB = el(('t', 'l'), ('l', 't'))
    # boson/fermion sectors
    Bb, ixb, H0b, Vb = R.build_identical('B', t, Dv, Dc, U); Pb = R.low_indices(Bb, 'B')
    Bf, ixf, H0f, Vf = R.build_identical('F', t, Dv, Dc, U); Pf = R.low_indices(Bf, 'F')
    wb = np.linalg.eigvalsh(H0b + Vb)[:2]; wf = np.linalg.eigvalsh(H0f + Vf)[:2]
    wd = np.linalg.eigvalsh(H0d + Vd)[:4]
    union = np.sort(np.concatenate([wb, wf]))
    return a1, a2, cex, cexB, wd, union

for model in ('U', 'ice'):
    print('MODEL', model)
    for p in [(1,1,1),(1,0.5,1),(1,4,1)]:
        for t in (0.02, 0.01):
            a1, a2, cex, cexB, wd, union = run(model, *p, t)
            print(f" {p} t={t}: a1={a1:.4f} a2={a2:.4f} cex(A)={cex:.4f} cex(B)={cexB:.4f}   "
                  f"max|spec_dist - spec_(B u F)| = {np.max(np.abs(wd-union)):.2e}")
