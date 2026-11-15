# GB1 generator-reading owner question: Astra max check

Checker: Codex gpt-6-astra, reasoning effort max, read-only, laptop, 2026-11-07 (run log ~/toe-lap/prior/astra_gb1gen.log; spec ~/toe-lap/tmpl/astra_gb1gen.txt). It checked the owner question on which generator reading GB1 uses before the lead asked it (owner rule 2026-11-06). The lead copied the final message below unchanged.

The framing is mostly right. It needs a distinction between a supplied generator and a logarithm determined by the tick.

R-SUM generally does **not** satisfy \(e^{-iH}=U_{KS}\). R-IA first defines a positive transfer. Its Hamiltonian is \(H^{(\lambda)}=-\lambda^{-1}\log T_{\rm loc}\). Equality with R-SUM’s \(H\) is not established at finite \(\lambda\). [GB1E.md:90](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/GB1E.md:90)

The question also needs these qualifications.

- The lift concerns GB1QL’s proposed SU(2) test family and its infinite-register target. It is not yet a result for either selected physical law. The measures live on finite tori with even \(N\ge4\) and even \(N_t\ge2\). The referee confirms the stated Haar density, gauge invariance, exact transfer and coordinate link-reflection positivity. [GB1E.md:7](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/GB1E.md:7), [GB1E_REFEREE.md:149](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/GB1E_REFEREE.md:149)
- “Undefined at irrational \(\tau_E/\pi\), bounded otherwise” is too loose. Strict R-GEN is undefined whenever **any gate** has \(-1\) in its spectrum. Rational examples also fail. Where it is defined, its finite-box sum is bounded and has no specified transfer-kernel lift. [GB1E_REFEREE.md:123](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/GB1E_REFEREE.md:123)
- “(H-class) fails first” requires \(N_t=N\) even, the (P8.1) reflection interface, and a class requiring time–space exchange invariance. For \(\mu_{\rm ex}\), the result excludes a discrete exceptional set of nonzero \(\theta\). For \(\mu_{\rm loc}\), failure holds at every parameter. With the stronger mirror interface, (H-RP) fails first wherever the required invariance fails. On the infinite lattice, (H-4D) remains missing. [GB1E_REFEREE.md:145](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/GB1E_REFEREE.md:145)

The menu needs four separate entries: R-SUM, R-IA, strict R-GEN, and the non-strict R3 variant. R3 is recorded, not proposed or adopted. For completeness, mention the recorded R-ISO calibration and its failing tests. This is not an exhaustive classification of possible generator prescriptions. [GB1E.md:94](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/GB1E.md:94), [GB1E.md:125](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/GB1E.md:125)

I would use the following proposed record text.

For R-SUM and R-IA, include this common clause:

> Use GB1QL’s specified layers and named operators. Treat \(\theta\) and \(\tau_E\) as supplied real coefficients. Retain their written values across the register family. For this Euclidean branch require \(\tau_E>0\). If only \(W_E\) is supplied, explicitly record one representative \(\tau_E+8\pi n>0\), with \(n\in\mathbb Z\). Denote that chosen value by \(\tau_E\) thereafter.

The files choose no numerical representative. The layer \(W_E\) determines only its residue modulo \(8\pi\). Different positive representatives generally give different Euclidean theories. [GB1QL.md:70](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/GB1QL.md:70), [GB1E_REFEREE.md:151](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/GB1E_REFEREE.md:151)

For **R-SUM**, record:

> For GB1’s specified layers \(e^{-i\tau_kK_k}\), set \(H=\sum_k\tau_kK_k\). Thus
> \[
> H=\tau_EA+\theta H_B,\qquad
> H_s=\tau_E\sum_\ell E_\ell^2+\theta\sum_C B_C^s.
> \]
> Use \(T(a_0)=e^{-a_0H}\) for each specified \(a_0>0\). No independent finite \(\lambda\) is selected. In the local-layer construction, set \(\lambda=a_0/n\) and take odd \(n\to\infty\).

This preserves the written sum and the proved limiting construction. [GB1E_DRAFT.md:118](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/GB1E_DRAFT.md:118), [GB1E.md:72](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/GB1E.md:72)

For **R-IA**, record:

> Supply one fixed \(\lambda>0\), in tick units, for each instantiated law. Keep it fixed across the register family. Define
> \[
> T_{\rm loc}=\Phi(\lambda\theta,\lambda\tau_E)
> =e^{-\lambda\theta H_B/2}e^{-\lambda\tau_EA}e^{-\lambda\theta H_B/2},
> \quad(\beta,t)=(-2\lambda\theta,\lambda\tau_E).
> \]
> Define \(H^{(\lambda)}=-\lambda^{-1}\log T_{\rm loc}\). At this step, \(a_0=\lambda\) and \(T_{\rm loc}=e^{-a_0H^{(\lambda)}}\).

The files supply no numerical \(\lambda\). Until one is supplied, this denotes a parameterized family. It does not establish \(H^{(\lambda)}=H\), or the same lift construction at every other step for that fixed \(H^{(\lambda)}\). [GB1E.md:86](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/GB1E.md:86), [GB1E_DRAFT.md:255](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/GB1E_DRAFT.md:255)

For **strict R-GEN widened to GB1**, record:

> For GB1, fix the certified cube gates \(e^{-i\theta B_C}\) and link gates \(e^{-i\tau_EE_\ell^2}\). Require \(g=e^{-iX_g}\), \(X_g=X_g^*\), and \(\lVert X_g\rVert<\pi\). Set \(H_U=\sum_gX_g\), with local derivation \(i\sum_g[X_g,A]\). The reading supplies a generator exactly when every gate has \(-1\notin\operatorname{spec}g\).

