"""O2 check 2: the equivalence principle measures the band-bottom curvature beta = Hess(E^2/2)|_{k=0}.

(i) Exact semiclassical statement for a Hamiltonian lattice whose static gravity enters as
    H -> sum_x (1+Phi(x)) h(x)  (h_00 coupled to the conserved energy density):
    a wavepacket of a band E_B(k) obeys dk/dt = -grad Phi * E_B, dx/dt = (1+Phi) grad_k E_B,
    so at k->0: d2x/dt2 = -grad Phi * E_B(0) * Hess E_B(0) = -beta_B grad Phi.
    Universality of free fall <=> beta_A = beta_B ; eta_AB = (beta_A - beta_B)/beta.
    Checked numerically below by integrating Hamilton's equations for two toy bands.
(ii) Estimate (sector-additive inertia of energy, an ASSUMPTION): beta_B = sum E_s / sum(E_s/beta_s),
    so eta ~ sum_s (f_s^A - f_s^B) * (delta beta_s / beta).  MICROSCOPE Ti vs Pt numbers from memory.
"""
import numpy as np

# ---- (i) numerical check of the fall law with two bands of different beta, same rest energy
def band(beta, E0):
    # E(k)^2 = E0^2 + beta * sum 2(1-cos k)   (nn lattice band; Hess(E^2/2) at 0 = beta I)
    E = lambda k: np.sqrt(E0**2 + beta*np.sum(2*(1-np.cos(k))))
    gE = lambda k: beta*np.sin(k)/E(k)
    return E, gE

def fall(beta, E0, g=1e-6, T=200.0, dt=0.01):
    E, gE = band(beta, E0)
    x = np.zeros(3); k = np.zeros(3)
    Phi_grad = np.array([0,0,g])         # Phi = g z
    for _ in range(int(T/dt)):           # leapfrog on H = (1+Phi(x)) E(k)
        k = k - 0.5*dt*Phi_grad*E(k)
        x = x + dt*(1+g*x[2])*gE(k)
        k = k - 0.5*dt*Phi_grad*E(k)
    return x[2]

T = 200.0; g = 1e-6
for beta, E0 in ((1.0, 1.0), (1.0, 5.0), (1.02, 1.0), (1.02, 5.0)):
    z = fall(beta, E0, g, T)
    a_eff = -2*z/T**2
    print(f"beta={beta:5.2f} E0={E0:4.1f}: measured a/g = {a_eff/g:.6f}  (prediction beta = {beta})")

# ---- (ii) MICROSCOPE translation (inputs from memory; labelled)
m_u = 931.494   # MeV
m_e = 0.51100
aC = 0.711      # MeV, semi-empirical Coulomb coefficient
def fractions(A, Z, BA):
    M = A*m_u
    fC = aC*Z*(Z-1)/A**(1/3)/M          # nuclear Coulomb self-energy fraction
    fe = Z*m_e/M                        # electron rest-energy fraction
    fs = (BA*A + aC*Z*(Z-1)/A**(1/3))/M # strong binding fraction (binding + Coulomb), magnitude
    fn = (A-Z)/A                        # neutron number fraction (proxy for n-vs-p channel)
    return dict(fC=fC, fe=fe, fs=fs, fn=fn)
Ti = fractions(48, 22, 8.723)
Pt = fractions(195, 78, 7.927)
eta_bound = 7e-15   # ~2 sigma from MICROSCOPE final: (-1.5 +- 2.3 stat +- 1.5 syst)e-15 (from memory)
print("\nchannel   f(Ti)       f(Pt)       Delta f     bound |dbeta/beta| <= eta/|Delta f|")
for ch in ("fC","fe","fs","fn"):
    d = Pt[ch]-Ti[ch]
    print(f"{ch:6s}  {Ti[ch]:.3e}  {Pt[ch]:.3e}  {d:+.3e}   {eta_bound/abs(d):.1e}")
dc = 8.55e-3     # F2 refereed one-loop c_e - c_gamma on Z^3 x R (used as the natural QED-loop scale)
dbeta = 2*dc
dfC = Pt["fC"]-Ti["fC"]
print(f"\nF2-size photon-vs-matter split: dbeta/beta = {dbeta:.2e} -> eta ~ {dbeta*abs(dfC):.1e} "
      f"vs bound {eta_bound:.0e}: excess x{dbeta*abs(dfC)/eta_bound:.1e}")
