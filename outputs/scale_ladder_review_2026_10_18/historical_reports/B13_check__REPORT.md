# B13 check: estimator, sign gauge, population bias, L=4 dip

Provenance: a fresh-context agent of the same model family; not independent in model family. It used its own DMC (`chk.py`) and exact-diagonalisation helpers, and neither uses `dmclib` or `ringlib`. Compute was about 75 min. Saved by the supervisor from the hand-back.

## 1. Estimator: correct

- Source: H(b) = −J·exp(i b c_p circ_p). E0 is even and analytic in b, so E0(iη) = E0 − χη²/2.
- The twisted matrix is stoquastic, so ⟨M²⟩ = A + χτ holds with no stray factors.
- **2³ checks:**
  - finite-difference χ = 0.26702 at V=0;
  - pure-gauge sources give χ = 0;
  - twisted-DMC energies match exact E0(iη) within about 2σ.

## 2. Stoquastic, and the sign of J is a gauge choice: confirmed

The diagonal unitary D(σ) = Π s_l^{(1+σ_l)/2} gives D(flip)/D = −1 on every sampled move at L = 2, 4, 6.

## 3. Population bias

Bias is large and nonlinear in 1/N for V ≤ 0. The time step dt acts only as a population-control knob, because propagation is in continuous time.

| Point | Result |
|---|---|
| V=1, L=4 (exact guide) | χ = 0.2346(16), reproduces the original |
| V=0.5, L=4 | energy converged (~2e−5); twisted-energy estimator χ_tw = 0.242(2) |
| V=0.5, L=6 | χ_FW = 0.248 / 0.263 / 0.259 for N = 500 / 2000 / 6000; twisted 0.2445(26) |
| V=0.5, L=8 | twisted ≈ 0.245 (one η, N=2000) |
| V=0, L=4 | E drifts from −0.29218 to −0.29308 over N = 500 → 12000. χ_FW goes from 0.170 to 0.122; 1/N extrapolation 0.127(9). Twisted: 0.159 at N=12000, before a −0.017 quartic correction |
| V=0, L=6 | E not converged. χ_FW = 0.25–0.28(4); twisted 0.217(14) |
| V=−0.5, L=4 | E not converged. χ_FW goes from 0.067 to 0.009(5) |
| V=−0.5, L=6 | χ_FW = 0.23(4), but twisted gives 0.159(13): the estimators disagree |
| V=−0.5, L=8 | unreliable: N/ESS = 5.8 |

The original 2³ validation floor of 2e−3 hid the bias: an N=2000 run sits 1.2e−3 above the exact energy.

## 4. The L=4 dip

The dip is real, but it is not explained:
- two estimators agree on it;
- it does not depend on the initial state;
- it deepens with N;
- the walkers stay in the W=0 sector, which is correct;
- there are no Bragg peaks (S ≤ 0.8).

Exact diagonalisation on 4³ is infeasible.

One hypothesis is untested: confinement-like suppression at L=4 that L=6 frustrates by commensurability. Testing it needs a converged L=8 run at V ≤ 0.

## 5. Verdicts

- **Robust:**
  - the model identity, and that it is sign-free;
  - χ ≈ 0.23–0.25 for V = 0.5–1 on 4³–8³, with no size dependence.
- **Not supported:** "no decay at V ≤ 0 for L = 6–8". Energies are unconverged, the guide degrades with L, and the estimators disagree.
- **For V ≤ 0:** nothing can be claimed. L=4 is suppressed there, possibly in a confinement-like way.
