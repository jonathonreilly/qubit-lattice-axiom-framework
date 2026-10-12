"""Q1 (C): physical translation of the quantum readings, using the refereed RZ/RL4/Y1 numbers.
Inputs (refereed): photon l_k = 7.9e-20 m (X1, collider bar), eps = (l_P/l_k)^4, proved rate c_low = 0.628 (RL4),
RZ in-band budget after every correction and a 1000-e-fold allowance: ln(N_B/S) >= 43,986 at 1 s / 1 Gpc (RZ referee);
for longer emission depths the rate budget gamma*tau (Y1/Z1 tables) minus <= 1150 e-folds of penalties."""
import numpy as np
hbar_c = 197.327e-15*1e6   # eV m  (197.327 MeV fm)
lP = 1.616e-35; lk = 7.9e-20; c = 2.998e8; Gpc = 3.086e25
eps = (lP/lk)**4; gam = 0.628*np.sqrt(eps)/lk
print("l_k = %.2g m -> hbar c/l_k = %.3g TeV ; eps = %.3g ; proved variance rate gamma = %.3g /m (one e-fold per %.3g m = %.2f h of c*t)" %
      (lk, hbar_c/lk/1e12, eps, gam, 1/gam, 1/gam/c/3600))
def tau(D, dt): return np.sqrt(2*D*c*dt + (c*dt)**2)   # (D+c dt)^2 - D^2 without cancellation
rows = [("lensed, 1 Gpc, 1 s", 43986.0), ("lensed, 1 Gpc, 8 h", gam*tau(Gpc, 8*3600) - 1150), ("lensed, 1 Gpc, 1 yr", gam*tau(Gpc, 3.156e7) - 1150),
        ("quasar 1e7 yr, 1 Gpc", gam*tau(Gpc, 3.156e14) - 1150)]
print("\n(1) Mixture reading (Theorem A): first-order coherence of the image with the GR (mean) mode, in band")
for name, nB in rows:
    print("   %-24s ln(N_B/S) >= %.4g  ->  Gamma_B = S/(S+N_B) <= exp(-%.4g) ; excess flux N_B/S >= e^%.4g" % (name, nB, nB, nB))
print("   observational need: VLBI visibility of lensed components O(0.1-1) and flux ratios to 10-20%% -> Gamma_B >~ 0.1-0.8, N_B/S <~ 0.2")
print("\n(2) Recombination reading (Gaussian per-mode noise; exact formula <a>_rec = 2 Psi/(2+V_ph), V_ph = nbar * N_B/S):")
for lab, nbar in [("radio core, T_b = 1e11 K at 5 GHz", 1.38e-23*1e11/(6.626e-34*5e9)),
                  ("optical disk, T_b = 3e4 K at 5.5e14 Hz", 1/np.expm1(6.626e-34*5.5e14/(1.38e-23*3e4))),
                  ("absurdly faint, nbar = 1e-100", 1e-100)]:
    nB = rows[0][1]; lnV = nB + np.log(nbar)
    print("   %-40s nbar = %.3g : ln V_ph = %.5g -> amplitude factor 2/(2+V_ph) = exp(-%.5g), flux factor exp(-%.5g)" %
          (lab, nbar, lnV, lnV - np.log(2), 2*(lnV - np.log(2))))
print("   observational need: lensed fluxes agree with smooth GR models to 10-20%% -> 4/(2+V_ph)^2 >= 0.8 -> V_ph <= %.3f" % (2/np.sqrt(0.8) - 2))
print("\n(3) Matter as a which-sprinkling recorder (shared l_k; SUGGESTED that matter's own per-realization noise has the same rate):")
for lab, T in [("1 hour", 3600), ("1 day", 86400), ("1 year", 3.156e7), ("1 Gyr", 3.156e16), ("13.8 Gyr", 13.8*3.156e16)]:
    print("   matter quantum of age %-9s : gamma c T = %.3g variance e-folds (overlap of its state between two independent sprinklings ~ e^-that)" % (lab, gam*c*T))
for lab, dt in [("1 s", 1.0), ("1 yr", 3.156e7)]:
    ta = tau(Gpc, dt); w = ta/2
    ncmb, nigm = 4.11e8, 0.25
    Ncmb = ncmb*np.pi*w**2*Gpc*(2/3); Nigm = nigm*np.pi*w**2*Gpc*(2/3)
    print("   needle of a %-4s lensed source at 1 Gpc: proper time %.2g m, transverse half-width %.2g m (%.2g pc); CMB photons inside ~%.1g, IGM baryons ~%.1g" %
          (lab, ta, w, w/3.086e16, Ncmb, Nigm))
print("   -> negligible decoherence needs the summed per-quantum which-sprinkling infidelity over these N quanta to be << 1, i.e. below ~1/N each")
print("\n(4) Records alone (Record axiom: a record pins its event): events per m^3 per s = c/l_P^4 = %.2g ; record formation in air ~ %.2g ; fraction %.1g" %
      (c/lP**4, 7e9*2.5e25, 7e9*2.5e25/(c/lP**4)))
print("\n(5) Kinematics behind the spectrum-condition lemma: q = k - k' for null k, k'")
rng = np.random.default_rng(3)
k = np.array([1.0, 0, 0, 1.0]); kp = rng.normal(size=(100000, 3)); kp /= np.linalg.norm(kp, axis=1)[:, None]
om = rng.uniform(0.01, 2, 100000); kp4 = np.column_stack([om, om[:, None]*kp]); q = k[None, :] - kp4
q2 = -q[:, 0]**2 + (q[:, 1:]**2).sum(1)    # signature (-,+,+,+); q2 >= 0 means spacelike or null
print("   min over 1e5 random null k': q^2 = %.3e (>= 0: momentum transfer between on-shell photons is never timelike)" % q2.min())
print("   a substrate whose fluctuation spectrum is supported in the closed forward cone (spectrum condition) cannot absorb it;")
print("   a Poisson (white) substrate has S(q) = rho for every q, so it can -> single-scattering (first-chaos) incoherent power > 0.")
