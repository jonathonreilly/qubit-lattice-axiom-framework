# Energy spread of the first actual birth on the seven-site path

Root analytic candidate, September 23, 2026. This is an exact conditional
calculation inside the **supplied compensated rotor target**, with its
stipulated monitored birth channels. It does not derive an apparatus, bath,
rest energy, or native record-formation law. A number-energy offset also
changes the meaning of an energy cost; its exact effect in this target is
derived below.

Use the seven-site path, A={1,3,5}, B={0,2,4,6}, initial all-A-plus,
B-empty, E=0 physical word `Omega`, and the actual resolved or coherent
birth instrument. Write

    H=K D+delta H4,  H4=-2 sum_(a<c sharing B) S_ac^*S_ac,
    L_mu=sqrt(kappa) B_mu,  Gamma=sum_mu L_mu^*L_mu.

Take K>0, delta>=0, kappa>0. The full physical path matrix has 52 words.
The initial word obeys `D Omega=0`, `H4 Omega=-12 Omega`, and
`Gamma Omega=12 kappa Omega`, so its target energy is sharply
`E_initial=-12 delta` and the first-event rate is `12 kappa`.

Let `rho_post=sum_mu L_mu |Omega><Omega| L_mu^*/(12 kappa)` be the
unconditioned state immediately after a first marked birth, with its mark
record discarded. The resolved and coherent instruments need not yield
the same density matrix, because the coherent edge channel retains sign
cross terms. Their first two target-energy moments nevertheless agree.
Every first channel vector lies in `D=0`, so its H expectation and H-square
expectation are `delta <H4>` and `delta^2 ||H4 v||^2` respectively,
independent of K. The exact channel identities are:

| first channel group | number | norm squared per channel | `<v,H4 v>` per channel | `||H4 v||^2` per channel |
|---|---:|---:|---:|---:|
| resolved endpoint A=1 or 5 | 8 | 1 | -2 | 12 |
| resolved middle A=3 | 4 | 1 | 0 | 0 |
| coherent endpoint edge | 4 | 2 | -4 | 24 |
| coherent middle edge | 2 | 2 | 0 | 0 |

Thus both instruments give total norm weight 12, H4 first moment -16,
and H4-square first moment 96. Consequently,

    tr(H rho_post)=-4 delta/3,
    tr(H^2 rho_post)=8 delta^2,
    Var_rho_post(H)=56 delta^2/9.                         (1)

The mean change of target energy at a first birth is `32 delta/3`.
Because the initial state is an H eigenvector, the Hamiltonian part of its
unconditioned energy derivative vanishes and the full anticommutator in
the birth dissipator gives

    d/dt tr(H rho_t)|_(0+) = 12 kappa * 32 delta/3
                             = 128 kappa delta.              (2)

This is an initial derivative, not integrated all-time heating. It is
positive for delta>0 in the specified target energy convention, and zero
when delta=0.

The uniform record-energy offset `H_mu=H+mu N` leaves every marked count
history and conditional density within a fixed-number sector unchanged
for this initial fixed-N state: each no-event number-block phase cancels
in density evolution, and each birth changes N by two. But a birth-energy
change becomes `Delta H+2mu`; hence its mean is
`32 delta/3+2mu` and the initial derivative becomes
`128 kappa delta+24 kappa mu`. The conditional transition-energy variance
remains `56 delta^2/9`. A number offset can therefore remove the mean
but cannot remove the spread when delta>0. This only says that one common
fixed energy shift does not align all post-birth spectral components;
it does not prohibit a reservoir with a spectrum, coherent preparation,
or interaction energy.

The stated moments use the actual channel vectors in the full Gauss
sector. They do not assume a matter-only projection, changed formation
instrument, or one common second waiting time. The adjacent exact
`first_birth_energy_spread_check.py` used the root rotor-path builder to
reconstruct all twelve resolved and six coherent first vectors, checked
all 52 physical words and every first vector against the separately built,
sealed independent PRE matrix, and found all table entries with integer
arithmetic. Its mean/variance arithmetic uses `Fraction`. External and
adjacent portable runs succeeded with identical results; logs and receipts
are preserved. This source comparison is a strong exact control, but the
new energy-spread interpretation has not received independent post-result
review. It is not a formal retained claim or an autonomous-reservoir
no-go.
