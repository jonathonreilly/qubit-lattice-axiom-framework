# Repo search

The target statements and methods were searched on `origin/main`, `pr/10114`, `pr/10133`, `pr/10134`, and `pr/10141` before derivation. The direct predecessors are row 754's product-rule bound and the existing correction retaining its exponential remainder.

This is a research-text check of FINISH row 883; it grants no scientific or audit status. No computer-assisted step will discharge a claim. The required prior record `library/prior/gap-brainstorm2-check-astra.md` is absent.

Search completed before derivation. Commands used bounded `git grep -n -i -E ... -- '*.md' '*.tex' | head` in `/Users/jonreilly/Projects/Physics`. Refs read: `origin/main` = `993f5e4f6d11a7e20a1cab9612c5749a53bae073`; `pr/10114` = `f76f6c649cff7dffbab664d8976e680e8f287fe9`; `pr/10133` = `89faef229ff6e6bde42baad15ed8270c2f4087d8`; `pr/10134` = `1e70c7211a2cdbc39001e619f1dd89db45e25851`; `pr/10141` = `c73ad7b177d94f89ff37b77386936e3d52b48b05`.

Terms: `FUSE-suff`, `Lemma SQ`, `Theorem SQ`, `SQ-F`, `Lemma RPF`, `KURT`, `flux ground state`, `fourth moment.*flux`, `fusion by squaring`; then `fusion by the product rule`, `transverse reflection positivity`, `Var_pi(f^2)`, `two.torelon`, `flux.*fourth.moment`, `FUSE-h`, `F-h.*fusion`, `kurtosis.*ground`. The second search returned no hits. The first returned name collisions: the soft-route `SQ.md:466` concerns a deviation square function; `parts/witness.md:535` on pr/10134 concerns a Gaussian plaquette fourth cumulant; `docs/CLOSURE_T2_M1_M2_DISTINGUISHER_NOTE_2026-05-10_t2m1m2.md` concerns beta-distribution kurtoses; the composite-network and native-electric-defect notes concern different flux models; `outputs/faster_three_site_2026_10_17/proofs/three_site_faster_nominal_check__REVIEW.md` concerns a displacement density. None states the requested flux-eigenfunction inequality. These are search-level exclusions, not claims to have reviewed those unrelated proofs.

Relevant hits in the pinned checkout (paths below are relative to this lane):

| Source | Exact statement used | Closeness and reuse |
|---|---|---|
| `library/gap-loop-eq-opus.md:196–208`, Claude Opus 5.5, row 754 | `1-r_1 <= 4 ‖f‖_inf^2 Dir(f)/Var_pi(f^2)`; its Corollary 6.3 gives `p_chi <= Theta_chi max(S_ev^(1/(4c)), exp(-a/(4c)))`. | Direct predecessor of SQ and SQ-F. The new note sharpens its eigenfunction estimate; it does not originate fusion through positivity. Row 754 is this file, not `gap-es1-opus.md`. |
| `library/gap-loop-eq-check.md:425–512`, Codex gpt-6-astra | The displayed maximum holds; PK and LOC do **not** imply a pure power of S. A continuous SU(2) kernel has `S=eta^a`, `p=q^a/(1+eta^a)`, fixed `q=1/8`. | Already settles the maximum-versus-pure-power issue. Reuse this counterexample below, without a duplicate attack. |
| `library/gap-fusion-astra.md:65–94` | The corrected electric bound is `Theta_chi[S^(1/(4c))+exp(-a/(4c))]`; light-sector bounds, small even sums, and other magnetic backgrounds remain separate. | The same correction is already carried downstream. |
| `library/gap-es1-opus.md:200–236`, Claude Opus 5.5 | FUSE-suff assumes both `p_z<=K sqrt(S)` outside a four-sector set L and `s_z<=KS` on L; it gives `Delta<=12K sqrt(S)+4KS+S'`. | Exact consumer. It does not assume an absolute confinement pattern, but it does require both clauses. |
| `library/gap-es1-opus-check.md:370–405`, Codex gpt-6-astra | The displayed consumer bounds hold; its numerical sufficient condition uses `max(1,K)`. | Existing arithmetic correction, retained here. |
| `library/gap-expose-astra.md:575–599` | E17 is `Q_F<=C a^p eta_*^(a/2)`; with `S_ev>=eta_*^a` it supplies FQ. | A sufficient absolute flux bound. It is a trace statement, not an eigenfunction-moment statement. |

