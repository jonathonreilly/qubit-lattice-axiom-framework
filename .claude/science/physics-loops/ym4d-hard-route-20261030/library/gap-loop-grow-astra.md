# Repo search

The assigned checkout is `0218f610d1c73eec9976e149f1d04d1b4e38b54d`.
`prior/gap-loop-grow-astra.md` does not exist there. The lead's
`prior/repo-search-2026-11-08.md` concerns older RG work. Its closest
hit, PR 10114's
`.claude/science/toe-ruleset-20261021/agents/ym4d-proof/MASS_GAP_LOCAL_BLOCK_ASTRA.md`,
was read at `f76f6c649cff7dffbab664d8976e680e8f287fe9`, lines 1–165.
That earlier Codex argument supplies local ground-state comparisons and
a positive one-step correlation. It does not supply an ES upper bound.
I reuse that distinction; I do not repeat its construction.

The more relevant lead search is `prior/gap-lit-xvol.md`, by Codex
gpt-6-luna high. It records searches of main and PRs 10114, 10133,
10134 and 10141. Its main hit was opened at
`a527a6fdaeb22ef8a0d1224cc2ba7bc42c48d3bc`:
`.claude/science/physics-loops/plaquette-bootstrap-closure-20260503/LITERATURE_BRIDGES.md`.
It records numerical single-volume bootstrap comparisons, not a hand
two-volume certificate. The search found no matching supplier. This is
a search result, not an absence theorem. No numerical bracket is used.

The immediate prior results are `gap-loop-pos-astra.md`, Sections 2–3,
with `gap-loop-pos-check-opus.md`; and Claude Opus 5.5's
`gap-loop-eq-opus.md`, with Codex's `gap-loop-eq-check.md`.
Theorem O and its Wilson witnesses are reused. The checker keeps
P-small's variance slack explicit; the numerical threshold attached
to that slack has an ARGUED uniformity input. Neither the earlier
radius-about-a/2 claim nor a general positivity obstruction is reused.
`gap-skeleton-final.md` 13.20 supplies the current consumer and the
boundaries with the separate LOC, fusion and gauge-invariant block lanes.

Searches of `open-registry.md`, `open-core.md`, `l17c.md`, `port-map.md`
and the relevant FINISH rows found no competing proof owner for row 767.
Row 768 owns the winding-loop literature search, not this proof attempt.
I do not take over that search or the LOC/fusion proofs.

The outline and CA-I were fetched once at `31a47c543775` to the requested
scratch paths. The full-read index was searched before source excerpts,
including its README, chunk files, obligations, and `ca-4.12-4.19/`.
The nearby results concern transfer positivity, chessboard bounds and
conditional source normalizers. No matching ES supplier was located in
those index searches. Exact read ranges and scope are recorded below.
Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors
of their text, for every use of that outline and account. Credit
Anderson–Kruczenski and Kazakov–Zheng for the bootstrap method, and
Makeenko–Migdal, Chatterjee and Jafarov for the loop-equation methods,
through the supplied literature records. No external numerical result
is a proof input.

Author: **Codex gpt-6-astra max**, FINISH row 767, 2026-11-12.
Research text, not an audit; grants no status. **PROVED** below means
a displayed hand argument, not an independent check. **ARGUED** names
an incomplete argument; **GUIDE** proves nothing; **OPEN** remains open.
Only this output file is edited. No numerical run is used.

**Outcome: partial, not the requested full disjunction.** Theorem A
extends the obstruction to sublogarithmic growing radii. Theorem C
extends it to product-compatible joint constraints. Section 3 gives
restricted winding obstructions and a finite-volume determinacy theorem.
No certificate reaches ES, and the three unrestricted classes remain OPEN.

## 1. Consumer and scope

**PROVED in the cited inputs.** With weight
\(\exp(s\sum_p x_p)\), \(x_p=\operatorname{tr}(U_p)/2\), let A and B
be the infinite-time cylinders with spatial sides a and 2a. Let E be
the centre-even thermal state on \(a^4\). Then

\[
 \delta=48a^4\int_0^\beta(p_A-p_B)\,ds,\qquad
 \log(1+\epsilon)=6a^4\int_0^\beta(p_E^{\rm ins}-p_A)\,ds.       \tag{1}
\]

