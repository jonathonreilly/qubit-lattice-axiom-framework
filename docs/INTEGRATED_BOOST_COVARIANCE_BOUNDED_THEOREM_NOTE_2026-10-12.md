---
claim_id: "integrated_boost_covariance_bounded_theorem_note_2026-10-12"
claim_type: "bounded_theorem"
claim_scope: "For one boost direction, supplied finite-range energy density, beta>0, same-state local invariance and the two remaining exact local Lie identities integrate to full norm-flow and canonical GNS covariance, maximal spectral-sum domains and joint spectral preimage covariance. Optional positive energy gives the forward cone. No nontrivial microscopic realization, fixed mass, geometric momentum, rotations or higher-dimensional Poincare conclusion is supplied."
upstream_dependencies:
  - microscopic_boost_flow_bounded_theorem_note_2026-10-12
  - microscopic_joint_flow_bounded_theorem_note_2026-10-12
runner: "scripts/integrated_boost_covariance_2026_10_12.py"
actual_current_surface_status: "conditional-support"
target_claim_type: "bounded_theorem"
trace_class: "direct_blocker_closure"
target_claim_id: null
target_blocker_text: "Conditional one-direction integration of actual rapid almost-local flows under the remaining exact local Lie identities; physical input realization is outside this target."
source_of_blocker_text: "handoff"
reachability_to_target: "closes"
artifact_role: "theorem"
next_trace_action: "Supply a nontrivial intended density/state satisfying the two remaining exact local Lie identities, then separately check any positivity or broader covariance claim."
conditional_surface_status: "Conditional one-direction integration from actual rapid almost-local flows and exact local Lie identities"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "The density, same-state local identities, two remaining exact Lie identities and optional positive energy remain supplied; no nontrivial joint physical example is constructed."
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# Integrated covariance of the actual microscopic boost

**Conditional bounded theorem, 2026-10-12; complete separate source review requires no mathematical correction.**
The answer to the scoped integration question is affirmative. The rapid
almost-local bounds and differentiability already proved for the actual
flows suffice to integrate their exact local Lie identities. The result
identifies the complete self-adjoint GNS generators and their domains.
The target is the integration implication, not existence of a nontrivial
finite-range density satisfying its supplied identities, nor a physical
Lorentz model. Root supplied the candidate route and is a contributor.

S denotes the original research collection. The [frozen milestone handoff](../.claude/science/physics-loops/toe-boost-gap-fock-closure-20261012/HANDOFF.md) and [evidence map](../.claude/science/physics-loops/toe-boost-gap-fock-closure-20261012/EVIDENCE_MAP.json) preserve the original source bundles and complete own evidence. The direct in-branch proof dependencies are [Boost](MICROSCOPIC_BOOST_FLOW_BOUNDED_THEOREM_NOTE_2026-10-12.md): B1-B37 actual all-time flows, rapid almost-local seminorm bounds, finite derivation losses, C1 flow orbits and canonical same-state GNS implementation; remaining local Lie identities are supplied here.; [Joint](MICROSCOPIC_JOINT_FLOW_BOUNDED_THEOREM_NOTE_2026-10-12.md): J9-J10 bounded Fourier/Gaussian spectral approximation supports the step from commuting canonical unitaries to commuting spectral measures. The separate mixed-history J1-J3 route is optional and is not applied to the weighted boost. Other named sources are historical context or transitive dependencies unless their use is stated explicitly. The 459-line analytic
draft was frozen before its author controls, at SHA-256
`79cedb09d7b60aef48639667d656a453bd433f40c2669c72260d0c008c4dccc1`.
At the author freeze, its recovery state was `CHECKPOINT.md` and its final input/output bindings were in `receipt.json`; current campaign recovery remains root-owned. No formal audit status is created.

## 1. Exact inputs, premise ledger and target

The following four inputs were read completely, at these SHA-256 identities:

| Source | SHA-256 |
|---|---|
| `MICROSCOPIC_BOOST_FLOW_PROBE.md` (758 lines) | `7ec1d7eecb4eba020548eba8b56dff66712f52b4eba634ba276dd67440d28de7` |
| `MICROSCOPIC_BOOST_FLOW_REVIEW.md` | `ed2c7e594714b9ba0dc1e8f0fed916e55c7a2e7c84bc0078acc6a00cd4292678` |
| `MICROSCOPIC_JOINT_FLOW_PROBE.md` (279 lines) | `35bcb1013b0716a4faa33fdbd75ff067427c1dec8e377f63ebb17ac301786ebd` |
| `MICROSCOPIC_JOINT_FLOW_REVIEW.md` | `9699043c35343901ef75ab6a29dd560ba4aa30f8a3b908643e959958e86447c9` |

