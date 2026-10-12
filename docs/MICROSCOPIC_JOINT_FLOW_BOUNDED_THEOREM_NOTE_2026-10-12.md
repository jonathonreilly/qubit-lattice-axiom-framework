---
claim_id: "microscopic_joint_flow_bounded_theorem_note_2026-10-12"
claim_type: "bounded_theorem"
claim_scope: "A finite family of supplied self-adjoint generators with bounded finite-range spin actions on the actual local cyclic domain and exact pairwise commutation there has strongly commuting spectral measures and commuting microscopic norm flows. Translation-covariant finite densities admit a complete one-site criterion and scalar-plus-local-divergence classification. No generic current conservation, integrated Poincare model or physical realization is derived."
upstream_dependencies:
  - microscopic_current_implementation_bounded_theorem_note_2026-10-12
runner: "scripts/microscopic_joint_flow_2026_10_12.py"
actual_current_surface_status: "conditional-support"
target_claim_type: "bounded_theorem"
trace_class: "upstream_support"
target_claim_id: null
target_blocker_text: "The strong joint-commutation premise of compact-patch microscopic H/current scattering constructions, once the intended model supplies the exact local identities."
source_of_blocker_text: "handoff"
reachability_to_target: "partially_closes"
artifact_role: "theorem"
next_trace_action: "Verify the full one-site conservation and cross-current identities for the intended model with actual self-adjoint generators and local actions."
conditional_surface_status: "Strong joint commutation from exact local-vector commutation and finite-range actions"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "The finite-range actions and self-adjoint generators remain supplied; exact commutation on their actual local cyclic domain is sufficient."
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# Joint microscopic flows from exact local-vector commutation

**Conditional bounded theorem, 2026-10-12; complete separate source review requires no mathematical correction.** Root contributed the proposed route. The author of this note previously reviewed the separate current-implementation lemma; that completed review does not independently review this new work. No physical axiom or audit status is supplied.

The conditional result is affirmative. For finitely many actual self-adjoint generators with the exact bounded finite-range local actions below, their pairwise commutators vanishing on every local cyclic vector imply strong joint commutation. The proof uses a mixed connected-history bound and direct unitary Taylor remainders. It does not assume that exponentials preserve the local domain or invoke an unchecked analytic-vector integrability theorem. A separate finite polynomial criterion identifies exactly what local commutation must be checked in a translation-covariant model, including cancellation by local spatial divergences.

## 1. Sources, scope and the precise target

S denotes the original research collection. The [frozen milestone handoff](../.claude/science/physics-loops/toe-regularity-joint-flow-20261012/HANDOFF.md) and [evidence map](../.claude/science/physics-loops/toe-regularity-joint-flow-20261012/EVIDENCE_MAP.json) preserve the source files, full author/reviewer evidence and their identities. The necessary prior source is the original `MICROSCOPIC_CURRENT_IMPLEMENTATION_PROBE.md`, all 399 lines, SHA-256 `bcc9b9503e49c17b6e6140c22f3971f35ccd3ed72de16f0371666dc9162dfd9a`. Its general finite-range estimate and implementation argument are I14–I29; its explicit energy-current construction is I1–I13. The completed source-bound review is `MICROSCOPIC_CURRENT_IMPLEMENTATION_REVIEW.md`, SHA-256 `305fa33efebf1e9f9dc09d0854eddf23065877004888f55e964d31cc403f6d17`, with receipt SHA-256 `1e8f868b6722ce57d60c626d3899e08f28fe6183e7aef5533a2891f96bb803fc`. They remain unchanged. Their exact source copies and identities are in `microscopic_joint_flow/sources/` and the source manifest. The actual in-branch proof uses are [Current](MICROSCOPIC_CURRENT_IMPLEMENTATION_BOUNDED_THEOREM_NOTE_2026-10-12.md): I14-I29 individual norm-flow construction and full canonical GNS implementation; I1-I13 additionally supplies the current-density application. Other historical references remain provenance only.

Main instruction authority remains `a13caa4885f547c8d206265b031ba7649e539fd9`, planning authority `3a4b2c66a1ead7a1c48b4359627e968f681e3c39`. Verified unchanged common instructions, minimal axioms and registry reads are reused from the preceding task; the physics-loop discovery, claim and delivery instructions were read for this author task. The explicit bounded dispatch controls scope: no branch, publication, audit, prompt or axiom action is part of this work. The theorem uses none of the registered scale, isotropy or realized-state primitives.

