# HOLEPAY affected-source review — final research-note disposition

Review date: 2026-10-30. All five findings in
[the first review](holepay_review.md) are resolved on the final identities
below. The note is suitable to retain as a **research note containing a
raw differentiated charge, geometric results, scoped counterexamples, and
conditional implications**. This verdict does not close EXTCONT E15,
authorize public proof-complete language, confer audit status, or establish
a Yang–Mills existence/mass-gap result.

## Finding dispositions

| First-review finding | Final source and disposition |
|---|---|
| HP12–HP14 sign/count hypotheses | **Resolved.** HOLEPAY.md:290–306 requires integer n>=1, c_H>0, and nonnegative charge/reference/boundary constants. The boundary substitution now has the required sign; HP14's division is defined. |
| History envelope and missing constant | **Resolved.** HOLEPAY.md:346–370 separates a directly estimated coefficient from distinct history masks. HP14h explicitly bounds the sum of history input norms by `B_hist M_input` and retains `(1+C_hole) B_hist` in the complete output bound. It does not evaluate B_hist or set it to one. |
| HP15 cap-comparison scope | **Resolved.** HOLEPAY.md:381–399 restricts the statement to zero source and a nonnegative sector or complete disjoint history sub-sum with an actual original-action charge. It states `0<zeta<=1`, `4zeta` strictly below every retained cut, and the additional bill owed by source-bearing variants. |
| Full-mask identity | **Resolved.** HOLEPAY.md:96–98 identifies the support map as the identity and retains every supplied weight. The operator is declared an identity only when those weights are one. |
| Refusal after partial mathematics | **Resolved by static control-flow review.** checks/holepay_check.py:20 initializes `math_started=False`; line 240 sets it after the successful initial guard and before the first mathematical routine; lines 250–252 use that flag for INCOMPLETE versus NOT RUN. A refusal inside the first section no longer relies on a completed check row. This path has not been executed. |

The added `w_H=exp(-Q_H)` definition at HOLEPAY.md:113–116 makes HP3's
product identity explicit. The fresh-gap paragraph at lines 401–409 now
carries `t>=1`, `q_gap>=0`, fixed-event boundaries, and its conditional
forward-law scope. Both clarifications agree with the previously checked
argument and add no new model estimate.

For HP14h, the independent check is direct: for every h, HP1 gives
`||output_h|| <= (1+C_hole)||K_h||` with the same constants. Triangle
inequality followed by the stated sum-of-norms envelope gives the displayed
bound, regardless of which inactive component contains a root in each
history. The active part omits the leading 1. A supremum of individual
history norms, or a supremum over roots of the joint rooted input, need not
bound the sum of those norms. The final text preserves this distinction.
An already summed fixed-mask coefficient may instead use HP12 directly,
but only after proving HP12 for that coefficient.

For HP15, its restored conditions make the earlier independent cap
derivation applicable: the plaquette cost is `48u_j zeta^2 n_j`, the
link-cap entropy is `8N^2 log(1+4N/zeta)n_j`, and the final kernel upper
and lower bounds together cost `16kappa u_j n_j/L^4`. The source-free
charge is therefore compared to the actual all-cut denominator with the
stated debit. The conclusion concerns failure of that upper-bound method
at unbounded volume/core ratio, not a lower bound on the actual quotient.

## Coverage, provenance, and remaining limits

I read the complete revision patch, the entire affected mathematical
argument, both changed runner control-flow regions, the revision sidecar,
and the updated log. Applying the patch **in reverse in memory** reconstructed
the exact first-reviewed note and runner hashes. Thus the patch accounts
for every change in those two files; unchanged arguments retain the
coverage and independent derivations recorded in the first review.
All fifteen entries in the existing source inventory still match their
recorded hashes. No underlying scientific premise changed.

The original review, criteria, execution JSON, stdout and stderr are
unchanged. The log correctly identifies the execution receipt as belonging
to the original runner and note, and the revised runner as unexecuted.
The receipt remains **NOT RUN**, with no mathematical PASS. The declared
geometry probe is an arbitrary-set regression, including a later seed
inside an existing hole; the log correctly says it does not realize RD
R2's active-only birth rule. This is a diagnostic coverage limit, not a
counterexample to the written cohort bound.

No remaining review defect blocks the research note at this scope. The
actual local paired representation, uniform quotient scores, current
selector regularity, original-reader payment, and complete history budget
remain open. HP14 and HP14h are unevaluated hypotheses. The corrected text
does not convert the smooth original-integrand factor into a proved
integrated history activity or claim a general obstruction.

| Final or preserved artifact | SHA-256 |
|---|---|
| HOLEPAY.md — final science source | b4e8cc82f2344a955d2ced33ded900af8d39a354dcbff21d8423b331121de4d4 |
| checks/holepay_check.py — final runner | 25e798d06c2b33b513cfc0ffde9aa32d5c4f764ddc8e014f45baf9e9fe75ee6b |
| checks/holepay_criteria.md — unchanged | 9eaf6cb4ac6605953326cf29993a81a337ed4c38b463b7ed47fb0251771153f4 |
| checks/holepay_review.md — preserved first review | cb6ccd04b6707b1e69631487aac3008e35374f24879c0bf3d4046635de5ac770 |
| checks/holepay_review_fix.patch | 7078d68de1d91aa710ab6e2e979578db294d6de1cd3b890d826df6553790754b |
| checks/holepay_sources.json — unchanged inventory | 2b12a05892f24ef9aee05b36c724207f8a94cba6ac265e47bbabae3bd251eb19 |
| checks/holepay_result.json and holepay_stdout.txt — historical NOT RUN | 0ab226a01873ff93ef55a19784eca32db6d0b25dd7848c0968e2dd1225d38754 |
| checks/holepay_stderr.txt — historical refusal | 1ae2ce53f6c4a3265acd385e7e4a21d827a2b5594337d0d9ae68b92a856b30dc |
| HOLEPAY_LOG.md — reviewed checkpoint before final-verdict bookkeeping | 8538bd0da5b7dec1cbb0edf8d7b491896d0b1b652c78ff3881138666d8d98301 |

This is affected-source confirmation by the **same independent reviewer in
the same session**, continuing the fresh restricted-input review. It is
**same-model-family review (Codex reviewing Codex)**, not a cross-family
check. Shared repository premises and the independence limits of the first
review remain. No scientific computation, runner execution, mutation test,
or unguarded fallback was performed; only text/hash bookkeeping ran. No
formal proof-assistant confirmation is claimed. Remote main freshness is
still uncertified. The reviewer wrote only this new final review file and
did not edit science sources, the first review, prompts, audits, or ledgers.

VERDICT: LAND
