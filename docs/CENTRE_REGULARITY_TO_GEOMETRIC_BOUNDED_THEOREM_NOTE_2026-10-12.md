---
claim_id: "centre_regularity_to_geometric_bounded_theorem_note_2026-10-12"
claim_type: "bounded_theorem"
claim_scope: "On an exactly selected positive isolated mass and one fixed joint lift chart, a supplied product spectral carrier, residual momentum H1 regularity and a central spectral power bound imply the geometric norm exponent a/(2a+1) and the exact chartwise graph projection. A supplied scalar massive boost representation gives a separate domain-to-H1 implication. Actual regular almost-local seed existence, density and microscopic realization remain open."
upstream_dependencies:
  - isolated_centre_filtering_bounded_theorem_note_2026-10-12
runner: "scripts/centre_regularity_to_geometric_2026_10_12.py"
actual_current_surface_status: "conditional-support"
target_claim_type: "bounded_theorem"
trace_class: "upstream_support"
target_claim_id: null
target_blocker_text: "A separately checked time-averaged scattering argument after matching the actual creator, transfer, graph and regularity hypotheses."
source_of_blocker_text: "handoff"
reachability_to_target: "partially_closes"
artifact_role: "theorem"
next_trace_action: "Identify a checked joint carrier and boost gauge for actual almost-local seed vectors, then prove their central rate and target density."
conditional_surface_status: "Geometric spectral regularity from explicit joint-carrier, Sobolev and central-rate hypotheses"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "The fixed-mass representation, Sobolev trivialization and actual creator regularity remain supplied, and abstract vector density is not operator density."
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# Central regularity gives a geometric shell bound in a fixed massive chart

**Claim type:** bounded theorem. **Actual current-surface status:** conditional-support. **Source review:** complete with no required mathematical correction. **Target:** the exponent \(\alpha=a/(2a+1)\) in the root sketch. The implication is proved below under an explicit joint spectral representation, Sobolev regularity and a central spectral rate. None of those representation/regular-seed hypotheses is derived from the lattice axioms or from a smooth geometric momentum marginal. The mass remains isolated and is selected exactly before this argument. The central atom need not be isolated.

The proof gives the sketch's estimate, improves its numerical line constant, and identifies the entire zero-detuning projection on the declared chart. A distinct squared-energy calculation checks the geometry and gives a stronger constant. A separately supplied scalar massive representation makes a boost-domain implication to the Sobolev premise explicit. It supplies no boost domain for actual local seeds, no density of regular almost-local creators, and no microscopic realization. No result from the separately mutable nonisolated-mass task is used.

## 1. Source binding and exact scope

S denotes the original research collection. The [frozen milestone handoff](../.claude/science/physics-loops/toe-regularity-joint-flow-20261012/HANDOFF.md) and [evidence map](../.claude/science/physics-loops/toe-regularity-joint-flow-20261012/EVIDENCE_MAP.json) preserve the source files, full author/reviewer evidence and their identities. The actual in-branch proof uses are [Centre](ISOLATED_CENTRE_FILTERING_BOUNDED_THEOREM_NOTE_2026-10-12.md): Supplied commuting-flow/mass premises, fixed almost-local filtering, exact isolated-mass selection and selected lift; no central isolation or downstream scattering/detector conclusion is imported. Other historical references remain provenance only.

| Source in S | SHA-256 | Actual use |
|---|---|---|
| `ISOLATED_CENTRE_FILTERING_PROBE.md` | `1dcb9580d128d8fc41b76517ce0fe18842291e8e32681fa9c6b22f0feb1e13de` | Complete 401-line read. I1–I4 give the supplied commuting flows and isolated mass; I7–I19 give almost-local smooth central filtering and exact mass filtering without I5. I21 fixes the lift/sign. I28 supplies only a marginal statement. No I5 central isolation is used here. |
| `ISOLATED_CENTRE_FILTERING_REVIEW.md` | `68ea0c2f00d0808ce5a6a63632b0bc84a05398260478510fb4f66256e885cbc9` | Complete source-bound review read; its review coverage belongs to that frozen filtering theorem, not this bridge. |
| `ROOT_CENTRE_REGULARITY_TO_GEOMETRIC_LEAD.md` | `e03a75616f2341b7b9d2f332f40bf05d6d4486787e0d558818b550af8aed3266` | Unverified target sketch, independently derived below. Root is a contributor, not an independent reviewer. |

Repository main authority is the instructed locally available `a13caa4885f547c8d206265b031ba7649e539fd9`; planning is `3a4b2c66a1ead7a1c48b4359627e968f681e3c39`. No refs were fetched or written. The exact instruction/read/source manifests and snapshots are in `centre_regularity_to_geometric/sources/`. The main skill and relevant references match that pinned main source. The approved primitive registry was read: no units-reference, kinetic-isotropy or realized-state primitive is being classified as a missing hypothesis. The separate analytic assumptions below concern an actual spectral representation, its vector domains and creator density; they carry additional content.

A bounded repository search found the earlier free massive Wigner/rapidity domain arguments, particularly `FREE_DIRAC_POINCARE_STONE_DIFFERENTIAL_GENERATOR_COINCIDENCE_COMMON_CORE_BOUNDED_THEOREM_NOTE_2026-06-08.md` (SHA-256 `4f9525311a3adbb220c0cf63d585b5511af912e7c3ad450f649b13e40a9fd94d`) and `FREE_DIRAC_POINCARE_GENERATORS_ESSENTIAL_SELFADJOINTNESS_BOUNDED_NOTE_2026-05-30.md` (`c7bccb41cefd6942a4853e89a2055ce8fd817d6573277c29d70e6184f0aa30c3`). Both were read completely. They concern a separately supplied free spin-1/2 carrier. Their prior rapidity mechanism is acknowledged; their status, numerics, spin cocycle and full dependency chain are not premises of the self-contained scalar-domain proof in §7. No exhaustive novelty claim is made. No open PR or unrelated campaign claim was reviewed.

