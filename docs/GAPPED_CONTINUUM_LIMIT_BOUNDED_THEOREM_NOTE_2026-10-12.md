---
claim_id: "gapped_continuum_limit_bounded_theorem_note_2026-10-12"
claim_type: bounded_theorem
claim_scope: "Chosen m,v>0 scaling of the supplied chain: actual energy/current/boost and rounded integer-shift groups converge strongly on fixed compact parameter sets, including finite words and full fermionic Fock completion. Original/centered compact-packet rates are O(a)/O(a^2). No operator-norm, uniform-in-particle-number, local-net, interacting or 3D limit."
upstream_dependencies:
  - concrete_gapped_chain_bounded_theorem_note_2026-10-12
runner: scripts/gapped_continuum_limit_2026_10_12.py
artifact_role: theorem
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: upstream_support
reachability_to_target: partially_closes
conditional_surface_status: "Chosen massive scaling of the accepted supplied one-dimensional spin model; group and domain limit in its identified full-spin GNS spaces"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
target_claim_id: null
target_blocker_text: "convergence of the actual generators' bounded groups."
source_of_blocker_text: "handoff"
next_trace_action: "Offer the checked group/domain limit as input to a separately reviewed local-observable route; no accepted named local-net target or theorem is imported here."
claim_type_reason: "Conditional theorem for the explicitly supplied one-dimensional model and stated hypotheses; finite controls supplement the full argument and confer no retained or framework-realization status."
---

**Publication status:** Completed source review and root integration found no required mathematical correction at the frozen original identity. Author-era pending-review statements below are preserved historical chronology and are superseded by this status. The complete argument remains unchanged.



# The actual gapped-chain boost has a controlled massive continuum group limit

**Author proof; independent review pending.** Root supplied the candidate
and is a coauthor. The proof below is conditional on the specified spin
family and the accepted parent construction. Its conclusion concerns
Hilbert-space representations and the actual energy, current, boost and
integer translations. It supplies no convergence of local observable nets,
fields, or interacting dynamics, and no framework parameter selection.

Fix arbitrary real `m,v>0`. As the supplied spacing `a` tends to zero, the
actual rescaled boost groups converge strongly, locally uniformly in their
parameters, to a free massive positive-energy representation of the
connected 1+1-dimensional Poincare group. Both the original spatial origin
and a shifted origin have this limit. Compact smooth one-particle packets
have an explicit `O(a)` error for the original boost and `O(a²)` for the
centered boost. These extend to fixed finite-particle packets, then strongly
to the full fermionic Fock space. The convergence is not operator-norm
convergence, nor uniform in particle number or unbounded boost times.

## 1. Source contract and actual scaling

Write S for this file's directory. All work is confined to this note and
`S/gapped_continuum_limit/`. The frozen source inputs are:

| Input | SHA-256 | Role |
|---|---|---|
| `ROOT_GAPPED_CONTINUUM_SCALING_SPEC.md` | `6849f63a704fe05d75cd48e3f2490e21c1d792003339fa64ce3975610f327dc2` | Unverified root candidate, corrected or proved below |
| `CONCRETE_GAPPED_CHAIN_PROBE.md` | `0aebc2ded245d9bc9ecae364db0d1a042f9642771ed788794dafd73fb7f621bd` | Full 930-line parent read; actual full-spin GNS identification |
| `CONCRETE_GAPPED_CHAIN_REVIEW.md` | `7c554adcf96ce281128c560af453234b346147f725879c25df17bbd9bcdb7d94` | Full source review read; no parent defect found, two control blind spots disclosed |
| `Concrete_chain_root_review_coverage.json` | `1b462069c5800e767daa00e8d1718cf5eefefbe85bc7a00fbe78d290fea01909` | Parent accepted at the supplied 1D-model/full-spin scope; no audit status conferred |

The spec's historical statement that parent review was active is superseded
by that acceptance. The parent proof supplies, for every `g>J>0`, a chosen
pure invariant full-spin GNS space unitarily identified with
`F_-(L²(T,dk/(2π)))`. Its actual canonical operators are

