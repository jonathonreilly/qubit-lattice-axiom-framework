---
claim_id: isolated_centre_filtering_bounded_theorem_note_2026-10-12
claim_type: bounded_theorem
claim_scope: "Actual implemented commuting finite-range flows, isolated positive mass and explicit mass-momentum restricted central spectral isolation give exact almost-local creators for arbitrary selected characters, with covered scattering, Fock and fixed-arrangement detector extensions under their separately stated hypotheses. No common finite order, microscopic realization or exhaustion follows."
upstream_dependencies:
  - compact_patch_scattering_covariance_bounded_theorem_note_2026-10-11
  - compact_patch_fock_isometry_bounded_theorem_note_2026-10-12
  - compact_detector_convergence_bounded_theorem_note_2026-10-12
runner: scripts/isolated_centre_filtering_2026_10_12.py
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: upstream_support
reachability_to_target: partially_closes
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# Exact creator filtering at isolated central characters

**Claim type:** conditional bounded theorem. **Status:** complete separate source review supports I1–I34; no applied audit verdict or retained status. This note replaces one supplied finite-order centre-selection hypothesis by the explicit spectral-isolation hypothesis below. It does not change an axiom or establish a microscopic realization, the existence of irrational isolated characters, full-GNS exhaustion, or the absence of other index obstructions. Root proposed the smooth-filter route and is a contributor.

The new estimate proves that a smooth Fourier sum of the actual automorphisms \( \nu_j=\operatorname{Ad}V_j \) preserves almost locality and every available norm time derivative. On the vacuum this sum is a smooth spectral multiplier of V. On full operators it filters **central transition differences**, not the outgoing central character alone. This distinction permits exact one-particle selection without asserting a global operator projection. A finite collection of selected isolated characters may contain irrational characters; the compact scattering, Fock and fixed-arrangement detector arguments survive at the precise scope stated below. Their common finite-order conclusion does not.

## 1. Exact source contract and supplied setting

S denotes the original research collection. The [complete milestone packet](../.claude/science/physics-loops/toe-centre-current-20261012/) preserves frozen sources, author evidence and independent review. The in-branch proof dependencies are [compact creators](COMPACT_PATCH_SCATTERING_COVARIANCE_BOUNDED_THEOREM_NOTE_2026-10-11.md), [Fock isometry](COMPACT_PATCH_FOCK_ISOMETRY_BOUNDED_THEOREM_NOTE_2026-10-12.md) and [detector convergence](COMPACT_DETECTOR_CONVERGENCE_BOUNDED_THEOREM_NOTE_2026-10-12.md). The following frozen sources are unchanged. Labels SC, F and C refer to their displayed equations or sections.

| Source | SHA-256 | Use |
|---|---|---|
| COMPACT_PATCH_SCATTERING_COVARIANCE_PROBE.md | d1d8ace7a450e0c00d780443f83a333223fff395b170994a83e1b65653302a4a | S1–S4, actual current/geometric flows, joint mass filter, LR estimate, direct creator/Cook/covariance proofs; its finite-q selector is replaced here |
| COMPACT_PATCH_SCATTERING_EX_PUBLICATION_REPAIR.md | d4aac1e14a20e82be994bd4b8de966f0063affcbaa22a40a173b126f77fa3516 | Separate unique-vacuum/gap scope |
| COMPACT_PATCH_FOCK_ISOMETRY_PROBE.md | 9bc3a309e8fc35978bcac0c360b8557fb6a3c4484cfc2034a277a94072369404 | Direct-property Fock proof F3–F19 and the first covariance identity in F20 |
| COMPACT_PATCH_FOCK_ISOMETRY_REVIEW.md | bc88af1dda77065d8806da9d689546547f40847a340177086793dab5f3a277cf | Separate predecessor review; does not check this extension |
| COMPACT_DETECTOR_CONVERGENCE_PROBE.md | bed0584922876c64de1658f3135390420b703dd661edf5076e02a0a36af34d64 | Direct fixed-arrangement hypotheses and C1–C28 |
| COMPACT_DETECTOR_CONVERGENCE_REVIEW.md | 2f9ebfed745c217d97750ddc5f7a5edeaffaede72895ad0da1af0974ef2c51f0 | Separate review at the unchanged PC source, not of this new filtering |

The read-only working tree was 296155eda2ca6a5ab6ae6307190362b9a84ea690 at launch and advanced concurrently to 5cbc581504721a323f5fa2064694a67141a3ee98 during root's projection publication. The complete changed-path inventory was checked against this proof's repository inputs; their bytes are unchanged, and that publication is not imported here. Planning instructions are bound at 3a4b2c66a1ead7a1c48b4359627e968f681e3c39. The source ledger records complete reading, earlier reading reused at verified identities, and limits. The independently checked status of predecessor proofs does not supply an independent check of this note.

Keep the original finite-dimensional-site quasi-local algebra on \(\mathbb Z^d\), cyclic vacuum GNS representation, positive H, and the actual finite-range bounded microscopic interactions implementing the commuting flows
\[
\alpha_t=\operatorname{Ad}e^{itH},\qquad
\rho_y=\operatorname{Ad}e^{-iy\cdot K},\qquad
\tau_x=\operatorname{Ad}T_x,\quad T_x=e^{-ix\cdot Q}.
\tag{I1}
\]
H and the components of K strongly commute; their implementers commute with T. Every implementer fixes \(\Omega\), and \(H\Omega=K\Omega=0\). K is the continuous current momentum \(P/\beta\), not a boost generator. Assume \(\beta>0\). In particular
\[
V_j=e^{ij\cdot K}T_j,\quad
\nu_j=\operatorname{Ad}V_j=\rho_{-j}\tau_j,\quad j\in\mathbb Z^d
\tag{I2}
\]
is a unitary representation of \(\mathbb Z^d\), implements actual automorphisms of the quasi-local algebra, fixes the vacuum, and commutes with all flows in (I1). No finite-order identity for V is assumed.