The boost note's B1–B37 are the provisional mathematical input: actual
all-time flows; uniform-on-compact-time rapid-AL bounds; continuous
derivations with finite seminorm loss; C1 rapid-AL orbits; and canonical GNS
implementation under the same state's two local identities. Its existence
input is the checked application of TWW, arXiv:2511.02941v2, with the
finite-spin/Lieb–Robinson hypotheses checked in that note. This worker reads
and applies the reviewed conditional lemma; it does not claim a second
complete review of TWW or of the upstream current helper. Their exact
provenance remains in the frozen input packet.

The joint-flow note's J1–J14 supplies a separately checked route from the
finite-range local commutation to strong joint commutation. Section 4 below
also proves that particular implication directly from rapid-AL C1 curves,
so the integration proof does not need a new analytic-vector theorem.
These are two mathematical routes, not two independent reviews of this
new note. The optional gapped-invariance probe is **not used**. Its separate
hypotheses and pending source-control closure therefore do not enter here.

The repository/instruction sources are bound in `sources/manifest.json`.
Root supplied checkout HEAD `dc7f415f73df3754653f4985382ca0fb96f07cda`, main
`a13caa4885f547c8d206265b031ba7649e539fd9`, and planning
`3a4b2c66a1ead7a1c48b4359627e968f681e3c39`; this worker used no Git operation.
The supplied planning AGENTS snapshot and current repo science workflow
were read. The repo reporting reference is
`8fdc997ce1735a7a132a2fe21732e5f9c9197ac386ea7dd0b4e4a1aa7269702e`.
The registry was inspected: no registered primitive is used to supply
a density, a selected invariant state, the Lie identities, positivity or
the parameter beta. No physical axiom/primitive is introduced.

The scoped statement search is preserved in `statement_search.*`. The
existing 1+1 and 3+1 boost-covariance notes concern supplied free-scalar
continuum two-point functions, not integration of a weighted spin derivation
and its canonical GNS generators. They are scope comparisons, not proof
inputs. The closest source is the microscopic boost note's explicit open
integrated-Lorentz obligation in its section 9. This is no exhaustive
literature or repository novelty claim. Root owns the wider campaign and
reports the currently concurrent PR science outside this integration scope.

## 2. Hypotheses and complete conclusion

Use the quasilocal spin tensor algebra over \(\mathbb Z^d\), d>=1, with
finite-dimensional full matrix site algebras, the l1 metric, and one fixed
coordinate b, exactly as in B1–B2 of the boost input. Write
\(B_L=\{x:|x|_1\le L\}\). Supply Hermitian translated densities
\(h_x=\tau_xh_0\), with support in \(x+B_R\), \(R\in\mathbb N_0\), and
uniform norm at most \(h<\infty\).
The positive-clock local derivations are
\[
 \delta_h A=i\sum_x[h_x,A],\qquad
 \delta_b A=i\sum_xx_b[h_x,A],\qquad
 \delta_p A=i\sum_x[p_b(x),A],                         \tag{C1}
\]
where the actual finite-range current density is
\[
 p_b(x)=\frac i2\sum_{|r|_1\le2R}r_b[h_x,h_{x+r}].      \tag{C2}
\]
It has support in \(x+B_{3R}\), is uniformly bounded, and B33 proves
\([\delta_h,\delta_b]=\delta_p\) on all local observables.

Supply the following additional exact algebra identities, for a fixed real
\(\beta>0\), on **every** local observable:
\[
 [\delta_h,\delta_p]=0,\qquad
 [\delta_p,\delta_b]=\beta\delta_h.                    \tag{C3}
\]
They are conditions on the given density, not generic consequences of
finite range or of C2. The negative example J21 in the joint-flow input
already shows why the first condition cannot be suppressed.

Supply a normalized state omega with both identities
\[
 \omega(\delta_h A)=\omega(\delta_b A)=0
 \quad(A\in\mathcal A_{\rm loc}).                       \tag{C4}
\]
Then B34 derives its current identity. The boost input constructs the
actual flows \(\alpha_t,\rho_u,\lambda_s\), respectively generated by
\(\delta_h,\delta_p,\delta_b\), and makes this same state invariant under
all three. Let
\[
 U(t)=e^{itH},\quad V(u)=e^{iuP},\quad W(s)=e^{isB}       \tag{C5}
\]
be their **canonical** GNS implementations in \((\pi,\mathcal H,\Omega)\). Write
\(\mathcal D=\pi(\mathcal A_{\rm loc})\Omega\). All fix Omega and obey
\(iG\pi(A)\Omega=\pi(\delta_G A)\Omega\) on the rapid AL algebra,
in particular on the actual local cyclic domain D. No initial supplied
self-adjoint generators are necessary. If separately supplied generators
have these exact local actions, B27–B29 identify them with C5.

