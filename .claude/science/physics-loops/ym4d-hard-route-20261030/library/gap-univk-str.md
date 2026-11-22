lead: anthropic/claude-fable-5-2/medium mac-mini-worker
lease_until: 2026-11-23T02:56Z

# gap-univk-str: the structural input (STR) of the logarithmic two-cutoff comparison (row 1398)

Provenance: Claude Fable 5.2, medium effort, Mac mini worker 2, at commit 778392267. Started 2026-11-22T14:56Z (date -u). Working state, not an audit; nothing here is a public claim.

Credit: the objects under study (the resolved interpolation, the assembly formula P_h, the stored units, the summed first variation, the ramp move) are from the complete account of Ethan Sussman and Levent Alpoge (with Claude and Codex as authors of their text), part III, and YM4_1400.tex. The reduction (LOG) to (STR)+(RAR) is row 1395; the corrected form of (STR) is check 1397 (gpt-6.2-astra).

## 0. Plan (written before reading)

Target: decide (STR) in the corrected form of check 1397, section 'An admissible repair of STR': along the ordinary common interpolation with A ramps, for every lambda and each recent direction z = (b, t), the restricted aligned sum with the fixed good-label projection, on its actual transverse fibre, is either positive with convex logarithm on (-R_z, R_z) or zero-free on the disc of radius R_z, R_z >= E_1/l_b; same for the ramp and stop-production move.

Steps, one per response, each appended here:

1. Read row 1395 sections 2, 4, 6, 8 and check 1397 in full; record the exact statement of (STR) and what the consumer needs.
2. Repo search: grep open-core.md and FINISH rows for (STR), aligned sum, good-label projection, diagonal fibre, zero-free; cite matches.
3. Read the account: CA-III 11962-11974 (P_h, stored units), 12104-12124 (diagonal fibres), 13621-13686 (conditional holomorphy), 13931 and 17436 ((c2)*), 17449-17459, 17561-17575 (summed first variation), 17679-17714 (ramp move); YM4_1400 L130223-130350.
4. Decide: prove one alternative for the summed retained function, or build a recent unit inside the account's stated bounds for which both fail with positive density.
5. Next two rows with decisive outcomes; RESULT line.

## 1. Repo search and the statement to decide (written after reading row 1395 and check 1397 in full)

Repo search (this lane folder; `origin/main` and the PR branches are not refs in this checkout; check 1397 L5-L7 ran the five-ref search for `restricted aligned sum|gap-univk-str` on 2026-11-22 and found no hit).
- `library/open-core.md`: zero hits for (STR), restricted aligned, good-label, diagonal fibre, zero-free, log-convex.
- FINISH rows with (STR): 1395, 1397, 1398 only.
- On file and used, not redone: row 1395 Theorem A/B (convex or zero-free chain), Lemma EXP, examples (E1), (E2); check 1397's diagonal-fibre repair of (STR) with the differential inequality |d'| <= s d, its example F(s) = 1 + 4s(1-s)/R^2 (LOG exact, STR false), and its source verdict that III 13621-13686 "supplies conditional holomorphy, exact ends and reading-level incidence, not positivity or a zero-free restricted sum" and that outline OH1 (23388-23404) "explicitly assumes nonnegative zero-source label measures".

**(STR*), the statement to decide (check 1397 L48, L110).** Let G be the fixed good set of labels (aligned, no live component of age a_0 or more), and for a point of the dial domain D* (III 12104-12124) let F := sum over h in G of tau_h[x](V_w), zero source, real centres, ramps of A. For every lambda in [0, 1] and every recent direction z = (b, t) (b >= k - a_0), the function eps -> F(lambda; eps e_z) on the fibre through the diagonal point lambda is (cvx*) positive with convex logarithm on the real interval (-R_z, R_z), or (zf*) free of zeros on |eps| < R_z, with R_z >= E_1/l_b. The same for the parameter s of the ramp and stop-production move (III 17679-17714).
The consumer (Theorem E as corrected by check 1397) needs it for every lambda, at every matched real centre in the window, on T_ell and T_(L ell).

