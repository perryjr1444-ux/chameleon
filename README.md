# Chameleon 🦎

**Hides your secrets in plain sight. A Proof-of-Concept for a defensive steganography framework.**

Chameleon is an exploration into multi-channel, resilient steganography. Instead of just hiding data, the full (theoretical) framework is designed to embed self-updating defensive payloads and canary tokens inside otherwise benign files, turning exfiltration into a detection opportunity.

This repository contains a functional Proof-of-Concept (PoC) for one of the most intriguing encoding channels: **Zero-Width Character Steganography**.

## The Problem

How do you know when an attacker has breached a server and is stealing your data? Often, you don't until it's too late. Defensive files are deleted, and log files are wiped.

## A Glimpse of the Solution

Chameleon's approach is to embed "canary" tokens (like fake AWS keys or URLs) directly and invisibly into the text files an attacker is likely to read (e.g., `.bash_history`, source code, `config.yaml`). When the attacker extracts and uses one of these invisible tokens, they unknowingly trigger an alert.

The full architectural vision includes multiple encoding layers and dynamic, rotating encryption keys to create a resilient, covert C2 and detection channel. You can read the full [architectural specification here](./docs/architecture.md).

---

## Proof-of-Concept: Zero-Width Encoding

The `poc` directory contains a simple, standalone Python script that demonstrates how to hide a secret message inside a standard text file using invisible Unicode characters.

### Quick Start

1.  **Prerequisites:** Python 3

2.  **Encode a secret message:**
    
    Let's hide the secret `"supersecret"` inside the `poc/cover.txt` file.

    ```bash
    # This will print the steganographic text to your terminal.
    # The output will LOOK identical to cover.txt, but the secrets are hidden inside.
    ./poc/chameleon_poc.py encode poc/cover.txt "supersecret" > poc/stego_text.txt
    ```

3.  **Verify the content:**
    
    The file `poc/stego_text.txt` looks normal, right?
    
    ```bash
    $ cat poc/stego_text.txt
    This is a normal text file.
    It has a few lines of content.
    Nothing to see here.
    Move along.
    ```

4.  **Decode the secret:**
    
    Now, let's pull the secret back out from the seemingly normal file.

    ```bash
    $ ./poc/chameleon_poc.py decode poc/stego_text.txt
    supersecret
    ```

### How it Works

The PoC converts your secret message into a binary string. It then maps those bits to invisible "zero-width" Unicode characters (`U+200B`, `U+200C`, etc.) and injects them between the legitimate characters of the cover text. They are invisible to the human eye and in most text editors, but they are still there, carrying your data.

## The Viral Launch

Now, I will provide the materials for the Hacker News post.