Put
\[
 k=\sqrt\beta,\quad c_s=\cosh(ks),\quad
 d_s=\frac{\sinh(ks)}{k},\qquad
 M_s=\begin{pmatrix}c_s&-d_s\\-\beta d_s&c_s\end{pmatrix}. \tag{C6}
\]
Under C1–C4:

1. H and P strongly commute, with joint spectral measure E. The actual
   algebra flows satisfy, on the entire quasilocal algebra for all real
   s,t,u,
   \[
   \lambda_s\alpha_t\lambda_{-s}
      =\alpha_{c_st}\rho_{-d_st},\qquad
   \lambda_s\rho_u\lambda_{-s}
      =\alpha_{-\beta d_su}\rho_{c_su}.                \tag{C7}
   \]
2. For any real a,b define the self-adjoint joint-spectral sum
   \[
   G(a,b)=\int(ae+bp)\,dE(e,p),\quad
   \operatorname{Dom}G(a,b)=
    \{\xi:\int|ae+bp|^2d\langle\xi,E(e,p)\xi\rangle<\infty\}.
                                                               \tag{C8}
   \]
   The complete operator equalities, including domains, are
   \[
    W(s)H W(s)^*=G(c_s,-d_s),\qquad
    W(s)P W(s)^*=G(-\beta d_s,c_s).                    \tag{C9}
   \]
   In particular \(W(s)\operatorname{Dom}H\) equals the first domain in
   C8, and similarly for P. A sum in C9 is not silently assigned only the
   intersection of the individual domains.
3. For every Borel set S in R^2,
   \[
    W(s)E(S)W(s)^*=E(M_s^{-1}S).                       \tag{C10}
   \]
   Thus the joint spectral support is invariant under M_s.
4. If in addition the actual H is positive, the joint spectral support
   lies in \(e\ge0,\ |p|\le k e\). Consequently
   \[
    \operatorname{Dom}H\subset\operatorname{Dom}P,
    \qquad\|P\xi\|\le k\|H\xi\|
       \quad(\xi\in\operatorname{Dom}H).              \tag{C11}
   \]
   This is the precise quadratic-form meaning of \(P^2\le\beta H^2\).
   It does not fix a mass or assert an isolated mass shell.

The state condition is needed for the GNS conclusions. C7 itself depends
only on the density and local Lie identities, because its proof is at the
algebra level.

## 3. Finite-word regularity is derived, not supplied

Let E_r here denote the normalized-trace conditional expectation onto
the algebra of B_r (distinct from the joint spectral measure E). Let
\(\mathcal F=\mathcal A_{\rm al}\), with the boost input's seminorms
\[
 p_\nu(A)=\|A\|+\sup_{r\ge0}(1+r)^\nu\|(1-E_r)A\|.
                                                               \tag{C12}
\]
It is a dense complete Frechet *-algebra; E_L A converges to A in every
seminorm. B15 gives the continuous endomorphisms of F with integer losses
\[
 p_\nu(\delta_j A)\le C_{\nu,j}p_{\nu+\ell_j}(A),
 \quad\ell_h=\ell_p=d+1,\quad\ell_b=d+2.               \tag{C13}
\]
The constant current norm/range in C2 meets the kappa=0 hypothesis of
B12–B17. There is no spatially growing current hidden in C13.

For any fixed word \(Q=\delta_{j_1}\cdots\delta_{j_n}\), iterating C13
gives a finite constant \(C_{\nu,Q}\) and loss
\(\ell(Q)=\sum_m\ell_{j_m}\) with
\[
 p_\nu(QA)\le C_{\nu,Q}p_{\nu+\ell(Q)}(A),\qquad
 p_\nu(Q(A-E_LA))
 \le2C_{\nu,Q}(1+L)^{\nu+\ell(Q)-q}p_q(A)
 \quad(q>\nu+\ell(Q)).                                \tag{C14}
\]
The second bound is B11 applied at exponent \(\nu+\ell(Q)\).
Thus all fixed finite words extend continuously, and the same local
approximants converge in each such word graph. No estimate uniform in
word length, factorial bound or nonzero analytic radius is asserted or
needed. Applying C14 to the degree-two identities extends C3 and B33
to every A in F.

