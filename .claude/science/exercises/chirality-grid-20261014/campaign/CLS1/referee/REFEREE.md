# CLS-1 independent referee report

**VERDICT: CONFIRMED WITH CORRECTIONS.**

The BCC label calculation, the loss of X2-L2's exact corner decoupling, the existence of symmetry-allowed light--light dimension-3 and dimension-4 bilinears, the free-proxy spectra, and the conclusion that a generic class-S completion is catastrophically non-Lorentz-invariant are sound.  The FIXED reading is **CLS-PRICE**, not CLS-KILL, because the registered R3 explicitly classifies a named symmetry/tuning as PRICE.  The important corrections are that equal translation charge proves that the hopping is *allowed*, not that its Wilson coefficient equals the Yukawa coefficient; no theorem in the packet proves that every symmetry capable of eliminating it also eliminates the Yukawa; the exact IceCube multipliers require an unshown map from the corner basis to the neutrino flavour basis; the advertised one-loop speed spread omits the toy's temporal wave-function term; and neither free-fermion proxy determines the many-body SMG outcome.

## Record and reproducibility

I read `REPORT.md`, both preregistrations, the CLS-1 FIXED item, X2, K1, OBS-3, OBS-4 and the OBS-4 referee report, and all `scripts/cls1_*.py` and saved outputs.  I reran, one process at a time through `./capped.sh`, the label/symmetry, invariant-count, theta, light-spectrum, bounds, and loop4 jobs.  Their numerical outputs reproduce exactly apart from the watchdog line (`referee_labels.out:1-34`, `referee_count.out:1-11`, `referee_theta.out:1-22`, `referee_light.out:1-54`, `referee_bounds.out:1-63`, `referee_loop4.out:1-5`).  Peak RSS was 14.9--215.5 MB, below the requested 0.3 GB.

I also made two small independent checks.  `referee_checks.py:1-63` independently enumerates the residual translations and sectors, verifies the sum/difference charge identity for all 64 ordered corner pairs, diagonalises the light adjacency matrix, checks the filter rank including an exceptional point, and separates SME coefficients from eigenvalue spreads; its output is `referee_checks.out:1-14`.  `referee_loop_full.py:1-108` reconstructs the worker's toy self-energy and includes both its spatial derivative and its computed temporal wave-function matrix; its output is `referee_loop_full.out:1-3`.

