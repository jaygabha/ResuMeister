import numpy as np
from flask import Flask, request
from json import JSONEncoder
from resume_parser import resumeparse
import json
app = Flask(__name__)

class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)

@app.route('/parse_resume',methods=['GET'])
def parse_resume():
    # Get the data from the POST request.
    try:
        file_path = str(request.args.get("file_path"))
        data = resumeparse.read_file(file_path)
        return json.dumps({'parsed_resume': data})
    except Exception as e:
        return json.dumps({"Error": str(e)})


if __name__ == '__main__':
    app.run(port=5004, debug=True)