import joblib
import sys

model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

def predict_command(cmd):
    vec = vectorizer.transform([cmd])
    pred = model.predict(vec)[0]
    prob = model.predict_proba(vec)[0][pred]
    return pred, prob

if __name__ == "__main__":
    
    if len(sys.argv) > 1:
        command = " ".join(sys.argv[1:])
        label, confidence = predict_command(command)

        verdict = "BENIGN" if label == 0 else "MALICIOUS"
        print(f"\nCommand   : {command}")
        print(f"Prediction: {verdict}")
        print(f"Confidence: {confidence:.2f}")

    else:
        print("Enter command (type 'exit' to quit)")
        while True:
            cmd = input("> ")
            if cmd.lower() == "exit":
                break

            label, confidence = predict_command(cmd)
            verdict = "BENIGN" if label == 0 else "MALICIOUS"
            print(f"{verdict} (confidence={confidence:.2f})")
