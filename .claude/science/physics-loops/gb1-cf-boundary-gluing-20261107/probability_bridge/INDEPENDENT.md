# Independent check: algebra, content measures, and effect probabilities

This is a restricted-input mathematical check, not an audit or an axiom amendment.
Source: `docs/MINIMAL_AXIOMS_2026-06-29.md`, `origin/main`
`bf92a1d763030836ed55631d5d7a7ef3b288f284`, SHA-256
`301bb33c1a743104208067c14684b34ba71d86674509111638ea898bc6e6c0dc`.
I read the whole governing file and current workflow/workhorse instructions.
I did not read the primary probability-bridge note or previous checker arguments.
Ordinary finite matrix algebra and Borel probability mathematics are used below;
a star operation, effects, operational contexts, clocks, and event identifications
are explicitly supplied comparison structures, not derived physical primitives.

## 1. What the bare algebra gives

On the complex algebra `M₂(C)`, the normalized trace is canonical:
`τ(A)=tr(A)/2=Tr(L_A)/4`, where `L_A` is left multiplication on the
four-dimensional complex vector space `M₂(C)`. It is complex linear,
`τ(I)=1`, tracial, and invariant under every similarity.
It is the unique normalized complex-linear similarity-invariant functional:
diagonal similarities force its values on `E₁₂,E₂₁` to vanish, and swapping
the two basis vectors forces equal values on `E₁₁,E₂₂`; normalization gives
one half each. Alternatively, traciality kills the commutators `E₁₂,E₂₁`
and `E₁₁-E₂₂`, giving the same uniqueness among normalized complex-linear traces.
These are specified uniqueness classes, not properties of every scalar function.
Trace, determinant, and arbitrary functions of them give many invariant functions.
If only real linearity is required, real-valued normalized traces include
`Re τ+c Im τ`, so the complex-linearity hypothesis cannot disappear silently.
`Re τ` is invariant also under complex conjugation, unlike complex-valued `τ`.

There is no positive cone specified by the bare algebra presentation.
After supplying the usual adjoint, `τ(A)≥0` for positive semidefinite `A`,
and `0≤τ(E)≤1` for effects `0≤E≤I`. On the full domain it is not a
probability assignment: `τ(-I)=-1`, `τ(2I)=2`, and `τ(iI)=i`.
Declaring all algebraic squares positive fails already because `(iI)²=-I`.
Even on effects, a normalized scalar functional is not a probability measure
on the set of matrix contents. An operational event-to-effect map would still
be needed. Neither complex linearity of readout nor that identification is an axiom.
Thus the canonical algebraic trace does not derive physical record odds.

## 2. All-similarity-invariant finite content measures

**Classification.** Every finite positive Borel measure `μ` on `M₂(C)`
invariant under all `A↦SAS⁻¹`, `S∈GL₂(C)`, is supported on `{zI:z∈C}`.
Conversely, every finite Borel measure on that center is invariant.
For probability measures this is exactly `μ=(z↦zI)_*ν`, with arbitrary
Borel probability `ν` on `C`; no preferred `ν` follows.

**Proof.** Write `A=[[a,b],[c,d]]`. Conjugating by `diag(2,1)` scales
`b` by 2 and `c` by 1/2. A finite positive measure on `C` invariant
under multiplication by 2 must be concentrated at zero: the disjoint shells
`{2ⁿ≤|z|<2ⁿ⁺¹}`, `n∈Z`, all have equal mass, hence mass zero by finiteness,
and their union is `C\{0}`. Apply this to both coordinate marginals.
Thus `b=c=0` almost surely. Conjugating a diagonal matrix by
`[[1,1],[0,1]]` gives upper-right entry `d-a`. Invariance and the established
zero upper-right marginal imply `a=d` almost surely. Central matrices are
fixed by every similarity, proving the converse. The proof also covers zero
and nonunit-mass finite positive measures; no claim is made for infinite measures.

This concerns a measure whose random variable is the *matrix content*.
It does not forbid the invariant positive linear functional `τ` after a star
operation is supplied. It is also stronger than unitary invariance: for example,
the unitary orbit law of `diag(1,0)` obtained by pushing forward normalized
Haar measure on `U(2)` is a noncentral unitarily invariant probability measure.

The explicitly named covariance in Admissibility is spatial translation and
proper cubic rotation covariance. It does not state that one fixed content
measure is invariant under every internal similarity. If “algebraic structure
alone” is strengthened to simultaneous similarity covariance of a local kernel,
the condition is `F(S·n)=S_*F(n)`. For fixed `n`, this imposes invariance
only under its stabilizer; full invariance follows when `n` itself is fixed
by all similarities, as for neighborhoods containing only central records.
This distinction is necessary even under the stronger covariance interpretation.

