# Narrow status and exact-mutation supplement

This is an affected-source supplement to the unchanged canonical review and conformance supplement. Root remains author. No ODE, aggregate, exact-control suite or variant was run by this checker. It is not a formal audit or publication approval.

## Complete affected scope and identities

I froze and read the complete note delta from `020558ea3f1f41928a485ef19421ebf25a05188a0de4c292c10fc11d6d19d37e` to **`dde833e8bcb69f4ab5e03eb911aa534dbf23647d5fb03cd1be469bac2e977122`**. The change is only the top-level proposal status plus the six-line mutation-accounting paragraph. No equation, supplier gate, necessary/sufficient claim or matter-solution qualification changed.

I read all 62 lines of `mutation_supplement_v1.py`, SHA **`37ac6013dd644f727508f0884f5b42bd629d3aa750cb70ec38bca868e69b2b21`**, all 43 lines of `MUTATION_SUPPLEMENT_FREEZE_v1.json`, SHA **`deab562eb71510c11a6d5095f87101256a2ecb690162697accd4222c9c81a5aa`**, and all 64 lines of `MUTATION_SUPPLEMENT_RESULTS_v1.json`, SHA **`b19746508248d42a39b8c711a07d53129dd722b52d2d76d6905475788df0c1a7`**. Immutable copies and the exact note diff are preserved in this directory.

## Status and retained scientific scope

`Status: proposed_retained` is a proposal label. The actual current surface remains explicitly `conditional-support`, the machine block remains upstream support, effective retention still requires later independent audit, and bare retained status remains disallowed. The change therefore does not assert current retained-grade authority or empirical confirmation. The earlier necessary/sufficient metric/scalar characterization and separate matter-theory premise continue unchanged.

## Five variants and their recorded failures

The supplement makes exactly one declared replacement in the unchanged scientific helper for each variant, writes and hashes the variant before execution, and its subprocess driver calls only `exact_controls()`. It does not run the synthetic ODE or the full aggregate. Failed exact identities are printed before a driver assertion. Timeouts, other exceptions and surviving variants are classified separately.

I mechanically reconstructed each variant from the frozen helper plus its one declared replacement, checked that the source match occurs exactly once, and compared the reconstructed hash with the freeze, result record and actual variant file. All five bindings match. `STATUS_MUTATION_BINDINGS_v1.json` records each comparison. This was byte manipulation only; none of the variant modules was imported or executed.

| Variant | Receipt's failed identity | Why the intended wrong expression is nonzero |
|---|---|---|
| Bianchi matter trace | `Bianchi_scalar_equation_nonzero_Fdot` | Replacing `-(rho-3p)` by `-(rho-p)` leaves residual `-2p` in the otherwise zero identity. |
| Tensor endpoint orientation | `smooth_endpoint_telescope` | The reversed first factor leaves `(Fmid-Fsrc)/sqrt(Fsrc Fobs)` for positive coefficients. |
| Sharp-interface transmission | `sharp_interface_flux_conservation` | Using `2Fmid/(Fsrc+Fmid)` leaves flux residual `4Fmid(Fmid-Fsrc)/(Fsrc(Fsrc+Fmid))`. |
| Transverse potential force | `transverse_x_stationary_equation` | Doubling the x-squared term leaves `k x exp(-(1-k)u/alpha)` against the required force. |
| Transverse kinetic factor | `background_geometric_coupling_distinction` | Halving the extra transverse stress leaves `-2F^2 Tperp/Fdot^2` against the exact coupling relation. |

These are nonzero expressions on generic allowed inputs, so the reported rejected identities correspond to genuine wrong formulas rather than setup errors. Every new result record reports exit1, the expected single failed identity, and the driver's `AssertionError: scientific control rejected variant`. No new survivor, timeout or other exception appears in the five receipts. This verifies receipt/source correspondence, not an independent rerun.

The new paragraph accurately adds five assertion rejections to the previously reported fourteen variants: seven previous plus five new assertions give twelve, alongside six domain refusals and one arithmetic exception, nineteen total. I did not revalidate the original fourteen receipts in this narrow pass; that subtotal is the unchanged prior evidence. The note continues to exclude the arithmetic exception from an independently decisive mathematical rejection. The variants test these exact-identity families; they do not establish universal test completeness, empirical predictivity or quantitative numerical accuracy.

## Unchanged bindings and limits

The scientific helper remains `1bf2d30207b99cea8508a612a739ed8b82dc7d6860920e101fb4e1374eccd9be`; primary `810882ad6271e53e5275905540beedcfc87ec963ac84e559d17c07006150ed0e`; checklist `0cb89a9f341c5e1db27d7a67b4b8a063626522659b6700210565e27c276de329`; protocol `7f504a86f3e82cbcc7129ba7c2233b044430e70b7ede1ad82564c298f9ea3ab1`. All were hash-checked against the reviewed versions.

No new discrepancy was found in this limited delta and mutation-source/receipt comparison. The original independent derivation and 42 controls are separate and unchanged. No cache, live index, staged inventory, archive, Git state, external source, observation or other campaign evidence was examined here. All writes are confined to this checker's directory. A later mechanical delivery binding remains a distinct task.
