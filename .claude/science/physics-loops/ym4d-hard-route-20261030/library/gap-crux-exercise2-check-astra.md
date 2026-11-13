# Repo search

Requested checkout pin: `79017e5f4`; source account pin: `31a47c543775`. The elementary implications survive with corrections. The asserted Coulomb exponent test fails on the printed shapes. The untwisted Z2 test is proved below; the meaningful positive-theta test for full compact Villain remains unresolved.

Research text only; no scientific or audit status is conferred. Computation is not a proof step.

## Search record and fixed scope

Checker: OpenAI Codex, dispatch `gpt-6-astra xhigh`, 2026-11-13. Checked text: Claude Fable 5.2's `gap-crux-exercise2-max.md` (637 lines), at `79017e5f46d2aa86d9f14d93df72c49c5b20bf8d`. This is the requested research check, not an audit or a status record. Only this output file is edited. The requested target-specific `prior/gap-crux-exercise2-check-astra.md` does not exist. `prior/repo-search-2026-11-08.md` was read; it supplies locators, not this check's conclusions.

All five requested refs were searched in `/Users/jonreilly/Projects/Physics`, using bounded `git grep -n -i -E ... -- '*.md' '*.tex' | head ...` commands. Their hashes at this read were:

| Ref | Hash |
|---|---|
| origin/main | 993f5e4f6d11a7e20a1cab9612c5749a53bae073 |
| pr/10114 | f76f6c649cff7dffbab664d8976e680e8f287fe9 |
| pr/10133 | 89faef229ff6e6bde42baad15ed8270c2f4087d8 |
| pr/10134 | 1e70c7211a2cdbc39001e619f1dd89db45e25851 |
| pr/10141 | c73ad7b177d94f89ff37b77386936e3d52b48b05 |

Terms: `TS-theta|transverse doubling|spreading exponent|Lemma CX1|square.root law|Villain.*twist|twist.*Villain`; then `twist deficit|transverse stability|electric.flux free energy|TS-theta|worldsheet doubling|Hellmann.Feynman continuation`; then `vortex.free.energy|twisted.partition.function|shifted integer.curl|concavity defect`. The second query returned no hits on all five refs. The first returned only unrelated Maxwell mode multiplicities and a soft-route numerical square-root comparison. Broader `theta sum`, `electric.flux` and `helicity modulus` discovery passes hit their caps or produced oversized lines; they establish no absence result.

Relevant hits and already existing work:

| Source | Exact statement used or excluded | Closeness |
|---|---|---|
| `origin/main:docs/PERIODIC_FINITE_CLOCK_VILLAIN_COVARIANCE_AND_OBSERVABLE_MASSLESSNESS_BOUNDED_THEOREM_NOTE_2026-09-14.md`, sections 1–3, 7–9 | On each affine integer-curl coset, `Cov(F) >= beta(1-delta) P_e`; its Hodge image has `P_c`. The finite-clock covariance sandwich retains an **upper**, not a positive lower, harmonic bound `beta P_h`. | Related discrete-Gaussian method. Neither an electric-flux parity bound nor a transverse-doubling estimate. Credit its Fröhlich–Spencer method; do not turn its local covariance result into a harmonic-sector result. |
| `pr/10114:.claude/science/toe-ruleset-20261021/agents/ym4d-proof/checks/review_massgap_block_literature.md:112–121` (also located on pr/10133) | The twisted and untwisted comparison needs a common interpolation parameter; a local implicit-function argument does not supply global continuation. | Related prior warning; supplies no TS estimate. |
| Local `gap-crux-restate.md:234–266` | Theorem F(b): `Z_odd(ja,kb\|c,d) <= Z_odd(a,b\|c,d)^(jk)`; (TUBE) requires `Z_odd(a,b\|2c,d) <= K Z_odd(a,b\|c,d) Z(a,b\|c,d)`. | WS is prior work. TUBE is an earlier, stronger transverse-locality proposal, not a proved TS supplier. Credit Claude Fable's note. |
| Local `gap-z2parity-astra.md:384–438` | For Z2, `Z^v/Z^0 <= epsilon_a/(1-epsilon_a)`, with `epsilon_a = (N/80)(80 exp(-2 beta))^(a^2)/(1-80 exp(-2 beta))`. | Supplies the low-temperature test. Reused below, not re-derived as a new contour theorem. |
| Local `gap-z2parity-astra.md:444–501` | Frozen 2T has `Z^v/Z^0 -> 1/61` at fixed torus; the displayed Maxwell theta ratio is explicitly a **free comparison model**. | Supplies exact flat counts and the correct scope of the Gaussian formula. |
| Local `gap-tu-retry.md:61–102` and `gap-hs-check-astra.md:201–211` | Theorem V says the periodic **Langevin** gap tends to zero for Villain beta at least `2^14`. The earlier check explicitly says this does not give the twisted odd-sector fraction. | The exercise's “Villain twist theorem, row 786” is a miscitation already diagnosed by the earlier check. Use that diagnosis; no new discovery is claimed. |
| Local `gap-es1-opus.md:36–165` | Theorem V expresses the defect through crossed-sector weights; Lemmas Z2-a–c give the Z2 cocycle representation, minimum area and fixed-box even-sector low-temperature bound. | Existing inputs for the finite-group comparison. They concern Z2, not all finite subgroups of SU(2). |

