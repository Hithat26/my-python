started = False
while True:
    command = input(">").lower()
    if command == "help":
        print("start - to start the car")
        print("stop - to stop the car")
        print("quit - to exit")
    elif command == "start" and not started:
        print("Car started...Ready to go!")
        started = True
    elif command == "start" and started:
        print("Car has already started!")
    elif command == "stop" and started:
        print("Car stopped.")
        started = False
    elif command == "stop" and not started:
        print("Car has already stopped!")
    elif command == "quit":
        break
    else:
        print("I don't understand that...")