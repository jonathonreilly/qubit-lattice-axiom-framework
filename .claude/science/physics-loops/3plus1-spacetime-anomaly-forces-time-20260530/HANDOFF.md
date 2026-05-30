# Handoff

Cycle 1 produced an exact no-go for the current P1' residual if P1' is
interpreted as the standard staggered `epsilon` index on finite even periodic
`Z^4` tori.

The proof is the square bipartite block identity:

```text
D = [[0,B],[-B^dag,0]],  B square
=> D^dag D = diag(BB^dag, B^dagB)
=> Tr(eps exp(-tD^dagD)) = 0.
```

Verification:

```text
python3 scripts/frontier_abj_epsilon_index_square_block_no_go.py
TOTAL: PASS=45 FAIL=0
```

Cycle 2 repaired the parent 3+1 theorem to the current repo surface. The old
"PR 402 closed / no successor companion" wording is gone. The parent theorem
first composed an accepted-premise packet with Clifford parity and the
single-clock theorem.

Cycle 3 retired the accepted-premise wording from the active parent route. The
parent theorem now composes:

```text
ABJ standard-theorem bridge
+ exact anomaly arithmetic
+ retained Clifford chirality parity
+ single-clock codimension-1 exclusion
=> d_t = 1.
```

Verification:

```text
PYTHONPATH=scripts python3 scripts/frontier_abj_standard_theorem_bridge_for_anomaly_forces_time.py
TOTAL: PASS=38 FAIL=0

PYTHONPATH=scripts python3 scripts/frontier_anomaly_forces_time_standard_abj_closure.py
TOTAL: PASS=33 FAIL=0

python3 scripts/anomaly_forces_time_abj_inconsistency_accepted_premise_runner.py
TOTAL: PASS=63 FAIL=0

python3 scripts/axiom_first_single_clock_codimension1_evolution_check.py
PASS=18 FAIL=0
```

This is the strongest honest current-surface positive status:
standard-theorem bounded closure. It is not unbounded A1+A2 closure because
the ABJ anomaly-to-inconsistency theorem is cited as a standard QFT theorem
rather than derived from the framework action.

The remaining unbounded positive work is one of:

1. taste-singlet/Adams staggered index permission theorem;
2. finite local Wess-Zumino/cohomology anomaly-to-inconsistency proof;
3. framework-admissible non-flat/imbalanced complex;
4. explicit bounded composition using ABJ as a standard theorem bridge.

Item 4 is now done in the repaired parent theorem without making the accepted
premise packet load-bearing. Recommended next block for unbounded closure
remains the taste-singlet/Adams staggered index permission theorem or the
finite local Wess-Zumino/cohomology theorem, because both stay close to the
standard ABJ proof while escaping the square-block `epsilon` no-go.

Cycle 4 internalized the ABJ step on the physical 3+1 framework action
surface. The active parent theorem now composes:

```text
framework-action U(1)^3 ABJ proof
+ exact anomaly arithmetic
+ retained Clifford chirality parity
+ single-clock codimension-1 exclusion
=> d_t = 1.
```

The new ABJ proof uses the action Dirac operator, the Wick-rotated local
3+1 heat-kernel spin trace, exact `Tr_LH[Y^3] = -16/9`, and a 3+1 abelian
local counterterm enumeration. It does not use a finite Euclidean `Z^4`
substrate, the accepted-premise packet, or the standard-theorem bridge as
load-bearing input.

Verification:

```text
PYTHONPATH=scripts python3 scripts/frontier_abj_from_framework_action_u1_cubic.py
TOTAL: PASS=56 FAIL=0
```

The old standard-theorem bridge remains a fallback/reference artifact. The
active parent route is now the framework-action proof. Effective retained
status still requires independent audit of this new proof and the non-ABJ
dependencies: action realization, physical hypercharge/matter surface, and
single-clock.