The E insertion includes the twist sign. The integrals, not necessarily
the integrands, are nonnegative. The target is
\(\delta\le10^{-7}\), \(\epsilon\le10^{-7}\) at an admissible physical
size, uniformly in the cutoff. A fixed finite lattice calculation alone
does not establish this last uniformity.

**PROVED scope correction, by reading Theorem O's quantifiers.** It
excludes fixed-radius, separate-state diameter certificates for all
sufficiently large a. It does not exclude such a certificate at every
individual a. At growing radius r(a), its bound is
\(48a^4J_{r(a)}\), respectively \(6a^4J_{r(a)}\), with no uniform lower
estimate on \(J_r\). These statements cannot be strengthened by changing
the order of the quantifiers.

## 2. Class A: an explicit obstruction for sublogarithmic radii

The new input beyond Theorem O is the uniform analytic bound in
Claude Fable 5.2's `gap-seed-sc.md`, Theorem 1 and Sections 2–3.
Claude Opus 5.5 checks that bound in `gap-seed-sc-check.md` Section 2.
That check records its same-provider limitation. The leading coefficient
is Theorem 2 there, already used by Theorem O. Neither the expansion
nor the wrapping-tube count is repeated here.

**PROVED GIVEN those two prior inputs: Theorem A.** Use exactly the
feasible set \(K_r(s)\) of Theorem O. Set

\[
 n=2r+4,\qquad d=4n,\qquad t_*=2^{-20},\qquad
 j_r=\frac{2^{-280n}}{n}.                                      \tag{2}
\]

For any integer \(r\ge2\), \(\beta\ge t_*\), and any measurable,
integrable pointwise certificate
\(p(\omega)-p(\nu)\le b(s)\) for all \(\omega,\nu\in K_r(s)\),

\[
                         \int_0^\beta b(s)\,ds\ge j_r>0.        \tag{3}
\]

The radius may be chosen as a function of a. Consequently that
separate-state method cannot establish the delta bound when

\[
 \frac{48a^4}{n}\,2^{-280n}>10^{-7},                            \tag{4}
\]

or the epsilon bound when

\[
 \frac{6a^4}{n}\,2^{-280n}>\log(1+10^{-7}).                     \tag{5}
\]

As before, \(a\ge2r+3\) makes the target states admissible. In
particular, every choice \(r(a)=o(\log a)\) fails both tests for all
sufficiently large a. More explicitly, the same holds if eventually
\(r(a)\le c\log_2 a\), for any fixed \(c<1/140\).

**Proof.** Retain Theorem O's two actual Wilson witnesses on \(n^4\)
and \((2n)^4\). Their membership in \(K_r\), including reflected
positivity, is already proved there. Write

\[
 \Phi_n(s)=16\log Z_n(s)-\log Z_{2n}(s),\qquad
 f_n(s)=p(\omega_n(s))-p(\omega_{2n}(s)).
\]

The imported facts, with the volume constants cancelling in either
action normalization, are

\[
 \Phi_n'=96n^4 f_n,\quad \Phi_n(0)=0,\quad
 [s^d]\Phi_n=192n^3 4^{-d},\quad [s^k]\Phi_n=0\ (k<d),          \tag{6}
\]

and analyticity for \(|s|<1/12800\), with
\(|\Phi_n(s)|\le(4/25)n^4(12800|s|)^d\). Put
\(R_*=2^{-14}<1/12800\). In particular
\(|\Phi_n|\le n^4\) on \(|s|=R_*\). Cauchy's coefficient formula gives

\[
             |[s^k]\Phi_n|\le n^4 R_*^{-k}.                   \tag{7}
\]

Here is the finite polynomial estimate used to recover a real lower
bound from the nonzero coefficient. If P has degree at most M on
\([0,1]\), Lagrange interpolation at \(j/M\), \(0\le j\le M\), gives

\[
              |[x^k]P|\le16^M\max_{[0,1]}|P|.                \tag{8}
\]

Indeed each interpolation numerator has sum of absolute coefficients
at most \(2^M\). Its denominator has absolute value
\(M^{-M}j!(M-j)!\). Summing these bounds gives
\(4^M M^M/M!\). The inequality
\(\log M!\ge\int_1^M\log x\,dx=M\log M-M+1\) bounds this by
\((4e)^M<16^M\). This proves (8) without evaluating the nodes.

