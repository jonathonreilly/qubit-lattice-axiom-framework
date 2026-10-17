"""Classify cubic-covariant nearest-neighbour Pauli stabilizer rules, one qubit per site of Z^3.

A rule is a set of signed Pauli strings supported on the star of the origin (the site
and its six neighbours), closed under the proper cubic group O acting on positions and,
on Pauli labels, by one of the four soldering-menu actions. Its translates generate the
stabilizer group. We enumerate single O-orbits (one generator up to symmetry), keep the
sign-consistent and mutually commuting ones, then test compatibility between orbits.
"""
import itertools, sys, json
import numpy as np

# proper cubic group as signed permutation matrices with det +1
O = []
for p in itertools.permutations(range(3)):
    for s in itertools.product((1, -1), repeat=3):
        M = np.zeros((3, 3), int)
        for i in range(3): M[p[i], i] = s[i]
        if round(np.linalg.det(M)) == 1: O.append(M)
assert len(O) == 24
STAR = [(0, 0, 0), (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
SIDX = {p: i for i, p in enumerate(STAR)}

def perm_sign(M):
    P = np.abs(M); return int(round(np.linalg.det(P)))

def Q(M, action):
    if action == 'trivial': return np.eye(3, dtype=int)
    if action == 'sign': s = perm_sign(M); return np.diag([1, s, s])
    if action == 'axis': return perm_sign(M) * np.abs(M)
    if action == 'full': return M
    raise ValueError

# Pauli label 0=I,1=X,2=Y,3=Z ; action of a signed permutation Q on labels: sigma_a -> Q[b,a] sigma_b
def act_label(Qm, a):
    if a == 0: return 0, 1
    col = Qm[:, a - 1]; b = int(np.nonzero(col)[0][0]); return b + 1, int(col[b])

def act(M, Qm, string, sign):
    """string: tuple of 7 labels on STAR; returns transformed (string, sign)."""
    out = [0] * 7; sg = sign
    for i, a in enumerate(string):
        if a == 0: continue
        pos = tuple(int(x) for x in M @ np.array(STAR[i]))
        b, s = act_label(Qm, a); out[SIDX[pos]] = b; sg *= s
    return tuple(out), sg

def orbit(string, action):
    """Signed orbit under O; returns dict string->sign, or None if sign-inconsistent."""
    orb = {}
    for M in O:
        st, sg = act(M, Q(M, action), string, 1)
        if st in orb and orb[st] != sg: return None
        orb[st] = sg
    return orb

def placed(string, shift):
    return {tuple(np.add(STAR[i], shift)): a for i, a in enumerate(string) if a}

def anticommute(P1, P2):
    n = 0
    for site, a in P1.items():
        b = P2.get(site, 0)
        if b and b != a: n += 1
    return n % 2 == 1

SHIFTS = [s for s in itertools.product(range(-2, 3), repeat=3) if sum(map(abs, s)) <= 4]

def family_commutes(strings_a, strings_b):
    for s1 in strings_a:
        P1 = placed(s1, (0, 0, 0))
        for s2 in strings_b:
            for sh in SHIFTS:
                if anticommute(P1, placed(s2, sh)): return False
    return True

def canon(orb):
    return min(orb)

if __name__ == '__main__':
    results = {}
    for action in ('trivial', 'sign', 'axis', 'full'):
        seen, good = set(), []
        for string in itertools.product(range(4), repeat=7):
            if not any(string) or string in seen: continue
            orb = orbit(string, action)
            # mark whole unsigned orbit as seen
            for M in O:
                seen.add(act(M, Q(M, action), string, 1)[0])
            if orb is None: continue
            strs = list(orb)
            if family_commutes(strs, strs):
                good.append((canon(orb), len(orb), orb[canon(orb)]))
        results[action] = good
        centre_active = [g for g in good if g[0][0] != 0]
        print(f'{action}: {len(good)} commuting sign-consistent single-orbit rules; centre-active {len(centre_active)}', flush=True)
        for g in good: print('   ', g)
    json.dump({k: [[list(g[0]), g[1], g[2]] for g in v] for k, v in results.items()}, open('single_orbits.json', 'w'))
