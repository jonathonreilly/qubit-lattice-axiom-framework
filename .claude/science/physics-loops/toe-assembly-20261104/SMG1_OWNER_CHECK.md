# SMG1 owner questions: Astra max check

Checker: Codex gpt-6-astra, reasoning effort max, read-only, laptop, 2026-11-07 (run log ~/toe-lap/prior/astra_smg1q.log; spec ~/toe-lap/tmpl/astra_smg1q.txt). It checked owner questions Q1 (gap reading), Q2 (W2.1) and Q3 (W2-LIGHT) before the lead asked them (owner rule 2026-11-06). The lead copied the final message below unchanged.

The questions need revision before they reach the owner. Q1 overstates Lemma F’s scope. Q2 conflates bilinear protection with gaplessness. Q3 offers a precise proposal, but its claimed completeness needs qualification.

The four tests must distinguish an **open success criterion** from an **assumed physical result**. Owner approval can choose a criterion. It cannot turn its conclusion into a derivation.

**Q1 needs a narrower statement.**

Lemma F proves
\[
1\in\operatorname{spec}(U|H_1),\qquad H_1=H^+\ominus\mathbb C\Omega\ne\{0\},
\]
under H1–H3. These include infinite translation covariance, stationarity and clustering. It excludes a neighbourhood of \(1\) free of spectrum on the vacuum complement. It does not exclude an isolated fixed eigenvalue or a gap after removing the entire fixed space. Finite segments and rings fall outside this theorem. [SMG1:85–106](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/SMG1.md:85), [Lemma F check:20–22](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/SMG1_LEMF_CHECK.md:20).

Thus “no NN-a tick has a spectral gap at a clustering vacuum” needs those qualifications. CH1 Amendment 7 uses broader shorthand. It does not establish R-GEN as a universal replacement. The referee’s conditional approval expressly excludes automatic use for VC1. [CH1:24](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/CH1.md:24), [Referee:293–297](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/SMG1_REFEREE.md:293).

The example list is neither exhaustive nor fully specified. These are exact candidate record texts. The alternatives beyond R-GEN are formulations for this review.

- **G — R-GEN.** “For SMG1, fix the certified gate decomposition as part of the supplied data. Write \(g=e^{-iX_g}\), with \(X_g=X_g^*\) and \(\|X_g\|<\pi\). Set \(H_U=\sum_gX_g\), with derivation \(i\sum_g[X_g,A]\). A ground state satisfies \(\omega(A^*[H_U,A])\ge0\) for every local \(A\). A unique gapped ground state has GNS generator with kernel \(\mathbb C\Omega\) and spectrum contained in \(\{0\}\cup[\Delta,\infty)\), where \(\Delta>0\). Tick stationarity remains a separate requirement.”

  This version excludes gates with eigenvalue \(-1\). Extra generator data cannot satisfy the same strict norm bound for such a gate. An extension needs different recorded conditions. [SMG1:21–29](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/SMG1.md:21).

- **F — gap off the whole fixed space.** “In the specified stationary-state GNS sector, put \(\mathcal F=\ker(U-1)\). Require some \(\delta>0\) such that
  \[
  \operatorname{spec}(U|_{\mathcal F^\perp})\cap\{z:|z-1|<\delta\}=\varnothing.
  \]
  Record \(\mathcal F\) separately. This condition asserts neither vacuum uniqueness nor an energy gap.”

  It is vacuous when \(\mathcal F^\perp=\{0\}\). The existing LZ1-SC decision separates static weight for a **dispersion** condition. It does not already adopt this gap condition. [TOE_ASSEMBLY:229](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/TOE_ASSEMBLY.md:229).

- **Q — a quasienergy gap at a named cut.** “Fix a quasienergy \(\varphi\ne0\pmod{2\pi}\) and a specified \(U\)-reducing sector \(\mathcal K\). Require some \(\delta>0\) such that
  \[
  \operatorname{spec}(U|_{\mathcal K})
  \cap\{e^{-i\varepsilon}:\operatorname{dist}_{2\pi}(\varepsilon,\varphi)<\delta\}
  =\varnothing.
  \]
  This is a gap at \(\varphi\), not a vacuum energy gap.”

  For the PS-7r sea, the named cut is \(\varphi=\pi\), and the condition concerns the one-body tick. [TOE_ASSEMBLY:184](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/TOE_ASSEMBLY.md:184). If “away from \(1\)” instead means a punctured neighbourhood of \(1\), it duplicates F.

- **H — a chosen Floquet Hamiltonian.** “For the specified tick unitary, supply a fixed real spectral branch \(b\), with \(e^{-ib(z)}=z\), and define \(H_F=b(U)\). State its sector and ground energy. ‘Gap’ means a positive energy gap above that ground space. Any locality, vacuum identification and infinite-volume realization of \(H_F\) remain proof obligations.”

  A spectral logarithm need not be local. A branch continuous at \(1\), with \(b(1)=0\), inherits Lemma F’s obstruction to a gap above the single vacuum vector. An unwrapped Hamiltonian can require more information than a branch function of \(U\).