Take \(M=12d\), and let P be the Taylor polynomial of
\(\Phi_n(t_*x)\) through degree M. Since \(t_*/R_*=1/64\), (7)
bounds the discarded tail uniformly on \([0,1]\) by

\[
 E_n\le\frac{n^4 64^{-(M+1)}}{1-1/64}
       <n^4 2^{-6M-5}.                                      \tag{9}
\]

Its degree-d coefficient is \(192n^3 2^{-22d}\). Apply (8):

\[
 192n^3 2^{-22d}
 \le16^M\left(\max_{0\le s\le t_*}|\Phi_n(s)|+E_n\right).
\]

Moreover
\(16^M E_n<n^4 2^{-24d-5}\le96n^3 2^{-22d}\).
The last inequality is \(n\le3072\,2^{2d}\), which follows from
\(n\le2^n\) and \(d=4n\). Therefore

\[
 \max_{0\le s\le t_*}|\Phi_n(s)|
       \ge96n^3 2^{-70d}=96n^3 2^{-280n}.                    \tag{10}
\]

By (6), its left side is at most
\(96n^4\int_0^{t_*}|f_n(s)|\,ds\). Both orders of the two
witnesses are admissible, so \(b(s)\ge|f_n(s)|\). This proves
(3), and (1) gives (4)–(5).

Finally
\(\log_2(a^4j_r)=4\log_2a-280(2r+4)-\log_2(2r+4)\).
It tends to infinity for sublogarithmic r. Under the displayed
logarithmic bound its leading term is at least
\((4-560c)\log_2a\), with a logarithmic correction. This also
tends to infinity when \(c<1/140\). QED.

**PROVED scope.** This is a restriction on support, not on word
length, matrix order or loop shape. The witnesses are unchanged from
Theorem O. The constants are deliberately loose. No physical
finite-size decay law or numerical estimate enters the proof. It gives
no obstruction for arbitrary \(r(a)\), in particular for box-scale
supports, and no impossibility result at every individual seed size.

**OPEN after this attack.** For radii outside (4)–(5), the witness
bound is too small to decide the target. Taking a larger radius does
not prove that the moment bounds become narrow enough. Neither a
successful ES certificate nor an exclusion of all of class A follows.

**PROVED U(1) compatibility.** The argument is a lower bound on
certificate width, not a seed theorem. Its numerical coefficient in
(6) is the SU(2) coefficient from the cited source. An Abelian version
would need its own coefficient and analytic bound. No seed for U(1)
is inferred, at any coupling. This meets the T1–T3 test without using
a numerical phase boundary.

## 3. Class B: winding equations, and where witnesses cease to work

### 3.1 Charged one-point equations do not enter the neutral equations

**PROVED.** Give each plaquette its fixed cocycle sign
\(\sigma_p\in\{1,-1\}\). For a closed path C using e once, the
checked Ward calculation gives, without a contractibility assumption,

\[
 3E_\sigma W(C)+s\sum_{p\ni e}\sigma_p E_\sigma[W(C)x_p]
       =s\sum_{p\ni e}\sigma_p E_\sigma W(C\ominus p).         \tag{11}
\]

The proof in `gap-loop-eq-check.md` Section 1 uses only the word at e.
It therefore applies to the periodic word, with each action derivative
multiplied by its sign. A deterministic seam dressing of C must also
be carried through its deformations. It does not change this argument.

Let \(q(C)\in(\mathbb Z_2)^4\) be the winding parity. Multiplying
the links across one coordinate cut by −I preserves Haar measure and
every plaquette weight, also in a fixed twist. It multiplies W(C)
by the corresponding character of q(C). Thus

\[
              E_\sigma W(C)=0\quad\text{if }q(C)\ne0.        \tag{12}
\]

Deformation by a plaquette preserves q. Multiplication by an action
plaquette does too. More generally the Wilson generator commutes with
each cut flip. All Ward equations preserve total parity, including
splitting terms. Hence all the expectations in (11) vanish for odd
parity. This holds at every finite coupling. The positive electric-twist
mixture preserves it, as does the cylinder limit for spatial winding
loops with fixed finite time support.

