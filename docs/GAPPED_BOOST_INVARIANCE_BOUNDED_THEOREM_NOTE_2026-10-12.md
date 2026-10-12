---
claim_id: "gapped_boost_invariance_bounded_theorem_note_2026-10-12"
claim_type: "bounded_theorem"
claim_scope: "A specified finite-range energy density with exact local current conservation and an invariant state whose canonical GNS energy has a simple positive-gap vacuum has zero current and first-moment expectation on local and rapid almost-local observables. No actual intended model, weighted-flow construction or Lorentz closure is supplied."
upstream_dependencies:
  - microscopic_current_implementation_bounded_theorem_note_2026-10-12
runner: "scripts/gapped_boost_invariance_2026_10_12.py"
actual_current_surface_status: "conditional-support"
target_claim_type: "bounded_theorem"
trace_class: "upstream_support"
target_claim_id: null
target_blocker_text: "Supply the intended density, exact conservation and simple gapped GNS vacuum, then match the separate weighted-flow theorem before use."
source_of_blocker_text: "handoff"
reachability_to_target: "partially_closes"
artifact_role: "theorem"
next_trace_action: "Supply the intended density, exact conservation and simple gapped GNS vacuum, then match the separate weighted-flow theorem before use."
conditional_surface_status: "Local current and boost state identities from a simple gapped GNS vacuum and exact conservation"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "The density, exact conservation and invariant simple gapped GNS state remain supplied; a separately matched boost theorem is downstream."
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# A simple gapped GNS vacuum and conserved current imply local boost invariance

**Conditional bounded theorem, 2026-10-12; separate complete source review requires no mathematical correction.** Root proposed the
gap-filter mechanism and is a coauthor. The conclusion below is a conditional
mathematical implication, with no audit status or physical-model existence
claim. The proof uses the actual finite-range energy dynamics, not an assumed
self-adjoint momentum or boost.

The implication is affirmative under the stated hypotheses. Exact local
current conservation makes the current expectation functional stationary
along the energy flow. A spectral filter inside the GNS gap then forces that
functional to vanish. The first-moment functional follows by the same
argument. Every required rapid almost-local extension, two-derivation
identity, time derivative and filter exchange is proved below. In particular,
the energy-flow seminorm bounds grow polynomially in time. The filtered
observable has scalar **vacuum columns for it and its adjoint**; it need not
be scalar as an algebra element or represented operator.

S denotes the original research collection. The [frozen milestone handoff](../.claude/science/physics-loops/toe-boost-gap-fock-closure-20261012/HANDOFF.md) and [evidence map](../.claude/science/physics-loops/toe-boost-gap-fock-closure-20261012/EVIDENCE_MAP.json) preserve the original source bundles and complete own evidence. The direct in-branch proof dependencies are [Current](MICROSCOPIC_CURRENT_IMPLEMENTATION_BOUNDED_THEOREM_NOTE_2026-10-12.md): Finite current pair algebra and the canonical uniform finite-range dynamics at the source-matched hypotheses; no extra actual-operator assumptions are imported. Other named sources are historical context or transitive dependencies unless their use is stated explicitly. Joint J17 is an optional test of the supplied conservation premise; the weighted-flow theorem is downstream, not a premise of G1-G6 implies G7.

## 1. Sources, scope and provenance

| Complete source read | SHA-256 | Use |
|---|---|---|
| ROOT_GAPPED_BOOST_INVARIANCE_LEAD.md | c9933c04b43c818ba3a12c02fe82e9526742a2e9b50eb290947980c47b3c77e7 | Unverified coauthor proposal, examined rather than presumed true |
| MICROSCOPIC_CURRENT_IMPLEMENTATION_PROBE.md | bcc9b9503e49c17b6e6140c22f3971f35ccd3ed72de16f0371666dc9162dfd9a | Finite current identity I6–I10 and canonical finite-range dynamics I14–I22 |
| MICROSCOPIC_CURRENT_IMPLEMENTATION_REVIEW.md | 305fa33efebf1e9f9dc09d0854eddf23065877004888f55e964d31cc403f6d17 | Existing source-bound review of that conditional theorem |
| MICROSCOPIC_JOINT_FLOW_PROBE.md | 35bcb1013b0716a4faa33fdbd75ff067427c1dec8e377f63ebb17ac301786ebd | Exact conservation is a finite one-site operator criterion, not a generic consequence of the current formula |
| MICROSCOPIC_JOINT_FLOW_REVIEW.md | 9699043c35343901ef75ab6a29dd560ba4aa30f8a3b908643e959958e86447c9 | Existing source-bound review; receipt a31a20468660e38ff42bf215dd84832a1f722551c29ea770156dfc71781d4b06 |
| MICROSCOPIC_BOOST_FLOW_PROBE.md | 7ec1d7eecb4eba020548eba8b56dff66712f52b4eba634ba276dd67440d28de7 | Optional downstream use only; its weighted-flow theorem is not a premise of the standalone proof below |

The boost-flow author receipt is
`556db66a03600f637ba47663e4faca9202d48baab65cbf81828e08015faa15c9`.
At dispatch its independent review was pending. This note supplies the local
state identities that theorem requests, if its other hypotheses and final
reviewed source are matched. It does not silently reuse the provisional
weighted-flow theorem to prove those identities.

Root supplied main instruction authority
`a13caa4885f547c8d206265b031ba7649e539fd9`, planning authority
`3a4b2c66a1ead7a1c48b4359627e968f681e3c39`, and science checkout
`dc7f415f73df3754653f4985382ca0fb96f07cda`. The planning snapshot is
`3d409e93abb3b58796a9c10ca6d21ba93b7edc73b8fb24e7364da97c805580a9`.
Instructions and sources were copied and hashed in
`gapped_boost_invariance/sources/manifest.json`. No Git operation was used
by this worker; freshness of refs and publication belongs to root. Current
repository physics-loop/workhorse entries match the installed entries. The
current repository `review-loop/references/FIXES_AND_REPORTING.md` was read,
including its output-preservation requirements.