`open-registry.md`, `open-core.md` and `l17c.md` have no match for this task, TS-theta, transverse doubling, Villain or CX1. No separate TS owner was found. Existing component results above are reused, not reopened.

The outline index was consulted first: README; matching chunk rows and neighbours; obligations entries 588–599 and related mass-gap scope. Searches for Villain, Coulomb, thermal/transfer, centre, flux, doubling and the named lemmas found no indexed TS theorem. Source SA 570–602 states that polynomial clustering does not give a positive mass gap. CA-I 2698–2713 explicitly does not assert a mass gap. Those are scope statements, not an absence theorem for the whole account. No Balaban estimate is needed by this check. Credit Sussman and Alpoge, with Claude and Codex, for the indexed account.

Notation below: `X` means the checked exercise. Its `q=(1-R)/(1+R)` is **odds**, whereas several older files use `q=(1-R)/2` for a probability. They are not interchangeable. Unless stated otherwise the model checks use `m=0`, fixed finite coupling, and all side lengths in `{a,2a}`; this includes the shapes used in Theorem E.

## 1. F5 — HOLDS AFTER CORRECTION

X:182–188. The displayed variational inequality HOLDS. Let `d=Delta(x)>0` and let the differentiable excited branch be realized by a normalized eigenvector. Its Rayleigh quotient gives

