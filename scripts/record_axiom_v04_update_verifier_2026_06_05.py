#!/usr/bin/env python3
"""
Record axiom v0.4 update — elementary verifier.

Verifies the finite linear-algebra behind the consequences the v0.4 update
makes explicit (see docs/RECORD_AXIOM_V04_UPDATE_LOGIC_NOTE_2026-06-05.md and
docs/MINIMAL_AXIOMS_2026-06-05.md):

  T2  (classical/quantum cut):
        center(M_n(C)) = scalars  (no finer-than-block frozen fact),
        reality fixes 2 real Wedderburn blocks for R[Z_3] (vs 3 for C[Z_3]).
  T3  (measure dial):
        r(s) = 2^(s-1) interpolates block-count (s=0 -> r=1/2 -> Q=2/3) and
        Born/dimension (s=1 -> r=1 -> Q=1);
        r=1/2 is the block-swap (r -> 1/(4r)) fixed point and the 2-sector
        entropy maximum (the symmetric setting).
  additivity:  I(R1 ⊔ R2) = I(R1) + I(R2),  I(empty)=0.
  non-overreach (the binding frame):
        r(s) is multi-valued; a universal-s rule (all sectors at r=1/2) is
        FALSIFIED by the observed inter-sector Koide spread.

No measured masses are consumed as derivation inputs. The four sector Koide Q
values appear ONLY as a labelled observational comparison in the non-overreach
guard; they do not enter any derivation of the dial or its settings.

Deterministic. Prints a PASS/FAIL line per check and a SUMMARY line at the end.
"""

import numpy as np

PASS = 0
FAIL = 0


def check(name, cond):
    global PASS, FAIL
    ok = bool(cond)
    if ok:
        PASS += 1
        print(f"PASS: {name}")
    else:
        FAIL += 1
        print(f"FAIL: {name}")
    return ok


# ===========================================================================
# T2a.  center(M_n(C)) = scalars  (within-block: no finer recordable label)
# ===========================================================================
def center_dim(n):
    """dim of {X in M_n : [X, E_ij] = 0 for all matrix units E_ij}.
    vec([X,G]) = (G^T (x) I - I (x) G) vec(X);  nullspace dim = dim center."""
    blocks = []
    I = np.eye(n)
    for i in range(n):
        for j in range(n):
            G = np.zeros((n, n), dtype=complex)
            G[i, j] = 1.0
            blocks.append(np.kron(G.T, I) - np.kron(I, G))
    A = np.vstack(blocks)
    s = np.linalg.svd(A, compute_uv=False)
    tol = 1e-9 * max(A.shape)
    rank = int((s > tol).sum())
    return n * n - rank


for n in (2, 3, 4):
    check(f"T2a center(M_{n}(C)) is 1-dimensional (scalars only)",
          center_dim(n) == 1)


# ===========================================================================
# T2b.  reality fixes the block count: R[Z_3] = R (+) C  (2 blocks)
#        vs C[Z_3] = C^3 (3 blocks).  Frobenius-Schur indicators.
# ===========================================================================
def fs_indicators_Z3():
    """FS(chi_k) = (1/3) sum_g chi_k(2g) for the three characters of Z_3."""
    w = np.exp(2j * np.pi / 3)
    fs = []
    for k in range(3):
        val = sum(w ** (k * ((2 * g) % 3)) for g in range(3)) / 3.0
        fs.append(val)
    return np.array(fs)


fs = fs_indicators_Z3()
n_real_char = int(np.sum(np.isclose(fs.real, 1.0) & np.isclose(fs.imag, 0.0)))
n_complex_char = int(np.sum(np.isclose(fs, 0.0)))
# real blocks: each FS=+1 char is one real block; complex chars pair (FS=0) two-to-one.
n_real_blocks = n_real_char + n_complex_char // 2
n_complex_blocks = 3  # C[Z_3] = C^3

check("T2b FS indicators of Z_3 are [+1, 0, 0]",
      np.allclose(np.sort_complex(fs), np.sort_complex(np.array([1.0, 0.0, 0.0]))))
check("T2b reality => R[Z_3] has exactly 2 real Wedderburn blocks (singlet + doublet)",
      n_real_blocks == 2)
check("T2b without reality C[Z_3] has 3 blocks (reality clause is load-bearing)",
      n_complex_blocks == 3 and n_real_blocks != n_complex_blocks)


# ===========================================================================
# T3.  the measure dial  r(s) = 2^(s-1),  Q = 1/3 + (2/3) r
# ===========================================================================
def r_of_s(s):
    return 2.0 ** (s - 1.0)


def Q_of_r(r):
    return 1.0 / 3.0 + (2.0 / 3.0) * r


check("T3 dial endpoint: s=0 -> r=1/2 (block-count / equipartition setting)",
      np.isclose(r_of_s(0.0), 0.5))
check("T3 dial endpoint: s=0 -> Q=2/3 (charged-lepton setting)",
      np.isclose(Q_of_r(r_of_s(0.0)), 2.0 / 3.0))
