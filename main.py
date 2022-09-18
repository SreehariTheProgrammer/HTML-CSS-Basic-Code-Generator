inp = input("Write the code for printing hello world in python for creating and writing the files: ")

a = "print('hello world')"
b = 'print("hello world")'

if inp.lower() == a or inp.lower() == b:
    with open("index.html", "w") as f:
        f.write("""<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="style.css">
        <link rel="shortcut icon" href="" type="image/x-icon">
        <title>Document</title>
    </head>
    <body>
        <!-- Your Code Here -->
    </body>
    </html>""")

    with open("style.css", "w") as f:
        f.write("""*{
        margin: 0;
        padding: 0;
        }""")

    print("Job Done Sir")
    input()

else:
    print("Wrong")
    print("I suggest you to try again.")
    input()