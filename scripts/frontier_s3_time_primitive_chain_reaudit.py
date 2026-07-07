#!/usr/bin/env python3
"""Review helper for S3_TIME_PRIMITIVE_CHAIN_NOTE.

The runner verifies the bounded conditional recut:

* the row is typed as a bounded theorem with named supplied premises;
* the displayed load-bearing matrix and endpoint images match recomputation;
* motivation-tier numerics are informational only;
* the no-go boundary and downstream firewall remain prominent.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from fractions import Fraction
from pathlib import Path
import re
import sys

import numpy as np

from frontier_quark_route2_exact_readout_map import restricted_readout_data


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
EXACT_TOL = 1.0e-12
READOUT_NOTE_NAME = "QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md"
TIME_NOTE_NAME = "QUARK_ROUTE2_EXACT_TIME_COUPLING_NOTE_2026-04-19.md"
NO_GO_NOTE_NAME = "QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md"

EXPECTED_PREMISE_BLOCK = """\
ENDPOINT-QE (named conditional premise): the E-channel center/shell endpoint
quotient is SUPPLIED as gamma_E(center)/gamma_E(shell) = 15/8; equivalently
rho_E = beta_E/alpha_E = 21/4 (rho_E is written r_E in the endpoint notes)
via the exact identity rho_E = 6*(q_E - 1); equivalently, granted ENDPOINT-RT
and SHELL-MULT, the center ratio gamma_T(center)/gamma_E(center) = -8/9.
Not derived: the no-go note
QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md, used at
its audited no-go scope, proves the restricted Route-2 carrier/readout class
leaves rho_E free unless an additional E-center endpoint ratio,
source-domain, or readout-map primitive is supplied.

ENDPOINT-RT (named conditional premise): the T-channel center/shell endpoint
quotient is SUPPLIED as gamma_T(center)/gamma_T(shell) = 5/6; equivalently
r_T = beta_T/alpha_T = -1.

