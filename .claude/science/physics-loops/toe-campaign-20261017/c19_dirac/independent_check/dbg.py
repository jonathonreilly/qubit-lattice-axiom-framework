import pickle, numpy as np, sys
sys.argv = ['x', '0', '0']
exec(open('search2.py').read().split('res = []')[0])
for fun, t1, x in pickle.load(open('search2_12.pkl', 'rb')):
    H = build(t1, x[0], 10 ** x[1], x[2:]); E = np.linalg.eigvalsh(bloch_batch(H, KG))
    print(t1, x[0], 10**x[1], 'score', score(t1, x[0], 10 ** x[1], x[2:]), 'doublets', doublets(H))
    for lev, Ed in doublets(H):
        print('   lev', lev, (E[:, lev] - Ed).max(), (Ed - E[:, lev+1]).max())
