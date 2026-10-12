"""Q1 (A): finite-dimensional checks of the structural statements of the Q1 report.

(A1) Theorem A (configuration-diagonal coupling): joint state sum_P psi(P)|P>|U_P chi0>; reduced light state equals the
     mixture sum_P |psi(P)|^2 U_P rho0 U_P^dag for ANY phases of psi.  Any later substrate-only unitary ("the substrate
     returns to its state") leaves the light's reduced state unchanged (no-signalling).
(A2) Postselection / final-state projection onto the initial substrate state |Sigma> = sum psi|P>: light state
     = sum |psi|^2 U_P chi0 = E U chi0 (the mean-propagated state); success probability ||E U chi0||^2
     = 1 - E||U chi0 - E U chi0||^2 (the variance is the missing probability).
(A3) Coherent-state recombination (classical source; per-realization S-matrix = displacement D(alpha_P)):
     for alpha = Psi + delta, delta circular complex Gaussian with E|delta|^2 = V (photon units),
        E D(alpha)|0> = (2/(2+V)) exp(-|Psi|^2 V/(2+V)^2) |2 Psi/(2+V)>     (claimed exact)
     checked in a truncated Fock basis against Monte Carlo and against the closed form.
(A4) Non-Gaussian noise: lognormal multiplicative alpha = Psi*W (E W = 1) and a mixture with a 'quiet' atom; the
     recombined amplitude is set by anti-concentration at the one-photon scale, not by the variance.
(A5) LCU: with complex amplitudes a coherent sum of different unitaries can be unitary (two-level example), but the
     result is not the mean of the U_P; and with psi >= 0 a convex combination of distinct unitaries is never unitary.
"""
import numpy as np
from scipy.special import gammaln
rng = np.random.default_rng(20261012)

def haar(n):
    z = (rng.normal(size=(n, n)) + 1j*rng.normal(size=(n, n)))/np.sqrt(2)
    q, r = np.linalg.qr(z); d = np.diag(r); return q*(d/np.abs(d))

print("=== (A1) Theorem A: configuration-diagonal coupling -> mixture, for any phases ===")
K, dL = 6, 4
U = [haar(dL) for _ in range(K)]
chi0 = np.zeros(dL, complex); chi0[0] = 1
w = rng.dirichlet(np.ones(K))                      # |psi|^2 = configuration weights
for trial, phases in enumerate([np.zeros(K), rng.uniform(0, 2*np.pi, K), np.pi*np.arange(K)/3]):
    psi = np.sqrt(w)*np.exp(1j*phases)
    joint = np.zeros((K, dL), complex)            # rows: substrate basis |P>, cols: light
    for P in range(K): joint[P] = psi[P]*(U[P] @ chi0)
    rhoL = joint.T @ joint.conj()                 # Tr_S |joint><joint|  (rho_ij = sum_P c_Pi c*_Pj)
    mix = sum(w[P]*np.outer(U[P] @ chi0, (U[P] @ chi0).conj()) for P in range(K))
    VS = haar(K)                                  # arbitrary later substrate-only unitary (recombination attempt)
    joint2 = VS @ joint
    rhoL2 = joint2.T @ joint2.conj()
    print(" phases set %d: ||rho_L - mixture|| = %.2e ; after substrate-only unitary ||rho_L' - rho_L|| = %.2e ; purity Tr rho^2 = %.4f" %
          (trial, np.abs(rhoL - mix).max(), np.abs(rhoL2 - rhoL).max(), np.real(np.trace(rhoL @ rhoL))))

print("\n=== (A2) final-state projection onto |Sigma>: mean-propagated state; success prob = 1 - variance ===")
psi = np.sqrt(w)*np.exp(1j*rng.uniform(0, 2*np.pi, K))
Sig = psi.copy()
joint = np.array([psi[P]*(U[P] @ chi0) for P in range(K)])
post = Sig.conj() @ joint                         # <Sigma|_S joint
meanU = sum(w[P]*(U[P] @ chi0) for P in range(K))
var = sum(w[P]*np.linalg.norm(U[P] @ chi0 - meanU)**2 for P in range(K))
print(" ||post - E U chi0|| = %.2e ; success prob ||post||^2 = %.6f ; 1 - E||U chi - mean||^2 = %.6f" %
      (np.linalg.norm(post - meanU), np.linalg.norm(post)**2, 1 - var))

print("\n=== (A3) coherent-state recombination with circular Gaussian noise ===")
Nf = 120
n = np.arange(Nf)
def coh(beta):
    return np.exp(-abs(beta)**2/2 + n*np.log(np.abs(beta) + 1e-300) + 1j*n*np.angle(beta) - 0.5*gammaln(n + 1))
