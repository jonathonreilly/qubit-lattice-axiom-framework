# Repo search

The lead's `prior/repo-search-2026-11-08.md` was read in full. Its
search concerns the large-field/history route, not the present vortex
bound. Its closest reusable hit is the local Wilson witness in
PR 10114's `MASS_GAP_LOCAL_BLOCK_ASTRA.md`, Sections 1–2. This is
already used by `gap-fusion-astra.md`; it is not a confinement estimate.
The target-specific `prior/gap-vortex-astra.md` is absent at the pin.

I fetched main and PRs 10114, 10133, 10134, 10141 and 10144. A fresh
search outside this lane for `vortex.free.energy`, `Tomboulis`,
`Kanazawa` and `Ito.Seiler` found six files: three matching soft-route
files on each of PRs 10114 and 10133. The relevant primary passage is
`checks/review_massgap_block_literature.md:112–121`: local interpolation
does not establish the common global endpoint for twisted ratios.
This is a caution, not a bound. The other two files are its import and
literature tables. I also read the cited Wilson witness at lines
89–166 of `MASS_GAP_LOCAL_BLOCK_ASTRA.md`. Credit its Codex author;
the fusion proof and Claude Opus check already consume that result.
No new vortex supplier was found by this targeted search.

Search revisions, in that order:

```
main    a527a6fdaeb22ef8a0d1224cc2ba7bc42c48d3bc
10114   f76f6c649cff7dffbab664d8976e680e8f287fe9
10133   89faef229ff6e6bde42baad15ed8270c2f4087d8
10134   1e70c7211a2cdbc39001e619f1dd89db45e25851
10141   fb99b4dddc7254e6124ac124887d58eeb3a77802
10144   1f20846b8057f6346ebab6c0dbebdabbd9e472a4
```

`open-registry.md`, `open-core.md`, `l17c.md` and the FINISH rows
were searched. No other row owns this vortex-bound task. Fusion
(765–766), channel decomposition (771, 776), and the literature
readings are prior inputs, not work to repeat. Search logs are in
`/tmp/gap-vortex-astra-20261112/`. This is a bounded search record,
not a theorem that no differently named result exists.

## Source and statement contract

Author: **Codex gpt-6-astra max**, FINISH row 778, 2026-11-12.
Source pin: `8adccdfdd33131ac3f44e2201f803b40911bbf2b`.
Research text, not an audit; this grants no status. `PROVED` below
means a written author proof, not an independent check. `ARGUED`,
`GUIDE` and `OPEN` retain their ordinary lane meanings. No numerical
calculation supplies a premise.

The requested GOAL and FINISH instructions were read first, after
checking for the missing prior memo. The current main workflow points
to RULES, SETTINGS and the research procedure; those were read without
checking main files into this tree. Only this output file is edited.

The outline and CA-I were fetched once at `31a47c543775` into the
requested `/tmp/sa_ym4.tex` and `/tmp/sa_ca_I.tex`. Credit **Ethan
Sussman and Levent Alpoge, with Claude and Codex as authors of their
text**, for their work. Index lookup came first. The outline index,
its obligations and the CA indices have no hit for the present vortex
free energy, electric/magnetic flux, Tomboulis or Kanazawa objects.
The nearby mass-gap rows of chunk 01 and obligations were read, then
outline 565–600: the additional positive spectral estimate is separate.
CA-I 2490–2515 and 2698–2714 likewise exclude a Wilson-loop or mass-gap
claim. These scope passages are not a proof about twists. Nothing
from their ultraviolet construction is silently used below.

Prior mathematics used: `gap-fusion-astra.md` Sections 5–6 and
`gap-fusion-check-opus.md` in full; `gap-skeleton-final.md`
13.16–13.20; the actual R1–R3/Theorem R statements and proofs in
`gap-means-max.md` 4.1–4.6; `gap-channel-astra.md` 1.2 and 3.4;
the twisted transfer and Fourier formulas in `gap-flux-exercise.md`
3.0–3.1; and `gap-transfer.md` 8–9.3.
Credit Claude Fable 5.2 for Theorem R, Codex for the fusion and
channel arguments, and Claude Opus 5.5 for the fusion check.

