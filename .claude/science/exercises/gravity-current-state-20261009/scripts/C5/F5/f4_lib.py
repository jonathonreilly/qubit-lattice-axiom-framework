"""F4 library: gauge-path families for the SF-strained root Dirac law (F1's law), one-loop additive mass at P = 0.

Reuses F1's law unchanged (f1_lib.py: Ferm, Phot, flowF, flowG1, quadrature): D_t(k) = D(Phi^F_t(k)), photon symbols d_{t,j},
Feynman gauge, critical m = 0 in the propagator, E_g strain in SF units t.

Path families (all gauge covariant with the generalized photon symbol d_j: every family is a unit 1-chain from 0 to n, so the
Ward identity sum_j d_j V_j(0,q) = D_t(q) - D_t(0) holds by telescoping; all agree on axis hops, i.e. on the separable t = 0 law):

  'stair M' (M = 1, 2, 3, ...): each hop n is routed along an M-round staircase: M rounds, each round = one leg of length n_j/M along
      every axis in a fixed order sigma; Wilson lines averaged uniformly over the 6 orders sigma (W-average).  M = 1 is F1's Psym.
      For M >= 2 legs have fractional length: the line integral uses the band-limited interpolation of the photon field (the
      generalized link along an axis leg of any length is exact in momentum space), as does the straight line.
      Momentum form (proved in the report): with corners P(r,S) = (r q + q_S)/M, S a subset of {x,y,z},
          V_x(0,q) = (1/d_x) sum_{r=0}^{M-1} sum_{S in {0,y,z,yz}} w_S [D_t(P(r, S+x)) - D_t(P(r,S))],  w = (1/3, 1/6, 1/6, 1/3),
      V_x(q,0) = V_x(0,q) (the reversed M-staircase of order sigma is the M-staircase of order sigma^rev).
      Diagonal seagull (M-part; the c-part cancels by oddness), sigma-INDEPENDENT for each M:
          N_x = sum_{r=0}^{M-1} [ (M-r) M_t(P(r,{x})) + (M-r-1) M_t(P(r,{y,z})) - 2 (M-r) M_t(P(r,0)) [r>=1] ],
      tadpole integrand sum_j N_j/d_j^2/(2 Om)  (M = 1: N_x = M_t(q_x e_x), F1's).
  'SL': the straight segment (Peierls line), = M -> infinity limit of 'stair M' (error O(1/M^2): the sigma-averaged staircase is a
      midpoint rule on the segment; the seagull sum is a 2D midpoint rule).  V_j^SL(0,q) = (q_j/d_j) int_0^1 d_j D_t(s q) ds.
  'J' (Psym-J): the SAME six axis-ordered paths, but the hop phase is exp(i int Jbar.A) with Jbar the averaged current (unitary),
      instead of the average of the six Wilson lines.  Same one-photon vertex as Psym; diagonal seagull
          N_x^J = sum_{T in {0,y,z,yz}} pi_T [M_t(P(0,T+x)) - M_t(P(0,T))],  pi = (10, 8, 8, 10)/36.
      For a single plaquette hop W-average = J-phase x cos(Phi/2) (Phi the enclosed flux): the two differ by an F^2 coupling.

Output of pieces(): base = <M/(2 E Om (E+Om))>, Tad[s] = <sum_j N^s_j/d_j^2/(2 Om)>, and the symmetric bilinear exchange
  E[a,b] = < sum_j [(a_a.a_b - b_a b_b) M - b_a (a_b.c) - b_b (a_a.c)] / (2 E Om (E+Om)) >,  V_j = i g.a_j + b_j.
dm(family with vertex a, seagull s) = base + Tad[s] + E[a,a];  mixtures V = (1-lam) V_a + lam V_b are bilinear in lam.
"""
import numpy as np, sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from f1_lib import Ferm, Phot, flowF, flowG1, Grid, ROOT, ROOT0, CPH, dm_sf, panels

AX = ('x', 'y', 'z')
WS = {0: 1/3, 1: 1/6, 2: 1/3}          # weight of the base subset S (of the two other axes) by its size
PI_J = {0: 10/36, 1: 8/36, 2: 10/36}


def frac_breaks(b, Ms):
    """panel breaks where a staircase corner component r q_l / M crosses the Dirac box edges b, pi - b (r = 1..M)."""
    out = set()
    for M in Ms:
        for r in range(1, M + 1):
            for e in (b, np.pi - b):
                v = e*M/r
                if 0 < v < np.pi:
                    out.add(round(v, 12))
    return sorted(out)


def mkgrid(b, n, hm, mph, Ms=None):
    br = [b, np.pi - b] + [CPH + i*(np.pi - CPH)/mph for i in range(mph)]
    if Ms:
        br += frac_breaks(b, Ms)
    return Grid(br, n, hm)


