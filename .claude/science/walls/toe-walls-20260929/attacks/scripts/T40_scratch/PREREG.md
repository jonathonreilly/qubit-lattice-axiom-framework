# T40 pre-registration (written before any test script was run)

Wall: the absolute charged-lepton scale a^2 = ((sqrt m_e + sqrt m_mu + sqrt m_tau)/3)^2 (or y_tau) is a free number.
Two numerical matches are on the table (lane entry L08-W4):
 F1: a^2 = m_W/256 (= g2 v /512).            note offset +0.032%
 F2: m_tau = v * alpha_bare * alpha_LM  (Wilson chain, exponent 18=16+2), note offset 0.017%
     with alpha_bare = 1/(4 pi), alpha_LM = alpha_bare/u0, u0 = <P>^(1/4), <P> = 0.5934 (quenched plaquette).

Best route to test: "one of F1/F2 is a usable derivation target" (route R1, in-lane), against the
alternative "both matches are the same kind of forking-paths coincidence and the scale is homogeneous free data".

## Test 1: does either match survive framework-only inputs and the tastes-in-measure plaquette shift (sibling T31)?
 Inputs (framework-only): v_fw = 246.2828 GeV (quenched chain), g2 at v from lattice g2(M_Pl)=1/2 (Ward no-go note,
 g2^2 = 1/(d+1)) run down by one-loop SM b2 = -19/6, alpha_bare, alpha_LM from P.
 T31 unquenched plaquette shifts dP = +0.021, +0.037, +0.065 (4/8/16 tastes).
 F2r = ratio form: m_tau / v_data predicted as alpha_bare*alpha_LM (only P^(-1/4) sensitive).
 F2a = absolute form: m_tau from M_Pl (7/8)^(1/4) u0 alpha_LM^18 (P^(-17/4) sensitive).
 F1f = a^2 predicted as g2_fw * v_fw / 512.
 PASS (route usable as a derivation target): at least one of F1f, F2r reproduces the data (a^2 or m_tau/v) within 0.5% with
   quenched P and within 2% at all three unquenched P.
 FAIL: otherwise.
 My prediction before running: F2r passes quenched (0.02%) and FAILS unquenched (shifts about -0.9%, -1.5%, -2.6%); F2a fails
 badly unquenched (-14% to -36%); F1f fails (about -2%) because g2_fw is not 0.6528. Overall FAIL.

## Test 2: look-elsewhere (p_LEE), null = a random scale
 Null: replace the true a^2 by a^2 * rho, rho log-uniform in [0.5, 2] applied jointly to every combination (so the fixed
 ratios between anchors m_W : m_Z : v are kept). Count the fraction of nulls that have ANY family member within the window.
 Family N (narrow; lane's): anchor m_W, scale a^2, expression b^k, b in {2,3,4,5,6,7,8,9,10}, k>=2 integer, |N|>100. Window 0.032%.
 Family B (broad, honest forking): scale in {a^2, m_tau, 6 a^2}, anchor in {m_W, m_Z, v, v/sqrt2}, dress in {1,2,sqrt2,1/sqrt2},
   expression b^k, b in {2,3,4,6,8,16}, k in 1..14. Window 0.032%.
 Family C (couplings): T = scale/anchor with scale in {a^2, m_tau}, anchor in {v, m_W, m_Z}; expressions
   alpha_bare^m alpha_LM^n u0^l (7/8)^(j/4) 2^s, m,n in 0..3, l in -4..4, j in {0,1}, s in {-2..2}; window 0.02%.
 Reading: NOT NOTABLE if p_LEE >= 20% for B and C; NOTABLE if <= 5% for both. My prediction: N about 1-3%, B 10-40%, C 20-60%.

## Test 3: anchor-convention test of the "structural exponent"
 For each anchor A and scale S compute e = log_base(A/S) for base 2 and 4. The count reading "256 = 4^4" survives only if at
 least two independent anchors give integer exponents within 0.1%. Prediction: only m_W (256); v gives 512*(1/g2) not a power.

## Test 4: homogeneity (exact)
 Run the landed corner-kernel runner (or reproduce Theorem 4): restriction of every stipulated quadratic to the T1 carrier is
 linear in its coefficient vector, and (alpha,beta,gamma) -> (a, Re b, Im b) has rank 3, so the overall scale is invariant under
 the group, the grading and every linear map: scale is free unless a non-homogeneous normalisation is supplied.
 PASS if rank 3 and scaling test exact; that prices the wall as "a scale-breaking normalisation is required".
