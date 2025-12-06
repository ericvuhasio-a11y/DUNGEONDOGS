from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return jsonify({
        "message": "DungeonDogs NPC Server — LIVE & HUNTING",
        "status": "paws-up",
        "endpoints": ["/npc", "/health"]
    })

@app.route("/health")
def health():
    return jsonify({"status": "WOOF!"})

@app.route("/npc")
def npc():
    query = request.args.get("query", "stranger").strip()
    breed = request.args.get("breed", "loyal").lower()
    
    responses = {
        "loyal": f"Woof! {query}? Follow me, I’ll guide you through the dark!",
        "sneaky": f"Heh… {query}? I know a secret tunnel… for a bone.",
        "grumpy": f"Bark! {query}? Just don’t die too fast, hooman.",
        "chaotic": f"AROOO! {query}?! LET’S BITE FIRST AND ASK LATER!"
    }
    reply = responses.get(breed, responses["loyal"])
    
    return jsonify({
        "npc": reply,
        "breed": breed,
        "mood": "ready to fetch"
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
