# red: the off-slice consumers of (4.4)
Provenance: Codex (GPT-6 family; requested effort: max; exact runtime identifiers unavailable), checkout `8b159d3f66c21d7d59506433037f2b2578a76acb`, Sussman–Alpoge commit `31a47c543775`; research text, not an audit; no status granted.

## 1. The question

[RED] specifies the nonlinear datum in (R9). It does not assert an off-slice Euler equation.
Here the physical slice means an on-shell reference pair, all parameters equal to one, and the physical gauge constraints.
The independent current, the decoupling parameters, and the ambient field argument give three distinct departures from that slice.

Adoption means (4.4), including the raw-row pairings and every operator assignment in `nl-r9.md` Section 4.
Products retain their actual parameter powers. No identity between undecoupled operators extends by declaration.

Credit for the outline and its method goes to Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text.
SA line numbers refer to [their pinned outline](https://raw.githubusercontent.com/ethanwsussman/Yang--Mills-LLM-experiment/31a47c543775/YM4_sketch_500.tex), fetched once to `/tmp/sa_ym4.tex`.
Balaban supplies the reduced-action method rebuilt in `nl-r9.md`.
All deductions below are written arguments. Searches only locate sources.

## 2. The defining consumers

**The first contraction reads bounds, not an off-slice action identity.**
SA L5773–5774 gives
> \(\mathbf a=\mathsf H_1(s)B'+\mathbf A_1,\quad \mathbf A_1+\mathfrak G(s)\mathsf W_s(\mathbf a)=0.\)

SA L5782 calls these “specified” data. L10368–10372 specifies reduction before decoupling.
Mechanism (j), L10562, limits the gradient identification to physical parameters and on-shell pairs.
This is a prescription. L10383–10402 sketches its analytic consequences; L3878–3881 keeps the nonlinear response estimates open.

The precise bound appears at SA L10387–10388 and L10573:
> \(\lvert\mathsf W_s(A_1)-\mathsf W_s(A_2)\rvert^\sharp_\varpi\le C\widehat b^2r\|A_1-A_2\|_\varpi.\)

The repository consumer is `dec-field.md:238–279`, especially
> \(a=H_1B'-\mathfrak G W_s(a)=:\Phi(a).\)

`nl-r9.md` Section 6 proves this bound for (4.4), conditional on its stated row and linear inputs.
It also proves holomorphy and \(W_s(0)=DW_s(0)=0\).
For \(b=\|B'\|<cB^{-4}\), put \(R=2Bb\), with Proposition 5.1's choice of \(c\).
The contraction constant is \(C_WB^3R\le1/8\).
The second contraction has constant at most \(1/4\).
Uniqueness, weighted response bounds, and holomorphy follow by the two convergent geometric series in Proposition 5.1.
No further value of \(W_s\) occurs in that proof.

**The second system imposes no off-slice equality with the first.**
SA L10426–10432 defines its own \((T,\lambda)\).
The identification at L10446–10464 and mechanism (k), L10580, uses
> \(\mathcal Q(\mathbf H)=B',\quad RD^{\mathsf T}\mathbf H=0,\quad F'(\mathbf H)=K_{\mathbf H}^{\mathsf T}\lambda.\)

Those are physical identities. SA L10462–10464 separates the two functions away from critical physical pairs.
`nl-r9.md:233–267` derives (4.4) on that slice before continuation.
Thus system (II) does not require another independent-current value of (4.4).

**The multiplier is a separate consumer of the field.**
SA L5786–5790 says “required independently”. L10407 and L10576 use
> \((D^{\mathsf T}DA,He_c)=(DA,DHe_c).\)

BGD5–BGD8, SA L10020–10076, derive and estimate
> \(\omega(A)=[1+(C'(A)E_0)^\sharp]^{-1}E_0^\sharp DF(A).\)

BGD5 uses criticality and \(Q_0E_0=1\). Its proof does not establish \(Q_0H(s)=1\).
`d3-local.md:70–92` instead defines
> \(\lambda_s=(I+H_s^{\mathsf T}C'_h{}^{\mathsf T})^{-1}H_s^{\mathsf T}F'_U(h),\quad j_s=R_hK_h^{\mathsf T}\lambda_s-K_0^{\mathsf T}\lambda_s^0.\)

This formula reads the (4.4) fixed point \(h\), not an off-slice Euler equation.
Its Neumann series converges when \(Bcr\le1/2\). At \(h=0\), it gives \(j_s=0\).
At physical parameters, BGD5 identifies its multiplier and current with the physical ones.
Away from them, it is the specified continuation of `wf-room-2.md:288–324`.
The independent current still enters through \(H_s\) and \(h\).
Its bounds require the paired lift estimates; (4.4) alone does not supply those estimates.

## 3. The downstream consumers

These are grouped by the operation that reads the response. Repeated applications use the same requirement.

1. **Weighted derivatives and spatial regularity.** `dec-field.md:276–279` reads
   > \((1+\mathfrak G W_s'(a))\dot a=H_1\beta.\)

   `ld-decoupled.md:85–120` uses distance-to-source weights. `bx-fix.md:83–99` applies the Hölder operator bound.
   SA L3874–3881, L10390–10402, L10576 and L12874–12883 require these estimates on enlarged complex domains.
   The latter passage reads the “Hölder member” of the operators, not a decoupled Laplacian estimate.
   The [NL] derivative bound controls the displayed inverse by its geometric series.
   Applying [PW-H] to the same equation gives the Hölder conclusion.
   Cauchy estimates then use holomorphy on the retained discs.
   These arguments use precisely (4.4), with the named linear estimates as inputs.

2. **Component restriction, reality, covariance and transport.** These are SA L5792–5797, L10400–10402 and L10576.
   `loc-3.md:119–121,147–159` reads (D1), (D1c), (D2), and a local current.
   The exact repaired consumer is `um1-fix.md:123–129`:
   > \(W_s(a):\quad\text{depth }2r;\qquad \Phi_s(a):\quad\text{depth }0.\)

   Keep the untagged diagonal in \(M_s=M_s^{\mathrm w}-a_0I\).
   Its three local runs have radius at most \(2r\). The next tagged operator has an input collar containing them.
   Thus each Picard iterate agrees with the component iterate on its read set.
   Convergence and uniqueness preserve that equality. Zero datum gives zero response.
   This proves the response property without asserting that every term of \(W_s\) is itself tagged.
   The Neumann series of `d3-local.md:81–92` proves the same assertion for the current.
   Real conjugation and transported charts commute with every local map and assigned walk.
   They therefore commute with the unique fixed points and their derivatives (`ti-cov.md:85–87`).
   These conclusions require the repaired hull and two-radius collar inputs.

3. **Pair shifts, brackets and action insertions.** SA L5751–5759 reads
   > \(P\dotplus(\mathbf H,\mathsf j)=(U,A'\boxplus\mathbf H,\mathbf J+\mathsf j).\)

   SA L5809–5824 then reads
   > \(\Phi_Y[F](s,\nu)=F((\rho_XP)\dotplus\nu\mathfrak h_Y(s;P,B')).\)

   This is `loc-3.md:125–145` and `um1.md` Lemmas P and S, with `um1-fix.md`'s repair.
   SA L5830–5861 proves Boolean resummation and the Cauchy bound, conditional on response and domain inclusion.
   The scalar action insertion repeats this at L15154–15171 and L15205–15227:
   > \(\Phi_{p,Y}(s,\nu)=\Phi_{p,\Lambda}(s\mathbf1_Y,\nu).\)

   Splitting proves this equality on admitted cores. Physical identification fixes the resummed endpoints.
   Intermediate values need only the assigned response, its bounds, and inclusion in the function's domain.
   Nothing requires replacing \(\mathbf J+\mathsf j\) by the current of the shifted connection.
   The source-formation and bootstrap uses, SA L15246–15253, L15365–15375 and L16529–16544, retain these same inputs.
   They do not require (4.4) to be a scalar gradient off slice.

4. **Window substitutions and removed comparisons.** SA (WF3), L15758–15775, reads
   > \(\mathcal M^j(e^{i\eta_k(t+\nu\zeta_\square)\mathbf H_k(P;s,B')}U_+(P)).\)

   (WF5)–(WF7), L15781–15867, and (OA7)–(OA8), L16826–16860, require bounds and hereditary domain admission.
   `wf-c.md:194–213` and `bx-fix.md` use the (4.4) field in exactly this formula.
   The inner map then constructs a new critical box background with its own current.
   SA L15945–15960 distinguishes this from outer and removed reduced-current assignments.
   Thus the inner current does not impose an Euler equation on the original off-slice response.
   WF13b, L16180–16195, applies the bracket to that composite map.

   For removed maps, `dec-field.md:329–348` explicitly retains
   > \(-\mathfrak G\{W(a^\square)-W^\square(a^\square)\}.\)

   Both values use (4.4), with their own local data and the same assignment rule.
   Subtracting the contractions gives (6.4); it requires bounds on all displayed residuals.
   `removed-fix.md` Theorems C–D retain pair, field and node comparison inputs.
   These are quantitative comparison obligations, not a request for another off-slice formula.
   The box-first route in `wf-c.md:194` forms no outer or removed term.

   Preserve the failed complete-pair replacement in `old-depth.md:31–56,348–354`.
   Its one-cube test has \(H(z)=zH\), field tangent \(zh\), and
   > \(\dot{\mathsf j}_z=z^2f,\qquad \partial_\epsilon J(e^{i\eta A_z(\epsilon)})|_0=zf.\)

   Here \(f=D^{\mathsf T}Dh\ne0\). Pairing the field tangent with \(H(z)\) gives the second factor of \(z\).
   That replacement needs \(zf\), whereas the adopted current gives \(z^2f\).
   Changing quadratic terms of \(W_s\) cannot change this first derivative.
   The failed route needs a different current assignment or its explicit bulk correction.
   SA L15954–15960 does not assert that replacement. The box-first route avoids it.

5. **New terms and later carriage.** `loc-3.md:122` requires
   > “Each new term of a move … is a finite sum of pieces, each reading only its polymer.”

   SA L17541–17564 treats Gaussian logarithms, normalisers, kept forms and pivot factors.
   SA L17908–17919 carries them through later steps and stages using \(\lambda(\mathbf H,\mathsf j)(s)\).
   Its quoted estimate is
   > \(|f_Y|\le2\mathsf a b_f e^{-(\bar\kappa-1)\mathfrak m(X,Y)}.\)

   `d3-local.md` Section 2 constructs local coefficients conditional on regional matrices, logarithms and convergence.
   Such coefficients read the response only through the substitutions in items 3–4.
   Component equality preserves their products, integrals and convergent sums.
   Adoption supplies no regional Gaussian inverse and no admission of a carried partial map.
   Those remain separate inputs to (D3) and `loc-3.md` Theorem W.

The physical endpoint calculation in `id-step.md:68–100` uses \(W^{\rm red}_1\) only on the physical branch.
SA BGR5–BGR6, L11780–11805, likewise does not identify arbitrary independent-current operators with a physical Hessian.
Neither adds an off-slice value condition.
The pointed estimates PH3 and PW1–PW3, SA L12931–12941 and L13445–13481, concern generated critical pairs.
Their use in the windows is already covered by item 4.

## 4. One written consumer needs a correction

`b4-step.md:258–265` says
> “Call this scalar \(R_s(a)\); its gradient is the five-term \(W_s^{\rm red}(a)\).”

It means (4.6) with decoupled data. This statement needs an extra identity.
The adopted \(M_s\) need not be symmetric; `gates/pw-bridge-gate.md:126` already records this distinction.
`h-walk.md:256` assigns ordered, unsymmetrised walk products. Symmetry of their sum at \(s=1\) does not establish symmetry after tagging.

Hold the pair and \(s\) fixed. Write \(d=d_s(a)\), \(p=H_s^{\mathsf T}J\), and \(z=a-H_sd\).
The claimed scalar is
\[
 R_s=-\langle p,d-\mathcal C_2\rangle
     -\langle Ka,M_sd\rangle+\tfrac12\langle d,M_sd\rangle+V_0(z).
\]
Differentiate the cross term with respect to each factor.
Differentiate the quadratic term with respect to each copy of \(d\).
Their gradients are
\[
 -K^{\mathsf T}M_sd-d'{}^{\mathsf T}M_s^{\mathsf T}Ka,
 \qquad \tfrac12d'{}^{\mathsf T}(M_s+M_s^{\mathsf T})d.
\]
This gives the exact formula
\[
 \boxed{\nabla R_s=W_s^{\rm red}
       +d_s'(a)^{\mathsf T}(M_s-M_s^{\mathsf T})
                              (Ka-\tfrac12d_s(a)).}                 \tag{1}
\]
Thus that scalar-gradient consumer needs the right side of (1), not automatically (4.4).
Equality requires the displayed correction to vanish throughout its ball. Adoption does not assert this.
At \(s=1\), the raw precision \(M\) is symmetric, so the correction vanishes.

The radial integral of (4.4) still obeys `b4-step.md`'s cubic bound (9).
Its identification with \(R_s\) at arbitrary \(s\) is the unsupported step.
That attempted reduction stops at `b4-step.md:270–277`; it supplies no intrinsic polymer estimate to the chain.
One can retain the radial integral as a separate scalar continuation, or estimate the displayed scalar directly.
Neither choice changes the R9 equation. Neither proves its missing intrinsic polymer estimate.
No Yang–Mills counterexample is asserted here.

## Result

**Correction.** Adoption closes [RED] as the specification of the active R9 response, under its named row and linear inputs.
Sections 2–3 give the consumer proof for that statement.
It does not validate every written use: `b4-step.md`'s scalar-gradient claim needs (1).
The failed complete-pair replacement also needs the current correction shown in item 4.
Neither stronger use is required by the outline or the active box-first route.

With the stated [PW], [Rows], hull and current hypotheses retained, the first open (LOC) input is row 226.
It must admit every carried partial map at every shifted argument of (R10), including decoupled corners and complex room.
Response existence does not prove that inclusion (`loc-3-check.md:28–38`).
The every-move use of [PW] still retains its energy, coefficient and geometry premises.
Regional matrices and coherent logarithms for (D3) also remain inputs.
This note supplies no audit, independent check, or retained status.
