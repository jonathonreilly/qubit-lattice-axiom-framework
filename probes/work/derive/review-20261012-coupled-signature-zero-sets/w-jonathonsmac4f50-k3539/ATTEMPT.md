# ATTEMPT: the 72 coupled-signature quadratic zero sets

Task `J:derive:review-20261012-coupled-signature-zero-sets:a1`. Worker: Claude Sonnet 5.5, one seat, no subagents, same-family and unrefereed. Nothing here is audited, retained or cross-model confirmed.

## Plain-language summary

The earlier test asked a narrow question: is each squared coordinate of the "unequal" block a *linear* combination of the pair-moment equations? For 72 of 240 ordered pairs the answer was no, and the note correctly said that this does not mean a nonzero solution exists. I treated the same equations as polynomial equations and solved them exactly. In every one of the 72 cases the only solution is the origin, over the rationals, reals and complex numbers, for all six coordinates (unequal block and partner). The proof is, per case, a short identity: every cube `x_i^3` equals a sum of (linear form) times (pair-moment quadric). All 432 identities are checked by exact rational arithmetic. So the unequal block is zero in all 240 ordered cases of the two-signature ansatz. No nonzero solution exists, so no positivity or normalization question arises for these pairs.

## Sources read (stated as required)

- Axioms: `docs/MINIMAL_AXIOMS_2026-06-29.md` read in full on current main (a77a3449c9...), lines 1-233. Used: Lattice (cubic adjacency, proper cubic rotations), Admissibility (one fixed nearest-neighbour rule, covariant), Record. They do not fix a Hamiltonian, weights or a formation rule (lines 104-118).
- Primitive registry: `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` read in full (lines 1-130). Approved primitives: `scale_reference_primitive`, `kinetic_isotropy_primitive`, `realized_state_primitive`. None is used; this is pure finite algebra on a supplied model.
- Source objects at frozen commit 516cb69d84... all four sha256 verified (see `RECOVERY_STATUS.json`); the same hashes hold on current main a77a3449c9. Also read: the parent `docs/ORDER_BLIND_NEAREST_NEIGHBOUR_..._2026-09-22.md` (Theorem 2 at lines 168-191, Theorem 4 at 212-256), `docs/SINGLE_HEIGHT_SIGNATURE_ORDER_BLIND_KERNEL_..._2026-10-10.md`, the equal-height note, and the claim scopes of the cap-pair siblings.
- Prior art: no earlier attempt on this problem under `probes/work/derive/` of the ai/probes view; no open PR title (229 searched) mentions signatures, order-blind kernels or zero sets.

## Setting and premises

1. ASSUMED (lane-supplied model, not axiom content). Formation reading of Admissibility; strictly positive translation-covariant order-blind rule on a finite alphabet; soldered reading; alphabet = proper orbit of (1,2,3) (24 points); `phi_d(a,b) = 1 + L_d(a,b)`; `L` soldered, bond-symmetric, slice-sum zero; `L` supported on the bonds of two height signatures; uniform average. The 2026-09-22 parent supplies the product form and the moment identity (parent lines 168-186) and the soldered reading (lines 212-218); I cite them, I do not re-prove them.
2. PROVED (short). `r0` is uniform: it is G-invariant and G acts transitively (freely) on the 24 points (second PASS line of check.py).
3. PROVED from 1. Pair moments are necessary. For d != e and neighbour values b, c the moment identity reads `E_a[(1+L_d(a,b))(1+L_e(a,c))] = 1`; the linear parts average to 0 by the slice condition, so `sum_a L_d(a,b) L_e(a,c) = 0` (all 15 direction pairs, all 24x24 values). Triple and higher moments are further necessary conditions and are not used, so a zero set of the pair moments alone bounds the full set from above.
4. Coefficient domain: kernel coordinates `x` in Q^6 with a rational kernel basis per signature; the quadrics have rational coefficients; all certificates are rational identities and hold over every field of characteristic 0 (Q, R, C). Variables x0-x2 are the first (extra) signature S, x3-x5 the partner T.

## Steps