**PROVED restricted exclusion.** Adding only charged one-point Ward
rows to a neutral system supplies no equation with a neutral unknown:
set every charged unknown to zero. This extends every solution of the
neutral rows and satisfies all the new rows. These are explicit
witness extensions of the *restricted linear system*. They are not
claimed to satisfy omitted global moment constraints.

**OPEN for full winding positivity.** An odd-odd Gram entry is neutral,
so its information is not covered by that exclusion. For example,
\(W(C)^2=(1+W(C^2))/2\). Mixed winding pairs, neutral winding words
and their reflected products are precisely additional data. The
previous splitting identity is already in `gap-loop-eq-opus.md` 6.3;
it is reused, not a new flux estimate. No small upper bound for those
neutral data follows from (12).

### 3.2 A restricted normalization obstruction

**PROVED.** At a fixed s, normalized loop data together with only
homogeneous sectorwise Ward and Gram constraints leave a free
unnormalized constant in each twist.
Write \(I_\sigma(F)=Z_\sigma E_\sigma F\). The assignments

\[
             \widetilde I_\sigma(F)=c_\sigma I_\sigma(F),
             \qquad c_\sigma>0,                              \tag{13}
\]

have the same normalized moments and satisfy every homogeneous Ward
identity. Every valid within-sector positive Gram form is multiplied
by a positive constant. Taking all c equal to one, or doubling just
one c, gives explicit different relative normalizations. Thus a
certificate reading only those sectorwise equations and positivity
cannot infer the required sector weights. These are witnesses to
missing normalization data, not different Wilson partition integrals.

**PROVED limit of that obstruction.** The actual Wilson family has

\[
 Z_\sigma(0)=1,\qquad
 \partial_s\log Z_\sigma(s)=E_\sigma\sum_p\sigma_p x_p.       \tag{14}
\]

There is also a fixed-s Haar anchor:
\(I_\sigma(e^{-sH_\sigma})=1\), where
\(H_\sigma=\sum_p\sigma_p x_p\). It gives
\(Z_\sigma=1/E_\sigma e^{-sH_\sigma}\). Full loop moments determine
this expectation by the uniformly convergent exponential series.
Thus the actual Haar anchor already removes (13), at a single s.
Alternatively, if (13) obeys (14), then \(\partial_s\log c_\sigma=0\)
and \(c_\sigma(0)=1\), so every c is one. Constraints linking twists,
or the actual coupling evolution, therefore invalidate these witnesses.
In particular this is not an exclusion of the proposed full class B.

### 3.3 Full finite-volume Ward data admit no different measure witness

The following result explains a more substantial limit on a proposed
extension of Theorem O. It concerns a fixed finite graph and all
polynomial Ward insertions, not just (11).

**PROVED: Theorem B.** Let \(X=\mathrm{SU}(2)^E\) on a fixed finite
connected periodic lattice, with its specified plaquettes and twists.
Let \(H=\sum_p\sigma_p x_p\). Among gauge-invariant Borel probability
measures on X, the equations

\[
 \nu\!\left(D_{e,j}F+sF D_{e,j}H\right)=0
 \quad\text{for every real coordinate polynomial F, e and j}   \tag{15}
\]

determine exactly \(d\mu=Z^{-1}e^{sH}dU\). They can equivalently be
written as gauge-averaged scalar loop-polynomial Ward equations.
For any continuous gauge-invariant f and any \(\eta>0\), a finite
subset of these equations already ensures
\(|\nu f-\mu f|<\eta\) over such probability measures.

**Proof of existence and uniqueness.** The displayed Gibbs measure
satisfies (15), since \(\int D_{e,j}(F e^{sH})\,dU=0\) by Haar
invariance. Polynomial Taylor approximants to
\(e^{-sH}G\) converge together with their first derivatives on X,
for every coordinate polynomial G. Indeed H and all first derivatives
are bounded on X, and the differentiated exponential series converges
uniformly. Substitution in (15), followed by this uniform limit, gives
\(\nu(e^{-sH}D_{e,j}G)=0\). The normalized measure proportional to
\(e^{-sH}\nu\), denoted rho, therefore satisfies \(\rho(D_{e,j}G)=0\).

