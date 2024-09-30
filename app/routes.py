import json
import os

from app import app
from app import llm_engine
from flask import jsonify, request, render_template, send_from_directory


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/api/generate", methods=["POST"])
def generate_api():
    # exit()
    if request.method == "POST":
        try:
            req_body = request.get_json()
            print(jsonify(req_body))
            content = req_body.get("contents")
            model = llm_engine.get_model(model=req_body.get("model"))
            message = llm_engine.get_human_message(content=content)
            response = model.stream([message])

            
            def stream():
                for chunk in response:
                    yield f"data: {json.dumps({'text': chunk.content})}\n\n"

            return stream(), {"Content-Type": "application/json"}

        except Exception as e:
            return jsonify({"error": str(e)})


@app.route("/<path:path>")
def serve_static(path):
    return send_from_directory("web", path)


if __name__ == "__main__":
    app.run(port=int(os.environ.get("PORT", 8080)))