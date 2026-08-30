# Block26 independent preexecution attack and repair ledger

No reviewer executed the target `main`. Three independent read-only attacks
returned `UNSAFE` on the first draft. Their objections and the preexecution
repairs are recorded here rather than overwritten.

| attack | first-draft finding | repair before first execution |
|---|---|---|
| runner/input binding | untracked source; no independent source pin; mutable/transitive packet surfaces omitted from the declared input list | add a separate post-commit `RUNNER_SOURCE_PIN.md`; include literal Block23/24/25 dependencies plus Block26 state, claim, no-go, panel, review, amendment, and static-attack surfaces in `AUDIT_INPUT_PATHS`; keep the pin itself outside that fingerprint to avoid self-reference and verify it inside the runner |
| finite tensor theorem | finite-size toy products and an unbound two-qubit order check did not warrant arbitrary finite language | bind the imported 1,176-branch local CPTP certificate to a symbolic positive-`n` induction, arbitrary-reference coefficient identity, and literal branches on disjoint complete carriers |
| pair/triangle symmetry | triangle source labels did not rotate; grant invariants were stored | use source labels `(e1,e3,e2)`, compare complete constraint maps and Locked words under the symmetry, enumerate all bit strings, and mutate a frozen source label |
| abstract owner qubits | valid one-hot algebra was not a lattice Record or append channel | demote it to a kinematic coupling control; forbid it from carrying the physical terminal |
| q=1/4 positive | only 2D effects and stored writer counts were checked | construct descriptors from the literal append branches plus both STOP families; derive the effect spectrum, success Locked-owner decoding, QND/debit/covariance, at-most-one append, maximal scalar residual, and a physical double-append mutation |
| singleton restriction | hard-coded routing table did not define a channel | construct four orthogonal commuting old-current-Record sectors and route complete literal channels on those direct-sum sectors; mutate the singleton to the attenuated raw mixture |
| common-target clique | pointer claim/grant words occupied the exact Blank shell and no physical Kraus family was present | remove the incompatible staged pointer claim; for every separately supplied nonempty subset and every stored label, use the `1/k` convex mixture of complete literal channels, retain STOP off-sector, and require exact-one Locked success on the declared all-valid/common-Blank sector |
| overclaim/no-go discipline | no written N1--N8 resolution and several answer toggles | land the full written N1--N8 analysis; because the stochastic steelman succeeds, mark the negative gate `FAIL`, remove the negative terminal, retain the deterministic enumeration only as a diagnostic, and mutate physical branch/STOP/QND/source/routing and terminal structures |
| derived-witness integrity | one no-write value, the maximal scalar, and two stdout witnesses were assigned rather than derived | remove the redundant value; derive the maximal scalar from the computed projector-sum spectrum and its PSD boundary; print the grant and renewal witnesses returned by the enumerations and carrier intersections |

The amendment intentionally does **not** claim that the axioms derive the
equal collision weights, the supplied claimant subset, invocation, physical
occurrence, renewal, Blank production, rate, retention, obligation
retirement, or TOE movement.

**Recheck status:** three independent static scopes returned `SAFE` on source
SHA `fa944ecc0e4528f3995e968f91808df7214008168c68268a444601c58015ebfa`,
conditional only on refreshing the frozen packet hashes and writing the
separate post-commit source pin. No reviewer imported or executed the target.
First target execution remains forbidden until those two mechanical gates are
complete.