Left translation of one link maps coordinate polynomials to coordinate
polynomials. Differentiating its polynomial expectation under rho now
shows it is constant along every one-parameter subgroup. These
subgroups generate each SU(2) factor. The real Stone–Weierstrass theorem
applies: coordinate polynomials contain constants and separate points
of compact X. They are therefore uniformly dense in continuous
functions. Thus rho is left invariant.
Averaging a continuous function over an independent product Haar
translation gives \(\rho G=\int G\,dU\). This proves rho is product
Haar measure, and proves the asserted formula for nu.

**Why the scalar equations really are loop equations.** For a
gauge-invariant nu, replace each integrand in (15) by its vertex-gauge
average. The average is a polynomial, is gauge invariant, and has the
same expectation. Every such polynomial is a polynomial in traces of
closed paths, as the following direct SU(2) argument shows.

Choose a spanning tree and set its links to I by a vertex gauge. The
remaining links become based holonomies \(V_i=c_iI+i v_i\cdot\sigma\).
The residual gauge acts on all vectors \(v_i\in\mathbb R^3\) by a common
rotation. Its invariant polynomials are generated by the scalars c_i,
the dot products \(v_i\cdot v_j\), and scalar triple products.
One explicit way to verify this last assertion is to average a
monomial over rotation matrices \((u,v,u\times v)\). First average
v on the unit circle perpendicular to u. Each even moment is a sum
of pairings of \(I-uu^T\), and each odd moment vanishes. Then average
u on the unit sphere; its even moments are sums of delta pairings.
For a uniform unit vector in a d-dimensional Euclidean space, its
order-2m moment is the sum over pairings of the metric tensors,
divided by \(d(d+2)\cdots(d+2m-2)\). To see this, Gaussian integration
by parts pairs one coordinate with each remaining coordinate, giving
the pairing sum by induction. Polar coordinates separate the radius;
one radial integration by parts gives the stated radial moment product.
Apply this with d=2 and metric \(I-uu^T\), then with d=3 and metric I.
Cross products contribute only epsilon tensors.
Contracting the resulting deltas and epsilons gives dot and triple
products; pairs of epsilons reduce by the determinant identity.
This proves the generation assertion, for each finite monomial.

Finally
\[
 W(V_iV_j)=c_ic_j-v_i\cdot v_j,
\]
\[
 W(V_iV_jV_k)=c_ic_jc_k-c_k(v_i\cdot v_j)
             -c_i(v_j\cdot v_k)-c_j(v_i\cdot v_k)
             +(v_i\times v_j)\cdot v_k.
\]
These express all the generators through based loop traces. Tree
gauge changes are finite products and inverses of links, hence
polynomial in quaternion coordinates. This proves the equivalence
claimed in the theorem. The resulting paths can wind around the
specified torus and can traverse the whole graph.

**Proof of finite selection.** Gauge-invariant probability measures
on compact X form a compact space in the weak topology. Each equation
in (15), after gauge averaging, defines a closed subset. Their common
intersection is the singleton mu by uniqueness. The closed set
\(B_\eta=\{\nu:|\nu f-\mu f|\ge\eta\}\) is compact and disjoint
from that intersection. The open sets where individual Ward equations
fail cover \(B_\eta\). A finite subcover exists; its equations give
the conclusion. Compactness here follows, for example, by taking a
diagonal limit of integrals on a countable dense set of continuous
functions; positivity and normalization extend the limit to a
positive functional on continuous functions, and the Riesz
representation theorem gives its probability measure. QED.

**PROVED scope.** The finite-selection assertion quantifies over
representable probability measures. It does not assert that a finite
positive-semidefinite relaxation excludes every nonrepresentable
moment assignment, nor produce an explicit sum-of-squares dual.
The finite list depends on the graph, s, f and eta. No bound on its
size, or uniformity in the cutoff, has been proved. The theorem also
does not select an infinite-time cylinder using a fixed time window.
It uses all first-order polynomial insertions in (15); completeness
of a particular list of single-loop Laplacian tests is not asserted.