The joint spectral measure of V is denoted \(P^V(d\theta)\), with the convention
\[
V_j=\int_{\mathbb T^d}e^{ij\cdot\theta}P^V(d\theta).
\tag{I3}
\]
It commutes with the spectral measures of H and K. The word “centre” names these character labels; it does not assert that their spectral projections are central elements of the observable algebra.

Keep the original isolated positive mass-Casimir hypothesis: for a selected \(M>0\), \(E_M=\mathbf1_{\{M^2\}}(H^2-\beta|K|^2)\) is nonzero and \(M^2\) is isolated in that self-adjoint operator's spectrum. Thus on \(E_M\mathcal H\),
\[
H=\varepsilon_M(K),\qquad \varepsilon_M(k)=\sqrt{M^2+\beta|k|^2}.
\tag{I4}
\]

Here is the precise new condition, including its possible restricted coverage. For each selected pair \((M,\theta)\), declare a countable collection of bounded open continuous-momentum patches \(O_{M,\theta,\ell}\). Each can be refined into relatively compact lift charts for \(k\mapsto k-\theta\pmod{2\pi}\). For each patch there is an open torus neighborhood \(U_{M,\theta,\ell}\) of \(\theta\) such that
\[
E_M\,\mathbf1_{O_{M,\theta,\ell}}(K)\,
P^V\bigl(U_{M,\theta,\ell}\setminus\{\theta\}\bigr)=0.
\tag{I5}
\]
There is no required uniform neighborhood size. Put
\[
O_{M,\theta}^{\rm cov}=\bigcup_\ell O_{M,\theta,\ell},\quad
\Pi_{M,\theta}=E_MP^V(\{\theta\}),\quad
\mathcal H_{M,\theta}^{\rm cov}
=\Pi_{M,\theta}\mathbf1_{O_{M,\theta}^{\rm cov}}(K)\mathcal H .
\tag{I6}
\]
Zero summands may be omitted. Nonzero coverage, when claimed, means this last projection is nonzero. Countability is no effectiveness claim; open subsets of \(\mathbb R^d\) have countable bases. The condition is on the **whole mass/patch spectral subspace**, not just on one vacuum vector. It includes all points of \(\operatorname{supp}h\) whenever \(h\in C_c^\infty(O_{M,\theta,\ell})\). No claim about the uncovered momenta is implied.

A sufficient stronger special case is that \(\theta\) is an isolated point in the joint V spectrum on \(E_M\mathcal H\). An open U then meets that restricted spectrum only at \(\theta\), giving (I5) on every momentum patch. Its point spectral projection is nonzero: otherwise that open spectral neighborhood would have zero projection, contrary to being a point in the support of the restricted spectral measure. This condition allows arbitrary torus characters, with no rationality requirement. Conversely (I5) does not infer global isolation; other momenta may carry nearby characters.

This local sufficient criterion is stated in the minimal commuting-flow/mass setting (I1)–(I5). No integrated Lorentz action or representation disintegration is proved or used. In a stronger setting where V commutes with an integrated Poincaré action, mass/central components may each carry the full mass hyperboloid, and local and global central spectra on nonempty momentum patches may then coincide. That disintegration has not been checked here. No strict weakening in that stronger representation class, or new physical escape from its constraints, is asserted.

## 2. Smooth central filtering: signs, operator meaning and derivatives

For \(\phi\in C^\infty(\mathbb T^d)\), set
\[
c_\phi(j)=\int_{\mathbb T^d}e^{-ij\cdot\vartheta}\phi(\vartheta)
                         \frac{d\vartheta}{(2\pi)^d},\qquad
\phi(\vartheta)=\sum_jc_\phi(j)e^{ij\cdot\vartheta}.
\tag{I7}
\]
Integrating \((1-\Delta)^L\phi\) by parts gives
\(\lvert c_\phi(j)\rvert\le C_L(1+|j|^2)^{-L}\).
Thus every polynomially weighted \(\ell^1\) coefficient sum is finite. Define the bounded linear map on the quasi-local algebra
\[
\mathcal C_\phi(B)=\sum_{j\in\mathbb Z^d}c_\phi(j)\nu_j(B),
\qquad
\|\mathcal C_\phi(B)\|\le\|c_\phi\|_{\ell^1}\|B\|.
\tag{I8}
\]
The series is absolutely norm convergent. Since \(V_j^*\Omega=\Omega\),
\[
\mathcal C_\phi(B)\Omega
=\sum_jc_\phi(j)V_jB\Omega=\phi(V)B\Omega.
\tag{I9}
\]
The series equality with the joint functional calculus follows from uniform Fourier convergence and the bounded spectral calculus. The minus sign in the coefficient integral is essential. Using the geometric-filter coefficient sign instead gives \(\phi(-\theta)\) on a character \(\theta\).

