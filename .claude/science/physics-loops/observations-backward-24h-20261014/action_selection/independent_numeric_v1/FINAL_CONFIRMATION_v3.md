# M12 final source and execution confirmation

This narrow supplement closes the source/receipt portion of `NUMERICAL_REVIEW_v1.md` (SHA256 `c3cfd208126aec9f1c8c27d7e02f663446ce5e58b9616ca69f1d1b2e782149f8`) and its identity `6eb433215c4de492603d44355bbc797602062bfe9368a97b6e06fd4b45c5e268`. Those originals, the independent pre-exposure run and both implementations' failed floating recoveries remain unchanged. No ODE, general inverse, aggregate or raw observation calculation was rerun for this supplement.

I read and preserved the complete affected delta. The note now correctly attributes the 2.962906e6 cancellation ratio to case 9, resolving my earlier prose finding. It also states that conserved-fluid metric/scalar membership does not construct a complete matter solution of S_m. This narrows the converse appropriately. The only helper addition is a nonzero-pressure metric control. Direct substitution into the independently derived formula, with F=2, Fdot=1, H=.5, Hdot=-.25, curvature=.5, rho=.3 and p=.1, gives kinetic stress D=3.1 and V=4.15. The primary is unchanged. Production helper functions are AST-identical to the first reviewed canonical source; only the aggregate's added test block changes. The protocol, cases, epochs and thresholds remain exact originals.

Final source identities:

| Item | SHA256 |
| --- | --- |
| Helper | `1bf2d30207b99cea8508a612a739ed8b82dc7d6860920e101fb4e1374eccd9be` |
| Primary | `df487184eb73a347b1c5c6aacc641d49ea482cac75e2494dac15dcd6d07923ca` |
| Note | `c8e52d53d2e2a4c02bc784668665e7d0c635c208492d32ebe968dd0e73bc8078` |
| Original protocol | `7f504a86f3e82cbcc7129ba7c2233b044430e70b7ede1ad82564c298f9ea3ab1` |
| Final cache | `c7ce3b03682676886b3ccdf3c587492809f6ebc3726c6cccc3122a13796173bd` |
| Final results | `e8a551d346094e7333bbb7ed9ece8b662836b743fd2ba6613b45f082b2875105` |
| Final summary | `5d2935fdc7fb62dfbcf42889ddeff6d870c7255828fd95bd785992b72f41872b` |

`FINAL_INPUT_FREEZE_v3.json` binds nine frozen source/protocol/output/receipt/cache files. Every current file matched its snapshot at the end of the binding check. The source freeze and result input hashes agree. Rebuilding the primary's ordered three-input fingerprint gives `e9c7e049c0fa0019adf66eca16ff1e2ee24f31a51ddca197dfedbe374fef309b`, matching the cache. The execution receipt records fresh status, exit 0, empty stderr, and 1.3328142166137695 seconds of 120. Cached stdout matches receipt stdout and the final summary. Projecting the full RESULTS object exactly reproduces SUMMARY.

All 102 current author controls pass. Relative to the original 91, there are eleven named additions: seven transverse/geometric-coupling controls, the curved and nonzero-pressure metric controls, a repeated-potential-epoch refusal, and the preserved-rounded-input failure control. The source-assembled current case-9 recovery passes, while the canonical rounded-input branch explicitly retains a nu error of approximately 2.5501573e-6, above the unchanged 5e-7 threshold. The original 90-pass/1-fail receipt is not relabeled as a 102-pass execution. My independently frozen errors of 4.8043605e-6 and 6.0835884e-6 remain failures too.

All 204 saved field, velocity and time entries match the exact expected conversion of the author's original float text into 50-digit mpmath values, and converting them back to float recovers the originals exactly. A first binding assertion incorrectly compared those 55-digit printed binary-multiprecision values with exact decimal text. It failed on u=-.6 because conversion tails of order 1e-52 are visible. `BINDING_SERIALIZATION_FAILURE_v3.json` preserves that failed script identity and diagnosis. The new binding checks the precise conversion/serialization rule instead of using an approximate tolerance; no scientific output or tolerance was changed. The final source-assembled recovered parameters differ from my independently assembled ones by at most 5.8117386605208e-41 relative. This is a model-algebra comparison, not a trajectory accuracy or observed-precision claim.

`FINAL_BINDING_RESULTS_v3.json` records the verified receipt and all changed control names. The accompanying `FINAL_IDENTITY_v3.json` binds this report, immutable earlier evidence, source delta, both binding scripts and the preserved serialization failure. This remains a focused computational/source check, not a formal audit, integrated landing approval or independent empirical validation.
