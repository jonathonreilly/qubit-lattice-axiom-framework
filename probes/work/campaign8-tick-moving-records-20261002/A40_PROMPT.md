You are lane A40 of an overnight, derivation-focused exploration ("Campaign 8"). This is the last lane, a SYNTHESIS: **one pattern of "kinds of places" for everything?** Time box: about 50 minutes. Derivation first, with tiny checks only.

## Why
Several late results point the same way, but they have not been put together.
- **A25:** the gravity ("shape") field needs a fixed 2×2×2 role layout (vertex, edge, face and cube roles; 1 of 8 translates; F6). As built, every role carries a field job. It also needs more than one qubit of content per place.
- **A31 D10:** if gravity's field lives in one qubit per place and records never lock it, then field places can never be recorded. **A34 C61:** in A25's layout every place carries field, so D10 would forbid all records unless a one-qubit field leaves some places free (not built).
- **A39 escape (e):** quiet empty space can carry light only if light is invisible to records. Records form only on matter places; light lives on field places that never record. The costs: two kinds of places, a law that treats them differently, and matter number exactly conserved (no vacuum pair creation).
- **A31 Theorem S, A33's parity route and A38:**
  - a painted π-flux sign pattern for matter cannot keep the field layout's face-diagonal half-turns;
  - the parity route allows a state-level 8-fold pattern to supply the twist, but A38's only covariant pointing texture gives a 2π/3 twist, not π.
- **A26:** matter couples to the gravity field through lapse and frame; the cross shear needs an in-cell sandwich (2×2 cells).

## Read (primary files; do not trust summaries)
SP=/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-focused-noyce-9a3983/34c0b720-f781-4af0-9bb7-5d2e1b60d22e/scratchpad
- `SP/c8/BRIEF.md`.
- The ERRATA sections at the end of each report below.
- `SP/c8/A25/REPORT.md`, `SP/c8/A31/REPORT.md`, `SP/c8/A33/REPORT.md`, `SP/c8/A38/REPORT.md`, `SP/c8/A39/REPORT.md`, `SP/c8/A26/REPORT.md`.
- `SP/c8/A34/REVIEW.md` C58, C61; `SP/c8/A34/REVIEW2.md` C89.

## Questions
1. **A layout.** Is there an assignment of the 8 roles of a 2×2×2 cell (or a coarser or finer one) into three kinds?
   - "Field places" carry light and gravity and never record.
   - "Matter places" can record; their quiet vacuum is calm and they carry matter.
   - Optionally "buffer places".

   The assignment should be consistent with:
   - the 24 site-centred turns (up to translation: a state-level pattern);
   - A25's need for vertex, face, edge and cube field components;
   - A31 D10;
   - A39 (e)'s conditions;
   - matter needing its own twist (A31/A33/A38).

   Enumerate role assignments up to symmetry, and list which constraints each one meets or breaks.
2. **Payload count.** How many real numbers or qubits per place does each kind need: the field's content (A25: 3, 1, 2 or 3 reals per role), matter's qubit, and light's sector? Is "more room per place" (a Qubit-axiom change) unavoidable in every assignment? State it exactly where possible.
3. **Couplings across kinds.** Matter places must feel gravity (A26 lapse and frame) and absorb light (A39: light recorded only through matter) without making field places record. What does the formation weight look like (F = F_matter ⊗ 1_field)? Is it consistent with Q7 (menus set by the conditions, including recorded neighbours) and with no-signalling (linear weights)?
4. **Does the matter twist (π flux) fit the kinds pattern?** Could matter places be only some roles, so that matter's sublattice structure lets π flux be compatible with the field layout (re-examine Theorem S's hypothesis "every plaquette touches a vertex- or cube-role site", or use matter-only plaquettes)? Give an exact symmetry statement where you can.
5. **Verdict for the owner.**
   - Is "one 1-of-8 pattern of kinds of places, where fields live on never-recording places and records live on matter places" a coherent single supplied choice?
   - Which earlier decisions does it bundle (13, 17, 21, 24, A39's decision)?
   - What does it cost against the axioms ("No site is privileged" versus a state-level pattern; one qubit per site)?

## Rules
- **Grading.** Grade every claim EXACT, CHECKED, ARGUED, SUPPLIED or COMPARATOR.
- **Language.** Never say a possibility is "read" or that a "question is asked". Never present a beat or heartbeat as adopted. Propose nothing as adopted; frame everything as owner decisions.
- **Compute.** Tiny checks only: `nice -n 10`, the four BLAS thread caps at 1, each run under 30 s and 200 MB, and only when the 1-minute load is below 6.
- **Files.** No git, no repo edits, no PRs. Put scripts in `SP/c8/A40/`. If your sandbox blocks writing REPORT.md, return the full report as your final message.

## Output
A report with these sections:
1. Question
2. Answer: short, graded
3. Derivation: role assignments, payloads, couplings, the twist
4. Checks
5. Open edges
6. Plain-language summary: one paragraph for the owner
