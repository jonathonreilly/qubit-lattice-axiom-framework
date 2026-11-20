lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-21T02:40Z

# Check of row 1286 (gap-owner-tiling-astra62): cross-provider, line by line

Queue row 1287. Checker: Claude Opus 5.5 max, Mac mini Claude worker 2. Started 2026-11-20T14:40Z (date -u).
Branch claude/ym4d-hard-route, pinned at a725fa855.
Target of the check: `library/gap-owner-tiling-astra62.md` (gpt-6.2-astra max, row 1286).
Background read against: rows 1273 and 1279 and their notes.

Process: each statement gets HOLDS, HOLDS AFTER CORRECTION, or FAILS, with the line.
Labels in this file: PROVED, ARGUED, GUIDE, OPEN. No numeric run is a proof step.

## Plan (at most eight steps)

1. Read the target note in full; list its claims with line numbers; read rows 1273 and 1279 and their notes.
2. Check the tree-sewing gap kappa_r g^(2/3)/(N l) for N^3 reduced blocks with dynamical frames; decide whether it is uniform in N.
3. Check the cyclic adjoint sewing count (12): at least 3N^3 soft centre-neutral excitations.
4. Check the Wilson-law bound (7).
5. Check every other statement of the note, against rows 1273 and 1279.
6. Say plainly what this means for the owner's tiling question.
7. Verdict table and RESULT line.

## Step log

(Steps are appended below as they finish.)

### Step 1. What the note claims (line numbers of `gap-owner-tiling-astra62.md` at a725fa855)

Read in full: the note (209 lines); row 1273's note, Lemma S and S_n (`gap-owner-threeaxis-opus.md` 324-395); check 1279 (`gap-threeaxis-check-astra.md`, all 123 lines); FINISH rows 1273, 1279, 1286, 1287.

Claims labelled PROVED by the author, grouped as the row asks:

- **Tree sewing (row's first claim).** (3) at 60-65 (common-frame constrained array); (4) at 67-72 (stiff springs, fixed graph, gap -> M^(-1/3) kappa_r in units g^(2/3)/l); (5) at 74-83; (6) at 85-91; spectral limit, upper and lower bounds 93-95; the "fixed fraction fails" corollary 97; thermal opposite answers 99-101; the tree with dynamical links and Gauss law 172-176.
- **Cyclic adjoint sewing (row's second claim).** (8)-(9)-(10) at 136-168 (ground energy and loop holonomy bounds); (11) at 153-159 (heat-kernel walk inequality); (12) at 178-191 (3M soft neutral levels); thermal consequence 193-197; the Wilson Hessian example at 170.
- **Wilson law (row's third claim).** Commutator mean 3/4 at 15; bond colouring 19-21; conditional density (1) at 23-27; low-energy bound (2) at 30-46; cutoff scope 48; trace sandwich (7) at 107-124; J > 0 at 126; comparison operators with the same O-histories 201-205.
- **OPEN and GUIDE.** 11, 128, 207 (OPEN); 3-9, 17, 52, 103, 130, 134 (GUIDE).

Background fixed by check 1279 (HOLDS there): Lemma S_n, K_n >= sqrt((n-1)/2) sum_i |y_i|, discrete singlet spectrum, gap kappa_n g^(2/3)/L, n >= 2. The note's r is row 1273's n (number of colour vectors per block).
