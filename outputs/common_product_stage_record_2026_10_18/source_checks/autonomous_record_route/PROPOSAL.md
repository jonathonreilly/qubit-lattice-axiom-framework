# Static two-body coherent completion bit: a local stationary candidate

Status: proposed construction and analytical exploration, not independently checked. There is an exact band-center two-port gate that transmits a head while applying X to one shared, initially supplied record qubit, up to one known common phase. It uses only static real positive one-/two-qubit blocks on an explicit cubic nearest-neighbor graph. The originally suggested odd arm-length offset is geometrically obstructed; two positive phase cells repair it. Finite-band stationary error can be bounded, but attachment to the complete autonomous emitter/source and a finite-window completion theorem remain open. This is not permanent halting, native Record identification or autonomous initialization.

## Inputs and exposure

Root supplied the exploratory terminal-contact/interferometer idea. I independently derived its local reflections, identified the cubic parity obstruction and constructed the phase-cell repair below. This is source-exposed original mathematics, not independent checking or a claim to have originated the general idea.

Use the canonical real mixer and positive Q conventions from the original endpoint note at SHA256 71c65d72570a32365ded6dacfc78308ac8429d9e8003a3731af88b5600eb45ff, previously read complete relevant source/filter/junction and geometry passages. The unchanged nominal converted lead is supplied by composition1cc6fec524a8184f844711a4fa6d72fcc7cd13a4c8b413cbc064cd4b2201df78 and its check f1653ba00c0f3d10d8846c1f010ad6dcddcd25535837dd87d17b9e655019a15c. The stationary wider band q=pi/2±4e-6 has checked source d79a1e9abbf0508a05169d4588539063854f0604ba8db933cf878496aa7328a2 and review3f721b75911630e0aec48688893c6bae84a182cafaa1012c977e9e262d6e180d. These identify the incoming architecture, not a theorem after adding this new gate. No runtime or finite theorem is inherited.

All coefficients below use the same nominal new hopping j>0. The record has no independent free Hamiltonian in this ideal construction. Its state |0> is an explicitly supplied initialization. The old/source B acts on the shared fiber as before; the new gate acts as identity on that fiber and uses only its kinetic energy. No scientific execution, numerical sweep, solver, delegation, Git/W/checkpoint/prompt/model change, axiom or publication occurred. Only this deliverable is written. Applicable unchanged workflow is reused.

## 1. Terminal contact and exact record action

At a terminal head site T connected to its one inward neighbor by -j, install the positive contact

    H_T=j n_T(I+X_R).

It is a genuine two-qubit operator of norm2j, PSD on the ENTIRE head/record space. With one incident Q(-j) bond the terminal's one-head diagonal is2j+jX_R. There is no separate record rotation, drive or timed intervention. Head number is conserved; record excitation number need not be.

In record-X sector x=+1 or-1, let n>=0 measure distance outward from the terminal toward the junction. For incoming exp(-iqn) plus reflected r_x exp(iqn), the terminal equation at kinetic E(q)=2j-j(w+w^-1), w=exp(iq), gives

    r_x(q)=-(x+w)/(x+w^-1).

At q0=pi/2,

    r_+(q0)=-i,  r_-(q0)=+i,
    r_terminal(q0)=-i X_R.                         (1)

Thus reflection applies X to a computational record |0>, producing |1> with common phase-i. The reflection is exactly unitary for real q in either X sector. A shared record coupled to two terminals is not duplicated: X_R commutes with both contacts, so decomposition into its two eigenspaces gives an exact pair of scalar scattering problems even when the head occupies a coherent arm superposition.

A direct controlled hop would have the form (a_y^*a_x+a_x^*a_y)X_R on three distinct qubits. That is THREE-body and is not an admissible block under the present two-body contract. The terminal reflection construction avoids supplying it or assuming a gadget reduction without proof.

## 2. Why an odd arm-length offset is unavailable in the stated geometry

An ordinary cubic nearest-neighbor graph is bipartite. Two terminals adjacent to the SAME record vertex have the same lattice parity. The two arm attachment vertices on a four-edge real-Hadamard junction square occupy opposite corners and likewise have the same parity. Therefore the two terminal-to-attachment path lengths have equal parity, irrespective of detours. Their length difference cannot be odd.

At band center a one-edge arm difference would give the desired extra round-trip factor w²=-1, but that odd difference is incompatible with the stipulated shared local record and square junction. A signed hopping on an arm does not repair this: its sign is traversed twice and cancels. This is a precise obstruction to that geometric ansatz, not a universal no-go for completion bits or two-body gates.

## 3. Positive reflectionless phase-cell repair

On an ordinary j arm replace one bond by hopping -sqrt(2)j and set its two incident one-head diagonals to3j, retaining -j connections to the adjoining sites. This uses only

    Q(-sqrt(2)j)
    +(2-sqrt(2))j n_left+(2-sqrt(2))j n_right,        (2)

