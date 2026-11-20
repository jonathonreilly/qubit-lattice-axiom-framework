lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-20T18:20Z

# gap-mini-solve-s-opus: the SU(2) mass gap, attack s (Opus 5.5 max, Mac mini worker 2)

Queue row 1228 of `FINISH.md`. Pinned at commit b34979e9a on branch `claude/ym4d-hard-route`.
Started 2026-11-20T06:20Z (date -u).

Labels: PROVED (written argument, checkable by hand), ARGUED (argument with a named gap), GUIDE (heuristic or numeric orientation, never a proof step), OPEN.

## Status

Step 0: file created. Reading the brief, FINISH.md rules, `parts/gap.md`, the RESULT lines of the earlier gap rows and `library/prior/gap-onebound-read-sol.md`.

## Step 0. Where the lane stands (record, not evidence; read 06:20Z-06:40Z)

Read: `GOAL.md`; `FINISH.md` L1-84, L299-360 and row 1228; RESULT lines of rows 1188-1225 (mini-solve a-r) and of
rows 1222, 1227, 1230; `library/gap-mini-branch-fable.md` L296-360 ((N-phys) and Theorem BP); `parts/gap.md` L1-60;
`library/gap-mini-solve-i-fable.md` L1-80 (screening table 1.2); `library/gap-mini-solve-p-fable.md` L250-300.

1. By Theorem BP (row 1179, check 1183) the only open lattice input of the Jaffe-Witten gap clause on the account's
   tr F^2 sector is (N-phys): at one physical side L, for every cutoff index j, the periodic centre-neutral excited
   trace of the cube n_j^3 at some time u_j <= n_j/K is at most 1/2. The other input is the continuum datum of the
   T0 chain (row 1225 Theorem E-N, unchecked composition).
2. In thermal words (rows 1180, 1184): the periodic box of side L at temperature K/L is on the confined side with a
   dilute neutral gas. Physically true for L large against the inverse glueball mass; false for small L.
3. Eighteen plain-brief rows (a-r) screened about fifty route families; every one is on the lane's map with a named
   failing step. Row 1224 (q) 8.4 recommends one precise question per row instead of a further screening.
4. Consequence for this row: no new screening. One precise question is chosen in Step 1, grepped against the record,
   and attacked to a proof or a counterexample.

## Step 1. How best to attack it (06:50Z)

**Judgement (ARGUED).** Every route on file ends at one kind of step: a selective inequality carried through the
band, where the running coupling is of order one. The only selective multiscale monotone in the literature is the
pinned-cell stiffness flow of OpenAI's 2D O(4) paper (row 1007 7.3; rows 1009-1016 read and port it). It works because
its twist is a global symmetry, so it acts on every pin, rough or not, and its direct cost is classical (row 1011
(M2)-(M3)). In 4D pure gauge theory the port fails at exactly that point: a twist applied to a rough pin has a
pin supremum that forgets colour coherence (row 1011 Proposition B, B'; row 1016 Theorem BH), there is no hidden
symmetry (Lemma CEN+), and any colour frame costs the non-abelian part of the pin (Lemma FR).

**The precise question of this row.** Proposition B concerns twists applied to the rough pins themselves. A cell of
a tiling has rough pins on its faces, but the twist need not live there. Put it on one face that is smooth: the
bottom face of a slab-shaped cell, pinned to a fixed abelian (here trivial) configuration, as in the
Schrodinger functional of Luscher, Narayanan, Weisz and Wolff. All other faces carry arbitrary pins. Then:

(Q-SF) Is the class of such cells closed under conditioning on the cell boundaries of a tiling, and does its
stiffness for a constant bottom twist have the two properties the 2D flow needs: a twist that is locally a
symmetry, and a start bound by dropping the covariance that is classical and uniform over the other pins?

Grep before work (06:45Z): `one smooth face`, `abelian bottom`, `smooth bottom`, `other faces arbitrary`,
`twist on one face`, `remaining faces` over `library/gap-*.md`: no hit on this class. Nearest on file: row 1011 4.7 (ii)
(all-abelian pins, not closed under conditioning); row 1195 (S1') (all-abelian pins); row 1202 (slab between two
trivially pinned plates, no tiling); row 1016 Lemma GT (Jacobian-one transports along curves). `library/open-core.md`
has no gap-lane entry for it.

Why either answer helps. If (Q-SF) holds, the 2D flow has a 4D gauge form with a class closed under conditioning,
and the next step is the variance gain (row 1011 (N3)). If it fails, the failure shows whether the obstruction is
the location of the twist (pins) or the interior non-abelian field, which sharpens row 1011 (N1)-(N3).