The three actual groups preserve F, have locally uniformly bounded
operator seminorms on F, and have C1 F-valued orbits, by B10/B18–B21 and
their uniform finite-range specializations. Each derivation commutes with
its own actual flow on F. These facts also justify the product rule used
below for a moving F-vector. Explicitly, if x(s) is C1 in F and T_s is one
of the groups, split the difference quotient as
\[
 \frac{T_{s+h}x(s+h)-T_sx(s)}h
 =T_{s+h}\frac{x(s+h)-x(s)}h+
   \frac{T_{s+h}-T_s}h x(s).                            \tag{C15}
\]
Local uniform seminorm bounds control the first term's moving input;
strong continuity on F controls the remaining fixed-input term. The limit
is \(T_sx'(s)+T_s\delta_Tx(s)\) in every seminorm.
Continuity of this derivative follows from the same bounds. This is a
pointwise product rule, not operator-norm differentiability on F or A.

We will also use the following elementary uniqueness fact on the Banach
space A. If T_t is an actual strongly continuous group with generator L,
and x(t) is C1 in norm, lies in Dom L, and satisfies x'(t)=Lx(t), then
\(T_{-t}x(t)\) has derivative zero. Indeed, split its difference quotient
as in C15, now using local operator-norm boundedness of T_t and the defining
generator limit on the single vector x(t). Hence x(t)=T_t x(0).
This proof works on any real compact time interval. It requires no common
core and no uniqueness theorem for an arbitrary unbounded ODE on a
Frechet space. The standard Banach-space formulation also appears as
[Engel–Nagel, Proposition II.6.2, p. 145](https://www.math.uni-tuebingen.de/de/forschung/agfa/members/engel-nagel_one-parameter-semigroups.pdf);
its role here is corroborating context because the needed proof has just
been supplied. Only that page's classical-solution definition and theorem
were inspected. The acquired PDF is SHA-256
`a48ba290280c718cbf6a65a6b09b4c3c59f622102619fe5b227d446c921a56ff`;
the acquisition receipt and extracted page are in `sources/`.

## 4. Commutation of the actual energy and current flows

For fixed A in F, C15 and the extended first identity of C3 imply
\[
 \frac d{dt}\bigl(\alpha_t\delta_p\alpha_{-t}A\bigr)
 =\alpha_t[\delta_h,\delta_p]\alpha_{-t}A=0.
                                                               \tag{C16}
\]
Thus \(\alpha_t\delta_p\alpha_{-t}=\delta_p\) on F. Fix t and let
\(x(u)=\alpha_t\rho_u\alpha_{-t}A\). It is C1 in F, belongs to the
norm-generator domain of rho, and has derivative
\(x'(u)=\delta_p x(u)\). The Banach-group uniqueness argument of section 3
gives x(u)=rho_u A. Norm density and the isometry of automorphisms extend
this equality to all of A. Therefore alpha and rho commute for all times.

Canonical GNS implementation then gives, on every cyclic vector,
\[
 U(t)V(u)\pi(A)\Omega
 =\pi(\alpha_t\rho_u A)\Omega
 =V(u)U(t)\pi(A)\Omega.                                \tag{C17}
\]
They are bounded unitaries, so equality holds on all Hilbert space. Their
spectral measures commute: a bounded operator commuting with every
\(e^{itH}\) commutes with H's spectral projections by bounded spectral
approximation, and applying this twice proves the assertion for H/P.
The explicit Fourier/Gaussian approximation in J9–J10 of the joint-flow
input supplies this standard spectral step without an unbounded-domain
interchange. The joint spectral measure E therefore exists.

Hypothesis matching for the independent route J1–J3 is exact. The energy
and C2 current interactions have finite range, bounded cardinality and
finite per-site norm; the canonical H/P have the exact local actions.
Locality makes their actual D invariant before products are taken, and C3
implies \([H,P]\mathcal D=0\). Thus that reviewed mixed-history theorem
gives the same C17 and strong commutation. It is used only for H/P;
the weighted boost is not a bounded finite-range interaction satisfying J1.

## 5. Conjugation of derivations and the hyperbolic ODE

For fixed A in F put
\[
 F_h(s)=\lambda_s\delta_h\lambda_{-s}A,\qquad
 F_p(s)=\lambda_s\delta_p\lambda_{-s}A.                \tag{C18}
\]
C13/C15 justify differentiating every factor, including the moving
derivation input. With the commutator order carefully retained,
\[
 F_h'(s)=\lambda_s[\delta_b,\delta_h]\lambda_{-s}A=-F_p(s),
 \qquad F_p'(s)=\lambda_s[\delta_b,\delta_p]\lambda_{-s}A
              =-\beta F_h(s).                         \tag{C19}
\]
The initial data are \((\delta_h A,\delta_p A)\). This finite-dimensional
scalar-coefficient ODE with values in F has the unique solution
\[
 \lambda_s\delta_h\lambda_{-s}
       =c_s\delta_h-d_s\delta_p,\qquad
 \lambda_s\delta_p\lambda_{-s}
       =-\beta d_s\delta_h+c_s\delta_p                 \tag{C20}
\]
on F. To avoid importing a general Frechet ODE theorem, multiply the vector
\((F_h,F_p)\) by the inverse scalar matrix exponential; the derivative is
zero. A continuously differentiable zero-derivative curve is constant in
each seminorm, equivalently after every continuous linear functional.
Its initial value fixes C20. In particular the first derivatives at s=0
are \(-\delta_p\) and \(-\beta\delta_h\), not their negatives.

## 6. Identify the complete algebra flows

For fixed real a,b the commuting product
\(T_t^{a,b}=\alpha_{at}\rho_{bt}\) is an actual strongly continuous
automorphism group. On F its norm generator is \(a\delta_h+b\delta_p\):
differentiate its product orbit using C15 and the already proved
commutation. Thus F is contained in that generator's domain; no claim
about a core is needed.

Fix s and A in F. The actual curve
\(x(t)=\lambda_s\alpha_t\lambda_{-s}A\) stays in F and has derivative,
by C20,
\[
 x'(t)=(c_s\delta_h-d_s\delta_p)x(t).                  \tag{C21}
\]
It is a norm-C1 classical solution for the already existing group
\(T_t^{c_s,-d_s}\), with initial value A. Applying the explicit uniqueness
proof gives the first identity of C7 on F. Repeating it with rho and
\((-\beta d_s,c_s)\) gives the second. Norm density then gives C7 on the
whole algebra. This is the step that agreement of formal commutators or
of unbounded operators on a merely dense local domain cannot replace.

## 7. Canonical GNS equality, exact domains, and clocks

Using the exact canonical action on cyclic vectors and C7 yields
\[
 \begin{split}
 W(s)U(t)W(s)^*&=U(c_st)V(-d_st),\\
 W(s)V(u)W(s)^*&=U(-\beta d_su)V(c_su).
 \end{split}                                            \tag{C22}
\]
For example, both sides of the first equality send \(\pi(A)\Omega\) to
\(\pi(\lambda_s\alpha_t\lambda_{-s}A)\Omega\). Cyclic density proves
the full bounded-unitary equality, with no commutant/phase ambiguity.
Equality of adjoint actions alone would not suffice for this argument.

By joint spectral calculus, \(U(at)V(bt)=e^{itG(a,b)}\), with the
domain C8. The conjugated unitary \(W(s)e^{itH}W(s)^*\) has generator
\(W(s)HW(s)^*\) on \(W(s)\operatorname{Dom}H\). Stone uniqueness
applied to C22 therefore proves C9 with complete domains. A similar
argument covers P. For clarity, G(a,b) is also the closure of
\(aH+bP\) on \(\operatorname{Dom}H\cap\operatorname{Dom}P\): for
\(\xi\in\operatorname{Dom}G(a,b)\), the joint spectral cutoffs
\(E([-n,n]^2)\xi\) lie in the intersection and converge to xi in G's
graph norm by dominated convergence. This proves that closure statement;
it does not identify its original intersection domain with the full domain.

The negative spatial clock specified in the campaign is
\[
 \mathcal T(t,y)=e^{itH}e^{-iyP/\beta}.                 \tag{C23}
\]
C22 gives the exact representation covariance
\[
 W(s)\mathcal T(t,y)W(s)^*
   =\mathcal T(c_st+d_sy,\ \beta d_st+c_sy).            \tag{C24}
\]
The coordinate matrix preserves \(\beta t^2-y^2\). There is exactly
one beta division in C23. If \(\theta=ks\) is chosen as dimensionless
rapidity, the generator of the reparametrized group is B/k, and the energy
pair \((H,P/k)\) transforms by
\(\left(\begin{smallmatrix}\cosh\theta&-\sinh\theta\\
-\sinh\theta&\cosh\theta\end{smallmatrix}\right)\).
This is an explicit reparametrization of this note's B, not identification
with any separately named scalar boost generator. The term spatial clock
does not assert that \(P/\beta\) equals a geometric-translation generator.

With \(L_s(t,y)=(c_st+d_sy,\beta d_st+c_sy)\), the bounded unitaries
\(\mathcal R((t,y),s)=\mathcal T(t,y)W(s)\) obey
\[
 \mathcal R(a,s)\mathcal R(a',s')
   =\mathcal R(a+L_sa',s+s').                          \tag{C25}
\]
They depend strongly continuously on their three real parameters. This
is an actual representation of the connected 1+1 translation/boost
semidirect product in these clocks. Faithfulness or physical realization
is not asserted. No second boost, rotation, or 3+1 Poincare claim follows.

## 8. Joint spectral covariance and positive energy

The joint spectral measure of the conjugated pair
\((W(s)HW(s)^*,W(s)PW(s)^*)\) is \(W(s)E(\cdot)W(s)^*\).
The pair C9, obtained by applying the invertible linear map M_s to
\((H,P)\), has joint measure \(S\mapsto E(M_s^{-1}S)\).
Uniqueness of the joint spectral measure proves C10. Notice the inverse
on the set argument. Since unitary conjugation preserves whether a
projection is zero, and M_s is a homeomorphism, the support Sigma of E
satisfies \(M_s\Sigma=\Sigma\).

Suppose now H is positive. Every conjugate in C9 is positive. A continuous
real linear function whose spectral multiplication operator is positive
must be nonnegative on Sigma: if it were negative at a support point,
it would be negative on a neighborhood with nonzero spectral projection.
Therefore for every \((e,p)\in\Sigma\) and every real s,
\[
 c_se-d_sp\ge0,
 \qquad e-\frac p k\tanh(ks)\ge0.                     \tag{C26}
\]
Taking s to plus and minus infinity gives \(e\ge|p|/k\), which also
implies e>=0. Alternatively rational s suffice by continuity, so no
uncountable intersection of state-dependent almost-everywhere sets is
needed. The converse is immediate for each forward-cone point.

Integrating \(p^2\le\beta e^2\) against every vector spectral measure
proves C11. The joint-spectral operator
\[
 \mathsf M^2=\int(e^2-p^2/\beta)\,dE(e,p)              \tag{C27}
\]
is positive and invariant under W(s), including its full domain, since
the integrand is invariant under M_s. It also strongly commutes with
the translation unitaries. C27 need not be scalar or have an isolated
eigenvalue. Even at the abstract representation level, a direct sum of
two positive-mass rapidity representations has different mass-squared
values while satisfying the covariance. Such an example is a scope
diagnostic, not a finite-range spin realization.

There is a useful optional domain consequence under positivity. On the
cone,
\[
 e^{-|ks|}e\le c_se-d_sp\le e^{|ks|}e.                 \tag{C28}
\]
Thus \(\operatorname{Dom}G(c_s,-d_s)=\operatorname{Dom}H\), and C9
then proves \(W(s)\operatorname{Dom}H=\operatorname{Dom}H\).
This domain invariance is a consequence of integrated covariance and
positivity, not a premise used to differentiate an unbounded commutator.

## 9. Checks, boundaries and next review

The proof's decisive checks are the finite-word graph approximation C14,
the F-valued product rule C15, the Banach-group uniqueness step C21,
canonical cyclic equality C22, and the full spectral domains C8–C10.
The complete proof was frozen before control implementation. The author
then read the complete control/logger source, every canonical output row,
and every changed mutation row, and reread the complete final argument.
These author checks are not independent review or infinite-volume tests.

`AUTHOR_CHECKS.md` gives a distinct explicit representation on
\(L^2(\mathbb R_+,dr/r)\): multiplication by
\(h_m(r)=m(r+r^{-1})/2\), \(p_m(r)=km(r-r^{-1})/2\), with the actual
unitary boost \(W(s)f(r)=f(r/e^{ks})\). Direct change of variables and
function composition give the covariance, and the generator on smooth
compactly supported functions is \(B=ikr\partial_r\). This checks signs
and normalization without the lattice Frechet argument. A direct sum at
two different masses also checks the limit of the cone/mass conclusion.
This is an abstract representation diagnostic, not a spin realization of
C1–C4. Its exact shift action is the comparator in `controls.py`.

The final canonical execution completed 71 predicates with zero failures.
Exact rational arithmetic checks nine spectral-point transformations and
their local differential products at three distinct beta values. Actual
unitary function compositions check both generator covariances and the
negative spatial clock. The maximum observed composition residual was
about \(5.84\times10^{-19}\), below the declared \(10^{-11}\) tolerance.
A fourth-order finite difference of the actual shifted multiplier checks
C19 with step \(10^{-4}\); its maximum residual was about
\(5.33\times10^{-12}\), below the declared \(10^{-8}\) tolerance.
Finite samples do not establish the universal F-valued product rule.

The domain diagnostic is a separate exact infinite-series argument. On
\(\ell^2(\mathbb N)\), take H with eigenvalues n and P with eigenvalues
\(10n/3\). For \(c=5/4,d=3/8\), the joint-spectral \(cH-dP=0\) has
the whole Hilbert space as its domain, whereas the algebraic sum on the
domain intersection excludes \(\xi_n=1/n\). That vector is square
summable but H xi is not. The finite control computes its partial norms;
the written series argument proves the domain distinction. This fixture
tests the sum convention and does not satisfy all the boost hypotheses.

Five declared mutations all returned exit 1, with full passing and failing
rows retained:

| Changed object | Failed / 71 | What distinguishes it |
|---|---:|---|
| Reverse the actual boost shift | 39 | Local Lie signs, generic shifted values, actual C1 derivative, unitary and projection covariance |
| Omit beta in current mixing | 13 | Current generator/unitary mixing and one selected projection |
| Divide the spatial clock by beta twice | 3 | Coordinate covariance at each tested beta |
| Use the forward spectral-set image | 3 | Three nonsymmetric spectral projections |
| Add a scalar energy phase | 50 | Vacuum fixation and the affine error in exact generator/unitary covariance |

Nondiscriminating rows are explicit. The reversed boost still obeys its
group law and preserves the quadratic mass invariant; its energy value
at zero rapidity also passes by the evenness of cosh. Correct generator
mixing does not test the spatial-clock divisor. Most selected projection
tests do not detect an added scalar energy phase. The local differential
checks are exact coefficient identities after the test-function derivative
cancels; they do not establish self-adjointness or general domains.

The initial domain helper inserted the known value N directly for the H
partial norm, making that one comparison tautological. Cold source reading
replaced it by the explicit sum of squared multiplication values. The
initial helper and all six initial executions remain preserved in
`history/` and `logs/`. The corrected helper and all five mutations were
then executed once each; every complete stdout and result JSON matched
its initial counterpart, while the final receipts bind the corrected
source. This repaired the evidence route without changing the proof or
claim. No timeout, unexpected nonzero science exit, or lost log occurred.

Each final run has a complete command, source hashes, timeout, elapsed time,
exit and stdout/stderr in `logs/final_*/receipt.json` and adjacent files.
The final canonical run used a 60-second limit and took about 0.037 seconds;
mutations used 30-second limits and each took less than 0.067 seconds.
Reproduce from `S/integrated_boost_covariance` using a fresh evidence name:

```text
python3 run_logged.py --name reproduction --timeout 60 --source controls.py --source run_logged.py -- python3 controls.py --mutation none --output reproduction.json
```

The logger refuses to overwrite an existing evidence directory; the
control's ordinary named JSON output is replaceable and contains no time
field. The final receipt records the actual Python environment and source
identities. No runner cache or repository validation result is claimed.
The optional reference-page extraction used pypdf because pdftotext was
unavailable; `operational_history.json` records the missing-file read and
successful fallback, including its PDF-font warning. The extracted
definition/theorem agree with the independently viewed primary-source page.

The beta>0 assumption is explicit. Beta=0 would give a nilpotent/shear
ODE and beta<0 a trigonometric ODE; neither is the claimed Lorentz case.
If R=0 the actual current vanishes. C3 with beta>0 then forces
\(\delta_h=0\), so C7–C11 remain valid in that degenerate case.

The result closes the specified **conditional integration** obligation.
Its physical application still requires a justified density and state,
the exact remaining local identities C3, and any requested positivity.
It derives neither those inputs nor a nontrivial example of their joint
realization. Mass shells, geometric momentum, multiple boosts, rotations,
channels, scattering/exhaustion and physical observable identification
remain outside the claim. The theorem is not a failed-search no-go or a
new physical premise.

At the author freeze, a fresh independent source review was required for the complete final note, matched upstream hypotheses and controls before substantial downstream reuse; that review is now complete and recorded below. The reviewed upstream results and root's proposed route do not
independently certify this author result. Frozen author operational record: no Lean formalization, repository pipeline, commit, PR, merge, push or audit action was performed by this worker. No editable prompt, axiom, prior frozen input or Git ref was changed.
The selected model/effort were preserved; no subdelegation or other-chat
message was used. The fixed deadline is 2026-10-12 16:00:52 UTC.


## Publication evidence and review record

The complete frozen author source is `INTEGRATED_BOOST_COVARIANCE_PROBE.md`, SHA-256
`71fe0b4cc1df0b34ef0ca55484ad8faffabe8155efa582bf09fc2eec8622c5ed`. Its separate review is `INTEGRATED_BOOST_COVARIANCE_REVIEW.md`, SHA-256
`273ea8db025c5c469864867d55ea0afe7adb05987c2eaef15b8c06825d0738f1`, with receipt SHA-256 `8a0988c3db50a91d937b8af78e3792df951392fd50866d65664f4889a7ab0ca6`.
The [evidence map](../.claude/science/physics-loops/toe-boost-gap-fock-closure-20261012/EVIDENCE_MAP.json) preserves the complete own
author/reviewer sources, earlier versions, failures, stdout/stderr, execution
receipts, root source-coverage records and their byte identities. The
[exact transformation map](../.claude/science/physics-loops/toe-boost-gap-fock-closure-20261012/PUBLICATION_EDITS.json) and
[reconstruction program](../.claude/science/physics-loops/toe-boost-gap-fock-closure-20261012/reconstruct.py) recover every byte of
this complete note and its entire primary. No mathematical correction is made.
Historical review-pending and worker-scope statements above describe the author
freeze; this separate appendix records the completed source review.

**Author/checker pairing:** Same selected model family in separate author/reviewer contexts; the selected model and reasoning effort were preserved. Candidate formulas and reported outcomes were visible before distinct controls, so this was neither blinded nor cross-family checking. Root proposed mechanisms and is a coauthor, not the independent reviewer. The mechanical preparer performed no new scientific review.

The complete C1-C28 source review requires no mathematical correction.
Actual rapid almost-local flows, finite seminorm losses and the moving-vector
product rule integrate the two remaining supplied local Lie identities. The
comparison group exists before classical-solution uniqueness is applied.
Canonical cyclic equality then gives complete Stone generators on maximal
joint-spectral sum domains, the inverse spectral-set image and the optional
positive-energy cone. No common core, analytic-vector or preexisting strong-
commutation premise is inserted. This closes the specified conditional
one-direction integration obligation, not physical realization of its inputs.

Boost B1-B37 is a direct dependency. Joint J9-J10 also directly supplies the
bounded Fourier/Gaussian spectral approximation used after commuting canonical
unitaries are established. The separate Joint J1-J3 mixed-history route is an
optional comparison and is not applied to the spatially weighted boost.
Gap-filter and weighted-closure results are not premises here. The uniqueness
argument is supplied in the note; its Engel-Nagel page is corroborating context
and remains externally inventoried without a new paper-reading claim.

The whole author helper has 71 recorded predicates. Its five original active
CLI branches fail 39, 13, 3, 3 and 50 predicates. The reviewer separately kept
the baseline byte-identical and materialized all six operative branch choices
for each mutant into complete helpers, preserving every comparator and gate.
All six review replays reproduce their original final stdout and result JSON
bytes. Both the original CLI representation and every reviewer source/diff,
stream, receipt and result are preserved. Reverse boosts still pass group-law
and mass-invariant checks; zero-rapidity energy is even; generator mixing does
not test the spatial divisor; selected projections may miss an energy phase.
Differential coefficient checks do not prove self-adjointness or full domains.

The author's initial domain helper assigned the expected partial norm directly.
Its corrected explicit sum, original helper and all six initial/final runs are
retained; the proof did not change. The separate reviewer froze its reconstruction
and planar Schwartz/Gaussian control before author helper/output exposure, while
the target's formulas and reported results were already visible. Its 38 exact
predicates and five whole-source mutants (2, 4, 1, 9 and 12 failed predicates)
test moving inputs, set images, intersection-domain restriction, beta and boost
direction. The cancellation-strip and distinct self-adjoint-extension witnesses
retain their exact scopes. Integrity controls reject altered or missing source;
that is provenance evidence, not a mathematical certificate. Root's earlier
text-spacing matcher failure and AST-only verifier repair remain preserved.

The theorem constructs conditional connected 1+1 translation/boost covariance
in the declared clocks. The intended density, invariant state, beta>0 and two
remaining local identities are supplied, with positive H optional. It supplies
no nontrivial common microscopic example, fixed mass, isolated shell, geometric
momentum identification, rotations, additional boosts, higher-dimensional
Poincare theorem, particles or scattering/exhaustion conclusion.

The [canonical finite primary](../scripts/integrated_boost_covariance_2026_10_12.py) retains every
original calculation and failure gate. Publication adds only mapped input and
timeout declarations, an assertion guard and finite-scope output. Original
adjacent-result writes are suppressed where present; the complete original
JSON outputs remain in the evidence map. Required output destinations in the
Boost and Integrated CLIs become optional for ordinary canonical execution.
Where present, self-hash calculations remain and refer to the source actually run.

Preparation ran no primary, mutant, independent control, runner-cache API,
vocabulary fixer, graph builder or audit compatibility check. Actual canonical
execution and complete original mutation replay are root's subsequent work,
recorded in [delivery checks](../.claude/science/physics-loops/toe-boost-gap-fock-closure-20261012/DELIVERY_CHECKS.md). Historical
source-bound results are not fresh canonical results. No retained promotion,
applied audit verdict, Lean certificate, helper-registry change or completed
publication is asserted here. Combined candidate validation and strict audit
lint remain separate landing gates.

This is a frozen milestone record. Root owns the sole live campaign checkpoint
and its current science-checkout pointer. Editable prompt files changed: none.
