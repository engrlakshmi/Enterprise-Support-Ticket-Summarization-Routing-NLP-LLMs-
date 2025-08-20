import pandas as pd
from summarizer import Summarizer
from classifier import TicketClassifier
from router import Router

def main():
    # Load tickets
    tickets = pd.read_csv("../data/tickets.csv")

    # Initialize agents
    summarizer = Summarizer()
    classifier = TicketClassifier()
    router = Router()

    # Process tickets
    results = []
    for _, row in tickets.iterrows():
        summary = summarizer.summarize(row["description"])
        classification = classifier.classify(row["description"])
        team = router.route(classification)
        results.append({
            "ticket_id": row["ticket_id"],
            "description": row["description"],
            "summary": summary,
            "classification": classification,
            "assigned_team": team
        })

    # Save results
    df = pd.DataFrame(results)
    df.to_csv("../data/processed_tickets.csv", index=False)
    print("Processed tickets saved to data/processed_tickets.csv")

if __name__ == "__main__":
    main()
