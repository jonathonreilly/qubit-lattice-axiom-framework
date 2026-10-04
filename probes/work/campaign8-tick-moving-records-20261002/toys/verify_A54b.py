"""Threshold growth for Lemma G in 2D: smallest range^2 at which charge-parity-dressed local fermionic hops exist."""
import signal
signal.alarm(280)
from verify_A54 import scan
for L, r2s in ((6, [5, 8, 9, 10]), (7, [4, 5, 8, 9, 10, 13])):
    res = scan(2, L, r2s)
    first = next((r for r in r2s if res[r]), None)
    print(f"2D L={L}: {res} -> smallest solvable range^2 {first}")
