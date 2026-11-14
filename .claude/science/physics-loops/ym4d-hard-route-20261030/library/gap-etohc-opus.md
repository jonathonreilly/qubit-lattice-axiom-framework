lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-14T17:51Z

# gap-etohc-opus: does (LSI-vac) plus (SG-step) give (HC-vac)?

Queue row 940 (FINISH.md). Author: Claude Opus 5.5, max effort, Mac mini worker 2.
Branch `claude/ym4d-hard-route`, pinned at db49e67f2. Started 2026-11-14T05:51Z.
Research-stage working state; nothing here is a public claim.

Labels: PROVED (written argument, checkable by hand), CONDITIONAL (on named inputs),
GUIDE (numerics, may refute or guide only), OPEN.

## Plan (at most eight steps; one per response)

1. Read row 931 (`library/gap-direction-max.md` Steps 5-7) and the FINISH rules; grep
   `library/open-core.md` and the FINISH rows for (E-to-HC); record the exact statements of
   (LSI-vac), (SG-step), (HC-vac) and what Proposition HC consumes.
2. Gaussian fact test: one mode (AR(1) / Ornstein-Uhlenbeck chain). Compute what (LSI-vac),
   (SG-step) and (HC-vac) are there, and Nelson's exponent q - 1 = e^(2 omega m).
3. Counterexample attack: a reversible kernel with both inputs and no hypercontractivity
   (if the lemma is false as stated, this is the answer).
4. Smallest extra hypothesis: what link between the Dirichlet form of P and the gradient form
   of (LSI-vac) makes it true; prove (E-to-HC) under it (discrete-time Gross argument, or
   continuous-time embedding).
5. Check whether the vacuum slice chain from the Wilson transfer operator satisfies that
   extra hypothesis (or what it would take).
6. GUIDE check on row 931's rotor chain (only if memory allows, under the numeric lock).
7. Literature/credit: Sussman-Alpoge account, Gross 1975, Diaconis-Saloff-Coste 1996,
   Miclo, Mossel et al. (discrete-time hypercontractivity); credit and statement map.
8. Final statement with labels and RESULT line.

## Progress log

(appended step by step below)

### Step 1: inputs, duplicate check, exact statements (READ at db49e67f2)

Read: FINISH.md (opening, How we work, Working efficiently, Rules, rows 931 and 938-943),
GOAL.md, `library/gap-direction-max.md` Steps 4-8 and Result (row 931, Claude Fable 5.2 max,
checked by no one; check row 938 is not on disk at this commit). Row 939's reading
(`library/prior/gap-lit-hcvac.md`) is not on disk at this commit.

Duplicate check (rule 0a). `grep -i -E "E-to-HC|HC-vac|LSI-vac|SG-step"` over
`library/open-core.md` and `library/l17c.md`: no hit. FINISH rows: 931 (names the lemma, does
not attack it), 939 (reading only), 940 (this row), 941 (attacks (LSI-vac)/(HC-vac) for SU(2),
not the implication), 942 (check of this row). No other row attacks (E-to-HC). Proceed.

Setting (row 931 Step 5, READ). M = SU(2)^(3|B|), the links of one time slice, with the product
of unit-S^3 metrics (compact, connected; gauge transformations act by isometries). T(u, w) > 0
the gauge-invariant Wilson transfer kernel, symmetric, real-analytic; Omega > 0 its ground
state, lambda_0 its top eigenvalue. nu = Omega^2 dU. p(u, w) := T(u, w)/(lambda_0 Omega(u) Omega(w))
is the density of pi_u := P(u, .) with respect to nu; p is symmetric, so P is nu-reversible and
nu is stationary. P g(u) = integral of p(u, w) g(w) nu(dw).
The centred score: grad_u log p(u, w) = G(u, w) - E_(pi_u) G(u, .), G = grad_u log T(u, .)
(the pi_u-mean of grad_u log p(u, .) is grad_u of 1, which is 0).

- (LSI-vac)_alpha: Ent_nu(f^2) <= (2/alpha) E_nu |grad f|^2 for gauge-invariant f
  (row 931's form Ent_nu(h) <= E_nu[|grad h|^2/h]/(2 alpha) with h = f^2).
- (SG-step)_sigma: for every u and unit z in T_u M, phi_(u,z) := z . grad_u log p(u, .)
  satisfies E_(pi_u) exp(lambda phi_(u,z)) <= exp(lambda^2 sigma^2/2) for all real lambda.
  (Row 931 says "almost every u"; for a continuous kernel this is the same, by continuity of
  u -> E_(pi_u) exp(lambda phi_(u,z)) in a continuous local frame and Fatou.)
- (HC-vac)_alpha': for every integer m >= 0, ||P^m h||_2 <= ||h||_(q'), q' = 1 + e^(-2 alpha' m).
- (E-to-HC): (LSI-vac)_alpha and (SG-step)_sigma imply (HC-vac)_alpha', alpha' = c(alpha, sigma) > 0.

Row 931's stop (quoted, Step 6): "at fixed q > 1 the telescoping gives a fixed per-step factor
on a quantity that starts at exp(extensive) ... the gain of Proposition HC needs q to grow along
the chain, and in discrete time the Dirichlet form of P is not the gradient form of (LSI-vac)."

Approach chosen (after the reading, before Step 2). Do not go through the Dirichlet form of P.
Put the continuous time in the Hopf-Lax (inf-convolution) semigroup on M instead, where the
gradient form of (LSI-vac) is the natural one, and carry the one-step smoothing of P by a
Harnack inequality in the metric of M. Three lemmas:
  (RD) Renyi bound from (SG-step): E_(pi_y)[(dpi_x/dpi_y)^lambda] <= exp(lambda(lambda-1) sigma^2 d(x,y)^2/2).
  (H)  Harnack from (RD) by Hoelder: (P g)(x)^p <= P(g^p)(y) exp(p sigma^2 d(x,y)^2/(2(p-1))).
  (BGL) Hopf-Lax hypercontractivity from (LSI-vac): ||e^(Q_s F)||_(1 + alpha s) <= ||e^F||_1.
Together: ||P g||_Q <= ||g||_p with Q - 1 = (p - 1)(1 + alpha/sigma^2), hence (HC-vac) with
alpha' = (1/2) log(1 + alpha/sigma^2). Credit for the method: F.-Y. Wang's dimension-free
Harnack inequality (1997) and Bobkov, Gentil and Ledoux (2001), RECALLED, rebuilt below.
