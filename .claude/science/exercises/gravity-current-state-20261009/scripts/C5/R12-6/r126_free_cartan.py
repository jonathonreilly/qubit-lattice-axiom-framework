"""C5 R12-6, script 1: quadratic (free) content of the equivariant (Cartan) gauged SUSY-QM law, built from the supercharge
   Q = sum_a psi_a^+ (p_a - i d_aW) + i sum_s sigma_s (v_s . psi) + c sum_s eta_s pi_{sigmabar,s},   c = 2*lam,
with W = lam*(<B,dA> + <tau,dB>) + (1/2)<phi, M_A phi>, v_s = gauge vector field of a unit gauge parameter at site s
(v_s = d0 delta_s on links, e J phi_s on matter).  Hand algebra (report section 3.1) gives
   Q^2 = i sum_s sigma_s L_s   (L_s = Gauss generator incl. fermions),   H = (1/2){Q,Q^+} >= 0, local.
Quadratic part of H at phi = 0, sigma = 0 (read off from the hand algebra):
   fermions:  psi^+ HessW psi  +  [ (c/2) (v_s.psi^+) eta_s + h.c. ]  ->  one-particle operator on (eta, psi_A, psi_B, psi_tau)
              = lam * [[0,d0^+,0,0],[d0,0,d1^+,0],[0,d1,0,d2^+],[0,0,d2,0]]  =  lam * K   (Kaehler-Dirac)
   bosons:    (1/2)|E|^2 + (1/2) lam^2 |C x|^2 on (A,B,tau) with Gauss law; sigma: (|c|^2/2)|pi_sigma|^2 + (1/2)|d0 sigma|^2.
Checks: (1) the assembled fermion operator equals R12-3's C_kd and K^2 = Delta*1_8 (cochain and box symbols);
        (2) boson frequencies: 6 physical (A_T 2, B 3, tau 1) at lam^2 Delta from (lam C)^2 on the gauge quotient, sigma
            (complex, 2 real) at (|c|^2/4) Delta = lam^2 Delta;  one-particle state count per q: bosons 8 = fermions 8;
        (3) the lam-family: every member has the same Q-structure (Q^2 independent of lam, c) and gauge-multiplet speed lam.
"""
import numpy as np, io, contextlib, sys
sys.path.insert(0, '.')
with contextlib.redirect_stdout(io.StringIO()):
    import r123_bf_multiplet as M
rng = np.random.default_rng(126)

def d_ops(D):
    d0 = np.array(D, complex).reshape(3, 1)
    d1 = np.zeros((3, 3), complex)
    for r, (j, k) in enumerate(M.PAIRS):
        d1[r, k] += D[j]; d1[r, j] -= D[k]
    d2 = np.array([[D[0], D[1], D[2]]], complex)
    return d0, d1, d2

def fermion_op(D, lam=1.0):
    d0, d1, d2 = d_ops(D)
    K = np.zeros((8, 8), complex)           # order: eta(1), A(3), B(3), tau(1)
    K[1:4, 0:1] = d0; K[0:1, 1:4] = d0.conj().T      # Cartan hopping (v.psi^+) eta, v_s = d0 delta_s
    K[4:7, 1:4] = d1; K[1:4, 4:7] = d1.conj().T      # Hess of <B,dA>
    K[7:8, 4:7] = d2; K[4:7, 7:8] = d2.conj().T      # Hess of <tau,dB>
    return lam * K

e_kd = e_sq = 0; nb_ok = True; worst = 0
for _ in range(400):
    q = rng.uniform(-np.pi, np.pi, 3)
    for Df in (M.Dwil, M.Dbox):
        D = Df(q); Dl = np.sum(np.abs(D) ** 2)
        for lam in (1.0, 0.7):
            K = fermion_op(D, lam)
            if lam == 1.0:
                e_kd = max(e_kd, np.abs(K - M.C_kd(D)).max())
            e_sq = max(e_sq, np.abs(K @ K - lam ** 2 * Dl * np.eye(8)).max())
            # bosons on the gauge quotient: (lam C_bf)^2 restricted to the complement of the gauge direction (d0,0,0)
            C = lam * M.C_bf(D)
            g = np.zeros(7, complex); g[:3] = D; g /= np.linalg.norm(g)
            Pphys = np.eye(7) - np.outer(g, g.conj())
            wb = np.linalg.eigvalsh(Pphys @ C @ C @ Pphys)
            wb = np.sort(wb)[1:]                                    # drop the gauge zero
            c = 2 * lam
            w_sigma = (abs(c) ** 2 / 4) * Dl                        # complex sigma: H = (|c|^2/2)|pi|^2 + (1/2)|d0 sigma|^2
            wbos = np.concatenate([wb, [w_sigma, w_sigma]])        # 6 + 2 = 8 real bosonic oscillators per q
            wfer = np.linalg.eigvalsh(K)                            # 8 one-particle fermion levels: 4 particles + 4 holes
            worst = max(worst, np.abs(np.sort(wbos) - lam ** 2 * Dl).max(), np.abs(np.sort(np.abs(wfer)) ** 2 - lam ** 2 * Dl).max())
            nb_ok &= (len(wbos) == 8 and len(wfer) == 8)
print('(1) assembled Cartan fermion operator == R12-3 C_kd (lam=1): max diff %.1e ; max|K^2 - lam^2 Delta 1_8| = %.1e' % (e_kd, e_sq))
print('(2) all 8 bosonic frequencies^2 and all 8 fermionic |levels|^2 equal lam^2*Delta: max dev %.1e ; counts 8=8: %s' % (worst, nb_ok))
# (3) doubler scan of the assembled operator (box symbol), lam = 1
N = 24; ks = (np.arange(N) + 0.5) * 2 * np.pi / N - np.pi
mins = []
for a in ks:
    for b in ks:
        for cc in ks:
            q = np.array([a, b, cc]); D = M.Dbox(q)
            ev = np.abs(np.linalg.eigvalsh(fermion_op(D)))
            mins.append((ev.min(), np.linalg.norm(q)))
mins = np.array(mins)
far = mins[mins[:, 1] > 1.0]
print('(3) box symbol, N=24 grid: min |level| over grid = %.4f (at |q| = %.3f); min |level| for |q|>1: %.4f  -> zeros only at q=0'
      % (mins[:, 0].min(), mins[np.argmin(mins[:, 0]), 1], far[:, 0].min()))
# (4) box photon inside the plateau: |level| = |q| exactly
q = np.array([0.31, -0.22, 0.17]); D = M.Dbox(q)
print('(4) box symbols inside the plateau, q=(0.31,-0.22,0.17): |levels| =', np.round(np.abs(np.linalg.eigvalsh(fermion_op(D))), 12), ' |q| = %.12f' % np.linalg.norm(q))
