#!/usr/bin/env python3 -I
# checks/e1c_largefield_posthoc.py -- POST-HOC. Written AFTER seeing e1_sweep.py's output,
# carries NO pre-registered verdict, and is labelled post-hoc in EPS1_SWEEP.md §4.
# It prices the one thing TAUFLAT named and did not quantify: the size of the large-field region.
# Exact Fraction; Decimal for display only.
from fractions import Fraction as F
from decimal import Decimal, getcontext
getcontext().prec = 60
def dec(x,p=40):
    getcontext().prec=p
    return +x if isinstance(x,Decimal) else Decimal(x.numerator)/Decimal(x.denominator)
def L10(x,p=50): return dec(x,p).log10()
def E(m,e): return F(m)*F(10)**e
EPS_T, EPS_P = E("6.7",-40), E("9.38495112638",-45)     # E_p = the EXACT bound (e1b)
C_FLAT,C_PRIME,THETA,N,L = F(1,640),F(53),F(1,24),F(2),F(3)
C_PR = C_FLAT/C_PRIME**2
B_N_82, LOG12800 = F(5381106005), F(9457,1000)          # HW l.2006 / l.1639
G_DX2 = E("2.456",-152)                                  # REVIEW_SF_S7 l.203
def a_bad(e): return C_PR*e*e
def g2_crc(e): return THETA*a_bad(e)/(B_N_82+LOG12800)
# PROOF.md l.4307-4308 [heuristic]: expected threshold-violating bonds per unit physical volume
# at level k ~ L^{4(K-k)} e^{-c ε_1²/g_k²}.  RLARGE l.943 fixes the constant: exponent ≥ ε_1²/(4N).
def expo(e,g2): return e*e/(4*N*g2)
o=[]
def P(s=""): o.append(s)
P("e1c_largefield_posthoc.py -- POST-HOC. No pre-registered verdict.")
P("Large-field region size: PROOF l.4307 density ~ L^{4(K-k)} e^{-ε_1²/(4N g_k²)} (rate RLARGE l.943).")
P("")
P("(1) at the ε-DRIVEN coupling ceiling g²_CRC(x82):")
for nm,e in (("E_t",EPS_T),("E_p",EPS_P)):
    g2=g2_crc(e); x=expo(e,g2)
    P("   %s  g_K² = %-13s  ε_1²/(4Ng²) = %-13s  levels K-k affordable = %s"
      % (nm,dec(g2,5),dec(x,6),(L10(x)).quantize(Decimal('0.01'))))
P("   -> the suppression exponent is EXACTLY invariant: %s"
  % (expo(EPS_T,g2_crc(EPS_T))==expo(EPS_P,g2_crc(EPS_P))))
P("")
P("(2) at the ε-INDEPENDENT binding ceiling g_DX² = 2.456e-152/C_Ω (C_Ω = 1):")
for nm,e in (("E_t",EPS_T),("E_p",EPS_P)):
    x=expo(e,G_DX2)
    P("   %s  ε_1²/(4Ng²) = %-14s  levels K-k affordable ≈ %s  (log10 %s)"
      % (nm,dec(x,6),(dec(x,20)/(4*L10(L))),L10(x).quantize(Decimal('0.01'))))
P("   -> falls by %s decades; the wrap requirement is ~205 levels, so the margin is"
  % (L10(expo(EPS_T,G_DX2)/expo(EPS_P,G_DX2))).quantize(Decimal('0.001')))
P("      %s decades of levels at E_p."
  % ((dec(expo(EPS_P,G_DX2),30)/(4*L10(L))/205).log10()).quantize(Decimal('0.01')))
P("")
P("(3) per-cube large-field weight e^{-ε_1²/(4Ng²)} at the DX' coupling:")
for nm,e in (("E_t",EPS_T),("E_p",EPS_P)):
    P("   %s  log10 of the weight = -%s" % (nm,dec(expo(e,G_DX2)*F(4343,10000),6)))
print("\n".join(o))
