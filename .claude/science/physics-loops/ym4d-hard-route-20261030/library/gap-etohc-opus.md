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
