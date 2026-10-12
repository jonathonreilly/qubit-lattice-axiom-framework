"""R6-5 (c): bounds (Kostelecky-Russell Data Tables, Jan 2026 update, arXiv:0801.0287v19, fetched; see downloads_kr/)
and tuning arithmetic.  Natural sizes are those of the explicit law in r65_cme*.out with a = l_P; they are model
numbers, not a universal natural-size theorem (cf. C5_O1_referee.md:27-36)."""
import numpy as np
MPl = 1.221e19          # GeV, non-reduced; a = 1/MPl
MPl_red = 2.435e18
beta_cmb = 369.82 / 299792.458   # Sun velocity w.r.t. CMB dipole frame
# --- bounds (GeV)
bT = {'e': 1e-26, 'p': 1e-26, 'n': 1e-27}            # Table S2, b~_T, Sun-centred frame (orders of magnitude)
bperp = {'e': 1.4e-31, 'p': 7.6e-33, 'n': 1.3e-33}   # D6 [52] Heckel 2008 (sigma of b~_X); D10 [108] He/Xe; D15 [124] Allmendinger
# --- natural sizes from the explicit law (lattice units -> GeV)
nat = {'tree, b = 1/a': 1.0 * MPl, 'tree, b = 0.1/a': 0.1 * MPl,
       'one-loop induced, G*chi5*b with G=0.1 a^2, chi5=0.507/a^2, b=0.1/a': 0.1 * 0.507 * 0.1 * MPl,
       'tree, b = 0.1/a, reduced Planck': 0.1 * MPl_red}
print("beta(CMB) = %.4e" % beta_cmb)
for s in ('e', 'p', 'n'):
    lim_boost = bperp[s] / beta_cmb
    print("species %s: b~_T(SCF) < %.0e GeV ; CMB-frame b0 via boost into b~_perp: < %.1e / %.3e = %.1e GeV (assumes lattice frame = CMB frame)"
          % (s, bT[s], bperp[s], beta_cmb, lim_boost))
    for name, v in nat.items():
        print("   %-70s %.1e GeV : tuning %.1f decades (b~_T), %.1f decades (boost route)"
              % (name, v, np.log10(v / bT[s]), np.log10(v / lim_boost)))
# --- (k_AF)_0
kAF_bound = 7.4e-45; k3_hint = (7.32e-45, 2.94e-45)
print("(k_AF)_0: bound %.1e GeV (Caloni et al 2023, D19 [144]); isotropic k(3)_(V)00 = (%.2f +- %.2f)e-45 GeV (Minami-Komatsu 2020 / Nilsson-Le Poncin-Lafitte 2024, D19 [142],[143])"
      % (kAF_bound, k3_hint[0] / 1e-45, k3_hint[1] / 1e-45))
print("   if it were unprotected at the anomaly size b/(4 pi^2)*e^2 with b=0.1/a: %.1e GeV -> %.1f decades (NOT the reading: protected, see r65_cme2.out)"
      % (0.0917 * 0.1 * MPl / (4 * np.pi ** 2), np.log10(0.0917 * 0.1 * MPl / (4 * np.pi ** 2) / kAF_bound)))
# --- d=5 on-shell CPT-odd photon term from the lattice-scale P-odd sector (side result)
e2 = 4 * np.pi / 137.036
kon = 3.0e-4     # r65_cme2.out, m=0.3/a, b=0.1/a, e=1, lattice units (k/q^2 on shell)
k5 = e2 * kon / MPl
print("d=5 on-shell: k/q^2 = e^2 * %.1e * a = %.1e GeV^-1 ; Table S3 isotropic k(5)_(V)00 sensitivity ~1e-34 GeV^-1 -> ~%.0f decades (normalisation factors O(sqrt(4 pi)) not matched)"
      % (kon, k5, np.log10(k5 / 1e-34)))
