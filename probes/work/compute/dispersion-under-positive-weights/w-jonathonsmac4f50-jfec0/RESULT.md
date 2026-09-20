dispersion-under-positive-weights, independent run 1 of 2
worker w-jonathonsmac4f50-jfec0 (claude-opus-5), unit C-dispersion-under-positive-weights-a1

PROVENANCE: I attempted the related derivation unit J:derive:waves-need-signed-weights:a2 earlier in this campaign, so this run is
not blind to that result. The supervisor should weigh it against the other independent run of this computation.

MODEL
  theta_{t+1} = sum_{j>=0} sum_p w_{j,p} theta_{t-j}(x + p) + noise,   w >= 0,  sum w = 1.
  Along a direction u, write X for the offset projected on u under the level-0 weights and Y under the level-1 weights:
  phi(k) = E[e^{ikX}], psi(k) = E[e^{ikY}], with means mu_1, mu_2, second moments q_1, q_2 and variances v_i = q_i - mu_i^2.

(1) ONE LEVEL (exact)
  |phi| <= 1 by the triangle inequality, and |phi(k)|^2 = 1 - k^2 Var(X) + O(k^4), so
      |phi(k)| = 1 - (1/2) Var(X) k^2 + O(k^4).
  The decay is quadratic, and vanishes only when Var(X) = 0, i.e. all the weight on one offset (a rigid translation).

(2) TWO LEVELS (exact): lambda^2 - a phi lambda - (1-a) psi = 0
  The root near 1 is  lambda = 1 + i k alpha + O(k^2)  with
      alpha = (a mu_1 + (1-a) mu_2)/(2 - a)         (real: a drift, arg lambda = alpha k)
  and
      |lambda(k)|^2 = 1 - 2 D k^2 + O(k^3),
      D = [ a v_1 + (1-a) v_2 + B ] / (2(2-a)),    B = a(1-a)(2 mu_1 - mu_2)^2/(2-a)^2 >= 0.

  Table (direction (1,0,0); D from the formula, |lambda| and arg from the roots of the quadratic):
   a     level 0              level 1                 alpha     D        |lambda| at k=0.05, 0.1, 0.2
   0.25  site+6 (light-cone)  backward {0,e1,e2,e3}  +0.1071   0.0617   0.999846, 0.999383, 0.997537
   0.25  6 neighbours         8 cube corners         +0.0000   0.2381   0.999405, 0.997618, 0.990465
   0.25  single site {0}      single shift {e1}      +0.4286   0.0175   0.999956, 0.999825, 0.999301
   0.5   site+6               site+6                 +0.0000   0.0952   0.999762, 0.999048, 0.996201
   0.5   site+6               backward               +0.0833   0.0812   0.999797, 0.999189, 0.996761
   0.5   6 neighbours         8 cube corners         +0.0000   0.2222   0.999444, 0.997778, 0.991108
   0.5   backward             backward               +0.1667   0.0648   0.999838, 0.999352, 0.997411
   0.5   single site {0}      single site {0}        +0.0000   0.0000   1.000000, 1.000000, 1.000000
   0.5   single site {0}      single shift {e1}      +0.3333   0.0370   0.999907, 0.999630, 0.998519
   0.5   single shift {e1}    single shift {e1}      +0.6667   0.0370   0.999907, 0.999630, 0.998519
   0.75  site+6               backward               +0.0500   0.1075   0.999731, 0.998926, 0.995715
   0.75  6 neighbours         8 cube corners         +0.0000   0.2000   0.999500, 0.998000, 0.992007
   0.75  single site {0}      single shift {e1}      +0.2000   0.0480   0.999880, 0.999520, 0.998080
  In every row arg lambda = alpha k to the printed digits, and |lambda| = 1 - D k^2 with the D of the formula.

(3) THE OBSTRUCTION (exact)
  B >= 0 on 0 <= a <= 1, so D >= [a v_1 + (1-a) v_2]/(2(2-a)) >= 0, and
      D = 0  iff  v_1 = v_2 = 0  and  a(1-a)(2 mu_1 - mu_2)^2 = 0.
  That is: each level on a single offset with p_2 = 2 p_1, or a single level (a = 0 or 1). Both are rigid translations:
  with phi = e^{ikp} and psi = e^{2ikp} the quadratic is solved exactly by lambda = e^{ikp}, so |lambda| = 1 and
  arg lambda = pk - a shift of the whole field by p per level, carrying no dispersion and no wave.
  Every other positive-weight law has D > 0, so |lambda| = 1 - D k^2 and never 1 - O(k^4).
  Degeneracy is a property of the direction: a law whose offsets share one coordinate is a rigid translation along that
  direction and dispersive across it.

  Random check: 200 positive multi-level laws (up to four levels of memory, up to five offsets, weights uniform on [0,1]
  normalised): 186 draws are non-degenerate along (1,0,0); the smallest estimated D is 0.011 and the median 0.23.

READING
  The expectation holds: positivity forces diffusion. A propagating mode needs |lambda| = 1 with arg lambda linear in k over a
  range of k; with non-negative weights the only laws that hold |lambda| = 1 are the rigid translations, whose "phase velocity"
  is the fixed shift per level and which carry no signal beyond moving the whole field. Waves need signed weights.
  No HIT.
