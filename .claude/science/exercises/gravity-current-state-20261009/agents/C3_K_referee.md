# C3 lane K (K-num + K-ana): referee verdict (codex gpt-5.6-sol, xhigh; other vendor; 2026-10-10)

## VERDICTS

- **K-num: REJECT as a lane-K FAIL; ACCEPT only as a bounded side result.** Its massive substitute model genuinely has a converged anisotropic \(O(e^2)\) term, but it is not the preregistered model.
- **K-ana: PARTIALLY SUPPORTED.** Its overall **INCONCLUSIVE** verdict is correct. Its “PASS-by-identity branch is closed” no-go is not established and must be replaced by the checker’s narrower statement.
- **Lane K: INCONCLUSIVE.** The registered setting was neither computed nor sufficiently defined to compute as written.

## Findings

1. **The 9/4/1 count and gauge null vector are correct.**

   Independent exact rerun gives 9 \(W(B_4)\)-invariant two-derivative forms, a 4-dimensional \(O(4)\) subspace, and a rank-8 gauge map with unique null vector
   \[
   Q_{\rm EH}=\tfrac14(I_1-2I_2+2I_3-I_4).
   \]
   See `work_ana/k_forms_exact.out:3–13` and the independent numerical construction in `work_num/out_forms.txt:1–5`.

   The TT restriction has rank \(4=1+3\): one isotropic and three anisotropic restricted structures (`work_ana/k_forms_exact.out:13`). This is a form-space count, not by itself a proof that exactly three physical counterterm tunings suffice.

2. **K-num’s regulated side-model numerics are sound at fixed nonzero masses.**

   I reproduced its \(L_p=6\), \(m^2=\mu^2=1\) result:
   \[
   c_{A4}=-5.24673\times10^{-5},\qquad
   |c_{A4}/\kappa_2|=0.4738.
   \]
   The stored sequence converges geometrically through \(L_p=16\) to \(c_{A4}\simeq-2.50\times10^{-5}\), ratio \(0.2286\): `work_num/out_summary.txt:4–8`, `work_num/verify/out_Lp16_mu1.txt:7–14`. The \(q^2\) versus lattice-\(s^2\) fit convention and three- versus four-point fits change the result negligibly. The brute-force calculation also reproduces the fast contraction at \(O(10^{-8})\): `work_num/out_bruteforce.txt:7–8`.

   Thus the substitute model really is anisotropic. Only two combinations were determined, but one would have sufficed for FAIL had this been the registered setting.

3. **The regulator and preregistration prevent that result from deciding lane K.**

   The preregistered primary theory had scalar mass \(m=0.5\) and a massless photon; nonconvergence was explicitly mapped to INCONCLUSIVE: `work_num/PREREG.md:15–17`, `work_num/PREREG.md:31–35`. The photon mass \( \mu^2A^2 \), together with \(m^2=1\), was added only after the massless runs failed: `C3_K-num_report.md:64–67`, `C3_K-num_report.md:194–204`.

   This is not an innocuous regulator for a stress-Ward-identity test: the h-independent photon mass is neither photon-gauge-invariant nor metric-coupled. Replacing it with a metric-coupled Proca term shifts \(c_{A4}\) by roughly 10–15%: `work_num/verify/out_proca_Lp10.txt:2–9`. More importantly, the \(\mu\to0\) limit was not computed; the massless sequence is nonconvergent, and \(\mu^2=0.1\) has only one box size: `C3_K-num_report.md:139–150`, `C3_K-num_report.md:194–204`.

   The substitute is also already \(O(1)\)-anisotropic at \(O(e^0)\), with cutoff-sized masses: `C3_K-num_report.md:188–192`. Consequently its \(O(e^2)\) result does not isolate the extra cost that the optimized-stress test was designed to measure.

   Finally, \(\kappa_2\) is a TT average, not an unambiguous coefficient of the gauge-invariant EH form—the measured isotropic sector is itself not EH-shaped (`C3_K-num_report.md:169`). Against the free kinetic term at physical \(e^2=4\pi\alpha\), the reported ratio is \(9\times10^{-5}\), below the literal \(10^{-4}\) bar: `C3_K-num_report.md:246–249`. This normalization issue reinforces, but is not needed for, the INCONCLUSIVE verdict.

4. **K-ana’s narrowed claim is correct; its no-go is not.**

   Its own exact algebra proves only
   \[
   c_{\rm an}=0
   \quad\Longleftrightarrow\quad
   \text{the anisotropic projection of }W^{(3)}\text{ vanishes},
   \]
   because the Ward images split into rank-3 \(O(4)\) and rank-5 anisotropic blocks: `C3_K-ana_report.md:101–108`.

   Full \(W^{(3)}=0\) is sufficient, but not necessary. An explicit counterexample is any non-EH \(O(4)\)-invariant combination such as \(F_1\): it has nonzero Ward violation but zero anisotropic coefficients. Therefore `C3_K-ana_report.md:137–141,219–223` overstates necessity.

   The valid conclusion is: the known symmetries—\(W(B_4)\), the tree graviton symmetry, U(1), and staggered shifts—allow all nine forms and do not force the five anisotropic ones to vanish. An exact coupled-stress Ward identity would suffice, but other identities, emergent rotations, or an accidental vanishing of only the anisotropic Ward component remain open. This matches `C3_K-ana_report.md:270–277`.

5. **The fixed setting is not implementable from the named ingredients.**

   The test registers K7a’s Euclidean \(Z^4\), \(W(B_4)\)-covariant h together with “K3a’s optimized range-\(R\) stress”: `TESTS.md:499–508`. But the K3a object is a continuous-time 3D Hamiltonian momentum charge. It does not supply a Euclidean \(Z^4\) stress tensor, four current components, an off-shell \(O(e)\) vertex, or the seagull needed to form the requested vacuum polarization: `work_num/PREREG.md:11–16`, `C3_K-ana_report.md:293–295`.

   Its actual symmetry is only spatial cubic \(\times\) time reflection. Under that group the correct form space is 26-dimensional with two gauge-invariant forms, not 9/1: `C3_K-ana_report.md:143–148`. The second gauge-invariant form is an independent speed/light-cone parameter, explicitly verified in `work_ana/k_speed_form.out:1–5`.

   Lane K therefore needs re-registration: either construct a genuinely \(W(B_4)\)-covariant Euclidean stress plus seagull and rerun the 9-form test, or retain K3a’s continuous-time setting and use the 26-form/2-gauge-invariant decomposition.

## Strongest correct statement

Keeping the grid has **not** been shown to cost only the two shear tunings. Hypercubic symmetry alone allows five anisotropic kinetic operators, whose direct TT restrictions span three speed/birefringence structures. They require some additional protection or tuning in a generic implementation.

But this campaign has not shown that those coefficients are nonzero for the intended optimized stress, nor that “three” is the complete physical tuning count—off-axis TT/longitudinal mixing makes that inference unsafe (`C3_K-ana_report.md:297–301`). Thus the defensible conclusion is:

> **Two shear tunings alone are not established; additional speed-sector protection/tuning remains an open, generically expected cost. The registered lane does not determine its presence or number.**