`library/prior/repo-search-2026-11-08.md` was read. It concerns other targets and supplies no SQ or RPF result. FINISH row 883 contains no separate “Repo prior work” paragraph. The registry search for the target names and fusion labels found no competing owner; its two LOC matches concern label locality, a different object. This check neither takes over KURT nor tries to prove it.

The SA index README, matching chunk rows and neighbouring rows, and `obligations.md:82–99` were consulted first. Searches for kurtosis, fourth moment, flux sector, electric flux, fusion, ground state and Markov found no indexed supplier of SQ or SQ-F; the fourth-moment hits are Gaussian recursion, not flux eigenfunctions. For RPF, `chunk-03.md` points to SA 2811–2818 and 2862–2879: the coordinate-site reflection form is an integral of squares, and AM5 proves reflection Cauchy–Schwarz. These source lines were read and are reused. SA 3198–3254 gives a different plateau: a polynomial bound relative to the invariant conditional field on the infinite lattice. It is not the finite-cylinder exponential bound being checked. Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for those inputs. No Balaban paper or complete-account assertion is imported into the arguments below; Tadeusz Balaban's renormalization work is background to the lane only.

## Provenance and scope

Checker: OpenAI Codex, task-specified runner gpt-6-astra xhigh, 2026-11-13. Source checkout: `a109aaa74bef91f06f553e2389c44a1bbbc709b6`. Author checked: Claude Fable 5.2 max, row 876. This file records a research-text check, not an audit or a status change. References to the source's later corrections are part of the statement checked. Scripts only read or write text and identify sources; no numerical run or computer-assisted proof is used.

Scope: SQ, SQ-F, diffusion/window statements, RPF/plateau, and the claimed consumer reduction and comparison of hypotheses. The brainstorming catalogue, toy runs, confinement claims about rival phases, and original literature recollections are not validated. The physical transfer kernel is reused from `library/gap-transfer.md:108–181`: a gauge average of a strictly positive continuous temporal kernel, positive as an operator, with a simple positive continuous vacuum. The source's gauge-invariant Hilbert space and order-two centre characters remain attached.

Checkpoint: requested checks complete; verdicts were appended one at a time below. Open obligations are KURT, the half-time prefactor, the exponential error budget, F-l, other magnetic backgrounds and the small even sums. No source, FINISH row, registry or audit record is edited. The output remains uncommitted in the requested pinned checkout; no push or external post was made.

## 1. Ground-state transform — HOLDS

Source 389–391. Normalize Omega in L2(dU). The unitary `Uf=Omega f` satisfies `U P U^{-1}=L/lambda_0`. The identity `L Omega=lambda_0 Omega` gives `P1=1`. Its joint measure is

\[
 \mu(dx)P(x,dy)=\lambda_0^{-1}\Omega(x)L(x,y)\Omega(y)\,dx\,dy,
\]

which is symmetric. Thus mu is stationary and P is reversible. Simplicity makes Omega invariant under each flip: its transformed positive unit eigenvector must equal Omega. Continuity and compactness give a strictly positive minimum of Omega. All statements hold at each finite box; no cutoff-uniform lower bound is asserted.

## 2. Lemma SQ — HOLDS

Source 393–394. Let `(X_0,X_t)` have the stationary Markov law for P, and put `G=g(X_0)`, `Y=g(X_t)`. Conditional variance gives the exact identity

\[
 \langle g^2,P^t g^2\rangle-\theta^{2t}\kappa
 =\mathbb E\!\left[G^2\operatorname{Var}(Y\mid X_0)\right]\ge0.
\]

Here `E[Y|X_0]=theta^t G`. Fourth integrability makes the left side finite: stationarity and Cauchy–Schwarz bound `E[G^2Y^2]` by kappa. This checks the pointwise Schwarz step through a stationary joint law. It needs a real eigenfunction and a Markov kernel; neither reversibility nor nonnegative spectrum is needed for this lemma. Integer `t>=1` is the stated range.

