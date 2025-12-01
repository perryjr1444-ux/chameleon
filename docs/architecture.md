# Chameleon: Architectural Specification

This document outlines the conceptual architecture for Chameleon, a defensive steganography framework.

## Core Principles

Chameleon is designed to provide a multi-layered, resilient method for embedding self-updating defensive payloads and "canary" tokens within seemingly innocuous data streams (e.g., text, images). The framework prioritizes stealth, redundancy, and active defense.

## System Components (Theoretical)

### 1. Multi-Channel Steganographic Encoder

The core of Chameleon is its ability to encode data across multiple steganographic channels simultaneously. This provides redundancy; if one channel is detected or corrupted, the payload can still be recovered from others.

-   **Zero-Width Character Encoding:** Uses invisible Unicode characters (`U+200B`, `U+200C`, etc.) to hide binary data between legitimate characters. Offers high density.
-   **Whitespace Pattern Encoding:** Encodes data in patterns of spaces and tabs at the end of lines. Low density, but extremely difficult to detect.
-   **Homoglyph Substitution:** Replaces common characters with visually identical Unicode characters (e.g., Latin 'a' with Cyrillic 'а'). The substitution map itself can be used to encode data.
-   **Unicode Normalization Exploitation:** Leverages differences in Unicode string normalization forms (NFC vs. NFD) to hide information.
-   **Semantic Encoding:** Modifies the structure or wording of text in a way that encodes data while preserving the original meaning (e.g., swapping synonyms based on a keyed dictionary).

### 2. Dynamic Key Rotation System

To prevent offline analysis and cracking, all embedded payloads are encrypted with ephemeral keys. The key generation process is designed to be dynamic and context-dependent, making it computationally infeasible to derive keys without the original context.

-   **Time-based Entropy:** The current time (divided into epochs) is used as a primary seed.
-   **Session-based Entropy:** A unique session or transaction ID is factored in.
-   **Content-based Entropy:** A hash of the cover medium (the text or file hiding the data) is used. This ties the encrypted payload to a specific piece of content.
-   **Deployment Context Entropy:** An identifier for the specific deployment or agent is included.

Keys are derived using a Key Derivation Function (KDF) like HKDF with the combined entropy sources.

### 3. Defensive Canary Injection

The framework can inject "canary" tokens alongside the primary payload. These are fake credentials, API keys, or URLs that, if accessed, trigger an alert. This turns the steganographic system into an exfiltration detection mechanism. If an attacker extracts and uses a canary, their presence is revealed.

### 4. Exfiltration Detection

Monitors network traffic and logs for the access attempts on canary tokens. The system can be configured to alert a central security dashboard or take automated actions.

### 5. Self-Updating Payload Mechanism

The embedded payload can contain instructions for the host system to fetch an updated version of itself. This allows defensive tools and canaries to be rotated or updated remotely, even in compromised environments, using the steganographic channel as a covert command-and-control (C2) link.
