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
        extracted_fields = {}
        extracted_fields["fullname"] = str(data.get("name")).title()
        extracted_fields["email"] = data.get("email")
        extracted_fields["phone"] = data.get("phone")
        extracted_fields["linkedin"] = ""
        extracted_fields["github"] = ""
        extracted_fields["education"] = []
        for i in range(0,len(data.get("university"))):
            uni_dict = {}
            uni_dict["university"] = str(data.get("university")[i]).title()
            if len(data.get("degree"))>i:
                uni_dict["program"] = str(data.get("degree")[i]).title()
            else:
                uni_dict["program"] = ""
            uni_dict["graduation"] = ""
            uni_dict["grade"] = ""
            uni_dict["coursework"] = ""
            extracted_fields["education"].append(uni_dict)
        
        extracted_fields["skills"] = data.get("skills")
        extracted_fields["experience"] = []
        for i in range(0, len(data.get("Companies worked at"))):
            exp_dict = {}
            if len(data.get("designition"))>=i:
                exp_dict["position"] = str(data.get("designition")[i]).title()
            else:
                exp_dict["position"] = ""
            exp_dict["company"] = str(data.get("Companies worked at")[i]).title()
            exp_dict["location"] = ""
            exp_dict["duration"] = ""
            exp_dict["points"] = []
            extracted_fields["experience"].append(exp_dict)

        return json.dumps({'parsed_resume': extracted_fields})
    except Exception as e:
        print(e)
        return json.dumps({"Error": str(e)})


if __name__ == '__main__':
    app.run(port=5004, debug=True)