This is the generator clause of the owner’s SMG1 prescription with a new scope. Its domain condition follows from R2. [TOE_ASSEMBLY.md:261](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/TOE_ASSEMBLY.md:261), [GB1E_REFEREE.md:125](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/GB1E_REFEREE.md:125)

For **non-strict R3**, record:

> Use the same fixed gates and sum. Replace \(\lVert X_g\rVert<\pi\) by \(\lVert X_g\rVert\le\pi\). Require \(X_g\) to be unique. This reading applies exactly when no gate has eigenvalue \(-1\).

The uniqueness clause matters. The non-strict bound alone leaves endpoint choices at eigenvalue \(-1\). The recorded wrapped formula is
\[
w(x)=x-2\pi\left\lfloor\frac{x+\pi}{2\pi}\right\rfloor,\qquad
H_{\rm wr}=V_\theta+\sum_\ell w(\tau_EE_\ell^2).
\]
Under the stated small-magnetic-angle and irrational-electric-angle hypotheses, this agrees with R3. Using that endpoint convention where \(-1\) is an eigenvalue would be another variant. [GB1E_REFEREE.md:135](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/GB1E_REFEREE.md:135), [GB1E.md:107](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/GB1E.md:107)

Neither bounded reading needs an unwrapped \(\tau_E\) representative or a \(\lambda\). Changing \(\tau_E\) by \(8\pi n\) leaves its gates unchanged. Both give the partition obstruction wherever their bounded generators exist.

For the recorded **R-ISO** alternative, the exact clause is:

> For \(\theta<0<\tau_E\), choose \(\lambda=\lambda_{\rm iso}\), where \(c_{\lambda\tau_E}=\lambda|\theta|\).

This fixes classical isotropy by calibration. It does not make \(\mu_{\rm loc}\) exchange invariant. [GB1E.md:176](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/GB1E.md:176), [GB1E_DRAFT.md:447](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/GB1E_DRAFT.md:447)

My four tests for the wording above are below. C marks a supplied physical choice that must remain explicit. Definedness is a separate check.

| Reading | 1: fixes target | 2: open-ended | 3: downstream premise | 4: unnecessary structure |
|---|---|---|---|---|
| R-SUM | **P.** Defines an input, not bridge success. | **P.** Operators and coefficients are fixed. | **C.** Supplies the energy reading and Euclidean correlations. | **P.** Uses the necessary written layer data. |
| R-IA | **P.** Assumes no vacuum or symmetry result. | **P.** The revised text fixes one step per law. | **C.** Supplies the Euclidean prescription. | **C.** A particular finite step lacks a law-based selection. |
| Strict R-GEN | **P.** Assumes no successful lift or gap. | **P.** Gates, branch and domain are explicit. | **C.** Selects the generator behind the proved obstruction. | **P.** Uses the existing decomposition and one branch selector. |
| Non-strict R3 | **P.** Assumes no successful lift or gap. | **P.** Uniqueness closes the prescription. | **C.** Selects the bounded generator. | **P.** Adds no further structure beyond the selector. |
| R-ISO | **F.** Calibrates to the isotropy target. | **P.** The root is unique. | **F.** Imposes tree-level isotropy. | **C.** This calibration is unnecessary for a lift. |

These are fresh GB1 grades for strict R-GEN. The SMG1 grades cannot simply be transferred. My R-SUM test 4 agrees with the referee’s P rather than the draft’s cautious C. My R-IA test 2 becomes P because the proposed wording fixes its parameter scope. The filed version remains C if later parts may select \(\lambda\) opportunistically. R3 and R-ISO match the recorded grades. [GB1E_REFEREE.md:163](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/GB1E_REFEREE.md:163)

Fixing a representative does **not** add unnecessary structure when the purpose is to specify one unwrapped Hamiltonian. It supplies information that the unitary lacks. That information generally changes the Euclidean theory. This belongs under test 3’s conditional grade. The files provide no privileged numerical representative.

R-SUM, R-IA and the bounded readings do not assume T0-start, Y3, VC1 or the YM consumers. Their consequences still require proofs. The bounded readings obstruct this particular transfer-kernel route. Finite-lattice anisotropy does not decide continuum isotropy restoration. R-ISO smuggles the classical calibration, but still does not establish Y3. The state relation, infinite-volume bridge, action-class membership and continuum conclusions remain open. [GB1E.md:215](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/GB1E.md:215), [GB1E.md:220](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/GB1E.md:220)

A GB1-scoped choice does not conflict with the owner’s SMG1-only decision. The question should explicitly say:

> This decision applies to GB1 only. SMG1 retains its strict bounded R-GEN. Any identification of their generators or vacuum states remains a separate obligation.

That qualification matters for later assembly. The generators agree in the stated finite-register regime only while the electric phases do not wrap. The condition cannot persist as \(s\to\infty\) at fixed positive \(\tau_E\). The assembly still requires one law and one vacuum. [GB1E.md:107](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/GB1E.md:107), [TOE_ASSEMBLY.md:698](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/TOE_ASSEMBLY.md:698)

I recommend R-SUM with the written positive real \(\tau_E\) fixed as supplied data, because it gives the proved finite-box semigroup lift without selecting a finite-step calibration or assuming downstream success.

I edited nothing and ran no git. Citations use refreshed GB1E `d969ee043222` and GB1 `7ffb69855fa9`, including the newly added Amendment 3. I did not repeat the referee’s full proof audit.