# entanglementFCQ_Unige
# Studio dell'entanglement in sistemi a 2 qubit

## Introduzione
L'obiettivo di questa relazione è affrontare l'argomento "Studio dell'entanglement in sistemi a 2 qubit", nell'ambito dell'esame di Fondamenti di Computazione Quantistica. L'obiettivo principale consiste nell'analizzare le differenze comportamentali tra stati separabili e stati entangled, ovvero fortemente correlati. Secondo la meccanica quantistica, lo stato di un sistema composto da qubit multipli è descritto dal prodotto tensoriale degli spazi vettoriali dei singoli qubit. L'entanglement si verifica in sistemi in cui la misura su un sottosistema influenza il secondo, dimostrando correlazioni che non esistono nella fisica classica.

## Svolgimento
La prova si divide in due punti che richiedono la preparazione e la misurazione di specifici stati quantistici[cite: 12]. Le simulazioni sono state effettuate mediante la scrittura di un codice Python dedicato.

### Punto 1: Stati Fattorizzabili
È stato costruito lo stato $|\psi\rangle=\alpha|0\rangle+\beta|1\rangle$ con $|\alpha|^{2}=0.4$ e $|\beta|^{2}=0.6$ per il primo qubit. Il secondo qubit è stato preparato nello stato $|-\rangle$. Questo stato complessivo è fattorizzabile (o separabile) e si può scrivere come prodotto tensoriale.

### Punto 2: Stati di Bell
È stato generato lo stato di Bell $|\Phi^{+}\rangle$, la cui formula matematica è definita come $\frac{1}{\sqrt{2}}(|00\rangle+|11\rangle)$. La generazione richiede l'applicazione di una porta controllata CNOT che agisce sullo stato composto[cite: 12]. L'esperimento è stato ripetuto per generare lo stato di Bell $|\Psi^{-}\rangle$, il quale fa sempre parte della base di Bell e corrisponde alla sovrapposizione $\frac{1}{\sqrt{2}}(|01\rangle-|10\rangle)$.

## Risultati e Discussione
Le simulazioni hanno fornito risultati perfettamente in linea con i principi previsti. 
<img width="883" height="237" alt="image" src="https://github.com/user-attachments/assets/cecb8ad8-55dd-4a7b-8580-b303914a1b9b" />


### Analisi delle Correlazioni
I risultati confermano le aspettative teoriche:
* **Stati Separabili:** La misurazione degli stati separabili generati al Punto 1 dimostra l'assenza di correlazione. La probabilità di misurare l'autovalore sul primo qubit risulta pari a $|\alpha|^{2}$ in modo del tutto indipendente dalla misura sul secondo qubit. Per gli stati separabili, la misura su uno dei due sistemi non influenza in alcun modo lo stato dell'altro.
* **Stati di Bell:** Le misure sugli stati di Bell al Punto 2 mostrano invece sistemi fortemente correlati[cite: 12]. Quando due qubit si trovano, ad esempio, nello stato $|\Phi^{+}\rangle$, la misura sul primo sistema condiziona e vincola lo stato del secondo. Pertanto, misurando il valore 0 sul primo qubit, si ha la certezza matematica di ottenere 0 sul secondo, confermando le proprietà uniche offerte dai sistemi quantistici.

## Autore
* **Francesco Giuseppino**
* (Matricola: 6520241)
