"""R19-31 (d): sizes through SM history against R19-21's bound line (canonical reading, conditional: m_g^2 a^2 = 16 pi mu, mu in R19-21's
SF-flow normalisation; bound 'no tensor mass/instability faster than H': 16 pi |mu| < (H a)^2, (H a)^2 = (8 pi/3)(pi^2/30) g* (T a)^4).
Normalisation: H-cov E_g strain l = (e^h, e^-h, 1) acts on soft modes as k_x -> e^-h k_x; R19-21's SF flow as k_x -> e^{t/2} k_x, so t = -2h and
mu_SF = mu_Hcov / 4 (exact for the soft/thermal factor; the UV coefficients are law data of the stated H-cov law).
Inputs (checked here, per e^2, H-cov): scalar-channel (S_loc) residue K = -0.0860 T^4 per complex scalar (r1931_mcheck.out);
photon channel -8.88e-4 T^4 per photon per complex charged scalar in the loop (r1931_sqed_cross.out (4));
Wilson additive mass d2(dm)/dh2 = -0.0621 per e^2 (r1931_wilson_mass.out); CW gap -0.082 e^2 m^2 per unit Phi (r1931_mcheck.out).
SM mapping = ESTIMATE (labelled): couplings at the lattice scale (RECALLED, ~M_P): e_eff^2 per Higgs complex component (3/4) g^2 + (1/4) g'^2 with
g^2 ~ 0.25, g'^2 ~ 0.2; quark QCD C_F g_s^2 with g_s^2 ~ 0.3; fermion speed-row Hessians NOT computed: bracketed by the scalar coefficient per dof."""
import numpy as np
MP = 1.22089e19
def Ha2(T, gs=106.75): return (8*np.pi/3)*(np.pi**2/30)*gs*(T/MP)**4
def ratio(mu_SF_over_Ta4, gs=106.75): return 16*np.pi*mu_SF_over_Ta4/((8*np.pi/3)*(np.pi**2/30)*gs)
g2, gp2, gs2 = 0.25, 0.2, 0.3
e2H = 0.75*g2 + 0.25*gp2
print('(B) (S_loc)-CW residue O(g^2 T^4): T-independent ratio m_g^2/H^2 in the radiation era (g* = 106.75)')
higgs = 2*e2H*(-0.0860)/4
print('  Higgs doublet scalar channel (2 complex x e_eff^2 = %.3f): mu_SF/(Ta)^4 = %+.4e  -> m_g^2/H^2 = %+.2e' % (e2H, higgs, ratio(higgs)))
ph = 12*25*(-8.88e-4)/4*g2      # 12 gauge bosons x ~25 complex-charged-dof-equivalents, coefficient per e^2 from the scalar loop (estimate)
print('  gauge-boson channel (12 bosons x ~25 charged complex dof, scalar-loop coefficient): mu_SF/(Ta)^4 ~ %+.2e -> %+.2e' % (ph, ratio(ph)))
for lab, c in (('fermions, speed rows bracketed as scalar coefficient x 45 Weyl/2 x C_F g_s^2-weighted', 22.5*(4/3)*gs2*(-0.0860)/4),
               ('Wilson massless soft fermions, <psibar psi>_th x dm\'\' (symmetric phase), 22.5 Dirac x C_F g_s^2', 22.5*(4/3)*gs2*(-0.0355)/4)):
    print('  %s: mu_SF/(Ta)^4 ~ %+.2e -> m_g^2/H^2 ~ %+.2e' % (lab, c, ratio(c)))
tot = higgs + ph + 22.5*(4/3)*gs2*(-0.0860)/4
print('  rough total (without the Wilson psibar psi term): m_g^2/H^2 ~ %+.2e (|m_g|/H ~ %.2f); with it ~ %+.2e' % (ratio(tot), np.sqrt(abs(ratio(tot))), ratio(tot + 22.5*(4/3)*gs2*(-0.0355)/4)))
print('  compare R19-21 quasiparticle (T a)^6 term: m_g^2/H^2 = 2.5e-6 at 1e16 GeV, falling as (Ta)^2 (4e-36 at T_c)')
for eps in (abs(ratio(tot)), 0.05):
    print('  superhorizon tensor amplitude factor over 55 e-folds of radiation era with |m_g^2/H^2| = %.3g: exp(+-%.3f*55) = %.3g / %.3g' % (eps, eps, np.exp(eps*55), np.exp(-eps*55)))
print('\n(A) CW-gap after (S_loc) (on-shell vs background-field, O(e^2 m^2) per unit Phi; m^2 -> m_th^2 ~ 0.4 T^2, Phi = T^2/12 per complex):')
gap = 2*e2H*(-0.082)*0.4/12/4
print('  mu_SF/(Ta)^4 ~ %+.2e -> m_g^2/H^2 ~ %+.2e  (an O(g^2 lambda_th) = O(g^4) residue, as the FIXED clause allows)' % (gap, ratio(gap)))
print('\n(C) Wilson-type edges, broken phase: <psibar psi>_th x d2(dm)/dh2 (NOT removed by (S_loc) unless psibar psi is a background):')
quarks = {'t': 172.69, 'b': 4.18, 'c': 1.27}
for T in (150.0, 100.0, 50.0, 10.0, 1.0):
    mu = 0.0
    for q, m in quarks.items():
        # <psibar psi>_th per Dirac colour: 4 <nF m/E>, continuum integral (GeV^3), then x a^3
        k = np.linspace(1e-4, 60*T + 10*m, 200001); E = np.sqrt(k*k + m*m)
        pp = 4*np.trapezoid(k*k/(2*np.pi**2)*m/E/(np.exp(np.minimum(E/T, 700)) + 1), k)
        mu += 3*pp/MP**3*(4/3)*gs2*(-0.0621)/4
    gs_ = 106.75 if T > 90 else 86.25
    print('  T = %6.1f GeV: mu_SF = %+.3e  m_g^2/H^2 = %+.3e (tachyonic)' % (T, mu, 16*np.pi*mu/Ha2(T, gs_)))
print('  today (canonical, path-averaged; electrons e^2 = 0.1 at the lattice scale; nucleons: sigma-term weight ~13 light-quark units x C_F g_s^2):')
lP = 1.616e-35; EP_eV = MP*1e9
for lab, n in (('IGM n ~ 0.25 /m^3', 0.25), ('Earth n ~ 3.3e30 /m^3', 3.3e30)):
    na3 = n*lP**3
    for who, w in (('electrons', 0.1), ('nucleons', 13*(4/3)*gs2)):
        mg2a2 = 16*np.pi*na3*w*0.0621/4
        print('   %-22s %-9s m_g = %.2e eV (tachyonic; LVK 1.92e-23 eV; 100 Hz GW energy 4.1e-13 eV)' % (lab, who, np.sqrt(mg2a2)*EP_eV))
