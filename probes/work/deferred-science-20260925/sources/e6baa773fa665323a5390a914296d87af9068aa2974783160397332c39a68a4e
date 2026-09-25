# Blind PRE: microscopic mean energy, formation activity and stationarity

A bound on the **actual unrescaled microscopic Hermitian mean energy** is sufficient for a statewise transfer of the common-law energy/activity inequality. It does not imply convergence of energy expectations or compactness of the states. The sufficient estimate uses the canonical Hermitian low cluster, retains high/low coherences, and compares finite-spin and rotor **quadratic forms**, not their operator norms on electrically bounded states.

The result below is conditional on the supplied compensated microscopic law and the pinned parent theorems. Its application of the common-law energy/activity inequality is additionally conditional on the expressly supplied provisional root36 result. No root37 candidate or control was read. The prior completed ground-filling check is historical context, not new independence for that result.

## 1. Exact premises and claim

The four main sources are at revision 60c5f194d940a7bbaf1cdd545296e31d74a02f1a:

| Note stem, all with _BOUNDED_THEOREM_NOTE_2026-09-24.md suffix | SHA256 |
|---|---|
| BOUNDED_BLOCK_DIAGONAL_COMPENSATION_TARGET | f6cbeb6e0ddaa7d5a7ede3d3f3c2b7f5b22d58adeba8ef84f8aabc10599fb0f9 |
| LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT | c63db3296e5705c57693c2deb109e506f336fae4848d3ab0926d13a98929802b |
| LOCAL_PAIR_FORM_AND_GENERAL_GRAPH_MAGNETIC_DYNAMICS | 7c5bc10d0ca1127c2a1ef6f5cf9269caf6e8f023a09a061c2da0d8e033e35a7a |
| FORMATION_BALANCE_AND_UNSATURATED_DARK_STATES | 2ae8d264eaff3ab47ecf4ec41fa21178ff444546bcc2e36d885d092732e30516 |

All four complete notes were read and their live bytes compared with those exact Git objects. The provisional import is GROUND_ENERGY_AND_ORIGINAL_FORMATION_ROOT.md, SHA256 efd15929c31fb137219efb571b99fd0bc3641410f1ea857339fdde65d9128a81, with its AUTHOR_SEAL.json, SHA256 24e2131d01c9e47b9d8c684486e726ab753d7cab1962566baee13fbd5fead572. Its complete argument was read; its seal entries were not followed into its code, output or another checker's work. I use its stated inequality as a named provisional dependency, without claiming a new independent certification of root36.

Fix a finite simple bipartite physical graph, positive \(K,\delta,\kappa\), unsigned tensor hard-core matter, and the full Gauss space. Orient each edge from A to B. At integer spin \(S\), put
\[
C=S(S+1),\qquad \epsilon^2C=\delta/K.
\]

Take \(S\to\infty\) along this equality, keeping the graph and all three couplings fixed. On the **full** physical spin space, including every A-vacancy grade and every allowed matter output, use exactly
\[
H_{\epsilon,S}=\delta\epsilon^{-4}
       (W+\epsilon T_S+\epsilon^2 C_S),\qquad
L_{j,\epsilon,S}=\sqrt\kappa\,\epsilon^{-1}j_S,
\quad
\Gamma_{\epsilon,S}=\kappa\epsilon^{-2}\sum_jj_S^*j_S.       \tag{1}
\]

Here \(C_S\) is the locally gated compensation in the main source, not an arbitrary bounded compensation and not the uncompensated Hamiltonian. Both the original two resolved sign channels and the stipulated unnormalized coherent edge sum are covered. Rescaling the coherent instrument would change the premise.

On the common physical rotor P space let
\[
h=KD+\delta H_{4,\infty}^C,\qquad
D=\sum_{a\to b:q_b=0}E_{ab}(E_{ab}-q_a),\qquad
\Gamma=\kappa\sum_jB_j^*B_j.                              \tag{2}
\]

The diagonal \(D\ge0\) retains its occupancy gate. The bounded pair Hamiltonian and formation maps are those of the parents, on all matter and winding configurations. Energy in (2) is the lower-bounded form expectation; finite energy is equivalent to finite \(D\) expectation.

