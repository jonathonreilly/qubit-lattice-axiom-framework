# la55_1 — exact-arithmetic checks of constants re-derived in LANEA55 (criteria written before the script)
Written 2026-10-29 UTC, before checks/la55_1_constants.py exists. Plain python, fractions.Fraction / integers only; no floats
in any verdict.

Each sub-check prints PASS/FAIL with the exact values. PASS criteria (pre-registered):
- C1 (LE far part, my count): 4*3*80*2*(8/7)^5 is < 3744 and < 10^4.  FAIL otherwise.
- C2 (LE far part, source's count): 2592*(8/7)^5 < 5054 and < 10^4.  FAIL otherwise.
- C3 (shell count): (2t+1)^4 - (2t-1)^4 == 64t^3 + 16t and <= 80t^3 for every integer 1 <= t <= 2000 (identity also checked as a
  polynomial by coefficient comparison).  FAIL on any t.
- C4 (tail): sum_{t>=n} 1/t^2 <= 2/n, checked as: the partial sum up to 10^5 plus the rigorous tail bound 1/(10^5 - 1) is <= 2/n for
  n = 1..200 (exact rationals).  FAIL on any n.
- C5 (U4' bootstrap): 48*(41/20)^5 <= 1738 and 1738*2 == 3476.  FAIL otherwise.
- C6 (LR-pot / FP arithmetic): 3 + 72 == 75; 75 + 8*10 == 155; 8*1 == 8; 8*5 == 40; 5*155 == 775; 5*8 == 40; 5*40 + 5 == 205;
  775 + 205*(3/2) <= 1083 (L >= 3 so L/(L-1) <= 3/2).  FAIL otherwise.
- C7 (Lemma Λ): for L in {3,5,7,9} and k = 1..12: 10*L*(L-1)*sum_{i<k} L^(k-1-i)*L^(2i) <= 10*L^(2k).  FAIL on any (L,k).
- CONTROL (designed to FAIL, proves the harness can fail): assert 48*(41/20)^5 <= 1737 — must print FAIL.
The script exits non-zero if any non-control check fails or if the control does not fail.
