# Frozen supervisor propagation candidate — 2026-11-08

This proof was written without reading the independent worker's deliverable.
The worker has sent only progress statements: a controlled-reversal readout
is possible with supplied quantum gates; data recording erases a tested
relative phase; using a spectator for a record leaves the original global
code. Those statements are prior exposure, not independent confirmations of
the following separate construction.

## 1. A genuine local permanent-record relay

Choose rank-one projectors as the supported record possibilities inside the
supplied M_2(C) domain. At an unrecorded site x, let N_R(x) be its already
recorded adjacent sites. Define one fixed conditional formation distribution:
if k=|N_R(x)|>0, mu_x=(1/k) sum_{y in N_R(x)} delta_{P_y}; if k=0, use the
unitarily invariant probability measure on rank-one qubit projectors.
Only new records are appended. This is normalized, depends only on immediate
neighbor record contents, varies with those contents, and is covariant under
all translations/proper cubic rotations (indeed also under simultaneous
unitary conjugation of contents). Old contents are never rewritten.

Supply an initial record P at x_0 and any finite self-avoiding path
x_0,...,x_L, with no other initial records; form the path sites in order.
Every previously recorded neighbor of the next site carries P, even if the
path touches itself. Induction gives mu_{x_j}=delta_P and the final record P
at arbitrary graph distance attainable by a straight path. This is a lawful
conditional realization with an externally supplied formation order; no
update law, rate or time scale is derived. It is not a full quantum code:
it transports an existing record value, not unknown coherent amplitudes.
Permanence and elementary locality therefore do not themselves prohibit
mediated influence. No proposed axiom edit is needed for this example.

## 2. A different phase readout using a returned adjacent route

Use the four native sites numbered 1,2,3,4 along one link. The source has
J0=(1000+0001)/sqrt(2), J1=(1000-0001)/sqrt(2).
Supply a fresh unrecorded pointer a adjacent to site 1, initially |0>.
Let B=X_1 X_4. B J0=+J0 and B J1=-J1.
This B need not preserve the entire five-state code; restrict this witness
to span(J0,J1), not the full code. A Hadamard test on B is:

H_a; CNOT(a,1); routed CNOT(a,4); H_a.

On the 5-site chain a,1,2,3,4, route the distant CNOT by swaps
(a,1),(1,2),(2,3), perform CNOT(3,4), and undo the three swaps in reverse.
The routing conjugation is exactly CNOT(a,4) and identity on the three
intermediate factors for arbitrary entangled inputs. The complete circuit
maps J0|0>_a to J0|0>_a and J1|0>_a to J1|1>_a. Selectively record a in Z
and never operate on a again. The four data sites remain in this tested
two-dimensional code; a superposition undergoes the intended observable
measurement, rather than retaining its coherence across the measured sectors.

This uses 8 adjacent two-site gates and 2 onsite Hadamards: one adjacent
CNOT and seven gates for the distance-four route. It supplies tensor quantum
kinematics, coherent initialization, gate availability, a driven schedule,
Born/Lueders probabilities, and an irreversible final record interpretation.
The axioms alone have selected none of these. The pointer's output |1>
is outside the original fixed-spectator global code.

## 3. Record-first comparison

Complete computational-basis recording of the data sends J0 and J1 to the
same mixture (|1000><1000|+|0001><0001|)/2. Every later process with identical
remaining inputs has the same output distribution on both. In the circuit
above each output is then fair. This is a counterexample to the particular
record-first implementation, not a theorem excluding different instruments,
preparation records, causal histories, or coherent fresh-site routes.

For J3=(1100-0011)/sqrt(2), the same data dephasing leaves half its weight in
Q=JJ*. The orthogonal symmetric partner (1100+0011)/sqrt(2) is outside Q.
This is a directly computed failure of equating four permanent Z records with
the live five-state quantum register.

## 4. Remaining target

Neither this circuit nor the record relay is the single autonomous homogeneous
Admissibility/Record realization of the whole glued code. The required next
object is a specified joint live-state/record-history law with local
propagation, code and output allocation, and checked symmetry. The current
axioms specify local formation odds but not that joint law. An axiom
clarification proposal remains a separate PR, not adopted science content.

## 5. Electric-value readout (second frozen derivation)

Before requesting an independent extension, derive a full-code physical
readout. The j=0 projector is P0=|J0><J0|, and E^2=(3/4)(Q-P0) on code.
U0, chronologically H_1,CX(1,4),X_4, prepares J0 from 0000. Decode by
X_4,CX(1,4),H_1; copy the predicate "all four decoded bits are zero" into
a fresh |0> output; undo the decoder. This exactly measures P0 and hence
E^2, preserving the full five-state active code after each outcome.

Use native coordinates data d_i=(i,0,0), i=1..4; output a=(1,1,0),
work b=(2,1,0), c=(3,1,0). These three are spectators at phase 0
(two coordinates differ from zero mod5), and the seven-site induced graph
is connected. Supply all three unrecorded in |0>. Negate the four decoded
data bits, perform CCX(d1,d2;b), CCX(b,d3;c), CCX(c,d4;a),
CCX(b,d3;c), CCX(d1,d2;b), and restore the four bits. The work bits
return to 0 for every data input; a flips precisely for all-zero data.
Decompose each Toffoli with V^2=X via five two-site gates, and route every
pair by forward adjacent SWAPs, the gate, and reverse SWAPs on this seven-site
graph. Routing is an exact tensor-permutation conjugation even through dirty
or entangled data. The final operation is
(I-P0) tensor I_a + P0 tensor X_a, with the two work bits restored.
The output probability for value 1 is Tr(P0 rho) on any encoded density
operator; report electric value 0 then, and 3/4 for output 0.
This is gauge invariant because j sectors are invariant under both endpoint
actions. It requires the same supplied quantum/instrument/schedule conditions
as above and uses a larger record-output space than the original frozen
spectator code. No unknown state is copied, and no measured record is reused.
