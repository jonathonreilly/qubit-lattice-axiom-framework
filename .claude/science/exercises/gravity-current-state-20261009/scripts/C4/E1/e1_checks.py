"""E1 (lane RE) checks. Pure arithmetic / group theory; no external data.
(1) Which Lorentz reps (j1,j2) admit a background tensor invariant under the
    chiral cubic group O (axiom Lattice: proper rotations only) and time
    translations, and the 4D unitarity floor on their dimension -> list of
    LV channels that are NOT automatically irrelevant at a unitary LI CFT.
(2) Chadha-Nielsen running = DGLAP n=2 singlet mixing: check against
    Kostelecky-Lane-Pickering Q^-3 and Gross-Wilczek d_NS(2)=32/75.
(3) Suppression factors over M_Pl -> Lambda_s for literature exponents and the
    exponent needed for each bound.
(4) UV dominance of TT stiffness / induced graviton LV under emergent LI.
"""
from fractions import Fraction as F
import math, itertools

# ---------- (1) O-invariants in SO(3) spin l and unitarity floors ----------
def chi(l, th):
    if abs(math.sin(th/2)) < 1e-14:
        return 2*l+1
    return math.sin((l+0.5)*th)/math.sin(th/2)
# classes of O: E, 8 C3 (2pi/3), 3 C2 (pi, face axes), 6 C4 (pi/2), 6 C2' (pi, edge axes)
classes = [(1,0.0),(8,2*math.pi/3),(3,math.pi),(6,math.pi/2),(6,math.pi)]
def nA1(l):
    return round(sum(n*chi(l,th) for n,th in classes)/24)
print("(1) multiplicity of A1 (O-invariant) in SO(3) spin l:")
print("   ", {l:nA1(l) for l in range(0,13)})
def so3_content(j1,j2):
    return [l for l in range(int(abs(j1-j2)), int(j1+j2)+1)]
def unitarity_floor(j1,j2):
    # Mack/Minwalla 4D: j1*j2 != 0 -> Delta >= j1+j2+2 (equality iff conserved);
    # j1*j2 == 0, j>0 -> Delta >= j+1 ; scalar -> Delta >= 1
    if j1==0 and j2==0: return F(1)
    if j1==0 or j2==0: return F(j1+j2)+1
    return F(j1+j2)+2
rows=[]
halves=[F(k,2) for k in range(0,13)]
for j1,j2 in itertools.product(halves,halves):
    if j1<j2: continue
    if (j1+j2).denominator!=1: continue   # bosonic operators only
    if j1==0 and j2==0: continue          # Lorentz scalars: not LV
    m=sum(nA1(l) for l in so3_content(j1,j2))
    if m==0: continue
    fl=unitarity_floor(j1,j2)
    rows.append((float(j1),float(j2),m,float(fl),float(4-fl)))
rows.sort(key=lambda r:r[3])
print("    (j1,j2)  #O-inv  Delta_min  coupling-dim(4-Delta_min)  -> status")
for j1,j2,m,fl,cd in rows[:14]:
    st = "can be relevant/marginal" if cd>=0 else "always irrelevant, exponent >= %.0f"%(-cd)
    print("    (%.1f,%.1f)   %d      %.1f        %+.1f   %s"%(j1,j2,m,fl,cd,st))

# ---------- (2) LV running = twist-2 n=2 singlet mixing ----------
def lam_plus_QCD(nf):   # units alpha_s/(4pi); gamma_qq(2)+gamma_gg(2)
    return F(64,9)+F(4,3)*nf
def beta0_QCD(nf): return 11-F(2,3)*nf
print("\n(2) d_NS(2) nf=4 =", F(64,9)/(2*beta0_QCD(4)), "(Gross-Wilczek 32/75)")
for nf in (3,4,5,6):
    print("    nf=%d: asymptotic quark momentum fraction %s ; singlet exponent d+ = %.4f"
          %(nf, F(3*nf,16+3*nf), float(lam_plus_QCD(nf)/(2*beta0_QCD(nf)))))
# QED, one Dirac fermion of unit charge: C_F->1, T_F->1, C_A->0
lam_qed = 2*1*F(8,3) + F(4,3)*1*2      # 16/3 + 8/3
b0_qed  = -F(4,3)
print("    QED: lambda+ = %s, beta0 = %s, exponent lambda+/(2 beta0) = %s  (KLP: Q^-3 => 3 in |.|)"
      %(lam_qed,b0_qed,lam_qed/(2*b0_qed)))
