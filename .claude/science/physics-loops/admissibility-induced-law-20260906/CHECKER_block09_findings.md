# Refuting pass — block 09 (supervisor-run, disjoint machinery; 2026-09-15)

`specs/supervisor_control_block09_refuter.py` (output in `.out.txt`); not an independent review.

| item | runner's route | refuting route | result |
|---|---|---|---|
| R1's dependence witness at (3,1,2) | the kernel formula with `K_3` on the three triples containing `x` | the conditional of the center of the 3x3x3 box from block 08's product form (`law_by_product_form`-style evaluation of all 27 sites' factors), all sites `+x`, the site `x + e_1 − e_2` varied | `793975879125/24719290847393`, equal |
| R3's within-pair witness | the two kernels `γ^{+++}_x`, `γ^{−−−}_x` on the same twelve-site configuration | the 3x3x3 product forms of the two classes (predecessors `x − e_i` versus `x + e_i`) at the center, search over the `6^6` diagonal assignments | `1646222697/263752139417`, equal |
| R4's irreversibility on the 2x2 column | `TV(J, J^T)` over unordered pairs from the orbit-reduced `π` | both marginals of `J` equal `π` (consistency), the reversed transfer `P*` is stochastic, and the total variation over ordered pairs halved | equal |

Attempts to refute the lemmas (nothing refuted): L1 — the finite identity needs every triple meeting the window to be an interior triple; the corner-receding limit of block 08 supplies boxes with that property for any fixed window. L2 — the a.s. equality of two versions of a conditional probability is standard; the step to everywhere-equality needs only full support and finite dependence, both proved. R3(c) — the ergodicity of each `μ_κ` from exponential decay of correlations (mixing ⇒ ergodic) and the mutual singularity of distinct ergodic laws are cited definition-level and used only in the last sentence of R3(c).

Findings: F1 (fixed) the phrase "no arrow of time is derived" collided with the runner's forbidden token — reworded. F2 (fixed) decimal strings in the runner tripped its own float scan — replaced by exact rational literals. F3 (fixed) the plane-law note landed on main after block 08's branch was cut; the stack was rebased onto that main so the note is a declared input. F4 (fixed) the note's own Review record quoted the offending phrase verbatim and re-tripped the substring scan; reworded (lesson: never quote a forbidden token inside the note, even to report its removal). Verdict of this pass: PASS-NO-BLOCKER at the supervisor's own standard, pending the owner's independent review.
