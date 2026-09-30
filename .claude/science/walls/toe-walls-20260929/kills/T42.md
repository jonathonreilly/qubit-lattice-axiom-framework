# Kill check on T42

Checker: Claude Sonnet 5.5, same vendor family as attacker and supervisor (same-family check, not independent). Scratch: `kills/T42_scratch/`.

Re-runs: `census.py`, `parity.py`, `comm_id.py` reproduce the attack outputs exactly. `mc.py` reproduces at new seeds (4^4: <P> 0.5968; 6^4: 0.5926; anchor 0.5934); plaquettes below 0.25 are 2e-5 to 3e-5, none below 0.1.

## Outcome verdict
WEAKENED. PRICED at a non-negativity premise stands. But the route table misses prior art, the argument against the licence is unsupported, and the price is one premise short.

## Route verdicts
| Route | Verdict | Reason, with evidence |
|---|---|---|
| R1 records-Gibbs | wounded (verdict kept, evidence wrong) | The abelian identification exists: `docs/U1_AUXILIARY_FACE_LOCAL_CONDITIONALS_UNCONDITIONAL_GAUGE_MEASURE_...2026-09-03.md` and `docs/U1_ROLE_ENCODED_DOUBLED_INCIDENCE_NEAREST_NEIGHBOR_GAUGE_LAW_...2026-09-03.md`. Link sites carry values, face-role sites carry an auxiliary possibility, and the link marginal is prod T(Phi_f) with T > 0. "Role sites hold no records (09-04 note)" has no path; I found no such note and the 09-03 notes say the opposite for faces. Test D (0/24) is on the undoubled lattice and misses this. Open: SU(3) (T27), T supplied, 4D/time (T15). |
| R2 improper symmetry | wounded (agree) | Vafa-Witten is mis-cited: its proof uses a positive Euclidean measure, so it supports the non-negativity reading. |
| R3 misframed | survives | It is the lane's own "cheapest test" (L11-W1), not new. It needs reflection positivity too (error 3). |

## Errors found
1. **Union argument unsupported.** "Second-order generation of E.B: suggested" fails in my run (`gen_parity_check2.py`). Abelian star-pair E.E plus sum of cos P: the per-cell density of i[H1,H2] has 12 classes, all E_l sin P with l in P (curl E, total derivative), zero E_normal.sin P classes, and is invariant under all 24 improper elements. P-even licensed inputs stay P-even. "12/12 unions contain an E.B support" is support inclusion only. Non-closure under products is prior art (06-11 narrowing note, section X). The licence's real leak is licensed P-odd star terms (E(iv), E(v), checked), which are irrelevant operators, not theta.
2. **P-odd is not CP-odd.** No C or T parity test of the SU(2) tripod or the abelian degree-6 star.
3. **Price one premise short.** Non-negativity kills the imaginary Euclidean coefficient (theta). A real Euclidean F.Ftilde term is positive, and is imaginary Minkowski theta (non-Hermitian). Only reflection positivity removes it. PREREG said "positive reflection-positive"; the final price says non-negativity alone. Real P-odd degree-6 star terms also pass non-negativity.
4. **Stale label.** The native positive-class note is now `unaudited / awaiting_audit` in the ledger; "retained_bounded, audited 2026-07-05" is history.
5. Checks out: 36 open PRs, none on theta or gauge positivity.

## Corrected plain-language verdict
The strong-force twist angle is zero in the repo only because the weight over gauge histories is assumed non-negative and part of a reflection-positive (Hermitian) theory; that survives averaging. The locality licence is no protector because it allows mirror-odd vertex terms, not because it fails under unions. Non-negativity would follow if force links are records, which the 2026-09-03 U(1) notes already do for a finite abelian plaquette weight. Open: SU(3), the time step, and reflection positivity.
