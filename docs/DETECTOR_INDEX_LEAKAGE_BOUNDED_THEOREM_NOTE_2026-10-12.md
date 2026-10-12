---
claim_id: detector_index_leakage_bounded_theorem_note_2026-10-12
claim_type: bounded_theorem
claim_scope: "For supplied microscopic finite-range H/current implementations and a fixed common-q selected scattering range, the index defect gives explicit positive finite-energy complement weight, two-state operator-to-vector bounds, an optional finite-block defect bound and selected-detector zero-atom bounds. No model, numerical local witness, all-channel no-go or physical readout probability is constructed."
upstream_dependencies:
  - compact_patch_scattering_covariance_bounded_theorem_note_2026-10-11
  - compact_patch_fock_isometry_bounded_theorem_note_2026-10-12
  - compact_detector_convergence_bounded_theorem_note_2026-10-12
  - detector_scattering_projection_bounded_theorem_note_2026-10-12
runner: scripts/detector_index_leakage_2026_10_12.py
cross_pr_dependencies:
  - pr: 9485
    revision: b8402c17d337f371c0c73696ef170727de9ab5bd
    role: required_partial_factor_index_proof
    status: provisional_unmerged
    source_sha256: bccf07d0ca041c9c0585beccb912ac35e1da12deadae3c50efb78d439cb9b441
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: upstream_support
reachability_to_target: partially_closes
conditional_surface_status: "Selected common-q scattering complement and detector-kernel estimates under supplied microscopic implementations"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# Finite-energy complement weight from the index and centre mechanism

**Conditional bounded theorem, 2026-10-12.** A separate complete source reconstruction supports L1–L26 and optional L27 at their stated hypotheses, with no required correction. The supervisor proposed the mechanism and is a coauthor, not its independent reviewer. No applied audit verdict or retained status is conferred. Physical implementations and the selected common-q scattering setting remain supplied conditions.

The checked shift obstruction already forces the selected scattering space to be proper under these conditions. No exhaustion condition EX is needed. More usefully, if \(U=V_{qe_b}\) and \(C\) is local, then
\[
\boxed{\quad
\|(1-P_{\rm sc})\mathbf1_{[m,E]}(H)C\Omega\|^2
\ge
\left[\frac{\|(U-1)C\Omega\|^2}{4}
      -\frac{\|HC\Omega\|^2}{E^2}\right]_+ .
\quad}                                                    \tag{L1}
\]
There exists a local \(C\) with nonzero numerator. Every sufficiently large finite \(E\) therefore has positive complement weight. The already reviewed detector range theorem makes this a lower bound on the zero spectral atom of any admissible positive sum of detectors for the selected sector. A new detector-family coverage theorem is unnecessary for that inequality.

The existence conclusion is the contrapositive of N1's conditional completeness-to-shift argument. It is not a new universal lattice no-go. The added content is the explicit vector estimate, the local energy bound and cutoff quantifiers, the operator-defect conversion with its state-preparation cost exposed, and an optional finite-block lower bound from the existing quantitative index theorem. No explicit physical local witness, numerical defect value, detector frame bound, all-channel classification, or physical realization is constructed.

## 1. Exact sources and what is being reused

