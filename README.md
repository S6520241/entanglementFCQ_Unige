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


______________________________________________________________



# entanglementFCQ_Unige
## Quantum Entanglement Analysis in 2-Qubit Systems

Project developed for the **Fundamentals of Quantum Computing** exam at the University of Genoa.

## 📋 Project Overview
This repository contains the implementation and experimental analysis of 2-qubit quantum circuits, focusing on the study of **entanglement** and non-classical correlations. 
The main objective is to simulate and compare the behavior of factorizable (separable) quantum states versus strongly correlated states (Bell states), highlighting the fundamental differences described by quantum mechanics.

---

## 🔬 Architecture and Case Studies
The simulation framework (built using **Python** and **Qiskit**) addresses three main scenarios:

1. **Factorizable (Separable) States:**
   * Configuration of the first qubit in the state $|\psi\rangle = \alpha|0\rangle + \beta|1\rangle$ with amplitudes $|\alpha|^2 = 0.4$ and $|\beta|^2 = 0.6$ via an $R_y$ rotation.
   * Preparation of the second qubit in the negative superposition state $|-\rangle$.
   * The overall state can be described as the tensor product of the individual subsystems.

2. **Bell State $|\Phi^{+}\rangle$:**
   * Generation of the maximally entangled state $\frac{1}{\sqrt{2}}(|00\rangle + |11\rangle)$.
   * Use of a Hadamard gate on the first qubit followed by a CNOT controlled logic gate.

3. **Bell State $|\Psi^{-}\rangle$:**
   * Implementation of the antisymmetric singlet state $\frac{1}{\sqrt{2}}(|01\rangle - |10\rangle)$ through the combined application of Pauli-$X$, Hadamard, and CNOT gates.

---

## 📊 Results and Correlation Analysis
Simulations executed via the aer simulator confirm the theoretical principles of quantum computing:
* **Absence of correlation in separable systems:** Measurement performed on the first qubit returns the eigenvalue with probability $|\alpha|^2$ completely independently of the state of the second subsystem.
* **Strong correlations/anticorrelations in Bell states:** Measurement performed on one qubit deterministically constrains the outcome of the other (e.g., collapse into $|00\rangle$ or $|11\rangle$), demonstrating the unique properties of quantum entanglement.

---

## ⚙️ Requirements and Usage
To run the simulations locally, you need Python and the required Qiskit libraries installed:

```bash
pip install qiskit qiskit-aer numpy
```
To run the simulation script and extract statistical counts:
```bash
python entanglementFCQ.py
```

## Author
Francesco Giuseppino (Student ID: 6520241)
Bachelor’s Degree in Computer Science – University of Genoa
