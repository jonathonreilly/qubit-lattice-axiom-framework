# Artifact Plan

## Source note

Rewrite the K-real note as a no-go / bounded finite-algebra locator:

- preserve the exact two-letter K-even algebra under a supplied readout;
- identify the K-odd phase channel;
- state that the baseline does not derive the instrument or measure selector.

## Runner

Expand the runner from 7 checks to 11 checks:

- retain the existing spectra, commutation, decomposition, entropy, and weight
  checks;
- add K-even/K-odd orthogonality;
- add K-even projection removing the phase channel;
- add text guards for the missing instrument and missing selector statements.

## Cache

Refresh the paired runner cache after the runner changes.