SHELL-MULT (named conditional premise): the shell coefficient ratio
(historically the shell-multiplicity candidate) is SUPPLIED as
a_T/a_E = alpha_T/alpha_E = -2."""

DISPLAYED_MATRIX_LINES = [
    "P_R^prem =",
    "[[1, 0, 21/4, 0],",
    " [0, -2, 0, 2]]",
]

DISPLAYED_IMAGE_LINES = [
    "P_R^prem E-shell  = (1, 0)",
    "P_R^prem E-center = (15/8, 0)",
    "P_R^prem T-shell  = (0, -2)",
    "P_R^prem T-center = (0, -5/3)",
]

FIREWALL_REQUIRED_PHRASES = [
    "Downstream source-boundary firewall",
    "cite the exact Route-2 carrier/readout/time authority chain",
    "cite the admissibility boundary",
    "leaves `beta_E / alpha_E` free",
    "derive an additional E-center endpoint ratio, source-domain, or",
    "do not cite this packet as a derivation of `beta_E / alpha_E = 21/4`",
    "do not cite it as a unique readout-to-slice time-coupling theorem",
    "do not cite it as final Einstein/Regge identification",
    "do not cite the granted T-side candidates as selecting the E-channel ratio",
    "do not use the Route-2 no-go as an exhaustive no-go",
    "do not promote this packet to a positive readout theorem",
    "promotion to a positive or unconditional readout theorem still requires",
    "the named premises may not be cited as derived",
]

MOTIVATION_REQUIRED_PHRASES = [
    "Motivation exhibit",
    "evidence only; not load-bearing; no value below is consumed by any claim",
    "nearest-rational scan",
    "-1.000030814262",
    "-2.005382749600",
    "5.257476782081",
]


@dataclass
class Counter:
    passed: int = 0
    failed: int = 0
    failures: list[str] = field(default_factory=list)

    def check(self, name: str, condition: bool, detail: str = "") -> None:
        if condition:
            self.passed += 1
            return
        self.failed += 1
        self.failures.append(f"{name}: {detail}" if detail else name)


def squash(text: str) -> str:
    return " ".join(text.split())


def section_after_heading(text: str, heading: str, next_heading: str) -> str:
    start = text.index(heading) + len(heading)
    end = text.index(next_heading, start)
    return text[start:end].strip()


def fenced_block_after(text: str, marker: str) -> str:
    marker_pos = text.index(marker) + len(marker)
    match = re.search(
        r"(?P<fence>`{3,})text\n(?P<body>.*?)(?P=fence)",
        text[marker_pos:],
        re.DOTALL,
    )
    return match.group("body").rstrip() if match else ""


def premise_block(note_text: str) -> str:
    match = re.search(
        r"## Named conditional premises\n\n```text\n(.*?)\n```",
        note_text,
        re.DOTALL,
    )
    return match.group(1) if match else ""


def parse_fraction(block: str, pattern: str) -> Fraction | None:
    match = re.search(pattern, block)
    return Fraction(match.group(1)) if match else None


def parse_premises(block: str) -> dict[str, Fraction | None]:
    return {
        "q_e": parse_fraction(
            block,
            r"gamma_E\(center\)/gamma_E\(shell\) = (-?\d+(?:/\d+)?)",
        ),
        "rho_e": parse_fraction(
            block,
            r"rho_E = beta_E/alpha_E = (-?\d+(?:/\d+)?)",
        ),
        "c_te": parse_fraction(
            block,
            r"gamma_T\(center\)/gamma_E\(center\) = (-?\d+(?:/\d+)?)",
        ),
        "q_t": parse_fraction(
            block,
            r"gamma_T\(center\)/gamma_T\(shell\) = (-?\d+(?:/\d+)?)",
        ),
        "rho_t": parse_fraction(
            block,
            r"r_T = beta_T/alpha_T = (-?\d+(?:/\d+)?)",
        ),
        "s_te": parse_fraction(
            block,
            r"a_T/a_E = alpha_T/alpha_E = (-?\d+(?:/\d+)?)",
        ),
    }


def mat_vec(
    rows: list[list[Fraction]], vec: tuple[Fraction, ...]
) -> tuple[Fraction, ...]:
    return tuple(
        sum((coef * comp for coef, comp in zip(row, vec)), Fraction(0))
        for row in rows
    )


def max_abs_delta(actual, expected) -> float:
    actual_arr = np.array([float(v) for v in np.ravel(actual)], dtype=float)
    expected_arr = np.array([float(v) for v in np.ravel(expected)], dtype=float)
    return float(np.max(np.abs(actual_arr - expected_arr)))


def check_note_and_sources(load: Counter, note_text: str, source_texts: dict[str, str]) -> None:
    note_flat = squash(note_text)
    readout_text = source_texts["readout"]
    time_text = source_texts["time"]
    no_go_text = source_texts["no_go"]
    theorem = section_after_heading(no_go_text, "## 6. Theorem", "## 7.")
    section4 = section_after_heading(no_go_text, "## 4. What Would Force 21/4", "## 5.")
    section4_trio = section4.split("So `21/4` is not mysterious", maxsplit=1)[0].rstrip()
    section6_quote = fenced_block_after(
        note_text,
        "Section 6 of the no-go note, quoted verbatim:",
    )
    section4_quote = fenced_block_after(
        note_text,
        "Section 4 of the no-go note, quoted verbatim:",
    )

    load.check("claim_id is unchanged", "claim_id: s3_time_primitive_chain_note" in note_text)
    load.check("row is typed bounded_theorem", "**Type:** bounded_theorem" in note_text)
    load.check("row is not typed open_gate", "**Type:** open_gate" not in note_text)
    load.check(
        "new-structure disclaimer is explicit",
        "named supplied premises below are conditional assumptions" in note_flat,
    )
    load.check("note cites exact readout map file", READOUT_NOTE_NAME in note_text)
    load.check("note cites exact time-coupling file", TIME_NOTE_NAME in note_text)
    load.check("note cites E-channel no-go file", NO_GO_NOTE_NAME in note_text)
    load.check(
        "note seeds exact readout map dependency with inline markdown link",
        f"[{READOUT_NOTE_NAME}]({READOUT_NOTE_NAME})" in note_text,
    )
    load.check(
        "note seeds exact time-coupling dependency with inline markdown link",
        f"[{TIME_NOTE_NAME}]({TIME_NOTE_NAME})" in note_text,
    )
    load.check(
        "note seeds no-go dependency with inline markdown link",
        f"[{NO_GO_NOTE_NAME}]({NO_GO_NOTE_NAME})" in note_text,
    )
    load.check(
        "readout authority states restricted class",
        "gamma_E = alpha_E u_E + beta_E delta_A1 u_E" in readout_text,
    )
    load.check(
        "time authority keeps unique theorem blocked",
        "does not yet exist as a unique theorem" in time_text
        or "does **not** determine one unique exact" in time_text,
    )
    load.check(
        "Section 6 theorem fenced quote matches source",
        section6_quote == theorem,
    )
    load.check(
        "Section 4 equivalence fenced quote matches source",
        section4_quote == section4_trio,
    )
    load.check(
        "no-go paraphrases use source vocabulary",
        "additional E-center endpoint ratio, source-domain, or readout-map primitive"
        in note_flat
        and "source-domain rule, or stronger readout" not in note_text,
    )
    load.check("Xi_R/Xi_P alias is declared once", note_text.count("Xi_P") == 1)
    load.check(
        "firewall includes all required needles",
        all(phrase in note_flat for phrase in FIREWALL_REQUIRED_PHRASES),
    )


def check_premise_algebra(load: Counter, note_text: str) -> None:
    block = premise_block(note_text)
    values = parse_premises(block)
    missing = ", ".join(sorted(key for key, value in values.items() if value is None))
    load.check("named premise block matches panel text", block == EXPECTED_PREMISE_BLOCK)
    load.check("all premise fractions parse from note text", not missing, missing)
    if missing:
        return

    q_e = values["q_e"]
    rho_e = values["rho_e"]
    c_te = values["c_te"]
    q_t = values["q_t"]
    rho_t = values["rho_t"]
    s_te = values["s_te"]
    assert q_e is not None
    assert rho_e is not None
    assert c_te is not None
    assert q_t is not None
    assert rho_t is not None
    assert s_te is not None

    alpha_e = Fraction(1, 1)
    beta_e = alpha_e * rho_e
    alpha_t = s_te * alpha_e
    beta_t = alpha_t * rho_t
    p_rows = [
        [alpha_e, Fraction(0), beta_e, Fraction(0)],
        [Fraction(0), alpha_t, Fraction(0), beta_t],
    ]
    p_prem = p_rows

    load.check(
        "premise fractions build the displayed P_R coefficients",
        (alpha_e, beta_e, alpha_t, beta_t)
        == (Fraction(1), Fraction(21, 4), Fraction(-2), Fraction(2)),
    )
    load.check(
        "displayed P_R rows appear in note",
        all(line in note_text for line in DISPLAYED_MATRIX_LINES),
    )
    load.check(
        "displayed endpoint image lines appear in note",
        all(line in note_text for line in DISPLAYED_IMAGE_LINES),
    )

    carrier_columns: dict[str, tuple[Fraction, ...]] = {
        "E-shell": (Fraction(1), Fraction(0), Fraction(0), Fraction(0)),
        "E-center": (Fraction(1), Fraction(0), Fraction(1, 6), Fraction(0)),
        "T-shell": (Fraction(0), Fraction(1), Fraction(0), Fraction(0)),
        "T-center": (Fraction(0), Fraction(1), Fraction(0), Fraction(1, 6)),
    }

    images = {
        name: mat_vec(p_prem, vector) for name, vector in carrier_columns.items()
    }
    expected_images = {
        "E-shell": (alpha_e, Fraction(0)),
        "E-center": (alpha_e + beta_e / 6, Fraction(0)),
        "T-shell": (Fraction(0), alpha_t),
        "T-center": (Fraction(0), alpha_t + beta_t / 6),
    }
    for name, expected in expected_images.items():
        load.check(
            f"{name} image matches independent fraction route (exact)",
            images[name] == expected,
        )

    q_t_affine = Fraction(1) + rho_t / 6
    s_te_affine = alpha_t / alpha_e
    q_e_affine = Fraction(1) + rho_e / 6
    c_te_affine = s_te_affine * q_t_affine / q_e_affine
    load.check(
        "affine quotient identities match supplied endpoint quartet",
        (q_t_affine, s_te_affine, q_e_affine, c_te_affine) == (q_t, s_te, q_e, c_te),
    )

    q_t_matrix = images["T-center"][1] / images["T-shell"][1]
    s_te_matrix = images["T-shell"][1] / images["E-shell"][0]
    q_e_matrix = images["E-center"][0] / images["E-shell"][0]
    c_te_matrix = images["T-center"][1] / images["E-center"][0]
    load.check(
        "matrix endpoint quotients match affine quotient identities (exact)",
        (q_t_matrix, s_te_matrix, q_e_matrix, c_te_matrix)
        == (q_t_affine, s_te_affine, q_e_affine, c_te_affine),
    )

    p_zero = [
        [alpha_e, Fraction(0), Fraction(0), Fraction(0)],
        [Fraction(0), alpha_t, Fraction(0), beta_t],
    ]
    zero_center = mat_vec(p_zero, carrier_columns["E-center"])
    target_center = mat_vec(p_prem, carrier_columns["E-center"])
    load.check(
        "rho_E remains non-selected by shell normalization (exact)",
        zero_center[0] != target_center[0]
        and zero_center[0] == alpha_e
        and mat_vec(p_zero, carrier_columns["E-shell"]) == images["E-shell"],
    )


def check_motivation(motivation: Counter, note_text: str) -> None:
    note_flat = squash(note_text)
    for phrase in MOTIVATION_REQUIRED_PHRASES:
        motivation.check(f"motivation needle {phrase}", phrase in note_flat)
    exact_columns = {
        "E-shell": (Fraction(1), Fraction(0), Fraction(0), Fraction(0)),
        "E-center": (Fraction(1), Fraction(0), Fraction(1, 6), Fraction(0)),
        "T-shell": (Fraction(0), Fraction(1), Fraction(0), Fraction(0)),
        "T-center": (Fraction(0), Fraction(1), Fraction(0), Fraction(1, 6)),
    }
    data = restricted_readout_data()
    replay_columns = {
        "E-shell": data.carrier_e_shell,
        "E-center": data.carrier_e_center,
        "T-shell": data.carrier_t_shell,
        "T-center": data.carrier_t_center,
    }
    motivation.check(
        "live replay carrier columns track the exact columns (float tolerance)",
        max(
            max_abs_delta(replay_columns[name], exact_columns[name])
            for name in exact_columns
        )
        < EXACT_TOL,
    )


def print_failures(label: str, counter: Counter, limit: int = 3) -> None:
    if not counter.failures:
        return
    print(f"{label} FAILURES (first {min(limit, len(counter.failures))}):")
    for failure in counter.failures[:limit]:
        print(f"- {failure}")
    if len(counter.failures) > limit:
        print(f"- ... {len(counter.failures) - limit} more")


def main() -> int:
    load = Counter()
    motivation = Counter()
    note = DOCS / "S3_TIME_PRIMITIVE_CHAIN_NOTE.md"
    readout = DOCS / READOUT_NOTE_NAME
    time = DOCS / TIME_NOTE_NAME
    no_go = DOCS / NO_GO_NOTE_NAME
    paths = {"note": note, "readout": readout, "time": time, "no_go": no_go}

    for key, path in paths.items():
        load.check(f"{key} file exists", path.exists(), str(path.relative_to(ROOT)))
    if load.failed:
        note_text = ""
        source_texts = {"readout": "", "time": "", "no_go": ""}
    else:
        note_text = note.read_text(encoding="utf-8")
        source_texts = {
            "readout": readout.read_text(encoding="utf-8"),
            "time": time.read_text(encoding="utf-8"),
            "no_go": no_go.read_text(encoding="utf-8"),
        }
        check_note_and_sources(load, note_text, source_texts)
        check_premise_algebra(load, note_text)
        check_motivation(motivation, note_text)

    print("S3 primitive-chain conditional bounded-theorem re-audit helper")
    print(f"LOAD-BEARING: PASS={load.passed} FAIL={load.failed}")
    print_failures("LOAD-BEARING", load)
    print("MOTIVATION-TIER (non-load-bearing; does not affect exit status)")
    print(f"MOTIVATION: PASS={motivation.passed} FAIL={motivation.failed}")
    print_failures("MOTIVATION", motivation, limit=1)
    print(f"TOTAL: PASS={load.passed} FAIL={load.failed}")
    if load.failed:
        print("VERDICT: S3 primitive-chain conditional bounded checks failed.")
        return 1
    print("VERDICT: conditional bounded theorem checks passed; motivation is non-fatal.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
