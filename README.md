<div align="center">

# 🔓 Reverse Engineering Lab

**My reverse engineering writeups: crackmes, CTF challenges and binary analysis**

![Ghidra](https://img.shields.io/badge/Ghidra-reverse%20engineering-red?style=flat-square)
![Python](https://img.shields.io/badge/Python-solutions-3776AB?style=flat-square&logo=python&logoColor=white)
![Writeups](https://img.shields.io/badge/writeups-step%20by%20step-2ea44f?style=flat-square)

</div>

---

## 🧩 Solved Challenges

| # | Challenge | Source | Difficulty | Platform | Language | Goal | Solution |
|:-:|-----------|--------|:----------:|----------|----------|------|----------|
| 1 | [easy_keygenme](https://crackmes.one/crackme/5c1cc7d533c5d41e58e005ee) by bahha | crackmes.one | 🟢 2.0 / 6 | Unix/linux etc. | C/C++ | Keygen | [📄 Writeup](bahha-s-easy-keygenme/README.md) · [🔑 Keygen](bahha-s-easy-keygenme/keygen.py) |
| 2 | [EasyCrack - Much0l0k0](https://crackmes.one/crackme/5cc1117833c5d4419da558dc) by paypain | crackmes.one | 🟢 2.0 / 6 | Unix/linux etc. | C/C++ | Keygen | [📄 Writeup](paypain-s-easycrack-much0l0k0\README.md) · [🔑 Keygen](paypain-s-easycrack-much0l0k0\keygen.py) |
> Difficulty is the rating given by each challenge's source.

---

## 🛠️ How I Approach a Binary

1. **Recon:** run it and see what input it expects and what it prints
2. **Static analysis:** load it in a disassembler/decompiler (Ghidra), find the entry point and follow the strings
3. **Clean up:** rename variables and functions until the decompiled code reads like source
4. **Rebuild the logic:** work out exactly what the program does with the input
5. **Solve:** write a keygen, patch, or script, find the flag or password, and test it against the original binary

---

## 📁 Structure

Every challenge gets its own folder:

```
reverse-engineering-lab/
└── <challenge-name>/
    ├── README.md     # the writeup
    ├── img/          # screenshots from the tools and the terminal
    ├── <solution>    # keygen, patcher or solve script
    └── <binary>      # the original challenge
```

---

## ⚠️ Disclaimer

Everything here is for learning. The binaries are public challenges written to be reversed (crackmes, CTF tasks and similar). Even so, it's good practice to run unknown binaries inside a VM.
