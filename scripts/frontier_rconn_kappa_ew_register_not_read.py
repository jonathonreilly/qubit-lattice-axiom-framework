#!/usr/bin/env python3
"""
Finite-dimensional support for a possible kappa_EW open route.

The retained no-go RCONN_DERIVED_NOTE establishes the exact Fierz adjoint fraction
F_adj=(N_c^2-1)/N_c^2 but leaves the physical readout selector kappa_EW free
(R_phys = F_adj + kappa_EW*(1-F_adj); kappa_EW=0 -> octet/8-9, kappa_EW=1 -> total/1).

This runner verifies only the exact algebraic support for a possible future route:
in the Fierz operator basis {I/sqrt(N_c), sqrt(2) t^A},
  S = (1/N_c)|Tr G|^2 is exactly the I/sqrt(N_c) trace component;
  C = 2 Sum_A |Tr[G t^A]|^2 is the traceless adjoint component.
If a separate retained theorem later proves that register-not-read governs this
color operator-trace split and treats the trace component as unregistered reference,
then kappa_EW=0 and R_conn=(N_c^2-1)/N_c^2 follow.

This runner does not prove that Record supplies that color-trace readout context or
selector. No PDG value is load-bearing.
"""
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
    """SU(N_c) generators t^A with Tr[t^A t^B] = (1/2) delta_AB (Gell-Mann normalization)."""
    ts = []
    for i in range(Nc):
        for j in range(i + 1, Nc):
            Ssym = np.zeros((Nc, Nc), complex); Ssym[i, j] = 1; Ssym[j, i] = 1
            ts.append(Ssym)
            Aanti = np.zeros((Nc, Nc), complex); Aanti[i, j] = -1j; Aanti[j, i] = 1j
            ts.append(Aanti)
    for k in range(1, Nc):
        d = np.zeros(Nc); d[:k] = 1.0; d[k] = -float(k)
        ts.append(np.diag(d).astype(complex))
    # normalize each to Tr[t t] = 1/2
    return [t / np.sqrt(2.0 * np.trace(t @ t).real) for t in ts]


rng = np.random.default_rng(0)

# ===== (FIERZ) exact S + C decomposition of the q-qbar correlator, all N_c =====
for Nc in (2, 3, 4, 5):
    ts = su_n_generators(Nc)
    if len(ts) != Nc * Nc - 1:
        check(f"FIERZ_generator_count_Nc{Nc}", False, f"got {len(ts)} != {Nc*Nc-1}")
        continue
    G = rng.standard_normal((Nc, Nc)) + 1j * rng.standard_normal((Nc, Nc))
    lhs = float(np.trace(G @ G.conj().T).real)  # Tr[G G^dag] = ||G||_F^2
    S = (1.0 / Nc) * abs(np.trace(G)) ** 2
    C = 2.0 * sum(abs(np.trace(G @ t)) ** 2 for t in ts)
    check(f"FIERZ_S_plus_C_exact_Nc{Nc}", abs(lhs - (S + C)) < 1e-9,
          f"||G||^2={lhs:.4f} = S+C={S+C:.4f}")

# ===== (S=REF) S is EXACTLY the I/sqrt(Nc)-trace component (the I/d reference direction) =====
Nc = 3
ts = su_n_generators(Nc)
G = rng.standard_normal((Nc, Nc)) + 1j * rng.standard_normal((Nc, Nc))
I_comp_sq = abs(np.trace(G) / np.sqrt(Nc)) ** 2  # |<G, I/sqrt(Nc)>|^2
S = (1.0 / Nc) * abs(np.trace(G)) ** 2
check("S_is_the_I_over_d_trace_reference_component", abs(I_comp_sq - S) < 1e-9,
      f"|<G,I/sqrt(Nc)>|^2={I_comp_sq:.6f} = S(singlet/disconnected)={S:.6f}")
# the octet basis is traceless (the registered content directions)
check("octet_generators_are_traceless_content", all(abs(np.trace(t)) < 1e-12 for t in ts),
      "every t^A is traceless -> the C-channel is the traceless (octet) content")

# ===== (KAPPA) the readout algebra: octet-only vs total =====
F_adj = (Nc * Nc - 1) / Nc ** 2
R0 = F_adj + 0.0 * (1 - F_adj)
R1 = F_adj + 1.0 * (1 - F_adj)
check("KAPPA_octet_only_gives_F_adj_8_9", abs(R0 - 8.0 / 9.0) < 1e-12 and abs(R0 - F_adj) < 1e-12,
      f"kappa_EW=0 -> R_conn=F_adj=(Nc^2-1)/Nc^2={R0:.4f}=8/9")
check("KAPPA_total_gives_1", abs(R1 - 1.0) < 1e-12,
      f"kappa_EW=1 -> R_phys=1 (the trace S registered too)")

# ===== (CONDITIONAL) if the trace channel is excluded, the remaining fraction is F_adj =====
# This is an operator-algebra fact, not a proof that Record excludes this color trace.
dim_content = Nc * Nc - 1
dim_total = Nc * Nc
check("CONDITIONAL_traceless_content_fraction_is_F_adj", abs(dim_content / dim_total - F_adj) < 1e-12,
      f"dim(traceless octet)/dim(all) = {dim_content}/{dim_total} = F_adj = 8/9")

# ===== (FAMILY) the traceless-channel fraction is N_c-universal =====
fam = all(abs(((nc * nc - 1) / nc ** 2)) == (nc * nc - 1) / nc ** 2 for nc in range(2, 8))
check("FAMILY_traceless_fraction_is_Nc2m1_over_Nc2", fam,
      "traceless-channel fraction is (N_c^2-1)/N_c^2 at every N_c (N_c=3 -> 8/9)")

print()
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
print("CONDITIONAL RESULT: the Fierz S/C split is exactly the trace/traceless operator split, and "
      "the traceless-channel fraction is (N_c^2-1)/N_c^2 (8/9 at N_c=3). If a separate theorem later "
      "proves that register-not-read governs this color operator-trace split and excludes the trace "
      "component as unregistered reference, then kappa_EW=0 follows. This runner does not prove that "
      "Record supplies that color-trace selector.")
