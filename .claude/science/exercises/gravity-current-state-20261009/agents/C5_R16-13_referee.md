# VERDICT: NOT CONFIRMED

The analytic and numerical core is largely reproducible as a conditional
`M + V0 + SF` calculation, but the central **LIFTED** reading is not confirmed.
The only joint zero uses the scalar M vertex on gapped G/Gw edges.  That vertex
cannot be the continuous, periodic, proper-cubic-covariant local lattice stress
required by the item’s R9-9/R13-5 setting.  The correct full-setting reading is
therefore **OPEN**.  The formal three-integral cancellation should be retained
as conditional support, not discarded.

1. **Theorem DT: confirmed with two scope corrections.**  Directly
   differentiating the projector trace gives the pair weight, alpha, beta and
   the stated
   
   \[
   \Xi_F={N_c\over8}\left\langle {|G|^2(|\partial_zc|^2-1)\over E^3}\right\rangle
   -{N_c\over32}\left\langle {|V|^2(5v_z^2-1)\over E^5}\right\rangle .
   \]
   
   An independent finite-q evaluation of the original pair bubble on
   D1(1.4,0.3), at m=0.3, agrees with DT to 2.1e-9 (T2g) and 2.6e-9 (Eg)
   (`R16-13_referee_checks.out:37-42`; independent implementation
   `referee_dt_check.py:28-60,81-97`).  The report’s derivation is otherwise
   correct (`R16-13_report.md:138-158`), with the notation at line 153 read as
   hat(c) dot partial_z hat(c) = 0.  Correction 1: the unspecified “+ seagull”
   at `R16-13_report.md:142` must be assumed q- and omega-independent
   (ultralocal); otherwise it can add to Xi.  Correction 2: V0 and SF are
   clearly stated (`R16-13_report.md:84-97`) and are mathematically reasonable
   as separate stipulated responses, but the report does not derive them from
   one Belinfante lattice action.  V0 omits the Wilson TT coupling, whereas SF
   uses p_i=s_i s_i'+M W_i' (`scripts/dirac.py:137-152`).  Thus the result is
   conditional on both law data, not a derived physical fermion stress.  This
   matters because the fixed setting asks for a Belinfante-symmetrized lattice
   stress (`TESTS.md:5597-5599`).

2. **Signs: confirmed for the stated D1/G comparison, not as a class-wide
   sign theorem.**  At m=0.01 an independent quadrature gives, per four-component
   Dirac field on D1(1.4,0.3),
   `(Xi_T2g,Xi_Eg,mu_E)=(+5.46009e-3,+2.82914e-3,-2.91854e-2)`, while G(1.4)
   gives `(-1.68922e-3,-8.48914e-4,+4.33836e-3)`
   (`R16-13_referee_checks.out:22-26`).  All three signs are therefore opposite,
   as claimed at `R16-13_report.md:181-192`.  The worker’s mu_E=-2.95e-2 is
   about 1% underconverged, but its sign and scale are sound.  The qualification
   is already visible in its DG/DZ scan: every sign occurs somewhere, so the
   result is not universal over Dirac edges (`R16-13_report.md:194-202`).

3. **Wilson-Dirac T2g shear mass: confirmed as a mechanism and explicit
   counterexample.**  For `M=m+sum W_j`, differentiating E^2/2 gives
   `H_xy=W'_x W'_y`; the separable Liouville cancellation used by R9-2 no
   longer applies (`R16-13_report.md:171-174`; compare
   `C5_R9-2_report.md:219-225`).  The independent D1 check gives
   `mu_T2=-1.15955e-6`, and the joint root gives `-3.52766e-5`
   (`R16-13_referee_checks.out:12,22-24`).  Hence R16-9’s coupling-specific
   zero row does fail for this stipulated Wilson sea (`C5_R16-9_report.md:218-225`).
   Logical correction: `H_xy` not identically zero alone does not prove that
   its zone integral is nonzero for every law; the justified statement is
   “generically/can be nonzero, with explicit checked witnesses.”

