lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-21T03:47Z

# gap-mini-solve-av-opus: mass gap for four-dimensional SU(2) Yang-Mills

Queue row 1296 of `FINISH.md`, pinned at commit 88cfc357c on branch `claude/ym4d-hard-route`.
Started 2026-11-20T15:47Z (date -u).

Labels: PROVED (written argument checkable by hand), ARGUED (argument with a named gap), GUIDE (heuristic or numeric, never a proof step), OPEN.

## Step 0: record read (2026-11-20T16:05Z by date -u)

Read: `GOAL.md` in full; `FINISH.md` L1-84, L299-349 and row 1296 (this item); the RESULT lines of rows 1244-1293
(the Opus mini-solve series aa-as); rows 1284-1295 (in-flight items); `parts/gap.md` L1-104 and L223-330 (state,
route registry, test table, exact price); `library/prior/gap-onebound-read-sol.md` L1-260 (row 1218);
`library/gap-mini-solve-aq-opus.md` Steps 0-1 (row 1284, in flight).

What the record fixes (statements about the record, not evidence; each is cited there):

1. Modulo the ultraviolet carry, the gap reads one lattice input, (N-phys) of row 1161: at one physical side L,
   uniformly in the cutoff, the periodic centre-neutral excited trace of the spatial cube at one time
   u <= n/K (K = 512) is at most 1/2. Equivalent forms on file: (W), (PHYS-SEED), (SEED) at one coupling of the
   window 2.3-2.6 with a carry, (SL) of row 1258.
2. Row 1218's published sources (credited to their authors there): A (Bhattacharjee, Bhattacharya, Lockwood,
   Romanov, Sessford, Singha Roy) proves the ascent from a thermal window bound (A-B*) to a gap, conditional on
   that seed and on (W); B (Bhattacharjee, Bhattacharya, Lockwood, Romanov) Corollary 166 proves BP(n, 1/2) for the
   straight-path block law at b = 2^k, beta_W <= k+2, torus side R <= exp(2^k/(17k)); B's own Remark 155 and row
   1219 call it non-selective. Zeng's routes are conditional.
3. Route registry (row 998): no route near closure; RA, RB, RC, RF blocked-equivalent; RE blocked-local; RG retired;
   RD (dichotomy) survives only as a weaker statement. Theorem-grade tests for any tool: compact U(1), the free
   photon, the product with a massless factor, Theorem D2 (supremum over tilts false), Lemma SHEET (uniform over
   coupling fields false), Proposition CA-FAIL (pinned-slice classes contain ordered members).
4. In-flight at this pin: aq (row 1284: (U-dom), H2' connectedness), as (row 1293, done: (PE)), at (row 1294, just
   started), au (row 1295, queued), owner tiling rows 1285-1287, Codex rows 1288, 1290.

## Step 1: how best to attack it (written 2026-11-20T16:35Z by date -u; judgement, ARGUED)

**The crux.** Modulo the ultraviolet carry, the Jaffe-Witten gap reads one lattice input, (N-phys), equivalently a
seed at one coupling in the window (a uniform cube gap plus the count (TR) of row 1259). Every proof of it must
contain a selective step at order-one coupling: a step that fails for compact U(1), the free photon, products with a
massless factor and frozen finite groups (parts/gap.md test table), and that is not a supremum over pins, tilts or
coupling fields (Theorem D2, Lemma SHEET, Proposition CA-FAIL).

**Screen (rule 0a).** Before reading the tables I re-derived the routes below; each has a match on file with its
first failing step, so none is attacked here.

| Route I re-derived | Match on file | First failing step there |
|---|---|---|
| Sharpness of the transition (OSSS, Aizenman-Barsky-Fernandez) | rows on FKG-NO, HF (row 1084) | no monotone (FKG) structure for SU(2) Wilson |
| Bourgain-Gamburd / Lubotzky-Phillips-Sarnak spectral gap of Hecke operators on SU(2) | `gap-brainstorm-max.md` item 12, `gap-brainstorm2-max.md` item 13; commutator line rows 778-795 | the commutator contraction and density flattening hold for the binary icosahedral group too (row 789 binding test); transport test (TR-F) open |
| Orbit-space curvature (Singer, Feynman), Bakry-Emery, Witten Laplacian | rows 1229, 1237 (Proposition UNI), 1251 (Zeng) | a coupling-uniform curvature makes the limit trivial; (TUN) is the gap |
| Small-volume valley confinement (Simon's x^2 y^2, Luscher's zero modes) and tilings | rows 1273, 1279, 1285-1287 | tiling carries free energies, not gaps; L m = kappa g^(2/3) is small at weak coupling |
| Migdal-Kadanoff decimation inequalities (Tomboulis 2007) | rows 799, 800, 1025, 1029 | one open inequality (TB)_n; gives the flux half only (Lemma FAC), off the path of (W) |
| Semiclassical confinement on R^3 x S^1 (Unsal and others), Polyakov mechanism, Gopfert-Mack | rows 1237, `gap-afield-*`, `gap-global-reform-max.md` | different theory; adiabatic continuity not a theorem |
| Spin-network / electric basis with 6j recoupling | rows 1076, 1081, `gap-descent-sign*.md` | recalled coefficient formula, GUIDE only; no sign at order one |
| Third law (no residual entropy) from a uniform gap, i.e. "uniform gap implies (TR)" | row 1259 Step 2 point 4, row 1291 | OPEN with no counterexample; needs a light-state count that no blind tool gives |
| 2D O(N) pinned-cell engine ported to 4D | rows 1007-1016, 1228, 1229 | fails in the class of all pins (B, B'), and at a trivially pinned plate (P5) |

Verdict (ARGUED): no route to the seed off the record, in agreement with rows 998, 1219, 1278, 1284. A further
screen is waste by row 998 9.5.

**What I work instead.** The rule "only closures count" points to an unowned open input whose closure is decidable
with sources on hand. Check 1288 (gpt-6.2-astra, `gap-uv-batch7-check-astra.md` Section 7) lists what the one-cutoff
carry still needs: (1) the seed and count; (2) the Section 9.1 inputs, including the blind-site expansion (needs
Balaban CMP 116, paywalled: stop by FINISH Rules); (3) a consistent physical normalization and its two-torus price
(reading N2 of row 1275 FAILS there); (4) the across-frame comparison (rows 1278, 1280, 1284 hold its parts); (5)
scope. Item 3 needs no CMP 116 and, by grep of FINISH.md and `library/open-core.md` for "physical normalization",
"N2", "V9" and "normalisation identity", is held by no row at this pin (hits: rows 1275, 1288 and row 1291's RESULT,
which names it as missing and does not take it).

Moves: the one-cutoff carry's item 3 (check 1288 7.3). Success: (V9) holds on its strong reading, so the physical
two-torus price is bounded by summable edge terms, and the carry's list loses item 3. Failure: the exact place where
the account's Section 9.1 representatives cannot be the physical bare constants, which then is a correction to the
carry route. It does not touch the seed; nobody should count it as progress on the crux.

**Plan.** Step 2: read the account's normalization passages that check 1288 cites (CA-II L140873-140926,
CA-III L11832-12058, L17396-17447, L18136-18302) and rows 1255, 1275 (Proposition V9). Step 3: prove the identity
that attaches Section 9.1's arrays to the physical bare densities, or find where it fails. Step 4: labels, RESULT.
If row 1294 or 1295 claims the same item first, I switch to the check of A's thermal ascent (Theorem F).