Equation (I9) is only the vacuum-column identity. If \(\xi,\eta\) are exact V-eigenvectors with phases \(\theta_{\rm out},\theta_{\rm in}\), then
\[
\langle\xi,\mathcal C_\phi(B)\eta\rangle
=\phi(\theta_{\rm out}-\theta_{\rm in})\langle\xi,B\eta\rangle .
\tag{I10}
\]
The inner product is antilinear in its first argument. This follows by inserting \(V_jBV_j^*\); it also describes the spectral-block multiplier by approximation for general spectral subspaces. In particular \(\mathcal C_\phi(B)\) is generally not \(\phi(V)B\), is not a projection of B onto an exact outgoing centre, and need not be an eigenoperator for \(\nu\). Absolute summability justifies
\[
\mathcal C_\phi\mathcal C_\psi=\mathcal C_{\phi\psi},\qquad
\mathcal C_\phi(B)^*=\mathcal C_{\phi^\sharp}(B^*),\quad
\phi^\sharp(\vartheta)=\overline{\phi(-\vartheta)}.
\tag{I11}
\]
Even a real \(\phi\) need not give a *-preserving map. If \(B^*\Omega=0\), however, each transformed adjoint annihilates \(\Omega\), so \(\mathcal C_\phi(B)^*\Omega=0\) directly. An idempotent vacuum multiplier on a selected subspace does not make \(\mathcal C_\phi\) globally idempotent.

The map commutes with every action in (I1) and with all their absolutely integrable smearings. If B has a norm derivative \(\delta_H B\), boundedness and
\(\alpha_t\mathcal C_\phi(B)=\mathcal C_\phi(\alpha_t B)\) permit the norm difference quotient:
\[
\delta_H^a\mathcal C_\phi(B)=\mathcal C_\phi(\delta_H^aB)
\tag{I12}
\]
for every norm derivative that B possesses, including all orders for the joint smooth creators below. The same assertion holds for any supplied norm current derivatives. No term proportional to j appears: the relevant flows commute.

Likewise this map does not enlarge **full operator** H/current transfer. One direct formulation is enough: if a test smearing with joint Fourier multiplier vanishing near the transfer support of B annihilates B, the same smearing annihilates \(\mathcal C_\phi(B)\), by (I8) and commutation. This is the defining annihilator characterization of transfer support. It proves preservation of the joint support, not just of its temporal projection. The same argument preserves any already imposed geometric operator-transfer support. On vectors the commuting spectral calculus also preserves the exact mass component and any exact graph support already present; a full operator mass-shell projection is not asserted.

## 3. The new uniform lattice-parameter almost-locality estimate

Norm convergence of (I8) alone would not prove almost locality. We now use the finite-range current implementations. Let \(\Lambda_R\) be the lattice ball of radius R about the origin, using a fixed lattice norm, and let \(\mathbb E_{\Lambda_R}\) be its contractive conditional expectation. For almost-local B, its norm-bounded approximants \(B_r=\mathbb E_{\Lambda_r}(B)\) obey
\[
\|B-B_r\|\le a_N(B)(1+r)^{-N},\qquad \|B_r\|\le\|B\|
\tag{I13}
\]
for every N. This follows from any almost-local approximants by contractivity, at a cost of a factor two.

For each of the d coordinate current flows the already supplied finite-range LR estimate SC (8) gives, after taking common constants for this finite list,
\[
\|(1-\mathbb E_{X^{r}})\rho_{u e_a}(D)\|
\le C_0|X|\|D\|e^{-\lambda(r-v|u|)}
\tag{I14}
\]
for local D supported in X. Constants absorb the fixed lattice norm. A ball slightly larger than \(X^r\) gives the same bound up to a harmless factor two by conditional-expectation contractivity. The estimates do not require a spectral gap for the current generators.
The physical H flow has the same finite-range estimate with its own constants; only the d current-flow constants enter the next lattice-parameter bound.

Fix
\[
c=\frac1{8d(1+v)}.
\]
For large R and \(|j|_1\le cR\), start with
\(D_0=\tau_j(B_{R/4})\), supported in
\(\Lambda_{R/4+|j|_1}\). Apply the d current-coordinate flows in succession. After the a-th flow, apply the conditional expectation onto the ball with radius
\[
r_a=R/4+|j|_1+aR/(2d).
\]
Denote the resulting local operator by \(D_a\). The padding at each step is \(R/(2d)\), every intermediate norm is at most \(\|B\|\), and every intermediate support has at most \(C_d(1+R)^d\) sites. Moreover
\[
R/(2d)-v|j_a|\ge3R/(8d),\qquad r_d\le7R/8<R .
\tag{I15}
\]
Integer rounding costs only a fixed constant; one may replace the first exponent margin by \(R/(4d)\) for all sufficiently large R. Telescope the d truncation errors using isometry of each untruncated flow. Commutativity identifies the untruncated composition with \(\rho_{-j}\tau_j\); this yields uniformly over \(|j|_1\le cR\)
\[
\|\nu_j(B)-D_d\|
\le a_N'(B)(1+R)^{-N}
\mathbin{+} C_d'(1+R)^d\|B\|e^{-\lambda R/(4d)}.
\tag{I16}
\]
The geometric displacement \(|j|_1\) has been included before the current flows; omitting it would not justify localization in \(\Lambda_R\).

Use these \(D_d=D_{R,j}\) in the finite local sum
\[
B_{\phi,R}=\sum_{|j|_1\le cR}c_\phi(j)D_{R,j}\in\mathcal A(\Lambda_R).
\]
The remaining terms are bounded by their norms, rather than by an exponentially growing LR estimate:
\[
\begin{split}
\|\mathcal C_\phi(B)-B_{\phi,R}\|
\le{}&\|c_\phi\|_1 a_N'(B)(1+R)^{-N}\\
&+\|c_\phi\|_1 C_d'(1+R)^d\|B\|e^{-\lambda R/(4d)}
\mathbin{+}\|B\|\sum_{|j|_1>cR}|c_\phi(j)|.
\end{split}
\tag{I17}
\]
The tail is \(O(R^{-N})\) for every N by (I7). Thus \(\mathcal C_\phi(B)\) is almost local. There is no count of small-j terms in the first two bounds: their coefficients were summed in \(\ell^1\). Applying exactly this proof to each \(\delta_H^aB\), followed by (I12), proves almost locality of every required norm time derivative.

