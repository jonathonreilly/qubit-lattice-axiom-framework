# Review History — microcausality many-body lightcone block01 (2026-07-18)

## Round 0 — supervisor work
Pre-battery caught a real physics subtlety before authoring: the first
test Hamiltonian (all-X chain) is commuting and the cone is never reached
— adopted as the T2 stall exhibit rather than discarded; the generic
instance re-chosen (X1X2 + Z2Z3). Supervisor-authored 16-gate runner. A
weak T2 mutation probe (H-swap invisible to the Z3 probe because the
arriving operator commutes with it) was caught and the T2 gates hardened
with the X3-probe conjunct; eight mutation families then all FAIL
correctly (L1, T1, T2-swap, T2d-mechanism, T3a, T3c, N, plus the
hardening re-probe).

## Round 1 — combined adversarial lens: 2 blockers / 2 major / 1 minor
ALL accepted as narrowings (core survives):
1. BLOCKER: "finite-speed" overclaim — the constant c = 2JM is
   region-level, not volume-uniform; T3 retitled finite-volume
   factorial-tail bound, LR-closure language removed, M = |E(Λ)| defined.
2. BLOCKER: "closes the many-body slice" overclaim — the cited task is
   the many-body fermionic transfer-matrix/LR lightcone with the
   quasilocal-composition step; rescoped everywhere to "a conditional
   finite-range spin lemma relevant to, but not closing, the named task."
3. T1 quantifier corrected to "zero of order at least d" (T2 itself shows
   why exact order can fail). 4. The tensor-product algebra and
   Heisenberg convention declared as supplied hypotheses (sign of (i)^k
   confirmed by the lens under that convention). 5. Minor label fixes;
   N8 echo dropped. BONUS adopted: the lens proved T2 is all-order
   (ad_H^k A = ad_{h12}^k A via the commuting collapse) — T2 strengthened
   with the identity note-carried.

## Disposition after fixes: pass
Post-fix runner `TOTAL: PASS=16 FAIL=0`; needle synced to the corrected
T1 wording; cache SHA re-pinned; quotes verified both directions.
