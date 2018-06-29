import json


# input: binary
# output: string or binary (will be converted to binary)

def call(data):
    #Convert input data from binary
    vals = json.loads(data.decode("utf-8"))

    #Apply the actual UDF
    out = classify(vals)

    #Return result converted into string
    return str(out)

def classify(vals):

    feature0 = float(vals['temperature'])
    feature1 = float(vals['humidity'])
    feature2 = float(vals['light'])
    feature3 = float(vals['co2'])
    feature4 = float(vals['humidityratio'])


    #manual copy of the model to avoid having to read it in from Spark model folder every time.
    if (feature2 <= 389.0):
        if (feature2 <= 241.333):
            if (feature3 <= 1449.25):
                if (feature3 <= 799.0):
                    return 0.0
                elif (feature3 > 799.0):
                    if (feature2 <= 87.0):
                        return 0.0
                    elif (feature2 > 87.0):
                        return 0.0
            elif (feature3 > 1449.25):
                if (feature0 <= 22.075):
                    return 0.0
                elif (feature0 > 22.075):
                    return 1.0
        elif (feature2 > 241.333):
            if (feature3 <= 465.0):
                return 0.0
            elif (feature3 > 465.0):
                return 1.0
    elif (feature2 > 389.0):
        if (feature3 <= 477.333):
            if (feature2 <= 432.75):
                if (feature0 <= 20.7):
                    if (feature3 <= 465.0):
                        return 1.0
                    elif (feature3 > 465.0):
                        return 0.0
                elif (feature0 > 20.7):
                    return 1.0
            elif (feature2 > 432.75):
                return 0.0
        elif (feature3 > 477.333):
            if (feature0 <= 22.6):
                if (feature0 <= 22.175):
                    if (feature0 <= 19.625):
                        return 1.0
                    elif (feature0 > 19.625):
                        return 1.0
                elif (feature0 > 22.175):
                    if (feature3 <= 948.666):
                        return 1.0
                    elif (feature3 > 948.666):
                        return 1.0
            elif (feature0 > 22.6):
                if (feature1 <= 26.89):
                    if (feature3 <= 1063.5):
                        return 1.0
                    elif (feature3 > 1063.5):
                        return 0.0
                elif (feature1 > 26.89):
                    return 1.0
