import app as backend_app
from flask import Flask, render_template,jsonify,request

app = Flask(__name__)

@app.route('/')
def index():
    try:
        return render_template('index.html')
    except Exception as e:
        return jsonify({"error": str(e)}), 500 

@app.route('/load-tasks', methods=['GET'])
def load_tasks():
    try:    
        data= backend_app.load_tasks()
        return {"tasks":data}
    except Exception as e:
        return jsonify({"error": str(e)}), 500 
    
@app.route('/save-tasks', methods=['POST'])
def saveTasks():
    try:    
        tasks = request.get_json() 
        backend_app.save_tasks(tasks['tasks'])

        return {"success":True}
    except Exception as e:
        return jsonify({"error": str(e)}), 500 

if __name__ == '__main__':
    app.run(debug=True)