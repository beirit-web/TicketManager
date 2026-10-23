tickets = [
    {
        "id": 1, "titel": "Drucker funktioniert nicht",
        "prioritaet": "hoch",
        "status": "offen"
    },

    {
        "id": 2, "titel": "Passwort zurücksetzen",
        "prioritaet": "mittel",
        "status": "erledigt"
    },

    {
        "id": 3, "titel": "Server nicht erreichbar",
        "prioritaet": "hoch",
        "status": "offen"
    },

    {
        "id": 4, "titel": "Software installieren",
        "prioritaet": "niedrig",
        "status": "offen"
    },

    {
        "id": 5, "titel": "Netzwerkproblem",
        "prioritaet": "hoch",
        "status": "erledigt"
    },

    {
        "id": 6, "titel": "VPN-Verbindung gestört",
        "prioritaet": "mittel",
        "status": "offen"
    },
    {
        "id": 7,
        "titel": "Unbekannter Fehler"
    }
]


def kritische_tickets(tickets):
    prio_liste = []

    for wichtig in tickets:
        if wichtig.get('prioritaet') == 'hoch' and wichtig.get('status') == 'offen':
            prio_liste.append(wichtig)
    return prio_liste


print(kritische_tickets(tickets))
print('######################')


def ticket_abschliessen(tickets, ticket_id):

    for ticket in tickets:
        if ticket.get('id') == ticket_id:

            if ticket.get('status') == 'offen':
                ticket['status'] = 'erledigt'
                return ticket

            else:
                return f"ID {ticket.get('id')} ist bereits erledigt"

    return f"Ticket {ticket_id} existiert nicht"


print(ticket_abschliessen(tickets, 3))
print(ticket_abschliessen(tickets, 3))

print(ticket_abschliessen(tickets, 4))
print(ticket_abschliessen(tickets, 8))
print('########################')


def ticket_statistik(tickets):
    fertiger_dict = {
        'gesamt': len(tickets),
        'offen': 0,
        'erledigt': 0,
        'hoch': 0,
        'ohne_status': 0
    }

    for statistik in tickets:
        if statistik.get('status', 0) == 'offen':
            fertiger_dict['offen'] += 1
        if statistik.get('status', 0) == 'erledigt':
            fertiger_dict['erledigt'] += 1
        if statistik.get('prioritaet', 0) == 'hoch':
            fertiger_dict['hoch'] += 1
        if statistik.get('status') is None:
            fertiger_dict['ohne_status'] += 1
    return fertiger_dict


print(ticket_statistik(tickets))

print('###################')


def ticket_validieren(ticket):

    if 'id' in ticket and 'titel' in ticket and 'status' in ticket:
        return True
    return False


for ticket in tickets:
    print(f"Ticket {ticket.get('id')}: {ticket_validieren(ticket)}")
