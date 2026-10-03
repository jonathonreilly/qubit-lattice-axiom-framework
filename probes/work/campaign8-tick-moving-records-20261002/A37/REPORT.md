*(Saved by the coordinator from the agent's final message; the agent did not write REPORT.md.)*

# A37 report: records that push the shared possibilities along ("flow") instead of trading places with them ("swap")

All models are supplied toys inside the record-tick shape (A27's Option R: compressed smooth change between ticks, linear step odds, the claim rule CL). Every step rule below is a named conditional, not framework content. The owner's ideas are instincts, not positions.

## 1. Question

Under SW, a record stepping x → y = x+e sends y's possibilities back to x. Can it instead push them onward or around, as in "neighbourhoods can shift" and "the probabilities can all push right"?

For three push families I check:
- one record step per tick, and how far the possibilities are displaced;
- covariance under the 24 soldered turns (Q3);
- linearity and no-signalling;
- admissibility (C40);
- conservation of possibility content and of energy (C60).

I also ask:
- Is push observably different from swap, in 1D and in 2D/3D?
- Does it give a wake, drag or inertia, or a trace that later records show?
- Is a record-driven conveyor compatible with Theorem N and A1 D12, and what does it do to the cones?
- How are clashes settled, with "one wins with its relative probability"?

## 2. Answer

**Short version: conditional yes on the full grid, conditional no on a single line, and no difference at all over calm empty space.**

- **Forced return flow (EXACT).** With one site's worth of possibilities per site, a record step x → y moves net exactly one site's worth of possibilities from y's side to x's side, through every surface separating them, and nothing anywhere else.
  - Classically this is a counting identity. In the quantum case it is the Choi-state information flux, which equals exactly one qubit for *any* unitary step.
  - No rule changes this balance. Push versus swap only decides which content lands in which spot.
- **1D (EXACT).** Suppose nothing is created or destroyed and every piece of content moves at most one site. Then the step is the swap (plus unrelated adjacent swaps), or the whole line shifts with the record, which is a pure relabeling and impossible if any other record is on the line.
  - So "flow = swap" holds exactly under conservation, nearest-neighbour reach and finite reach.
  - The owner's push-right exists only by relaxing one of these:
    - the half-line conveyor: everything ahead shifts and a fresh calm spot appears behind. It is lossless only on an endless empty line, and it changes possibilities arbitrarily far away within one tick (CHECKED: TV 0.245 at 30 sites);
    - a capped push with a long return jump (reach L+1);
    - push-and-absorb or fill-behind rules, which destroy one site's worth per step.
- **2D/3D (EXACT + CHECKED).** Possibilities can flow around the record. The minimal rule rotates a square: the front content moves to the side, the side content moves back, and the back-side content fills the vacated spot.
  - It is conservative, linear and complete, moves the record one site per tick, and reaches at most 2 sites.
  - In 3D a deterministic covariant rule must send the front content along the step axis, which means swap or an infinite line conveyor (EXACT). So the side must be picked at random.
  - The random pick blurs structured neighbourhoods: purity given the step is 0.50 in 2D (CHECKED).
- **Where it makes a difference.**
  - Over calm product backgrounds all rules give identical snapshots, energies (C60 unchanged) and record statistics (EXACT).
  - With neighbour-blind odds, the records' own motion is identical under every rule (EXACT and CHECKED): no drag, no inertia.
  - Differences appear only through structured possibilities: where linked content ends up (later records show it), whether content can ever cross a record (never, under 1D push rules), and wakes.
  - With neighbour-sensitive odds the motion differs. Stepping onto an excitation leaves it behind under swap and in front under push. So when the odds favour stepping onto excitations, swap gives reversal and push gives persistence: p_same 0.26–0.29 against 0.69–0.71 (CHECKED).
  - In a classical gas analog, push with those odds makes the record self-propelled at 0.154 sites per tick, ahead of a growing pile averaging 37 sites. Push with odds that disfavour excitations cages it.
  - This is a memory left in the pushed content, not inertia (ARGUED).
- **Costs.**
  - The admissibility gap is the same as for swap (C40). Under the strict reading (β = 0), every rule becomes a re-formation at y and swap equals fill-behind exactly. Lone −n records in calm space then never move (C67b).
  - Refills must be calm, which needs the calm axis (C30). Otherwise each step costs O(J).
  - Overlapping pushes need one joint instrument per conflict cluster. Relative odds combined across sites signal (TV 3.5e-3, CHECKED).
- **Theorem N and A1 (EXACT).** A record-driven push is compatible with both. It is part of the irreversible record event, and its direction comes from the record's random step. Finite pushes carry no standing flux, only the unit return. Only the infinite conveyor carries a standing flux, and it breaks every cone.

## 3. Derivation

**Setup (SUPPLIED).**
- Snapshot: records (site, pure content |r⟩) and shared possibilities ρ on unrecorded sites.
- A step x → y has odds (c/z)·tr(W_y ρ), with W = β + (α−β)|r⟩⟨r| (content weight) or W = 1 (blind), followed by a post-step map M_{x→y} on the possibilities. The record content moves to y.
- A rule is conservative if M is a bijection of site contents, or a unitary V: H_{W∖x} → H_{W∖y} on a window W.
- A refill ω is the fresh state a rule may put at x.
- The rules studied:

| Name | What happens at a step x → y |
|---|---|
| SW, swap | y's content goes to x |
| PS, flow around | y → y+f → x+f → x, with f ⊥ e |
| PL_L, capped line push | y → y+e → … → y+Le, and y+Le's content jumps to x |
| PA, push to the first calm spot | the train at y shifts to the first calm site; x calm |
| P∞, conveyor | everything on the ray ahead shifts by e; x refilled |
| PF, fill behind | y's content erased; x quiet; the smooth change refills it |

**Step 1. Return flow (EXACT; CHECKED t1).**
- *Classical.* For every finite region S: (possibility items in S after) − (before) = [x∈S] − [y∈S], since the domains are Z^d∖{x} and Z^d∖{y}. In 1D this means flux −1 across the crossed bond and 0 elsewhere.
- *Quantum.* Take any unitary V and any split W = W₁⊔W₂ with x∈W₁ and y∈W₂, and form the Choi state with references R_i.
  - V maps the maximally mixed input to the maximally mixed output, and the Choi state is pure, so S(K₁R₂) = S(K₂R₁).
  - Therefore ½[I(K₁:R₂) − I(K₂:R₁)] = ½·log₂[(dim K₁/dim H₁)(dim H₂/dim K₂)] = 1 qubit, from y's side to x's side.
  - The flux is 0 for splits that do not separate x from y.
  - This is kinematic: it holds for every rule.
- *Corollary.* The displacements of possibility content always sum to exactly −e per conservative step with finite support.

**Step 2. 1D classification (EXACT; CHECKED t1a).**
- With |f(z)−z| ≤ 1, the item filling x comes from y or from x−1.
  - If from y: both half-lines must map into themselves, which forces adjacent transpositions. This is the swap.
  - If from x−1: the shift propagates both ways, giving the global shift. Any other record on the line, or finite support, excludes this case.
- With a fresh spot at x and no erasure, the right half-line must shift to infinity: the half-line conveyor P∞.
- With an erasure at site s ≥ y, the content y..s−1 shifts by one and s's content is erased: PA-type or PF.
- This is the record-step analog of A3's Lemma L1 (pair mixing or shift). It corrects the earlier "in 1D, flow = swap" as follows: it holds only under conservation, nearest-neighbour reach and finite reach.

**Step 3. 2D/3D: loops (EXACT, via A1 D7; CHECKED t1b).**
- The full-content bijection (record included) decomposes into closed even lattice loops.
- The record's loop through the directed bond (x,y) has length 2 (swap) or ≥ 4 (flow around). Lengths 2–20 occur in the enumerated windows.

**Step 4. Covariance (EXACT; CHECKED t1c, t4).**
- In 3D the quarter turn g about the step axis fixes x and y. Covariance of a deterministic rule gives F(y) = gF(y), so F(y) lies on the axis.
- With nearest-neighbour reach that means x (swap) or y+e, and y+e forces y+2e, and so on: the infinite conveyor.
- So deterministic covariant flow-around is impossible in 3D. The uniform mixture over the 4 sides is covariant (CHECKED: error 1.2e-17; a single fixed side gives deviation 0.018).
- In 2D no proper turn fixes the bond, so a handed deterministic choice ("always turn left") is covariant. This matches A11's 2D-only circulation.
- Refill (EXACT, Schur on the stabilizer of r): an unglued refill must be ω(r) = p|r⟩⟨r| + (1−p)|r⊥⟩⟨r⊥| with p a law constant.
  - A calm refill needs p ∈ {0,1} and every record content equal to ±n with one sign (C30's condition), or else a law-level axis.
  - Refills tied to the grid (for example pointing along e) are covariant but glued.
- All rules are unglued with W built from r or W = 1 (CHECKED for PS: turning space alone 0, turning possibilities alone 8e-15).

**Step 5. The rules against the criteria (EXACT by construction unless noted).**

| Rule | Record per tick | Reach of the possibilities' displacement | Covariant / glued | Linear, no-signalling | Content | Energy on calm snapshots (calm refill) |
|---|---|---|---|---|---|---|
| SW | 1 | 1 | yes / unglued | yes, support {x,y} | conserved | C60 |
| PS (2D/3D) | 1 | 1 per item, footprint 2 | 3D: only as a mixture / unglued | yes, support ≤ 2 | conserved per branch; the mixture blurs | C60 |
| PL_L | 1 | L+1 (the return jump) | yes / unglued | yes, support L+1 | conserved | C60 |
| PA | 1 | train length, unbounded and state-dependent | yes if "calm" is set by r / unglued | linear only as a train-length measurement; unbounded support | conserved, but the train pattern decoheres | C60 |
| P∞ | 1 | infinite | yes / unglued | linear, but infinite support (Step 7) | lossless only on an endless empty ray; with a record ahead it must erase or shove | C60 locally; content and energy pushed to infinity |
| PF | 1 | 1 | yes / unglued | yes, support {x,y} | one site's worth destroyed per step | C60 |

- Admissibility is the same as for SW for every rule (C40, Step 6).
- PA must decohere: the classical push-until-vacancy map is not injective. "Excitation at y, y+1 empty" and "y empty, excitation at y+1" give the same output, so it cannot be an isometry.

**Step 6. Admissibility and the strict reading (EXACT).**
- With β = 0 the step Kraus contains |r⟩⟨r|_y: a Lüders cut of y onto r with odds (c/z)⟨r|ρ_y|r⟩, which is the formation of r at y.
- SW then moves the projected copy |r⟩ to x. So SW(β=0) ≡ PF(β=0, ω=r): the record leaves a copy of its content behind.
- Push rules instead shove the copy forward.
- For −n records in calm space ⟨−n|n⟩ = 0, so no lone step happens under any rule (C67b).
- With β > 0 or blind odds, every rule places r at y regardless of y's menu (C40 unchanged).

**Step 7. Cones and signalling (EXACT; CHECKED t2).**
- Linear local instruments cannot signal outside their support. The step footprint adds to the record cone: radius 1 (SW, PF), 2 (PS), L+1 (PL), unbounded (PA, P∞).
- P∞ check: an excitation 30 sites ahead, one tick, with the step allowed versus impossible. TV of its position law is 0.245 for P∞ and exactly 0 for every other rule.
- P∞ therefore breaks both the strict record cone and Option R's faint-leak cone for possibilities.

**Step 8. Energy (EXACT on calm snapshots; CHECKED near excitations).**
- On calm snapshots with a calm refill the post-step snapshot is identical for all rules, so C60 applies verbatim: 0 for a lone record or for +n contents, 2J per contact gained or lost for −n contents.
- An equal-odds refill (½) in 3D changes ⟨H⟩ by −J(5 + n_r·n) per step: −6J or −4J. With J ~ E_P that is a grid-scale ghost source.
- Single-excitation 1D toy, ΔE of one step (units of J):

| Excitation position | SW | PL1 | PL2 | P∞ | PA | PF |
|---|---|---|---|---|---|---|
| +2 (ahead) | +4 | +4 | 0 | 0 | +4 | +4 |
| −1 (behind, adjacent) | −4 | −4 | −4 | −4 | −4 | −4 |

  - No rule tested conserves ⟨H⟩ near excitations.

**Step 9. Observable differences (EXACT, then CHECKED).**
- Calm product background: none. An i.i.d. product background σ^⊗: none for permutation rules (SW, PL, PS); a trail of ω for refill rules.
- Neighbour-blind odds: the record law (with CL) never involves the possibilities, so it is identical across rules. This holds provided blocked loops fall back to swap (a named choice). CHECKED: identical step sequences in t2 and t5.
- Linked content (t3, t4): with y Bell-linked to a distant b, the site where later records match b's records afterwards is:

| Rule | Site holding the link | Z-agreement / X-agreement / mutual information |
|---|---|---|
| SW | x | 1 / 1 / 2 bits |
| PL, conveyor | y+1 | 1 / 1 / 2 bits |
| PA | y+1, classical part only | 1 / 0.5 / 1 bit |
| PF | nowhere | — |
| 2D PS | y±f, each | 0.75 / 0.75 / 0.587 bits |

- Crossing in 1D (EXACT; CHECKED): under P∞, PA and PF, content never crosses a record, because the change cannot cross one and these steps never move content across it. Records become perfect barriers. Under swap one site's worth crosses per step.

**Step 10. Momentum, drag, inertia.**
- *Net recoil.* The net content displacement is −e per conservative step for every rule (EXACT). Push redistributes the recoil; it does not add any.
- *Carrying (t2, blind odds).* Slope of the excitation's displacement against the record's: SW −0.33, PL2 −0.16, P∞ +0.61, PA +0.29. Push carries content along; swap passes through it.
- *One-step rule (EXACT for a frozen background).* After stepping onto an excitation, the excitation sits at x (swap), at y+e (line push) or at y+f (around). With odds that favour excitations the next step goes back, onward or sideways respectively. The flow-around "turning" case is ARGUED only (not simulated).
- *Quantum 1D toy (CHECKED).*
  - Exact two-step p_same, odds favouring excitations: SW 0.287 / 0.256; push rules 0.685–0.713; PF 0.500.
  - Monte Carlo lag-1 step correlation: SW −0.21 (MSD 10.6) against push +0.17 to +0.21 (MSD 34–45).
  - Odds disfavouring excitations give weak, mixed effects.
- *Classical gas analog (t5, SUPPLIED decohered possibilities).*
  - PA with odds favouring excitations: MSD 54,632 against 224 for SW, speed 0.154 sites per tick, pile ahead averaging 37.5 sites (max 79). Self-propelled.
  - PA with odds disfavouring excitations: MSD 67 against 721 for blind odds. Caged between the piles it builds: drag.
  - Blind PA: wake density about 0.11 behind and a bow of 0.25–0.49 ahead, against a 0.3 background.
- *Inertia (ARGUED).* This is not inertia. There is no velocity variable; the memory sits in the pushed content, needs neighbour-sensitive odds, and fades as that content spreads in the quantum toy. A19's verdict on registered movers is untouched.

**Step 11. The owner's 1D challenge, Theorem N and A1 (EXACT).**
- "All push right" is P∞, or a relabeling.
- Theorem N needs a reversible covariant nearest-neighbour tick. A push is part of the irreversible record instrument (the same exit as SW, A29 C27). It moves nothing in voids.
- A1 D12 kills the standing flux of a covariant law. Here the instrument is covariant, and each outcome's direction comes from the record's random step. The mean flux is 0 for isotropic odds.
- Finite conservative pushes carry no standing flux, only the −1 at the crossed bond. Only P∞ carries +1 across every cut ahead.
- Record-driven conveyors supply no law-level chirality index (ARGUED).

**Step 12. Clashes (EXACT construction; CHECKED t3).**
- Same target: CL's single-site claim gives exact relative odds (A27).
- Push footprints can overlap even when targets differ. The linear options are:
  - an odds-blind priority (no signal, but not relative odds);
  - one joint instrument on the conflict cluster, with E_A = (c/z)W_A(y_A) and E_B = (c/z)W_B(y_B). It is exclusive and gives P(A | someone goes) = w_A/(w_A+w_B) exactly (0.623150 against 0.623150), with TV ≤ 1.5e-16.
- Combining separately computed odds is quadratic and signals: TV 3.53e-3.
- Clusters can chain, so the joint instrument is unbounded in principle and needs Σ_i E_i ≤ 1, which forces small c (ARGUED).
- P∞ makes every pair of records on a line conflict.
- In 1D, head-on conservative nearest-neighbour steps must both be swaps (Step 2).

## 4. Checks

Every run used `nice -n 10`, all four thread caps at 1 and a 55 s alarm (`run.sh`, `run1.sh`). The 1-minute load was 1.7–3.4 at each start.

| Script → output | What it checks | Result | Time, peak memory |
|---|---|---|---|
| `t1_return_flow.py` | Exhaustive enumeration in 1D, 2D (up to 4×5, 85,861 maps) and a 3D 12-site window; Choi flux | Step 1–4 numbers; 0 flux and displacement failures; 2 of 2 equivariant 3D maps are swaps; quantum flux 1.000000 qubit (random unitary: 2.135 − 0.135) | 3.0 s, 97 MB |
| `t2_chain_1d.py energy-cone` | ΔE per step; P∞ cone | Step 7–8 | 0.4 s, 58 MB |
| `t2_chain_1d.py exact {blind, attract, repel}` | Exact two-step laws by density-matrix branches | Undecided weight ≤ 1e-7; total 1.000000 | ≤ 1.9 s, ≤ 62 MB |
| `t2_chain_1d.py mc {…}` | 1500 trajectories × 100 ticks | Step 9–10; lag-1 statistical error about ±0.007; edge leak ≤ 3e-4 | ≤ 1.6 s, ≤ 124 MB |
| `t2b_pf_check.py pfcheck` | Random starts, different J, τ, c | PF's 0.500000 is special to localized starts (correlations ±0.004 to ±0.062 otherwise) | 1.9 s, 59 MB |
| `t3_clash_trace.py` | Clash rules; link location | Step 9 and 12 numbers; completeness 4.4e-16 | 0.1 s, 28 MB |
| `t4_plaquette.py` | PS on a 3×3 patch, 7-qubit link test, 3D template | Completeness 3.6e-15; covariance 3.1e-15; purity 0.5036 (min 0.5001); link and 3D numbers as above | 3.6 s, 196 MB |
| `t5_snowplough.py {blind, attract, repel}` | Classical gas analog (L=200, 300 runs, 1500 ticks) | Step 10 numbers | about 3 s, 35 MB |

**Budget breach.** The first two `t4` versions peaked at 570 MB and 315 MB, over the 300 MB cap; each finished in under 6 s. I then restructured the script (vector-based 3D check, 7-qubit link test), and the final run used 196 MB.

**Not run.** A 3D quantum or classical toy of PS with neighbour-sensitive odds ("turning"), and a 3D snowplough.

## 5. Real-physics match (comparators, not adopted)

- **Incompressible flow.** The return flow is the lattice version of the backflow a body forces in an incompressible fluid (Darwin drift, 1953). Swap is direct exchange and PS is the Zener ring mechanism of diffusion in solids.
- **Infinite push.** P∞ is a "Hilbert hotel" (unilateral shift) move. The GNVW index forbids it for automorphisms; it exists only as an endomorphism with a source. Its instant influence at any distance is ruled out by relativity and no-signalling. That is a falsifier of P∞ if records or possibilities carry light-cone physics.
- **Environment-memory walks.** The push persistence resembles PushASEP (Borodin–Ferrari 2008), the biased tracer in a 1D lattice gas (Burlatsky et al. 1996), the true self-avoiding walk (Amit–Parisi–Peliti 1983) and excited random walks (Benjamini–Wilson 2003). Ideal-fluid "added mass" is the known flow-made inertia; it has no analog here because the steps are stochastic.
- **What is consistent with observation.** A body moving through calm vacuum leaves no wake under any rule.
- **What would discriminate or falsify.**
  - Decoherence of structured surroundings at every step under PS (purity about 1/2 per step in 2D, about 1/4 per step in 3D by hand).
  - Records whose odds look at their neighbours: persistent movement under push against bouncing under swap.
  - Grid-scale energy per step from any non-calm refill.

## 6. Open edges

1. A coherent covariant sideways flow (beyond permutations or random mixtures) in 3D.
2. 3D toys: PS turning statistics, and whether push self-propulsion survives the change and 3D relaxation.
3. A proof, independent of GNVW, that 1D quantum nearest-neighbour steps are swaps up to local reshuffling.
4. Whether any step rule conserves energy near excitations.
5. A joint per-site instrument combining formation, push footprints and the clash clusters (A27 open edge 1, now larger).
6. Records shoving records: the exclusion needed to keep I2.
7. Owner decisions (none adopted):
   - in 1D, swap against fill-behind or long jumps;
   - in 2D/3D, allow flow-around with a random side;
   - the refill state;
   - joint clash instruments;
   - whether step odds look at the neighbours.

## 7. Plain-language summary

When a record steps into a neighbouring spot, what was there has to go somewhere. If every spot always holds exactly one spot's worth of possibilities and nothing is made or destroyed, then overall exactly one spot's worth must end up back where the record came from, whatever the rule. On a single line the only tidy way to do that is the swap. "Everything pushes right" does exist, but only if the push runs all the way along an endless empty line, which changes things arbitrarily far away at the same moment. The only other options are to wipe out a spot's worth of possibilities each step, or to let something jump back several spots. On the full grid there is a real alternative: the possibilities can flow around the record, from the front to the side, back along the side, and into the spot the record left. It obeys all the rules, but since no side is special it must pick one at random, which slightly blurs linked possibilities. In calm empty space it makes no difference at all. It matters only near busy, linked possibilities: later records show where things went, nothing can slip past a pushing record on a line, and if a record's stepping odds look at its neighbours, pushing makes it keep going (or get hemmed in) where swapping makes it bounce back. That is a memory left in what it pushed, not true momentum; with odds that ignore the neighbours, records move exactly the same way under every rule. When two pushing records get in each other's way, "one wins with its relative probability" still works, but only if the law settles the whole tangle at once.