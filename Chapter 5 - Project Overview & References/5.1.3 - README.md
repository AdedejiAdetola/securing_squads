# 🔐 Secure Signing on Squads Protocol – Architecture Overview

---

## 🧭 Problem

Multisig is foundational to Web3 treasury security — but even the best systems are vulnerable when **signer intent is unclear**, **UI trust is assumed**, or **threshold logic is misused**.

Recent high-profile exploits (Bybit, Harmony, Safe) prove that:

- Attackers don’t need to steal keys — they can **deceive signers**.
- **Frontends are mutable**, spoofable, and exploitable.
- Many multisig protocols lack true **proof of intent**.
- Plugin architectures introduce **new attack surfaces**.
- Even quorum enforcement often lacks **policy rigor**.

> ✅ **The attacker model has evolved — the signing experience hasn’t.**

---

## 🎯 Our Solution

We’ve designed a **secure, intent-verifiable signing architecture** layered on top of the Squads Protocol — designed for institutions, DAOs, and signers who can’t afford to be wrong.

This system enforces:

### 🔐 Canonical Signing Intents

A structured `txintent.json` that binds human-readable transaction summaries to executable logic.

### 🛠 Zero-Trust CLI Enforcement

No signer can act unless:

- The intent is verified and hashed.
- The frontend/client hash is validated.
- The policy is explicitly passed.

### 🧱 Role + Policy Enforcement

Thresholds alone aren't enough. We enforce:

- Minimum signers
- Manual execution separation
- Signer role validation

### 📎 Frontend Hash + OOB Verification

Supports:

- IPFS/ICP UI verification
- QR hash display
- Multiclient signer review (airgap-friendly)

### 🔍 Threat-Aligned Architecture

Covers spoofing, tampering, plugin injection, buffer abuse, signer drift, and more.

---

## 🔐 Threats & Defenses

| Threat / Exploit                     | Covered ✅ | Defense                                       |
| ------------------------------------ | ---------- | --------------------------------------------- |
| Musked UX / Spoofed Frontend         | ✅         | Canonical `intent_hash` + UI `client_hash`    |
| Proposal Buffer Tampering            | ✅         | Instruction hash in `txintent`                |
| Plugin Execution Hijack              | ✅         | Registry + policy filtering in vault          |
| Ghost Signer Bot                     | ✅         | CLI + Hardware wallet + biometric enforcement |
| Signer Drift / Rotation Abuse        | ✅         | Policy floor on signer config                 |
| Last Signer Exploits (2-Min Rule)    | ✅         | Timelock + manual exec flag                   |
| Cross-Environment Key Confusion      | ✅         | Network binding in `txintent`                 |
| All Signers Deceived via Monoculture | ✅         | Multiclient review model                      |
| Metadata Spoof via API               | ✅         | Local simulation, signed metadata             |

---

## 📁 Project Structure

| Chapter       | Theme                                                  |
| ------------- | ------------------------------------------------------ |
| **Chapter 1** | Squads lifecycle, signer roles, real-world incidents   |
| **Chapter 2** | STRIDE & DREAD threat modeling + novel attack classes  |
| **Chapter 3** | Secure signing principles, intent schema, and examples |
| **Chapter 4** | CLI specification (command flow, validations, logs)    |
| **Chapter 5** | This overview + full manifest and references           |

📂 `intent_examples/` → Real transaction samples for validation  
📂 `utils/` → Hashing logic (reference only)

---

## 📚 References

### 🔬 Multisig Incident Reports

- [OtterSec – Multisig Security in Practice](https://osec.io/blog/2025-02-22-multisig-security)
- [Cubist – Preventing the Bybit Hack](https://cubist.dev/blog/understanding-and-preventing-the-bybit-hack)
- [New York Times – North Korea and the Bybit Hack](https://www.nytimes.com/2025/03/06/technology/bybit-crypto-hack-north-korea.html)
- [Elliptic – Harmony Bridge Attack](https://www.elliptic.co/blog/harmony-horizon-bridge-hack-analysis)
- [BNB Chain – Postmortem on Bridge Exploit](https://www.bnbchain.org/en/blog/bnb-chain-bridge-incident-postmortem)

### 🧠 Architectural Thought Leadership

- [DFINITY – Chain-Served Web3 UX](https://github.com/dfinity/http-proxy)
- [Squads – Advanced Security Best Practices](https://docs.squads.so/main/additional-resources/advanced-security-best-practices)
- [Safe{Wallet} – Community UX Spoofing Discussions](https://community.gnosis-safe.io)

---

## ✅ Outcome

This system:

- ⚙️ Enforces signing integrity from input to signature
- 🔒 Prevents intent mismatch and signer deception
- 💡 Educates and guides multisig operators, not just developers

It is:

- Field-informed ✅
- Architecturally novel ✅
- Implementation-agnostic ✅
- Secure-by-default ✅

---

**Built for the Secure Signing Challenge by design — not by accident.**
