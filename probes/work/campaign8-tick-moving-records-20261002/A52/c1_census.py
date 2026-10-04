"""A52 c1: GF(2) census of fermionic link decorations at a corner, restricted to the stabilizer of a
record direction f; enumeration of strict invariant tournaments; transport to the full O-orbit."""
import signal, itertools, sys
signal.alarm(100)
import numpy as np
from a52lib import *
sys.path.insert(0, '/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-focused-noyce-9a3983/34c0b720-f781-4af0-9bb7-5d2e1b60d22e/scratchpad/c8/A48')
from a48lib import link_system, GROUPS

def stab_line(f):
    return [g for g in range(24) if act_vec(g, f) in (tuple(f), tuple(-np.array(f)))]

SUB = {
    'O (no record)': list(range(24)),
    'T (12 even)': GROUPS['T (12 even turns)'],
    'C3  = Stab(body diag 111)': stabilizer((1, 1, 1)),
    'D3  = Stab(line 111)': stab_line((1, 1, 1)),
    'C4  = Stab(axis +z)': stabilizer((0, 0, 1)),
    'D4  = Stab(line z)': stab_line((0, 0, 1)),
    'C2' + "'" + ' = Stab(face diag 110)': stabilizer((1, 1, 0)),
    "D2' = Stab(line 110)": stab_line((1, 1, 0)),
    'D2  (three axis half-turns)': GROUPS['D2 (3 axis half-turns)'],
    'C2z': GROUPS['{1, C2z}'],
    'trivial (generic record)': [ID],
}
print("(1) A45 GF(2) system (link decorations at a corner, Gauss-parity switching allowed)")
for name, G in SUB.items():
    res = []
    for stat in ('fermion', 'boson'):
        for sw in (True, False):
            rows, nv, *_ = link_system(G, stat, allow_switch=sw)
            res.append(gf2_consistent(rows))
    print("   %-34s |G|=%2d  fermion(sw)=%-5s fermion(no sw)=%-5s boson(sw)=%-5s" % (name, len(G), res[0], res[1], res[2]))

print("(2) strict tournaments (orientations of the 15 leg pairs) invariant under each group")
pairs = [(i, j) for i in range(6) for j in range(i + 1, 6)]
pidx = {p: k for k, p in enumerate(pairs)}
B = np.array(list(itertools.product([0, 1], repeat=15)), dtype=np.int8)   # bit 1: T[i][j]=1 (i<j)
def pair_map(g):
    im = np.zeros(15, int); fl = np.zeros(15, np.int8)
    for k, (i, j) in enumerate(pairs):
        a, b = PERM[g][i], PERM[g][j]
        if a < b: im[k] = pidx[(a, b)]
        else: im[k] = pidx[(b, a)]; fl[k] = 1
    return im, fl
PM = [pair_map(g) for g in range(24)]
def bits_to_T(bits):
    T = [[0] * 6 for _ in range(6)]
    for (i, j), b in zip(pairs, bits):
        if b: T[i][j] = 1
        else: T[j][i] = 1
    return T
def transitive(T):
    for a, b, c in itertools.permutations(range(6), 3):
        if T[b][a] and T[c][b] and not T[c][a]:
            return False
    return True
for name, G in SUB.items():
    mask = np.ones(len(B), bool)
    for g in G:
        im, fl = PM[g]
        # invariance: T'[P i][P j] = T[i][j]  <=> bit at image pair = bit XOR flip
        mask &= np.all(B[:, im] == (B ^ fl), axis=1)
    inv = B[mask]
    ntr = sum(transitive(bits_to_T(b)) for b in inv)
    print("   %-34s invariant tournaments: %5d  (transitive orders among them: %d)" % (name, len(inv), ntr))

print("(3) the 32 C3(111) tournaments: transport to the 8 body diagonals")
okc = 0
for T0 in ALL_C3_T:
    assert is_tournament(T0)
    fam, conf = family(T0)
    cov = all(transport_T(g, fam[f])[0:6] == fam[act_vec(g, f)] for g in range(24) for f in fam)
    okc += int(conf == 0 and cov and len(fam) == 8 and all(is_tournament(T) for T in fam.values()))
print("   tournaments with 0 conflicts, covariant family on 8 diagonals, all fermionic: %d / %d" % (okc, len(ALL_C3_T)))
# relation between T_f and T_{-f}
T0 = ALL_C3_T[0]; fam, _ = family(T0)
print("   example T_f0 (row i: legs j whose field factor hop i carries):")
for i in range(6):
    print("      hop %s: %s" % (NAMES[i], [NAMES[j] for j in range(6) if T0[i][j]]))
diffs = [sum(fam[f][i][j] != fam[F0][i][j] for i in range(6) for j in range(6)) // 2 for f in BD]
print("   pairs whose orientation differs from T_f0, per body diagonal f:", dict(zip(BD, diffs)))

print("(4) control: a fermionic tournament that is NOT C3-invariant (BK order -x<-y<-z<+x<+y<+z)")
order = [1, 3, 5, 0, 2, 4]
Tbk = [[0] * 6 for _ in range(6)]
for a in range(6):
    for b in range(6):
        if order.index(a) < order.index(b):
            Tbk[b][a] = 1      # later hop carries Z on earlier legs
famb, confb = family(Tbk)
print("   is tournament: %s; transport conflicts over the 24 turns: %d (0 = well defined)" % (is_tournament(Tbk), confb))
print("   distinct tournaments assigned to f0 by the 3 turns in Stab(f0):",
      len({str(transport_T(g, Tbk)) for g in C3GROUP}))
print("done")