## 3. A legal-domain family and its infinite-volume realization

Supply the condition `D={⊥,0,I}^{Z³}` on legal record configurations;
`⊥` denotes absence and is not the matrix zero. Keep the full possibility
domain `M₂(C)`. For the six immediate neighbors, let `k` count present
records and `l` count records equal to `I`. For any fixed `0<a<1`, set
`F_a(n)=p_a(n)δ_I+(1-p_a(n))δ_0`, `p_a(n)=(a+l)/(1+k)`.
Since `0≤l≤k≤6`, `0<p_a(n)<1`; its support is always exactly `{0,I}`.
It varies with conditions: the empty, one-zero, and one-identity neighborhoods
have probabilities `a`, `a/2`, and `(a+1)/2`. Counts make the rule translation
and proper-cubic-rotation covariant. Zero and identity are algebraically defined;
no basis or site is selected. The rule is also covariant under all simultaneous
similarities on this legal domain, since every present content is central.

Here is an actual infinite-volume process, using supplied auxiliary time.
For any deterministic initial configuration in `D`, give initially absent sites
independent `T_v~Exp(1)` and independent `U_v~Uniform[0,1]`; initially present
records remain fixed. At `T_v`, site `v` locks `I` iff
`U_v≤p_a(n_v(T_v-))`, and otherwise locks `0`; it never changes again.
This instruction needs an existence proof because, from the all-absent state,
infinitely many births precede any positive time and there is no first global birth.

The needed predecessor graph has an edge from an initially absent `v` to an
initially absent neighbor `w` only if `T_w<T_v`. A descending path has distinct
vertices. For any fixed length-`n` path of distinct initially absent vertices,
its `n+1` iid continuous clocks have the specified decreasing order with
probability `1/(n+1)!`. There are at most `6ⁿ` such paths from `v`, so
`P(a descending path of length n from v)≤6ⁿ/(n+1)!→0`.
Therefore each vertex almost surely has bounded descending-path depth.
Finite degree then makes its entire predecessor set finite. Countably many
vertices give this property simultaneously with probability one. Evaluate each
finite predecessor graph from earlier clocks upwards; overlapping graphs agree
because the same recursive rule and marks are used. This defines the process.
Initially present neighbors are fixed leaves. All clock ties have probability zero.

Before `T_v`, no record value depends on `U_v`: predecessor paths into the past
cannot use the later clock at `v`. Consequently the conditional draw at formation,
given the prior configuration and the formation time, is exactly `F_a`.
All `T_v` are finite almost surely, simultaneously for all initially absent sites.
Each coordinate path changes at most once, giving permanent records and no
rerecording; the process is also cadlag in the countable product topology.
The content readout `r(0)=0`, `r(I)=1`, undefined at `⊥`, meets Record.
From the all-absent state records form almost surely. The process is spatially
equivariant, and its law from the all-absent state is spatially invariant.

**Axiom-level disposition.** This is a supplied realization, not derived dynamics.
Under the literal supplied-legal-domain reading of Qualification it meets the
four axioms: every state in `D` receives exactly one law answer, with nonconstant
local odds; no full-support condition or arbitrary initial matrix content is
stated. Different `a` give distinct odds at the same legal neighborhood with the
same readout. This is operationally witnessed by conditioning on a site having
the earliest clock among itself and its six initially absent neighbors, an event
of probability `1/7`; its identity-record probability is then `a`.
Thus the literal axioms do not select unique local odds. A stronger demand that
every matrix be realizable as initial record content would exclude this domain,
but is an additional premise. The construction does not settle that stronger task.

## 4. Binary nonlinear qubit assignment: its exact reach

Now supply the ordinary adjoint and effects. Fix a rank-one orthogonal projector
`P` and set `f_P(E)=h(tr(PE))`, `h(t)=t²/[t²+(1-t)²]`.
The trace argument lies in `[0,1]`. The function is continuous and increasing
(`h′(t)=2t(1-t)/[t²+(1-t)²]²`), has values in `[0,1]`, satisfies `h(0)=0`, `h(1)=1`, and
`h(1-t)=1-h(t)`. Hence `f_P(0)=0`, `f_P(I)=1`, and
`f_P(E)+f_P(I-E)=1` for every binary effect measurement.
It is order preserving, covariant under simultaneous unitary changes of `P,E`,
and invariant under unitaries fixing `P`. It is not invariant under arbitrary
unitary changes of `E` while holding `P` fixed. General similarities need not
preserve this supplied star/effect domain, so no such covariance is asserted.
For rank-one `Q`, `f_P(Q)=f_Q(P)`, while `f_P(P)=1` and `f_P(I-P)=0`.
These are sharp calibration identities. Actual repeatability after an outcome
requires an update rule (e.g. preparing `Q`); no instrument or process is defined
by this binary formula, especially for unsharp effects.

