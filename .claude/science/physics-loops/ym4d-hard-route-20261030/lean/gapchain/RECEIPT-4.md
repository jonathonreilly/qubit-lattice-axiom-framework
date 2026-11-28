# Repo search

The lead's November 8 search covered main and PRs #10114, #10133, #10134 and #10141. I checked the two theorem names in the Lean files outside this lane on main `8b11ae2bb95e` and the four PR refs `f76f6c649cff`, `89faef229ff6`, `1e70c7211a2c` and `a2f6a430e251`, respectively. The searches returned no implementation. The closest soft-route hit was `MASS_GAP_LOCAL_BLOCK_ASTRA.md` on #10114, lines 106–149. It gives a local, one-step plaquette correlation estimate. The target-specific prior file was absent, and the registry assigns physical seed production to separate work. [Lead's search](../../library/prior/repo-search-2026-11-08.md) · [Open registry](../../library/open-registry.md)

In the pinned checkout, row 1459 supplies the kernel proof of M1, row 1161 supplies the finite-aspect hand proof, and row 1657 supplies the actual centre projections, signed Wilson integrals, rectangular spectra and equality of their moments. Row 1643 locates the separation between the fixed-coupling assembly and the continuum reduction. Those are the closest local results. [Lemma M1](GapChain/LemmaM1.lean) · [Finite-aspect argument](../../library/gap-solve9-astra62.md) · [Stage 3](GapChain/Stage3.lean) · [Row 1643](../../library/gap-direction8-fable.md)

# Stage 4 of the conditional gap chain

**BUILT.** Both implications kernel-check at their exact Stage 0 types on parent `8e60948e0e4133ecbbfc043b9d9c760610277fa5`. The new module imports Stage 0 and Stage 3. An `example : type_of% @GapChain.…` assigns each new theorem directly to the corresponding interface. Both public proofs depend only on `propext`, `Classical.choice` and `Quot.sound`. The output below covers every theorem declared in the module. This is conditional research for FINISH row 1658. The production of a calibrated neutral seed and the remaining Stage 3 comparison are open. [Stage 4](GapChain/Stage4.lean) · [Stage 0 interfaces](GapChain/Stage0.lean) · [Stage 3 receipt](RECEIPT-3.md)

## W8. The neutral rank-one test at both times

Write \(T=\Gamma.\mathrm{transfer}(3,\beta)\) and let \(P\) be the actual neutral centre projection. Stage 3 identifies this projection and proves that it commutes with \(T\). The new trace identity works at every integer time \(a\ge2\), including time two. In a Hilbert basis diagonalizing the positive operator \(TP\), the positive slots have precisely the sector moments. The remaining basis vectors lie in its kernel. Parseval for the release Peter–Weyl family and summation of the nonnegative squared overlap coefficients identify the spectral sum with the release trace and prove absolute summability. The strictly positive two-step Wilson integral gives \(\lVert T\rVert>0\).

Since \(PT^w=(TP)^w\), the original test vector and scale can be used in M1. If \(v_i\) are the eigenvalues of \(TP\), the resulting inequalities are

\[
  \bigl(1-(2/5)^2\bigr)\sum_i v_i^{2w}
       \le \lVert (TP)^w\rVert^2 \le \lVert T\rVert^{2w}.
\]

The second bound uses \(\lVert P\rVert\le1\). Each \(v_i/\lVert T\rVert\) lies in \([0,1]\), so the normalized moments decrease after \(2w\). Subtracting one gives \(4/21\) at both \(2w\) and \(\max(3,2w)\). This argument needs only the operator norm bound on each slot. It applies without choosing a neutral top eigenvector. [Stage 1 proof](GapChain/LemmaM1.lean) · [Stage 0 check, W8](../../library/lean-gap-chain-stage0-check-opus.md)

## W7. The strict finite-cube Pfaffian seed

