# Block 1: fixed-payload charged phase route comparison

Status: exploratory derivations. No independent reviewer or phase theorem.

## Exact electric-density spectral moment

Let D be outgoing incidence, B the oriented plaquette boundary, DB=0.
For real link f and site h, set F=E(f)-rho(h). For charge-one matter,
H=H_E+H_on+sum_l h_l+sum_p kappa_p(1-Re W_p),
h_l=V_l+V_l^dag, [E_l,V_l]=V_l, and [rho(h),V_l]=(D^T h)_l V_l.
This holds with the hard finite shift because the raising commutator is exact.
Writing v=f-D^T h and b=B^T f gives the operator identity

    [F,[H,F]] = -sum_l v_l^2 h_l
                 +sum_p kappa_p b_p^2 Re W_p.

For a pure ground vector, half its expectation equals
sum_n (E_n-E_0)|<n|F|0>|^2. The variance is the zeroth moment,
including zero-energy ground-space transitions unless projected out.
Gauss gives F=E(v) on the physical space. For f=D^T h it vanishes exactly.
For a transverse plane-wave f, the magnetic contribution has a curl-squared
factor O(k^2), but the charged hopping contribution generally does not.
Thus copying the pure-link variational argument drops an actual term. Even
an upper moment needs a lower bound on nonzero-energy spectral weight before
it implies a small excitation energy. This is a route obligation, not a no-go.

## Conjugate opposite-charge alternative

For each finite spatial phase history A_t, take two independent CAR sectors
with h_minus(A_t)=h_plus(A_t)^*. Give them opposite gauge charges and
conjugate bare hopping matrices. Temporal Gauss insertions are conjugate too.
Then B_minus=B_plus^* for the SAME ordered product, and the full Fock trace
is det(I+B_plus) det(I+B_plus)^*=|det(I+B_plus)|^2>=0.
This is a different supplied Hamiltonian from PR8099: charges and flavor
symmetry differ. It removes only the fixed-history fermion phase. Hard finite
integer links still lack an entrywise-positive continuous phase heat kernel.

A finite Z_N phase carrier with cyclic phase-step electric Laplacian has
entrywise nonnegative heat kernels and diagonal magnetic/Peierls factors.
Its exact Gauss constraint is modulo N. Combining it with the conjugate
matter pair is a candidate fully positive finite-payload Trotter measure.
Need derive exact projected trace, local transfer law, and continuum/Trotter
limits before claiming this construction. Any Coulomb-phase bridge is separate.

Free two-node h_plus and h_minus(k)=h_plus(-k)^* give four nodes, total Hall
cancellation and matching free metrics. Gauge-neutral cross-species pairing
is an allowed possible instability unless excluded or controlled. It must not
be hidden by calling the determinant-positive model a proven Weyl phase.

## Literature and actual read scope

Falconi, Bonn 2023 slides: title, introductory scope, action and regularization,
Ward identities, running-coupling construction through slide 23 have been read.
It supplies a comparison, not a theorem imported here: the formal kernels have
C^n n! bounds, and the IR cutoff removal is stated perturbatively. Search did
not locate a final full manuscript; do not claim none exists.

Frohlich-Spencer IHES/P/81/40, 1981 preprint: recovered actual 85-page PDF from
IHES archive. Abstract and opening introduction pages 1-9 read so far. It
states pure U(1) and large finite Z_N intermediate QED phases; it does not yet
supply our dynamical-matter theorem. Read exact conditions and proof next.

Tool failures preserved: initial PDF read raced an unfinished download; later
pdftotext was unavailable. The PDF download completed, and pypdf extracted both
files successfully. No mathematical inference used the failed commands.