The minimal axiom source and primitive registry were inspected. The theorem
uses none of the three registered primitives to supply a density, a selected
state, a spectrum or a conservation identity. Those are explicit mathematical
hypotheses here; no framework axiom or primitive is added. The scoped source
search and all its output are saved under `gapped_boost_invariance/logs/`.
Matches included the existing current implementation and conditional
scattering/locality inputs, but did not supply this precise state-invariance
implication. No exhaustive repository, open-proposal or literature novelty
claim is made.

## 2. Exact theorem and hypotheses

Let \(\mathcal A\) be the quasilocal tensor algebra of fixed
finite-dimensional full matrix algebras on \(\mathbb Z^d\), \(d\ge1\),
with the \(\ell^1\) metric. Write
\(B_L=\{x:|x|_1\le L\}\), and let \(\mathcal A_{\rm loc}\) be
the local algebra. Fix a coordinate b and the translation convention
\(\tau_j\mathcal A(X)=\mathcal A(X+j)\). Supply a finite-range density
\[
 h_x=\tau_x(h_0)=h_x^*,\qquad
 \operatorname{supp}h_x\subset x+B_R,\qquad
 \|h_x\|\le h<\infty,\qquad R\in\mathbb N_0.                 \tag{G1}
\]
On local observables define the finite sums
\[
 \delta_hA=i\sum_x[h_x,A],\qquad
 \delta_bA=i\sum_xx_b[h_x,A].                               \tag{G2}
\]
The actual energy dynamics \(\alpha_t\) is the canonical point-norm
continuous finite-range flow with local generator \(\delta_h\), equivalently
the norm limit of finite-volume energy flows. Its existence and equivalence
are supplied by the finite-range construction in the frozen current source
I14–I22. They also follow from its connected-history Taylor remainders;
no boost dynamics is needed. Each local derivation in G2 maps locals to locals.

Use the actual energy-current density and derivation
\[
 p_b(x)=\frac i2\sum_{|r|_1\le2R}r_b[h_x,h_{x+r}],\qquad
 \delta_pA=i\sum_x[p_b(x),A].                               \tag{G3}
\]
It is Hermitian, supported in \(x+B_{3R}\), and has
\(\|p_b(x)\|\le h^2c_{R,b}\), where
\(c_{R,b}=\sum_{|r|_1\le2R}|r_b|\). Its local derivation obeys
\[
 [\delta_h,\delta_b]A=\delta_pA
 \qquad(A\in\mathcal A_{\rm loc}).                         \tag{G4}
\]
To recall why no divergent rearrangement occurs, pad a finite center set I
by 3R about the support of A. Both second derivatives are finite commutators
with \(H_I=\sum_Ih_x\) and \(B_I=\sum_Ix_bh_x\). Finite Jacobi and
\([H_I,B_I]=\tfrac12\sum_{x,y\in I}(y_b-x_b)[h_x,h_y]\) give G4.
A surviving pair overlaps and has at least one member meeting the support
of A, so this padding includes every contribution. For R=0, p=0.

The additional algebraic hypothesis is **exact local conservation**:
\[
 [\delta_h,\delta_p]A=0
 \qquad\hbox{for every }A\in\mathcal A_{\rm loc}.             \tag{G5}
\]
It is an operator identity in the local algebra. The finite criterion J17
of the frozen joint-flow source can test it on a complete one-site matrix
basis with adequate padding. Neither stationarity, the current formula,
expectations of selected observables nor a commutator on the vacuum alone
establish G5.

Supply an \(\alpha\)-invariant state \(\omega\). Let
\((\pi,\mathcal H,\Omega)\) be its normalized cyclic GNS representation,
and let H be the actual canonical generator:
\[
 e^{itH}\pi(A)\Omega=\pi(\alpha_t(A))\Omega,
 \qquad H\Omega=0.
\]
Assume
\[
 H\ge0,\qquad \ker H=\mathbb C\Omega,\qquad
 \operatorname{spec}H\subset\{0\}\cup[\Delta,\infty)
 \quad\hbox{for some }\Delta>0.                            \tag{G6}
\]
This is a simple gapped vacuum in this particular representation. No
uniqueness of all algebraic ground states is required. No self-adjoint P or
B, boost-state invariance or current-state invariance is assumed.

**Theorem.** Under G1–G6,
\[
 \boxed{\quad\omega(\delta_pA)=0,
             \qquad\omega(\delta_bA)=0
             \quad(A\in\mathcal A_{\rm loc}).\quad}          \tag{G7}
\]
The same identities hold for every rapid almost-local A, with the uniquely
continuous extensions defined next. This theorem asserts infinitesimal local
state invariance; any all-time boost implementation uses the separately
reviewed weighted-flow construction after premise matching.

## 3. Rapid almost-local topology and all finite derivation graphs

Let \(E_L\) be normalized partial trace onto \(\mathcal A(B_L)\),
extended as a contractive conditional expectation to \(\mathcal A\).
Nested expectations satisfy \(E_LE_r=E_{\min(L,r)}\). For nonnegative
integers n put
\[
 p_n(A)=\|A\|+\sup_{r\ge0}(1+r)^n\|(1-E_r)A\|,
 \qquad\mathcal A_{\rm al}=\bigcap_{n\ge0}\{A:p_n(A)<\infty\}.
                                                                  \tag{G8}
\]
Allowing all real nonnegative exponents gives the same space and topology.
The center is a fixed origin; a change to another fixed origin gives equivalent
seminorms, not a uniform bound over all translations.