**Statewise sufficient theorem.** For each finite energy ceiling \(E_{\max}\), there are graph/coupling/ceiling-dependent constants, uniform in sufficiently large \(S\), such that every physical density \(\rho_{\epsilon,S}\) satisfying
\[
\mathcal E_{\epsilon,S}:=\operatorname{Tr}
          (H_{\epsilon,S}\rho_{\epsilon,S})\le E_{\max}      \tag{3}
\]

has a normalized comparison density \(\omega_{\epsilon,S}\) on the physical rotor P space with
\[
\operatorname{Tr}(D\omega_{\epsilon,S})\le C_{E_{\max}},
\qquad
\operatorname{Tr}(h\omega_{\epsilon,S})
 \le\mathcal E_{\epsilon,S}+C_{E_{\max}}\epsilon,
\]
\[
\left|\operatorname{Tr}(\Gamma_{\epsilon,S}\rho_{\epsilon,S})
       -\operatorname{Tr}(\Gamma\omega_{\epsilon,S})\right|
 \le C_{E_{\max}}\epsilon.                              \tag{4}
\]

The density \(\omega_{\epsilon,S}\) is extracted by a canonical unitary rotation for analysis; neither the physical evolution nor its actual outputs are projected away. No preparation assumption or convergence of \(\rho_{\epsilon,S}\) is required. Mixtures and inter-grade/inter-number coherences are allowed.

Let \(e_{\epsilon,S}=\inf\operatorname{spec}H_{\epsilon,S}\) and \(e_*=\inf\operatorname{spec}h\), each over its full physical space. Then
\[
e_{\epsilon,S}\longrightarrow e_*.                       \tag{5}
\]

Suppose, as a separate premise, that every normalized finite-energy common density obeys
\[
\operatorname{Tr}(\Gamma\omega)\ge
a-b\bigl(\operatorname{Tr}(h\omega)-e_*\bigr),
\qquad b>0.                                              \tag{6}
\]

Equations (4) give, uniformly over the family (3),
\[
\operatorname{Tr}(\Gamma_{\epsilon,S}\rho_{\epsilon,S})
 \ge a-b(\mathcal E_{\epsilon,S}-e_*)-C_{E_{\max}}\epsilon.
                                                               \tag{7}
\]

Replacing \(e_*\) with \(e_{\epsilon,S}\) costs an additional
\(b|e_{\epsilon,S}-e_*|=o(1)\). This is the sufficient transfer, not an assertion of equality of the two energy expectations.

## 2. Hermitian cluster coercivity

The compensation target theorem supplies a canonical unitary \(U_{\epsilon,S}=I+O(\epsilon)\), uniform in \(S\), for which \(U^*H_{\epsilon,S}U\) commutes exactly with \(W\). It also preserves physical Gauss and record number because its spectral/polar construction uses operators preserving them. This is the Hermitian Hamiltonian rotation, not a spectral rotation of the non-Hermitian no-event generator.

Write \(P=1_{\{W=0\}}\), \(Q=I-P\). On the spin P space, the exact compensation identity and the canonical fourth-order expansion give
\[
H_{\rm low}:=PU^*H_{\epsilon,S}UP
=KD+\delta H_{4,S}^C+R_{\epsilon,S},\qquad
\|R_{\epsilon,S}\|\le c\delta\epsilon^2.                 \tag{8}
\]

In particular, the second-order term is exactly \(KD\) even near the finite-spin boundary. Since \(H_{4,S}^C\) is uniformly bounded at fixed graph, \(H_{\rm low}\ge KD-b_0I\) for a fixed \(b_0\).

The integer W clusters above zero stay within \(O(\epsilon)\) of positive integers. Uniform boundedness of \(T_S,C_S\) therefore gives, for sufficiently small \(\epsilon\),
\[
QU^*H_{\epsilon,S}UQ\ge
       \frac{\delta}{2\epsilon^4}Q.                    \tag{9}
\]

For \(\sigma=U^*\rho U\), put
\[
q=\operatorname{Tr}(Q\sigma),\quad p=1-q,\quad
\sigma_0=P\sigma P,\quad x=\operatorname{Tr}(D\sigma_0).
\]

