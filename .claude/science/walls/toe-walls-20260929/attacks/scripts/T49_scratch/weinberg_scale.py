"""Part C: numbers for W2, no pass/fail.  If lepton number is not exact, the lowest lepton-number
violating operator built from the SM doublet is the dimension-5 Weinberg operator (LH)(LH)/Lambda.
Its neutrino mass is c v^2 / Lambda.  With the repo's only scale a^-1 = M_Pl (scale_reference_primitive):"""
import math
v = 246.3           # GeV, value used in docs (W2 arm b)
MPl = 1.22089e19    # GeV, same value as walls/L10_scratch/ladder_and_dirac.py
aLM = 2*0.045333918 # as in L10_scratch/ladder_and_dirac.py
m_target = 0.05e-9  # GeV (0.05 eV atmospheric)
m_W = v**2/MPl      # GeV
print(f"v^2/M_Pl = {m_W:.3e} GeV = {m_W*1e9:.3e} eV")
c = m_target/m_W
print(f"coefficient c needed for 0.05 eV: {c:.3e};  log10 c = {math.log10(c):.2f};  1/alpha_LM^k for k=4: {aLM**-4:.3e}; k=3.83 -> {aLM**-3.83:.3e}")
print(f"exponent k with c = alpha_LM^-k: {-math.log(c)/math.log(aLM):.3f}")
# Dirac arm: y needed
y_need = m_target*math.sqrt(2)/v
print(f"Dirac arm: y_nu needed = {y_need:.3e}; y_eff = g^2/64 = 6.66e-3 -> suppression {y_need/6.66e-3:.3e}; exponent in alpha_LM: {math.log(y_need/6.66e-3)/math.log(aLM):.3f}")
# probability of hitting within 13% by a random exponent for step 1/aLM
print(f"chance a random log-position lies within +-13% of a rung of step 1/alpha_LM={1/aLM:.2f}: {2*math.log(1.13)/math.log(1/aLM):.3f}")
