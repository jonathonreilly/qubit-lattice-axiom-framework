"""C8 skeletons for the class-3 screen: words in S^{+-1}, S^{+-2}, R (=R_L), Rt, E+- (= exp(+-i pi/4 R_L)) and on-site slots o.
Hygiene (cyclic): no adjacent S-powers (merge), no RR / RtRt / oo, no E next to E or R (E+E+ = iR, E+E- = 1, E+R = iE-).
At least one E letter, n_S != 0 (n_S = 0: zero k* velocity by the extended L1), 1 or 2 slots, word ends in a slot.
Classes: cyclic rotation and complex conjugation (E+ <-> E-, slot -> conjugate slot; PC is conjugation-closed up to phase)."""
import itertools
SP = {'S': 1, 'Si': -1, 'S2': 2, 'S2i': -2}
TOK = ['S', 'Si', 'S2', 'S2i', 'R', 'Rt', 'E+', 'E-', 'o']
def nS(sk): return sum(SP.get(t, 0) for t in sk)
def bad_pair(a, b):
    if a in SP and b in SP: return True
    if a == b and a in ('R', 'Rt', 'o'): return True
    if (a[0] == 'E' and (b[0] == 'E' or b == 'R')) or (b[0] == 'E' and a == 'R'): return True
    return False
def canon(sk):
    cands = []
    for w in (sk, tuple({'E+': 'E-', 'E-': 'E+'}.get(t, t) for t in sk)):
        cands += [tuple(w[i:] + w[:i]) for i in range(len(w))]
    return min(cands)
def generate(maxlen=5):
    seen = {}
    for n in range(2, maxlen + 1):
        for sk in itertools.product(TOK, repeat=n):
            no = sk.count('o')
            if no not in (1, 2) or sk[-1] != 'o' or not any(t[0] == 'E' for t in sk) or nS(sk) == 0: continue
            if any(bad_pair(sk[i], sk[(i + 1) % n]) for i in range(n)): continue
            seen.setdefault((no, canon(sk)), sk)
    return seen
if __name__ == '__main__':
    g = generate()
    for no in (1, 2):
        v = [x for (n, c), x in g.items() if n == no]
        import collections; print(no, len(v), collections.Counter(len(x) for x in v))
