import sys, pickle
sys.argv = [sys.argv[0], '4', '0']
src = open('rev_A2_TIsearch.py').read().split("found = None")[0]
exec(src)
perm = pickle.load(open('TI_ordering_L4.pkl', 'rb'))
S = build(make_order(perm)); kap, bare = loopdata(S, list(range(nV)))
print("TI ordering L=4, index labels: #sigma=-1:", sum(s == -1 for s in sigmas(bare)), "; -I:", contains_minus_I(bare))
print("kappa per type (#-1/total):", {t: (sum(1 for (tt, _), k in zip(faces, kap) if tt == t and k == -1), sum(1 for tt, _ in faces if tt == t)) for t in TYPES})