## 2. The representation and regularity hypotheses

Fix \(d\ge1\), \(M,\beta>0\), \(n_0\in\mathbb Z^d\), and a target central-character representative \(\theta_0\). Work on one declared compact joint lift chart. The geometric momentum \(p\) and the central character \(\theta\) have chosen injective real coordinate charts for their torus values. All vectors under consideration have support in a fixed compact \(p\)-set and in a bounded Borel set \(\Theta\) of the central chart, and their actual current momentum is
\[
 k=p+\theta+2\pi n_0. \tag{G1}
\]
The integer \(n_0\) is the same for the entire subspace in this theorem. Put
\[
 E(k)=\sqrt{M^2+\beta|k|^2},\qquad
 \Sigma(p)=E(p+\theta_0+2\pi n_0),\qquad
 D(p,\theta)=E(p+\theta+2\pi n_0)-\Sigma(p). \tag{G2}
\]
We have already restricted to \(E_M\mathcal H\); the positive-energy mass formula (I4) is exact here. Mass isolation is the source-side reason the fixed smooth joint H/K filter (I18)–(I19) can make this restriction without sacrificing almost locality. It is not a consequence of central regularity. No estimate on \(H^2-\beta|K|^2-M^2\) is substituted for an estimate on D.

The extra **joint spectral representation hypothesis** is a specified isometry J of the declared spectral subspace into
\[
 L^2(\mathbb R^d_p\times\Theta,\,dp\,d\nu(\theta);\mathcal F), \tag{G3}
\]
where \(\nu\) is a fixed sigma-finite Borel measure and \(\mathcal F\) a fixed separable Hilbert space. In this representation H, K, Q and V have the multiplication actions in (G1)–(G2) and the filtering source. J's range may be a measurable field of closed subspaces of \(\mathcal F\), with arbitrary countable/infinite multiplicity. Sobolev derivatives are taken in this **declared ambient trivialization**; they need not lie in the physical fibre. Merely choosing an abstract measurable multiplicity decomposition does not establish this regularity.

Write \(f=J\psi\), \(P_0f=\mathbf1_{\{\theta_0\}}f\), and \(f_\perp=(1-P_0)f\). We require
\[
 f_\perp\in L^2\bigl(\Theta,d\nu;H^1(\mathbb R^d_p;\mathcal F)\bigr),\qquad
 S_\ell^2=\|f_\perp\|^2+\ell^2\sum_{i=1}^d\|\partial_{p_i}f_\perp\|^2<\infty,\quad\ell>0. \tag{G4}
\]
The stronger hypothesis that all of f is H1, as in the sketch, suffices. No p derivative of the target atom is needed for the residual bound. If H1 is initially given only inside the p chart, compact support strictly inside it supplies an H1 zero extension: multiply by a smooth cutoff equal to one on that support, supported inside the chart, and extend the product by zero. A sharp restriction crossing a boundary is not silently treated as an H1 extension.

Let \(\delta(\theta)=|\theta-\theta_0|\) in this chosen lift. Assume, for some \(a>0\), \(C\ge0\), \(r_0>0\),
\[
 \|\mathbf1_{\{0<\delta\le r\}}f\|\le Cr^a,\qquad 0<r\le r_0. \tag{G5}
\]
The central atom itself is excluded. Choose the chart and \(r_0\) so the near-target ball does not meet a central coordinate cut; for example \(\overline B(\theta_0,r_0)\) can lie inside an injective torus chart. Equivalently (G5) may be supplied directly for the coordinate sets displayed. Arbitrary atomic, singular or continuous \(\nu\) is allowed. A nonzero point-character vector is asserted only if \(P_0f\ne0\).

Choose a closed ball \(B_P\) containing the p support. Choose R so
\[
 |p+\theta+2\pi n_0|,\ |p+\theta_0+2\pi n_0|\le R
 \quad(p\in B_P,\ \theta\in\Theta). \tag{G6}
\]
For example \(R=P+\sup_{\theta\in\Theta\cup\{\theta_0\}}|\theta+2\pi n_0|\) works for a ball of radius P about zero. Define explicit constants
\[
 E_*=(M^2+\beta R^2)^{1/2},\quad
 c=\frac{\beta M^2}{E_*^3}>0,\quad
 \epsilon_*=c\ell r_0,\quad
 \alpha=\frac{a}{2a+1}. \tag{G7}
\]
Here \(\ell,r_0\) have momentum units, c has energy/momentum-squared units, and \(\epsilon_*\) has energy units. The torus/lattice convention may make momentum dimensionless; the scale formula still avoids equating powers of quantities with unmatched units.

## 3. Hilbert-valued line bound and measurable directional slicing