## 3. Theorem SQ and its energy consequence — HOLDS AFTER CORRECTION

Source 396–402, read with the author's correction at 499. The intended Wilson statement holds. Its abstract statement must explicitly require a real normalized eigenvector in a character with `chi^2=1`, a nonzero sector eigenvalue, and `L>=0` as an operator for all integer times. A strictly positive pointwise kernel alone does not give nonnegative spectrum. The author's correction at 499 already supplies the last requirement. “Every group” at 402 means its order-two parity sectors, not arbitrary charge characters.

With those hypotheses set `h=g^2-1`, `theta=lambda_chi/lambda_0` and `rho=lambda_1^+/lambda_0`. Continuity of `Psi=L Psi/lambda_chi` and the positive minimum of Omega give bounded g. Order two makes h invariant under **all** centre flips. Its norm squared is `kappa-1`, and its mean is zero. Spectral resolution on that subspace gives

\[
 \langle g^2,P^t g^2\rangle
 =1+\int_{[0,\rho]}s^t\,d\nu_h(s)
 \le1+(\kappa-1)\rho^t.
\]

Combining with section 2 proves exactly

\[
 \theta^{2t}\le\kappa^{-1}+(1-\kappa^{-1})\rho^t.
\]

For t=1 self-adjointness suffices for the spectral upper bound; for even t negative eigenvalues would invalidate that step without the extra hypothesis. The theorem includes kappa=1, when it gives only `theta^(2t)<=1`. At finite positive Wilson coupling on connected `SU(2)^E`, a continuous nonzero odd g actually has kappa>1: equality would force `g^2=1` everywhere, hence g constant by connectedness, contradicting oddness. This supplies no uniform separation from 1.

For positive theta and rho, `1-e^{-2E} >= (1-1/kappa)(1-e^{-m})` is exact, where `E=-log theta`, `m=-log rho`. Since `1-e^{-2E}<=2E`, the stated lower bound for E follows. Zero eigenvalues are handled before taking logarithms or by the extended-energy convention. No localization or clustering estimate enters.

## 4. Diffusion identity and the factor 4/3 — HOLDS AFTER CORRECTION

Source 404 (also 279). The algebra and constant hold. State the analytic domain and the meaning of m: H is a conservative symmetric diffusion, its form obeys the chain rule, g is a real normalized order-two eigenfunction with `Hg=Eg`, `kappa>1`, and the chain rule and integration by parts below are legitimate. In particular `g^2-1` must lie in the even form domain, and testing the eigen-equation by `g^3` must be justified. Smooth eigenfunctions of the finite-volume compact Hamiltonian have this property. Here m is the bottom of the **even, vacuum-orthogonal** spectrum, not the full gap.

Writing the form as `Ecal(u,v)=int Gamma(u,v) dmu`, the weak eigen-equation tested with g cubed gives

\[
 E\kappa=\mathcal E(g,g^3)=3\int g^2\Gamma(g)\,d\mu,
 \qquad
 \mathcal E(g^2,g^2)=4\int g^2\Gamma(g)\,d\mu.
\]

The Rayleigh inequality for `g^2-1` therefore gives

\[
 m(\kappa-1)\le\tfrac43 E\kappa.
\]

For the variance-one Ornstein–Uhlenbeck law, `g=x`, `Hg=g`, `kappa=3`, and `H(x^2-1)=2(x^2-1)`. Thus the quotient is 2, as claimed. A separate hand check uses `H=-d^2/dx^2` on the uniform circle, centre flip `x->x+pi`, and `g=sqrt(2) sin x`: `E=1`, `kappa=3/2`, `g^2-1=-cos(2x)`, and its even Rayleigh quotient is 4. The displayed bound also equals 4. Both checks use exact identities.

A ground-state transform of a compact kinetic Laplacian plus a smooth real potential has a diffusion form: in `Omega^{-1}(H_phys-E_0)Omega`, the zero-order term cancels by the ground-state equation. Thus the finite-lattice Hamiltonian application retains its usual domain and real-vacuum hypotheses. No assertion about `-log` of the discrete transfer operator follows from this product rule. The source correctly distinguishes them.

