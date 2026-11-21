# G0-COVER: the seed gauge is a plaquette test, not an estimate

Lead (Claude Fable 5.2), FINISH row 606. Checkout `770d40b77`.
Research text, not an audit. This grants no scientific status.
Lemma A was checked line by line by Codex (gpt-6-astra max), lane `g0-cover`: [g0-cover-check](g0-cover-check.md), Step 0. That is one reading by another model, not an audit.
The lead's decision on the result is in the last section.

Credit **Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text**.
Credit **Tadeusz Bałaban** for the method: the tests on the localized background, CMP 122 (1989) 175–202, (1.19)–(1.23).

## Why this file exists

Four lanes reduced I-ENTRY-MATCH to **G0-SEED** ([g-zero](g-zero.md), last section).
Each lane tried to *derive* a gauge bound for the actual real reference from an analytic estimate of a shift $`h`$.
Each attempt was circular or stopped at the seed.
This file changes the question. It makes three points.

1. The seed bound on a read is equivalent to small plaquettes of the same real factor on the read's box. Constants are fixed.
2. Bałaban does not derive that smallness for the localized background. He *tests* it, with a characteristic function, and sends the failed components to the large-field side.
3. So the open statement is a finite coverage statement, G0-COVER below. It has three outcomes, and each one is decisive.

## Lemma A (equivalence)

Let $`V`$ be a unitary lattice field. Use the operator norm.

**(A1) Necessity.** Let $`R`$ be a set of bonds and $`u`$ one gauge on its sites with $`|V^u(b)-1|\le a`$ for all $`b\in R`$.
Let $`p`$ be a plaquette with all four bonds in $`R`$. Then

```math
|\partial V(p)-1|=|\partial V^u(p)-1|\le\sum_{b\in\partial p}|V^u(b)-1|\le 4a .
```

*Proof.* $`\partial V^u(p)=u(x)\,\partial V(p)\,u(x)^{-1}`$ at the base point $`x`$, and the norm is unitarily invariant.
For unitary $`W_i`$, $`|W_1W_2W_3W_4-1|\le\sum_i|W_i-1|`$ by telescoping, and $`|W^{-1}-1|=|W-1|`$. $`\square`$

No smallness of $`a`$ is used. This is the computation in [g-zero](g-zero.md), route 3, without its central-element step.

**(A2) Sufficiency.** Let $`B`$ be a nonwrapping fine-site box of half-width $`q`$ steps with $`|\partial V(p)-1|<\varepsilon`$ for every plaquette $`p\subset B`$.
Then one gauge $`u`$ on $`B`$ gives $`|V^u(b)-1|\le 8q\,\varepsilon`$ on every bond of $`B`$.
For SU(2) and $`8q\varepsilon<1/4`$, the principal logarithm $`\eta A=-i\log V^u`$ has

```math
\eta|A|\le 16q\,\varepsilon,\qquad \eta^2|\nabla A|\le 32q\,\varepsilon .
```

*Proof.* This is [pi-admit](pi-admit.md), section 5.1, (8)–(10), which ports the comb gauge of the account. It uses only the plaquette bound on the whole box. $`\square`$

**Corollary.** Fix a required raw read $`\widehat q`$ and a box $`B\supset\widehat q`$ of half-width $`q_B`$.
If the real factor $`U_p`$ has $`|\partial U_p(p')-1|<a_\flat^Y/(32q_B)`$ on all plaquettes of $`B`$, then G0-SEED holds on that read.
If one plaquette with boundary in $`\widehat q`$ has $`|\partial U_p(p')-1|>4a_\flat^Y`$, then G0-SEED fails on that read.
Plaquette size is gauge invariant and local. No shift $`h`$ appears.

## Fact B (the source method tests the background)

The lead read CMP 122 p. 181 in the owner's PDF.
The localized background $`U^{(n)}_{k,Z}`$ of (1.19)–(1.20) uses the original fields $`V`$ on $`Z\cap\Omega_k^c`$ and the substituted data $`M(Q^{s*}_kV_k)`$ on $`Z\cap\Omega_k`$.
(Corrected 2026-11-09. The first draft had the two regions reversed. The check lane found this; the lead read p. 180 again on the page image.)
Then (1.22)–(1.23) insert a decomposition of unity $`1=\chi^{(n)}_k+(1-\chi^{(n)}_k)`$ in each component of $`Z`$.
The function $`\chi^{(n)}_k`$ restricts the plaquettes of the localized background itself:

```math
|U^{(n)}_{k,Z}(\partial p)-1|<\bigl(1-\beta(\cdots)\bigr)\,\varepsilon_h\,(L^{k-h}\eta)^2
```

on the stated regions, with thresholds that tighten step by step.
A component with $`1-\chi`$ "introduced new large fields", leaves $`Z`$, and is treated like the other large-field regions.

So in the source method the regularity of the actual reference is part of the definition of the summand.
The nested thresholds are the two-radius structure that [g-zero](g-zero.md), section 2, built by hand.
The earlier lanes did not have this page: the Mini lane header named a paper folder that does not exist there. The header is fixed (row 606).

