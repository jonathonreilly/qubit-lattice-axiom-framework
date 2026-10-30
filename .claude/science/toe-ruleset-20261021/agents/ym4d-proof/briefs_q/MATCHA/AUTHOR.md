# Lane MATCHA: build RM1 on an actual mixed history, by opening its ancestry
**Why.** REFMATCH.md (LAND, c00876a6da) PROVES a conditional theorem for one complete real RG step (§6). Its §7 table lists the OPEN inputs. The first and most discriminating is the **exact inherited-to-product reference (RM1)**, with fixed support and the full main action, plus the differentiated background smallness **RM2** and its regeneration. REFMATCH §7's ARGUED next construction: start with one bounded mixed core on a fixed positive sector, open its inherited ancestry, and write the actual paired numerator and reference on identical variables. Then absorb the nonperturbative main action into an explicitly specified reference *before* testing RM2.

**Target.** Execute that construction.
1. Take one bounded mixed core on a fixed positive sector. Open its inherited ancestry and write the exact paired numerator/reference on identical variables. Keep all endpoint masses, rho/b_j, a fine/coarse derivative, and the four original source labels.
2. Absorb the main action into the specified reference. Test RM2 on what remains: is the remainder a small differentiated tilt, in the fixed norm, with the support rate that RM9–RM13 need? Give the exact number, or the exact failing inequality.
3. Say whether this generalises uniformly over histories, or which history class it fails for.

**Deliverable: MATCHA.md**, with each item marked PROVEN, ARGUED or OPEN. Read REFMATCH.md and its review, MIXSMALL.md, REALRGA.md, RD3.md, RD4.md, CHARGE.md.

## Common rules (all queue lanes)
- **Process.** Follow PROCESS_LIGHT.md. Pre-register any numerics in checks/matcha_criteria.md. Report statuses honestly as PROVEN, ARGUED or OPEN. A check that fails is reported as failed.
- **Files you may touch.** Create and edit only MATCHA.md, MATCHA_LOG.md and checks/matcha_*. Do not modify any existing file. The runner discards all other edits.
- **Coordinator lanes.** Avoid the active coordinator lanes listed under HANDOFF.md "Current assignments": fixed source radius, finite-coupling kernel remainder, original-law coercivity and tails. If you need one of their outputs, state it as a named input.
- **Reading.** Use grep -n and offsets for large files. Literature may supply methods only. Credit the authors, and mark anything recalled from memory as [m]. An [m] item can never carry weight in the argument.
- **Resources.** Run with nice and BLAS=1, under 1 GB (self-check RSS via resource.getrusage or psutil; do NOT use resource.setrlimit(RLIMIT_AS) - it fails on macOS), with load < 8 and at least 30% memory free. No pools. The sandbox may block nice; if it does, report that instead of weakening the guard.
- **Limits.** No commits. No audit or ledger files. No axiom edits. Final message under 300 words.
