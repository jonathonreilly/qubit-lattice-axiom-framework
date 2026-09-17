import sys, os, os, random, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, sys.argv[1])
from shape import solve_restricted, MinTree, run_automaton, level, m
random.seed(int(sys.argv[2]))
cases = []
for name, Z in (("Z_A", m.Z_A), ("Z_B", m.Z_B), ("W1", m.W1), ("W2", m.W2), ("W3", m.W3)):
    root, (A_, B_, L_), marks = Z
    st = [(a, b, cc) for a in range(A_) for b in range(B_) for cc in range(L_)]
    cases.append((name, run_automaton(st, {z: 1 for z in marks}), root))
for (A_, B_, L_) in ((4, 4, 7), (5, 5, 8)):
    sites = [(a, b, cc) for a in range(A_) for b in range(B_) for cc in range(L_)]
    n = 0
    while n < int(sys.argv[3]):
        zeta = {z: 1 for z in random.sample(sites, random.randint(3, 16))}
        eta = run_automaton(sites, zeta); ones = [z for z, v in eta.items() if v == 1]
        if len(ones) < 12 or len(ones) > 70: continue
        cases.append((f"rand{A_}{B_}{L_}_{n}", eta, max(ones, key=level))); n += 1
loss = {(c, r): 0 for c in (1.0, 2.0) for r in ("R1", "R2", "R12")}; tested = 0; t0 = time.time()
for name, eta, root in cases:
    mt = MinTree(eta, root)
    for c in (1.0, 2.0):
        r = mt.solve(c)
        if r is None: continue
        base = r["E"] - 3 * (r["S"] - 1) - c * r["A"]
        for rr in ("R1", "R2", "R12"):
            v = solve_restricted(mt, c, set(rr.replace("12", "1,2").split(",")) if rr == "R12" else {rr})
            if v is None or v > base + 1e-9:
                loss[(c, rr)] += 1
                if loss[(c, rr)] <= 2: print(f"   loss: {name} c={c} {rr}: base {base} restricted {v}")
    tested += 1
print(f"{tested} realizations ({time.time()-t0:.0f}s); realizations where a restriction raises the minimum: {loss}")
