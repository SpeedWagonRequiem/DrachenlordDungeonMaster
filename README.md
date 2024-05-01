# Discord Bot: Rainer Winkler Adventures

## Beschreibung
Dieses Repository enthält den Code für einen Discord-Bot, der die Rolle von Rainer Winkler, einem fiktiven Charakter inspiriert von YouTube-Persönlichkeiten, übernimmt. Der Bot interagiert mit Benutzern in Discord-Kanälen, indem er Textnachrichten verarbeitet, auf sie mit kontextbezogenen, charakteristischen Antworten reagiert und diese Antworten mithilfe einer Text-to-Speech-Technologie in Sprachausgaben umwandelt.

## Features
- **Chat-Interaktion**: Der Bot nimmt an Gesprächen teil, indem er auf Benutzereingaben reagiert und dabei den Kontext früherer Nachrichten berücksichtigt.
- **Rollenbasierte Antworten**: Antworten basieren auf der festgelegten Rolle von Rainer Winkler, inklusive spezifischer Persönlichkeitsmerkmale und Verhaltensweisen.
- **Text-to-Speech**: Antworten werden nicht nur als Text, sondern auch als Sprachausgabe übermittelt, wobei der Dienst von ElevenLabs genutzt wird.

## Technologien
- **Python**: Die Hauptprogrammiersprache für den Bot.
- **Discord.py**: Eine Python-Bibliothek, die es ermöglicht, mit der Discord API zu interagieren.
- **OpenAI's GPT-4**: Nutzt die fortschrittliche KI von OpenAI für die Generierung von Antworten.
- **ElevenLabs API**: Wird verwendet, um Textantworten in Sprachausgaben umzuwandeln.

## Setup
### Voraussetzungen
- Python 3.8 oder höher
- Discord Account und ein Bot Token
- API-Keys für OpenAI und ElevenLabs

### Umgebungsvariablen
Stellen Sie sicher, dass folgende Umgebungsvariablen gesetzt sind:
- `OPENAI_API_KEY`: Ihr API-Key für OpenAI.
- `ELEVENLABS_API_KEY`: Ihr API-Key für ElevenLabs.
- `DISCORD_TOKEN`: Der Token Ihres Discord Bots.

### Installation
1. Klonen Sie das Repository auf Ihren lokalen Computer.
2. Installieren Sie die erforderlichen Abhängigkeiten mit `pip install -r requirements.txt`.
3. Starten Sie den Bot durch Ausführen von `python chatgpt_character.py`.

## Benutzung
Fügen Sie den Bot zu einem Discord-Server hinzu und interagieren Sie mit ihm in einem Kanal namens `dungeons-and-dragons`. Der Bot wird automatisch auf Nachrichten reagieren, die auf den Charakter von Rainer Winkler abgestimmt sind.

## Beitrag
Beiträge sind willkommen! Für größere Änderungen öffnen Sie bitte zuerst ein Issue, um zu diskutieren, was Sie ändern möchten.

## Lizenz
Dieses Projekt steht unter der MIT-Lizenz. Details finden Sie in der `LICENSE`-Datei.