\[
 H_{\rm lat}=d\Gamma(E_{\rm lat}),\quad
 B_{\rm lat}=d\Gamma\!\left(i(E_{\rm lat}\partial_k+
                 E_{\rm lat}'/2)-E_{\rm lat}/2\right),\quad
 P_{\rm lat}=d\Gamma(4gJ\sin k),                         \tag{1}
\]

where `E_lat(k)=2 sqrt(g²+J²-2gJ cos k)`. Its geometric shift by an
integer n is `Γ_-(exp(-ink))`. The full-spin identification, including odd
particle numbers, its choice of vacuum, and the actual weighted-flow
construction are imported only at this explicit parent scope. The new
continuum proof does not attempt to reproduce its infinite-volume spin
existence theorem.

Choose, rather than derive, the family

\[
 \sigma_a=\sqrt{m^2/4+v^2/a^2},\quad
 g_a=\sigma_a/2+m/4,\qquad J_a=\sigma_a/2-m/4.           \tag{2}
\]

For every `a>0`, these are positive, `g_a-J_a=m/2`, and
`g_aJ_a=v²/(4a²)`. The gap is m and the parent's `c=sqrt(4gJ)` is `v/a`.
No uniform localization constant for the parent's spin automorphism as
`a→0` is assumed or needed. Its existence is used separately for each a.

Let `I_a=(-π/a,π/a)`, `H_a=L²(I_a,dq)`, with endpoints identified for
derivative domains. To remove the parent measure normalization first use
`ψ↦ψ/sqrt(2π)`. In Lebesgue normalization the scaling unitary is

\[
 (U_a\psi)(q)=\sqrt a\,\psi(aq).                         \tag{3}
\]

Thus the direct map from the parent's normalized measure has factor
`sqrt(a/(2π))`. Conjugating the one-particle operators in (1), and scaling
the boost and current by a, gives exactly

\[
 E_a(q)=\sqrt{m^2+4v^2\sin^2(aq/2)/a^2},\qquad
 p_a(q)=\frac{v^2}{a}\sin(aq)=E_a E_a',                 \tag{4}
\]
\[
 b_a^0=i(E_a\partial_q+E_a'/2)-aE_a/2,\qquad
 b_a^c=i(E_a\partial_q+E_a'/2).                          \tag{5}
\]

Specifically, `b_a^0=U_a(a b_lat)U_a*` and
`p_a=U_a(a p_lat)U_a*`; energy has no additional rescaling. We reserve
lowercase b,p for one-particle operators. The parent obtained its origin
term from the literal first moment `{X-1/2,K}/2`; its differentiated
eigenframe anticommutator vanishes. Scaling leaves `-aE_a/2`, with the
displayed sign. Commutators alone would not fix this sign.

The centered operator adds `(a/2)E_a`, corresponding to shifting the
spatial first-moment weights by `+a/2`. This is an actual origin change.
The multiplier `exp(iaq/2)` has antiperiodic endpoint values and does not
give a unitary equivalence of these two *periodic-domain* generators.
On Fock space, `B_a^ε=dΓ(b_a^ε)` is defined by its self-adjoint sector
sums. The formula `B_a^c=B_a^0+(a/2)H_a^F` means equality on, and closure
from, the finite smooth-particle common core; equality of maximal sum
domains is not asserted.

The repository instruction snapshot is the supplied main authority
`a13caa4885f547c8d206265b031ba7649e539fd9`; the supplied planning identity
is `3a4b2c66a1ead7a1c48b4359627e968f681e3c39`. The current local science
workflow, relevant skill procedures, minimal axiom memo and primitive
registry were read. Installed physics-loop/workhorse sources and the
used references matched the source snapshot byte for byte. No Git fetch
or mutation was performed under the bounded contract. The four axioms
and registered primitives do not supply the specific family (2), state,
dimension or dynamics; none is used to hide those choices. No editable
prompt, axiom, canonical runner or audit surface is changed.

## 2. Complete finite-circle domains, phases and winding

Put

\[
 u_a(q)=\int_0^q\frac{dp}{E_a(p)},\qquad
 L_a=\int_{I_a}\frac{dq}{E_a(q)}.                         \tag{6}
\]

This is a smooth increasing coordinate on a circle of length L_a, with
`u_a(±π/a)=±L_a/2`. The unitary

\[
 (S_af)(u)=\sqrt{E_a(q_a(u))}\,f(q_a(u))                 \tag{7}
\]

satisfies `S_a b_a^c S_a*=i∂_u`. On the u-circle the Fourier expansion
defines the self-adjoint derivative with domain `H¹_per`, and smooth
periodic functions are a core. For each fixed a, E_a is bounded above
and below by positive numbers with smooth bounded derivatives. The
coordinate and multiplier in (7) therefore preserve H¹, including its
periodic trace, with equivalent graph norms. Consequently

\[
 \operatorname{Dom}b_a^c=\operatorname{Dom}b_a^0
     =H^1_{\rm per}(I_a).                                \tag{8}
\]

The last equality uses the bounded real potential `-aE_a/2`. The
smooth periodic functions and trigonometric polynomials are cores for
both operators. All assertions are for fixed a; their graph-norm
equivalence constants need not be uniform in a.

There is a useful exact origin check. Multiplication by `exp(iaq/2)`
followed by (7) carries b_a^0 to `i∂_u` with **antiperiodic** boundary
condition `g(L_a/2)=-g(-L_a/2)`. Indeed
`M_exp(iaq/2)^* b_a^c M_exp(iaq/2)=b_a^0` as differential expressions,
and the multiplication changes the trace. The centered spectrum is
`{2πn/L_a:n∈Z}` and the original-origin spectrum is
`{(2n+1)π/L_a:n∈Z}`. This is not a periodic-domain gauge equivalence.

Let `F_{a,s}` be the complete real lift of the circle flow satisfying

\[
 \partial_sF_{a,s}(q)=E_a(F_{a,s}(q)),\quad F_{a,0}(q)=q,
 \quad F_{a,s}(q+2\pi/a)=F_{a,s}(q)+2\pi/a.              \tag{9}
\]

The positive speed has no singularity, and either circle completeness
or the coordinate relation `u_a(F_{a,s})=u_a(q)+s` on lifted coordinates
gives every real s. Differentiation in q gives
`∂_q F_{a,s}=E_a(F_{a,s})/E_a(q)`. With periodic extension of f,

\[
 (W_a^c(s)f)(q)=
 \sqrt{\frac{E_a(F_{a,s}(q))}{E_a(q)}} f(F_{a,s}(q)),
                                                                    \tag{10}
\]
\[
 (W_a^0(s)f)(q)=
 \sqrt{\frac{E_a(F_{a,s}(q))}{E_a(q)}}
 e^{ia(F_{a,s}(q)-q)/2}f(F_{a,s}(q)).                    \tag{11}
\]

The Jacobian proves unitarity, the flow/cocycle identities prove the
group law, and dominated convergence on smooth functions followed by
density proves strong continuity. Differentiation at zero on the cores
gives `W_a^ε(s)=exp(-is b_a^ε)`. Both amplitudes and the phase in (11)
are periodic in q. However, `F_{a,L_a}(q)=q+2π/a`, whence

\[
 W_a^c(L_a)=1,\qquad W_a^0(L_a)=-1.                      \tag{12}
\]

The original phase has nontrivial winding; dropping it changes the
finite-a operator. The opposite sign origin has the same one-winding
holonomy, so (12) alone cannot detect an origin-sign error.

For comparison of circle and line scales,

\[
 L_a\ge\int_{I_a}\frac{dq}{\sqrt{m^2+v^2q^2}}
     =\frac2v\operatorname{arsinh}\frac{v\pi}{am}
     \longrightarrow\infty.                            \tag{13}
\]

Only this divergence, not any claimed exact asymptotic for L_a, is used.

## 3. The line generator and exact limiting representation

On `H=L²(R,dq)` define `E(q)=sqrt(m²+v²q²)`, `p(q)=v²q`, and
`u(q)=v^(-1)arsinh(vq/m)`. Its inverse is
`q(u)=(m/v)sinh(vu)`, with `dq/du=E(q(u))`. The unitary
`(Sf)(u)=sqrt(E(q(u)))f(q(u))` identifies

\[
 b=S^*(i\partial_u)S,
 \quad\operatorname{Dom}b=S^*H^1(\mathbb R),\quad
 bf=i(Ef'+E'f/2).                                      \tag{14}
\]

For completeness, Fourier transformation takes `i∂_u` to multiplication
by a real frequency (with the sign set by the Fourier convention), so
it is self-adjoint on H¹. Smooth compact functions form a core: cutoff
an H¹ function with cutoffs whose first derivatives are O(1/R), then
mollify, with both function and derivative converging in L². The map S
carries `C_c^∞(R_q)` bijectively to `C_c^∞(R_u)`. Hence the former is
a core for b, not merely a formal commutator domain.

The full flat-measure domain has the equivalent descriptions

\[
 \begin{split}
 \operatorname{Dom}b
 &=\{f\in L^2:f\text{ is locally absolutely continuous},\\
 &\hspace{39mm} Ef'+E'f/2\in L^2\}\\
 &=\{f\in L^2:f\text{ is locally absolutely continuous},\\
 &\hspace{39mm} Ef'\in L^2\}.                            \tag{15}
 \end{split}
\]

The first follows by the distributional derivative in the smooth
coordinate transformation; H¹ locally has an absolutely continuous
representative. Conversely, a locally absolutely continuous f with the
displayed derivative condition gives an L² weak derivative of Sf and
hence Sf∈H¹. The second equality uses `|E'|≤v`, so the zeroth-order
term is a bounded L² multiplier. No boundary condition at infinity is
added to (15); the transformed derivative is on the complete real line.

Translations in u give

\[
 F_s(q)=q\cosh(vs)+\frac{E(q)}v\sinh(vs),\qquad
 (W(s)f)(q)=\sqrt{\frac{E(F_s(q))}{E(q)}}f(F_s(q)),
 \quad W(s)=e^{-isb}.                                   \tag{16}
\]

This constructs a strongly continuous unitary group and identifies its
full generator, rather than inferring it from infinitesimal brackets.
The exact identities

\[
 E(F_s)=E\cosh(vs)+(p/v)\sinh(vs),\qquad
 p(F_s)=p\cosh(vs)+vE\sinh(vs)                           \tag{17}
\]

follow either from `E(q(u))=m cosh(vu)` or direct substitution with the
positive square root. For any measurable multiplier h, substitution in
(16) gives

\[
 W(s)M_hW(s)^*=M_{h\circ F_s},
 \quad \operatorname{Dom}(M_{h\circ F_s})
   =\{f:(h\circ F_s)f\in L^2\}.                         \tag{18}
\]

This proves covariance as an equality with full domains. For one
particle, `Dom E=Dom p`, because E is comparable to `1+|q|`. Also
`e^{-v|s|}E≤E(F_s)≤e^{v|s|}E`, and `1+|F_s(q)|` is comparable to
`1+|q|`. Thus both right sides of (17), with their maximal multiplication
domains, have this same domain. The positive mass relation
`E²-p²/v²=m²` is an identity of joint spectral multipliers; the
unbounded difference on `Dom E²` has the bounded extension `m²1`.

Define energy and spatial-translation groups
`A(t)=exp(-itE)` and `C(y)=exp(-iyq)`. They commute. Equations (17)-(18)
give

\[
 W(s)A(t)C(y)W(s)^*
 =A\left(t\cosh(vs)+\frac yv\sinh(vs)\right)
  C\left(y\cosh(vs)+vt\sinh(vs)\right).                 \tag{19}
\]

Thus `U(t,y,s)=A(t)C(y)W(s)` is a strongly continuous representation of
`R² ⋊ R`, with the Lorentz action on the parameter pair `(t,y)` displayed
in (19). This fixes the orientation convention. It is connected 1+1
kinematics; rotations or any further spacetime dimension are not inferred.

## 4. Coefficient inequalities and the moving compact packet

For every real z,

\[
 |z-\sin z|\le |z|^3/6,\qquad
 0\le z^2-\sin^2z\le z^4/3.                             \tag{20}
\]

The first is the integral of `1-cos z≤z²/2`; the second follows from
`(|z|-|sin z|)(|z|+|sin z|)≤2|z||z-sin z|`. Factoring the difference
of the squared energies and using `E+E_a≥2m` gives, for `|q|≤R`,

\[
 0\le E-E_a\le a^2c_0(R),\quad c_0(R)=\frac{v^2R^4}{24m},
 \qquad |p_a-p|\le\frac{a^2v^2R^3}{6},                 \tag{21}
\]
\[
 |E_a'-E'|\le a^2c_1(R),\quad
 c_1(R)=\frac{v^2R^3}{6m}+\frac{v^4R^5}{24m^3}.          \tag{22}
\]

Indeed `E_a'=v²sin(aq)/(aE_a)` and `E'=v²q/E`; splitting their
difference into the sine error divided by E_a and
`v²q(E-E_a)/(E_aE)` gives exactly (22). The global bounds are

\[
 m\le E_a(q)\le E(q)\le m+v|q|,\qquad
 |E_a'(q)|,|E'(q)|\le v.                                \tag{23}
\]

For E_a use `E_a≥2v|sin(aq/2)|/a` in its derivative formula;
at a zero of the sine its derivative is zero. The bounds hold also for
the periodic lift of E_a on R, although the comparison E is not periodic.

Let `f∈C_c^∞(R)` have support in `[-R,R]`, and fix `S≥0`. The support
of `W(t)f` is `F_{-t}(supp f)`. Both time orientations obey the scalar
comparison `d|q|/d|t|≤m+v|q|`; integrating, or using (16), yields

\[
 \operatorname{supp}W(t)f\subset[-M,M],\quad |t|\le S,
 \qquad M=(R+m/v)e^{vS}-m/v.                            \tag{24}
\]

This includes the inverse-flow orientation. Smooth dependence of F and
the multiplier in (16) shows that `t↦W(t)f` is continuous in every
smooth seminorm on this common compact set, and differentiable there.
It is also continuous in the b graph norm and preserves `||bf||`.

A useful derivative bound, uniform for `|t|≤S`, is

\[
 \|(W(t)f)'\|\le D_f,
 \qquad D_f=\frac{\|bf\|}{m}+\frac{v}{4m}\|f\|.          \tag{25}
\]

This uses `(Wf)'=-iE^{-1}bWf-(E'/(2E))Wf`, unitarity and
`max_q |E'/(2E)|=v/(4m)`. The maximum occurs at `|vq|=m`.
The coefficient v/(4m), rather than the coarser v/(2m), is justified
by `max_{x≥0} x/(1+x²)=1/2`.

## 5. Duhamel comparison on the actual domains

Use the restriction `R_a:H→H_a` and its adjoint, zero extension.
They are contractions with

\[
 R_aR_a^*=1_{H_a},\qquad R_a^*R_a=Q_a=1_{I_a}.           \tag{26}
\]

They are not global unitaries. If `π/a>M`, every `R_aW(t)f` in (24)
vanishes in a neighborhood of the endpoints of I_a, hence belongs to
both periodic domains (8). Its map into each graph norm is continuous;
the explicit differential expressions, common compact support and
smooth seminorm continuity prove this directly.

For fixed s with `|s|≤S`, let
`G(t)=W_a^ε(s-t)R_aW(t)f`, with t between 0 and s in its oriented
sense. The Hilbert derivative of `R_aW(t)f` is `-iR_abW(t)f`.
The graph continuity just proved permits the product derivative of the
unitary group acting on this moving domain vector. More explicitly,
write its difference quotient as the derivative of W_a on the fixed
domain vector plus W_a times the vector difference quotient; strong
continuity and graph continuity take each term to its limit. Therefore

\[
 G'(t)=iW_a^\varepsilon(s-t)
           (b_a^\varepsilon R_a-R_ab)W(t)f,             \tag{27}
\]
\[
 W_a^\varepsilon(s)R_af-R_aW(s)f
 =-i\int_0^s W_a^\varepsilon(s-t)
           (b_a^\varepsilon R_a-R_ab)W(t)f\,dt.         \tag{28}
\]

The integrand is a continuous Hilbert-space vector and the integral is
a Bochner integral. For negative s the same oriented identity holds;
its norm estimate integrates over an interval of length |s|. Nothing
here differentiates zero extension across an endpoint.

Combining (21), (22), (25) and unitarity yields the promised estimates

\[
 \boxed{\sup_{|s|\le S}
 \|W_a^c(s)R_af-R_aW(s)f\|
 \le S a^2\left[c_0(M)D_f+\frac{c_1(M)}2\|f\|\right].} \tag{29}
\]
\[
 \boxed{\sup_{|s|\le S}
 \|W_a^0(s)R_af-R_aW(s)f\|
 \le S\left\{a^2\left[c_0(M)D_f+
                    \frac{c_1(M)}2\|f\|\right]
              +\frac{aE(M)}2\|f\|\right\}.}            \tag{30}
\]

The original-origin estimate is not obtained by treating the potential
as small in global operator norm: `a max E_a/2` tends to v, not zero.
It is small on the moving compact packet, which is precisely what (28)
tests. The centered limit improves the rate but is unnecessary for
convergence of the actual original boost.

Set `\widetilde W_a^ε(s)=R_a*W_a^ε(s)R_a`. For the compact packet above
the line vector `W(s)f` has support in I_a, so (29)-(30) also hold for
the compressed difference from W(s)f. For arbitrary `f∈H`, choose a
fixed compact smooth g close in norm. Contraction and unitarity bound
the error on f by the error on g plus `2||f-g||`, uniformly for `|s|≤S`.
Taking a→0 and then g→f proves

\[
 \sup_{|s|\le S}\|\widetilde W_a^\varepsilon(s)f-W(s)f\|
 \longrightarrow0,\qquad f\in H,\quad\varepsilon=0,c.   \tag{31}
\]

The compressed operators satisfy
`\widetilde W_a(s)\widetilde W_a(t)=\widetilde W_a(s+t)` but have
identity Q_a on H, not 1. Their failure to be globally unitary does
not obstruct this strong convergence. For every a their difference
from W(s) has norm at least one, by taking f supported outside I_a.
Thus the statement cannot be strengthened to operator-norm convergence
with these comparison maps.

## 6. Energy, current clocks, actual integer shifts, and finite words

On H_a put `A_a(t)=exp(-itE_a)` and
`C_a(y)=exp(-iy p_a/v²)`. Equation (21) and
`|exp(ix)-exp(iy)|≤|x-y|` give, for f supported in `[-R,R]⊂I_a`,

\[
 \|(A_a(t)R_a-R_aA(t))f\|
       \le |t|a^2c_0(R)\|f\|,\qquad
 \|(C_a(y)R_a-R_aC(y))f\|
       \le |y|a^2R^3\|f\|/6.                            \tag{32}
\]

The physical current clock is a continuous group for each a, but it is
not identified with continuous geometric spin translations. The actual
geometry supplies only the integer shifts

\[
 (T_a^nf)(q)=e^{-ianq}f(q),\qquad n\in\mathbb Z.         \tag{33}
\]

Choose any integer function n_a(y) with `|an_a(y)-y|≤a/2`, with either
choice at ties. Then

\[
 \|(T_a^{n_a(y)}R_a-R_aC(y))f\|
       \le aR\|f\|/2.                                  \tag{34}
\]

This is uniform in y and requires no derivative domain. In fact (33)
preserves periodic H¹ because n is integer. A noninteger multiplier
from a chosen logarithm of T_a would generally fail that domain
property. The rounded functions y↦T_a^{n_a(y)} need not be continuous
or exactly additive at finite a; they converge locally uniformly
strongly to the genuine continuous translation group C. The same
compact-packet/density argument as in §5 proves locally uniform strong
convergence for every one-particle vector for all three families in
(32)-(34), after compression by R_a and R_a*.

This convergence extends to **every fixed finite word**, mixing centered
or original boosts, energy evolution, current clocks, and actual rounded
integer translations. To prove it, denote its one-particle factors by
V_{a,j}(θ_j) with limiting factors V_j(θ_j), and set
`\widetilde V_{a,j}=R_a*V_{a,j}R_a`. Equation (26) gives the exact
factorization

\[
 R_a^*V_{a,1}\cdots V_{a,k}R_a
    =\widetilde V_{a,1}\cdots\widetilde V_{a,k}.          \tag{35}
\]

Telescope the products. Each term is bounded by a single-factor
convergence error acting on a limiting right-tail vector
`V_{j+1}⋯V_k f`. As θ ranges over a compact parameter rectangle these
right-tail vectors form a compact subset of H: the limiting factors
are jointly strongly continuous and there are finitely many of them.
Convergence uniform in parameters on a fixed vector, with a uniform
norm bound at most two on the differences, is uniform on a compact
set of vectors by a finite epsilon-net. Thus

\[
 \sup_{\theta\in K}
 \|R_a^*V_{a,1}(\theta_1)\cdots V_{a,k}(\theta_k)R_af
       -V_1(\theta_1)\cdots V_k(\theta_k)f\|
 \longrightarrow0.                                    \tag{36}
\]

The empty word is Q_a and also converges strongly to 1. Finite-word
convergence does not assume a Poincare group law at finite a. In
particular (36) applies to approximants for U(t,y,s) in (19), with
either the actual geometric translations or the current clocks.

An explicit packet rate is available if desired. Suppose all boosts
have `|s_j|≤S_j`, energies `|t_j|≤T_j`, and translations `|y_j|≤Y_j`.
Let `S_*=Σ_boost S_j`,

\[
 M_*=(R+m/v)e^{vS_*}-m/v,\qquad
 K_f=\|bf\|+
 \left(v^2M_*\sum_{\rm energy}T_j+
       E(M_*)\sum_{\rm translation}Y_j\right)\|f\|,
 \quad D_*={K_f\over m}+{v\over4m}\|f\|.               \tag{37}
\]

Every right-tail packet and its intermediate limiting boost orbit
stays within `[-M_*,M_*]`. The bound on its b graph norm follows from
`bA(t)f=A(t)(bf+tpf)`,
`bC(y)f=C(y)(bf+yEf)`, and invariance under W. If `π/a>M_*`, (36)
on f has error at most the sum of the following applicable terms:

| Factor | Error contribution |
|---|---|
| Any centered boost j | `S_j a²[c0(M_*)D_*+c1(M_*)‖f‖/2]` |
| Any original-origin boost j | Previous term plus `S_j aE(M_*)‖f‖/2` |
| Energy j | `T_j a²c0(M_*)‖f‖` |
| Current clock j | `Y_j a² M_*³‖f‖/6` |
| Actual rounded integer shift j | `aM_*‖f‖/2` |

All-centered words using current clocks have O(a²) bounds. A word with
an original-origin boost or rounded integer shift has the stated O(a)
bound. A rate is not asserted for arbitrary L² vectors obtained by
density, where no common compact support or graph norm is given.

## 7. Full Fock domains and exact covariance

Let `F=⊕_{n≥0} wedge^n H` and `F_a=⊕_{n≥0} wedge^n H_a`. The parent
identifies F_a with its actual full-spin GNS space after (3). For any
self-adjoint one-particle generator g, `dΓ(g)` means the Hilbert direct
sum of the self-adjoint sector sum g^(n), with the vacuum value zero:

\[
 \operatorname{Dom}d\Gamma(g)=
 \{\Psi:\Psi_n\in\operatorname{Dom}g^{(n)},
                 \sum_n\|g^{(n)}\Psi_n\|^2<\infty\}.     \tag{38}
\]

Here g^(n) is the closure of the sum on a smooth tensor core, **not**
its unclosed action restricted to the intersection of all one-body
domains. This distinction matters for generators with both signs.

For the line boost, `S^⊗n` sends b^(n) to `iΣ_j ∂_{u_j}`. Fourier
transformation on R^n gives its full domain as functions whose Fourier
transform times `Σ_j ξ_j` is square integrable, restricted to the
antisymmetric subspace. This permits cancellations among the frequencies;
individual partial derivatives need not all be in L². Smooth compact
antisymmetric functions are a core. One proof cuts off and mollifies
for the single constant directional derivative `Σ∂_j`: the derivative
of a radius-R cutoff is O(n/R), and convolution commutes with the
directional derivative. Averaging with the norm-one antisymmetrizer
preserves the convergence. Pulling back by S^⊗n proves the same core
claim in q coordinates.

For the centered circle boost, `(S_a)^⊗n` gives the periodic directional
derivative on the n-torus, with Fourier domain weighted by
`Σ_j 2πl_j/L_a`. Its trigonometric core and smooth core follow directly
by finite Fourier truncation. The original boost adds the bounded
n-sector potential `-(a/2)Σ_j E_a(q_j)`; hence the same n-sector domain
and smooth core suffice. Equivalently one may use the antiperiodic
condition separately in each u_j. Finite-sector truncation then gives
cores for the direct sums (38). None of these statements identifies
the two full Fock domains after adding the unbounded particle-number
dependent potential. They establish the core closure statement after
(5), which is all that is needed.

The energy, current and momentum generators are the maximal real
joint-spectral multipliers, in the n-sector,

\[
 h_n=\sum_{j=1}^n E(q_j),\qquad p_n=v^2\sum_{j=1}^n q_j,
 \qquad h_{a,n}=\sum_j E_a(q_j),\quad p_{a,n}=\sum_jp_a(q_j).
                                                               \tag{39}
\]

Their direct-sum domains are defined by square integrability of these
**total** multipliers. Write `H^F=dΓ(E)`, `P^F=dΓ(p)` and
`B^F=dΓ(b)`. Positivity gives `|p_n|≤v h_n` and hence
`Dom H^F⊂Dom P^F`. Equality must not be inferred from the one-particle
case: momenta can cancel within a sector. For example, in two-particle
coordinates r=(q1-q2)/2 and z=q1+q2, take an antisymmetric function
`χ(z)g(r)`, with χ smooth supported in |z|<1, g odd in L², and
`r g(r)∉L²`. It lies in Dom P^(2) since p_2=v²z is bounded on its
support, but not Dom H^(2), since h_2 grows linearly with |r| there.
This is an explicit domain witness, not a heuristic about cancellations.

The lifted group is `W^F(s)=Γ_-(W(s))=exp(-isB^F)`. It conjugates
the joint spectral multipliers by the coordinate change in every
variable. Consequently

\[
 W^F(s)H^FW^F(s)^*
  =M_{h_n\cosh(vs)+(p_n/v)\sinh(vs)},\qquad
 W^F(s)P^FW^F(s)^*
  =M_{p_n\cosh(vs)+v h_n\sinh(vs)},                     \tag{40}
\]

where both notation and domains include the direct sum over n and
the maximal square-integrability condition. The first multiplier is
between `e^{-v|s|}h_n` and `e^{v|s|}h_n`, so its domain is Dom H^F.
The second need not have that domain or Dom P^F. If written as a
linear combination of H^F and P^F, it is the self-adjoint closure of
that sum on Dom H^F. To see that this restriction is a core for the
maximal combination, apply joint spectral cutoffs `1_{h_n≤K}`: they
converge both on a vector and on its image under the combination;
their ranges lie in Dom H^F. This also settles domain issues caused
by cancellations in a boosted total momentum.

Second quantization of (19) gives the exact connected-group covariance
on F and the strong continuity of its representation. Its vacuum has
zero generators. Its one-particle mass is m. The relation
`(H^F)²-(P^F)²/v²=m²1` is **not** claimed on the entire Fock space:
already the vacuum and two-particle sector violate that fixed-mass
identity. No many-particle domain is transferred from the one-particle
case by analogy.

## 8. Varying Fock spaces and quantitative finite-particle limits

Set `\mathcal R_a=Γ_-(R_a)` and
`\mathcal R_a*=Γ_-(R_a*)`. Functoriality, first on tensor products and
then on their direct sums, gives

\[
 \|\mathcal R_a\|=\|\mathcal R_a^*\|=1,\qquad
 \mathcal R_a\mathcal R_a^*=1_{F_a},\qquad
 \mathcal R_a^*\mathcal R_a=\Gamma_-(Q_a).               \tag{41}
\]

The last operator is a projection and converges strongly to 1 on F.
These maps are isometries on each fixed state supported in a common
compact momentum interval, once that interval lies in I_a, including
fixed finite-particle such states. They are not global unitaries.

For any of the one-particle words V_a in §6 with limit V,

\[
 \mathcal R_a^*\Gamma_-(V_a)\mathcal R_a
       =\Gamma_-(R_a^*V_aR_a) 
       \longrightarrow\Gamma_-(V)
 \quad\text{strongly, locally uniformly in the word parameters.}  \tag{42}
\]

Here is the proof beyond a formal use of Γ. If A_a and A are
contractions, then on a decomposable n-tensor the difference
`A_a^⊗n-A^⊗n` is the sum of n terms, each with one factor
`(A_a-A)f_j` and the other factors of norm at most `||f_l||`.
One-particle locally uniform strong convergence makes every term
vanish. Finite linear combinations of tensors are dense, and the
operator differences have norm at most two, so the result extends to
the full n-fold tensor space. Commuting with the norm-one
antisymmetrizer restricts it to the fermionic sector. Finally truncate
an arbitrary Fock vector to finitely many sectors; the error on the
tail is at most twice its norm. The finite sum converges uniformly on
compact parameter sets. This proves (42), without a particle-number
uniform estimate or an exchange of two uncontrolled limits.

The groups in (42) are exactly `exp(-isB_a^ε)`, `exp(-itH_a^F)`,
`exp(-iyP_a^F/v²)` and the full-spin geometric integer shifts under
the parent identifications. Thus the limit includes the actual
original boost and actual geometric translations, not only auxiliary
one-particle multipliers. Algebraic factorization of finite words uses
`\mathcal R_a\mathcal R_a*=1` just as in (35).

The following quantitative version covers smooth, possibly entangled,
antisymmetric n-particle packets Ψ supported in `[-R,R]^n`. In the
ambient tensor space define

\[
 D_{j,\Psi}={\|b_j\Psi\|\over m}+{v\over4m}\|\Psi\|,
 \quad j=1,\ldots,n.                                    \tag{43}
\]

Under W(s)^⊗n the support stays in `[-M,M]^n` with (24), and
`||b_jW(s)^⊗n Ψ||=||b_jΨ||`. Applying the moving-vector Duhamel proof
to the **sum** of n differential expressions therefore gives

\[
 \begin{split}
 &\sup_{|s|\le S}
 \|\Gamma_n(W_a^c(s))R_a^{\wedge n}\Psi
             -R_a^{\wedge n}\Gamma_n(W(s))\Psi\|\\
 &\quad\le Sa^2\left[c_0(M)\sum_jD_{j,\Psi}
                   +\frac{n c_1(M)}2\|\Psi\|\right].   \tag{44}
 \end{split}
\]

For the original boost add `Sa nE(M)||Ψ||/2`. The notation
`Γ_n` means restriction to the n-sector. Individual b_j need not
preserve antisymmetry; they are used in the ambient tensor norm to
bound the invariant sum. Their separate graph norms cannot be replaced
by the norm of the total boost, since the latter permits cancellations.

For energy, current and rounded integer translations the respective
n-sector bounds are

\[
 |t|na^2c_0(R)\|\Psi\|,\qquad
 |y|na^2R^3\|\Psi\|/6,\qquad
 naR\|\Psi\|/2.                                        \tag{45}
\]

These follow by the difference of the total phases, or by tensor
telescoping. For a finite word use (37) with each `||bf||` replaced
by `||b_jΨ||`, the same phase bound added for each j, and sum over j
in the boost row; the other rows gain the displayed factor n.
For a finite Fock vector the squared sector bounds may be added and
square-rooted, since the sectors are orthogonal. Such rates require
fixed finite sectors, supports, parameters and derivative norms.

## 9. Preserved finite-lattice obstruction and the scope of this limit

On the finite-a smooth core the exact scaled brackets are

\[
 [b_a^\varepsilon,E_a]=ip_a,\qquad
 [b_a^\varepsilon,p_a]=iv^2E_a\cos(aq),\qquad
 [E_a,p_a]=0.                                          \tag{46}
\]

The origin potential commutes with both multipliers. For every a>0,
`E_a cos(aq)` is not a constant multiple of E_a on the circle: dividing
by the strictly positive E_a would require cos(aq) to be constant
almost everywhere. The parent local Pauli-orbit calculation rules out
the corresponding scalar closure of this density before entering the
GNS representation. Neither obstruction is erased by this continuum
theorem. They are two realizations of the same fixed-model residual,
not two independent physical walls.

The parent's normalized rapidity is `ρ=vs`, since
`a b_lat=v(b_lat/c)`. Its old fixed-model patch bound kept m/c fixed
while shrinking dimensionless momentum k. Here

\[
 m/c=am/v\longrightarrow0,\qquad k=aq,\qquad
 |k|\le aR.                                            \tag{47}
\]

Inserting (47) into the parent flow bound gives
`a[R cosh|ρ|+sqrt(R²+(m/v)²)sinh|ρ|]`: a fixed physical support
expands by a fixed physical amount at fixed rapidity while its
dimensionless support still shrinks with a. The old obstruction
assumed a fixed positive m/c; this family changes that hypothesis.
It is consequently compatible with the old limitation rather than a
counterexample to it. Fixed-a winding at time L_a is likewise preserved;
the theorem is uniform only on fixed compact time intervals, while
L_a diverges by (13).

This is a constructive limit of the chosen family of full-spin GNS
representations after explicit interspace maps. It does not construct
maps of the local spin observable algebras with convergent localization
regions. In particular the parent's exponentially localized
diagonalizing maps have a-dependent decay constants, and no uniform
control of them has been supplied. Wightman fields, local nets,
interacting scattering, three-dimensional symmetry, a physical
identification of v or m, and framework selection of (2) require
additional arguments. No inability or impossibility theorem for those
tasks is asserted.

## 10. Negative-claim discipline and remaining obligations

The negative statements here have exact scopes: fixed-a scalar closure
fails for (46), the half-origin multiplier changes the circle boundary
condition, compressed convergence is not in global operator norm, and
the parent's fixed-m/c shrinking-patch limitation remains. The positive
continuum theorem is not bounded by an invented count of independent
no-go walls.

| Check | Scoped result |
|---|---|
| N1, actual alternatives | Origin shifting (5) is ATTEMPTED: it changes the rate but leaves (46). A periodic gauge identification is ATTEMPTED and refuted by the trace/holonomy in §2. Replacing current by branch momentum is examined in the accepted parent: it alters the first bracket and global periodic-domain behavior; no general boost is excluded. The parent's explicit density improvement changes current conservation and is only a prior result for that family, not an independent theorem here. The scaling (2) is ATTEMPTED and succeeds in (31)-(42). These are recorded alternatives, not five closed attack families or an exhaustive search. No N1 packet PASS is claimed. |
| N2, dependent restrictions | The local stress and (46) are the same model obstruction. Origin/gauge and varying-space operator-norm observations concern different mathematical assertions; no implication of physical impossibility is drawn from their combination. Unproved local-net and interacting limits are unattempted obligations, not independent impossibility walls. |
| N3, assumptions | The dimension, density, state, family (2), flat measure, comparison maps, fixed compact parameters and packet derivative norms are explicit. “Canonical” refers only to the parent-identified GNS implementers; no extra dynamics or physical selector is inferred. |
| N4, matching residual | Parent C29-C31 is exactly (46) after `k=aq`, `P_a=aP_lat`, `b_a=ab_lat`. Parent C38 uses m/c, which equals am/v here. No parent no-go is transferred across that changed premise. |
| N5, resolution | The new analytic estimates resolve one-particle modes, fixed finite-particle blocks and strong full-Fock vectors. They neither check a local site observable limit nor a lattice-wide local-net limit. The finite-a obstruction is a multiplier identity on the full circle, inherited also from the parent's local density proof. |
| N6, conventions | A spatial origin shift is a legitimate geometric convention change and is explicitly realized. It improves one rate and does not retire the finite-a cos(aq) residual. No new axiom is claimed necessary for the open physical extensions. |
| N7, strongest counter-route | A critic can retain the actual origin and geometric shifts, change the family with a, and seek continuum covariance despite every fixed-a failure. That is precisely the successful route (2)-(42). A broader no-go for emergence would be false. The remaining possible local-net bridge would need explicit local-observable maps and uniform localization estimates, which this proof neither supplies nor rules out. |
| N8, prior comparison | The complete accepted parent explicitly left a small-m/c scaling route live. The root's bounded search and existing `LORENTZ_BOOST_COVARIANCE_2D_THEOREM_NOTE.md` concern the known dispersion and a free-scalar two-point limit, not the full-spin boost/domain limit. No novelty-to-literature or exhaustive repository/open-PR coverage is claimed. |

The author analytic claims (2)-(47) have no intentionally open internal
lemma; they are proposed proofs for independent examination. Their
load-bearing review targets are the actual scaling and origin, periodic
versus antiperiodic domains, differentiability of the moving graph-domain
vector in (27), the compact-time density extension, Fock maximal domains,
and finite-word convergence. The parent's conditional status is inherited;
no retained-status or audit conclusion is written here. Numerical controls
below are discriminating author checks, not proofs of these analytic steps.

The analytic text through this section is frozen before scientific control
execution. Its exact identity and the later control protocol are preserved
under `gapped_continuum_limit/frozen/`. Subsequent mathematical corrections,
if any, must retain this initial source and state their reason.

## 11. Author controls and evidence

The initial analytic note (819 lines) was frozen at 2026-10-12 08:53:17 UTC,
SHA-256 `bef63d168ee16f70d36788154402342873a5295668674cba3c023d15a45c104e`.
The frozen control protocol is
`753783c9015a9686dcafe278777f0c565d36f071a7cf1fae2fc40e72214e529e`.
Root read that complete analytic source before the controls and reported
no requested mathematical change. Root is a coauthor; this is not a
separate-context review. The analytic proof is unchanged apart from
repairing six TeX line-break escapes and displaying table norms with
Unicode bars; the exact delta is preserved.

All numerical code is new author code. It imports no campaign or parent
helper. The reference matrix obtains its energy band by diagonalizing
the parent's actual 2×2 kernel, Fourier transforms it to a hopping
kernel, and uses the literal position weight
`a(n+l-1)/2`. Hermitian spectral evolution is compared to a separately
integrated characteristic ODE and the **complete complex** wavefunction.
The comparison tests the origin, normalization, phase, half-density and
orientation. Both constructions share the specified model conventions;
they are different-method author controls, not independent review.

| Calculation | Observed result and limitation |
|---|---|
| Circle, `m=.91,v=1.17,a=.37`; both signs of `.43`, `.91`, and `L_a+.23` | At mode cutoff 128, the largest full-wavefunction error is `2.57e-13`; the actual matrix holonomy differs from `-1` by `7.03e-14`. These are floating diagnostics, not certified uniform error bounds. |
| Literal weighted origin action | Baseline differential/matrix discrepancy `3.65e-15`; reversing the origin gives `1.88652`, deleting it gives `.943261`. Unitarity and one-cycle holonomy alone do not determine the origin sign. |
| Compact moving packet, `m=1.2,v=.83,R=.7,s=±.35` | Every tested group error is below the separately quadratured actual Duhamel residual integral, which is below (29) or (30). Both signs were evaluated. |
| Actual translations and a mixed four-factor word | The rounded integer phase obeys (34), has periodic trace, and the mixed `W(.23)A(.31)T(.57)W(-.19)` obeys its §6 majorant at `.2,.1,.05`. Rounding makes finite-spacing word errors nonmonotone; no monotonic-rate assumption is used. |
| Two-particle Slater packet | Direct two-variable antisymmetric quadrature matches the Gram-determinant calculation within `4.6e-16` in squared error. At a=.2 and .1, tensor errors `.0692209` and `.0346201` lie below sums of one-particle errors. Final norm-square errors are below `1.8e-12`. This checks one finite-sector example, not the full Fock theorem. |

For the compact packet, the positive-time errors and proved majorants are:

| a | Centered error | (29) majorant | Original-origin error | (30) majorant |
|---:|---:|---:|---:|---:|
| .4 | `5.304991e-4` | `.02498209` | `.08629730` | `.14285739` |
| .2 | `1.329263e-4` | `.00624552` | `.04316610` | `.06518317` |
| .1 | `3.325043e-5` | `.00156138` | `.02158580` | `.03103020` |
| .05 | `8.313787e-6` | `.00039035` | `.01079339` | `.01512476` |

The rates come from the analytic inequalities, not a fit to this table.
All full values and the intermediate residual integrals are retained in
`results/baseline_packet_v3.json`. The spectral data are in
`results/baseline_circle_v2.json`.

There were real diagnostic failures, preserved before refinement. The
initial cutoff sequence 24,48,80 did not meet the preregistered `2e-9`
target after one winding: the errors were approximately `.11664`,
`.00040845`, and `2.357856e-8`. Increasing the cutoff to 128 met the
same target without changing the model, method or tolerance. The first
450-point two-particle quadrature had norm-square discrepancy `3.74e-7`.
An added explicit `2e-10` norm gate still failed at 1000 points
(`5.819e-10`), then passed at 2000 points. The original sources, complete
failed results and every source delta are under `frozen/control_revision_1/`,
`frozen/control_revision_2/` and `frozen/control_revision_log.json`.
No analytic theorem was repaired by changing an acceptance value.

Nine source-level candidate variants were run with the reference sources
and tolerances unchanged. Every variant has a relevant rejecting witness,
and the weaker survivors matter:

| Defect | Rejecting witness | Surviving or untested weaker assertion |
|---|---|---|
| Reverse origin sign | Fixed-a full wavefunction and literal weighted action; some actual-residual integral bounds also fail | Every tested broad O(a) analytic majorant survives; this modified origin has the same continuum limit |
| Delete origin | Fixed-a wavefunction and weighted action | The entire packet suite survives; the centered flow really does converge and fits the weaker O(a) bound |
| Reciprocal half-density | Full wavefunction, integrated norm, and small-a continuum bounds | It leaves unrelated origin-action and domain witnesses unchanged |
| Delete half-density | Same independent norm/wavefunction witnesses | Unrelated gauge/translation checks do not test this error |
| Scale speed by `1/v` | Full wavefunction and every tested continuum analytic majorant | Unitarity survives; it is a differently parametrized group |
| Treat the gauged derivative as periodic | Actual matrix versus predicted cycle differs by 2; reconstructed eigenfunctions fail the periodic q-trace | The packet suite is unchanged because it never calls the global gauge-domain formula; it cannot certify that domain |
| Reverse integer-shift orientation | Phase bound and mixed word | Circle boost tests do not exercise translation orientation |
| Use noninteger geometric interpolation | Endpoint trace fails (one witness `1.60799`) | Its multiplier is exactly the limiting C(y), so the continuum phase bound survives; it is not an actual lattice shift |
| Use floor instead of nearest integer | The claimed half-spacing bound fails for selected signs/parameters | These remain actual integer shifts and still converge with the weaker full-spacing O(a) bound |

These are specific source mutants, not an exhaustive enumeration of all
possible implementation errors. Complete mutations, all failed predicates
and surviving analytic-bound labels are in `frozen/mutation_plans.json`
and `results/mutant_findings.json`. A single PASS count is never used as
support for an infinite-dimensional theorem.

Every scientific subprocess had an actual 60-second timeout. None timed
out. The 23 scientific runs and three provenance-corruption controls
retain argv, cwd, start/end time, elapsed time, code/input hashes, exit
status, complete stdout/stderr and machine-readable results. Externally
pinned candidate-source, reference-helper and manifest corruptions each
failed before scientific execution. A refresh confirmed all sixteen
original source/instruction inputs unchanged and all 26 process streams
and result hashes intact. These checks authenticate bytes, not proofs.
Early read-only tool calls and preparation commands were not wrapped in
the local subprocess recorder; their absent process metadata is not
invented. Their inspected sources and deterministic preparer are saved.

The [reproduction instructions](../.claude/science/physics-loops/toe-supplied-chain-20261012/EVIDENCE_MAP.json),
[current checkpoint](../.claude/science/physics-loops/toe-supplied-chain-20261012/EVIDENCE_MAP.json), full source
manifest and final receipt identify the deliverable. Root reported a
09:02 UTC publication-worktree update to `358fdf795a5504d4d7fd13344bbbd5df5504ebea`
for earlier notes, with this task's sources and main/planning identities
unchanged; it supplies no new premise for this proof. No local Git or
publication action was performed by this author.

No Lean execution is claimed. A finite algebra certificate would not
settle the transport domains or moving-vector differentiation. The next
step is the fresh review of this exact proof and source-coupled evidence,
especially (8), (15), (27), (36), (38)-(44). The remaining physical
obligations stay those named in §9. No new retained status, audit verdict,
framework realization or local-net theorem is implied.



## Publication evidence and limits

**Author/checker pairing:** Same selected model family and reasoning effort, separate author/reviewer contexts with candidate formulas exposed; not blinded or diverse-family. Root supplied routes and is a coauthor. Mechanical packaging adds no independent scientific review.

Maximal sector-sum and direct-sum domains use TOTAL multipliers; cancellation prevents importing one-particle energy/momentum domain equality. The two full-Fock origin domains need not agree. Original winding cutoff24/48/80 and two-particle quadrature450/1000 failures remain, followed by fixed-gate128/2000 refinement. Reviewer h=.01/.005 failures remain before .0025. Origin-sign broad-majorant survivors and missing-origin/periodic-gauge packet survivors remain. No interval or Lean certificate is claimed.

Hashes quoted in the original argument identify frozen probe inputs, not the administratively renamed canonical notes; the publication map records that lineage. The complete original note, separate source review, root coverage, all author/reviewer sources, raw results, failed attempts and refinement history are reconstructable from the [evidence map](../.claude/science/physics-loops/toe-supplied-chain-20261012/EVIDENCE_MAP.json). Raw external papers remain outside the packet, with [version/source identities](../.claude/science/physics-loops/toe-supplied-chain-20261012/EXTERNAL_SOURCE_INVENTORY.json). Canonical execution and whole-source replay outcomes are not predeclared; the root execution receipt records their actual outcomes.

This three-note milestone selects one integrable one-dimensional model and scaling family. It imports no massive-carrier theorem or pending local-algebra route. Exact finite-spacing Lie closure still fails. No interacting, local-net, 3D, physical-selector, interval or new Lean certificate is supplied. Global combined validation and strict audit lint remain separate independent landing gates; no audit verdict or retained promotion is applied.

Direct proof input: [the supplied concrete chain](CONCRETE_GAPPED_CHAIN_BOUNDED_THEOREM_NOTE_2026-10-12.md), at its full-spin construction and actual-generator scope.