Each finite-p_n space is complete. A p_n-Cauchy sequence is norm-Cauchy,
and every tail map is norm-continuous; passing to the norm limit preserves
its uniform tail Cauchy bound. Thus the countable intersection is Fréchet
complete. It is a *-algebra: compare AB to \((E_rA)(E_rB)\) and apply
\(1-E_r\), whose norm is at most two. This bounds its tail by
\(2(\|A\|\|(1-E_r)B\|+\|B\|\|(1-E_r)A\|)\).
Adjoints preserve every p_n.

For q>n the nested expectations give
\[
 p_q(E_LA)\le p_q(A),\qquad
 p_n(A-E_LA)\le2(1+L)^{n-q}p_q(A).                         \tag{G9}
\]
Indeed, for r≤L the tail of \((1-E_L)A\) equals \((1-E_L)A\);
for r≥L it equals \((1-E_r)A\). Bounding these two regions and the norm
term proves G9. Locals are therefore dense in the full rapid topology.

Consider any of the more general local derivations
\[
 D_wC=i\sum_xw(x)[g_x,C],\quad
 \operatorname{supp}g_x\subset x+B_\rho,\quad\|g_x\|\le g,
 \quad |w(x)|\le W(1+|x|)^\kappa,                           \tag{G10}
\]
where \(\kappa\in\mathbb N_0\), \(W,g<\infty\), and the g_x and
weights are Hermitian and real when a *-derivation is required. Translation
covariance is unnecessary for this graph lemma. For local C in B_L,
\[
 \operatorname{supp}D_wC\subset B_{L+2\rho},\qquad
 \|D_wC\|\le K(1+L)^{d+\kappa}\|C\|,
 \quad K=2gW3^d(1+\rho)^{d+\kappa}.                        \tag{G11}
\]
Only centers in B_(L+rho) contribute. Count them using
\(|B_a|\le3^d(1+a)^d\) and bound their weights. A local operator in B_L
has \(p_n(C)\le3(1+L)^n\|C\|\). Consequently
\[
 p_n(D_wC)\le3K(1+2\rho)^n(1+L)^{n+d+\kappa}\|C\|.         \tag{G12}
\]

For A rapid AL decompose
\(C_0=E_1A\), \(C_m=E_{2^m}A-E_{2^{m-1}}A\), m≥1.
This is a convergent sum in every seminorm by G9. It obeys
\[
 \operatorname{supp}C_m\subset B_{2^m},\qquad
 \|C_m\|\le2^{q+1}(1+2^m)^{-q}p_q(A)\quad(m\ge1).          \tag{G13}
\]
Put u=n+d+κ. For q>u, G12–G13 prove absolute convergence in p_n and
\[
 \begin{split}
 D_wA&:=\sum_{m\ge0}D_wC_m,\\
 p_n(D_wA)&\le C_{n,q}p_q(A),\\
 C_{n,q}&=3K(1+2\rho)^n
       \left(2^u+\frac{2^{q+1}}{2^{q-u}-1}\right).
 \end{split}
 \tag{G14}
\]
The zeroth term has the 2^u bound; the rest use
\(\sum_{m\ge1}2^{-m(q-u)}=(2^{q-u}-1)^{-1}\).
These are finite constants with strict q>u; no endpoint or optimality claim
is made. By density the extension is unique among continuous extensions in
this topology. The Leibniz and adjoint rules extend by continuity.

There is also an absolutely norm-convergent density formula
\[
 D_wA=i\sum_xw(x)[g_x,A]\qquad(A\in\mathcal A_{\rm al}).     \tag{G15}
\]
For a distant center x, g_x commutes with \(E_{|x|/2}A\) once
\(|x|>2\rho\). The norm of that summand is at most a fixed constant
times \(p_q(A)(1+|x|)^{\kappa-q}\). Sum over dyadic annuli, whose
cardinalities are bounded by a constant times \(2^{md}\); q>d+κ
makes the sum converge. The remaining centers are finite. Apply the same
majorant to E_LA, using G9, and take L→∞ term by term. Its sum agrees
with the extension G14 by graph convergence and with the local formula on
each E_LA. This identifies the two definitions without rearranging an
uncontrolled infinite sum.

Take q=n+L_w in G14, with \(L_w=d+\kappa+1\). Then
\(p_n(D_wA)\le C_{n,w}p_{n+L_w}(A)\). For every finite word
\(D=D_{w_1}\cdots D_{w_k}\), iteration proves
\[
 p_n(DA)\le C_{n,D}p_{n+L_D}(A),\qquad
 L_D=\sum_{j=1}^k(d+\kappa_j+1).                          \tag{G16}
\]
All intermediate elements are rapid AL. In particular, for q>n+L_D,
\[
 p_n\bigl(D(A-E_LA)\bigr)
 \le2C_{n,D}(1+L)^{n+L_D-q}p_q(A).                         \tag{G17}
\]
This proves local approximation in every finite graph, not merely norm
approximation of A. The empty word is the identity. It also covers zero
densities without dividing by their norms.

For energy and current use κ=0, with losses d+1 and radii R, 3R.
For the boost use κ=1, loss d+2, radius R and w(x)=x_b. G16–G17
therefore extend both local identities to all rapid AL A:
\[
 [\delta_h,\delta_b]A=\delta_pA,
 \qquad [\delta_h,\delta_p]A=0.                             \tag{G18}
\]
For clarity, approximate A by E_LA in G4/G5. The two boost-energy words
have total loss 2d+3; the two energy-current words have loss 2d+2.
For any output p_n, the common input p_(n+2d+4) makes every error in
G17 tend to zero. This justifies the two-derivation identity extension
before it is used on evolved or filtered observables.

## 4. A finite-volume light-cone estimate

