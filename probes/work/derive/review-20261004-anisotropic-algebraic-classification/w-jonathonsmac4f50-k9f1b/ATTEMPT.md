# Anisotropic flux-free comparator: an exceptional-locus result on the second mirror line, and a complex census of the node scheme

Task `J:derive:review-20261004-anisotropic-algebraic-classification:a1`. Worker: Claude Sonnet 5.5, one pass, same family as the sources, **unrefereed**.
Files: this note, `check.py` (52 checks, about 2 to 3 minutes, one process), `RECOVERY_STATUS.json`.

## Plain-language summary

The supplied model is a four-site Bloch matrix M(f). The question is when its two middle bands touch at zero energy, i.e. when det M = 0.

1. **Result (proved, symbolic in all positive couplings).** There are two special lines in momentum space, f = (x, 1-x, 0) and f = (x, 1-x, 1/2), fixed by a mirror symmetry. The sources treat the first. On the second, det M is 16 times a product of two sums of three squares. A touching on that line therefore exists only if Jx = Jy and Jz = 8 kappa^2 Jx / (4 kappa^2 + Jx^2). This is the landed "handover" family, and it is now the complete answer on that line for every positive coupling. For Jx != Jy there is never a touching there, so the charge-two handover points do not survive as points on this line when Jx != Jy.
2. **Result (checked, five couplings).** Over the complex numbers, the set where M has rank at most 2 has length 34 at each of the five supplied couplings: 4 points on the first mirror line, 10 points on the plane f1 = f2 (a second integer quintic, none on the real torus), and 20 points that are the supplied quintic orbit. This gives an algebraic upper bound on the real-torus census that agrees with the sources' interval-certified count.
3. **Not shown.** That the off-plane degree is 5, or that the length is 34, for all couplings. The route stops at a symbolic elimination for the 20-point stratum (step 14).

## Setting, premises, and what was read

- **Read:** `docs/MINIMAL_AXIOMS_2026-06-29.md` in full (axioms at lines 35-77, "Axioms and approved primitives are the complete supplied foundation" at line 108) and `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` (the three approved primitives `scale_reference_primitive` line 31, `kinetic_isotropy_primitive` line 58, `realized_state_primitive` line 98, on main). None supplies a band-structure or Majorana comparator, or a coupling value. The comparator is therefore a supplied model, not an axiom consequence. Nothing here derives it from Lattice, Qubit, Admissibility or Record, and nothing here uses any of the three primitives.
- **ASSUMED (supplied):** the network, hopping-sign convention and `u = +1` sector, in the matrix M(z) built from the TERMS table of the pinned source runner (`scripts/composite_site_network_flux_free_off_plane_touchings_are_quintic_algebraic_points_at_five_anisotropic_couplings_2026_10_01.py`, `TERMS`); positive couplings Jx, Jy, Jz, kappa > 0; H = iM, z_j = exp(2 pi i f_j).
- **Landed background** (not new): det M >= 0, and a zero-energy touching of the middle bands is exactly a zero of det M (`docs/COMPOSITE_SITE_NETWORK_FLUX_FREE_THE_LINE_TOUCHINGS_AND_THEIR_CHARGES_ARE_EXACT_FOR_GENERAL_COUPLINGS_BOUNDED_THEOREM_NOTE_2026-10-01.md:4`); on the first line det M = 16 q(c)^2 (same note, line 4); the five integer quintics Q5 and the 4-point orbit (`docs/COMPOSITE_SITE_NETWORK_FLUX_FREE_OFF_PLANE_TOUCHINGS_ARE_QUINTIC_ALGEBRAIC_POINTS_AT_FIVE_ANISOTROPIC_COUPLINGS_BOUNDED_THEOREM_NOTE_2026-10-01.md:4`, completeness left open at line 131-132); the interval-cleared census at ten couplings (`docs/COMPOSITE_SITE_NETWORK_FLUX_FREE_CERTIFIED_TOUCHING_CENSUS_ACROSS_COUPLING_REGIMES_BOUNDED_THEOREM_NOTE_2026-10-01.md:94-97`, "a proof that the off-plane degree is 5 for all couplings" open); the Jx = Jy = 1 handover family (`docs/COMPOSITE_SITE_NETWORK_FLUX_FREE_HANDOVER_TOUCHINGS_ARE_EXACT_CHARGE_TWO_POINTS_FOR_EVERY_J_BETWEEN_0_AND_2_BOUNDED_THEOREM_NOTE_2026-09-28.md:4`, "no statement at ... anisotropies Jx != Jy").
- All four source notes and four source scripts were retrieved at the pinned commit `2868a0c453e667d1267f0e1e7403732a11893d78` and all eight sha256 values match (see `RECOVERY_STATUS.json`). Current `origin/main` adds only ledger JSON files for these notes; no new docs on this topic.
- **Prior art checked:** the earlier unlanded attempt `probes/work/derive/campaign6-20260928-comparator-anisotropic-touchings/w-jonathonsmac4f50-jf263/ATTEMPT.md` (Krawczyk nodes at two couplings, splitting of the charge-two points with `sqrt(1-Jy)` in floating point) does not treat the second mirror line or the complex scheme. Open PR search (`gh pr list`, titles with composite / flux / touching / anisotropic / handover): none. Related tasks in the same lane (`...-cubic-unfolding`, `...-anisotropic-event-coverage`) are different obligations; the event-coverage task may overlap with step 6 (the TRIM table), see below.

