import os
import discord
import requests
import random

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
ELEVENLABS_API_KEY = os.getenv('ELEVENLABS_API_KEY')
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
client = discord.Client(intents=intents)

# Chat-History für die aktuelle Session initialisieren
chat_history = []

@client.event
async def on_ready():
    print(f'Eingeloggt als {client.user}!')

@client.event
async def on_message(message):
    if message.author == client.user or message.channel.name != 'dungeons-and-dragons':
        return

    # Nachricht zur Chat-History hinzufügen
    chat_history.append({'role': 'user', 'content': message.content})

    # Kontext für die KI aus der Chat-History erstellen
    context = " ".join(msg['content'] for msg in chat_history[-5:])  # Die letzten 5 Nachrichten berücksichtigen

    character_prompt = f"""
    Du bist Rainer Winkler, der liebenswerte Drachenlord von YouTube. Du hast angst vor den Haidern und bist deswegen immer auf der Flucht inerhalb Deutschlands. In diesem Gespräch wird Rainer zum Dungeon Master um ein neues Abenteuer zu beginnen, ...
    {context}
    Wenn du als Rainer antwortest, musst du die folgenden Regeln befolgen:
    1) Geib kurze Antworten, etwa 1-2 Absätze.
    2) Sage Gelegentlich sowas wie: "Brot und Brötchen wird nicht mehr kommen".
    3) Bleibe immer in deiner Rolle, egal was passiert.
    4) Schreibe und verwende neue Sprüche, die lustige Beobachtungen über die aktuellen Situationen sind.
    5) Du hast eine Freundin die aus "Denken" kommt.
    6) Dein Vater heißt Rudi und kommt aus "Buddeln".
    7) Beleidige die Haider ab und zu.
    8) Fasse deine Antworten in wenigen Sätzen zusammen.
    """

    # Senden der Nachricht an OpenAI mit dem Modell GPT-4
    response = requests.post(
        'https://api.openai.com/v1/chat/completions',
        headers={'Authorization': f'Bearer {OPENAI_API_KEY}'},
        json={
            'model': 'gpt-4',
            'messages': [{'role': 'system', 'content': character_prompt}],
            'max_tokens': 150
        }
    )
    if response.status_code == 200:
        data = response.json()
        if 'choices' in data and data['choices'][0]['message']['content']:
            openai_response = data['choices'][0]['message']['content']
            chat_history.append({'role': 'bot', 'content': openai_response})  # Antwort zur Chat-History hinzufügen
        else:
            return
    else:
        return

    # Hinzufügen zufälliger Ausrufe und Abschlussphrasen
    if random.random() < 0.1:  # 10% Chance, "Hagebuddne" zu sagen
        openai_response = "Hagebuddne! " + openai_response
    openai_response += " Etzio!"

    # Senden der Antwort an ElevenLabs zur Sprachgenerierung
    audio_response = requests.post(
        "https://api.elevenlabs.io/v1/text-to-speech/EQRbYWqcEn5t65MALWec",
        headers={
            "Accept": "audio/mpeg",
            "Content-Type": "application/json",
            "xi-api-key": ELEVENLABS_API_KEY
        },
        json={
            "text": openai_response,
            "model_id": "eleven_multilingual_v1",
            "voice_settings": {
                "stability": 0.5,
                "similarity_boost": 0.5
            }
        }
    )
    if audio_response.status_code == 200:
        with open('response.mp3', 'wb') as f:
            f.write(audio_response.content)
        await message.channel.send(file=discord.File('response.mp3'))
    else:
        print("Fehler bei der Generierung der Audio-Datei:", audio_response.status_code)
        print("Antwortdetails:", audio_response.text)

client.run(DISCORD_TOKEN)
