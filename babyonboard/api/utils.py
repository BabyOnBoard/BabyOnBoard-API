from django.core import serializers
import json


JSON = 'json'

def jsonify(model):
    serialized = serializers.serialize(JSON, [model])
    aux_json = json.loads(serialized)

    if 'model' in aux_json[0]:
        del aux_json[0]['model']

    result = json.dumps(aux_json[0])

    return result
