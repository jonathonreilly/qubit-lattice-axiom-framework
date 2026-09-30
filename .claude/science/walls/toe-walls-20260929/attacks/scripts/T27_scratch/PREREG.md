# T27 pre-registration (written before any test script was run), 2026-09-29 ~14:45Z

Attacker: Claude Sonnet 5.5 (same vendor family as the supervisor; same-family checks).

Wall T27 = L06-W3. Route under test (R1): keep the wall's own supplied model (SU(2)
one-rishon plaquette from docs/A_NON_ABELIAN_GAUSS_LAW_HAS_NO_RECORD_PATTERN_SOLUTIONS_...
2026-09-03) but change ONE premise: the readout basis. Replace "records are colour-resolved
patterns in the fixed occupation basis" by "records are the colour-blind local invariants
(matter occupation n_v, link orientation o_e, and, at valence >= 4, vertex coupling labels)".
Question: in that readout, is the non-abelian Gauss law a local support rule on record
patterns, and does the dynamics act locally on those patterns?

Model conventions copied from the note's runner (scripts/non_abelian_gauss_law_no_record_pattern_
solutions_check_2026_09_03.py): 4-cycle, links e_k=(i=k,j=k+1), 8 JW matter modes (mode 2v+a),
link = orientation (i/j) x colour bit, U^{ab} = -|j,b><i,a|, E^a_{e,s}=P_s tau^a/2,
G_v^a = rho_v^a + sum_{e at v} E^a_{e,v}, H_hop = -t sum_e eta_e sum_ab [psi^dag_ia psi_jb U^ab + h.c.],
eta=(1,1,-1,-1), t=1.

## Test A (baseline: is my build the note's model?)  -- must pass before B..E mean anything
PASS: dim 65536; [G,H_hop]=0 exactly; rank of the Gauss kernel = 82; zero computational-basis
patterns in the kernel; dim(R cap I) = 1296 atoms; ground energy of H_hop on the kernel = -sqrt(34)
(-5.830951894845) to 1e-9.
FAIL (any mismatch): my model is not the note's; fix the build; B..E are void until A passes.

## Test B (completeness and support rule of the colour-blind labels)
For each of the 1296 atoms (n_v in {0,1,2}, o_e in {i,j}) compute rank(P_G P_atom).
PASS: every rank is 0 or 1; exactly 82 atoms have rank 1; the 82 rank-one images are mutually
orthogonal and span the kernel; and the set of rank-1 atoms equals the local Z2 rule
"for every vertex v, (number of rishons at v) + [n_v == 1] is even".
FAIL: some atom has rank >= 2 (labels do not resolve the Gauss sector), or the rank-1 set differs
from the Z2 rule (the Gauss law is not a local parity rule on these labels).

## Test C (locality of the hop in label space)
Project H_hop to the 82-dim basis of unit label vectors. PASS: (C1) every nonzero entry connects two
labels that differ by exactly one link hop (one orientation bit flips, the two end-vertex occupations
change by one in opposite directions, all other labels equal); (C2) the spectrum equals the full-model
Gauss-sector spectrum to 1e-9; (C3) the magnitude |<a'|H|a>| depends only on the labels at the two
end vertices and the links touching them (independent of the labels of the far vertices and the
opposite link).  FAIL: any entry at longer range, or a far-label dependence in the magnitude.
Record separately: whether the SIGN depends on the Jordan-Wigner string (far matter parity).

## Test D (locality of the magnetic/plaquette term)
Tr U_p + h.c. (U_p^{ad} = sum U_01^{ab}U_12^{bc}U_23^{cx}U_30^{xd}, the note's holonomy).
PASS: gauge invariant ([G, TrU_p]=0 exactly); in the label basis it connects only labels that differ
by shifting every rishon one step around the plaquette (all four orientation bits flip), matter
labels unchanged.  FAIL: it changes matter labels or is not gauge invariant.

## Test E (valence-6 vertex, the Z^3 star: cost of the labels and covariance)
Local space = 2 matter modes x 6 rishon colour qubits (256 dims), all six rishons at v.
PASS: Gauss kernel dimension is c(6)=10 (= 5 for n=0 and 5 for n=2, 0 for n=1); the 5-dim
intertwiner space is resolved by the commuting local invariants (E_1+E_2)^2, (E_1+E_2+E_3)^2,
(E_1+..+E_4)^2, (E_1+..+E_5)^2 (5 distinct joint labels); cube-rotation group (24 rotations acting
as permutations of the 6 links) acts on the 5-dim space with a character decomposing into
S4 irreps; report the decomposition.  Bits needed for the vertex label: ceil(log2 10)=4.
FAIL: joint labels not distinct (needs non-local operators), or kernel dimension differs.

## Test G (route R2: qubit as gauge singlet, parton/baryon site)
SU(2) Abrikosov partons on L=4 sites (Fock 4^L=256): local gauge generators G_i = (f_up^dag f_down^dag,
f_down f_up, (n-1)/2). PASS: kernel of all G_i has dimension 2^L, is spanned by 2^L computational-basis
patterns (single occupancy), the spin operators S_i and S_i.S_j commute with every G_i, and the
number of Gauss-satisfying basis patterns is 2^L out of 4^L (compare: 0 of 65536 in the wall's model).
SU(3) baryon site: 3 colour modes per site, L=3 sites: kernel of SU(3) colour generators is the span of
{|000>,|111>}^L, i.e. 2^L patterns, and the site is a qubit.
FAIL: kernel dimension differs or patterns are not in the kernel.  (Passing G does NOT pass the wall:
it shows a kinematic gauge singlet per site but no dynamical gauge field; that judgement is made in
the report, not by the test.)

## What decides the outcome
- If A..E PASS: the "0 of 65536" and "colour invisible" parts of the wall are readout-basis
  artifacts (route R1 survives as a reframing); what is left is HOSTING (label registers on Z^3 sites
  with NN formation and cubic covariance) and the readout-context selection. Outcome MISFRAMED or
  PRICED depending on whether the residue is one named premise.
- If B or C FAIL: R1 is dead in the wall's own model; outcome STANDS.

## Addendum (written 14:50Z, AFTER all scripts had been run; disclosure, not a pre-registration)
The star test (t27_E_star.py), the valence-6 vertex test (t27_E_vertex6.py), the SU(3) vertex test
(t27_E3_su3_vertex.py) and the parton test (t27_G_partons.py) were designed and run after tests A-D had passed.
Their pass/fail readings are the ones in Test E / Test G above plus the docstring at the top of each script,
all of which were written before the corresponding run (star: 4-link star, the pair Casimir at the centre must
resolve every rank-2 atom, the hop must stay single-link-local, kernel dimension must equal
sum_o prod_v c(p_v) = 186; SU(3): kernel nonzero iff (n+p) = 0 mod 3, and 5 distinct local Casimir labels at
p = 6). The star and SU(3) tests were not in this file before running; only the scripts' docstrings carry
their readings. Between writing and running, the scripts were changed only to fix an out-of-memory SVD
(full_matrices on a tall matrix, killed with exit 137 before any result) and a matter-number eigenvalue count,
before any PASS/FAIL line came from the fixed code.
Not tested: Jordan-Wigner sign locality, static-source energies, SU(3) plaquette or full SU(3) dynamics, links
of spin above 1/2, cubic covariance of any hosting, any formation dynamics.
