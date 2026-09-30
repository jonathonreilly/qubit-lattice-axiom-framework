import math
hbar=6.582119569e-25; M1=5.323e10; vh=174.1; m=0.0503e-9
# standard type-I seesaw with v=174 GeV: m_nu = y^2 v^2 / M  (m_D = y v)
y2=M1*m/vh**2
G=y2*M1/(8*math.pi); print("standard seesaw: y^2=%.3e  Gamma=%.3e GeV tau=%.2e s"%(y2,G,hbar/G))
# attack used m = y^2 v^2/(2M)
y2a=2*M1*m/vh**2; Ga=y2a*M1/(8*math.pi); print("attack (extra factor 2): y^2=%.3e Gamma=%.3e tau=%.2e s"%(y2a,Ga,hbar/Ga))
# lane: k_decay = mtilde/m* = 47.24, m* = 1.08e-3 eV (standard equilibrium neutrino mass), Gamma/H(T=M1)
MPl=1.2209e19; gs=106.75; H=1.66*math.sqrt(gs)*M1**2/MPl
print("H(T=M1)=%.3e GeV ; 47.24 H = %.3e GeV ; tau = %.2e s"%(H,47.24*H,hbar/(47.24*H)))
print("mtilde implied by k=47.24 with m*=1.08e-3 eV: %.4f eV"%(47.24*1.08e-3))
tuniv=4.35e17; print("y needed for tau>t_univ (standard): y < %.2e ; ratio to y: %.1e"%(math.sqrt(8*math.pi*hbar/tuniv/M1), math.sqrt(8*math.pi*hbar/tuniv/M1)/math.sqrt(y2)))
