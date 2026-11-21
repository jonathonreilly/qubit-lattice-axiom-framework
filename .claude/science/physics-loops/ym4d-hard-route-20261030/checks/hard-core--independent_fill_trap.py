#!/usr/bin/env python3
"""A finite, exact proof attempt for (FILL), Text 3.2 of parts/hard-core--independent.md: a trap in the faces that fire.

A face phi fires when the pattern of removed cells around it is bad, and then ALL the cells around it are removed. So outside the
initial set every removed cell lies in a full block B_psi, psi a face that has fired, and around phi the removed cells that are not
seeds are a union of traces B_psi n B_phi, with psi fired earlier.

A set P of faces is a TRAP if for every phi in P, every union of traces B_psi n B_phi over psi NOT in P is a good pattern at phi.
Let Z be the union of the blocks of P. If no seed lies in Z, then no face of P ever fires: at the first firing in P, the removed
cells around phi would be such a union, which is good, so it would not fire. So a cell c such that all faces with c in their block
are in P is never removed, for ANY initial set avoiding Z. The rule's non-monotonicity does not matter here.

The largest trap inside a given finite set is computed by deleting faces until none violates the condition, which is a monotone
iteration, since deleting from P only enlarges what is allowed. Everything is exact boolean arithmetic.

Pre-registered criteria, written before the first run. Target: one cell c = 0.
    PROVED-r: for some r <= 4, the largest trap among the faces with block inside the sup ball B_r(0) contains all the faces around 0.
    Then cl(Lambda_0) lies in Lambda_0 + B_D, with D the sup radius of Z, for every Lambda_0: (FILL) holds, with ratio at most
    (2 D + 1)^4, by this check, with no probability and no float.
    NO-TRAP: not so for r = 2, 3, 4. Then this form of argument does not close (FILL), and nothing is said about (FILL) itself.

Relative form, run after the absolute one. G is a good set. At a face phi the removed cells are now a union of traces and the trace
T_G of G on B_phi, where T_G is the pattern of a refinement of a good set of blocks of side >= 3, so that T_G is itself a good
pattern, of a face of the same or lower codimension, a product. Same deletion, with T_G ranging over all such patterns compatible
with phi. The conclusion needs cells of G excluded, so the check there is only that a cell off G is safe.
    PROVED-REL-r, or NO-TRAP-REL.

Result of the first run: NO-TRAP at r = 2, 3, 4: the deletion peels the ball layer by layer down to nothing. So this form of
argument does not close (FILL). The union of ANY traces is too generous: the rule is exact, so a neighbouring firing can spoil
a pattern, and the trap does not see that. It says nothing about (FILL) itself, which the numerics support.

Second run, criteria written before it: env HC_EDGE_ONLY=1, the rule at faces of codimension 3 only, where a bad pattern is exactly an
antipodal pair, so an exact union of two singletons. By hand, in one slice: a point (1, 1, 1) of a fired lattice needs a pair containing
(2, 0, 0) or a permutation, or (0, 0, 0), and (2, 0, 0) needs a pair containing some (1, +-1, +-1): a cycle, so neither can fire first.
    PROVED-EDGE: a trap protects the target, at some r <= 4. NO-TRAP-EDGE otherwise.
Result of the second run: NO-TRAP-EDGE. Only the vertex faces, which never fire under this rule, survive the deletion. My hand count looked at
one slice; traces of edges along the other axes are also singletons in that slice, so the cycle is not closed.

Run under the numeric lock, nice, RSS checked against 2 GB.
"""
import importlib.util
import itertools
import os
import pathlib
import sys
import time

HERE = pathlib.Path(__file__)
spec = importlib.util.spec_from_file_location("patterns", HERE.with_name("hard-core--independent_patterns.py"))
pm = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pm)

Q4 = list(itertools.product((0, 1), repeat=4))
Q3 = list(itertools.product((0, 1), repeat=3))


def vertex_face(v):
    return ("v", tuple(v))


def edge_face(axis, pos):
    return ("e", axis, tuple(pos))


def block(face):
    """Ordered list of cells around the face, in the bit order of the pattern tables."""
    if face[0] == "v":
        v = face[1]
        out = [None] * 16
        for b in Q4:
            k = b[0] | b[1] << 1 | b[2] << 2 | b[3] << 3
            out[k] = tuple(v[i] - 1 + b[i] for i in range(4))
        return out
    axis, pos = face[1], face[2]
    others = [i for i in range(4) if i != axis]
    out = [None] * 8
    for b in Q3:
        k = b[0] | b[1] << 1 | b[2] << 2
        c = [0] * 4
        c[axis] = pos[axis]
        for j, i in enumerate(others):
            c[i] = pos[i] - 1 + b[j]
        out[k] = tuple(c)
    return out


def faces_of_cell(c):
    out = []
    for b in Q4:
        out.append(vertex_face(tuple(c[i] + b[i] for i in range(4))))
    for axis in range(4):
        others = [i for i in range(4) if i != axis]
        for b in Q3:
            pos = list(c)
            for j, i in enumerate(others):
                pos[i] = c[i] + b[j]
            out.append(edge_face(axis, pos))
    return out


