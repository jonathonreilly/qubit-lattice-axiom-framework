"""Lane RG probe G2, part 2: amplitude-weighted umklapp ratios on energy shells.

Usage: python g2_shells.py KIND d m mediator    (mediator in {coul, lind})
Tree 2<->2 amplitude of identical scalars through a gapless mediator:
  T_0 = V(q_t) + V(q_u),  q_t = k1-k3, q_u = k1-k4
  coul: static massless lattice exchange V = 1/Omega(q)^2  (gapless; forward cut |q|>0.3)
  lind: static lattice Lindhard kernel V = chi_0(q) of a 2D/3D TB Fermi sea (mu=-1, T=0.02)
Network vertex filters: T_n = F(k1)F(k2)F(k3)F(k4) T_0 (exact for product vertices).
Measures on a shell E (exact collision measure, see g2_lib):
  eps_same = rms_U |T_n| / rms_N |T_n|          (same shell)
  eps_ref  = rms_U |T_n| / rms_N,low |T_n|      (normal reference on a low shell with no umklapp)
  eps_D    = sqrt(<|T_n|^2 |D|^2>/<|T_n|^2>)/2pi (rate-weighted sawtooth defect per collision)
  plus vacuum (k1,k2 uniform) and thermal (exp(-E/T)) energy-integrated versions.
"""
import numpy as np, sys, time
from g2_lib import *
from g2_filters import f_binom, minimax_filter

KIND, d, m, MED = sys.argv[1], int(sys.argv[2]), float(sys.argv[3]), sys.argv[4]
rng = np.random.default_rng(2026 + d)
eps = make_disp(KIND, m)
NS = 60000 if d == 2 else 40000

# ---- mediator
if MED == 'coul':
    def V(q):
        return 1.0 / np.maximum(Omega2(q), 1e-300)
    QCUT = 0.3
else:
    Lk = 48 if d == 2 else 20
    g1 = (np.arange(Lk) + 0.5) * 2 * np.pi / Lk - np.pi
    KK = np.stack(np.meshgrid(*([g1] * d), indexing='ij'), -1).reshape(-1, d)
    eK = -2 * np.sum(np.cos(KK), 1); mu, Tf = -1.0, 0.02
    fK = 1 / (1 + np.exp((eK - mu) / Tf))
    def V(q):
        out = np.empty(len(q))
        for i0 in range(0, len(q), 256):
            qq = q[i0:i0 + 256]
            ekq = -2 * np.sum(np.cos(KK[None, :, :] + qq[:, None, :]), -1)
            fkq = 1 / (1 + np.exp((ekq - mu) / Tf))
            de = ekq - eK[None, :]
            small = np.abs(de) < 1e-8
            num = np.where(small, fK * (1 - fK) / Tf, fK[None, :] - fkq)
            den = np.where(small, 1.0, de)
            out[i0:i0 + 256] = np.mean(num / den, 1)
        return out
    QCUT = 0.0


def amp0(k1, k2, k3, k4):
    qt, qu = wrap(k1 - k3), wrap(k1 - k4)
    T = V(qt) + V(qu)
    keep = np.minimum(np.linalg.norm(qt, axis=1), np.linalg.norm(qu, axis=1)) > QCUT
    return T, keep


def legs(F, k1, k2, k3, k4):
    return F(k1) + F(k2) + F(k3) + F(k4)   # log Phi


def prodF(f):
    # returns log|F(k)| summed over components (log domain avoids underflow at large n)
    return lambda k: np.sum(np.log(np.abs(f(k)) + 1e-320), axis=-1)


def lrms(logA, w, sel):
    # log of sqrt( sum w A^2 / sum w ) over sel
    from scipy.special import logsumexp
    return 0.5 * (logsumexp(2 * logA[sel], b=w[sel]) - np.log(np.sum(w[sel])))


filters = [('a', r, prodF(f_binom(r))) for r in [0, 1, 2, 4, 8, 12, 16, 24, 32, 48, 64, 80]]
kap = np.pi / 4
for n in [4, 8, 12, 16, 24]:
    f, dl, _, _ = minimax_filter(n, kap)
    f0 = f(np.array([0.0]))[0]
    filters.append(('c', n, prodF(lambda k, f=f, f0=f0: f(k) / f0)))
    print(f'# (c) kappa=pi/4 n={n}: minimax delta={dl:.3e}')

