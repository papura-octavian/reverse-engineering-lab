<div align="center">

# 🔓 Reverse Engineering Lab

**My writeups and keygens for crackmes from [crackmes.one](https://crackmes.one)**

![Ghidra](https://img.shields.io/badge/Ghidra-reverse%20engineering-red?style=flat-square)
![Python](https://img.shields.io/badge/Python-keygens-3776AB?style=flat-square&logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/platform-Linux%20x86--64-FCC624?style=flat-square&logo=linux&logoColor=black)

</div>

---

## 🧩 Solved Crackmes

| # | Crackme | Author | Difficulty | Platform | Language | Goal | Solution |
|:-:|---------|--------|:----------:|----------|----------|------|----------|
| 1 | [easy_keygenme](https://crackmes.one/crackme/5c1cc7d533c5d41e58e005ee) | bahha | 🟢 2.0 | Linux x86-64 | C++ | Keygen | [📄 Writeup](bahha-s-easy-keygenme/README.md) · [🔑 Keygen](bahha-s-easy-keygenme/keygen.py) |

> Difficulty is the community rating from crackmes.one, on a scale from 1.0 to 6.0.

---

## 🛠️ How I Solve Them

1. **Recon:** run the binary and see what input it asks for and what it prints
2. **Static analysis:** open it in Ghidra, find `main`, and follow the strings
3. **Clean up:** rename variables and functions until the decompiled code reads like source
4. **Rebuild the logic:** work out exactly how the input is checked
5. **Solve:** write a keygen (or find the password) and test it against the original binary

---

## 📁 Structure

Every crackme gets its own folder:

```
reverse-engineering-lab/
└── <crackme-name>/
    ├── README.md     # the writeup
    ├── img/          # screenshots from Ghidra and the terminal
    ├── keygen.py     # the solution (if it's a keygenme)
    └── <binary>      # the original crackme
```

---

## ⚠️ Disclaimer

Every binary here is a crackme: a challenge written to be reversed and published on crackmes.one for practice. Even so, it's good practice to run unknown binaries inside a VM.
