# Lane CHARGE: renewal after charging the original weight (the route RENEW leaves open)
**Why.** RENEW.md (LAND, scoped) PROVES an exact periodic SU(N) family, for every N ≥ 2 and every odd L ≥ 3, of persistent-flux coarse fields that stay maximally rough under the RG. Positive-measure neighbourhoods of it persist for any finite number of steps. That refutes a uniform *forward, pointwise-in-input* return mechanism. RENEW explicitly does **not** refute renewal **after charging the original weight**, changing the matched reference, or extracting relevant or marginal terms. It also proves that localized linear defects dilute as L^(-2r), and it names the exact missing sub-lemma: a finite-window operator bound on the actual all-cut reference.

**Target.** Probe each mechanism below.
- **(R1) Charge the original weight.** Persistent-flux configurations carry Wilson action, roughly flux² per block, at *every* scale. Show that charging that action once, at the original scale where it is paid, outweighs their entropy and their persistence across all later steps. Build the history-level accounting so that this action is not counted twice (keep RD's "raw charges used once" rule). Decide whether the resulting price beats the per-step volume factor.
- **(R2) Extract the flux sector.** Treat persistent flux as a separate topological or flux sector. Possibilities: a sum over flux classes (twisted boundary conditions, torons), or a background-field expansion around the flux solution, where BFT_A and BFT_B cover nontrivial backgrounds at their reviewed scope. Renewal is then only needed relative to the sector's background.
- **(R3) The finite-window operator bound.** Prove RENEW's named sub-lemma: exact reader integration (JMBRA clause 1) combined with fresh-gap prices (JMBRB) on the all-cut reference.

For each mechanism, report PROVEN, ARGUED or OPEN, with the exact failing inequality if there is one. Give the updated status of LF-JMBR clauses 2–5. If renewal fails even after charging, say whether the soft-kernel route needs a change, and which one.

**Deliverable: CHARGE.md.** Read RENEW.md and its review, JMBRA.md, JMBRB.md, LFPRICE.md, RD3.md, RD4.md, BFT_A.md and BFT_B.md (nontrivial-background clauses), the existence lane's Polyakov/flux material (grep ../ym4d-existence/E/EXISTENCE.md for torons and flux), and SOFTHARD.md.

## Common rules (all queue lanes)
- **Process.** Follow PROCESS_LIGHT.md. Pre-register any numerics in checks/charge_criteria.md. Report statuses honestly as PROVEN, ARGUED or OPEN. A check that fails is reported as failed.
- **Files you may touch.** Create and edit only CHARGE.md, CHARGE_LOG.md and checks/charge_*. Do not modify any existing file. The runner discards all other edits.
- **Coordinator lanes.** Avoid the active coordinator lanes listed under HANDOFF.md "Current assignments": fixed source radius, finite-coupling kernel remainder, original-law coercivity and tails. If you need one of their outputs, state it as a named input.
- **Reading.** Use grep -n and offsets for large files. Literature may supply methods only. Credit the authors, and mark anything recalled from memory as [m]. An [m] item can never carry weight in the argument.
- **Resources.** Run with nice and BLAS=1, under 1 GB (self-check RSS via resource.getrusage or psutil; do NOT use resource.setrlimit(RLIMIT_AS) - it fails on macOS), with load < 8 and at least 30% memory free. No pools. The sandbox may block nice; if it does, report that instead of weakening the guard.
- **Limits.** No commits. No audit or ledger files. No axiom edits. Final message under 300 words.