MPl=1.22e19; mZ=91.19
# QCD n_f=6 running from 1 TeV to M_Pl at one loop
a_TeV=0.0884
inv=1/a_TeV + (float(beta0_QCD(6))/(2*math.pi))*math.log(MPl/1e3)
a_Pl=1/inv
dplus=float(lam_plus_QCD(6)/(2*beta0_QCD(6)))
print("    QCD nf=6: alpha_s(M_Pl)=%.4f alpha_s(1TeV)=%.4f ; quark-gluon LV suppression M_Pl->TeV = %.3f"
      %(a_Pl,a_TeV,(a_Pl/a_TeV)**dplus))
# QED electron only from M_Pl to m_e
inv_e=137.036-(2/(3*math.pi))*math.log(MPl/0.000511)
print("    QED(e only): 1/alpha(M_Pl)=%.1f ; e-gamma LV suppression M_Pl->m_e = %.3f"
      %(inv_e,(inv_e/137.036)**-3*1.0 if False else (137.036/inv_e)**-3))

# ---------- (3) power-law suppression ----------
bounds = {"e/gamma photon decay (lattice sign)":2.7e-19,
          "nu (IceCube PeV)":1e-20,
          "p/gamma GZK Cherenkov (if c_p>c_g)":4e-23,
          "graviton/gamma GW170817":1e-15}
print("\n(3) exponent gamma needed: delta0*(Ls/MPl)^gamma < bound")
for delta0 in (1.0,0.1):
  for Ls in (1e3,1e4,1e5):
    r=Ls/MPl
    need={k:math.log(b/delta0)/math.log(r) for k,b in bounds.items()}
    print("    delta0=%.1f Lambda_s=%.0e GeV (ratio %.1e, %.1f decades):"%(delta0,Ls,r,-math.log10(r)),
          ", ".join("%s: %.2f"%(k.split()[0],v) for k,v in need.items()))
print("    suppression at Lambda_s=1e4 GeV for literature exponents:")
lit={"QED CN (0.78 total)":None,"BPS13 Lifshitz max 2alpha~0.7":0.7,
     "BPW24 kappa=1":1.0,"BPW24 kappa=2":2.0,"QED3 large-N 32/(5pi^2 N), N=4":32/(5*math.pi**2*4),
     "QCD-like one-loop 0.72*alpha*, alpha*=1":float(lam_plus_QCD(6))/(4*math.pi)}
for k,g in lit.items():
    if g is None: continue
    print("      %-40s gamma=%.3f  suppression=%.1e"%(k,g,(1e4/MPl)**g))

# ---------- (4) UV dominance ----------
print("\n(4) vacuum shear stiffness ~ int_0^L E^3 eta(E) dE, eta=(E/L)^g (emergent LI from the cutoff down):")
for g in (0,0.7,1,2,5):
    print("    gamma=%.1f: stiffness / (no-emergence value) = %.3f ; induced graviton-kinetic LV ~ int E eta: %.3f"
          %(g,4/(4+g),2/(2+g)))
print("    P0 requires 9.0e-102 (framework conv.) / 5.7e-99 (refereed) of natural size; GW170817 1e-15")

# ---------- (5) energy-dependent LV above the exit scale ----------
# Above Lambda_s the strong sector is probed directly: delta(E) ~ delta0*(E/MPl)^gamma.
print("\n(5) exponent needed when the bound is set at energy E above Lambda_s (delta0=1):")
hi={"photon decay, 1.4 PeV photon (lattice sign c_g>c_e)":(1.4e6,2.7e-19),
    "p vacuum Cherenkov, 1e20 eV (only if c_p>c_g)":(1e11,4.4e-23),
    "p/gamma lattice-like sign, 1e20 eV":(1e11,9e-13)}
for k,(E,b) in hi.items():
    print("    %-55s gamma >= %.2f"%(k, math.log(b)/math.log(E/MPl)))
# ---------- (6) TT-stiffness scale from the graviton-mass bound ----------
mg=1.3e-23; Mbar=2.435e27   # eV
mu=(mg*Mbar)**2
print("\n(6) TT stiffness bound mu < (m_g Mbar_Pl)^2 = %.2e eV^4 = (%.0f eV)^4 ; CC scale ~ (2.3e-3 eV)^4"%(mu,mu**0.25))
print("    broken SUSY at 1 TeV: mu ~ m^4/16pi^2 exceeds the bound by %.1e"%((1e12)**4/(16*math.pi**2)/mu))
print("    SM-coupling cap on CN-type drag: gamma_QCD <= lambda+ alpha_s(TeV)/4pi = %.3f -> 15 decades give %.3f"
      %(float(lam_plus_QCD(6))*0.09/(4*math.pi),(8.2e-16)**(float(lam_plus_QCD(6))*0.09/(4*math.pi))))
print("    SU(3) nf=12 Banks-Zaks 2-loop alpha*=%.3f -> one-loop gamma+ = %.2f (illustrative; alpha* not small)"
      %(4*math.pi*3/50, float(lam_plus_QCD(12))*(4*math.pi*3/50)/(4*math.pi)))
