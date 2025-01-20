# Digitaler-Leseassistent-fuer-Kinder-
WWI22DSA/B Natural Language Processing (Aktuelle Data Science-Entwicklungen I)
Model also found on hugging face:
https://huggingface.co/mxhmxt/distilbert-qa-digital-reading-assistant-for-children/tree/main

Digitaler Leseassistent für Kinder: 
Ein interaktives Tool zur Unterstützung beim Lesen


Beschreibung:
Wir möchten ein Tool entwickeln, das Kinder beim Lesen unterstützt. Oft stoßen sie auf Wörter, die sie nicht verstehen, oder haben Fragen zu einem Text, die sie ohne Hilfe nicht beantworten können. Unser Projekt soll genau hier helfen.


Der Plan ist, einen interaktiven Leseassistenten zu bauen, der:

Schwierige Wörter erkennt und kindgerechte Erklärungen dazu liefert.
Fragen zu Texten beantwortet, damit Kinder das Gelesene besser verstehen können.
Eine einfache Benutzeroberfläche bietet, die Spaß macht und leicht zu bedienen ist.
Um das umzusetzen, nutzen wir moderne NLP-Technologien wie Named Entity Recognition (NER) und Question-Answering-Modelle (z. B. BERT, distilbert-base-uncased). Außerdem bauen wir eine intuitive Oberfläche, die Kinder zum Lesen und Interagieren einlädt.

Gruppenmitglieder:

Alexander Rohr
Tim Stelzner
Mehmet Marijanovic
Rouah Abdul Jawad



Abschnitt Worteinteilung

Da die Kinder in der Lage sein sollten bestimmte Grundwörter zu verstehen und es einen großen Aufwand für die Webseite jedes Wort zu erklären, muss davon auszugehen sein, dass die Kinder einige Wörter kennen. Diese Liste muss erstmals gefunden werden. Dies stellte zuerst ein Problem dar, da es nicht viele Listen online zur Verfügung stehen, die nach Klassenlevel oder nach Sprachlevel (A1, A2, B1 etc.). Was jedoch online zur Verfügung steht ist eine Liste des Landes NRW zum Grundwortschatz im deutschen. Ein Problem jedoch bei dieser Liste ist, dass diese nicht alle Formen eines Wortes haben. So ist zum Beispiel bei Nomen nur die Nominativ Singular Form vorhanden und bei Verben nur der Singular plural Präsenz vorhanden, wie zum Beispiel „lesen“.
Erstmal werden die Wörter aus dem PDF in eine Text Datei eingefügt und mittels eines Textsprunges getrennt. Die Textdatei wird dann mittels ChatGPT um die anderen Wortformen erweitert. Diese daraus resultierende Textdatei besitzt 1600  anstelle von ursprünglichen 533 Wörtern und ist größtenteils vollständig mit allen Formen der Grundwörtern.
Danach wird ein Programm geschrieben welches die Aufgabe hat Wörter aus einem Text in 3 Listen einzuteilen. Die 3 Listen sind: Grundwörter, Wörter die in der Textdatei vorhanden sind, Andere Wörter, Wörter die nicht im Grundtext stehen, jedoch in einem Onlinelexikon stehen, und sonstige Wörter, Wörter die weder im Grundtext noch im Online Lexikon stehen. Um dies umzusetzen wird ein String eines Textes verwendet, dieser wird in die einzelnen Wörter zerlegt und in eine Liste eingefügt, indem die Wörter zwischen den Leerzeichen getrennt werden. Zusätzlich werden nur Buchstaben die den Char-value von deutschen Klein und Großbuchstaben haben(). Daraufhin werden die Wörter in Kleinbuchstaben transformiert und mit der Textdatei verglichen, die auch in Kleinbuchstaben transformiert werden. Dies ist notwendig da beim Vergleich zwischen zwei Wörtern/Strings diese den exakt gleichen Wert haben. Die daraus resultierenden Wörter werden daraufhin in die 3 Listen eingeteilt. 

In der Anwendung der App wird in Schritt 4 werden die verschiedenen Funktionen definiert die zuvor beschrieben wurden. Zuerst wird die Grundtext Datei geladen, damit die schwierigen Wörter gefunden werden können, in diesem Fall sind schwere Wörter alle Wörter die nicht im Grundwörter Textdatei stehen. Die nächsten 2 Funktionen extrahieren die Bedeutungen von einem Wort, falls die Bedeutung von einem Wort nicht stehen, werden die grammatikalischen Merkmale von einem Wort wieder gegeben. Falls diese auch nicht dasteht wird der gesamte Text wiedergegeben. In Schritt 5 wird der der Input Text alle Zeichen entfernt die keine deutschen Buchstaben  oder Leerzeichen sind. Die Wörter werden dann nach der Entfernung aller Zeichen werden alle schwierigen Wörter nach deren Bedeutungen oder grammatikalischen Merkmale überprüft. Sollte keines der beiden gefunden werden, werden die Wörter nochmal mit anfängende Klein- und Großbuchstaben untersucht. Die schwierigen Wörter werden im originellen Text dann Rot markiert. Die Bedeutungen und Grammatikalischen Merkmale werden daraufhin unterhalb des originalen Inputs eingefügt.