The exact Hamiltonian block diagonalization removes energy cross terms, without discarding density coherences. Equations (8)–(9) imply
\[
\mathcal E_{\epsilon,S}\ge
 Kx-b_0+\frac{\delta}{2\epsilon^4}q.
\]

Thus (3) implies
\[
x\le(E_{\max}+b_0)/K,\qquad
q\le 2(E_{\max}+b_0)\epsilon^4/\delta.                   \tag{10}
\]

If the family is nonempty, the right side can be made nonnegative by harmless enlargement of the ceiling. For large \(S\), \(p\ge1/2\). Define \(\omega=\sigma_0/p\), embedded in the common rotor P space. It has finite spin-box support and finite electric form energy. Equation (10) applies to **rotated high-cluster mass**. The bare W population of a canonically dressed low state can be \(O(\epsilon^2)\); replacing the rotated mass in (10) with that bare population would be wrong.

## 3. The exact finite-spin magnetic correction

Let \(F_{a,S}\) be the outward star map, \(M_{a,S}=PF_{a,S}^*F_{a,S}P\), and
\[
\Delta_{a,S}=\frac1C D_a,\qquad
D_a=\sum_{b\sim a:q_b=0}E_{ab}(E_{ab}-q_a),\quad
\Delta_S=\sum_a\Delta_{a,S}.
\]

Let \(\mathcal R\) be the ordered pairs \((a,c)\) with either \(a=c\) or \(a,c\) sharing a B neighbor. Write \(S_{ac,S}=F_{c,S}F_{a,S}P\). The canonical coefficient in the compensation parent has the following exact finite-spin form:
\[
\boxed{\;
H_{4,S}^C=
-2\sum_{\substack{a<c\\a,c\ {\rm share}\ B}}
        S_{ac,S}^*S_{ac,S}
-\frac12\sum_{(a,c)\in\mathcal R}
        \{M_{a,S},\Delta_{c,S}\}.
\;}                                                       \tag{11}
\]

To derive it, use \(C_0=M+\Delta_S\), so \(M^2-\{M,C_0\}/2=-\{M,\Delta_S\}/2\). On a one-vacancy word missing A site \(a\), compensation terms at \(c=a\) vanish, and the local occupancy gate kills every \(c\) sharing a B neighbor with \(a\). For the remaining distant stars it leaves \(F_c^*F_c+\Delta_c\). Orthogonality of the vacancy grades and disjoint support then give
\[
A^*C_1A=
\sum_{\text{ordered distant }a,c}S_{ac,S}^*S_{ac,S}
+\sum_{\text{ordered distant }a,c}M_{a,S}\Delta_{c,S}.
\]

The outward spin maps commute: shared destinations make both orders zero, while distinct destinations use commuting link and matter operators. Hence \(Z^*Z/2=2\sum_{a<c}S_{ac,S}^*S_{ac,S}\). The distant pair terms cancel. On distant stars \(M_a\) commutes with \(\Delta_c\), so the second distant sum cancels precisely those terms of \(-\{M,\Delta_S\}/2\). The remaining terms are (11).

This keeps the finite-spin anticommutators; they need not have a sign. Simply replacing the rotor shifts in the local pair Hamiltonian by spin shifts misses these terms.

## 4. Controlled form and loss comparison without flux confinement

For a legal unit shift \(e\mapsto e+k\), \(k=\pm1\), the normalized spin amplitude is
\[
w_S(e,k)=\sqrt{1-e(e+k)/C}.
\]

On a spin input \(|e|\le S\), its defect \(d=e(e+k)\) lies in \([0,C]\); a forbidden boundary step has \(d=C\) and amplitude zero. The elementary inequality
\[
(1-\sqrt{1-u})^2\le u,\qquad 0\le u\le1                 \tag{12}
\]

therefore also covers boundary paths.

For a fixed outward two-hop path contributing to \(S_{ac}\), both traversed links have empty B endpoints in the original P word. Their two nonnegative defects are terms in the original \(D\). The first hop does not change the other link or A charge; a shared destination is forbidden in both models. The difference of the two amplitudes is consequently bounded in squared norm by a fixed multiple of \(D/C\). Summing finitely many partial-isometry paths gives
\[
\|(S_{ac,S}-S_{ac,\infty})\psi\|
\le\frac{\sqrt2 z_a z_c}{\sqrt C}\|D^{1/2}\psi\|,
\qquad \psi\in P_S.                                    \tag{13}
\]