5. CHECKED. Independent reconstruction (no shared code): 24 rotations, 24-point orbit, 144 ordered / 84 reversal-classes of bond orbits, 21 signatures (6 opposite, 3 equal, 12 unequal), four bond classes each, slice rank 1, kernel dimension 3 each. Sampled kernel elements are covariant, bond-symmetric and slice-zero.
6. CHECKED. Pair-moment quadrics assembled with the full symmetric off-diagonal coefficient (`l_i r_j + l_j r_i` for i != j). Assembly equals direct lattice sums at random rational points; a MUTANT that drops the second cross coefficient fails that check.
7. CHECKED. The linear monomial test, rebuilt: 168 certified, 72 left. The 72 equal the list printed by the source runner (`scripts/unequal_height_signature_with_one_partner_2026_10_10.py:266`, hard-coded in check.py as data). All 72 partners are themselves unequal-height signatures (the 60 other unequal+unequal pairs are linearly certified; equal and opposite partners never appear among the 72). The quadric span has dimension 20 (48 pairs) or 18 (24 pairs) of 21.
8. CHECKED, lead case `(-3,-2)` vs `(-3,-1)` (20 quadrics). check.py prints them: `x_i^2 - x5^2` for i = 0..4, `x0 x2`, `x1 x2`, `x0 x3`, `x0 x4`, `x1 x3`, `x1 x4`, `x2 x5`, `x3 x5`, `x4 x5`, `x0 x5 - x5^2`, `x1 x5 + x5^2`, `x0 x1 + x5^2`, `x2 x3 - x5^2`, `x2 x4 + x5^2`, `x3 x4 + x5^2`. This contains the four forms quoted in the task.
9. PROVED given 8 (hand argument, lead case). Over R: `x0 x2 = 0` gives x0 = 0 or x2 = 0, and `x0^2 = x5^2 = x2^2` then gives x0 = x2 = 0 = x5; the remaining squares equal x5^2 so every coordinate is 0. Over C and as an identity: `x5^3 = x2 (x2 x5) - x5 (x2^2 - x5^2)` (verified exactly in check.py). So the nonlinear consequences of (-3,-2) vs (-3,-1) already force zero, not only the unequal block but the partner too.
10. CHECKED (exact, 432 identities) then PROVED by consequence. For each of the 72 pairs and each k in 0..5 check.py solves a linear system over Q for cofactors `h_{kj}` (linear forms) with `x_k^3 = sum_j h_{kj} q_j`, and re-verifies the polynomial identity by independent term-by-term multiplication. Hence `x_k^3 = 0` at any common zero, so `x_k = 0`: the common zero set of the pair-moment quadrics over Q, R and C is the origin only, for every one of the 72 pairs. A tampered cofactor is rejected (mutant).
11. CHECKED (second exact route). sympy Groebner: `1 in (q_j, 1 - t x_k)` for all 72 x 6 cases, i.e. each `x_k` lies in the radical over Q, hence vanishes on the complex variety.
12. CHECKED (floating point, not a proof). Multistart minimisation of the sum of squared moments on the unit sphere gives minima between 5.6e-2 and 2.5e-1 over the 72 pairs; nothing near zero.
13. PROVED by assembly of 7, 10 and the cited parts. In all 240 ordered cases (unequal signature S plus any other T) the unequal block vanishes: by step 7 for 168 (`x_i^2` in the span of quadrics, so `x_i = 0`), by step 10 for 72. A kernel with vanishing pair moments is then supported on T alone and falls under the single-signature classification (CITED, not re-proved: opposite T gives the cap-pair span, any other T gives zero; `docs/SINGLE_HEIGHT_SIGNATURE_ORDER_BLIND_KERNEL_BOUNDED_THEOREM_NOTE_2026-10-10.md:4` claim_scope). In the ansatz "one unequal signature plus at most one other signature" no pair-moment-null kernel therefore leaves the eighteen cap-pair kernels. Scope: two-signature support only.
14. READING. The 72 ordered pairs are 36 unordered pairs, closed under `d -> -d` (a symmetry of the problem: it maps the signature `(h1,h2)` to `(-h1,-h2)` up to reversal); 18 classes. I did not rely on the symmetry; every ordered pair is certified directly.

## Controls

