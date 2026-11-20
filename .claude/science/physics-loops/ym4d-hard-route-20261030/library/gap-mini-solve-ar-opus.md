lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-21T02:55Z

# gap-mini-solve-ar-opus: an attack on the SU(2) four-dimensional mass gap

Queue row 1291 of `FINISH.md`. Worker: Claude Opus 5.5, max effort, Mac mini worker 3.
Pinned commit: 404e2e322. Started 2026-11-20T14:55Z.

Labels: PROVED (a complete written argument here or in a cited, checked library file),
ARGUED (an argument with a named gap), GUIDE (heuristic or numeric orientation only),
OPEN (not established).

## 0. Status of this file

Step 1 done (briefing read and digested, Section 1). Next: Section 2, the choice of attack.

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