def faces_in_ball(r):
    out = set()
    for c in itertools.product(range(-r, r + 1), repeat=4):
        for f in faces_of_cell(c):
            if all(max(abs(x) for x in cell) <= r for cell in block(f)):
                out.add(f)
    return out


class Checker:
    def __init__(self):
        bad3, _ = pm.bad_table(3)
        bad4, _ = pm.bad_table(4)
        if os.environ.get("HC_EDGE_ONLY"):
            bad4 = set()
        self.bad = {"v": bad4, "e": bad3}
        self.full = {"v": 65535, "e": 255}
        self.cache = {}
        self.blocks = {}
        self.index = {}

    def blk(self, f):
        if f not in self.blocks:
            self.blocks[f] = block(f)
            self.index[f] = {c: k for k, c in enumerate(self.blocks[f])}
        return self.blocks[f]

    def any_bad_union(self, kind, masks, extra=frozenset((0,))):
        """Is some union of a subset of `masks`, with one of the base patterns in `extra`, a bad pattern? masks are removed sets."""
        key = (kind, frozenset(masks), extra)
        if key in self.cache:
            return self.cache[key]
        bad = self.bad[kind]
        full = self.full[kind]
        seen = set(extra)
        stack = list(extra)
        res = False
        ms = list(masks)
        while stack:
            cur = stack.pop()
            if (full ^ cur) in bad:
                res = True
                break
            for m in ms:
                n = cur | m
                if n not in seen:
                    seen.add(n)
                    stack.append(n)
        self.cache[key] = res
        return res

    def traces(self, phi, P):
        """Removed-set masks at phi from faces psi not in P, psi != phi."""
        cells = self.blk(phi)
        idx = self.index[phi]
        masks = set()
        seen = set()
        for c in cells:
            for psi in faces_of_cell(c):
                if psi in seen:
                    continue
                seen.add(psi)
                if psi == phi or psi in P:
                    continue
                m = 0
                for cell in self.blk(psi):
                    if cell in idx:
                        m |= 1 << idx[cell]
                if m:
                    masks.add(m)
        return masks


def largest_trap(chk, start, base=None, verbose=True):
    P = set(start)
    t0 = time.time()
    rounds = 0
    while True:
        rounds += 1
        remove = []
        for phi in P:
            masks = chk.traces(phi, P)
            extra = base(phi) if base else frozenset((0,))
            if chk.any_bad_union(phi[0], masks, extra):
                remove.append(phi)
        if not remove:
            break
        P.difference_update(remove)
        if verbose:
            print(f"  round {rounds}: removed {len(remove)}, left {len(P)}, t={time.time()-t0:.0f}", flush=True)
        pm.check_rss()
    return P


def report(P, target=(0, 0, 0, 0)):
    around = faces_of_cell(target)
    protected = all(f in P for f in around)
    z = set()
    for f in P:
        z.update(block(f))
    D = max((max(abs(x) for x in c) for c in z), default=-1)
    return protected, D, len(P)


def relative_base(chk):
    """Traces of a good set at phi, for the relative form: the removed set is a product over the coordinates in which phi sits on a
    coarse face. All subsets of B_phi of the form { sigma : sigma_i = s_i on I }, unions of those that are good patterns."""
    cache = {}

    def base(phi):
        kind = phi[0]
        if kind in cache:
            return cache[kind]
        d = 4 if kind == "v" else 3
        size = 2**d
        sub = []
        for I in itertools.product((None, 0, 1), repeat=d):
            m = 0
            for v in range(size):
                if all(I[i] is None or (v >> i & 1) == I[i] for i in range(d)):
                    m |= 1 << v
            sub.append(m)
        seen = {0}
        stack = [0]
        while stack:
            cur = stack.pop()
            for m in sub:
                n = cur | m
                if n not in seen and (chk.full[kind] ^ n) not in chk.bad[kind]:
                    seen.add(n)
                    stack.append(n)
        cache[kind] = frozenset(seen)
        return cache[kind]

    return base


def main():
    chk = Checker()
    print("tables ready", flush=True)
    done = None
    for r in (2, 3, 4):
        start = faces_in_ball(r)
        print(f"r={r}: start with {len(start)} faces", flush=True)
        P = largest_trap(chk, start)
        protected, D, n = report(P)
        print(f"r={r}: trap has {n} faces, target protected: {protected}, sup radius of Z: {D}", flush=True)
        if protected:
            print(f"PROVED-{r}: every initial set with no cell within sup distance {D} of a cell leaves that cell kept", flush=True)
            done = (r, P, D)
            break
    if done is None:
        print("NO-TRAP")
        return
    if os.environ.get("HC_EDGE_ONLY"):
        print("PROVED-EDGE")
        return
    r, _, _ = done
    base = relative_base(chk)
    for r2 in sorted({r, 3, 4}):
        if r2 < r:
            continue
        start = faces_in_ball(r2)
        P = largest_trap(chk, start, base=base, verbose=False)
        protected, D, n = report(P)
        print(f"relative r={r2}: trap has {n} faces, target protected: {protected}, sup radius of Z: {D}", flush=True)
        if protected:
            print(f"PROVED-REL-{r2}", flush=True)
            return
    print("NO-TRAP-REL")


if __name__ == "__main__":
    main()