The spin outputs are embedded in the rotor Hilbert space here; a blocked spin path is compared with its actual rotor output, including when that output is outside the spin box. Since both two-hop maps have norm at most \(z_a z_c\), their squared-norm quadratic forms differ by at most a graph constant times \(C^{-1/2}\|\psi\|\|D^{1/2}\psi\|\).

Also \(0\le\Delta_{c,S}\le z_cI\), \(\|M_{a,S}\|\le z_a^2\), and
\[
\left|\frac12\langle\psi,\{M_{a,S},\Delta_{c,S}\}\psi\rangle\right|
\le z_a^2\sqrt{z_c/C}\,\|\psi\|\,\|D^{1/2}\psi\|.       \tag{14}
\]

Combining (11)–(14) proves, for a normalized positive density \(\nu\) supported in \(P_S\),
\[
\left|\operatorname{Tr}
       [(H_{4,S}^C-H_{4,\infty}^C)\nu]\right|
\le \frac{c_H}{\sqrt C}\sqrt{\operatorname{Tr}(D\nu)}.   \tag{15}
\]

For example, one sufficient finite graph constant is
\[
c_H=4\sqrt2\sum_{\text{overlapping }a<c}z_a^2z_c^2
       +\sum_{(a,c)\in\mathcal R}z_a^2\sqrt{z_c}.
\]

The density version follows by spectral decomposition and Cauchy–Schwarz, or directly by Hilbert–Schmidt norms. No bound on the electric fields of occupied B links is used.

The jump comparison has a similar input-side estimate. Each \(B_{ab,\sigma}=Pj_{ab,\sigma}F_aP\) first hops to a B site \(d\ne b\), then creates on the still-empty edge \((a,b)\). The first defect is in \(D\). The second uses a possibly different sign, but, for \(q_a=\pm1\) and integer \(e\),
\[
e^2\le2e(e-q_a)+1,\qquad
e(e+\sigma)\le4e(e-q_a)+2.                              \tag{16}
\]

Both links are initially empty-B links. Equations (12) and (16) give
\[
\|(B_{j,S}-B_j)\psi\|
\le\frac{c_j}{\sqrt C}\|(D+I)^{1/2}\psi\|.
\]

The finitely many original resolved or coherent path sums only change graph constants. Hence, writing \(\Gamma_S=\kappa\sum_jB_{j,S}^*B_{j,S}\),
\[
|\operatorname{Tr}[(\Gamma_S-\Gamma)\nu]|
\le\frac{c_\Gamma}{\sqrt C}
        \sqrt{\operatorname{Tr}[(D+I)\nu]}.             \tag{17}
\]

The spin/rotor maps and norms in (13)–(17) use the same supplied matter algebra and all physical output words. Neither a field-only postbirth Hamiltonian nor a special low-flux output projection has been inserted.

## 5. Mixed high/low coherences and proof of the statewise transfer

For the exactly rotated microscopic channel \(\widetilde j=U^*j_SU\), the parent expansion is
\[
\widetilde jP=\epsilon B_{j,S}+O(\epsilon^2),\qquad
\|\widetilde jQ\|\le c_j',
\]

uniformly in spin. Therefore the PP loss block agrees with \(\kappa B_{j,S}^*B_{j,S}\) up to \(O(\epsilon)\); the QQ block has norm \(O(\epsilon^{-2})\); and the PQ loss block has norm \(O(\epsilon^{-1})\). For a positive density,
\[
\|P\sigma Q\|_1\le\sqrt{pq}.
\]

The complete loss comparison, including both off-diagonal density blocks, is thus
\[
\left|\operatorname{Tr}(\Gamma_{\epsilon,S}\rho)
         -\operatorname{Tr}(\Gamma_S\sigma_0)\right|
\le c\left(\epsilon p+\epsilon^{-2}q+
                       \epsilon^{-1}\sqrt{pq}\right).
                                                               \tag{18}
\]

