"""CLS-1 step 2: light sector under class S in the free-fermion partner proxies (per Spin(10) component, 3D, one-body).
Model A: static site partner coupled through the full filtered field (rank of phi(P) decides zero modes).
Model B: channel-restricted partner: only singular channels of phi with sigma >= sig_th get an SMG partner
         (sig_th = (W_c/W)^(1/4); sig_th = 1 <-> W = W_c, the weakest mirror (hw0/hw2, |f| = 1) at threshold).
Outputs: control C1, theta, light channel weights, zero-mode counts, light energies at P (a-type), eigen-speeds (c-type)."""
import numpy as np, itertools, sys
sys.path.insert(0, '.')
from cls1_core import *
def P(*a): print(*a); sys.stdout.flush()
rng = np.random.default_rng(1015)
Pk = np.array([PI, 0, 0])                  # folded odd point: components (pi,0,0),(pi,pi,pi),(0,0,pi),(0,pi,0)
ODD = ["hw1_x(pi,0,0)", "hw3(pi,pi,pi)", "hw1_z(0,0,pi)", "hw1_y(0,pi,0)"]
LIGHT = [0, 2, 3]; HW3 = 1
arch = {}

def light_modes_at(k, H, tol_psi=1e-9, nlight=6):
    w, v, pw = eig_with_psi_weight(H)
    sel = np.where(pw > 0.5)[0]
    order = sel[np.argsort(np.abs(w[sel]))]
    return w, v, pw, order[:nlight]

P("=== C1 control: eps = eta = kappa = 0 recovers X2-L2 exact decoupling at the odd point ===")
for Delta in (0.5, 1.0, 2.0):
    H = H_modelA(Pk, Delta)
    w, v, pw = eig_with_psi_weight(H)
    z = np.abs(w) < 1e-12
    vz = v[:, z]
    # light content: psi weight on hw1 components; chi weight; hw3 weight of psi-carrying zero modes
    psi_light = sum((np.abs(vz[2*c:2*c+2, :])**2).sum(0) for c in LIGHT)
    hw3w = (np.abs(vz[2*HW3:2*HW3+2, :])**2).sum(0)
    # one-body decoupling: H applied to each light psi basis state
    worst = max(np.abs(H[:, 2*c + s]).max() for c in LIGHT for s in (0, 1))
    P(f"  Delta={Delta}: zero modes {z.sum()} (psi-carrying {(psi_light>0.5).sum()}), hw3 weight in zero modes {hw3w.max():.1e}, "
      f"max |H e_light| = {worst:.1e} (light psi states are exact zero modes, no chi/hw3 admixture); mirror hw3 pair at +-{np.sort(np.abs(w))[-1]:.3f}")

P("\n=== S0 (no Theta): P-a on-site density eps*sum_K cos(K.x) psi^dag psi; light energies at P (a-type shifts) ===")
P("  model B, Delta=1, sig_th=1 (hw3 the only partnered odd channel); expectation 2*eps (A1) and -eps (E x2):")
rowsS0 = []
for eps in (0.003, 0.01, 0.03, 0.1, 0.33, 1.0):
    H = H_modelB(Pk, 1.0, 0.0, 1.0, eps_a=eps)
    w, v, pw, lo = light_modes_at(Pk, H)
    e = np.sort(w[lo])
    rowsS0.append([eps] + list(e))
    P(f"  eps={eps:6.3f}: light (psi-weighted) energies at P = {np.round(e, 6)}  ratio to eps {np.round(e/eps, 4)}")
arch['S0_density_light_energies'] = np.array(rowsS0)
for Delta in (0.5, 2.0):
    H = H_modelB(Pk, Delta, 0.0, 1.0, eps_a=0.1)
    w, v, pw, lo = light_modes_at(Pk, H)
    P(f"  Delta={Delta}, eps=0.1: {np.round(np.sort(w[lo]), 6)}")
H = H_modelA(Pk, 1.0, 0.0, eps_a=0.1)
w, v, pw, lo = light_modes_at(Pk, H)
P(f"  model A (full static partner), eps=0.1: {np.round(np.sort(w[lo]), 6)}")
H = h_psi(Pk, eps_a=0.1)   # no mirror gap at all
P(f"  no partner (free walker + P-a), eps=0.1, odd sector at P: {np.round(np.linalg.eigvalsh(H), 6)}  (expect 3eps x2, -eps x6)")