def avgD(alphas):
    # E D(alpha)|0> = E coherent(alpha), averaged over samples
    out = np.zeros(Nf, complex)
    for a in alphas: out += coh(a)
    return out/len(alphas)
for Psi, V in [(1.0, 0.1), (1.0, 1.0), (2.0, 4.0), (1.5, 20.0), (3.0, 100.0)]:
    M = 40000
    d = np.sqrt(V/2)*(rng.normal(size=M) + 1j*rng.normal(size=M))
    st = avgD(Psi + d)
    pred = (2/(2 + V))*np.exp(-Psi**2*V/(2 + V)**2)*coh(2*Psi/(2 + V))
    nrm = np.linalg.norm(st)
    a_obs = np.vdot(st[:-1], np.sqrt(n[1:])*st[1:])/nrm**2          # <a> in the normalized recombined state
    print(" Psi=%.1f V=%6.1f: MC norm %.5f  closed-form norm %.5f  ||MC-pred||/||pred|| = %.3f ; <a>_rec = %.4f%+.4fi vs 2Psi/(2+V) = %.4f ; mean-field Psi = %.1f" %
          (Psi, V, nrm, np.linalg.norm(pred), np.linalg.norm(st - pred)/np.linalg.norm(pred), a_obs.real, a_obs.imag, 2*Psi/(2 + V), Psi))

print("\n=== (A4) non-Gaussian noise: recombined amplitude is controlled by anti-concentration at 1 photon ===")
def pair_stats(alpha, maxpairs=4_000_000):
    # norm^2 = E_{P != P'} exp(-|a|^2/2 - |a'|^2/2 + conj(a') a) ; <a>_rec = E[a e^{..}]/norm^2 (independent pairs)
    R = len(alpha); idx = rng.integers(0, R, size=(min(maxpairs, R*R), 2)); idx = idx[idx[:, 0] != idx[:, 1]]
    a = alpha[idx[:, 0]]; b = alpha[idx[:, 1]]
    k = np.exp(-abs(a)**2/2 - abs(b)**2/2 + np.conj(b)*a)
    N2 = k.mean(); A = (a*k).mean()/N2
    return np.abs(N2), A
Psi = 1.0
for label, gen in [
        ("circular Gaussian, V=50", lambda M: Psi + np.sqrt(25)*(rng.normal(size=M) + 1j*rng.normal(size=M))),
        ("lognormal multiplicative, E|W|^2=51", lambda M: Psi*np.exp((s := np.sqrt(np.log(51.0)))*rng.normal(size=M) - s**2/2)*np.exp(1j*rng.uniform(-0.0, 0.0, M))),
        ("lognormal amp x uniform phase", lambda M: Psi*np.exp((s := np.sqrt(np.log(51.0)/1.0))*rng.normal(size=M) - s**2/2)*np.exp(1j*rng.uniform(0, 2*np.pi, M))),
        ("90% quiet (alpha=Psi) + 10% Gaussian V=500", lambda M: np.where(rng.uniform(size=M) < 0.9, Psi + 0j, Psi + np.sqrt(250)*(rng.normal(size=M) + 1j*rng.normal(size=M)))),
        ]:
    al = gen(4000)
    Vemp = np.var(al.real) + np.var(al.imag)
    N2, A = pair_stats(al)
    print(" %-45s var=%.1f |E alpha|=%.3f : recombination prob ~ %.4f ; <a>_rec = %.3f%+.3fi (Gaussian formula 2Psi/(2+V) = %.4f)" %
          (label, Vemp, abs(al.mean()), N2, A.real, A.imag, 2*abs(al.mean())/(2 + Vemp)))

print("\n=== (A5) linear combination of unitaries ===")
sz = np.diag([1, -1]).astype(complex)
c1, c2 = 1/np.sqrt(2), 1j/np.sqrt(2)
Wm = c1*np.eye(2) + c2*sz
print(" (1/sqrt2) 1 + (i/sqrt2) sigma_z unitary? ||W^dag W - 1|| = %.1e ; but the mean (1+sigma_z)/2 = diag(1,0) is not." %
      np.abs(Wm.conj().T @ Wm - np.eye(2)).max())
# convex combination of distinct unitaries: strictly contractive on some vector
Ws = 0.5*U[0] + 0.5*U[1]
print(" convex 0.5 U0 + 0.5 U1: min singular value %.4f (<1, so never unitary unless U0 = U1 up to nothing)" % np.linalg.svd(Ws, compute_uv=False).min())