The literature searches `prior/gap-lit-grok-paths.md` D and
`prior/gap-lit-flux.md` were read and credited to their named authors.
Kanazawa's primary text, arXiv:0808.3442v3, Section 2, and Seiler's
arXiv:0901.4246v1, Sections 2–3, were then read. No fresh broad
literature survey is claimed. The supplied papers folder is absent
on this worker. The PDF was fetched, but `pdftotext` is unavailable;
the primary arXiv HTML supplies the formulas used here.

## 1. Target and checkpoint

**Definition.** Let \(\Lambda=(a,a,c,d)\), with \(a\geq3\) and
\(c,d\in\{a,2a\}\), and use the Wilson normalization of the fusion
note. For \(k\in H^2(\Lambda;\mathbb F_2)\), set

\[
 r(k)=Z^k/Z^0,\qquad D=\max_k[-\log r(k)].
\]

**PROVED input, reused.** Each \(Z^k>0\), and \(Z^k\leq Z^0\),
by (TM-tw) and (S2). Thus this \(D\) is exactly the absolute-log
quantity in fusion (14). In every time frame, at fixed spatial twist
\(m\), the electric Fourier coefficients are nonnegative.

**OPEN target.** On a specified compact
\(I=[\beta_-,\beta_+]\subset(0,\infty)\), prove

\[
 D\leq C a^p e^{-\sigma a^2},\qquad C<\infty,\ p\geq0,\ \sigma>0,
 \tag{V}
\]

uniformly in \(\beta\in I\) and the required shapes. This is a bare
Wilson question. Identifying a coarse effective kernel remains separate.

**Checkpoint, 2026-11-12, final.** Sections 2 and 4–6 contain hand
proofs, not independently checked. The non-abelian contraction
survives arbitrary bounded Wilson reweighting of each selected pair.
It gives an area estimate and a uniform endpoint comparison for
the specified commutator word. The three identification tests in
Section 7 fail to turn it into a vortex estimate. The missing
step is the comparison of the actual twisted normalizers, or a
proved common representation (CF) that retains them. No bound
on \(D\) at order-one coupling has been obtained. The next
decision concerns that comparison, not more auxiliary smoothing.

## 2. Exactly how much electric suppression suffices

**Definition.** Choose time direction \(r\), a spatial twist \(m\)
in that frame, and a spatial direction \(i\). Write
\(v_{ri}\) for its one-plane temporal twist and \(C_i\) for the flip.
Define the parity probability

\[
 q_{r,i}(m)=
 \frac{\operatorname{Tr}(T_{r,m}^{n_r}(1-C_i)/2)}
      {\operatorname{Tr}(T_{r,m}^{n_r})}
 =\frac12\left(1-\frac{Z^{m+v_{ri}}}{Z^m}\right),
 \qquad Q=\max_{r,i,m}q_{r,i}(m).
 \tag{1}
\]

**PROVED.** These are probabilities in \([0,1/2)\). Moreover,

\[
 2Q\leq D,\qquad D\leq24Q\quad\hbox{if }Q\leq1/24.
 \tag{2}
\]

*Proof.* Positivity of the sector traces gives the probability formula.
Positivity of the twisted integral gives its strict upper bound.
Since \(e^{-D}\leq Z^k/Z^0\leq1\), the ratio in (1) is at least
\(e^{-D}\). Hence \(2q\leq1-e^{-D}\leq D\).

For the converse, in one time frame let \(e\) have \(s\) nonzero
bits. The signs of the commuting flips are random variables under
the positive trace state. The event that their product is negative
is contained in the union of the \(s\) negative-sign events. Therefore

\[
 \frac{Z^{m+e}}{Z^m}\geq1-2sQ. \tag{3}
\]