- **I — retain the original vacuum-complement condition.** “Require \(\operatorname{spec}(U|H_1)\cap\{z:|z-1|<\delta\}=\varnothing\) for some \(\delta>0\).” Lemma F rules this out under H1–H3.

Deferral is also available. Changing H1–H3 would be a separate proposal, not another meaning of “gap”.

| Option | Test 1: target | Test 2: bounded specification | Test 3: downstream premise | Test 4: needed structure |
|---|---|---|---|---|
| G | **C:** specifies the gap target only | **P:** decomposition fixed beforehand | **C:** stationarity and physical identification remain open | **C:** generator data exceed NN-a |
| F | **C:** specifies a different target | **P:** fixed space and quantifiers are explicit | **C:** static weight cannot silently count as removed mirrors | **P:** uses the existing unitary |
| Q | **C:** specifies a named spectral target | **P:** cut and sector are fixed | **C:** no inference to a vacuum mass gap | **C:** the selected cut needs its own reason |
| H | **C:** specifies an energy-gap target | **P:** branch and sector are fixed beforehand | **C:** locality and vacuum identification remain open | **C:** the Hamiltonian requires justification |
| I | **C:** remains an open target | **P:** exact condition | **C:** existence cannot be assumed | **P:** no added structure |

I is mathematically unavailable under the stated hypotheses. That is distinct from failing a smuggle test.

R-GEN **does depend on the decomposition**. The referee gives
\[
e^{-iA}e^{-iB}=e^{-iB}e^{-iA''},\qquad A''=e^{iB}Ae^{-iB},
\]
but the sums are \(A+B\) and \(B+A''\). Both respect the principal-generator bound. [Referee:253](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/SMG1_REFEREE.md:253).

That dependence is not inherently open-ended. Test 2 passes when the decomposition is fixed before evaluating the gap. It fails if a lane may refactor the same tick until a favourable generator appears.

I therefore agree with **C, P, C, C** for the referee’s bounded R-GEN proposal. I reject extending that approval automatically to every TOE gap. R-GEN also supplies no tick stationarity. The conjugated-tick example proves that separation. [Referee:255](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/SMG1_REFEREE.md:255).

**Q2 should ask about W2.1, not whether symmetry makes the 16 light.**

W2.1 is
\[
\operatorname{Sym}^2(D)^G=0.
\]
It forbids invariant bilinear masses. It does not prove gaplessness under interactions. SMG1 itself exhibits a symmetric interacting gap despite the quadratic obstruction. W2.3 separately requires the light two-point limit. [SMG1:25](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/SMG1.md:25), [SMG1:51–53](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/SMG1.md:51).

The exact binary options are:

- **Keep W2.1.** “Retain \(G_{\rm SM}\hookrightarrow G\), the 16-component \(D\), and W2.1: \(\operatorname{Sym}^2(D)^G=0\). Retain W2.2–W2.3 and the separately selected replacement for W2.4. W2.1 excludes invariant bilinear masses. The existence of the light 16 remains to be proved.”
- **Drop W2.1.** “Delete W2.1. Retain \(G_{\rm SM}\hookrightarrow G\), the same 16-component \(D\), W2.2–W2.3, and the separately selected replacement for W2.4. No bilinear-protection condition is required.”

These options are complete for retaining or deleting that clause. Neither deletes \(\nu^c\). A fifteen-field target requires a separate amendment to \(D\), the index range \(A=1,\ldots,16\), W2.3 and the W2.4 replacement.

W2 already selects the full 16. CG1’s broader target makes \((1,1)_0\) optional. [TOE_ASSEMBLY:718](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/TOE_ASSEMBLY.md:718), [TOE_ASSEMBLY:462](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/TOE_ASSEMBLY.md:462).

Keeping W2.1 forces \(G\supsetneq G_{\rm SM}\), since \(\nu^c\nu^c\) is an SM singlet. It does not force \(G=\operatorname{Spin}(10)\). Both live laws supply candidate protecting groups. [SMG1:33,148](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/SMG1.md:148).

| Option | Test 1 | Test 2 | Test 3 | Test 4 |
|---|---|---|---|---|
| Keep | **C:** an explicit W2 target restriction | **P:** exact invariant-space condition | **C:** protection is required, not established | **P:** the larger group serves the chosen bilinear restriction |
| Drop | **C:** changes W2’s success criterion | **P:** deletes one definite condition | **C:** assumes neither a neutrino mass nor its absence beyond W2.3 | **P:** adds no structure |

I agree with the referee’s **C, P, C, P** for retaining W2.1. I disagree with “a light \(\nu^c\) would be unprotected” after deletion. Protection would be **unrequired**. It could still hold in a successful construction. [Referee:299–301](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/SMG1_REFEREE.md:299).

**Q3 correctly identifies a required replacement, but “another” is not an exact option.**

The universal W2.4 contradicts W2.3. The existential version permits every operator to be scaled to zero. Neither should remain an available success criterion. [Referee:153–159](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/SMG1_REFEREE.md:153).

The referee option can be recorded exactly as follows:

