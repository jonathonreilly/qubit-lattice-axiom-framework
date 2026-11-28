# Check: library/w125-match.md

**Verdict: FIX.** Three one-line repairs. No mathematical gap. Nothing fails.

Checked line by line by Claude (Opus 5.5), 2026-11-08, one reading.
Note at branch `claude/ym4d-hard-route` commit `f70c307da` (584 lines, Codex gpt-6-astra).
Sources read: Y = YM4_1400.tex at `2bc0658f`; CA-I and SA at `31a47c543775`.
This is one check. It is not an audit. It grants no status.

## Findings

Each finding gives the note line, the source line and a result.

1. **H-C-AVERAGE, flux matrix (1).** Note 72–81; Y 4725–4779 and 71619–71647.
   The coefficient, the row sum \(L^2\) and the column sum \(L^{-2}\) match Y.
   They match IN1 (15)'s \(W(p',p)\), IN1 161–162. The offset count matches Y's.
   CONFIRMED.

2. **Local remainder (2) and the bound (3).** Note 83–104; Y 71619–71693; IN1 (15).
   The carrier is the four-block rectangle, with no exterior layer, as in Y.
   The step from logarithms to defects gives \(|F|\le f+Cf^3\), so \(C_{\rm SO}\) absorbs it.
   The ceiling \(\varpi_L\) of IN1 (15) is the regular-branch ceiling. CONFIRMED.

3. **Cone masks (4) and the small-energy certificate (5).** Note 106–137; Y 71697–71842.
   The sets, the inclusion under one-step reads, the norms \(\|A\|_{2\to2}\le1\) and \(\|A\|_{1\to1}\le L^{-2}\),
   the constant \(\tfrac14\) and the alternative \(\tfrac12e_*\) all match Y. CONFIRMED.

4. **W1 contrapositive (6)–(7).** Note 139–169; Y 71845–71892.
   The tower, the \(6\rho\) torus condition, the radii in (6), \(\varepsilon_1=3\sqrt c\,\epsilon_t\) and \(3B_3\sqrt c<1\) match Y.
   One hypothesis is not stated. Y 71849–71851 requires aligned test partitions,
   \(\check R_t\le\check R_k\le L\check R_t\), all powers of \(L\).
   IN1's \(R_j=\lceil(\log m_j)^r\rceil_{L^{\mathbb N_0}}\) (IN1 26) is Y's \(\check R_j\) (Y 1109). It satisfies this for a high \(X_0\), by IN1 (1).
   The note uses alignment only later, at line 324.
   Note 165 says "Equivalently". The top-plaquette form is the step before (7), not its equivalent. Both follow.
   MISMATCH (a missing hypothesis, low severity). **Repair:** add the alignment hypothesis to §2. Say that IN1's \(R_j\) satisfies it. Change "Equivalently" to "Before (5) is applied".

5. **Weighted form (8).** Note 171–181; Y 76786–76808. \(\theta_t\epsilon_t^2=P_t^2\) holds by IN1 (2), since \(\epsilon_j=g_jP_j\).
   The arithmetic is right. CONFIRMED.

6. **W2 carriers and rows (9)–(10).** Note 186–207; Y 71912–71920.
   Full double blocks, crossing plaquettes, both cones (the second ending at level \(k\)), and the row identities match Y.
   Keeping the §2 top rows is needed for the level-\(t\) defect bound. Y uses those rows implicitly. CONFIRMED.

7. **Gauge energy (11) and the undefined-mean convention.** Note 209–223; Y 71920–71923, 71943–71945, 62018–62027.
   A factor equals one at an undefined mean, sitewise, as in Y 62026.
   The identity \(1-\tfrac12\operatorname{Re}\operatorname{tr}H=\tfrac12|H-1|_{\rm op}^2\) holds for SU(2) (Y 76781). CONFIRMED.