wmax = eps(np.full((1, d), np.pi))[0] if KIND == 'KG' else 2.0 * d
if KIND == 'KG':
    EU = 2 * np.sqrt(m ** 2 + 2)
    Elow = 2 * m + 0.5 * (EU - 2 * m)
    shells = [('low', EU + 0.15), ('mid', 0.5 * (EU + 2 * wmax)), ('top', 2 * wmax - 0.4)]
else:
    EU = -4.0 * (d - 1)  # min pair energy at K_x = pi: eps(a,0..)+eps(pi-a,0..) = -4(d-1) for every a
    Elow = -4.0 * d + 0.6
    shells = [('low', EU + 0.3), ('mid(nested E~0)', 0.37), ('top', 4.0 * d - 1.0)]
print(f"# {KIND} d={d} m={m} mediator={MED}; umklapp threshold E_U={EU:.4f}, pair band top {2*wmax:.4f}, Elow={Elow:.3f}")

t0 = time.time()
k = sample_shell(eps, d, Elow, NS, rng)
T0, keep = amp0(*k[:4]); w = k[4]
U = umklapp(*k[:4])
print(f"# low reference shell E={Elow:.3f}: {len(w)} configs, umklapp fraction {U.mean():.3f} (must be 0)")
ref = {}
for lab, n, F in filters:
    lT = np.log(np.abs(T0) + 1e-320) + legs(F, *k[:4])
    ref[(lab, n)] = lrms(lT, w, keep & ~U)

for sname, E in shells:
    k = sample_shell(eps, d, E, NS, rng)
    T0, keep = amp0(*k[:4]); w = k[4]
    U = umklapp(*k[:4]); D = defect(*k[:4])
    D2 = np.sum(np.round(D / (2 * np.pi)) ** 2, 1)   # exact integer winding: removes roundoff floor
    print(f"\n## shell {sname} E={E:.3f}: {len(w)} configs ({keep.mean():.3f} kept), umklapp measure fraction "
          f"{np.sum(w[U&keep])/np.sum(w[keep]):.3f}, |T0| range on U [{np.min(np.abs(T0[U&keep])):.2e},{np.max(np.abs(T0[U&keep])):.2e}]"
          f" on N [{np.min(np.abs(T0[~U&keep])):.2e},{np.max(np.abs(T0[~U&keep])):.2e}]  ({time.time()-t0:.0f}s)")
    print("  filt  n   log10 eps_same  log10 eps_ref  log10 eps_D  log10 maxPhi_U  log10 maxPhi_N(shell)")
    L10 = np.log(10)
    for lab, n, F in filters:
        lP = legs(F, *k[:4]); lT = np.log(np.abs(T0) + 1e-320) + lP
        su, sn = U & keep, ~U & keep
        rU = lrms(lT, w, su); rN = lrms(lT, w, sn)
        from scipy.special import logsumexp
        eD = 0.5 * (logsumexp(2 * lT[su], b=w[su] * D2[su]) - logsumexp(2 * lT[keep], b=w[keep]))
        print(f"  ({lab}) {n:3d}  {(rU-rN)/L10:9.3f}  {(rU-ref[(lab,n)])/L10:9.3f}  {eD/L10:9.3f}  {lP[su].max()/L10:9.3f}  {lP[sn].max()/L10:9.3f}")
    sys.stdout.flush()

# vacuum / thermal energy-integrated
k = sample_free(eps, d, NS, rng)
T0, keep = amp0(*k[:4]); w = k[4]
U = umklapp(*k[:4]); D = defect(*k[:4]); D2 = np.sum(np.round(D / (2 * np.pi)) ** 2, 1)
Epair = eps(k[0]) + eps(k[1])
print(f"\n## energy-integrated: {len(w)} configs; weights vacuum (uniform k1,k2) and thermal exp(-(E-Emin)/T)")
print("  filt  n   log10 eD_vac  eD_T=1  eD_T=0.5  eD_T=0.25   (eps_D = rate-weighted rms sawtooth winding per collision)")
from scipy.special import logsumexp
su = U & keep
for lab, n, F in filters:
    lT = np.log(np.abs(T0) + 1e-320) + legs(F, *k[:4])
    row = []
    for Tt in [None, 1.0, 0.5, 0.25]:
        lw = np.log(w) + (0.0 if Tt is None else -(Epair - Epair.min()) / Tt)
        row.append(0.5 * (logsumexp(2 * lT[su] + lw[su], b=D2[su]) - logsumexp(2 * lT[keep] + lw[keep])) / np.log(10))
    print(f"  ({lab}) {n:3d}  " + "  ".join(f"{x:9.3f}" for x in row))
print(f"# total {time.time()-t0:.0f}s")
