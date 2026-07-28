# Goal

## Exact target contract

**Target statement:** On the supplied five-lift recovered bank, the quantities
`tau_b(i) = log(1+b_i)` have a unique minimum at lift `0`; that minimum lies
strictly in the supplied stabilization window; and the exact threshold-volume
field evaluated there has unique minimizer lift `0`.

**Quantifiers/domain:** Every `i` in the five-entry recovered bank and every
competitor `j > 0` in that same bank.

**Allowed premises:** The supplied-bank triples and exact piecewise
threshold-volume formula already named by the parent note; the supplied
stabilization endpoints; elementary monotonicity of `log(1+x)`. The bank
identity and endpoint authority remain open upstream dependencies.

**Forbidden weakenings:** Sampling only part of the bank, replacing strict
inequalities with rounded ties, or assuming lift `0` wins because it is called
preferred.

**Required boundary cases:** The equality `c=b_0`, where the adjacent pieces
of `V_tau(H_0)` meet, and strict middle-branch membership for all competitors.

**Completion witness:** An explicit table of positive breakpoint, window, branch,
and selector-gap margins, reproduced by the paired runner.

**Not closure:** A claim that `tau_phys=tau_b,min`, a microscopic selector law,
or a theorem beyond the recovered bank.
