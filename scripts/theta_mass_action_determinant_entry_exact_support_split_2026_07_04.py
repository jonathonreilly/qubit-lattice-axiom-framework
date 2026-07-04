#!/usr/bin/env python3
"""Verifier for theta mass action determinant-entry exact-support split."""

from __future__ import annotations

import cmath
import math
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
NOTE = DOCS / "THETA_MASS_ACTION_DETERMINANT_ENTRY_EXACT_SUPPORT_SPLIT_NOTE_2026-07-04.md"
EXHAUSTION = DOCS / "THETA_P2_DETERMINANT_READOUT_EXHAUSTION_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-11.md"
EPSILON_REALITY = DOCS / "THETA_MASS_SIDE_EPSILON_HERMITICITY_REALITY_BRIDGE_DISCHARGE_BOUNDED_THEOREM_NOTE_2026-06-11.md"
W2_NO_GO = DOCS / "THETA_MASS_W2_PHYSICAL_REGISTRABILITY_STRETCH_NO_GO_NOTE_2026-07-04.md"
REGISTRY = DOCS / "ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md"

PASS = 0
FAIL = 0


def flat(text: str) -> str:
    return " ".join(text.split())


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    ok = bool(ok)
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f" -- {detail}" if detail else ""
    print(f"{tag}: {label}{suffix}")


def section(title: str) -> None:
    print("\n" + "-" * 78)
    print(title)
    print("-" * 78)


def close(a: float, b: float, eps: float = 1.0e-12) -> bool:
    return abs(a - b) < eps


def angle_close(a: float, b: float, eps: float = 1.0e-12) -> bool:
    return abs(math.atan2(math.sin(a - b), math.cos(a - b))) < eps


def gr_mul(p: dict[int, sp.Expr], q: dict[int, sp.Expr]) -> dict[int, sp.Expr]:
    out: dict[int, sp.Expr] = {}
    for m1, c1 in p.items():
        for m2, c2 in q.items():
            if m1 & m2:
                continue
            sign = 1
            rest = m2
            while rest:
                low = rest & -rest
                bit = low.bit_length() - 1
                if bin(m1 >> (bit + 1)).count("1") % 2:
                    sign = -sign
                rest ^= low
            mask = m1 | m2
            out[mask] = out.get(mask, 0) + sign * c1 * c2
    return {mask: sp.simplify(coeff) for mask, coeff in out.items() if coeff != 0}


def gr_int(p: dict[int, sp.Expr], generator: int) -> dict[int, sp.Expr]:
    out: dict[int, sp.Expr] = {}
    bit = 1 << generator
    for mask, coeff in p.items():
        if not (mask & bit):
            continue
        below = bin(mask & (bit - 1)).count("1")
        sign = -1 if below % 2 else 1
        new_mask = mask ^ bit
        out[new_mask] = out.get(new_mask, 0) + sign * coeff
    return {mask: sp.simplify(coeff) for mask, coeff in out.items() if coeff != 0}


def exp_poly(action: dict[int, sp.Expr], max_degree: int) -> dict[int, sp.Expr]:
    expo: dict[int, sp.Expr] = {0: sp.Integer(1)}
    term: dict[int, sp.Expr] = {0: sp.Integer(1)}
    for degree in range(1, max_degree + 1):
        term = gr_mul(term, action)
        term = {mask: coeff / sp.Integer(degree) for mask, coeff in term.items() if coeff != 0}
        for mask, coeff in term.items():
            expo[mask] = expo.get(mask, 0) + coeff
    return {mask: sp.simplify(coeff) for mask, coeff in expo.items() if coeff != 0}


def bilinear_action(matrix: sp.Matrix, n: int) -> dict[int, sp.Expr]:
    action: dict[int, sp.Expr] = {}
    for i in range(n):
        for j in range(n):
            if matrix[i, j] == 0:
                continue
            gi = 2 * i
            gj = 2 * j + 1
            mask = (1 << gi) | (1 << gj)
            sign = 1 if gi < gj else -1
            action[mask] = action.get(mask, 0) + sign * matrix[i, j]
    return action


def berezin_partition_from_action(action: dict[int, sp.Expr], n: int) -> sp.Expr:
    out = exp_poly(action, 2 * n)
    for i in range(n):
        out = gr_int(out, 2 * i)
        out = gr_int(out, 2 * i + 1)
    return sp.simplify(out.get(0, 0))


def berezin_gaussian(matrix: sp.Matrix) -> sp.Expr:
    n = matrix.rows
    return berezin_partition_from_action(bilinear_action(matrix, n), n)


