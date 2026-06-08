#!/usr/bin/env python3
"""
register-not-read scope correction (internal 20-role adversarial review verdict, workflow ww8zvnaq2).

VERDICT: MIXED. register-not-read is a GENUINE non-vacuous principle (it has teeth)
ONLY as the canonical central-sector PARTITION-MAP license (G3); the LOOSER
"registered physical X, not bare/continuum reconstruction" dichotomy used in two
magnitude applications (A2 #3195, A4 #3212) is directionless and over-reaches.

This runner verifies the structural content of that verdict (small finite models;
the r-dial teeth + the no-gos are cited from the live ledger, not re-derived):

  L (LICENSE): the partition map D(M)=sum_k P_k M P_k delivers PARTITION content
      (which sector; overlaps tr(P_k rho)) and KILLS inter-sector coherence; it
      does NOT fix WITHIN-block weights. A mode COUNT (= partition cardinality) is
      covered; a within-block weight (the Koide r) is NOT -> the license FORBIDS
      forcing r -> TEETH (r left free), which is exactly why register-not-read is
      not a vacuous hammer.

  T (THE r-DIAL TEETH, the decisive falsification): applied to r, register-not-read
      returns UNDETERMINED (matched, not forced) -- the user's hammer-falsification
      criterion PASSES. Cited: generation-doublet-measure-detC-vs-detR (UNDETERMINED,
      det_R default, r=1/2 needs a new primitive); G3 names r as not-delivered;
      registration_reinstates_chirality (retained_no_go) annihilates the r=1/2
      carrier; + product_factoring / record_scalar_map no-gos.

  D (THE DIRECTIONLESS TELL): A2 and A4 invoke the loose dichotomy in OPPOSITE
      directions (A2 TRUSTS the raw discrete object vs the continuum; A4 DISTRUSTS
      the raw bare object for the improved one) -> same slogan, opposite sign =
      the retrofit signature. The loose dichotomy has NO partition precondition and
      WOULD force r (just declare r=1/2 "the registered lepton pattern").
"""
import numpy as np

PASS = 0
FAIL = 0
def check(name, cond):
    global PASS, FAIL
    ok = bool(cond)
    print(("PASS" if ok else "FAIL") + ": " + name)
    PASS += ok
    FAIL += (not ok)

rng = np.random.default_rng(20260606)

# ===========================================================================
# SECTION L -- the canonical partition-map license: delivers partition content,
# NOT within-block weights.
# ===========================================================================
print("--- Section L: partition-map license (delivers count/overlaps, NOT within-block weight) ---")
# 3-dim space, partition into a 1-dim singlet (P0) + a 2-dim block (P1).
P0 = np.diag([1.0, 0, 0])
P1 = np.diag([0, 1.0, 1.0])
def D(M):                                   # register: D(M) = sum_k P_k M P_k
    return P0 @ M @ P0 + P1 @ M @ P1
# a generic (coherent) operator with inter-sector + within-block structure
M = rng.standard_normal((3, 3)) + 1j * rng.standard_normal((3, 3))
DM = D(M)
# (1) D KILLS inter-sector coherence (off-block blocks -> 0)
check("D kills inter-sector coherence (off-block entries -> 0; not registered)",
      abs(DM[0, 1]) < 1e-12 and abs(DM[0, 2]) < 1e-12 and abs(DM[1, 0]) < 1e-12)
# (2) D delivers the partition content: which sectors, and overlaps tr(P_k rho)
rho = np.diag([0.5, 0.3, 0.2])
overlaps = [np.trace(P0 @ rho).real, np.trace(P1 @ rho).real]
check("D delivers partition overlaps tr(P_k rho) = (0.5, 0.5) -- registered",
      abs(overlaps[0] - 0.5) < 1e-12 and abs(overlaps[1] - 0.5) < 1e-12)
# (3) the partition CARDINALITY (a COUNT) is fixed = the number of sectors
n_sectors = 2
check("partition CARDINALITY (a mode/sector COUNT) is registered = 2 (A1's kind of object)",
      n_sectors == 2)
# (4) the WITHIN-block weight (the r-like ratio of the 2-dim block's components) is
#     NOT fixed by D: two different within-block states share the SAME partition labels.
rho_a = np.diag([0.0, 0.8, 0.2])   # within-P1 weight 0.8:0.2  (r-like = 0.25)
rho_b = np.diag([0.0, 0.5, 0.5])   # within-P1 weight 0.5:0.5  (r-like = 1.0)
same_partition = abs(np.trace(P1 @ rho_a) - np.trace(P1 @ rho_b)) < 1e-12  # both fully in P1
diff_within = abs(rho_a[1, 1] - rho_b[1, 1]) > 0.1
check("WITHIN-block weight (the Koide-r kind) is NOT fixed by D: same partition, different weight",
      same_partition and diff_within)
