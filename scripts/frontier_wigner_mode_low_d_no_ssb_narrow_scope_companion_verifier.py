#!/usr/bin/env python3
"""Verifier for WIGNER_MODE_LOW_D_NO_SSB_NARROW_SCOPE_COMPANION_NOTE_2026-06-02.
17 checks: Part A (4) Bogoliubov+IR sanity; Part B (6) scope-narrowing
class-A inline lemmas vs origin/main; Part C (7) No-Go discipline gate."""
from __future__ import annotations
import json, math, os, re, subprocess, sys
from itertools import product
import numpy as np

PASS = 0
FAIL = 0
LOG: list[str] = []


def record(name, ok, detail=""):
    global PASS, FAIL
    PASS, FAIL = (PASS + 1, FAIL) if ok else (PASS, FAIL + 1)
    tag = "PASS" if ok else "FAIL"
    LOG.append(f"[{tag}] {name}" + (f"  ({detail})" if detail else ""))


REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NOTE_PATH = "docs/WIGNER_MODE_LOW_D_NO_SSB_NARROW_SCOPE_COMPANION_NOTE_2026-06-02.md"


def read_origin_main(path):
    try:
        out = subprocess.run(["git", "show", f"origin/main:{path}"],
                             cwd=REPO_ROOT, capture_output=True, text=True, check=False)
        return out.stdout if out.returncode == 0 else ""
    except Exception:
        return ""


def read_local(path):
    p = os.path.join(REPO_ROOT, path)
    return open(p).read() if os.path.exists(p) else ""


def load_ledger():
    raw = read_origin_main("docs/audit/data/audit_ledger.json")
    try:
        return json.loads(raw) if raw else {}
    except Exception:
        return {}


# ======================================================================
# Part A — finite Bogoliubov + IR-sum sanity exhibits
# ======================================================================
print("=" * 72); print("PART A  Bogoliubov + IR-sum sanity exhibits"); print("=" * 72); print()

I2 = np.eye(2, dtype=complex)
SX = np.array([[0, 1], [1, 0]], dtype=complex)
SY = np.array([[0, -1j], [1j, 0]], dtype=complex)
SZ = np.array([[1, 0], [0, -1]], dtype=complex)

# A.1: finite Gibbs Bogoliubov inequality on a 2-qubit block.
H2 = -0.5 * (np.kron(SX, I2) + np.kron(I2, SX)) - np.kron(SZ, SZ)
beta = 0.8
w, V = np.linalg.eigh(H2)
wt = np.exp(-beta * (w - w.min()))
rho = (V * wt) @ V.conj().T / wt.sum()
A = np.kron(SY, I2); C = np.kron(SX, I2)
lhs = abs(np.trace(rho @ (C @ A - A @ C))) ** 2
anti = A @ A.conj().T + A.conj().T @ A
dcom = (C @ H2 - H2 @ C) @ C.conj().T - C.conj().T @ (C @ H2 - H2 @ C)
rhs = (beta / 2) * np.trace(rho @ anti).real * np.trace(rho @ dcom).real
record("A.1.bogoliubov.finite_inequality_holds", lhs <= rhs + 1e-9,
       f"|<[C,A]>|^2={lhs:.4f} <= {rhs:.4f}")


# A.2: IR-sum threshold I_d(L) on Z^d.
def IR(d, L):
    s = 0.0
    for k in product(range(L), repeat=d):
        if all(ki == 0 for ki in k):
            continue
        kv = [2 * math.pi * ki / L for ki in k]
        s += 1.0 / (2 * sum(1 - math.cos(km) for km in kv))
    return s / (L ** d)


I18, I116 = IR(1, 8), IR(1, 16)
I28, I216 = IR(2, 8), IR(2, 16)
I38, I316 = IR(3, 8), IR(3, 16)
record("A.2.IR_sum.d=1.diverges", I116 > I18 * 1.5, f"I_1(8)={I18:.4f}, I_1(16)={I116:.4f}")
record("A.2.IR_sum.d=2.diverges", I216 > I28 * 1.05, f"I_2(8)={I28:.4f}, I_2(16)={I216:.4f}")
record("A.2.IR_sum.d=3.finite", abs(I316 - I38) / max(I38, 1e-12) < 0.20,
       f"I_3(8)={I38:.4f}, I_3(16)={I316:.4f}")

for line in LOG[-4:]:
    print(line)
print()


# ======================================================================
# Part B — scope-narrowing class-A inline lemmas
# ======================================================================
print("=" * 72); print("PART B  Scope-narrowing class-A inline lemmas"); print("=" * 72)

ledger = load_ledger()
rows = ledger.get("rows", {}) if isinstance(ledger, dict) else {}

BOG_ID = "mermin_wagner_bogoliubov_textbook_import_note_2026-05-18"
bog = rows.get(BOG_ID, {})
bog_status = bog.get("effective_status", "") or ""
bog_scope = bog.get("claim_scope", "") or ""
ok_B1 = (bog_status == "retained_bounded"
         and "Bogoliubov inequality" in bog_scope
         and ("no continuous-symmetry SSB conclusion" in bog_scope
              or "excludes the Ward" in bog_scope))
record("B.NS-W1.1.ledger.bogoliubov_retained_bounded_excludes_no_SSB", ok_B1,
       f"status={bog_status!r}")