The existing compact-patch S1 requires actual strongly commuting microscopic H/current generators. The prior implementation lemma deliberately leaves that strong-commutation premise open. This note replaces it by exact polynomial commutation on the **same actual local cyclic domain**, after the local actions and self-adjoint generators are supplied. It does not prove those commutation identities for an intended physical model.

A read-only statement search of the root-reported checkout at `f6f4348151734908dea3b32048ee1f36f694035b` found 46 lines in 33 files. The relevant hits either supplied strong commutation in the scattering/detector hypotheses or used commuting diagonal electric terms; they did not provide the particular local-vector argument below. Complete search output and the limited hit disposition are saved. No exhaustive repository/literature novelty claim is made. The contribution claimed is a direct resolution of the named conditional implication.

## 2. Actual operators, local actions and domains

Let \(\mathcal A\) be the quasilocal tensor algebra of fixed finite-dimensional spin sites on \(\mathbb Z^d\), and let \((\pi,\mathcal H,\Omega)\) be a nonzero cyclic GNS representation with normalized \(\Omega\). Write \(B_L=\{x\in\mathbb Z^d:|x|_1\le L\}\) and use nonnegative integer radii. For \(j=1,\ldots,M\), where M is finite, supply a self-adjoint interaction \(\Psi_j\) with finite range and
\[
 |X|\le s_j,\qquad J_j=\sup_z\sum_{X\ni z}\|\Psi_j(X)\|<\infty,
 \qquad \delta_j(A)=i\sum_X[\Psi_j(X),A].                 \tag{J1}
\]
Terms assigned to the empty set can be discarded. Each local sum is finite. Put \(s=\max(1,s_1,\ldots,s_M)\) and \(\mathcal D=\pi(\mathcal A_{\rm loc})\Omega\). Supply actual self-adjoint operators \(G_j\) satisfying
\[
 \mathcal D\subset\operatorname{Dom}G_j,\qquad
 G_j\pi(A)\Omega=-i\pi(\delta_j(A))\Omega
 \quad(A\in\mathcal A_{\rm loc}).                       \tag{J2}
\]
These are vector equalities, not quadratic-form or formal-sum identities. Since every \(\delta_j\) maps locals to locals, J2 derives \(G_j\mathcal D\subset\mathcal D\). Thus every finite mixed operator word has domain containing D and preserves it. It also derives \(G_j\Omega=0\) by A=1. No common core, essential-self-adjointness assertion or exponential invariance of D is assumed.

The additional exact condition is
\[
 (G_jG_k-G_kG_j)\xi=0
 \quad(\xi\in\mathcal D,\ 1\le j,k\le M).              \tag{J3}
\]
The products are already justified by J2. Commutation on some other unspecified dense set, on the vacuum alone, or only as expectation values is not J3.

**Conditional joint-flow lemma.** Under J1–J3, all spectral projections of the supplied \(G_j\) commute. Their unitary groups form a strongly continuous representation of \(\mathbb R^M\). The individual microscopic norm flows commute on the whole quasilocal algebra and have these exact vacuum-fixing GNS implementations. The proof follows.

## 3. Mixed connected histories and absolute convergence

For local \(A\in\mathcal A(Y)\), \(a=|Y|\ge1\), and any prescribed ordered list \(j_1,\ldots,j_N\),
\[
 \|\delta_{j_1}\cdots\delta_{j_N}(A)\|
 \le\|A\|\,2^N\Bigl(\prod_{l=1}^N J_{j_l}\Bigr)
        \prod_{k=0}^{N-1}\bigl(a+k(s-1)\bigr).           \tag{J4}
\]
Expand the nested commutator from its innermost operation. A nonzero term at each step uses an interaction set meeting the accumulated support union. It adds at most s−1 sites, and, for the interaction used at that step,
\[
 \sum_{X:X\cap Z\ne\varnothing}\|\Psi_j(X)\|
       \le J_j|Z|.
\]
Multiply those bounds along the history tree and use a factor two per commutator. The argument counts each history's union, not the whole accessible ball. It applies to disconnected Y and to every color ordering, without commutation assumptions. It remains valid when finite-volume cutoffs delete terms. This proves J4 by a finite expansion at every fixed order.

J2 also gives
\[
 G_{j_1}\cdots G_{j_N}\pi(A)\Omega
       =(-i)^N\pi(\delta_{j_1}\cdots\delta_{j_N}(A))\Omega. \tag{J5}
\]
Contractivity of pi therefore transfers J4 to the mixed operator words on D.

