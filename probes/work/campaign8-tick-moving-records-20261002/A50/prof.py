"""A50 prof: time one evaluation of the search objective (C2z, axis window)."""
import signal, sys, time
signal.alarm(120)
sys.argv = ['x', 'C2z', 'axis', 'T', '0']
t0 = time.time()
exec(open('t2_search.py').read().split("print(\"group %s")[0])
t1 = time.time()
br = [0] * len(struct); p = rng.uniform(-3, 3, size=npar)
t2 = time.time()
for _ in range(20): sd = seeds_of(p, br)
t3 = time.time()
for _ in range(20): A, L = FH.arrays(sd)
t4 = time.time()
for _ in range(20): r, th = evaluate(sd)
t5 = time.time()
print("setup %.3f s; seeds %.2f ms; arrays %.2f ms; evaluate %.2f ms; residual len %d" %
      (t1 - t0, (t3 - t2) * 50, (t4 - t3) * 50, (t5 - t4) * 50, len(r)))