15. CHECKED, equal-height control preserved. `(-3,-3)` beside `(3,-3)` is not forced by the linear square test (as the source states), but the nonlinear route does force its equal-height block to zero: first certificate at degree 4 (not 3). So failure of the linear test is, again, not a nonzero-solution witness. Incidental, one pair only: this block is nilpotent over Q, hence also origin-only over C for this pair; the equal-height note's remark that its argument is over Q/R and not C is a statement about the argument, not contradicted.
16. CHECKED, positive controls with teeth. Two opposite signatures `(-3,3)`, `(-2,2)`: the point `(1,-2,3,0,0,0)` kills every quadric and every raw lattice pair moment, and the degree-3 machinery correctly returns no certificate; a single opposite signature has no pair-moment quadric at all.

## What is new, and what is not

NEW (scoped): steps 9-11 and 13: origin-only certificates for all 72 ordered pairs left by the 2026-10-10 direct test, exact per-case degree-3 Nullstellensatz identities, a Groebner cross-check, and the consequence that the unequal block vanishes in all 240 ordered cases. The stronger fact that the partner block also vanishes in those 72 cases (it is unequal) is also new. The target sentence of the source note ("solve the real or rational zero sets of the 72 pairs") is answered.

NOT new: the group/orbit/signature enumeration, the 168/72 split, the lead-case row space quoted by the task, the equal-height control behaviour, the single-signature classification.

## Not shown (scope guard)

- Nothing about supports on three or more signatures (the equal-height triple with joint kernel dimension 10 stays open), the full affine bond space, other orbits, non-uniform `r0` or rules with zeros.
- No positivity or normalization analysis is needed or given for these 72 pairs because no nonzero pair-moment solution exists; `phi = 1` on all bonds of these supports.
- Only pair moments were used. Parent Theorem 2 and the converse are cited.
- No physical law selection, scale or formation rate is inferred. The result is a finite-model exclusion inside the stated ansatz.

## No-Go Discipline Gate (negative claim: "no nonzero pair-moment-null kernel on S+T")

Packet status: **incomplete; no PASS claimed.**

- N1 routes actually run: (a) linear span of quadrics (source, ATTEMPTED); (b) ideal membership / Nullstellensatz degree-3 identities, with Groebner radical membership and the hand argument for the lead case as variants of the same family (ATTEMPTED); (c) floating-point sphere minimisation (ATTEMPTED, not a proof). A real-radical sum-of-squares route and a resultant or eigenvalue (multiplication-matrix) route were not run; they are not needed for the proof but are needed to reach five independent families. The five-family quota is therefore not met and I do not manufacture families. This is a packet limitation, not doubt about the finite identities.
- N2: one ansatz; no wall count asserted.
- N3 hidden conditions, now explicit: soldered reading; uniform `r0`; formation (sequential) model; pair moments from parent Theorem 2 (cited); rational kernel basis; two-signature support.
- N4 residual matching: unequal note (residual = 72 unresolved, matches); single-height note (classifies the lone partner, used only for the partner step 13); equal-height note (control only). Parent Theorems 2 and 4 are cited for the model, not as negative witnesses.
- N5: tested per signature-pair block, exactly, with all 15 direction pairs and all 576 neighbour-value pairs; not tested per mode, per site ensemble or lattice-wide dynamics.
- N6: no new axiom or primitive; registry primitives are irrelevant here.
- N7 steelman: with a third signature the cancellation structure changes (the equal-height triple has joint kernel dimension 10), so an unequal block could survive in a support of three signatures, or when `r0` is not uniform or the rule has zeros. Concrete next artifact: run the same exact degree-3/Macaulay test on supports (unequal, X, Y) for the 1330 triples; the machinery in check.py generalises by changing the variable count.
- N8: the sibling notes (cap pairs, one-hot caps, opposite cap lines, three-cap lines) record successive escapes from smaller spans; this result does not extend to those escapes.

## First unresolved step

Inside the stated mathematical scope there is none. The first open step is step "N1 five-route packet" above (and independent confirmation of this same-family result), then supports on three signatures.

## Files

`check.py` (31 checks, about 38 s, 0.46 GB), `check_output.txt` (its output), `RECOVERY_STATUS.json`, `src/` (verbatim copies of the four source objects), `dev/` (exploration scripts, not part of the deliverable).
