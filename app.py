from flask import Flask, request, jsonify

app = Flask(__name__)

# ✅ Root route to prevent "Not Found" error
@app.route("/")
def home():
    return "✅ Neurostark Backend is Live!"

# ✅ Example route for generating a film
@app.route("/generate", methods=["POST"])
def generate_film():
    data = request.json
    script = data.get("script")
    genre = data.get("genre")
    image_url = data.get("image")

    # Simulated response — replace with your real logic
    result = {
        "status": "success",
        "message": f"Film generated in genre: {genre} with image: {image_url}",
        "download_url": "https://yourserver.com/download/sample.mp4"
    }
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
