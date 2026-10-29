# Author brief: cost soft blocking (decision 4) against Balaban's hard δ-constraint

Lead: Claude Opus 5.5, 2026-10-29. One Codex author context runs on the Mac mini; a separate reviewer follows.
The session that would have priced decision 4 was planned in RTARGET.md l.670 and never ran. This lane runs it.

## Question
Do we keep decision 4 (the soft gauge-covariant S4' kernel), switch to Balaban's hard δ(M(U)V^{-1})
blocking, or use a hybrid? A hybrid would be, for example, hard on the h_U part and 't Hooft-averaged on
the residual, as NA-FP already does (SF.md l.1635); or a soft kernel with κ → ∞ on some levels only. The
criterion is the total remaining work to the FULL proof as HANDOFF.md defines it ("Active full-proof
goal" and "Remaining proof path", steps 1-6), not elegance.

## Sources
- **Our files (this folder).** Use `grep -n` and read by offset; never read a file over about 1000 lines
  whole.
  - HANDOFF.md, ASSEMBLY55.md, CODEX_REVIEW_ASSEMBLY.md.
  - PROOF.md: "Decision 4: the RG kernel" and "Decision 4 is MADE".
  - REVIEW_S9_S10.md: D4-obs and decision-4 governance.
  - RTARGET.md: around l.203, l.475 and l.1152 (BAL-F3).
  - STEP55.md and CODEX_REVIEW_STEP.md: the normaliser 𝒩_t and the returned denominator.
  - ALIGN55.md, CODEX_REVIEW_ALIGN*.md and RECOVERY_ALIGNMENT_ASTRA.md: S_E and axial both fail.
  - BFT_A.md, BFT_B.md, REVIEW_BFT_B_S8.md: background regularity, slices, root spikes.
  - SPHERE2_55.md l.500-512: softness is load-bearing at the seam.
  - LARGE55.md, LCONV55.md and their Codex reviews.
  - literature/NOTES.md: our Balaban/Dimock extracts. Only CMP 109:249-301 was read directly.
- **Open literature only.** Balaban's own CMP papers are not available. Use the arXiv papers that cite and
  reconstruct his work. Look under ARXIV_DIR, which the wrapper gives you; it may be empty. In particular
  look for:
  - Dimock, "The renormalization group according to Balaban" I-III (arXiv, including 1212.5562);
  - Dimock's other expositions;
  - other open reconstructions you find there.
- **No paywalled or pirated sources.** Never use Sci-Hub or LibGen, and do not try to get around a bot
  check. Mark anything you cite from memory as [m]. An [m] item is never load-bearing.

## Deliverable: SOFTHARD.md
1. **Ledger of soft-specific costs.** List every open or recently closed obstruction in our files whose
   existence, or whose difficulty, comes from the softness of the kernel. For each one give:
   - the exact quote and its location;
   - why softness causes it;
   - what the hard route needs in its place, quoting the open literature with section and equation where
     it exists, and saying explicitly when it does not;
   - whether that replacement is proven in the open literature for 4D non-abelian gauge theory, proven only
     for scalars or abelian/QED, or not available openly.

   At minimum cover:
   - the normaliser and returned denominator;
   - the slice/alignment failures and the background-field theorem's background regularity, including lane
     A's root-funnel spikes;
   - D4-obs (the observable comparison);
   - the κ windows;
   - the large-field architecture (LARGE55 / LCONV55).
2. **Ledger of soft-specific gains.** List what the hard route would lose or need to re-prove. Each entry
   must name the files whose reviewed results would be invalidated. Include:
   - complex continuation and cluster expansion on the smooth kernel;
   - the sphere-seam argument;
   - bare-marginal invariance. Check whether a normalised δ also preserves the Wilson marginal; we believe
     it does, so verify it rather than assume it;
   - every PROVEN or Codex-confirmed item that consumes the soft kernel's form.
3. **Hybrid options.** Check at least two concrete hybrids against both ledgers.
4. **Verdict.** Give one of KEEP-SOFT, SWITCH-HARD or HYBRID-<name>, with:
   - the reason;
   - the reviewed results lost if we switch;
   - the walls removed and the walls added;
   - the single decisive open question, if the verdict depends on one.
   This is a recommendation to the owner, not a decision: decision 4 stays in force until the owner rules.
5. **Exact finite check (optional).** Run one only if it settles a disputed ledger entry, for example
   whether the normalised δ kernel preserves the bare marginal on a tiny finite-group lattice.
   - Write `checks/sh_criteria.md` before the script.
   - Run one process with `nice -n 10`, with every BLAS thread variable set to 1.
   - Keep RSS under 2 GB, checked by the script itself, which exits if it is exceeded.
   - Start only if `memory_pressure` shows at least 50% free and the load average is below 20.
   - Never use multiprocessing pools.

## Provenance
- The very first edit is the PRE-STATED section of SOFTHARD.md, containing statements only. Log its stat
  and byte size in SOFTHARD_LOG.md.
- Statuses: PROVEN, ARGUED, OPEN, or QUOTED (with the source).

## Rules
- Write only SOFTHARD.md, SOFTHARD_LOG.md and checks/sh_*.
- No commits, pushes or PRs. Edit no other file.
- No audit or ledger files, and no axiom edits.
- Final message under 300 words: the verdict, the top three entries from each ledger, and the decisive
  question.

## Owner directive (added 2026-10-29 17:30 UTC, after launch)
"if we need their proofs or lemmas just rebuild them and put them in the repo / PR / library. why keep referencing papers."
- Literature results are never load-bearing citations. Price each hard-route requirement as the cost of
  rebuilding it as a self-contained proof on our structures.
- Add a section **"Library rebuild list"**: the specific lemmas from the open expositions (Dimock and others)
  that either route needs. For each, give its statement, a size and difficulty estimate, and whether the open
  text contains a complete proof we can rebuild.
- Credit the original authors by name in each entry.