Nevertheless it rules out the specific attempt to extend Theorem O
by retaining two different actual measures satisfying the *full*
volume-labelled Ward data: there is only one on each finite graph.
An arbitrary-volume witness ceases to satisfy those premises.
The actual plaquette values still have to be bounded. Determinacy
is not an estimate of either integral in (1).

**PROVED U(1) test; OPEN target.** Equation (11) has Casimir 1 rather
than 3 for U(1), as the prior check proves. The parity, normalization
and compact-measure arguments themselves also apply to U(1), with
its own Ward coefficients. They yield neither an even thermal-sum
upper bound nor a gap. An attempted inference of ES from finite-volume
determinacy alone would therefore fail T1 in any U(1) regime where
the seed fails. No claim about a phase threshold is needed here.
Neutral winding estimates, the cylinder limit, and the two ES
tolerances at a physical size remain OPEN.

## 4. Class C: joint positivity versus a joint volume relation

### 4.1 Tensor moment matrices still admit the old witnesses

**PROVED: Theorem C.** Start with independent copies of \(K_r(s)\).
Add all ordinary positive moment and compact-group localizing
constraints on their product algebra. Add Ward equations in either
copy, multiplied by arbitrary polynomial tests in the other copy.
Also allow all reflected Gram matrices for the componentwise time
reflection, with complete support inside each copy's patch. None of
these additions removes Theorem O's width obstruction, or (3).

**Proof and witnesses.** Use
\(\omega_n\otimes\omega_{2n}\) and
\(\omega_{2n}\otimes\omega_n\), restricted to the two patches.
They are actual positive product measures. Pointwise localizers
remain nonnegative. Every polynomial on the product is a finite sum
of products of polynomials on the factors. Each multiplied Ward
identity therefore factors, with a zero factor. For reflection
positivity, the reflected Gram form on a finite set of product tests
is the tensor product of the two positive Gram forms. Restricting
that form to any linear combinations preserves positivity. Each
marginal also retains its required symmetries. The plaquette
differences of these two witnesses are \(f_n\) and \(-f_n\).
Thus every universal upper bound is at least \(|f_n|\), exactly as
in Theorem O. The same construction works for any finite number
of separately labelled copies. QED.

**PROVED scope.** A mixed moment matrix alone does not specify a
coupling induced by the physical larger box. The theorem excludes
only the stated product-compatible constraints. An actual gluing
identity, an identified boundary law, or a quantitative condition on
cross moments can invalidate these witnesses. This is not an
exclusion of all joint certificates.

### 4.2 Actual independent gluing and chessboard comparisons are prior work

**PROVED in the cited inputs; no new attack here.** Independent-box
gluing is already treated in `gap-crux-restate.md:145–156`. Its
Jensen bound pays a surface term from
\(192a^3-96a^2\) seam plaquettes. The transfer-entropy identity is
already `gap-skeleton-max.md:260–275`, Lemma 4. The sector-purity
form and its retained thermal terms are in
`gap-es1-opus-check.md:58–83`. I do not rederive those identities or
claim them as new exclusions. Their smallness input remains absent.

The Sussman–Alpoge outline, lines 26980–27011, similarly proves the
repeated-source comparison through
\(\operatorname{Tr}Y^q\le(\operatorname{Tr}Y)^q\) for positive Y.
That proof is used as supplied outline text, with the
authors credited above. Its source-normalizer conclusion also uses
stability, a partition floor and a vacuum-density comparison. Lines
26920–26932 explicitly retain the formation and common-coupling
hypotheses. No ES upper bound is supplied by that passage.

### 4.3 A precise joint certificate, and two failed constructions

**PROVED conditional certificate.** For almost every s, let
\(\pi_{AB,s}\) be a positive joint law with exactly the A and B
marginals in (1). Let X and Y be their normalized plaquettes. Use a
fixed time anchor and uniform spatial/orientation averaging on each
cylinder; use uniform finite anchor/orientation averaging on E.
These choices are included in the marginal law. There is no uniform
probability distribution over infinitely many cylinder time anchors.
Define \(D_{AB}(s)=E_{\pi_{AB,s}}(X-Y)^2\). Similarly define
\(D_{EA}(s)\), using the signed E insertion. Assume measurability
in s. Ordinary two-variable moment positivity gives

