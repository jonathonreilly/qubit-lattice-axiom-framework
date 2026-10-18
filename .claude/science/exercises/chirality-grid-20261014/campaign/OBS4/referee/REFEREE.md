# OBS-4 independent referee report

## VERDICT: CONFIRMED WITH CORRECTIONS

`FCNC-PRICE` is the correct FIXED reading under the worker's pre-registered rule 10.  The central calculation is sound in its stated degenerate-heavy D3 benchmark: the corner selection rule is correct, the exact B-gen matrices give order-one u↔c neutral-scalar Yukawas, the Q4 coefficient and the quoted Isidori--Nir--Perez (INP) rows are normalized correctly, and the equal-vev benchmarks require between 3.8×10^3 and 7.7×10^3 TeV (or half of this under the worker's stipulated factor-0.5 coupling bracket).  The class-S route is a genuine named-structure price and not something supplied by X2 as written.

The corrections are material.  The 0.88 TeV analytic number is a one-source estimate, not a bound on the stated general 28-quartic potential; that potential has six independent all-four-doublet source orbits.  Differential evolution is not a global upper-bound certificate.  I reproduce the reported 0.770 and 1.088 TeV optima, but the 8\(\pi\) optimum has an explicit negative quartic direction and is not bounded from below.  Moreover, the four-doublet potential search covers D3, not D6: D6 has repeated fields with the same translation charge, and bilinears between equal-charge fields are translation-even.  Finally, the report does not exclude cancellations from a general non-degenerate, mixed neutral-scalar spectrum, and it does not recompute the OBS-3 loop escape in class S.  Consequently, “KILL level for X2 as written” is a persuasive result for the tested D3 spectra, not a theorem over every D3/D6 scalar potential that the construction permits.

## Audit record

I read the fixed criterion first (`TESTS.md:439-453`), then the pre-registration and dated deviations (`PREREG.md:12-133`; `PREREG_FOLLOWUP_2026-10-15.md:3-28`), the worker report and scripts, and the relevant X2/OBS-3 source statements.  I checked the cited primary literature directly:

