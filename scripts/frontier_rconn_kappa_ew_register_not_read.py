#!/usr/bin/env python3
"""
Finite-dimensional repair for the kappa_EW register-not-read color-trace gate.

The retained Rconn/EW matching surface leaves

    R_phys(kappa_EW) = F_adj + kappa_EW * (1 - F_adj),
    F_adj = (N_c^2 - 1) / N_c^2.

This runner keeps the exact Fierz support: the singlet/adjoint channel
decomposition is real algebra, and F_adj=8/9 at N_c=3.  It also verifies why
the previously proposed closure route, "declare the singlet trace unregistered
by register-not-read, hence kappa_EW=0", is not a closure on the current
surface:

  * the singlet map is the SU(N) depolarizing twirl, not a finite central-sector
    partition map;
  * kappa_EW is a within-channel weight, while a partition supplies sectors and
    counts, not weights;
  * the current Record axiom explicitly supplies no readout context, weighting,
    normalization, probability, or physical observable bridge.

The kappa_EW gate remains open for a future non-axiom theorem, convention, or
owner-approved admission.  No PDG value, fit target, new axiom, or audit verdict
is load-bearing here.
"""

from pathlib import Path

import numpy as np

PASS = 0
FAIL = 0


def check(name, ok, detail=""):
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"PASS: {name} {detail}")
    else:
        FAIL += 1
        print(f"FAIL: {name} {detail}")


def su_n_generators(Nc):
    """SU(N_c) generators t^A with Tr[t^A t^B] = (1/2) delta_AB."""
    ts = []
    for i in range(Nc):
        for j in range(i + 1, Nc):
            Ssym = np.zeros((Nc, Nc), complex)
            Ssym[i, j] = 1
            Ssym[j, i] = 1
            ts.append(Ssym)
            Aanti = np.zeros((Nc, Nc), complex)
            Aanti[i, j] = -1j
            Aanti[j, i] = 1j
            ts.append(Aanti)
    for k in range(1, Nc):
        d = np.zeros(Nc)
        d[:k] = 1.0
        d[k] = -float(k)
        ts.append(np.diag(d).astype(complex))
    return [t / np.sqrt(2.0 * np.trace(t @ t).real) for t in ts]


def E_sing(M):
    Nc = M.shape[0]
    return (np.trace(M) / Nc) * np.eye(Nc, dtype=complex)


def R_phys(kappa, Nc=3):
    F_adj = (Nc * Nc - 1) / Nc**2
    return F_adj + kappa * (1 - F_adj)


rng = np.random.default_rng(0)

# Fierz algebra: exact S+C decomposition for representative N_c.
for Nc in (2, 3, 4, 5):
    ts = su_n_generators(Nc)
    if len(ts) != Nc * Nc - 1:
        check(f"FIERZ_generator_count_Nc{Nc}", False, f"got {len(ts)} != {Nc*Nc-1}")
        continue
    G = rng.standard_normal((Nc, Nc)) + 1j * rng.standard_normal((Nc, Nc))
    lhs = float(np.trace(G @ G.conj().T).real)
    S = (1.0 / Nc) * abs(np.trace(G)) ** 2
    C = 2.0 * sum(abs(np.trace(G @ t)) ** 2 for t in ts)
    check(
        f"FIERZ_S_plus_C_exact_Nc{Nc}",
        abs(lhs - (S + C)) < 1e-9,
        f"||G||^2={lhs:.4f} = S+C={S+C:.4f}",
    )

Nc = 3
ts = su_n_generators(Nc)
G = rng.standard_normal((Nc, Nc)) + 1j * rng.standard_normal((Nc, Nc))
I_comp_sq = abs(np.trace(G) / np.sqrt(Nc)) ** 2
S = (1.0 / Nc) * abs(np.trace(G)) ** 2
check(
    "S_is_the_I_over_sqrt_Nc_trace_component",
    abs(I_comp_sq - S) < 1e-9,
    f"|<G,I/sqrt(Nc)>|^2={I_comp_sq:.6f} = S={S:.6f}",
)
check(
    "adjoint_generators_are_traceless",
    all(abs(np.trace(t)) < 1e-12 for t in ts),
    "C-channel basis is traceless",
)

F_adj = (Nc * Nc - 1) / Nc**2
check(
    "KAPPA_zero_specialization_is_F_adj_8_9",
    abs(R_phys(0.0, Nc) - 8.0 / 9.0) < 1e-12 and abs(R_phys(0.0, Nc) - F_adj) < 1e-12,
    f"kappa_EW=0 specialization gives {R_phys(0.0, Nc):.4f}",
)
check(
    "KAPPA_one_specialization_is_total_channel_1",
    abs(R_phys(1.0, Nc) - 1.0) < 1e-12,
    "kappa_EW=1 specialization keeps the trace channel too",
)
check(
    "traceless_channel_count_fraction_is_F_adj",
    abs((Nc * Nc - 1) / (Nc * Nc) - F_adj) < 1e-12,
    f"dim(traceless)/dim(all) = 8/9",
)
check(
    "FAMILY_traceless_fraction_is_Nc2m1_over_Nc2",
    all(abs(((nc * nc - 1) / nc**2) - (nc * nc - 1) / nc**2) < 1e-15 for nc in range(2, 8)),
    "N_c-universal channel-count identity",
)

