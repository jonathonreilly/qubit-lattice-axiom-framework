---
claim_id: microscopic_current_implementation_bounded_theorem_note_2026-10-12
claim_type: bounded_theorem
claim_scope: "For bounded finite-range spin densities and supplied self-adjoint H, B, P with exact local cyclic H and first-moment B actions and P=i[H,B] on that domain, derive the finite-range current, common local analytic radius, norm thermodynamic dynamics and full canonical GNS adjoint implementation. Boost realization, strong joint commutation and a physical model remain supplied."
upstream_dependencies: []
runner: scripts/microscopic_current_implementation_2026_10_12.py
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: upstream_support
reachability_to_target: partially_closes
conditional_surface_status: "Microscopic current implementation from explicit local-vector boost action and closure"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# Microscopic current implementation from exact local-vector action

**Conditional bounded theorem, 2026-10-12; complete separate I1–I31 source review supports the implication.** The supervisor supplied the proposed mechanism and is a coauthor. This note establishes a conditional implementation lemma, not the existence of its boost/domain premises in a physical model. It has no audit or retained status.

The proposed route works with a precise extra hypothesis: the self-adjoint boost must act on every local cyclic vector by the displayed local first-moment derivation, and the integrated momentum must equal the commutator on that same domain. Those statements are not inferred from formal sums or first-moment translation covariance. Once supplied, they imply invariance of the local cyclic domain and identify the momentum's unitary group with the finite-range current flow. A direct Taylor-remainder argument suffices; no new Nelson theorem, essential-self-adjointness theorem, scattering input, positivity of H, gap, unique vacuum or separating-vacuum assumption is used.

S denotes the original research collection. The [complete milestone packet](../.claude/science/physics-loops/toe-centre-current-20261012/) preserves the frozen proposal, full control logs, independent review, recovery history and source identities. Prior science remains unchanged.

## 1. Sources and the exact obligation

| Source in the packet | SHA-256 | Role |
|---|---|---|
| ROOT_MICROSCOPIC_CURRENT_IMPLEMENTATION_LEAD.md | f5937c130f4e7c771f729e4946d472cea7abee90b8587deb4ad7140a11b6d70c | Complete 94-line proposal, tested rather than treated as authority |
| INDEX_TO_PHYSICS_NEXT_OBLIGATION.md | cb512af29397a3a6e8c58161bbe1dd6c15e61944b5f8bdd9ae0c1a0cc53c2536 | Exact microscopic implementation gap and single-beta clock convention |
| C4_N1_report.md | c284a41bfee8a1238643330ddd46f3a7c4f6f1a865509a9aaec5ab6f4238ad13 | H-loc current expression; H-int and H-cov remain supplied, not verified here |
| COMPACT_PATCH_SCATTERING_COVARIANCE_PROBE.md | d1d8ace7a450e0c00d780443f83a333223fff395b170994a83e1b65653302a4a | S1 implementation requirements and positive H/negative P clock conventions |
| APPROXIMATE_PARTIAL_FACTOR_INDEX_PROBE.md | bccf07d0ca041c9c0585beccb912ac35e1da12deadae3c50efb78d439cb9b441 | P11 identifies the finite-range uniform-current input required downstream |
| APPROXIMATE_PARTIAL_FACTOR_INDEX_REVIEW.md | 9118707fdcc85cdfd0a1160598872fb8544a9de757b3a1efe8e93292719c533c | Existing source-bound conditional index review; no new audit authority |

The recovered draft was fully read and its complete proof reconstructed in the present author recovery. The full lead and index-to-physics assessment, N1's H-loc/H-int/H-cov context and Step 1, the scattering probe's complete S1–S4 block, and the partial-factor probe's complete P11 microscopic-flow argument were read at the frozen identities above. The index review is source-bound context, not a proof input to this implementation lemma; no new review of its entire index theorem is claimed. Main instruction authority is `a13caa4885f547c8d206265b031ba7649e539fd9`, planning instruction authority is `3a4b2c66a1ead7a1c48b4359627e968f681e3c39`, and the read-only science checkout was observed at `5cbc581504721a323f5fa2064694a67141a3ee98`. Applicable instructions were read from the selected revisions, and installed physics-loop/workhorse entry points matched them exactly. Source checks and instruction hashes are in `microscopic_current_implementation/logs/recovery3_acquisition.json`. No repository source or ref is changed.

The selected-main statement search is recorded in `microscopic_current_implementation/logs/selected_main_statement_search.json`. Matched context included finite-volume nested-commutator support, native ring interaction norms and Gaussian-CAR analytic vectors. The inspected statements do not supply this general spin-current local-vector implementation argument; no exhaustive literature or repository novelty claim is made. The contribution here is discharge of the exact implementation obligation named by the frozen assessment. The primitive registry and current minimal axioms were inspected: this lemma uses none of the three registered primitives and adopts no new physical premise. Its H/B/P/domain data remain explicitly supplied mathematical hypotheses.

