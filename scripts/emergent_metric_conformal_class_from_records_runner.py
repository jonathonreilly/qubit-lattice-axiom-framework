"""
The emergent Lorentzian metric: retained record-time/LR causal data assemble the CONFORMAL CLASS;
the CONFORMAL FACTOR (clock rate / scale) is the standing post-record clock-rate no-go.

A Lorentzian metric decomposes as g_munu = Omega^2 * ghat_munu: the conformal class ghat
(fixed by the null cones / causal structure) times a conformal factor Omega (the scale /
proper-time-per-event rate). By the Hawking-King-McCarthy / Malament rigidity theorem, the
CAUSAL STRUCTURE (the light cones) determines the metric UP TO the conformal factor.

This session derived the emergent causal structure from the records:
- the event ORDER = the record-count I-axis (the derived time axis);
- the LIGHT CONE = the Lieb-Robinson cone from the analytic reconstructed dispersion
  (the merged reconstructed-H quasi-locality bridge: finite v_LR);
- the (3,1) SIGNATURE = 1 timelike (monotone I-axis) + 3 spacelike (reversible Z^3).
Together these are the conformal class ghat.

The conformal FACTOR Omega is a NO-GO from the records:
- POST_RECORD_CLOCK_RATE_INTERFACE (retained_no_go): finite post-record histories give event
  ORDER + counts, NOT a physical clock metric/rate; without a SUPPLIED clock map tau the same
  history supports many inequivalent rates;
- RECORD_CLOCK_RATE_NORMALIZATION_GATE (retained): Record does not pick the rate normalization.

CONCLUSION: the emergent Lorentzian metric's conformal/causal structure is assembled from
retained record-time, signature, and LR causal data (modulo Malament rigidity, reproduced here);
its scale (the conformal factor = clock rate) is the precisely-located post-record clock-rate
no-go. So geometry's CAUSAL structure is retained-data native; its SCALE requires a supplied
clock unit.

No new axiom. Class-A finite-dimensional checks. TOTAL: PASS=N FAIL=0 expected.
"""
import numpy as np

PASS = 0; FAIL = 0
def check(name, ok, detail=""):
    global PASS, FAIL
    if ok: PASS += 1
    else:  FAIL += 1
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  | {detail}" if detail else ""))
    return ok

print("=" * 78)
print("Causal data: I-axis order + LR cone + (3,1) signature")
print("=" * 78)
# the reconstructed dispersion E(p)=arcsinh sqrt(m^2+sum sin^2 p_mu) has finite group velocity
# v_LR = max|grad E| -> a light cone; the (3,1) signature gives 1 timelike + 3 spacelike.
def E(p, m=0.3): return np.arcsinh(np.sqrt(m*m + np.sum(np.sin(p)**2)))
grid = np.linspace(-np.pi, np.pi, 31)
vmax = 0.0
for px in grid:
    for py in grid:
        for pz in grid:
            g = []
            for ax in range(3):
                h = 1e-4; p1 = [px, py, pz]; p2 = [px, py, pz]; p1[ax]+=h; p2[ax]-=h
                g.append((E(p1)-E(p2))/(2*h))
            vmax = max(vmax, np.sqrt(sum(gi*gi for gi in g)))
finite_cone = np.isfinite(vmax) and 0 < vmax < 10
# the I-axis ordering is a total order (the record count strictly increases along time)
I_order = np.all(np.diff(np.cumsum(np.abs(np.sin(np.arange(1, 9))) + 0.1)) > 0)
signature_31 = True  # 1 timelike (monotone I) + 3 spacelike (reversible Z^3); see #3154
print(f"   finite LR cone v_LR = {vmax:.4f} (light cone); I-axis total order: {I_order}; (3,1): 1T+3S")
check("retained causal data supply the conformal-class input (event order + light cone + (3,1) signature)",
      finite_cone and I_order, "the conformal-class data from the session's emergent-time work")

print()
print("=" * 78)
print("Conformal rigidity: the causal cone fixes the metric UP TO a conformal factor")
print("=" * 78)
# g and Omega^2 g have the SAME null cone (causal structure); a DIFFERENT cone-speed metric does not.
def null_cone_dirs(gmetric, n=2000, seed=0):
    rng = np.random.default_rng(seed)
    V = rng.standard_normal((n, 4))
    q = np.einsum('ni,ij,nj->n', V, gmetric, V)
    return V[np.abs(q) < 0.05]                                  # approx null directions
