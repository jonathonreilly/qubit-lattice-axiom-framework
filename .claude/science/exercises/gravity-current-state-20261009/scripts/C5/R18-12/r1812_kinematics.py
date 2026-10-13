"""C5 R18-12 (a): are edge quanta kinematically able to decay?  Exact energy + crystal-momentum (mod 2 pi) bookkeeping.

(A) one-photon emission  f(K) -> f(k') + gamma(K - k'):  margin D_A(K) = min_k' [eps(k') + omega(K - k')] - eps(K).
    D_A < 0 at a grid point k' is an explicit allowed final state (certifies OPEN; float precision only).
    D_A >= 0 on the grid does not certify closure; closure is certified analytically (Lemma L) where it holds.
(B) edge-photon decay  gamma(Q) -> f(p) fbar(Q - p)  or  gamma gamma:  margin D_B(Q) = min(E_pair, E_gg) - omega(Q).
(C) corner classes K = (pi,0,0), (pi,pi,0), (pi,pi,pi): lowest charge-0 and charge-1 states found among
    {single f, single gamma, f + gamma, f + fbar pair, gamma gamma}, with their Killing defect Delta (R16-8/R18-8).
Worlds: one charged species (S, G scalar; D1 Dirac) + one photon (R85, std, max, min1), m in {0, 0.3}.
Grid N = 48 (spacing 0.131), includes 0 and the zone corners.  Random edge samples: 500 per world (seed 1812).
"""
import os, sys, time
os.environ.setdefault("OMP_NUM_THREADS", "2")
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from r1812_laws import Matter, PHOTONS, omega, omega_shift, photon_delta, B, WPI, wrap

N = 48
kg = -np.pi + 2*np.pi*np.arange(N)/N
lines = []
def pr(s=""):
    print(s, flush=True); lines.append(s)

rng = np.random.default_rng(1812)
def edge_samples(n):
    out = []
    while len(out) < n:
        K = rng.uniform(-np.pi, np.pi, size=3)
        if (np.abs(K) > B).any(): out.append(K)
    ax = [(k, 0.0, 0.0) for k in np.linspace(B + 0.01, np.pi, 40)]
    di = [(k, k, 0.0) for k in np.linspace(B + 0.01, np.pi, 20)] + [(k, k, k) for k in np.linspace(B + 0.01, np.pi, 20)]
    return np.array(out + ax + di)

def margin_A(mat, ph, K, Eg):
    return (Eg + omega_shift(ph, K, kg)).min() - mat.eps(K)[0]

def margin_B(mat, ph, Q, Eg):
    epair = (Eg + mat.shifted_eps(Q, kg)).min()
    wg = omega(ph, np.stack(np.meshgrid(kg, kg, kg, indexing='ij'), -1).reshape(-1, 3)).reshape(N, N, N)
    egg = (wg + omega_shift(ph, Q, kg)).min()
    return min(epair, egg) - omega(ph, Q)[0], epair, egg

t0 = time.time()
Ks = edge_samples(500)
pr("C5 R18-12 kinematics.  b = %.2f; D1 Wilson r = 1/sqrt3, W_pi = %.4f; grid N = %d; %d edge samples" % (B, WPI, N, len(Ks)))
pr("")
pr("(A) fermion/scalar edge quanta: one-photon decay f(K) -> f(k') + gamma(K - k')")
pr("    columns: world | frac edge samples with D_A < -1e-9 (decay OPEN, explicit final state) | among defect-carrying (|Delta|>1e-6):"
   " frac open | min eps over defect-carrying samples with D_A >= 0 | min D_A")
resA = {}
for mname in ('S', 'G', 'D1'):
    for m in (0.0, 0.3):
        mat = Matter(mname, m); Eg = mat.grid_eps(kg)
        eK = mat.eps(Ks); dl = mat.delta(Ks); defect = np.abs(dl).max(1) > 1e-6
        for ph in ('R85', 'std', 'max', 'min1'):
            D = np.array([margin_A(mat, ph, K, Eg) for K in Ks])
            op = D < -1e-9
            cl_def = (~op) & defect
            emin = eK[cl_def].min() if cl_def.any() else np.nan
            resA[(mname, m, ph)] = (op, D, eK, defect)
            pr("  %-3s m=%.1f %-5s | open %.3f | defect: open %.3f (n=%d) | min eps closed&defect = %s | min D_A = %+.4f"
               % (mname, m, ph, op.mean(), op[defect].mean(), defect.sum(),
                  ("%.4f" % emin) if np.isfinite(emin) else "none", D.min()))
