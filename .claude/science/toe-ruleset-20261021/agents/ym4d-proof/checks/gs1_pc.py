#!/usr/bin/env python3
# checks/gs1_pc.py  --  target T55-O, check gs1.
# Written AFTER checks/gs1_criteria.md.  Exact integer arithmetic only.
# No numpy, no BLAS, no machine-wide numeric lock.  Runtime ~seconds.
#
# Implements BFT_A Lemma PC's operator P (BFT_A.md section 23.1) literally, with the
# [RBA5-fix] U2 sign reading (BFT_A.md section 27), and tests clauses A1-A6 of
# checks/gs1_criteria.md.
#
# Conventions (fixed in the criteria file before this script):
#   (d*G)_nu(z) = sum_mu [ G_{mu,nu}(z - e_mu) - G_{mu,nu}(z) ]
#   (d*e)(z)    = sum_mu [ e_mu(z - e_mu)     - e_mu(z)      ]
#   G_{nu,mu} = -G_{mu,nu}

import itertools
import random

SEED = 20261028
N = 7          # box side of the lift (no wrap: supp is kept well inside)
DIM = 4
TRIALS = 12


# ---------- basic lattice operations (exact integers, dict-valued) ----------

def grid(dim, n=N):
    return list(itertools.product(range(n), repeat=dim))


def shift(pt, mu, s):
    q = list(pt)
    q[mu] += s
    return tuple(q)


def two_form_get(G, pt, mu, nu):
    """Antisymmetric lookup in a 2-form stored on mu<nu keys."""
    if mu == nu:
        return 0
    if mu < nu:
        return G.get((pt, mu, nu), 0)
    return -G.get((pt, nu, mu), 0)


def codiff_2form(G, dim, n=N):
    """e_nu(z) = sum_mu [G_{mu,nu}(z-e_mu) - G_{mu,nu}(z)]."""
    e = {}
    for pt in grid(dim, n):
        for nu in range(dim):
            tot = 0
            for mu in range(dim):
                if mu == nu:
                    continue
                tot += two_form_get(G, shift(pt, mu, -1), mu, nu)
                tot -= two_form_get(G, pt, mu, nu)
            if tot:
                e[(pt, nu)] = tot
    return e


def codiff_1form(e, dim, n=N):
    """(d*e)(z) = sum_mu [e_mu(z-e_mu) - e_mu(z)]."""
    out = {}
    for pt in grid(dim, n):
        tot = 0
        for mu in range(dim):
            tot += e.get((shift(pt, mu, -1), mu), 0)
            tot -= e.get((pt, mu), 0)
        if tot:
            out[pt] = tot
    return out


# ---------- Lemma PC's operator P ----------

def pc(e, dim, n=N):
    """BFT_A Lemma PC, section 23.1.  e: {(pt,nu): val} with pt a dim-tuple.
    Returns G: {(pt,mu,nu): val}, mu<nu, with d*G = e for co-closed compactly
    supported e."""
    if dim <= 1:
        return {}                      # d=1: co-closed + compact support => e = 0
    a = 0
    carriers = [pt[0] for (pt, nu) in e if nu != a and e[(pt, nu)] != 0]
    if not carriers:
        return {}
    b = max(carriers)

    # W_nu(z') = sum_t e_nu(t, z'),  as a (dim-1)-form with components relabelled nu -> nu-1
    W = {}
    for nu in range(1, dim):
        for zp in grid(dim - 1, n):
            tot = 0
            for t in range(n):
                tot += e.get(((t,) + zp, nu), 0)
            if tot:
                W[(zp, nu - 1)] = tot

    G = {}
    # G_{a,nu} = -S_nu + 1[z_a >= b] W_nu
    for nu in range(1, dim):
        for zp in grid(dim - 1, n):
            Wv = W.get((zp, nu - 1), 0)
            S = 0
            for t in range(n):
                S += e.get(((t,) + zp, nu), 0)
                val = -S + (Wv if t >= b else 0)
                if val:
                    G[(((t,) + zp), a, nu)] = val

    # transverse construction on the slice z_a = b
    Gamma = pc(W, dim - 1, n)
    for (zp, i, j), v in Gamma.items():
        G[(((b,) + zp), i + 1, j + 1)] = v
    return G


def relabel_1form(e, perm, dim):
    """Push a 1-form through the coordinate permutation perm (perm[i] = new index of axis i)."""
    out = {}
    for (pt, nu), v in e.items():
        npt = [0] * dim
        for i in range(dim):
            npt[perm[i]] = pt[i]
        out[(tuple(npt), perm[nu])] = v
    return out