Here is a self-contained estimate for the uniform energy dynamics. Assign
h_x to the nonempty set x+B_R. Its interaction Φ has
\[
 |Z|\le s:=|B_R|,\qquad\operatorname{diam}Z\le\ell:=2R,
 \qquad J:=\sup_z\sum_{Z\ni z}\|\Phi(Z)\|\le s h.           \tag{G19}
\]
Finite-volume cutoffs only delete terms and preserve these bounds.
Let \(\alpha_t^\Lambda\) be one such finite-volume flow. For B
supported in Y define
\(C_B(X,t)=\sup_{0\ne A\in\mathcal A(X)}
\|[\alpha_t^\Lambda A,B]\|/\|A\|\).
Within G20–G23, Φ denotes the retained interaction in this finite
volume; its s, ℓ and J bounds remain those in G19.
For t≥0,
\[
 C_B(X,t)\le C_B(X,0)+
 2\sum_{Z:Z\cap X\ne\varnothing}\|\Phi(Z)\|
           \int_0^t C_B(Z,u)\,du.                         \tag{G20}
\]
To derive this inequality, put
\(K_X=\sum_{Z\cap X\ne\varnothing}\Phi(Z)\) and
\(F(t)=[\alpha_t^\Lambda A,B]\). Jacobi gives
\[
 F'=i[\alpha_t^\Lambda K_X,F]
       -i[\alpha_t^\Lambda A,[\alpha_t^\Lambda K_X,B]].
\]
The homogeneous equation is conjugation by a finite-dimensional unitary
propagator, so variation of constants preserves its norm. Isometry gives
the factor 2||A|| in the inhomogeneous term; then take the supremum.
For negative times use the interaction -Φ, with identical estimates.

Iteration of G20 is legitimate in finite volume. For disjoint X,Y it gives
\[
 C_B(X,t)\le2\|B\|
       \sum_{m\ge1}\frac{(2|t|)^m}{m!}a_m(X,Y),            \tag{G21}
\]
where a_m is the sum of \(\prod_{j=1}^m\|\Phi(Z_j)\|\)
over chains Z_1 meeting X, each Z_(j+1) meeting Z_j, and Z_m meeting Y.
Dropping the last restriction yields
\[
 a_m\le |X|J(sJ)^{m-1}.                                  \tag{G22}
\]
The first step has total weight at most |X|J, and each next step at
most sJ. The remainder after m iterations is bounded by the same
quantity times \(2\|B\|(2|t|)^m/m!\), hence tends to zero.
Thus the infinite series in G21 follows from actual finite ODEs, not a
formal expansion of the growing observable's support.

A contributing chain also satisfies dist(X,Y)≤mℓ. Multiplication by
\(\exp(m\ell-\operatorname{dist}(X,Y))\) is consequently an upper
bound on its indicator. With \(v=2sJe^\ell\), summing G22 gives
\[
 \|[\alpha_t^\Lambda A,B]\|
 \le2\|A\|\|B\|\,|X|\,
       e^{v|t|-\operatorname{dist}(X,Y)}.                  \tag{G23}
\]
The trivial commutator bound remains available. If J=0 the dynamics is
the identity and the disjoint commutator vanishes; the displayed bound
remains valid with v=0. No division by J is required. The bounds are
independent of Λ and |Y|.

For A supported in B_L take Λ containing B_L. For r≥L, E_r in finite volume is Haar averaging
over the unitaries in the outside tensor factor. Every such unitary has
norm one and its support is at distance at least r−L from B_L.
Average G23, combine with \(\|1-E_r\|\le2\), and pass to the norm
thermodynamic limit. This gives
\[
 \|(1-E_r)\alpha_t A\|
 \le2\|A\|\min\{1,\ |B_L|e^{v|t|-(r-L)}\}\quad(r\ge L).
                                                                  \tag{G24}
\]
For r<L the bound 2||A|| suffices. This argument permits arbitrarily
large outside unitary supports; no hidden |Y| factor is lost in the
conditional expectation step.

## 5. Polynomial energy-flow bounds and differentiability

For n≥0 let
\(M_n=\sup_{r\ge0}(1+r)^n e^{-r/2}<\infty\).
Split the tail supremum at \(r_*=2(L+v|t|+1)\). Below r_* the
trivial bound contributes at most
\(2\cdot3^n\|A\|(1+L+v|t|)^n\). Above it,
\(v|t|-(r-L)<-r/2\), so G24 contributes at most
\(2M_n|B_L|\|A\|\). Since
\(|B_L|\le3^d(1+L)^d\), a sufficient local estimate is
\[
 p_n(\alpha_t A)\le K_n(1+|t|)^n
                    (1+L)^{n+d}\|A\|,
 \quad K_n=1+2[3(1+v)]^n+2\cdot3^dM_n.                    \tag{G25}
\]
The constants are deliberately coarse. This cone split is the step that
converts the exponential light-cone estimate into a polynomial in time.

Apply G25 to the dyadic decomposition G13. For every q>n+d,
\[
 \boxed{\quad
 p_n(\alpha_t A)\le K_n
 \left(2^{n+d}+\frac{2^{q+1}}{2^{q-n-d}-1}\right)
 (1+|t|)^n p_q(A),\qquad A\in\mathcal A_{\rm al}.\quad}    \tag{G26}
\]
Absolute convergence in every p_n follows. Its norm limit is α_tA
by isometry, so the element defined by the rapid sum is the actual energy
orbit. The choice q=n+d+1 will be used below. This proves preservation
of rapid AL and equicontinuity on compact time intervals, with an explicit
finite loss in the input seminorm.

