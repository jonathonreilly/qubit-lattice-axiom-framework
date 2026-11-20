lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-21T03:02Z

# gap-mini-solve-as-opus: the four-dimensional SU(2) mass gap (FINISH row 1293)

Started 2026-11-20T15:02Z (date -u) on the Mac mini Claude worker 2, branch claude/ym4d-hard-route pinned at 05378c8d5.
Research-stage working state. Labels: PROVED, ARGUED, GUIDE, OPEN, as the row asks.

## Status

Steps 0-1 done; Step 2 (reading the step) done, written 2026-11-20T15:18Z (date -u); Step 1 written 2026-11-20T15:10Z (date -u). Next: Step 3, Theorem PE and its proof.

## Repo search (rule "Repo first")

This checkout has no `origin/main` ref and holds `docs/` only in the index, so main and the open PR branches
(#10114, #10133, #10134, #10141, #10144) were not searched from here; only this folder was. Rule 0a grep of
`FINISH.md`, `library/open-core.md`, `library/l17c.md` for "parity envelope", "(PE)", "half-loop": the only match is
row 1280 (`library/gap-mini-solve-ap-opus.md`, this worker's thread, Proposition PE ARGUED). No queued row owns it.

## Step 0. Record read (statements about the record, not evidence)

Read at the pin: `GOAL.md` in full; `FINISH.md` L1-85 and L299-356, row 1293; the RESULT segments of rows 1240-1296;
`parts/gap.md` L1-104; `library/prior/gap-onebound-read-sol.md` in full (row 1218); row 1280
(`library/gap-mini-solve-ap-opus.md`) L42-469; row 1291's file (its Step 1 digest only, no choice yet). Summary:

1. The infrared seed ((N-phys) of row 1161, equivalently (SL)/(RR) of row 1258 at one weak coupling, or the stronger
   full-thermal window (A-B*) of Bhattacharjee et al.) is OPEN. About sixty idea families are screened on file (rows
   1189, 1194, 1199 tables; rows 1228-1287). Row 1218's reading: none of the three published sources supplies it.
2. The one-cutoff carry on the pin route (rows 1233, 1255, 1256, 1260, 1264, 1267, 1268, 1275, 1278, 1280) is a
   chain of implications. Its open inputs after row 1280 and checks 1263, 1266, 1276, 1288: the supplier readings
   (E0)-(E6), (E+), (TH) against Balaban's CMP 116 (not on this machine); either (U-dom) or the inputs (P1)-(P4) of
   row 1280's parity envelope (PE); row 1267's (H2)-(H3) (row 1278: H3' given readings, H2' ARGUED); the account's
   outstanding `9.1:prop-blind-site-expansions`; (V9) (check 1288: row 1275's reading N2 FAILS); (DET)'s inputs.

## Step 1. How best to attack it (judgement, ARGUED; written 2026-11-20T15:10Z by date -u)

**The seed.** I do not attack it. Every route I can name (vortex free energies, Migdal-Kadanoff bounds, abelian
projection, Gribov region, Bakry-Emery, chessboard and infrared bounds, Lee-Yang in beta, twisted boxes, layer
reductions, large N) has a match in the tables cited in Step 0, item 1, and `parts/gap.md` (row 998 9.5) names a
further blind screen as waste. The seed is a statement at order-one coupling with a number in it, and no hand method on
file or in the literature read here reaches it.

**The item: the parity envelope (PE) of row 1280, from ARGUED to PROVED given precisely stated inputs.** Claim of
(PE): the unmarked coefficient of one Balaban step obeys |f_(k+1)| <= C theta_k^(-1) (log theta_k)^q + tails, not only
EM's C theta_k^(-1/2) (log theta_k)^(p_0): one step has no half-loop term. Row 1280 4.5 shows what it buys: the drift
of the account's runs from the scaffold becomes polylog, (U) closes without (U-dom), and Route Z's flow law (B3+) of
row 680 gets its mechanism.

Moves: the one-cutoff carry on the pin route (row 1280 5.2: (U) needs (U-dom) and (E+), or (PE)); Route Z's (B3+)
(row 680 Section 5). Success: (PE) becomes PROVED GIVEN inputs that are read in the account's text, so (U) leaves the
carry without (U-dom). Failure: an odd-in-g term in the step that survives the parity, which would be a named obstruction
for (PE), (B3+) and Route Z.

**New idea for the proof (to be written in Step 3).** Row 1280 used a parity rule degree by degree ((P2)), which needs
Taylor remainders. A cleaner device: every factor of the step that is a function of the configuration depends on the
coupling g and the normalized fluctuation b only through exp(i g b) (and on g^2 through the action's prefactor), so it
is invariant under the joint flip (g, b) -> (-g, -b). Replace g by a complex parameter h in the fluctuation, keep the
cut frozen at the actual g, and use the symmetry of the Gaussian reference: the localized coefficient is then an
analytic function of h that is even up to the cut's asymmetry, and a Cauchy estimate for even functions gives
f(g) - f(0) = O((g/r)^2) on a disc of radius r of order 1/(log theta)^(p_0). The cut's asymmetry is a thin shell at the
threshold (path products and their inverses differ only at third order), so it costs tails by row 1280's Lemma SW.

**Plan.** Step 2: read YM4_EM's one-step kernel and coefficient theorem (definitions of f, of the unmarked output, of
the cut, and what EM assumes of the localization and of complex data). Step 3: state and prove Theorem PE in the form
those definitions allow (Lemmas: flip invariance, even Cauchy estimate, near-evenness from Lemma SW, assembly). Step 4:
check the flip invariance against each factor of the step (action, Haar and chart densities, soft axial weight, cut,
inherited list) in Balaban's CMP 119 as read in rows 1268 and 1280. Step 5: consequences, labels, RESULT.

## Step 2. What the step is, in the account and in Balaban (READ; written 2026-11-20T15:18Z by date -u)

Sources: Sussman and Alpoge, `YM4/EM/YM4_EM.tex` at c7fef8b21b58 (2001 lines; credit Ethan Sussman and Levent Alpoge,
with Claude and Codex as authors of their text), fetched by URL into a scratch folder outside the repository, cited
EM:n; Balaban, CMP 119 (1988) 243-285, the owner's copy, pp. 247, 267, 268 read as page images.

**2.1 The step (EM:544-578).** At real admitted data the step is the actual finite integral
    E_(k+1)[x_k, f](W) = log int K_(k,theta_k)(W, dV) exp(-x_k A(U_k(V)) + S_f(U_k(V))) + x_k A(U_(k+1)(W)) - S_f(U_(k+1)(W)),
where K is "the fixed all-small-field kernel on M(V) = W. It uses the given fibre density, gauge weight and
fluctuation cut. In the resolved fibre chart its real free array is B and its field is V'(W, B)". The frame theta_k fixes
"the lattice partitions, Gaussian references, real fluctuation coordinates and tests"; the Wilson weight x_k does not
(EM:502-506), tau_k = x_k/theta_k. The background identities V'(W, 0) = M^k U_(k+1)(W), U_k(V'(W, 0)) = U_(k+1)(W) are
required of the supplied backgrounds (EM:550-555). The inherited list S_f is a sum of fixed functions of the
configuration (EM:538-543).

**2.2 The cut and the Gaussian (EM:580-606, EM:619-624).** "In the analytic integral presentation the sharp test is a
fixed Borel restriction in the real free variables." The Gaussian reference is exp(-<B, Delta B>/2), Delta = Delta_A +
Delta_G (action and gauge precisions), with the weight shift (tau_k - 1)<B, Delta_A B>/2 as in (em:eq-frozen-gaussian-rewrite).

**2.3 The localization (EM:629-647).** "One prescribed convergent localization gives the pointed output E_(k+1) after
the specified scalar has been separated". It is required to be covariant under the orthogonal maps O_(r,W) of the real
free coordinates that admitted isometries r induce: "This change transports the cut, completed response, measure factors
and point z to rz". Nothing is said about the map B -> -B.

**2.4 The output and the coefficient (EM:678-706, EM:840-843, EM:1173-1205, EM:1338-1384).** E_(k+1) = N_(k+1) +
G_(k+1,tau_k) + F_(k+1); the unmarked residual obeys ||E^u_(k+1) - N_(k+1) - G_(k+1,tau_k)|| <= C delta(theta_k) on the
absolute core (Proposition em:prop-prefix-formation), delta(y) = A_1 y^(-1/2) (log y)^(p_0) (EM:345), 2 p_0 > 1
(EM:874-875). Sum_X N_(k+1) = log Z_k(W) - log Z_k(1), Z_k the "constrained reference Gaussian normalizer without a
fluctuation cut"; the total of G is background-free. The coefficient map b_j (Proposition em:prop-companion-coefficient)
is the second moment of the companion kernel, the limit of the torus Hessians at the trivial datum P_o; it is linear,
real on real data, |b_j(E)| <= C a^(-2) cal(A) for a family of norm cal(A) on a core of physical radius a, and it does not
depend on the coherent localization of a physical total. Theorem em:thm-coefficient-envelope: b_(k+1) = b^0 + f_(k+1) +
q_(k+1) with f_(k+1) = b_(k+1)(F^u_(k+1)); its bound |f| <= C theta_k^(-1/2) (log theta_k)^(p_0) is exactly the norm bound
on F^u times the fixed extraction cost of the absolute core (EM:1379-1384). So EM's envelope is a size bound; nothing in
EM uses the structure of F^u.

**2.5 Balaban's all-small-field step (CMP 119 pp. 267-268, (3.15)-(3.16)).** After the scaling A'_k = g_k A_k the step
is an integral over the free variables A_k of
    exp[-(1/2) <A_k, C* Delta^(k) C A_k> + P^(k)(g_k, U_(k+1), A_k)]
times characteristic functions; the configuration inside P^(k) is U_k(exp i[g_k C A_k - h D~(g_k C A_k)] V^(k)), so it
depends on g_k and A_k only through g_k A_k, and the inherited terms enter as (E_k + R_k + B_k)(that configuration) minus
their value at U_(k+1). The scalars in front (log g_k d(g)|B(Gamma)*|, log sigma_0 |B(Gamma)*|, -log z (L^4 - 1)|Gamma|)
depend on counts only, not on the field. The small-field cut is introduced on the normalized fluctuation itself, (3.16):
chi(sup over b in (box'~2)^(k)* of |A_k(b)| < delta_k) on each cube, and the earlier small-field characteristic function
"is equal to 1, because of the bound on A_k introduced by the second" (p. 268). So the all-small-field cut is a product
of tests |A_k(b)| < delta_k on the free variables: it is even under A_k -> -A_k. The soft axial gauge (1.5) (p. 247) is
an inserted average over gauge transformations with weight exp(-g_0^(-2) [1 - Re tr U^u(y, x)]) and a truncation of the
contour variables U(y, x); it is a function of the configuration, and its truncation sits among the earlier
characteristic functions. Balaban also states that a delta-function axial gauge averaged over lattice symmetries is an
equivalent alternative (p. 247).

**2.6 What this gives (READ).** In the step every factor except the Gaussian reference and the cut is a function of the
configuration, and the configuration is a function of the background and of (scale) x (free variable); the
Gaussian reference is a fixed quadratic form, and the cut is a fixed set that is even in the free variable (Balaban
(3.16); EM's "fixed Borel restriction"). Neither EM nor CMP 119 uses this for the coefficient; EM bounds f by the norm of
F^u. Step 3 uses it.

