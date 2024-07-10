from generator import generate_offer

# Read the request to generate a new offer.
def cmd():
    while True:
        message = input("\nIntrodu o solicitare de proiect: ")

        if message == "exit":
            break

        generate_offer(message)

        print("Offert generated!")

cmd()