For fixed j, the same construction with only the finitely many flows proves that \(\nu_j\) preserves the direct class. Fixed physical/current translations have the same property from (I14), and a fixed geometric shift only moves the support. Constants can depend on the fixed transformation, \(\phi\), the isolation collar and the packet. Nothing here is uniform as isolating neighborhoods shrink, \(|j|\) grows with scattering time, or infinitely many species/patches are combined.

## 4. Exact joint mass/centre selection and covered one-particle density

Fix one patch in (I5) and \(h\in C_c^\infty(O_{M,\theta,\ell})\). Choose a smooth compact real function \(\eta\) supported inside the mass-Casimir isolating neighborhood and equal to one at \(M^2\). Choose \(\chi\in C_c^\infty((0,\infty))\), equal to one on \(\varepsilon_M(\operatorname{supp}h)\). For local A set
\[
G(E,k)=\chi(E)h(k)\eta(E^2-\beta|k|^2),\qquad
g(s,y)=\frac1{(2\pi)^{d+1}}\int e^{-iEs+ik\cdot y}G(E,k)\,dE\,dk,
\]
\[
B_g(A)=\int_{\mathbb R^{d+1}}g(s,y)\alpha_s\rho_y(A)\,ds\,dy.
\tag{I18}
\]
G is smooth and compactly supported; g is Schwartz. The original SC joint-smearing proof uses (I14) for the finite H/current flows, cutting the smearing variables into a region of size proportional to R and a Schwartz tail. It proves almost locality. Differentiating by shifting the s integration variable gives \(\delta_H^aB_g(A)=B_{(-\partial_s)^ag}(A)\); these are almost local by the identical bound. Its whole joint H/K operator transfer lies in \(\operatorname{supp}G\), as applying another joint smearing multiplies G. Its temporal transfer is in some compact \(I=[\epsilon,L]\subset(0,\infty)\). This is positive temporal operator transfer, not just a property of \(B_g(A)\Omega\).
In particular \(B_g(A)^*\Omega\) would have H spectrum in \([-L,-\epsilon]\), which is empty because \(H\ge0\); thus it is zero. Vacuum invariance then preserves this annihilation under the central and geometric filters.

The vacuum calculation with the signs in (I18) is
\[
B_g(A)\Omega=G(H,K)A\Omega=h(K)E_MA\Omega.
\tag{I19}
\]
Here the isolated Casimir first selects \(E_M\), positivity of H fixes the branch in (I4), and \(\chi\) is exactly one on the remaining compact momenta. No geometric shell isolation is used.

Choose \(0\le\phi\le1\), smooth on the torus, equal to one on a neighborhood of \(\theta\) and with \(\operatorname{supp}\phi\subset U_{M,\theta,\ell}\). Such a bump exists with its support strictly inside U, also when the torus coordinate cut crosses \(\theta\). Define
\[
B_{M,\theta,h}(A)=\mathcal C_\phi(B_g(A)).
\]
By (I5), including the closed support of h, the exact joint functional-calculus identity is
\[
\phi(V)h(K)E_M
=P^V(\{\theta\})h(K)E_M,
\qquad
B_{M,\theta,h}(A)\Omega=\Pi_{M,\theta}h(K)A\Omega.
\tag{I20}
\]
Indeed \(\phi- \mathbf1_{\{\theta\}}\) vanishes outside U, vanishes at \(\theta\), and its remaining spectral contribution on this mass/patch subspace vanishes by (I5). All factors commute. This proves exact selection on the whole declared mass/patch spectral subspace, not approximate selection on its vacuum vector alone.

Equations (I12), (I17) and the transfer argument prove all original direct creator properties for this B: almost locality with all norm time derivatives; the same compact joint H/K transfer and positive temporal interval; \(B^*\Omega=0\); and exactly the selected mass and character on the vacuum. The centre filter and the joint H/K filter commute as bounded smearings, with Fubini justified by their \(\ell^1\) and \(L^1\) norms. The proof of exact selection nevertheless uses the already mass/momentum-filtered subspace in (I20); applying a bump to an arbitrary unfiltered vacuum vector would not supply that premise.

On this exact character the relation (I2) gives
\[
T_j\psi=e^{-ij\cdot K}e^{ij\cdot\theta}\psi,\qquad
Q=k-\theta\pmod{2\pi}.
\]
In a lift chart write \(k=p+\theta+2\pi n\). The exact dispersion is therefore
\[
\Sigma_{M,\theta,n}(p)
=\sqrt{M^2+\beta|p+\theta+2\pi n|^2}.
\tag{I21}
\]
Both signs follow from \(T_j=e^{-ij\cdot Q}\); changing a representative of \(\theta\) only relabels n. Irrationality creates no chart-boundary term.

For detector use impose the additional full geometric operator filter. Choose a smooth \(\zeta\) supported compactly in the torus chart and equal to one near the image of \(\operatorname{supp}h\), and put
\[
\mathcal G_\zeta(B)=\sum_z b_\zeta(z)\tau_z(B),\qquad
b_\zeta(z)=\int_{\mathbb T^d}e^{ip\cdot z}\zeta(p)\frac{dp}{(2\pi)^d}.
\tag{I22}
\]
This coefficient sign is the opposite of (I7), because \(T_z=e^{-izQ}\). The vacuum multiplier is \(\zeta(Q)\). The full geometric operator transfer is contained in \(\Lambda=\operatorname{supp}\zeta\); applying another geometric filter multiplies their multipliers, proving the support assertion for the full operator. A small-translation/Schwartz-tail split proves almost locality, also for all time derivatives. It commutes with \(\mathcal C_\phi\) and the joint H/K filter and preserves their temporal transfer. At the stated choice of \(\zeta\) it preserves the vector in (I20). For a later packet refiltering it is enough that \(\zeta=1\) near that packet's vacuum support; creator-independence below then preserves its scattering vector.