## 2. What the account says about how the array enters a label term (READ; "III n" = line n of LOCAL:ym4d-papers/sa-ca)

READ in this step: III 11804-12170, 13621-13790, 13915-13945, 17405-17600, 17640-17730.

2.1 **The label term.** tau^c_h is "the h-th term chi T^w e^(A^w - E^c) of that expansion, read as a complex Borel measure", chi "the product of the characteristic functions of the label", T^w "the large-field operation at the stop", A^w "the effective action at the stop" (III 11855-11862). "tau_h[x; t^A]" is "the V_w-marginal of an integrand that P_h assembles from the array", and "That integrand is entire in the entries of the array" (III 17436-17441). Norms are total variations on the chart space (Omega_h, mu_h) "of the label's common inner variables" (III 11884-11886).

2.2 **No positivity statement.** A grep of III 11000-19000 for nonnegative / non-negative / positive measure / signed / real-valued finds no statement that tau_h[x^(lambda, eps)] is a nonnegative measure at real arrays; the only reality statement on the dial domain is "the data s^0 and D^0 are real" (III 17490). The proof of the modulus bound says "Neither a Schwarz-type step nor any cancellation between different labels is used" (III 17517). This agrees with check 1397 L99-L100 (the outline's OH1 assumes nonnegative zero-source label measures as a hypothesis).

2.3 **The array is not of exponent type only.** The proof of the resolved interpolation lemma (III 13709-13775) lists how slots move on the dial domain:
 (x) slots of direct uses and of stored terms: "A slot u of a resolved stored term B carries the value (1-lambda) x_u^A + lambda x_u^B + eps G_u^(n)" (III 13715-13719), read through an "activity per cell" and a "value per cell" (III 13727-13740). These are the units of the effective action and the stored boundary terms.
 (o) "At the T-site, operator slots again carry a convex combination of the two runs' values. It lies in the tolerance ball of the tolerance lemma of the T-site. The class-n pieces, at |eps| <= Lambda_z, move this combination by at most |eps| d^op_n" with |eps| d^op_n <= (1/4) m_G^T (III 13742-13762). The operator direction W^(z),op "consists of the class-n pieces of Lemma zone-split: the operator pieces, the potential pieces and the normaliser pieces" (III 13928).
 (a) "Among the class pieces at the T-site, those that enter as potentials have activity |eps| d^op_n eps-bar^pr [...] The remaining class pieces enter additively and need no such factor" (III 13767-13775).
So a class z = (n, k') carries, besides exponent units, operator, potential and normaliser pieces of the T-sites and pieces that enter additively. Lemma EXP of row 1395 covers (x) only, and only if the remaining factor is a nonnegative density.

2.4 **Incidence (ported, III 17522-17548 and 13664-13686).** eps_z enters tau_h only if zone j is present in h at level k', inside a component live at k' (untouched, second-class with omega_Y kept in the label, or arrested); for j <= k-2 this forces a live component of age >= k-j-1 at the stop. So for the good set G (no live component of age >= a_0) only classes with j >= k - a_0 occur, and a class with j >= k-1 can be read by every label with a large-field region.

2.5 **The ramp and stop-production move (III 17679-17714).** (m3) "replaces the ramps by t^A + s(t^B - t^A), and at the same time it interpolates the small slots of the production block P at the stop level"; the slots "read V_k only [...] and there are at most N_w^4 of them", each with |eta^A + s(eta^B - eta^A)| <= (1 + 20 C_chi theta_chi^k |s|) 1{f^B < (1+varpi_0)c}; the disc is |s| <= (20 C_chi N_w^4 theta_chi^k)^(-1). The slots are multiplicative factors of the integrand (the integrand of a label is "a product prod_iota v_iota over its components", III 17726), affine in s. They are not exponents.

