import webbrowser
file = open('helloworld.html', 'w' )

msg = """<html>
    <head> 
         <title>Hello World</title>
    </head>
    
    <body>
         <p>Hello World</p>
    </body>
</html>
"""
file.write(msg)
file.close()
webbrowser.open("C:/Users/jaysh/Desktop/pythonnew/helloworld.html")
