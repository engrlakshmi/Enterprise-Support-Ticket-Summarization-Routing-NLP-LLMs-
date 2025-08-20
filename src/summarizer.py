from transformers import pipeline

class Summarizer:
    def __init__(self, model="facebook/bart-large-cnn"):
        self.summarizer = pipeline("summarization", model=model)

    def summarize(self, text, max_length=30, min_length=5):
        return self.summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)[0]['summary_text']


if __name__ == "__main__":
    s = Summarizer()
    print(s.summarize("Outlook not opening after update, user unable to access email"))