in place of the ordinary bond; each adjacent ordinary bond supplies another j to its incident diagonal. All coefficients in(2) are positive, and no vacancy scalar is introduced.

For left incidence at the first cell site, at q0 let amplitudes1+a and b on its two sites. Their equations give

    sqrt(2)b=(1+i)+(1-i)a,
    b=(1+i)(1+a)/sqrt(2).

Hence a=0 and b=(1+i)/sqrt(2). The free bond has transmission w0=i in these site reference planes. The cell's relative one-way transmission is therefore

    eta=b/w0=(1-i)/sqrt(2).

It is reciprocal and reflectionless from both sides. One cell gives relative round-trip eta²=-i. TWO disjoint such cells on one arm give eta^4=-1, while preserving the arm length and its parity. At q0 there are no intercell multiple reflections; their ordinary separation contributes only the same free propagation already included in the arm reference plane. This replaces the forbidden odd geometric offset by positive static two-body scattering phases.

## 4. Explicit cubic layout with one record

Use local translated coordinates for this appended gadget; it can be placed away from the existing device. Record R=(0,0,0), terminals T0=(1,0,0), T1=(-1,0,0). Both terminal contacts are NN to this one record.

Arm0 path is

    (1,0,0),(2,0,0),(2,1,0),(1,1,0),(1,2,0),...,(1,8,0).

Arm1 path is

    (-1,0,0),(-1,1,0),...,(-1,8,0),(-1,8,1),(0,8,1).

Each has11 head vertices and10 edges. Their attachment ends are A0=(1,8,0), A1=(0,8,1). Port starts P_in=(0,8,0), P_out=(1,8,1) are the other corners of their unit square. Install all four junction edges with hopping block -jU, U=2^-1/2[[1,1],[1,-1]], in the stated arm/port ordering. These are three negative and one positive real hopping, each magnitude j/sqrt(2). At each of the four square vertices add the positive vacancy (sqrt(2)-1)j(I-n); with the incident ordinary arm/lead bond this restores diagonal2j and supplies total scalar

    c_R=4(sqrt(2)-1)j.                              (3)

Put the two phase cells on arm1's bonds between y=2 and3 and between y=5 and6. They have disjoint endpoints and ordinary neighbors. The two arms, cells, shared record and junction are all distinct vertices with NN installed interactions. Unused geometric NN adjacencies carry no automatically assumed interaction.

An input lead extends from P_in along (0,8+m,0), m>=0. An output lead extends from P_out along (1+m,8,1), m>=0. A translated/rotated finite connecting path can join the existing new-j output to this input port; its chosen length and common propagation phase must be recorded in an eventual complete geometry. No zero-length connection or resource count for that as-yet-unspecified cable is asserted. The local two-arm/junction portion contains24 head vertices,24 head-hopping edges (20 arm,4 junction), and ONE additional record qubit, before counting external lead vertices. Two phase cells replace existing edges rather than adding vertices.

## 5. Full positive inventory and stationary gate

Local head blocks are18 ordinary Q(-j) arm bonds, two Q(-sqrt(2)j) phase bonds, four signed junction Q bonds of magnitude j/sqrt(2), four positive phase-cell onsite occupations (2-sqrt(2))j n, four junction vacancies (sqrt(2)-1)j(I-n), and the two positive terminal contacts j n_T(I+X_R). Ordinary lead Q(-j) bonds continue outward. There is no terminal entrance compensation J n_T: the record contact supplies the missing terminal diagonal j along with its intended jX_R term. All blocks are static, real, PSD and at most two-body on this explicit lattice. The only new common scalar in this inventory is(3). Shared record incident-block norm load is4j, not the norm of a supplied three-body operation. Internal old/source B is not duplicated.

At the port origins the two arm reflections have the common factor w^(2(L+1)), L=10, just as in the canonical real mixer. Arm0 reflection is w^22 r_terminal and arm1 is its negative at q0. Thus

    S_R(q0)=U diag(w0^22 r_terminal,-w0^22 r_terminal)U^T
            = i X_port tensor X_R,                 (4)

since w0^22=-1 and r_terminal=-iX_R. In either incident port the head exits the opposite port with zero reflection and record action X_R, with the SAME scalar phase+i. In particular |0>_R becomes|1>_R. An arbitrary record input experiences X, not erasure or reset. Arbitrary old/reference input is untouched by this local gate except the common propagation phase and the pre-existing old operation. At the center there are no four separately chosen old-column phases.

## 6. A bounded nonzero-band stationary estimate

Fix |q-pi/2|=x<=4e-6, or more loosely x<=1e-3 for the elementary bounds here. For a real endpoint potential v, r_v=-(v+jw)/(v+j/w) has derivative magnitude<=2/|sin q|<3. This covers terminal v=+/-j and the cell's parity potentials v=j(1-sqrt(2)), j(1+sqrt(2)). The terminal operator therefore obeys

    ||r_terminal(q)+iX_R||<=3x.

