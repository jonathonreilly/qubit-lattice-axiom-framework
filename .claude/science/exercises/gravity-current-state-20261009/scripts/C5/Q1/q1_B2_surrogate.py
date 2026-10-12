"""Q1 (B2): eps = 1/8 recombination channel: MC realizations vs a Gaussian surrogate with the same mean and the same
(non-circular) 2x2 real covariance, and vs the circular closed form 2/(2+V_ph).  Bootstrap error on the MC estimator."""
import numpy as np
S = "/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/RZ/Z2/"
rng = np.random.default_rng(11)
D = np.load(S + "z2_A_e0125.npz"); phi = D["phi"][:, :, 3]; t = D["tobs"]; T = float(D["T"]); d = float(D["d"])
R, K = phi.shape; late = t >= max(d + 1.5, T - 4.0)
def rec(al):
    i, j = np.triu_indices(len(al), 1); a, b = al[i], al[j]
    k1 = np.exp(-np.abs(a)**2/2 - np.abs(b)**2/2 + np.conj(b)*a); k2 = np.conj(k1)
    N2 = 0.5*(k1.mean() + k2.mean()); A = 0.5*((a*k1).mean() + (b*k2).mean())/N2
    return abs(N2), A
ks = np.where(late)[0][::20]
print("eps=1/8, carrier w0=1; per time: V/|Psi|^2, then for nbar: [MC prob, MC |<a>_rec|/|mean|  (bootstrap sd)] [surrogate R samples] [surrogate 6000] [circular 2/(2+V_ph)]")
for k in ks:
    m = phi[:, k].mean(); dl = phi[:, k] - m; V = np.mean(np.abs(dl)**2); Psi2 = max(abs(m)**2 - V/R, 1e-12); Pm = np.sqrt(Psi2)
    C = np.cov(np.vstack([dl.real, dl.imag]))
    print(" t=%.2f  V/|Psi|^2=%.0f  circularity |E d^2|/V=%.2f" % (t[k], V/Psi2, abs(np.mean(dl**2))/V))
    for nbar in [1e-3, 1e-2, 3e-2, 1e-1]:
        sc = np.sqrt(nbar)/Pm; mu = sc*m
        N2, A = rec(sc*phi[:, k])
        bs = []
        for _ in range(20):
            idx = rng.integers(0, R, R); n2b, Ab = rec(sc*phi[idx, k]); bs.append(abs(Ab)/abs(mu))
        out = []
        for Ms in [R, 6000]:
            z = rng.multivariate_normal([0, 0], C, size=Ms); g = m + z[:, 0] + 1j*z[:, 1]
            n2s, As = rec(sc*g); out.append((n2s, abs(As)/abs(mu)))
        Vph = nbar*V/Psi2
        print("   nbar=%-6g V_ph=%7.2f  MC: prob %.4f amp %.3f (sd %.3f) | surr(R): %.4f %.3f | surr(6000): %.4f %.3f | circ: amp %.3f prob %.4f" %
              (nbar, Vph, N2, abs(A)/abs(mu), np.std(bs), out[0][0], out[0][1], out[1][0], out[1][1], 2/(2+Vph), (2/(2+Vph))**2*np.exp(-2*nbar*Vph/(2+Vph)**2)))