\[
 \delta\le48a^4\int_0^\beta\sqrt{D_{AB}(s)}\,ds,\qquad
 \log(1+\epsilon)\le6a^4\int_0^\beta\sqrt{D_{EA}(s)}\,ds.    \tag{16}
\]

Indeed \(|E(X-Y)|^2\le E(X-Y)^2\), and the exact marginals give
the integrands in (1). This is a joint certificate using a cross
moment, not two separate plaquette intervals. It reaches the requested
tolerances if the two right sides are at most \(10^{-7}\) and
\(\log(1+10^{-7})\), respectively. For example, sufficient uniform
bounds are

\[
 D_{AB}(s)\le\left(\frac{10^{-7}}{48\beta a^4}\right)^2,
 \qquad
 D_{EA}(s)\le\left(\frac{\log(1+10^{-7})}{6\beta a^4}\right)^2.
                                                               \tag{17}
\]

These are sufficient, not necessary, for ES. They have not been
established for a coupling of the target states.

**PROVED failure of the product construction.** For \(a\ge7\), the
four links of a plaquette touch at most 24 action plaquettes.
Conditioning on their exterior, the log density relative to their
product Haar law has oscillation at most \(48s\), including twists.
Consequently its normalized density lies between
\(e^{-48s}\) and \(e^{48s}\). For either the signed or unsigned
plaquette x,

\[
 |E_s x|\le d_s,\qquad E_s x^2\ge\tfrac14-d_s,
 \qquad d_s=e^{48s}-1.                                        \tag{18}
\]

The Haar values are 0 and 1/4: the product around the plaquette is
Haar SU(2), whose scalar quaternion coordinate has second moment
1/4. Conditioning and then averaging proves (18); the same bounds
pass to cylinder limits and positive twist mixtures. No uniform
analyticity assumption is needed.

For \(0\le s\le2^{-10}\),
\(d_s\le(3/64)/(1-3/64)=3/61<1/16\), using
\(e^u\le(1-u)^{-1}\) for \(0\le u<1\). Thus
\(\operatorname{Var}_s(x)\ge1/4-1/16-1/256>1/8\).
For independent marginals,

\[
 D_{AB}=\operatorname{Var}(X)+\operatorname{Var}(Y)
                       +(EX-EY)^2\ge\tfrac14,                \tag{19}
\]

and the same holds for EA. If \(\beta\ge2^{-10}\), both integrals
in (16), before their volume factors, are at least \(2^{-11}\).
Even the smaller prefactor gives \(6a^4/2048>10^{-7}\) for
\(a\ge1\). Hence this product-coupling certificate cannot meet
either tolerance. This refutes that certificate's sufficient test,
not the actual ES numbers. Coupling the two Haar plaquettes identically
at s=0 instead gives zero cost, so the loss is avoidable in principle.

**PROVED failure of deterministic tiling as the larger-box marginal.**
Periodically repeating one a-box in a 2a-box forces
\(x_p=x_{p+a e_i}\). The two plaquettes have disjoint edge supports
when \(a\ge3\). Their squared difference is not the zero polynomial:
set all links to I except one edge of p, which is set to −I. The two
traces are then −1 and 1. An open neighborhood has positive Haar
measure and positive squared difference. The actual finite Wilson
density is strictly positive there at every finite coupling. Thus

\[
                 E_{2a}(x_p-x_{p+a e_i})^2>0,                 \tag{20}
\]

whereas deterministic tiling gives zero. For a cylinder the same
conclusion follows by conditioning on the finite union of these
plaquette links: the conditional density has a strictly positive
lower bound relative to Haar, uniform in the exterior. Literal
reflection copying has the same defect for a reflected plaquette
pair. Reflection-positivity inequalities do not assert such a
deterministic-copy law; (20) does not refute those inequalities.

**OPEN after these attacks.** Construct a genuine coupling, or a
different signed joint certificate, with the correct global marginals
and an error small enough in (1). Product coupling gives (19), while
literal copying fails (20). The existing chessboard inequalities
give no such cross-moment estimate. I have no witness satisfying all
possible actual gluing relations and violating ES; therefore class C
as a whole remains open.