The proof below is self-contained from finite commutator algebra, finite-dimensional unitary dynamics and the spectral theorem for an already supplied self-adjoint P. It does not import the claim that a formal commutator is essentially self-adjoint or integrates to a Poincaré representation.

## 2. Precise local hypotheses; domains are part of the statement

Use the finite-dimensional spin tensor algebra on \(\mathbb Z^d\), \(d\ge1\), with the \(\ell^1\) metric. Put \(B_R=\{x:|x|_1\le R\}\), with integer \(R\ge0\), and choose the geometric convention
\[
\tau_j(\mathcal A(X))=\mathcal A(X+j),\qquad
h_x=\tau_x(h_0)=h_x^*,\quad
\operatorname{supp}h_x\subset x+B_R,\quad \|h_x\|\le h.
\tag{I1}
\]
Here \(h<\infty\). The opposite geometric shift convention reverses translation labels and index signs; it does not change the implementation result. The chosen convention gives the N1 first-moment sign \(T_jB_bT_j^*=B_b-j_bH\) when that operator identity is separately justified.

For local A define the genuinely finite local sums
\[
\delta_h(A)=i\sum_x[h_x,A],\qquad
\delta_b(A)=i\sum_x x_b[h_x,A].
\tag{I2}
\]
Both map \(\mathcal A_{\rm loc}\) into itself. The position factor is bounded on the finite set relevant to each A, although it is not uniformly bounded as A is translated.

Let \((\pi,\mathcal H,\Omega)\) be a cyclic GNS representation, \(\|\Omega\|=1\), and
\[
\mathcal D=\pi(\mathcal A_{\rm loc})\Omega.
\]
This is a dense linear space: finite sums of local observables are local in the union of their supports. Supply self-adjoint \(H,B_b,P_b\), with the local-domain inclusions in I4 below, and require only
\[
H\Omega=B_b\Omega=0.
\tag{I3}
\]
Since \(\Omega=\pi(1)\Omega\in\mathcal D\), its domains are already included in I4. The equation \(P_b\Omega=0\) will follow from the local commutator relation; it is not an additional vacuum assumption.
The exact extra local conditions are
\[
\begin{split}
&\mathcal D\subset\operatorname{Dom}H\cap\operatorname{Dom}B_b
                         \cap\operatorname{Dom}P_b,\\
&iH\pi(A)\Omega=\pi(\delta_h(A))\Omega,\qquad
 iB_b\pi(A)\Omega=\pi(\delta_b(A))\Omega
       \quad(A\in\mathcal A_{\rm loc}),\\
&P_b\xi=i(HB_b-B_bH)\xi\quad(\xi\in\mathcal D).
\end{split}                                                    \tag{I4}
\]
The products in the last line are well-defined by the derived invariance immediately below. One can equivalently include their domains in I4, but that adds no assumption. These are equalities of actual Hilbert vectors, not quadratic-form identities or formal infinite sums.

The notation \(i[H,\pi(A)]\Omega\) means exactly the first local-vector equality, using \(H\Omega=0\); it does not assert that \(\pi(A)\) preserves all of \(\operatorname{Dom}H\). The same applies to B. If H is already the invariant-vector implementer of the microscopic energy flow, its local domain and first equality follow by differentiating the norm-differentiable local orbit and applying the generator definition. The boost equality and the closure identity on this particular \(\mathcal D\) remain new supplied conditions. H-int on an unspecified domain does not establish them.

Because \(\delta_h(A)\) and \(\delta_b(A)\) are local, I4 gives
\[
H\mathcal D\subset\mathcal D,\qquad B_b\mathcal D\subset\mathcal D,
\qquad\mathcal D\subset\operatorname{Dom}(HB_b)\cap\operatorname{Dom}(B_bH).
\tag{I5}
\]
Every finite word in H and B is consequently defined on \(\mathcal D\) and preserves it. This is a conclusion from the local action, not a domain assumption hidden in the commutator notation. No invariance under their exponentials, and no claim that \(\mathcal D\) is a core for B, is needed. Applying the last line of I4 to \(\Omega\) now gives \(P_b\Omega=i(HB_b-B_bH)\Omega=0\). Self-adjointness of P is used below; the integration argument imposes no additional core, analytic-domain or strong-commutation premise on H or B.

## 3. Finite pair symmetrization, signs, support and interaction norm

