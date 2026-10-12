"""O1 check 3: bound arithmetic (exact kinematics where cheap), and implied tuning factors."""
from mpmath import mp, mpf, sqrt, findroot, log10, pi
mp.dps = 40
me = mpf('0.51099895e6'); mp_ = mpf('938.272e6'); Eg = mpf('1.4e15')   # eV
# photon decay gamma -> e+ e-, dispersion E^2 = c^2 p^2 + m^2 (c_gamma = 1 + d, c_e = 1)
# threshold: (c_g p)^2 = 4 m^2 + p^2  (collinear, equal split)  => d_th(E) exact:
def dth(E, m):
    # c_g p = E, p = E/c_g ; E^2 = 4 m^2 + E^2/c_g^2 -> c_g = E/sqrt(E^2-4m^2)
    cg = E / sqrt(E**2 - 4*m**2); return cg - 1
print("photon decay e+e- at 1.4 PeV: exact d_th =", mp.nstr(dth(Eg, me), 6), " approx 2m^2/E^2 =", mp.nstr(2*me**2/Eg**2, 6))
print("photon decay p pbar at 1.4 PeV:           ", mp.nstr(dth(Eg, mp_), 6))
# F2 natural one-loop split (refereed): c_e - c_gamma = -8.55e-3 (photon faster): tuning factor
nat = mpf('8.55e-3'); b = dth(Eg, me)
print("tuning factor needed (bound/natural):", mp.nstr(b/nat, 4), "  miss without tuning:", mp.nstr(nat/b, 4))
alpha = mpf(1)/137.036
print("alpha/(4 pi) =", mp.nstr(alpha/(4*pi), 5), "; xi=2 lattice value -10.26*alpha/(4pi) =", mp.nstr(10.26*alpha/(4*pi), 4))
# UHECR (Klinkhamer-Schreck 2008, 98% CL): -9e-16 < kappa_tr < 6e-20 ; tuning vs natural ~6e-3..9e-3
for nm in ('6e-3', '8.55e-3'):
    print(f"  UHECR one-sided 6e-20 / natural {nm} =", mp.nstr(mpf('6e-20')/mpf(nm), 3))
# GW170817: -3e-15 <= dc/c <= 7e-16; natural graviton-matter split ~1e-2 (E2 estimate, reading)
print("GW170817 tuning vs ~1e-2 natural:", mp.nstr(mpf('7e-16')/mpf('1e-2'), 3), "to", mp.nstr(mpf('3e-15')/mpf('1e-2'), 3))
# Hughes-Drever: neutron spatial c_jk ~1e-29 (Smiciklas+2011). In a preferred frame with isotropic c_00 there,
# a lab moving at beta sees anisotropic c'_jk ~ c_00 * beta^2 (traceless part of beta_j beta_k). CMB frame beta:
beta = mpf('1.23e-3')
print("CMB dipole beta^2 =", mp.nstr(beta**2, 3), "=> c_00(neutron) <~ 1e-29/beta^2 =", mp.nstr(mpf('1e-29')/beta**2, 3), "(order of magnitude; projection factors not computed)")
# dimension 5: LHAASO GRB 221009A E_QG,1 > 10 E_Pl => coefficient xi = E_Pl/E_QG < 0.1
print("dimension-5 (linear) coefficient bound (E_QG,1 > 10 E_Pl): < 0.1 of Planck-natural")
# dimension 6 with a = l_P: LHAASO quadratic E_QG,2 > 6e-8 E_Pl  (B1 report) -- a natural O(1) a^2 p^4 term passes
print("dimension-6 a^2 p^4 at a = l_P: needs E_QG,2 > 6e-8 E_Pl; natural is ~E_Pl/sqrt(12) -> passes by",
      mp.nstr(log10((1/sqrt(12))/mpf('6e-8')), 3), "decades in scale")
# QED log running (E2, refereed): 8.55e-3 -> 7.34e-3 at 1.4 PeV; required power-law exponent over 12.94 decades
dec = log10(mpf('1.22e28')/Eg)
z = log10(mpf('7.34e-3')/b)/dec  # rough: exponent needed if the split fell as (E/M_Pl)^z from 7.3e-3
print("decades M_Pl -> 1.4 PeV:", mp.nstr(dec, 4), "; power z needed ~", mp.nstr(log10(nat/b)/dec, 4), "(E2 refereed: 1.27564)")
