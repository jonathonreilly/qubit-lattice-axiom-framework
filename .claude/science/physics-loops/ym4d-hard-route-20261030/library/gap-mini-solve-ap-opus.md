lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-21T01:35Z

# gap-mini-solve-ap-opus: queue row 1280

Started 2026-11-20T13:35Z (date -u). Pinned commit 220f8a48d, branch claude/ym4d-hard-route.
Task (row 1280): prove that four-dimensional SU(2) Yang-Mills theory has a mass gap in the Jaffe-Witten sense; first consider how best to attack it, then do it.
Labels: PROVED, ARGUED, GUIDE, OPEN. Numerics guide only.

## Status

Step 0 (reading the folder rules and the earlier work): done 2026-11-20T13:48Z (date -u). Step 1 (choice of attack): in progress.

## Step 0. Record read (statements about the record, not evidence; written 2026-11-20T13:48Z by date -u)

Read: `GOAL.md` in full; `FINISH.md` L1-84 and L299-360; the row of this item (L1361); the RESULT lines of rows
1007, 1009-1011, 1013, 1016, 1228, 1255-1260, 1264, 1267-1269, 1273-1276, 1279; `parts/gap.md` L1-104 (state of
attack); `library/prior/gap-onebound-read-sol.md` (row 1218) in full; `library/gap-phys-seed.md` L311-401 (Theorem
ZD-c, Corollary Z4, Proposition MB, (MONO-Delta)); `library/gap-mini-solve-i-fable.md` L23-114 and
`library/gap-mini-solve-b-fable.md` L35-57 (the screening tables); `library/gap-mini-solve-al-opus.md` L34-59 and
L545-576; the opening of `library/gap-mini-solve-an-opus.md` (row 1277, in flight on worker 1: the slab hypothesis
(M) of Bhattacharjee et al. along the 4D tuning, so this row does not take it).

What the record fixes (each item cites where it is proved or checked; none is re-derived here):

1. The gap clause splits (Theorem BP, row 1179, check 1183): the continuum datum of the T0 chain plus one lattice
   input, (N-phys) of row 1161: at one physical side, uniformly in the cutoff, the periodic centre-neutral excited
   trace of the cube at a time u at most n/K is at most 1/2.
2. (N-phys) is equivalent in strength to a lower bound of asymptotic-scaling type on the deconfinement coupling at
   temporal extent n/K (rows 1180, 1184, check 1187). It implies confinement of static charges at every coupling,
   itself open for 4D SU(2).
3. The one-cutoff carry (row 1233 Proposition 3.7 and rows 1255-1275) reduces the all-cutoff input to one datum at
   one coupling, modulo inputs of the Sussman-Alpoge account and of Balaban's CMP 116 (not on this machine).
4. Row 1218's sources: A (Bhattacharjee et al.) gives a one-scale thermal criterion with a conditional ascent of the
   lane's own kind (stronger than (N-phys)); B's weak-coupling Corollary 166 is non-selective (it holds for the
   massless Villain U(1) as well; on file in the rows that cite it); Zeng's routes are conditional.
5. More than seventy candidate mechanisms for the seed have been screened by rows 998, 1128-1130, 1179-1199 and
   1255-1275; each stops at the same place: no selective inequality is known at order-one coupling, and the only
   all-coupling template (the posted 2D O(N) proofs) needs a rigid non-abelian symmetry on the integration variables,
   which lattice gauge theory lacks (Lemma CEN+, row 1016; row 1228).