## 5. The window statement — HOLDS AFTER CORRECTION

Source 406; earlier formulation 280. Both displayed bounds at 406 hold. From SQ at t=1,

\[
 \kappa(\theta^2-\rho)\le1-\rho,
 \qquad
 \kappa-1\le\frac{1-\theta^2}{\theta^2-\rho}
 \quad(\theta^2>\rho).
\]

The diffusion estimate similarly gives
`kappa <= m/(m-4E/3)` when `E<3m/4`. The earlier `m/(m-2E)` bound under `E<m/2` is a valid weaker consequence, not the sharp diffusion version.

The last sentence needs a discrete-time qualification. In the diffusion case `E/m->0` does force kappa to 1. For one discrete step the sufficient condition is `(1-theta^2)/(1-rho)->0`, not merely `E/m->0`. The already existing kernel of `gap-loop-eq-check.md:474–505` has `theta=1/8`, `rho=eta->0`, `kappa=2`. Hence `E/m=log(8)/log(1/eta)->0` while kappa stays 2, even though `theta^2>rho` eventually. This reuses the prior counterexample.

Once kappa tends to 1, the claimed L4 proximity is valid. Choose `s(x)=sign(g(x))`, with either sign at zeros. Pointwise,

\[
 |g-s|^4=(|g|-1)^4\le(g^2-1)^2,
 \qquad \|g-s\|_4^4\le\kappa-1.
\]

This says that g is nearly sign-valued. It does not prove spontaneous symmetry breaking, degeneracy, or the required light-sector estimate.

## 6. The fourth-moment identities — HOLDS

Source 408. The flux law has density `g^2` relative to mu. Its chi-square divergence is therefore `int(g^2-1)^2 dmu=kappa-1`; this is also the squared norm of the even mean-zero component of `g^2`. Equality kappa=1 is exactly `|Psi|=Omega` almost everywhere.

For the conditional-expectation claim put `A=E[g^2|F]` and `b=E[g|F]`. Conditional variance and Schwarz give

\[
 \mathbb E(g^2-1)^2\ge\mathbb E(A-1)^2
 \ge\mathbb E(A-1)_+^2
 \ge\mathbb E(b^2-1)_+^2,
\]

because `A>=b^2`. This verifies the inequality without assuming independence of the two halves or a sign for mixed terms.

## 7. Multiplicity elimination and Theorem SQ-F — HOLDS

Source 486–494. Use the periodic magnetic background, `p_chi(t)=Z_chi(t)/Z_0(t)` and `S(t)=Z_0(t)/lambda_0^t-1`. These are sector ratios, not E17's odd fraction divided by the full partition function. For integer `t>=3`, the electric Fourier formula gives

\[
 0\le Z_\chi(t)=\tfrac18\sum_e(-1)^{\chi\cdot e}Z^e(t)
 \le\tfrac18\sum_e Z^e(t)=Z_0(t).
\]

The first inequality is spectral positivity; the second uses the positive Boltzmann integrals `Z^e`. Thus for even `a>=6`,

\[
 \Theta_\chi=\frac{Z_\chi(a/2)}{\lambda_0^{a/2}}
 =p_\chi(a/2)[1+S(a/2)]\le1+S(a/2).
\]

No crossing symmetry at the unequal times is needed. Spectral calculus in the chi sector, and `Z_0(a)>=lambda_0^a`, give

\[
 p_\chi(a)\le\Theta_\chi\theta^{a/2}.
\]

For kappa>1 put `u=1-theta` and `c=2 kappa/(kappa-1)`. SQ gives `1-rho <= c u`, since `1-theta^2 <=2u`. When `cu<=1/2`, integrating `(1-x)^{-1}<=2` on `[0,cu]` gives `log(1-cu)>=-2cu`. Hence `S(a)>=rho^a>=exp(-2cua)` and
`theta^(a/2)<=exp(-ua/2)<=S(a)^(1/(4c))`.
When `cu>1/2`, `exp(-ua/2)<exp(-a/(4c))`. Finally `1/(4c)=(kappa-1)/(8 kappa)`. Therefore the displayed SQ-F estimate, with its **maximum retained**, is correct:

\[
 p_\chi(a)\le[1+S(a/2)]\max\{S(a)^{\gamma_\chi},e^{-\gamma_\chi a}\},
 \qquad \gamma_\chi=\frac{\kappa_\chi-1}{8\kappa_\chi}.
\]

For kappa=1 its limiting statement has gamma=0 and is just `p_chi<=1+S(a/2)`; the proof must not divide by kappa-1 there. At positive finite Wilson coupling section 3 excludes that case. An empty or zero-eigenvalue sector has zero numerator and is handled separately.

The comparison to row 754 is correct: for the eigenfunction, the new bound is `Dir(g^2)<=kappa(1-theta^2)`, instead of `4||g||_inf^2(1-theta)`. Since `kappa<=||g||_inf^2` for `||g||_2=1`, this improves the coefficient. The independent density-of-states assumption MULT is unnecessary for the **displayed bound**. Uniform control of `1+S(a/2)` is still necessary when that factor is to become a cutoff-independent constant.

## 8. “KURT alone supplies the electric F-h” — FAILS

First failing inference in the final corrected discussion: source 496, repeated at 506 and 511. SQ-F proves a maximum with an exponential remainder and a half-time prefactor. Remark 6.1 of row 754 requires a pure power with a controlled constant; it cannot remove either issue.

This is already covered by `gap-loop-eq-check.md:474–512` and carried into `gap-fusion-astra.md:70–94`. Reuse its kernel on Haar SU(2): `f=tr U`, `h=f^2-1`,

\[
 K_\eta(U,V)=1+\tfrac18 f(U)f(V)+\eta h(U)h(V),
 \qquad 0\le\eta<1/36.
\]

The cited hand proof gives positivity, the eigenvalues `1,1/8,eta`, and `Ef^2=1`, `Ef^4=2`. Hence the very same example satisfies KURT with `kappa=2`, while `S=eta^a` and `p_chi=8^{-a}/(1+eta^a)`. At fixed a and eta tending to zero, no fixed K and positive exponent bound p by `K S^gamma`. Thus the existing counterexample applies to KURT too. It is a counterexample to the inference from these kernel hypotheses, **not** a Wilson-action counterexample or a model of all crossing identities.

A correct conditional replacement, with `gamma_0=c_0/[8(1+c_0)]`, `S<=1`, and an additional uniform bound `1+S(a/2)<=B_0`, is

\[
 p_\chi(a)\le B_0\,[S(a)^{\gamma_0}+e^{-\gamma_0 a}].
\]

The remainder can be made smaller than a fixed tolerance by choosing sufficiently large lattice a. This is useful, but it must appear in the consumer's arithmetic. Alternatively, an additional uniform lower bound `S(a)>=e^{-M a}`, with finite `M>0`, absorbs it into a pure power: for `alpha=gamma_0/max(1,M)`, the maximum in SQ-F is at most `S^alpha` when `S<=1`.

There is an existing fixed-coupling supplier for the latter alternative: `gap-fusion-astra.md:95–137` gives
`S(t)>=eta(beta)^t`, `eta(beta)=e^{-80 beta}r(beta)^4/[4+16r(beta)^4]`.
On a compact positive beta interval it supplies finite uniform M. Credit that prior witness; do not reprove it. This particular bound does not supply a cutoff-independent M on a trajectory with beta tending to infinity. No such uniform comparison is proved in the checked note.

Also, small `S(a)` does not by itself bound `S(a/2)` from above uniformly in the cutoff: the latter sums square roots of the nonnegative terms summed by the former. A bound on their number or on the half-time sum is additional. Eliminating MULT is valid; eliminating every prefactor obligation is not.

## 9. Lemma RPF — HOLDS AFTER CORRECTION

Source 426–434. The displayed correlation inequality holds from the two named inputs, for nonnegative **integer** lattice times. Its assertion that Phi is fully centre-even needs a qualification: O must have a definite character of the full centre-flip group, and reflection must preserve that character. Oddness under direction 1 alone, as printed, only makes Phi even under that one flip. A winding line in direction 1 has the required full character. Without it, the inequality below still holds, but its spectral consumer must use the sector even under the specified flip, not the completely trivial character sector.

