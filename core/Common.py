import json

def jsonToDict( postValues ):
    dictValues = None
    try:
        dictValues = postValues.get_json()
    except Exception as errMsg:
        postValues
    
    return dictValues