pr("  [%.0f s]" % (time.time() - t0))
pr("")
pr("(A2) axis line K = (k,0,0): first k (>b) where one-photon decay opens, per world (blank = closed on the whole line)")
axis = np.linspace(B + 0.01, np.pi, 40)
for key, (op, D, eK, defect) in resA.items():
    sel = op[500:540]
    pr("  %-3s m=%.1f %-5s : open at k = %s" % (key[0], key[1], key[2], ", ".join("%.2f" % k for k in axis[sel][:6]) + (" ..." if sel.sum() > 6 else "")))
pr("")
pr("(B) edge photons: decay gamma(Q) -> f fbar or gamma gamma (Q random in the photon edge |q_j| > 1, 150 samples) for the R85 photon")
Qs = []
while len(Qs) < 150:
    Q = rng.uniform(-np.pi, np.pi, size=3)
    if (np.abs(Q) > 1.0).any(): Qs.append(Q)
Qs = np.array(Qs + [(k, 0.0, 0.0) for k in np.linspace(1.05, np.pi, 20)])
for mname in ('S', 'G', 'D1'):
    for m in (0.0, 0.3):
        mat = Matter(mname, m); Eg = mat.grid_eps(kg)
        MB = np.array([margin_B(mat, 'R85', Q, Eg)[0] for Q in Qs])
        pdl = photon_delta('R85', Qs); pdef = np.abs(pdl).max(1) > 1e-6
        st = (MB >= -1e-9) & pdef
        w = omega('R85', Qs)
        pr("  world %-3s m=%.1f + R85: edge photons with decay closed on grid: %.3f; defect-carrying & closed: %d of %d; lightest such omega = %s"
           % (mname, m, (MB >= -1e-9).mean(), st.sum(), pdef.sum(), ("%.4f" % w[st].min()) if st.any() else "none"))
pr("  [%.0f s]" % (time.time() - t0))
pr("")
pr("(C) corner classes: lowest states found (charge 0 and charge 1), R85 photon unless stated")
corners = {'(pi,0,0)': np.array([np.pi, 0, 0]), '(pi,pi,0)': np.array([np.pi, np.pi, 0]), '(pi,pi,pi)': np.array([np.pi]*3)}
for mname in ('S', 'G', 'D1'):
    for m in (0.0, 0.3):
        mat = Matter(mname, m); Eg = mat.grid_eps(kg)
        for cn, K in corners.items():
            for ph in ('R85', 'std'):
                ef = mat.eps(K)[0]; dlf = mat.delta(K)[0]
                wv = omega(ph, K)[0]; dlg = photon_delta(ph, K)[0]
                efg = (Eg + omega_shift(ph, K, kg)).min()
                _, epair, egg = margin_B(mat, ph, K, Eg)
                c1 = min((ef, 'single f'), (efg, 'f + gamma'))
                c0 = min((wv, 'single gamma'), (epair, 'f fbar pair'), (egg, 'gamma gamma'))
                pr("  %-3s m=%.1f %-10s %-4s: eps_f=%.4f (Delta_xx=%+.3f) omega=%.4f (Delta_xx=%+.3f) f+g=%.4f pair=%.4f gg=%.4f"
                   " | q=1 ground: %s %.4f | q=0 ground: %s %.4f"
                   % (mname, m, cn, ph, ef, dlf[0], wv, dlg[0], efg, epair, egg, c1[1], c1[0], c0[1], c0[0]))
pr("  [%.0f s]" % (time.time() - t0))
open(os.path.splitext(os.path.abspath(__file__))[0] + ".out", "w").write("\n".join(lines) + "\n")
