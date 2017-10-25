from django.core import serializers
import json
import subprocess


JSON = 'json'


def jsonify(model):
    if model is None:
        return json.dumps({})

    serialized = serializers.serialize(JSON, [model])
    aux_json = json.loads(serialized)

    if 'model' in aux_json[0]:
        del aux_json[0]['model']

    result = json.dumps(aux_json[0])

    return result

def runCScript(movement_type):
    test = subprocess.Popen(["echo", movement_type], stdout=subprocess.PIPE)
    output = test.communicate()[0]
    print(output)
    return