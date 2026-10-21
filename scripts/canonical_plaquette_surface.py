#!/usr/bin/env python3
"""
Canonical plaquette-derived quantities on the bounded SU(3) beta=6 surface.

Authority:
  docs/PLAQUETTE_SELF_CONSISTENCY_NOTE.md

These constants use the declared pure-gauge beta=6 plaquette comparison/reuse
input 0.5934. This module does not derive or certify that input. See the current
boundary-input and reproduction scopes in docs/ALPHA_S_DERIVED_NOTE.md and
docs/PLAQUETTE_SELF_CONSISTENCY_NOTE.md.
"""

from __future__ import annotations

import math

CANONICAL_PLAQUETTE = 0.5934
CANONICAL_ALPHA_BARE = 1.0 / (4.0 * math.pi)
CANONICAL_U0 = CANONICAL_PLAQUETTE ** 0.25
CANONICAL_ALPHA_LM = CANONICAL_ALPHA_BARE / CANONICAL_U0
CANONICAL_ALPHA_S_V = CANONICAL_ALPHA_BARE / (CANONICAL_U0 ** 2)