def pieces(F, G, grid, t, Ms=(1, 2, 3, 4), nrk=2, chunk_pts=2.0e5, check_ward=False):
    x, w = grid.x, grid.w
    N = len(x)
    chunk = max(1, int(chunk_pts/(N*N)))
    dxv = G.d(flowG1(G, x, +1, t, nrk)); dyv = G.d(flowG1(G, x, -1, t, nrk)); dzv = G.d(x)
    base = 0.0
    Tad = {('M', M): 0.0 for M in Ms}; Tad['J'] = 0.0
    E = {(a, b): 0.0 for i, a in enumerate(Ms) for b in Ms[i:]}
    ward = 0.0

    def Dt(kx, ky, kz):
        Wz = F.W(kz)
        fx, fy = flowF(F, kx, ky, Wz, t, nrk)
        sz = F.s(kz) + 0*fx
        return (F.s(fx), F.s(fy), sz, F.W(fx) + F.W(fy) + Wz + 0*fx)

    for i0 in range(0, N, chunk):
        iz = np.arange(i0, min(N, i0 + chunk))
        X = x[:, None, None]; Y = x[None, :, None]; Z = x[iz][None, None, :]
        dd = [dxv[:, None, None] + 0*Z, dyv[None, :, None] + 0*Z, dzv[iz][None, None, :] + 0*X + 0*Y]
        Om = np.sqrt(dd[0]**2 + dd[1]**2 + dd[2]**2)
        ww = w[:, None, None]*w[None, :, None]*w[iz][None, None, :]
        Dq = Dt(X, Y, Z)
        c = Dq[:3]; Mq = Dq[3]
        Eq = np.sqrt(c[0]**2 + c[1]**2 + c[2]**2 + Mq*Mq)
        den = 2*Eq*Om*(Eq + Om)
        base += float((ww*Mq/den).sum())
        V = {}
        for M in Ms:
            Vacc = [[0.0]*4 for _ in range(3)]
            Nacc = [0.0, 0.0, 0.0]
            Jacc = [0.0, 0.0, 0.0]
            cur0 = None                                   # D at P(r, {}) carried from previous round
            for r in range(M):
                cache = {}
                def corner(S):
                    key = frozenset(S)
                    if key in cache:
                        return cache[key]
                    if len(key) == 0 and cur0 is not None:
                        cache[key] = cur0; return cur0
                    if len(key) == 3 and r == M - 1:
                        cache[key] = Dq; return Dq
                    kx = (r + ('x' in key))*X/M; ky = (r + ('y' in key))*Y/M; kz = (r + ('z' in key))*Z/M
                    if r == 0 and len(key) == 0:
                        val = (0.0, 0.0, 0.0, 0.0)
                    else:
                        val = Dt(kx, ky, kz)
                    cache[key] = val
                    return val
                for j, a in enumerate(AX):
                    oth = [o for o in AX if o != a]
                    for S in ([], [oth[0]], [oth[1]], oth):
                        Dhi = corner(S + [a]); Dlo = corner(S)
                        wS = WS[len(S)]
                        for l in range(4):
                            Vacc[j][l] = Vacc[j][l] + wS*(Dhi[l] - Dlo[l])
                        if M == 1:
                            Jacc[j] = Jacc[j] + PI_J[len(S)]*(Dhi[3] - Dlo[3])
                    # seagull numerator
                    Nacc[j] = Nacc[j] + (M - r)*corner([a])[3] + (M - r - 1)*corner(oth)[3]
                    if r >= 1:
                        Nacc[j] = Nacc[j] - 2*(M - r)*corner([])[3]
                cur0 = corner(['x', 'y', 'z'])
                del cache
            V[M] = [[Vacc[j][l]/dd[j] for l in range(4)] for j in range(3)]
            Tad[('M', M)] += float((ww*(Nacc[0]/dd[0]**2 + Nacc[1]/dd[1]**2 + Nacc[2]/dd[2]**2)/(2*Om)).sum())
            if M == 1:
                Tad['J'] += float((ww*(Jacc[0]/dd[0]**2 + Jacc[1]/dd[1]**2 + Jacc[2]/dd[2]**2)/(2*Om)).sum())
            if check_ward:
                for l in range(4):
                    res = sum(V[M][j][l]*dd[j] for j in range(3)) - Dq[l]
                    ward = max(ward, float(np.max(np.abs(res))))
        for (a, b) in E:
            num = 0.0
            for j in range(3):
                Va, Vb = V[a][j], V[b][j]
                num = num + (Va[0]*Vb[0] + Va[1]*Vb[1] + Va[2]*Vb[2] - Va[3]*Vb[3])*Mq \
                    - Va[3]*(Vb[0]*c[0] + Vb[1]*c[1] + Vb[2]*c[2]) - Vb[3]*(Va[0]*c[0] + Va[1]*c[1] + Va[2]*c[2])
            E[(a, b)] += float((ww*num/den).sum())
        del V
    out = dict(base=base, Tad=Tad, E=E)
    if check_ward:
        out['ward'] = ward
    return out


def fam_dm(P, vert, sg):
    """dm for a family: vertex type vert (M), seagull type sg (('M', M) or 'J')."""
    return P['base'] + P['Tad'][sg] + P['E'][(vert, vert)]


def mix_dm(P, a, b, lam, sga, sgb):
    """weighted mixture of W-averages: V = (1-lam) V_a + lam V_b, seagull (1-lam) N_a + lam N_b (linear in the Wilson-line weights)."""
    key = lambda u, v: (u, v) if (u, v) in P['E'] else (v, u)
    Eab = P['E'][key(a, b)]
    Ex = (1 - lam)**2*P['E'][(a, a)] + 2*lam*(1 - lam)*Eab + lam**2*P['E'][(b, b)]
    return P['base'] + (1 - lam)*P['Tad'][sga] + lam*P['Tad'][sgb] + Ex
