"""T63 test D: arithmetic of the note (docs/PRIMORDIAL_SPECTRUM_NOTE.md) and its amplitude/tensor consistency."""
import math
NS, SIG = 0.9649, 0.0042
def ns_formula(d, Ne): return 1 - 2/Ne + (d-3)/(d*Ne)
def ns_poisson(d, Ne): return 1 - d/Ne
def ns_intake(d, Ne): return 1 - 2/Ne - (d-3)/(d*Ne**2)
print("D1 tilt arithmetic")
for label, Ne in (("N_e=60 (chosen)", 60.0), ("N_e for central n_s: 2/(1-n_s)", 2/(1-NS)), ("N_e=(1/3)ln(1e183)", math.log(1e183)/3), ("N_e=(1/3)ln(1e78)", math.log(1e78)/3)):
    v = ns_formula(3, Ne)
    print("   %-34s N_e=%7.2f  n_s(d=3)=%.4f  (%+.1f sigma)   Poisson-only 1-3/N_e=%.4f (%+.1f sigma)" % (label, Ne, v, (v-NS)/SIG, ns_poisson(3, Ne), (ns_poisson(3, Ne)-NS)/SIG))
lo, hi = 2/(1-(NS-SIG)), 2/(1-(NS+SIG))
print("   1-sigma window on N_e: %.1f - %.1f  => N_obs = e^(3 N_e): 10^%.1f - 10^%.1f" % (lo, hi, 3*lo/math.log(10), 3*hi/math.log(10)))
print("   e^180 = 10^%.2f; 10^183/e^180 = 10^%.1f" % (180/math.log(10), 183-180/math.log(10)))
print("\nD3 d-dependent term and the added term")
for d in (2, 3, 4):
    Ne = 60.0
    print("   d=%d  note (*) %.5f   Poisson-only %.5f   intake(1/N_e^2) %.5f   (*) minus Poisson-only = %+.5f = (%.3f)/N_e" % (d, ns_formula(d, Ne), ns_poisson(d, Ne), ns_intake(d, Ne), ns_formula(d, Ne)-ns_poisson(d, Ne), (ns_formula(d, Ne)-ns_poisson(d, Ne))*Ne))
print("   at d=3 the term added to the Poisson-only result is +1/N_e = %+.4f = %.1f sigma of Planck; only the term relative to slow-roll (d-3)/(d N_e) vanishes" % (1/60, (1/60)/SIG))
print("   profile needed: Delta^2 ~ H^d, n_s-1 = -d dlnH/dN_rem  => target -2/N_rem requires H ~ N_rem^(2/d) (input, not derived)")
print("\nD2 amplitude and tensor consistency, a^-1 = M_Pl = 1.221e19 GeV, reduced Planck mass M_p = M_Pl/sqrt(8 pi)")
AS = 2.1e-9
Ha = AS**(1/3)
fac = math.sqrt(8*math.pi)          # H/M_p = (H a) * M_Pl/M_p
Hp = Ha*fac
Pt = 2*Hp**2/math.pi**2
print("   Poisson-cell scalar amplitude A_s=(H a)^3=2.1e-9 needs H a=%.2e (H=%.1e GeV); GR tensors at that H give P_t=%.1e, r=%.1e (bound r<0.036)" % (Ha, Ha*1.221e19, Pt, Pt/AS))
Hp_r = math.pi*math.sqrt(0.0025*AS/2); Ha_r = Hp_r/fac
print("   the note's r=0.0025 with A_s=2.1e-9 needs H a=%.2e; the Poisson amplitude there is (H a)^3=%.1e, short of 2.1e-9 by 10^%.1f" % (Ha_r, Ha_r**3, math.log10(AS/Ha_r**3)))
Hp_b = math.pi*math.sqrt(0.036*AS/2); Ha_b = Hp_b/fac
print("   largest H allowed by r<0.036: H a=%.2e (H=%.1e GeV); Poisson amplitude there %.1e, short by 10^%.1f" % (Ha_b, Ha_b*1.221e19, Ha_b**3, math.log10(AS/Ha_b**3)))
print("   cell size l (in Planck lengths) that would fit A_s=2.1e-9 with H at the r bound: l = %.0f l_P" % (Ha/Ha_b))

print("\nD4 amplitude of a STATIC lattice pattern at horizon scale today (route R2 and any fixed-pattern route)")
t_age_s = 13.8e9*3.156e7; t_P = 5.391e-44
T = t_age_s/t_P
R_sites = 46.5e9*9.461e15/1.616e-35   # particle horizon in Planck lengths
print("   age = %.2e ticks; particle-horizon radius = %.2e sites" % (T, R_sites))
for alpha, c in ((0.0, 0.03), (1.0, 0.03)):
    k = 1.0/R_sites
    rho = 0.2
    Delta2 = k**3 * c * k**alpha/(2*math.pi**2*rho**2)
    print("   S(k) = %.2f k^%.0f: Delta_delta^2 at k = 1/R = %.1e   (needed ~ A_s = 2.1e-9: short by 10^%.0f)" % (c, alpha, Delta2, math.log10(2.1e-9/Delta2)))
print("   coefficient a static alpha=1 tail would need: c = A_s * 2 pi^2 rho^2 / k^4 = %.1e (lattice-rule value ~ 0.03)" % (2.1e-9*2*math.pi**2*0.04*R_sites**4))
