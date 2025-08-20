from transformers import pipeline

class TicketClassifier:
    def __init__(self, model="facebook/bart-large-mnli"):
        self.classifier = pipeline("zero-shot-classification", model=model)
        self.labels = ["Network Issue", "Hardware Issue", "Software Issue", "Critical", "Low Priority"]

    def classify(self, text):
        result = self.classifier(text, candidate_labels=self.labels)
        return result["labels"][0]  # return top label


if __name__ == "__main__":
    clf = TicketClassifier()
    print(clf.classify("VPN connection dropping frequently"))