## Steps

Labels: PROVED (full argument, identities machine-verified symbolically in `check.py`), CHECKED (executed), ASSUMED, READING.

**Symmetries (all positive couplings).**

1. **PROVED/CHECKED (B1, exact Laurent identity).** Let P be the real orthogonal matrix with P[0,3] = -1, P[3,0] = 1, P[1,2] = 1, P[2,1] = -1 (P^2 = -1). Then P M(z1,z2,z3) P^-1 = M(1/z2, 1/z1, 1/z3), identically in z and in all four couplings. So the mirror f -> (-f2, -f1, -f3) is implemented by a constant unitary. The plain swap f1 <-> f2 does not appear to be (exploratory floating-point search for a constant intertwiner, with and without conjugation, found only the P above; not in `check.py`; check B4 only confirms that the mirror needs the z3 inversion), but det M is invariant under it (B2) and under f -> -f (B3), as the sources state. Background (A1, A2): M(z) + M(1/z)^T = 0 and the characteristic polynomial has no mu^3 or mu^1 term.
2. **PROVED/CHECKED (B5).** The fixed set of the mirror is the two lines L0 = {(x, 1-x, 0)} and L1 = {(x, 1-x, 1/2)}. On both, P commutes with M, so M splits into two 2x2 blocks (P = +i and P = -i eigenspaces).

**The second mirror line L1 (new).**

3. **PROVED/CHECKED (C1-C4, exact Laurent identity in w with z1 = w^2).** With C = cos(pi x), S = sin(pi x), s = 2CS:
   - SOS+ := (Jz - 2 kappa s)^2 + ((Jx+Jy) C - 4 kappa S)^2 + (Jx-Jy)^2 S^2,
   - SOS- := (Jz + 2 kappa s)^2 + ((Jx+Jy) C + 4 kappa S)^2 + (Jx-Jy)^2 S^2,
   - det M(x, 1-x, 1/2) = 16 SOS+ SOS-,

   and the two blocks have real determinants 4 SOS- (P = +i) and 4 SOS+ (P = -i). Expanded: SOS+- = A -+ 4 kappa (Jx+Jy+Jz) sin(2 pi x), A = Jx^2+Jy^2+Jz^2 + 2 Jx Jy cos(2 pi x) + 4 kappa^2 (1-cos)(3+cos). This also gives det M >= 0 on L1 without appeal to the general positivity.
4. **PROVED (C5, C6 verify the algebra; the logic is below).** For positive Jx, Jy, Jz, kappa, det M vanishes at a point of L1 iff Jx = Jy, Jz (4 kappa^2 + Jx^2) = 8 kappa^2 Jx, and tan(pi x) = Jx/(2 kappa) (point x) or x -> 1-x (SOS- = 0).
   Argument for SOS+ = 0. All three squares vanish. Jz = 2 kappa s with Jz > 0 gives s != 0, hence S != 0. Then (Jx-Jy) S = 0 gives Jx = Jy. Then (Jx+Jy) C = 4 kappa S gives tan(pi x) = Jx/(2 kappa) > 0. Then s = 2 tan/(1+tan^2) = 4 kappa Jx/(4 kappa^2+Jx^2), so Jz = 2 kappa s = 8 kappa^2 Jx/(4 kappa^2 + Jx^2), and cos(2 pi x) = (4 kappa^2 - Jx^2)/(4 kappa^2 + Jx^2). Conversely at these values all three squares vanish identically (C6). SOS- = 0 is the mirror x -> 1-x.
   **Consequence: for Jx != Jy there is no touching on L1 for any positive Jz, kappa**, and the line's det M is bounded below by 16 (Jx-Jy)^2 S^2 SOS- near S != 0.
