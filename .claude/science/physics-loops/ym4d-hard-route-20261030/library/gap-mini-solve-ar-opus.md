lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-21T02:55Z

# gap-mini-solve-ar-opus: an attack on the SU(2) four-dimensional mass gap

Queue row 1291 of `FINISH.md`. Worker: Claude Opus 5.5, max effort, Mac mini worker 3.
Pinned commit: 404e2e322. Started 2026-11-20T14:55Z.

Labels: PROVED (a complete written argument here or in a cited, checked library file),
ARGUED (an argument with a named gap), GUIDE (heuristic or numeric orientation only),
OPEN (not established).

## 0. Status of this file

Step 2 done (Section 2: judgement and choice, written 2026-11-20 by date -u). Next: Section 3.

## 1. Briefing digest (what this row starts from)

Read at the pin: `GOAL.md`; `FINISH.md` rules, How we work, Working efficiently, row 1291;
`parts/gap.md` State of attack, route registry, test table, price (L1-104, L223-330);
`library/prior/gap-onebound-read-sol.md` in full (row 1218, gpt-6.1-sol reading);
the RESULT lines of rows 1217, 1228-1290 (mini-solve s to ap, laptop-solve 1-3, owner rows, astra solve 29-32,
fresh, fresh2). Nothing below is new; it fixes the starting point.

1. The crux, as the lane states it: (N-phys) of row 1161 (`gap-solve9-astra62.md` 146-148), restated in
   row 1218: there are L and j_0 such that for every j >= j_0 some integer u_j with 3 <= u_j <= n_j/K has
   s_{+,j}(u_j; n_j^3) = Tr_{H_+} U_j^{u_j} - 1 <= 1/2 (centre-neutral thermal sum of the periodic spatial
   cube of physical side L at physical time u_j a_j, uniform in the cutoff). Equivalent forms on file:
   (W) with (BDD-Delta) and (Z-UNB) (row 720, Theorem ZD-c); (SL)/(RR) of row 1258 at one coupling.
2. Bhattacharjee et al. (preprint 202611.1282, authors' archive copy) prove a conditional ascent from the
   full-thermal one-scale seed (A-B*) to a transfer gap; the seed at weak coupling is open in their text.
   Their B paper (Hexagon 2610.00341v7) proves BP(n,1/2) for very coarse straight-path block variables of
   Wilson SU(2) at growing beta_W <= k+2 on tori of size R <= exp(2^k/(17k)) (Corollary 166), by
   convolution damping of non-trivial representations; the ascent (H2)/(S) is open. Zeng's tunnelling package
   is conditional; row 1251 found its (TUN) to be the gap itself.
3. Route registry (row 998): RA, RB, RC, RF blocked-equivalent; RE blocked-local; RG retired; RD survives as
   a weaker statement. Methods 1-36 set aside (parts/gap.md L52-79). The theorem-grade tests for a carry
   tool are compact U(1), the free photon, a product with a massless factor, Theorem D2 (no supremum over
   tilts), Lemma SHEET (no uniformity over coupling fields), and (row 1140) no uniformity over backgrounds
   at large b.
4. The recent Opus rows (1228-1280) screened about sixty ideas for the seed and found none off the record;
   most then worked side items of the one-cutoff carry (rows 1233, 1248, 1255, 1256, 1260, 1264, 1267, 1268,
   1275, 1278, 1280). Row 1278: at the window coupling the glueball correlation length is about one lattice
   spacing, and every published rigorous method stops roughly ten times lower in beta; Proposition CA-FAIL
   rules out criteria uniform over boundary data.
5. Owner direction for this row: horsepower on the crux; a plain brief ("solve the problem").

## 2. How best to attack it (judgement; ARGUED unless cited)

**2.1 Where the problem stands.** By the record (Section 1, items 1-4), and modulo the open inputs of the
one-cutoff carry, the Jaffe-Witten gap for SU(2) needs one infrared input: a seed of Wilson SU(2) at one weak
coupling, that is, a uniform gap of the periodic cubes plus a count of light states (row 1259, Corollary CD1),
at a size of many correlation lengths. In the form (N-phys) with K = 512 this is a pressure bound deep in the
confined phase (row 1284 Step 0, item 2). It is the lattice mass-gap problem at one coupling. No hand method in
the lane or in the literature read here reaches it.

**2.2 What the 2D proofs show, and why the port stops (GUIDE, from rows 1009-1016, 1072-1074, 1140, 1243-1249).**
The posted 2D O(N) proofs (OpenAI; Ding, Huang and Yang; unrefereed) reach the one-coupling statement by a
bound that holds at every coupling, with a non-optimal exponential rate. They get it from a stiffness
iteration whose gain is a tadpole (the curvature of the target sphere), proved uniformly over pins and
strengths. In 4D gauge theory three facts on file block the port:
(a) the class "uniform over pins" does not close: two pinned slices make a 3D O(4) magnet (Proposition CA-FAIL,
rows 1072-1074), and coupling fields make critical members (Lemma SHEET, row 996);
(b) the gauge theory has no rigid non-abelian twist on its integration variables (CEN+, row 1016; Lemma DR,
row 1273);
(c) the 4D one-loop gain is a two-propagator bubble whose sign comes from the paramagnetic spin term; one-sided
tools (Jensen with a flow of bounded strength) keep only the screening part (row 1244 Proposition 2.3; row 1249).
In my own terms, (c) is this: in -log(Z(B)/Z(0)) the anti-screening part is minus half a variance of the
spin coupling, a second cumulant, and Jensen drops every cumulant beyond the first. A flow can restore it only
if the flow is long-range, which is an RG step through the band.

**2.3 Decision.** A further screen of mechanisms is named waste on file (row 998 9.5; rows 1228-1284 screened
about sixty families with none off the record). I checked eight more names against the record before deciding
(Yamazaki-Yonekura reduction and adiabatic continuity: Route T, rows 842, 862; spectral independence, entropy
factorisation and localisation schemes: `gap-mini-solve-o-fable.md` L55 with `prior/gap-lit-tiltcov.md` Step 3,
"each is an engine; its local input at block scale is a one-scale seed of kind (K-one)"; Bakry-Emery and Polchinski
flow: method 31; Gribov region: the screen table of `gap-mini-solve-am-opus.md` L32; the Kogut-Susskind ground-state
transform: row 1281, Lemma V; Nielsen-Olesen and gluon paramagnetism: row 1244; the count half (TR): row 1259). All are on
file. So I do not run another screen.

I also tested whether the count half is free given the gap (a counterexample or a proof would settle row 1259's
open sentence "the implication uniform gap implies a seed itself stays OPEN"). Result, ARGUED: neither direction
is reachable by soft tools. (i) A proof needs the low-lying states to be particle-like: RP, locality and a gap on
every box shape give nothing per unit volume, because a chessboard or doubling bound always reintroduces the
Casimir term t c(Y) of a smaller box (Section 3.0 below writes this out). (ii) A counterexample needs exponentially
many states at bounded energy above a unique gapped vacuum; the known sources of such counts (subsystem
symmetries, fracton and topological sectors) come with degenerate vacua, so they lose the uniform gap. I record
this and stop there.

**Item chosen for the rest of this row.** The infrared seed stays OPEN here. I spend the row on a closable input of
the critical path that no row owns and whose sources are reachable from this machine, and I name it in Section 3
after a rule-0a check against the parallel rows 1284 and 1293.