The selected mass/centre chart relation (I21) is a **vacuum** graph statement. Equation (I22) supplies the different, load-bearing **full operator** geometric transfer statement. Neither says the global H/Q spectrum has an isolated shell. Smooth real dispersion extensions to the entire torus can be chosen separately for each species/chart, equal to (I21) on a neighborhood of \(\Lambda\); compact containment leaves a collar for the extension.

The vectors in (I20), and hence their geometrically filtered versions, span a dense subspace of \(\mathcal H_{M,\theta}^{\rm cov}\). To see the quantifiers explicitly, a vector \(\psi\) in that subspace orthogonal to all of them obeys
\(\overline h(K)\Pi_{M,\theta}\psi=0\) for each \(h\in C_c^\infty(O_{M,\theta,\ell})\), by cyclicity of local \(A\Omega\). Smooth cutoff exhaustion of each open patch gives
\(\mathbf1_{O_{M,\theta,\ell}}(K)\psi=0\). The countable union is the whole declared support of \(\psi\), so \(\psi=0\). Refining a patch into lift charts does not lose density: a finite smooth partition on each compact support of h, then countable exhaustion, gives the same argument. Choose each packet amplitude equal to one on the geometric image of that compact support to realize the same vector as a packet vacuum vector. Charts are overlapping coordinate descriptions of one spectral subspace, not extra copies in a direct sum.

Thus full density in \(\Pi_{M,\theta}\mathcal H\) follows if the declared coverage has full spectral projection there, for example if its open union is \(\mathbb R^d\). Otherwise the proven density is exactly the covered subspace (I6). A patchwise condition does not silently become an all-momentum or all-channel condition.

## 5. Which scattering, covariance, Fock and detector proofs extend

For the new creator B and a smooth compact chart amplitude, set
\[
f_t(x)=\int e^{ip\cdot x-it\Sigma(p)}\widehat f(p)\frac{dp}{(2\pi)^d},
\qquad C_t(B,f)=\sum_x f_t(x)\alpha_t\tau_x(B).
\tag{I23}
\]
The exact graph gives \(C_t(B,f)\Omega=\widehat f(Q)B\Omega\), independent of t, and \(C_t(B,f)^*\Omega=0\). The norm derivative has both terms
\[
\partial_t C_t(B,f)=C_t(\delta_HB,f)+C_t(B,f^{(1)}),
\qquad \widehat f^{(1)}(p)=-i\Sigma(p)\widehat f(p).
\tag{I24}
\]
The new filter commutes with \(\delta_H\); it creates no omitted time-dependent remainder.

For each fixed finite family with internally disjoint compact velocity supports, SC §§4–6 now apply to these direct properties. In particular all derivative/adjoint equal-time commutators are rapid after common \(\alpha_t\) is removed. Each packet norm is \(O((1+|t|)^d)\); a pairwise derivative commutator is \(O((1+|t|)^{2d-N})\), from almost locality and off-velocity Schwartz packet tails. In the derivative of an n-factor product, commuting the differentiated factor to the vacuum leaves every one of the n−2 other factors. The resulting bound is
\[
\|\partial_t(C_{1,t}\cdots C_{n,t}\Omega)\|
\le c_N(1+|t|)^{nd-N}.
\tag{I25}
\]
Take \(N=nd+2\); for n=1 the derivative is exactly zero. Incoming and outgoing Cook limits, permutation symmetry and multilinearity follow as before. The estimates depend on fixed filters and separations, not on a common finite order.

SC §7 creator-independence is a direct-property argument and also survives. A difference packet whose one-particle vector is zero kills the vacuum at every t; move it right and use the same rapid commutators with all remaining factors. If equal one-particle vectors have different admissible packet cutoffs, insert cutoffs near their common spectral support. Every discarded \((1-h)\widehat f\) piece remains inside the original packet support and kills the vacuum; its commutators therefore still have the original separation. Finite local partitions compare common charts, while (I20) supplies exact equality of the selected vectors. A common q is not used. With the additional Fock hypotheses below, the Gram identity supplies the full well-defined extension across charts and creator realizations.

For any fixed j, \(\nu_j\) preserves the direct properties by §§2–3 and commutes with all filters and the packet flow. Although B need not be a V-eigenoperator, \(\nu_j(B)\Omega=e^{ij\theta}B\Omega\). Fixed conjugation may therefore pass through each finite-time packet product and its strong limit; creator-independence gives
\[
V_j\Psi^\pm(\psi_1,\ldots,\psi_n)
=\Psi^\pm(V_j\psi_1,\ldots,V_j\psi_n)
=e^{ij\cdot(\theta_1+\cdots+\theta_n)}
 \Psi^\pm(\psi_1,\ldots,\psi_n)
\tag{I26}
\]
for character-homogeneous inputs. The same reasoning gives fixed physical/geometric/current translation covariance. No transformed strictly local seed, or estimate uniform over j, is required.

For Fock isometry add exactly F1:
\[
\ker H=\mathbb C\Omega,\qquad
\operatorname{spec}(H)|_{\Omega^\perp}\subset[\gamma,\infty),
\quad\gamma>0,
\tag{I27}
\]
with the original finite-range H interaction. For a **finite** collection of distinct selected \((M,\theta)\), take the actual orthogonal Hilbert sum
\(\mathcal H_1^{\rm cov}=\bigoplus_{(M,\theta)}\mathcal H_{M,\theta}^{\rm cov}\).
Distinct mass or character projections are orthogonal; finite order is unnecessary for that assertion. The following is the exact dependency check on the Fock proof.

