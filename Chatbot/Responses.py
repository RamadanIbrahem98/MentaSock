import random

# an advice for the doctor
R_ADVICE = "If I were you, I would check the vital signals or dicom image again for any to check for any abnormaities"

# check for unknown words and returns a resposnse
def unknown():
    response = ["Could you please re-phrase that? ",
                "What does that mean?"][
        random.randrange(2)]
    return response