By (10), the three terms are \(O(\epsilon)\), \(O(\epsilon^2)\) and \(O(\epsilon)\). Dropping the coherent cross term would be unjustified, although keeping it gives a vanishing error. Equation (17), \(C^{-1/2}=\epsilon\sqrt{K/\delta}\), and normalization by \(p=1-O(\epsilon^4)\) now give the rate assertion in (4).

For energy, (8) and (15) imply
\[
\operatorname{Tr}(h\sigma_0)
\le\operatorname{Tr}(H_{\rm low}\sigma_0)+O_{E_{\max}}(\epsilon).
\]

The rotated high Hamiltonian is nonnegative by (9), so the right side is at most \(\mathcal E_{\epsilon,S}+O_{E_{\max}}(\epsilon)\). Dividing by \(p\) adds \(O_{E_{\max}}(\epsilon^4)\); the actual mean energy also has a fixed lower bound \(-b_0\). This proves the remaining assertion in (4).

For clarity, positivity also gives
\(\|\sigma-\omega\|_1\le2\sqrt q+q\), and \(U=I+O(\epsilon)\) gives \(\|\rho-\omega\|_1=O(\epsilon)\) after embedding. That auxiliary density estimate is not used to infer any moment. The form and high-band estimates above are the independent reason the one-sided energy and rate comparisons hold.

## 6. Spectral infima without a compactness assumption

Let \(e_{\rm box}(S)\) be the infimum of the rotor form \(h\) over normalized vectors in the physical P spin box. These finite spaces are nested, and their union contains the finite-support physical core. Since \(KD\) is diagonal and \(H_{4,\infty}^C\) is bounded,
\[
e_{\rm box}(S)\downarrow e_*.
\]

For large \(S\), \(e_{\rm box}(S)\) has a fixed upper bound given by one finite-support physical trial. Its minimizing vectors have bounded \(D\) expectation because \(h\ge KD-\delta\|H_{4,\infty}^C\|\). Dressing such a vector by \(U\), and using (8), (15), gives
\[
e_{\epsilon,S}\le e_{\rm box}(S)+c\epsilon.
\]

This supplies a fixed upper bound on the full microscopic infimum. Apply (4) to an actual finite-spin ground density, which exists in the finite physical spin Hilbert space. The common energy is at least \(e_*\), so
\[
e_*-c\epsilon\le e_{\epsilon,S}
                  \le e_{\rm box}(S)+c\epsilon.        \tag{19}
\]

This proves (5). No common ground eigenvector, compact resolvent, tight electric family or equality of finite-spin and rotor spectra is needed. The box approximation error \(e_{\rm box}(S)-e_*\) has no general rate asserted here. Exactly the same argument works inside a fixed allowed number sector because all rotations preserve number.

## 7. Provisional common-law application and exact microscopic stationarity

On the equal even degree-six torus \(L\ge6\), \(n=|A|=|B|\), the expressly imported root36 result gives, in a fixed number sector \(N=n+m\), for all positive \(K,\delta,\kappa\),
\[
\langle\Gamma\rangle\ge4\kappa(5n-6m)
  -\frac{4\kappa}{5\delta}(\langle h\rangle-e_m).
\]

Thus (7) has a sector version with these constants and the sector infimum, including sectors where its right side is nonpositive and supplies no useful activity lower bound.

The global root36 inequality requires its additional **fixed-graph sufficiently small \(K/\delta\)** hypothesis. Conditional on that premise,
\[
a=\frac{16}{5}\kappa n,\qquad b=\frac{4\kappa}{5\delta}.
\]

Consequently every family obeying (3) satisfies
\[
\langle\Gamma_{\epsilon,S}\rangle
\ge\frac{16}{5}\kappa n
  -\frac{4\kappa}{5\delta}
       (\mathcal E_{\epsilon,S}-e_*)-C_{E_{\max}}\epsilon. \tag{20}
\]

This includes all inter-number coherences because the imported inequality covers arbitrary normal densities, and no number pinching was imposed on the actual microscopic state.

At each finite spin the bounded total record number obeys **exactly**
\[
[N,H_{\epsilon,S}]=0,\quad [N,L_{j,\epsilon,S}]=2L_{j,\epsilon,S},
\quad
\mathcal L_{\epsilon,S}^*(N)=2\Gamma_{\epsilon,S}.       \tag{21}
\]

