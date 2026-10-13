"""R19-15 probe (b): cubic decomposition of the static TT response.
Traceless symmetric strain = E_g (2 comps) + T_2g (3 comps) under O_h; under O(3) it is one l=2 irrep.
Any O(3)-covariant clause (built from g, u, h_munu = g+uu, scalars e0, W; weight-1 densities) gives
equal E_g and T_2g coefficients, so it acts only on the singlet S = (2 mu_E + 3 mu_T2)/5 and never on the
cubic anisotropy A = mu_E - mu_T2. Numbers: inputs quoted from archived outputs (sources in comments)."""
rows = {
 'NN scalar m=1 (V3 comparator; PRICE_NOTE:290-293)': (1.97038864e-3, 0.0),
 'Dirac c1 per field at the 0+ root (R19-11 table; vR19-11 c1(muT2) confirmed)': (1.06932e-2, 2.73929e-3),
 'SM residual totals of the 0+ law (R19-11 table; vR19-11 item 4)': (4.70e-19, 1.20397e-19),
 'twisted-mass SM residual (R19-11 P-R19-11c; vR19-11 item 5)': (4.38e-36, -2.3e-39),
 'scalar c0 per field at 0+ root, mu_E only (R19-11 table)': (1.112970e-2, 0.0),
}
bound = 3.20e-98   # vR19-11 item 4 (100 Hz, conditional on the graviton bridge)
for k, (mE, mT) in rows.items():
    S = (2*mE + 3*mT)/5; A = mE - mT
    print('%-75s mu_E %+.4e mu_T2 %+.4e | singlet S %+.4e | anisotropy A %+.4e | |A|/bound %.1e' % (k, mE, mT, S, A, abs(A)/bound))
print('An isotropic clause shifts (mu_E, mu_T2) by (c, c): A is invariant; zeroing both needs A = 0 first.')
