# Independent referee report: C5 probe R5-3

## VERDICT: CONFIRMED WITH CORRECTIONS

The route-level reading—all four broad routes remain **OPEN**, with only narrow conditional exclusions—is correct. The algebra and numerical reproductions mostly pass. The report nevertheless overstates three points: (i) G1–G3 are a deliberately narrow class, not a complete classification of reference rules; (ii) Lemma S applies to the original global sequester, not generically to later local or Gauss–Bonnet sequesters; and (iii) the Baum–Hawking expression is a divergent formal weight, while the fixed-count stationary point is a minimum of its real-axis exponent, not a controlled saddle. The route-2 R2-4 exclusion also requires the full W1–W3 system and cannot be inferred from a prior on a global constant alone.

## 1. Lemma PT

**Finding: algebra confirmed; completeness denied; numerical scale confirmed with a wording correction.**

- Under the stated assumptions, the proof is exact. From `R5-3_report.md:77-79,92-97`, metric compatibility, the Bianchi identity, conservation of the true matter stress, and $S_{\mu\nu}=T_{\mu\nu}+f g_{\mu\nu}$ give
  
  \[
  \partial_\nu(\Lambda-8\pi Gf)=0,
  \qquad
  G_{\mu\nu}+\Lambda_c g_{\mu\nu}=8\pi G T_{\mu\nu}.
  \]
  
  A prescribed subtraction is therefore either inconsistent with constant-Λ GR when it changes, or is exactly undone by the unimodular integration field.
- G1–G3 are **not complete** for all rule sets capable of controlling vacuum curvature. They omit an independent global equation or four-form flux fixing Λ_c, a dynamical compensator, non-c-number/state-dependent source terms, modified/nonmetric gravity, energy exchange or nonconservation, and exact symmetries. The report itself names only part of this outside class at `R5-3_report.md:81-84,101-104`. Bianchi conservation shows that the combination is constant; it does not prove that the constant is an unconstrained initial datum in a theory with an additional global equation.
- G3's phrase “state-independent c-number” that “may change at phase transitions” (`R5-3_report.md:79`) should mean field-independent/prescribed within each phase. Literally, a state-independent number does not track a state transition.
- The electroweak comparator reproduces: `scripts/r53_numbers.out:6` gives $\Delta V=1.1888\times10^8\,\mathrm{GeV}^4=4.721\times10^{54}\rho_\Lambda$. Thus the required residual precision is $\rho_\Lambda/\Delta V=2.12\times10^{-55}$, equivalently one part in $4.72\times10^{54}$. This is the correct order, conditional on the tree-level Higgs-potential comparator and on having no outside compensating/global mechanism. The QCD values in `scripts/r53_numbers.out:7-9` also reproduce.

## 2. Lemma S and sequestering

**Finding: identity and main numerical obstruction confirmed; boundary hypotheses and model scope need tightening.**

- The integration by parts at `R5-3_report.md:158-167` is correct:
  
  \[
  \int a^3R\,dt=6[a^2\dot a]-6\int a\dot a^2dt+6k\int a\,dt.
  \]
  
  With $\langle R\rangle=0$, a finite nonnegative bang limit of $a^2\dot a=a^3H$, and a finite nonpositive crunch limit, it follows that $k\int a\,dt\geq\int a\dot a^2dt$, hence $k>0$ and
  
  \[
  |\Omega_{K0}|={k\over\dot a_0^2}\geq {\langle\dot a^2\rangle_a\over\dot a_0^2}.
  \]
  
  The report should explicitly require the endpoint limits to exist and be finite; signs alone do not license the boundary subtraction.
