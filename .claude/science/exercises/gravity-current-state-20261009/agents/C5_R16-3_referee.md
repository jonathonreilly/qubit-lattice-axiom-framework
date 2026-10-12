# VERDICT: CONFIRMED WITH CORRECTIONS

The primary FIXED reading is **REFUTED** in the full stated class: Z1 is an explicit smooth subluminal law with positive \(T_{2g}\) coefficient for both displayed R9-9 vertices. Independently, Theorem B″ earns **DERIVED on its proper subclass**. These labels answer different quantifiers and should both be recorded. The corrections concern Lemma V's strict equivalence, the generality of the tuning count, the numerical range quoted for P-Z, and the meaning of “matter cone.”

1. **Z1 witness — confirmed.** I rebuilt the smooth-step law without importing the worker's modules and evaluated the original anomaly form and the integrated-by-parts form with piecewise Gauss--Legendre quadrature. At \(m=0.3\),

   \[
   \Xi_{M,T_{2g}}=+3.904715281345\times10^{-4},\qquad
   \Xi_{U,T_{2g}}=+2.810148690651\times10^{-4}.
   \]

   The two forms agree to \(3.3\times10^{-15}\) absolute and are stable under three quadrature resolutions; a direct scrambled-Sobol 3D integration independently gives \(+3.90695(84)\times10^{-4}\) for M. This reproduces the worker's signs and values. (R16-3_referee_checks.py:174-202; R16-3_referee_checks.py:239-254; R16-3_referee_checks.out:3-6; R16-3_report.md:73-103.)

