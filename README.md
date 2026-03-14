Jordan - Home Chatbot
===================

Jordan is a mischievous little doorman made with the vintage ChatterBot library. It interviews every visitor, rolls its digital eyes at strangers, and unlocks a stash of hyper-personal trivia when Mark finally steps inside. Think of it as a text-only smart home concierge that lives entirely in your terminal.

Highlights
----------
- Identity quiz with special replies for Mark, Jane, and uninvited guests.
- Pretrained house lore (owner, hometown, favorite book/movie/sport) powered by `ListTrainer`.
- Endless chat loop that learns lightweight conversations on the fly until you say goodbye.
- Super small codebase: `main.py` runs the story, `functions.py` keeps the bot utilities.

Requirements
------------
- Python 3.8–3.10 recommended (ChatterBot is abandoned and picky about interpreters).
- `chatterbot==1.0.4`
- `chatterbot-corpus`

Setup
-----
```bash
git clone <your-fork-url> jordan-home-chatbot
cd jordan-home-chatbot
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install chatterbot==1.0.4 chatterbot-corpus
```

Run It
------
```bash
python main.py
```
State your identity when prompted. Answer with “Mark” to trigger extra training data (hometown, favorite book, movie, and sport). Type “bye”, “bye jordan”, or “good bye” whenever you want to shut the conversation down.

Make It Yours
-------------
1. Drop new `[question, answer]` pairs into the Mark section of `main.py` (or add your own identity branches).
2. Call `custom_train(home_bot, your_list)` for each topic.
3. Restart the bot and keep iterating on tone, personality, or even the access rules.

Wishlist
--------
- Voice-based identity check or OTP flow instead of plain text.
- Persistent storage so Jordan remembers every conversation.
- Fun UI wrapper (Tkinter, web, or even a neon LED display) for that sci‑fi foyer vibe.

Feel free to fork it, remix it, and teach Jordan even more embarrassing facts about Mark.
