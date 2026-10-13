"""R19-5: counterexample to 'exact W1 removes own-direction placement' (P-R18-13c) in the channel-decoupled class:
UD's pair block multiplied by R18-13's own-direction factors u_d(q_i) (T_ii), u_o(q_i)u_o(q_j) (T_ij), u(s) = 1 - w + w cos s,
with large signed weights, completed exactly by the same construction (scattering: Lemma Div; pair: Lemma P1)."""
import numpy as np, sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import r195_dirac_exact as R
import r195_dirac_exact2 as R2
UD0 = R.UD
def run(band, wd, wo, rng, n=200):
    rmax = smax = pm = 0.0
    for t in range(n):
        k2 = rng.uniform(-np.pi, np.pi, 3); q = rng.uniform(-np.pi, np.pi, 3) * rng.choice([0.2, 0.5, 1.0])
        ud = 1 - wd + wd*np.cos(q); uo = 1 - wo + wo*np.cos(q)
        fac = lambda i, j: ud[i] if i == j else uo[i]*uo[j]
        Rk = R.wrap if hasattr(R, 'wrap') else None
        R.UD = lambda band_, k, i, j: fac(i, j) * UD0(band_, k, i, j)
        R2.UD = R.UD
        M = R2.glued(band, k2, q)
        Mb = R2.glued(band, k2 + q, -q)       # Hermitize with the same own-direction factors (even in q)
        MH = [[0.5*(M[a][b] + Mb[a][b].conj().T) for b in range(4)] for a in range(4)]
        r, s = R.residual(band, MH, k2, q, R2.Dfull); rmax, smax = max(rmax, r), max(smax, s)
        k1 = k2 + q; kb = k2 + q/2
        for i in range(3):
            for j in range(3):
                Pa, Pb = band.proj(k1, 1), band.proj(k2, -1)
                pm = max(pm, np.abs(Pa@MH[i+1][j+1]@Pb - fac(i, j)*Pa@UD0(band, kb, i, j)@Pb).max())
        R.UD = UD0; R2.UD = UD0
    return rmax, smax, pm
rng = np.random.default_rng(77)
band = R.Band(R.D1(0.909103707957, 0.555604225797), 0.01)
for wd, wo in ((-1.17, -0.196), (-3.0, 2.0)):
    r, s, pm = run(band, wd, wo, rng)
    print(f'own-direction (w_d, w_o) = ({wd}, {wo}) on UD pair block, m = 0.01, 200 random (k,q) on the torus (glued near/far): '
          f'W1 residual {r:.2e}, symmetry {s:.2e}, pair block - u-smeared UD {pm:.2e}')