Define
\[
p_b(x)=\frac i2\sum_{|r|_1\le2R}r_b[h_x,h_{x+r}],\qquad
\delta_p(A)=i\sum_x[p_b(x),A].
\tag{I6}
\]
The r-sum is finite. Terms with \(|r|_1>2R\) commute because the h supports are disjoint. Each \(p_b(x)\) is self-adjoint, translation-covariant and supported in \(x+B_{3R}\). Set
\[
c_{R,b}=\sum_{|r|_1\le2R}|r_b|,\qquad v_{3R}=|B_{3R}|.
\]
The triangle and commutator bounds give
\[
\|p_b(x)\|\le h^2c_{R,b}.
\tag{I7}
\]
Treat \(p_b(x)\) as an interaction term assigned to the finite set \(x+B_{3R}\), combining terms if a representation of the interaction has repeated sets. A valid interaction \(\Psi_p\) therefore has
\[
s_p\le v_{3R},\qquad \ell_p\le6R,\qquad
J_p:=\sup_z\sum_{X\ni z}\|\Psi_p(X)\|
       \le v_{3R}h^2c_{R,b}.
\tag{I8}
\]
Here \(s_p\) bounds term cardinality and \(\ell_p\) bounds its diameter. J is the per-site sum of term norms, with no extra cardinality or volume normalization. Radius \(3R\) and diameter \(6R\) are deliberately distinguished. If \(R=0\), then \(c_{R,b}=0\) and the current is zero.

To prove the derivation identity without rearranging divergent sums, let \(A\in\mathcal A(Y)\). A center contributing to a first commutator is within R of Y. A second commutator can use a center within 3R of Y. Choose a finite center set I containing all centers within 3R and set
\[
H_I=\sum_{x\in I}h_x,\qquad B_I=\sum_{x\in I}x_bh_x.
\]
Both second local derivatives agree with the corresponding finite double commutators. Finite Jacobi and finite interchange of x,y give
\[
\begin{split}
[\delta_h,\delta_b](A)
 &=-[[H_I,B_I],A],\\
[H_I,B_I]
 &=\sum_{x,y\in I}y_b[h_x,h_y]
   =\tfrac12\sum_{x,y\in I}(y_b-x_b)[h_x,h_y].
\end{split}                                                    \tag{I9}
\]
For a nonzero \([[h_x,h_y],A]\), the pair overlaps and at least one h support meets Y. Thus one center is within R and the other within 3R of Y. All contributions to the final local commutator are already in I. Substituting \(y=x+r\) in that finite local expression yields
\[
\boxed{[\delta_h,\delta_b](A)=\delta_p(A).}
\tag{I10}
\]
This also matches N1's density \(\tfrac12(x_b-y_b)i[h_y,h_x]\): reversing the commutator turns it into the coefficient in I9. The factor \(1/2\) is required when both orientations of each pair are summed.

Using I4/I5 on the local observables \(\delta_h(A),\delta_b(A)\),
\[
\begin{split}
HB_b\pi(A)\Omega&=-\pi(\delta_h\delta_b(A))\Omega,\\
B_bH\pi(A)\Omega&=-\pi(\delta_b\delta_h(A))\Omega,\\
\boxed{P_b\pi(A)\Omega=-i\pi(\delta_p(A))\Omega.}
\end{split}                                                    \tag{I11}
\]
Hence \(P_b\mathcal D\subset\mathcal D\) and
\[
P_b^n\pi(A)\Omega=(-i)^n\pi(\delta_p^n(A))\Omega
\quad(n\ge0).
\tag{I12}
\]
This is the local-vector relation to be integrated. It is not yet a full automorphism statement.

For later sign checks, translation of the local first moment is also a finite identity:
\[
\tau_j\delta_b\tau_{-j}=\delta_b-j_b\delta_h,
\qquad \tau_j\delta_p\tau_{-j}=\delta_p.
\tag{I13}
\]
These derivation identities alone do not equate unbounded boost operators on their complete domains. If an invariant geometric implementation T is supplied, they give the corresponding equality on \(\mathcal D\); promoting boost covariance to the full integrated operator relation still requires its own domain argument. An origin shift adding a constant multiple of \(\delta_h\) to \(\delta_b\) leaves I10 unchanged.

## 4. Connected nested commutators and a common analytic radius

The following general estimate is useful beyond this density. Let \(\Psi(X)=\Psi(X)^*\) be a finite-range interaction on the spin algebra, with nonempty finite sets X, uniformly bounded cardinality \(|X|\le s\), and
\[
J=\sup_z\sum_{X\ni z}\|\Psi(X)\|<\infty,
\qquad \delta_\Psi(A)=i\sum_X[\Psi(X),A].
\tag{I14}
\]
Scalar terms assigned to the empty set can be removed because they do not affect the derivation. Take \(s\ge1\). For A supported on a finite set Y with \(a=|Y|\ge1\),
\[
\boxed{
\|\delta_\Psi^n(A)\|
\le\|A\|(2J)^n\prod_{k=0}^{n-1}\bigl(a+k(s-1)\bigr).
}
\tag{I15}
\]
The empty product at \(n=0\) is one. The same estimate holds for every finite-volume derivation obtained by deleting interaction terms.

