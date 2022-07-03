# > 3.10

status = 400

match status:
    case 100:
        print("Continue")
    case 200:
        print("OK")
    case 300:
        print("Multiple Choices")
    case _:
        print("status not handled")