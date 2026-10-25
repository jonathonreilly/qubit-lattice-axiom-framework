# ATTEMPT: first-order strain response after a supplied taste split

Task `J:derive:review-20261016-taste-split-linear-strain:a1`. Worker: Claude Sonnet 5.5. Same family as every earlier TW-2 worker and referee; unrefereed; no cross-family confirmation was run. Not accepted science, not an audit verdict. No repository file was edited. Files: `check.py` (run: `PASS=54 FAIL=0`, 75 s, 0.46 GB), `check_output.txt`, `RECOVERY_STATUS.json`, `src_*.md` (the two verified source objects).

## 0. Plain words first

The question: when the taste split makes one twin light and one heavy, the light twin's mass can change in proportion to a gravitational-wave strain (first order), not only to its square. The TW-2 referee noted the preregistered test (the second derivative, "Hessian") never looks at this. Does a symmetry force the first-order coefficient to vanish?

Answer in three parts.
1. For the axis-aligned split the lane studied (taste vector along a lattice axis), **no symmetry forces zero**. One tetragonal strain component is allowed, and an explicit exact model gives it a nonzero value. The lane's own refereed number, B' = -0.0454 per e^2, is consistent with that.
2. If the **one-site translations** of the staggered field are counted together with the rotations, the allowed first-order response collapses to a single constant: the light-twin mass slope is `beta * sum_a h_aa nhat_a^2`. Every off-diagonal (T2g shear) strain then has **exactly zero** first-order twin-mass response for every split direction. A split whose taste vector points along the cube body diagonal has **zero** first-order mass slope for every strain.
3. This corrects one statement in the source (it said the body-diagonal first-order term "moves to T2g (allowed; not computed)"). It does not rescue the axis-split hazard: that branch keeps one free constant, which only a tuned symbol shape can cancel, not a symmetry.

Everything depends on one premise about the lane's own law (P3 below) that I could not test in the lane's code.

## 1. What I read

- `docs/MINIMAL_AXIOMS_2026-06-29.md` (233 lines) in full, and `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` (130 lines) in full, on current main `a77a3449c9`. The approved primitives there are `scale_reference_primitive`, `kinetic_isotropy_primitive`, `realized_state_primitive`. **None is used or needed here, and no new primitive is proposed.** The Lattice axiom supplies translations and proper cubic rotations (`MINIMAL_AXIOMS_2026-06-29.md:35-41`). The staggered kinetic law, the strain flow, the one-loop law and the splitting operator are downstream supplied content (`:108-130`).
- Source branch `claude/strain-hot-matter-twins-20261013`, frozen commit `6afb06951a13ca861b50f47a8faf5d5c06594109` (branch tip equals it, `git ls-remote`). Both source objects read in full; sha256 verified (`check.py` rechecks them): referee verdict `dacc968f...`, report `3dc6105c...`.
- Also read from that commit: `scripts/TW2/tw2_alg.py/.out`, `tw2_conv.py`, `referee/referee_tw2_independent.py/.out`, `f3_lib.py`, `f1_lib.py`.
- **Source mismatch the supervisor must know.** The TW-2 scripts import `flat/sublum.py`, `dirac.py`, `r1934_lib.py`. These are **not on the frozen branch or on current main**, so the lane's one-loop integral (B', B'') cannot be rerun from the repository. I did not try to reconstruct them. All lane numbers below are quoted, not reproduced.
- Prior art searched: main docs and `.claude/science`, open PRs by title. Related: `THE_GENERATION_COUNT...`, `TASTE_SCALAR_ISOTROPY_THEOREM_NOTE.md` (a Hessian isotropy theorem; no strain), open PR #9922 (translation characters force family-diagonal mixing in a different model, the cube tick; same kind of mechanism, different object, count once). Nothing on main or in open PR titles computes the translation-pair selection rule below. Related task `...flavour-strain-scope:a1` (residual-symmetry classification from the chirality-grid source) is a different source and is not advanced here.

## 2. Separation of sources