Proof: expand the nested derivation into ordered tuples \(X_1,\ldots,X_n\). A term vanishes unless \(X_k\) meets \(Y\cup X_1\cup\cdots\cup X_{k-1}\). For such a connected history the union has size at most \(a+(k-1)(s-1)\). At the next step,
\[
\sum_{X:X\cap Z\ne\varnothing}\|\Psi(X)\|
\le\sum_{z\in Z}\sum_{X\ni z}\|\Psi(X)\|
\le J|Z|.
\]
Multiply these successive bounds and use a factor two for each commutator. Every step has finitely many terms by finite range and the finite lattice neighborhood, so the expansion and regrouping are legitimate. Bounding by the size of the whole radius-n ball would introduce an unnecessary dimension-dependent growth and would not prove the claimed radius. I15 counts each connected support history instead.

If \(r=s-1>0\) and \(J>0\), write \(z=2Jr|t|\) and \(c=a/r\). The nth Taylor majorant is
\[
\|A\|\,z^n\frac{(c)_n}{n!},\qquad
\sum_{n\ge0}z^n\frac{(c)_n}{n!}=(1-z)^{-c}
\quad(0\le z<1).
\tag{I16}
\]
The series identity follows by the usual binomial recurrence or by solving \((1-z)f'=cf\), \(f(0)=1\), for its power series. The ratio of successive majorants tends to z, so every term and every tail tend to zero for
\[
|t|<\rho:=\frac1{2J(s-1)}.
\tag{I17}
\]
This radius is independent of the support size a and the finite volume; the prefactor and convergence rate may depend strongly on a. The initial set Y can be disconnected and have arbitrary diameter; “connected history” means each new interaction set meets the accumulated union, not that Y itself is connected. No convergence at \(|t|=\rho\) is asserted. If \(s=1\), I15 becomes \(\|A\|(2Ja)^n\), giving an entire exponential majorant. If \(J=0\), the derivation vanishes. If A is scalar, all derivatives of positive order vanish. These cases need no division by zero or artificial finite radius.

## 5. Finite-volume construction and uniform Taylor remainders

For a finite spatial volume \(\Lambda\), define
\[
G_\Lambda=\sum_{X\subset\Lambda}\Psi(X),\qquad
\alpha_t^\Lambda(A)=e^{itG_\Lambda}Ae^{-itG_\Lambda}.
\tag{I18}
\]
The local Hamiltonian is bounded and self-adjoint. For each real t and integer \(N\ge1\), iterated differentiation gives the norm integral remainder
\[
\alpha_t^\Lambda(A)
=\sum_{k=0}^{N-1}\frac{t^k}{k!}\delta_\Lambda^k(A)
+\frac{t^N}{(N-1)!}\int_0^1(1-u)^{N-1}
          \alpha_{ut}^\Lambda(\delta_\Lambda^N(A))\,du.
\tag{I19}
\]
Its norm is bounded by \(|t|^N\|\delta_\Lambda^N(A)\|/N!\), uniformly in \(\Lambda\) by I15. This uses isometry of the real-time automorphism, not a volume-uniform bound on \(\|G_\Lambda\|\).

If \(\ell\) bounds interaction diameters, each connected support history of length k lies in the \(k\ell\)-neighborhood of Y. Therefore, whenever \(\Lambda\) contains that neighborhood,
\[
\delta_\Lambda^k(A)=\delta_\Psi^k(A).
\tag{I20}
\]
For \(|t|<\rho\) (or any finite t in the entire cases), first choose N so that the common remainder bound is small, then choose \(\Lambda\) containing the N-step neighborhood. This proves both the norm thermodynamic limit and the local Taylor formula
\[
\alpha_t^\Psi(A):=\lim_{\Lambda\nearrow\mathbb Z^d}\alpha_t^\Lambda(A)
=\sum_{k\ge0}\frac{t^k}{k!}\delta_\Psi^k(A).
\tag{I21}
\]
The limit is independent of the exhausting volumes. On a compact interval \(|t|\le t_0<\rho\), the same argument is uniform in t. Finite-volume isometry and density of the local algebra extend the small-time limit to every quasilocal A. Its limit preserves products and adjoints.

For any real t choose an integer m with \(|t/m|<\rho\); in an entire case any sufficiently convenient m works. On all quasilocal observables, point-norm convergence of isometries implies convergence of every fixed finite composition: if \(F_\Lambda\to F\) and \(G_\Lambda\to G\), then
\[
\|F_\Lambda G_\Lambda(A)-FG(A)\|
\le\|G_\Lambda(A)-G(A)\|
  +\|(F_\Lambda-F)(G(A))\|\longrightarrow0.
\]
Thus
\[
\alpha_t^\Lambda=(\alpha_{t/m}^\Lambda)^m
\longrightarrow(\alpha_{t/m}^\Psi)^m.
\tag{I22}
\]
This constructs the norm limit for every t; different choices of m give the same limit of the same finite-volume net. Passing to the finite-volume group law now gives \(\alpha_s^\Psi\alpha_t^\Psi=\alpha_{s+t}^\Psi\), including inverse \(\alpha_{-t}^\Psi\). Hence these are automorphisms. Continuity at zero follows from I21 on locals and isometry on their norm closure, and the group law gives point-norm continuity everywhere. This provides the needed microscopic flow without an additional thermodynamic-limit import. Uniform convergence on any compact time interval can also be obtained by subdivision and finite nets in the compact sets of continuous limiting orbits; only pointwise convergence and small-time uniformity are needed below.

In particular, the generator on a local A is exactly \(\delta_\Psi(A)\). Any other point-norm continuous automorphism group whose generator agrees there has the same iterated local derivatives and isometric Taylor remainders, hence agrees first for small t and then for all t. No assertion about an unspecified formal generator domain is being used.

For the density construction in §3, the interaction-volume cutoff (I18) need not equal \(i[H_\Lambda,B_\Lambda]\) at a boundary. The pair identity (I9) is used only on padded local observables. If the h cutoff includes every h term supported in a spatial volume containing the \(4R\)-neighborhood of Y, its two local derivatives on A agree with the infinite expressions. For the assigned p-interaction sets in I8, the conservative neighborhood \(Y^{6Rn}\) stabilizes its nth coefficient. These are sufficient padding bounds, not an asserted equality of different finite-volume Hamiltonians.

## 6. Direct unitary Taylor comparison and full GNS implementation

More generally, suppose a self-adjoint P satisfies \(P\Omega=0\), \(\mathcal D\subset\operatorname{Dom}P\), and
\[
P\pi(A)\Omega=-i\pi(\delta_\Psi(A))\Omega
\quad(A\in\mathcal A_{\rm loc}).
\tag{I23}
\]
Locality gives \(P\mathcal D\subset\mathcal D\) and all powers in I12. Since representations are contractive, I15 implies
\[
\|P^n\pi(A)\Omega\|
\le\|A\|(2J)^n\prod_{k=0}^{n-1}(a+k(s-1)).
\tag{I24}
\]
For \(\xi\in\operatorname{Dom}P^N\), the spectral theorem or repeated strong integration along the unitary group gives
\[
\left\|e^{itP}\xi-\sum_{k=0}^{N-1}\frac{(it)^k}{k!}P^k\xi\right\|
\le\frac{|t|^N}{N!}\|P^N\xi\|.
\tag{I25}
\]
For completeness, its vector remainder is \((it)^N/(N-1)!\) times the integral of \((1-u)^{N-1}e^{iutP}P^N\xi\) over \(0\le u\le1\); self-adjointness supplies the unitary norm bound. No essential-self-adjointness conclusion is invoked.

The remainders in I19 and I25 tend to zero on the same interval. Their coefficients match because \(i^k(-i)^k=1\). Therefore
\[
e^{itP}\pi(A)\Omega=\pi(\alpha_t^\Psi(A))\Omega
\qquad(A\in\mathcal A_{\rm loc},\ |t|<\rho).
\tag{I26}
\]
At this point equality is only on vacuum columns; promoting it to an adjoint action requires the following additional steps.

First, using \(e^{-itP}\Omega=\Omega\),
\[
\omega(\alpha_t^\Psi(A))
=\langle\Omega,e^{itP}\pi(A)\Omega\rangle=\omega(A).
\tag{I27}
\]
Norm density extends invariance to all quasilocal A for these small times. The flow group law then extends state invariance to every real t. Define its canonical GNS unitary by
\[
W_t\pi(A)\Omega=\pi(\alpha_t^\Psi(A))\Omega.
\tag{I28}
\]
Indeed,
\[
\|\pi(\alpha_t^\Psi(A))\Omega\|^2
=\omega(\alpha_t^\Psi(A^*A))=\omega(A^*A)
=\|\pi(A)\Omega\|^2.
\]
Thus state invariance respects null vectors and makes I28 well-defined and isometric; inverse time gives a unitary. Point-norm continuity gives strong continuity. For small t, I26 and density imply \(W_t=e^{itP}\) as bounded operators. The group laws give equality for all t.

Finally, for quasilocal A,B, use the canonical action on their dense cyclic vectors:
\[
\begin{split}
W_t\pi(A)W_t^*\pi(B)\Omega
 &=W_t\pi(A\alpha_{-t}^\Psi(B))\Omega\\
 &=\pi(\alpha_t^\Psi(A))\pi(B)\Omega.
\end{split}
\]
Consequently
\[
\boxed{\quad e^{itP}\pi(A)e^{-itP}=\pi(\alpha_t^\Psi(A))
\quad(A\in\mathcal A,\ t\in\mathbb R).\quad}
\tag{I29}
\]
Neither vacuum separation nor faithfulness is needed for this represented implementation. In this spin algebra, the cyclic unital representation is in fact faithful: its restriction to each local full matrix factor is a unital representation and hence isometric; norm density extends isometry to \(\mathcal A\). This permits later transfer of represented equalities back to the full algebra without purity of the state. The given construction already defines the algebra automorphism independently of that observation. Among self-adjoint operators fixing \(\Omega\) and satisfying I23, the implementing unitary group, and hence its generator, is unique.

Apply I23–I29 with \(P=P_b\) and \(\Psi=\Psi_p\), using I11. This proves the conditional current-implementation lemma under I1–I4.

## 7. Physical and current clocks, translations, and what remains of S1

Write \(\widehat\alpha_t^p\) for the positive-clock flow constructed above. The result is
\[
\operatorname{Ad}e^{itP_b}=\widehat\alpha_t^p,
\qquad
\alpha_s^{P_b}:=\operatorname{Ad}e^{-isP_b}=\widehat\alpha_{-s}^p
\tag{I30}
\]
in the given representation. The negative-clock infinitesimal derivation is \(-\delta_p\), equivalently the positive-clock interaction is \(-\Psi_p\). For \(K_b=P_b/\beta\), \(\beta>0\),
\[
\operatorname{Ad}e^{-iyK_b}=\widehat\alpha_{-y/\beta}^p,
\qquad J_{K_b}\le J_p/\beta.
\tag{I31}
\]
Thus the N1 time \(s=q/\beta\) for generator P is the same as time q for generator K, with exactly one beta division. The physical-time convention remains \(\operatorname{Ad}e^{itH}\) and \(\delta_h=i\sum[h_x,\cdot]\). No sign is transferred silently between these clocks.

The single-current lemma does not derive strong commutation of H with P, or of different momentum components. A separate geometric-covariance consequence is available only with an additional supplied invariant translation implementation: the current interaction is translation-covariant. Translating a finite-volume flow replaces \(\Lambda\) by \(\Lambda+j\); their limits give \(\tau_j\widehat\alpha_t^p=\widehat\alpha_t^p\tau_j\). If geometric unitary implementers \(T_j\) fixing \(\Omega\) are supplied, then their action and the canonical action I28 commute on a dense cyclic set. Hence \(T_j\) commutes with every \(e^{itP_b}\). This part of S1 follows from the lemma plus the supplied geometric implementation. The existence and state invariance of those geometric implementers are not derived from the current lemma alone.

| S1/index input | Consequence or remaining condition |
|---|---|
| P is the actual finite-range bounded-current implementer | Derived from the precise I4 local-vector action and closure on \(\mathcal D\), with I8 quantitative norms |
| K=P/beta generates its stated microscopic flow | Derived with the explicit scaling and clock in I31 |
| P and K fix the vacuum | Derived from I3–I5; no separate P-vacuum assumption is needed |
| H implements the physical-time finite-range dynamics | Already supplied in the task; the exact local H action is the part used by this proof. H positivity is a separate condition |
| Current commutes with geometric translations | Algebra flow commutation is derived; Hilbert implementation commutation follows when invariant geometric implementers are supplied |
| Constants fixed independently of tube width | Derived: I8 depends only on h, R and dimension; the time and beta are fixed parameters |
| P11 microscopic LR input | The finite-range interaction and uniform norm required by P11 are now identified with P under I4; P11’s stated LR theorem and tube argument remain its own mathematical input |
| H/P and distinct momentum components strongly commute | Still required for S1's joint action; not proved by the single-current implementation lemma or by the generic energy-current formula |
| Self-adjoint integrated Poincaré generators and exact closure | Still supplied; no boost or representation is constructed |
| The boost acts by the local first moment on all \(\mathcal D\) | Explicit extra premise, not obtained from H-cov or formal notation |
| The commutator identity holds on that same \(\mathcal D\) | Explicit extra premise, not inherited from an unnamed dense or analytic domain |
| H is positive, vacuum unique and gapped; particles and centres exist | Unused by this lemma and still needed where downstream physics invokes them |
| Scattering covariance, detector coverage, EX and physical realization | Not supplied by this lemma |

Finite-range improvements are not free identifications. If a current improvement has a separately proved matching local-vector action, one can apply the general lemma to the improved interaction with its new support and J. For an addition \(\Xi\), one may use \(J_{\rm new}\le J_p+J_\Xi\), the maximum interaction cardinality and the maximum range. If its derivation is proved identically zero, it leaves the automorphism unchanged; otherwise the generator identity must actually change with the local action. Merely appending the words “plus an improvement” to the formal sum does not prove either fact.

## 8. Failed shortcuts and limits of the conditional reduction

1. **Formal P=i[H,B] does not identify B with the local first moment.** A finite diagnostic is \(H=\operatorname{diag}(0,1,2)\) on \(\mathbb C^3\), \(\Omega=e_0\), and \(B=|e_1\rangle\langle e_2|+|e_2\rangle\langle e_1|\). All three H,B,P fix \(\Omega\), and \(P=i[H,B]\ne0\). If the designated energy density is a single site at coordinate zero, its local first moment and its p-density vanish. The local B action in I4 fails. This tests that missing implication; it is not a lattice Poincaré model or a counterexample to the full theorem.
2. **First-moment translation covariance is not the local action.** Algebraically, adding a translation-invariant operator C to a covariant B preserves \(T_jBT_j^*=B-j_bH\), wherever both sides are actually defined, but can change \(i[H,B]\) by \(i[H,C]\). This is a freedom in that equation, not a construction of an operator satisfying the entire physical setting. The covariance equation supplies no equality with the specific commutator sums on \(\mathcal D\).
3. **Domains cannot be dropped before applying Jacobi to unbounded operators.** Jacobi here is applied only to the finite bounded density sums in I9. Hilbert products are separately justified by I5. Agreement on another unspecified core is not substituted for agreement on local cyclic vectors.
4. **Vacuum columns alone are not adjoint implementation.** I26 is followed by state invariance and canonical GNS construction before I29. No inference from \(X\Omega=0\) to \(X=0\) occurs.
5. **A ball-volume count does not establish the claimed radius.** The bound is on each connected nested support union. Dimension-dependent growth of the whole accessible ball is a looser estimate and can destroy this particular analytic-series argument. That failed estimate is not a physical obstruction.
6. **Finite-volume first moments have boundary terms.** The finite pair commutator, the truncated density sum, and the assigned-interaction cutoff need not be equal at a boundary. Only their padded local coefficients are used. Periodic coordinates do not make the first moment a periodic observable.
7. **The radius is support-independent, not the bound itself.** Factors depending on a remain in I15/I16. There is no uniform convergence rate over arbitrary growing supports and no operator-norm convergence of the infinite-volume unitary groups.
8. **Existence and locality are still supplied.** The result does not establish a self-adjoint B with I4 in the vacuum representation, justify the Poincaré Lie algebra there, or show that a physically realized model has these properties. Changing those domains or allowing an interaction outside the checked finite-range class lies outside this theorem; no universal impossibility claim follows.

## 9. Author verification, finite controls and recovery

The analytic result is the implication I1–I4 ⇒ I29, with the explicit current I6 and bounds I8. The author reconstructed each load-bearing step after recovery: D invariance before unbounded products; finite padded Jacobi before pair symmetrization; per-history support growth before the Taylor bound; termwise stabilization and uniform finite-volume remainders before the norm limit; point-norm composition before the group law; and state invariance/null-vector preservation before full GNS implementation. No open proof step remains in this conditional author argument. Independent proof review was pending at author freeze; the completed review below confers no retained or audit status.

The direct Taylor method is the completed author route. An analytic-vector essential-self-adjointness theorem was unnecessary because self-adjoint P is already a premise. Formal infinite-sum rearrangement, a whole-ball support count, promotion of vacuum-column equality by separation, and an unproved local-domain consequence of H-cov were rejected shortcuts, not independently exhausted physical routes. The exact remaining physical obligation is construction/verification of I4 for the specified boost and integrated momentum in the intended microscopic model. That is outside the conditional implication proved here; no claim that it is impossible or easy follows.

The author runner is `microscopic_current_implementation/finite_controls.py`. It uses exact Gaussian-rational coefficients for sparse Pauli algebra and separately assembled dense Kronecker matrices for finite matrix checks. Its noncommuting one-dimensional density is

\[
h_x=X_{x-1}Z_{x+1}+\tfrac12Y_x+\tfrac14Z_{x-1}Y_x.
\]

This is a finite algebra fixture, not a candidate satisfying the physical boost/vacuum/Poincaré hypotheses. Its exact triangle norm bound is h≤7/4; for the assigned current interaction, I8 gives p-term norm≤147/8 and J≤1029/8. Floating matrix eigenvalues are only reported observations and are not substituted for these analytic upper bounds.

The controls establish the following finite facts:

- Five one- and two-site Pauli probes have `[delta_h,delta_b](A)=delta_p(A)` exactly. Reversing the current sign, omitting the pair factor one-half, or reversing the first-moment translation sign produces detected nonzero defects.
- The p-density is Hermitian and supported inside [-3,3]. The local pair reduction agrees with center padding of radius 3R. Radius R fails on the displayed probe with exact coefficient l1 defect 93/4.
- For a separate nearest-neighbor bond interaction, the nth local Taylor coefficient is unchanged by a volume padded by n interaction diameters, through n=5; deleting the last layer gives nonzero coefficients at every tested order.
- Exact enumeration of rooted support histories through order seven, including a disconnected initial support, respects the cardinality/count bound. Removing the support-growth factor already fails at order two: six enumerated histories exceed the mutant bound four. Singleton and zero-interaction cases are enumerated separately.
- Dense finite matrices give zero residual between i[H,B] and the relative-coordinate pair sum. The negative current clock and one beta division agree; reversed clock and double beta division differ in operator norm by approximately 0.962 and 0.981, respectively, in the chosen finite fixture. Finite unitary Taylor remainders through order six lie below their displayed derivative-norm bounds.

The final execution completed with 50 checked predicates and no failed predicates. This count is an execution summary, not an evidence grade. Complete rows, actual software versions and the runner hash are in `microscopic_current_implementation/finite_controls_results.json`; stdout is `microscopic_current_implementation/logs/finite_controls.final.jsonl`. Reproduce with Python 3 and NumPy/SciPy:

```text
python3 microscopic_current_implementation/finite_controls.py
```

The runner uses only its own directory for the result JSON. Exact algebra rows are distinct from floating matrix controls. Neither kind establishes an unbounded domain, self-adjointness, thermodynamic convergence, a Lieb–Robinson theorem, physical realization, or correctness of the analytic proof. There was no independent numerical or proof checker in this author recovery. The sparse and dense routes are different finite arithmetic checks written by this same author and share the fixture; they are not an independent review.

Two earlier control runs and their exact sources/results remain under `logs/`. Subsequent edits made the mutation/support predicates executable failure gates, replaced a redundant arithmetic edge check by actual singleton/zero history enumeration, corrected a padding-radius field label, and separated the exact triangle bound from numerical norm observations. These were author validation refinements; no failed mathematical control was suppressed.

Two explicit platform disconnect request IDs are preserved: `d8b30d99-0af8-4663-ade1-1950f8b68e30` and `30f8456c-bfa0-4295-8850-c2939a9cb712`. The original `logs/operational_history.json` and `logs/root_recovery_after_two_disconnects.json` remain unchanged. The earlier inventory recorded no completed note; recovery subsequently found a substantial 27,197-byte draft with filesystem mtime 2026-10-12 02:21:13 UTC. Its exact bytes were preserved before edits as `logs/PROBE.recovered_before_recovery3.md`, SHA-256 `6a12d85cfb33907c301006fae99fae1f9ffd5e3fcea021ea51c62f5121b1c036`. `logs/recovered_draft_discrepancy.json` records that discovery, and the original checkpoint is preserved as `logs/CHECKPOINT.before_recovery3.md`. A create-only write first refused to overwrite the recovered note and changed no files. No hidden platform diagnosis or reconstruction of lost reasoning is asserted.

Frozen author operational record: Root supplied the candidate mechanism and is a coauthor. A fresh independent reviewer must inspect the exact final source, especially the domain implication, finite symmetrization, common analytic radius, all-time finite-volume extension and canonical GNS step, before publication or substantial downstream reuse. The source-bound author receipt and the current checkpoint identify the final files and remaining obligations. No prompt file, axiom, audit result, Git ref, repository source, prior frozen packet or other chat was changed. Model and reasoning effort were preserved; no subdelegation was used. The campaign deadline remains 2026-10-12 16:00:52 UTC. Publication update: the exact final argument has now received the separate source review below.


## Publication verification and remaining obligations

The separate review supports all I1–I31 with no required mathematical correction.
Report305fa33efebf1e9f9dc09d0854eddf23065877004888f55e964d31cc403f6d17,
receipt1e8f868b6722ce57d60c626d3899e08f28fe6183e7aef5533a2891f96bb803fc.
Its reconstruction and occupation-basis hopping control froze before author
helper exposure. A closed-form current exponential and nonseparating vacuum
test the full algebra, including a wrong right action with identical vacuum
columns but nonzero operator defects. All34independent predicates and all50
original rows passed. Five actual copied-source defects were rejected; known
nondiscriminating rows, including the contiguousa=3history fixture throughorder7,
are retained. Finite controls do not prove the domain or thermodynamic argument.
Original author logs lack per-run timeout/elapsed receipts; no metadata is
invented. Reviewer runs recorded60second limits and0.250/0.679second completion.
The two platform disconnects, late-draft discrepancy and all saved versions remain.
The published helper suppresses only its adjacent JSON-file side effect,
declares audit inputs and prints scoped execution totals. Every calculation is
unchanged; the printed helper hash changes with these explicit packaging edits.

Root proposed the mechanism and is a contributor, not the independent reviewer.
Shared source/metadata exposure is disclosed in the review; it is not blind
checking or an independence claim based on predicate counts. Complete proofs,
controls, review, failures and source hashes are preserved in the packet.
PUBLICATION_EDITS.json and reconstruct.py recover the note and entire primary
from frozen bytes and explicit metadata edits. No displayed mathematics changes.
The [finite primary](../scripts/microscopic_current_implementation_2026_10_12.py) is an executable finite check;
DELIVERY_CHECKS.md records its actual run and mechanical publication checks.
No Lean certificate, applied audit verdict, physical axiom change or retained
promotion is asserted. Global combined audit and strict audit lint remain
independent landing gates. The sole live campaign checkpoint remains in the
transport worktree; this packet is a frozen milestone.