Delete from \(k\) all planes incident to axis 1, then all remaining
planes incident to axis 2, then the remaining plane 34. The three
applications of (3) have at most 3, 2 and 1 bits. Each denominator
is the next numerator; no change of coupling or measure is inserted.
Consequently

\[
 r(k)\geq(1-6Q)(1-4Q)(1-2Q)\geq1-12Q.
\]

For \(12Q\leq1/2\), integration of \((1-x)^{-1}\leq2\) on
\([0,12Q]\) gives \(-\log(1-12Q)\leq24Q\). This proves (2).
Thus an area bound on \(Q\) and (V) have the same asymptotic
content, up to constants. This reduction is not a confinement proof.

**Definition for the weaker consumer.** In frame 1 put

\[
 Q_F=\max_{m_2=0,\ i\in\{3,4\}}q_{1,i}(m),
 \qquad S=S_{\rm ev}(a;(a,c,d)).
\]

**PROVED sufficient test.** Every crossed sector with \(\chi\ne0\)
satisfies

\[
 p_{\chi,m}\leq8Q_F. \tag{4}
\]

Indeed such a \(\chi\) has a negative bit in direction 3 or 4.
Its trace is bounded by that entire negative-parity trace.
Also \(Z^m\leq Z^0\) and
\(Z_{0,0}=\frac18\sum_e Z^e\geq Z^0/8\).
These are exactly the two comparisons used in (4).

If \(Q_F<1/192\), the twelve such weights have total below \(1/2\).
The crossed weights sum to four and each is at most one. Thus each
of the four magnetic weights is at least \(1-96Q_F>1/2\), whereas
each other weight is at most \(8Q_F<1/2\). The light group is
\(L_{\rm mag}\) without assuming (ES).

The weakest sufficient test used in this note is consequently

\[
 8Q_F\leq K(a)\sqrt S,\qquad Q_F<1/192,\qquad
 K(a)\leq C_1a^{p_1}. \tag{FQ}
\]

It gives the fusion input (F-h), not the separate even seed. The
already proved witness \(S\geq\eta(\beta)^a\) makes
\(Q_F\leq C_2a^{p_2}\eta_*^{a/2}\) sufficient, where
\(\eta_*=\min_I\eta>0\), with \(K=8C_2a^{p_2}\), for large
\(a\). An area exponent is unnecessary for this implication.
Neither (FQ) nor its witness-based supplier is proved at order one.

## 3. What the light group and single-state result permit

**PROVED consequence of prior inputs; no new supplier.** Theorem R
is conditional on the even seed. Its four light sectors and
`gap-channel-astra.md` (23)–(24) do not supply the small parameter
they consume. Simple eigenvalues can approach the periodic top
eigenvalue as the box grows.

For the positive Wilson measure there is also a useful restriction
already implicit in (S1) and the prior kappa/full ordering:
the diagonal candidate \(L_\kappa\) cannot be the light group.
For a nonzero diagonal point \((\chi,m)=(m,m)\) in the crossed
set, (S1) gives \(p_{0,m}\geq p_{m,m}>1/2\). The magnetic point
\((0,m)\) would also be light, contrary to that candidate group.
Equivalently, \(S_\kappa\leq S_{\rm full}\) contradicts the
kappa branch of Theorem R. This is a consequence of existing
positivity, not a new non-abelian distinction.

The electric and magnetic candidates remain. On a periodic box
\(m=0\), the centre acts by a real sign; a charged state can have
zero momentum and a one-dimensional point-group representation.
For \(\chi=0\) the twisted momentum shifts in channel (6a)
vanish. Thus the single-state conclusion does not distinguish
these two candidates. Positivity-improving transfer kernels give
a strict finite-box Perron inequality, but no uniform distance
from equality here. Trying to infer (V) from these inputs stops
at that quantitative comparison. This is an unsuccessful route,
not a counterexample to (V).

