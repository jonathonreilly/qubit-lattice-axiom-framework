"""Lane RI, probe I3, script 4: L* readouts for the separable (per-axis) flattening, from i3_cubic_designs.out values."""
B = 5.7e-99; Bfw = 9.0e-102
muE_NN, muT_NN = 3.69453e-3, 1.17819e-2
L = 64; muE, muT, px, rho = 1.20605e-5, 5.74119e-7, 1.53607e-4, 6.35917e-2
cE = muE * L**2 / muE_NN; cT = muT * L**3 / muT_NN
print(f"separable-flat: mu_E/mu_E(NN) = {cE:.3f} L^-2 ; mu_T2/mu_T2(NN) = {cT:.3f} L^-3 (fits from L=64)")
for tag, b in (("refereed 5.7e-99", B), ("framework 9.0e-102", Bfw)):
    print(f"  P0 {tag}: L*(mu_E) = {(cE/b)**0.5:.3e} ; L*(mu_T2) = {(cT/b)**(1/3):.3e}")
Lcap = 7.650e14
print(f"at the observational cap L = {Lcap:.2e}: separable mu_E/natural >= {cE*Lcap**-2:.2e}, mu_T2/natural >= {cT*Lcap**-3:.2e}")
