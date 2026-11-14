# P10: preparatory boundary, representation, stability and sourced exactness

Provenance: Codex (GPT-6 family; effort not exposed), 2026-11-05; checkout `37ce286433941bb9aa1a2d41dcb99466fc5a8a58`. Research text, not an audit; grants no status. Port of Ethan Sussman and Levent Alpoge's complete account at `31a47c543775`, with Claude and Codex as authors of their text; credit also to Tadeusz Balaban for his stage theorem and renormalisation construction. Written proofs only; no computational discharge. Not yet checked by another model.

## 1. Sources, standing and conventions

CA-I means `theorem_0_complete_account_raw_I.tex`, revision `31a47c543775`,
read at `/tmp/sa_ca_I.tex`. SA means `YM4_sketch_500.tex` at that revision,
read at `/tmp/sa_ym4.tex`. A citation `CA-I:54985` is a source-file line.
The source convention at CA-I:27–76 distinguishes a proved implication
from the supply of its antecedents. An unqualified heading declares a proof;
it does not make the inputs unconditional. Mathematical statements below
retain the source's quantifiers, bounds and exceptions. Prose is restated.

The owner supplies these standings at this checkout:

| Input | Standing retained here | Use or scope |
|---|---|---|
| [P1](p1-base.md) | Checked port | Wilson conventions and finite first-passage arithmetic. |
| [P3](p3-free.md) | Checked port | Free-field algebra; not the interacting representation. |
| [P4](p4-operator.md) | Checked port | Conditional operator and chart implications, with their inputs. |
| [P5](p5-induction.md) | Checked port | A5, A6, A12 and A13; not every induction lemma. |
| [P7](p7-torus.md) | Checked port | A14, conditional on all seven hypotheses. |
| [P6](p6-correlation.md) | Ported | Correlation induction; its source and window assumptions remain. |
| [P8](p8-positivity.md) | Ported | Its finite positivity and limit implications; not A18. |
| [P9](p9-witness.md) | Ported | Its witness/volume-transfer implications, with their inputs. |
| [MU](../mu.md), [LRB](../lrb.md), [OC](../oc.md), [UI](../ui.md), [PDA](../pda.md), [LSC](../lsc.md) | Refereed | Only their actual stated domains and conclusions. No automatic identification with a differently scoped CA leaf. |

These standings come from the owner, not a new check in this file. An older
provenance sentence in an input does not change them. The normalization
qualification from [NRM](../../gates/nrm-check.md) remains attached to LSC.
The open lemma `R_V` in [PD](../pd.md) does not supply A18.

Navigation used the outline index README, chunk rows and obligations before
source excerpts; the CA 4.12–4.19 index and full index then located the ports.
SA:20133–20138 separates dilation from torus independence.
SA:22564–22586 sketches frozen-source exactness; SA:22935–22950 gives its
frame version conditionally. These passages are orientation, not substitutes
for the CA proofs. `chain-ca.md` A14 and §7.2 require a level induction.
The workflow at the pinned commit was read with `git show`, since this is
a sparse checkout. Only this output file is changed.

## 2. A10: preparatory boundary terms

**Source:** `4.18:thm-preparatory-boundary`, CA-I:54985–55052;
proof CA-I:55054–55192. The heading is unqualified: the source declares
a **proved implication**. Its first input, CA-I:54989–54998, is assumed.
It is not proved by the transfer argument below.

### 2.1 Exact hypotheses and notation

Fix step `k`. Retain the following named hypotheses.

* **H-STAGE:** Balaban's inductive preparatory-stage theorem, CMP 122a
  (1.60)–(1.70), holds with its standing hypotheses. It supplies the
  analyticity spaces, weighted norm, constants
  `c_G,K_L,𝔰,𝔭_j,𝔩_j,q,C_2,κ_1,ϑ,K'_S`, rates `a_m`, and conditions
  `(K),(Q⁺),γ≤γ₀`. Its Gaussian normalization, cluster expansion and
  stage-cumulation conclusions are part of this input.
* **H-PROFILE-CLASS:** Those statements hold for every system with profiles
  admissible at every stage. This is distinct from H-STAGE for the printed
  profiles.
* **H-RECURSION:** The profile-independent integration structure and the
  recursion `4.18:def-stage-recursion`, CA-I:54226–54363, apply. The two
  inputs `(α),(β)` of `4.18:prop-profile-independence`, CA-I:54497–54505,
  are retained. Both systems represent the same stage-zero action, use
  the same members, couplings, collars, fields, cutoffs and Gaussian
  measures, and differ only in the compensating Wilson weights.
* **H-INDICATOR:** Hypothesis (ii) of `4.18:lem-weight-difference`,
  CA-I:54694–54698: the smoothed indicators lie in `[0,1]`, vanish within
  distance `σ/8` of a member, and equal one outside its `σ/4` neighbourhood.
* **H-PREPARED:** The prepared component, sequence, collars and admissible
  profiles of `4.18:def-prepared-sequence`, `def-profiles-admissible` and
  `def-coupling-excess` are supplied, with `(K),(Q⁺),γ≤γ₀` at step `k`.

The source invokes the weight-difference lemma beyond its separately named
indicator input. To expose that use, **H-WEIGHT** retains its other premises
(i),(iii)–(viii), CA-I:54690–54715: `0≤β_i≤b₀`; the two prepared-sequence
relations; ten-layer growth `Z_i⊃(Z_{i-1})^{+10a_i}` at T-levels;
`Z''_{j+1}⊂Z''_k`; distance at least `10a_k` from `Z''_k` to `Zᶜ`;
the stated `5a_k/4` neighbourhood inside `Z^{∼−8}`; the inclusion
`Ω_{i+1}⊂(Z'_i{}^{∼5})ᶜ`; and the filing rule for cubes meeting the collar.
The geometric supply of these facts is not reproved here.
We use the lemma's conclusions (a)–(d), CA-I:54717–54748, as a named
conditional input on those premises, not as a fact about arbitrary profiles.

Write `Π` for the prepared system and `Π°` for the companion. For stage
`n+1`, `0≤n≤N−1`, put `j=h+n`. Here `N` is the number of preparatory
stages; in §5, `N` instead denotes the gauge-group rank, as in that source.
Use the source spaces `Ũ_k^{(n+1)c,Σ}(X)` and filing sets `𝔻_m`.
The weighted Wilson functional and norm are

\[
A(w,\mathbb U)=\sum_p w(x_-(p))\mathcal A_p(\mathbb U),\qquad
\|C\|=\sup_m\sup_{\square\in\pi_m}
 \sum_{X\ni\square,\,m(X)=m}\|C(X)\|_\infty e^{a_m d_m(X)}.
\tag{A10.1}
\]

Here `π_m` partitions into cubes of side `Mu_m`. The filing level is the
least `m≥j+1` with `X⊂Ω_{m+1}ᶜ`; admissible terms also meet `Ω_m` and
`R_n`. These are CMP 122a (1.63), written at CA-I:54339–54353.
The plaquette functions use their holomorphic complexification; `Re tr`
on real group fields is not extended as an antiholomorphic operation.

### 2.2 Statement

Under §2.1, at every indicated stage:

(a) `ℂ_k^{(n+1)}=Σ_X ℂ_k^{(n+1)}(X)`, with the filing conditions of
CMP 122a (1.63).

(b) Each term is a restriction of a holomorphic function on
`Ũ_k^{(n+1)c,Σ}(X)`. Its dependence on `(𝕌,𝕁)` and exterior fluctuations
is confined to `X`.

(c) `‖ℂ_k^{(n+1)}‖≤C₀=c_G(d,L,M)+1`. With schedule parameter `β` from
`4.4:def-post-step-space` and glossary decay parameter `κ`,

\[
a_k=(1+3\beta)\kappa,\qquad
a_m=\begin{cases}(1+3\beta)\kappa &(F_m),\\
(1-\beta)\kappa &\text{otherwise},\end{cases}
\quad j+1\le m\le k-1.
\tag{A10.2}
\]

(d) For `X∈𝔻_m`,

\[
|\mathbb C_k^{(n+1)}(X,(\mathbb U,\mathbb J))|
 \le C_0e^{-a_m d_m(X)}.
\tag{A10.3}
\]

At `m=k`, or lower levels satisfying `(F_m)`, this has rate
`(1+3β)κ` and coefficient `c_Ω=1` in `4.18:rem-required-bound`.

(e) The accumulated terms satisfy

\[
\sup_x\sum_{i\le n+1}\sum_{X\ni x}\|\mathbb C_k^{(i)}(X)\|_\infty
 \le3(N_0+3)C_0.
\tag{A10.4}
\]

(f) There is a split `ℂ_k^{(n+1)}=ℂ_G+ℂ_I` with

\[
\|\mathbb C_G\|\le c_G,\quad
\|\mathbb C_G-\mathbb C_G|_{(1,0)}\|\le\vartheta,\quad
\|\mathbb C_I\|\le K'_S(N_0+8)C_0\vartheta\le1.
\tag{A10.5}
\]

For `n+1≤N−N₀`, the prepared and companion terms agree term by term.
For later stages, their differences are precisely
`A((e_{n+1}−e_n)1_□,U_k^{(n+1)})`, filed as single-cube terms.
Here `e_n=x_Π^{(n)}−x_{Π°}^{(n)}` is the profile excess, not vacuum energy.

### 2.3 Proof on the companion-system route

First run the companion with admissible profiles `φ°_A` at every stage.
Its stage-zero counterterms carry those same profiles. H-PROFILE-CLASS
allows H-STAGE at each successive stage. Its base and inductive bounds
therefore give the same `C₀` throughout this finite run. We do not infer
H-PROFILE-CLASS by inspecting the theorem's conclusion.

**(filled: compensation and the logarithm).** Let `F_n` be the full stage
action. It is common at zero by H-RECURSION. Suppose it is common at `n`.
The interaction bracket is the difference between the shifted and unshifted
values of `F_n+g_j^{-2}A`. Hence the two brackets coincide. All other
integration factors coincide by H-RECURSION, so the fluctuation integrals
`I_{n+1}` coincide. Use the logarithm furnished by the same convergent
expansion and its fixed normalization in H-STAGE. Equality of integrals
alone would leave an additive `2πiℤ` ambiguity for arbitrary logarithms;
this common series fixes it. The recursion gives

\[
F_{n+1}=F_n(U_k^{(n+1)},0)+E_0^{(j)}+\log I_{n+1},
\]

which is common. Induction proves equality of the full actions and
fluctuation integrals at all stages. Subtracting their Wilson/non-Wilson
splits gives

\[
\mathfrak E_\Pi^{(n)}-\mathfrak E_{\Pi^\circ}^{(n)}=A(e_n,\cdot),\qquad
\mathbb C_\Pi^{(n+1)}-\mathbb C_{\Pi^\circ}^{(n+1)}
 =A(e_{n+1}-e_n,U_k^{(n+1)}).
\tag{A10.6}
\]

This is the proof of the profile-independence implication needed here,
on CA-I:54495–54600's recursion route.

Let `ℂ_G(X)+ℂ_L(X)` be the companion's localized logarithm. Assign each
fine plaquette to the unique cube in `π_{j+1}` containing its base point.
Linearity in `w` gives

\[
A(w_{n+1},U)=\sum_{C\in\pi_{j+1}}A(w_{n+1}1_C,U).
\]

Define the prepared family by adding this cube term to `ℂ_G(C)+ℂ_L(C)`.
For other `X`, retain `ℂ_G(X)+ℂ_L(X)`. The common outer-ramp part at the
last stage keeps its companion filing. H-WEIGHT files every additional
cube meeting the excess support at `m=j+1`, meeting `R_n`, with
`d_{j+1}(C)=0`. The companion filing and this extra filing prove (a).