**Exact failure of effect coarse-graining.** Take
`P=diag(1,0)`, `Q=(1/2)[[1,1],[1,1]]`, `E=Q/2`, `F=(I-Q)/2`.
These are distinct commuting effects, `EF=0`, and `E+F=I/2`.
Their `P`-expectations are `1/4,1/4,1/2`, respectively, so
`f_P(E)+f_P(F)=1/10+1/10=1/5 ≠ 1/2=f_P(E+F)`.
The three-effect menu `{E,F,I/2}` sums to `I`, but the three assigned weights
sum to `7/10`. Binary normalization and sharp calibration therefore do not
derive finite-effect additivity or a normalized probability for every POVM.

## 5. The operational bridge and its quantifier

Fix preparation records `R`, separated from device/apparatus records `C`.
Supply (i) realization of every effect as a record event, (ii) probabilities
depending only on `R,E` across device contexts, (iii) **for every** pair `E,F`
with `E+F≤I`, a common context containing exclusive events with those effects,
whose union has effect `E+F`, and (iv) certainty of `I`.
Ordinary event-probability additivity then yields a well-defined
`f:EFFECTS→[0,1]`, `f(I)=1`, and `f(E+F)=f(E)+f(F)` for every such pair.

**Finite-dimensional proof of density representation.** First `f(0)=0`.
If `E≤F`, additivity for `E,F-E` gives monotonicity. Subdividing an effect
into `n` equal pieces gives rational homogeneity `f(qE)=qf(E)` for
`0≤q≤1`. Sandwiching any real `t∈[0,1]` between rational numbers and using
monotonicity gives `f(tE)=tf(E)`; continuity is a conclusion, not an assumption.
For positive `X`, choose an integer `n≥max(1,||X||)` and define
`L_+(X)=n f(X/n)`. Homogeneity makes this independent of `n`: compare any two
choices with a larger common integer. Choosing a common scale for `X,Y,X+Y`
proves additivity on the positive cone. The same scaling identity gives real
positive homogeneity. Define `L(A-B)=L_+(A)-L_+(B)` for positive `A,B`;
this is well defined since `A-B=C-D` implies `A+D=C+B`. It is a real-linear
functional on Hermitian matrices and extends complex linearly to `M₂(C)`.
The nondegenerate trace pairing on Hermitian matrices gives a unique Hermitian
`ρ` with `L(H)=tr(ρH)`. Positivity on rank-one matrices says
`v†ρv=L(vv†)≥0`; normalization says `trρ=1`. Thus `f(E)=tr(ρE)`.
Uniqueness follows because effects span the Hermitian matrices and their complex
span is all `M₂(C)`. This proves the conditional theorem including dimension two.

The common-context quantifier is essential. The weaker rule “for groupings that
already exist, the union effect is the sum” does not imply that every summable
pair is co-realizable. Binary-only contexts `{E,I-E}`, for every effect `E`,
with the nonlinear assignment of section 4 satisfy all binary unions and
context-independent values, yet violate the desired density representation.

The theorem is the finite-dimensional effect version associated with Paul Busch,
[quant-ph/9909073](https://arxiv.org/abs/quant-ph/9909073); a related POVM route is
Caves et al., [quant-ph/0306179](https://arxiv.org/abs/quant-ph/0306179).
The proof above checks the particular implication needed here directly.
The current axioms do not supply an adjoint/effect interpretation, all-effect
realizability, preparation/device separation, common-context completeness,
or context-independent event identification and probabilities. Ordinary additivity
for disjoint Borel events of one already-given probability law is available;
identifying their union with operator addition across contexts is the missing step.
These are substantial extra premises, not consequences of Record permanence.
The bridge fixes the *form* and uniquely represents each given `f`; it does not
select `ρ` or a map from preparation records to `ρ`. If the extra preparation
condition makes rank-one `P` certain, positivity forces `ρ=P`; that condition
also needs justification. Conditioning on the entire apparatus-containing record
configuration does not establish invariance while the apparatus is changed.
The theorem is not circular when its operational hypotheses are justified
independently, but calling those hypotheses axiom-derived would import precisely
the missing event and context structure.
