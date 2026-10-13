"""R19-10 numbers: sizes against rho_Lambda at a = l_P (Planck units, G = c = hbar = 1, a = l_P).
Reads r1910_adiabatic.out (ramped insertion), uses r1910_insert_product.out and r1910_dislocation.out values.
  - standing in-progress density: rho_ins = (3H/a^3) * A, A = time-integrated excess per inserted site (hbar units);
    rho_ins / rho_Lambda = 8 pi A / (Omega_L H0)   [flat FRW, rho_Lambda = Omega_L 3H0^2/(8 pi)]
  - net per-Hubble-time injection: 3 eps_inf / rho_Lambda
  - Lemma S-ins bound: A >= dE_bp^2 / (2 Gamma), Gamma = sup ||[K(t), H_B]||
  - dislocation climb (R12-2 geometry): line density 3H/(a v); rho_def = 3 H delta_line / v
"""
import numpy as np, re, os
here = os.path.dirname(os.path.abspath(__file__))
H0 = 67.4/3.0857e19*5.391e-44; OmL = 0.685; rhoL = OmL*3*H0**2/(8*np.pi)
R = 8*np.pi/(OmL*H0)
print('H0 = %.4e t_P^-1 ; rho_Lambda = %.4e ; standing factor 8 pi/(Omega_L H0) = %.3e per unit A' % (H0, rhoL, R))

# ---- parse ramp runs -------------------------------------------------------------------------------------
data = {}; m = None
for line in open(os.path.join(here, 'r1910_adiabatic.out')):
    mm = re.match(r'=== m = ([0-9.]+):', line)
    if mm: m = float(mm.group(1)); data[m] = []; continue
    mt = re.match(r'\s+T=\s*(\d+) N=\s*\d+: eps_inf = ([0-9.e+-]+) ; A_fix = ([0-9.e+-]+) ; A_law = ([0-9.e+-]+)', line)
    if mt and m is not None:
        data[m].append(tuple(float(x) for x in mt.groups()))
for m, rows in data.items():
    a = np.array(rows)
    print('=== m = %.1f (ramped plane insertion, per inserted site) ===' % m)
    for T, e, Af, Al in a:
        print('  T=%3d: net 3 eps_inf = %.2e rho_L per Hubble time ; standing (A_law) = %.2e rho_L ; (A_fix) = %.2e rho_L'
              % (T, 3*e/rhoL, R*Al, R*Af))
    tot_c = R*a[:, 3] + 3*a[:, 1]/rhoL
    print('  [checked, computed T only] min over T in {%s} of (standing A_law + net per Hubble time) = %.1e rho_L (T = %d);'
          % (','.join('%d' % t for t in a[:, 0]), tot_c.min(), a[np.argmin(tot_c), 0]))
    print('     A_law grows ~linearly beyond the range; for T -> 0 net -> P-loc dE (larger), so this is the floor of the family')
    big = a[a[:, 0] >= 8]
    if len(big) >= 2:
        p, lc = np.polyfit(np.log(big[:, 0]), np.log(big[:, 1]), 1)
        sl = np.polyfit(big[:, 0], big[:, 3], 1)[0]
        print('  fit (T >= 8): eps_inf ~ %.3g T^%.2f ; A_law slope dA/dT = %.4f (mean in-progress excess delta-bar)'
              % (np.exp(lc), p, sl))
        if p < 0:
            # T needed for net per-Hubble-time injection below rho_Lambda (EXTRAPOLATION: suggested)
            Tneed = (3*np.exp(lc)/rhoL)**(1/(-p))
            print('  [suggested; POWER-LAW extrapolation, valid only if the fit form holds; for gapped m it is superpolynomial] extrapolated over ~%d decades] net < rho_L needs T > %.1e t_P (Hubble time %.1e t_P);'
                  % (int(np.log10(Tneed/64)), Tneed, 1/H0))
            print('     standing at that T: %.1e rho_L' % (R*sl*Tneed))
            # minimise standing + net over T
            Ts = np.logspace(0, 70, 7001)
            tot = R*sl*Ts + 3*np.exp(lc)*Ts**p/rhoL
            i = np.argmin(tot)
            print('     min over T of (standing + net per Hubble time) = %.1e rho_L at T = %.1e t_P' % (tot[i], Ts[i]))

# ---- Lemma S-ins ------------------------------------------------------------------------------------------
print('=== Lemma S-ins: A >= dE_bp^2/(2 Gamma) -> standing >= 8 pi dE_bp^2/(2 Gamma Omega_L H0) rho_L ===')
for name, dE in [('3D scalar plane, m=0 (P-loc)', 0.059431), ('3D scalar plane, m=1', 0.040510),
                 ('3D Wilson-Dirac plane, m=0', 0.975567), ('1D scalar point, m=0.05', 0.559603)]:
    for G in (1.0, 10.0):
        print('  %-30s Gamma=%4.0f: A >= %.2e -> standing >= %.1e rho_L' % (name, G, dE**2/(2*G), R*dE**2/(2*G)))
    print('  %-30s Gamma needed for standing < rho_L: > %.1e (Planck units E_P/t_P)' % (name, R*dE**2/2))

# ---- dislocation climb ------------------------------------------------------------------------------------
print('=== dislocation climb (R12-2: line density 3H/(a v_climb)); delta_line from r1910_dislocation.out ===')
for m, dl in [(1.0, -0.09904), (0.3, -0.10845), (0.0, -0.10987)]:
    for v in (1.0, 1e-3):
        print('  m=%.1f v=%.0e c: rho_def = 3 H delta_line / v = %.1e rho_L (sign of delta_line: %s)'
              % (m, v, R*dl/v, 'negative' if dl < 0 else 'positive'))
print('  equivalent in-progress action per inserted site: A = delta_line * (a / v)')

# ---- effective equation of state of an H-tracking term (if treated as a separately conserved fluid) ----------
print('=== rho_ins proportional to H: 1 + w_ins = -Hdot/(3H^2) = (1 + w_tot)/2 ===')
for lab, wt in [('radiation era', 1/3), ('matter era', 0.0), ('de Sitter', -1.0)]:
    print('  %-14s w_tot = %+.3f -> w_ins = %+.3f' % (lab, wt, (1 + wt)/2 - 1))