## G0-COVER (the statement to decide)

For each original noncompletion item-10 source, and each required raw read $`\widehat q`$ without a supplied certificate, take the box $`B(\widehat q)`$.
Classify each plaquette of $`B(\widehat q)`$ for the real factor $`U_p`$ of that source:

- **T (tested).** A characteristic function of the summand restricts this plaquette of this real factor. Examples: the bare P0 test with its nested collar ([pi-admit](pi-admit.md) (7)–(8)); a port of (1.22)–(1.23).
- **M (minimizer).** The value is that of a constrained minimizer whose regularity theorem applies with tested data.
- **F (free).** Neither. The source domain allows an arbitrary value on one bond of the plaquette.

Outcomes.

- **All T or M, with thresholds that fit the Corollary.** G-zero is proved outside completion. The proof is Lemma A plus the table.
- **One F plaquette inside a read.** Set that plaquette to $`-I_2`$. This is a counterexample to G0-SEED as quantified. The repair is a restatement: add the plaquette test on $`B(\widehat q)`$ to the item-10 domain, and check that each consumer supplies it at actual fields.
- **The account has no port of $`\chi^{(n)}_k`$.** Then the repair is to add Bałaban's test to the summand. Its cost is the small factor for the failed components.

## Status

| Statement | Status |
|---|---|
| Lemma A | Written by the lead. Checked line by line by Codex (gpt-6-astra max): pass, in dimension four. |
| Fact B | Test and exclusion mechanism: read by the lead and by the check lane. Data-domain sentence corrected (above). The port is located: CA-I 54241–54303, 131947–132023; YM4_1400 63836–63876. |
| G0-COVER as stated | Not decided. The check lane certified no complete T/M cover and no legal F plaquette on the original CA-I item-10 domains. |
| G0-SEED on the unchanged CA-I item-10 domains | Not proved and not refuted. Closed as a work item by the decision below. |
| G0-SEED on a domain with the complete-box test | Proved at a raw read, by Lemma A. The threshold is $`a_\flat^Y/(32q_B)`$. |

## Decision (lead, 2026-11-09)

Two lanes stopped at the same statement: `g-zero` and `g0-cover`. The rule is: restate, do not run a third proof lane on it.

**What the check lane found.**

- The original CA-I item-10 source domains do not contain a test of every plaquette of the box $`B(\widehat q)`$ for the real factor of the source. The lines are CA-I 131725–131739, 110264–110276, 133022–133039.
- The CA-I text has a later repair on the never-averaged collar: the clause $`Q_5`$ at CA-I 141135–141161.
- YM4_1400 has the clause in the definition of the domain. This is `rg:structured-local-gauge`, Y 1251–1274. The lead read Y 1247–1286.
  - The structured space imposes the real and complex curvature bounds on every plaquette of the bare bonds in $`Y\cap\Omega_0`$.
  - It requires good real gauges on a fixed family of cubes. The family includes all gauge cubes of the strip response.
  - Y 1276–1279: when a substitution or a restriction is applied, the clauses must be verified for the resulting triple.

**Decision.**

1. Work on the YM4_1400 domain, not on the CA-I item-10 domain. The CA-I text is under `YM4/Old/` in their repository at `3ac0bf4f2973`.
2. On that domain G0-SEED is a clause of the domain. No estimate of a shift is necessary.
3. The open statement is the admission statement. Name: **G0-COV-ADMIT**. For each operation of the history sum (birth, sibling stage, T-step, later stage, completion elsewhere, dissolution), the triple that the operation makes has the clauses of `rg:structured-local-gauge` on its address. This is a part of root R2 (ADMISSION) in [t0-approach](t0-approach.md).
4. The payment for a failed test is a second open statement. Name: **G0-COV-PAY**. A failure at a plaquette $`p`$ gives $`a_p(U)\ge\rho_B^2/2`$ for the Wilson action of the same plaquette of the same field. The factor is $`\exp[-x_p\rho_B^2/(4D_*)]`$ if the share $`x_p`$ is not spent and at most $`D_*`$ failures use $`p`$. The allocation is not proved. This is a part of root R5 (WITNESS).

**Where the proof of G0-COV-ADMIT could die.** Lemma A gives the gauge from the plaquette test only at index 0.
At index $`n`$ the clause is $`L^n|\mathsf v|,\ L^{2n}|\delta\mathsf v|\le a_\flat`$ on cubes of side $`12\mathfrak M\xi_n`$.
If the cube has about $`L^n`$ bare sites on a side, the comb gauge with plaquettes of size $`\varepsilon L^{-2n}`$ gives $`L^n|\mathsf v|\lesssim\varepsilon`$ but $`L^{2n}|\delta\mathsf v|\lesssim L^n\varepsilon`$.
So the difference clause at index $`n\ge1`$ needs the regularity of a minimizer (class M), not a plaquette test alone (class T).
This scaling remark is a hand estimate by the lead. It is not checked, and the size of $`\xi_n`$ in bare units must be read from the text first.
