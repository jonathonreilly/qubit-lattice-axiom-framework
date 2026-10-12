"""Q1 (B): what the quantum readings see, computed on the actual sprinkling realizations of lane RZ (probe Z2's
saved fixed-source carrier MC, op0, eps = 1, 1/2, 1/4, 1/8; source with a past edge; observer worldline).

For the mixture reading (substrate traced out; Theorem A) the light's reduced state is E_P |alpha_P><alpha_P| with
alpha_P = lambda*phi_P (coherent-state quantization of the classical source).  Observables:
  first-order coherence with the mean mode:  Gamma(t) = |E phi|^2 / E|phi|^2  (= fringe visibility of image against a GR
  reference, = purity of the coherent component); typical-vs-mean: median|delta|^2/V, E ln|delta|^2, kurtosis, circularity.
  Growth rates of V (annealed) vs median and exp E ln|delta|^2 (quenched/typical) along the late window.
For the recombination reading (single substrate final state, uniform amplitude) the light state is E_P D(alpha_P)|0>:
  recombination probability  N2 = E_{P != P'} exp(-|a|^2/2 - |a'|^2/2 + conj(a') a)
  observed amplitude          <a>_rec = E[a e^{...}]/N2,   compared with the GR/mean amplitude and with 2Psi/(2+V_ph).
Scaling: alpha_P = sqrt(nbar) phi_P/|Psi| so that the MEAN field carries nbar photons per mode; V_ph = nbar V/|Psi|^2.
"""
import numpy as np, glob, sys
S = "/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/RZ/Z2/"
rng = np.random.default_rng(7)
files = [S + "z2_A_e1.npz", S + "z2_A_e05.npz", S + "z2_A_e025.npz", S + "z2_A_e0125.npz"]
JW = 3          # carrier w0 = 1 (complex carrier)
for fn in files:
    D = np.load(fn); phi = D["phi"][:, :, JW]; t = D["tobs"]; eps = float(D["eps"]); T = float(D["T"]); d = float(D["d"])
    R, K = phi.shape
    tau = np.sqrt(np.maximum(t**2 - d**2, 1e-9))
    late = t >= max(d + 1.5, T - 4.0)
    m = phi.mean(0); dl = phi - m; V = (np.abs(dl)**2).mean(0); sem2 = V/R
    G = np.abs(m)**2/(np.abs(m)**2 + V)
    # unbiased |Psi|^2 estimate: |m|^2 - V/R
    Psi2 = np.maximum(np.abs(m)**2 - sem2, 0)
    Gu = Psi2/(Psi2 + V)
    a2 = np.abs(dl)**2
    med = np.median(a2, 0)/V; kur = (a2**2).mean(0)/V**2; circ = np.abs((dl**2).mean(0))/V
    Elog = np.log(a2 + 1e-300).mean(0)
    sel = late
    def slope(y): return np.polyfit(tau[sel], y[sel], 1)[0]
    print("=== eps=%g (R=%d), carrier w0=1, late window tau in [%.2f, %.2f] ===" % (eps, R, tau[sel][0], tau[sel][-1]))
    print(" median over late window: |mean|^2/sem^2 = %.2f ; Gamma = |E phi|^2/E|phi|^2 = %.4f (bias-corrected %.4f) ; V/|Psi|^2 ~ %.3g" %
          (np.median(np.abs(m[sel])**2/sem2[sel]), np.median(G[sel]), np.median(Gu[sel]), np.median(V[sel]/np.maximum(Psi2[sel], 1e-300))))
    print(" shape of delta (late-window medians): median|d|^2/V = %.3f (circ. Gaussian 0.693) ; E|d|^4/V^2 = %.2f (circ. Gaussian 2) ; |E d^2|/V = %.3f (0 if circular)" %
          (np.median(med[sel]), np.median(kur[sel]), np.median(circ[sel])))
    print(" growth rates d/dtau over late window: ln V (annealed) %.3f ; ln median|d|^2 %.3f ; E ln|d|^2 (quenched) %.3f ; [Gaussian: all equal]" %
          (slope(np.log(V)), slope(np.log(np.median(a2, 0))), slope(Elog)))
    # tail weight: fraction of V carried by the top 1% / 10% of realizations at the last time
    k = K - 1; srt = np.sort(a2[:, k])[::-1]
    print(" at t=T: share of E|d|^2 carried by top 1%%: %.2f, top 10%%: %.2f (exponential law: %.2f, %.2f)" %
          (srt[:max(1, R//100)].sum()/srt.sum(), srt[:max(1, R//10)].sum()/srt.sum(), (1 + np.log(100))/100, (1 + np.log(10))/10))
    # recombination channel at a few late times, as a function of photon scale
    if eps <= 0.25:
        ks = np.where(sel)[0][::max(1, sel.sum()//6)][:6]
        for nbar in [1e-3, 1e-2, 1e-1, 1.0]:
            Ns, Ar, Vp = [], [], []
            for k in ks:
                Pm = np.sqrt(Psi2[k]) if Psi2[k] > 0 else np.abs(m[k])
                al = np.sqrt(nbar)*phi[:, k]/Pm
                i, j = np.triu_indices(R, 1)
                a, b = al[i], al[j]
                ker = np.exp(-np.abs(a)**2/2 - np.abs(b)**2/2 + np.conj(b)*a)
                ker2 = np.exp(-np.abs(b)**2/2 - np.abs(a)**2/2 + np.conj(a)*b)
                N2 = 0.5*(ker.mean() + ker2.mean())
                A = 0.5*((a*ker).mean() + (b*ker2).mean())/N2
                mu = np.sqrt(nbar)*m[k]/Pm
                Ns.append(abs(N2)); Ar.append(abs(A)/abs(mu)); Vp.append(nbar*V[k]/Pm**2)
            Vp = np.array(Vp)
            print("  recombination, nbar=%g (V_ph median %.3g): prob median %.3g ; |<a>_rec|/|mean amp| median %.3f (Gaussian 2/(2+V_ph): %.3f)" %
                  (nbar, np.median(Vp), np.median(Ns), np.median(Ar), np.median(2/(2 + Vp))))
    sys.stdout.flush()
