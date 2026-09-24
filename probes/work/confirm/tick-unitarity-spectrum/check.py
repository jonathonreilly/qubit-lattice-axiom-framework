"""Independent confirmation of the strict-tick transport census.

Exact Gaussian-integer arithmetic. Line unitarity is the Bloch symbol identity
U(z)^dagger U(z) = I as a Laurent polynomial, not a ring matrix at roots of unity.
The finder's script is not called.
"""
import itertools
import sys

FAILS = []
N = 12
UNIMOD = [(2, 0), (-2, 0), (0, 2), (0, -2)]
HALF = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
QUART = [(1, 0), (-1, 0), (0, 1), (0, -1)]
ZERO = (0, 0)


def want(label, ok):
    if not ok:
        FAILS.append(label)
    print(("PASS " if ok else "FAIL ") + label, flush=True)


def conj(a):
    return (a[0], -a[1])


def mul(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def n2(a):
    return a[0] * a[0] + a[1] * a[1]


def add_poly(p, q):
    out = dict(p)
    for k, v in q.items():
        out[k] = (out.get(k, ZERO)[0] + v[0], out.get(k, ZERO)[1] + v[1])
    return {k: v for k, v in out.items() if v != ZERO}


def mul_poly(p, q):
    out = {}
    for i, a in p.items():
        for j, b in q.items():
            c = mul(a, b)
            prev = out.get(i + j, ZERO)
            out[i + j] = (prev[0] + c[0], prev[1] + c[1])
    return {k: v for k, v in out.items() if v != ZERO}


def conj_poly(p):
    return {-k: conj(v) for k, v in p.items()}


def columns(full):
    vals = [ZERO] + UNIMOD + (HALF + QUART if full else [])
    out = []
    for c in itertools.product(vals, repeat=3):
        if n2(c[0]) + n2(c[1]) + n2(c[2]) == 4:
            out.append(c)
    return out


def symbol(cols):
    m = len(cols)
    B = [[dict() for _ in range(m)] for _ in range(m)]
    for j, (a, b, c) in enumerate(cols):
        B[j][j] = add_poly(B[j][j], {0: a})
        rt = (j + 1) % m
        B[rt][j] = add_poly(B[rt][j], {(1 if j == m - 1 else 0): b})
        lf = (j - 1) % m
        B[lf][j] = add_poly(B[lf][j], {(-1 if j == 0 else 0): c})
    return B


def symbol_unitary(cols):
    B = symbol(cols)
    m = len(cols)
    for i in range(m):
        for j in range(m):
            acc = {}
            for k in range(m):
                acc = add_poly(acc, mul_poly(conj_poly(B[k][i]), B[k][j]))
            expect = {0: (4, 0)} if i == j else {}
            if acc != expect:
                return False
    return True


def det_poly(M):
    n = len(M)
    if n == 0:
        return {0: (1, 0)}
    total = {}
    for perm in itertools.permutations(range(n)):
        sign = 1
        p = list(perm)
        for i in range(n):
            while p[i] != i:
                j = p[i]
                p[i], p[j] = p[j], p[i]
                sign = -sign
        term = {0: (sign, 0)}
        for i in range(n):
            term = mul_poly(term, M[i][perm[i]])
        total = add_poly(total, term)
    return total


def dispersive(cols):
    B = symbol(cols)
    m = len(cols)
    # sums of principal minors, as Laurent polynomials; dispersive if any depends on z
    for k in range(1, m + 1):
        acc = {}
        for S in itertools.combinations(range(m), k):
            sub = [[B[i][j] for j in S] for i in S]
            acc = add_poly(acc, det_poly(sub))
        if any(power != 0 for power in acc):
            return True
    return False


def ring(cols):
    m = len(cols)
    V = [[ZERO for _ in range(N)] for _ in range(N)]
    for n in range(N):
        a, b, c = cols[n % m]
        V[n][n] = (V[n][n][0] + a[0], V[n][n][1] + a[1])
        r = (n + 1) % N
        V[r][n] = (V[r][n][0] + b[0], V[r][n][1] + b[1])
        left = (n - 1) % N
        V[left][n] = (V[left][n][0] + c[0], V[left][n][1] + c[1])
    return V


def vh(V):
    return [[conj(V[j][i]) for j in range(N)] for i in range(N)]


def matmul(A, B):
    out = [[ZERO for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for k in range(N):
            if A[i][k] == ZERO:
                continue
            for j in range(N):
                if B[k][j] == ZERO:
                    continue
                c = mul(A[i][k], B[k][j])
                out[i][j] = (out[i][j][0] + c[0], out[i][j][1] + c[1])
    return out


def transports(V):
    dag = vh(V)
    eps = [1 if n % 2 == 0 else -1 for n in range(N)]
    eps_v_eps = [[(eps[i] * eps[j] * V[i][j][0], eps[i] * eps[j] * V[i][j][1]) for j in range(N)] for i in range(N)]
    conjV = [[conj(V[i][j]) for j in range(N)] for i in range(N)]
    eps_c_eps = [[(eps[i] * eps[j] * conjV[i][j][0], eps[i] * eps[j] * conjV[i][j][1]) for j in range(N)] for i in range(N)]
    pv = [[V[(-i) % N][(-j) % N] for j in range(N)] for i in range(N)]
    pcv = [[conj(V[(-i) % N][(-j) % N]) for j in range(N)] for i in range(N)]
    return {
        "eps": eps_v_eps == dag,
        "eps K": eps_c_eps == dag,
        "P": pv == dag,
        "P K": pcv == dag,
    }


def dimerized(V):
    on = []
    for n in range(N):
        hop = V[(n + 1) % N][n] != ZERO or V[n][(n + 1) % N] != ZERO
        on.append(hop)
    return not any(on[n] and on[(n + 1) % N] for n in range(N))


def nonzero_phase(col):
    nz = [x for x in col if x != ZERO]
    return nz[0] if len(nz) == 1 else None


def census(m, full):
    cols = columns(full)
    out = {
        "columns": len(cols),
        "candidates": 0,
        "symbol_unitary": 0,
        "dispersive": 0,
        "non_monomial": 0,
        "with": {"eps": 0, "eps K": 0, "P": 0, "P K": 0},
        "eps_not_dimer": 0,
        "pk_phases": set(),
        "p_phases": set(),
    }
    for combo in itertools.product(cols, repeat=m):
        out["candidates"] += 1
        if not symbol_unitary(combo):
            continue
        out["symbol_unitary"] += 1
        V = ring(combo)
        # the ring embedding of a symbol-unitary tick is unitary
        gram = matmul(vh(V), V)
        eye = all(gram[i][j] == ((4, 0) if i == j else ZERO) for i in range(N) for j in range(N))
        if not eye:
            out["eps_not_dimer"] += 1000000
            continue
        t = transports(V)
        if (t["eps"] or t["eps K"]) and not dimerized(V):
            out["eps_not_dimer"] += 1
        if not dispersive(combo):
            continue
        out["dispersive"] += 1
        if any(sum(x != ZERO for x in c) > 1 for c in combo):
            out["non_monomial"] += 1
        for k in t:
            out["with"][k] += int(t[k])
        if m == 2:
            phases = tuple(nonzero_phase(c) for c in combo)
            if t["P K"]:
                out["pk_phases"].add(phases)
            if t["P"]:
                out["p_phases"].add(phases)
    return out


quoted = {
    2: {"candidates": 63504, "unitary": 208, "dispersive": 32, "eps": 0, "epsK": 0, "P": 8, "PK": 8, "non_monomial": 0},
    3: {"dispersive": 128, "eps": 0, "epsK": 0, "P": 16, "PK": 32, "non_monomial": 0},
    4: {"candidates": 20736, "dispersive": 512, "eps": 0, "epsK": 0, "P": 32, "PK": 32, "non_monomial": 0},
}

ok = True
phase_ok = True
for m, full in ((2, True), (3, False), (4, False)):
    r = census(m, full)
    q = quoted[m]
    print(
        f"m={m} columns={r['columns']} candidates={r['candidates']} symbol_unitary={r['symbol_unitary']} "
        f"dispersive={r['dispersive']} non_monomial={r['non_monomial']} transports={r['with']} "
        f"eps_not_dimer={r['eps_not_dimer']}",
        flush=True,
    )
    if "candidates" in q and r["candidates"] != q["candidates"]:
        ok = False
    if "unitary" in q and r["symbol_unitary"] != q["unitary"]:
        ok = False
    if r["dispersive"] != q["dispersive"] or r["non_monomial"] != q["non_monomial"]:
        ok = False
    if r["with"]["eps"] != q["eps"] or r["with"]["eps K"] != q["epsK"]:
        ok = False
    if r["with"]["P"] != q["P"] or r["with"]["P K"] != q["PK"]:
        ok = False
    if r["eps_not_dimer"] != 0:
        ok = False
    if m == 2:
        # P o K on a monomial shift: the two nonzero entries are equal; P: they are conjugates
        for phases in r["pk_phases"]:
            if None in phases or phases[0] != phases[1]:
                phase_ok = False
        for phases in r["p_phases"]:
            if None in phases or phases[1] != conj(phases[0]):
                phase_ok = False
        print(f"  PK phases {sorted(r['pk_phases'])}", flush=True)
        print(f"  P phases {sorted(r['p_phases'])}", flush=True)

want("exact symbol census matches the reported counts: no dispersive tick carries eps or eps o K, and P / P o K match", ok)
want("m=2 dispersive P o K shifts have equal hop phases, and P shifts have conjugate hop phases", phase_ok)

print(f"TOTAL FAIL={len(FAILS)}")
if FAILS:
    print("SUMMARY: not reproduced - " + FAILS[0])
    sys.exit(1)
print(
    "HIT: confirmed - on radius-1 unitary ticks, tested by the Bloch symbol rather than the ring, "
    "no dispersive tick at periods 2, 3, 4 carries the eps or eps o K transport "
    "(32, 128, 512 dispersive ticks, all monomial). The transports that survive are P o K and P: "
    "(8, 8), (32, 16), (32, 32)."
)
print(
    "SUMMARY: confirmed the falsifier. The C-reading through eps or eps o K is empty on this strict-tick class. "
    "Line unitarity was the Laurent identity U(z)^dagger U(z) = 4 I, and the same counts reappear. "
    "The theorem's forward and converse directions were not re-proved."
)
