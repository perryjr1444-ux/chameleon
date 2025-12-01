This file contains the recommended content for your Hacker News post.

**Submission URL:** [https://news.ycombinator.com/submit](https://news.ycombinator.com/submit)

Select the "Show HN" option when you post.

---

### Recommended Title

**Show HN: I made a tool that hides secrets in plain text with invisible characters**

*Alternative title:*
**Show HN: Chameleon – A steganography tool to turn data exfiltration into detection**

---

### Recommended Text Body (URL is the GitHub repo)

Hi HN,

I've been working on a concept for a defensive framework called "Chameleon". The idea is to go beyond passive monitoring and embed active defenses (like canary tokens) directly into the data an attacker might steal.

The full vision is a multi-layered steganography system with rotating keys. The goal is to turn an attacker's own data exfiltration activities into a detection mechanism. When they steal a file and use an invisible canary credential hidden within it, they trip an alarm.

To get this idea out there, I've written up the [architectural spec](https://github.com/perryjr1444-ux/chameleon/blob/main/docs/architecture.md) and built a functional Proof-of-Concept for what I think is the coolest encoding channel: Zero-Width Characters.

The PoC is a simple Python script that can hide any string inside a normal-looking text file by injecting invisible Unicode characters between the letters. You can copy the output, paste it somewhere else (like a chat app or social media), and the secret message is still there, ready to be decoded.

I think it's a powerful demonstration of how much data can hide in plain sight.

The project is open source and I'm keen to hear your feedback on the concept and the PoC. What are some ways this could be used or abused?

Thanks for checking it out!