Let L_h be the closed norm generator of α. Locals are in its domain and
L_hA=δ_hA there. G9 and G17 give norm graph approximation by E_LA,
so closedness gives
\[
 \mathcal A_{\rm al}\subset\operatorname{Dom}L_h,
 \qquad L_hA=\delta_hA.                                   \tag{G27}
\]
The generator commutes with its actual group on its domain: apply α_t
to the norm difference quotient. Thus
\(\partial_t\alpha_t A=\alpha_t\delta_hA=\delta_h\alpha_tA\)
in norm for rapid AL A.

To justify differentiation in stronger seminorms, first prove continuity
there. For q>n>0, interpolation of the two tail bounds
2||C|| and \(p_q(C)(1+r)^{-q}\) yields
\[
 p_n(C)\le\|C\|+(2\|C\|)^{1-n/q}p_q(C)^{n/q}.              \tag{G28}
\]
For n=0 use p_0≤3||·||. Apply G28 to α_tA−α_sA. Its norm tends to
zero, while G26 bounds its higher seminorm uniformly for t near s.
Hence every rapid orbit is continuous in every p_n. Since δ_hA is
also rapid AL, the norm identity
\(\alpha_tA-A=\int_0^t\alpha_u\delta_hA\,du\) holds as a
Fréchet integral too: its continuous Riemann sums converge in each complete
seminorm and have the stated norm limit. Therefore
\[
 p_n\left(\frac{\alpha_tA-A}{t}-\delta_hA\right)
 \le\sup_{|u|\le|t|}p_n(\alpha_u\delta_hA-\delta_hA)
 \longrightarrow0.                                      \tag{G29}
\]
Translation in time and iteration prove smooth rapid AL orbits. In
particular every finite continuous derivation word may be applied after a
time derivative. No analytic-vector radius for a boost is asserted.

Combining G16 with G26 also proves the explicit graph-orbit bound
\[
 p_n(D\alpha_tA)\le K_{n,D}(1+|t|)^{n+L_D}
                          p_{n+L_D+d+1}(A)                \tag{G30}
\]
for every finite word D from §3. This is the domination needed for all
later graph-valued filter integrals.

## 6. Stationarity of the current functional

State invariance and norm differentiation imply
\(\omega(\delta_hC)=0\) for local C. G9/G17 extend it to every
rapid AL C. Define the continuous linear functionals
\[
 \ell_p(C)=\omega(\delta_pC),\qquad
 \ell_b(C)=\omega(\delta_bC).                              \tag{G31}
\]
They are continuous in p_(d+1) and p_(d+2), respectively, by G14.
For every rapid AL A, G29 and the two-derivation identity G18 give
\[
 \frac{d}{dt}\ell_p(\alpha_tA)
 =\omega(\delta_p\delta_h\alpha_tA)
 =\omega(\delta_h\delta_p\alpha_tA)=0.                    \tag{G32}
\]
The first equality is differentiation through a continuous functional
in the required stronger topology; the second uses the extended exact
conservation identity. The final equality applies energy stationarity to
the rapid AL element δ_pα_tA. Thus
\(\ell_p(\alpha_tA)=\ell_p(A)\) for every real t.

This establishes stationarity of the functional without assuming that
ω is invariant under a current flow, and without an unbounded P or
formal Hilbert-space commutator.

## 7. Gap filtering, both vacuum columns, and the exchanges

Choose a real even \(g\in C_c^\infty((-\Delta,\Delta))\) with
g(0)=1, and let f be its inverse Fourier transform in the convention
\[
 g(\lambda)=\int_{\mathbb R}f(t)e^{it\lambda}\,dt,
 \qquad f(t)=\frac1{2\pi}\int_{\mathbb R}g(\lambda)e^{-it\lambda}\,d\lambda.
                                                                  \tag{G33}
\]
An even smooth bump equal to one near zero is one choice. Repeated
integration by parts, including after differentiating in t, proves that
f is Schwartz; real even g makes f real and even. Also ∫f=1.
There is no positivity requirement on f.

For rapid AL A define
\[
 A_0=\int_{\mathbb R}f(t)\alpha_tA\,dt.                    \tag{G34}
\]
The norm integral exists. More strongly, G26 and the Schwartz bound make
the truncated integrals Cauchy in every p_n, so they converge in the
complete rapid algebra to the same A_0. Each finite word D in §3 can be
exchanged with this integral:
\[
 DA_0=\int_{\mathbb R}f(t)D\alpha_tA\,dt.                  \tag{G35}
\]
Indeed, on finite intervals continuity and Riemann sums justify the
exchange. The p_n tail of the right-hand side is at most
\(K_{n,D}p_{n+L_D+d+1}(A)
\int_{|t|>T}|f(t)|(1+|t|)^{n+L_D}dt\), which tends to zero
by G30. Continuity G16 controls the left-hand tail. This proves the
exchange in every graph seminorm; a merely exponential-in-time bound
would not establish it from the Schwartz condition.

The GNS spectral theorem and the actual implementation give
\[
 \begin{split}
 \pi(A_0)\Omega
   &=g(H)\pi(A)\Omega=P_0\pi(A)\Omega=\omega(A)\Omega,\\
 \pi(A_0^*)\Omega
   &=g(H)\pi(A^*)\Omega=P_0\pi(A^*)\Omega=\omega(A^*)\Omega,
 \qquad P_0=|\Omega\rangle\langle\Omega|.
 \end{split}
 \tag{G36}
\]
The first vector integral follows by applying the bounded map
C↦π(C)Ω to the norm integral. The second uses real f, so
A_0* is the same filter of A*. G6 and the strict Fourier support give
g(H)=P_0. The gap is separately assumed in G6; positivity locates the
nonzero spectrum on the positive side. A two-sided isolated simple zero
eigenvalue would suffice for this mathematical step.

