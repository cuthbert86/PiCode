# Security Policy

## Overview

This repository contains MicroPython / CircuitPython code designed primarily for microcontrollers such as the Raspberry Pi Pico and similar embedded devices.

As this project is intended for educational, experimental, and embedded development purposes, the security model differs from that of web applications or cloud-hosted systems. However, responsible disclosure of vulnerabilities is still important.

---

## Supported Versions

Security updates are applied to the latest version of the main branch.

| Version | Supported |
|---------|-----------|
| Latest (main branch) | ✅ |
| Older releases | ❌ |

Users are encouraged to run the most recent version of the code.

---

## Scope of Security Concerns

Relevant security concerns may include:

- Hardcoded credentials or secrets
- Unsafe handling of Wi-Fi or network connections
- Insecure data transmission
- Buffer overflows or unsafe memory usage
- Exposed debugging interfaces in production deployments
- Unsafe firmware configuration guidance

Physical access vulnerabilities (e.g., direct USB flashing or hardware probing) are generally considered out of scope unless caused by insecure configuration within this repository.

---

## Reporting a Vulnerability

If you discover a potential security issue, please report it responsibly.

**Please do not disclose security vulnerabilities via public GitHub issues.**

Instead, contact:

📧 [your-email@example.com]

Please include:

- A clear description of the issue
- Steps to reproduce (if applicable)
- Affected files or components
- Potential impact

You can expect:

- Acknowledgement within a reasonable timeframe
- Investigation of the issue
- A fix or mitigation where appropriate

---

## Secure Usage Guidelines

When using code from this repository:

- Do not commit Wi-Fi passwords or API keys to version control
- Store secrets in a separate configuration file excluded via `.gitignore`
- Avoid exposing devices directly to the public internet without proper safeguards
- Use secure network protocols where possible
- Regularly update MicroPython / CircuitPython firmware

---

## Disclaimer

This project is provided for educational and development purposes and is supplied "as is", without warranty of any kind.

Users are responsible for evaluating the security suitability of this code for their own deployments, particularly in network-connected or production environments.

---

Thank you for helping improve the security and reliability of this project.