> For quasi-local \(A\), real \(p\) and \(\lambda>0\), put
> \[
> A^{\lambda,p}(x,t)=\lambda^p\alpha^{\lfloor\lambda t\rfloor}
> (\tau_{[\lambda x]}A),\qquad
> \widetilde A^{\lambda,p}(x,t)=(-1)^{\lfloor\lambda t\rfloor}A^{\lambda,p}(x,t).
> \]
> Call \((A,p)\) admissible when both connected two-point functions converge as distributions on \((x,t)\ne(0,0)\). Each field is paired with its own adjoint at \((0,0)\).
>
> For every admissible pair, the limit for \(\widetilde A^{\lambda,p}\) is zero.
>
> For every finite family of admissible pairs, the connected \(n\)-point functions of the \(A_i^{\lambda,p_i}\) converge on non-coinciding points. Their limits equal connected correlations of Wick polynomials in the W2.3 free field and its derivatives.

This preserves the quantifiers and content of W2.4′. The nearest-cell tie rule remains the one in SMG1. [Referee:163](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/SMG1_REFEREE.md:163), [SMG1:24](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/SMG1.md:24).

My tests are **C, P, C, C**:

1. **C.** It is a proposed W2 success criterion.
2. **P.** Its admissibility quantifiers are fixed.
3. **C.** Its full Wick-polynomial limits must remain conclusions to prove.
4. **C.** Full free-field correlation closure is stronger than merely excluding additional species.

The fourth rating differs from the referee’s P. W2.3 specifies a two-point distribution. It does not itself establish all higher free-field correlations. [Referee:165–167](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/SMG1_REFEREE.md:165).

There is also a coverage obligation. W2.4′ constrains pairs whose two-point limits already converge under power normalization. It does not establish that every unwanted light sector has such a representative. It explicitly demodulates only the \(\pi\) channel. The stated \(\pi\) argument supplies no general coverage theorem for other carriers.

Static weight also needs an explicit disposition. LZ1-SC’s separate static class does not automatically exempt static correlations from W2.4′.

The files supply no second completed replacement. The exact alternative presently available is:

> “Do not adopt W2.4 or W2.4′. Keep W2-LIGHT open. Retain the selected W2.1 and W2.2–W2.3. Require a fully stated replacement before claiming exclusion of every additional light sector.”

Deferral passes **P, P, P, P**. It adds no physical premise or discretionary completion rule. An adopted blank cheque labelled “another condition” would fail test 2.

**The decisions are distinct, but their interfaces are linked.**

Keeping or dropping W2.1 fixes neither a gap definition nor a light-sector criterion. R-GEN fixes neither \(G\) nor the number of light fields.

W2.4′ refers to tick evolution \(\alpha\). R-GEN concerns \(H_U\). Choosing R-GEN does not prove that its gap removes light tick correlations.

A whole-sector gap must also be distinguished from selective mirror gapping. W2 and VC1 retain massless content. Lemma M permits genuine mirror–light mixing at degree four. A separate gapped mirror factor cannot simply be assumed. [SMG1:132–139](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/SMG1.md:132), [TOE_ASSEMBLY:524](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/TOE_ASSEMBLY.md:524).

Changing the target to fifteen fields would change W2.4′’s reference field. Merely dropping W2.1 would not.

None of these choices, recorded as open criteria, settles the named downstream problems:

- **CH1:** the selective gap and light-sector completeness remain construction obligations. The gauged measure and reflection positivity remain separate. [TOE_ASSEMBLY:447–458](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/TOE_ASSEMBLY.md:447).
- **CG1:** supplying \(D|_{G_{\rm SM}}\) names the desired representation. It does not derive its physical realization, P-HY or P-COMP. [TOE_ASSEMBLY:462–475](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/TOE_ASSEMBLY.md:462).
- **VC1:** no choice constructs the required stationary vacuum. R-GEN’s ground state cannot be substituted automatically. The charged-sector candidate is also unadopted, and ZM1-INV supplies no charged-field map. [TOE_ASSEMBLY:225](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/TOE_ASSEMBLY.md:225), [TOE_ASSEMBLY:252–255](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/TOE_ASSEMBLY.md:252).
- **YM mass gap:** none supplies it. The cited T0 interface explicitly excludes the mass-gap conclusion. Its chiral-matter extension is separate. [TOE_ASSEMBLY:588,606](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/TOE_ASSEMBLY.md:588).

Treating the desired light content or physical gap as an axiom would instead fail tests 1 and 3. The prior digest does not remove those obligations. It records atomic results, finite diagnostics and failed selective-gap constructions. [prior/SMG1:23–39](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/prior/SMG1.md:23), [prior/SMG1:55–74](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/prior/SMG1.md:55).

My recommendations are:

- **Q1:** Use bounded R-GEN for SMG1, because it matches the established generator results while preserving FLQ and downstream bridges.
- **Q2:** Keep W2.1 as a bilinear-protection target, because both live groups support that condition without establishing interacting gaplessness.
- **Q3:** Keep W2-LIGHT open pending a bounded clarification of coverage, because W2.4′ alone does not justify the unrestricted phrase “nothing else is light.”

All six source hashes were unchanged at the final check. No files were edited. No git commands ran.