For any bounded local Q, both columns in G36 give
\[
 \omega(QA_0)=\omega(Q)\omega(A)
             =\omega(A_0Q),
 \qquad\omega([Q,A_0])=0.                                \tag{G37}
\]
For example, using an inner product linear in its second entry,
\(\omega(A_0Q)=\langle\pi(A_0^*)\Omega,\pi(Q)\Omega\rangle
=\overline{\omega(A^*)}\omega(Q)\).
This calculation uses no separating property and gives no global scalar
identity for A_0. The absolutely convergent series G15 permits termwise
expectation in the current and weighted sums. Therefore
\[
 \ell_p(A_0)=0,\qquad\ell_b(A_0)=0.                       \tag{G38}
\]

Exchange δ_p and ω with G34 using G35 and boundedness of the state,
then use G32 and ∫f=1:
\[
 0=\ell_p(A_0)=\int f(t)\ell_p(\alpha_tA)dt=\ell_p(A).
                                                                  \tag{G39}
\]
This proves current infinitesimal invariance on all rapid AL observables.

## 8. The first-moment functional

For the same actual rapid orbit, G18/G29 give
\[
 \begin{split}
 \frac{d}{dt}\ell_b(\alpha_tA)
 &=\omega(\delta_b\delta_h\alpha_tA)\\
 &=\omega(\delta_h\delta_b\alpha_tA)-\omega(\delta_p\alpha_tA)
 =0.
 \end{split}
 \tag{G40}
\]
Energy stationarity applies to δ_bα_tA, and G39 applies to α_tA.
All the two-generator graph products were established in §3 before this
calculation. Thus ℓ_b is stationary along α too. The very same filtered
A_0 and G35/G38 yield
\[
 0=\ell_b(A_0)=\int f(t)\ell_b(\alpha_tA)dt=\ell_b(A).       \tag{G41}
\]
Equations G39/G41 prove G7. They derive the local state identity for the
specified first-moment density and the specified state. They do not identify
that density or state with a physical realization by definition.

## 9. Premise controls and counterexamples

