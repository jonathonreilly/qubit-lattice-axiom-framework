# T56 pre-registration (written before t56_test.py was run)

Author: Claude Sonnet 5.5 (same vendor family as supervisor). Wall T56 = L12-W4.
Note on order: `quick_probe.py` (exploratory, run BEFORE this file) showed that the lane's own
converged Sommerfeld kernel (`scripts/dm_full_closure_same_surface_thermal_support_common.py:60-80`,
weight v^2 exp(-(x/4) v^2), S = pi z/(1-exp(-pi z)), z = alpha/v) gives R(0.0907)=5.443, R(0.048)=4.416,
and that replacing pi -> 2 pi in S gives R(0.048)=5.579, R(0.0907)=7.97. The factor-2 hypothesis below
was formed from that; T2/T3 test it. T4/T5 were designed before any run.

## Question
Is there a channel and coupling for the dark annihilation that is fixed by something other than the
choice alpha_X = alpha_LM (kappa = 1, self-conjugate counting, no dark Sommerfeld factor), such that
m_DM = 16 v = 3940.53 GeV gives Omega_DM h^2 = 0.120 (+-10%)? And are the wall's "two pins"
(alpha_GUT ~ 0.048 vs alpha_LM ~ 0.0907) two physical choices or one?

## T1 reproduction gate
My kernel reproduces the lane's R(alpha_lo)=5.442020 and R(alpha_hi)=5.482856 to 3e-4 relative.
PASS: yes. FAIL: stop, report kernel mismatch, drop T3.

## T2 Sommerfeld argument (factor-2 hypothesis H2)
Solve the s-wave radial Schrodinger equation numerically, reduced mass mu = m/2, V = -alpha/r
(and repulsive), k = mu v_rel, for eta = alpha/v_rel in {0.05, 0.1, 0.25, 0.5, 1.0, -0.1, -0.25}.
Compare S_num with S_2pi = 2 pi eta/(1-exp(-2 pi eta)) and S_pi = pi eta/(1-exp(-pi eta)).
PASS (H2): S_num within 1% of S_2pi at all points and off S_pi by >5% for |eta| >= 0.25.
FAIL: the lane's pi form is right for v = v_rel and H2 is dead.

## T3 what the corrected kernel says (only if T1 and T2 pass)
R_true(alpha) := 31/9 * (8 S1 + S8)/9 with argument 2 pi alpha_eff/v_rel. Exactly R_true(alpha) = R_lane(2 alpha).
Prediction P3a: the April band alpha_GUT in [0.03, 0.05] gives S = R/(31/9) in [1.36, 1.65] with the
corrected kernel, matching the notes' "[1.4, 1.7]" within 0.05 at both ends, while the lane's June
kernel gives [1.17, 1.30] (fails by > 0.15 at the low end).
Prediction P3b: the alpha that gives R = 5.364 (Planck-2018 central) is 0.0445 +- 0.002 (corrected) vs 0.0898 +- 0.004 (lane).
Prediction P3c: R_true(alpha_LM) = 7.9 +- 0.2, i.e. > +45% above 5.364.
PASS reading: the "two pins" are one pin (R_obs) under a factor 2 in the Sommerfeld argument.
FAIL reading: if the corrected kernel misses the April band by > 0.1, the factor-2 story does not
explain the April numbers and the two pins remain two independent choices.

## T4 independent freeze-out solve (dark sector, m = 16 v, g* = 106.75, M_Pl = 1.2209e19)
Solve dY/dx = -(lambda(x)/x^2)(Y^2 - Yeq^2) numerically (no x_F choice), sigma v = kappa pi alpha^2/m^2,
Omega h^2 = 2.742e8 (m/GeV) Y_inf (x2 if Dirac, i.e. species + antispecies).
P4a: (kappa=1, alpha_LM, self-conjugate counting, S=1) gives Omega h^2 = 0.1275 +- 15% (lane analytic value).
P4b (degeneracy): for S=1, Omega h^2 depends on (m, alpha) through m/alpha only:
spread of Omega over m in {8,16,32} v at fixed m/alpha is < 5%.
PASS P4b: T55 and T56 are one relation (only m/alpha_X is tested). FAIL: spread >= 5%.

## T5 fixed-channel table at m = 16 v (no free coupling; SM 1-loop running from M_Z)
Inputs: alpha_s(M_Z)=0.1180, alpha_2(M_Z)=0.0338, alpha_Y(M_Z)=0.01017; run with b3=-7, b2=-19/6, bY=+41/6
from M_Z to mu = m (band mu in [m/2, 2m]); framework's alpha_s(v)=0.1033 run the same way as a cross-check.
Channels:
 C1 colour-triplet Dirac (W2 base x fiber embedding, C_F=4/3) annihilating through SU(3) to gg + 6 flavours,
    colour-resolved Sommerfeld (singlet -C_F alpha_s attractive weight 2/27 of gg; octet +alpha_s/6 repulsive),
    sigma v = (pi alpha_s^2/m^2)[7/27 + 2 n_f/9], Dirac counting (Omega x2 vs self-conjugate).
 C2 = C1 + SU(2) doublet EW piece (own LO estimate, no EWSB effects).
 C3 lane's formula read as an unbroken dark U(1): Dirac psi psibar -> gamma_D gamma_D, sigma v = pi alpha^2/m^2,
    alpha_D = alpha_LM, with S=1 and with the (corrected) Coulomb S(alpha_LM).
 C4 gauge singlet / hypercharge-only (Y=1/3): sigma v from U(1)_Y only.
Predictions: C1 Omega/0.120 in [1.4, 2.0]; C2 a further 10-15% lower; C3 (S=1, Dirac) = 0.255 and with S 0.13-0.17;
C4 Omega/0.120 > 100. Required thermal mass for C1 in [2.6, 3.4] TeV (10.5-13.8 v).
PASS (wall stands as "the match is the choice"): no fixed channel C1-C3 lands within 10% of 0.120 at 16 v
without picking alpha_X by hand.
FAIL: some fixed channel with no free coupling lands within 10%: then the 16 v coincidence has a standard-physics
explanation and the wall reduces to the charge assignment (T54) plus the gauge couplings (T28-T30, T33).
Range statement R6: the spread of Omega(16 v) across the ambiguity set
{Dirac, self-conjugate} x {dark Sommerfeld in, out} x {C1, C2, C3} has max/min > 2, larger than the lane's
claimed +-6% agreement.

## Addendum (before the run of t56_test.py)
The SU(2) piece of C2: the W/Z/H channels need a colour-singlet QQbar, so a colour-averaged cross-section is
diluted by 1/N_c = 1/3 relative to a colourless doublet. So I now expect C2 to be only ~+3-5% over C1
(not 10-15% as written above). All other predictions unchanged.

## T6 (added after seeing T1-T5 output, so it is exploratory not pre-registered)
Single-coupling closure of the lane's own chain eta = C m^2, C = K x_F/(sqrt(g*) M_Pl pi alpha_X^2 R 3.65e7),
using one alpha both in alpha_X and in the Sommerfeld R(alpha). Reading: if no single alpha gives eta within 10% of
6.12e-10 under the corrected kernel, the chain never closed with one coupling.