def unrelabel_2form(G, perm, dim):
    """Pull a 2-form back through perm, restoring mu<nu storage with the sign."""
    inv = [0] * dim
    for i in range(dim):
        inv[perm[i]] = i
    out = {}
    for (pt, mu, nu), v in G.items():
        opt = tuple(pt[perm[i]] for i in range(dim))
        omu, onu, val = inv[mu], inv[nu], v
        if omu > onu:
            omu, onu, val = onu, omu, -v
        out[(opt, omu, onu)] = out.get((opt, omu, onu), 0) + val
    return {k: v for k, v in out.items() if v}


# ---------- test quantities ----------

def total_component_sums(e, dim):
    return [sum(v for (pt, nu), v in e.items() if nu == mu) for mu in range(dim)]


def first_moment_matrix(e, dim):
    M = [[0] * dim for _ in range(dim)]
    for (pt, nu), v in e.items():
        for mu in range(dim):
            M[mu][nu] += pt[mu] * v
    return M


def signed_totals(G, dim):
    T = {}
    for mu in range(dim):
        for nu in range(mu + 1, dim):
            T[(mu, nu)] = sum(v for (pt, a, b), v in G.items() if a == mu and b == nu)
    return T


def sign_coherent(G, dim):
    for mu in range(dim):
        for nu in range(mu + 1, dim):
            signs = {(1 if v > 0 else -1) for (pt, a, b), v in G.items()
                     if a == mu and b == nu and v != 0}
            if len(signs) > 1:
                return False
    return True


def bounding_cube(support_pts):
    lo = [min(p[i] for p in support_pts) for i in range(DIM)]
    hi = [max(p[i] for p in support_pts) for i in range(DIM)]
    return lo, hi


# ---------- the run ----------

def random_e(rng):
    """e := d*G0 for a random compactly supported integer 2-form G0."""
    G0 = {}
    for pt in itertools.product(range(2, 5), repeat=DIM):
        for mu in range(DIM):
            for nu in range(mu + 1, DIM):
                v = rng.randint(-3, 3)
                if v:
                    G0[(pt, mu, nu)] = v
    return codiff_2form(G0, DIM)


