import os
import json

import logging
LOGGER = logging.getLogger("server")

from . import ROOT_DIR


def _load_model(model):
    print('_load_model(): model',model)
    if not os.path.exists(model["model"]["fn"]):
        return False
    return {
        "fn": model["model"]["fn"],
        "type": model["model"]["type"],
        "fine_tune_layer": model["model"]["fineTuneLayer"]
    }

def load_models():
    models = dict()
    
    model_json = json.load(open(os.path.join(ROOT_DIR,"models.json"),"r"))
    for key, model in model_json.items():
        model_object = _load_model(model)
        
        if model_object is False:
            LOGGER.warning("Files are missing, we will not be able to serve the following model: '%s'" % (key)) 
        else:
            models[key] = model_object

    
    if os.path.exists(os.path.join(ROOT_DIR, "models.mine.json")):
        model_json = json.load(open(os.path.join(ROOT_DIR,"models.mine.json"),"r"))
        for key, model in model_json.items():
            
            if key not in models:
                model_object = _load_model(model)
                
                if model_object is False:
                    LOGGER.warning("Files are missing, we will not be able to serve the following model: '%s'" % (key)) 
                else:
                    models[key] = model_object
            else:
                LOGGER.warning("There is a conflicting dataset key in models.mine.json, skipping.")

    print('load_models(): models', models)
    return models