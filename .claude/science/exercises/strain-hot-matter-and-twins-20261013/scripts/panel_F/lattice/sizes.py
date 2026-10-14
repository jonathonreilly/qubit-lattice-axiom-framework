"""Panel F lattice lens: sizes, doubler masses, additive-mass size, medium cutoff. Reads repo D1 class (unmodified)."""
import sys, numpy as np
R='/Users/jonBridger/Projects/Physics-baremetal-probes/.claude/worktrees/toe-leverage-analysis-e8a790/.claude/science/exercises/gravity-current-state-20261009/scripts/C5/R18-5'
sys.path.insert(0, R)
from dirac import D1
hbarc_eVm = 1.973269804e-7      # eV m
lP = 1.616255e-35               # m
EP_GeV = hbarc_eVm/lP/1e9       # 1/a in GeV for a = l_P
print(f"1/a (a=l_P) = {EP_GeV:.4e} GeV")
# (b) doubler masses on the R18-9 root
law = D1(0.909103708, 0.555604226)
Wpi = float(law.W(np.pi)); print(f"W(pi) = {Wpi:.6f} /a ; doubler masses n*W(pi), n=1,2,3: {[round(n*Wpi,4) for n in (1,2,3)]} /a")
print(f"  -> {Wpi*EP_GeV:.3e}, {2*Wpi*EP_GeV:.3e}, {3*Wpi*EP_GeV:.3e} GeV")
print(f"S(pi/2) = {float(law.S(np.pi/2)):.4f}, S(pi) = {float(law.S(np.pi)):.2e}  (odd, zero at pi: NN doublers)")
# additive mass, one loop, R19-34/F1: dm = 0.041858390 e^2 /a
dm1 = 0.041858390
for name, g2 in [("QED e^2=4pi/137", 4*np.pi/137.036), ("QED e^2=0.1 (packet)", 0.1), ("QCD C_F g^2, g^2=0.3", 4/3*0.3), ("QCD C_F g^2, g^2=0.25", 4/3*0.25)]:
    print(f"  delta m ({name}) = {dm1*g2:.3e}/a = {dm1*g2*EP_GeV:.3e} GeV")
print(f"  standard Wilson QCD one-loop |am_c| ~ 51.43*C_F/(16pi^2) g^2 = {51.43*4/3/(16*np.pi**2):.3f} g^2 (RECALLED)")
me = 0.51099895e-3
print(f"  m_e / (QED delta m) = {me/(dm1*4*np.pi/137.036*EP_GeV):.2e}  (cancellation precision needed at h=0)")
# (c) sizes
for name, mGeV in [("electron",0.51099895e-3),("up quark ~2.2MeV",2.2e-3),("down ~4.7MeV",4.7e-3),("muon",0.1056584),("proton (Compton)",0.938272),("top",172.7)]:
    lam = hbarc_eVm/(mGeV*1e9)
    print(f"  {name:18s} reduced Compton {lam:.3e} m = {lam/lP:.3e} a ; (lam/a)^3 = {(lam/lP)**3:.1e} sites")
rp = 0.8409e-15
print(f"  proton charge radius {rp:.3e} m = {rp/lP:.3e} a ; sphere volume {(4/3*np.pi*(rp/lP)**3):.1e} sites")
print(f"  hydrogen Bohr radius 5.29e-11 m = {5.29e-11/lP:.2e} a")
# medium: F1 |m_g| Earth 3.6e-9 eV
mg = 3.65e-9; h_eVs = 4.135667696e-15
print(f"F1 Earth |m_g| = {mg:.2e} eV -> cutoff freq m c^2/h = {mg/h_eVs:.3e} Hz ; evanescent decay length hbar c/m = {hbarc_eVm/mg:.1f} m (for omega << m)")
print(f"  100 Hz quantum hbar*omega = {h_eVs*100:.3e} eV")
# GR medium scale for comparison: sqrt(4 pi G rho) in Earth
G=6.674e-11; rho=5514.; hbar_eVs=6.582119569e-16
w=np.sqrt(4*np.pi*G*rho); print(f"GR Jeans-type rate in Earth sqrt(4 pi G rho) = {w:.3e} 1/s -> {w*hbar_eVs:.3e} eV ; mu_rho ~ {(w*hbar_eVs)**2/rho:.2e} eV^2 m^3/kg vs F2 bound 1.5e-29")
# strain per fermion: 1/2 dm'' t^2 with dm''=0.0242 e^2/a (SF units)
for h in (1e-21, 1e-9):
    print(f"  per-fermion shift at strain {h:g}: 0.5*0.0242*e2*h^2/a = {0.5*0.0242*0.0917*h*h*EP_GeV:.2e} GeV")
