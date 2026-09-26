# Centered Gauss constraints, staggered sectors and an adjoint escape

2026-09-21. A separate conditional operator/ensemble diagnostic. Author
derivation; independent review pending. This does not alter the published
long-wavelength theorems or establish additional physical photons.

## 1. Why the numerical signal needs a full momentum-space check

The Gauss-loop equilibrium screen uses a centered divergence, with Fourier
symbol proportional to s(k)=(sin k1,sin k2,sin k3). The earlier local-curl
note already records its extra high-frequency zeros. Here the sharper
question is whether the constrained static ensemble itself relates the
correlations near different corners of the Brillouin zone.

Use the single-species seven-state restriction: E(x) is zero or one of
the six signed unit axes, and pi_z(E) is proportional to z^n on D2 E=0,
where D2 E(x)=sum_i[E_i(x+e_i)-E_i(x-e_i)]. The following statement is
exact on an EVEN periodic torus. It is not automatically an identity on
the odd boxes used in the numerical screen.

For eta in {0,1}^3, put D_eta=diag((-1)^eta_i) and define

    (T_eta E)_i(x)=(-1)^(eta.x) (-1)^eta_i E_i(x).       (1)

Each transformation is an involution, preserves the seven-state menu,
occupation, and activity weight. Since the two neighboring parity factors
are equal,

    D2(T_eta E)(x)=(-1)^(eta.x) D2 E(x).                (2)

Thus T_eta is a measure-preserving bijection of the constrained grand
ensemble. It is a statistical symmetry, not an allowed immutable-record
event: the map can change a record label. The same construction works
separately on E and B in the thirteen-state two-species ensemble, preserving
the shared capacity restriction because it changes signs only.

With Fourier convention exp(-ik.x),

    Ehat_(T_eta E)(k)=D_eta Ehat_E(k-pi eta).

Consequently the matrix structure factor of the finite even grand law obeys

    S(k+pi eta)=D_eta S(k) D_eta,                       (3)

and its trace is identical at all eight translated wavevectors. Global
E inversion also preserves the ensemble, so its one-point mean is zero;
the same identity holds with connected covariances. Any subsequential
infinite-volume limit of these even periodic measures inherits the local
symmetry. When a spectral density is not an ordinary function, (3) is
understood for the covariance spectral measure under momentum translation.

In particular, if this symmetric thermodynamic state has a nonanalytic
transverse projector near zero, it has the corresponding translated
structure near every pi eta. This is a conditional implication, not a proof
that the phase exists. An odd finite torus frustrates the parity map at its
seam; no even/odd equivalence or unbroken symmetry of an arbitrary selected
infinite-volume state is claimed.

## 2. Geometric origin and the distinction from kinetic modes

An occupied E_i slot at x joins charge vertices x-e_i and x+e_i. Those
vertices have the same coordinate parity. The centered charge graph on
the infinite lattice therefore splits into eight parity subgraphs. Different
subgraphs are not statistically independent: choices of axis at a shared
midpoint compete for the one-record capacity. This observation explains
the eight constraints without asserting eight decoupled gauge theories.

For a supplied *undamped centered Maxwell operator* with curl symbol
C_0(k)=[i s(k)]_cross and generator

    G_0(k)=c [[0,C_0(k)],[-C_0(k),0]],

the transverse eigenvalues are +/-i c|s(k)|, twice each. All eight pi eta
are zeros; expansion near a corner replaces q by D_eta q. This is an
operator comparison, not the dispersion of the full stochastic record
generator at arbitrary lattice wave number.

That distinction matters. The actual whole-record process has positive
symmetric exchange floor kappa. For every one-site feature, that floor
acts on its Fourier sum exactly with multiplier

    -4 kappa sum_i sin^2(k_i/2),                        (4)

or N times this on the Euler clock. This term does not vanish at the seven
nonzero corners. Other rates couple observables, so (4) alone is not an
all-time correlation-decay bound. It does, however, invalidate importing
the undamped operator's eight cones as eight proved slow kinetic modes.
The earlier Euler/fluctuation theorems control fixed smooth macroscopic
modes near k=0, not arbitrary staggered observables. The numerical static
ensemble and the kinetic model must keep their separate hypotheses.

## 3. A local adjoint-difference alternative has only one zero

The centered stencil is a choice. Define forward and backward differences

    d_i^+ f(x)=f(x+e_i)-f(x),
    d_i^- f(x)=f(x)-f(x-e_i),
    C_+=d^+ cross, C_-=d^- cross.

On a periodic lattice C_+^*=C_-. Each has its own exact divergence identity:
d^+ dot C_+=0 and d^- dot C_-=0. Supply the field equations

    partial_t E=c C_- B,     partial_t B=-c C_+ E.       (5)

Then d^- dot E and d^+ dot B are conserved, and the real quadratic energy
sum_x(|E|^2+|B|^2)/2 is conserved by adjointness. Both are elementary
identities of this specified operator, with no probabilistic assumptions.

For v_i=exp(ik_i)-1, C_+=[v]_cross and C_-=C_+^*.
The vector triple-product identity gives

    C_+^* C_+=|v|^2 I-v v^*,
    C_+ C_+^*=|v|^2 I-conj(v) v^T.                     (6)

Thus the four transverse eigenvalues of (5) are +/-i c|v|, twice each,
and two longitudinal eigenvalues are zero. The transverse frequency obeys

    omega^2=4 c^2 sum_i sin^2(k_i/2),                   (7)

with its only Brillouin-zone zero at k=0. For |k| small it has the same
leading isotropic speed as the centered stencil. It provides a concrete
operator-level escape from the additional centered zeros.

This is standard finite-difference/adjoint machinery, not a new physical
theory. The spatial assignment of the two fields, their cubic action,
record-based readouts, formation law, and a positive whole-record Markov
generator realizing (5) have NOT been supplied here. In particular,
substituting a nicer symbol into a continuum comparison does not prove
that the existing stochastic dynamics realizes it. Site rotations of the
old polar/axial readout cannot silently be reused for displaced components.

## 4. What this changes in the campaign

The encouraging fugacity-one spectrum should be tested across the full
Brillouin zone and, separately, in the formation-selected sector. The exact
even-volume symmetry is a cheap diagnostic before expensive scaling fits.
It does not erase the static result or the small-k wave construction.
It prevents identifying either one with a unique physical field spectrum
without inspecting the additional sectors and actual kinetic damping.

The adjoint alternative keeps open a local construction with one transverse
zero. Its microscopic realization is a new obligation. Nothing here proves
a universal obstruction, Lorentz symmetry, a quantum vacuum, a physical
carrier count, or any fraction of a TOE.