5. **CHECKED (C8-C10, exact).** At Jx = Jy = Jp, Jz = 8 kappa^2 Jp/(4 kappa^2+Jp^2), e^{2 pi i x} = (2 kappa + i Jp)^2/(4 kappa^2+Jp^2): tr M = 0 and all sixteen 3x3 minors of M vanish, symbolically in Jp and kappa. At Jp = 1 this is the landed handover parametrisation (kappa^2 = J/(4(2-J)), J = Jz; the landed note gives the points as e^{2 pi i x} = (2q +- i)^2/(1+4q^2) with q = kappa). Positive control (1, 1, 18/13; 3/4) at z1 = (5+12i)/13. Negative controls: moving Jz by 1/1000, or Jx by 1/1000, makes the minors nonzero at that point. Floating cross-check (C7): at each of the five supplied (Jx != Jy) couplings the minimum of det M/16 over L1 on a 2001-point grid is positive (0.30 to 37.5).
   **NEW relative to the sources:** the landed handover note covers only Jx = Jy = 1 and says nothing for Jx != Jy; scaling gives Jp > 0 arbitrary at Jx = Jy, but the closed statement "no touching on L1 iff Jx != Jy, and on the locus exactly these two points", valid for all positive couplings, is not in the sources. **READING:** with the charge-two merged point at Jx = Jy, the quantity (Jx-Jy)^2 S^2 in step 3 is what keeps the pair apart on L1 once Jx != Jy; the earlier unlanded campaign-6 attempt reports a splitting into two simple nodes in floating point, consistent with this but not derived from it.
6. **CHECKED (B6, B7; exact evaluation) (elementary, possible overlap with the open event-coverage task).** At the eight points z_j = +-1, det M = 16 g^2 with g(1,1,1) = (Jx+Jy)^2 - Jz^2, g(-1,-1,1) = (Jx-Jy)^2 - Jz^2, g(+-1,-+1,1) = Jx^2 - Jy^2 - Jz^2 - 4 kappa^2, g(+-1,-+1,-1) = Jx^2 - Jy^2 + Jz^2 + 4 kappa^2, g(1,1,-1) = (Jx+Jy)^2 + Jz^2 > 0, g(-1,-1,-1) = (Jx-Jy)^2 + Jz^2 + 16 kappa^2 > 0. So a touching at one of these eight points occurs exactly on the four hypersurfaces Jz = Jx+Jy, Jz = |Jx-Jy|, Jx^2 = Jy^2+Jz^2+4 kappa^2, Jy^2 = Jx^2+Jz^2+4 kappa^2. The first two are the "boundary couplings" of the sources; I did not find the last two stated in the pinned notes.

**Complex census at the five supplied couplings B, A, C, F, G (`check.py` section D).**

7. **CHECKED (exact, D1).** On the slice z1 z2 = 1, the points where all 3x3 minors of M vanish are exactly z3 = 1 together with z1^2 q((z1+1/z1)/2) = 0, with q the landed line quadratic: 4 complex points, 2 on the torus when q has a root in (-1,1) (B, A, C, F) and 0 at G. No point has z3 = -1 (consistent with step 4, which excludes a touching there for Jx != Jy; the complex statement is stronger and is the lex Groebner basis result).
8. **CHECKED (exact lex Groebner basis, D2).** On the slice z1 = z2 =: z, the rank<=2 locus is 10 complex points: z3 = w is a root of a squarefree palindromic polynomial P(w) = w^5 Q'(w + 1/w) of degree 10 and z is a linear function of w. Q' is an integer quintic, **irreducible over Q at all five couplings**; at B,

   `Q'(x) = 6561 x^5 + 182250 x^4 + 2003940 x^3 + 11064420 x^2 + 29877520 x + 86152832`,

   the other four are printed by `check.py`. An exact Sturm count finds **no root of Q' in [-2,2]**, so no point of this slice has |z3| = 1 and none is on the real torus. The swap plane z1 = z2 is the only locus (besides the mirror lines) where the swap symmetry of det M has fixed points, but it carries no operator symmetry (step 1), so its 10 points are not protected by a block structure; READING: they are a second algebraic family attached to the same minors.
