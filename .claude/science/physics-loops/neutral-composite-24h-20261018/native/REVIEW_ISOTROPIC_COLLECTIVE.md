# Focused isotropic collective review

Disposition: DEMOTE pending two narrow geometry qualifications. The exact collective algebra and scoped dynamical conclusions otherwise pass. No shared edits or formal audit.

Required fixes: (1) qualify the canonical variational energy and actual-ground O(1/N) maximal-spin weight by the growing even-x periodic family, Lx>=4, as already required in the proof. (2) require both the momentum mesh and the infrared cutoff to be invariant under x/y exchange when dropping the Gram correction. Equal-side cubic tori suffice. On general rectangular periods retain -(2J^2/N)|sum_cut F|^2. The independent report explicitly records this qualification; the main proof should too.

The PHP compression, coherent leakage norm, fourth-moment reconstruction, and lower/upper operator bounds are consistent. Coherent-state symbol injectivity in the fixed maximal-spin irrep justifies reconstructing the full quartic operator, so the result includes symmetric entangled states. Distinct nearest-neighbor bonds and degree-two incidence per axis suffice for the H-squared calculation: length-three cycles cause no additional term. Thus sides>=3 are valid for these exact identities and the 27-site controls. This does not relax the separate even-x dimer matching condition.

The variational dimer expectation and projected ground-eigenvalue equation give the stated weight bound using the UPPER leakage bound. No closeness of the dimer product to the exact ground is assumed, and no ground phase is inferred. The bound concerns maximal-spin weight rather than exclusion of all collective structures.

The first residual has two spin flips, magnetic quantum number S-2, and vanishing raising action by sum a_alpha^2=0. It therefore lies exactly in total spin S-2. Coherent vectors span P, extending the range statement to all symmetric inputs. It concerns the first action only. The Fourier spin-pair Gram factors and continuum kappa^7 coefficient are correct subject to the mesh qualification above. The filtered vector is not an invariant spectral subspace or canonical boson occupation.

The local short-time magnetization coefficient follows from four units of magnetization loss per bond pair flip. Bounded-degree third nested commutators supply a volume-uniform remainder for local observables; this avoids mistaking an extensive global leakage norm for a uniform survival-probability theorem. No long-time lifetime follows.

The inspected controls apply native H to low-excitation Dicke vectors and compare 25 collective matrix elements, then check coherent spinors, two-qubit dimer expectations and highest-weight cancellation. The infrared helper integrates the exact continuum form factor. These are accurately described as local/algebraic controls rather than full 27-qubit ED or an empirical test. The runner explicitly binds its proof and imported helpers. No duplicate source-bound replay was performed.

## Reviewed SHA-256 identities

- `docs/NATIVE_ISOTROPIC_COLLECTIVE_NOTE_2026-10-18.md`: `2ff0ca239d158af925ffec012cae3aed4db25cad4e58e03b734ee7aac35820d3`
- `scripts/native_isotropic_collective.py`: `63db4826ad201c5a8c009d38a0a8962788937bf5f21c93f28771ec2e63b5b62b`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/ISOTROPIC_COLLECTIVE_PROOF.md`: `daba867b46797bc64e3e8d016b6d6dd7148c47521a80ca7bfab769dee37202a6`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/INDEPENDENT_ISOTROPIC_COLLECTIVE.md`: `508d662ac707d8f7d9a1fa96669ef888d2841125d9da6d5620f8d1a7b28dc0cd`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_isotropic_collective_control.py`: `02ad2e891e0823b987b5221e204e0067b1f7d59c36686732ca22e89f2f48650a`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_isotropic_ir_control.py`: `d0ea8ab2248b5e958c344e35c1037aa1a1d100f3276d8552cf11cd241c7e2e44`

## Affected-source confirmation — final PASS

Verified both requested geometry qualifications. The canonical ground-weight statement now explicitly applies to growing periodic grids with even Lx>=4. The proof requires x/y symmetry of both momentum mesh and cutoff for cancellation, and retains the full Gram correction in general. These resolve both findings. Final disposition: PASS for the scoped maximal-spin identities, specified-family ground-weight bound, and initial fluctuation diagnostic. Parent reports replay passed; no duplicate replay or formal audit was performed.

- `docs/NATIVE_ISOTROPIC_COLLECTIVE_NOTE_2026-10-18.md`: `2ff0ca239d158af925ffec012cae3aed4db25cad4e58e03b734ee7aac35820d3`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/ISOTROPIC_COLLECTIVE_PROOF.md`: `daba867b46797bc64e3e8d016b6d6dd7148c47521a80ca7bfab769dee37202a6`
