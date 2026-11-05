# Positivity dichotomy of the large-field operations

Provenance: Codex, 2026-11-05, checkout `c04b80758f0ed2cac26749baca173a0dd8a50c4a`. Research text, not an audit; grants no status. Hand-proof lane for Sussman–Alpoge Proposition `4.32:prop-positivity-dichotomy`. Not yet checked by another model.

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the outline and complete account at `31a47c543775`; Tadeusz Balaban for the large-field construction they use.

## 1. Source contract and comparison

The target is CA-I 156837–156950, including all five parts of (d).
Its status sentence, “Proof outstanding.”, is at 156953. Its Route is
at 156955–156998.
Here CA-I/II/III mean `theorem_0_complete_account_raw_{I,II,III}.tex`
at the pinned Sussman–Alpoge revision. SA means `YM4_sketch_500.tex`
at that revision. No numerical calculation is a proof input.

The Route orders the work as follows: reference denominators; definedness
and analyticity; reality; independence of the support; the integral
representation; the null/non-null alternative; locality of the returned
operation. In particular, positivity is not a consequence of the already
positive bare Wilson measure without an identification of the formulas.

The statement uses Balaban's exact operations, not an arbitrary kernel
representation. It asks for:

| Clause | Required conclusion |
|---|---|
| (a) | Every weight factor is strictly positive at every admitted real pair, including independent real currents. |
| (b) | Positive integral operators and positive labelled measures. |
| (c) | Finite positive reference normalizations at every admitted exterior; Fubini and reversed gauge-fixing equivalence. |
| (d1) | One Borel integration space, measure and characteristic set per history, independent of the exterior pair and of the ambient torus. |
| (d2) | The exact formula with prefactor \((2^d d!)^{-1}\), finite exponent, and no discarded constraints. |
| (d3) | Positive unweighted support mass iff positive operator mass at some, hence every, admitted real pair. |
| (d4) | A null label vanishes on the entire complex domain, including its later activity and product contributions. |
| (d5) | The returned operation's measures, constraints and tests read only its integrated variables and its component's block field. |

The requested comparison gives no existing proof of these clauses:

* **AG1.** Lines 74–82 assume positive probability kernels and positive
  history weights. Lemma 3, lines 521–564, proves a logarithmic expansion
  assuming its actual healed-family representation and majorants. Lemma 4,
  lines 587–634, assumes a positive centre measure and a strictly positive
  centre mass before proving a zero-free disc. None constructs the
  CA measures or proves (a), (c), (d1), (d2), or (d5). Its disc is a version
  of a subsequent analytic estimate, not the dichotomy.
* **TP1.** PRES, lines 103–114, assumes the positive stopped law. The
  Result, lines 638–650, retains PRES as an input. This proves no clause
  of 4.32.
* **IN1.** H-LF, line 146, assumes Borel kernels and nonnegative physical
  real weights. H-E, lines 176–185, assumes Borel scalar factors,
  real-pair exponents, and the required factorization with every Jacobian
  and normalizer included. Theorem 11's proof, lines 571–574, explicitly
  takes positivity from H-LF. The class at lines 216–219 requires positive
  stored measures. These are hypotheses, not proofs of 4.32. Physical-real
  positivity also has a smaller domain than (a)'s independent-current
  assertion. H-SUM, lines 208–215, is another input.

This agrees with `port-map.md`, Tables 1–3 and plan 4.2(4). In particular,
the positive factors in `4.27:lem-factor-positivity` are **radius factors**,
not weight factors: CA-I 132608–132674. The elimination-factor bookkeeping
at CA-I 107383–107514 does not assert the missing reality of every
interaction member either.

The outline index was read first: README; the R24 rows and neighbours of
chunk 05; the operation rows and neighbours of chunk 16; the class rows of
chunk 17; and their entries in `obligations.md`. The cited source ranges
read were SA 6265–6286, 17497–17532, 17566–17608, and 19408–19425.
R24 defines a positive fixed-measure representation. The operation section
assumes normalized positive moves; its argument establishes their
composition. Neither identifies the complete account's independent-current
weights. The old wide literature record is `lit-large-field.md`, §§0–1:
its YM3/QED3 comparison has no recycling operation of this kind.

Further source inputs were located through `sa-index/ca-full/index.tsv`
and checked in bounded ranges. The important ones are:

| Source | What is used here |
|---|---|
| CA-I 60950–61190 | The representation and its analytic/majorant inputs; these are carried inputs, not proved anew. |
| CA-I 10504–10590 | The radii and the hypotheses of twist stability. |
| CA-I 14992–15106 | The response chart is real for real independent \(J\), real data and real switches. Port this fact. |
| CA-I 20497–20511; 84388–84455 | The exponent of \(\mathbf T'_k\); only its quadratic form and \(V(X^\sim)\) depend on the exterior pair. |
| CA-I 51725–51780; 78008–78019 | Both classes of components; the gauge constraints; the core and shell variables of the operation. |
| CA-I 105753–105805; 108030–108033 | Component locality of the preparation tests, as cited there from Balaban. |
| CA-II 108960–109093 | The explicit reference quotient, `8.7:eq-resampling-kernel-2`, and its scope. |
| CMP 109, pp. 260–262, (1.3)–(1.10) | Explicit Gaussian extensions and the separately assumed analytic extensions of the interaction members. |
| CMP 119, pp. 251–252, (1.21)–(1.23); pp. 257–258, (2.17)–(2.21) | The strip substitution and component operations. |

The local CMP 109/119 texts were read in `~/ym4d-papers`. Direct download
requests for CMP 122a/b returned publisher article HTML, not PDFs. No claim
below is based on having read those PDFs. Formulas attributed to them here
are the formulas reproduced at the cited CA/SA locations. The unverified
identification with their full construction remains explicit.

### Uses of the proposition

The literal label search finds the declaration only. Searching its title
also finds the following uses; their surrounding passages were read.

| Source | Required part |
|---|---|
| CA-I 21331–21407; 22860–22876 | Positive base mass in the island-operator bound; the large-field expansion takes the dichotomy as an input. |
| CA-I 157028–157084 | Stability hypothesis (h1) needs termwise positive measures; (h8) needs positive reference normalizers. |
| CA-I 157457–157594 | Gauge fixing uses defined reference laws and the null/non-null alternative. |
| CA-II 71305–71320 | The two-point theorem uses positivity for union bounds. |
| CA-II 105508–105618 | The terminal-live proof integrates against a nonnegative remaining measure and sums nonnegative masses. |
| CA-II 106450–106469 | The young-cell estimate lists the dichotomy among its hypotheses. |
| CA-I 166624; CA-III 110873–110878, 111063–111065, 111100–111101, 111215–111216 | Dependency/status listings, not additional proofs. |

## 2. Reference denominators: the measure argument

This section supplies the positivity argument **after** the reference
background exists on the specified cutoff domain. That background-domain
input is exactly the input cited in the first paragraph of the Route,
CA-I 156961–156971. It is not inferred from this section.

**Lemma 1 (tree gauge and an open reference set).** Let \(E\) be a finite
edge set and \(T\subset E\) its gauge-fixing forest, including the
anchoring edges used in the reference law. Eliminate the tree variables
by setting \(V'_e=1\), \(e\in T\). Let \(\lambda_T\) be product Haar
probability in the remaining variables. Suppose the Borel indicator \(\chi\)
contains a product of identity neighbourhoods of these free variables.
Suppose \(U(V'V_\Lambda)\in SU(N)^E\) is defined and Borel on this cutoff.
For a nonnegative finite plaquette weight \(\zeta\), set

\[
 Z_\Lambda=\int\chi(V')
 \exp\{-g_k^{-2}A(\zeta,U(V'V_\Lambda))\}\,d\lambda_T(V').
 \tag{1}
\]

Then \(0<Z_\Lambda\le1\). This holds separately at every exterior for
which these hypotheses hold; no exterior-uniform lower bound is required.

*Proof.* The tree delta is a measure, not a function to omit. In each
tree coordinate its integral is evaluation at the identity. Product
integration therefore gives exactly \(\lambda_T\) on the free coordinates.
Equivalently, fix a root and remove leaves successively. Multiplication
by the parent gauge variable preserves Haar measure. Each tree edge
eliminates one gauge variable with Jacobian one. An anchoring edge fixes
the otherwise remaining constant gauge transformation.

Every nonempty open set \(B\) in a compact group has positive Haar mass.
Indeed, its translates cover the group and a finite subcover exists.
If \(m_G(B)=0\), that finite cover would give \(m_G(G)=0\), a contradiction.
Hence a product \(B\) of identity neighbourhoods in the free coordinates
has \(\lambda_T(B)>0\). With no free coordinates its mass is one.

Use the action at CA-I 60970–60974 and the normalized trace convention
at CA-I 157605–157606. A unitary matrix satisfies
\(-1\le\operatorname{Re}\operatorname{tr}W\le1\). Thus, writing
\(Q_\zeta=\sum_p\zeta(p)\),

\[
 0\le A(\zeta,U)\le2Q_\zeta,
 \qquad
 e^{-2g_k^{-2}Q_\zeta}\lambda_T(B)\le Z_\Lambda\le1.
 \tag{2}
\]

Both bounds follow by integrating pointwise inequalities. The lower
bound is strictly positive since the graph and the coupling are finite.
This proves the lemma. ∎

In SA 17604–17608 the reference cutoff is
\(\lvert i^{-1}\log V'(b)\rvert<M_0\varepsilon_k\).
It contains the required free-coordinate neighbourhood of the identity.
CA-II 109006–109030 reproduces the corresponding quotient from
CMP 122a (1.100). Lemma 1 proves its positivity once the cited background
construction is admitted on this cutoff. It avoids the insufficient
argument that a nonempty set must have positive measure.

The reference density divided by (1) has integral one. For a finite
positive input kernel \(\tau_e\), with exterior \(e\), put
\(m(e)=\tau_e(1)\) and let \(s_e\) be this reference probability.
The replacement \(m(e)s_e\) has the same mass \(m(e)\). Tonelli applied
to the exterior measure proves preservation of total mass. Averaging a
gauge transform with Haar probability preserves every gauge-invariant
test function. Hence the reversed tree-gauge operation gives the required
equivalence for such functions; it need not give equality of densities.
This is the measure content of (c), conditional on its stated
background-domain and Borel inputs.

## 3. The exact null-label implication

**Lemma 2 (common measure).** Let a finite set of histories carry positive
measures \(\mu_\omega\), fixed measurable sets \(S_\omega\), and measurable
weights \(w_\omega(\xi,p)\). Assume that \(w_\omega\) is finite everywhere
on its stated domain, strictly positive on \(S_\omega\) for real \(p\),
and absolutely integrable for each admitted \(p\). The real parameter
set is nonempty. Define

\[
 T_pF=\frac1{2^d d!}\sum_\omega
       \int_{S_\omega} F(\omega,\xi)w_\omega(\xi,p)\,d\mu_\omega.
 \tag{3}
\]

Then the positive-operator assertion of (b), the equivalences in (d3),
and the operator assertion of (d4) hold for (3), with
\(\mathfrak m=\sum_\omega\mu_\omega(S_\omega)\).

*Proof.* For real \(p\), (3) defines a positive finite measure. Integrating
\(|F|\le\|F\|_\infty\) proves
\(|T_pF|\le\|F\|_\infty T_p1\).
If \(\mu_\omega(S_\omega)=0\), its integral is zero for every admitted
complex \(p\). Conversely, at a real \(p\),

\[
 S_\omega=\bigcup_{n\ge1}
 \{\xi\in S_\omega:w_\omega(\xi,p)\ge1/n\}.
\]

If \(\mu_\omega(S_\omega)>0\), one set in this union has positive
measure. Its contribution to the integral is positive. Thus zero
weighted mass is equivalent to zero unweighted mass, history by history.
The index set is finite and each real summand is nonnegative. Summing
gives the equivalence for the full operator, at every real \(p\).

If \(\mathfrak m=0\), every \(S_\omega\) is null. The integral over
each is zero for every complex \(p\), whatever its phase. This uses a
null-set identity, not analytic continuation from the real set. The
argument applies to every measurable \(F\) for which the operator is
defined. ∎

Once (d1)–(d2) are established for the **actual** operation, take
\(w_\omega=e^{\Phi_\omega}\). Lemma 2 supplies the sixth step of the
Route. A containing summand is then zero before any subsequent finite
sum or absolutely convergent resummation. Removing it preserves the
density, activities and products. Quotients must be formed only after
this removal. This gives precisely the null-label bookkeeping of (d4).

Lemma 2 does not establish (d1) or (d2). In particular, a block delta
cannot be replaced by unweighted Haar measure. Even on one group,
\(\int F(v)\delta_1(v)\,dv=F(1)\) is different from \(\int F(v)\,dv\).
The reduction to free coordinates must transport the tests and the
observable as well as every Jacobian. The source's statement is not
refuted by this example: its integration space may already be reduced.
It is a check that any proof of that statement must pass.

## 4. Reality at independent currents: three attacks

Write \(P=(\mathbf U,\mathbf J)\). On the group and the Hermitian
Lie-algebra convention, the real structure is

\[
 \sigma P=((\mathbf U^\dagger)^{-1},\mathbf J^\dagger).
 \tag{4}
\]

It acts bondwise. Its fixed points have \(\mathbf U\in SU(N)\) and
Hermitian traceless \(\mathbf J\). In real-centred exponential coordinates
it is ordinary coordinate conjugation. Work on a conjugation-invariant
polydisc contained in the admitted pair domain. For a scalar holomorphic
function \(v\), put \(v^\#(P)=\overline{v(\sigma P)}\).
This is holomorphic: conjugating the coefficients of its convergent
coordinate power series gives its power series. The identity \(v=v^\#\)
implies reality at every real pair. Conversely, reality on the real open
part of such a polydisc implies the identity: apply the one-variable
identity theorem successively in every coordinate.

The member examined below is the **actual** \(V_\omega(X^\sim;\xi;P)\)
of CMP 122b (1.66)–(1.71), including its prescribed subtractions and
inherited boundary terms. This is the \(V\) in CA-I 20497–20511. Its
localisation and size statement are reproduced at CA-I 95908–95950.
Its size counts old cells; it is not a depth-independent difference
estimate. This distinction is explicit at CA-I 95946–95974.

### Attack 1: determine the extension from both real slices

The Route explicitly rejects uniqueness from the physical graph
\(\mathbf J=J(\mathbf U)\) alone. Adding the zero-current slice still
does not give uniqueness, even with gauge covariance and arbitrarily
many prescribed low-order jets.

Here is a hand witness to that inference. Let \(j(\mathbf U)\) be the
physical current, extended holomorphically in a small chart about the
flat field. In the Wilson action, replace
\(\operatorname{Re}\operatorname{tr}W\) by
\(\tfrac12\operatorname{tr}(W+W^{-1})\), which agrees with it for unitary
\(W\). This gives a holomorphic finite sum of traces of products of bond
matrices and their inverses; its current derivatives are holomorphic
as well. The current is Hermitian on real fields
and vanishes at the flat field. At a fixed bond \(b\), set

\[
 h(P)=\operatorname{tr}(\mathbf J(b)^2)
       \operatorname{tr}((\mathbf J(b)-j(\mathbf U)(b))^2),
 \qquad v_\varepsilon(P)=i\varepsilon h(P)^r,
 \quad r\ge1,\quad\varepsilon>0.
 \tag{5}
\]

The traces are invariant under simultaneous gauge conjugation of the two
currents. On real pairs, both traces are nonnegative, so \(h\) is real.
It vanishes identically on each of \(\mathbf J=0\) and
\(\mathbf J=j(\mathbf U)\). Choose a nonzero Hermitian traceless \(H\)
with \(\operatorname{tr}H^2=1\). At the flat field and current \(tH\) on
bond \(b\), one has \(h=t^4\). Hence
\(v_\varepsilon=i\varepsilon t^{4r}\ne0\) is nonreal whenever \(t\ne0\).
All sufficiently small such \(t\) lie in the independent-current chart.

The zero on each slice has transverse order at least \(2r\).
Given any finite jet order, increasing \(r\) makes those jets vanish.
On a fixed smaller closed polydisc, \(h^r\) and each of its finitely many
specified derivatives are bounded. Decreasing \(\varepsilon\) therefore
makes their perturbations as small as desired. This argument uses
compactness and polynomial differentiation, not a numerical estimate.

**Failure of the attack.** Neither slice fixes the transverse current
coefficients. In coordinates \(q=\mathbf J-j(\mathbf U)\), the physical
graph fixes only the constant term in the Taylor expansion in \(q\).
Equation (5) shows that the extra zero-current slice and any finite jets
still leave nonreal higher terms. It is a counterexample to an inference,
**not** to Proposition 4.32: it has not been identified with an allowed
member of Balaban's actual construction. Thus it cannot be substituted
for the requested counterexample endpoint.

### Attack 2: use a small phase and continue positivity from \(J=0\)

CA-I 84394–84416 compares the operation at \(P\) with the operation at
\((U,0)\) by a small extra exponent. AG1 Lemma 4 already proves the
zero-free-disc conclusion when its positive-centre and oscillation
hypotheses hold. We retain that conditional conclusion; no new proof of
its zero-free theorem is needed here.

Even granting a stronger, uniform estimate
\(\sup_\xi|\Delta_\omega(\xi;P)|\le1/4\), the following continuation
argument fails. A nonzero holomorphic weight, positive at \(J=0\), need
not remain real on the real-current path. In the one-point probability
space take \(w(P)=\exp(v_\varepsilon(P))\), with (5). It equals one on
both real anchor slices, is everywhere nonzero, and can have arbitrarily
small exponent. Along the real path just used,

\[
 \operatorname{Im} w(P(t))=\sin(\varepsilon t^{4r})>0
 \quad\text{if }0<\varepsilon t^{4r}<1.
 \tag{6}
\]

For completeness, on \(0<\theta<1\) the sine series gives
\(\sin\theta\ge\theta-\theta^3/6>0\): the terms after the first two
can be paired into nonnegative pairs since their successive absolute
values decrease. This establishes (6) by hand.

Shrinking the final coupling ceiling cannot turn an inequality into an
exact reality identity. This remains so in the account's order of
choice. Suppose, solely for this attempted route, the extra exponent
has bound \(C g_k(\log g_k^{-2})^a\), with \(C>0,a\ge0\) fixed by
Stages 0–7. For \(n>a\) an integer and \(t=\log g_k^{-2}\ge1\), the
exponential series gives

\[
 C t^a e^{-t/2}\le C2^n n!\,t^{a-n}.
 \tag{7}
\]

Choose
\(t_0\ge\max\{1,(4C2^n n!)^{1/(n-a)}\}\) and then impose
\(\gamma\le e^{-t_0/2}\) at Stage 8. The bound is at most \(1/4\)
for every \(g_k\le\gamma\). This is an admissible downward ceiling,
chosen before \(\gamma_H,g,m,g_0,K\), exactly as CA-I 1642–1717
requires. No depth or volume may enter \(C\). The old-cell size bound
on \(V\) does **not** supply this premise.

**Failure of the attack.** Even under this favourable bound, (6) persists
at arbitrarily small positive \(t\) and phase. Nonvanishing can prevent
a sign change only after reality has been proved. Positive real part
or a small argument cannot supply the nonnegative measures used in
stability (h1), or the ordered integrations in the terminal-live proof.
This attack therefore neither proves (a) nor gives a corrected theorem
adequate for those consumers.

### Attack 3: commute the prescribed construction with conjugation

This is the route that could prove the needed identity. A useful
closure argument can be completed, but its application to the actual
localized scalar interaction cannot yet be completed here.

**Lemma 3 (closure under real operations).** On conjugation-invariant
coordinate domains, scalar holomorphic functions satisfying \(f=f^\#\)
retain that identity under real linear combinations, products,
composition with maps commuting with the real structures, and inverses
where defined. They also retain it under real-coordinate differentiation,
integration against a fixed real measure with locally uniform integrable
majorants, and normally convergent sums. A holomorphic logarithm of such a function
on a connected domain retains it if its prescribed value is real at one
real point. The analogous assertion holds for a single-valued square
root prescribed real at a point where it is nonzero.

*Proof.* The assertions for sums, products, compositions and inverses
are identities obtained by conjugating the formulas. Difference
quotients along a real coordinate commute with conjugation; their
limits give the derivative assertion. For integration, write a complex
integrand as its real and imaginary parts and use the majorant to
integrate both; conjugation changes the sign of the second part.
On any smaller closed polydisc the majorant also permits Fubini in the
Cauchy integral formula. Expanding its Cauchy kernels on a still smaller
polydisc gives a convergent power series for the integral, so it remains
holomorphic.
Conjugation commutes with limits of convergent partial sums, proving
the assertion for normally convergent sums while retaining holomorphy.

If \(L\) is the prescribed logarithm, then \(e^{L^\#}=e^L\), so
\(L^\#-L\in2\pi i\mathbb Z\). This continuous integer-valued multiple
is constant on the connected domain and is zero at the given real
point. For a square root \(R\), \(R^\#=R\) in a neighbourhood of that
point by uniqueness of the root with the prescribed nonzero value;
the identity theorem extends this equality over the connected domain.
This proves the lemma. ∎

In particular, a localisation written with real switch derivatives,
real switch integrals and real combinatorial coefficients preserves
reality **if the switched input is real at real switches**. Connected
expansions made from these operations preserve it too, provided their
majorants justify the stated sums and integrals. No sign of an individual
connected coefficient is needed; its real exponent has positive
exponential.

The chart is not an open part of this argument. Port CA-I
`4.5:prf-chart-covariance`, especially clause (4), 15027–15028 and its
proof 15099–15102. It establishes reality at independent real \(J\),
real \(B\) and real switches. The switched chart proposition
`4.5:prf-chart-walk-localisation`, 15265–15345, carries that clause on
its stated hypotheses. We do not replace it by a new chart proof.

There is, however, a distinction between a real full sum and real
members after the construction assigns localisation domains. The
account's rule, CA-I 5120–5153 and 8839–8910, attaches switch products
according to each walk's footprint. In the elementary scalar example

\[
 K_1=\tfrac12+ih,\qquad K_2=\tfrac12-ih,
 \qquad K(s)=s_1K_1+s_2K_2,
 \tag{8}
\]

with real \(h\ne0\), \(K(1,1)=1\) is real while \(K(1,0)\) is not.
Thus reality of a total before localisation does not prove reality
after independent masks. A sufficient certificate is a conjugation
pairing of the terms that preserves their footprints and their scalar
coefficients; terms paired in this way receive the same real switch
monomial, so their sum is fixed by conjugation. The ported chart result
supplies reality for its own switched objects. Equation (8) is not a
claim that those chart walks fail.

For \(V_\omega\), the remaining identification is with **all** of the
prescribed localized inherited members, background differences and
normalization branches in CMP 122b (1.66)–(1.71). The cited
holomorphy and convergence statements allow the operations of Lemma 3
once their inputs and branches have been identified; they do not
themselves make that identification. The apparently broader
`4.38:cor-volume-families` does not bypass it: its hypothesis (c),
CA-I 60678, assumes propagation of the family clauses, and its proof
60698–60699 obtains reality from that hypothesis.

One can instead manufacture a real extension on a symmetric chart:

\[
 v_{\mathbb R}:=\tfrac12(v+v^\#).
 \tag{9}
\]

It is holomorphic, fixed by conjugation, has the same values wherever
the real input values of \(v\) are already real, and preserves a
conjugation-symmetric absolute bound. It introduces no additional
field reads. But it need not equal the prescribed extension. In (5),

\(v_\varepsilon^\#=-v_\varepsilon\), so (9) is identically zero and
changes \(e^{v_\varepsilon}\) off the anchor slices. Nonlinear
operations later in the construction need not commute with replacing
their input by its average (9).

**Failure of the attack.** Lemma 3 provides a precise sufficient
mechanism. Neither the reality of the chart nor reality of the full
unswitched density identifies every member of the actual \(V_\omega\)
with that mechanism. Symmetrization constructs a different candidate;
proving that it is the original operation would require the same
missing conjugation identity. This is the specific identification
still needed, not a failure of holomorphic calculus or of convergence.

## 5. Scope of the partial proof

Lemmas 1–3 are proved above from their displayed inputs. Lemma 1 settles
the measure-theoretic part of reference positivity once the cited
background-domain construction is supplied. Lemma 2 settles the
null/non-null implication once the actual common-measure formula and
pointwise positive weights are supplied. Lemma 3 gives a way to propagate
reality through specified operations. None is a proof of those missing
identifications by itself.

In particular, the reduction of the actual delta constraints, the
exterior independence of all transported tests, and the returned
locality assertion have not been proved here by writing out the entire
operation. The stopping point below is a necessary sublemma at the
Route's third step; it is not claimed to be an equivalence with all of
4.32. No counterexample to the actual proposition has been established.
The three attacks concern this sublemma, not replacement operations.

## Round 1 stopping lemma (retained)

**Open lemma**

**Reality of the prescribed localized interaction at independent
currents.** Fix the parameters in the complete account's order:
\(N\), its Stage-0 data, \(L\), the remaining Stage-1–7 choices,
then \(\gamma,\gamma_H\), then the admitted \(g,m,g_0,K\).
Let \(k\le K\). Use precisely the induction inputs of the Route at
CA-I 156955–156959: clause (a), definedness and analyticity of the
factors, and (d5), at every \(j<k\); use the definedness part of (i-a)
at level \(k\). Let \(X\) and \(\omega\) be as in Proposition 4.32,
and take every real \(\xi\in S_\omega\). Keep the actual localization, subtractions,
normalizations and branches of CMP 122b (1.66)–(1.71).

For every real-centred, \(\sigma\)-invariant coordinate polydisc
\(Q\subset\mathfrak D_k(X)\), prove the pointwise identity

\[
 V_\omega(X^\sim;\xi;\sigma P)
   =\overline{V_\omega(X^\sim;\xi;P)}
       \qquad(P\in Q).
 \tag{R_V}
\]

In particular the prescribed \(V_\omega\) must be real at **every**
admitted real independent pair, not merely on \(J=0\), on \(J=J(U)\),
or almost everywhere in the integration variables. The identity must
hold at the radii of the account's twist-stability lemma; no
history-, depth- or volume-dependent choice of an earlier parameter
is allowed.

This is an attempt to prove a step the account explicitly leaves open,
not a correction or a check of a completed proof. Attack 1 fails because
the two anchor slices do not determine transverse current coefficients.
Attack 2 fails because arbitrarily small nonzero phases defeat real
positivity. Attack 3 reaches the exact remaining task: verify
conjugation for the prescribed localized scalar members and their
branches, so that Lemma 3 applies to the original \(V_\omega\).
The chart's already proved reality is retained. Proposition 4.32 and
its downstream consumers remain conditional.

## 6. Continuation, 2026-11-05: three new attacks

Provenance: Codex continuation at the same checkout and source revision.
Sections 1–5, Lemmas 1–3, and the first round's stopping statement are
retained. The three attacks below start from \((R_V)\). None is a
computer-assisted step or a counterexample to Proposition 4.32.

The source statement, status sentence, Route, and uses listed in §1 were
read again. The literal proposition label still occurs only at its
declaration. The title occurs at the consumers recorded in §1. The
comparison with AG1, TP1 and IN1 is unchanged: their positive laws and
real scalar factors are inputs. In particular, physical-real positivity
in H-LF does not imply positivity for independent real currents.

New source passages read for this continuation are:

| CA-I lines | Use |
|---|---|
| 4389–4412; 9831–9906 | Independent-current domains. The current has a size bound; it is not required to be the current of the configuration. |
| 10304–10349 | The physical current and its plaquette-star formula. |
| 13705–13799; 14155–14202 | The prescribed free-current operators and the higher-order scalar \(V^J\). |
| 15470–15540; 15543–15585 | Ward identities and reduction of these operators at a true pair. |
| 8839–8910; 5218–5289 | The fixed walk rule and the vertex formula. |
| 9615–9699; 9794–9829 | Independence and agreement of terms wholly inside the small-field region; the stated restriction on straddling terms. |
| 93993–94113; 94120–94172 | The boundary family, and the separate extension rules for far and rough nuclei. |
| 95977–96063 | The five families of the resummed density and its definition through carriers. |
| 21005–21048 | The actual connected-series definition of the polymer logarithm. |

These were located through the outline index, including the neighbouring
R24 and operation rows, and `sa-index/ca-full/`. The old literature search
`lit-large-field.md`, §§0–1, was reused. The outline's operation is read at
SA 17497–17548 and 17566–17608. It does not identify an arbitrary real
independent-current pair with a physical background. The two-volume
independence statements in CA-I concern the *same pair* in two settings;
they do not supply such an identification either.

### Attack 4: realize the pair by changing a physical exterior

One possible way to prove \((R_V)\) would be to realize each real local
pair as the restriction of a physical configuration and its current.
Locality would then transfer physical reality to that pair. This is
stronger than analytic continuation from one slice: it asks for a
physical realization of each point. The realization fails locally.

**Lemma 4 (a fixed plaquette star fixes its physical current).** Let
\(b\) be a bond, and let \(\operatorname{Star}(b)\) contain every bond
of every plaquette containing \(b\). Let \(U\) and \(W\) agree there.
Then the currents of CA-I 10304–10332 satisfy

\[
 J(W)(b)=J(U)(b).
 \tag{10}
\]

Consequently, a pair \((U,J)\) with
\(J(b)\ne J(U)(b)\) has no physical extension agreeing with both entries
on a domain containing \(\operatorname{Star}(b)\).

*Proof.* The account's formula, with its spacing \(\xi\), is

\[
 J(W)(b)=\xi^{-3}\sum_{p\ni b}
       \pi\frac{W(\partial_b p)-W(\partial_b p)^{-1}}{2i}.
 \tag{11}
\]

Each factor in each ordered product \(W(\partial_b p)\) lies in
\(\operatorname{Star}(b)\). Replacing it by the equal factor of \(U\)
leaves the product, its inverse, and its projected imaginary part
unchanged. The finite sum therefore gives (10). The second assertion
follows by contradiction from (10). ∎

There are admitted real pairs to which this obstruction applies.
On a domain containing an interior plaquette star, take
\(U=\mathbf1\), a nonzero Hermitian traceless matrix \(H\), and a current
equal to \(tH\) at one positively oriented interior bond, zero at the
others, with the usual reversed-bond convention. For a fixed finite
label on this domain, choose \(t>0\) smaller than all its current radii divided by
\(|H|\). The flat configuration, its averages, and their physical
currents meet the remaining conditions. Its physical current is zero,
since every plaquette in (11) is the identity. Thus this independent
current is admitted but cannot be obtained by changing a physical field
outside the star. The current inequality is CA-I 9856–9858. The cube
gauge condition there constrains \(U\), not a divergence of \(J\).
The same example works in the hereditary class: all restricted flat
backgrounds are flat, and there are only finitely many current bounds
at a fixed finite level.

The obstruction is stronger than a failure of current conservation.
Take instead a circulation \(tH\) around one interior plaquette,
with the signs of its oriented boundary, still at \(U=\mathbf1\).
At each of its four vertices one incoming and one outgoing contribution
cancel, so the flat covariant divergence is zero. Formula (11) still
gives zero physical current on every bond. Fixing the flat plaquette
stars therefore prevents realization even of this conserved nonzero
independent current. Take \(t\) small enough for the same finite bounds.

This also explains the limit of the far-nucleus convention. A smooth
far subtracted copy is evaluated at

\[
 \operatorname{ext}_v(P)
  =(U_{p_v},J_{p_v})\bigl(Q_v,M^{p_v}(\mathbf U|_{Q_v})\bigr),
 \tag{12}
\]

by CA-I 94133–94151. It lies on a physical minimizer-and-current graph
at real data and does not read the independent \(\mathbf J\). If a
member is real on that graph, this particular pullback is real. But
the same convention evaluates every other subtracted copy, including
rough nuclei, at \(P\) itself. Replacing those evaluations by (12)
would change the prescribed construction.

**Exact failure.** Locality and enlargement cannot turn every independent
pair into a physical pair. Equation (11) forbids the proposed lifting
on the plaquette star. The account's actual split leaves direct
independent-current evaluations at rough nuclei. No choice of a larger
box, smaller coupling, or stronger exterior regularity removes this
failure. This is an obstruction to the proposed lifting, not to
\((R_V)\).

### Attack 5: obtain a positive real law by forcing the current

A second route would add a real source to the Wilson action, so that
the expansion about a fixed \(U\) has the independent current \(J\).
The resulting positive integral could then be used to establish reality.
There are two separate requirements: existence of a positive forced
integral, and equality with the account's prescribed extension.

**Lemma 5 (the constraint on a gauge-invariant forcing).** Let \(S\) be
a differentiable, gauge-invariant real action on a finite lattice. Write
its first variation about \(U\), with lattice spacing \(\eta>0\), as

\[
S(e^{i\eta A}U)=S(U)+\langle A,j_S(U)\rangle+o(|A|).
\]

For gauge parameters vanishing at fixed boundary sites, let
\(\mathcal D_U\lambda\) be the infinitesimal gauge direction, with
the sign convention of CA-I 15500–15511. Then

\[
 \mathcal D_U^*j_S(U)=0
 \tag{13}
\]

on the unfixed sites. In particular, at a flat field a nonzero current
supported on one bond between two unfixed distinct sites cannot be
the current of such an action.

*Proof.* A gauge change with parameter \(t\lambda\) has fluctuation
\(-t\mathcal D_U\lambda+O(t^2)\). Gauge invariance makes the first
derivative of the action along this curve zero. Hence
\(\langle\mathcal D_U\lambda,j_S(U)\rangle=0\) for every allowed
\(\lambda\). The definition of the transpose gives (13). At the
flat field, take \(\lambda=H\) at one endpoint of the selected bond
and zero at the other sites. For the single-bond current \(tH\), the
pairing is a nonzero signed positive lattice factor times
\(t\operatorname{tr}H^2\). Thus it cannot vanish for every
\(\lambda\). ∎

This is the first Ward identity of the account, applied to a proposed
forcing. Its proof is included to identify precisely what this attack
requires. It is not a new proof of the account's already proved Ward
lemma. Since the independent-current domain contains the single-bond
example of Attack 4, an action invariant under gauge changes of the
integration field, with the source held fixed, cannot realize all its
currents. A source transforming jointly with the background is a
different requirement: Lemma 5 does not rule out that construction.
Its issue is the identity with the prescribed extension, considered next.

Dropping gauge invariance makes a positive forced integral easy, but
does not establish the needed equality. To see the distinction by
hand, use real coordinates \(A\) on a compact chart cutoff \(K\) of
positive Lebesgue mass, with a bounded continuous real action
\(S_U(A)\). Put \(h=J-J(U)\) in these coordinates and define

\[
 Z_U(h)=\int_K e^{-S_U(A)-\langle A,h\rangle}\,dA.
 \tag{14}
\]

The integrand is positive and bounded above and below by positive
constants for each fixed real \(h\), so \(0<Z_U(h)<\infty\). For
complex \(h\) in a compact set, boundedness of \(A\) gives an integrable
bound on the exponential and all its parameter derivatives. Its power
series can therefore be integrated term by term. Thus \(Z_U\) is
holomorphic and satisfies
\(Z_U(\bar h)=\overline{Z_U(h)}\). Wherever it is nonzero, the local
logarithm normalized to the real logarithm at a real point is real on
nearby real points, by Lemma 3.

Formula (14) proves a property of this defined source integral. It
does not identify it with \(\mathbf T'_k\). A linear source changes
the first Taylor coefficient of \(S_U\), leaving its second and higher
coefficients unchanged. In contrast, the prescribed construction
uses the operators

\[
 (G^J_\pi)^{-1}=\Delta_a-\Theta'_J,
 \qquad
 \Theta'_J=\mathfrak k_J\Lambda+
       \Lambda^T\mathfrak j_J+\Lambda^T\mathfrak m_J\Lambda,
 \tag{15}
\]

and the \(J\)-dependent linearising map \(\mathfrak L^J\), not a
source-independent chart. These are CA-I 13720–13765 and 13996–14012.
At the true current the account identifies them with Balaban's
operators, CA-I 15543–15585. That identification is stated at
\(J=J(U)\), not as an identity with (14) for independent \(J\).
Matching higher Taylor coefficients and the Jacobian after this change
of coordinates would be required before using (14).

There is a useful port here. The scalar \(V^J\) of
`4.5:def-higher-order-functional` is real on its real domain. Read the
display at CA-I 14169–14186: it is a real linear combination of
bilinear pairings of the real chart objects, and the real Taylor
remainder \(V_0(\mathfrak L^J A';U)\). Reality of the chart objects is
already supplied by `4.5:prf-chart-covariance`(4). For \(V_0\), subtract
the constant, linear and quadratic Taylor terms of the real Wilson
action in real exponential coordinates. These coefficients are real,
so the remainder is real. Substitution into that displayed definition
proves the assertion for \(V^J\), with no new radius or constant.
This is the primitive higher-order action functional. It is not the
resummed interaction \(V_\omega(X^\sim)\).

**Exact failure.** Forcing invariant in the integration field with a
fixed source is ruled out for some admitted currents by (13).
Gauge-fixed real forcing does give (14), but no
identity with the prescribed localized scalar interaction has been
established. The port of \(V^J\) settles the primitive functional
only. It does not cover the inherited members, their filed pieces,
or the reference-denominator boundary family. Those are the objects
in \((R_V)\); replacing them by the logarithm of (14) is unjustified.

### Attack 6: recover the localized terms from positive subdomain laws

The third new route is to reconstruct the prescribed localized
interaction from logarithms of positive partition functions on every
subdomain. It would avoid proving a sign for connected coefficients:
only their reality matters. It requires more information than a
positive full partition function.

The required combinatorial operation is already proved in the account;
port `4.4:lem-vertex-formula`, CA-I 5218–5269. In its notation,

\[
 f_\sigma(P)=
 \sum_{\tau\subseteq\sigma}(-1)^{|\sigma\setminus\tau|}
                       f(1_\tau;P).
 \tag{16}
\]

Thus real values of *every prescribed vertex functional*
\(f(1_\tau;P)\) imply reality of every \(f_\sigma(P)\).
The account identifies these vertices, CA-I 5271–5287: they evaluate
one and the same nonlinear functional with each operator \(K\)
replaced by its masked walk sum \(K^{W(\tau)}\). This is an identity
about the fixed rule, not a statement that the vertex is the logarithm
of a new Wilson integral on \(W(\tau)\).

For example, a sufficient additional identity for this approach would be

\[
 f(1_\tau;P)
   =\log Z_\tau(P)-\log Z_\emptyset(P)+c_\tau(P),
 \qquad
 Z_\tau(P)>0,\quad c_\tau(P)\in\mathbb R
 \quad(P\ {\rm real}),
 \tag{17}
\]

with the logarithms and the constants *equal to the prescribed ones*.
If a vertex has a different normalization, (17) must include that
normalization too. A finite sum as in (16) would then be real.
The same reasoning applies to total interactions on nested domains:
if \(L(D)=\sum_{E\subseteq D}v(E)\) holds with the actual members and
real \(L(D)\) for every domain \(D\), subtracting the already determined
proper-subdomain members proves reality of \(v(D)\). This is just the
finite inversion embodied in (16); no new localization formula is
being substituted for the account's.

I tried to identify the vertices in (17) using the account's
whole-lattice comparison. What it supplies is more limited:
`4.4:cor-localised-independence`, CA-I 9615–9669, and
`4.4:cor-potential-agreement`, CA-I 9794–9817, identify a localized
member in two settings when its domain is contained in
\(\Lambda_{k+1}\), as a function of the **same** restricted
\((\mathbf U,\mathbf J,A)\). They do not identify it with a
restricted partition function. The latter corollary expressly leaves
straddling domains out, CA-I 9821–9827. Its reference to the cover
argument in Balaban CMP 119, p. 276, is labelled there as printed
without proof. Neither comparison removes the independent current or
the retained boundary members.

Even the elementary covariance step in the proposed identification
requires care. Restricting a covariance and constructing a covariance
on a restricted domain are different operations. For a hand calculation,
let

\[
 A=\begin{pmatrix}2&-1\\-1&2\end{pmatrix},\qquad
 A^{-1}=\frac13\begin{pmatrix}2&1\\1&2\end{pmatrix}.
 \tag{18}
\]

The form of \(A\) is \(x^2+y^2+(x-y)^2>0\) away from zero.
The first-coordinate compression of \(A^{-1}\) is \(2/3\);
the inverse of the first-coordinate compression of \(A\) is \(1/2\).
The displayed inverse is checked by multiplying the two matrices.
Thus domain restriction by itself cannot turn a prescribed covariance
into that of a new positive subdomain integral. This is not a claim
that the account's walk rule uses the wrong restriction. Its cell and
walk definitions could supply the right comparison; (18) shows why
that comparison has to be established, not assumed.

There is also a definite port concerning the logarithm. The account
defines its connected coefficient, CA-I 21005–21039, by

\[
 \mathbf R'^{(k)}(X)=
 \sum_{n\ge1}\frac1{n!}
 \sum_{\bigcup_pX'_p=X}
 \rho^T(X'_1,\ldots,X'_n)\prod_p F(X'_p).
 \tag{19}
\]

Here \(\rho^T\) is the finite sum of products of
\(\zeta(X'_p,X'_q)-1\), with \(\zeta\in\{0,1\}\).
It is therefore a real integer. Whenever the actual activities are
real and the account's absolute convergence holds, every partial sum
in (19) is real and its limit is real. The split into new boundary
terms and new \(\mathbf R\)-terms selects by the localization domain
and preserves that conclusion. This uses the supplied connected-series
definition; it neither chooses a different logarithm branch nor
reproves the cluster theorem. It propagates reality of activities.
Using it to infer the reality of its input activities would be circular.

The reference-denominator family remains a concrete obstacle to (17).
In `4.23:def-boundary-terms`, CA-I 93993–94036, the family
\(\mathfrak v^{\mathbf C}(Y_4)\) includes the denominator term
\(I(U_0)\). Its listed clauses are analyticity, joint gauge invariance,
and the summed absolute bound \(1+c_I M^5\). They do not assert reality
at independent real pairs. CA-I 94094–94097 says explicitly that these
clauses are an additional input to the correlation theorem.
The positive reference law of Lemma 1 gives a real logarithm of its
total normalization at a physical real exterior; it does not identify
each masked vertex or the required partial sum of this family with
that logarithm at independent \(J\).

The five-family decomposition at CA-I 95977–96063 is useful for locating
these terms. Its carrier notation is not an identity equating each
family with a positive subdomain integral, nor is it by itself an
identification of that section's density with every
\(V_\omega(X^\sim)\) in (1.71).

**Exact failure.** The finite vertex inversion (16) works, and the
connected logarithm (19) preserves real inputs. What this attack has
not established is the identity (17), or an equivalent real-input
description, for the prescribed masked functionals, including the
straddling and reference-denominator contributions. The available
comparison is equality in two settings at the same pair, not equality
with the positive subdomain laws. Naive restriction does not prove the
missing identity, as (18) demonstrates. Positivity of a full partition
function alone consequently does not finish this attack.

## 7. What this continuation adds

Lemmas 4 and 5 are hand proofs of obstructions to two proposed
realizations of an independent current. The circulation example
separates them: it obeys the Ward constraint of Lemma 5 but still
cannot be lifted through the flat stars in Lemma 4. The real primitive
\(V^J\), the vertex formula, and the preservation of reality by (19)
are ports or direct consequences of the account's proved formulas.
They are retained as such, not claimed as new proofs of those parts
of the account.

The parameter order is unchanged. Stages 0–7 are fixed first.
Then \(\gamma\) is chosen downward, then \(\gamma_H\); only afterwards
come \(g,m,g_0,K\), in the order of CA-I 1642–1717. The small \(t\)
in the current examples chooses a point inside already fixed radii.
It is not a new parameter of the construction and imposes no
history-dependent ceiling on an earlier constant. No argument here
shrinks an already chosen radius to exclude independent real currents.

The stopping lemma below concerns the prescribed **sum**
\(V_\omega\). Proving every filed member real would be sufficient but
is stronger than the lemma and is not imposed as a new requirement.
Cancellations within the actual sum are allowed. What cannot be used
is a replacement of that sum by its real part, a different source
integral, or a differently normalized subdomain logarithm.

## Result

**Open lemma**

**Reality of the prescribed scalar interaction at independent current.**
Use the parameter order and domains of
`4.32:prop-positivity-dichotomy`. At level \(k\), assume exactly the
Route's induction data: reality (a), finite analytic definedness and
the Borel component-locality clause (d5) at every \(j<k\), and the
definedness part of clause (i-a) at \(k\). Fix an admitted component
\(X\), one of its finite histories \(\omega\), and real integration
variables \(\xi\in S_\omega\). Let
\(V_\omega(X^\sim;\xi;P)\), \(P=(\mathbf U,\mathbf J)\),
be the scalar interaction actually prescribed by Balaban
CMP 122b (1.66)–(1.71), as used in the account, with its actual
localizations, inherited terms, background subtractions, denominator
terms and normalized analytic branches. The required assertion
\((R_V)\) is

\[
 V_\omega(X^\sim;\xi;P)\in\mathbb R
 \qquad\text{for every }P\in\operatorname{Reg}_k(X).
 \tag{20}
\]

Equivalently, in every conjugation-invariant polydisc \(Q\) centred
at a real point and contained in its stated analytic domain,

\[
 V_\omega(X^\sim;\xi;\sigma P)
     =\overline{V_\omega(X^\sim;\xi;P)},\qquad P\in Q,
 \quad
 \sigma(\mathbf U,\mathbf J)
       =((\mathbf U^\dagger)^{-1},\mathbf J^\dagger).
 \tag{21}
\]

Here the involution acts bondwise on the field variables and uses
the account's Hermitian real current convention. The equivalence is
local: on a real-centred chart, a holomorphic scalar real on the open
real slice has real Taylor coefficients (differentiate along real
coordinate directions), so it obeys the displayed reflection identity.
Conversely, evaluation at a fixed point of \(\sigma\) gives reality.

This is the same necessary open lemma retained from round 1, now tested
by three further attacks. Attack 4 fails because a fixed plaquette
star fixes its physical current, even for the conserved circulation.
Attack 5 supplies a positive source integral but no identity between
it and the prescribed higher-order and localized construction;
fixed-source gauge invariance also excludes nonconserved currents.
Attack 6 supplies finite inversion of vertex values but not their
identification with positive subdomain logarithms, in particular for
the retained boundary contributions. None is a counterexample to the
actual proposition.

If \((R_V)\) is proved, its scalar exponential is strictly positive at
every real integration point, so this specific obstruction in the
Route's reality step is removed. This is not asserted to complete
4.32: the exact measure and support identifications in (c), (d1),
(d2) and (d5) must still be supplied, and the other weight factors
must be followed through the same induction. Lemmas 1–3 remain
conditional tools for those steps. Proposition 4.32, stability
hypothesis (h1), and its downstream uses remain unproved here.