9. **CHECKED (modular, D3).** Groebner basis of the full minors ideal plus a saturation variable (grevlex, GF(32003)), computed by sympy: zero-dimensional of length **34** at each of B, A, C, F, G. The characteristic polynomial of multiplication by z3 equals, mod 32003, (x-1)^4 * P_swap(x) * (x^5 Q5((x+1/x)/2))^2, with P_swap from step 8 and Q5 the supplied quintic. So length 34 = 4 + 10 + 2*10 (the supplied 4-point orbit: 5 values of alpha, each with 2 values of z3 and 2 points each).
10. **CHECKED (exact, D4).** Each supplied Q5 is irreducible over Q with exactly one root in [-1,1]; the three z3-polynomials (z3 = 1, P_swap, the quintic orbit) are pairwise coprime over Q and only the line stratum vanishes at z3 = 1.
11. **READING/CHECKED (D5; ASSUMED that 32003 is a good prime for these five ideals, not verified).** Real-torus points need |z3| = 1. That leaves z3 = 1 (the 4 line points, 2 on the torus when q has a root in (-1,1)), no swap-plane point, and for the generic stratum the unit-circle roots of the squared factor, each carrying at most 2 points: at most 4. The sum is 6 (B, A, C, F) and 4 (G), which equals the interval-certified census of the sources. So the sources' real-torus census is reproduced, as an upper bound, by a method with no Taylor clearing, and the 10 swap-plane points and the pairing of the 20 generic points are made explicit.

**What is not shown.**

12. **NOT SHOWN.** Torus points of the swap plane for general positive couplings. 3000 random couplings (floating point, 61x61 grid plus Nelder-Mead refinement) give minimum of det M on the plane z1 = z2 (scaled by (sum J)^4) never below 3e-8; the smallest values sit at the points (+-1,+-1,+-1) where det M is a square (step 6) and are positive. This is a sample, not a theorem.
13. **NOT SHOWN.** That length 34 holds for all positive couplings: the five fixtures include J_z < |Jx-Jy| (G), J_z = Jx (A, C), large kappa (G, C) and J_z > Jx+Jy has not been run. A bad prime or a non-generic coupling could change the count.
14. **FIRST UNRESOLVED STEP (14).** A symbolic (over Q(Jx, Jy, Jz, kappa)) elimination of the 20-point generic stratum to a polynomial in alpha = cos 2 pi f3, to show that its degree is 5 for generic couplings, to find its discriminant and its resultant with Q' (the locus where generic orbits collide with the swap plane: a candidate for the birth/death surface of the off-plane orbit), and to read off where its real roots in [-1,1] stay realizable (d^2 = sigma^2 - 4 pi >= 0, nonzero denominators s1+s2 etc.). A rational Groebner computation of the full 3-variable system at B was started and killed after 26 minutes without finishing (sympy, pure Python); that is why step 9 is modular.

## What is NEW relative to the sources

- Steps 1-2 (operator form of the swap-inversion symmetry and its two fixed lines): the sources state spectral symmetries; I did not find P or the block structure on L1 in them.
- Steps 3-5 (second mirror line): new theorem for all positive couplings. Scope: this concerns the line L1 only. It says nothing about the generic off-plane orbit.
- Step 6: elementary; the last two hypersurfaces may overlap with the open event-coverage task.
- Steps 7-11: new data (swap-plane stratum, second family of quintics, length 34 at five couplings), CHECKED modular. Not new: the line quadratic (D1 reproduces it), the quintic Q5 and the real census.
- Retrieval, the old numerical results, the Krawczyk nodes of the unlanded attempt and the known corrections are background.

## Status words

Nothing here is retained, audited or accepted. Step 4 is a complete proof given the identity of step 3, which `check.py` verifies by exact expansion. The remaining steps are labelled as above.
