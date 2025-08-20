class Router:
    def __init__(self):
        self.rules = {
            "Network Issue": "Network Team",
            "Hardware Issue": "IT Hardware Team",
            "Software Issue": "App Support Team",
            "Critical": "Incident Response Team",
            "Low Priority": "Helpdesk"
        }

    def route(self, classification):
        return self.rules.get(classification, "General Support")


if __name__ == "__main__":
    r = Router()
    print(r.route("Network Issue"))
