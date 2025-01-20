from transformers import pipeline

# Pipeline initialisieren mit dem trainierten deutschen Modell
qa_pipeline = pipeline("question-answering", model="deepset/gelectra-base-germanquad")

def frage_beantworten_verbessert(text_abschnitte, frage, kindgerecht=True):
    """
    Verarbeitet Textabschnitte und eine Frage und liefert eine kindgerechte Antwort.

    :param text_abschnitte: Liste von Textabschnitten.
    :param frage: Die Eingabefrage (Text).
    :param kindgerecht: Boolescher Wert, ob die Antwort kindgerecht sein soll.
    :return: Kindgerechte Antwort als Text.
    """
    beste_antwort = None
    beste_score = 0

    try:
        for abschnitt in text_abschnitte:
            # Frage beantworten für jeden Abschnitt
            result = qa_pipeline(question=frage, context=abschnitt)

            # Prüfen, ob die Antwort besser ist als die vorherige
            if result['score'] > beste_score:
                beste_antwort = result['answer']
                beste_score = result['score']

        # Überprüfen, ob eine valide Antwort gefunden wurde
        if beste_antwort and beste_score > 0.2:  # Score-Schwelle für sinnvolle Antworten
            if kindgerecht:
                return f"Aus dem Text habe ich herausgefunden: {beste_antwort}. Ich hoffe, das erklärt es gut für dich!"
            else:
                return beste_antwort
        else:
            return (
                "Ich konnte die Frage nicht direkt aus dem Text beantworten. "
                "Aber ich versuche trotzdem zu helfen: Vielleicht hilft es, den Text noch einmal anzusehen."
            )

    except Exception as e:
        return (
            "Es gab ein Problem bei der Verarbeitung. "
            f"Ich kann die Frage nicht aus dem Text beantworten: {str(e)}"
        )


# Beispielhafte Nutzung
if __name__ == "__main__":
    # Neuer Lesetext in Abschnitte unterteilt
    text_abschnitte = [
        """
        Benni soll in seiner Klasse einen Vortrag halten, welche Berufe seine Familie ausübt.
        Er sagt, sein Onkel sei Feuerwehrmann. Benni durfte schon oft mit im Feuerwehrauto sitzen.
        
        Einmal wurde sein Onkel zu einem Einsatz gerufen und musste in einem Familienhaus einen Brand löschen.
        Bei solchen Einsätzen darf Benni nicht mitfahren. Bei weniger gefährlichen Aufgaben aber schon.
        
        Eine verletzte Katze saß auf einem Baum und kam nicht mehr herunter. Benni durfte helfen.
        Der Junge versuchte, die Katze zu locken. Es gelang ihm und er nahm die Katze an sich.

        Er kletterte langsam die Leiter hinunter und freute sich, bei einem Feuerwehreinsatz dabei gewesen zu sein.
        Bennis Klasse war begeistert, als er die Geschichte erzählte und stolz vor ihnen stand.
        """
    ]

    # Fragen zum Text
    fragen = [
        "Welchen Beruf hat Bennis Onkel?",
        "Welches Tier hat Benni gerettet?",
        "Was für ein Haus brannte?",
        "Wo saß das Tier?"
    ]

    # Antworten für jede Frage generieren
    for frage in fragen:
        antwort = frage_beantworten_verbessert(text_abschnitte, frage)
        print(f"Frage: {frage}\nAntwort: {antwort}\n")


# https://www.grundschule-arbeitsblaetter.de/deutsch/lesetexte/#lesetexte-fragen-neu
