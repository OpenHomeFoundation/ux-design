"""Merge a JSON patch into design-kit/state.json.

Usage: python3 patch_state.py <state.json> <patch.json>
Objects merge recursively, lists append new items, other values replace.
"""
import json, sys

state_path, patch_path = sys.argv[1], sys.argv[2]
d = json.load(open(state_path))


def deep(a, b):
    for k, v in b.items():
        if isinstance(v, dict) and isinstance(a.get(k), dict):
            deep(a[k], v)
        elif isinstance(v, list) and isinstance(a.get(k), list):
            a[k] += [x for x in v if x not in a[k]]
        else:
            a[k] = v


deep(d, json.load(open(patch_path)))
json.dump(d, open(state_path, 'w'), indent=1)
print('state ok; last steps:', d['completedSteps'][-3:])