The IceCube Table 1 values were checked against the primary paper, [Aartsen et al., arXiv:1709.03434v3](https://arxiv.org/html/1709.03434v3): at 99% CL it gives \(|\operatorname{Re,Im}\mathring a^{(3)}_{\mu\tau}|<2.9\times10^{-24}\,\mathrm{GeV}\) and \(|\operatorname{Re,Im}\mathring c^{(4)}_{\mu\tau}|<3.9\times10^{-28}\).  The paper also says these one-at-a-time limits set the diagonal SME parameters to zero.

## 1. Key claim: light--light hopping

### 1.1 What is proved

At an order-two Brillouin-zone corner, \(-Q=Q\pmod{2\pi}\).  Consequently

\[
Q_c+Q_{c'}=Q_{c'}-Q_c\pmod{2\pi},
\]

so \(\psi_c\psi_{c'}H_0S_K\) and \(\psi_c^\dagger\psi_{c'}S_K\) have the same **translation** character.  The worker's enumeration gives, for each hw2 \(K\), both an hw1--hw1 pair and an hw1--hw3 pair (`scripts/labels.out:8-11`); my exhaustive check agrees (`referee_checks.out:4`).  This is the exact correction to the earlier OBS-4 statement, which established only hw1--hw3 permission (`OBS4_REFEREE.md:127-139`).

No symmetry actually specified in class S forbids the light--light bilinears:

- Spin(10) allows \(\overline{16}\,16\,S\) through the singlet in \(\overline{16}\otimes16\); if the UV Yukawa is written Spin(10)-covariantly, its \(16\,16\,H_0S\) contraction is a different invariant.  After reduction to \(G_{SM}\), generation-changing kinetic terms between fields with identical gauge quantum numbers remain gauge singlets.  These statements show permission, not equality of couplings.  X2's original Majorana exclusion instead uses the absence of a singlet in \(16\otimes16\) (`X2_COMBO_REPORT.md:84-88`).
- The equal-amplitude condensate retains the proper cubic group acting on corners and the three \(S_K\)'s together.  The explicit density P-a, modulated walker hop P-c, and filter modulation P-d are cubic covariants (`scripts/cls1_labels.py:45-88`; reproduced at `referee_labels.out:13-19`).  Thus the residual permutation symmetry of the condensate does not remove them.  A less symmetric condensate only permits more structures.
- The invariant-space count is correct: exact translations permit two corner-diagonal linear-in-momentum structures, whereas BCC permits five, leaving a three-dimensional corner-off-diagonal quotient (`scripts/cls1_count.py:69-103`; `referee_count.out:1-10`).  This is the precise content of “three new structures not removable by OBS-3's two”; OBS-3's corner-diagonal premise is explicit at `OBS3_REPORT.md:75-78`.
- The proposed antiunitary \(\Theta\) forbids the on-site density P-a but permits P-c and P-d (`referee_labels.out:14-19,23-33`).  Therefore \(\Theta\) removes the dimension-3 hazard, not the dimension-4 hazard.

Accordingly, the strongest symmetry result is: **class S removes the translation selection rule, and the stated Spin(10)/\(G_{SM}\), cubic, and condensate symmetries leave explicit dangerous light--light operators allowed.**

### 1.2 What is not proved

“Same translation charge” does not equate Wilson coefficients.  The hopping coefficient \(g'\) and the coefficient of the higher-dimensional Yukawa operator are independent couplings.  If \(S\) is canonically normalised and \(g'=O(1)\), its vev does give the natural scale \(\epsilon=g'f\); but setting \(g'=g\), hence \(\epsilon a=0.33\), is the preregistered naturalness convention (`PREREG.md:57-60`), not a consequence of the Yukawa.  The correct technical wording is “generic and unprotected,” not “generated at the same coefficient whenever the Yukawa is present.”

The statement that *any* symmetry removing the hopping also removes the Yukawa is too strong and is not proved.  Indeed, the worker's own \(\Theta\) separates the CPT-odd density hopping from the Yukawa while leaving the intended Yukawa toy \(\Theta\)-covariant (`scripts/cls1_labels.py:69-88`; `scripts/cls1_loop.py:1-4`).  What is true is narrower: residual translations cannot distinguish the two momentum channels, and no additional **presently supplied** symmetry forbids all three CPT-even c-type structures.  A new internal/form-factor/spacetime selection rule would itself be named extra structure and would need a fresh compatibility check with the diagonal and off-diagonal Yukawas.

Radiative generation is supported but not established for the actual model.  The toy produces BCC-only kinetic structures at one loop (`scripts/loop2.out:2-5`; `scripts/loop3.out:3-8`), but the actual B-gen vertex matrices and Spin(10) spin contraction are outside scope (`REPORT.md:118-125`).  The toy even has special cancellations: its spatial off-diagonal coefficient vanishes when \(y_0=y_1\) (`scripts/loop.out:2,5,8,11`).  Thus “nonzero whenever” is false for that component; the defensible statement is that no general OBS-3 cancellation survives and generic unequal/complex couplings regenerate allowed structures.

## 2. Item (i): labels and \(\Theta\)

**Confirmed at the perturbative one-body level.**  The surviving translations obey \(n_x=n_y=n_z\pmod2\), with residues 000 and 111 (`scripts/cls1_labels.py:9-16`; `referee_checks.out:1`).  Their two corner classes are

- \(\{\mathrm{hw0},\mathrm{hw2}\}\), four R nodes, index \(+4\);
- \(\{\mathrm{hw1},\mathrm{hw3}\}\), four L nodes, index \(-4\).

The independent table is at `referee_checks.out:2-3`, and the full rerun at `referee_labels.out:2-6`.  Since \(T_{(1,1,1)}=(-1)^{\mathrm{hw}}\), its character equals node chirality.  A weak BCC-preserving Dirac mass cannot pair opposite chiralities at a folded point, while a Spin(10)-invariant Majorana bilinear is unavailable.  This justifies the report's word “perturbatively” (`REPORT.md:45-51`).

Two scope corrections are needed.

First, “no bilinear can pair anything” should not be read as an all-strength theorem.  BCC bilinears can move nodes; the worker's own random test loses the \(\pm4\) charge from a radius-0.6 sphere at strengths 0.3--0.6 and did not test global annihilation (`scripts/cls1_index.py:60-71`; `scripts/index.out:1-4`).  The sector indices protect small deformations while the enclosing surface stays gapped, not arbitrary-strength bilinears.

Second, \(\Theta\) is only a **candidate extra one-body particle-hole/CPT structure** in this packet.  The scripts verify \(h(-k)+Mh(k)M=0\) for the displayed free matrices (`scripts/cls1_labels.py:69-88,126-138`), which pins the appropriate free folded point, but they do not construct \(\Theta\) on the full Spin(10) Yukawa, gauge links, or interacting quartic.  The report concedes that the gauge-link extension is only suggested and that many-body SMG is untested (`REPORT.md:118-125`).  K1's anomaly statement did not include \(\Theta\) (`K1_KILL_REPORT.md:128-153`).  Hence “non-perturbatively this needs \(\Theta\)” must be narrowed to “an all-strength one-body pinning statement needs an extra symmetry such as the proposed \(\Theta\)”; it is not a many-body theorem.

## 3. Item (iii): observable sizes and one-loop toy

### 3.1 Tree-level proxies

The arithmetic in `scripts/cls1_bounds.py:8-30` is internally correct and reruns exactly (`referee_bounds.out:1-30`).  The cubic light density matrix has eigenvalues \((-\epsilon,-\epsilon,2\epsilon)\), independently reproduced at `referee_checks.out:5`, so its eigenvalue range is \(3\epsilon\).  At \(\epsilon a=0.33\) and \(1/a=1.22\times10^{19}\) GeV this is \(1.2078\times10^{19}\) GeV.  P-c gives speeds \(1-\eta,1,1+\eta\), hence range \(2\eta\) (`referee_light.out:33-37`).  P-d gives a numerical range 0.1595 at \(\kappa=0.33\), rather than exactly \(\kappa^2=0.1089\) at that non-asymptotic value (`referee_light.out:38-42`).

The IceCube numbers themselves are correct, but the mapping is overstated.  Table 1 bounds one off-diagonal \(\mu\tau\) SME **matrix coefficient** at a time, with diagonal coefficients set to zero; the report divides those limits by a three-flavour eigenvalue range.  For a two-flavour pure off-diagonal coefficient \(x\), the eigenvalue range is \(2|x|\).  At the central point, the coefficient-level ratios are \(\epsilon/a_{\rm IC}=1.39\times10^{42}\) and \(\eta/c_{\rm IC}=8.46\times10^{26}\), whereas the report's spread ratios are \(4.16\times10^{42}\) and \(1.69\times10^{27}\) (`referee_checks.out:10-13`).  Moreover, no PMNS/charged-lepton rotation from the corner basis to the IceCube \(\mu,\tau\) basis is supplied.  Therefore the printed \(4\times10^{42}\), \(1.7\times10^{27}\), and \(2.8\times10^{26}\) are order-of-magnitude proxy comparisons, not exact experimental exclusions of those corner matrices.  The correction is only order unity for generic flavour projection and does not affect the conclusion that an untuned order-one coefficient is fantastically excluded.

The reported tuning \(\sim6\times10^{-28}\) is consequently reliable only as an order-of-magnitude coefficient tuning.  The count establishes three independent **corner/spin tensor structures per internal representation**, not “about 18 counterterms.”  Eighteen assumes independent coefficients for six SM multiplets; exact Spin(10) could relate them, while broken-phase Yukawas could generate a different internal count.  The report properly labels 18 as suggested (`REPORT.md:94-98`), and it should remain so.

### 3.2 One-loop toy: qualitative result confirmed, quoted number corrected

The saved and rerun spatial calculation is stable: at phase 0.07 it gives \(2.27\times10^{-5}\) at \(N=48\) and \(2.34\times10^{-5}\) at \(N=64\) (`referee_loop4.out:2-3`).  The real-coupling spatial basis coefficient \(0.14674(y_0-y_1)y_1\) is also reproduced by the worker's scans (`scripts/loop2.out:2-5`).

However, this is not the full dispersion of the toy.  The loop code computes an off-diagonal temporal matrix \(Z=\partial\Sigma/\partial(i\omega)\) (`scripts/cls1_loop.py:62-75`) and even constructs a normalisation matrix, but then never uses it in the speed eigenvalues (`scripts/cls1_loop.py:92-99`).  `cls1_loop4.py` likewise uses only the spatial matrices (`scripts/cls1_loop4.py:84-97`).  Keeping the same integral and removing the corner-diagonal blocks as counterterm-removable, I obtain \(\max|Z_{\rm off}|=0.01474\) and a canonically normalised speed spread \(2.92\times10^{-2}\) at phase 0.07; the temporal term already gives \(2.93\times10^{-2}\) at phase zero (`referee_loop_full.out:1-2`).  Sign conventions for \(Z\) can change details but not justify dropping it.

Thus the specific “\(2.3\times10^{-5}\), \(6\times10^{22}\) over IceCube” row is **not confirmed as the toy's complete one-loop answer**.  The corrected same-toy assembly is roughly \(7.5\times10^{25}\) times the IceCube coefficient number if one makes the same direct spread comparison.  This strengthens, rather than weakens, the qualitative conclusion that OBS-3's corner-diagonal cancellation is gone.  It remains a toy result, not a calculation of the actual B-gen/SMG theory.

## 4. Item (ii): zero-mode count and proxy fidelity

For model A at the folded odd point, the elementary-fermion nullity per spin is

\[
\dim\ker\Phi(P)=4-\operatorname{rank}\Phi(P).
\]

This is a correct linear-algebra statement for the static-partner Hamiltonian (`scripts/cls1_core.py:47-62`).  Strictly, the full doubled Hamiltonian also contains a partner nullspace, so “number of zero modes” should specify the elementary \(\psi\) nullity.  At \(\kappa=0\), rank \(\Phi=1\), giving three elementary light modes.  At \(\kappa=0.33\), rank is four and the singular values reproduce the worker (`referee_checks.out:6-7`; `referee_light.out:20-28`).

The statement “rank four for every \(\kappa\ne0\)” has an isolated algebraic exception: for the displayed equal-amplitude filter

\[
\det\Phi(P)=\kappa^3(4-3\kappa),
\]

so rank drops to three again at \(\kappa=4/3\) (`referee_checks.out:8-9`).  This does not affect the scanned \(0<\kappa\le1\) or the central \(\kappa=0.33\), but the theorem statement needs the exception.

The first-order coupling statement is correct: the three light-channel singular values begin as \(2\kappa,\kappa,\kappa\), so the quartic four-light strength scales as \(Ww^4\), not as \(W\theta^4\) with only hw3 probability (`scripts/cls1_light.py:56-84`; `referee_light.out:20-28`).  The literal static-partner model's zero hw3 elementary weight and nonzero partner weight are also correct within that Hamiltonian (`scripts/cls1_theta.py:15-37`; `referee_theta.out:1-13`).

Of the two proxies, **model B is qualitatively closer to SMG**, because a weak projection of an interacting channel should not automatically make a bilinear gap; model A gaps every nonzero singular channel by construction and its free auxiliary field brings the unpaired zero modes already identified as the T5 pathology (`REPORT.md:78-81`).  Model B nevertheless is not a many-body calculation: it inserts a hard, momentum-dependent SVD threshold and assumes the criterion \(Ww^4<W_c\), ignoring mixed light--mirror channels and critical dynamics (`scripts/cls1_core.py:64-78`; `PREREG.md:45-50`).  Its \(\kappa\lesssim0.55\) result is therefore a registered comparator, not evidence that X2's actual filtered quartic remains gapless.  The decisive many-body no-gapless-composite/SMG question remains open (`X2_COMBO_REPORT.md:169-177`; `K1_KILL_REPORT.md:198-203`).

## 5. FIXED reading

**CLS-PRICE is the correct FIXED reading in the declared lane.**  The FIXED definitions say PRICE when safety requires a named structure or tuning and KILL only when no such escape is admitted (`TESTS.md:524-529`); preregistration R3 makes that application explicit (`PREREG.md:57-61`).  The candidate escape is \(\Theta\) for the dimension-3 term plus tuning/counterterms for the allowed dimension-4 tensors.  The coefficient tuning is of order \(10^{-27}\) at tree-natural size (order-unity flavour-normalisation corrections do not matter), while the exact number of internally independent counterterms is not established.  KILL is therefore contrary to R3 even though the untuned proxy is KILL-level throughout the registered \(f\) range.

This reading is deliberately limited to a 3D continuous-time walker, one-body free-fermion auxiliary-partner proxies, and a simplified one-loop Yukawa toy.  It does not establish \(\Theta\) for the full gauged interacting law, does not calculate the actual B-gen vertex/self-energy, and contains no many-body SMG calculation.  The full class-S X2 completion therefore remains dynamically unresolved even though its generic naturalness problem is clear.

## Strongest correct statement

Breaking unit translations with all three hw2 singlet condensates leaves BCC translations and folds the corners into an all-R \(\{\mathrm{hw0},\mathrm{hw2}\}\) class and an all-L \(\{\mathrm{hw1},\mathrm{hw3}\}\) class, so weak BCC-preserving bilinears cannot directly Dirac-pair the folded nodes; nevertheless the same order-two momentum identity used by the CKM Yukawa also permits cubic-, Spin(10)/\(G_{SM}\)-, and condensate-symmetric light--light density and kinetic operators, including three new CPT-even corner-off-diagonal kinetic tensors.  Their coefficients are independent of the Yukawa but are generically natural unless further structure is imposed, and order-one projections exceed neutrino Lorentz-violation scales by roughly \(10^{26}\) for dimension four (and \(10^{42}\) for the CPT-odd dimension-three term if \(\Theta\) is absent).  The free proxies confirm loss of exact X2-L2 decoupling but disagree on gapping, while the one-loop toy confirms regeneration qualitatively and requires a temporal-term correction; therefore the registered result is CLS-PRICE—candidate \(\Theta\) plus approximately \(10^{-27}\)-level kinetic tuning—not CLS-KILL, strictly within one-body proxies and a toy loop, with the many-body SMG fate still open.
