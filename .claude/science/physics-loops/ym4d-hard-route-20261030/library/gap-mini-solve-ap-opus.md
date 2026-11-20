lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-21T01:35Z

# gap-mini-solve-ap-opus: queue row 1280

Started 2026-11-20T13:35Z (date -u). Pinned commit 220f8a48d, branch claude/ym4d-hard-route.
Task (row 1280): prove that four-dimensional SU(2) Yang-Mills theory has a mass gap in the Jaffe-Witten sense; first consider how best to attack it, then do it.
Labels: PROVED, ARGUED, GUIDE, OPEN. Numerics guide only.

## Status

Step 0 (reading the folder rules and the earlier work): done 2026-11-20T13:48Z (date -u). Step 1 (choice of attack): done 2026-11-20T13:52Z. Step 2 (reading the account's test-cube rule): in progress.

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

## Step 1. How best to attack it (judgement, ARGUED; written 2026-11-20T13:52Z by date -u)

**The seed.** I re-derived, before reading the screening tables, about a dozen routes to the infrared input: center
vortex recursions, the 't Hooft electric-magnetic Fourier duality, abelian projection, the small-volume zero-mode
spectrum as a start for a flow, a strong-coupling expansion at the scale where the running coupling is of order one,
Durhuus-Frohlich layers with the posted 2D O(4) theorem, path coupling, Bakry-Emery, positivity of dual spin foams,
continuity in theta, and a scale-invariant infrared limit argued by compactness. Each has a match on file (Step 0, item
5, and the tables cited there), and each stops where the record says: no selective inequality at order-one coupling.
Two remarks of mine, GUIDE only: (i) in the small-volume regime the neutral gap in units of 1/L is smaller for SU(2)
(of order g(L)^(2/3), Simon's quartic valley, row 1273) than for compact U(1) (2 pi, the first photon), so the
deep ultraviolet gives no selective start for a flow in the plain gap variable; the crossing of 2 pi is inside the
band. (ii) The one-cutoff datum that the carry leaves is a statement at one coupling in the band; by the K7 constraint
(row 1189 table) a hand proof of it must be quantitative at order-one coupling. So the carry does not make the seed
easier; it makes the crux a single finite statement. I have no route to the seed that is not on file, and by
`parts/gap.md` (row 998 9.5) another blind screen is waste. I do not attack the seed.

**The item.** The open inputs of the one-cutoff carry on the pin route after row 1268 (8.2 there) are: (U) the
test-cube size; the readings (E0)-(E6) against Balaban's CMP 116 (not on this machine; Project Euclid bot check);
(H2)-(H3) of row 1267; the 9.1 hypothesis (e) `9.1:prop-blind-site-expansions` (outstanding in the account; it
reads CMP 116); (DET)'s inputs. Only (U) and (H2)-(H3) can be worked here without CMP 116. Rule 0a: (U) is named
only in row 1268 (author, this worker's thread); no queued row owns it (grep of FINISH.md for "(U)" at this pin).

**Item: (U) of row 1268 (7.7).** In the account the test-cube size is R_k = least power of L at least
(log g_k^(-2))^r (CA-I L45885-45912, from Balaban CMP 119 (2.5)); EM's age gate reads R at min_{i <= j} theta_i
(EM L364-370). The frozen-scaffold frame phi and the run's own frame psi have thresholds that differ by a relative
amount theta^(-1/2) polylog, so their R can differ near the jumps of R. Theorem FCT' of row 1268 assumes both frames
use one family of test cubes at every step.

Moves: the one-cutoff carry on the pin route (row 1233 Proposition 3.7; rows 1256, 1260, 1267, 1268). Success: (U)
leaves the carry's input list, so (FC-1) along the pin runs rests only on the supplier's expansion (E0)-(E6), (TH),
(H2)-(H3). Failure: a use of R in the account's step that is two-sided at the precision theta^(-1/2), so that the
frames cannot share test cubes; then the comparison needs a cube-change estimate, which reads CMP 116.

**Plan.** Step 2: read the account's conditions on R (Definition 4.14:def-block-size-conditions, CA-I L45636-45915)
and the places where the one-step theorem and EM read R. Step 3: state a common test-cube sequence and prove that it
meets every condition in both frames. Step 4: what changes in Theorem FCT' and the carry. Step 5: labels, RESULT.