Take the witness \(u\) from the neutral physical seed, so \(3\le u\), \(512u\le n\) and the neutral moment at \(u\) is at most \(3/2\) in periodic-vacuum units. Here \(4\mid n\) and \(n\ge 2^{70}\). Row 1161 supplies the flux comparison, magnetic translation and finite-aspect argument. Its lines 213–227 treat the small and large alternatives for the seven periodic charged top weights. The new proof bounds the common Pfaffian contribution directly, so the same calculation applies in both alternatives. [Row 1161](../../library/gap-solve9-astra62.md) · [Row 1643's check of the finite-aspect estimates](../../library/gap-direction8-fable.md)

1. Averaging over the original electric signs before changing the time direction gives the sharp comparison of every sector moment with the periodic neutral moment. Two changes of frame erase the magnetic bits. The proof uses nonnegativity of the actual crossed Fourier sectors. All sectors therefore have short-time normalized moment at most \(3/2\).
2. A compensated spatial half-period translation preserves the signed Wilson kernel. Its square is the centre translation specified by a row of the magnetic twist. For misaligned electric and magnetic flux, one such row has character \(-1\). Composing the translation with complex conjugation gives an antilinear map squaring to \(-1\) on each positive eigenspace. A complex line cannot support this map. Thus a positive misaligned top level has at least two spectral slots. Counting slots also bounds each excited level in every sector. At \(t\ge (j+1)u\) the excited tail, and the entire misaligned sector, are each bounded by \((3/2)(3/4)^j\).
3. The time comparison uses the integer displacement \(k=\lfloor n/2^{69}\rfloor\). It satisfies \(k\ge1\), \(n\le2^{70}k\) and \(u+k+2k\,2^{67}\le n\). For a normalized level \(z\), the second difference is exactly \(z^{n-k}(1-z^k)^2\). Two geometric-sum bounds give a sector second difference at most \(2^{-133}\). Fourier inversion and positivity in the crossed time frames at \(n-k\) and \(n+k\) compare the forward differences of pure magnetic and pure temporal twists. The finite bit tables and the paths of at most four elementary basis changes are checked by the kernel. All three periods use the original periodic vacuum for normalization.
4. For a nonzero magnetic twist \(m\), the pure magnetic normalized weight at \(n\) is at most \(3/2\), and its drop from \(n\) to \(n+k\) is at most \(2^{-121}\). Let \(\rho\) be the aligned sector's normalized top level and \(x=\rho^n\). The neutral and aligned terms in the magnetic sum give \(x\le3/4\). Positivity of the slot drops gives \(x(1-\rho^k)\le2^{-121}\). Since \(1-x\le2^{70}(1-\rho^k)\), it follows that \(x(1-x)\le2^{-51}\), hence \(x\le2^{-49}\) and \(\rho^{n/2}\le2^{-22}\).
5. At half time, \((3/2)(3/4)^{255}\le2^{-84}\). Stage 3's exact Pfaffian identity sums the eight diagonal electric–magnetic sectors. Subtracting the periodic vacuum leaves at most \(2^{-84}+7(2^{-22}+2^{-84})<2^{-18}\). The sides in the conclusion are exactly \((n,n,n,n/2)\).

## Sources and conventions

Ethan Sussman and Levent Alpoge, with Claude and Codex as the authors of their text, supply the release transfer, slice, inner-product and Peter–Weyl conventions. The indexed outline at lines 587–605 and complete account I at lines 3209–3223 delimit the clustering statement. Account I explicitly leaves OS4 and a mass gap open in that passage. The index of items 4.12–4.19 yielded no prior Pfaffian implication. The finite-torus Pfaffian deduction used here comes from the lane. Both source files were fetched once at `31a47c543775`. [Outline](https://raw.githubusercontent.com/ethanwsussman/Yang--Mills-LLM-experiment/31a47c543775/YM4_sketch_500.tex) · [Complete account I](https://raw.githubusercontent.com/ethanwsussman/Yang--Mills-LLM-experiment/31a47c543775/theorem_0_complete_account_raw_I.tex) · [Outline index](../../library/sa-index/README.md) · [Account index](../../library/sa-index/ca-4.12-4.19/README.md)

Rows 1457 and 1458 prescribe the time direction, domain, calibration and shared witnesses. Row 1652 fixes the two interfaces, and row 1653 gives the hand check of W8. Stage 2 already supplies the conditional reconstruction implication. Both new proofs preserve the original cube, coupling and witnesses. [Design](../../library/lean-gap-chain-design-fable.md) · [Design check](../../library/lean-gap-chain-design-check-astra62.md) · [Stage 0 receipt](RECEIPT-0.md) · [Stage 2 receipt](RECEIPT-2.md)

## Build and trusted base

The scratch project's toolchain was Lean `4.33.1` at `819816b2e0a3bf405af45ae5c7af2491d8f5bee6`. Mathlib was `0df444a360eaa60ab8c11dca51a86af692955474` and the replayed release was `3932084a9b82fc79466b4a2faad9ec032b637445`. The trusted computation is the Lean kernel checking proof terms against those imported objects, with the axioms listed below. Exact finite decisions use ordinary `decide`. The inequalities are proved over naturals and reals.

The project copied the pinned local modules, linked the prebuilt packages and added the two requested roots. The release-only preflight found all 21,134 dependency jobs up to date. Each worker used two Lean threads, nice level 10, and a launch gate of at least 50% free from `memory_pressure -Q`. The final build and measured dependency replay serialized compiler processes with a worker lock. A guard rejected external source compilation, and the child sandbox denied writes to the fixture. For memory control, the worker used 47,189 byte-verified scratch copies of compiled dependency artifacts. An external pager advised macOS on resident pages of these read-only copies. The compiler and kernel binaries were the pinned binaries throughout. The guard ran the following Lake targets inside the prepared scratch project, with the toolchain and read-only artifact mapping above.

```sh
LEAN_NUM_THREADS=2 /usr/bin/nice -n 10 lake --no-cache build +GapChain.Stage0:olean +GapChain.Stage4:olean
```

Lake reported `Built GapChain.Stage4 (156s)` and `Build completed successfully (21144 jobs).` Only the Stage 4 module compiled in the final invocation. A second invocation with `--no-build` reported `All targets up-to-date (21144 jobs).` Stage 4 produced zero compiler warnings. The previously built Stage 0 still contains its four designated placeholders. All 91 new theorems passed the axiom check. The release's cached diagnostic messages in the Lake log are replay output.

| Verified artifact | SHA-256 |
| --- | --- |
| Repository and scratch copies of `Stage4.lean` | `1c19a96e9b79cf19689df32849fcf41e716078c42e503107b62ae3a9a825ab1d` |
| Compiled `GapChain/Stage4.olean` | `955044bb52d575885cd7abe301f29967dc24537be722397a682dc675a20d47d8` |

## Resource record

Wall times below are in seconds and peak RSS is in bytes as reported by Darwin `wait4`. The worker wall time includes any setup-file remapping and waiting for the child. The driver row measures the outer run. Driver and compiler peaks must not be added. The final Stage 4 compiler worker took **156.370 s** and peaked at **4,918,919,168 bytes**. The highest recorded compiler peak across development was **5,572,722,688 bytes**.

The first bare `~/.elan/bin/lean --version` in the checkout reported 4.36.0. Its shell call took about 0.60 s and did not capture peak RSS. The table includes its measured replay and the scratch 4.33.1 check. The first bootstrap guard misclassified three local paths because macOS resolved `/tmp` to `/private/tmp` and refused them before launching Lean. After that correction, a sampler's call to `/bin/ps` failed under the read-only fixture sandbox. Lake reported 17 s for SequenceLemma, 18 s for TheoremS, and 4.7 s for LemmaM1 in that attempt. Their per-process peaks are unavailable. All three were subsequently compiled with the corrected sampler and individually measured. Two scratch diagnostic sessions hit the conservative RSS cutoff. The second stopped during an early natural-division tactic. The final proof uses the division-with-remainder identity and linear inequalities there.

| Run | Program or local module | Free at launch | Wall s | Peak RSS bytes | Exit |
| --- | --- | ---: | ---: | ---: | ---: |
| version-pinned | lean --version | 70% | 0.444 | 50,233,344 | 0 |
| version-pinned | lean driver | 70% | 0.481 | 50,233,344 | 0 |
| preflight | lake driver | 70% | 22.011 | 1,030,832,128 | 0 |
| bootstrap | lean --githash | 70% | 0.052 | 49,807,360 | 0 |
| bootstrap | lake driver | 70% | 18.054 | 986,071,040 | 1 |
| base-and-imports | lean --githash | 70% | 0.041 | 49,807,360 | 0 |
| base-and-imports | lake driver | 70% | 38.528 | 912,605,184 | 1 |
| local-deps | lean --githash | 68% | 0.051 | 49,790,976 | 0 |
| local-deps | SequenceLemma | 68% | 19.721 | 2,984,280,064 | 0 |
| local-deps | TheoremS | 66% | 3.397 | 3,401,252,864 | 0 |
| local-deps | LemmaM1 | 66% | 3.652 | 3,180,920,832 | 0 |
| local-deps | Wilson | 66% | 5.017 | 3,403,907,072 | 0 |
| local-deps | Transfer | 66% | 11.740 | 3,454,566,400 | 0 |
| local-deps | Stage0 | 66% | 320.757 | 3,270,049,792 | 0 |
| local-deps | Trace | 65% | 17.622 | 3,412,918,272 | 0 |
| local-deps | Stage3 | 65% | 576.103 | 4,672,733,184 | 0 |
| local-deps | Stage4 | 66% | 385.719 | 5,572,001,792 | -9 |
| local-deps | lake driver | 68% | 1357.538 | 5,572,001,792 | 1 |
| editor2 | lean --githash | 68% | 0.051 | 49,807,360 | 0 |
| editor2 | Stage4 | 68% | 513.609 | 5,572,722,688 | -9 |
| editor2 | lake driver | 68% | 531.244 | 5,572,722,688 | 1 |
| editor3 | lean --githash | 68% | 0.051 | 49,823,744 | 0 |
| editor3 | Stage4 | 68% | 473.048 | 4,941,987,840 | 0 |
| editor3 | lake driver | 68% | 490.623 | 4,941,987,840 | 0 |
| stage4-final | lean --githash | 68% | 0.051 | 49,774,592 | 0 |
| stage4-final | Stage4 | 68% | 156.370 | 4,918,919,168 | 0 |
| stage4-final | lake driver | 69% | 174.016 | 4,918,919,168 | 0 |
| stage4-uptodate | lean --githash | 69% | 0.051 | 49,807,360 | 0 |
| stage4-uptodate | lake driver | 69% | 17.047 | 983,662,592 | 0 |
| default-version-replay | elan/lean --version | 69% | 0.666 | 51,200,000 | 0 |

The diagnostic sessions used ordinary Lean elaboration to check successive source drafts in one process per session. Those sessions share their process peak across all in-process draft checks. The last development session checked the complete release candidate in 13.012 s before the fresh Lake invocation. Full driver logs, the resource records, each completed draft's elapsed milliseconds and diagnostics, and the dependency copy hashes are in the scratch directory below. Only the final source and its recorded build output are needed to identify the delivered result.

- Scratch project and downloads are in `/tmp/sa-lean-gap-chain-stage4-astra62.P1obT5`.
- The final build and resource logs are `logs/stage4-final.log`, `logs/stage4-uptodate.log` and `logs/runs.jsonl`. The full dependency copy inventory is `archive.tsv`.
- The download SHA-256 values were `d7f77d4da3eb23038250c52468a341281d9ba86b4af21d3371d208a2537d4b6f` for the outline and `4cb5cb5e0af8dbddbee207926621300350e018c6cf1d6567a753167ce10e6e93` for account I.

## Verbatim kernel axiom reports

The following are the messages emitted by the final Lake compiler, in source order. Lake's filename and position prefixes have been removed.

```text
'GapChain.Stage4.releaseSectorBasis' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage4.pwTrace_of_eigenbasis' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage4.projected_power' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage4.projectedTrace_eq_sectorWeight' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage4.periodicTransfer_norm_pos' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage4.neutralTail_iff_sectorWeight' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage4.neutral_projection_norm_le' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage4.neutralTail_after_rankOne' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage4.neutralTail_of_rankOneAtTime' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage4.inFrame_time' depends on axioms: [propext]
'GapChain.Stage4.inFrame_planes' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage4.raw_in_frame' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage4.crossed_neutral_sum' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage4.crossed_erasure' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage4.sectorWeight_le_periodicNeutral' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage4.cubeSides_ge_two' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage4.sectorMoment_bound' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage4.excited_slot_le' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage4.tail_at_multiple' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage4.magneticBit_diag' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage4.magneticBit_symm' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage4.magneticBit_plane' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage4.misaligned_row' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage4.halfTurn_val' depends on axioms: [propext, Quot.sound]
'GapChain.Stage4.halfTurn_twice' depends on axioms: [propext, Quot.sound]
'GapChain.Stage4.finRotate_val_if' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage4.halfTurn_rotate' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage4.inStrip_halfTurn' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage4.inStrip_boundary' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage4.shiftedSite_twice' depends on axioms: [propext, Quot.sound]
'GapChain.Stage4.shift_rectStep' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage4.strip_curl' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage4.strip_squared' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage4.compensated_sq' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage4.pi_pull_involution' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage4.compensated_apply' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage4.compensated_preserving' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage4.rectStep_comm' depends on axioms: [propext, Quot.sound]
'GapChain.Stage4.rectFace_spatial' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage4.compensated_word' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage4.compensated_action' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage4.compensated_temporal' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage4.compensated_gauge' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage4.compensated_kernel' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage4.rectHalfWeight_gauge' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage4.rectSymKernel_gauge_right' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage4.compensated_flip' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage4.compensated_electricEntry' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage4.pull_operator_commutes' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage4.sliceConj_smul' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage4.pull_conjugate' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage4.real_kernel_conjugate' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage4.rectSector_conjugate' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage4.magneticShift_square' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage4.magneticShift_commutes' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage4.translation_on_sector' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage4.finrank_ne_one_of_antilinear' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage4.misaligned_not_simple' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage4.slot_le_of_moments' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage4.misaligned_partner' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage4.cubeFluxSpectrum' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage4.flux_moment_bounds' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage4.geometric_loss' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage4.differenceStep_budget' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage4.second_difference_term' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage4.second_difference_identity' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage4.sector_second_difference' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage4.inFrame_involution' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage4.invert_fourier' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage4.fourier_raw' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage4.fourier_time' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage4.boxSides_cube_diag' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage4.fourier_cube' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage4.fourier_raw_nonneg' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage4.fourier_sub' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage4.fourier_second' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage4.character_abs' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage4.signed_flux_sum' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage4.fourier_bound' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage4.changed_character' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage4.shear_bound' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage4.comparisonPath_spec' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage4.path_bound' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage4.pure_comparison' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage4.short_ratio_at' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage4.cube_comparisons' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage4.pureMag_upper' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage4.untwistedElectric_sum' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage4.level_drop_bounds' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage4.aligned_half_small' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Stage4.kappaSeed_of_neutralPhysicalSeed' depends on axioms: [propext, Classical.choice, Quot.sound]
```

## Next row and decisive outcome

Complete Stage 3's `PairWindowEstimate` on the same seeded cutoffs. The first remaining identification is the ordered vacuum matrix element of the doubly centred product \((\theta X)(\tau_{(2n+1)a_j}Y)\) viewed as one finite slab. The separation-independent exponential prefactor and the vanishing thermal/volume error must hold with the original cutoff state and witnesses. The decisive outcome is a kernel proof of `expClusters_of_kappaSeed` at its exact Stage 0 type using only the three allowed axioms, or the first explicit estimate or witness identification that fails. [Stage 3's remaining estimate](RECEIPT-3.md#first-remaining-estimate)