| Fock step | Hypotheses supplied here and unchanged proof |
|---|---|
| F7–F9 finite-energy bounds | Almost-local commutator sum and strictly positive compact temporal transfer from (I18)–(I22). The common kernel of all mixed lowering words and the creator's upper-energy padding remain required. No centre-order input occurs. |
| F10–F11 regular packet bounds | For \(k=p+\theta+2\pi n\), \(D^2\Sigma=\beta E^{-1}1-\beta^2E^{-3}kk^{\mathsf T}\) and \(\det D^2\Sigma=\beta^dM^2/E^{d+2}>0\). Translation of k by an arbitrary fixed \(\theta\) does not change this identity. Smooth compact chart supports remain required. |
| F12–F14 mixed contractions | Unique-vacuum gap (I27), the unchanged finite-range H clustering estimate, almost locality of the new creators, and those regular packet bounds give the \(O(|t|^{-d/2})\) contraction error. The two packets may have different masses/centres. Orthogonality makes the scalar contraction zero between distinct selected sectors. |
| F15–F16 Gram recursion | Velocity partitions use each packet's own smooth dispersion. Rapid double commutators and the uniform finite-energy bound on every remaining finite word are unchanged. Polynomial bounds alone would still be insufficient for the contraction error. |
| F17–F19 spectral/density step | Equation (I20) and the covered density just proved replace the finite-q selector. All other inputs are unchanged, as detailed next. |

For clarity, the last step requires no new absolute-continuity assumption. For each new creator,
\[
\langle B\Omega,T_xB\Omega\rangle
=\langle\Omega,[B^*,\tau_x(B)]\Omega\rangle .
\tag{I28}
\]
This sequence is rapidly decreasing by almost locality and \(B^*\Omega=0\), so its torus spectral measure has a smooth density. Density of the vectors (I20) makes every Haar-null Q projection vanish on the entire covered one-particle subspace. On each lift chart \(Q=k-\theta\) transfers that conclusion to Lebesgue-null K sets. Countable chart coverage suffices.

The velocity map
\[
v_M(k)=\frac{\beta k}{\sqrt{M^2+\beta|k|^2}},\qquad
k_M(v)=\frac{Mv}{\sqrt\beta\sqrt{\beta-|v|^2}}
\tag{I29}
\]
is a smooth bijection onto \(\{|v|<\sqrt\beta\}\) with nonzero Jacobian. For a fixed momentum of a second particle there is at most one momentum of the first at equal velocity, even for different masses. Absolute continuity and Fubini make pairwise equal-velocity diagonals null. The complement has a countable cover by product momentum neighborhoods with disjoint closed velocity images. The creator-density proof works in each such subpatch, since (I5) is preserved under restricting O. Their symmetrized tensor products are dense in every Fock sector.

The unchanged contraction/recursion proof F14–F16 now gives the permanent Gram formula F5 on the admissible domain, and hence unique isometries
\[
W^\pm:\Gamma_s(\mathcal H_1^{\rm cov})\longrightarrow\mathcal H,\qquad
V_jW^\pm=W^\pm\Gamma_s(V_j|_{\mathcal H_1^{\rm cov}}).
\tag{I30}
\]
Different particle sectors are orthogonal. General unseparated raw packet products are not claimed to converge; their Fock vectors are defined by continuous extension. This extends the original Fock theorem by verifying its proof hypotheses, not by treating its finite-q theorem statement as already covering irrational characters. Only the final finite-order conclusion in F20 is lost. The scattering ranges remain closed subspaces, with no surjectivity conclusion.

For the detector theorem, choose each full geometric carrier \(\Lambda_i\) by (I22), and choose nonnegative smooth spatial cutoffs whose compact convex velocity regions are mutually disjoint and contain the respective \(v_i(\Lambda_i)\), with positive collars as in PC hypothesis 4. Where necessary, refine the compact one-particle patches before choosing these cutoffs. Internally separated compact data admit finite such refinements; arbitrary unseparated raw data are not thereby made admissible. Use separate smooth dispersion extensions for every species/chart.

Every direct PC hypothesis is now available: almost-local B and \(\delta_HB\), positive compact full temporal transfer \(I_i\), compact full geometric transfer \(\Lambda_i\), exact vacuum graph (I21), and convex velocity containment. Therefore the entire proof C3–C24 applies unchanged. In its notation,
\[
S_t=J_te^{-it\omega(D)}\longrightarrow S\quad\hbox{strongly},\qquad
e^{it\omega(D)}g(D)\mathsf h(X/t)F_t\psi
\longrightarrow\mathsf h(v(D))S^*\psi
\tag{I31}
\]
in norm for each finite-energy \(\psi\). The full-source identity
\(\mathcal R_t=P_\Lambda\mathcal R_t=q(D)\mathcal R_t\)
comes from the full filter (I22), the closed carrier subspace and its strong derivative, exactly as in C7/C11/C13/C16; it is not inferred from (I21). The fixed-time finite-rank step, reversed Duhamel order, both Schur sums for \(s\ge t\), and the species-specific free limit require no finite-order centre input. No strong adjoint limit of \(S_t\) is inferred.

If in addition the energy-only vacuum remainder
\[
(J-I_1-\cdots-I_n)\cap\operatorname{spec}H\subset\{0\}
\tag{I32}
\]
holds for a bounded energy interval J, (I27) and the same operator ordering give the positive detector limit C28,
\[
Q_J(t)=P_JJ_t\mathsf h(X/t)J_t^*P_J
\longrightarrow
P_JS\mathsf h(v(D))S^*P_J
\tag{I33}
\]
strongly, with the same form of fixed-arrangement finite-energy bound, computed for the new creators, and scattering range. Constants depend on the new filter seminorms; the old numerical constants are not transferred. Thus PC extends to the new direct creators; (I32), finite-energy bounds and cutoff geometry must still be supplied for each arrangement. ND, energy capture, all-channel coverage and EX are separate.

