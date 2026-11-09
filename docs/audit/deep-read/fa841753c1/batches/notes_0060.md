# Docs-top batch, note 60

Pin: `fa841753c1a6296e5ad45518375660b0f1004769`

Runners were not executed.

Fixes in this batch: none

## Note 60

- Path: `docs/LOCAL_CONSERVING_PREPARATION_BOUNDED_THEOREM_NOTE_2026-10-16.md`
- Result: no fix
- Checked:
  - `sum_{l=1}^L sin^2(pi l/(L+1))=(L+1)/2`, so `b_l=sqrt(2/(L+1)) sin(pi l/(L+1))` is normalized. The adjacent overlap equals `cos(pi/(L+1))`, and `2-2 cos(theta)=4 sin^2(theta/2)`, so `d_L=a_L=2 sin(pi/[2(L+1)])`. Then `d_L<=pi/(L+1)` and `4 q d_L<=4 pi q/(L+1)`.
  - Reflection gives mean index `(L+1)/2` and battery mean `q+(L-1)/2`, so `mu_B=Delta[q+(L-1)/2]`. The edge sum `sum_{i=1}^{L-1} w_{i+1}` equals that same excess `(L-1)/2`. Support width `L-1` gives `Var<=(L-1)^2/4`.
  - For `|r-y|<=1/4` and `k=floor(r)+2`, `k-y` lies in `(3/4,9/4]`, so `3 pi/2<lambda<=9 pi/2<6 pi=Q_*`. The root enclosure satisfies `0<k-x<5/4<2`.
  - `f_h=(1-cos(2 pi t/h))/h` has integral `1`, maximum `2/h`, and total variation `4/h`. The author slot bounds give strength `g/2` and slew `sigma/2`. The preparation split gives envelope `sigma/4` and carrier `sigma/4`. With `theta<=pi/2`, the carrier is at most `pi Delta/h`.
  - Serial norms are at most `2 pi` and preparation norms at most `5 pi/2`, both at most `Q_*=6 pi`. The absolute-work bounds `(4 hbar/h)(sum||Q_j||+m lambda)<=g(G+m)` and `g(G+M)+(pi/2) Delta G` follow. Calibration `(25)` sums to the Hamiltonian budget; runtime `(29)` is five shares of at most `epsilon/5`; the preparation allocation sums to `3e/4`.
  - Centering gives mean error at most `a e/2` and second-moment error at most `a^2 e/2`. The variance gap is at most `(3/2) a^2 e`, so the displayed `3 a^2 e` is larger.
  - For `q=1,L=3`, the packet is `(1/2,1/sqrt(2),1/2)` on a `2^5=32`-dimensional battery. Omitted phase at `x=pi/2` has overlap `-1/2` and squared trace norm `3`. The branch-phase witness has squared trace norm `3/2-sqrt(6)/2`. Reversed conditional `Y` has overlap `0` and squared trace norm `4`. `[n,Y]=iX`. The order witness `E=Z`, `V=Hadamard` on `|0>` is orthogonal.
  - The `q=1` mixture has readiness trace norm `2 delta` and energy-gain discrepancy `2 Delta delta`. If `e_bat<2 delta`, then `(Delta/2)(e_bat+2 delta)<2 Delta delta`.
  - `30 s^2(1-s)^2` integrates to `1` and vanishes with its derivative at both endpoints. Author `M=L+2q` gives `m=L+3q+1`; root `M=L+2q-1` is one battery qubit smaller. The end sine ratio is `1/(2 cos alpha)>=1/2`, so `s_i^2>=1/5` and the arccos derivative is at most `sqrt(5)`. `SWAP=(I+XX+YY+ZZ)/2`, and `exp(-i pi(I-SWAP)/2)=SWAP`.
- Not checked: the imported count `O(4^n n^(3/2))`, beyond the routing factor that turns an `O(n)` multiplier into the exponent sum `5/2`; SHA-256 strings; source byte lengths; and the historical fixture process. The discriminators above were recomputed from the printed amplitudes, not by running the script.
- Finding: The recomputed sine, shift, lambda, pulse, work, budget, and `q=1,L=3` identities match the printed digits. The note already separates the author battery `M=L+2q` from the root battery `M=L+2q-1`, treats the Bai–Marvian synthesis as an imported premise, and does not identify a driver, a vacuum supplier, an efficient compiler, interacting old Hamiltonians, or a retained audit. `proposed_retained` with `bare_retained_allowed: false` and `audit_required_before_effective_retained: true` is not an audit pass.
- Open: the unrevalidated 38-page synthesis proof; sparse compilation and target-specific certificates; microscopic drive, vacuum, phase reference, and measured-energy identification; autonomous clock, halt, and indefinite reuse; interacting old Hamiltonians and disconnected ports; a common phase for coherently controlled programs with different `W`; and preparation on the root battery size. Retained status remains an open audit.
