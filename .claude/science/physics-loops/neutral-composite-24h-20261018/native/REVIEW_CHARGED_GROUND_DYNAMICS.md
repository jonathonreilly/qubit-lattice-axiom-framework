# Final focused charged-ground-dynamics source review

Disposition: PASS. No material integration fix found. This is a scoped source review, not a formal audit. Root authorship preserved; repository unchanged.

The canonical note states the actual finite-native asymptotic claim with the required geometry and limit: even fixed M>=4, even fixed open column height L>=6, positive Jz and Jx=Jy=lambda Jz, lambda tending to zero. It explicitly distinguishes this from growing periodic cubes. The stronger native claim is supported by the two finite-dimensional analytic reductions and independent hierarchy report, rather than inferred from the numerical coefficient-model replay.

The first reduction includes the entire aligned-column block; the second divides by lambda^4 and isolates the plaquette-positive block. The degree-versus-denominator bound accounts for grouped events, extra events and higher diagonal insertions. Equality requires exactly M/2 minimal nearest-neighbor pair events in a row or column perfect matching. The positive L-4 factor is essential and is secured by L>=6. The first nonscalar coefficient cannot be changed by near-identity gauge rotations because all earlier ground-block coefficients are scalar. Fixed sizes are indispensable; no uniform growing-array threshold is supplied or implied.

The earlier pair-compression error is corrected: a single pair event creates plaquette defects, and its direct P+ compression vanishes. The two matching families, defect cost 8K per occupied run, and inverse-run sum binom(2n-2,n-1) produce the stated negative row-flip amplitude. Both the independent matching and hierarchy reports support this coefficient. For M=4,L=6 the arithmetic is K=5Jz lambda^4/32, t=Jz lambda^6/32, tau=t^2/(2K)=Jz lambda^8/320, and 4tau=Jz lambda^8/80.

The regular row/column character representation has the single total-product relation. Thus positive tau gives a unique all-plus leading ground character and a first allowed two-character-flip gap 4tau. At fixed finite dimensions the o(tau) remainder preserves the unique ground and yields the stated actual native leading gap. A local Z toggles one row and one column character with limiting amplitude one, so its particular low-line weight tends to one. This does not require all excited two-flip character lines to remain exactly degenerate beyond leading order.

The charged/neutral distinction is accurate. Local Z is charged under the corresponding x and y planes; translated Z correlations in the invariant ground state are confined to a vertical column. A neutral longitudinal distance-two diagnostic cannot connect distinct characters in the one-state-per-character ground band, exactly, not merely at leading order. Open longitudinal boundaries preserve the plane algebra used here; the separately linked charge note uses periodic cubes for its earlier band construction, but its local charge selection proof also applies to this open-column geometry. The canonical note does not import the periodic-cube gap estimate into this different limit.

Runner inspection confirms a 16-column coefficient model, not a 96-spin diagonalization. Its 512 representatives gauge-fix one row and column; the two characters differ by the gauge factor a[0], exactly the character toggle reached by Z00. The Z00 matrix element between those representatives is therefore the displayed vector overlap. Exact rational recursion checks n=2,...,14. Output ratios, weights and residuals agree with the note. These two-sector computations measure the selected charged sector splitting; they are not an independent exhaustive finite-t/K global-gap certificate. The analytic asymptotic character argument supplies the gap conclusion, which is adequate for the stated claim.

Source hierarchy and limits are clear: supplied Hamiltonian, anisotropy and finite geometry; derived asymptotic ground dynamics and local-spin coupling; numerical development controls; no empirical calibration, uniform large-size limit, isotropic scalar identification or cosmological conclusion. The explicit prior-art attribution appropriately avoids claiming discovery of compass subsystem symmetry.

No expensive replay was needed: the existing independent arithmetic/hierarchy checks were reused, and the canonical source, runner bindings and frozen result were inspected directly. This review does not independently re-prove the imported native K and t coefficients.

## SHA256 identities

- `docs/NATIVE_CHARGED_GROUND_DYNAMICS_NOTE_2026-10-18.md`: `a8d4c82b8c56cd01cbd2bd0d5f78814cb295853c1cda5c6bacf5ac1c4d86373d`
- `scripts/native_row_tunneling.py`: `c0fb74963a0ab1dc958fee0436fb8bff3b4a3fc7c1369a9478fd04e504defc14`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/HIERARCHICAL_ROW_TUNNELING_PROOF.md`: `9190455e97facf549b92d26141703fcac9d5a37cd53d54c24f3e4c6c2118e082`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/PLANE_CHARGE_MOBILITY_PROOF.md`: `190c5eb5633da814c19627a0f6ed4c390c4b55eb95ffafcc24a43bd1ce56c7a5`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/INDEPENDENT_HIERARCHICAL_NATIVE.md`: `2d8c3aa2a59cbe3ceaaa80eaacb3d47d3f64e60f79e429af5857c7c4369e9de8`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/INDEPENDENT_ROW_TUNNELING.md`: `09ab7c70b99e4a8d424053fabe49bd8947323c07b234f65757b707666f4c3955`
- `outputs/native_row_tunneling/result.json`: `d1711cf3f7d9dc80cbeac6655ab5484018c61095512336735c89300afe6703e9`