This is the full original generator with every channel. Every normal stationary density therefore has zero total formation activity. Zero instantaneous activity alone is not asserted to imply stationarity.

For stationary states with uniformly bounded mean energy, (20) implies
\[
\liminf_{S\to\infty}
  [\mathcal E_{\epsilon,S}-e_{\epsilon,S}]
\ge4\delta n.                                           \tag{22}
\]

The same liminf statement holds for an arbitrary sequence of stationary finite-spin states: if its energy excess has a finite liminf, use a bounded-energy subsequence attaining that liminf; if it diverges to positive infinity, the assertion is automatic. Equation (19) bounds the infima and the whole family is uniformly lower bounded. This is not an assertion that arbitrary stationary families have bounded energy.

Any microscopic state family whose actual energy excess above \(e_{\epsilon,S}\) tends to zero has
\[
\liminf\langle\Gamma_{\epsilon,S}\rangle
    \ge16\kappa n/5>0.
\]

In particular, every microscopic ground density is nonstationary for sufficiently large spin in this conditional parameter regime. The uniformity in (4) ensures this statement is over all ground densities, not a selected pure or nonnegative eigenvector.

The order is: fix the finite graph; for the global corollary select fixed positive \(K,\delta,\kappa\) satisfying the provisional small-ratio premise; then take \(S\to\infty\) with the exact \(\epsilon\) relation. There is no joint weak-coupling/volume limit, volume-uniform threshold, or global conclusion at arbitrary \(K/\delta\).

## 8. Preserved counterexamples and limits of the bridge

**Bounded microscopic energy does not imply energy convergence.** Take a fixed finite-support physical low vector \(\psi\) and a unit vector \(\chi\) in an available positive W grade \(r\). At large spin use their exact canonical dressings and the mixture with high weight \(p_\epsilon=\epsilon^4\). Its density tends to \(|\psi\rangle\langle\psi|\), but its high contribution to mean energy tends to \(\delta r\), since the high block is \(\delta\epsilon^{-4}(rI+O(\epsilon^2))\). Its energy remains bounded. A coherent superposition with high amplitude \(\epsilon^2\) has the same energy mechanism. The rate cross term is still \(O(\epsilon)\), as (18) requires.

**A bare P energy or density estimate is insufficient.** On the physical square, the zero-electric all-A-plus basis state has exact microscopic mean energy \(4\delta\epsilon^{-2}\) and microscopic rate zero. Its canonical dressing is \(O(\epsilon)\) close in norm, has limiting mean energy \(-4\delta\), and limiting rate \(8\kappa\). The actual microscopic energy bound (3) excludes the bare state. Neither bare P support nor density convergence supplies that bound.

**Electric tightness fails even for stationary zero-energy families.** On a fully occupied physical word, \(W=T_S=C_S=j_S=D=0\). Choose a fixed legal full-occupancy charge assignment and a reference Gauss flow, then add increasing integer circulation on a cycle while increasing the physical spin box. Each basis density is an exact microscopic stationary zero-energy state; distinct electric words are mutually orthogonal. Such a sequence has no trace-norm-convergent subsequence. These full-occupancy assignments exist on the specified even cubic tori. The square control supplies a smaller explicit instance. No compactness inference from (3) is used in the proof.

**Operator convergence on D-bounded inputs also fails.** A concrete general-graph example is \(K_{3,3}\), with A charges all plus and B charges \((+,-,0)\). In row-major A-to-B edge order take
\[
E=(t-1,1-t,0,\;-t,t,0,\;0,0,0),\qquad t=\lfloor S/2\rfloor.
\]

This satisfies Gauss and has \(D=0\). There is only one vacant B site, so the entire rotor pair Hamiltonian vanishes in this P number sector. Send the charge at A0 to vacant B2 and return the old plus charge at B0. The resulting word has \(D=2t^2\). In (11) all A stars are nearby, and the input has \(\Delta=0\), so the corresponding finite-spin coefficient is
\[
-\frac{t^2}{C}\sqrt{1-\frac{t(t-1)}C}
   \longrightarrow-\sqrt3/8.
\]

