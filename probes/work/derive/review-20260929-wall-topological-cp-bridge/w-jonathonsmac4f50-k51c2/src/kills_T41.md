# Kill check on T41

Checker: Claude Sonnet 5.5 (same family as attacker; same-family check only). Read the axioms memo in full and `PRIMITIVE_REGISTRY_CHECK.md`. Re-ran `t41_test.py`: identical results. Scratch: `kills/T41_scratch/kill_checks.py`.

## Outcome verdict
WEAKENED. T41 is a real open gate (no open PR or note closes it). S1 and S2 are correct. "MISFRAMED" overreaches: it is the lane's own W7 status stretched over the cluster, the cheaper question is not cheaper, and the plain verdict is broader than the evidence. Better label: STANDS, priced at "quark block is K-real (Hermitian)" plus exhaustion.

## Route verdicts
| Route | Verdict | Reason, with evidence |
|---|---|---|
| R1 index first | wounded | Rests on unproved exhaustion (P2 note premise (ii); W7). Repo already has a 2D nonzero-index supplier (`THETA_SUPPLIER_FLAVORED_GRADING_SPECTRAL_FLOW...2026-07-02`), uncited. S3 support is tautological. |
| R2 parity plus positivity | wounded | Agree. Citations are correct. Needs an improper symmetry, so it is the orientation bit (T23). |
| R3 build the carrier | wounded, not dead | Carriers are Hermitian by construction, which supplies K-reality. The imported constant c12_u fixes the sign bit: arg det(M_uM_d) is pi at c12_u=0.9 and 0 from 1.0 to 1.48 (K3). "Carriers lack the datum" is wrong. |

## Errors found
1. **Plain verdict overgeneral.** "Phase couples to nothing; no lepton input" holds only for the epsilon-twisted graded coupling (S2: tr eps=0, taste-nonsinglet). In the repo's own coupling K(x)1+1(x)A, a generic complex A gives a live phase on the same balanced surface (S1 info line: -1.80 rad; K2: -2.24 rad, against 0.0 for the graded form). `THETA_MASS_ORIENTATION...2026-07-01` T6 and `THETA_MASS_SIDE_EPSILON_HERMITICITY...2026-06-11` (checks 7-8) say this. The 06-11 note calls K-reality "the same C3 K-real structure" as the lepton selection. That is the cross-sector identification. Neither note was cited.
2. **S3 cannot fail.** Class readouts depend on |det| by definition; any rephasing keeping singular values passes (K1: 3e-14). Only the toy p_nu weight has content, and it is non-framework.
3. **S4 is not a test.** Eigenbasis sign flips leave M M-dagger identically fixed (K4: 1e-15).
4. **S5 tests too much.** A Hermitian block has real det, so det-channel K-constancy is automatic for any Hermitian carrier (K3). The J sign flip is ordinary CP violation.
5. **Label.** "Proved" for the forcing pairs (KCPT note:89-116) uses Record finite additivity, removed 2026-08-13 (`MINIMAL_AXIOMS:220-224`). Correct label: conditional, unaudited.
6. **Cluster.** W7 (interface, exhaustion) is a different wall; the MISFRAMED reading is its own "possibly misframed" status.
7. **Cheaper question.** "Does the lattice supply tr(eps)≠0?" is the T42/T43 supplier wall.

Fine: the disclosed run 1 comparator fix; the S2 algebra is exact for balanced B.

## Corrected plain-language verdict
The open obligation stands. Showing quarks share the leptons' counting channel shows only that record readouts cannot see the mass phase. That gives zero phase only if readouts are the sole place the phase acts, which is the separate exhaustion wall. On the balanced surface the phase is inert only for the epsilon-twisted coupling. For the repo's own flavor coupling it vanishes only if the quark block is Hermitian, the premise this wall asks to derive; the atlas quarks supply it and their sign bit by hand.