**PROVED U(1) test.** The conditional implication (16) uses no group
identity and applies to U(1) as well. T1 says its *quantitative joint
cost hypothesis* must fail wherever the corresponding U(1) seed
fails; mere existence of a coupling is not that hypothesis. In (18)
the Abelian Haar second moment is 1/2, so the product-coupling failure
persists. Strict positivity also rules out deterministic copying for
U(1). None of these statements incorrectly produces an Abelian seed.

## 5. Source ranges and verification

The source comparison is bounded. The index neighbours read were
chunk 01:60–74, 02:83–106, 03:19–36, 12:27–36, 24:119–135,
29:130–135, and obligations:17–28. The source excerpts read were:

| Outline lines | Content and relation to this note |
|---|---|
| 588–599 | Polynomial clustering does not give a gap; an extra spectral estimate is required. |
| 2195–2257; 2313–2336 | Positive one-link coefficients and the finite transfer trace; existing ingredients, not new results here. |
| 2773–2795 | Quaternion Gram expansion; the existing reflected-positivity framework. |
| 13023–13065 | A Hessian annihilates gauge gradients under the stated hypotheses; different from probability-measure determinacy. |
| 26920–26932; 26980–27011 | Conditional common vacuum densities and the repeated-source chessboard comparison; used with the limits stated in Section 4.2. |
| 32326–32380 | Additional rotation Ward inputs, explicitly required; different from the one-link Ward equations. |

No theorem of CA-I is imported after the index comparison. It was
downloaded once and not read whole. No Balaban paper or OCR formula
is used. No computer-assisted proof, enumeration, solver, or numerical
guide was run. The interpolation in Theorem A is an analytic argument;
its nodes were not evaluated by a program.

**PROVED means author proof only.** The author checked the coefficient
and volume factors, the two witness orders, the gauge-average step,
the compactness quantifiers, and the marginal and variance identities
by hand. This is self-checking, not an independent check. A check of
Theorems A–C and (16)–(20) is still needed before another lane treats
these arguments as checked. No claim or status file was changed.

## 6. Final checkpoint

Source revision: the assigned commit above; main rules at a527a6fdaeb2.
The full prior target record is absent. Theorem A excludes
sublogarithmic radii for the separate-state class. Theorem B fixes
the finite-volume measure under the full polynomial Ward system.
Theorem C preserves the old witnesses under product-compatible joint
constraints. The positive joint-distance certificate (16) is proved
conditionally; product coupling and deterministic tiling fail as
specified. Larger growing supports, full winding constraints, actual
joint gluing, both ES numbers, and cutoff uniformity remain OPEN.

The precise remaining obligation is still (1) with its two stated
tolerances, uniformly along the physical-cutoff family. For separate
pointwise certificates, one must leave the range excluded by (4)–(5).
For winding certificates, one must quantitatively bound the neutral
moments and keep the Haar normalization and global period data.
For the joint route, a sufficient next statement is a genuine coupling
meeting the two integral tests in (16); no such coupling is supplied.
These are alternatives inside row 767, not new registry ownership.

Failed routes to retain: charged one-point rows alone; homogeneous
sector normalizations without their Haar anchor; product-compatible
joint positivity; independent-marginal use of (16); deterministic
tiling. Existing independent gluing and entropy arguments remain
credited prior work. None excludes genuine volume gluing or all
box-scale loop certificates. No new physical axiom is introduced.

Recovery: the shared checkout changed branches during this run. The
author therefore saves a local commit on
`research/gap-loop-grow-astra-20261112` in
`/tmp/gap-loop-grow-astra-4t7rwedq/worktree`, based on the assigned
commit. The identical output is left at the requested lane path in
the supplied checkout. No push, public post or independent review is
performed by this run.

RESULT: PROVED by hand, not independently checked: Theorem O extends to sublogarithmic growing radii with explicit width 2^(-280(2r+4))/(2r+4), and to the stated product-compatible joint constraints; full finite-volume polynomial Ward data determine the Wilson measure. Charged one-point rows, unanchored sector weights, independent-marginal coupling bounds and deterministic tiling fail in the precise senses above. No ES certificate reaches 10^(-7), and no exclusion of all of A, B or C is proved; the physical seed and mass gap remain OPEN, with no status granted.
