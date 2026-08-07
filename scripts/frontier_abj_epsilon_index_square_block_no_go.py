#!/usr/bin/env python3
"""No-go: the standard staggered epsilon index vanishes on even Z4 tori.

This runner checks the algebra behind the ABJ residual P1':

    A_t[U] = Tr(eps exp(-t D[U]^dag D[U]))

for the massless nearest-neighbor staggered Dirac operator on finite even
periodic Z^4 tori with U(1) link phases.  In epsilon-parity order the operator
has square bipartite form

    D = [[0, B], [-B^dag, 0]]

with equal plus/minus sublattice sizes.  Therefore BB^dag and B^dag B have the
same spectrum including zero multiplicity, so A_t[U] = 0 for every background U.
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np


PASS = 0
FAIL = 0
CHECKS: list[dict[str, object]] = []


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        status = "PASS"
    else:
        FAIL += 1
        status = "FAIL"
    CHECKS.append({"name": name, "status": status, "detail": detail})
    print(f"[{status}] {name}" + (f"  {detail}" if detail else ""))


def site_index(coords: tuple[int, int, int, int], dims: tuple[int, int, int, int]) -> int:
    t, x, y, z = coords
    lt, lx, ly, lz = dims
    return (((t % lt) * lx + (x % lx)) * ly + (y % ly)) * lz + (z % lz)


def coords_from_index(i: int, dims: tuple[int, int, int, int]) -> tuple[int, int, int, int]:
    lt, lx, ly, lz = dims
    z = i % lz
    i //= lz
    y = i % ly
    i //= ly
    x = i % lx
    t = i // lx
    return t, x, y, z


def eta(mu: int, coords: tuple[int, int, int, int]) -> int:
    return 1 if sum(coords[:mu]) % 2 == 0 else -1


def epsilon(coords: tuple[int, int, int, int]) -> int:
    return 1 if sum(coords) % 2 == 0 else -1


def random_u1_links(dims: tuple[int, int, int, int], seed: int) -> np.ndarray:
    rng = np.random.default_rng(seed)
    n = int(np.prod(dims))
    phases = rng.uniform(-np.pi, np.pi, size=(n, 4))
    return np.exp(1j * phases)


def flux_u1_links(dims: tuple[int, int, int, int], n_tx: int = 1, n_yz: int = 1) -> np.ndarray:
    """A periodic constant-flux-style U(1) background on the tx and yz planes."""
    lt, lx, ly, lz = dims
    links = np.ones((int(np.prod(dims)), 4), dtype=complex)
    for i in range(int(np.prod(dims))):
        t, x, y, z = coords_from_index(i, dims)
        # Landau-gauge implementation with boundary twist for each plane.
        links[i, 0] *= np.exp(2j * np.pi * n_tx * x / (lt * lx))
        if x == lx - 1:
            links[i, 1] *= np.exp(-2j * np.pi * n_tx * t / lt)
        links[i, 2] *= np.exp(2j * np.pi * n_yz * z / (ly * lz))
        if z == lz - 1:
            links[i, 3] *= np.exp(-2j * np.pi * n_yz * y / ly)
    return links


def staggered_dirac(dims: tuple[int, int, int, int], links: np.ndarray) -> np.ndarray:
    n = int(np.prod(dims))
    d = np.zeros((n, n), dtype=complex)
    for i in range(n):
        c = coords_from_index(i, dims)
        for mu in range(4):
            forward = list(c)
            forward[mu] += 1
            j_f = site_index(tuple(forward), dims)
            backward = list(c)
            backward[mu] -= 1
            j_b = site_index(tuple(backward), dims)
            phase = eta(mu, c)
            d[i, j_f] += 0.5 * phase * links[i, mu]
            d[i, j_b] += -0.5 * phase * np.conjugate(links[j_b, mu])
    return d


def analyze_background(label: str, dims: tuple[int, int, int, int], links: np.ndarray) -> dict[str, object]:
    print(f"\n== {label}: dims={dims} ==")
    d = staggered_dirac(dims, links)
    n = d.shape[0]
    eps_diag = np.array([epsilon(coords_from_index(i, dims)) for i in range(n)])
    eps = np.diag(eps_diag)
    plus = np.where(eps_diag == 1)[0]
    minus = np.where(eps_diag == -1)[0]
    order = np.concatenate([plus, minus])
    d_ord = d[np.ix_(order, order)]
    np_ = len(plus)
    nm = len(minus)
    b = d_ord[:np_, np_:]
    lower = d_ord[np_:, :np_]
    upper_left = d_ord[:np_, :np_]
    lower_right = d_ord[np_:, np_:]

    antiherm = float(np.max(np.abs(d + d.conj().T)))
    anticomm = float(np.max(np.abs(eps @ d @ eps + d)))
    ul = float(np.max(np.abs(upper_left))) if upper_left.size else 0.0
    lr = float(np.max(np.abs(lower_right))) if lower_right.size else 0.0
    block_relation = float(np.max(np.abs(lower + b.conj().T))) if b.size else 0.0

    check(f"{label}: equal epsilon sublattice sizes", np_ == nm, f"N_+={np_}, N_-={nm}")
    check(f"{label}: D anti-Hermitian", antiherm < 1e-12, f"max={antiherm:.3e}")
    check(f"{label}: eps D eps = -D", anticomm < 1e-12, f"max={anticomm:.3e}")
    check(f"{label}: diagonal parity blocks vanish", max(ul, lr) < 1e-12, f"max={max(ul, lr):.3e}")
    check(f"{label}: lower block equals -B^dag", block_relation < 1e-12, f"max={block_relation:.3e}")

    bb = b @ b.conj().T
    btb = b.conj().T @ b
    eval_bb = np.sort(np.linalg.eigvalsh(bb))
    eval_btb = np.sort(np.linalg.eigvalsh(btb))
    spectral_gap = float(np.max(np.abs(eval_bb - eval_btb)))
    check(f"{label}: BB^dag and B^dagB spectra match including zeros", spectral_gap < 1e-10, f"max={spectral_gap:.3e}")

    traces = {}
    dd = d.conj().T @ d
    for t in [0.1, 0.5, 1.0, 2.0]:
        vals, vecs = np.linalg.eigh(dd)
        expdd = (vecs * np.exp(-t * vals)) @ vecs.conj().T
        a_t = np.trace(eps @ expdd)
        traces[str(t)] = {"real": float(np.real(a_t)), "imag": float(np.imag(a_t))}
        check(f"{label}: A_t vanishes at t={t}", abs(a_t) < 1e-9, f"A_t={a_t.real:.3e}+{a_t.imag:.3e}i")

    zero_b = int(np.sum(eval_bb < 1e-10))
    zero_btb = int(np.sum(eval_btb < 1e-10))
    check(f"{label}: zero-mode multiplicities match", zero_b == zero_btb, f"ker BBdag={zero_b}, ker BdagB={zero_btb}")

    return {
        "label": label,
        "dims": dims,
        "n_plus": np_,
        "n_minus": nm,
        "max_antihermitian_error": antiherm,
        "max_eps_anticommutator_error": anticomm,
        "max_block_relation_error": block_relation,
        "max_spectrum_difference": spectral_gap,
        "zero_multiplicity_plus": zero_b,
        "zero_multiplicity_minus": zero_btb,
        "a_t": traces,
    }


def synthetic_rectangular_control() -> dict[str, object]:
    """Show that non-zero epsilon index requires leaving square-block form."""
    rng = np.random.default_rng(20260530)
    b = rng.normal(size=(5, 4)) + 1j * rng.normal(size=(5, 4))
    bb = b @ b.conj().T
    btb = b.conj().T @ b
    t = 0.7
    tr_plus = float(np.sum(np.exp(-t * np.linalg.eigvalsh(bb))))
    tr_minus = float(np.sum(np.exp(-t * np.linalg.eigvalsh(btb))))
    a_t = tr_plus - tr_minus
    check(
        "rectangular control: epsilon trace can be nonzero only after sublattice imbalance",
        abs(a_t - 1.0) < 1e-9,
        f"N_+-N_-=1, A_t={a_t:.12f}",
    )
    return {"n_plus": 5, "n_minus": 4, "a_t": a_t}


def n5_execution_certificate(
    results: list[dict[str, object]], control: dict[str, object]
) -> None:
    """Report the granularity this no-go actually resolves.

    Reporting only: adds no check and does not touch PASS/FAIL or the JSON.
    """
    print("\n== N5 execution certificate: what this runner resolves ==")

    sites = [int(np.prod(r["dims"])) for r in results]
    max_entry_err = max(
        max(
            float(r["max_antihermitian_error"]),
            float(r["max_eps_anticommutator_error"]),
            float(r["max_block_relation_error"]),
        )
        for r in results
    )
    max_spec = max(float(r["max_spectrum_difference"]) for r in results)
    zero_mults = sorted({int(r["zero_multiplicity_plus"]) for r in results})
    max_a_t = max(
        abs(complex(v["real"], v["imag"]))
        for r in results
        for v in r["a_t"].values()
    )

    print(
        "per_element: checked - the staggered operator is assembled entry by entry, "
        "each hop writing d[i, j] = +-0.5 eta_mu(c) U_mu(i) into a single matrix "
        "element, and the three structural identities D + D^dag, eps D eps + D and "
        f"lower + B^dag are then verified as elementwise maxima, the worst over all "
        f"{len(results)} backgrounds being {max_entry_err:.3e}."
    )
    print(
        "per_site: checked - both gradings are evaluated site by site over the full "
        f"volume, epsilon(c) = (-1)^(t+x+y+z) at each of the {sites[0]} and "
        f"{sites[-1]} sites to split them into the plus and minus index sets, and "
        "eta_mu(c) = (-1)^(sum of the first mu coordinates) recomputed at every site "
        "for every one of the four hop directions."
    )
    print(
        "per_mode: checked - the two Laplacians BB^dag and B^dagB are fully "
        "diagonalized and their sorted spectra compared eigenvalue against "
        f"eigenvalue, agreeing to {max_spec:.3e} at worst, and the zero modes are "
        f"counted separately on each side, matching at multiplicity {zero_mults} "
        "across the random and flux backgrounds."
    )
    print(
        "per_block: checked - this is the granularity the no-go turns on: reordering "
        "the sites by epsilon parity puts D into the bipartite form [[0, B], "
        "[-B^dag, 0]], and the runner verifies the two diagonal parity blocks vanish "
        "identically and that the lower block is exactly -B^dag, which is what forces "
        "B square and the two spectra equal."
    )
    print(
        "lattice_wide: checked - the index itself is a whole-lattice trace, "
        "A_t = Tr(eps exp(-t D^dag D)) summed over every site of the torus and "
        f"evaluated at t = 0.1, 0.5, 1.0 and 2.0 for each background, never exceeding "
        f"{max_a_t:.3e}; the rectangular control with N_+ - N_- = "
        f"{int(control['n_plus']) - int(control['n_minus'])} returns "
        f"A_t = {float(control['a_t']):.12f}, showing the trace is not blind."
    )
    print(
        "  scope: the tori tested are fixed at dims (4, 2, 2, 2) and (4, 4, 4, 4); "
        "no large-volume or continuum limit is taken, so the result is a statement "
        "about equal-sublattice even periodic Z4 tori, not an asymptotic one."
    )


def main() -> int:
    print("ABJ epsilon-index square-block no-go")
    results = []
    backgrounds = [
        ("Z4xZ2^3 random U(1)", (4, 2, 2, 2), random_u1_links((4, 2, 2, 2), 1)),
        ("Z4xZ2^3 flux U(1)", (4, 2, 2, 2), flux_u1_links((4, 2, 2, 2), 1, 1)),
        ("Z4^4 random U(1)", (4, 4, 4, 4), random_u1_links((4, 4, 4, 4), 2)),
        ("Z4^4 flux U(1)", (4, 4, 4, 4), flux_u1_links((4, 4, 4, 4), 1, 1)),
    ]
    for label, dims, links in backgrounds:
        results.append(analyze_background(label, dims, links))
    control = synthetic_rectangular_control()
    n5_execution_certificate(results, control)

    summary = (
        "For every tested even periodic Z4 torus and U(1) background, the "
        "standard massless staggered epsilon index vanishes because D has "
        "square bipartite block form. Closing P1' requires leaving this "
        "same-surface epsilon-index setup: e.g. an imbalanced/curved complex, "
        "a taste-singlet/Adams/overlap index operator, or an accepted ABJ premise."
    )
    out = {
        "claim": "standard staggered epsilon index vanishes on equal-sublattice even periodic Z4 tori",
        "pass": PASS,
        "fail": FAIL,
        "checks": CHECKS,
        "backgrounds": results,
        "rectangular_control": control,
        "summary": summary,
    }
    out_path = Path("outputs/abj_epsilon_index_square_block_no_go_2026-05-30.json")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(out, indent=2) + "\n")
    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    print("SUMMARY:", summary)
    print(f"Wrote {out_path}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
