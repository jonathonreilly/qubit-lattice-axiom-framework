"""B26 skeleton enumeration for the enlarged palette.  Tokens: S^p (p=+-1,+-2), R (=R_L), Rt (=A0 R_L A0^-1), o (on-site slot).
Even-A words map to these tokens with the same length (A_a X A_b Y = -S^-a X~ S^b Y, X~ = A0-dual).
Reduction to the OLD palette: Rt -> -S R S^-1; merge adjacent S powers cyclically; canonical = min cyclic rotation, modulo
A0-duality (S^p -> S^-p, R <-> Rt, palette -> palette).  A skeleton is NEW if its reduced canonical class differs from every
skeleton screened in B20/B23 (SKEL1, SKEL2, SKPI6, SKTASTE) and n_S != 0 (n_S = 0: zero k* velocity by L1)."""
import itertools
SP = {'S': 1, 'Si': -1, 'S2': 2, 'S2i': -2}
def expand(sk):
    out = []
    for t in sk:
        if t == 'Rt': out += [1, 'R', -1]
        elif t in SP: out.append(SP[t])
        else: out.append(t)
    return out
def reduce_cyc(seq):
    seq = list(seq)
    changed = True
    while changed and len(seq) > 1:
        changed = False
        # merge adjacent ints (cyclic) and drop zeros
        for i in range(len(seq)):
            j = (i + 1) % len(seq)
            if i != j and isinstance(seq[i], int) and isinstance(seq[j], int):
                v = seq[i] + seq[j]
                if j > i: seq = seq[:i] + ([v] if v else []) + seq[j + 1:]
                else: seq = ([v] if v else []) + seq[1:i]
                changed = True; break
        if changed: continue
        for i in range(len(seq)):
            if isinstance(seq[i], int) and seq[i] == 0: seq.pop(i); changed = True; break
        if changed: continue
        # R R -> 1 (involution) cyclically
        for i in range(len(seq)):
            j = (i + 1) % len(seq)
            if i != j and seq[i] == 'R' and seq[j] == 'R':
                seq = [x for t, x in enumerate(seq) if t not in (i, j)]; changed = True; break
    return seq
def canon_seq(seq):
    if not seq: return ()
    rots = [tuple(seq[i:] + seq[:i]) for i in range(len(seq))]
    return min(rots, key=lambda t: tuple(str(x) for x in t))
def dual(sk):
    m = {'S': 'Si', 'Si': 'S', 'S2': 'S2i', 'S2i': 'S2', 'R': 'Rt', 'Rt': 'R', 'o': 'o'}
    return tuple(m[t] for t in sk)
def canon(sk):
    return min(canon_seq(reduce_cyc(expand(sk))), canon_seq(reduce_cyc(expand(dual(sk)))), key=lambda t: tuple(str(x) for x in t))
def nS(sk): return sum(SP.get(t, 0) for t in sk)
OLD = [('S', 'o'), ('S', 'R', 'o'), ('S', 'o', 'R'), ('S2', 'o'), ('S', 'S', 'R', 'o'), ('S', 'R', 'S', 'o'), ('S', 'R', 'Si', 'o'), ('S', 'R', 'S', 'R', 'o'),
       ('S', 'o', 'S', 'o'), ('S', 'o', 'Si', 'o'), ('S', 'o', 'R', 'o'), ('S', 'R', 'o', 'R', 'o'), ('S2', 'o', 'S2', 'o'), ('S2', 'o', 'S2i', 'o'),
       ('S', 'R', 'o', 'S', 'R', 'o'), ('S', 'R', 'o', 'Si', 'R', 'o'), ('S', 'o', 'S', 'R', 'o'), ('S', 'o', 'Si', 'R', 'o'), ('S', 'R', 'o', 'S', 'o')]
OLDC = {canon(s) for s in OLD}
TOK = ['S', 'Si', 'S2', 'S2i', 'R', 'Rt', 'o']
def generate(maxlen=5):
    seen = {}
    for n in range(2, maxlen + 1):
        for sk in itertools.product(TOK, repeat=n):
            no = sk.count('o')
            if no not in (1, 2) or 'Rt' not in sk: continue
            if sk[-1] != 'o': continue                         # rotate so the word ends in a slot (cyclic class rep)
            # raw-word hygiene: no adjacent S-tokens (they merge), no RR / RtRt / oo (cyclic)
            bad = False
            for i in range(n):
                a, b = sk[i], sk[(i + 1) % n]
                if (a in SP and b in SP) or (a == b and a in ('R', 'Rt', 'o')): bad = True; break
            if bad or nS(sk) == 0: continue
            c = canon(sk)
            if c in OLDC: continue
            # reduced n_S must be nonzero too (it is the conserved total power)
            seen.setdefault((no, c), sk)
    return seen
if __name__ == '__main__':
    g = generate()
    one = [v for (no, c), v in g.items() if no == 1]; two = [v for (no, c), v in g.items() if no == 2]
    print(f"new reduced classes: 1-slot {len(one)}, 2-slot {len(two)}")
    for v in sorted(one, key=len): print('  1', v, '->', canon(v))
    for v in sorted(two, key=len)[:400]: print('  2', v, '->', canon(v))
