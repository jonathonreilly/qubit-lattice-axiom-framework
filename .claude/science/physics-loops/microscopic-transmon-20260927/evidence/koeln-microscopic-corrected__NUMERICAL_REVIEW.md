# Corrected microscopic-transfer independent check

2026-09-27. Read complete protocol, both calibrators, model and input manifests; checked all24 supplied records. No optimizer reproduction. Both manifests match. The unchanged model hash is the previously checked signed sinc(mB/Bnode) construction; ablation changes only the per-harmonic envelope plus required low-level recalibration.

Exactly12 unique expected (rawcase,start) records occur in each family; all calibration vectors reproduce from the source-corrected265-delay Ramsey01 snapshot and unchanged archived12 center. All circuit fits return success. Crucially raw_period_0.15 originates from a raw fit with success=false (150-evaluation limit), while its downstream circuit calibration can fit those supplied numbers successfully. These are different success statements. Keep that family as a nonconverged-raw-calibration diagnostic, not an identified physical input. The.22/.30 raw fits terminate by ftol above gradient tolerance. No03 or12-dispersion observation enters either circuit objective.

Independent selected raw_period_0.3/start.01 spectra were reconstructed by direct rectangular spatial integration (or entire local potential times fundamental sinc for ablation), phase-plane-wave projection and full charge tensor photon diagonalization. No author scientific builder was imported. Cutoffs N22/K12/grid4096/spatial64 and N28/K16/grid16384/spatial128 were used. All selected labels are unique and high overlap. The maximum primary discrepancy over first-three means/full endpoint dispersions is0.000402Hz; maximum independent cutoff change is0.000544Hz.

| Model | Fine mean f03 GHz | Fine full δ03 GHz |
|---|---:|---:|
| spatial | 14.669197761379 | 0.038610901957 |
| ablation | 14.669393228528 | 0.038589338332 |

These checks establish selected finite numerical consistency, not source-pipeline certification, physical uncertainty, a global optimum or microscopic identification. Corrected source membership repairs the specific readout-reference inclusion error. It does not resolve the common-center/parity mapping, geometry, fixed-cavity transfer, finite-drive or drift assumptions. All prior267-sample analyses remain historical and must not be promoted by this corrected review.

Evidence: independent_ablation_check.py, independent_ablation_snapshot.json, independent_ablation_results.json/log and independent_key_controls.json. SHA-256:

- `PROTOCOL.md`: `7925802e312340caa7674328571ebd949c480bcf7481c1b676adf33ad5ecf8ca`
- `calibrate_ablation.py`: `f78cac7c1b59d9c7ab369031f3f8651e0d01dce9e1d72c52d977754d94f6ff96`
- `ABLATION_INPUTS.json`: `d1a7ff0f95b9a74ec9f264d68ff4aa22ed34165ed92e83b18ab7e87df68b467f`
- `calibrate.py`: `87b218627352976b294de063e8f99a754c216b42e8bd6daeb192f6d1f86b45f8`
- `INPUTS.json`: `de0eed867acf8b735de8e9fcd2960c79893ccc1a8d936e3fbc293d2e5d165b42`
- `raw_transfer_fits.json`: `0a8b8b6786c913374895951a0b9908d274130bb0c16d5824ebf1ef12c4182d3e`
- `harmonic_ablation_fits.json`: `71a135379713aa516bd8b75450b3887727d153e728148421d69fe302bef32f65`
- `model.py`: `d9db69aa06122958dc81120c1518ef2e3148a01dfd46a2f1820e0d593eac8cf3`
- `independent_ablation_check.py`: `a935d078f3f9e787e92c0497950e67aa9b3e02a446be43a43e7e8c6631961077`
- `independent_ablation_snapshot.json`: `5c906a9ee288bb31bc32dd203ff4152ce1f841b07c1efae30bc43e2716aac7f6`
- `independent_ablation_results.json`: `8b6e1ad18d6aa4127fae86f68e5b63125e57d31a707ccb00a6f5468f51877502`
- `independent_ablation_check.log`: `9841643c388af7d8db47e7c5827ca9f71bc13ab78f38d175566608ef4b2d8110`
- `independent_key_controls.json`: `f1b841119d7323ad8aafa0e8fab461f08438b12bbf612f10b9938c3d0eeace92`
- `evaluation.json`: `112f3a145c1773cb713bb0b6082d11cc75aba2a2fdfbd5bea4f86cef76b7f334`
- `../koeln-ramsey-reference-corrected/fits.json`: `68fea0a2fd98d9e6d783082f32f629a8b9be62b3269f27ab14312c38df6eb823`