**Density gauge changes must preserve the conservation premise too.**
For a Hermitian finite local density q_x, change
\(h_x\mapsto h'_x=h_x+q_x-q_{x+e_b}\). Finite reindexing on every
local observable gives
\[
 \delta'_h=\delta_h,\qquad
 \delta'_b=\delta_b+\delta_q,\qquad
 \delta'_p=\delta_p+[\delta_h,\delta_q],\qquad
 [\delta_h,\delta'_p]=[\delta_h,\delta_p]
                       +[\delta_h,[\delta_h,\delta_q]].     \tag{G42}
\]
Thus fixed energy dynamics do not fix the first moment. The current and
its conservation condition must be recomputed for the chosen density.
If both densities satisfy the theorem's hypotheses, applying the theorem
to each gives invariance for both first moments. This is a consequence of
the proved implication, not a premise declaring all gauges harmless.
An origin change adds a constant multiple of δ_h to δ_b, leaves δ_p
unchanged and preserves the concluded expectation identity.

For an exact qubit example on the one-dimensional chain, let
\(n=|1\rangle\langle1|=(1-Z)/2\) and
\[
 h_x=n_x+X_x-X_{x+1}.                                      \tag{G43}
\]
The actual energy derivation is the onsite δ_n. In the all-|0⟩ product
GNS representation, the canonical H counts flipped spins. On the dense
orthonormal basis indexed by finite sets F of flipped sites it has
eigenvalue |F|. The diagonal self-adjoint realization has zero eigenspace
\(\mathbb C\Omega\) and gap one, and implements the actual onsite flow. The state is
stationary and translation invariant.

Direct Pauli multiplication and finite reindexing give
\[
 \delta_b= i\sum_x x[n_x,\cdot]+i\sum_x[X_x,\cdot],\quad
 p_x=\tfrac12(Y_x+Y_{x+1}),\quad
 \delta_p=i\sum_x[Y_x,\cdot].                              \tag{G44}
\]
The signs use \(i[n,X]=Y\), \(i[n,Y]=-X\). At the origin,
\[
 \omega(\delta_bY_0)=-2,\qquad
 [\delta_h,\delta_p](Y_0)=2Z_0\ne0.                        \tag{G45}
\]
The gap and simple kernel survive this density coboundary, but exact
conservation fails. Hence this is a control against dropping G5, not a
counterexample to the theorem. It also explains why stationarity plus
translation invariance cannot replace G5.

**A positive gap above a degenerate kernel does not suffice.** On qutrit
sites put
\[
 n=|2\rangle\langle2|,\quad
 Q=|0\rangle\langle1|+|1\rangle\langle0|,\quad
 Y_{01}=-i|0\rangle\langle1|+i|1\rangle\langle0|,
 \quad h_x=n_x+Q_x-Q_{x+1}.                                \tag{G46}
\]
Now [n,Q]=0. Every h_x commutes with every h_y, so p=0 and exact
conservation holds. The actual energy flow is again onsite. In the all-|0⟩
product GNS representation, H counts sites in level 2; its diagonal basis
is indexed by finite modifications with labels 1 or 2. Its positive spectrum
starts at one, but every finite modification using only level 1 is in its
kernel, which is therefore not one-dimensional. The state is invariant.
Finite reindexing gives
\[
 \delta_b=i\sum_xx[n_x,\cdot]+i\sum_x[Q_x,\cdot],
 \qquad\omega(\delta_bY_{01,0})=-2.                        \tag{G47}
\]
Here α_t(Y_01,0)=Y_01,0 and the gap filter leaves it unchanged.
It maps Ω to a nonzero orthogonal zero-energy vector. This identifies the
exact failure of G36 if the simple-kernel hypothesis is removed, while
retaining the other finite-spin hypotheses and a positive excitation gap.

**Uniqueness in this GNS representation is sufficient even when algebraic
ground states are not globally unique.** For the qubit chain
\(h_x=(1-Z_xZ_{x+1})/2\), both all-|0⟩ and all-|1⟩ product states
are invariant ground states. In the first product GNS representation a
nonempty finite flipped set F has energy equal to its number of domain
walls, namely twice the number of its interval components. Thus the zero
eigenspace is \(\mathbb C\Omega\) and the gap is two in that representation. The
other product state is not an additional vector in this representation's
kernel. All h_x commute, p=0, and h_xΩ=0 makes the boost expectation
identity immediate. This exact example verifies the distinction in G6;
the theorem does not need to identify or classify all algebraic ground states.

**One scalar vacuum column is insufficient.** On \(\mathbb C^2\), set
\(\Omega=e_0\), \(C=|0\rangle\langle1|\), and Q=X. Then
\[
 C\Omega=0=\omega(C)\Omega,\qquad C^*\Omega=e_1,
 \qquad\omega([Q,C])=-1.                                  \tag{G48}
\]
This is an exact diagnostic of that shortcut, not an output of the valid
real gap filter. The adjoint condition in G36 is indispensable to the
particular commutator calculation G37.

**Even both scalar columns do not make the filtered operator scalar.**
Take H=diag(0,2,5), Ω=e_0 and a filter supported in (-1,1). For
\[
 A=\begin{pmatrix}7&1&2\\3&11&4\\5&6&13\end{pmatrix},
 \qquad A_0=\operatorname{diag}(7,11,13).                   \tag{G49}
\]
The spectral formula multiplies its ij entry by g(E_i−E_j); all
nonzero energy differences are outside the support. Both vacuum columns
equal 7Ω and every vacuum commutator expectation vanishes, while
A_0≠7I. Filtering below the vacuum gap removes vacuum excitations, not
all zero-energy-transfer operators in the full algebra.

**Other rejected analytic shortcuts.** Arbitrary norm approximations do
not supply a derivation graph approximation: for onsite h_x=Z_x,
\(A_N=X_{Ne_b}/N\) tends to zero in norm, but
\(\delta_bA_N=-2Y_{Ne_b}\) has norm two. These derivatives do not
converge, so this example does not contradict closedness. G17 supplies the
required stronger convergence. An exponential-in-time seminorm estimate
alone gives no domination under a Schwartz time integral; the cone split
G25/G26 is used before integration. Finally, a zero commutator on Ω or
only selected expectations is weaker than the local identity G5; none is
substituted for it in G32.

These controls concern the named weakened hypotheses and proof shortcuts.
They assert no universal obstruction to a physical boost model or to a
gapless or degenerate-vacuum theorem with additional hypotheses.

## 10. Author verification and remaining handoff

The standalone implication proved is G1–G6 ⇒ G7, with graph extension
G14–G18, polynomial orbit control G26/G30 and filter exchange G35. The
finite-current identity is matched to the reviewed source. The added
light-cone argument in §4 is proved directly from finite commutator ODEs,
not imported from the provisional weighted-flow construction. The spectral
theorem for the supplied self-adjoint H and elementary Fourier inversion are
the only Hilbert-space/filter tools used. No unbounded boost product or
essential-self-adjointness theorem enters this proof.

The author helper `gapped_boost_invariance/finite_controls.py` uses exact
SymPy Gaussian-rational matrices. It separately constructs the finite H/B
commutator and the oriented pair current. For the coboundary fixtures it
checks energy, boost, current and conservation actions on every one-site
matrix unit (four qubit units and nine qutrit units). These small cutoffs
are exact for those site-zero actions because every derivative in these
onsite-sum fixtures stays at site zero; they are not a claimed generic
padding theorem. Their finite physical onsite Hamiltonians, distinct from
the density cutoffs with boundary terms, have zero multiplicities one and
eight and positive gap one. The infinite-volume kernel statements in §9
are justified by their explicit diagonal GNS bases, not inferred from
finite-volume counts.

The helper also evaluates the exact finite spectral filter entry by entry,
checks both vacuum columns and every three-dimensional matrix-unit
commutator expectation, and detects the one-sided-column failure. Its
nearest-neighbor bond-chain enumeration verifies the support-chain count
and maximal travel distance through order seven. It counts immediate
overlap chains from G21, not the accumulated-support histories of a Taylor
expansion. The enumerated totals are 2,6,18,54,162,486,1458, below the
respective bounds 2·4^(m−1); each maximal distance is exactly m, rejecting
a bound with the last step omitted. These finite arithmetic checks do not
prove the general graph, light-cone, thermodynamic or filter arguments.

The final baseline completed 105 predicates with none failed in about 0.355
seconds under a declared 60-second timeout. This is an execution summary,
not a proof grade. Five explicit computation variants inject a reversed
current sign, a missing current half-factor, a globally scalar filter,
a rank-one zero projection in the degenerate fixture, or the one-sided
commutator shortcut. They returned exit 1 with respectively 5,5,1,1,1
failed predicates, under 30-second timeouts, each in less than 0.335 seconds.
The complete passing and failing rows, stdout, stderr, source hashes,
commands, timeouts, elapsed times and exit codes are preserved in `logs/`
and `mutations/`. There were no timeouts or unintended execution failures.
The zero-current qutrit fixture is nondiscriminating for current sign or
scale mutations, and scalar vacuum columns are nondiscriminating for the
global-scalar mutation; the separate operator comparison detects that
mutation. These limits are retained rather than counted as extra proof.

The cold source read found one control weakness: the initial baseline
filtered-operator comparison reused its computed matrix on both sides,
although its injected mutation was detected. The final helper compares
the entrywise spectral calculation with the separately derived G49 matrix
diag(7,11,13). The original source, output, all initial variants and the
correction record are preserved. All final controls and variants were
rerun after this source change; their output rows match the initial rows.
This was a correction to author verification, not to the analytic argument.

The analytic draft was written before the control source. Its explicit
byte snapshot was saved after the first baseline execution as
`ANALYTIC_DRAFT.after_first_control.md`; no pre-execution hash freeze or
blinded check is claimed. Both proofs and controls are this author team's
work, with shared prior knowledge of the candidate formulas. They are not
an independent proof review. The final author read and evidence inventory
are recorded in the source-bound receipt. Reproduce a baseline from
S/gapped_boost_invariance with a fresh log name:

```text
python3 run_logged.py --name reproduction --timeout 60 --source finite_controls.py --source run_logged.py -- python3 finite_controls.py --output finite_controls.reproduction.json
```

The helper's canonical JSON output can be replaced on an ordinary repeat;
the logging helper requires a unique run name so earlier execution evidence
is preserved. Initial and final executions exercised replacement at the same
canonical JSON path. A separate collision control rejected a reused log name
before child execution and preserved all three original log-file hashes.
Both Python sources compiled successfully. All 22 acquired source/instruction
files matched their original hashes at the final byte check. These checks
concern execution and provenance, not the mathematical implication.
No runner-cache API is used. Python/SymPy versions and exact
source identities are in the result JSON and receipt. No Lean formalization
or broad repository mechanical pipeline was run by this bounded author.

At the author freeze, the next scientific handoff was a fresh independent review of this exact
proof, especially the finite ODE recursion, polynomial time bounds,
two-derivation graph extension, both vacuum columns and their absolute
commutator sums. On successful premise matching, G7 supplies B3/B4 to the
separate weighted-flow theorem: B4 already follows from α-invariance, and
B3 is the conclusion proved here. Its independently reviewed final source
must still be checked before the canonical boost/current construction is
reused. This note does not establish the supplied density, state, simple
gap or exact current conservation in an intended physical model. It gives
no Lorentz closure, rotation relation, centre-density, scattering or Fock
conclusion. Those downstream questions keep their own premises.

Frozen author operational record: only this note and `gapped_boost_invariance/` were written. No editable
prompt file, framework axiom, prior frozen source, repository file, Git ref,
PR or audit result was changed. No other-chat message, model/effort override
or subdelegation occurred. Root is a coauthor, so root's author read is not
the required independent review. The fixed campaign deadline remains
2026-10-12 16:00:52 UTC.


## Publication evidence and review record

The complete frozen author source is `GAPPED_BOOST_INVARIANCE_PROBE.md`, SHA-256
`94d1f879927135d378dcafb6e9b603465155906a71fed5ca301b4354566cea14`. Its separate review is `GAPPED_BOOST_INVARIANCE_REVIEW.md`, SHA-256
`7834a02d0543fa148e2589e90d727d9ac1ef7eb354cceb7552e7f87dce853126`, with receipt SHA-256 `6175025b87d7df07ec76c37059af7554d4349eb8bffc753566dd5556d6af6b18`.
The [evidence map](../.claude/science/physics-loops/toe-boost-gap-fock-closure-20261012/EVIDENCE_MAP.json) preserves the complete own
author/reviewer sources, earlier versions, failures, stdout/stderr, execution
receipts, root source-coverage records and their byte identities. The
[exact transformation map](../.claude/science/physics-loops/toe-boost-gap-fock-closure-20261012/PUBLICATION_EDITS.json) and
[reconstruction program](../.claude/science/physics-loops/toe-boost-gap-fock-closure-20261012/reconstruct.py) recover every byte of
this complete note and its entire primary. No mathematical correction is made.
Historical review-pending and worker-scope statements above describe the author
freeze; this separate appendix records the completed source review.

**Author/checker pairing:** Same selected model family in separate author/reviewer contexts; the selected model and reasoning effort were preserved. Candidate formulas and reported outcomes were visible before distinct controls, so this was neither blinded nor cross-family checking. Root proposed mechanisms and is a coauthor, not the independent reviewer. The mechanical preparer performed no new scientific review.

The complete G1-G49 source review requires no mathematical correction.
The proof derives both local state identities from the supplied simple gapped
GNS vacuum and exact current conservation. It checks finite ODE/Lieb-Robinson
recursion without an outside-support volume, polynomial time bounds before
Schwartz filtering, both graph extensions and both scalar vacuum columns.
It never infers that the filtered observable is a globally scalar operator.
The Current note is the direct proof dependency. The Joint finite-site
criterion is an optional way to test the supplied conservation premise, and
the weighted-flow result is downstream; neither is used in G1-G6 implies G7.

The final author helper has 105 finite predicates. The five original CLI
variants fail 5, 5, 1, 1 and 1 predicates; some variants alter comparison claims
instead of the computed routine. The separate reviewer used exact rational-pair
controls with 134 predicates and five actual source substitutions, failing
24, 24, 4, 2 and 1. The complete fixtures and nondiscriminating rows remain
available. Counts indicate recorded sensitivity only, not the analytic proof.

The initial author filter comparison used its own computed matrix on both
sides. Its correction independently derives the diagonal comparison matrix;
the initial helper, all outputs, correction diff and final runs are preserved.
The saved analytic draft snapshot followed the first baseline execution;
neither a pre-execution hash freeze nor blinded author checking is claimed.
Six author result/stdout replays were bound exactly in the source review.
The degenerate vacuum, one-column shortcut, nonconserved current, density-gauge
and global-scalar counterexamples keep their original scopes. GNS vacuum
uniqueness is not uniqueness among all ground states. Actual density, state,
gap and conservation remain hypotheses; no intended physical model, Lorentz
closure, weighted-flow realization, scattering or Fock conclusion is supplied.

The [canonical finite primary](../scripts/gapped_boost_invariance_2026_10_12.py) retains every
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