For a cell, reflection a is the parity half-sum, with a(q0)=0, hence |a|<=3x. Transmission b is the half-difference; its relative factor B=b/w has B(q0)=eta and derivative magnitude<=4 (using |b|<=1 on the real band). Thus |B-eta|<=4x and |B²-eta²|<=8x. These bounds retain the correct FREE-bond phase w.

For ANY unit-modulus terminal/load reflection r in a given record-X sector, exact concatenation through one cell gives the same scalar formula as the canonical phase-filter proof, with direct term at most3x and denominator>=1-3x. Relative to eta² r its error is at most

    3x+(8x+3x)/(1-3x)<=15x.

All zero-floor bounds are non-strict at x=0. The actual load after the first cell is again unit-modulus because this is a real finite terminated arm. Applying the same estimate to the second cell gives arm1 reflection within30x of MINUS the otherwise identical unmodified arm reflection. The two equal arm lengths ensure their unmodified reference factors coincide. No derivative of an approximate load is required and no intercell return is dropped.

Conjugating the two arm matrices by U preserves operator norm. Relative to the target

    S_target(q)=rho_R(q) X_port tensor X_R,
    rho_R(q)=-i w^22,

the arm0 discrepancy is<=3x and arm1 discrepancy<=33x. Consequently

    ||S_R(q)-rho_R(q)X_port tensor X_R||<=33x.       (5)

This is a coherent full two-port/record scattering bound, not merely a transition probability. On the fixed4e-6 band it is<=1.32e-4. It includes reflected output and the wrong-record component; neither is postselected away. The exact scalar rho_R(q), any connection-cable phase, the new c_R time phase and old aging must enter a full comparator. Wavepacket weighting could improve(5), but no such combined theorem is claimed here.

## 7. What is still missing for an autonomous completion record

The local theorem candidate is a stationary band-center gate with a nearby-band error bound. It does NOT yet show that the existing emitter-launched packet reaches and leaves this new gadget in a specified finite window. Adding a reflecting multi-arm region changes the global endpoint Green function, record-dependent return phases, possible bound states and packet normalization. Even small stationary reflection is not permission to inherit the previous actual mass/escape constants unchanged.

The attached construction must retain both record-X sectors coherently. The gate is scalar on each old/source B eigenspace but has different record-sector reflection phases. Existing old/source closed components remain closed channels at the gate; their returns and any record-dependent closed resonances need bounds. Unlike the source's one-selected-channel presentation, the enlarged record fiber has two degenerate propagating record-X channels; analyzing each conserved sector is legitimate, silently reusing a rank-one spectral assertion for the entire enlarged fiber is not. Their coherent recombination and the initially supplied |0> must be paid in the final operator norm.

A decisive next bounded obligation is: freeze the connecting path/placement, derive the complete full-fiber reflection/transmission and closed-load kernel of this gadget, compose it with the ACTUAL converted/emitter device, and prove a comparison whose ideal output has record|1> and all other apparatus registers blank while preserving old/reference coherence. Then derive temporal separation and finite-end transfer for that combined graph. Stationary bounds(4)–(5) are inputs, not a substitute for those steps. It may be preferable to use a sufficiently distant record gate for a finite-window argument, but no buffer length or timeline is assumed sufficient here.

An additional distinction is essential: even a future proof of record|1> in the final finite-window output would NOT remove the supplied observation window. An autonomous completion SIGNAL would require an all-time false-positive/heralded-correctness statement: at arbitrary times, the record1 sector must implement the specified W on arbitrary old/reference input with the required complete remaining outputs, and its success probability must eventually become high. This scattering calculation proves neither that implication nor a bound on early record1 events. The record can rotate while the head still occupies a terminal or an arm, so record1 by itself does not currently certify that the head has reached the output or that the other apparatus is blank. Equations(4)–(5) support only a prospective asymptotic/finite-window flag construction. They do not provide all-time certification, a heralded map guarantee, or freedom to read at an arbitrary unknown completion time. Such a theorem is a separate obligation and is not forced by labeling the qubit a record.

Once the head has left the terminal-contact region, that contact no longer drives the record in the one-head sector, and the ideal free record has no autonomous relaxation term. This explains finite-window storage compatibility; it is not permanent stability for the coupled finite device. A returning head can traverse the gate again and toggle X back. Finite-end recurrences and residual incoming/reflected amplitudes must therefore remain in the complete error budget, not be called a halt. No irreversible latch, dissipation, environmental reset or measurement is supplied.

The bit is a supplied qubit observable in a mathematically specified apparatus. Identifying it with the framework's native Record, deriving its |0> initialization, assigning units, manufacturing correlated coefficients or implementing readout are still open physical interfaces. The construction shows a concrete ordinary local-positive two-body candidate for coherent record writing, with a precise repair to the odd-length idea; it does not close those interfaces or prove a universal negative result about alternatives.