For two labels j,k, set r=s−1. If r>0, the absolute double-series majorant is
\[
\begin{split}
 &\sum_{m,n\ge0}\frac{(2J_j|u|)^m(2J_k|v|)^n}{m!n!}
       \prod_{l=0}^{m+n-1}(a+lr)\\
 &\hspace{15mm}=\sum_{N\ge0}\frac{[2(J_j|u|+J_k|v|)]^N}{N!}
       \prod_{l=0}^{N-1}(a+lr)
       =(1-z)^{-a/r},\qquad
 z=2r(J_j|u|+J_k|v|)<1.                                \tag{J6}
\end{split}
Grouping by N=m+n is the binomial theorem; all summands of this majorant are nonnegative. The last identity is the rising-factorial series. Thus the common open diamond of convergence is independent of a, though its bound is not. No boundary convergence at z=1 is claimed. If s=1, replace the majorant by \(\exp(2a(J_j|u|+J_k|v|))\), valid for all finite u,v. A scalar A has zero positive derivatives. If \(J_j=0\), its derivation is zero; J2 makes \(G_j=0\) on dense D, and closedness makes the supplied operator the zero operator on all H. These cases require no division by zero.

The same multinomial argument works for any finite number of colors with \(z=2r\sum_jJ_j|t_j|<1\). Pairwise use will suffice below.

## 4. Direct comparison of actual unitary products

For a self-adjoint G and \(\xi\in\operatorname{Dom}G^N\), the spectral theorem gives
\[
 \left\|e^{itG}\xi-\sum_{l=0}^{N-1}\frac{(it)^l}{l!}G^l\xi\right\|
       \le\frac{|t|^N}{N!}\|G^N\xi\|.                  \tag{J7}
\]
For example, integrate the Nth strong derivative along the real unitary orbit: the remainder is \((it)^N/(N-1)!\) times the integral of \((1-w)^{N-1}e^{iwtG}G^N\xi\) from w=0 to 1. Its norm gives J7 for either time sign. No domain conclusion for a different generator is used here.

Fix \(\xi=\pi(A)\Omega\) and (u,v) in J6's diamond. First expand \(e^{ivG_k}\xi\) using J7 and J4, then apply the bounded unitary \(e^{iuG_j}\) to that convergent series. For each fixed n, \(G_k^n\xi\) is a local cyclic vector by J5, so its \(G_j\) Taylor series converges in the same support-independent interval. The joint majorant J6 then permits the double expansion and all rearrangements:
\[
 e^{iuG_j}e^{ivG_k}\pi(A)\Omega
   =\sum_{m,n\ge0}\frac{(iu)^m(iv)^n}{m!n!}
          G_j^mG_k^n\pi(A)\Omega.                      \tag{J8}
\]
This sequential argument never assumes \(e^{ivG_k}\mathcal D\subset\operatorname{Dom}G_j\). Only finite powers on the invariant D occur before the bounded unitary is applied.

J3 permits adjacent swaps in any finite word on D: after every intermediate factor the vector remains in D. Hence \(G_j^mG_k^n\xi=G_k^nG_j^m\xi\). Exchange m,n and the order of factors in the absolutely convergent sum. The reverse sequential expansion gives
\[
 e^{iuG_j}e^{ivG_k}=e^{ivG_k}e^{iuG_j}                 \tag{J9}
\]
on dense D and then as bounded operators, for the diamond. For arbitrary real u,v, choose integers p,q large enough that (u/p,v/q) lies in that diamond. The two small-step operators commute, so their finite powers commute. Their separate group laws give J9 for all real u,v. In the entire or zero cases the same conclusion is immediate or follows by this subdivision.

For completeness, commuting unitary groups give commuting spectral projections without any generator-domain interchange. If a bounded T commutes with every \(e^{itG}\), it commutes with every Fourier-integrable function of G. Gaussian convolution of a finite-interval indicator has an integrable Fourier transform, and its spectral strong limit is the interval projection plus half its endpoint atoms. The atom at c is the strong limit of \(\exp[-n(G-c)^2]\), also a Fourier-integrable function of G. Subtract the half-atoms to obtain each open-interval projection. Monotone limits give arbitrary interval and then Borel projections. Bounded T commutes through these strong limits. Apply this first with the other unitary group and then with its spectral projections. All \(G_j\) therefore strongly commute.

Their finite product \(U(t_1,\ldots,t_M)=\prod_j e^{it_jG_j}\) is a strongly continuous representation of the additive group \(\mathbb R^M\), independent of factor order. Any real linear combination has the self-adjoint joint-spectral generator
\[
 G(c)=\int_{\mathbb R^M}\Bigl(\sum_jc_j\lambda_j\Bigr)\,dE(\lambda),
 \quad\operatorname{Dom}G(c)=\left\{\xi:\int\left|\sum_jc_j\lambda_j\right|^2
                        d\langle\xi,E(\lambda)\xi\rangle<\infty\right\}. \tag{J10}
\]
On D it equals the finite sum \(\sum_jc_jG_j\), since D is in each individual domain. No unproved closure of a formal infinite Hamiltonian or boost sum is identified with J10. Products on their full unbounded domains are not assumed to be everywhere defined. The theorem concerns the supplied self-adjoint operators; it has not constructed them.

## 5. Algebra commutation, thermodynamic limits and phases

The prior implementation lemma's general part I14–I29 applies separately to each J1/J2 pair. To make its use explicit: connected-history Taylor bounds and finite-volume isometric remainders give a small-time norm thermodynamic limit with stabilized local coefficients. Fixed compositions of point-norm convergent isometries extend that limit to every real time and supply its group law. Self-adjoint vector Taylor remainders then identify its invariant-state canonical GNS unitary with \(e^{itG_j}\). Thus
\[
 e^{itG_j}\pi(A)\Omega=\pi(\alpha_t^j(A))\Omega,\qquad
 \operatorname{Ad}e^{itG_j}\pi(A)=\pi(\alpha_t^j(A))      \tag{J11}
\]
for every quasilocal A and real t. These individual limits are obtained before any joint-limit assertion. No claim that differently truncated finite-volume Hamiltonians commute is required. This distinction matters when their commutator is a boundary term.

There is also a useful purely local equivalence. Put \(C_{jk}=[\delta_j,\delta_k]\), a derivation on the local algebra. J5 gives
\[
 [G_j,G_k]\pi(A)\Omega=-\pi(C_{jk}(A))\Omega.             \tag{J12}
\]
If J3 holds, apply this to AB and use the Leibniz rule:
\[
 0=\pi(C_{jk}(AB))\Omega
  =\pi(C_{jk}(A))\pi(B)\Omega+\pi(A)\pi(C_{jk}(B))\Omega
  =\pi(C_{jk}(A))\pi(B)\Omega.                          \tag{J13}
\]
Density of local cyclic vectors makes the bounded operator \(\pi(C_{jk}(A))\) zero. The spin representation is faithful: every restriction to a local full matrix algebra is unital and isometric, and local norm density extends that property. Hence \(C_{jk}(A)=0\) as an algebra element. Conversely, this algebra identity implies J3 by J12. Vacuum separation is not assumed; the multiplication by arbitrary B in J13 is essential.

From commuting derivations, the algebra version of J8 is
\[
 \alpha_u^j\alpha_v^k(A)
   =\sum_{m,n\ge0}\frac{u^mv^n}{m!n!}\delta_j^m\delta_k^n(A)
   =\alpha_v^k\alpha_u^j(A)                            \tag{J14}
\]
inside the same diamond. The sequential Taylor expansion and absolute bound J6 justify it, using already constructed individual norm flows. Density and finite-power subdivision extend it to all quasilocal A and all times. This agrees with the consequence of J9/J11 and faithfulness.

Commuting adjoint actions alone can leave an implementer in the representation's commutant; in an irreducible representation that ambiguity can be a projective scalar phase. Here the canonical action and common fixed Ω remove it. By J11,
\[
 e^{iuG_j}e^{ivG_k}\pi(A)\Omega
 =\pi(\alpha_u^j\alpha_v^k(A))\Omega
 =e^{ivG_k}e^{iuG_j}\pi(A)\Omega.
\]
This is equality on a dense cyclic set, not just equality after adjoint action or on Ω. Both the direct-vector and the algebra argument give exact unitary commutation. They share the mixed estimate and are two author checks, not independent reviews.

## 6. A finite local identity criterion

Suppose now the interactions are given by translation-covariant bounded Hermitian densities \(g_j(x)=\tau_x(g_j(0))\), supported in \(x+B_{L_j}\) with norm at most \(h_j\). Define the local Hermitian commutator density
\[
 q_{jk}(x)=i\sum_{|y-x|_1\le L_j+L_k}[g_j(y),g_k(x)].     \tag{J15}
\]
Then
\[
 [\delta_j,\delta_k](A)=i\sum_x[q_{jk}(x),A],\qquad
 \operatorname{supp}q_{jk}(x)\subset x+B_{2L_j+L_k},
 \quad \|q_{jk}(x)\|\le2|B_{L_j+L_k}|h_jh_k.             \tag{J16}
\]
For the identity, let Y support A and take the finite center set \(T=Y+B_{2(L_j+L_k)}\). Put \(F_l(T)=\sum_{x\in T}g_l(x)\) for l=j,k. Both double derivations on A equal their corresponding double commutators with these finite sums: an inner k center is within \(L_k\) of Y and an outer j center is within \(L_j+2L_k\), and the reverse order obeys the reversed bound. Finite Jacobi therefore gives \(-[[F_j(T),F_k(T)],A]\). Only overlapping density pairs with at least one support meeting Y can survive. Every such pair is in T, since its other center is within \(L_j+2L_k\) or \(L_k+2L_j\) of Y. Their finite regrouping gives J15/J16. The two labels are ordered and distinct; there is no pair factor 1/2. The support and norm follow from overlap distance and the commutator norm bound. Assigning the ball of radius \(L=2L_j+L_k\) gives per-site norm at most \(2|B_L||B_{L_j+L_k}|h_jh_k\). This asymmetric density assignment need not equal the one obtained by reversing labels, although their derivations are negatives.

For **any** translation-covariant Hermitian finite local density q with \(\operatorname{supp}q\subset B_L\), a necessary and sufficient criterion for \(\delta_q=0\) is
\[
 \boxed{\quad i\sum_{|x|_1\le L}[\tau_x(q),E_0]=0
 \quad\hbox{for every member }E_0\hbox{ of a complete one-site matrix basis.}\quad} \tag{J17}
\]
Each equality is an equality of finite operators in \(\mathcal A(B_{2L})\). Terms outside the displayed center set commute with the site at zero. Necessity is immediate. For sufficiency, linearity gives the identity on the whole one-site matrix algebra; translations give it at every site; the derivation rule gives it on every finite tensor product and hence every local observable. An identity or one chosen observable alone is not a complete basis test. State expectations or vacuum columns cannot replace the operator equalities in J17.

For the previous note's energy/current densities, one may use \(L_h=R\), \(L_{p_b}=3R\), \(h_h=h\), \(h_{p_b}=h^2c_{R,b}\). Thus a sufficient explicit commutator-density radius is 5R, with
\[
 \|q_{h,p_b}(x)\|\le2|B_{4R}|h^3c_{R,b},
 \qquad J_{h,p_b}\le2|B_{5R}||B_{4R}|h^3c_{R,b}.        \tag{J18}
\]
J17 is then a finite collection of polynomial identities in \(\mathcal A(B_{10R})\). For two current components use radius 9R, test support \(B_{18R}\), and the analogous density bound \(2|B_{6R}|h^4c_{R,a}c_{R,b}\). These are conservative bounds; they are not a claim that exact conservation follows from the current formula.

## 7. Why a nonzero commutator density can still conserve

For finite local spin densities there is an exact description of the cancellation. Choose a Hermitian one-site tensor basis consisting of 1 and traceless matrices, orthogonal in the normalized trace. Expand
\[
 q=c1+\sum_w c_w w,                                    \tag{J19}
\]
where each nonidentity tensor word has finite nonempty support and nonidentity factors there. For Hermitian q all coefficients are real. For each translation orbit O of nonidentity words, let \(s_O=\sum_{w\in O}c_w\); only finitely many summands and orbits occur in q. Then
\[
 \delta_q=0
 \quad\Longleftrightarrow\quad s_O=0\text{ for every nonidentity orbit O}
 \quad\Longleftrightarrow\quad
 q=c1+\sum_{b=1}^d(a_b-\tau_{e_b}(a_b))
 \text{ for Hermitian local }a_b.                       \tag{J20}
\]

Here is a finite proof, including the potentially delicate necessity. A nonempty finite word has no nonzero translation stabilizer: otherwise its finite support would be invariant under arbitrarily large multiples of a nonzero vector. For a fixed site z, collect from the finitely many translates of q meeting z only the tensor words whose factor at z is nonidentity. Call this finite operator K_z. Its support is in \(z+B_{2L}\), and \(\delta_q(E_z)=i[K_z,E_z]\). The coefficient of any fixed word in K_z is exactly its orbit sum \(s_O\), because each original orbit member has a unique translation to that word. No infinite scalar sum or unbounded global Hamiltonian is being rearranged.

If the derivation vanishes, K_z commutes with the full matrix factor at z. Its normalized partial trace at z is also zero, because every word collected has a traceless factor there. A member of that factor's commutant is \(1_z\otimes B\); its partial trace is B. Hence K_z=0. Linear independence of the finite tensor basis forces all of its word coefficients to vanish. Choose z in the support of any nonidentity word to obtain every \(s_O=0\). The reverse implication follows from the same finite K_z coefficient calculation.

For the last equivalence, fix a reference word w in each orbit. Vanishing orbit sum writes its contribution as a finite sum of \(c_v(\tau_v(w)-w)\). Choose a finite nearest-neighbor coordinate path from 0 to v. Every positive step contributes \(-(1-\tau_{e_b})\tau_u(w)\), and every negative step contributes \((1-\tau_{e_b})\tau_{u-e_b}(w)\). The path telescopes, and collecting finitely many such terms gives local a_b. They are Hermitian since the tensor basis and coefficients are real. Conversely, each local translation difference has zero derivation: its two finite local commutator sums cancel after shifting the center label. Scalars also have zero derivation. This proves J20.

For J15 the scalar coefficient is zero because the product trace annihilates each finite commutator. Thus exact conservation can hold with a nonzero q that is a local divergence. J20 classifies finite local spin densities only; no assertion about general quasilocal densities, fermionic grading, infinite-support cohomology or physical continuity laws is made.

## 8. Discriminating examples and failed weaker criteria

**The current formula does not generically conserve.** On a one-dimensional qubit chain set
\[
 h_x=Z_xZ_{x+1}+X_x.
\]
This is translation-covariant, Hermitian, bounded and of radius R=1. The prior current formula gives
\[
 p_x=-Z_xY_{x+1}-Z_{x-1}Y_x.
\]
It has the same derivation as \(p'_x=-2Z_xY_{x+1}\), since their difference is a local translation difference. Direct Pauli multiplication gives
\[
 q'_x=i\sum_y[h_y,p'_x]
 =-4X_{x+1}-4Y_xY_{x+1}-4Z_xX_{x+1}Z_{x+2}+4Z_xZ_{x+1},
\]
and
\[
 \boxed{[\delta_h,\delta_p](Z_0)
 =-8Y_0+8Y_{-1}X_0+8X_0Y_1-8Z_{-1}Y_0Z_1\ne0.}         \tag{J21}
\]
The four tensor words are linearly independent. This exact example defeats the claim that finite range and the current formula alone supply J3. It is not a counterexample to the conditional joint-flow lemma, and no physical boost/Poincaré realization for it is asserted.

**Requiring q itself to vanish is too strong.** Already \(q=Z_0-Z_1\) is nonzero but has zero derivation. A current example is \(h_x=X_xX_{x+1}+Y_xY_{x+1}\). Write
\[
 f_x=X_xX_{x+1}+Y_xY_{x+1},\quad
 t_x=X_xZ_{x+1}Z_{x+2}X_{x+3}+Y_xZ_{x+1}Z_{x+2}Y_{x+3}.
\]
For its actual p from I6, direct algebra gives
\[
 q_0=\delta_h(p_0)=2(f_{-1}-f_1-t_{-2}+t_0)
      =a-\tau_1(a),\qquad
 a=2(f_{-1}+f_0-t_{-2}-t_{-1}).                         \tag{J22}
\]
Thus all three Pauli basis tests in J17 vanish although q_0 is nonzero. This is an exact algebraic cancellation; it does not construct the physical generators or their representation.

**Checking only selected observables or the vacuum is too weak.** For q=Z_0, \(\delta_q(Z_0)=0\) but \(\delta_q(X_0)=-2Y_0\). Also, any two finite tracial-GNS commutator generators annihilate Ω=1, so their commutator annihilates Ω even when it acts nontrivially on local cyclic vectors. The negative fixture's six-site periodic matrix control gives zero tracial-vacuum residual but nonzero local action with norm about 25.889. It tests that weakness only; it is not the infinite-volume proof.

**Adjoint actions can hide phases.** At the discrete fixed elements X and Z on a qubit, their adjoint actions commute whereas XZ=−ZX. They have no common nonzero fixed vector. This is a finite diagnostic of the projective ambiguity, not an example of two commuting continuous one-parameter automorphism groups. J2/J11 and cyclicity supply the additional exact implementation information used here.

**Finite boundaries and absolute bounds require care.** A divergence can survive as a boundary term in an open finite-volume sum. Commutation of all infinite-volume flows is proved after the individual norm limits; finite open cutoffs need not commute. Conversely, a single small periodic test can alias tensor supports and cannot replace J17 with its verified padding. A bound on each single-generator series does not by itself justify an arbitrary double rearrangement; J4/J6 provide the needed absolute joint bound.

## 9. Consequence for the supplied S1 conditions

Apply the lemma to \(G_0=H\) and \(G_b=P_b\), using the previous exact local actions and current interaction. It is enough to establish
\[
 [H,P_b]\mathcal D=0,\qquad [P_a,P_b]\mathcal D=0        \tag{J23}
\]
as actual vector identities, with products already justified. Equivalently, under those supplied actions, establish the finite derivation tests J17 for every pair. They then imply the strong joint commutation required in S1. For a common interaction cardinality bound \(s=|B_{3R}|\), one can use \(J_H\le|B_R|h\) and \(J_{P_b}\le|B_{3R}|h^2c_{R,b}\). These constants do not depend on a transverse tube width.

For \(K_b=P_b/\beta\), \(\beta>0\), strong commutation is unchanged. The joint microscopic action has the convention
\[
 \operatorname{Ad}\bigl(e^{itH}e^{-i\sum_b y_bP_b/\beta}\bigr)
 =\alpha_t^H\prod_b\widehat\alpha^{p_b}_{-y_b/\beta},    \tag{J24}
\]
where the equality is in the faithful representation before identifying algebra automorphisms. There is exactly one beta division and the current clocks remain negative. Geometric translation commutation still uses the invariant geometric implementation described in the previous lemma; this note does not construct it.

What remains supplied is substantial: self-adjoint boost and integrated momentum realizations, their exact local actions and boost closure on this D, and the local conservation/cross-current identities J23 or J17 for the intended model. Strong joint commutation is now a proved consequence **if those exact local identities hold**. Positivity, gap, particles, mass-shell/centre data, scattering, detector exhaustion, full completeness and physical identification remain separate. No integrated Poincaré model or generic energy-current conservation has been derived.

## 10. Verification and recovery

The full analytic argument was drafted before executing the controls and is preserved as `microscopic_joint_flow/ANALYTIC_DRAFT.before_controls.md`. The runner `microscopic_joint_flow/controls/joint_controls.py` uses exact Gaussian-rational binary symplectic Pauli arithmetic. Separately assembled six-site periodic Kronecker matrices compute H and the once-oriented pair current directly. The exact negative polynomial J21 agrees with that dense matrix calculation with zero residual; its action norm is about 25.888543820. The positive XX case has zero finite matrix commutator, while the tested unitary-product residuals are approximately `2.26e-16` for XX and `0.04513` for the nonconserving fixture.

The initial execution completed 37 predicates with none failed. These are execution facts, not proof grades. Mixed-color history counts depend on ordering (for a single seed, `rb` has 8 histories and `br` has 12), and the common bound covers both. Omitting support growth fails all ten selected history cases. The binomial-majorant rows only check arithmetic grouping; they cannot prove the history estimate. The vacuum-only checks are explicitly nondiscriminating, and reversing the order of the already commuting positive pair cannot expose a false universal commutation claim; the noncommuting fixture provides that discriminator.

Five actual source mutants were executed with the same 37 predicates. Reversing the current sign and omitting its half each failed three predicates; deleting support growth failed ten; reversing the Jacobi-density sign failed three; and dropping a divergence term failed one. All five completed with exit 1, as expected, and their passing, nondiscriminating rows are retained too. The baseline completed in about 0.32 seconds; each mutant in about 0.21–0.48 seconds, with a declared 60-second timeout for each run. No timeout or unintended execution failure occurred.

Complete source-mutant executions, all stdout/stderr, declared timeouts, commands, elapsed times, exits and source hashes are retained in `microscopic_joint_flow/logs/` and `mutations/`. The final checkpoint and receipt state the exact current evidence and failures. Finite controls cannot establish an unbounded domain, self-adjoint realization, thermodynamic limit or physical model. At author freeze no independent reviewer had checked this new candidate; the separate complete source review is now recorded below. No Lean formalization or external integrability theorem is claimed.

Frozen author operational record: Only this note and `microscopic_joint_flow/` were written. The prior current source/review remain frozen. No repository source, Git ref, PR, audit result, editable prompt, axiom or other chat was changed; no model override or subdelegation was used. Root is a contributor to this new author result. The fixed campaign deadline is 2026-10-12 16:00:52 UTC.


## Publication evidence and review record

The frozen author source is `MICROSCOPIC_JOINT_FLOW_PROBE.md`, SHA-256 `35bcb1013b0716a4faa33fdbd75ff067427c1dec8e377f63ebb17ac301786ebd`.
The separate source review is `MICROSCOPIC_JOINT_FLOW_REVIEW.md`, SHA-256 `9699043c35343901ef75ab6a29dd560ba4aa30f8a3b908643e959958e86447c9`,
with review receipt SHA-256 `a31a20468660e38ff42bf215dd84832a1f722551c29ea770156dfc71781d4b06`. The complete source,
review, controls, output streams, failures, source revisions and root coverage
records are indexed by the [evidence map](../.claude/science/physics-loops/toe-regularity-joint-flow-20261012/EVIDENCE_MAP.json).
The [exact transformation map](../.claude/science/physics-loops/toe-regularity-joint-flow-20261012/PUBLICATION_EDITS.json) and
[reconstruction program](../.claude/science/physics-loops/toe-regularity-joint-flow-20261012/reconstruct.py) recover the entire note
and primary from their frozen bytes. Historical write-scope and pending-review
statements above describe the author freeze; the following record describes
the completed source review. Root contributed the mechanisms and is a coauthor,
not the independent reviewer. No new review was performed by the packaging worker.

The review supports J1-J24 without a required mathematical correction. It
read the actual current-implementation predecessor in full and matched the
local action, mixed-domain, individual-flow and full GNS implementation uses.
The joint conclusion remains conditional on the supplied self-adjoint operators
and the exact commutation identities on their actual local cyclic domain.

The reconstruction and distinct implementation froze before author helper,
output and mutant exposure. Candidate result summaries and upstream source and
receipt metadata were visible; this was not blinded checking. Exact Gaussian-
integer open-cutoff matrices, a complete qutrit basis and weighted two-dimensional
histories test different fixtures from the author helper. The baseline and all
five saved whole-source mutants reproduced their scientific output rows and
stdout exactly; replay result timestamps changed and were explicitly excluded
from metadata equality. The current-sign, half-factor, support-growth, Jacobi-
sign and divergence-term mutants fail their recorded gates. Passing mutant
rows, tracial-vacuum nondiscrimination, positive-pair sign/rescaling survival
and arithmetic-only binomial checks remain visible.

The canonical primary suppresses only the adjacent JSON-file write, declares
its inputs/timeout and assertion guard, and reports scoped execution totals.
Every calculation is preserved. Its printed self-hash correctly changes with
those recorded edits. Its only file read is its own source for that integrity
hash; declared note/dependency inputs bind the proof scope for the cache.
Neither the finite controls nor the classification builds an actual self-adjoint
realization or proves conservation for an intended physical model. The failed
instruction-freshness check and subsequent exact current-reference reread in
the review remain preserved; no prompt source was changed.


The [canonical finite primary](../scripts/microscopic_joint_flow_2026_10_12.py) is separate from the
analytic proof. For the mass and regularity primaries, `TOTAL` counts one
completed assertion-guarded driver; for the joint primary it counts its recorded
finite predicates. Neither total is a proof grade. Canonical execution, whole-
source mutation replays, current cache creation, graph acknowledgment and final
focused checks were **not run by preparation**. Their actual results must be
recorded in [delivery checks](../.claude/science/physics-loops/toe-regularity-joint-flow-20261012/DELIVERY_CHECKS.md) before publication.
No helper-registry policy change or formal audit is performed here.

The complete frozen argument retains its supplied conditions, scoped negative
witnesses and open application obligations. No Lean certificate, applied audit
verdict, retained promotion, new physical axiom or microscopic model is asserted.
The global combined pipeline and strict audit lint remain independent landing
gates. This is a frozen milestone packet; the sole live campaign checkpoint
remains in the transport worktree. Editable prompt files changed: none.


Checker pairing: the authors and focused reviewers used separate worker
contexts of the same configured model family, preserving the user's selected
model and reasoning effort. Different model families and blind checking are
not claimed. The distinct reconstruction/control mechanisms and actual source
exposure are documented above and in each complete source review. This pairing
disclosure is not an independent-audit grade or a retained-status decision.