- Independent reruns reproduce `scripts/r53_curvature_bound.out:1-6`: the past numerator is 0.4832, denominator 0.5272, their ratio is 0.9166, and the chosen $|\Omega_{K0}|=0.002$ benchmark requires a total denominator 241.6 $a_0/H_0$. “242” and “about 240 Hubble times” are accurate for that benchmark. Continuing ΛCDM for $H_0^{-1}$ gives 2.010, also reproduced.
- The requested `scripts/r53_closed_scan2.out:3-18` supports the limited toy-scan statement. Rows 9 and 14 fail the printed integral identity and are false roots; the remaining reported roots have $\min\Omega_m=1.0038$–1.0096 and $q>0$. This finite scan is corroboration, not a theorem over potentials.
- The original global Kaloper–Padilla equations do reduce to $\langle R\rangle=0$; their historic-universe discussion also requires positive spatial curvature. See [Kaloper–Padilla 1406.0711](https://arxiv.org/html/1406.0711). This validates `R5-3_report.md:147-162` for that model.
- The reduction is **not generic to later versions**. The manifestly local four-form formulation leaves a residual curvature determined by flux data rather than imposing $\langle R\rangle=0$ as an identity; see [Manifestly Local Vacuum Energy Sequestering](https://arxiv.org/html/1505.01492). The Gauss–Bonnet extension instead imposes a flux relation on $\langle R_{\rm GB}\rangle$ and contains a residual ΔΛ; see [Vacuum Energy Sequestering and Graviton Loops](https://arxiv.org/html/1606.04958). Lemma S therefore cannot exclude either class without their additional flux choices and field equations.
- The correct exclusion is narrower than a general “sequestering” exclusion: **the original global $\langle R\rangle=0$ model, homogeneous bang-to-crunch FRW, finite signed endpoint terms, and no extremely long low-$\dot a$ phase is observationally excluded by its order-unity closed curvature.** The scope at `R5-3_report.md:183-186` is basically right; “no ≈240-Hubble-time loiter” is tied to the selected 0.002 benchmark rather than an exact observational theorem.

## 3. Route 2: Baum–Hawking/Coleman and R2-4

**Finding: exponent confirmed; probability and fixed-count interpretations require major qualification; R2-4 applies only conditionally.**

- Given the formal single-$S^4$ Hawking weight $w(\Lambda)=\exp[3\pi/(G\Lambda)]$,
  
  \[
  \log{w(\Lambda_{\rm obs}/2)\over w(\Lambda_{\rm obs})}
  ={3\pi\over G\Lambda_{\rm obs}}=3.3087\times10^{122},
  \]
  
  exactly as in `R5-3_report.md:190-192` and `scripts/r53_numbers.out:18-20`. Hawking's original sign motivation is summarized in [Hawking 1984](https://www.sciencedirect.com/science/article/abs/pii/0370269384913704).
- This does **not** define a probability distribution on $\Lambda>0$: it is non-normalizable at $0^+$. Thus “disfavour” is valid only as a ratio of formal weights, and `R5-3_report.md:193` should not say the weight “predicts” exact zero. Coleman's [many-universe construction](https://scixplorer.org/abs/1988NuPhB.310..643C/abstract) adds another exponential and is not the same measure. Polchinski's phase objection is correctly directed: in four dimensions the relevant saddle phase reverses the naive sign; see [Polchinski 1989](https://www.sciencedirect.com/science/article/pii/0370269389903870). These contour and conformal-factor problems keep the route OPEN, not VIABLE.
- R2-4's theorem is broader than local dynamical variables—W1 permits any configuration space—but narrower than “any positive weight.” Its actual assumptions are a positive joint measure, a real **local source coupling**, and the observed isotropic $1/p^2$ GR response (`C5_R2-4_report.md:103-119`). Adding a global Λ variable to such a full joint measure does not evade the theorem. A positive marginal prior $P(\Lambda)$, or the on-shell Hawking factor by itself, does not supply W2 or W3 and is not excluded by R2-4. Therefore the bounded result at `R5-3_report.md:196-205` should read: **no full positive W1–W3 Euclidean realization can produce both the long-range GR source response and the proposed Λ weighting.** It is not a no-go for a weight on a global constant in isolation.
- Differentiating the fixed-count exponent in `R5-3_report.md:207-210` does give $\Lambda_*=\sqrt{24\pi^2/V}$. But its second derivative is $+6\pi/(G\Lambda^3)$, so this is a **minimum** of the real-axis exponent, while the displayed integral diverges at both $\Lambda\to0^+$ and $\Lambda\to\infty$. It is only a formal stationary point until an inverse-Laplace contour and convergent measure are specified; it is not a controlled saddle or a prediction. The report's conclusion that it merely trades the scale problem for $V$ remains correct.

## 4. Route 4: Gibbs–Duhem and forming records

**Finding: thermodynamic identity and free-additive-constant objection confirmed; record dynamics and gravitational coupling are not derived.**

- For $E=V\epsilon(N/V)$, `R5-3_report.md:214-217` correctly obtains $\partial E/\partial V|_N=\epsilon-n\epsilon'=-p$. A conserved extensive charge, freely adjustable volume, and zero external pressure therefore give $\epsilon-\mu n=0$. This is the self-sustained-medium/q-theory equilibrium argument.
- For nonconserved $N$ at fixed $V$, an **interior reversible minimum** would satisfy $\epsilon'(n_*)=0$, leaving $\epsilon(n_*)$ arbitrary under $\epsilon\mapsto\epsilon+C$. That establishes the important negative result: record formation alone cannot select the additive vacuum-energy constant.
- Permanent monotone record creation does not, by itself, prove equilibration at an interior minimum. It can stop at saturation, a one-sided/KKT boundary, a kinetic barrier, or nowhere. Accordingly, “forming records leave the energy at $\epsilon_{\min}$” is too strong unless an energy-lowering dynamics and accessible interior endpoint are added. The safer claim is that **none of those formation conditions fixes the additive constant**.
- Nor does ordinary Gibbs–Duhem thermodynamics prove that gravity couples to $\epsilon-\mu n$; a q-variable/four-form or an explicit source theorem is needed, as the report correctly admits at `R5-3_report.md:219-230`. [Klinkhamer–Savelainen–Volovik 1601.04676](https://arxiv.org/abs/1601.04676) supports the further warning at `R5-3_report.md:231`: in their reversible FRW dynamics, the Minkowski asymptote still needs specially selected initial data.

## 5. DESI and curvature comparators

**Finding: tabulated value and sign are right; the quoted absolute bound is a working benchmark, not the DESI result.**

- [DESI DR2 Results II, arXiv:2503.14738](https://arxiv.org/html/2503.14738) reports for ΛCDM+Ω_K with DESI+CMB $10^3\Omega_K=2.3\pm1.1$, with positive Ω_K denoting open curvature, and says there is no significant preference for nonflat geometry. Thus `R5-3_report.md:170-171` has the number and sign right.
- A closed prediction Ω_K ≤ −0.003 lies $(0.0023-(-0.003))/0.0011=4.8\sigma$ from that one-dimensional Gaussian central value, so “about 5σ” is arithmetically fair **within that ΛCDM+curvature likelihood**. It is not a model-independent likelihood for sequestering cosmologies.
- $|\Omega_K|\le2\times10^{-3}$ is not the quoted DESI confidence interval—the central value itself is $2.3\times10^{-3}$. It should be labelled a round working target. This does not affect the robust no-loiter contradiction, because Lemma S predicts at least 0.9166 from the ΛCDM-like past, hundreds of times larger.
- DESI's $w_0>-1,w_a<0$ best-fit quadrant is only a qualitative comparator. The DR2 paper finds evolving-dark-energy preference dependent on the supernova set, and the best-fit histories can cross $w=-1$. It neither validates the sequester nor a canonical single-field quintessence model. The restrained claim should be that a negative constant plus a dynamical component can mimic that effective quadrant.

## 6. Reading and scope

**Finding: the all-OPEN reading is confirmed.**

- Route 1 remains OPEN because neither the axioms nor the unimodular integration constant selects its value (`R5-3_report.md:117-138`).
- Route 2 remains OPEN because its zero peak is formal and contour-dependent; the bounded R2-4 exclusion is valid only for a full W1–W3 realization (`R5-3_report.md:188-210`; `C5_R2-4_report.md:103-130`).
- Route 3 remains OPEN because the strong curvature exclusion is confined to the original global homogeneous $\langle R\rangle=0$ model and does not cover local, Gauss–Bonnet, inhomogeneous, or specially loitering variants (`R5-3_report.md:183-186`).
- Route 4 remains OPEN because an augmented q-like conserved sector with free volume is not logically inconsistent, but the stated record axioms supply neither that sector nor its gravitational source rule (`R5-3_report.md:219-236`).
- Hence no route meets the fixed VIABLE criterion, but no class-complete no-go has been proved. The two EXCLUDED results survive only with the scopes stated above.

## Strongest correct statement

Within a Levi-Civita metric theory with conserved true matter stress, a prescribed c-number vacuum subtraction cannot protect the geometry across phase transitions: Bianchi conservation turns it into an unchanged integration constant, so the electroweak shift alone demands a residual cancellation at roughly one part in $4.7\times10^{54}$ unless an additional global, dynamical, symmetry, or modified-gravity equation is supplied. The original global Kaloper–Padilla $\langle R\rangle=0$ rule is additionally incompatible with a homogeneous ΛCDM-like past and observed near-flatness unless the future contains an extraordinarily long low-expansion phase, but that conclusion does not extend to local or Gauss–Bonnet sequesters. Positive full Euclidean W1–W3 measures cannot reproduce GR, whereas the Baum–Hawking factor alone is divergent and the record Gibbs–Duhem argument leaves an unfixed additive constant. Thus this campaign exhibits no untuned, observationally viable derivation of $\langle\Lambda\rangle=0$, while the evidence is not broad enough to prove that no augmented rule set can do so.