8. **Birth gauge region.** Note 225–231; CA-I 50192–50211 and 50251–50265.
   The gauge fixing lies in the complement of \(P_t'^{\sim1}\cup\widehat Y^{\sim5}\). \(Q_t\) and \(Q_1\) lie one coarse layer inside it. CONFIRMED.

9. **W2 contrapositive (12)–(14).** Note 233–286; Y 71925–71957; Y 10815–10871.
   The radius \(\varepsilon_1=3\sqrt{c_Q}\delta_k\), the bound \(B_3\varepsilon_1\le L^2c_2^{\rm elem}\), the curvature \(2B_3\varepsilon_1L^{-2}\) and the axial representative match Y.
   (13) is Y's rigidity-defect estimate exactly, with coefficient one on the coarse difference.
   \(d_T\le\sqrt{2G_Q}\) and the threshold \(2\delta_k\) match. (14) implies IN1's cited form SA 18287–18301, because \(P_Q\subset\mathfrak c^\sim\). CONFIRMED.

10. **Conversion (15).** Note 287–307; IN1 (1), (2).
    \(\theta_k\delta_k^2=(A_1/A_0)^2P_k^2\) holds by IN1 (2). \(P_k/P_t\) and \(\theta_k/\theta_t\) are bounded above and below by IN1 (1).
    The gauge coefficient is the original \(\theta_{t-1}\), as in Y 76929. CONFIRMED.

11. **Protected reads (§4).** Note 311–371; Y 71958–72093.
    The quarantine \(t\le m_\flat\), remakes strictly above \(m_\flat\), the three reads, the adapted representative and the island-absorption exclusion all match Y.
    The note claims nothing beyond the adopted class (note 369–371). CONFIRMED.

12. **W5 rows, inset and floor (17)–(18).** Note 376–409; Y 76865–76884; Y 72724–72737.
    The restored-field rows and the six-cell inset match Y. \(4M_2R_m+1<MR_m\) is Y's inequality, since IN1's \(R_m\) is Y's \(\check R_m\).
    The derivation from \(L\ge27\) and \(M\ge L^2M_2\) is right for \(M_2\ge1\). CONFIRMED.

13. **W5 regularity step (19).** Note 411–423; Y 76884–76894.
    The note calls this "the same separated-tower criterion as in §2". Under §2, a top defect below \(\zeta\epsilon_m\) gives a lifted radius \(\tfrac32\zeta\epsilon_m\), not \(\zeta\epsilon_m\).
    (19) copies Y 76886's constants. Y also drops the factor \(\tfrac32\) there.
    The note also leaves out Y 76890's torus condition. The added condition \(\zeta^2\epsilon_m^2\le2e_*\) is right; it makes (5) take its first branch.
    MISMATCH (a constant, harmless). **Repair:** use \(\varepsilon_1=\tfrac32\zeta\epsilon_m\) in (19). Require \(\tfrac32B_3\zeta<1\). Add the torus condition.

14. **W5 carrying action (20)–(21) and the two-action table.** Note 424–455; Y 76894–76906; SA 17642–17654.
    The \(x_m\) weight, the action region, the taper equal to one, and the difference between the carrying and the inner prepared action all match.
    The note writes index \(m\) for the source's \(k\) in SA 17646. This is only relabelling. CONFIRMED.

15. **W5 allocation (22) against IN1 H-C-CUT.** Note 462–474; Y 76906–76917; IN1 171 and 527.
    The arithmetic is right in both mark conventions. IN1's mark is \(P_t/2\); Y's is \(P_m\).
    Two identities are not stated. First, IN1's constant \(c_w\) is the note's \(c_{\rm cut}\) (Y's \(c_0\)).
    IN1's order (IN1 233) fixes \(c_w\) after the certificate constants and \(N_{\rm cut}\). So \(c_w:=c_{\rm cut}\) is admissible.
    Second, IN1's cut-leaf level \(t\) is the island level \(m\).
    UNCLEAR (missing identities). **Repair:** add one sentence stating both identities.

16. **Stopped weight (§6).** Note 485–499; Y 76758–76777; IN1 (1), (3).
    \(\theta_s\ge\theta_t-C_6R_t-c_5\), \(x_s\ge\tfrac34\theta_s\) and \(\upsilon\ge\theta_t/2\) are right. Here \(C_6=\overline BC_R\); the note does not define it. CONFIRMED.

17. **Overlap and floor (§6).** Note 501–508; Y 76811–76864 and 76918–76929.
    The two-cell witness, the multiplicity \(5^4\), the halo and floor, and the original-level gauge assignment match.
    The note writes \(D=5^4\). \(D\) already names \(\square^{\sim4}\) (note 139) and IN1's graph degree (IN1 157).
    CONFIRMED (notation clash). **Optional repair:** rename it \(D_{\rm ov}\).

18. **W6 payer types (table and (23)).** Note 510–535; Y 76738–76744 and 76918–76937.
    W1 is paid by Wilson energy alone. W2 is paid by Wilson energy plus \(\theta_{t-1}G\), and both payers are needed. W5 is paid by the carrying fresh-field Wilson action, not the inner mass.
    No Gaussian reserve is used. The integration reserve, W4 and kept coercivity stay open. The ledger matches Y. CONFIRMED.

19. **Scope and stopping point (§7).** Note 537–584; open-registry 226; geoh.md 371.
    GEOH-O1 is registered and owned by GEOH. No claim reaches unrestricted actual histories. CONFIRMED.

## Repairs, in order

1. §2: add the aligned power-of-\(L\) partitions as a hypothesis. Say that IN1's \(R_j\) satisfies it. Replace "Equivalently" (finding 4).
2. §5 (19): put the lift factor \(\tfrac32\) in. Add the torus condition (finding 13).
3. §5 (22): state \(c_w=c_{\rm cut}\), and that the IN1 leaf level is \(m\) (finding 15).

Optional: define \(C_6=\overline BC_R\). Rename the overlap bound \(D\).
After these repairs the note can ADVANCE without another check.