H-STAGE supplies holomorphy and local dependence of the first two
summands. The third is a finite sum of holomorphic plaquette functions
whose plaquettes are assigned to `C`. Its pullback uses the same local
response map and admitted domain as H-RECURSION. Thus it has exactly the
same local reading as the stage theorem's cube term. This proves (b).
No holomorphy is inferred from positivity at real fields.

H-WEIGHT gives `|w_{n+1}|≤β_{j+1}`, just as for the companion. Consequently,
on the stage theorem's stated enlarged spaces,

\[
\|A(w_{n+1}1_C,\cdot)\|_\infty
 \le\beta_{j+1}(LM)^4\,4(2\widetilde\alpha_0+\widetilde\alpha_1)^2
 \le\vartheta.
\tag{A10.7}
\]

The second inequality is an explicit H-STAGE input, not proved here.
The first follows from that input's plaquette bound and the weight supremum.

**(filled: the norm of the cube family).** At a fixed filing level and
fixed cube, only that cube's new singleton can occur in (A10.1).
Its exponential weight is one since its tree size is zero. Its norm is
therefore at most the supremum in (A10.7), with no factor counting all
cubes of the torus. Termwise triangle inequalities in (A10.1) now give

\[
\begin{aligned}
\|\mathbb C_k^{(n+1)}\|
&\le\|\mathbb C_G\|+\|\mathbb C_L\|+\vartheta\\
&\le c_G+K_L(\mathfrak s+\mathfrak p_j+\mathfrak l_j)M^q
 e^{C_2\kappa_1+4\sqrt d(2+4\beta)\kappa}+\vartheta
\le c_G+1.
\end{aligned}
\tag{A10.8}
\]

The cluster bound and final smallness inequality are H-STAGE under
`(K),(Q⁺),γ≤γ₀`. Its rate-selection step supplies (A10.2). Singleton
terms do not alter the rates. This proves (c).

For (d), select one cube of `X` in the supremum defining the norm.
The sum there has nonnegative summands, including
`‖ℂ(X)‖∞e^{a_md_m(X)}`. Bound that summand by `C₀` and divide by the
positive weight. This proves (A10.3), including the qualified strong rate.

For (e), apply the H-STAGE cumulation clause to the prepared families.
Its inputs are the bound `C₀` at every earlier stage and intersection
with that stage's collar. These have just been established in (c) and (a).
Its conclusion is exactly (A10.4). The factor `3(N₀+3)` is inherited
from that named lemma; this port does not silently prove its geometric count.

For (f), keep the companion's `ℂ_G`. Put `ℂ_I=ℂ_L` plus the filed cube
family, including the common outer ramp. The Gaussian bounds are
H-STAGE's two Gaussian estimates. Its sharper interaction estimate reads
the cube family only through its support, filing and (A10.7). These are
unchanged, so it gives the third estimate in (A10.5). This sharper estimate
is a separate H-STAGE input, not a consequence of `‖ℂ‖≤c_G+1` alone.

Finally `4.18:eq-coupling-excess-d`, CA-I:54135–54143, gives zero excess
increment when `j+1≤k₀`, equivalently `n+1≤N−N₀`. Equation (A10.6)
then gives termwise equality using the common localized logarithm.
For `j+1∈I_M`, (A10.6) and the plaquette partition give exactly the stated
single-cube differences. This proves the last assertion.

**A10 standing.** The transfer implication is ported. H-STAGE,
H-PROFILE-CLASS, the integration structure and geometric weight supply
remain hypotheses. In particular, CMP 122a (1.60)–(1.70) is not discharged.

## 3. A15: the torus-independent number of steps

**Source:** `4.38:cor-step-count`, CA-I:60810–60838;
proof CA-I:60841–60878. Unqualified heading: **proved implication**.
The seven antecedents are explicitly invoked at CA-I:60812–60813.

### 3.1 Antecedents and exact definitions

**H-TORUS** consists of all seven A14 hypotheses, CA-I:58188–58216:

1. Localized independence `4.4:cor-localised-independence` and whole-lattice
   interior sufficiency `4.4:lem-interior-sufficiency`.
2. The averaged-Laplacian walk expansion on its base class, determination
   by the data on each walk footprint, and the accompanying single-cell lemma.
3. Reflection and permutation covariance for that expansion, and the
   covariance clause of `4.4:def-one-family-hypothesis` for the other
   operators of `𝕃₁`.
4. The operator bounds at free current.
5. The large-field contribution to the coupling increment.
6. The large-field representation and bound, all six format clauses,
   CMP 122b p.390's new-region description, the near-exterior-island clause,
   cell rounding of the prepared sequence, the accompanying format lemma,
   and the further format clauses used there. Also convergence and analytic
   extension on joined domains, CMP 122a p.192 (1.70) and CMP 122b p.377
   (1.68)–(1.69). The unused clauses of that further statement are not assumed.
7. Locality of label creation/change and the free-interior-bond integrand
   clause of `4.38:def-standing-data`.

P7 is the checked port of A14 from these inputs, with its previous-level
hypothesis `(H_j)`. It is not their unconditional supplier.
P5 supplies the conditional flow argument from its own A12 assumptions.
Name its actual increment and continuation bounds **H-FLOW** here:
the increments can be formed while `x_i≥γ⁻²`; the new inverse coupling is
positive; and the two-sided drift bound holds through the levels formed,
with `λ♯>0`, `B♯>0` and defect `c₅`. This is not strict monotonicity.
In formulas, the retained drift bound is
`λ♯(j−i)−c₅≤x_i−x_j≤B♯(j−i)` for all formed `i≤j`;
the case `j=i+1` supplies the one-step upper drop used below.

Theorem 0's parameter setting is retained: `d=4`, `SU(N)`, `N≥2`;
odd `L≥L₀(N)`; the ordered auxiliary choices; `0<g≤γ_H`;
`γ_H≤(γ⁻²+c₅+1)⁻¹ᐟ²`; and `0<g₀≤g₋(g)`.
The definitions at CA-I:632–680 and 57027–57092 give

