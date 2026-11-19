# BWL – Wareneinsatz und Rohgewinn

Interaktive BWL-Übung zu **Einkauf, Verkauf, Buchungssätzen, Wareneinsatz und Rohgewinn**.
Die Anwendung ist für Smartphones, Tablets und Desktop-Browser optimiert.

## 🌐 Webseite

**[Interaktive Übung öffnen](https://leontofficial.github.io/BWL-Wareneinsatz/)**

Die Übung läuft direkt im Browser, ohne Installation, Anmeldung oder API-Schlüssel.

## ✅ Automatische Prüfung

Über **GitHub Actions** wird die Webseite bei Änderungen, Pull Requests und täglich geprüft:

- HTML-Struktur und interne Verweise (Tabs, Formulare und Schaltflächen)
- Vorhandensein der wichtigsten Übungsabschnitte
- JavaScript-Syntax
- Keine bekannten alten Schul- und Personenbezüge in der HTML-Datei
- Erreichbarkeit der öffentlichen Webseite beim täglichen Lauf

Bei einem fehlgeschlagenen täglichen Check wird automatisch ein GitHub-Issue erstellt, sofern nicht bereits ein offenes gleichnamiges Issue existiert. Es werden **keine automatischen Änderungen an der Webseite vorgenommen**.

[Prüfungen ansehen](https://github.com/LeonTOfficial/BWL-Wareneinsatz/actions)

## 🔒 Sicherheit

Die Prüfungen nutzen Python und Node.js aus der GitHub-Laufzeit ohne zusätzliche Actions aus Drittquellen. Änderungen an `index.html` werden ausschließlich durch normale Git-Commits vorgenommen. Für die automatischen Fehlerberichte benötigt die GitHub Action Schreibrechte für Issues.

*Hinweis: Die Anwendung ist ein Lernmodell. Rechnungen und Namen in der Übung sind fiktiv.*
