# Lane REALRGA: design the real-derivative (Taylor-seminorm) RG induction contract
**Why.** REALONLY.md (LAND, cd67e1c9e6) proves REAL-SUFFICES for every downstream consumer: H_reg/E0′, PL-1L, K4MATCH, TQ2, N5B, REC/OSLEAF, the coupling flow and the source response. Only the *existing* RG contract (RD4 / LF-JMBR / STEP55) is COMPLEX-NEEDED, and only because of its contours, holomorphic logarithms and maximum principle. REALONLY §7 says a real-derivative induction "is a different, presently unconstructed contract". Five RG-core lanes stalled at the complex mixed-reader norm.

**Target.** Design the contract precisely, as an induction hypothesis that is carried from step to step:
1. **The norm.** Specify real Taylor seminorms of polymer activities in the fine and coarse fields and in the original sources: the order k of derivatives, the field-size regulators (large-field weights), and the locality/decay weights. Method precedent: Bauerschmidt–Brydges–Slade's T_φ seminorms for φ⁴ and SAW, and Brydges' Taylor seminorms. Credit them, and rebuild everything here for SU(N) lattice gauge fields with the soft kernel.
2. **The replacements.** For each place where the current contract uses complex analyticity, give the real replacement and prove it, or name it as OPEN:
   - zero-freeness of normalizers. Real positivity may make it trivial for real sources; check this;
   - Cauchy derivative bounds, replaced by direct derivative estimates through the chain rule and the product property of Taylor seminorms;
   - logarithms of partition functions, replaced by real logarithms of positive quantities;
   - polymer-gas cluster expansion. A real-norm cluster expansion needs either convergent Mayer bounds with real activities or a BBS-style "Polymer gas / circle product" formulation. Specify which.
3. **What carries over.** Map every landed RG-core result onto the new contract and mark each one CARRIES, NEEDS-REWORK or OBSOLETE. The results are CHARGE (real-sector, PROVEN), RD3, RD4, JMBRA, JMBRB, RENEW, LFPRICE and LIB1.
4. **Consumer check.** Show that the contract's output gives exactly the real estimates that REALONLY's consumers need, using REALONLY's table.

**Deliverable: REALRGA.md**, containing the contract statement, a status per item, and the carry-over map.

## Common rules (all queue lanes)
- **Process.** Follow PROCESS_LIGHT.md. Pre-register any numerics in checks/realrga_criteria.md. Report statuses honestly as PROVEN, ARGUED or OPEN. A check that fails is reported as failed.
- **Files you may touch.** Create and edit only REALRGA.md, REALRGA_LOG.md and checks/realrga_*. Do not modify any existing file. The runner discards all other edits.
- **Coordinator lanes.** Avoid the active coordinator lanes listed under HANDOFF.md "Current assignments": fixed source radius, finite-coupling kernel remainder, original-law coercivity and tails. If you need one of their outputs, state it as a named input.
- **Reading.** Use grep -n and offsets for large files. Literature may supply methods only. Credit the authors, and mark anything recalled from memory as [m]. An [m] item can never carry weight in the argument.
- **Resources.** Run with nice and BLAS=1, under 1 GB (self-check RSS via resource.getrusage or psutil; do NOT use resource.setrlimit(RLIMIT_AS) - it fails on macOS), with load < 8 and at least 30% memory free. No pools. The sandbox may block nice; if it does, report that instead of weakening the guard.
- **Limits.** No commits. No audit or ledger files. No axiom edits. Final message under 300 words.
