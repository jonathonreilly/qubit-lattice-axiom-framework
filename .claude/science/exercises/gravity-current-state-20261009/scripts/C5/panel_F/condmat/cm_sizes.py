"""Panel F condmat lens: sizes and locality of the root's D1 edge (archived dirac.py/sublum.py, unmodified copies in arch/)."""
import sys, numpy as np
sys.path.insert(0, sys.argv[1])
from dirac import D1
law = D1(0.909103708, 0.555604226)
Wpi = float(law.W(np.pi)); print(f"W(pi) = {Wpi:.6f} /a  -> corner (doubler) masses m + n*W(pi), n=1..3: {[round(n*Wpi,4) for n in (1,2,3)]}")
# hopping range: Fourier coefficients of s(k) and W(k) on a fine 1D grid
N = 4096; k = 2*np.pi*np.arange(N)/N - np.pi
s = law.S(k); W = law.W(k)
cs = np.fft.fft(np.fft.ifftshift(s))/N; cw = np.fft.fft(np.fft.ifftshift(W))/N
for r in (1,2,4,8,16,32,64,128):
    print(f"hop range r={r:4d}: |s_r| = {abs(cs[r]):.3e}   |W_r| = {abs(cw[r]):.3e}")
# physical sizes, a = Planck length (non-reduced)
lP = 1.616255e-35; hbarc_GeVm = 1.973269804e-16; MP = hbarc_GeVm/lP
alpha = 1/137.036; e2 = 4*np.pi*alpha
print(f"1/a = {MP:.3e} GeV")
dm_qed = 0.041858390*e2*MP; print(f"QED additive mass on root edge: 0.04186 e^2/a = {0.041858390*e2:.3e}/a = {dm_qed:.2e} GeV = {dm_qed/0.000511:.1e} m_e")
for name, mass in [("electron",0.000511),("u quark (2.2 MeV)",0.0022),("nucleon",0.938),("top",172.6)]:
    lam = hbarc_GeVm/mass
    print(f"{name:18s}: reduced Compton {lam:.2e} m = {lam/lP:.1e} sites; m*a = {mass/MP:.1e}")
print(f"proton charge radius 0.84 fm = {0.84e-15/lP:.1e} sites")
# per-fermion strain mass shift for a GW of amplitude h (SF units t ~ h), Hessian +2.424e-2 e^2/a
for h in (1e-21, 1e-9):
    dmf = 0.5*2.42401e-2*e2*h**2*MP*1e9
    print(f"uncancelled per-fermion mass shift at strain {h:g}: {dmf:.2e} eV")
# evanescence: F1 Earth |m_g| = 3.6e-9 eV
mg = 3.6e-9; hbarc_eVm = 1.973269804e-7; hP = 4.135667696e-15
print(f"m_g=3.6e-9 eV: cutoff frequency {mg/hP:.2e} Hz; decay length {hbarc_eVm/mg:.1f} m; amplitude after 9.3e6 m: exp(-{9.3e6*mg/hbarc_eVm:.2e})")
# GR's own medium scale for Earth rock: 4 pi G rho
G=6.674e-11; rho=5.5e3; hbar_eVs=6.582119569e-16
print(f"GR medium scale sqrt(4 pi G rho) for rho=5.5e3: {np.sqrt(4*np.pi*G*rho):.2e} 1/s = {np.sqrt(4*np.pi*G*rho)*hbar_eVs:.1e} eV; F2 bound in rock ~2.9e-13 eV")
print(f"ratio F1 mu_rho / (4 pi G)-scale per mass: {2.42e-21/((4*np.pi*G)*hbar_eVs**2):.1e}")