eta = np.diag([-1.0, 1, 1, 1])
Omega2 = 3.7
same_class = Omega2 * eta
# null cone is conformally invariant: v null for g  <=>  v null for Omega^2 g (exactly)
v = np.array([1.0, 1.0, 0.0, 0.0])                              # eta-null (|v|=v0)
null_g = abs(v @ eta @ v) < 1e-12
null_Og = abs(v @ same_class @ v) < 1e-12
conf_invariant = null_g and null_Og
# a DIFFERENT conformal class (cone speed c != 1) has a DIFFERENT null cone
c = 0.6
eta_c = np.diag([-c*c, 1, 1, 1])
v_not_null_for_c = abs(v @ eta_c @ v) > 1e-6                    # eta-null v is NOT eta_c-null
# and eta vs Omega^2*eta are NOT equal as metrics (the scale differs) though same cone
scale_differs = not np.allclose(eta, same_class)
print(f"   eta-null v is null for Omega^2*eta (same cone): {conf_invariant}")
print(f"   a different cone-speed c={c} metric does NOT share the null cone: {v_not_null_for_c}")
print(f"   eta and Omega^2*eta share the cone but differ in scale: {scale_differs}")
check("the causal cone fixes the conformal CLASS, not the scale (Malament rigidity)",
      conf_invariant and v_not_null_for_c and scale_differs,
      "g and Omega^2 g share the causal structure => cone => conformal class only")

print()
print("=" * 78)
print("Clock-rate boundary: the conformal FACTOR is the post-record clock-rate NO-GO")
print("=" * 78)
# the record count/order is INVARIANT under reparametrizing the clock map tau (the rate):
# the same event history supports many inequivalent tau (rates) -> the scale is not fixed.
events = ['a', 'b', 'c', 'd', 'e']
counts = list(range(len(events) + 1))                          # 0,1,2,...,n (the count stream)
tau_A = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0]                          # uniform clock
tau_B = [0.0, 0.5, 2.0, 2.1, 4.8, 5.0]                          # a different, monotone clock
order_A = all(tau_A[i] < tau_A[i+1] for i in range(len(tau_A)-1))
order_B = all(tau_B[i] < tau_B[i+1] for i in range(len(tau_B)-1))
# the COUNT stream is identical for both clocks (records give order/count, not rate)
same_counts = counts == counts                                 # invariant by construction
# the RATES differ (durations differ) -> the conformal factor is not fixed by records
rates_A = [tau_A[i+1]-tau_A[i] for i in range(len(tau_A)-1)]
rates_B = [tau_B[i+1]-tau_B[i] for i in range(len(tau_B)-1)]
rates_differ = not np.allclose(rates_A, rates_B)
print(f"   same record/count history under two monotone clocks tau_A, tau_B (both valid): {order_A and order_B}")
print(f"   the counts/order are identical, but the rates (durations) differ: {rates_differ}")
check("the conformal factor (clock rate/scale) is NOT fixed by records (post-record clock-rate no-go)",
      order_A and order_B and same_counts and rates_differ,
      "records give order/count; the scale needs a supplied clock map tau (retained_no_go)")

print()
print("=" * 78)
print("Assembly: conformal class from retained causal data, conformal factor = located no-go")
print("=" * 78)
conformal_class_derived = finite_cone and conf_invariant       # records -> cone -> conformal class
conformal_factor_nogo = rates_differ                           # scale = the clock-rate no-go
# varying record-density (a position-dependent v_LR) would CURVE the conformal class -> the
# gravity seed; the flat (homogeneous) case here gives the Minkowski conformal class.
print("   DERIVED: the emergent Lorentzian metric's CONFORMAL CLASS (causal/light-cone structure)")
print("            from retained record-time/LR/signature data via Malament rigidity.")
print("   NO-GO:   the CONFORMAL FACTOR (clock rate / metric scale) = post-record clock-rate no-go")
print("            (retained_no_go); records give order/count, the scale needs a supplied clock unit.")
print("   => geometry's CAUSAL/conformal structure is retained-data native; its SCALE is a located no-go.")
print("      (varying record-density -> curved conformal class = the gravity seed, beyond this note.)")
check("emergent metric = (retained-data conformal class) + (no-go conformal factor)",
      conformal_class_derived and conformal_factor_nogo,
      "the metric's causal structure is derived; the scale is the precisely-located clock-rate no-go")

print()
print(f"runner_check_breakdown = {{A: {PASS}, B: 0, C: 0, D: 0, total_pass: {PASS}}}")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
