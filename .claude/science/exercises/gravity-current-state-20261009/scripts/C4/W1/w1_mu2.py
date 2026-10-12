"""W1 main: mu2(c) = -(1/24)[A + 4 c.L + 2 c^T Q c] for onsite phi^4 (V=1) and for NN phi^2phi^2 (V'),
general local quartic dressings of l1-diameter <= r projected on E / T2. L-convergence over L."""
import numpy as np, sys, time
from w1_core import *
m = float(sys.argv[1]) if len(sys.argv) > 1 else 1.0
Ls = [int(a) for a in sys.argv[2].split(',')] if len(sys.argv) > 2 else [12, 16, 20, 24]
rs = [int(a) for a in sys.argv[3].split(',')] if len(sys.argv) > 3 else [1, 2]
tn, wn = tquad(24, 9.0)
t0 = time.time()
E3 = np.eye(3, dtype=int)
BOND = [canon([(0,0,0),(0,0,0),tuple(E3[mu]),tuple(E3[mu])]) for mu in range(3)]   # phi_x^2 phi_{x+mu}^2
# V'(k) for (1/4) sum_{x,mu} phi_x^2 phi_{x+mu}^2 = (1/24) sum V' phi^4  ->  V' = 6 sum_mu b_{bond_mu}
def gidx(orbs):
    rep_of = {}
    for oi, orb in enumerate(orbs):
        rep = orb[0]
        for gi, R in enumerate(GROUP):
            mo = act(R, rep)
            if mo not in rep_of: rep_of[mo] = (oi, gi)
    return rep_of
for r in rs:
    mon = enumerate_monomials(r); orbs = orbits(mon); rep_of = gidx(orbs); midx = {mo: i for i, mo in enumerate(mon)}
    for L in Ls:
        J0, W0 = strained(L, m, 0, 'E'); fld = Field(gx_from_k(J0, W0, tn), wn); F = FourPoint(fld, use_sym=True)
        # monomial Gram via invariance: <b_m, b_m'> = IP[orbit(m)][g_m^{-1} m']
        IP = [dict() for _ in orbs]
        def ip(m1, m2):
            oi, gi = rep_of[m1]; m2p = act(GROUP[gi].T, m2)
            d = IP[oi]
            if m2p not in d: d[m2p] = inner_mono(F, orbs[oi][0], m2p)
            return d[m2p]
        M = len(mon); Qm = np.zeros((M, M))
        for i in range(M):
            for j in range(i, M):
                Qm[i, j] = Qm[j, i] = ip(mon[i], mon[j])
        # bond-vertex overlaps with monomials (eps=0): <V', b_m> and <V',V'>
        Vb = np.array([6*sum(ip(b, mo) if b in rep_of else inner_mono(F, b, mo) for b in BOND) for mo in mon]) if r >= 1 else None
        for ch in ['E', 'T2']:
            funcs = channel_functions(orbs, ch)
            if not funcs:
                print(f'm={m} r={r} L={L} ch={ch}: no channel functions at this range'); continue
            C = np.zeros((len(funcs), M))
            for a, fdict in enumerate(funcs):
                for mo, c in fdict.items(): C[a, midx[mo]] += c
            fdot = Field(gdot_x(L, m, ch, tn), wn)
            Lm = np.array([L_mono(fld, fdot, mo) for mo in mon])
            Qf = C @ Qm @ C.T; Lf = C @ Lm
            ev, U = np.linalg.eigh(Qf); keep = ev > 1e-9*ev.max(); Neff = int(keep.sum())
            Ub = U[:, keep]/np.sqrt(ev[keep])          # orthonormal (Q-metric) basis
            Lo = Ub.T @ Lf                              # coordinates: f(c) = A + 4 Lo.y + 2 y.y
            ell = float(Lo @ Lo)
            # undressed onsite A
            d = 0.04; I = {e: onsite_I(L, m, e, ch, tn, wn) for e in [-d, -d/2, 0, d/2, d]}
            D = lambda e: (I[e]+I[-e]-2*I[0])/e**2; A = (4*D(d/2)-D(d))/3
            fmin = A - 2*ell
            line = (f'm={m} r={r} L={L:2d} ch={ch:2s}: N_eff={Neff:3d} A={A:.6e} mu(c=0)={-A/24:+.5e} '
                    f'ell=L^TQ+L={ell:.6e} f_min=A-2ell={fmin:+.5e} max_c mu2={-fmin/24:+.5e} ')
            if fmin <= 0:
                s1 = 1 - np.sqrt(1 - A/(2*ell)); s2 = 1 + np.sqrt(1 - A/(2*ell))
                y1 = -s1*Lo; ynorm = np.linalg.norm(y1)
                line += f'| feasible; min-|y| solution along -Q^-1 L: s={s1:.5f} |y|={ynorm:.4e} (rel. to |V|_w={np.sqrt(I[0]):.4e})'
            else:
                line += '| INFEASIBLE in this basis'
            print(line, f'[{time.time()-t0:.0f}s]'); sys.stdout.flush()
            if r == max(rs) and L == max(Ls):
                np.savez(f'w1_quadric_m{m}_r{r}_L{L}_{ch}.npz', A=A, Lf=Lf, Qf=Qf, C=C, Lo=Lo, Ub=Ub)