- **Axioms say:** nothing about strain, taste splitting, or one-loop mass shifts. Only the lattice symmetry group is used.
- **The lane supplied** (not derived here): the staggered edge with the doubler structure; the face-diagonal splitting symbol `cos k_i cos k_j` and its triplet transformation (`C5_TW2_report.md:88-121`); the SF strain flow `D_t(k) = D(Phi_t k)` with `v=(t/2) h.p` for E_g strains (`C5_TW2_report.md:21-33`); the one-loop law and its numbers (`:136-165`); the fixed-axis selector and the Hamming-splitting scale (kept supplied; no grid-scale lambda is forced, referee `:19`).
- **Proved or checked here:** sections 4-7.

## 3. Premises (every one is an assumption that can be wrong)

- **P1 (supplied).** The splitting is `sigma * sum_a n_a O_a`, `O_a` the face-diagonal triplet (O_23, O_31, O_12), with `|sigma n|` small; first order in `sigma n` is the target.
- **P2 (supplied, extended).** Strain acts by the flow `D(k) -> D(Phi_t k)`, `v_a = (t/2) sum_b h_ab p_b`, `p = grad(E^2/2)`. The lane applied it to the diagonal E_g strains only (T2g photon singular, `C5_TW2_report.md:33`). I apply the same formula to all symmetric traceless `h`.
- **P3 (ASSUMED about the lane's real law; verified only for my re-implementation).** The strained one-loop twin mass-matrix functional (i) is covariant under the staggered cubic rotations with `h -> R h R^T`; (ii) is covariant under the one-site shifts `S_a` taken in even pairs (`S_aS_b` preserves the singlet mass), which act trivially on a uniform strain; (iii) has an O(`sigma`) part linear in the amplitudes `sigma n_a`. The lane's own checks support (i) and a version of (ii): it records that `O_12` keeps `S1S2`, `S3Theta` (`C5_TW2_report.md:118`) and that the strained split law satisfies the folding rule (`:127`). It never tests T2g or the translation pairs against a strained law, and its photon, Psym vertices and lift are not in my model.
- **P4 (reading).** Twin masses are the two eigenvalues `mu0 +- |mu|` of the twin-space matrix `mu0 + mu.tau`, `mu_a` = coefficient on `O_a`.
- **P5 (ASSUMED).** At O(`sigma`) the corner self-energy has no taste-nonsinglet structure other than the `O_a` projections that shifts the twin masses once strain is on. The lane checked this for E_g and tetragonal strains (`:127-132`), not for T2g.

## 4. Steps

**1. (CHECKED, exact; re-derivation, not new.)** I rebuilt the staggered operator `h` on an `L^3` torus (L = 8, also 6 and 10) in exact dyadic arithmetic, without the lane's dictionary. Exhaustive search finds the one-site shifts `S_a` (sign field unique up to sign), and the face-diagonal mass-like operators `O_a = i diag(cx) cos k_i cos k_j` are the unique solutions of `{O,h}=0` in their class (exact nullspace). `check.py` A1-A5. The shift table reproduces the lane's: `S_c` flips exactly `O_c`; for `O_12` it commutes with `S1,S2` and anticommutes with `S3` (`scripts/TW2/tw2_alg.out:32`).

**2. (CHECKED, exact.)** The staggered rotations (sign field unique up to sign) carry the triplet `(O_23,O_31,O_12)` into itself by the **vector representation** (A10-A14; sign gauge `d=(-1,-1,-1)`, i.e. exactly `R`). Matches `tw2_alg.out:40-43` and report `:116`.

**3. (CHECKED, exact.)** The first-order strain-flow operators `dH(h)`, `dO_a(h)` (including the strain dependence of the split-mass symbols) are hermitian, eps-odd / eps-even as required, keep `{O,h}=0` along the flow, commute with every `S_c` (carry the same sign as `O_a`), and are covariant under the staggered rotations with `h -> R h R^T` (A6-A9, A13), for six strains including off-diagonal ones. This shows the extension P2 to T2g is a legal staggered operator.

**4. (PROVED, given P3; the finite group facts are also CHECKED exactly.) Selection theorem.** Let `b(h; n)` be the O(`sigma`) mass vector (coefficients on `O_a`). By P3, for every pair `(M,R)` in the group `G` generated by the rotation pairs `(R,R)` and the translation pairs `(T,1)`, `T in {diag(-1,-1,1), diag(1,-1,-1), diag(-1,1,-1)}` (`S_aS_b`), one has `b(RhR^T; Mn) = M b(h;n)`. Writing `b = K(h) n` (linear in `n`): `K(RhR^T) = M K(h) M^T`.
- Translation pairs alone: `K = T K T` for the three sign matrices, so `K_ab = 0` for `a != b`. K is diagonal for every h.
- `C2` about `x` (`R=M=diag(1,-1,-1)`) flips `h_xy,h_xz` and leaves `K_zz` fixed, so `K_zz` does not depend on them; `C2` about `y` removes `h_yz`. `C4` about `z` swaps `h_xx <-> h_yy`. With `tr h = 0`: `K_zz = beta h_zz`. The cyclic rotation gives the same `beta` for `K_xx`, `K_yy`.
- Result: **`K(h) = beta diag(h_11,h_22,h_33)`**, one constant. Exact linear algebra confirms: the space of equivariant `K` has dimension 1 for rotations plus translation pairs, 2 for rotations alone (constants `beta_E`, `beta_T`), 15 for translation pairs alone (B1, B6, B7; `|G| = 96`).
- The singlet (twin-mean) mass has no response linear in `n` for any `h`: dimension 0 with or without translations (B8).

**5. (PROVED, from 4 and P4; sympy-checked.) Consequences.**
- Light-twin mass slope for splitting vector `n`: `d|mu|/dt = sigma beta sum_a h_aa nhat_a^2 |n|` (E1).
- Axis `n=z`: slope `beta h_zz` (the tetragonal component only). E_g strain `diag(1,-1,0)` gives exactly 0: reproduces the lane's "exactly even" (`C5_TW2_report.md:134`).
- Face diagonal `n=(1,1,0)/sqrt2`, same strain: `-(1/2) beta h_zz` (E3).
- **Body-diagonal `n=(1,1,1)/sqrt3`: slope 0 for every traceless strain, E_g and T2g alike** (E2). Group form: the pair-stabiliser has order 12 and acts on strains as the tetrahedral group, which has no invariant vector in the 5-dim strain space (B3). With rotations alone the stabiliser of the vector is C3 (order 3; the source's D3 also contains elements that flip `n`) and leaves one trigonal T2g invariant (B3): this is the source's `:172` statement. **It is removed by the translation pairs.**
- **Every T2g strain, any `n`: zero first-order twin-mass response at O(`sigma`).**
- Axis: no first-order twin mixing (`K n` stays parallel to `n`). Non-axis `n`: the taste direction rotates at first order by `beta t (h_aa nhat_a)_perp`, independent of `sigma` (E4); for body diagonal with E_g strain this is nonzero while the mass slope is 0. The source observed such an odd part (`C5_TW2_report.md:171`). Its physical size and meaning are SUGGESTED, not computed.

**6. (PROVED, B9 + spectra.) No spatial symmetry forces the tetragonal coefficient to vanish.** A symmetry zero for the tetragonal coefficient of axis `n` would need a group element sending `h_tet -> -h_tet` with `n` fixed. Conjugation preserves the spectrum of `h`; `diag(-1,-1,2)` and `diag(1,1,-2)` differ. No element of the 48-element cube group does it (checked). Internal discrete symmetries (C, P, T, chiral conjugation) act trivially on a uniform strain (reading), so they cannot do it either. The E_g B1 zero on the axis exists only because C4 maps B1 to -B1.

**7. (CHECKED, exact; this is the explicit counterexample, a toy functional.)** On the exact torus (L=8; L=10 gives the identical value, so it equals the infinite-lattice moment), the third moment `tr[O_a(t) H^3]/V` of the taste-vector observable, with `H = h + (1/2) eps + t dH + s O_b + ts dO_b`, gives the coefficient of `t s`:
- `K_0 = (7/16) * identity`; `K'(tet=diag(-1,-1,2)) = diag(-1/8,-1/8,1/4)`, so **`beta = 1/8 != 0`**; `diag(1,-1,0) -> diag(1/8,-1/8,0)`; `diag(3,-5,2) -> diag(3/8,-5/8,1/4)`. So `K'_aa = beta h_aa` exactly, off-diagonal entries exactly 0.
- All four T2g strains (xy, yz, zx, trigonal): `K' = 0` exactly. Singlet channel exactly 0 (C0-C8).
- A smooth resolvent version `tr[O_a H (H^2+mu^2)^{-1}]` (float, tolerance 1e-12, L=6) shows the same structure, `K'_zz = -2 K'_xx = 0.036877` (D1-D2).

**8. (CHECKED, with tolerance; control.)** Adding the rotation-invariant but translation-breaking diagonal `V = 0.4 sum_a (-1)^{x_a}` (exactly invariant under both rotations, flipped by `S_a`; D3) reopens the T2g channel: `K'_xy = 1.5e-5` against `< 1e-12` without it, and the diagonal channel stays (D4-D5). So the T2g zero comes from the translation pairs, and the check can fail.

**9. (arithmetic only; READING for the lane.)** From the lane's refereed `B'(tet, axis) = -0.04541594 per e^2` (`C5_TW2_report.md:144`; referee `-0.0454159364`), the selection rule predicts for the same strain a face-diagonal split coefficient `-B'/2 = +0.0227` and exactly zero for body-diagonal and any T2g. These predictions have **not** been tested against the lane's code (it cannot be rerun).

## 5. What is NEW and what is not

- **Not new:** retrieval; the folding-class algebra and the `T_1` transformation of the triplet (`C5_TW2_report.md:88-121`, referee `:9`); the D4 symmetry-allowed tetragonal term and B' (`:166-175`); the clock-row arithmetic.
- **New (scoped, same family, unrefereed):**
  (a) The pair-group selection theorem (step 4): translation pairs make the first-order twin-mass response tensor diagonal and, with rotations, a single constant `beta`; hence T2g shears give zero and body-diagonal splitting gives a **forced zero first-order mass slope**.
  (b) A correction of `C5_TW2_report.md:172-173`: the body-diagonal first-order mass term does not "move to T2g", and the blanket claim that a first-order coupling is "symmetry-allowed in every case" holds only for directions with a nonzero `sum h_aa nhat_a^2` available. The source's rotation-only stabiliser omits the one-site-translation compensation it itself uses for the axis case (`:118`).
  (c) An exact finite-lattice model with all the stated symmetries in which `beta = 1/8 != 0`, together with the exact proof that no spatial symmetry forces the tetragonal coefficient to vanish.
  (d) The twin-mixing statement (step 5, last bullet) as a symmetry consequence.

## 6. Reading for the clock-row branch hazard (READING; not an exclusion)

The source's hazard (x4.7-17.8, `C5_TW2_referee_verdict.md:21`) lives on the axis branch and stays: a tuned symbol shape (source `:164`, price P-TW2b) cancels `beta` for the axis case with one number, not a symmetry. A taste vector along the cube body diagonal has no first-order twin-mass slope by step 5. That route costs more covariance (no translation pair fixes the vector; only rotation-translation combinations do), leaves the Hessian and first-order twin mixing, and needs the actual lane law to satisfy P3. It is a pointer for a test, not a proposal.

## 7. First unresolved step, and what is not done

- **First unresolved step: P3(ii) for the lane's real law.** The T2g and body-diagonal zeros hold for the lane's one-loop mass shift only if its strained photon-plus-Psym-vertex functional commutes with the translation pairs and the rotations. I verified this only for the fermion-side operator class (exactly) and for a toy functional. The disjoint test is to run the lane's 8x8 evaluator (`scripts/TW2/tw2_sigma8.py`) for a body-diagonal split with a T2g strain, and for the translation pair against the strained one-loop output. It is blocked by the missing `flat/` modules and by the T2g singular photon frame (`C5_TW2_report.md:33`).
- Not done: second order; the value of `beta` in the lane's law (not forced by any symmetry here, `-0.0454` is the lane's); Dirac structures other than `O_a` projections under strain (P5); the eps-odd twisted splitting family's translation signs; the Hamming-weight reading; any experimental row or flavour statement. A finite response in one model is not an exclusion, and nothing here derives a flavour structure.
- Attack points for a referee: the linearity-in-`n` step; whether the lane's twin-space 2x2 reading (P4) survives strain; whether `S_aS_b` is a symmetry of the lane's lift `U=1` Psym vertices; and that the toy functional shares only symmetry, not dynamics, with the lane.