For \(g\in H^1(\mathbb R;\mathcal F)\), use its locally absolutely continuous representative. The scalar function \(m(s)=\|g(s)\|^2\) is locally absolutely continuous and
\[
 m'(s)=2\operatorname{Re}\langle g(s),g'(s)\rangle\quad\hbox{a.e.},\qquad
 \int|m'|\le2\|g\|_2\|g'\|_2. \tag{G8}
\]
These facts follow first for smooth finite-rank functions, then by H1 approximation on bounded intervals. Cauchy–Schwarz makes \(m'\) integrable. Thus m has finite limits at both infinities; its integrability forces both limits to be zero. The two fundamental-theorem formulas for m give
\[
 2m(s)=\int_{-\infty}^s m'(t)\,dt-\int_s^\infty m'(t)\,dt,
\]
so, for every s,
\[
 \|g(s)\|^2\le\|g\|_2\|g'\|_2
 \le\frac{1}{2\ell}\left(\|g\|_2^2+\ell^2\|g'\|_2^2\right). \tag{G9}
\]
The first constant is sharp: \(g(s)=e^{-|s|}v\), \(\|v\|=1\), has both squared L2 norms and its squared supremum equal to one. In particular the weaker line inequality written in the root sketch is valid at \(\ell=1\).

For \(\delta>0\) set \(u(\theta)=(\theta-\theta_0)/\delta\). One must not choose a nonmeasurable family of rotations. An explicit Borel orthogonal matrix with \(R(u)e_1=u\) is
\[
 R(u)=I-2\frac{(e_1-u)(e_1-u)^T}{|e_1-u|^2}\ (u\ne e_1),\qquad R(e_1)=I. \tag{G10}
\]
It is a Householder reflection, which is sufficient: orientation does not enter Lebesgue measure. This formula also handles \(d=1\); the transverse variable is then absent. For \(p=R(u)(s,z)\), define the pullback \(g(s,z,\theta)=f_\perp(R(u)(s,z),\theta)\). It is jointly measurable, and \(dp=ds\,dz\) for every fixed \(\theta\ne\theta_0\).

The usual line slicing can be obtained here without an uncountable exceptional-direction claim. Approximate \(f_\perp\) in the Bochner H1 norm by finite sums of measurable theta-simple functions times smooth finite-rank p functions. Pullback by the displayed measurable R preserves the L2 norm; the s derivative of the approximants is
\[
 \partial_s g=(u\cdot\nabla_p f_\perp)(R(u)(s,z),\theta),\qquad
 \|u\cdot\nabla_p f_\perp\|\le
 \left(\sum_i\|\partial_{p_i}f_\perp\|^2\right)^{1/2}. \tag{G11}
\]
The approximants therefore converge in \(L^2(dz\,d\nu;H^1(ds;\mathcal F))\). Their limit is the measurable pullback g and has the stated weak derivative. Consequently for almost every \((z,\theta)\), this actual slice is H1 and (G9) applies. Tonelli is legitimate for its nonnegative bounds, including arbitrary central atoms. Null choices of representatives remain null under the theta-dependent pullback, again by Tonelli and the fibrewise orthogonal change of variables.

## 4. Transversality, zero detuning and the power estimate

The massive Hessian is
\[
 D^2E(k)=\frac{\beta}{E(k)}I-\frac{\beta^2}{E(k)^3}kk^T. \tag{G12}
\]
Its radial eigenvalue is \(\beta M^2/E(k)^3\), and its transverse eigenvalues are \(\beta/E(k)\). All are at least c on \(B_R\). Put \(q=\theta-\theta_0=\delta u\), \(k_0=p+\theta_0+2\pi n_0\). The entire segment \(k_0+tq\), \(0\le t\le1\), lies in \(B_R\) by convexity and (G6), so
\[
 \partial_uD(p,\theta)
 =\delta\int_0^1u^TD^2E(k_0+tq)u\,dt\ge c\delta. \tag{G13}
\]
For a fixed theta and transverse z, the line's intersection with \(B_P\) is an interval. D is strictly increasing along that interval. Its intersection with \(\{|D|\le\epsilon\}\) has length at most \(2\epsilon/(c\delta)\); this follows by integrating (G13) between any two points in that sublevel set. It also covers an empty interval or a tangent slice. The support of f may be nonconvex: it is contained in this interval, which is all the estimate requires.

Multiply that interval length by (G9), then integrate z and theta. For \(r>0\),
\[
 \|\mathbf1_{\{|D|\le\epsilon\}}\mathbf1_{\{\delta>r\}}f\|^2
 \le\frac{\epsilon}{cr\ell}S_\ell^2. \tag{G14}
\]
No differentiability in theta and no finite-dimensional multiplicity assumption was used. At \(\ell=1\), this is stronger by a factor two than the proposed \(2\epsilon\|f\|_{H^1_p}^2/(cr)\) bound. Use \(\delta>r\) here and \(0<\delta\le r\) below so an atom on the radius r is not double counted.

The two pieces are orthogonal. Equations (G5) and (G14) give, for \(0<r\le r_0\),
\[
 \|\mathbf1_{\{|D|\le\epsilon\}}f_\perp\|^2
 \le C^2r^{2a}+\frac{\epsilon}{cr\ell}S_\ell^2. \tag{G15}
\]
For \(0<\epsilon\le\epsilon_*\), choose
\(r=r_0(\epsilon/\epsilon_*)^{1/(2a+1)}\). Both terms have the same power, yielding the claimed norm estimate with its full scale and constant:
\[
 \boxed{\ \|\mathbf1_{\{|D|\le\epsilon\}}(1-P_0)f\|
 \le\bigl(C^2r_0^{2a}+S_\ell^2\bigr)^{1/2}
       (\epsilon/\epsilon_*)^{a/(2a+1)}.\ } \tag{G16}
\]
For larger epsilon the trivial bound \(\|f_\perp\|\) remains available. For \(C,S_\ell>0\), an optional optimizing radius is
\(r_{\rm opt}=[\epsilon S_\ell^2/(2ac\ell C^2)]^{1/(2a+1)}\), provided it is at most \(r_0\); (G15), rather than an unqualified optimizer formula, handles zero constants and all scales. No optimality of the exponent is claimed.

In particular spectral monotone continuity as \(\epsilon\downarrow0\) gives
\(\mathbf1_{\{D=0\}}f_\perp=0\). The following independent algebra proves a stronger zero-kernel statement on the entire supplied chart, without H1 or the central power bound:
\[
 D(p,\theta)=
 \frac{\beta\,[2k_0\cdot q+|q|^2]}{E(k_0+q)+E(k_0)}. \tag{G17}
\]
For every fixed \(\theta\ne\theta_0\), the numerator vanishes on one affine hyperplane of \(\mathbb R^d_p\), hence on a Lebesgue-null set. Fubini with (G3) gives zero residual graph projection. At \(\theta=\theta_0\), D vanishes for all p. Thus on the declared spectral subspace
\[
 \boxed{\ \mathbf1_{\{H-\Sigma(Q)=0\}}=P^V(\{\theta_0\})\ } \tag{G18}
\]
with the smooth chart extension of \(\Sigma\) interpreted only on that subspace. The equality includes all multiplicities. It does not assert a global spectral identity across other lifts or masses, nor does it assert that either side is nonzero.

## 5. Distinct affine-slab control of the geometric step

Rationalization (G17) supplies more than a kernel check. Both energies are at most \(E_*\) on the support. Therefore
\[
 |D|\le\epsilon\quad\Longrightarrow\quad
 \left|u\cdot(k_0+q/2)\right|
 \le\frac{E_*\epsilon}{\beta\delta}. \tag{G19}
\]
On every line this is a containing affine slab of length \(2E_*\epsilon/(\beta\delta)\). Unlike the primary Hessian proof, this calculation uses the exactly quadratic squared dispersion; it does not infer a lower derivative bound. It independently recovers (G14)–(G16), and improves their constant by replacing c with
\(\kappa=\beta/E_*\ge c\). For that improvement use the correspondingly changed scale \(\epsilon_*'=\kappa\ell r_0\). The two routes share the proved one-dimensional Sobolev lemma, so this is a distinct geometric derivation, not complete methodological independence or an independent source review.

For an exact one-dimensional control, let \(x=p+q/2\), \(q=\delta>0\), \(n_0=\theta_0=0\). If \(0<\epsilon<\sqrt\beta\delta\), the positive solution of \(D=\epsilon\) is
\[
 x_\epsilon^2=
 \frac{\epsilon^2(M^2+\beta\delta^2/4-\epsilon^2/4)}
 {\beta(\beta\delta^2-\epsilon^2)}. \tag{G20}
\]
Indeed writing \(A=M^2+\beta x^2+\beta\delta^2/4\), one has
\(D^2=2A-2\sqrt{A^2-\beta^2x^2\delta^2}\). Solving this equation gives (G20); the chosen positive branch satisfies the unsquared sign equation. Since D is odd and increasing in x, the sublevel interval is \([-x_\epsilon,x_\epsilon]\). If \(\epsilon\ge\sqrt\beta\delta\), the whole real line is in the band (the limiting velocity bound), so this endpoint formula must not be used.

For \(g_L(x)=(1-|x|/L)_+\),
\[
 \|g_L\|_2^2=2L/3,\quad\|g_L'\|_2^2=2/L,\quad
 \int_{-t}^t|g_L|^2dx=2(t-t^2/L+t^3/(3L^2)),\quad0\le t\le L. \tag{G21}
\]
Equations (G20)–(G21) predict a finite-atom vector's band norm without using the Hessian inequality as the prediction. They are the companion control's analytic basis. No quadrature, fitted spectral exponent, finite p mesh or tolerance-tuned prefactor replaces the proof.

## 6. Charts, weights, filters and actual regular seeds

Changing a representative of theta and changing \(n_0\) oppositely preserves (G1). Within this theorem the representative and lift are fixed once. Different lifts of the same target centre can have different energy graphs: central projection alone does not select the chosen graph there. A finite partition is legitimate only when its actual spectral pieces and target branches are specified. Smooth compact p cutoffs preserve H1 by the product rule. For a finite smooth partition with \(\sum_j|\chi_j|^2=1\) on the relevant support, \(f\mapsto(\chi_j f)_j\) is an isometric bookkeeping map; its pieces are not extra physical species or duplicate copies in the target Hilbert space. Each piece needs its own valid fixed-lift relation, convex bound and graph statement. If there is one consistent target graph and each piece satisfies these assumptions, square the individual bounds and sum; use the minimum exponent and the finite constants after fixing a common small scale. This sentence does not supply such a consistent graph across crossing branches.

A positive scalar weight \(w(p,\theta)\) can be absorbed by \(f=\sqrt w\,\psi\) only after checking the derivatives in the chosen chart:
\[
 \partial_i f=\sqrt w\,\partial_i\psi+
       \tfrac12(\partial_i\log w)f. \tag{G22}
\]
For instance a weighted H1 norm and a uniform bound \(L_w\) on \(|\nabla_p\log w|\) give
\(\|\nabla f\|\le\|\nabla\psi\|_{L^2(w)}+(L_w/2)\|\psi\|_{L^2(w)}\).
This is a condition on the joint field and its gauge, not on the marginal measure of p. Singular/vanishing weights or merely measurable fibre gauges require another argument and are not covered by this conversion.

For a bounded multiplier m with bounded p gradient,
\[
 S_\ell(mf_\perp)\le\|m\|_\infty S_\ell(f_\perp)
  +\ell\|\nabla_pm\|_\infty\|f_\perp\|,\qquad C_m\le\|m\|_\infty C. \tag{G23}
\]
The derivative follows by the weak product rule and the triangle inequality on the vector \((f,\ell\nabla f)\); the central rate is a commuting-multiplier estimate. Thus supplied regularity survives smooth compact h(K), geometric-chart filters, and the smooth central multiplier of I9. These filters alone do not create a p derivative for a rough wavefunction.

Apply this to actual almost-local creators only under the following explicit seed contract. For every allowed B, the fixed smooth mass filter has already given \(B\Omega\in E_M\mathcal H\) with the required chart support; B and its time derivatives have the filtering source's direct almost-local/transfer properties; and the residual \(J B\Omega\) satisfies (G3)–(G5). Then (G16)/(G18) give the geometric regularity and exact target component for that B. The constants may depend on B and on its chart. The condition is on the actual vacuum vector, not a proxy wavefunction chosen after computing a target.

If a dense one-particle class is needed, it is a further hypothesis or proof obligation:
\[
 \overline{\operatorname{span}\{P^V(\{\theta_0\})B\Omega:
                       B\text{ belongs to this regular direct class}\}}
  =\mathcal H_{0}^{\rm declared}. \tag{G24}
\]
Cyclicity of all local \(A\Omega\) does not prove (G24), since it puts no rate/domain condition on those A. In the full ambient product carrier (G3), H1 vectors with central support either at the atom or a positive distance from it are dense: approximate by smooth compact p functions and cut the off-atom theta support away from \(\theta_0\). This density also holds in the physical carrier (G25), whose multiplicity fibres are independent of p. It is **not** automatic in an arbitrary p-dependent range of J: smoothing can leave that range. Even in dimension one, a scalar range restricted to a positive-measure closed set with empty interior has no nonzero globally H1 sections, since an H1 representative is continuous and vanishes on the dense open complement. A separate range-preserving approximation theorem would be needed there. Even where the abstract density statement is valid, it uses spectral operations at the vector level and is not a construction of almost-local operators. Smooth shrinking central filters only converge strongly on vectors; I17 supplies no uniform almost-local control as their collar shrinks. The distinction remains explicit.

For a finite family of independently admissible creators with positive exponents, the minimum exponent is positive after putting their bounds on a common scale. No uniform exponent or seminorm over a whole countable dense class is proved. If a separate time-averaged scattering theorem assumes a geometric exponent \(\alpha\) and a width exponent \(\nu\in(1/(1+\alpha),1)\), this estimate makes the algebraic interval \(((2a+1)/(3a+1),1)\) nonempty. No time-averaged scattering, Fock, detector or density theorem is imported from the concurrent nonisolated-mass work or proved by that arithmetic observation.

## 7. An explicit scalar massive boost-domain implication

Here is a genuine conditional way to supply (G4), with its measure and domain checked. It is an additional representation assumption, not a consequence of I1–I4. Supply
\[
 \mathcal K=\int_\Theta^\oplus
    L^2(\mathbb R^d_k,dk/(2E(k));\mathcal M_\theta)\,d\nu(\theta), \tag{G25}
\]
where \(\mathcal M_\theta\) is a separable measurable multiplicity field with a supplied measurable embedding into a fixed separable ambient Hilbert space, independent of k. H and current K are multiplication by E(k) and k. The central operators act by \(e^{ij\theta}\). Scalar Lorentz boosts leave theta and multiplicity fixed and act by pullback on \((E,\sqrt\beta k)\):
\[
 (U_i(s)\psi)(k,\theta)=\psi(\Phi_i(-s)k,\theta),\quad
 k_i'=k_i\cosh s+E(k)\sinh s/\sqrt\beta,\quad k_j'=k_j\ (j\ne i). \tag{G26}
\]
For fixed transverse \(y=(k_j)_{j\ne i}\), put
\[
 m_\perp(y)=\sqrt{M^2+\beta|y|^2},\quad
 k_i=m_\perp\sinh t/\sqrt\beta,\quad
 E=m_\perp\cosh t,\quad dk_i/(2E)=dt/(2\sqrt\beta). \tag{G27}
\]
The boost is exactly \(t\mapsto t+s\). Hence (G26) is a unitary strongly continuous translation group on the full real rapidity line, fibre by fibre and then in the direct integral. Strong continuity follows on smooth compact t test functions and theta/multiplicity-simple vectors by dominated convergence, and on all vectors by density and unitarity. There is no half-line boundary condition.

With the convention \(U_i(s)=e^{-is\mathcal B_i}\), the Fourier transform in t identifies the self-adjoint generator and its full domain:
\[
 \mathcal B_i=-i\partial_t=-iE(k)\partial_{k_i}/\sqrt\beta,\qquad
 \operatorname{Dom}\mathcal B_i
 =\{\psi:\partial_t\psi\in L^2(dt\,dy\,d\nu;\mathcal M_\theta)\}. \tag{G28}
\]
This domain statement follows directly from the multiplication generator of translations in Fourier space: its domain is \(\eta\widehat\psi\in L^2\), equivalent to the displayed weak derivative. Pulling back the smooth rapidity diffeomorphism gives the distributional k formula. It is not an inference from agreement of formal commutators on an unspecified core.

If \(\psi\in\bigcap_i\operatorname{Dom}\mathcal B_i\), let \(J_w\psi=(2E)^{-1/2}\psi=:f\) in flat k measure. The weak product rule and (G28) give
\[
 \partial_{k_i}f
  =i\frac{\sqrt\beta}{E}J_w\mathcal B_i\psi
       -\frac{\beta k_i}{2E^2}f. \tag{G29}
\]
Since \(E\ge M\) and
\(\sup_k\beta|k|/(2E^2)=\sqrt\beta/(4M)\),
\[
 \|\nabla_k f\|
 \le\frac{\sqrt\beta}{M}
         \left(\sum_i\|\mathcal B_i\psi\|^2\right)^{1/2}
       +\frac{\sqrt\beta}{4M}\|\psi\|. \tag{G30}
\]
In particular f is H1. After a smooth joint chart cutoff m(k,theta), (G23) supplies the corresponding compactly supported H1 bound. At fixed theta, the change \(k=p+\theta+2\pi n_0\) has derivative \(\partial_p=\partial_k\), so it supplies exactly (G4) in the prescribed lift. The invariant-measure derivative term in (G29) is essential.

The regular domain in (G28) is dense: compact smooth k functions times theta/multiplicity-simple sections form a dense common subspace. Its target-central projection is also dense in the target atom when that atom exists, because central projection commutes with these explicit boosts. This again proves a Hilbert-space domain fact; it does not prove that a cyclic local algebra supplies a dense set of such regular vacuum columns, their central power rate, or a boost action preserving almost-local observables.

For finite spin, a **separately checked** representation formula of the form
\(\mathcal B_i=-iE\partial_{k_i}/\sqrt\beta+A_i(k,\theta)\), with a locally bounded matrix connection and a domain where this equality holds distributionally, gives the same local argument by replacing \(\mathcal B_i\psi\) with \((\mathcal B_i-A_i)\psi\). The connection norms enter the constant. No arbitrary finite-spin or momentum-dependent multiplicity representation is being claimed to have this formula here. The complete scalar proof above is sufficient to answer whether any actual explicit boost-domain assumption can supply H1; identifying it with the microscopic boost and proving the regular seed contract remain separate.

## 8. Preserved counterexamples to specific shortcuts

These are explicit spectral constructions. They test exactly the hypothesis deletions indicated; no construction here is asserted to realize the microscopic finite-range quasi-local dynamics of I1. They do not refute (G16).

**A smooth p marginal does not supply the joint hypothesis.** In one dimension let \(\theta_0=0\), \(M=\beta=1\), and take a nonzero smooth compactly supported density \(|g(p)|^2dp\) inside \((1/4,1/3)\). Let the joint measure be supported on \(\theta=-2p\), with the fixed lift \(n_0=0\). Then \(k=p+\theta=-p\), so \(E(k)=E(p)\): the entire vector has D=0 although its central character stays away from zero. Its p marginal is smooth, and its near-zero central mass is zero for \(r_0<1/2\). It violates (G3), since the joint diagonal is singular to \(dp\,d\nu(\theta)\) for any sigma-finite central measure dominating this continuous diagonal component. To see the last statement, almost every theta has a singleton p fibre, which has zero Lebesgue measure; Fubini makes the diagonal product-null. An extra target-central atom can be added as an orthogonal summand without changing this witness. Thus neither the zero-kernel conclusion nor the positive power bound follows from the smooth Q marginal in I28. The missing step is joint absolute continuity, not a p-derivative estimate on that marginal.

**H1 alone does not give the central rate or the geometric power.** Take central atoms \(\theta_n=e^{-n}\), \(n\ge1\), counting measure, and a fixed normalized \(g\in C_c^\infty((1,2))\). Set \(f_n(p)=g(p)/\sqrt{n(n+1)}\) on the fixed mass \(M=\beta=1\). The sum of squared norms is one and the integrated H1 norm is finite. Since E is 1-Lipschitz, \(|D(p,\theta_n)|\le\theta_n\). At \(\epsilon_N=e^{-N}\), the geometric band contains every component \(n\ge N\), whose squared norm is
\[
 \sum_{n=N}^\infty\frac1{n(n+1)}=\frac1N. \tag{G31}
\]
This exceeds \(K^2\epsilon_N^{2\alpha}\) for all sufficiently large N, for any fixed \(K<\infty\) and \(\alpha>0\). The same tail shows (G5) fails for every positive a. These are compact fixed-lift vectors in a genuine joint product representation. A target atom can again be added independently.

**The central rate alone does not give the geometric power.** Let \(\theta_n=1+1/n\), \(w_n=e^{-n^2}\), and let \(g_n\) be the normalized tent of width \(w_n\) centred at \(p=-\theta_n/2\). Set \(f_n=g_n/\sqrt{n(n+1)}\), again on \(M=\beta=1\). Their p supports lie inside one fixed compact chart, and (G5) holds with C=0 for \(r_0=1/2\), for every a. At the centre of each tent D=0. Since each massive group velocity has absolute value at most one, \(|\partial_pD|\le2\); consequently the whole n-th tent lies in \(|D|\le2w_n\). At \(\epsilon_N=2e^{-N^2}\) the residual squared band norm is at least \(1/N\). This again defeats every positive-power norm bound. The integrated derivative norm is
\(\sum_n3/[n(n+1)w_n^2]=\infty\), so precisely the H1 hypothesis fails. Exact D=0 still has measure zero in this example; absence of a residual atom is strictly weaker than a quantitative rate.

**Mass isolation must be used on the vector.** Let the target mass be M=2, \(\beta=1\), \(\theta_0=0\). On another spectral component choose \(0<p<1/4\), \(\theta=1\), \(k=p+1\), and
\(m(p)^2=3-2p\). Then
\[
 m(p)^2+k^2=4+p^2,\qquad m(p)^2\in(5/2,3). \tag{G32}
\]
A smooth compact p wavefunction on this component lies on the target geometric energy graph and is far from the target centre. Add a target Casimir-4 component: that mass is spectrally isolated from the displayed off-mass interval. Thus having an isolated target mass somewhere in the representation is insufficient if the vector has not actually received \(E_M\). The fixed filter of I18–I19 removes this component exactly. This control does not trade the present isolated mass for a nonisolated mass or borrow the concurrent author's result.

**Different lifts change the target graph.** At \(\theta=\theta_0=0\), \(M=\beta=1\), the \(n=1\) branch has \(E(p+2\pi)\), while the \(n_0=0\) target clock is \(E(p)\). Their squared energies differ by \(4\pi p+4\pi^2\), nonzero on a small compact p chart about zero. A smooth vector on that other branch is entirely in \(P_0\), but not in the selected graph projection. This rejects a global version of (G18) that forgets the fixed lift. It does not prevent correctly specified chartwise branch estimates.

**Boost domain without a checked gauge formula is insufficient for coordinate H1.** In the scalar representation of §7, choose a smooth compact function h nonzero near \(k_1=0\), and the unitary multiplication \(W(k)=e^{i/k_1}\) away from that hyperplane (define its value arbitrarily on the null hyperplane). Conjugate the entire representation by W. The vector Wh belongs to every corresponding conjugated boost domain \(W\operatorname{Dom}\mathcal B_i\). It is not ordinary H1 near \(k_1=0\): on either punctured half-neighborhood, its derivative contains \(-ik_1^{-2}Wh\), which is not L2; any weak H1 derivative must agree with this smooth derivative away from zero. The singular connection in the conjugated boost formula is exactly what (G29) would have omitted. This is a gauge/domain witness, not a failure of the explicit smooth scalar gauge used in §7.

The other deliberate finite defects are algebraic: removing the factor two or beta from (G17), replacing the lower Hessian eigenvalue by the upper bound \(\beta/M\), halving the sharp coefficient in (G9), or omitting the invariant-measure derivative in (G29). The control reports an explicit mismatch for each. The continuous witnesses above, rather than a count of failed finite tests, establish their stated nonimplications.

## 9. No-go discipline: scope check, no universal packet claim

**N1 — actual alternatives.** The positive target is closed conditionally by two real geometric mechanisms: massive Hessian transversality and exact quadratic-energy slabs. The scalar boost-domain mechanism additionally supplies H1 in its explicit representation. The negative statements in §8 each concern one precise deleted hypothesis and carry an explicit witness; their six different deleted hypotheses are not five independent approaches ruling out one common universal target. Accordingly no universal no-go or five-route packet PASS is claimed. That procedural limitation does not replace, enlarge or invalidate the displayed witness proofs. All witness routes are `ATTEMPTED` here; none is labelled ruled out by an uninspected prior verdict.

**N2 — condition relations.** There is no numerical count of independent physical walls. The dependencies that could otherwise be conflated are:

| Pair | Established relation at this scope |
|---|---|
| Joint carrier / H1 | H1 in (G4) is defined in the carrier/trivialization (G3), so they are not counted as independent framework walls. The tent sequence shows the carrier alone does not supply H1. |
| Joint carrier / central rate | A central rate is meaningful without that carrier; the diagonal witness has a central gap but lacks the carrier. Conversely the logarithmic sequence has the carrier and no central power. |
| H1 / central rate, within (G3) | Neither supplies the other: the two sequence constructions prove the two nonimplications. |
| Scalar representation plus boost domains / carrier and H1 | The explicit package (G25)–(G30) supplies both; they are not three independently unresolved claims inside that package. Its identification with the microscopic representation is a separate question. |
| Mass isolation / exact vector restriction | Isolation permits the source's fixed smooth filter; it does not say an arbitrary vector has been filtered. Equation (G32) separates the statements. |
| Chart/lift / any rate | Fixing a lift defines the target D and the graph identity. The other-lift witness changes this predicate; rates for a different predicate are not a substitute. |
| Regular seed class / its target density | Regularity is part of the seed-class definition. Density (G24) is an additional closure statement about that class. No implication from ordinary cyclicity or a count of regular abstract vectors is claimed. Relations to a concrete microscopic seed construction remain unresolved, rather than declared independent. |

**N3 — hidden-condition scan.** The complete proof was checked for implicit representation, domain, cutoff, normalization and multiplicity assumptions. The joint product measure, ambient derivative trivialization, compact support/zero extension, finite lift, exact mass restriction, central rate, boost formula/domain and seed density are explicitly separated in §§2, 6 and 7. The local primitive registry and old Wigner sources are context, not undeclared physical premises. The phrase scan and source-bound self-check are in the companion evidence; it supplies no proof by word matching.

**N4 — residual matching.** I17 is used only for the already proved almost locality of a fixed smooth central filter; its lack of a uniform shrinking-collar estimate is the precise reason a strong vector cutoff is not being promoted here to an exact almost-local creator. I19 supplies exact isolated-mass filtering, not the central rate. I28 supplies a marginal density, whose insufficiency for this joint argument is proved by the new diagonal witness. The old free Dirac sources explain the prior rapidity mechanism only; their spin or realization claims are not witnesses for a microscopic obstruction in this note.

**N5 — resolution.** The counterexamples are individual/direct-integral spectral constructions; the scalar domain calculation is a supplied continuum representation. There is no per-site local-algebra model or lattice-wide impossibility result. The finite control prints separate per-element, per-site, per-mode, per-block and lattice-wide scope statements. No negative theorem is inferred from a finite grid's artificial atom on a crossing hyperplane.

**N6 — live partial closure.** Smooth coordinate and weight changes are mathematical choices with checked derivative effects, not new physical axioms. The explicit scalar-domain calculation is a live route to H1. Central spectral isolation, when actually available, restores the exact filter of I20 and eliminates the residual directly. An integrated central Lorentz decomposition or actual regular-seed construction could supply further hypotheses. Neither is declared impossible or reclassified as requiring a new axiom. Approved scale/isotropy/state primitives are not used as negative walls.

**N7 — strongest challenge to an overbroad negative reading.** A concrete massive representation in which V commutes with the integrated Lorentz action could make the conditional momentum measures absolutely continuous in a common smooth carrier. Actual boost-smooth almost-local vacuum columns, with a checked central spectral rate and dense target components, would then satisfy every premise of the bridge. The task is to construct and verify those columns, not to defeat the spectral counterexamples, which deliberately omit one of these properties. The present filtering source's Lorentz caveat explicitly leaves this route open; §§3–7 give the exact terminal estimates it would need. No conclusion that the microscopic application cannot close is supported here.

**N8 — cross-source comparison.** The frozen filtering theorem already repairs exact central selection when its I5 isolation condition holds; that mechanism is retained as an allowed stronger case. The earlier massive Wigner notes used full-line rapidity instead of a failed common Gaussian analytic-vector claim; the present scalar argument likewise uses the actual translation generator and never revives that rejected route. The bounded source search and complete reads are logged. No full campaign-wide obstruction search or audit status review is claimed, because this artifact makes no universal obstruction assertion.

## 10. Evidence, failures and handoff

The complete mathematical argument is §§2–7. Its two geometric derivations share the one-dimensional Sobolev input; the scalar-domain implication is proved separately from its explicit unitary flow. There is no Lean claim, admitted theorem presented as checked, or new external theorem import. Ordinary measure theory, weak differentiation and the Fourier characterization of the full-line translation generator are used with their actual hypotheses shown. At author freeze a fresh source review was required for the general direct-integral slicing, graph projection, weights and domain matching before substantial downstream reuse; the completed source review is recorded below.

The companion `analytic_control.py` uses exact fractions for squared-energy and endpoint polynomial identities, and 75-digit Decimal arithmetic for a separate bisection of the original energy difference. It integrates the compact tent profiles by (G21); it does not use a Hessian bound to predict the endpoints or measured band mass. Its finite central atoms have a nontrivial two-component multiplicity normalization. The finite examples support the checked algebra and discriminate the listed defects; they cannot verify the general Bochner slicing proof or physical realization.

The first control execution was declared with a 60-second timeout, exited 0 in **0.082806 seconds**, and wrote 6,759 stdout bytes with empty stderr. Three independent energy-root comparisons had maximum endpoint difference **2.71521e-70** against a fixed **1e-60** tolerance. Four finite band evaluations satisfied both Hessian and affine-slab bounds. Eight explicit defect comparisons were rejected at their witnessed identities or inequalities. Three telescoping-tail controls support the exact sequence arithmetic; the infinite-sequence consequences are established analytically in §8. The run did not test a microscopic lattice model. Source cleanup/reproduction and final freeze metadata are recorded separately in the final receipt so a later source revision cannot silently reuse this execution.

The final revised control additionally checks eight exact exponent balances and four rational Householder selectors, directly differentiates the invariant weight by a fixed 75-digit finite difference, and evaluates the two actual lift-energy formulas. It ran under a separate 60-second timeout, exited 0 in **0.077857 seconds**, and wrote 7,225 stdout bytes with empty stderr. Final control source SHA-256: `b0623963415f4b0ad04b035832c5be793404eb885933c9150cd58133dcc4fbfb`. Its complete output and exact start/end times are in `centre_regularity_to_geometric/logs/analytic_control_frozen_candidate.*`. These refinements changed the control implementation; both prior implementations and their successful logs remain preserved.

Preserved operational failures: the initial runner wrapper invocation put its timeout option after the positional `REMAINDER` name and failed before reading sources; the fixed runner logs OSError as well as timeouts and captures stdin source. Initial broad file-discovery and source-search displays were truncated; the latter complete stdout is retained, and the scientific prerequisites and matched boost arguments were subsequently read in complete bounded segments. No truncated display is treated as scientific verification. A pre-freeze author source check found and corrected one density overstatement: H1 density in the ambient product space need not hold in an arbitrary momentum-dependent spectral range. The original draft and exact correction are preserved; §6 now distinguishes that range from the p-independent scalar representation. No mathematical baseline control failed or timed out. Any later failures are recorded in the companion logs and receipt rather than overwritten.

Frozen author operational record: Only this note and `centre_regularity_to_geometric/` are writable outputs. The root owns publication and repository changes. No Git ref/write, PR, audit verdict, axiom, editable prompt, other-chat or subdelegation action was performed. Read-only git source/ref inspection is recorded explicitly. Editable prompt files changed: **none**. The fixed campaign deadline is **2026-10-12 16:00:52 UTC**.

**Frozen author handoff:** the elementary conditional bridge was ready for independent source review. Publication update: that source review is complete. The exact remaining application obligations are a supplied/proved joint representation with the declared trivialization, regularity and rate of actual almost-local seed vectors, and density of their target vectors. The scalar boost result supplies one conditional H1 mechanism; it does not discharge those seed or physical-identification obligations. The concurrent nonisolated-mass result may later consume (G16) only through its own independently checked hypotheses. No full scattering, Fock, detector, asymptotic completeness, index escape or TOE closure is asserted.


## Publication evidence and review record

The frozen author source is `CENTRE_REGULARITY_TO_GEOMETRIC_PROBE.md`, SHA-256 `9ec8c3148442f981d6b3d4d38027ffde0d2a64adbd6e4664d6a24b5d3d06608a`.
The separate source review is `CENTRE_REGULARITY_TO_GEOMETRIC_REVIEW.md`, SHA-256 `bdeb88293de00f16e45a6747f46edda8c3391db5fdf3f1503c7a584b68ac3703`,
with review receipt SHA-256 `0032ce4b7688228cc8200acd2997ac0978474f5ee8c6347636349a215798e6bc`. The complete source,
review, controls, output streams, failures, source revisions and root coverage
records are indexed by the [evidence map](../.claude/science/physics-loops/toe-regularity-joint-flow-20261012/EVIDENCE_MAP.json).
The [exact transformation map](../.claude/science/physics-loops/toe-regularity-joint-flow-20261012/PUBLICATION_EDITS.json) and
[reconstruction program](../.claude/science/physics-loops/toe-regularity-joint-flow-20261012/reconstruct.py) recover the entire note
and primary from their frozen bytes. Historical write-scope and pending-review
statements above describe the author freeze; the following record describes
the completed source review. Root contributed the mechanisms and is a coauthor,
not the independent reviewer. No new review was performed by the packaging worker.

The review supports the complete G1-G32 conditional source without a required
mathematical correction. The source's earlier density overstatement is retained
as history with its complete correction diff: ambient H1 density does not give
H1 density in an arbitrary momentum-dependent physical range. The final source
already distinguishes that range, the full product carrier, the explicit scalar
carrier and actual almost-local operator columns.

The reconstruction and distinct controls froze before opening the current
author helper/output or the earlier density draft; the candidate proof and
its descriptions of controls and witnesses were visible. Root's preliminary
view and source freshness message are disclosed in the review. The independent
line proof uses Fourier Cauchy-Schwarz. Separate two-dimensional energy
bisection and the actual boost pullback test geometry and the invariant-measure
term. These are distinct finite checks, not blind checking or proof by counts.

The original helper's upper-bound gates allow two wrong tent integrals to
survive: zero mass and deletion of the quadratic term. A separate exact
rational Simpson integration of the actual squared tent matched the authentic
function and rejected both. The canonical helper keeps the original calculations
and their limitation; it does not silently add a new gate. All surviving and
rejected mutants and the post-evidence exact check are preserved. The analytic
source's tent formula is unchanged. The original helper reproduced all 7,225
stdout bytes; publication adds only declarations, an assertion guard and
completion/scope lines. The scalar domain implication does not construct
actual boost-regular almost-local seeds, a dense regular creator class or an
identified microscopic representation.


The [canonical finite primary](../scripts/centre_regularity_to_geometric_2026_10_12.py) is separate from the
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