\[
\begin{gathered}
x_j=g_j^{-2},\quad x_j=x_{j-1}-\beta_j,\quad
g_-(g)=(g^{-2}+B_\sharp)^{-1/2},\\
K=\min\{j\ge0:x_j\le g^{-2}+B_\sharp\},\\
R(g')=\min\{L^i:i\in\mathbb Z_{\ge0},\ L^i\ge(\log g'^{-2})^r\},\qquad
m_{\mathbb T}(g')=11+m'+\log_LR(g'),\quad M=L^{m'},\\
s_j(m,K')=2L^{m+K'-j},\\
\mathcal S_j=\{(m,K'):K'\ge j,\quad
 L^{m+K'-i}\ge L^{11}M\check R_i\ (0\le i\le j)\},\\
\mathcal S_j^\flat=\mathcal S_{j-1}\cap\{K'\ge j\}\quad(j\ge1).
\end{gathered}
\tag{A15.1}
\]

**H-CELL** retains the two comparisons taken by statement at
CA-I:57122–57129:

\[
\check R_K\le R(g_-(g)),\qquad
\check R_i\le L^{K-i}\check R_K\quad(0\le i\le K).
\tag{A15.2}
\]

The additive constant `E` is zero while the site-wise induction runs.
The source fixes it afterwards at the Theorem 0 sites. Its use requires
**H-HOM**: T is linear, R is homogeneous of degree one, and the construction
choices and extracted terms do not read `E` (CA-I:57047–57053).
The precise vacuum convention used for stability is set in §5.

### 3.2 Statement, parts (a)–(f)

(a) Starting from `g₀`, the increments of `4.2:def-increment` generate
`g₁,g₂,…` without any choice of site `(m,K')`, as long as `x_k≥γ⁻²`.

(b) `K(g₀,g)` is therefore site-independent, in particular independent of `m`.

(c) If `K'=K` and `m≥m_T(g₋(g))`, then

\[
(m,K)\in\bigcap_{j\le K}\mathcal S_j.
\tag{A15.3}
\]

The `K` steps at that site subtract exactly the common increments `β_j`.

(d) After those steps, `E`, initially zero at every site, is fixed by
Theorem 0's condition at `(m,K)`.

(e) `K` is a well-defined nonnegative integer. The physical-torus run
produces the couplings constructed before choosing a torus, the last
torus-identification assertion of clause (0).

(f) The auxiliary tori called item `(A7)` of the cell-size-multiplier
statement in the source are covered by the same site-volume-independence
assertion. Their admission at the levels used is retained as **H-AUX**.
The reference `(A7)` at CA-I:60836–60837,60876–60877 supplies no new
estimate; this port does not infer admissibility of an arbitrary small torus.

### 3.3 Proof

At zero the bare coupling is fixed before a site. Suppose
`g₀,…,g_{j−1}` and all earlier extracted increments are site-independent.
P7's `4.38:prf-increment-site-free` deduction then forms the real number
`β_j` from those couplings and fixed parameters. Its construction uses
the complete regular part, including the Gaussian normalizer and the
fluctuation logarithm with aged R-remainders, as defined at
CA-I:3764–3825. It does not substitute the small-field term alone.
H-FLOW gives `x_j>0`; thus `g_j=x_j^{-1/2}` is unique and site-independent.
The prescribed cell multiplier and the inequalities defining `𝒮_j`
are then site-independent. This proves (a) by induction.

**(filled: no site or stopping-time circle).** For fixed `K'≥j`, each
condition in `𝒮_j^flat` is a lower bound on `m`; there are finitely many.
Choosing `m` above their maximum gives an auxiliary site before `Ř_j`
is known. Its torus side tends to infinity with `m`. The extraction at
level `j` therefore uses `𝒮_j^flat`, built only from previous data.
Only after extraction are `x_j,Ř_j,𝒮_j` formed. No value of the eventual
first-passage index enters that order.

The set whose minimum defines `K` depends only on the common sequence
and `g`. This proves (b), once its nonemptiness is checked.

**(filled: existence of first passage).** Put `T=g⁻²+B♯`. If `x₀≤T`,
then `K=0`; the initial condition `g₀≤g₋(g)` forces `x₀=T>g⁻²`
in this case. Otherwise every index before a passage obeys
`x_j>T>γ⁻²`, so H-FLOW permits the next extraction.
If no passage occurred, choose an integer
`n>(x₀−T+c₅)/λ♯`. The lower drift bound gives
`x_n≤x₀−λ♯n+c₅<T`, a contradiction. Such an integer exists by the
Archimedean property. At a nonzero first passage, the upper one-step
drop bound gives `x_K≥x_{K−1}−B♯>g⁻²≥γ_H⁻²≥γ⁻²`.
Thus the terminal step remains admitted. This is P1's first-passage
arithmetic on H-FLOW's actual bounds, without an assumption that each
increment is positive. The minimum of a nonempty subset of the
nonnegative integers exists. This proves the integer assertion of (e).

For (c), the volume assumption says `L^m≥L¹¹MR(g₋(g))`. For
`0≤i≤j≤K`, H-CELL gives

\[
L^{m+K-i}\ge L^{11}M L^{K-i}R(g_-(g))
 \ge L^{11}M L^{K-i}\check R_K\ge L^{11}M\check R_i.
\]

Also `K≥j`. These are all conditions of `𝒮_j`, proving (A15.3).
The site-wise step and the common extraction agree by P7. Induction
over the `K` steps proves the remaining assertion of (c) and (e).

For (d), choose the prescribed `E` at this site after the run. For a
positive scalar `a=e^{-E}`, H-HOM gives
`(RT)(aρ)=a(RTρ)` and, by induction, `(RT)^k(aρ)=a(RT)^kρ`.
The extracted increments and geometrical choices stay fixed. Thus
setting `E` later means applying one scalar to the whole finite run.
It is not a new normalization inserted at each step.

Finally P7 quantifies over every admitted site. Apply it to each
auxiliary site of H-AUX at the levels used there. This proves (f).
Nothing in this argument removes H-TORUS, H-FLOW, H-CELL or H-AUX.

## 4. A17: the inductive representation

**Source:** `4.20:thm-representation`, CA-I:61095–61206.
Its unqualified heading declares a proved statement. CA-I:61208–61210
places its proof in the following sections, within the joint induction
of (0) and (i). CA-I:3573–3632 and 166702–166709 specify that order.
This is a **conditional assembly port**. It does not turn the many cited,
printed, incomplete or outstanding suppliers into proofs.

### 4.1 Exact representation and statement

Use Theorem 0's `(H1)`–`(H6)`, CA-I:1126–1182, and the choices in
`4.20:not-representation`, CA-I:60940–61064. Thus `d=4`, `G=SU(N)`,
`N≥2`, with the parameter and volume conditions of §3.1.
For completeness, **REP-PARAM** means all six conditions as follows:

1. **(H1)** Pure `SU(N)` Wilson theory in four dimensions, with
   `A(U)=Σ_p[1−Re tr U(∂p)]`, on the periodic torus of side `2L^m`
   and spacing `L⁻ᴷ`. The source asserts (0),(i) for `N≥2`; its
   general-rank passage still needs the two unproved Chapter 4
   statements. Its claims (ii)–(vi) at `N=2` do not supply them.
2. **(H2)** `L` is odd and `L≥L₀(N)`. The single existential floor
   `L₀` is fixed once, not assigned a numerical value. Every condition
   on `L` is a lower bound reading only the finite pre-`L` data.
3. **(H3)** Balaban's auxiliary parameters are chosen in the fixed
   order of `2.3:not-stages-first`, `not-stages-middle`, and
   `not-stages-last`: the decay constants, cube sizes, action constants,
   analytic radii, increment bound and type-I cutoffs, among others.
   Each is either determined by earlier choices, one-sided bounded
   by a positive function of them, or in one of the finitely many
   nonempty windows. In particular `M₁<M₂=L²M₁<M=L^{m′}`.
   Then choose `γ`, then `γ_H≤(γ⁻²+c₅+1)⁻¹ᐟ²`, with `c₅=2c₂`.
   There is no upper bound on `L,M,M₁,κ,κ₁,q,p₀,K,m`, age, depth
   or step count, and no positive lower bound on a coupling.
   Writing `M₁=L^{m′₁}`, `M₂=L^{m′₂}`, the integers `m′₁`,
   `m′₂−m′₁`, `m′−m′₂` are fixed before `L` and independent of it.
   The detailed one-sided inequalities and windows in those order
   tables remain named parameter-admission hypotheses; we do not
   prove their simultaneous consistency here.
4. **(H4)** `0<g≤γ_H`.
5. **(H5)** `m≥m_T(g₋(g))`, with exactly the definitions (A15.1).
   This is solely a lower volume condition.
6. **(H6)** `0<g₀≤g₋(g)`, with `K` the first passage (A15.1)
   and no lower bound on `g₀`.

The extra source condition (H7) belongs to the correlation clauses
and is not added to A17; its admitted-source setting is retained
separately by H-SOURCE-IND in §6. The source itself identifies
`2.4:prop-m-freeness` as incomplete at `(*)`, CA-I:1202–1205.
The source defines `ρ_k=(RT)^kρ₀`, with its creating-step split included.
The symbol `ρ_k dV_k` denotes a measure; live second-class gauge slices
need not have a Haar density.

For a label `𝒮`, set

\[
\begin{aligned}
A_{k,\mathcal S}(x_k,U_k)
 &=-A(x_k(\cdot),U_k)+\mathbf E_k(U_k)+\mathbf R_k(U_k)
       +\mathbf B_k(U_k,\underline\eta)-E_k[\mathcal S],\\
\mathbf E_k(U)&=\sum_{j\le k}\sum_{X\subset\Lambda_j}
       [\mathbf E^{(j)}(X,U)-\mathbf E^{(j)}(X,1)],\\
\mathbf R_k(U)&=\sum_{j\le k}\sum_{X\subset\Lambda_j}
       [\mathbf R^{(j)}(X,U)-\mathbf R^{(j)}(X,1)].
\end{aligned}
\tag{A17.1}
\]

The domains in the sums belong to `𝒟_j`. Other terms, including
R-made terms outside those interiors, enter `𝐁_k` without subtraction.
The variables `η̲` are stored earlier fluctuations, integrated by the
large-field operations. The exact measure representation is

\[
\rho_k\,dV_k=\sum_{\mathcal S}\mathbf T'_k(\mathcal S)
 [\chi_{k,\mathcal S}\exp A_{k,\mathcal S}(x_k,U_k(V_k))]\,dV_k.
\tag{A17.2}
\]

Labels are the admissible large-/small-field histories. On an unoperated
component, `𝐓'_k(𝒮)` uses the prepared `𝐓''_k` of CMP 122b (1.72).
On an R-operated component it uses (1.71), including CMP 122a (1.82),(1.88)
preparation tests and the singular second-class gauge factors. Its bounds
include CMP 122b (1.73),(1.79),(1.89). This is the precise content of
CA-I:61046–61063, not an arbitrary positive-kernel replacement.

The source theorem asserts the following for every `0≤k≤K`.

**(a)** Representation (A17.2) holds, with the inductive hypotheses and
bounds of CMP 119 §2, subject to these exact qualifications:

* CMP 119 (2.47) is excluded.
* The pointwise upper member of (2.50) is replaced by the integrated
  bound of A19, `∫ρ_k dV_k≤exp(E₊N_k)`.
* CMP 119 (2.48) and Theorem 2 use the modified forms stated later in
  the account. Other altered displays are read in their stated use-site forms.

Every localized term created at `j≤k` has a domain `X∈𝒟_j`, is gauge
invariant, and reads the background only on `X`. It is analytic on
`U_j^c(X,α₀,α₁)` and, except for (b), has bound
`const·exp(−κd_j(X))`. Fresh terms have bounds on the enlarged spaces
with rate `(1+4β)κ`. Here the unindexed `β` is the schedule parameter,
not a coupling increment.

`U_j^c` means the **one-power hereditary class**. Restriction to subregions
made from finer cubes is an identity in that class. It contains the
hereditary reading of CMP 109 (1.11)–(1.16), under either tower rule:
the maximal tower of CMP 109 or the sequence of CMP 119 (2.13).
Every member of each tower carries regularity of its constrained minimizer
and a collar of two layers of its own cubes. Analyticity therefore holds
on those hereditary Balaban domains. Reproduction of this class is an
induction input, not a consequence of restricting a single complex domain.

**(b)** Exceptions are boundary terms whose localization domain contains
a live second-class region. Write `Z=⋃_iY_i` for those regions.
For a new R-born boundary term at step `j`, whose domain contains no
older still-live second-class region, CMP 122b (1.99) gives

\[
|\mathbf B'^{(j)}(X,(\mathbf U,\mathbf J))|
 \le O(1)c_1 e^{-(1+\frac12\beta)\kappa d_{j,Z}(X)},\qquad
c_1\in\{e^{-p_0(g_j)},\alpha^{1/3}\}.
\tag{A17.3}
\]

`𝐁'` is a boundary term, not an operation. `α` and `β` in (A17.3)
have the meanings of CMP 122b; `α` is not an analyticity radius.
The remaining two kinds are later T-/R-descendants while the region
stays live, and new terms whose domains contain an older live region.
Each has bound `C exp(−c d^θ(X))`, with `c>0` and constants as in (c).
Here `d^θ(X)≤d_{j,Z}(X)`. No reverse comparison is asserted.
Decay in `d_{j,Z}` itself is claimed only in the case (A17.3).

**(c)** Constants depend on `L,𝔭,γ,N`, and on the scale only through
`g_k`, except for the explicitly two-scale factor

\[
\varpi_{jn}=\max\{1,(x_j/x_n)^2\}
           =\max\{1,g_n^4/g_j^4\},\qquad j\le n.
\tag{A17.4}
\]

It occurs in the modified CMP 119 (2.44), Theorem 2 bounds and their
descendants. The flow gives `x_n≤x_j+c₅` and the threshold gives
`x_j>g⁻²≥γ_H⁻²≥γ⁻²+c₅+1>c₅`. Hence `x_n≤2x_j` and

\[
g_j^{\kappa_0}\varpi_{jn}\le4g_j^{\kappa_0-4}g_n^4.
\tag{A17.5}
\]

No constant, including `varpi`, depends on `K,m`, position, or `g₀`
except through the indicated running couplings.

The assertions above reproduce the mathematical statement at
CA-I:61095–61206. For its integrated upper member, and wherever the
vacuum-energy conclusions are used, `ρ` must have the common convention
specified in §5.2. That is an explicit **(correction)** to its Chapter 1
bare-density reading, not a change to a normalized observable.

### 4.2 Expanded antecedents: the joint induction

The theorem has no self-contained list of antecedents beside its heading.
The following list separates the inputs hidden by its cross-references.
Each named item means the cited statement **with every hypothesis and
its actual source domain**, not a stronger version suggested by its title.
Unproved suppliers stay assumptions even when a later implication is proved.

| Name | Required input and role | Standing retained |
|---|---|---|
| REP-PARAM | `(H1)`–`(H6)`, the ordered floors/ceilings and nonempty windows, and admissible cell geometries | Theorem 0 setting, CA-I:1126–1205. Consistency and `2.4:prop-m-freeness` are not proved by choosing symbols. |
| REP-BASE | Bare Wilson density, extended Borel block map, background/minimizer definitions, exact creating split and actual R reference laws | CA-I:841–944,60940–60964; algebraic base below, with analytic/map supply retained. |
| REP-FLOW | Small-field step; widened cube-gauge condition and its reproduction; finite one-loop law and unmarked bound; large-field increment; localized independence; operator bounds; large-field representation; hereditary class; torus independence | All items (a),(a′),(b)–(h) of A12, CA-I:56424–56441, plus earlier-level representation only. P5 and P7 port the conditional deductions. |
| REP-BASEPOINT | Local real base `4.4:prop-local-real-base`, with its hypotheses | Source outstanding at CA-I:8373; refereed LRB supplies its stated implication. |
| REP-OPERATORS | `4.5:thm-operator-bounds` and `4.14:thm-operator-theorem`, including data admission and actual-use membership | Checked P4; its own named premises remain. Uniform increment is supplied by refereed UI on its stated scope. |
| REP-MINIMIZER | `4.13:lem-minimizer-unique` and `4.13:lem-own-constant` | Source outstanding, CA-I:45163,45204; refereed MU and OC respectively, with their regular/continued meanings and hypotheses. |
| REP-PREPARED | Prepared-nest geometric admission, separate next-step condition (A2), profile-compatible stage data and domain membership | Refereed PDA supplies (A1), not (A2) or arbitrary analytic admission. P4 retains both separate demands; CA-I:45557–45634,49495–49546. |
| REP-BOUNDARY | A10 and the Wilson-term/action-domain estimates at the preparation | A10 is §2, conditional on H-STAGE and the other §2 inputs. `4.18:thm-action-domain`, CA-I:56123–56279, retains all its listed inputs. |
| REP-RF | The relative small-field machine, `(RF)_k⇒(RF)_{k+1}`, including its one-run/two-run and source variants | `4.21:prop-relative-machine`, CA-I:61212–61325, explicitly outstanding at 61325. Expanded below. |
| REP-KEPT | Geometry of live pockets; kept members as data; probe contribution; stage totals; foreign-operation behavior | `4.22:not-live-region-geometry`, `def-kept-term-reader`, `lem-probe-summand`, `prop-stage-totals`, `prop-foreign-operation`; source/supplier distinctions below. |
| REP-STAGE | Stage-domain estimates, survivor-block expansion, density/gauge bounds and norm conversion | Sections 4.23–4.24, with holonomy and field-dependence inputs below. These are not supplied merely by P4's free-current operator theorem. |
| REP-DISSOLVE | Gaussian-piece continuation/oscillation, non-deep-piece bounds and dissolution | Section 4.25, including its incomplete lemmas. Needed when a live piece is changed or removed. |
| REP-INHERIT | Substitution, nesting, source-room and inheritance statements on the actual stored domains | Section 4.26; earlier-level estimates do not by themselves imply new-domain membership. |
| REP-ARREST | Arrested spaces; stage-map, descent, stored-term/room-table, R-layer, T-step, keystone, post-arrest and localized change-of-variables inputs | `4.27:thm-arrest-theorem`, CA-I:137628 onward, explicitly incomplete. In particular its two unasserted raw-point loci are retained as missing supply, not covered by its partial conclusions. |
| REP-CORE | `4.28:prop-core-freezing` with (i)–(vii), especially near-pair sum lemma (e) | CA-I:146051–146113 is a conditional statement. Its input `4.28:lem-near-pair-sums` (e) is incomplete. The closing list's description of core-freezing as incomplete does not close that input. |
| REP-COVER | `4.29:cor-cubewise-analysis` with all nine assumptions | CA-I:151575–151654. Expanded below; includes the printed cover-transfer sentence, not proved by the corollary. |
| REP-COUNT | Stratified-frame counts at `a=δ₀/32` and attached-object bounds | `4.30:prop-frames-instance`, CA-I:153174–153223, assumes (a)–(h), including incomplete `prop-cell-counting`. Boundary nonpinch/width hypotheses remain. |
| REP-POS | A18, `4.32:prop-positivity-dichotomy`, all clauses (a)–(d5) | Explicitly outstanding at CA-I:156837,156953. Open `R_V` in PD is not solved. |
| REP-STABILITY | A19's (h2)–(h11), in addition to the structural representation and REP-POS | Used after structural induction, not to prove that same structure. §5 ports the implication and its normalization correction. |

**REP-RF expanded.** The terms covered are T-/R-born boundary terms,
live frozen chain terms, chain terms inside R, and interrupted-preparation
change-of-variables terms. A term kept under T′ on an entire pocket strip
is a separate kept member. For each covered term `F` of level `j≤k`:

* `(f0)` it has one scaffold label `A_F∈𝐃_j` meeting `Ω_j` and
  `Z_j^boxplus` (the latter is waived when pockets occur), finitely many
  live pockets `(Y,m)` with `m≤j` touching `A_F`, and at most one term
  per kind/domain/history;
* `(f1)` its true support is `X_F=A_F∪⋃Y^sharp`; it reads configuration,
  current and further source data only there, and `w` only in `X_F^+`;
  its stored domain has the specified radius-`ε_k` orbit datum and lies
  in its kind's analyticity space;
* `(f2)` the actual norm is taken on that stored domain. Fresh boundary
  terms have `B₀exp(−κ_out d_j(A_F))`, `κ_out≥2κ`; stored ones have
  `B₀exp(−κd_j(A_F))`. R-born terms have
  `C c₁(g_j)exp(−(1+β_s/4)κd_j(A_F))≤B₀exp(−κd_j(A_F))`.
  Chain norms are bounded by `C₀^sharp`, with top rate `8κ/5` and
  lower rate `4κ/5`. Interrupted changes have their separately stated bound;
* `(f3)` the label/pocket list depends on the scaffold, not the source,
  and is common to two runs and their difference;
* `(f4)` `A_F` has a cube in the first enlargement of `Z_j^boxplus`.

The transition also needs decoupling of sources, tubes about live
regions, labels/bounds for interrupted changes, persistence of near-group
weights for one and two runs, and orbit-data supply on stored domains.
The last two are explicitly unproved at CA-I:61304–61310,61345–61349.
The output-radius loss is retained separately for T/R and preparation.
There is no claimed bound on `d_j(X_F)` from these label-domain estimates.

**REP-CORE expanded.** Its seven inputs are: the displayed parameter
floors and full box-lemma/near-pair-box hypotheses; arrested-piece
statements including removal upon completion; box clauses on `𝔗` for
data in and outside the run; clauses on `Z^on` when no lifted point is
met; near-pair sums including data outside the run; matching of the
actual near pairs, their boxes inside `Y`, and the window envelope
`R_n≤Ř`; and near-pair sum bounds (c)–(f), with (e) still incomplete.
In particular its conditions include `R_min≥5L`, `L≥12`, `M≥3L`,
`2≤L₀`, `L₀²≤L/3`, `δw≥16 log L+4`, `β₀=1/7`,
`(N₀+1)(N₀+3)≤N` at each attempt, and `g_n²β'≤1` where required.
The `N` here is that preparatory attempt parameter, not gauge rank.

**REP-COVER expanded.** Its nine inputs are: native-cover clauses
(a)–(h″); exact cube localization; near-field scope; native-scale
window-minimizer clauses (d1),(d2); complex hypotheses (K1)–(K3) and
their inclusion; scale/window-rim thresholds; all transfer inputs in
`4.29:rem-transfer-inputs`; CMP 119 p.276's transfer of CMP 109 §§3–4
to that cover, read with native level `n↦s`; and the domain/radius
sequence conditions plus the minimizer restriction lemma.
The good-cube case uses the full local family and restriction identity.
The remaining level-`j` cubes use only CMP 109 (3.6)–(3.17), without
a gain `L^{j−s}` or a minimizer chain. Neither case supplies the printed
transfer premise.

### 4.3 The published-input and open-input frontier

These are named hypotheses, not proofs imported by reputation.
The following expands **all entries** of the joint (0)/(i) published
lists at CA-I:166563–166648. Repeated entries are identified, not counted
twice. Each formula or theorem retains its own hypotheses.

| Named published input | Exact Balaban locus |
|---|---|
| B95-profile | CMP 95 (1.118). |
| B96-profile | CMP 96 p.229 (2.36), cover profiles and partition of unity. |
| B96-L21, B96-L24, B96-P26, B96-P27 | CMP 96 Lemmas 2.1, 2.4; Propositions 2.6, 2.7, respectively. |
| B98-P1 through B98-P7 | CMP 98 Propositions 1, 2, 3, 4, 5, 6, 7, separately. |
| B99a-L1, B99a-T2, B99a-T4, B99a-P6 | CMP 99a Lemma 1; Theorems 2, 4; Proposition 6, pp.98–99. |
| B99a-action | CMP 99a (1.19), p.79. |
| B99b-T31,T32,T33,T34,T37,T39,T310,T311,T312,T313,T314,T315 | CMP 99b Theorems 3.1, 3.2, 3.3, 3.4, 3.7, 3.9, 3.10, 3.11, 3.12, 3.13, 3.14, 3.15, separately. |
| B99b-C35,C36,C38 | CMP 99b Corollaries 3.5, 3.6, 3.8, separately. |
| B102b-T1,P3,P9 | CMP 102b Theorem 1, including (7)–(9), p.279; Propositions 3 and 9. |
| B109-T1,T3,L4,L5,L6 | CMP 109 Theorems 1 and 3; Lemmas 4, 5, 6. |
| B109-derivatives | CMP 109 (3.37)–(3.50). |
| B116-L1,L2,L3 | CMP 116 Lemmas 1, 2, 3. |
| B119-T1,T2,C3 | CMP 119 Theorems 1 and 2; Corollary 3, with the upper bound used only after integration. |
| B122a-P1 | CMP 122a Proposition 1. |
| B122b-T1,P1 | CMP 122b Theorem 1, pp.355–356, and Proposition 1. The stage/representation application retains its actual domain hypotheses. |

The same lists also cite the following sentences **printed without
proof**. These remain separate named inputs:

| Name | Printed statement and locus |
|---|---|
| PRINT-PREP | Prepared large-field data admission, CMP 122a pp.178–179. PDA supplies its geometric (A1) instance, with the distinction in §4.2. |
| PRINT-COVER | Repeating CMP 109 §3, Lemmas 5–6 on CMP 119's cover, CMP 119 p.276. |
| PRINT-TOWER0 | Lowest two tower regularity conditions, CMP 99b p.396 (3.35),(3.37). |
| PRINT-LOCAL | Locality of interactions, CMP 122b p.379. |
| PRINT-COMPLEX | Complex-pair reading of the inclusion CMP 109 (1.17). |
| PRINT-CURVATURE | Near-data extension of CMP 109 (3.26)–(3.28), p.277. |
| PRINT-INVERSE | Covariance-inverse bounds and walk expansion, CMP 99b §3 before (3.132). |
| PRINT-WALKS | Further operator walks, CMP 99b §3 after Theorem 3.9. |
| PRINT-AVERAGE | Analytic averaging-derivative bounds, CMP 98 §E p.43. |
| PRINT-FAR-J | Second far-family current inequality, CMP 99b (3.49),(3.69). |
| PRINT-GAS | Bracket as a polymer gas, CMP 122b (1.90). |
| PRINT-MODIFY | Large-field bounds after the remaining modifications, CMP 122b p.386. |
| PRINT-LAYERS | Layerwise gauge clauses, CMP 122a (1.64)–(1.69), pp.190–191. |
| PRINT-CEILING | Layerwise ceiling from small coupling, CMP 122a p.192. |
| PRINT-OLD | Old terms beside a new large-field region, CMP 122b p.375. |
| PRINT-JOIN | Joined-domain extension/bounds, CMP 122a p.192 (1.70) and CMP 122b p.377 (1.68)–(1.69). |
| PRINT-BOUNDARY | Absolute boundary bounds and gauge invariance, CMP 122b (1.11),(1.23)–(1.48), p.369. |
| PRINT-SOLVE | Analytic solution of the equation, CMP 122b p.367 (1.40)–(1.41). |

The account's two open-input lists, CA-I:166615–166624 and
166650–166692, must also stay attached. They are expanded here rather
than hidden behind “the induction hypotheses.” The source list is not
an infallible census: a local implication can be proved while one of
its antecedents remains open.

| Name | Input retained and source standing |
|---|---|
| O-unmarked | `4.2:lem-unmarked`, CA-I:4031, incomplete. |
| O-reblock-in | `4.12:prop-reblocking-inside`, CA-I:44127, incomplete. |
| O-real-slots | `4.12:cor-real-factor-slots`, CA-I:44803: the list calls it incomplete; its local proof is conditional on reblocking and its hypothesis (b). Retain those inputs. |
| O-reblock-out | `4.12:prop-reblocking-outside`, CA-I:45085, outstanding. |
| O-minimizer, O-own-gauge | Source `4.13` leaves, CA-I:45162,45203; use refereed MU/OC only on their stated hypotheses. |
| O-positive | A18, CA-I:156837; all clauses retained, including open `R_V`. |
| O-volume | Volume counts named as a relative-machine input, CA-I:166652–166653. |
| O-data-1, O-data-2 | The two data bounds for the correlation proof, separately retained, CA-I:166654–166655. |
| O-kernel-difference | Relative-machine kernel-difference bound, CA-I:166656–166657. These last four prose inputs have no resolved supplier in `chain-ca.md` §5; this port does not invent one. |
| O-live-geometry | `4.22:not-live-region-geometry`, CA-I:85575: outstanding geometry, contour, cell, counting and anchor assertions. |
| O-kept-reader | `4.22:def-kept-term-reader`, CA-I:85720: the asserted label/norm/law-site supply reads O-live-geometry. A definition is not its geometric proof. |
| O-probe | `4.22:lem-probe-summand`, CA-I:86220: local conditional proof; retain kept oscillation, geometry and anchor hypotheses. Listed outstanding at 166662. |
| O-stage-totals | `4.22:prop-stage-totals`, CA-I:87328, incomplete. |
| O-foreign | `4.22:prop-foreign-operation`, CA-I:87631: conditional proof on presentation-site, kept-holomorphy/oscillation, probe and open geometry inputs; listed outstanding at 166664. |
| O-norm-conversion | `4.24:prop-norm-conversion`, CA-I:106533, outstanding. |
| O-field-dependence | `4.24:prf-field-dependence`, CA-I:106589, incomplete. |
| O-holonomy | `4.24:prop-holonomy-bound`, CA-I:107073, outstanding. |
| O-piece-oscillation | `4.25:lem-piece-oscillation`, CA-I:111188, incomplete. |
| O-dissolution | `4.25:prop-dissolution`, CA-I:115062, incomplete. |
| O-T-layer | `4.27:lem-t-step-layer`, CA-I:131633, incomplete. |
| O-weights | `4.27:lem-weights-heredity`, CA-I:132878, incomplete. |
| O-stage-cubes | `4.27:prf-stage-move-cubes`, CA-I:134184, incomplete. |
| O-density | `4.27:prf-density-increase`, CA-I:135143, incomplete. |
| O-current-probe | `4.27:lem-current-probe`, CA-I:135723, incomplete. |
| O-zero-margin | `4.27:prf-index-zero-margin`, CA-I:136192, incomplete. |
| O-ambient | `4.27:prf-ambient-inclusion`, CA-I:136490, incomplete. |
| O-arrest | `4.27:thm-arrest-theorem`, CA-I:137628, incomplete. |
| O-newborn | `4.27:prf-newborn-continuation`, CA-I:138485, incomplete. |
| O-live-bounds | `4.27:prop-live-piece-bounds`, CA-I:138933, incomplete. |
| O-raw-current | `4.27:rem-raw-current-radius`, CA-I:140297, incomplete. |
| O-zero-members | `4.27:rem-index-zero-members`, CA-I:140692, incomplete. |
| O-core | REP-CORE's missing near-pair-sum input, CA-I:146051–146113; listed under core-freezing at 166686. |
| O-two-sided | `4.30:lem-no-two-sided-point`, CA-I:152408, incomplete. |
| O-cell-count | `4.30:prop-cell-counting`, retained by REP-COUNT's (h), CA-I:153220–153223; the frames-instance is a proved implication. |
| O-N3 | Stability of the near action for `N≥3`, standing hypotheses at CA-I:164243 onward; incomplete according to 166690–166691. Not used at `N=2`. |

The list's Combes–Thomas covariance-decay entry is explicitly said **not
to be used in clause (i)** at CA-I:105181–105194. It is recorded, not
promoted to an extra A17 hypothesis. Conversely the missing local real
base, uniform increment, near-group persistence and stored orbit supply
are visible in §4.2 even though the summary lists omit them.
REP-DISSOLVE also retains `4.25:lem-gaussian-pieces` (110806) and
`lem-non-deep-pieces` (114658), and REP-ARREST retains
`4.27:lem-real-minimiser` (136809), all with their marked gaps.

This is an expansion of the named assembly frontier, not a claim that
every edge inside those long conditional inputs has been independently
checked. A local input whose complete proof is not written in this file
remains a named hypothesis with its transitive premises.

### 4.4 Proof: level induction, with the suppliers kept separate

The proof below is the account's assembly route. It proves the
implication from §4.2–§4.3. In particular it does not prove
REP-RF, the unasserted loci of REP-ARREST, or any printed Balaban sentence.

**Base.** At level zero, the history is empty and there is no stored
fluctuation. The action is the bare Wilson action, plus its one chosen
additive constant. The localized correction families are empty, so every
assertion about their domains, decay and live pockets is vacuous.
The normalized product Haar measure gives the finite Wilson integral.
Thus (A17.1)–(A17.2) have their level-zero meaning. Background/map admission
is REP-BASE, not inferred from the existence of the integral.
If the initial presentation already inserts a small-/large-field
partition, apply REP-BASE's exact finite partition to this bare term;
its summands have the same sum. This does not assume that the
never-large indicator is identically one.

**Inductive order.** Assume the structural representation, all its
individual term bounds, and the already established flow through level
`k`. Use the account's order at CA-I:3593–3613:

1. At coupling `g_k`, form the complete regular fluctuation action.
2. Extract `β_{k+1}` by P7 and apply the finite/unmarked/large-field
   estimates of REP-FLOW. They read only levels at most `k`.
3. Set `x_{k+1}=x_k−β_{k+1}`. P5's flow deduction gives positivity and
   the two-sided flow bounds. Then fix the cell size and the creating
   thresholds.
4. On an admitted step, perform T, preparation, R, and the localized
   exponentiation, in that order.

**(filled: the induction object).** The structural part of A17 means
its representation and local/domain/majorant clauses, without the
integrated upper bound quoted from A19. A19 is proved after that
structure is in place, using its separately listed (h1)–(h11).
Thus the occurrence of A19 in A17(a) does not make the local representation
depend on its own integrated conclusion. At an internal stage, only
completed earlier stages and levels are inputs. REP-INHERIT and
REP-ARREST have that stage/level order as part of their hypotheses.
CA-I:166702–166709 asserts this order; we keep the required input
admissions, rather than deriving them from that assertion alone.

**T and the creating split.** Apply the exact Borel push-forward of
REP-BASE to each old labelled measure. Inserting the finite creating
partition replaces each old term by the sum of its products with the
new indicators, since their sum is one. Append the chosen new regions
to the label. Their complete sum therefore represents exactly the
T-push-forward. The normalized gauge identities, changes of variables
and small-field step in B109-T1/T3 and B119-T1 supply its fluctuation
representation. No pointwise Haar density is required for a term that
already carries a gauge slice.

The actual data at a cover cube are admitted by REP-OPERATORS,
REP-MINIMIZER, REP-COVER and the widened-gauge clause of REP-FLOW.
Those are necessary **application hypotheses**, not consequences of
the phrase “small coupling.” At a good native-scale cube use
REP-COVER's full-family and minimizer-restriction clauses. At its other
cubes use its shorter CMP 109 (3.6)–(3.17) branch. The named small-field
bounds then give the fresh localized terms, their gauge invariance,
enlarged-space analyticity, and the fresh rate `(1+4β)κ`.
The one-power hereditary input carries the earlier families with the
ordinary rate. A pullback is taken only on the admitted stored domain.

**Preparations, including interrupted ones.** Apply §2 to each admitted
prepared component, using REP-PREPARED and REP-BOUNDARY. Its cumulative
bound controls the sum over all stages; multiplying the bound for one
stage by the total number of stages would not give the asserted constants.
For stored and interrupted terms, the precise analytic input used is
`4.26:thm-inherited-expansion`, CA-I:119813–119900. Name it
**H-INHERITED-EXPANSION**, with its three hypotheses: the stage-expansion
constant conditions; the flat zeroth analyticity input and newborn room
clause for every `T∈𝒯`; and the implication from the lettered clauses
at every `Z^on` location to each term clause, with unused room `ρ_m`,
including the extended arrested-clause reading on excluded components.
Its conclusions are joint holomorphy, real-strong-box boundedness,
gauge invariance, locality, and

\[
\|\mathbb C_k^{(n)}\|^{A,\flat}_{(n)}\le C_0^\sharp,
\quad
\sum_{\mathcal S}e^{\kappa_A|\mathcal S|}
 \sup|\mathbb C_k^{(n)}(X,\mathcal S)|
 \le C_0^\sharp e^{-a_md_m(X)},
\tag{A17.6}
\]

with its specified relative length for its `𝒦_d` terms.
Its domain inclusions and room budgets are part of the named input.
REP-ARREST, REP-CORE, REP-DISSOLVE and REP-KEPT supply the application
clauses needed on live pieces. Where their proofs stop, we assume
the missing supplier; we do not extend a partial theorem into an
unasserted raw-point locus. This is the precise conditional meaning
of carrying a stored term through a later preparation.

**R and re-exponentiation.** On a qualifying component, integrate its
actual term and insert the prescribed normalized reference law. On
first-class components apply the reversed gauge equivalence; on
second-class components retain the slice measure. Components not
qualifying retain their partly formed operation. REP-POS and the
normalization/mass hypotheses of §5 admit these operations. The
result is exactly the recursive density `(RT)ρ_k`, by its definition.

P5's A5 implication and the retained strip/cluster hypotheses identify
the bracket with the exponential of its absolutely convergent connected
series. Consequently exponentiating its logarithm returns that same
bracket. Finite regrouping of label terms and absolutely convergent
regrouping of their internal series preserve the integral formulas.
Add the new localized terms to the old action, subtract unit values
only for the interior families specified in (A17.1), and put the
subtracted constants into `E_{k+1}[𝒮]`. This gives exactly (A17.1) and
(A17.2) at `k+1`, including the top-integrated operations and preparation
factors. Omitting stored factors would change this equality.

**(filled: the position-dependent coupling).** For each `j`, subtract
`x_j=x_{j−1}−β_j` from the profile recursion. Then

\[
x_j(\cdot)-x_j=x_{j-1}(\cdot)-x_{j-1}
                   +\beta_j(1-\varphi_j).
\]

Summing and using `x₀(·)=x₀` gives
`x_k(·)−x_k=Σ_{j≤k}β_j(1−φ_j)`. On the intersection of the eroded
small-field domains every summand is zero. No nesting or sign of
`β_j` is needed. This verifies the Wilson part of (A17.1) under the
account's profile convention.

**Exceptional boundary terms.** For a new term with no older live
second-class region, retain the original relative-length bound
CMP 122b (1.99), in its admitted domain. This is (A17.3).
To see the distinct weaker claim for the other terms, use the account's
skeleton route, `4.21:lem-skeleton`, CA-I:63275–63391, and
`4.21:prop-birth-site`, CA-I:77396–77560. Name the latter's inputs
**H-BIRTH**: constituent bounds in `𝔑^A`; the strip theorem, strip-potential
corollary and combinatorial clauses (u1)–(u7); skeleton clauses (a)–(c)
and distance clause (d); and the floor `β_sκ/4≥λ_θ`.
They are not supplied by the numerical value of a rate.

For a first-group domain `X`, take the union `A=sk(X)` of cubes met
by its fixed minimizing relative tree. Its length is the tree length
`d^θ(X)=d_j(A)`, with `d_j(A)≤d_{j,W}(X)`. It may touch a one-layer
enlargement; we do not assert `A⊂X`. The skeleton lemma also says
`N_j(A)≤c_d(d_j(A)+1)`.

**(filled: the skeleton entropy).** Given `A`, the set `X\W` is a
subfamily of its cubes, so has at most `2^{N_j(A)}` possibilities.
Every island contained in `X` touches a cube of `X\W`.
Because islands are pairwise non-touching, those possible islands inject
into at most `3^dN_j(A)` neighbouring cube choices. Selecting them gives
at most `2^{3^dN_j(A)}` possibilities. Thus

\[
\#\{X:A(X)=A\}\le2^{(1+3^d)N_j(A)}
 \le e^{\lambda_\theta(d_j(A)+1)}.
\]

H-BIRTH's input bound and distance clause then imply

\[
\begin{aligned}
\mathfrak N^A(\mathbf B'^{(j)}(A))
&\le e^{\lambda_\theta(d_j(A)+1)}C_{99}c_1^\flat(g_j)
           e^{-(1+\beta_s/2)\kappa d_j(A)}\\
&\le e^{\lambda_\theta}C_{99}c_1^\flat(g_j)
           e^{-(1+\beta_s/4)\kappa d_j(A)}.
\end{aligned}
\tag{A17.7}
\]

The last line follows by subtracting exponents and using
`λ_θ≤β_sκ/4`. Older live strips are carried in the pocket list; they
enter neither this entropy count nor a new length. H-BIRTH's support
clause puts the true reading region in `A∪⋃_{P_A}Y^sharp`.
REP-RF then carries later descendants in that labelled format with
the stated stored rate. Term-by-term bounds follow because each term
is bounded by its norm's corresponding nonnegative summand.
Thus the result is a bound in the skeleton/tree length. It gives no
reverse inequality between that length and `d_{j,Z}`. This proves
exactly the two exceptional cases in (b), conditional on H-BIRTH and
the still-open propagation input; the original stronger metric is
not propagated by fiat.

**Locality, analytic domains and constants.** At each of these moves,
the named input supplies the local domain and the actual substitution
map. Composing two local admitted readings reads the union of their
specified supports, which is the support used for filing the output.
Products, finite sums and locally uniformly convergent holomorphic
series preserve holomorphy and gauge invariance; the required uniform
convergence and complex admission are the stage/cluster and stored-domain
hypotheses already named. The one-power hereditary reproduction gives
the hereditary class in (a), and restriction of a holomorphic function
to its included Balaban domains gives the asserted analyticity there.

Every step is a map from the prescribed norm ball into the same
prescribed norm ball, by the named stage, kept-term, counting and
inheritance bounds. Induction therefore retains their constants;
it does not sum a new unconstrained constant once per level. Their
only scale dependence is the stated running-coupling dependence, with
the following explicit exception.

**(filled: the ratio bound, including backward excursions).** The flow
bound gives `x_n≤x_j+c₅<2x_j`. Set `t=x_j/x_n>1/2`. If `t≥1`, then
`max(1,t²)=t²≤4t²`. If `1/2<t<1`, then
`max(1,t²)=1<4t²`. Multiplication by `g_j^{κ₀}` gives
(A17.5), since `g_j^{κ₀}t²=g_j^{κ₀−4}g_n⁴`.
No stepwise monotonicity or cutoff-dependent bound was used.
The parameter-dependence clauses of the named inputs and P7's site
independence now give (c).

This closes the structural induction at `k+1`. First-passage containment
in §3 admits every step through `K`. A19 below then supplies the
integrated upper member under its additional hypotheses, completing
the stated conditional assembly of (a)–(c). The cases involving the
extra `N≥3` stability inputs remain conditional on those inputs.

## 5. A19: integrated stability and equality of integrals

**Source:** `4.33:thm-stability`, CA-I:157028–157112;
proof CA-I:157114–157241. The unqualified heading declares a
**proved implication**. The source has **(h1)–(h11)**, not only
(h1)–(h8). The last three are needed for the equality of integrals.

### 5.1 All eleven hypotheses

Let `k≤K`. Set `N_k=#` scale-`k` unit cubes, so
`N_j=L^{-4(j−k)}N_k` for `j≥k`, and `ℓ_j=log g_j⁻²`.
For a history `𝒮=(Ω_j,Λ_j)`, let

\[
Z_j=\mathbb T_m\setminus\Lambda_j,\quad
Z_j^+=Z_j\cup\{\text{touching }MR_j\text{-cubes of }\Lambda_j\},\quad
\Gamma_n=\Omega_n\setminus\Omega_{n+1},
\]

where `Ω₀=𝕋_m`, `Ω_{k+1}=∅`, and `|Γ_n|` counts its own scale-`n`
unit cubes. `Y(𝒮)` contains every large-field component, operated or not.
Write `τ_𝒮=dV^ext⊗τ_𝒮^{V^ext}` for the representation's componentwise
kernel, with exterior Haar probability `dV^ext`. Its fibre may be singular.
The norm below is total variation. These conventions are CA-I:157000–157026.

**(h1)** At every `j≤K`, A17's representation, inductive local bounds
and termwise majorants hold. Each real labelled term is nonnegative
by A18 and has finite mass by CMP 122b (1.73),(1.79).
**A18 remains the named hypothesis REP-POS.** The open `R_V` says that
the *prescribed* scalar interaction must be real at every independent
admitted real pair, not just at the diagonal physical pair. Bare Wilson
positivity does not prove this assertion about its localized factors.

**(h2)** On real fields in `supp χ_k`, `𝐄_k` and `𝐑_k` are real, and

\[
|\mathbf E_k|+|\mathbf R_k|\le C_EN_k,\qquad
C_E=E_1^\sharp(1-L^{-\beta_T})^{-1}+1.
\tag{A19.1}
\]

`E₁^sharp,β_T` are the constants of the carried CMP 119 (2.45)–(2.46),
depending only on `L,N,𝔭`, not `g_k`.

**(h3)** `ℓ_j>0` for `j≤k`, with the flow proposition as its named supplier.

**(h4)** The vacuum-energy theorem applies in the **same normalization
as the density**. Its flow and representation hypotheses, localized
independence, and label-independence of R-made unit-configuration values
are all retained. Exactly these two conclusions are used:

\[
\begin{aligned}
\text{(a)}\quad&-E_k[\mathcal S_\emptyset]=\mathfrak l_k-\mathfrak r_k,
\quad\mathfrak l_k\ge0,\quad |\mathfrak r_k|\le C_{\mathfrak r}N_k;\\
\text{(c)}\quad&-E_k[\mathcal S]\le C_\Gamma(g_k)|\Gamma_k|
 +\sum_{j=1}^k(C_{\log}\ell_{j-1}+C_{\mathrm{loc}})|Z_j^+|_j,\\
&C_\Gamma(g_k)=\tfrac32(N^2-1)(\ell_k+B_\sharp\gamma^2)+C_{\mathfrak r}.
\end{aligned}
\tag{A19.2}
\]

`C_r≥0` depends only on `L,N,𝔭`. The logarithmic part is nonnegative
under the positivity condition stated in (h3)/(h4). The correction
needed to apply (a) to the account's original bare density is §5.2.
Writing “the vacuum theorem applies” without that correction is invalid.

**(h5)** For every label and every real exterior,

\[
\|\tau_{\mathcal S}^{V^{\rm ext}}\|
 \le\mathfrak M_k(\mathcal S)
       \exp\left[-E_k[\mathcal S]+C_{\rm maj}\sum_{n=0}^k|\Gamma_n|\right].
\tag{A19.3}
\]

`𝔐_k≥0` is exterior-independent; `C_maj≥0` depends only on `L,N,𝔭`.
Its three distinct suppliers are: CMP 122b (1.79) on R-operated
components; the CMP 122b (1.72) T″-majorant on unoperated components,
after the last constraint is integrated out by (h7), with the carried
CMP 119 (2.48) bound for frozen terms; and CMP 119 (2.43)–(2.44)
outside `Y(𝒮)`. The Wilson exponent is nonpositive.
None of these three majorants is replaced by pointwise boundedness
of a Haar density.

**(h6)** With

\[
q_k(\mathcal S)=C_{\rm maj}\sum_{n<k}|\Gamma_n|
 +\sum_{j=1}^k(C_{\log}\ell_{j-1}+C_{\rm loc})|Z_j^+|_j,
\qquad
\sum_{\mathcal S}\mathfrak M_k(\mathcal S)e^{q_k(\mathcal S)}
 \le e^{c_MN_k},
\tag{A19.4}
\]

`c_M≥0` depends only on `L,N,𝔭`. This is a separate history-sum
hypothesis. CA-I:157243–157249 explains the per-cell suppression route,
but that paragraph does not give a fresh proof of all counts and
operation-majorant suppliers. The definition of `q_k` proves no bound
on its exponential moment.

**(h7)** The block map `𝓜` is Borel on all configurations and has unit
fibre mass: `∫dV δ(𝓜(U)V⁻¹)=1` for every `U`.

**(h8)** Every reference normalizer in CMP 122a (1.100)–(1.102) is
finite and strictly positive wherever used. R replaces a term by
`m_τ(Ṽ) 𝔰(·;Ṽ)`, where `m_τ` is its component integral and `𝔰`
is a probability measure. On a second-class component, `𝔰` lives on
the gauge slice and can be singular relative to Haar.

**(h9)** On first-class components, the reversed Faddeev–Popov operation
preserves integrals of gauge-invariant functions. This is equivalence
of densities as in CMP 122b p.378, not pointwise equality.

**(h10)** Removing `χ''_k` under the integral is an equality, in the
creating-step proposition's precise form of CMP 122a (1.89).

**(h11)** The creating step inserts an exact finite partition of unity
inside T.

The analytic background used below is named **H-MEASURE**: normalized
Haar integration on compact matrix groups and their finite products, its
left/right/inversion invariance, Tonelli/Fubini for finite measures or
absolutely integrable functions, and dominated/uniform convergence for
these integrals. These foundational measure facts are not rebuilt in
P10. All nontrivial RG mass, positivity and integrability inputs are
the explicit (h1),(h5)–(h11), not part of H-MEASURE.

### 5.2 (correction): fix the vacuum constant before applying (h4)(a)

This follows [NRM §5](../../gates/nrm-check.md) and the corrected refereed
LSC. It is visible directly in CA-I:159153–159160,159321–159327.
Let `T` denote the full torus at the corresponding step, set
`e_j=E^{(j)}(T,T)`, and put

\[
E_{\rm vac}=\sum_{j=0}^{K-1}e_j,\qquad
\widehat\rho_k=e^{-E_{\rm vac}}\rho_k^{\rm bare},\qquad
\widehat Z=e^{-E_{\rm vac}}Z_{\rm bare}.
\tag{A19.5}
\]

At every label, add this same constant to the bare additive energy.
For the never-large label,

\[
E_k^{\rm vac}=E_{\rm vac}-\sum_{j<k}e_j=\sum_{j=k}^{K-1}e_j,
\qquad
E_k^{\rm bare}=-\sum_{j<k}e_j=E_k^{\rm vac}-E_{\rm vac}.
\tag{A19.6}
\]

Thus the bare version of (h4)(a) is

\[
-E_k^{\rm bare}=E_{\rm vac}+\mathfrak l_k-\mathfrak r_k,
\tag{A19.7}
\]

not the printed expression without `E_vac`. This is an algebraic
identity, independent of any numerical estimate of a partition function.

For clarity, the source one-step energy input, CA-I:159412–159426, is

\[
e_j=-\tfrac32(N^2-1)(L^4-1)N_{j+1}\log x_j+r_j,
\quad |r_j|\le D_0N_{j+1},
\quad D_0=(L^4-1)c_G^\sharp+K_*(E_0+1).
\tag{A19.8}
\]

For `N=2`, its logarithmic coefficient is `9/2`. This one-step
estimate and its domain/locality assumptions remain part of (h4).
Given them and positive `log x_j` along the full run, the tail in
(A19.6) has a nonpositive logarithmic part. Its remainder obeys

\[
\sum_{j=k}^{K-1}|r_j|
 \le D_0N_k\sum_{t=0}^{K-k-1}L^{-4(t+1)}
 \le\frac{D_0}{L^4-1}N_k.
\tag{A19.9}
\]

**(filled)** The finite sum is
`(1−L^{-4(K−k)})/(L⁴−1)≤1/(L⁴−1)`, by multiplying the
geometric sum by `1−L⁻⁴` and cancelling adjacent terms. No computed
constant is used. At `k=K` every tail is empty. This is why the
vacuum-normalized energy, rather than the bare accumulated energy,
has the current-volume remainder required by (h4)(a).

All hypotheses (h4)–(h6) must be read in this **same** convention.
The port does not mix a bare upper bound with a normalized lower one.
For every normalized observable,
`∫F hatρ/∫hatρ=∫F ρ^bare/∫ρ^bare`, since the same nonzero scalar cancels.
The source's bare and normalized unnormalized integrals are different.

### 5.3 Exact conclusions

For any family satisfying §5.1, the source's conclusions are:

1. Under (h1),(h2),(h3),(h4)(a),

   \[
   \chi_k e^{-x_kA(U_k)-E_-N_k}dV_k\le\rho_kdV_k,
   \qquad E_-=C_E+C_{\mathfrak r}.
   \tag{A19.10}
   \]

   `E_-` depends only on `L,𝔭,N`, not `g_k,k,K,m,g₀`.

2. Under (h1),(h3),(h4)(a),(h4)(c),(h5),(h6),(h7),

   \[
   \int\rho_kdV_k\le e^{E_+(g_k)N_k},\qquad
   E_+(g_k)=\tfrac32(N^2-1)(\log g_k^{-2}+B_\sharp\gamma^2)
             +C_{\mathfrak r}+C_{\rm maj}+c_M.
   \tag{A19.11}
   \]

   Also `E₊≤C(L,𝔭,γ,N)(1+log g_k⁻²)`. This is an integrated bound.
   No pointwise upper member of CMP 122b (0.1) is asserted.

3. Under part 2's hypotheses at `K`, and (h1),(h7)–(h11) at the
   steps used, `E₊(g_K)≥0` and

   \[
   \int\rho_jdV_j\le e^{E_+(g_K)N_j}\quad(0\le j\le K).
   \tag{A19.12}
   \]

   If `g_K≥g₋(g)`, then

   \[
   E_+(g_K)\le\tfrac32(N^2-1)
       [\log(g^{-2}+B_\sharp)+B_\sharp\gamma^2]
       +C_{\mathfrak r}+C_{\rm maj}+c_M.
   \tag{A19.13}
   \]

4. Under (h1),(h7)–(h11),

   \[
   \int\rho_kdV_k=\int\rho_0dU\quad(0\le k\le K).
   \tag{A19.14}
   \]

For the account's vacuum-energy application, set `ρ=hatρ` in these
formulas. In bare variables (A19.10) has an additional factor
`e^{E_vac}` on its left, and (A19.11)–(A19.12) have that same factor
on their right. Equality (A19.14) is valid separately in either
convention, with both endpoints in that convention.

### 5.4 Proof of the four conclusions

**Lower member.** Nonnegative labelled measures in (h1) allow us to
retain only the never-large term:

\[
\rho_kdV_k\ge\tau_{\emptyset}
 =\chi_k\exp[-x_kA(U_k)+\mathbf E_k(U_k)+\mathbf R_k(U_k)
                          -E_k[\emptyset]]dV_k.
\]

**(filled: comparison as measures).** Its exponent is real.
By (h2), `𝐄_k+𝐑_k≥−C_EN_k`.
By (h3),(h4)(a), `−E_k[∅]≥−C_rN_k`.
Exponentiation preserves order. For any Borel set, integrate the
resulting nonnegative pointwise inequality for this one term and add
the other nonnegative terms. This proves the **measure** inequality
(A19.10), even when other terms are singular. The stated dependence
of `E_-` follows by adding the two explicitly independent constants.

**Integrated upper member.** The representation outside `Y(𝒮)` gives
the exterior Haar disintegration specified above. H-MEASURE and (h5)
give

\[
\left|\int\tau_{\mathcal S}\right|
\le\int dV^{\rm ext}\,\|\tau_{\mathcal S}^{V^{\rm ext}}\|
\le\mathfrak M_k(\mathcal S)
 e^{-E_k[\mathcal S]+C_{\rm maj}\sum_{n=0}^k|\Gamma_n|}.
\]

Use (h4)(c), then separate `n=k` in the last sum. The exponent is at
most `q_k(𝒮)+(C_Γ(g_k)+C_maj)|Γ_k|`.
Since `Ω_{k+1}=∅`, `Γ_k=Ω_k⊂𝕋_m` and `|Γ_k|≤N_k`.
**(filled: the sign needed for the volume replacement).** The
coefficient is nonnegative: `ℓ_k>0`, `B♯>0`, `C_r≥0`,
`C_maj≥0`. Replacing `|Γ_k|` by `N_k` therefore preserves this upper
bound. Sum the finitely many labels and use (h6):

\[
\begin{aligned}
\int\rho_kdV_k
&\le e^{(C_\Gamma(g_k)+C_{\rm maj})N_k}
       \sum_{\mathcal S}\mathfrak M_k(\mathcal S)e^{q_k(\mathcal S)}\\
&\le e^{(C_\Gamma(g_k)+C_{\rm maj}+c_M)N_k}.
\end{aligned}
\]

The exponent is exactly `E₊(g_k)N_k`.
**(filled: constant dependence).** To check the final dependence,
put `a=3(N²−1)/2` and
`b=a(C_β+1)γ²+C_r+C_maj+c_M`. Since `B♯≤C_β+1` and
`ℓ_k≥0`, `E₊≤aℓ_k+b≤max(a,b)(1+ℓ_k)`.
The maximum reads only `L,𝔭,γ,N`. This proves (A19.11).

**Equality of integrals.** Induct over the steps. For T, the literal
meaning of its delta notation is the image measure under the Borel
map `𝓜`. **(filled: kernel interpretation)** On the constant function one,

\[
\int(T\rho_k)dV_{k+1}
 =\int\rho_kdV_k\int dV_{k+1}\,
   \delta(\mathcal M(V_k)V_{k+1}^{-1})
 =\int\rho_kdV_k.
\]

The measures are finite and nonnegative by (h1), and (h7) makes the
inner integral one. The finite creating partition (h11) preserves
this mass by summing its indicators before integration.

On an R component, (h8) yields

\[
\int d\widetilde V\int m_\tau(\widetilde V)
                      \mathfrak s(dV;\widetilde V)
 =\int d\widetilde V\,m_\tau(\widetilde V)=\int\tau.
\]

This uses probability mass one, not absolute continuity of `𝔰`.
Apply (h9) to the gauge-invariant function one and (h10) to the
specified characteristic factor. Each remaining operation also
preserves the integral. Composing the finitely many component operations
gives `∫ρ_{k+1}=∫ρ_k`. Iterating from zero proves (A19.14).

**Last-level constant.** Every summand defining `E₊(g_K)` is
nonnegative under the stated hypotheses. By (A19.14) and (A19.11),

\[
\int\rho_jdV_j=\int\rho_KdV_K
 \le e^{E_+(g_K)N_K}\le e^{E_+(g_K)N_j},
\]

since `N_K=L^{-4(K−j)}N_j≤N_j`. This proves (A19.12).
Finally `g_K≥(g⁻²+B♯)⁻¹ᐟ²` implies
`g_K⁻²≤g⁻²+B♯`. Monotonicity of the logarithm gives (A19.13).

The proof has used (h6) and positive reference normalizers, not proved
them. It neither removes REP-POS/`R_V` nor produces a pointwise upper bound.

## 6. A20: exactness under complex sources

**Source:** `4.34:lem-sourced-exactness`, CA-I:157263–157283;
proof CA-I:157286–157395. The heading is unqualified: a **proved
conditional implication**, conditional on the correlation induction.
The proof is Sussman–Alpoge's five-move argument, using Balaban's
block-averaging, gauge-fixing and forward/reversed constructions.

### 6.1 Statement and the hypotheses carried by the induction

Let `w=Σ_i z_i f_i`, with complex coefficients `z=(z_i)_i`. Let `r`
be the number fixed in the setting of the correlation theorem, and assume

\[
\sup|\zeta_j|\le\frac83r.
\tag{A20.1}
\]

At every level `k` at which the correlation theorem's induction hypothesis
holds at `w`, the effective density of `1.5:def-densities` satisfies

\[
\int\rho_k^w\,dV_k=\int\rho_0^w\,dU=Z(z),\qquad
\rho_0^w(U)=\exp[-A(x_0-w,U)-E].
\tag{A20.2}
\]

Both members are analytic in `w`. Here the measures on the displayed
configuration spaces are product Haar, the Wilson action is that of
`1.1:def-wilson-action`, and `E` is the additive constant in the bare
density. As elsewhere, delta notation may denote a finite measure.
Analyticity of the effective mass is asserted on the open source domain
on which the induction applies. This is not a claim that the induction
holds for every complex source. The bare mass has an entire extension
in the finitely many coordinates `z_i`.

The induction is a substantial named premise, not a consequence of
(A20.1). Its concrete uses here are these:

* **H-SOURCE-IND:** the correlation induction and its admitted inputs
  hold on the source domain being used, with the actual effective
  densities, shifts, history domains and prescribed branches. The
  standing of [P6](p6-correlation.md) is **ported**. Its B3 register
  retains, in particular, the outstanding polydisc proposition,
  preparatory window statement, frozen whole-disc bounds and step
  hypotheses; this lemma supplies none of them. Source-free inputs
  retain the standings in §1 and the limitations in §4.
* **H-COMPLEX-MOVES:** the induction constructs the effective object by
  the five moves below. Its representations and convergent expansions
  are exact at each fixed source, with the local domains, gauges,
  refined T partition and logarithm branches required by those moves.
  The total-variation majorants required for each integration and
  interchange hold. A source-free positivity inequality is not such
  a majorant by itself.
* **H-GAUGE-SECTOR:** each gauge-fixing bond has a positive cutoff
  `ε_k`, and its weight `a` obeys
  `|Im a|≤sup|ζ_j|` and `(8/3)r ε_k²≤1`. The latter is the relation
  expressly invoked at CA-I:157333–157338, from the correlation setting.
  Gauge invariance of the remaining integrand and the prescribed
  gauge-fixing factorization are also retained, as in CMP 109.
* **H-SOURCE-REFERENCE:** for every exterior field and R component
  the chosen reference is source-independent, nonnegative and has
  finite positive mass. In the density notation of the source this is
  `0<D⁰=∫s⁰<∞`. The required measurable dependence on exterior fields
  is supplied. Positivity of these normalizers is the named
  CMP 122a pp. 176–177 input at CA-I:157372–157374, not proved here.
* **H-FORWARD-REVERSE:** the specified forward and reversed changes of
  variables have the integral-preserving property supplied by CMP 122b
  on these gauge-invariant integrands, with their actual domains and
  characteristic factors. No pointwise equality is assumed.

We also retain H-MEASURE from §5.1, now using Fubini for absolutely
integrable complex functions or finite complex measures. `E` is fixed
independently of `z`. In the vacuum-normalized convention it may be the
single unsourced value `E_vac` of §5.2. An additional source-dependent
counterterm would change `Z(z)` and is not silently introduced.

### 6.2 Proof, move by move

**(a) Block averaging.** Let `𝓜` be Balaban's block-average map,
extended as the Borel map of `1.5:def-block-average` on all
configurations, not only small fields. At every configuration `U`,
the kernel `δ(𝓜(U)V⁻¹)dV` is the point mass at `𝓜(U)` and has mass one.
For a finite complex input measure `τ^w`, the block operation is its
image under `𝓜`. Consequently

\[
\int dV\int\delta(\mathcal M(U)V^{-1})\,\tau^w(dU)
=\int 1\,\tau^w(dU).
\tag{A20.3}
\]

**(filled: complex interchange).** Interpret this as integration of a
probability kernel against a finite complex measure. Its total variation
is bounded by the same kernel integrated against `|τ^w|`; its mass is
at most `‖τ^w‖`. Fubini therefore applies. No order inequality on the
complex density is used. This operation is linear in `τ^w`.

**(b) Gauge fixing.** Fix a bond `(y,x)` and a gauge transformation
with `u(y)=1`. Then `U^u(y,x)=U(y,x)u(x)⁻¹`. Define

\[
q(v)=1-\operatorname{Re}\operatorname{tr}v,\qquad
\mathfrak z(a)=\int_{SU(N)}dv\,
 1_{\{|v-1|<\varepsilon_k\}}e^{-a q(v)}.
\tag{A20.4}
\]

Haar invariance under translation and inversion gives, for every `U`,

\[
\int du(x)\,1_{\{|U^u(y,x)-1|<\varepsilon_k\}}
                 e^{-a q(U^u(y,x))}=\mathfrak z(a).
\tag{A20.5}
\]

To divide, one must prove the right member nonzero. With normalized
trace `tr 1=1` and unitary `v`, expansion of `(v−1)^*(v−1)` gives

\[
q(v)=\tfrac12\operatorname{tr}((v-1)^*(v-1)),\qquad
0\le q(v)\le\tfrac12|v-1|^2\le\varepsilon_k^2
\tag{A20.6}
\]

on the indicator's support. The trace of a positive matrix divided
by its dimension is bounded by its largest eigenvalue; this proves
the operator-norm inequality. H-GAUGE-SECTOR gives
`|(Im a)q(v)|≤1`. Hence

\[
|\mathfrak z(a)|\ge\operatorname{Re}\mathfrak z(a)
 \ge\cos(1)\,\mathfrak z(\operatorname{Re}a)>0.
\tag{A20.7}
\]

**(filled: strict positivity).** The real integrand is positive on
the open neighbourhood `|v−1|<ε_k`. A nonempty identity neighbourhood
in a compact group has positive Haar measure: its translates cover
the group, a finite subcover exists, and zero measure of the
neighbourhood would give zero measure of that finite cover. Moreover
`cos t≥1−t²/2≥1/2` for `|t|≤1` (integrate `|sin t|≤|t|`). Thus the
strict inequality in (A20.7) does not rest on a numerical estimate.

Divide (A20.5) by `𝔷(a)` and insert this resolution of one. At fixed
source, its normalized complex kernel has absolute mass bounded by
`𝔷(Re a)/|𝔷(a)|≤1/cos(1)`. The finite number of bond insertions
therefore preserves integrability; H-COMPLEX-MOVES supplies the
majorants for the subsequent integrations.

Interchange the gauge and configuration integrations, and make the
specified gauge change of variables. Each real plaquette density is
unchanged because its holonomy is conjugated. Multiplication by a
complex scalar weight independent of `U` preserves this equality.
Thus `A(c,U^u)=A(c,U)` for complex `c` too. With the remaining
integrand's gauge invariance in H-GAUGE-SECTOR, the same Haar change
used by Balaban preserves the integral. Fixing `w` also fixes `a`,
so insertion and integration are linear in the input measure.

**(c) Representation moves.** For a finite partition of unity
`Σ_αχ_α=1`, summing `χ_ατ^w` returns `τ^w`, and summing their
integrals returns its mass. The refined T operation has exactly one
active term at each configuration, by the supplied refined-partition
identity. Its equality holds before any integration; arbitrary
overlaps are not discarded. Changes of variables use their prescribed
Jacobians or Haar invariance. Mayer rearrangements use the exact
identities and absolute convergence in H-COMPLEX-MOVES, so summation
and integration may be interchanged.

If a prescribed convergent logarithm expansion represents `G^w`,
write its sum as `L^w`. The branch convention includes
`exp L^w=G^w`. Replacing `G^w` by `exp L^w` therefore leaves the
integrand exactly unchanged. This does not take the logarithm of an
arbitrary, possibly zero, large-field integral.

**(correction: what is linear).** CA-I:157287–157290 and
157359–157364 call every move linear in the integrand, including
the passage to logarithmic representations. The map `G↦log G`
alone is not linear. The represented integrand is unchanged by
`G↦exp(log G)`, and the mass is unchanged. The latter identity,
together with the linear partition and integration operations,
is the property needed here. No linearity of effective potentials
or their logarithms is used.

**(d) Large-field normalization.** Hold the exterior configuration
`\widetilde V` fixed. With `Λ` the integrated component, put

\[
N^w(\widetilde V)=\int dV|_\Lambda\,\tau^w,
\qquad D^0(\widetilde V)=\int dV|_\Lambda\,\mathsf s^0.
\tag{A20.8}
\]

The reference and `D⁰` can depend on the exterior fields; their
source independence and strict positivity are H-SOURCE-REFERENCE.
Neither `N^w` nor `D⁰` depends on the integrated variables.
Thus the replacement has the same component mass:

\[
\int dV|_\Lambda\,
 \frac{\mathsf s^0N^w(\widetilde V)}{D^0(\widetilde V)}
=N^w(\widetilde V).
\tag{A20.9}
\]

**(filled: no hidden division by a sourced mass).** For each exterior
field the normalized reference is a probability measure. The variation
of the replacement on this component is `|N^w(\widetilde V)|`,
which is at most the variation of the original conditional input.
The exterior majorant in H-COMPLEX-MOVES therefore makes the replacement
integrable. One needs no uniform positive lower bound on `D⁰` for
this mass identity. It is enough that the normalized reference is a
well-defined measurable probability kernel. The same argument applies
to the prescribed singular reference measures. In particular
`N^w=0` is allowed. Integrating (A20.9) over the exterior fields
preserves the total integral, linearly in `τ^w`.

**(e) Forward and reversed transformations.** Apply the specified
changes of variables from CMP 122b. The weighted action is gauge
invariant by (b), and the relevant Haar measures are invariant.
H-FORWARD-REVERSE includes the domains and characteristic-factor
identities needed for these transformations. Their integral
equalities therefore apply at the fixed complex source. They
need not identify the two integrands pointwise.

Each step is a composition of these five kinds of exact move.
Starting with `ρ₀^w`, iterate the equality of mass over the finitely
many steps through `k`. This proves (A20.2).

### 6.3 Analyticity and the scope of the denominator assertion

**(filled: entire bare mass).** The bare lattice is finite. Since
the Wilson action is linear in its weight,

\[
\rho_0^w(U)=e^{-A(x_0,U)-E}
              \exp\left(\sum_i z_i A(f_i,U)\right).
\tag{A20.10}
\]

Each `A(f_i,U)` is continuous and bounded on the compact real
configuration space, say by `M_i`. On every compact polydisc
`|z_i|≤R_i`, the exponential series is absolutely and uniformly
bounded by `exp(Σ_iR_iM_i)`. The remaining factor is bounded too.
The finite Haar integral can consequently be taken term by term
in the locally uniformly convergent power series. It is an entire
function of all the finitely many `z_i`. Equality (A20.2) identifies
the effective mass with that analytic function on the induction's
open source domain. No differentiation of indicator functions or
of a singular effective density is required.

**(correction: source-dependent denominators).** The last sentence
of the source proof, CA-I:157393–157394, says that no denominator
depending on the source occurs. The proof of (b) permits `a` to
depend on the running shifts, in which case `𝔷(a)` can depend on
the source. Its nonvanishing is proved by (A20.7), rather than by
source independence. The precise assertion established for (d)
is that the R denominator `D⁰` is positive and source-independent;
there is no division by `N^w` or by a sourced large-field partition
function. If a particular gauge prescription freezes `a`, its
`𝔷(a)` is source-independent as well, but that is not needed.
This qualification changes no equality in the proof.

This proves analyticity of the total mass, not its nonvanishing,
not a global analytic `log Z`, and not the correlation induction
premise itself. It uses no reflection-positivity claim at complex
source.

## 7. Result

The following five implications from Ethan Sussman and Levent Alpoge's
complete account, with Claude and Codex as authors of their text,
have been ported on their stated route, crediting Balaban's construction:

* **A10**, `4.18:thm-preparatory-boundary`: full conditional
  companion-system transfer, including all six conclusions and
  the early-stage equality. Balaban CMP 122a (1.60)–(1.70) is
  H-STAGE, an input rather than a theorem proved here.
* **A15**, `4.38:cor-step-count`: all six conclusions, retaining
  the `g⁻²+B♯` stopping threshold and the physical/auxiliary-site
  distinction.
* **A17**, `4.20:thm-representation`: the full representation,
  analytic/local/norm assertions, exceptions and antecedent
  register, with a conditional proof by the source's level
  induction. This is an assembly of the named step implications;
  their unreproduced proofs and explicitly outstanding inputs
  remain hypotheses. It is not closure of the full RG induction.
* **A19**, `4.33:thm-stability`: all four conclusions, using all
  eleven printed hypotheses (h1)–(h11), with the indicated subsets
  for each conclusion. The upper bound is integrated. The
  normalized lower bound uses the fixed vacuum constant.
* **A20**, `4.34:lem-sourced-exactness`: the five exact moves,
  the gauge-normalizer nonvanishing argument and analyticity
  of the common mass, conditional on the correlation induction.

The **(filled)** passages spell out compensation and branch matching,
cube filing and norm estimates, first-passage/site induction,
the stage/skeleton/ratio steps in representation assembly,
vacuum-tail algebra, positive-measure domination, complex-kernel
Fubini, strict gauge-normalizer positivity, reference normalization
and uniform power-series integration. They are written deductions
from the named inputs, not numerical or computer-assisted steps.

The **(correction)** passages retain NRM's `E_vac` correction to
(h4)(a), distinguish unchanged represented integrands from the
nonlinear logarithm map, and qualify the source's final blanket
denominator assertion by separating the zero-free gauge normalizer
from the source-independent R denominator. These qualifications
do not claim to supply any missing stage theorem.

The complete named-hypothesis registers are §§2.1, 3.1, 4.2–4.3,
5.1 and 6.1. In particular, H-STAGE and its full admissible-profile
scope; H-WEIGHT and its geometry; H-TORUS and the auxiliary admission;
the published and open representation suppliers; A18/REP-POS with
the actual `R_V` of [PD](../pd.md); the history majorant (h6),
positive reference normalizers and exact transformation identities;
and the correlation induction and its complex bounds all remain
named premises wherever not proved in full here. The checked,
ported and refereed inputs have only the standing and scope stated
in §1. The account's “outstanding,” “incomplete” and cited-input
qualifications are not erased by the assembly proof.

No proof of T0, status promotion, audit verdict or closure of A18 is
claimed. No run has been used to discharge a mathematical step.
This research text is **not yet checked by another model**.
