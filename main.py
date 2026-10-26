tickets = []


def kritische_tickets(tickets):
    prio_liste = []

    for wichtig in tickets:
        if wichtig.get('prioritaet') == 'hoch' and wichtig.get('status') == 'offen':
            prio_liste.append(wichtig)
    return prio_liste


def ticket_abschliessen(tickets, ticket_id):

    for ticket in tickets:
        if ticket.get('id') == ticket_id:

            if ticket.get('status') == 'offen':
                ticket['status'] = 'erledigt'
                return ticket

            else:
                return f"ID {ticket.get('id')} ist bereits erledigt"

    return f"Ticket {ticket_id} existiert nicht"


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


def ticket_validieren(ticket):
    return 'id' in ticket and 'titel' in ticket and 'status' in ticket


def ticket_erstellen(tickets, titel, prioritaet):
    ids = []

    for ticket in tickets:
        ids.append(ticket['id'])

    if not ids:
        neue_id = 1
    else:
        neue_id = max(ids) + 1

    neues_ticket = {
        'id': neue_id,
        'titel': titel,
        'prioritaet': prioritaet,
        'status': 'offen'
    }

    tickets.append(neues_ticket)
    return neues_ticket


print('---- Erstellt ----')
print(ticket_erstellen(tickets, "Monitor defekt", "hoch"))
print(ticket_erstellen(tickets, "Tastatur defekt", "mittel"))
print('---- Gefunden ----')
print(ticket_abschliessen(tickets, ticket_id=1))
print('---- Statistik ----')
print(ticket_statistik(tickets))

print('---- Validation ----')

for ticket in tickets:
    if ticket_validieren(ticket):
        print(f"Ticket {ticket.get('id')}: Gültig")
    else:
        print(f"Ticket {ticket.get('id')}: Ungültige Eingabe")