Thus \(\|(H_{4,S}^C-H_{4,\infty}^C)\psi_S\|\) need not vanish even though \(\langle D\rangle_{\psi_S}=0\). This does not contradict (15), which is a statement about the quadratic form on the same input density. The counterexample explains why a claim of uniform operator convergence would be an invalid strengthening of the proof.

If a bounded-energy microscopic family additionally converges in trace norm, the comparison densities have the same limit, the rate converges by boundedness of \(\Gamma\), and the common form energy is lower semicontinuous. This still supplies only a one-sided energy statement, not equality of means. No such limiting density is assumed in (20)–(22).

The theorem is instantaneous and conditional on the actual mean-energy ceiling; it does not prove that a time-evolving microscopic family preserves that ceiling. It transfers a ground/stationarity constraint without a limit of stationary densities. It does not provide convergence of unbounded powers, energy variances, energy derivatives, a persistence time, heat or work, a physical reservoir, a measured vacuum, masses, or empirical exclusion. A prepared nonequilibrium state remains a distinct physical identification route. No additional axiom or field-only dynamics has been adopted.

## 9. Own evidence, failed attempt and verification scope

primitive_control.py was written from the charge/electric primitives. Its final source SHA256 is 412d728fbf1137454311dd3e55d68c49ee49c5a1df120c3ed350ff53d99071a5. At spin one all allowed normalized ladder amplitudes are exactly one, so its primitive Gauss paths, compensation and fourth-order matrices use exact integers and fractions. It compares the parent's canonical coefficient with independently assembled (11) on 51 physical columns across a square, a three-star tree with a distant pair, and \(K_{3,3}\). It covers both negative-charge placements, spin boundaries, D-zero and D-positive words, and the cancellation of a distant pair. All 13,035 primitive output Gauss checks pass. Dropping the finite-spin correction fails on retained cases.

The same program checks 556 integer sign/flux cases across seven spin values for (16) and the allowed defect range. Eight additional rows evaluate the exact fractional prefactor and square-root weight of the displayed unconfined-flux counterexample; those floating amplitudes are evaluations of the analytic formula, not a fresh many-body path enumeration at those larger spins.

Attempt01 failed before producing scientific rows because an edge pair was unpacked as a triple. Its complete source, empty stdout, traceback and receipt remain in primitive_attempt01/. Attempt02 fixed that one line and succeeded. Attempt03 added six nonzero-D/circulation cases; all 45 earlier rows are unchanged. Both diffs and all three complete attempts are preserved. The final primitive output SHA256 is 7066541369da5efc342e407e6205712694baffdbad22f6cd0a0f8103a3807c9f; its true execution was 0.12205154192633927 seconds, exit zero, empty stderr.

microscopic_control.py, SHA256 74fc088937a5af5adb482b313807c835f8deefd323f9c230aa021365c48e231c, separately constructs the complete physical square \(N=2\) and \(N=4\) spin spaces for \(S=4,8,12,16,24\), with \(K=\delta=\kappa=1\). It implements the original microscopic Hamiltonian and all resolved/coherent channels, constructs the canonical low isometry, and compares it with the spin target and rotor compressed forms. It retains five full rows and 20 mixed-state/coherence rows, as well as the bare/dressed and escaping-flux diagnostics. This is a small finite floating control, not a degree-six test of the provisional root36 inequality.

Its sole run took 0.13716625003144145 seconds, exited zero and had empty stderr; complete output SHA256 is 4e7914448941be58c6b705724a118a158830c6b1171a9c39b89259b39e222d6a. At \(S=24\), the actual ground rate is about 7.98313 against common rate 8; the rare high component still contributes about 0.501309 energy, despite high weight about \(1.38889\,10^{-6}\). These are diagnostics, not fitted constants or asymptotic proofs. A computed rotated high weight as small as \(-5.33\,10^{-15}\) is retained floating roundoff around the exactly zero value for a low-cluster eigenvector, not a negative physical probability.

All complete source arguments and all scientific rows were read. No parent or author scientific program was opened, imported or executed; no other checker or root37 packet was accessed. The source/evidence manifest, full execution logs, repairs and exact hashes are sealed separately. The supporting scripts test decisive algebra and finite realizations; the uniform estimates, spectral conclusion and common-law conditional transfer are proved above, not inferred from PASS labels.
