lead: anthropic/claude-fable-5-2/medium mac-mini-worker
lease_until: 2026-11-25T03:38Z

# gap-k2-signed-readout-fable (queue row 1479)

Status: IN PROGRESS. Started 2026-11-24T15:38Z (date -u). Pinned at commit 490b37e88.

## 0. Plan

Item: the signed one-step readout of the block map Q2, i.e. statement (DR): for a fixed strength
ratio a and an analytic family of centres containing the SU(2) Wilson input at large x, enclose the
one-step transverse Hessian coefficient b(Phi) (decrement x - x') with explicit error, or exhibit an
admissible centre with nonpositive limiting decrement.

Steps (each is appended here when done):

1. Read the sources the row names: `library/gap-k2-tool-design-fable.md` 3.2, 4.3-4.4;
   `library/gap-k2-t1-small-field-astra62.md`; Proposition GA; row 1472's record. Fix the exact
   definitions of Q2, x, x', b(Phi), "admissible centre", (DR).
2. Write the one-step formula for x' as an exact expression (saddle + Gaussian one-loop +
   remainder) and isolate the non-abelian terms using Proposition GA.
3. Evaluate or enclose the limiting decrement b; compare with (11/(3 pi^2)) log 2 = 0.2575.
4. Remainder bound K/x, or the obstruction; verdict on (DR).
5. Next two rows with decisive outcomes.

Nothing below this line is established until its step is written.
