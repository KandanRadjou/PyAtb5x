browser_name = input("enter the browser name\n")
match browser_name:
    case "firefox":
        print("Starting firefox")
    case "chrome":
        print("starting chrome")
    case "edge":
        print("starting edge")
    case "safari":
        print("starting safari")
    case _:
        print("browser not found")
