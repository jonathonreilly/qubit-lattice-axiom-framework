# Current checkpoint

Updated 2026-10-16T14:55:26.551420+00:00. Proposed sparse compiler source is complete and ready for root review; parent and extension acceptance remain pending.

For n=L+3q, d=2^q, p=d(d-1)/2 and a_count=L+q+1, the proof gives G0=a_count*[p*(152T(n-2)+68(q-1))+152T(n-1)], where T(1)=1 and T(k)=2T(floor(k/2))+2T(ceil(k/2)). Spatial full-SWAP routing gives Gbar=(2n-1)G0, explicitly bounded by K_q L^4. The exact logical isometry uses one clean ancilla and phase one. Selected support is a_count*d, with the V-dependent minimal support separately identified.

All gates use the prior positive local alphabet. Fixed-slot padding gives nominal tau=(Gbar+1)h, hence O(epsilon^-4) at fixed q. The optional pulse-start-error model adds two idle guard slots and prices complete timing history, without changing the exponent. Quantum duration begins with a supplied ready state and compiled schedule; no efficient classical synthesis or preparation bound is claimed. Actual physical and arithmetic precision requests, global versus per-site errors, scalar phases, energy and drive-work qualifications are explicit.

One exact finite scientific source executed after one preserved preexec launcher failure. Source-at-launch SHA256 is 2ede311427e4e765dfa0f75ac3ad7feeb4af31f5873f42a5bb1c787216c7d565. The successful source completed with exit zero; the wrong-adjoint and omitted-inverse mutants had exact squared residuals 16 and 32/5. Full source, launchers, argv/cwd, limits and streams are retained. General theorem and timing extension are analytical, not proved by the finite example.

Parent identities/read coverage and exposure are in SOURCE_MANIFEST.json and AUTHOR_CHECK_AND_EXPOSURE.md. PRECHECK_FINDINGS.md preserves the earlier provisional checkpoint without claiming a pre-run cryptographic freeze. The root proposal and review directories remain unread. No prior packet or canonical/Git/PR/audit/cache/lock/prompt/axiom surface changed. The next decision is independent proof/count/interface review, including an optional emitted end-to-end word; no such full compiler run is claimed.