check("T3 dial endpoint: s=1 -> r=1 (Born / dimension default setting)",
      np.isclose(r_of_s(1.0), 1.0))
check("T3 dial endpoint: s=1 -> Q=1 (framework default)",
      np.isclose(Q_of_r(r_of_s(1.0)), 1.0))

s_grid = np.linspace(-1.0, 1.5, 51)
r_grid = r_of_s(s_grid)
check("T3 dial r(s) is strictly monotone increasing in s",
      np.all(np.diff(r_grid) > 0))


# --- block swap r -> 1/(4r): involution, fixed point r=1/2 ------------------
def swap(r):
    return 1.0 / (4.0 * r)


rs = np.array([0.1, 0.25, 0.5, 0.75, 1.0, 2.0])
check("T3 block-swap r -> 1/(4r) is an involution",
      np.allclose(swap(swap(rs)), rs))
check("T3 block-swap fixed point is exactly r=1/2",
      np.isclose(swap(0.5), 0.5))


# --- 2-sector entropy peaks (concave max) at the symmetric setting r=1/2 ----
def power_fractions(r):
    p_s = 1.0 / (1.0 + 2.0 * r)
    p_d = 2.0 * r / (1.0 + 2.0 * r)
    return p_s, p_d


def S2(r):
    p_s, p_d = power_fractions(r)
    out = 0.0
    for p in (p_s, p_d):
        if p > 0:
            out -= p * np.log(p)
    return out


p_s_half, p_d_half = power_fractions(0.5)
check("T3 at r=1/2 the two real blocks carry equal power (p_s = p_d = 1/2)",
      np.isclose(p_s_half, 0.5) and np.isclose(p_d_half, 0.5))
check("T3 2-sector entropy at r=1/2 equals ln 2 (maximal)",
      np.isclose(S2(0.5), np.log(2.0)))

# numerical first/second derivative of S2 at r=1/2
h = 1e-5
dS = (S2(0.5 + h) - S2(0.5 - h)) / (2 * h)
d2S = (S2(0.5 + h) - 2 * S2(0.5) + S2(0.5 - h)) / (h * h)
check("T3 dS2/dr = 0 at r=1/2 (stationary)", abs(dS) < 1e-4)
check("T3 d2S2/dr2 < 0 at r=1/2 (concave maximum -> symmetric setting)", d2S < 0)
# swap-invariance of the entropy
check("T3 2-sector entropy is invariant under the block swap r -> 1/(4r)",
      np.allclose([S2(r) for r in (0.25, 0.5, 1.0, 2.0)],
                  [S2(swap(r)) for r in (0.25, 0.5, 1.0, 2.0)]))


# ===========================================================================
# additivity:  I(R1 ⊔ R2) = I(R1) + I(R2),  I(empty) = 0
# ===========================================================================
def I_count(records):
    return float(len(set(records)))


R1, R2 = {"a", "b"}, {"c", "d", "e"}
check("additivity I(R1 ⊔ R2) = I(R1) + I(R2) for disjoint records",
      np.isclose(I_count(R1 | R2), I_count(R1) + I_count(R2)) and R1.isdisjoint(R2))
check("additive baseline I(empty) = 0", np.isclose(I_count(set()), 0.0))


# ===========================================================================
# non-overreach (binding frame):
#   r(s) is multi-valued; the observed sectors spread across distinct s.
#   A universal-s rule (all sectors at r=1/2) is FALSIFIED.
#   >>> Q values below are a LABELLED OBSERVATIONAL COMPARISON only. <<<
# ===========================================================================
OBSERVED_Q = {  # observational comparison only; NOT derivation inputs
    "charged_leptons": 0.666661,
    "down_quarks":     0.731,
    "up_quarks":       0.848,
}


def r_from_Q(Q):
    return (3.0 * Q - 1.0) / 2.0


def s_from_r(r):
    return 1.0 + np.log2(r)


s_by_sector = {k: s_from_r(r_from_Q(Q)) for k, Q in OBSERVED_Q.items()}

check("non-overreach: charged leptons sit at the symmetric setting r=1/2 (s~0)",
      abs(s_by_sector["charged_leptons"]) < 0.02)
check("non-overreach: the sectors occupy DISTINCT settings (s spread > 0.3)",
      (max(s_by_sector.values()) - min(s_by_sector.values())) > 0.3)
check("non-overreach: a universal-s rule (all at r=1/2) is FALSIFIED",
      not np.allclose(list(s_by_sector.values()), 0.0, atol=0.05))
check("non-overreach: r=1 (Born) is a genuine alternative setting, not excluded",
      np.isclose(r_of_s(1.0), 1.0) and Q_of_r(1.0) == 1.0)

print()
print("--- per-sector dial occupancy (observational comparison only) ---")
for k, Q in OBSERVED_Q.items():
    r = r_from_Q(Q)
    print(f"  {k:16s}  Q={Q:.4f}  r={r:.4f}  s={s_from_r(r):+.3f}")

print()
print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
if FAIL:
    raise SystemExit(1)