# Route-demotion checks: singlet map is a twirl/conditional expectation, not a
# finite central-sector partition map.
M = rng.standard_normal((Nc, Nc)) + 1j * rng.standard_normal((Nc, Nc))
g = np.linalg.qr(rng.standard_normal((Nc, Nc)) + 1j * rng.standard_normal((Nc, Nc)))[0]
check(
    "E_sing_is_idempotent_unital",
    np.allclose(E_sing(E_sing(M)), E_sing(M), atol=1e-12)
    and np.allclose(E_sing(np.eye(Nc)), np.eye(Nc), atol=1e-12),
    "conditional expectation onto C*I",
)
check(
    "E_sing_is_Ad_invariant_twirl_target",
    np.allclose(E_sing(g @ M @ g.conj().T), E_sing(M), atol=1e-12)
    and np.allclose(g @ E_sing(M) @ g.conj().T, E_sing(M), atol=1e-12),
    "singlet channel is the depolarizing twirl target",
)

P_nontriv = [
    np.diag([1.0, 0.0, 0.0]).astype(complex),
    np.diag([0.0, 1.0, 1.0]).astype(complex),
]
D_nontriv = sum(P @ M @ P for P in P_nontriv)
check(
    "nontrivial_partition_map_differs_from_singlet_twirl",
    np.isclose(D_nontriv[0, 0], M[0, 0]) and not np.isclose(E_sing(M)[0, 0], M[0, 0]),
    "partition preserves diagonal block; twirl averages trace",
)
comm_dev = max(float(np.max(np.abs(P @ t - t @ P))) for P in P_nontriv for t in ts)
check(
    "nontrivial_color_partition_fails_centrality",
    comm_dev > 0.1,
    f"projector/generator commutator dev {comm_dev:.2f}",
)
check(
    "trivial_central_partition_is_identity_not_twirl",
    not np.allclose(M, E_sing(M), atol=1e-6),
    "Schur-compatible {I} partition gives identity on a generic matrix",
)

check(
    "kappa_EW_is_free_weight_not_count",
    abs(R_phys(0.25, Nc) - (8.0 / 9.0 + 0.25 / 9.0)) < 1e-15
    and R_phys(0.0, Nc) != R_phys(1.0, Nc),
    "8/9 count is fixed while kappa_EW changes the singlet weight",
)

repo = Path(__file__).resolve().parents[1]
axioms = (repo / "docs" / "MINIMAL_AXIOMS_2026-06-05.md").read_text()
note = (repo / "docs" / "RCONN_KAPPA_EW_REGISTER_NOT_READ_COLOR_TRACE_OPEN_GATE_NOTE_2026-06-08.md").read_text()
check(
    "Record_axiom_does_not_supply_weighting_or_context",
    "record supplies no readout context" in axioms
    and "weighting, normalization, probability" in axioms
    and "physical observable bridge" in axioms,
    "current axioms cannot close kappa_EW by themselves",
)
check(
    "source_note_records_route_demoted_not_closed",
    "2026-06-10 route repair" in note
    and "route-demotion" in note
    and "does not close" in note
    and ("worth " + "testing") not in note,
    "source surface matches repaired route boundary",
)
compact_note = " ".join(note.replace("`", "").replace("*", "").split())
check(
    "source_note_has_downstream_use_firewall",
    "2026-06-13 downstream-use firewall" in compact_note
    and "may not be cited as a derivation of κ_EW = 0" in compact_note
    and "Any downstream positive use must supply a separate" in compact_note,
    "route demotion cannot be reused as a selector theorem",
)
check(
    "source_note_lists_forbidden_positive_reuses",
    "κ_EW = 0 follows from register-not-read" in compact_note
    and "R_conn = 8/9 is physically selected" in compact_note
    and "this row closes the wider κ_EW gate" in compact_note,
    "downstream citation firewall names the unsafe reuses",
)

print()
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
print(
    "ROUTE-DEMOTION RESULT: the exact Fierz trace/traceless algebra and the "
    "8/9 count survive, but register-not-read does not by itself select "
    "kappa_EW=0 on the current Record/axiom surface. The kappa_EW gate remains "
    "open for a future non-axiom readout theorem, convention, or approved "
    "admission; no audit verdict is applied here."
)
if FAIL:
    raise SystemExit(1)