To check the inequality directly, use the reflection-positive form `(A,B)_R=<A theta_2 B>`. Normalization gives `(1,1)_R=1`. For `F=O_0 O_t`, its support lies in the positive spatial half and Schwarz against 1 gives

\[
 |\langle O_0 O_t\rangle|^2
 \le\langle O_0 O_t O'_0 O'_t\rangle
 =\langle\Phi\Omega,(L/\lambda_0)^t\Phi\Omega\rangle.
\]

The last equality is the time transfer identity; it also holds at t=0 as an equal-time identity. The vacuum part of `Phi Omega` is `C Omega`, and the mixed terms with phi vanish. This proves exactly

\[
 \langle\phi,(L/\lambda_0)^t\phi\rangle\ge f(t)^2-C^2.
\]

No connected four-point sign or clustering estimate was used. Spatial RP itself also gives `C=<O theta_2 O> >=0`. The finite-torus coordinate-site proof in SA 2811–2818 and AM5 supplies RP; taking the cylinder limit preserves it for these bounded finite-time tests. This is an input reused from Sussman and Alpoge's text, not a newly proved all-mirror theorem.

The sector correction matters algebraically: if O contains characters chi and psi, its product with its reflection contains cross terms of character chi times psi. Both characters can be odd in direction 1 while their product is nontrivial in another direction. The source supplies no cancellation of those terms.

## 10. RPF plateau and its proved spectral consequences — HOLDS AFTER CORRECTION

Source 436–439. Retain section 9's full-character hypothesis and integer-time restriction. Write `Q=L/lambda_0` on `L2(dU)`; this is the unitary image of the Markov operator P. Then phi is even and orthogonal to Omega, with
`V=||phi||^2=E_mu Phi^2-C^2 <=1-C^2`. Positive spectral calculus gives

\[
 f(t)^2\le C^2+V\rho^t
 \le C^2+(1-C^2)\rho^t\le C^2+\rho^t.
\]

This proves the printed plateau, with a slightly stronger coefficient. At t=0 use `rho^0=1`. It gives no bound on C itself.

For the thermal-sum consequence, take integer `t>=1` and `t'>=t`. If V>0, the normalized spectral measure of phi lies in the even excited spectrum. Jensen applied to `x->x^(t'/t)` gives

