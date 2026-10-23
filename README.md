<div align="center">

<img src="ticket-manager/assets/ticket-manager-banner.svg" alt="TicketManager – Python IT-Support-Tickets" width="900">

# TicketManager

**Ein Python-Lernprojekt zur Verwaltung, Validierung und statistischen Auswertung von IT-Support-Tickets.**

<img src="ticket-manager/assets/python-badge.svg" alt="Python" height="30"> <img src="ticket-manager/assets/learning-badge.svg" alt="Lernprojekt" height="30"> <img src="ticket-manager/assets/data-badge.svg" alt="Fiktive Daten" height="30">

</div>

## Über das Projekt

TicketManager ist eine kleine, derzeit konsolenbasierte Python-Anwendung. Ich entwickle sie Schritt für Schritt, um meine Kenntnisse in Python, Datenstrukturen und Programmierlogik praktisch zu vertiefen.

Das Projekt verwendet **ausschließlich fiktive Beispieldaten**. Es ist ein Lernprojekt und noch kein produktives Ticketsystem.

## Aktuelle Funktionen

- **Kritische Tickets filtern:** offene Tickets mit hoher Priorität ermitteln.
- **Tickets abschließen:** ein Ticket anhand seiner ID suchen und seinen Status ändern.
- **Ticket-Statistik:** Gesamtzahl, offene und erledigte Tickets sowie Tickets mit hoher Priorität zählen.
- **Pflichtfelder prüfen:** feststellen, ob ein Ticket die Schlüssel `id`, `titel` und `status` enthält.
- **Unvollständige Datensätze berücksichtigen:** fehlende Schlüssel mit `dict.get()` erkennen.

> **Entwicklungsstand:** Die Funktionen werden aktuell anhand einer Python-Liste mit Dictionaries getestet. Es gibt noch keine Datenbank, Benutzerverwaltung oder Weboberfläche.

## Verwendete Python-Konzepte

`list` · `dict` · `for` · `if / else` · `and` · `in` · `dict.get()` · `return` · `len()` · f-Strings

## Beispiel eines Tickets

```python
{
    "id": 3,
    "titel": "Server nicht erreichbar",
    "prioritaet": "hoch",
    "status": "offen"
}
```

## Projekt lokal ausführen

**Voraussetzung:** Python 3.

```bash
git clone https://github.com/beirit-web/TicketManager.git
cd TicketManager
python main.py
```

## Geplante Weiterentwicklung

- [ ] Funktionen in separate Python-Module aufteilen
- [ ] Automatisierte Tests ergänzen
- [ ] Fehlerfälle und Ticketstatus robuster behandeln
- [ ] Tickets dauerhaft speichern, beispielsweise mit SQLite
- [ ] Optional später eine Django-Webanwendung entwickeln

## Hinweise

Die Ticketdaten und Fehlerfälle dienen ausschließlich dem Üben. Änderungen an den Daten bleiben derzeit nur während der Programmausführung erhalten.

---

<div align="center">
  <img src="ticket-manager/assets/footer.svg" alt="Lernen · Entwickeln · Verbessern" width="680">
</div>
