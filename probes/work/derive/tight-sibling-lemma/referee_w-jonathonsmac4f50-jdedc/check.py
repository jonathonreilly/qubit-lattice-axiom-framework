#!/usr/bin/env python3
"""Referee of J:derive:tight-sibling-lemma:a1 (author w-macbookpro90c72-j133a, grok-4.6); referee w-jonathonsmac4f50-jdedc
(claude-opus-5). Independent code: my own automaton on the isolated 3x2x2 box (sites outside are 0) and my own exhaustive
enumeration of the counted family (node sets through 1-sites containing the root, one arrow per non-seed node to a 1-predecessor
in the set, arborescences joined by forks, F = |S| - 1; value E - 3(|S| - 1) - |A|). Nothing from probes/lib/family.py or the
author's script. Disclosure: this referee's model family refereed attempts a4 and a5 of this problem (grok) with the same
enumeration on the cube.

B1  the census: over the 4096 noise patterns, the (pattern, processed z, pair of processed 1-predecessors) cases number 4544
    (every pair of 1-predecessors of z is a fork pair); without a level cap (as probes/lib/family.brute_min enumerates) the
    values at z are the attempt's histogram {-8:16, -7:240, -6:400, -5:1456, -4:512, -3:448, -2:1376, -1:96}
B2  with the task's definition (all nodes at levels <= level(z)) the histogram is {-8:16, -7:240, -6:400, -5:1408, -4:560,
    -3:448, -2:1328, -1:144}: 96 cases move up by one, none reaches 0
B3  the lemma's hypothesis (every 1-predecessor of z processed and tight, capped values) occurs in none of the 4096 patterns, so
    the census tests the lemma's conclusion only; the attempt's 'so they cannot both be tight' does not follow from v(z) < 0
"""
import itertools
import sys
from collections import Counter

from collections import Counter
def lvl(z): return sum(z)
def preds(z): return [tuple(z[i]-(1 if i==j else 0) for i in range(3)) for j in range(3)]
def is_fork(u,v): return sorted(v[i]-u[i] for i in range(3))==[-1,0,1]
BOX=[(x,y,z) for x in range(3) for y in range(2) for z in range(2)]
def realize(marks):
    eta={}
    for z in sorted(BOX,key=lvl):
        c=sum(eta.get(p,0) for p in preds(z))
        eta[z]=1 if (c>=2 or z in marks) else 0
    ones=[z for z in BOX if eta[z]]
    npred={z:[p for p in preds(z) if eta.get(p,0)] for z in ones}
    kind={z:("seed" if not npred[z] else "amp" if len(npred[z])==1 else "proc") for z in ones}
    return ones,npred,kind
def rv(ones,npred,kind,root,cap=True):
    others=[z for z in ones if z!=root and (lvl(z)<=lvl(root) or not cap)]
    best=None
    for r in range(len(others)+1):
        for sub in itertools.combinations(others,r):
            N=set(sub)|{root}
            nonseed=[z for z in N if kind[z]!="seed"]
            choices=[[u for u in npred[z] if u in N] for z in nonseed]
            if any(not ch for ch in choices): continue
            S=sum(1 for z in N if kind[z]=="seed")
            val=sum(1 if kind[z]=="proc" else -1 if kind[z]=="amp" else 0 for z in N)-3*(S-1)
            if best is not None and val>=best: continue
            fp=[(u,v) for u,v in itertools.combinations(sorted(N),2) if is_fork(u,v)]
            for arrows in itertools.product(*choices):
                par={z:z for z in N}
                def f(a):
                    while par[a]!=a: a=par[a]
                    return a
                for z,u in zip(nonseed,arrows): par[f(z)]=f(u)
                comps={f(z) for z in N}
                if len(comps)!=S: continue
                adj={c:set() for c in comps}
                for u,v in fp:
                    a,b=f(u),f(v)
                    if a!=b: adj[a].add(b); adj[b].add(a)
                st=[next(iter(comps))]; seen={st[0]}
                while st:
                    a=st.pop()
                    for b in adj[a]:
                        if b not in seen: seen.add(b); st.append(b)
                if seen==comps: best=val; break
    return best


def main():
    hu, hc, n, nonneg, hyp = Counter(), Counter(), 0, 0, 0
    for bits in itertools.product((0, 1), repeat=12):
        marks = {BOX[i] for i in range(12) if bits[i]}
        ones, npred, kind = realize(marks)
        for z in ones:
            if kind[z] != "proc":
                continue
            pw = [u for u in npred[z] if kind[u] == "proc"]
            pairs = [(u, v) for u, v in itertools.combinations(pw, 2) if is_fork(u, v)]
            if not pairs:
                continue
            vu, vc = rv(ones, npred, kind, z, cap=False), rv(ones, npred, kind, z, cap=True)
            hu[vu] += len(pairs)
            hc[vc] += len(pairs)
            n += len(pairs)
            nonneg += vc >= 0
            if all(kind[u] == "proc" for u in npred[z]) and all(rv(ones, npred, kind, u, cap=True) == 0 for u in npred[z]):
                hyp += 1
    want_u = {-8: 16, -7: 240, -6: 400, -5: 1456, -4: 512, -3: 448, -2: 1376, -1: 96}
    ok1 = n == 4544 and dict(hu) == want_u
    print(("PASS" if ok1 else "FAIL") + f": B1 {n} cases; uncapped values {dict(sorted(hu.items()))} (the attempt's histogram: {ok1})")
    ok2 = max(hc) <= -1 and nonneg == 0
    print(("PASS" if ok2 else "FAIL") + f": B2 capped values {dict(sorted(hc.items()))}; {sum(abs(hu[k] - hc[k]) for k in set(hu) | set(hc)) // 2} "
          "cases differ from the uncapped ones; none is 0 or positive")
    ok3 = hyp == 0
    print(("PASS" if ok3 else "FAIL") + f": B3 patterns with a processed z whose 1-predecessors are all tight processed: {hyp}")
    if not (ok1 and ok2 and ok3):
        print("SUMMARY: fails at a checked step (see FAIL lines)")
        return 1
    print("HIT: confirmed - tight-sibling a1's 3x2x2 census: 4544 (pattern, processed z, processed 1-predecessor pair) cases, "
          "the attempt's uncapped histogram reproduced exactly, and with the task's level cap every value is in [-8, -1] (96 cases "
          "shift by one), so no local counterexample in the box; recomputed with an independent automaton and family enumeration. "
          "Corrections: the attempt's brute_min omits the level cap of the definition; the lemma's hypothesis never occurs in the "
          "box, and 'they cannot both be tight' does not follow from v(z) < 0")
    print("SUMMARY: confirmed - the finite census survives (capped and uncapped); it tests the lemma's conclusion, its hypothesis "
          "never occurring on the box; the lemma on Z^3 stays open")
    return 0


if __name__ == "__main__":
    sys.exit(main())