4. **Joint zero: numerically confirmed after a small re-solve.**  A separate
   positive-octant tensor Gauss-Legendre implementation, importing none of the
   probe’s evaluators (`referee_numeric.py:1-40`), evaluates the published point
   as `(-6.98e-8,-4.30e-8,+3.92e-6)` rather than zero
   (`R16-13_referee_checks.out:3-6`).  Re-solving only `(b2,bf,r)` at m=0.01
   gives `(1.740668966789,1.313474886012,0.572783392213)` and independent
   higher-resolution residuals `(-1.93e-11,-1.16e-11,+1.51e-9)`; the Jacobian
   determinant is `6.7484e-8` (`R16-13_referee_checks.out:8-13`).  At m=0.001,
   a separate re-solve gives `(1.736408230221,1.310237125763,0.575485614089)`
   with the same accuracy and a nonzero determinant (`R16-13_referee_checks.out:15-20`).
   Both r values are strictly below `1/sqrt(3)`, so Lemma V1 proves the Dirac
   edge subluminal; the scalar derivative bound proves the other two edges
   subluminal (`R16-13_report.md:176-179,246`).  The three-condition/three-tuning
   count is therefore numerically genuine.  Two corrections travel with it:
   `verify_root6.py` freezes the width fraction `fr2`, not physical `w2`
   (`scripts/verify_root6.py:26-28`; `scripts/content4.py:7-10`), and the claimed
   O(m^2) transfer to all light masses is false for Wilson
   `M=m+sum W` (`R16-13_report.md:265-266`).  The fixed-law residual is linear in
   m in the independent scan (`R16-13_referee_checks.out:28-35`); the m=0.001
   result is valid because it was separately retuned.

5. **Fixed reading: OPEN, not LIFTED.**  Abstracted from its setting, the
   isolated clause at `TESTS.md:5609-5612` is indeed met by the conditional
   three-functional exercise: explicit mixed content, subluminal dispersions,
   a common light mass, a checked zero and count three.  The clause must,
   however, be read inside the registered R9-9/R13-5 local-stress setting at
   `TESTS.md:5597-5599`.  That setting requires a quasi-local stress with a
   smooth pair kernel (`C5_R13-5_report.md:85-97,143-160`), and the winning
   scalar M vertex fails it.  Therefore no admissible local-law lift has been
   exhibited.  Nonzero mu_T2 is an additional physical shear row but is not by
   itself a violation of the literal three-row clause.  Likewise, two scalar
   edges and absent SM multiplicities leave probe (c) open
   (`TESTS.md:5603-5607`; `R16-13_report.md:294-297`), while omitted photons do
   not invalidate an existential witness because they were optional
   (`TESTS.md:5599`).  “PERSISTS ... false as worded” at
   `R16-13_report.md:298` is too strong: this nonlocal conditional witness does
   not refute persistence within the local-stress class.  Neither LIFTED nor
   PERSISTS is established there.

6. **R17-4 Lemma M applies directly and is independently sound.**  Proper
   `C2_y` covariance makes a T_xy amplitude odd under
   `(K_x,K_z)->(-K_x,-K_z)`.  At the torus fixed point `(pi,K_y,0)`, periodicity
   therefore forces every continuous amplitude to vanish, whereas M requires
   squared magnitude `g(pi)g(K_y)>0` on these doubler-free G/Gw edges
   (`C5_R17-4_report.md:114-124`).  Thus M has no absolutely summable real-space
   stress kernel there (`C5_R17-4_report.md:123-127`).  This is not merely a
   later surprise: R13-5 had already stated that M on G is nonlocal and that U
   should be used (`C5_R13-5_report.md:168-180`).  The R16-13 root explicitly
   uses M on both scalar families (`R16-13_report.md:233-239`); its U attempt did
   not find a root (`R16-13_report.md:208-217`).  Failed U searches are not a
   no-go, so the local problem remains OPEN.

**Strongest correct statement.**  Under an ultralocal-seagull assumption and the explicitly stipulated V0 Dirac TT response plus SF strain flow, Theorem DT, the D1 opposite-sign example, Lemma V1, and a nonzero Wilson-Dirac T2g shear mass are correct; moreover, a reproducible subluminal `2 G + 2 G_w + 1 D1` content has a codimension-three zero of the two axial bare-cone coefficients and mu_E at each separately tuned light mass, with a nonsingular three-knob Jacobian.  This does not lift R16-9 in the registered local-stress setting: the scalar M amplitude used by the only root is nonlocal on both gapped edges, V0 and SF have not been obtained from one Belinfante action, mu_T2 remains nonzero, and neither one-Higgs-edge nor SM-count content is reached.  The full reading is therefore **OPEN**, while the conditional M/V0/SF three-integral cancellation is valid support.
