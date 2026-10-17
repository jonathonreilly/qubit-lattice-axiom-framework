exec(open('equiv.py').read().split("if __name__ == '__main__':\n    for t in fixed")[0])
import time, sys
for L in (4, 6):
    t0 = time.time()
    Gp, nq, q, qc = build_cond(L, copy_orders(fixed[0]))
    r, _ = rref_rank(Gp)
    print('full kept group: L', L, 'log2 dim', nq - r, 'rows', Gp.shape, round(time.time() - t0), flush=True)