The later detector/scattering-projection note is not a premise or conclusion of this proof. It was under separate review at this task's launch; root subsequently reported a completed separate check, which is not imported here. Its conditional substitution of admissible creator/Fock/PC properties could be considered only at its own declared scope; no projection or exhaustion result is needed to establish (I7)–(I33).

## 6. Exact finite multivariate interpolation without a common period

The original finite-q average is not automatically a selector once its finite-order premise is removed. In one dimension its value on another character \(\vartheta\) is
\(q^{-1}\sum_{j=0}^{q-1}e^{ij(\vartheta-\theta)}\), generally nonzero. For q=2 and \(\vartheta-\theta=1\) radian it is \((1+e^{i})/2\ne0\). The replacements below and in §4 supply their own exact spectral hypotheses.

There is also a finite-sum route when the **entire relevant restricted** V spectrum lies in a finite set of distinct characters \(\Theta=\{\theta^{(1)},\ldots,\theta^{(r)}\}\). The restriction can be a mass component or a previously selected mass/momentum subspace; it must commute with V. Write \(z^{(a)}_m=e^{i\theta^{(a)}_m}\). For each \(b\ne a\), choose one coordinate \(\ell(a,b)\) with \(z^{(a)}_{\ell(a,b)}\ne z^{(b)}_{\ell(a,b)}\). The multivariate polynomial
\[
p_a(z)=\prod_{b\ne a}
\frac{z_{\ell(a,b)}-z^{(b)}_{\ell(a,b)}}
     {z^{(a)}_{\ell(a,b)}-z^{(b)}_{\ell(a,b)}}
\tag{I34}
\]
has \(p_a(z^{(c)})=\delta_{ac}\). Its expansion has finitely many monomials \(z^j\), so substituting those coefficients in (I8) is a finite sum of the actual \(\nu_j\). On the restricted vacuum subspace its multiplier is exactly the character spectral projection. Finite sums preserve the same direct properties, and denominators are nonzero. They need not be uniformly bounded as different characters approach one another.

This formula permits arbitrary distinct characters, including irrational ones. It is not enough to specify a finite subset of a larger uncontrolled relevant spectrum: (I34) generally does not vanish at unspecified characters. Such a subset needs its own smooth isolation filters, a prior restriction, or other exact support information.

One integer direction need not separate all finite characters. For
\(\Theta=\{(1,1),(1,-1),(-1,1),(-1,-1)\}\subset(S^1)^2\),
every \(j=(a,b)\in\mathbb Z^2\) gives values \(z_1^az_2^b\) in \(\{1,-1\}\), so at most two values distinguish four points. Nevertheless the finite multivariate polynomial \((1+z_1)(1+z_2)/4\) selects \((1,1)\). This is an exact counterexample to the one-direction shortcut, not to finite-character selection.

## 7. Preserved failures, continuum scope and finite-order boundary

**Nonisolated and nonatomic characters.** The spectral projection \(P^V(\{\theta\})\) may be zero. On such a subspace an exact point-character vector is necessarily zero. If \(0\le\phi_n\le1\) are smooth bumps equal to one near \(\theta\), with supports shrinking to \(\theta\), dominated convergence of scalar spectral measures proves \(\phi_n(V)\to P^V(\{\theta\})\) strongly. In a nonatomic component this limit is zero. For example, multiplication by \(e^{ij\vartheta}\) on \(L^2(\mathbb T)\) has no point-character eigenvectors; a nonzero smooth bump retains an arc of characters, not a point. This is a spectral example, not a local-UHF countermodel to the microscopic assumptions.

Even an atom does not suffice for a uniform smooth exact selector on an entire subspace if it is an accumulation point of its other V spectrum. Consider on \(\mathbb Ce_0\oplus\ell^2(\mathbb N)\) the phases \(\theta_0=0\), \(\theta_n=1/n\). Every continuous \(\phi\) with \(\phi(0)=1\) has \(\phi(1/n)\to1\), and therefore cannot equal the point projection on that whole subspace. Shrinking smooth bumps converge strongly to \(|e_0\rangle\langle e_0|\), but their operator-norm distance from it is one. More generally an accumulating restricted spectral support obstructs that continuous exact projection in the same way. This does not forbid exact filtering of a particular vector with a smaller isolated support or a patch satisfying (I5).

Passing from the strong vector limit of shrinking filters to an almost-local exact creator would require additional control not provided here: the estimates (I7)/(I17) depend on all relevant Fourier moments and isolation collars. No uniform almost-local seminorm bounds or norm convergence of the filtered observables as the collar shrinks has been proved. This missing control is retained, not replaced by a finite-resolution numerical observation.

**An approximate centre does not supply the exact packet clock.** A vacuum vector carrying two characters at the same geometric momentum can carry two different current momenta and hence two different energies. With \(\beta=M=1\), geometric \(p=0\), current \(k_0=0,k_1=1\), its mass energies are \(1,\sqrt2\), and its characters are \(0,1\) modulo \(2\pi\). Using the \(\theta=0\) clock leaves \(e^{it(\sqrt2-1)}\) on the second component. Its derivative does not vanish. This elementary spectral control is not an admissible infinite-lattice model, but it exactly rejects replacing (I20)/(I21) by an unresolved centre band in the Cook calculation. A continuum-centre scattering construction, if possible by other methods or further support information, is not supplied or ruled out by this note.

