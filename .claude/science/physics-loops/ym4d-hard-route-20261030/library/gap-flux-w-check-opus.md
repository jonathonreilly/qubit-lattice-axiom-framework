lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-17T02:37Z

# Check of row 1052's Lemma FLUX-W and target T_JW-lat (row 1054)

Written by Claude Opus 5.5 (max), Mac mini worker 3, started 2026-11-16 14:37Z (date -u),
from commit b04caeebc on branch claude/ym4d-hard-route. Same provider as the author of
row 1052 (Claude Opus 5.5 high), so this is not an independent check in the sense of the
working rules; row 1055 (gpt-6-astra) is the cross-provider check. A research check, not an
audit; no mass gap is claimed anywhere in this file.

Object checked: `library/gap-wall-assumptions-opus.md` (row 1052) at b04caeebc: Lemma
FLUX-W (a)-(d), the definition of T_JW-lat (6b), sections 6c and 6d, and the Reading
"(W) = Jaffe-Witten gap + unbroken centre on tori".

## Plan (at most eight steps, one per response)

1. Read the sources: FINISH rules (build on published work, efficiency, rules), row 1052's
   FLUX-W, 6b-6d and Reading, and the on-file statements it uses: (W), (TM-c), (G1) of
   row 720, (PHYS-SEED), M_*.
2. Hand test of (a): one plaquette in an (i,k)-plane at the crossing plane; plaquette count;
   Haar invariance; commutation of C_i with T on gauge-invariant functions (TM-c).
3. Hand test of (b), (c): a two-state toy transfer operator; psi_0 invariance; E_e >= m.
4. Check (d): (G1) of row 720, (PHYS-SEED), M_*; does (W) force every flux energy above M_*.
5. Check T_JW-lat (6b): definition, and whether it implies the Jaffe-Witten gap for the
   lattice route.
6. Check 6c (frozen Z_2, Q_8, 2T do not bind T_JW-lat; flat field on a simply connected
   region is pure gauge) and 6d (no set-aside verdict changes).
7. Check the Reading ((W) = JW gap + unbroken centre on tori; argued one way, reading for
   strictness).
8. Meaning: does replacing (W) by T_JW-lat lose or gain anything; is it easier for SU(2).
   Verdicts, RESULT line.

## Status

Step 1 in progress.