def main() -> int:
    print("Theta mass action determinant-entry exact-support split")
    print("=" * 78)

    note = NOTE.read_text(encoding="utf-8")
    exhaustion = EXHAUSTION.read_text(encoding="utf-8")
    epsilon_reality = EPSILON_REALITY.read_text(encoding="utf-8")
    w2_no_go = W2_NO_GO.read_text(encoding="utf-8")
    registry = REGISTRY.read_text(encoding="utf-8")

    note_flat = flat(note)
    exhaustion_flat = flat(exhaustion)
    epsilon_flat = flat(epsilon_reality)
    w2_flat = flat(w2_no_go)
    registry_flat = flat(registry)

    section("A - source boundaries")

    check("note declares bounded theorem claim type", "**Claim type:** bounded_theorem" in note)
    check("note status is exact-support split, not effective retained", "exact-support source-side split" in note_flat and "independent audit required" in note_flat)
    check(
        "note denies theta retirement, W2 derivation, registry edits, and gauge claim",
        "does not retire theta" in note_flat
        and "does not derive W2 physical registrability" in note_flat
        and "does not edit any Tier-A registry" in note_flat
        and "does not claim anything about the gauge-side winding residual" in note_flat,
    )
    check("runner path is wired in note", Path(__file__).name in note)

    section("B - existing sources name this split")

    check(
        "exhaustion bridge separates W2 and action-level determinant-entry premises",
        "W2 physical-registrability" in exhaustion
        and "action-level `theta_eff` determinant-entry" in exhaustion
        and "does **not** derive the W2 physical-registrability theorem" in exhaustion_flat
        and "or the action-level `theta_eff` determinant-entry theorem" in exhaustion_flat,
    )
    check(
        "epsilon-reality packet names the bilinear matter determinant half",
        "matter measure's only partition-level phase object is" in epsilon_flat
        and "`arg det`" in epsilon_reality
        and "first-power Berezin" in epsilon_flat
        and "Not** a claim beyond bilinear matter terms" in epsilon_reality,
    )
    check(
        "block25 keeps W2 open",
        "W2 physical registrability bridge remains live" in w2_flat
        and "does not prove that the physical mass-surface readout is that supplied determinant channel" in w2_flat,
    )
    check(
        "registry keeps theta mass side localized to determinant-readout bridge",
        "localized onto the named **determinant-readout bridge**" in registry,
    )

    section("C - exact Gaussian bilinear determinant entry")

    a, b, c, d, e, f, g, h, i = sp.symbols("a b c d e f g h i")
    k3 = sp.Matrix([[a, b, c], [d, e, f], [g, h, i]])
    z3 = berezin_gaussian(k3)
    check("explicit 3-pair Berezin expansion equals det K", sp.simplify(z3 - k3.det()) == 0)

    k2 = sp.Matrix([[a, b], [c, d]])
    z2 = berezin_gaussian(k2)
    check("explicit 2-pair Berezin expansion equals det K", sp.simplify(z2 - k2.det()) == 0)

    p, q, r = sp.symbols("p q r")
    k1 = sp.Matrix([[p]])
    block = sp.diag(k2, k1)
    check(
        "independent block sum multiplies determinant weights",
        sp.simplify(berezin_gaussian(block) - berezin_gaussian(k2) * berezin_gaussian(k1)) == 0,
    )

    z_a = 2.0 * cmath.exp(1j * math.pi / 5.0)
    z_b = 3.0 * cmath.exp(1j * math.pi / 7.0)
    phase_ok = angle_close(cmath.phase(z_a * z_b), cmath.phase(z_a) + cmath.phase(z_b))
    check("partition phase is additive modulo 2 pi under block product", phase_ok)

    alpha = math.pi / 8.0
    k_alpha = complex(1.25 * cmath.exp(1j * alpha))
    check(
        "K/CPT conjugation pairs determinant weights by alpha -> -alpha",
        abs(k_alpha.conjugate() - 1.25 * cmath.exp(-1j * alpha)) < 1e-12
        and angle_close(cmath.phase(k_alpha.conjugate()), -cmath.phase(k_alpha)),
    )

    section("D - hostile guards")

    x, y, u, v, quartic = sp.symbols("x y u v quartic")
    kq = sp.Matrix([[x, y], [u, v]])
    action = bilinear_action(kq, 2)
    top_mask = (1 << 0) | (1 << 1) | (1 << 2) | (1 << 3)
    action_with_quartic = dict(action)
    action_with_quartic[top_mask] = action_with_quartic.get(top_mask, 0) + quartic
    z_quartic = berezin_partition_from_action(action_with_quartic, 2)
    check(
        "quartic non-Gaussian witness leaves supplied Gaussian class",
        sp.simplify(z_quartic - kq.det() - quartic) == 0,
        f"Z = {sp.factor(z_quartic)}",
    )

    same_det_a = sp.diag(sp.Integer(2), sp.Integer(3))
    same_det_b = sp.diag(sp.Integer(1), sp.Integer(6))
    check(
        "same determinant can have different inverse insertion data",
        same_det_a.det() == same_det_b.det()
        and same_det_a.inv()[0, 0] != same_det_b.inv()[0, 0],
        f"det={same_det_a.det()}, inv00={same_det_a.inv()[0, 0]} vs {same_det_b.inv()[0, 0]}",
    )

    check(
        "note explicitly excludes non-Gaussian and source/insertion overreach",
        "Non-Gaussian matter is outside the theorem" in note
        and "Source and insertion observables are outside the theorem" in note,
    )
    check("note keeps W2 open", "W2 is not supplied here" in note and "does not prove that the physical readout context is W2 Record-registrable" in note_flat)

    section("E - trace and no-overclaim checks")

    check("note says the split is useful but not retirement authority", "It must still be composed with a separate W2 theorem" in note)
    check("note leaves physical action-surface selection open", "does not derive that surface" in note and "Physical action-surface selection" in note)
    check("remaining live routes include W2 and action-surface derivation", "Derive or explicitly approve W2 physical registrability" in note and "physical mass action really lies on this supplied Gaussian" in note)

    banned = [
        "theta is retired",
        "retires theta",
        "w2 is derived",
        "physical action surface is selected",
        "tier-a registry is edited",
        "gauge-side winding is solved",
    ]
    found = [phrase for phrase in banned if phrase in note_flat.lower()]
    check("banned overclaim phrases are absent", not found, str(found))

    print("\n" + "=" * 78)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
