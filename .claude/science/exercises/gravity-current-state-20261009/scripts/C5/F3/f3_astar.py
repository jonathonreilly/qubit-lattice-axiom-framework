"""F3 (c) arithmetic: Hess(a) = Hess_F1 + 2 a L_G (SF units t; H-cov units x4, same a since t^2 = 4 h^2 on soft modes),
zero at a* = -Hess_F1/(2 L_G); natural-size range; tuning precision demanded by F2's Earth row (F1: exceeded by 1.62e8,
f1_envscale.out:2); IR Pauli-term estimate (suggested): delta a_lepton ~ 4 a t^2 (m l_P)."""
HF1 = {'B1 (R18-9, 344 nodes)': 2.4240112e-02,     # f1_root_conv2.out:3
       'B2 (R18-9, 240 nodes)': 2.4261092e-02,     # f1_branches.out:4
       '0+ root B1 (240 nodes)': 2.4534992e-02}    # f1_branches.out:5
L = {'R18-9': {'G1': -8.585829728e-01, 'G2': -1.502128368e+00, 'G3': -7.119680532e-01, 'G4': -8.465599019e-01},   # f3_resp_main.out (344)
     '0+': {'G1': -8.581123348e-01, 'G2': -1.502419329e+00}}                                                     # f3_resp_root0.out (240)
for br, H in HF1.items():
    root = '0+' if br.startswith('0+') else 'R18-9'
    for g, Lg in L[root].items():
        a = -H/(2*Lg)
        print('%-24s %s: Hess_F1 %+.6e  L %+.6e  ->  a* = %+.6e   max dressing angle per unit t^2: 2 a* max|f| = %.4f'
              % (br, g, H, Lg, a, 2*abs(a)*{'G1': 3**0.5, 'G2': 2*3**0.5, 'G3': 3**0.5, 'G4': 3**0.5}[g]))
H = HF1['B1 (R18-9, 344 nodes)']; L1 = L['R18-9']['G1']; L2 = L['R18-9']['G2']
print('\nrange for |a| <= 1 (G1 alone): Hess in [%+.4f, %+.4f] ; (G1 and G2, |a_i| <= 1): [%+.4f, %+.4f] ; unbounded for unbounded a'
      % (H - 2*abs(L1), H + 2*abs(L1), H - 2*(abs(L1) + abs(L2)), H + 2*(abs(L1) + abs(L2))))
print('H-cov units (x4): Hess_h(a) = %+.5f %+.5f a  (G1)' % (4*H, 8*L1))
excess = 1.62e8
print('tuning precision to pass F2 row 1 (Earth crossing): |a/a* - 1| <= 1/%.2e = %.1e' % (excess, 1/excess))
a1 = -H/(2*L1)
for lab, t, ml in (('electron, t ~ 1e-9 (static potential scale)', 1e-9, 4.2e-23), ('electron, t ~ 1e-21 (GW strain)', 1e-21, 4.2e-23),
                   ('top quark, t ~ 1e-9', 1e-9, 1.4e-17)):
    print('IR Pauli estimate (suggested) %-44s: delta a ~ 4 a* t^2 (m l_P) = %.1e' % (lab, 4*a1*t*t*ml))