P("\n=== S1 (Theta imposed): P-d filter modulation kappa; light channel weights, theta, zero modes ===")
P("  phi(P) = diag(f) + kappa (J-1) on (hw1_x, hw3, hw1_z, hw1_y); f(hw1)=0, f(hw3)=2")
rowsS1 = []
for kappa in (0.003, 0.01, 0.03, 0.1, 0.2, 0.33, 0.5, 1.0):
    F = phi(Pk, kappa)
    U, sv, Vh = np.linalg.svd(F)
    vheavy = Vh[0].conj()
    # light space = orthogonal complement of the heavy right-singular vector (channel-restricted partner, model B)
    th2_total = 1 - abs(vheavy[HW3])**2                # total hw3 weight spread over the 3 light modes
    # direct diagonalisation of model B at P (sig_th between light and heavy channels)
    sig_th = 0.5 * (sv[0] + sv[1])
    HB = H_modelB(Pk, 1.0, kappa, sig_th)
    w, v, pw = eig_with_psi_weight(HB)
    zl = np.where((np.abs(w) < 1e-10) & (pw > 0.5))[0]
    hw3_dd = (np.abs(v[2*HW3:2*HW3+2, zl])**2).sum()          # summed over the 6 light zero modes (3 flavours x 2 spin)
    chi_dd = (np.abs(v[8:, zl])**2).sum()
    # analytic single-partner formula: partner couples to f3*psi_hw3 + kappa*sum(light) -> theta_A1^2 = 3k^2/(4+3k^2)
    th2_single = 3 * kappa**2 / (4 + 3 * kappa**2)
    # model A (full static partner): zero modes at P with psi weight
    HA = H_modelA(Pk, 1.0, kappa)
    wA, vA, pwA = eig_with_psi_weight(HA)
    zA = ((np.abs(wA) < 1e-10) & (pwA > 0.5)).sum()
    lightgapA = np.sort(np.abs(wA[pwA > 0.3]))[0]
    rowsS1.append([kappa, sv[0], sv[1], sv[2], sv[3], th2_total, hw3_dd / 2, th2_single, chi_dd, zA, lightgapA, len(zl)])
    P(f"  kappa={kappa:5.3f}: sing.values {np.round(sv, 4)} | light w = {np.round(sv[1:], 4)}, margin 1/w_max^4 = {1/sv[1]**4:9.3g} | "
      f"theta^2(hw3 in light space): SVD {th2_total:.6f}, direct-diag {hw3_dd/2:.6f}, single-partner formula {th2_single:.6f}; "
      f"chi wt {chi_dd:.1e}; model B light zero modes {len(zl)}; model A psi zero modes {zA}, model-A light gap {lightgapA:.4f}")
arch['S1_kappa_table'] = np.array(rowsS1)
P("  columns archived: kappa, sv0..sv3, theta2_svd, theta2_directdiag, theta2_single, chi_wt, modelA_zero, modelA_lightgap, modelB_zero")

P("\n=== light eigen-speeds near P (c-type): 6 lightest psi-weighted branches, |q| = 1e-4, 26 lattice + 60 random directions ===")
dirs = [np.array(d, float) for d in itertools.product((-1, 0, 1), repeat=3) if any(d)]
dirs = [d / np.linalg.norm(d) for d in dirs] + [x / np.linalg.norm(x) for x in rng.normal(size=(60, 3))]
qq = 1e-4
def speeds(Hfun):
    sp = []
    for d in dirs:
        H = Hfun(Pk + qq * d)
        w, v, pw, lo = light_modes_at(Pk + qq * d, H)
        sp.append(np.sort(np.abs(w[lo])) / qq)
    return np.array(sp)               # ndir x 6
rowsV = []
for lab, mk in [("control", lambda e: dict()),
                ("P-c eta", lambda e: dict(eta=e)),
                ("P-d kappa", lambda e: dict(kappa=e)),
                ("P-c eta, amps (1,.7,.4)", lambda e: dict(eta=e, amps=(1, .7, .4)))]:
    for e in ((0.0,) if lab == "control" else (0.003, 0.01, 0.03, 0.1, 0.33)):
        kw = mk(e); kap = kw.pop('kappa', 0.0)
        amps = kw.get('amps', (1, 1, 1))
        svP = np.linalg.svd(phi(Pk, kap, amps), compute_uv=False)
        sig_th = 0.5 * (svP[0] + svP[1]) if kap > 0 else 1.0
        sp = speeds(lambda k: H_modelB(k, 1.0, kap, sig_th, **kw))
        spread = sp.max() - sp.min()
        per_dir_spread = (sp.max(1) - sp.min(1)).max()
        aniso = (sp.mean(1).max() - sp.mean(1).min())
        rowsV.append([e, sp.min(), sp.max(), spread, per_dir_spread, aniso])
        P(f"  {lab:24s} {e:6.3f}: speeds in [{sp.min():.6f}, {sp.max():.6f}], flavour spread at fixed direction (max) {per_dir_spread:.3e}, "
          f"direction-dependence of mean {aniso:.3e}; spread/e = {spread/max(e,1e-30):.4f}, spread/e^2 = {spread/max(e*e,1e-30):.4f}")
arch['speeds_table'] = np.array(rowsV)

P("\n=== gaplessness check near P (Theta-even case): min |E| of psi-weighted states on a k-shell grid around P ===")
for lab, kw, kap in [("P-c eta=0.33", dict(eta=0.33), 0.0), ("P-d kappa=0.33", dict(), 0.33), ("both 0.33", dict(eta=0.33), 0.33)]:
    svP = np.linalg.svd(phi(Pk, kap), compute_uv=False)
    sig_th = 0.5 * (svP[0] + svP[1]) if kap > 0 else 1.0
    worst = []
    for r in (0.01, 0.05, 0.1):
        for d in dirs:
            H = H_modelB(Pk + r * d, 1.0, kap, sig_th, **kw)
            w, v, pw, lo = light_modes_at(Pk + r * d, H)
            worst.append(np.abs(w[lo]).min() / r)
    H = H_modelB(Pk, 1.0, kap, sig_th, **kw); w, v, pw, lo = light_modes_at(Pk, H)
    P(f"  {lab:16s}: |E| at P of the 6 light = {np.abs(w[lo]).max():.1e}; min over shells of (lowest |E|)/r = {min(worst):.4f}  (node stays at P, linear dispersion)")

np.savez('cls1_light_archive.npz', **arch)
P("archived cls1_light_archive.npz:", list(arch))