S denotes the original research collection. The [complete milestone packet](../.claude/science/physics-loops/toe-detector-index-leakage-20261012/) preserves the full frozen proof, sources, separate review, controls and failures; EVIDENCE_MAP.json gives exact recovery. The required partial-factor index proof is a provisional cross-PR dependency in [PR #9485](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/9485), head b8402c17d337f371c0c73696ef170727de9ab5bd. Its complete original source and review are preserved here; it is not assumed present on main. In-branch inputs are [compact creators](COMPACT_PATCH_SCATTERING_COVARIANCE_BOUNDED_THEOREM_NOTE_2026-10-11.md), [Fock isometry](COMPACT_PATCH_FOCK_ISOMETRY_BOUNDED_THEOREM_NOTE_2026-10-12.md) and [detector convergence](COMPACT_DETECTOR_CONVERGENCE_BOUNDED_THEOREM_NOTE_2026-10-12.md). The [selected projection](DETECTOR_SCATTERING_PROJECTION_BOUNDED_THEOREM_NOTE_2026-10-12.md) is used only for optional L27. Science authority remains a13caa4885f547c8d206265b031ba7649e539fd9 and planning3a4b2c66a1ead7a1c48b4359627e968f681e3c39. Author acquisition and concurrent publication records remain frozen in the packet.

| Source in S, unless noted | SHA-256 | Used content |
|---|---|---|
| INDEX_TO_PHYSICS_NEXT_OBLIGATION.md | cb512af29397a3a6e8c58161bbe1dd6c15e61944b5f8bdd9ae0c1a0cc53c2536 | Complete assessment, microscopic identification and EX boundary |
| APPROXIMATE_PARTIAL_FACTOR_INDEX_PROBE.md | bccf07d0ca041c9c0585beccb912ac35e1da12deadae3c50efb78d439cb9b441 | Complete P1–P15; P8/P10/P11 supply the conditional shift obstruction and the constants used in §7 |
| APPROXIMATE_PARTIAL_FACTOR_INDEX_REVIEW.md | 9118707fdcc85cdfd0a1160598872fb8544a9de757b3a1efe8e93292719c533c | Complete source-bound independent review; does not certify N1's physical premises |
| COMPACT_PATCH_SCATTERING_COVARIANCE_PROBE.md | d1d8ace7a450e0c00d780443f83a333223fff395b170994a83e1b65653302a4a | Complete construction; S1–S4 and (29)–(30) |
| COMPACT_PATCH_SCATTERING_EX_PUBLICATION_REPAIR.md | d4aac1e14a20e82be994bd4b8de966f0063affcbaa22a40a173b126f77fa3516 | Explicit unique vacuum and positive gap for EX |
| COMPACT_PATCH_SCATTERING_COVARIANCE_REVIEW.md | 924b2fa9d6175bcbc213d164da6322d3fde0d769f06a5608d4aadc1644f974be | Complete review of the core construction and the separate EX wording issue |
| COMPACT_PATCH_FOCK_ISOMETRY_PROBE.md | 9bc3a309e8fc35978bcac0c360b8557fb6a3c4484cfc2034a277a94072369404 | Complete proof; F1/F2/F20 identify the selected closed range and its time/centre covariance |
| COMPACT_PATCH_FOCK_ISOMETRY_REVIEW.md | bc88af1dda77065d8806da9d689546547f40847a340177086793dab5f3a277cf | Complete review at those conditional premises |
| COMPACT_DETECTOR_CONVERGENCE_PROBE.md | bed0584922876c64de1658f3135390420b703dd661edf5076e02a0a36af34d64 | Complete C1–C28; C25–C28 give positive detector limits with selected scattering range |
| COMPACT_DETECTOR_CONVERGENCE_REVIEW.md | 2f9ebfed745c217d97750ddc5f7a5edeaffaede72895ad0da1af0974ef2c51f0 | Complete independent review; ND and EX are not supplied |
| C4_N1_report.md, frozen source copy | c284a41bfee8a1238643330ddd46f3a7c4f6f1a865509a9aaec5ab6f4238ad13 | Complete report read; only its explicit setting, Step 1 and exclusions are used |
| C4_B1_report.md, frozen source copy | 95044a142cf94ad397c5f7b2bdf806905d2f40bb166fb8d5920fb5daf54a7a0e | Complete Theorem U/first-moment context; its bounded-sector argument is not a premise here |
| C4_M1_report.md, frozen source copy | fb2d6b5f54fcff8680219dce5f903d6620e5f987d4f093462502dc3e600b1b2b | Complete T3 and nearby scope; its assumed scattering convergence is not silently imported |

The N1/B1/M1 copies are those specified by the assessment, originally under S/partial_factor_review/frozen/sources/. The checked partial-factor theorem is reused at its stated mathematical scope; this author did not independently reconstruct RWW/NSY or rerun the earlier source controls. Source hashes establish identity, not proof. The new estimates below are supplied in full.

The optional §9 input is DETECTOR_SCATTERING_PROJECTION_PROBE.md, 330 lines, SHA-256 91c561d9d24d27bd4c5be26f0f688553d3d690df51766c9f6de5ec70f3ed38b4, with freeze receipt 41e516aec74bd86d28702f5c079522f9ba8c91422eb660021190a241de176b72. It was read at that frozen revision as a provisional conditional source. Its separate checker was pending when provided. Nothing through §8 depends on its new coverage claim. Publication update: its separate review is complete, SHA d9ab71d88615c78cb49eda7cc85ff263d65c12be6cc6e019314cd96eb42a20a2, receipt1fed9654096e0c67535640f60c1f1c318ac313c1436d84a21c4544b744f6ce3b. The leakage checker separately verified the chosen-family applicability; the conditional statement in §9 remains unchanged.

## 2. Precise conditional setting

The result concerns the following matching hypotheses, not their derivation from the framework axioms.

1. \(\mathcal A\) is the quasilocal full qubit tensor-product algebra on \(\mathbb Z^d\), with \(d=2\) or \(3\), and geometric translations \(\tau_x\). The vacuum GNS representation \((\pi,\mathcal H,\Omega)\) is nonzero and cyclic, with \(\|\Omega\|=1\). Suppress \(\pi\) after stating implementer identities. The UHF algebra is simple, so this representation is faithful.
2. The physical-time interaction has finite range and
   \[
   J_H:=\sup_x\sum_{Z\ni x}\|\Phi_H(Z)\|<\infty,\qquad
   \alpha_s^H=\operatorname{Ad}e^{isH},\quad H\ge0,\quad
   \ker H=\mathbb C\Omega,\quad
   \operatorname{spec}H\subset\{0\}\cup[m,\infty),\ m>0.       \tag{L2}
   \]
   This is the actual microscopic implementation in the invariant vacuum GNS representation. The interaction norm is the sum over finite sets containing a site, without a hidden cardinality or volume normalization.
3. For one lattice direction \(b\), \(P_b\) is the actual generator of a translation-invariant finite-range uniformly bounded current interaction. Its microscopic flow is
   \[
   \alpha_s^{P_b}=\operatorname{Ad}e^{-isP_b}.
   \]
   The implementers \(H,P_b,T_x\) strongly commute where appropriate and fix \(\Omega\). A formal first-moment sum or Lie bracket is not this implementation premise. Put \(\beta>0\), choose the common positive integer \(q\), and define
   \[
   t_*=q/\beta,\qquad U=V_{qe_b}=e^{it_*P_b}T_{qe_b},
   \qquad \gamma=(\alpha_{t_*}^{P_b})^{-1}\tau_{qe_b}.
                                                               \tag{L3}
   \]
   Then \(U\Omega=\Omega\), \(U\) commutes with every spectral projection of \(H\), and
   \[
   \pi(\gamma(A))=U\pi(A)U^*.                              \tag{L4}
   \]
   The generator is \(P_b\) at time \(q/\beta\), not \(P_b/\beta\) at that same time.
4. \(P=P_{\rm sc}\) is the projection onto the closed outgoing scattering range over the fixed finite mass/centre selection F2 of the Fock source; the vacuum is included. Every selected one-particle component obeys \(V_{qe_b}=1\) as an operator, including multiplicity spaces. The independently reviewed creator and Fock covariance imply
   \[
   UP=P,\qquad [P,e^{isH}]=0\quad(s\in\mathbb R).           \tag{L5}
   \]
   It is enough to supply any declared closed constructed scattering span with these two properties. No claim about unspecified additional channels is then gained. Write \(Q=1-P\).
5. When detectors are mentioned, each is an admissible selected-sector arrangement satisfying the reviewed detector source's full operator transfer, convex velocity separation and energy-only vacuum-remainder conditions C25–C28. No all-channel or common-kernel premise is added.

Integrated Poincaré and first-moment covariance are one proposed upstream route to these premises. The estimates themselves use precisely L2–L5 and the matched shift-index theorem; they do not need to infer them from formal commutators. EX is neither assumed nor used.

## 3. Index nontriviality and the local cyclic witness

If \(\gamma=\mathrm{id}\), (L3) gives
\[
\tau_{qe_b}=\alpha_{q/\beta}^{P_b}
\quad\hbox{on all of }\mathcal A.                         \tag{L6}
\]
This is exactly the full-algebra identity excluded by P8/P10/P11 of the reviewed partial-factor theorem for fixed nonzero q and fixed microscopic current interaction constants. The tube flow has index zero; its composition with the shift has index \(qL^{d-1}\log2\), incompatible with the proved vanishing normalized interior bound. Hence \(\gamma\ne\mathrm{id}\). This application has the same qubit algebra, finite-range current, finite time, and uniform constants as that theorem.

Faithfulness and (L4) imply \(U\ne1\). Cyclicity now supplies the required local witness:
\[
\exists C\in\mathcal A_{\rm loc}:\qquad
d_C:=\|(U-1)C\Omega\|>0.                                 \tag{L7}
\]
Indeed, if the bounded operator \(U-1\) killed every local \(C\Omega\), it would kill their dense linear span and be zero. Local linear combinations remain local in the finite union of their supports. This does not say that every local observable on which \(\gamma\) acts nontrivially has nonzero vacuum defect. The vacuum need not be separating.

By (L5), \(P(U-1)=0=(U-1)P\). Thus the nonzero vector
\[
\chi_C=(U-1)C\Omega
\]
already lies entirely in \(Q\mathcal H\). In particular \(P\ne1\). This is the existing N1 contrapositive in its selected-sector form; index nontriviality does not construct C or a physical model satisfying all the hypotheses.

## 4. The universal defect-to-complement estimate

Because U is unitary and fixes \(P\mathcal H\) pointwise,
\[
(U-1)=(U-1)Q,\qquad
(U-1)^*(U-1)\le4Q.
\]
Consequently, for every \(\psi\in\mathcal H\),
\[
\boxed{\quad \|Q\psi\|^2\ge\tfrac14\|(U-1)\psi\|^2.\quad}  \tag{L8}
\]
The factor \(1/4\) is optimal on these abstract hypotheses: take \(U=-1\) on a complementary line. Fixed vectors can also occur inside \(Q\mathcal H\), so zero U-defect does not imply zero complement weight. No converse lower bound on defect in terms of all complement weight is asserted.

These are norms of GNS vectors. Their interpretation as a physical readout probability would require its own observable/state bridge; this note supplies no Born-rule or Record readout identification.

## 5. Local energy domains and finite spectral windows

For \(C\in\mathcal A(X)\), X finite, the microscopic generator is
\[
\delta_H(C)=i\sum_{Z:Z\cap X\ne\varnothing}[\Phi_H(Z),C].
\]
The sum is norm convergent; finite range even confines it to finitely many finite subsets. The stated \(J_H\) gives
\[
\|\delta_H(C)\|
\le2\|C\|\sum_{Z:Z\cap X\ne\varnothing}\|\Phi_H(Z)\|
\le2J_H|X|\|C\|.                                        \tag{L9}
\]
For finite volumes containing the finite-range neighborhood of X, the finite-volume derivative at C is exactly this same \(\delta_H(C)\). Finite-volume Duhamel and the microscopic norm thermodynamic limit, uniform on compact time intervals, give \(\alpha_s^H(C)-C=\int_0^s\alpha_u^H(\delta_H(C))\,du\) in norm. Point-norm continuity therefore proves the needed norm derivative. Since \(e^{isH}C\Omega=\alpha_s^H(C)\Omega\), the generator definition gives
\[
C\Omega\in\operatorname{Dom}H,\qquad
iHC\Omega=\delta_H(C)\Omega,\qquad
h_C:=\|HC\Omega\|\le2J_H|X|\|C\|.                        \tag{L10}
\]
This is the physical-time interaction norm, not the momentum-current norm used for the index argument.

For finite \(E\ge m\), set \(F_E=\mathbf1_{[m,E]}(H)\) and \(G_E=\mathbf1_{(E,\infty)}(H)\). The unique vacuum and gap imply \(1=P_0+F_E+G_E\), with \(P_0=|\Omega\rangle\langle\Omega|\). Because \(QP_0=0\) and \(Q\) commutes with these projections,
\[
\|QF_EC\Omega\|^2
=\|QC\Omega\|^2-\|QG_EC\Omega\|^2
\ge d_C^2/4-\|G_EC\Omega\|^2.
\]
Spectral calculus and L10 give \(\|G_EC\Omega\|\le h_C/E\). This proves (L1). Thus, for the existential witness in L7,
\[
E>2h_C/d_C\quad\Longrightarrow\quad
\|QF_EC\Omega\|^2>0.                                    \tag{L11}
\]
The threshold is at least m: \(h_C\ge m\|QC\Omega\|\ge md_C/2\). Any \(E>4J_H|X|\|C\|/d_C\) is a sufficient, possibly larger choice. These are conditional thresholds after C and its defect are known; index alone supplies neither value.

A second analytic check uses the additional strong commutation of U with H:
\[
d_{C,E}^2:=\|(U-1)F_EC\Omega\|^2
=d_C^2-\|(U-1)G_EC\Omega\|^2
\ge d_C^2-4h_C^2/E^2,
\]
and then applies L8 to \(F_EC\Omega\). This reproduces (L1) with the same coefficient. These two derivations are author checks by different projection decompositions, not a separate independent review.

Also \(\chi_C\in\operatorname{Dom}H\), with
\[
\|H\chi_C\|\le2h_C.
\]
For any E with \(F_E\chi_C\ne0\), its normalization is a unit vector in \(F_EQ\mathcal H\). It has compact energy support and pure complement weight one. Its existence does not make the projected vector a strictly local excitation operator.

For every \(0<\varepsilon<1\), sufficiently large finite E gives \(d_{C,E}^2\ge(1-\varepsilon)d_C^2\). A useful stronger existential statement is that for every \(0<\varepsilon<1\) there are some local D and some finite E for which the normalized \(F_ED\Omega\) has complement weight exceeding \(1-\varepsilon\): first choose a unit vector in nonzero \(F_EQ\mathcal H\), then approximate it by local cyclic vectors and apply the contraction \(F_E\). No uniform local norm, support radius or choice algorithm follows from cyclicity.

Finally, partition \([m,E]\) into N disjoint Borel intervals \(J_k\) of diameter at most \(m/8\), with the last endpoint assigned exactly once. Orthogonality gives at least one k with
\[
\|Q\mathbf1_{J_k}(H)C\Omega\|^2
\ge \frac1N\left[d_C^2/4-h_C^2/E^2\right]_+.             \tag{L12}
\]
This produces a narrow finite energy window without assuming spectral boundary sets have zero measure. It is suitable for the optional projection theorem, whose windows have diameter less than m/4.

## 6. What an operator-norm defect does and does not control

For local A,B, write \(D_A=\pi(\gamma(A)-A)\), \(a=\|A\|\). The exact ordered identity is
\[
D_AB\Omega
=(U-1)AB\Omega+UA(U^*-1)B\Omega.                        \tag{L13}
\]
It yields
\[
c_{A,B}:=\|D_AB\Omega\|
\le2\bigl(\|QAB\Omega\|+a\|QB\Omega\|\bigr),              \tag{L14}
\]
and hence
\[
\|QAB\Omega\|^2+a^2\|QB\Omega\|^2\ge c_{A,B}^2/8.        \tag{L15}
\]
Both terms in L13 are necessary. In particular an estimate for AB alone is unavailable from this identity.

Faithfulness gives \(\|D_A\|=\|\gamma(A)-A\|=:\Delta_A\). If \(\Delta_A>0\), for every \(0<r<\Delta_A\), cyclicity supplies a local B with \(\|B\Omega\|=1\) and \(c_{A,B}>r\): approximate a unit vector on which \(D_A\) has norm exceeding r by normalized local cyclic vectors. This argument does not bound \(\|B\|\), its support or its energy moment.

For \(W(C)=\|QC\Omega\|^2/\|C\Omega\|^2\) when \(C\Omega\ne0\), (L14) gives
\[
\max\{W(B),W(AB)\}\ge c_{A,B}^2/(16a^2)>r^2/(16a^2).
                                                               \tag{L16}
\]
A zero AB vector is omitted. Indeed \(\|AB\Omega\|\le a\), so the right side of L14 is at most \(4a\max\{\sqrt{W(B)},\sqrt{W(AB)}\}\). This is an existential state-norm conversion with an uncontrolled preparation cost, not a lower bound on \(\|D_A\Omega\|\).

For finite \(E\ge m\) use L10 for B and AB, and set \(r_E=(h_{AB}+a h_B)/E\). Splitting each U-defect into vacuum, \(F_E\) and high-energy parts in L13 gives
\[
[c_{A,B}-2r_E]_+
\le2\bigl(\|QF_EAB\Omega\|+a\|QF_EB\Omega\|\bigr).
\]
Whenever \(c_{A,B}>2r_E\), at least one nonzero normalized window vector has
\[
\max\{W_E(B),W_E(AB)\}
\ge[c_{A,B}-2r_E]^2/(16a^2),                            \tag{L17}
\]
where \(W_E(C)=\|QF_EC\Omega\|^2/\|F_EC\Omega\|^2\); zero window vectors are omitted. The inequality uses \(\|F_EAB\Omega\|\le a\), \(\|F_EB\Omega\|\le1\). This keeps the missing operator-to-vacuum conversion visible even when the operator defect has an explicit lower bound.

## 7. Optional finite-block operator defect from the quantitative index bound

This section uses no state-norm comparison. It sharpens the nontriviality step at the same supplied current interaction. Use the constants and conventions of the partial-factor source P5/P11 for the current flow at \(t_*=q/\beta\): \(C_Q\), positive \(\mu,\nu\), and \(A_{\rm tail},E_{\rm bd}\ge1\). They depend on the fixed microscopic current interaction and time, not the tube width L.

For integers \(L\ge2\) and \(V=L^{d-1}\), let
\[
j=\left\lceil\mu^{-1}\log(3456C_QA_{\rm tail}L^{d+3})\right\rceil,\quad
R=\left\lceil\nu^{-1}\log(8E_{\rm bd}jL^{d+3})\right\rceil,\quad
B_L=V-(L-2R)^{d-1},
                                                               \tag{L18}
\]
using L only when \(1\le R<L/2\). Let \(\mathcal F_L\) be the full interior algebra on the 4j longitudinal slices used in P4. Define
\[
\Delta_L=\|(\gamma-\mathrm{id})|_{\mathcal F_L}\|,\quad
e_L=4E_{\rm bd}jV e^{-\nu R},\quad
a_L=4C_QA_{\rm tail}V e^{-\mu j}.                       \tag{L19}
\]
Then \(e_L+a_L\le(1/2+1/864)L^{-4}<L^{-4}\).

Let \(\gamma_L=(\alpha_{t_*}^{P_b,W})^{-1}\tau_{qe_b}\) on the tube. The P11 tail and index computations require no full-algebra shift identity: their proofs use microscopic LR plus a fixed longitudinal shift, and respectively the zero-index continuous tube path plus index additivity. The identity-error step is replaced by the triangle inequality below. Thus
\[
C_Q f_L(j)\le L^{-4}/3456,\qquad
\operatorname{ind}\gamma_L=qV\log2.
\]
For \(A\in\mathcal F_L\),
\[
\|\gamma_L(A)-A\|
=\|\tau_{qe_b}(A)-\alpha_{t_*}^{P_b,W}(A)\|
\le\|\gamma(A)-A\|+\|\alpha_{t_*}^{P_b}(A)-\alpha_{t_*}^{P_b,W}(A)\|.
\]
The already proved microscopic Duhamel estimate bounds the second term by \(e_L\|A\|\). This is the only modification of the reviewed exact-identity application.

Consequently, if \(0<\kappa\le1\), \(\kappa>e_L+a_L\), and
\[
\frac{2jB_L}{V}
+\frac{8j\kappa}{\sqrt2}
+\frac{3g(\kappa/\sqrt2)}{V\log2}<|q|,
\quad g(x)=(1+x)\log(1+x)-x\log x,                     \tag{L20}
\]
then
\[
\boxed{\quad \Delta_L>\kappa-e_L-a_L>0.\quad}           \tag{L21}
\]
Otherwise \(\Delta_L+e_L+a_L\le\kappa\le1\), and P8 applied to the tube contradicts L20. This is a proved conditional finite inequality, not an assertion that a small operator-error estimate has been measured.

Such choices exist with the same microscopic constants fixed. Take
\[
\kappa_L=\min\{1/2,\ |q|/(16\sqrt2\,j)\}.
\]
Its middle term in L20 is at most \(|q|/4\). For sufficiently large L, the sum of the first and third terms is less than \(|q|/2\), while \(e_L+a_L<\kappa_L\). Indeed \(j,R=O(\log L)\), \(B_L/V=O(R/L)\), and \(\kappa_L\) is eventually of order \(1/\log L\). Thus L21 gives a finite-block defect threshold.

The finite-dimensional unit ball of \(\mathcal F_L\) is compact, so some local \(A\), \(\|A\|=1\), attains \(\Delta_L\). Combining L21 with L16/L17 is legitimate only with the extra cyclic approximant B and its actual norm/support/energy costs. L21 alone gives no numerical vacuum defect or universal preparation-energy bound. Computing conservative tube constants and a finite-block supremum is also not a construction of the hypothesized physical model.

## 8. Detector-undetected weight from range inclusion alone

Fix a bounded energy interval \(J\subset[m,\infty)\) and put \(\Pi_J=\mathbf1_J(H)\). For each admissible arrangement \(\ell\), the reviewed detector theorem supplies positive operators
\[
0\le Q_{J,\ell}(t)\le b_\ell\Pi_J,\quad
Q_{J,\ell}(t)\xrightarrow[t\to\infty]{\rm strong}Q_{J,\ell},
\quad
\operatorname{Ran}Q_{J,\ell}\subset\Pi_JP\mathcal H,     \tag{L22}
\]
with a finite uniform bound \(b_\ell\). One may take the source's bound \(M_{L_\ell}^2\|\mathsf h_\ell\|_\infty\). These are the positive compressed coincidence expressions of C26/C28, not a claim that every finite-time ordered product is positive.

Positivity includes self-adjointness. The range inclusion and its adjoint give
\[
Q_{J,\ell}=\Pi_JP\,Q_{J,\ell}\,\Pi_JP,\qquad
Q_{J,\ell}\Pi_JQ=0.                                    \tag{L23}
\]
For any countable family with strictly positive weights, the same complement is in its common kernel. In particular define
\[
K_{J,N}(t)=\sum_{\ell\le N}\frac{2^{-\ell}}{1+b_\ell}Q_{J,\ell}(t),
\quad
K_J=\sum_{\ell\ge1}\frac{2^{-\ell}}{1+b_\ell}Q_{J,\ell}.
\]
The sums are positive contractions supported in \(\Pi_J\), with norm tails at most \(2^{-N}\). Positivity shows that \(\ker K_J\) is exactly the common kernel of its summands. On \(\Pi_J\mathcal H\), let
\[
Z_J=\mathbf1_{\{0\}}(K_J)\Pi_J.
\]
Then
\[
Z_J\ge\Pi_JQ,\qquad
\boxed{\quad
\langle\psi,Z_J\psi\rangle
\ge\|Q\psi\|^2\ge\tfrac14\|(U-1)\psi\|^2
\quad(\psi\in\Pi_J\mathcal H).\quad}                     \tag{L24}
\]
A family can be empty, in which case \(K_J=0\) and \(Z_J=\Pi_J\). Existence of a nonempty or covering family is not inferred by this inclusion.

In particular a window and local C supplied by L12 have
\[
\langle\Pi_JC\Omega,Z_J\Pi_JC\Omega\rangle
\ge\frac1N[d_C^2/4-h_C^2/E^2]_+>0.                     \tag{L25}
\]
Normalization divides every squared quantity by \(\|\Pi_JC\Omega\|^2\). The pure complement vector obtained in §5 is killed by every limit detector in that family. This is invisibility to the specified selected-sector asymptotic detectors; it is not invisibility to all observables or all possible particle detectors.

The atom also has the ordered resolvent form
\[
Z_J=
\operatorname{s-lim}_{\eta\downarrow0}
\operatorname{s-lim}_{N\to\infty}
\operatorname{s-lim}_{t\to\infty}
\eta(K_{J,N}(t)+\eta1)^{-1}\Pi_J.                       \tag{L26}
\]
At fixed \(\eta>0\), resolvent identities give strong continuity under the t-limit and a norm tail at most \(2^{-N}/\eta\). Spectral dominated convergence gives the final atom. Thus L24/L25 also lower-bound the corresponding ordered resolvent expectation. No uncontrolled simultaneous limit or uniform rate is asserted. The common kernel may contain further selected scattering vectors missed by the family.

## 9. Optional exact atom identification, conditional on the new projection proof

Only if the new frozen projection theorem in §1 is independently accepted under its actual hypotheses, for each J of diameter less than m/4 choose the family it constructs. Its P24–P30 then give
\[
Z_J=\Pi_J(1-P_{\rm sc}).                                \tag{L27}
\]
For that particular family the first inequality in L24 is equality. The defect and energy lower bounds remain inequalities. This is an optional sharpening of the observable expression, not a premise of the existence result, and not a proof of ND or EX.

Under the supplied microscopic/common-q hypotheses the selected scattering range is proper, so an assertion of ND that would detect every vector in every finite-energy window using only this selected-sector family cannot hold. That conditional consequence does not settle the framework's ND problem: a microscopic realization and correct all-channel selection have not been established, and unselected ordinary channels may account for the complement.

## 10. Failed shortcuts and positive escape routes

- **Faithfulness is not a separating vacuum.** On \(\mathbb C^3\), take the faithful defining representation of \(M_3\), \(\Omega=e_0\), \(U=\operatorname{diag}(1,1,-1)\), \(A=|e_1\rangle\langle e_2|\). Then \(\Omega\) is cyclic, \(\|\gamma(A)-A\|=2\), but \((\gamma(A)-A)\Omega=0\). Taking \(B=|e_2\rangle\langle e_0|\) reveals the defect. The other sign assignment \(U=\operatorname{diag}(1,-1,1)\) exchanges which term of L13 is necessary. These are inference controls, not lattice models of the full setting. On a product-vacuum qubit lattice, a translated local Pauli Z gives the same operator/vacuum mismatch: \(\|Z_{-b}-Z_0\|=2\), while \((Z_{-b}-Z_0)\Omega=0\).
- **A nonzero defect cannot be confined above every finite energy.** Strong spectral exhaustion forbids that for a fixed vector. It does not give an energy scale independent of the vector or microscopic H. Rescaling H rescales that cost. The explicit L10/L11 bound is the available conditional control.
- **The unique-vacuum qualification matters.** If another zero-energy vector carries \(U=-1\), U can be nontrivial while every positive-energy window has zero defect. A gap above a multidimensional ground space does not exclude this. Without a positive gap but with a unique vacuum, spectral intervals bounded away from zero still exhaust its orthogonal complement; the detector vacuum-remainder construction would need separate treatment.
- **Range alone without self-adjointness is insufficient.** \(Q_0=|e_0\rangle\langle e_1|\) has range in \(\mathbb Ce_0\) but does not annihilate \(e_1\). L23 uses the actual positive detectors.
- **Different centre spectra remain live.** Irrational centre phases or rational phases with unbounded denominators need not have one common q on a complete sector. For example, on an abstract orthogonal basis, phases \(\exp(2\pi i/n!)\) have a dense union of finite-order fixed subspaces but no single power fixing every vector. This is a kinematic diagnostic, not a microscopic realization. A union of differently selected scattering sectors may be complete even when every fixed-common-q sector is proper.
- **Incomplete selection is a concrete interpretation alternative.** The complement may contain other masses, centres, charged sectors, or non-particle excitations. The estimate does not decide which. Adding channels on which \(V_{qe_b}\) is not the identity changes the theorem's P premise. Charged-field detector constructions outside the supplied local observable class require their own covariance and range proof.
- **Missing microscopic identification is a genuine scope change.** If the integrated momentum is only formal, is not implemented by the stated current flow, has interactions outside the checked locality class, or acts on infinite-dimensional sites, the exact index theorem used here has not been matched. The statement does not exclude those possibilities. A merely abstract Fock identification without local-creator covariance likewise does not give L5; the nonlinear number-phase example in the assessment makes that distinction.
- **Neither a detector zero nor a symmetry zero proves completeness.** A family may miss scattering vectors, and U may fix vectors outside its selected scattering space. No lower detector frame bound or reverse implication was derived.

## 11. No-Go Discipline Gate at the exact conditional scope

The main artifact is a positive inequality with a conditional proper-subspace consequence. No universal physical impossibility or complete enumeration of theories is claimed.

**N1 — Distinct attack mechanisms actually examined.**

| Family and mathematical object | Attempt and result | Status/source |
|---|---|---|
| Full-algebra current/shift comparison | Allow a small but nonzero interior defect instead of exact identity; the tube comparison gives L20/L21 rather than pretending that the exact-identity theorem already had this estimate | ATTEMPTED; §7, matched partial-factor P8/P11 and its independent review |
| Cyclic representation/state conversion | Put the nontrivial algebra action in an operator annihilating the vacuum; this defeats the separating shortcut but L7/L13 use dense local cyclic vectors correctly | ATTEMPTED; §3/§6 and the explicit \(M_3\)/product-vacuum controls |
| Spectral escape to arbitrarily high energies | Try to leave all bounded windows blind to the defect; orthogonal spectral exhaustion and the local generator domain give L1/L11 | ATTEMPTED; §5, including the separate zero-energy diagnostic |
| Detector algebra/kernel | Try to retain a response on the complement despite scattering range, or cancel responses in a sum; positivity and adjoints forbid this in L23/L24, while a nonselfadjoint control shows the missing-premise failure | ATTEMPTED; §8 and reviewed detector C25–C28 |
| Scattering implementation and centre selection | Try abstract Fock phases or increasingly large rational denominators; these can avoid one global finite-order action, so they are preserved as out-of-domain escapes instead of being claimed excluded | ATTEMPTED scope test; assessment's explicit number-phase example and §10's unbounded-denominator construction |

These are five mathematical stress mechanisms, not five exhausted physical models. The supporting sources are source-reviewed conditional mathematics, not claimed retained audit authorities. No formal N-packet PASS or landing is requested by this external author probe.

**N2 — Premise relations, without an invented independent-wall count.**

| Premise bundles | Actual relation used |
|---|---|
| Microscopic current implementation / algebra nontriviality | The former plus the matched index theorem implies the latter; they are not independent requirements |
| Constructed common-q covariance / \(UP=P\) | The former implies the latter by the existing finite-packet/Fock covariance proof; no second scattering wall is counted |
| Time covariance / reducing P / spectral cutoff | Time covariance implies reducing P; unique vacuum and gap identify the particular interval exhaustion. These are a dependency chain |
| Microscopic H implementation / local energy domain | L9/L10 derive the domain and bound, rather than assuming them separately |
| Detector convergence/range / common-kernel inclusion | Reviewed C28 plus positivity implies the inclusion. New family coverage is not needed |
| New support equality / no-common-kernel ND | Equality identifies the complement; it does not prove that complement zero. It is not substituted for ND |
| Current implementation / selected particle existence, and either / physical realization | No mutual implication or independence theorem is established here. They stay explicit supplied inputs; no numerical count of independent physical walls is asserted |

**N3 — Hidden-premise scan.** The theorem's leaves are the full qubit algebra, actual H/current implementations and their norm bounds, invariant cyclic vacuum with L2, the selected covariance L5, the source-reviewed index result, and the source-reviewed detector result where used. “Common” means an operator identity including multiplicities. Faithfulness is used on algebra operators; cyclicity is used on vectors. The new projection input is marked optional. No empirical phase, law selector, diamond-norm conversion, globally regular Bloch band, vacuum separation or EX was inserted. The source scan log records the wording check; it is not mathematical validation.

**N4 — Residual match.**

| Cited witness | Its residual | Role here |
|---|---|---|
| Partial-factor P11/P29 | Full-algebra finite-time qubit shift with fixed microscopic constants | Exact match to the hypothetical \(\gamma=\mathrm{id}\) in L6; §7 supplies its own extension for nonzero defect |
| N1 §2.2 Step 1 and line 271 | Complete constructively covariant common-q scattering implies the shift identity | Same premise chain, used contrapositively; this limits novelty |
| Covariance (29)–(30), Fock F20 | Product centre action on the selected constructed range | Exact match to L5, with no onto claim |
| Detector C28 | Positive fixed-arrangement limits have selected scattering range | Exact match to L22; no coverage imported |
| B1-U and M1's bounded-sector arguments | Bounded H/P on an invariant sector | Nonmatching; not obstruction witnesses here |
| M1 T3 | One-dimensional index plus assumed scattering covariance/completeness | Historical precursor only; no replacement for the checked higher-dimensional tube argument |

**N5 — Resolution.** The estimates concern individual Hilbert vectors, local cyclic preparations, full finite interior block algebras in §7, and the quasilocal infinite-lattice automorphism under its microscopic hypotheses. A single-site expectation does not supply the block norm. No per-mode detector completeness, universal species coverage, finite-ring index or physical Record evolution is tested. The helper's five resolution lines explicitly separate finite execution from these written infinite-dimensional arguments.

**N6 — Partial closure and primitives.** The pinned primitive registry and actual minimal-axiom note were inspected. No scale reference, kinetic-form isotropy or realized-state primitive is needed by this dimensionless operator theorem or reclassified as a missing physics premise. None supplies the current implementation, particle selection or detector readout bridge. No “new axiom required” conclusion is made. Expanding an incomplete sector or deriving the actual microscopic implementation is a legitimate next mathematical/physical route; relabeling the selected P as the whole Hilbert space cannot establish EX. The existing covariance and Fock results have already retired some earlier constructive gaps, and are used at those scopes.

**N7 — Steelman.** A hostile reader should insist that “undetected” may merely mean omitted by the chosen detector menu. The strongest concrete escape is to construct additional scattering channels whose centre phases have no shared finite denominator and prove their covariance and detector range under the same microscopic model; their enlarged scattering projection may evade \(UP=P\) and exhaust the GNS space. Even before that, the current's exact microscopic implementation might fail. Those routes remain open and prevent a universal lattice or TOE no-go. They do not contradict L1/L24 for the fixed common-q selection. The terminal positive obligations are an actual microscopic realization and a justified enlarged channel construction, not another restatement of EX.

**N8 — Cross-cycle echo.** The matching history is explicit: N1's approximate tube lemma was a genuine open proof obligation, subsequently addressed by the reviewed partial-factor theorem; the local-creator covariance and Fock isometry also now have source-bound checks. Those retirements are included here. Main statement searches at a13caa48, preserved in full, found no matching defect-to-selected-complement theorem; their unrelated “defect,” “shift” and “detector cycle” hits are context only, and broad absence or literature novelty is not inferred. The present proper-subspace conclusion remains the familiar N1 contrapositive; repeating that conclusion alone would not be new progress. No claim that all alternative physical routes were closed follows from the search or these five stress families.

## 12. Evidence, remaining checks, and recovery

The analytic proof is L3–L27. The finite helper checks constants, exact matrix identities, operator-to-vacuum failure, necessity of both L13 terms, positivity/range implications, energy-domain normalization, energy-cutoff arithmetic, and finite resolvent/order diagnostics. Those controls do not prove the infinite-algebra index theorem, physical realization, analytic detector convergence or independent correctness of this author's new proof. Complete commands, outputs, source-bound mutation failures and execution metadata are preserved under S/detector_index_leakage/. The baseline execution at 01:58 UTC used a declared 60-second timeout, exited 0 in about 0.035 seconds, and preserved all output. All six copied-source mutants exited 1 at their intended assertions: the defect coefficient, either ordered identity term, the local energy factor, the high-energy subtraction, and the resolvent sign. The receipt freezes the exact note and all helper/evidence files.

Frozen author review priorities: The priority independent checks are the microscopic identification in L3/L6, the projection commutations and domain in §5, the optional quantitative tube comparison in §7, and the range-versus-coverage distinction in §8. The supervisor's original suggestion and this author's two internal derivations are not independent review. No Lean verification is asserted. Publication update: those checks are now complete in the separate report preserved below; no Lean verification is asserted.

Frozen author operational record: Only this new note and its assigned evidence directory were written. Earlier notes and receipts remain unchanged. Editable prompt files changed: none. No repository source, Git ref, PR, audit data, axiom, platform instruction or other chat was changed; no model override or subdelegation was used. The recovery surface is S/detector_index_leakage/CHECKPOINT.md. The next decision is separate source-bound review of the displayed estimates, followed by a choice between deriving a microscopic realization or extending the selected channel spectrum. Campaign deadline: 2026-10-12 16:00:52 UTC.


## Publication verification and unresolved physical inputs

The separate report has SHA fbd6bbbfe6d725b531da2d3c53e650fbcbb07c8195d7af151043d5eab14df39f,
receipt0e96c15785d6e5f74d160a5753bdd33b47f91ac5f425de809e5749ecffaa9254.
The complete reconstruction and distinct rational operator-order control froze
at02:16:57UTC, before new author control inspection. The seven-dimensional
rotating fixture checks all principal minors, including a sharp reflection,
high-energy tails, both ordered identity terms and noncommuting positive sums.
Its five JSON records cover six finite subjects; they are not six independent
proofs. The complete author baseline and all six intended mutation failures
were reproduced exactly. Two reviewer searches exited with signal9; their
partial logs support no absence or novelty assertion.

The [finite control](../scripts/detector_index_leakage_2026_10_12.py) preserves every original calculation.
PUBLICATION_EDITS.json and reconstruct.py recover the full proof and primary
from frozen bytes and declared metadata additions. No displayed mathematical
argument is changed. DELIVERY_CHECKS.md records execution and mechanical checks.
Global combined audit and strict audit lint remain independent landing gates.

The result quantifies the complement of a fixed selected common-q channel set.
It does not establish that the supplied microscopic hypotheses are realizable,
construct an effective local preparer or detector measurement probability, or
exclude an enlarged scattering theory without a common finite denominator.
No Lean certificate, applied audit verdict, physical axiom change or retained
promotion is asserted. The sole live campaign checkpoint remains in the
transport worktree; this packet is a frozen milestone.
