"""GR-lens arithmetic for panel F. Plain floats; constants RECALLED (CODATA-level)."""
import math
hbarc = 1.973269804e-7      # eV m
lP = 1.616255e-35            # m (non-reduced Planck length)
MPl = 1.220890e28            # eV (non-reduced)
G = 6.67430e-11; c = 2.99792458e8; hbar = 1.054571817e-34
e2 = 4*math.pi/137.036       # e^2 at low energy (the repo's e^2 ~ 0.1)
mN = 1.67262192e-27          # kg
print("== (b) additive mass on the root edge: delta m a = 0.04186 e^2 (rR19-34:12)")
dm_a = 0.04186*e2
print(f"  delta m a = {dm_a:.3e}; delta m = {dm_a*MPl/1e9:.3e} GeV = {dm_a:.2%} of 1/a; / m_e = {dm_a*MPl/0.51099895e6:.2e}")
print("== (c) sizes in Planck lengths (reduced Compton wavelength hbar/mc)")
for name, m_eV in [("electron",0.51099895e6),("up quark (current, 2.2 MeV)",2.2e6),("proton",938.272e6),("top",172.7e9)]:
    lam = hbarc/m_eV
    print(f"  {name:28s} hbar/mc = {lam:.3e} m = {lam/lP:.2e} sites; in BZ: k a = {lP/lam:.1e}")
print(f"  proton charge radius 0.841 fm = {0.841e-15/lP:.2e} sites; volume ~ {(0.841e-15/lP)**3*4*math.pi/3:.1e} sites")
print("== elastic-medium comparator: L = (1/64piG)(hdot^2-(grad h)^2) - mu_s h_ij h_ij/4  =>  m_g^2 = 16 pi G mu_s / c^2")
for name, mu in [("crust 3e10 Pa",3e10),("mantle 1e11 Pa",1e11),("steel 8e10 Pa",8e10)]:
    w2 = 16*math.pi*G*mu/c**2          # s^-2
    print(f"  {name:16s} omega_g = {math.sqrt(w2):.2e} rad/s, |m_g| = {hbar*math.sqrt(w2)/1.602176634e-19:.2e} eV")
print("== framework channel per nucleon (canonical: mu = n * w * Hess; F1 Hess_t = 2.424e-2 e^2 /a; w_N = 5.2 = 13 x C_F g_s^2)")
Hess_e2 = 2.42401e-2
wN = 5.2; we = 0.1
perN_eV = wN*Hess_e2*MPl   # energy per nucleon per unit (h_ij h_ij /4)... = Hess * w in eV (Planck units -> eV)
rho = 5500.0; n = rho/mN
mu_planck = n*lP**3*(wN*Hess_e2 + 0.5*we*Hess_e2)
mg = math.sqrt(16*math.pi*mu_planck)/lP*hbarc
print(f"  Earth rho=5500: n a^3 = {n*lP**3:.2e}; |m_g| = {mg:.2e} eV (F1 quotes 3.6e-9)")
mu_rock_perN = 1e11/n/1.602176634e-19
print(f"  stiffness per nucleon: lattice channel w*Hess*M_Pl = {perN_eV:.2e} eV  vs rock mu_shear/n = {mu_rock_perN:.2e} eV  ratio {perN_eV/mu_rock_perN:.1e}")
print("== GW170817 in rock with |m_g| = 3.6e-9 eV")
for f in (30,100,400):
    E = 2*math.pi*f*hbar/1.602176634e-19
    print(f"  f={f:4d} Hz: hbar omega = {E:.2e} eV; m_g/omega = {3.6e-9/E:.1e}")
L = hbarc/3.6e-9
print(f"  evanescence length hbar c/m_g = {L:.1f} m; e-folds over 9293 km chord = {9.293e6/L:.2e}")
print("  surface near-node: |h(0)|/|h_inc| ~ 2 k/kappa at 100 Hz:", f"{2*(2*math.pi*100/c)*L:.1e}")
print("== per-fermion mass shift without the rule, delta m = 1/2 Hess h^2 (electron weight e^2; Hess_t e^2/a)")
H_e = Hess_e2*e2*MPl
for lab, h in [("GW h=1e-21",1e-21),("static traceless strain ~ Phi_Earth 7e-10 (only if the lattice frame carries it)",7e-10),("~ Phi_Sun@1AU 1e-8",1e-8),("~ Phi_Galaxy 1e-6",1e-6)]:
    print(f"  {lab:80s} delta m_e ~ {0.5*H_e*h*h:.1e} eV")
print("== sensitivity to the fermion cutoff a_f (m_g^2 ~ 16 pi G n Hess/a_f): Earth row exceeded by 1.6e8 in mu")
print(f"  passes without any rule only if 1/a_f < M_Pl/1.6e8 = {1.2209e19/1.6e8:.1e} GeV")
