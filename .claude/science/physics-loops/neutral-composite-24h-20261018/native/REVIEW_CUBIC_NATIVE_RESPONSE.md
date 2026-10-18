# Focused cubic native response review

Disposition: PASS pending the narrow reproduction fix below; no science demotion requested. Ordinary scoped review only, no formal audit or merge.

The note correctly limits the conclusions to the supplied finite Hamiltonian, chosen plane/spatial sectors, and explicitly chosen summed diagnostics. It distinguishes exact symmetry dimensions from numerical lowest-eigenvalue candidates and disclaims global ground, thermodynamic scalar, mass scaling, and detector identification. The 36-site rectangle is not assigned cubic irreducible labels. The original Cz length-three alias and its removal at length four are correctly scoped. Source weights are overlaps with centered summed operators, not intensive residues or empirical coupling strengths.

Reused INDEPENDENT_CUBIC_SECTORS, CUBIC_RESPONSE, NATIVE_Q, RECT_ENGINE, RECT_TRANSLATIONS and SPACEGROUP. The raw logical Pauli double commutator is formed before spatial projection; every Ha preserves the plane sector, making that stage legitimate. The corrected response script follows this order. The previously incorrect projected-Ha calculation and unresolved quadrature nodes are preserved and excluded from accepted claims. The source mean and variance, selected lines, and residual limits in the note agree with the frozen JSON. The 20 saved eigenpairs include the ground and 19 excited vectors; captured connected weight is the sum over those excited lines.

Read the runner and relevant model/response source. Independently checked every manifest SHA256: 17 source files and 11 result files match. The runner's 29 literal inputs equal those 28 files plus IDENTITIES.json exactly. The four response captured-weight sums agree to floating-point rounding; the largest saved residual is 9.083779814337347e-12. The short runner tests an 8-site physical intertwiner and recomputes selected 27-site responses; it explicitly only hashes frozen 36-site outputs. I did not duplicate the large eigensolves or the parent's in-progress replay.

Required narrow fix: replace the abbreviated IDENTITIES.large_recipe with an ordered clean-scratch recipe including neutral_rect_ground.py before neutral_rect_spacegroup.py and neutral_rect_spacegroup_response.py, an explicit working directory, exported thread limits applying to every command, and scratch-to-frozen result filename mapping. The original recipe acknowledges missing basis dependencies but does not supply the complete executable sequence. No other material finding.

Reviewed hashes:
- `docs/NATIVE_CUBIC_SCALAR_RESPONSE_NOTE_2026-10-18.md`: `c8429fe15b071f89204a9d1b1380f99d41bca682dd42bc9eb40eaed8b0df768b`
- `scripts/native_cubic_scalar_response.py`: `36e94200908b10bd4eeaefbd593196634b3fb8b74e679b0b62457b3a6270f275`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/cubic_results/IDENTITIES.json`: `ae5e5afaae8767d847b325e0d94dc948f8dbe54b300f3f746eca47f9c0779221`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_rect_spacegroup_response.py`: `1f0e77779a09877d67ef77c097e69b401eeb36acbcfd4f3e79011d381fb1cd83`

Final affected-fix confirmation: PASS. REPRODUCTION.md now supplies repository-root starting context, exported thread limits, the ordered ground → spacegroup → response sequence, and scratch-to-frozen mapping. The manifest points to it. The additional original-Cz failed diagnostic is preserved and declared. Rechecked all 17 source and 12 result hashes; all match, and the runner now declares 31 existing inputs including the recipe. No outstanding material finding. Large scientific calculations were not rerun for this metadata fix.
- Updated `.claude/science/physics-loops/neutral-composite-24h-20261018/native/cubic_results/REPRODUCTION.md` SHA256: `88dd9bb3c8336ffd723e838c5f3900b90f13746da015f556c839f0d66c7bafe7`
- Updated `.claude/science/physics-loops/neutral-composite-24h-20261018/native/cubic_results/IDENTITIES.json` SHA256: `52108e0c5d8cb9b3ad355712662afc031e819bcaf4ae6bfd45d886f30f114ee0`
- Updated `scripts/native_cubic_scalar_response.py` SHA256: `6428e673308eda131a7b539ae72ca2752c1a0e8f77755d330ac18507867c0b07`