\[
 S_{\rm ev}(t')\ge\frac{\langle\phi,Q^{t'}\phi\rangle}{V}
 \ge\left(\frac{\langle\phi,Q^t\phi\rangle}{V}\right)^{t'/t}
 \ge(f(t)^2-C^2)_+^{t'/t}.
\]

If V=0, omit the undefined quotients; RPF gives `(f(t)^2-C^2)_+=0`, so the final inequality is still true. The spectral assertion permits real t' once the power and trace are defined; RPF was only used at the integer time t.

For the “two tubes” bound additionally take `f(t)>0` and `f(t)>=2C`. Then `rho^t >= f(t)^2-C^2 >=3 f(t)^2/4`, which yields
`m <=2 E_eff(t)+log(4/3)/t`. The zero observable must not be fed into `log f(t)`. The later optimization over a real time in Stage 3 is not supplied by the integer-time RPF statement; neither that argued optimization nor its transverse-box comparison is used here.

## 11. What FUSE-suff actually consumes

**No absolute confinement pattern is required — HOLDS.** Source 504's narrower reframing follows directly from `gap-es1-opus.md:204–217`. The light set L can be any four crossed sectors satisfying the hypotheses. The bounds depend on their weights and thermal sums, not on selecting the confining pattern. This observation and the allowance of any fixed positive exponent already belong to Theorem V, FUSE-suff and row 754's Remark 6.1. Credit those results; this is not a newly established consumer.

**“The consumer needs only F-h” — FAILS literally.** It also needs F-l for all four light sectors, small even sums on the required boxes, and the stated smallness inequality. The note acknowledges F-l at 415 and 496, which must qualify its summary. F-h must cover all twelve heavy crossed sectors at all three shapes. SQ-F proves only the periodic-background electric estimate. A lower bound on kappa at an unspecified notion of “not light” does not select the consumer's four-sector set or bound its sector thermal sums.

The complete arithmetic can retain the remainder. Suppose, in addition to F-l, **all twelve** heavy sectors obey
`p_z <= B_0(S^gamma_0+exp(-gamma_0 a))`, with the same constants on the three shapes. Set `R=S^gamma_0+exp(-gamma_0 a)`. If `6B_0 R+2K_l S<=1/2`, Theorem V gives

\[
 \Delta(c,d)\le12B_0R+4K_l S+S',\qquad
 \delta\le7\max_{c,d}\{12B_0R+4K_l S+S'\}.
\]

This is the valid consumer with an error budget. It still requires a uniform half-time bound for B_0, sufficiently small even sums, the light-sector bounds, and a choice of a that pays for the exponential. It proves no new physical-scale estimate by itself.

**Magnetic-background extension — not supplied by SQ-F.** Applying SQ to `T_(B,m)` uses its own vacuum, own even spectrum and own even trace. That is a legitimate same-operator implication for nonzero electric characters, but it does not identify any of these quantities with the periodic ones. When (0,m) is light, F-l does bound its same-background thermal sum at time a by K times the periodic sum. It does not by itself compare the two top even gaps or control the half-time prefactor. For a purely magnetic heavy sector (`chi=0`) the relevant ground-state ratio in its own transformed space is the constant 1, so squaring supplies nothing. The author correctly leaves the dyonic comparison open at 496; “the flux half leaves the crux” at 416 or 511 must not erase it.

## 12. Is KURT genuinely weaker than LOC or E17? — FAILS as a claimed logical weakening

Source 359–360, 413–422, 488, 496 and 511. The improved estimate for the **same eigenfunction** is real. But LOC is existential over trial functions, while KURT concerns the actual top flux eigenfunction. E17 concerns traces and a specified decay rate. Neither a change of object nor fewer symbols establishes a weaker hypothesis. The note gives no implication from either original condition to KURT.

Here is a hand-checkable separation within the abstract positive-kernel setting, on connected SU(2). It tests the claimed ordering, not the Wilson model. Write `x=tr(U)/2`, `f=tr U`, `h=f^2-1`, and use normalized Haar measure. The moments already proved in row 754's check give `Ef=Eh=0`, `||f||_2=||h||_2=1`, `Var(f^2)=1`, `||f||_infinity=2`, `||h||_infinity=3`. Define

\[
 g_n(U)=\frac{\tanh(nx)}{\|\tanh(nx)\|_2},\qquad
 K_n(U,V)=1+\tfrac14 g_n(U)g_n(V)+\tfrac1{16}h(U)h(V).
\]

The Haar set x=0 has measure zero. Dominated convergence gives `||tanh(nx)||_2->1`, `kappa_n=E g_n^4->1`. For all sufficiently large n, `||g_n||_infinity^2<=5/4`. Consequently

\[
 K_n\ge1-\tfrac14\tfrac54-\tfrac1{16}9=\tfrac18>0.
\]

The functions 1, g_n and h are orthonormal: g_n is odd under `U->-U`, h is even. Therefore K_n is a continuous reversible Markov kernel, positive as an operator, with eigenvalues `1,1/4,1/16` on these functions and zero elsewhere. Its unique top odd eigenfunction is g_n. It is uniformly separated from the vacuum, but no n-uniform KURT constant exists.

Nevertheless the fixed trial function f satisfies LOC uniformly. Positivity gives `Dir_n(f)<=||f||_2^2=1`, hence

\[
 \operatorname{Dir}_n(f)\le\tfrac43(1-\tfrac14)\|f\|_2^2,
 \qquad
 \|f\|_\infty^2\|f\|_2^2=4\operatorname{Var}(f^2).
\]

Thus `c_1=4/3`, `c_2=4`, and `Theta_chi=(1/4)^(a/2)<=1` work for every n. **LOC does not imply KURT on the stated kernel premises.** If LOC were restricted to the true eigenfunction with bounded c_2, it would imply `kappa-1>=1/c_2`; that restricted statement is not LOC as printed.

The same family also has

\[
 S(a)=(1/16)^a,\quad
 p_\chi(a)=\frac{(1/4)^a}{1+(1/16)^a},\quad
 \frac{Z_\chi(a)}{\operatorname{Tr}K_n^a}
 \le(1/4)^a=(1/16)^{a/2}.
\]

Thus even the exact exponential trace form used by E17, together with its matching lower bound on S, need not control kappa. This one-sector example does not claim the full Wilson magnetic-background or crossing structure. It rules out deriving the proposed eigenfunction ordering from those trace estimates alone. A Wilson-specific implication would need a separate proof.

Conversely KURT is not an absolute confinement bound. For a simple exact test take three equiprobable states `-,0,+`, the flip interchanging the outer states, and
`P_a=(1-1/a)I+(1/a)Pi`, where Pi averages over the states, `a>=3`. The normalized odd eigenfunction is `sqrt(3/2)(-1,0,1)`, so kappa=3/2 for every a. The nonconstant even and odd eigenvalues both equal `theta_a=1-1/a`. Hence `p_chi(a)=theta_a^a/(1+theta_a^a)` tends to `1/(e+1)`, and the odd fraction of the full trace tends to `1/(e+2)`. No fixed exponential E17-type decay holds. The even thermal sum also stays of order one, so this is not a counterexample to a gap theorem with its glue hypotheses.

Verdict: KURT is a different open sufficient ingredient for the corrected SQ-F estimate. Calling it strictly weaker than the existential LOC or than E17 is unsupported, and false as a general implication between the stated kernel conditions. No Wilson-specific non-implication or proof of KURT is asserted here. Near-sign shape alone also does not imply a light flux or spontaneous symmetry breaking: K_n has that shape with the fixed heavy ratio 1/4.

## Disposition

| Statement | Verdict | What survives |
|---|---|---|
| Ground-state transform; Lemma SQ | HOLDS | Reversible Markov construction; exact conditional-variance inequality. |
| Theorem SQ and energy bound | HOLDS AFTER CORRECTION | Real order-two character; incorporate the author's positive-operator correction. The intended Wilson inequality holds. |
| Diffusion form | HOLDS AFTER CORRECTION | Constant 4/3 holds; specify the even gap and form domains. |
| Window | HOLDS AFTER CORRECTION | Both displayed bounds hold; discrete-time near-sign conclusion needs a small step deficit, not E/m alone. |
| Fourth-moment/chi-square identities | HOLDS | Including the conditional-expectation inequality. |
| Multiplicity elimination; displayed SQ-F | HOLDS | Keep the maximum and `1+S_ev(a/2)`. |
| KURT alone gives pure electric F-h | FAILS | Existing counterexample applies; extra remainder/prefactor control is required. |
| RPF; plateau | HOLDS AFTER CORRECTION | RPF inequality holds at integer times; full-even spectral bound needs a definite full centre character. |
| Consumer allows nonconfining flux patterns | HOLDS | Already in FUSE-suff. |
| Consumer needs only F-h | FAILS | F-l, small even sums, all heavy sectors and uniform constants remain. |
| KURT is genuinely weaker than LOC/E17 | FAILS as a claimed implication | Improved coefficient for the eigenfunction, but no established ordering of the actual hypotheses. |

Search addendum: the complete-account index `library/sa-index/ca-full/` was also searched for kurtosis, electric flux, flux ground state, fusion by squaring/product methods, squared eigenfunctions and transverse reflection. No matching entry was found. This is a bounded search result, not a theorem of absence.

The valid mathematical content is the SQ/SQ-F estimate with its exact scope and error terms. No order-one flux estimate, mass gap, continuum result, or standing is granted. The argued half-box and phase-identification claims are outside this check. No numerical or formal-verification program was run.

RESULT: Lemma SQ and the displayed SQ-F bound HOLD; Theorem SQ, diffusion/window and RPF/plateau HOLD AFTER the stated scope corrections; KURT alone supplying pure F-h, “F-h only”, and the claimed logical weakening of LOC/E17 FAIL; the flux and glue estimates remain open, with no status granted.
