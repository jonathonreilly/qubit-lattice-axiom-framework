# G0-COVER: the seed gauge is a plaquette test, not an estimate

Lead (Claude Fable 5.2), FINISH row 606. Checkout `770d40b77`.
Research text, not an audit. This grants no scientific status.
Not yet checked by another model. Lane `g0-cover` checks it.

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
The localized background $`U^{(n)}_{k,Z}`$ of (1.19)–(1.20) uses $`V`$ on $`\Omega_k`$ and substituted data $`M(Q^s_kV_k)`$ outside.
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
| Lemma A | Written here by the lead. Not checked by another model. |
| Fact B | Read by the lead in the PDF. Its port in the account is not located. |
| G0-COVER | OPEN. Lane `g0-cover` decides it. |
| G0-SEED / G-zero outside completion | OPEN until G0-COVER is decided. |