cmw_text = read_origin_main("docs/AXIOM_FIRST_COLEMAN_MERMIN_WAGNER_THEOREM_NOTE_2026-04-29.md")
nc = re.search(r"##\s*Non-Claims(.+?)(?:##|\Z)", cmw_text, flags=re.DOTALL)
nc_block = nc.group(1) if nc else ""
ok_B2 = ("no spontaneous breaking of continuous symmetries" in nc_block
         and "d <= 2" in nc_block)
record("B.NS-W1.2.non_claim.cmw_disclaims_no_SSB", ok_B2,
       "Non-Claims block contains the d<=2 no-SSB disclaimer")

local_note = read_local(NOTE_PATH)
ok_B3 = ("H_Ward_norm" in local_note
         and "NAMED CONDITIONAL HYPOTHESIS" in local_note
         and "(NS-W1)" in local_note
         and ("Assume the conditional hypothesis" in local_note
              or "Assume `H_Ward_norm`" in local_note))
record("B.NS-W1.3.conditional_form.NS_W1_H_Ward_norm_clause", ok_B3,
       f"present: {ok_B3}")

NOE_ID = "axiom_first_lattice_noether_theorem_note_2026-04-29"
noe = rows.get(NOE_ID, {})
noe_status = noe.get("effective_status", "") or ""
noe_scope = noe.get("claim_scope", "") or ""
ok_B4 = (noe_status == "retained_bounded"
         and "U(1) current" in noe_scope
         and "(2Z)^3" in noe_scope
         and "support-only" in noe_scope)
record("B.NS-W2.1.ledger_scope.noether_retained_bounded_with_bounded_scope",
       ok_B4, f"status={noe_status!r}")

parent_text = read_origin_main("docs/WIGNER_MODE_LOW_D_SUBLATTICE_THEOREM_NOTE_2026-05-02.md")
ok_B5 = ("carrying a continuous global" in parent_text
         and "Q = " in parent_text
         and "U(1) current" in noe_scope
         and "(2Z)^3 central two-step Ward identity" in noe_scope)
record("B.NS-W2.2.text_scope_gap.parent_generic_exceeds_upstream_specific",
       ok_B5, f"parent_generic + upstream_specific: {ok_B5}")

ok_B6 = ("(NS-W2.a)" in local_note
         and "(NS-W2.b)" in local_note
         and "U(1) phase generator" in local_note
         and "central two-step translation generator" in local_note
         and "admitted free staggered" in local_note)
record("B.NS-W2.3.narrowed_form.NS_W2_generator_and_carrier_restriction",
       ok_B6, f"all tokens present: {ok_B6}")

print()
for line in LOG[-6:]:
    print(line)
print()


# ======================================================================
# Part C — No-Go discipline gate
# ======================================================================
print("=" * 72); print("PART C  No-Go discipline gate"); print("=" * 72)


def _scan_retained_general_no_SSB():
    for r in rows.values():
        if not isinstance(r, dict):
            continue
        s = (r.get("claim_scope") or "").lower()
        if r.get("effective_status") == "retained" and (
                "no spontaneous breaking" in s or "no continuous-symmetry ssb" in s):
            return True
    return False


def _scan_retained_general_noether():
    for r in rows.values():
        if not isinstance(r, dict):
            continue
        s = (r.get("claim_scope") or "").lower()
        if (r.get("effective_status") == "retained" and "noether" in s
                and "lattice" in s and "bounded" not in s and "staggered" not in s):
            return True
    return False


route1 = bog_status == "retained_bounded"
route2 = ok_B2
route3 = not _scan_retained_general_no_SSB()
route4 = not _scan_retained_general_noether()
record("C.no_go.N1.route1.Bogoliubov_import_bounded_not_no_SSB", route1,
       f"status={bog_status!r}")
record("C.no_go.N1.route2.CMW_IR_sum_explicit_no_SSB_disclaimer", route2,
       "Non-Claims contains the disclaimer")
record("C.no_go.N1.route3.no_retained_general_no_SSB_on_main", route3,
       "ledger scan negative")
record("C.no_go.N1.route4.no_retained_general_lattice_noether_on_main", route4,
       "ledger scan negative")

ok_C3 = ("H_Ward_norm" in local_note
         and "NAMED CONDITIONAL HYPOTHESIS" in local_note)
record("C.no_go.N3.honest_residual_label.H_Ward_norm_named_conditional",
       ok_C3, f"present: {ok_C3}")

ok_C4 = ("d ∈ {1, 2}" in local_note and "conditional" in local_note.lower())
record("C.no_go.N4.no_substrate_overreach.d_in_1_2_and_conditional",
       ok_C4, f"present: {ok_C4}")

normalized = re.sub(r"\s+", " ", local_note)
ok_C5 = ("(NS-W2.a)" in local_note and "(NS-W2.b)" in local_note
         and "No other choice of" in normalized)
record("C.no_go.N5.no_generator_overreach.NS_W2_a_b_only",
       ok_C5, f"present: {ok_C5}")

print()
for line in LOG[-7:]:
    print(line)
print()


# ======================================================================
# Summary
# ======================================================================
print("=" * 72); print("SUMMARY"); print("=" * 72)
print(f"  PASS: {PASS}")
print(f"  FAIL: {FAIL}")
print()
if FAIL == 0:
    print("WIGNER_MODE_LOW_D_NO_SSB_NARROW_SCOPE_COMPANION_VERIFIER=PASS")
    sys.exit(0)
else:
    print("WIGNER_MODE_LOW_D_NO_SSB_NARROW_SCOPE_COMPANION_VERIFIER=FAIL")
    for line in LOG:
        if line.startswith("[FAIL]"):
            print(line)
    sys.exit(1)