def main():
    rng = random.Random(SEED)
    print("gs1 -- Lemma PC operator and three elementary claims.  seed=%d  N=%d  d=%d  trials=%d"
          % (SEED, N, DIM, TRIALS))
    print()

    a1_ok = a2_ok = a3_ok = a4_ok = True
    a4_distinct = False
    coherent = 0

    for tr in range(TRIALS):
        e = random_e(rng)
        # pre-condition: e co-closed
        assert not codiff_1form(e, DIM), "generator produced a non-co-closed e"

        G = pc(e, DIM)

        # --- A1 exactness + support
        back = codiff_2form(G, DIM)
        if back != e:
            a1_ok = False
            print("  A1 FAIL on trial %d: d*(Pe) != e" % tr)
        sup_e = sorted({pt for (pt, nu) in e})
        sup_G = sorted({pt for (pt, mu, nu) in G})
        lo, hi = bounding_cube(sup_e)
        if any(not all(lo[i] <= p[i] <= hi[i] for i in range(DIM)) for p in sup_G):
            a1_ok = False
            print("  A1 FAIL on trial %d: supp(Pe) leaves the bounding cube of supp e" % tr)

        # --- A2 zero component sums
        sums = total_component_sums(e, DIM)
        if any(s != 0 for s in sums):
            a2_ok = False
            print("  A2 FAIL on trial %d: component sums %s" % (tr, sums))

        # --- A3 first-moment identity + antisymmetry
        M = first_moment_matrix(e, DIM)
        T = signed_totals(G, DIM)
        for mu in range(DIM):
            for nu in range(mu + 1, DIM):
                if T[(mu, nu)] != M[mu][nu]:
                    a3_ok = False
                    print("  A3 FAIL on trial %d: sum G_%d%d = %d, first moment = %d"
                          % (tr, mu, nu, T[(mu, nu)], M[mu][nu]))
        for mu in range(DIM):
            for nu in range(DIM):
                if M[mu][nu] + M[nu][mu] != 0:
                    a3_ok = False
                    print("  A3 FAIL on trial %d: M not antisymmetric at (%d,%d)" % (tr, mu, nu))

        # --- A4 primitive independence (reverse the axis order)
        perm = [DIM - 1 - i for i in range(DIM)]
        e2 = relabel_1form(e, perm, DIM)
        G2raw = pc(e2, DIM)
        G2 = unrelabel_2form(G2raw, perm, DIM)
        if codiff_2form(G2, DIM) != e:
            a4_ok = False
            print("  A4 FAIL on trial %d: the second primitive is not a primitive" % tr)
        if G2 != G:
            a4_distinct = True
        T2 = signed_totals(G2, DIM)
        if T2 != T:
            a4_ok = False
            print("  A4 FAIL on trial %d: signed totals differ between primitives" % tr)

        # --- A5 sign coherence
        if sign_coherent(G, DIM):
            coherent += 1

    print("A1  d*(Pe) = e exactly and supp inside the cube : %s" % ("PASS" if a1_ok else "FAIL"))
    print("A2  every component of e sums to zero           : %s" % ("PASS" if a2_ok else "FAIL"))
    print("A3  sum_z G_munu = sum_z z_mu e_nu, M antisym    : %s" % ("PASS" if a3_ok else "FAIL"))
    print("A4  signed totals primitive-independent         : %s%s"
          % ("PASS" if a4_ok else "FAIL",
             "" if a4_distinct else "   (VACUOUS: the two primitives never differed)"))
    print("A5  sign-coherent trials                        : %d / %d" % (coherent, TRIALS))
    print("    verdict: %s" % ("SIGN-COHERENT-GENERIC" if coherent == TRIALS else "SIGN-MIXED"))

    # A5 (ii): the single-plaquette input, where sign coherence is expected to be possible
    q = ((3, 3, 3, 3), 0, 1)
    dq = {q: 1}
    e_q = codiff_2form(dq, DIM)
    G_q = pc(e_q, DIM)
    ok_q = (codiff_2form(G_q, DIM) == e_q)
    print("A5(ii) e = d*delta_q : P e exact=%s, sign-coherent=%s, |supp|=%d, values=%s"
          % (ok_q, sign_coherent(G_q, DIM), len(G_q), sorted({v for v in G_q.values()})))
    print()

    # ---------- A6 designed-FAIL control ----------
    print("A6 DESIGNED-FAIL CONTROL (each clause below MUST fail)")
    # A6a: a non-co-closed compactly supported current
    bad_pt = (2, 3, 4, 1)
    e_bad = {(bad_pt, 0): 1}
    a6a_coclosed = (codiff_1form(e_bad, DIM) == {})
    G_bad = pc(e_bad, DIM)
    a6a_exact = (codiff_2form(G_bad, DIM) == e_bad)
    a6a_sums = total_component_sums(e_bad, DIM)
    a6a_fired = (not a6a_coclosed) and (not a6a_exact) and any(s != 0 for s in a6a_sums)
    print("  A6a non-co-closed input : co-closed=%s  d*(Pe)=e : %s  component sums %s  -> %s"
          % (a6a_coclosed, a6a_exact, a6a_sums, "FIRED" if a6a_fired else "DID NOT FIRE"))

    # A6b: a 2-form that is not a primitive of e
    rng2 = random.Random(SEED + 1)
    e_one = random_e(rng2)
    e_two = random_e(rng2)
    G_wrong = pc(e_two, DIM)                       # primitive of the WRONG current
    T_wrong = signed_totals(G_wrong, DIM)
    M_one = first_moment_matrix(e_one, DIM)
    a6b_fired = any(T_wrong[(mu, nu)] != M_one[mu][nu]
                    for mu in range(DIM) for nu in range(mu + 1, DIM))
    print("  A6b wrong primitive     : signed totals match the first moments : %s  -> %s"
          % (not a6b_fired, "FIRED" if a6b_fired else "DID NOT FIRE"))

    # A6c: antisymmetry of M for the non-co-closed current
    M_bad = first_moment_matrix(e_bad, DIM)
    a6c_fired = any(M_bad[mu][nu] + M_bad[nu][mu] != 0
                    for mu in range(DIM) for nu in range(DIM))
    print("  A6c antisymmetry of M   : antisymmetric : %s  -> %s"
          % (not a6c_fired, "FIRED" if a6c_fired else "DID NOT FIRE"))
    print()
    control = a6a_fired and a6b_fired and a6c_fired
    print("CONTROL: %s" % ("FIRED on all three clauses" if control
                           else "DID NOT FIRE -- A1-A3 are NOT evidence"))


if __name__ == "__main__":
    main()
