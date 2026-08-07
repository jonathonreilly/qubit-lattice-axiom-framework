#!/usr/bin/env python3
"""Y_T source-Higgs pole-row normalization no-go runner.

Authority note:
    docs/YT_SOURCE_HIGGS_POLE_ROW_NORMALIZATION_NO_GO_NOTE_2026-05-23.md

The runner checks the narrow claim that strict single-pole rows and
Gram-purity evidence certify common-pole support but do not fix absolute
operator normalization. Consequently, pole rows alone cannot derive the
Yukawa-side selector kappa_Y=0.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
NOTE = DOCS / "YT_SOURCE_HIGGS_POLE_ROW_NORMALIZATION_NO_GO_NOTE_2026-05-23.md"
STATUS_NOTE = DOCS / "YT_SOURCE_ACTION_SUPPORT_PACKET_NOTE_2026-05-22.md"
COLOR_NOTE = DOCS / "YT_COLOR_PROJECTION_CORRECTION_NOTE.md"
SCALE_NOTE = DOCS / "OBSERVABLE_PRINCIPLE_SCALE_INVARIANT_SOURCE_RESPONSE_NARROW_THEOREM_NOTE_2026-05-16.md"

PASS_COUNT = 0
FAIL_COUNT = 0


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def check(name: str, passed: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    if passed:
        PASS_COUNT += 1
        tag = "PASS"
    else:
        FAIL_COUNT += 1
        tag = "FAIL"
    suffix = f": {detail}" if detail else ""
    print(f"[{tag}] {name}{suffix}")


def k_y(kappa_y: Fraction) -> Fraction:
    return Fraction(8, 9) + kappa_y * Fraction(1, 9)


@dataclass(frozen=True)
class PoleRow:
    a_s: Fraction
    a_h: Fraction
    q: Fraction
    t: int

    @property
    def e_t(self) -> Fraction:
        return self.q ** self.t

    @property
    def e_t_plus_one(self) -> Fraction:
        return self.q ** (self.t + 1)

    @property
    def c_ss(self) -> Fraction:
        return self.a_s * self.a_s * self.e_t

    @property
    def c_sh(self) -> Fraction:
        return self.a_s * self.a_h * self.e_t

    @property
    def c_hh(self) -> Fraction:
        return self.a_h * self.a_h * self.e_t

    @property
    def c_ss_next(self) -> Fraction:
        return self.a_s * self.a_s * self.e_t_plus_one

    @property
    def gram_det(self) -> Fraction:
        return self.c_sh * self.c_sh - self.c_ss * self.c_hh

    @property
    def mass_ratio(self) -> Fraction:
        # exp(m) in the usual C(t) / C(t+1) effective-mass extraction.
        return self.c_ss / self.c_ss_next

    def rescale(self, mu: Fraction, lam: Fraction) -> "PoleRow":
        return PoleRow(
            a_s=mu * self.a_s,
            a_h=lam * self.a_h,
            q=self.q,
            t=self.t,
        )


def main() -> int:
    print("=" * 78)
    print("Y_T SOURCE-HIGGS POLE-ROW NORMALIZATION NO-GO")
    print("=" * 78)

    note = read(NOTE)
    status_note = read(STATUS_NOTE)
    color_note = read(COLOR_NOTE)
    scale_note = read(SCALE_NOTE)

    print("\nPart 0: source and context anchors")
    check("source note exists", NOTE.exists(), str(NOTE.relative_to(ROOT)))
    check("Y_T source-action consolidated status note exists", STATUS_NOTE.exists(), str(STATUS_NOTE.relative_to(ROOT)))
    check("color-projection correction note exists", COLOR_NOTE.exists(), str(COLOR_NOTE.relative_to(ROOT)))
    check("scale-invariant source-response note exists", SCALE_NOTE.exists(), str(SCALE_NOTE.relative_to(ROOT)))
    check("source note is typed no_go", "**Claim type:** no_go" in note)
    check(
        "source note registers this runner",
        "scripts/frontier_yt_source_higgs_pole_row_normalization_no_go.py" in note,
    )
    check(
        "Y_T source-action status exposes canonical LSZ as an open gate",
        "Derive canonical `O_H` and scalar LSZ normalization" in status_note,
    )
    check(
        "color note exposes kappa family",
        "K_Y(kappa_Y) = F_adj + kappa_Y * F_singlet" in color_note
        and "8/9 + kappa_Y/9" in color_note,
    )
    check(
        "scale note supplies ratio-invariance analogy",
        "overall scale `c` cancels exactly" in scale_note,
    )

    print("\nPart 1: exact pole-row Gram purity")
    base = PoleRow(a_s=Fraction(5, 3), a_h=Fraction(7, 4), q=Fraction(5, 7), t=3)
    check("base Gram determinant vanishes", base.gram_det == 0, str(base.gram_det))
    check("base effective-mass ratio is amplitude-blind q^-1", base.mass_ratio == Fraction(7, 5), str(base.mass_ratio))
    check("single-pole residues are nonzero", base.c_ss > 0 and base.c_sh > 0 and base.c_hh > 0)

    print("\nPart 2: source/Higgs rescaling invariance")
    scalings = [
        (Fraction(2, 1), Fraction(3, 1)),
        (Fraction(3, 5), Fraction(11, 7)),
        (Fraction(13, 17), Fraction(19, 23)),
        (Fraction(9, 8), Fraction(8, 9)),
    ]
    for mu, lam in scalings:
        row = base.rescale(mu=mu, lam=lam)
        check(f"Gram determinant invariant at mu={mu}, lambda={lam}", row.gram_det == 0)
        check(
            f"mass ratio invariant at mu={mu}, lambda={lam}",
            row.mass_ratio == base.mass_ratio,
            str(row.mass_ratio),
        )
        check(
            f"C_ss scales by mu^2 at mu={mu}",
            row.c_ss == mu * mu * base.c_ss,
            str(row.c_ss),
        )
        check(
            f"C_HH scales by lambda^2 at lambda={lam}",
            row.c_hh == lam * lam * base.c_hh,
            str(row.c_hh),
        )

    print("\nPart 3: normalized residue ratios do not fix amplitudes")
    normalized = base.c_sh * base.c_sh / (base.c_ss * base.c_hh)
    check("normalized rank-one residue ratio equals one", normalized == 1, str(normalized))
    for mu, lam in scalings[:3]:
        row = base.rescale(mu=mu, lam=lam)
        ratio = row.c_sh * row.c_sh / (row.c_ss * row.c_hh)
        check(f"normalized residue ratio stays one at mu={mu}, lambda={lam}", ratio == 1, str(ratio))

    print("\nPart 4: kappa_Y ambiguity is absorbable by normalization")
    k_connected = k_y(Fraction(0))
    k_full = k_y(Fraction(1))
    lambda_squared = k_full / k_connected
    check("K_Y(kappa=0)=8/9", k_connected == Fraction(8, 9), str(k_connected))
    check("K_Y(kappa=1)=1", k_full == 1, str(k_full))
    check("full/connected squared-normalization ratio is 9/8", lambda_squared == Fraction(9, 8), str(lambda_squared))
    check(
        "lambda^2=9/8 absorbs connected normalization into full-trace normalization",
        k_connected * lambda_squared == k_full,
        f"{k_connected} * {lambda_squared} = {k_connected * lambda_squared}",
    )
    check(
        "pole-row equations do not contain kappa_Y",
        "kappa_Y" not in PoleRow.__annotations__,
        str(PoleRow.__annotations__.keys()),
    )

    print("\nPart 5: note claim-boundary guards")
    required_phrases = [
        "common-pole support",
        "cannot by themselves derive the Yukawa-side selector",
        "canonical scalar LSZ normalization",
        "not a global no-go for Y_T",
        "does not mean positive Y_T closure has been obtained",
        "does not use `H_unit`",
    ]
    for phrase in required_phrases:
        check(f"source contains boundary phrase {phrase!r}", phrase in note)
    forbidden_phrases = [
        "This proves positive Y_T closure",
        "Y_T is closed by pole rows",
        "kappa_Y = 0 is derived",
        "proposed_retained",
        "PDG",
        "m_t(pole)",
        "y_t(v)",
    ]
    for phrase in forbidden_phrases:
        check(f"source avoids overclaim/import phrase {phrase!r}", phrase not in note)

    print()
    print("=" * 78)
    print("N5 EXECUTION CERTIFICATE")
    print("=" * 78)
    dets_after = sorted({str(base.rescale(mu, lam).gram_det) for mu, lam in scalings})
    ratios_after = sorted({str(base.rescale(mu, lam).mass_ratio) for mu, lam in scalings})
    print(
        f"per_element: the two-by-two residue Gram of the source and Higgs "
        f"interpolators is formed explicitly from exact rationals — with "
        f"amplitudes a_S = {base.a_s}, a_H = {base.a_h} and pole factor "
        f"q = {base.q} at separation t = {base.t}, the entries C_SS = "
        f"{base.c_ss}, C_SH = {base.c_sh} and C_HH = {base.c_hh} are all "
        f"strictly positive while the determinant C_SH^2 - C_SS C_HH is "
        f"exactly {base.gram_det}, so the matrix is rank one entry for entry."
    )
    print(
        f"per_site: checked and not executed — the only index this runner "
        f"carries is a Euclidean time separation, evaluated at t = {base.t} "
        f"and t = {base.t + 1} inside a closed-form geometric row; no spatial "
        f"site, link or volume is instantiated, so nothing is decided per "
        f"site."
    )
    print(
        f"per_mode: exactly one pole mode is present and it is resolved "
        f"cleanly — C(t) = a^2 q^t yields the effective-mass ratio "
        f"C(t)/C(t+1) = {base.mass_ratio} in exact arithmetic, and that ratio "
        f"is unchanged under every tested amplitude rescaling "
        f"(values {ratios_after}), so the mode location is pinned while the "
        f"mode amplitude is not."
    )
    print(
        f"per_block: the source/Higgs operator block is where the no-go bites "
        f"— across {len(scalings)} independent rescalings (mu, lambda) the "
        f"Gram determinant stays {dets_after}, C_SS scales as mu^2 and C_HH "
        f"as lambda^2, the normalized residue ratio C_SH^2/(C_SS C_HH) stays "
        f"exactly {normalized}, and the whole kappa_Y ambiguity is absorbed by "
        f"the single block normalization lambda^2 = {lambda_squared} carrying "
        f"K_Y from {k_connected} to {k_full}."
    )
    print(
        f"lattice_wide: checked and not executed — a pole row at fixed "
        f"separation says nothing about extent, and neither a volume, a "
        f"boundary condition nor a continuum limit appears anywhere in this "
        f"file; 22 of its {PASS_COUNT + FAIL_COUNT} checks are source-document "
        f"reads (4 file-existence tests and 18 substring assertions) that "
        f"resolve nothing numerical."
    )
    print("=" * 78)
    print(f"RESULT: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    print("=" * 78)
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
