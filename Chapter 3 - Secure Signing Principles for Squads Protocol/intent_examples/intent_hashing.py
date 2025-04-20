## 🔐 `intent_hashing.py` (Canonical Hasher)

import json
import hashlib

def canonical_intent_hash(file_path: str) -> str:
    with open(file_path, 'r') as f:
        data = json.load(f)

    # Remove fields not part of hash logic
    hashable_fields = {k: v for k, v in data.items() if k != "intent_hash"}
    serialized = json.dumps(hashable_fields, sort_keys=True, separators=(',', ':'))
    return hashlib.sha256(serialized.encode()).hexdigest()

# Usage
# print(canonical_intent_hash("transfer_usdc.json"))