\[
 E_0(x+h)\le E_1(x)+hE_1'(x),\qquad
 -\Delta'(x)\le {d\over h}
 +{E_0(x)+hE_0'(x)-E_0(x+h)\over h}.
\]

This requires `x+h` in the family domain. At a degeneracy use an eigenvector of the compressed derivative for the chosen one-sided branch. The simple ground state and bounded perturbation suffice for the usual isolated-eigenvalue derivative, not for every spectral edge without an eigenvector.

The square-root corollary requires a **uniform interval bound**: if `-E_0'' <= M` on `[x,x+h]`, then the defect is at most `M h^2/2`. If the interval on which this same `M>0` is known contains `h=sqrt(2d/M)`, then

\[
 -\Delta'(x)\le\sqrt{2Md}.
\]

A point value `|E_0''(x)|` is not sufficient. For example take
`H(x)=[[x,epsilon],[epsilon,-x]]`, `0<epsilon<1`, at `x=-1`. It has
`Delta=2 sqrt(1+epsilon^2)`, `-Delta'=2/sqrt(1+epsilon^2)` and
`|E_0''|=epsilon^2/(1+epsilon^2)^(3/2)`. The pointwise proposed right side is only `2epsilon/sqrt(1+epsilon^2)`.

The following interpretation is unsupported: “the second derivative ... is extensive (a specific heat times the volume).” F5 assumes neither locality nor a uniform susceptibility estimate. Perturbation theory instead gives

\[
 -E_0''(x)=2\langle Q B\psi_0,(H-E_0)^{-1}Q B\psi_0\rangle
 \le {2\|B\|^2\over\Delta(x)}.
\]

There is no automatic volume-linear bound. Nor must a first-order transition close a finite-volume simple ground gap: finite-volume avoided crossings are compatible with F5. The exact inequality survives; the asserted volume law and finite-volume phase-transition inference must be removed. No uniform linear continuation estimate follows.

## 2. Lemma TD and its zero-thermal-sum law — HOLDS

X:495–500. The proof uses the two positive operators in the **same crossed frame**, and `b<=a`. Retain those hypotheses. Write `alpha_0=A/a^2`, `alpha_v=B/b^2`. Directly from their eigenvalue sums,

\[
 (1+S_0)^{-2}\le\alpha_0\le1,\qquad
 (1+S_v)^{-2}\le\alpha_v\le1.
\]

Thus `A-B <= a^2-b^2+2S_v b^2`, using
`1-(1+s)^(-2)<=2s`. Also
`A+B >= (a+b)^2/[2(1+S)^2]`. Division gives exactly

\[
 q(2n_j)\le 2(1+S)^2\left(q(n_j)+{S_v\over2}\right),
\]

because `b/(a+b)<=1/2`. There is no reversed inequality or lost factor.
If `S_0=S_v=0`, then `A=a^2`, `B=b^2`, and independently

\[
 q(2n_j)={1-(b/a)^2\over1+(b/a)^2}
 ={2q(n_j)\over1+q(n_j)^2}.
\]

“Free law” must mean this rank-one/zero-thermal-sum law, or another case where the normalized spectral factors cancel. It is not the general finite-temperature law of a free Gaussian gauge theory. The algebra alone does not identify its factor two as an entropy of tube positions. The additive thermal error is real; TD does not prove TS-theta.

## 3. WS2 and Theorem E given TS-theta — HOLDS AFTER CORRECTION

X:487–493,502–507. Credit the existing Theorem F for the sheet-power inequality. The normalized version is immediate from the trace eigenvalues: the odd numerator at doubled time is at most its square; the even denominator is at least the squared ground contribution. Hence
`F(2n_1,n_i)>=2F(n_1,n_i)-2log(1+s_+)`.
At the second sheet doubling the first error is doubled and the second error is added. The bound is therefore `4F-6log(1+s_*)`, as printed.

The precise repaired hypotheses are `0<theta<4`, `0<q<1`, one constant `C` independent of size, and the bounds on **both** intermediate sheet-frame thermal sums. TS must apply at `(2n,2n|n,n)`. If background twists are allowed, positivity and the projection formula must hold in each frame used. “Spatial in frame 1” alone does not ensure this after axis exchange. The untwisted case `m=0` has no such mismatch.

Put `r=4/theta>1`. Then

\[
 \Phi(2n)\ge r\Phi(n)-D,
 \quad D={6\over\theta}\log(1+s_*)+C,
 \quad \Phi_*={D\over r-1}.
\]

Subtracting `Phi_*` gives `Phi(2n)-Phi_* >= r(Phi(n)-Phi_*)`; iteration proves the claimed bound. This is a valid conditional theorem, with no input supplying TS or the uniform thermal bound.

The numerical seed description needs correction. For `theta=1,s_*=4`, the **odds** threshold is

\[
 q<5^{-2}e^{-C/3},\qquad
 p={q\over1+q}< {e^{-C/3}\over25+e^{-C/3}}.
\]

Only at `C=0` is this `q<1/25`, or `p<1/26`. There is no universal four-percent seed while `C` is unspecified. Nor does an upper bound of one on the fully centre-even thermal sum imply `s_+<=4`: the four sectors even under only one flip each have their own excited traces. A separate comparison of those traces is required. Increasing `C` can make TS vacuous and the seed unattainable; E retains that cost exactly.

A sufficient corrected bound is `s_+<=3+4S_ev`. Indeed Fourier projection over the three centre flips gives `Z_chi<=Z_0`, since every twisted partition function in that Fourier sum is positive. The one-flip-even space is the sum of four such charge sectors. Therefore its trace is at most `4lambda_0^t(1+S_ev)`. With `S_ev<=1`, one may use `s_*=7`, not the printed 4. At `theta=1,C=0` this yields `q<1/64` and `p<1/65`.

## 4. Lemma CX1 — HOLDS

X:519. Set `G_k=G(2^k n_0)` and `d_k=G_(k+1)-G_k`. Its hypothesis is exactly `d_(k+1)>=d_k`; hence

\[
 G_k=G_0+\sum_{j=0}^{k-1}d_j\ge G_0+kd_0.
\]

For `G=Phi`, `q_k<=q_0 exp(-kd_0)`. For a prescribed positive threshold `eta<q_0`, any integer `k>log(q_0/eta)/d_0` suffices. This supplies no sign of `d_0` or of the second difference for the gauge theory.

X:521's next paragraph proves only that separate convexity of two log traces does not establish convexity of their difference. Its claim that CVX is false in the model class is explicitly based on an ARGUED finite-size-scaling description, not a written in-class counterexample. CX1 does not validate that separate assertion.

## 5. “Coulomb has theta = 4 exactly” — FAILS for the printed TS

X:510–515. Two separate issues break this inference.

First fix the **compact free Maxwell comparison**, for which the harmonic calculation is valid. The derivation of `gap-z2parity-astra.md:487–501` extends to a rectangular box: the holonomy angle has inertia `n_j n_k/(e^2 n_i)`. At time `n_1`, its integer electric flux `l` has weight `exp(-tau l^2)`, with

\[
 \tau={e^2n_1n_i\over2n_jn_k},\quad
 E(\tau)=\sum_{l\ \mathrm{even}}e^{-\tau l^2},\quad
 O(\tau)=\sum_{l\ \mathrm{odd}}e^{-\tau l^2},\quad
 F_G(\tau)=\log{E(\tau)\over O(\tau)}.
\]

Other harmonic and oscillator factors cancel for this single parity. Doubling both transverse sides sends `tau` to `tau/4`. Positivity of `E-O` follows from Poisson summation of the alternating Gaussian sum, so `F_G>0`.

Here are hand bounds, with no numerical calculation:

\[
 \tau-\log3\ \le F_G(\tau)\le\tau+\log2\qquad(\tau>0). \tag{G1}
\]

For `tau>=1`, `E<=1+2/(e^(4tau)-1)<2`, while
`2e^(-tau)<=O<=2e^(-tau)/(1-e^(-8tau))<3e^(-tau)` and `E>=1`. These give (G1). For `0<tau<=1`, Poisson summation on `2Z` gives the common factor `sqrt(pi)/(2sqrt(tau))` times
`1+2 sum_(r>=1) a^(r^2)` for E and
`1+2 sum_(r>=1) (-1)^r a^(r^2)` for O, where `a=exp(-pi^2/(4tau))<1/8`. Thus `O/E>=5/9` and `F_G<log2`; the lower bound in (G1) is then negative. The elementary inequalities used are `pi>3`, `e<3`, and the Taylor lower bound `exp(9/4)>8`.

On the consumer shapes all sides lie in `{a,2a}`, so `tau<=2e^2`, independently of a. Therefore the **printed** TS holds in this massless comparison model with the explicit constants

\[
 \theta=1,\qquad C=2e^2+\log2,\qquad n_0=3. \tag{G2}
\]

Indeed its right side is nonpositive and its left side is positive. More generally every `theta>0` works with `C=(2e^2+log2)/theta`. A free additive constant prevents this bounded-shape condition from excluding the Gaussian Coulomb model.

The corrected statement about 4 has different quantifiers. If arbitrarily large sheet-to-transverse aspect ratios are allowed at fixed coupling, then `tau` is unbounded. The elementary leading terms give

\[
 F_G(\tau)=\tau-\log2+O(e^{-4\tau}).
\]

Hence `F_G(tau)/theta-F_G(tau/4)` is unbounded when `0<theta<4`. For `theta=4`, (G1) proves the inequality for all `tau>0` with
`C_4=log3+(log2)/4`. Thus 4 is the **least admissible exponent on unbounded aspect ratios**, not an exact linear law for F and not a selective exponent for the printed consumer shapes. The asymptotic difference at theta 4 tends to `-(3/4)log2`, so even the Gaussian F does not scale exactly by one quarter.

Second, standard compact lattice Villain theory is not this free harmonic law. Its full integer surface sum has additional sector-dependent weights, discussed below. Row 786 is a Langevin-gap theorem, as already recorded in `gap-hs-check-astra.md:207–211`; it cannot supply the missing equality.

The claimed split “TS false only for Coulomb; seed false only for deconfined” therefore FAILS. Already in the free comparison, Phi on symmetric tori is constant. If WS2 and TS hold with constants `s_*,theta,C`, their valid recurrence forces `D>=(4/theta-1)Phi`. Its seed cannot be strict. The additive constant and the thermal bound remain part of the discrimination; they cannot be dropped from the test.

## 6. TS-theta in low-temperature Z2, untwisted background — HOLDS

Use the existing cocycle-component bound (Z) of `gap-z2parity-astra.md:384–438`, whose geometry comes from Claude Opus's `gap-es1-opus.md`. This is an application of that result, not a new Peierls proof.

Let `a=min n_mu>=8`, `max n_mu<=2a`, `m=0`, and `beta>=5/2`. There are `N=6 product n_mu<=96a^4` plaquettes. Set `b=80exp(-2beta)`. The Taylor sum through degree seven gives
`exp(5)>648240/5040>128`, so `b<5/8`. Therefore the prior bound gives

\[
 \epsilon_a\le {16\over5}a^4(5/8)^{a^2}
 \le {16\over5}a^4 2^{-a^2/2}<\frac14. \tag{Z1}
\]

For the last inequality check `a=8`; thereafter the ratio of successive bounds is at most `(9/8)^4 2^{-17/2}<1`. Hence

\[
 0<R={Z^v\over Z^0}\le {\epsilon_a\over1-\epsilon_a}\le\frac13,
 \qquad q={1-R\over1+R}\ge\frac12,
 \qquad 0<F\le\log2.
\]

The enlarged torus also has `F>=0`. Consequently TS holds with the explicit, coupling-uniform constants

\[
 \boxed{\theta=1,\quad C=\log2,\quad n_0=8,\quad \beta\ge5/2,\quad m=0.} \tag{Z2}
\]

For every fixed `beta>(log80)/2`, the same argument gives `theta=1,C=log2` with an explicit cutoff choice. Put `lambda=2beta-log80>0` and take any integer

\[
 n_0\ge\max\left(3,{8\over\lambda},
 \sqrt{{2\over\lambda}\max\left(0,\log{24\over5(1-e^{-\lambda})}\right)}\right).
\]

Since `4log a<=4a<=lambda a^2/2` above that cutoff, (Z) is at most `1/4`. The exact threshold is `(log80)/2`; “above 2.191” is only a rounded description, not its exact endpoint.

This proves the requested large-beta test in the untwisted family. It proves neither the small/intermediate-beta TS statement nor uniformity in a nonzero fixed spatial twist m. The prior all-class estimate bounds `Z^k/Z^0`; it does not bound `Z^(m+v)/Z^m` by division when both terms are small. Those extensions are not silently claimed.

The result shows TS alone is compatible with deconfinement. It does not, by itself, prove that every possible choice of the seed constants fails; that would also require the stated thermal-sum hypotheses. The actual odds tend to one and F tends to zero in this large-torus Z2 regime.

## 7. The Q8/2T test narrowing — FAILS as an argument for exempting ES

X:178,231,275,287,435–437,553–560. The valid logical rule is: a comparison model refutes `H=>T` only when it satisfies H and fails that **same T**. A local mass gap does not imply every finite-volume seed, especially a trace seed counting all topological states. Thus the test for a confinement conclusion is not automatically a test for a local mass gap. This part of the narrowing HOLDS.

The further claim that frozen Q8 and 2T have small **ES**, so those groups are “void” tests for every direct ES route, is unsupported and has an explicit finite-box failure. Their centre-even sector retains noncentral flat holonomies. Z2 does not have these additional holonomies after its whole centre has been projected out.

Prior work used here: `gap-crux-skeleton-check-astra.md:305–306` already distinguishes flat spatial commuting triples from four-torus gauge-class counts, and warns that a gap alone is not a trace seed. `gap-q8test-check-astra.md:171–180` gives the relevant groups and centralizers. A direct search for centre-even Q8/2T flat-sector thermal bounds found no supplier; a broader “commuting triples” search on the five refs located continuous SU(N) holonomy statements in the older existence project, a different object.

Here is a short witness, avoiding any enumeration. For either `G=Q8` or `G=2T`, consider a fixed spatial torus of sides at least three. Flat gauge classes are commuting holonomy triples modulo simultaneous conjugation. The triples `(1,1,1)` and `(i,1,1)` lie in distinct orbits even after the three central flips: conjugation and multiplication by central signs cannot change whether the first entry is central. The indicators of their two orbits therefore give two orthogonal, gauge-invariant, centre-even flat vectors.

Normalize the one-link temporal matrix by its identity entry, so `k(g,h)=exp[-beta(1-ReTr(g h^(-1))/2)]`. Put `g=|G|`, `d_G=min_(h!=1)(1-ReTr(h)/2)`; thus `d_Q8=1` and `d_2T=1/2`. Let E be the number of spatial links and `z=exp(-beta d_G)`. In temporal gauge the transfer, on gauge-invariant functions, is a positive scalar times

\[
 T=D^{1/2}KD^{1/2},\qquad K=\bigotimes_{e=1}^{E}k.
\]

D is the normalized spatial weight. On flat configurations D is one; elsewhere it is at most z. Gauge projection commutes with these operators. The matrix `K-I` has nonnegative off-diagonal entries and row sum at most `(1+(g-1)z)^E-1`. For the orthogonal projection P onto flat configurations,

\[
 \|T-P\|\le\eta:=(1+(g-1)z)^E-1+z. \tag{FG1}
\]

This also holds after the centre-even projection. P has rank at least two there. Min-max gives `lambda_1>=1-eta`, while `lambda_0<=1+eta`. The finite-beta Perron vector is centre-even, so the normalizer is the same top eigenvalue as in ES. At integer time t,

\[
 S_{\rm ev}(t;B)\ge\left({1-\eta\over1+\eta}\right)^t\ge\frac12
 \quad\hbox{if}\quad
 \beta\ge {1\over d_G}\log\bigl(16E(g-1)t\bigr). \tag{FG2}
\]

For the last assertion, `E(g-1)z<=1/(16t)`, `exp(u)-1<=2u` for `u<=1/16`, so `eta<=3/(16t)<1/(4t)`. Then the ratio is at least `1-2eta>=1-1/(2t)` and Bernoulli's inequality proves the bound. On a cube at t=a, take `E=3a^3`. These are explicit finite couplings where the first number of ES is not small at the chosen box. No machine count is used.

This does **not** prove failure of ES at every box for one fixed finite beta, or locate a freezing transition. The frozen limiting transfer itself has at least two centre-even flat states at every box, so its even sum is at least one. This invalidates the claimed frozen-model justification for exemption. The finite-beta estimate shows the same obstruction at each specified box, not the failure of an existential seed at every box for one fixed beta. A future ES comparison must check its actual projected state count; this check leaves that fixed-beta existential question undecided.

The fixed-torus frozen ratios already in `gap-kappa-order.md:114–120` and `gap-z2parity-astra.md:444–483` also correct “F is tiny at every size”:

\[
 R_{Q8}\to3/23,\quad q_{Q8}\to10/13,\quad F_{Q8}\to\log(13/10);
 \qquad
 R_{2T}\to1/61,\quad q_{2T}\to30/31,\quad F_{2T}\to\log(31/30).
\]

These finite nonzero constants make TS harmless in the **frozen fixed-box limit**, with `theta=1,C=0` when every compared box is taken to that limit. They are not finite-coupling, uniform-in-size theorems. Their proven flux-countertest content must be retained; the claimed order-one transition locations remain GUIDE. The Z2 theorem is a separate, rigorous finite-beta test, not proof of the corresponding Q8/2T phase assertion.

## 8. Standard compact Villain U(1): exact reduction and the unresolved part

**Verdict on X's asserted Villain evaluation — FAILS.** The Gaussian evaluation is not an evaluation of the full compact lattice model of row 786. The meaningful positive-theta TS statement for that model is **not decided here**. This is an unresolved model question, not a counterexample and not a fourth check verdict for a proved statement.

Fix the actual convention of `gap-tu-retry.md:61–74`:

\[
 \phi_\beta(t)=\sum_{r\in\mathbb Z}e^{-r^2/(2\beta)}e^{irt},
 \qquad Z=\int\prod_p\phi_\beta((dA)_p)\,dA.
\]

Absolute convergence allows termwise integration on a fixed finite torus. Let `L=ker(delta_2) intersect Z^P`, and let sigma represent the temporal pi-twist. Character orthogonality gives the exact formulas

\[
 Z^0=\sum_{n\in L}e^{-\|n\|^2/(2\beta)},\qquad
 Z^v=\sum_{n\in L}(-1)^{\langle n,\sigma\rangle}e^{-\|n\|^2/(2\beta)},
\]

\[
 q_V={\sum_{n\in L:\langle n,\sigma\rangle\ \mathrm{odd}}e^{-\|n\|^2/(2\beta)}
 \over\sum_{n\in L:\langle n,\sigma\rangle\ \mathrm{even}}e^{-\|n\|^2/(2\beta)}}. \tag{V1}
\]

This is a positive integer-surface formula for the odds. It does not remove the integer constraint.

For clarity decompose by the six integral homology numbers `w`. Let `n_w` be a sum of coordinate planes representing w, `h_w=P_h n_w`, and `b_w=n_w-h_w`. Integer boundaries form `K_c=delta_3 Z^C`. The integer homology of the cubical four-torus is free of rank six, so each sector is `n_w+K_c`. Orthogonality gives

\[
 Z_w=\exp\!\left[-{1\over2\beta}
 \sum_{\mu<\nu}{n_\mu n_\nu\over\prod_{\rho\ne\mu,\nu}n_\rho}w_{\mu\nu}^2\right]
 A_w,\qquad
 A_w=\sum_{k\in K_c}e^{-\|b_w+k\|^2/(2\beta)}. \tag{V2}
\]

The numerator and denominator in (V1) sum (V2) over odd/even `w_(1i)`. The Gaussian formula deletes the dependence of `A_w` on w. No cited theorem permits that deletion.

An elementary fixed-box check shows why equality cannot hold identically in beta. Put `A=n_1 n_i`, `B=n_j n_k>1`. Every odd integer closed surface meets each of the A transverse cuts with a nonzero odd integer sum. Thus its squared norm is at least A. Equality consists precisely of a flat oriented `(1,i)` plane, of either sign, at one of B transverse positions. (Closure forces its position to remain constant between adjacent cuts.) The even sum contains the zero current. Consequently, at fixed box as `beta` tends to zero,

\[
 q_V=2B\,e^{-A/(2\beta)}(1+o(1)),\qquad
 q_G=2e^{-A/(2\beta B)}(1+o(1)). \tag{V3}
\]

The Gaussian tails over the finite-rank integer lattice justify the indicated remainder without enumeration: the next squared norms are separated by a positive integer. The exponents disagree. In particular equal-aspect cubes of different sides have different Villain odds as analytic functions of beta. The finite-volume partition functions are real analytic for `beta>0`; equality on any whole open coupling interval would extend to all beta, contradicting (V3). This refutes an **exact** finite-lattice Gaussian identification throughout a purported Coulomb interval. It does not refute an infrared asymptotic comparison.

Three attempted routes to positive-theta TS stop at distinct explicit estimates:

1. **Harmonic factorization:** (V2) is exact, but the needed relative estimate on `A_w` is absent. For instance a uniform upper bound on `F_V` on the bounded-aspect family would suffice for TS. Formula (V2) alone supplies no such bound on the odd/even sum ratio.
2. **The existing periodic covariance theorem:** PV (7.3), its Hodge image, and row 786 control exact/coexact fluctuations. Homology is fixed on each such affine coset. The harmonic contribution is not controlled from below. Thus their covariance estimate cannot supply the missing relative weights by the law of total covariance. This is the same observable/sector mismatch already noted in the prior check, not a failure of PV's theorem.
3. **Direct flux insertion:** adding one flat integer plane of squared norm A bijects the even and odd homology classes. Pairing the insertions with their negatives gives only an area-cost estimate of order `exp(-A/(2beta))`; spreading the plane fractionally would leave the integer-current lattice. That estimate grows with `a^2` in F and does not prove a size-independent TS constant. In the primal image formula, a smooth pi-flux shift instead bounds the twist ratio from below; that gives a **lower** bound on F, the wrong direction for making TS trivial.

For route 3 the exact bound is worth recording. If P is one flat unit plane, the odd sum equals
`exp(-A/(2beta)) sum_(n even) exp(-||n||^2/(2beta)) exp(-<n,P>/beta)`.
The even ensemble is invariant under `n -> -n`, so its last factor averages to a cosh, at least one. Hence `q_V>=exp(-A/(2beta))`, or `F_V<=A/(2beta)`. It does not stay bounded on the required family. This elementary injection is a diagnostic, not the required flux-spreading theorem.

A precise missing sufficient input, for fixed beta in the intended weak-coupling range, is

\[
 \inf_{a\ge a_0}\ \inf_{n_\mu\in\{a,2a\}}
 {\sum_{w:w_{1i}\ \mathrm{odd}}e^{-\|h_w\|^2/(2\beta)}A_w
  \over\sum_{w:w_{1i}\ \mathrm{even}}e^{-\|h_w\|^2/(2\beta)}A_w}
 \ge c_\beta>0. \tag{V4}
\]

Then `theta=1,C=-log c_beta` would prove TS immediately. V4 is sufficient, not claimed necessary or equivalent. A comparison directly between the two sizes in TS might avoid it. Neither (V4) nor that direct comparison is proved or refuted by this check. The weaker conclusion “row 786 implies V4” is false as an inference: its observable and dynamics are different.

Thus the fully compact, fixed-beta Villain decision requested in the brief remains an open part of this output. No Gaussian replacement, finite-volume limit in beta, or numerical run has been counted as its solution. The free/no-monopole comparison is decided in section 5, with its different model and quantifiers explicit.

There is also a literal quantifier defect: with only `theta<4` as printed, `theta=-1,C=0` makes TS automatic for every finite `F>=0`, including both lattice models. It cannot produce Theorem E's growth. Throughout the substantive model discussion, TS has the repaired condition `0<theta<4`; the negative-theta loophole is not counted as a solution of that intended problem.

## Check disposition and remaining work

| Requested statement | Verdict | Exact scope |
|---|---|---|
| F5 variational inequality | HOLDS | Eigenvalue branches and admissible h as stated in section 1. |
| F5 square-root/volume conclusion | HOLDS AFTER CORRECTION | A fixed interval curvature bound is needed; extensivity and finite-volume closure are not consequences. |
| TD | HOLDS | Both crossed-frame positive transfers and `b<=a`. |
| TD “free law” | HOLDS | Exactly for the zero-thermal-sum case specified in its sentence; no generic free-field identification. |
| WS2 and E given TS | HOLDS AFTER CORRECTION | `0<theta<4`, valid intermediate frames, actual thermal sums and C retained; the sample `s_*=4` is not supplied. |
| CX1 | HOLDS | Conditional discrete convexity only. |
| “U(1) has theta 4 exactly” for the printed TS | FAILS | The bounded-aspect Gaussian model has theta 1 with (G2). Four is optimal only on unbounded aspect ratios. |
| Q8/2T narrowing | FAILS as an argument for the stated blanket exemption | The conditional-comparison logic holds; local gappedness does not supply ES. The fixed-beta existential ES question for those groups is not settled here. |
| Low-temperature Z2 TS | HOLDS | (Z2), m=0; neither all couplings nor nonzero m is claimed. |
| Exact compact-Villain Gaussian evaluation | FAILS | (V1)–(V3) retain missing sector weights. Positive-theta TS for the full model remains unresolved. |

No numerical experiment, enumeration, interval calculation, Lean run, audit, or external post was performed. The existing source notes, registry, FINISH and scientific status were not changed. No new claim about the entire SU(2) route, mass gap or finite-coupling phase diagram follows.

The open item from this brief is a positive-theta TS proof or counterexample for **full compact Villain at fixed beta**, with the intended shapes and background quantifiers. Equation (V4) is one sufficient missing bound, not a replacement goal claimed solved. Extension of the Z2 test to all spatial backgrounds is also unproved here. The current report is saved at the requested path and remains local, uncommitted and unpushed.

RESULT: HOLDS — F5's variational inequality, TD and its zero-thermal-sum law, CX1, and untwisted Z2 TS for beta>=5/2 with theta=1,C=log2,n0=8; HOLDS AFTER CORRECTION — F5's square-root interpretation and Theorem E with its actual thermal and seed constants; FAILS — the printed Coulomb theta=4 selectivity, the exact compact-Villain Gaussian identification, and the argument exempting Q8/2T from every ES test. Full compact-Villain positive-theta TS and the nonzero-background Z2 extension remain unresolved. Research check only; no status or mass-gap claim.
