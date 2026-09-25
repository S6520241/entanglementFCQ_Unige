# entanglementFCQ_Unige
# Quantum Entanglement Analysis in 2-Qubit Systems

Progetto sviluppato nell'ambito dell'esame di **Fondamenti di Computazione Quantistica** presso l'Università degli Studi di Genova.

## 📋 Panoramica del Progetto
Questo repository raccoglie l'implementazione e l'analisi sperimentale di circuiti quantistici a 2 qubit, focalizzandosi sullo studio dell'**entanglement** e delle correlazioni non-classiche. 
L'obiettivo principale è simulare e confrontare il comportamento di stati quantistici fattorizzabili (separabili) rispetto a stati fortemente correlati (stati di Bell), evidenziando le differenze fondamentali descritte dalla meccanica quantistica.

---

## 🔬 Architettura e Casi Studio
Il framework di simulazione (realizzato tramite **Python** e **Qiskit**) affronta tre scenari principali:

1. **Stati Fattorizzabili (Separabili):**
   * Configurazione del primo qubit nello stato $|\psi\rangle = \alpha|0\rangle + \beta|1\rangle$ con ampiezze $|\alpha|^2 = 0.4$ e $|\beta|^2 = 0.6$ tramite una rotazione $R_y$.
   * Preparazione del secondo qubit nello stato di sovrapposizione negativa $|-\rangle$.
   * Lo stato complessivo è descrivibile come prodotto tensoriale dei singoli sottosistemi.

2. **Stato di Bell $|\Phi^{+}\rangle$:**
   * Generazione dello stato entangled massimale $\frac{1}{\sqrt{2}}(|00\rangle + |11\rangle)$.
   * Utilizzo di una porta Hadamard sul primo qubit seguita da una porta logica controllata CNOT.

3. **Stato di Bell $|\Psi^{-}\rangle$:**
   * Implementazione dello stato di singoletto antisimmetrico $\frac{1}{\sqrt{2}}(|01\rangle - |10\rangle)$mediante l'applicazione combinata di porte di Pauli-$X$, Hadamard e CNOT.

---

## 📊 Risultati e Analisi delle Correlazioni
Le simulazioni eseguite tramite il simulatore aerodinamico confermano i principi teorici della computazione quantistica:
* **Assenza di correlazione nei sistemi separabili:** La misura effettuata sul primo qubit restituisce l'autovalore con probabilità $|\alpha|^2$ in modo totalmente indipendente dallo stato del secondo sottosistema.
* **Forti correlazioni/anticorrelazioni negli stati di Bell:** La misura eseguita su un qubit vincola deterministicamente l'esito dell'altro (es. collasso in $|00\rangle$ o $|11\rangle$), dimostrando le proprietà uniche dell'entanglement quantistico.

---

## ⚙️ Requisiti e Utilizzo
Per eseguire le simulazioni localmente, è necessario disporre di Python e delle librerie Qiskit installate:

```bash
pip install qiskit qiskit-aer numpy
```
Per lanciare lo script di simulazione ed estrarre i conteggi statistici:

```bash
python entanglementFCQ.py
```

## Autore
Francesco Giuseppino (Matricola: 6520241)

Corso di Laurea in Informatica – Università degli Studi di Genova