2. **Subluminality — confirmed for the whole zone.** Nonoverlapping smooth transitions make \(\sigma'\) a convex interpolation of adjacent values in \(\{-1,0,1\}\), so \(\max|\sigma'|=1\). More generally,

   \[
   |\nabla\epsilon|^2=
   \frac{\sum_i \sigma_i^2\sigma_i'^2}{m^2+\sum_i\sigma_i^2}
   \leq \frac{\sum_i\sigma_i^2}{m^2+\sum_i\sigma_i^2}<1
   \quad(m>0).
   \]

   An independent whole-zone maximization gives \(v_{\max}=0.984560016681\) at \(m=0.3\), with \(\max|\sigma'|=1.000000000000\). At \(m=0\) the bound is non-strict and the box is luminal. (R16-3_referee_checks.py:105-111; R16-3_referee_checks.py:227-236; R16-3_referee_checks.out:7; C5_R14-3_report.md:43-50.)

3. **IBP identity — confirmed.** With \(g=\sigma^2\), \(f=g'/2=\sigma\sigma'\), \(A=g''/2-1\), \(\epsilon'=f/\epsilon\), and a \(k_z\)-independent vertex, periodicity gives

   \[
   0=\int\partial_z(f\epsilon^{-5})\,dk_z
    =\int\left[(g''/2)\epsilon^{-5}-5f^2\epsilon^{-7}\right]dk_z.
   \]

   Therefore

   \[
   \Xi=\frac1{32}\left\langle |V|^2\frac{5f_z^2-\epsilon^2}{\epsilon^7}\right\rangle
      =\frac1{32}\left\langle |V|^2\frac{5v_z^2-1}{\epsilon^5}\right\rangle.
   \]

   The normalization and sign also match the previously refereed Theorem T. (C5_R9-9_report.md:122-130; C5_R9-9_referee_verdict.md:7-12; R16-3_referee_checks.out:3-5.)

4. **Lemma V — application confirmed, statement needs a strictness repair.** The transverse decomposition is correct, and any open interval where \(I(B)>0\) admits a smooth symmetrized \(B_{2g}\) test vertex supported over its preimage. My independent A-form/IBP evaluations give \(I_{W08}(1)=+0.1357592587\), \(I_{W08}(1.1)=+0.0520723257\), \(I_{W14}(1)=+0.2220055534\), and \(I_{W14}(1.1)=+0.1694390632\). Thus the “negative for every rich abstract vertex” form really does fail on W08 and W14, including at \(m=1\). (R16-3_referee_checks.py:257-262; R16-3_referee_checks.out:8-11; R16-3_report.md:154-170.)

   The literal equivalence at R16-3_report.md:150-158 is not proved as written and needs a nondegeneracy qualifier: \(I\le0\) and “not identically zero” only immediately imply \(\Xi\le0\). Strict negativity for *every* nonzero smooth vertex additionally requires that no allowed vertex can be supported in the preimage of \(I=0\); this is automatic if \(I<0\) throughout the accessible interval, but not from “not identically zero” alone when \(g\) has positive flat stretches. Also, this is a richness statement about abstract test vertices, not a result that W1 realizes every such vertex; that limitation was already identified for R9-9's analogous lemma. (C5_R9-9_referee_verdict.md:14; R16-3_report.md:160-170.)

5. **Theorem B″ — confirmed, with “endpoint” read bilaterally.** On a monotone stretch incident to a gapped valley, \(|h'|\le1/\sqrt5\) makes

   \[
   5h^2h'^2-(B+h^2)\le -B<0.
   \]

   A remaining stretch joins a zero to a peak; the \(|h'|\le1\) inequality integrates to \(F(P)-F(0)=F(P)<0\), where \(F(x)=-x(B+x^2)^{-5/2}\). The finite stretch decomposition therefore gives \(I(B)<0\) for all \(B>0\), hence \(\Xi<0\) for every nonzero nonnegative \(k_z\)-independent weight. The hypothesis must cover both stretches having a gapped valley as either endpoint, not merely the left-to-right stretch “ending” there. It contains \(\mathcal U_0\) vacuously and the displayed gentle-valley law nonvacuously. (R16-3_report.md:172-191; C5_R14-3_report.md:177-182.)

6. **One simultaneous zero — confirmed; tuning claim narrowed.** An independent root solve for the M vertex at \(m=0.1\) in the \(A,C2,C\) simplex gives

   \[
   (u,v)=(0.955977637884,\,0.024523462318),\qquad
   1-u-v=0.019498899798.
   \]

   The IBP residuals are \((\Xi_{E_g},\Xi_{T_{2g}})=(4.4\times10^{-18},1.4\times10^{-17})\); the original A-form gives \((-1.0\times10^{-15},-3.5\times10^{-15})\). The law is in the simplex, has \(\max|\sigma'|=1\), and has \(v_{\max}=0.998292503599\). The local Jacobian determinant is \(8.04\times10^{-5}\ne0\), so these are two locally independent shape tunings in this family. That supports “the construction uses two tunings per edge and chosen vertex prescription,” but it is not a theorem that every possible one-parameter designed family must fail. (R16-3_referee_checks.py:265-306; R16-3_referee_checks.out:12-18; R16-3_report.md:193-227.)

   Analyticity in \(m^2\) is also correct: the anomaly vanishes on the common exact box, while wherever it is nonzero the longitudinal edge has \(g_z\ge g_*>0\), giving a uniform denominator gap around \(m^2=0\). At this common zero the independently recomputed P62 shear is \(\mu_E=+6.1917\times10^{-3}\), so it is not a triple zero. “No triple zero found” remains only a finite-family search statement, as the worker says. (R16-3_referee_checks.out:16; R16-3_report.md:220-234.)

7. **How to record the FIXED reading — REFUTED primary, DERIVED subclass.** The whole setting in the probe includes all of \(\mathcal S\), so Z1 satisfies the literal REFUTED clause and answers the title question “can any?” affirmatively. B″ independently satisfies the literal DERIVED clause on a smaller class containing \(\mathcal U_0\) and genuine gapped-valley laws. The non-misleading record is therefore **“REFUTED in \(\mathcal S\) by Z1; DERIVED on the B″ gentle-valley subclass.”** It should not be collapsed to SUGGESTED, nor should the subclass theorem overwrite the counterexample in the larger class. (TESTS.md:5087-5103; R16-3_report.md:253-267.)

8. **Prescription and price scope — confirmed with one numerical price correction.** The result is conditional on the pair-creating scalar zero-point vacuum, axial \(q\), the displayed M or U TT vertex, a \(k_z\)-independent pair vertex, an ultralocal seagull, and the **assumed rather than constructed** standard-W1 longitudinal/time completion. \(\Xi\) is the graviton shift relative to the bare cone; because the matter graviton-loop shift is excluded, “on the matter cone” here does not establish equality of fully dressed physical poles. In the empty number-conserving Fock vacuum \(\Xi=0\) trivially. (R16-3_report.md:31-46; C5_R9-9_referee_verdict.md:5; C5_R9-9_referee_verdict.md:23; C5_R11-1_referee_verdict.md:19-23.) These dynamics, source/action identification, and the supplied vacuum are downstream/open inputs rather than consequences of the minimal axioms. (MINIMAL_AXIOMS_2026-06-29.md:114-130; MINIMAL_AXIOMS_2026-06-29.md:173-190.)

   The qualitative P-Z price—sharp full-slope zigzags produce longer-range hopping—is correct, and Z1's independently computed raw coefficient is \(|\epsilon_{128}|=2.01\times10^{-7}\). But the report's quoted \(10^{-7}\)–\(10^{-6}\) range is not valid for every displayed valid zero: the \(A,C2,C\), \(m=0.1\) zero checked above has \(|\epsilon_{128}|=3.67\times10^{-5}\). (R16-3_referee_checks.out:19-20; R16-3_report.md:236-249; R16-3_report.md:280-289.)

**Strongest correct statement.** Within R14-3's smooth separable one-band class and the prescription-scoped R9-9 pair-creating scalar calculation, a whole-zone subluminal full-slope zigzag edge exists for which the bare-cone \(T_{2g}\) coefficient is strictly positive at \(m=0.3\) for both M and U, so the proposed universal negativity is refuted; convex edge mixing also gives a verified common \(E_g/T_{2g}\) zero for a chosen vertex using two locally independent shape parameters, although no simultaneous P62 shear zero is established. Conversely, if every monotone stretch incident to a positive gapped valley obeys \(|\sigma'|\le1/\sqrt5\), then \(I(B)<0\) and hence \(\Xi<0\) for every nonzero nonnegative longitudinally independent vertex, giving a genuine DERIVED subclass. Neither statement supplies the missing W1 completion, a standard/deformed W2 protection, the dressed matter pole, or the vacuum from the axioms, and the zigzag/zero laws pay nontrivial longer-range hopping tails.
