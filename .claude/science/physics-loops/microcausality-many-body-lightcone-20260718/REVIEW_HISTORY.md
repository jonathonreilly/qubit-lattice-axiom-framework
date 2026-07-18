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

# Block02 review history (2026-07-18)

## Round 0 — supervisor work
Pre-battery 8/8 (multinomial expansion, dead sequences, unique reaching
sequence at k=2, later-step death on 4 sites, Z^3 bond-adjacency degree
10). Two exact discoveries during battery/authoring: (i) the planned
walk-adjacent count is NOT what the plain multinomial gives — the honest
Taylor-level count is accumulated-support, volume-uniform per coefficient
and on a certified local time window only (all-time uniform stays open);
(ii) the k=3 commutator vanishes sequence-by-sequence against EVERY
site-3 probe — a full support retreat with k=4 re-arrival (order-parity
breathing), adopted as the upper-bound-not-equality exhibit.

## Round 1 — combined adversarial lens: 0 blockers / 4 major / 2 minor
ALL accepted; one finding STRENGTHENED the theorem:
1. W5's ratio needed the recurrence N_{k+1} <= 6(m+k)N_k stated and
   proven (unique-prefix extension) with zero-term/t=0/J=0 cases —
   ADDED, recurrence gated on the chain (N1=1, N2=2 exact).
2. "Volume-uniform"/"local data only" required the family-level J_*
   hypothesis — inventory stated explicitly everywhere.
3. N1 contained two false routes (lens's independent enumeration matched
   the runner: k=2 X3/Y3 register, Z3 silent; k=3 all silent; k=4
   re-arrival) — rewritten truthfully with orders > 4 named untested.
4. The strengthened body claim (every sequence vs every probe) was
   under-gated — now each k=3 term is gated against both X3 and Z3
   (generating the site algebra) and Y3 at k=2 is gated.
5. STRENGTHENING adopted: a touching bond adds at most ONE new site —
   count improved to prod 6(m+j), ratio (m+k)/(k+1), monotonicity for
   ALL m >= 1 (the m'=2 absorption deleted).
6. Frontmatter window synced to the body's certified sufficient window.

## Mutation checks — ten families, all FAIL correctly
W1 (expansion weight), W2 (later-miss flip), W3 (pair bond count),
W3c (recurrence factor), W4a (inequality direction — chosen after a
slack-bound probe lesson), W4c (retreat flip), W4b2 (Z3 silence flip),
W5 (monotonicity constant), W5a (m>=1 form), N (needle).
Unmutated: `TOTAL: PASS=19 FAIL=0`; cache SHA-pinned, exit_code 0.

## Disposition after fixes: pass