**ARGUED literature boundary.** The Tomboulis–Yaffe inequality in
Kanazawa's Theorem 1, and its generalization in Theorem 2, convert
a small twist deficit to a Wilson-loop bound. The proof uses
site reflection positivity and, as printed, dyadic fits of the
rectangle into the torus. For SU(2) its input is
\(q=(1-Z^-/Z)/2\); it gives \(|\langle W(C)\rangle|\leq
2q^{A_C/(L_\mu L_\nu)}\). It gives no upper bound on \(q\).
See [Kanazawa, Section 2](https://arxiv.org/html/0808.3442v3#S2).
I use it only to identify the strength of the target, not as an
unproved converse or a vacuum mass-gap theorem. Ito and Seiler's
criticism, as explained by
[Seiler, Section 3](https://arxiv.org/html/0901.4246v1#S3), requires
a non-abelian input for an all-coupling confinement
argument. The next estimate has that distinction explicitly.

## 4. Non-abelian averaging: an exact contraction

**Definition.** For independent normalized Haar variables \(A,B\)
in SU(2), let \(\mu\) be the law of \([A,B]=ABA^{-1}B^{-1}\).
On \(L^2(SU(2),dg)\) set

\[
 (Kf)(g)=\int f(gh)\,d\mu(h),\qquad (Jf)(g)=f(-g).
\]

**PROVED, local group lemma.** On the centre-odd subspace \(J=-1\),

\[
 \|K\|_{2\to2}=\frac14. \tag{5}
\]

*Proof.* For an irreducible unitary representation \(\rho\) of
dimension \(d\), Haar averaging of \(\rho(A)X\rho(A)^*\)
commutes with every \(\rho(g)\). It is therefore
\((\operatorname{tr}X/d)I\). Averaging matrix units gives the
matrix-coefficient orthogonality relation with coefficient \(1/d\).
Apply these two identities successively:

\[
 \int\rho([A,B])\,dA\,dB
 =\frac1d\int\chi_\rho(B)\rho(B)^*\,dB
 =\frac1{d^2}I. \tag{6}
\]

For completeness, the SU(2) polynomial coefficient spaces are those
of \(\operatorname{Sym}^n\mathbb C^2\), of dimension \(d=n+1\).
These representations are irreducible: the diagonal subgroup has
the distinct monomial weights, and the raising and lowering
generators connect consecutive monomials with nonzero coefficients.
Symmetrization and contraction by the invariant alternating tensor
give
\(\mathbb C^2\otimes\operatorname{Sym}^n\mathbb C^2
=\operatorname{Sym}^{n+1}\mathbb C^2\oplus
\operatorname{Sym}^{n-1}\mathbb C^2\) for \(n\geq1\).
Dimension counting verifies that these exhaust the tensor product.
Induction decomposes every polynomial in matrix entries. Conjugate
entries of an SU(2) matrix are again signed entries, so these
polynomials form a self-adjoint algebra separating points. Their
density on the compact group gives the full \(L^2\) decomposition.
This is the polynomial form of the Peter–Weyl input already used
in the outline's one-bond calculation, lines 2197–2243; it supplies
no Wilson infrared estimate.

The centre acts on this coefficient space by \((-1)^{d-1}\).
On the odd spaces, \(d=2,4,6,\ldots\). Equation (6) makes \(K\)
scalar there, with largest eigenvalue \(1/4\), attained at \(d=2\).
Right translations are unitary, so \(K\) is bounded and the
calculation on the dense polynomial core extends to \(L^2\).
This proves (5).

**PROVED direct bounded-function version.** The commutator measure
has Haar density, for eigenangle \(0<\theta<\pi\),

\[
 w(\theta)=\frac{\pi-\theta}{2\sin\theta}\geq\frac12. \tag{7}
\]

Here is a derivation without a character-series limit. Write
\(B=\cos\phi+i\sin\phi\,n\cdot\sigma\).
The Haar density of \(\phi\) is \((2/\pi)\sin^2\phi\).
For Haar \(A\), the vector in \(ABA^{-1}\) is uniform on the
two-sphere. Its scalar product \(u\) with \(n\) is uniform on
\([-1,1]\). Thus
\(x=\tfrac12\operatorname{tr}[A,B]=\cos^2\phi+u\sin^2\phi\)
has, conditional on \(\phi\), density \(1/(2\sin^2\phi)\) on
\([\cos2\phi,1]\). Integrating over
\(\phi\in[\theta/2,\pi-\theta/2]\) gives density
\((\pi-\theta)/\pi\) for \(x=\cos\theta\).
The Haar density of \(x\) is \(2\sin\theta/\pi\).
Their quotient proves (7). The inequality is
\(\sin\theta\leq\pi-\theta\). Conjugation invariance supplies
the uniform conditional axis; endpoints have zero Haar measure.

Consequently \(\mu=\tfrac12 dg+\tfrac12\mu'\) for a probability
measure \(\mu'\). Every bounded centre-odd \(f\) has Haar mean
zero, so \(\|Kf\|_\infty\leq\tfrac12\|f\|_\infty\).
This weaker contraction does not need polynomial density.

**PROVED finite-beta version on actual Wilson conditional laws.**
Fix any twist \(k\), any two distinct links, and all other links
\(\xi\). Each selected link meets at most six plaquettes. The
part of the exponent depending on them has oscillation at most
\(24\beta\). Its normalized density relative to product Haar is
therefore between \(\delta_\beta\) and \(\delta_\beta^{-1}\), where

\[
 \delta_\beta=e^{-24\beta}. \tag{8}
\]

The same holds for two based loop holonomies \(A,B\), provided
each uses one selected link once and does not use the other.
Conditional on \(\xi\), these are separate Haar-preserving
coordinate changes on the two links. Their joint law has the
decomposition \(\delta_\beta(dA\,dB)+(1-\delta_\beta)\nu_\xi\).
After taking its commutator, let \(K_\xi\) be the corresponding
right-convolution operator. Right convolution by any probability
measure is an \(L^2\) contraction and commutes with \(J\).
Equations (5)–(8) give

\[
 \|K_\xi\|_{J=-1}\leq
 \rho_\beta:=1-\frac34e^{-24\beta}<1. \tag{9}
\]

The bounded-function version has coefficient
\(1-\tfrac12e^{-24\beta}\). These estimates are uniform in
\(\xi\), volume, and twist; on \(I\) use \(\beta_+\).
They are statements about the displayed auxiliary convolution.
They are not statements about the norm of \(T_{B,m}\).

**PROVED U(1) failure of the mechanism.** In U(1), every
commutator equals one, for every conditional law. Its convolution
is the identity, including on the nonempty subspace
\(f(-g)=-f(g)\). Thus (5) and every strict version of (9) fail
there. The distinction is noncommutativity, not just a finite
subgroup of the centre.

## 5. An area estimate that this operation really does prove

**PROVED auxiliary Wilson observable; not (V).** On each requested
torus, for \(a\geq8\), one can construct a bounded gauge-invariant
loop word \(W_a\) such that, in every twisted Wilson measure,

\[
 |\langle W_a\rangle_k|
 \leq \rho_{\beta_+}^{\lfloor a/4\rfloor^2}
 \leq \exp\left(-\frac{-\log\rho_{\beta_+}}{64}a^2\right).
 \tag{10}
\]

This is a direct test of the non-abelian mechanism at order one.
It does not change which loop or partition function the target reads.

*Construction and proof.* Choose base points
\(x=(4j,4l,0,0)\), with \(0\leq j,l<\lfloor a/4\rfloor\).
Select the outgoing links in directions 1 and 2 at each base.
Two different bases have periodic separation at least four in
one of those axes. Thus no plaquette contains selected links
from two different bases. Condition on every unselected link.
The selected pairs are then independent: every Wilson factor
contains links of at most one pair. Twisting changes no incidence.

Let \(A_x\) be the elementary 13-plaquette holonomy based at
\(x\), and \(B_x\) the 24-plaquette holonomy there. Each uses
exactly its own selected link once. Transport them to a common
root by paths \(P_x\) using only unselected links. Such paths
can run in the layer \(x_3=1\), with direction-3 segments to the
bases; all selected links lie in \(x_3=0\). Put

\[
 W_a=\frac12\operatorname{tr}
 \prod_x P_x[A_x,B_x]P_x^{-1}, \tag{11}
\]

in one fixed order. All factors are conjugated at the same root,
so the trace is gauge invariant. Its absolute value is at most one.
Equation (6) for the fundamental representation and the mixture
in (8) give

\[
 \left\|\mathbb E\left(P_x[A_x,B_x]P_x^{-1}\mid\xi\right)
 \right\|_{\rm op}\leq\rho_\beta.
\]

Conditional independence makes the expectation of the ordered
matrix product equal the ordered product of these expectations.
Submultiplicativity gives \(\rho_\beta^N\), with
\(N=\lfloor a/4\rfloor^2\). Taking the trace and integrating
\(\xi\) preserves the bound. Finally
\(\lfloor a/4\rfloor\geq a/8\) for \(a\geq8\), proving (10).
All constants follow from displayed inequalities; no enumeration
or numerical estimate enters.

**PROVED scope test.** This word has zero net oriented traversal
of every link: a commutator uses each constituent loop and its
inverse. In U(1), \(W_a=1\) identically. For SU(2), it is invariant
under every closed centre change on links; each based loop changes
by a central sign, which cancels in its commutator. The word has
no winding electric charge. It is neither the ordinary rectangle
in the Tomboulis–Yaffe inequality nor an electric parity projector.
No inequality comparing (1) to (10) has been proved.

## 6. The stronger comparison available for that same word

The following tests whether arbitrary nonnegative endpoint data can
be retained. It is useful because an expectation of one loop word
alone does not control a partition-function ratio.

**PROVED.** Put \(\delta=e^{-24\beta_+}\) and
\(s=1-\delta/2<1\). Let \(\nu_1,\ldots,\nu_N\) be the
conditional laws of the transported commutators in Section 5,
at any fixed exterior and twist, with \(N\geq2\). Their product
has a density \(w_N\) relative to Haar satisfying

\[
 w_N(g)\geq\frac{\delta^2}{2},\qquad
 \left|\frac{w_N(-g)}{w_N(g)}-1\right|
 \leq\varepsilon_N:=8\delta^{-4}s^{N-2}
 \quad\hbox{for Haar-almost every }g. \tag{12}
\]

*Proof.* The two-sided density bound in (8), pushed forward by
the commutator map, gives inequalities of measures
\(\delta\mu\leq\nu_j\leq\delta^{-1}\mu\).
Conjugation by the fixed transport does not change \(\mu\).
By (6), \(\mu*\mu\) has the uniformly absolutely convergent
character density, with \(\chi_d\) denoting the dimension-\(d\)
character,

\[
 \sum_{d=1}^{\infty}d^{-3}\chi_d(g).
\]

Indeed its matrix Fourier coefficients are \(d^{-4}I\);
the displayed series has these coefficients. Polynomial density
identifies the measure. Since \(|\chi_d|\leq d\), its absolute
value is at most
\(\sum_{d\geq1}d^{-2}\leq1+\int_1^\infty x^{-2}dx=2\).
By (7), its density is also at least \(1/2\).
Positivity of convolution now gives

\[
 \delta^2/2\leq w_2\leq2\delta^{-2}.
\]

Further convolution with probability measures preserves the lower
bound. Also each \(\nu_j\geq(\delta/2)dg\). Convolution by it
contracts the supremum norm of a centre-odd function by at most
\(s\), since the Haar part integrates that function to zero.
The difference \(w_2(g)-w_2(-g)\) is odd and has supremum norm
at most \(4\delta^{-2}\). Applying the remaining \(N-2\)
convolutions gives \(4\delta^{-2}s^{N-2}\). Divide by the lower
bound \(\delta^2/2\) to obtain (12).

In particular, for any measurable \(F\geq0\) with finite nonzero
integral against \(w_N\),

\[
 \left|\frac{\int F(-g)w_N(g)\,dg}
                 {\int F(g)w_N(g)\,dg}-1\right|
 \leq\varepsilon_N. \tag{13}
\]

This follows by substituting \(g\mapsto-g\) in the numerator
and applying (12) pointwise. The comparison is uniform in \(F\)
and in the exterior. Thus it survives integration against one
**common nonnegative exterior weight**. When
\(\varepsilon_N\leq1/2\), the absolute logarithm of the ratio
is at most \(2\varepsilon_N\), by integration of \(1/(1+x)\).

**OPEN common-factorization test for the target.** For each pair
\((m,m+v_{ri})\), it would suffice to represent its two actual
partition functions as

\[
 \begin{split}
 Z^m&=\int d\lambda(\xi)\int F_\xi(g)w_{\xi,N}(g)\,dg,\\
 Z^{m+v_{ri}}&=\int d\lambda(\xi)\int F_\xi(-g)w_{\xi,N}(g)\,dg,
 \end{split} \tag{CF}
\]

with the same nonnegative \(d\lambda,F_\xi,w_{\xi,N}\), the
measure bounds of (12), and \(N\geq c a^2\) for a fixed \(c>0\).
All factors, including every normalization, must be identical
except for the displayed sign. Equations (13), (1) and (2) would
then prove (V), with constants uniform on \(I\). For example,
for sufficiently large \(a\), they give
\(Q\leq\varepsilon_N/2\) and \(D\leq12\varepsilon_N\).
This is a sufficient representation, not a representation proved
for Wilson theory, and not claimed to be the weakest hypothesis.
The weaker actual-model consumer remains (FQ).

## 7. Attempts to identify the operator: exact failures

### 7.1 Gauge averaging does not supply the needed operation

**PROVED obstruction to this implementation.** Let \(\Gamma_x(h)\)
be the usual local gauge action at a site. On the physical Hilbert
space, \(\Gamma_x(h)\psi=\psi\). Consequently

\[
 \int\Gamma_x([A,B])\psi\,dA\,dB=\psi. \tag{14}
\]

This holds also in a nonzero electric-flux sector. Such a sector
is gauge invariant; it is charged under a winding flip, not under
a site gauge transformation. For example the trace of a spatial
Polyakov loop is gauge invariant and changes sign under its
winding flip. It is a nonzero physical vector fixed by (14).
Thus the colour contraction (5) cannot be implemented on the
flux sector merely by inserting local gauge integrals.
This blocks that attempted use of non-abelian structure exactly.

### 7.2 Many local contractions are not many serial contractions

**PROVED obstruction to tensorizing (5) as an area estimate.**
On \(L^2(SU(2)^N)\), let \(K^{\otimes N}\) act independently
and let \(J_{\rm all}\) change every variable's sign. The function
\(f(g_1,\ldots,g_N)=\operatorname{tr}g_1\) is centre odd and has
eigenvalue \(1/4\), for every \(N\). In fact the norm on the
odd subspace is exactly \(1/4\): a tensor coefficient is odd
when an odd number of its factors have even dimension, and its
eigenvalue is \(\prod_j d_j^{-2}\). At least one factor is at
most \(1/4\); all others can be trivial. It is not \(4^{-N}\).

The geometry in (11) forces a **single product** through all
selected pairs. A general charged boundary state need not have
that form. Even in the actual selected-link experiment, a
Polyakov trace using only direction-3 links is measurable in the
conditioned exterior and is unchanged by every pair integration.
Its direction-3 centre charge remains. A proof would have to
force every relevant flux contribution through a common serial
carrier and retain its weight. Neither Theorem R nor single-state
dominance establishes this geometry.

### 7.3 Exact Wilson integration retains different normalizers

**PROVED identity locating the failed step.** For the selected
pairs of Section 5, split the Wilson exponent into plaquettes
meeting no selected link and plaquettes meeting each pair.
No plaquette meets two different pairs. At fixed exterior \(\xi\),
write their positive factors as \(C_k(\xi)\) and
\(f_{k,x}(A_x,B_x;\xi)\), respectively. The separate Haar
coordinate changes have Jacobian one. Exactly,

\[
 Z^k=\int d\xi\ C_k(\xi)\prod_x z_{k,x}(\xi),\qquad
 z_{k,x}(\xi)=\int f_{k,x}(A,B;\xi)\,dA\,dB. \tag{15}
\]

Sections 4–6 control the normalized laws
\(f_{k,x}/z_{k,x}\) and their product commutator. They do so
for every \(k\), separately. They put no relative estimate on
\(C_k\prod_x z_{k,x}\) and \(C_0\prod_x z_{0,x}\).
When computing \(Z^k\), the integral of each conditional
commutator density is simply one. Its flattening therefore does
not flatten the missing factors in (15).

Moving a centre stack by link sign changes preserves its
cohomology class. It does not turn a nontrivial twist into the
sign of the contractible word (11) with all factors in (15)
unchanged. No such change of variables is supplied. Reflection
positivity gives positive forms in each twisted box; it does not
identify these different normalizers. Claiming (CF) from the
conditional contraction would omit precisely these factors.

This is the same kind of common-normalization issue stressed by
Ito and Seiler, now displayed for this attempted SU(2) mechanism.
It is not an obstruction theorem against other factorizations,
or a counterexample to (V).

## 8. What is proved, and the remaining statement

| Statement | Author label | What it gives |
|---|---|---|
| (2) | PROVED | The all-twist area bound is equivalent, up to constants for small values, to the area bound on the parity probabilities (1). |
| (4), (FQ) implication | PROVED | A weaker sufficient condition for (F-h); it needs only the crossed magnetic backgrounds and a comparison to the even sum. |
| (5)–(9) | PROVED | An exact non-abelian contraction, with uniform conditional finite-beta constants. It fails for U(1). |
| (10)–(13) | PROVED | Area suppression and arbitrary nonnegative endpoint comparison for one explicit commutator word in the actual Wilson measures. |
| (14), tensor example, (15) | PROVED | The displayed gauge-averaging, tensorization and normalization shortcuts do not identify that word with the flux trace. |
| (CF) for the actual twisted pair | OPEN | A sufficient common representation; no construction is given. |
| (FQ) at order one; (V) | OPEN | The requested fusion supplier and the stronger vortex estimate remain unproved. |

The precise missing Wilson estimate can be stated without any new
representation. For \(\beta\in I\), on all the requested shapes,
one needs either

\[
 \max_{m_2=0,\ i=3,4}
 \frac{\operatorname{Tr}(T_{(a,c,d),m}^{a}(1-C_i)/2)}
      {\operatorname{Tr}(T_{(a,c,d),m}^{a})}
 \leq\frac{K(a)}8\sqrt{S_{\rm ev}(a;(a,c,d))}
 \tag{16}
\]

with polynomial \(K\) and the smallness in (FQ), or, for the
full requested conclusion, the area estimate for all frames and
backgrounds in (1). The latter is equivalent to (V) by (2), not
a newly easier problem. The proposed non-abelian route would have
to prove (CF), or an inequality with the same common-normalizer
control, before its local contraction can supply either estimate.

No auxiliary assumption is promoted to a Wilson fact. No numerical
run, machine enumeration, or computer-assisted proof was used.
The new mathematics has not been checked by another provider.
No audit, registry, queue, source proof, or scientific status was
changed. No cutoff-uniform result follows: an effective coarse
kernel still has to be identified, as the fusion note requires.

RESULT: OPEN — (14)/(V) and order-one (F-h) are not proved; hand proofs give a non-abelian conditional commutator contraction and an area bound for an explicit Wilson loop word, but the common-normalizer comparison to the actual electric-flux traces remains missing.