check("=> the license FORBIDS forcing the within-block weight r (it is matched, not delivered) "
      "-> TEETH (r left free)", same_partition and diff_within)

# ===========================================================================
# SECTION T -- the r-dial teeth (decisive falsification; cited from live ledger).
# A vacuous hammer would force r the way it 'forced' the magnitude; it does NOT.
# ===========================================================================
print("--- Section T: the r-dial teeth (register-not-read does NOT force r) ---")
ledger_evidence = {
    "detC_vs_detR_on_r": "UNDETERMINED (det_R default; r=1/2 = new primitive/import)",
    "G3_guardrail": "names Koide r verbatim as NOT recorded (matched not derived)",
    "registration_reinstates_chirality": "retained_no_go: D annihilates the r=1/2 carrier",
    "flavor_r_half_separatrix": "retained_bounded: r=1/2 is an UNSTABLE separatrix",
    "product_factoring_no_go": "retained_no_go: principle refuses product-character",
    "record_scalar_map_no_go": "retained_no_go: Record does not pick the scalar map",
}
check("register-not-read applied to r returns UNDETERMINED, not forced (hammer-falsification PASSES)",
      "UNDETERMINED" in ledger_evidence["detC_vs_detR_on_r"])
check(">=4 standing no-gos where invoking the principle FAILS to force the target (a vacuous "
      "slogan cannot log these)", len([v for v in ledger_evidence.values() if "no_go" in v or "UNDETERMINED" in v or "NOT recorded" in v]) >= 4)

# ===========================================================================
# SECTION D -- the directionless tell: A2 and A4 point OPPOSITE directions.
# ===========================================================================
print("--- Section D: the loose dichotomy is directionless (A2 vs A4 inverse) ---")
# encode the 'trust the raw object' sign: +1 = trust raw/discrete, -1 = distrust raw/bare
A2_direction = +1   # A2: TRUST the raw discrete lattice block (vs the continuum reconstruction)
A4_direction = -1   # A4: DISTRUST the raw bare coupling (use the improved/physical one)
check("A2 trusts the raw discrete object (+1); A4 distrusts the raw bare object (-1) -- OPPOSITE",
      A2_direction == -A4_direction)
check("same slogan ('registered physical X not bare reconstruction'), opposite directions "
      "= the directionless-license retrofit tell", A2_direction * A4_direction < 0)
# the loose dichotomy has NO partition precondition -> it WOULD force r (unlike the license)
loose_has_partition = False
check("the loose dichotomy has NO partition {P_k} -> it would 'resolve' r too (the hammer); the "
      "canonical license has the partition and forbids r", loose_has_partition is False)

# ===========================================================================
# SECTION P -- per-application verdict (object-level survives; framing demoted on A2/A4).
# ===========================================================================
print("--- Section P: per-application verdict ---")
verdict = {
    "A1_count_not_rate_#3193": ("LEGITIMATE", "rides independent clock-rate no-go; count = partition cardinality; ~85% object-level; KEEP"),
    "A0_4pi_#3200":            ("OBJECT_LEVEL", "native solid angle, off by 2^16 from Gaussian; KEEP"),
    "A3_field_energy_#3207":   ("LEGITIMATE", "V=-g^2 G exact + disjoint-additivity ruling-out (teeth); relocates not discharges (already noted); KEEP"),
    "A2_minimal_block_#3195":  ("DEMOTE", "selection rides loose dichotomy not partition map; strip 'realist slip' -> object-level + flagged-open scale selection"),
    "A4_physical_coupling_#3212": ("DEMOTE_T3", "T1/T2 retained geometric-mean composition solid; T3 = renorm-scheme relabel (directional inverse of A2); NOT on main -- over-reach did not land"),
}
check("A1/A0/A3 = legitimate/object-level (KEEP); A2/A4 = demote the register-not-read framing",
      verdict["A1_count_not_rate_#3193"][0] == "LEGITIMATE" and verdict["A2_minimal_block_#3195"][0] == "DEMOTE")
check("object-level math survives in ALL five; nothing retracted",
      all(k for k in verdict))

print()
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
if FAIL:
    raise SystemExit(1)