**A norm sum need not preserve almost locality merely by convergence.** The actual repair is the uniform small-j estimate (I16) plus the Schwartz tail (I17). Applying a global exponentially growing LR bound and integrating it against an arbitrary Schwartz coefficient tail would not establish the claimed estimates. Likewise fixed-j covariance does not authorize taking j proportional to scattering time.

**The lost common-q conclusion.** On a nonzero selected one-particle character, \(V_{qe_a}=1\) would force \(q\theta_a\in2\pi\mathbb Z\). A finite collection of finite-order characters has a common such q by taking the least common multiple of their orders. If any selected character has an irrational component relative to \(2\pi\), no positive integer q can satisfy all these identities. For instance \(q(\sqrt2-1)\in\mathbb Z\) would imply \(\sqrt2=1+m/q\), impossible. The nonzero one-particle sector already lies in the Fock range, so no cancellation between multiparticle character sums restores a common order on that whole range.

Consequently the earlier exact common-q inference toward a full-algebra translation/shift identity is not furnished in this setting. Neither (I26) nor (I30) asserts \(V_j^q=1\). This does not construct an irrational microscopic centre, supply EX, or evade every index obstruction. Possible alternative obstruction arguments and a physical realization are separate questions.

## 8. Evidence and control scope

The genuinely new analytic work is (I7)–(I20), especially the uniform locality estimate and the patchwise spectral quantifiers. Equations (I21)–(I33) reuse exact predecessor proof arguments after checking their direct hypotheses and removing the common-q conclusion. The finite multivariate route (I34) and the failure examples are proved here. No new external theorem is imported. Basic joint spectral calculus and Fourier manipulations are made explicit; the finite-range LR, clustering, scattering and detector arguments are the exact source-bound dependencies listed above.

The companion directory isolated_centre_filtering/ contains the source ledger, one current checkpoint, operational history, finite algebra controls, complete declared-timeout execution logs, author self-check and freeze receipt. The controls discriminate Fourier signs, transition-difference versus outgoing-only filtering, adjoint/order identities, multivariate separation, locality-radius arithmetic and exact packet clocks. They cannot certify infinite-volume almost locality, convergence of Fourier tails, scattering limits, physical premises, or independence. No finite test of many q values is substituted for the irrationality argument.

Eight finite controls ran once under a declared 60-second timeout, exited 0 in 0.0595 seconds, and produced nine complete JSON records with empty stderr. The largest reported phase-identity error was below \(1.9\times10^{-15}\). Wrong central coefficient signs, outgoing-only filtering, real-but-odd * preservation, omitted mass restriction, one-direction separation of the four torsion characters, omitted geometric radius and the unresolved single packet clock were all rejected by the specified controls. Sixty exact rational radius cases and sixteen exact torsion interpolation values are arithmetic checks only. A separate declared 60-second source check exited 0 in 0.144 seconds and verified 25 current inputs plus all 63 PC and 57 projection predecessor input/output bindings. These are author checks, not independent evidence for analytic convergence.

The final metadata refresh first stopped on the concurrent repository revision change. Its full failure log is preserved; a complete changed-path inventory then confirmed that all bound repository inputs were byte-identical. The first inventory-command launch also had a mistyped duplicate path component and exited before running the script; its log and successful corrected retry are retained. The refreshed source check and final freeze verification use separate logs. No scientific control failed or timed out.

Frozen author operational record: This author theorem requires a fresh focused check before substantial downstream use. The previous PC and projection notes and their frozen evidence are unchanged. Editable prompt files changed: none. Only this note and its assigned external evidence directory are outputs. No Git/repository/PR/publication/audit/axiom/prompt mutation, other-chat message, model/effort override or subdelegation was performed. The fixed campaign deadline remains 2026-10-12 16:00:52 UTC. Publication update: the separate source check below is complete; the historical pending statement describes the author freeze.


## Publication verification and remaining obligations

The separate review supports all I1–I34 with no required mathematical correction.
Report68ea0c2f00d0808ce5a6a63632b0bc84a05398260478510fb4f66256e885cbc9,
receipt8eeb364e11eb54d3cb4a6127596d6f9d422f6acd9d88b1275346922661c99abc.
The full reconstruction and distinct four-site spin/current-flow calculation
froze before author-helper exposure. The initial Fourier truncation failed
the declared1e-8 tolerance; resolution refinement at unchanged tolerance gave
error4.02e-14. The failure, both code versions and complete logs are preserved.
Author reproduction was byte-exact. Ten copied-source defects were rejected.
One survived: deleting the positive shift from the successful final-radius
inequality weakens that inequality. The source's separate overfilled-budget
counterexample does not test every support step. The analytic construction
explicitly includes the geometric displacement; arithmetic alone does not
prove locality. No uniform shrinking-collar bounds or microscopic irrational
sector are supplied. The accumulating-atom, nonatomic and unresolved-clock
examples retain their limited spectral scope.

Root proposed the mechanism and is a contributor, not the independent reviewer.
Shared source/metadata exposure is disclosed in the review; it is not blind
checking or an independence claim based on predicate counts. Complete proofs,
controls, review, failures and source hashes are preserved in the packet.
PUBLICATION_EDITS.json and reconstruct.py recover the note and entire primary
from frozen bytes and explicit metadata edits. No displayed mathematics changes.
The [finite primary](../scripts/isolated_centre_filtering_2026_10_12.py) is an executable finite check;
DELIVERY_CHECKS.md records its actual run and mechanical publication checks.
No Lean certificate, applied audit verdict, physical axiom change or retained
promotion is asserted. Global combined audit and strict audit lint remain
independent landing gates. The sole live campaign checkpoint remains in the
transport worktree; this packet is a frozen milestone.