- [INP, arXiv:1002.0900, Table I](https://arxiv.org/pdf/1002.0900#page=9), including all five LR rows used here;
- [UTfit, arXiv:0707.0636, operator basis and Table IV](https://arxiv.org/pdf/0707.0636#page=11);
- [Harnik--Kopp--Zupan, arXiv:1209.1397, Eq. (29) and Table II](https://arxiv.org/pdf/1209.1397#page=18).

For an implementation-independent flavour check, `referee_checks.py:37-153` reconstructs the exact parameterized textures but diagonalizes (MM^\dagger) and reconstructs the right singular vectors, rather than importing the worker's SVD path.  It also enumerates the residual translation group and quartic orbits (`referee_checks.py:156-186`).  Separate runs reproduce the potential optima and sample the quartic form on 102,400 general complex directions plus 102,400 neutral directions (`referee_checks.py:189-226`).  All runs went through `capped.sh`, one at a time, with measured peaks 25.9, 84.5, and 83.4 MB (`referee_checks.out:21`; `referee_potential.out:6`; `referee_potential8.out:6`).

## 1. S1 and S4

### S1: confirmed

For a two-component Yukawa (\psi_c^T C\psi_{c'}\Phi_K), a unit translation contributes the phase

\[
  e^{i(Q_c+Q_{c'}+K)\cdot n}.
\]

At Brillouin-zone corners, (K=-K\pmod{2\pi}), so invariance gives (K=Q_c+Q_{c'}\pmod{2\pi}), exactly as stated at `REPORT.md:43-48`.  The same result would be written as a momentum difference in four-component notation; sum and difference coincide for these order-two corner momenta.  The walker-spin insertion (\tau_x\sigma_c) acts on internal/spin indices and carries no translation character, so it does not change the selection rule (`REPORT.md:50-56`; `OBS3_REPORT.md:68-72`).

The diagonal entries therefore live at (K=0), while the three unordered off-diagonal pairs live at (K_x=(0,\pi,\pi)), (K_y=(\pi,0,\pi)), and (K_z=(\pi,\pi,0)).  B-gen has both orientations of every pair nonzero, so D3 needs one electroweak doublet in each of these three sectors in addition to (H_0).  One complex doublet can carry both oriented Yukawa entries because those are independent coupling constants.  The four-doublet physical count (16-3=13) is also correct (`REPORT.md:50-54`).

### S4: the symmetry statement is right for D3, but the numerical ceiling is not proved as generally as claimed

For the D3 field set ((H_0,\Phi_x,\Phi_y,\Phi_z)), the four translation characters are the four elements of (\mathbb Z_2^2).  Hence (\Phi_a^\dagger\Phi_b) is nontrivial whenever (a\ne b), and every cross-charge dimension-two bilinear, including (H_0^\dagger\Phi_K), is forbidden.  This confirms the absence of the usual soft (m_{12}^2) tadpole/decoupling limit asserted at `REPORT.md:125-128` and implemented at `scripts/obs4_potential.py:2-7`.  Once all three hw2 fields condense, charge-neutral quartics containing all four sectors can generate effective tadpoles, so the stronger statement “there is no tadpole” must be read as “there is no independent dimension-two tadpole.”

The published analytic arithmetic is reproducible.  With

\[
 v_x\ge {57.5\ \mathrm{GeV}\over\sqrt{4\pi}}=16.22\ \mathrm{GeV},\qquad
 v_0v_yv_z\le \left({v^2-v_x^2\over3}\right)^{3/2},
\]

a *single* source term gives

\[
 M_x\le\left[4\pi\,{[(v^2-v_x^2)/3]^{3/2}\over v_x}\right]^{1/2}
     =0.8812\ \mathrm{TeV},
\]

matching `scripts/obs4_r2.py:100-106`, `scripts/r2.out:49-53`, and my independent value (`referee_checks.out:19-20`).  It is not, however, the analytic bound for the general potential searched later.  The tensor enumeration contains 28 CP-even Hermitian quartic orbits, of which **six** contain all four fields and contribute coherently to the same neutral tadpole (`scripts/obs4_potential.py:15-30`; `referee_checks.py:172-186`; `referee_checks.out:19-20`).  If the cap (4\pi) is put on each orbit coefficient, the corresponding crude coherent single-carrier scale is (\sqrt6\times0.881=2.16) TeV, not 0.88 TeV.  The worker's 0.33/0.47 TeV three-carrier geometric-mean estimate at `scripts/r2.out:49-53` similarly uses one effective source coefficient; allowing six capped orbit coefficients multiplies that scale by (\sqrt6).  The numerical search includes those six terms and therefore is the relevant worker evidence for the full CP-even D3 potential.

I reproduce the search values to all shown digits: 0.769766 TeV at (4\pi) (`referee_potential.out:1-3`) and 1.087819 TeV at (8\pi) (`referee_potential8.out:1-3`), matching `scripts/potential.out:3-8`.  But `differential_evolution` with one seed is a heuristic best-found maximum, not a certified global maximum (`scripts/obs4_potential.py:88-95`).  Thus it cannot by itself prove that every admissible potential lies below 1.09 TeV.

Boundedness from below was omitted explicitly (`scripts/obs4_potential.py:8-10`; `PREREG_FOLLOWUP_2026-10-15.md:25-28`).  Conceptually, omitting BFB enlarges the search domain, so a *certified* maximum on that larger domain would be a conservative upper bound.  Numerically, however, the (8\pi) maximizing point is not a physical allowed potential: I find (V_4=-9.76) on a sampled unit neutral direction (`referee_potential8.out:4-5`).  The reproduced (4\pi) point survived my finite random stress test (`referee_potential.out:4-5`), but that is not a BFB proof.  BFB therefore matters to the interpretation of the displayed (8\pi) point (“allowed/reachable” is false), while its omission biases a genuine exclusion ceiling conservatively.

There are two further scope gaps:

1. D6 is defined with distinct up and down fields at each (K) (`PREREG.md:45-52`), but the potential runner contains only four fields with distinct charges (`scripts/obs4_potential.py:2-7`).  In D6, (\Phi_{K,u}^\dagger\Phi_{K,d}) has zero translation charge and is not forbidden.  Heavy orthogonal same-charge combinations can therefore have ordinary dimension-two mixing.  One expects an active vev direction per charge still to inherit an electroweak radial mode, but the worker did not prove the generalized Rayleigh/coupling statement or search the seven-doublet potential.  The phrase “every mixed bilinear is odd” at `REPORT.md:126` is true only when there is one field per charge.
2. The flavour calculation assumes three degenerate heavy Higgs-basis doublets.  A general non-degenerate, mixed spectrum weights the carrier terms with a propagator matrix rather than a common (1/M^2).  The report itself concedes that it has not excluded a fine-tuned non-degenerate cancellation (`REPORT.md:200-203`).

Accordingly, the correct S4 conclusion is: exact translations remove the ordinary cross-charge decoupling parameter and make a TeV-scale active D3 carrier sector natural under perturbative quartics; the reported search strongly supports, but does not prove, a 1.1 TeV universal ceiling.  This qualification does not rescue the untuned D3 benchmarks, whose required masses are three to four orders of magnitude larger.

## 2. Flavour-changing couplings and the Higgs basis

The exact B-gen parametrization is indeed what the worker says: one common diagonal and six unit-modulus oriented off-diagonals before the overall sector scale (`scripts/obs3_univ_copy.py:78-85,119-130`; copied at `scripts/obs4_core.py:35-53`).  My independent eigensystem reconstruction gives

- B-gen: (\lvert\widehat Y^0_{uc}\rvert=0.656951), (\lvert\widehat Y^0_{cu}\rvert=0.656955), and (\lvert\widehat Y^0_{sd,ds}\rvert=0.01506) (`referee_checks.out:1-4`);
- B-gen120: (0.65689) and (0.01486), respectively (`referee_checks.out:9-12`).

These agree with the worker's table (`scripts/table.out:1-14`) and confirm the claimed (0.66) and (0.015).  The support projections sum to the full mass matrix, and the vev-aligned direction is diagonal in the mass basis (`scripts/obs4_core.py:68-84`; `scripts/table.out:7,14`; independently `referee_checks.out:5,13`).

It is legitimate to introduce a Higgs basis even though the vevs belong to distinct translation sectors.  A unitary rotation among canonically normalized doublets with the same electroweak quantum numbers is a field redefinition, not an assertion that translation remains unbroken.  In that basis the broken translations act non-diagonally.  Completeness gives, for (i\ne j),

\[
 \sum_{a\in\mathrm{heavy}}N^a_{ij}N^{a*}_{ji}
 =\sum_K\widehat Y^K_{ij}\widehat Y^{K*}_{ji}
  -Y^{\rm light}_{ij}Y^{{\rm light}*}_{ji}
 =\sum_K\widehat Y^K_{ij}\widehat Y^{K*}_{ji},
\]

because (Y^{\rm light}=M/v) is diagonal.  This validates `REPORT.md:60-61,83-85` for a common heavy mass.  It does **not** validate replacing a general physical scalar propagator by (M^{-2}\mathbf1); that is an additional spectral assumption.

One wording correction is useful: (H_0) is a translation-basis field, not the observed light Higgs.  Its projected matrix has the quoted large off-diagonal entries, but the aligned light scalar does not (`REPORT.md:158-159`; `scripts/table.out:7`).  Calling “the ordinary Higgs part” flavour-changing is correct only in this field-component sense.

## 3. \(\Delta F=2\), the bounds, and the tuned point

With the convention (\langle\phi^0_K\rangle=v_K), write (\phi^0_K=v_K+(H_K+iA_K)/\sqrt2).  A real (H) gives half of

\[
 C_4^{ij}=-{\widehat Y_{ij}\widehat Y^*_{ji}\over M_H^2},
\]

and a degenerate (A) gives the other half; the (C_2,\widetilde C_2) pieces cancel.  Therefore a degenerate complex heavy doublet gives exactly

\[
 C_4^{ij}=-{\widehat Y_{ij}\widehat Y^*_{ji}\over M^2},
\]

with no missing factor of two.  This agrees with the code convention (`scripts/obs4_core.py:7-9,94-111`) and with the single-real-scalar formula in Harnik--Kopp--Zupan Eq. (29), which the worker reproduces from UTfit at the percent level (`scripts/obs4_r2.py:15-23`; `scripts/r2.out:1-6`).

The INP LR scales are transcribed correctly: (K=(1.8\times10^4,3.2\times10^5)), (D=(6.2\times10^3,1.5\times10^4)), (B_d=(1.9\times10^3,3.6\times10^3)) TeV for real/imaginary coefficients, and (B_s=3.7\times10^2) TeV for the modulus (`REPORT.md:87-96`; `scripts/obs4_core.py:86-92`).  They are old 2007/2010 UTfit/INP inputs, deliberately used as the fixed comparator, not a 2026 global-fit update.

For equal D3 vevs, my reconstructed B-gen pair sums are

\[
 z_D=0.1132785-0.2630705i,\qquad
 z_K=1.46384\times10^{-4}+2.58471\times10^{-5}i,
\]

and the INP prescription (M_{*,r}=\Lambda_r\sqrt{|\operatorname{Re/Im}z|}) gives (M_*=7693.6) TeV, bound by (D_{\rm Im}) (`referee_checks.out:6-8`).  B-gen120 gives 3799.6 TeV, bound by (K_{\rm Im}) (`referee_checks.out:14-16`).  These independently confirm `REPORT.md:98-109`.  The broader (1.27\times10^3\)--(7.90\times10^3) TeV range is the minimum/maximum over the worker's displayed factor-0.5 searched examples, not a theorem over the exact B-gen solution manifold (`scripts/refit.out:2-35`).  The factor-0.5 Yukawa running is recalled rather than computed (`REPORT.md:108-110,176`).

The primary INP use is stronger than the worker's secondary direct estimate.  UTfit evolves the full operator basis at NLO; the worker's `run_C4` keeps only one multiplicative LO exponent (`scripts/obs4_core.py:136-143`) and does not include (Q_4\)-(Q_5) mixing.  This limitation is already secondary to the reading and does not affect the table-based (M_*).

The vev-tuned cancellation is real within the common-heavy-mass ansatz.  At the B-gen optimum, the D sum is only (4.05\times10^{-5}) of the sum of term magnitudes, and 1% vev jitter raises the median requirement from 29.7 TeV to 896 TeV (`scripts/r2.out:22-27`).  B-gen120 similarly gives (8.75\times10^{-5}), 43.0 TeV, and 545 TeV (`scripts/r2.out:39-44`).  The factor-0.5 bracket therefore gives 14.8 and 21.5 TeV.  The joint texture/vev search found 49.9--51.7 TeV at unit coupling, rather than improving the saved B-gen optimum (`scripts/tuned.out:26-38`).  This validates the stated fragility, but it is a local numerical result, and the optimized vevs were not embedded in an explicit scalar potential with the assumed degenerate spectrum.

## 4. No-alignment and NFC lemmas

The two useful lemmas are correct in the stated field content.

- Pich--Tuzón alignment (Y^K=\zeta_KM) is impossible when nonzero (Y^K) have disjoint proper supports while (M) has full support (`REPORT.md:73-75`).
- If all heavy Higgs-basis combinations were diagonal in the same mass basis, adding the already diagonal light direction would make every support matrix simultaneously bi-diagonal.  With invertible diagonal support (D), the matrices (O_KD^{-1}) would then be commuting normal matrices.  For two distinct pair supports, however, ((A_xA_y)_{10}=a_{12}b_{20}\ne0) while ((A_yA_x)_{10}=0), exactly as stated at `REPORT.md:75-78`.  B-gen has all of these entries nonzero.
- With one definite-translation-charge doublet per fermion charge sector, the only full-rank single support is the diagonal one, so the left rotations are monomial and (|V_{\rm CKM}|) is a permutation.  Equivalently, retaining only one off-diagonal pair per sector leaves an exact CKM zero.  This confirms the NFC conclusion at `REPORT.md:78-79` for the declared definite-momentum doublets.

These are not universal no-go theorems against arbitrary new multiplets, residual internal symmetries, or tuned propagator cancellations.  In particular, D6's same-translation-charge copies permit bilinear mixing, although after heavy orthogonal combinations are integrated out the active vev directions still face the disjoint-support problem.  The report does not supply the generalized D6 theorem.

## 5. Class S and the light--mirror protection

If all three singlets (S_{K_x},S_{K_y},S_{K_z}) condense, a translation (n\in\mathbb Z^3) survives iff

\[
n_y+n_z\equiv n_x+n_z\equiv n_x+n_y\equiv0\pmod2,
\]

so (n_x\equiv n_y\equiv n_z\pmod2).  This is the BCC sublattice with conventional cell (2a).  Enumeration gives the two residue classes (000) and (111) mod 2 (`referee_checks.out:17-18`).  All three hw1 corners and hw3 transform with the same odd character; hw0 and the three hw2 corners share the even character.  The worker's BCC/label claim is therefore correct (`REPORT.md:34-36,160`; compare X2's original per-corner protection at `X2_COMBO_REPORT.md:84-95`).

This genuinely removes the premise of X2-L2.  The exact commutator there relies on full corner conservation and on the filter vanishing at each individual hw1 corner (`X2_COMBO_REPORT.md:90-95`).  Once only BCC translations remain, (Q_{hw3}-Q_{hx}=K_x) is a reciprocal vector of the residual lattice, and (\psi_{hx}^\dagger\psi_{hw3}S_{K_x}) is translation-invariant.  X2 had already observed the same momentum channel for an hw2 Higgs (`X2_COMBO_REPORT.md:97-104`).  If its dimensionless coefficient is generic and (f=O(1/a)), it is an allowed (O(1/a)) mixing.

“Allowed” is the strongest proved word: the coefficient is not calculated or shown nonzero.  BCC translations alone cannot distinguish hw1 from hw3, so they cannot retain X2-L2.  A new internal charge, form-factor zero, or other exact selection rule might forbid the hopping, but none is present in the stated class S; it would be further named structure and would have to remain compatible with (\psi\psi H_0S_K).  No residual symmetry currently in the packet supplies that protection.

With only one electroweak doublet, its dimension-four neutral Yukawa is (M/v), so it has no tree-level Higgs FCNC (`REPORT.md:147-150`).  Singlet fluctuations still have flavour-changing couplings of order (m_{\rm off}/f) and mediate a nonzero tree-level amplitude of order (m_{\rm off}^2/f^4); it is fantastically small for (f\gtrsim0.03/a), but “tree-level FCNC vanishes” should be narrowed to “dimension-four Higgs FCNC vanishes.”  More importantly for logical closure, the worker labels survival of the OBS-3 one-loop Lorentz-violation cancellation in class S only “suggested” and did not recompute it (`REPORT.md:150-151,200-203`).  Thus class S is a credible passing architecture, not a fully checked X2+B-gen completion.

## 6. FIXED reading and scope

The fixed definitions say `FCNC-PRICE` whenever passing needs a stated mass, alignment, tuning, or named structure (`TESTS.md:448-453`).  The pre-registration makes the intended application explicit: unit-translation breaking above the electroweak scale, including class S, is named structure and therefore PRICE if it passes (`PREREG.md:92-105`).  Under those rules, the answer is **FCNC-PRICE**, not FCNC-KILL.  A high-scale singlet route lies outside X2 as written, but that is precisely the price being recorded; it is not supposed to count as a mass supplied by X2.

The additional phrase “at KILL level for X2 as written” should be retained only as a benchmark statement.  It is quantitatively true for the tested D3 degenerate and H-only spectra, even after the displayed vev cancellation, but it is not established for every scalar spectrum the construction permits because the 1.1 TeV cap is uncertified, D6 was not subjected to its own potential analysis, and non-degenerate tuned cancellations were not excluded (`REPORT.md:190-203`).  None of these gaps makes the model safe without a price; they prevent promotion of the benchmark failure to a universal KILL theorem.

The audited scope is: tree-level neutral-scalar exchange; D3 in the degenerate (H/A) benchmark plus an H-only spot check; D6 flavour couplings but not a complete D6 scalar-potential proof; class S as a high-scale named-structure route; the 2007 UTfit/2010 INP operator inputs and phase conventions; low-scale Yukawas plus the stipulated uncomputed factor-0.5 bracket.  It excludes charged-Higgs boxes, loop FCNC, electroweak/direct-search constraints, a current global flavour fit, and a complete UV vacuum construction (`REPORT.md:190-203`).

## Per-item disposition

1. **S1 and S4:** S1 confirmed.  Cross-charge bilinears and the usual D3 decoupling term are forbidden.  The 0.881 TeV arithmetic is correct for one quartic source, not for the general potential.  The 0.770/1.088 TeV searches reproduce, but are not upper-bound proofs; the 8\(\pi\) optimum fails BFB.  D6 contains allowed same-charge bilinears and is not covered by the four-doublet search.
2. **Mass-basis couplings:** confirmed.  Independent values are (0.65695) for (H_0:u\leftrightarrow c) and (0.01506) for (H_0:s\leftrightarrow d).  The Higgs-basis rotation is legitimate after spontaneous translation breaking, but (H_0) itself is not the observed aligned Higgs.
3. **\(\Delta F=2\):** the degenerate-(H/A) (C_4) formula, INP rows, and B-gen/B-gen120 (M_*) values are confirmed.  The 15--43 TeV vev cancellations and their 1% fragility are genuine within that ansatz.  General non-degenerate/mixed cancellation is open.
4. **Alignment/NFC:** confirmed for the declared definite-momentum D3/B-gen field content; not a no-go against arbitrary additional fields or symmetries.
5. **Class S:** BCC and the merging of all hw1 labels with hw3 are confirmed.  The exact X2-L2 guarantee is lost and (O(1/a)) hopping is symmetry-allowed, not dynamically proved.  No protecting residual symmetry is supplied.  Dimension-four Higgs FCNC is absent, while tiny singlet-exchange FCNC and the OBS-3-loop recheck remain open details.
6. **Fixed reading:** `FCNC-PRICE` confirmed under rule 10.  Universal `FCNC-KILL` for X2 as written is not proved; “KILL level” is valid only for the tested D3 spectrum class.

## Strongest correct statement

At tree level, for the exact B-gen/B-gen120 textures realized by one electroweak doublet in each of the four translation sectors and for a degenerate heavy-(H/A) D3 spectrum, exact corner conservation fixes disjoint Yukawa supports whose mass-basis images contain (|\widehat Y_{uc}|\simeq0.657) and (|\widehat Y_{sd}|\simeq0.015); the resulting (Q_4) coefficient, evaluated with the fixed 2007 UTfit/2010 INP bounds, requires untuned masses of roughly (1.3\times10^3)--(7.9\times10^3) TeV across the worker's sampled realizations and coupling bracket, while a vev cancellation can reduce selected B-gen benchmarks to 15--43 TeV only at (O(10^{-4}\!-!10^{-5})) amplitude tuning.  Exact translations forbid the ordinary cross-charge bilinear decoupling term, making TeV-scale active D3 carriers the natural perturbative outcome, but the advertised 1.1 TeV universal ceiling and universal X2-KILL theorem are not established for general BFB, CP-violating, D6, or non-degenerate mixed potentials.  The fixed result is nevertheless `FCNC-PRICE`: evasion requires named extra structure or tuning, and the concrete singlet-flavon route breaks translations to BCC, merges hw1 with hw3, and therefore forfeits X2-L2's exact light-corner decoupling unless a further unsupplied symmetry is added.
