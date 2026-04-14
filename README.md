# ABORABSHTOOL
The Ultimate OSINT &amp; Reconnaissance Suite. Effortlessly track social media footprints and perform deep server infrastructure analysis with a professional CLI interface.
# 🛡️ ABORABSHTOOL v1.0
> **The Ultimate Hybrid Suite for OSINT & Infrastructure Reconnaissance**

**ABORABSHTOOL** is a high-performance security toolkit engineered for modern digital investigations. It bridges the gap between social media intelligence (OSINT) and network auditing, allowing security researchers and developers to verify digital footprints and analyze server infrastructures within seconds.

---

## 💎 Core Capabilities

### 👤 1. Social Media Intelligence (OSINT)
This module automates the process of tracking a target's presence across the global digital landscape.
- **Dynamic Probing:** Instantly verifies usernames on platforms like **Instagram, TikTok, Twitter, GitHub, and Snapchat**.
- **Efficiency:** Uses advanced HTTP response analysis to detect account existence without triggering security blocks.

### 🌐 2. Advanced Infrastructure Auditing
A deep-dive recon engine designed to extract technical intelligence from any domain.
- **WHOIS Intelligence:** Aggregates domain ownership data, registrar history, and critical lifecycle dates.
- **Nmap-Powered Scanning:** Performs precise port auditing (80, 443, 21, 22, 3306) to identify active services, open gateways, and server-side software versions.

---

## 🎮 Execution Guide (Usage)

Once the tool is deployed, use the following commands in your terminal:

### A. Tracking a Digital Footprint (Username Search)
To find where a user is active on social media:
```bash
python aborabsh.py --user [target_username]
