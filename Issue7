import webbrowser
import random
def color():
    r = lambda: random.randint(0, 255)
    return('#%02X%02X%02X' % (r(),r(),r()))
num = (int)(input('Enter a number: '))
msg = """<p style='color:{};'>hello world</p> """
print ("number read from file : " + str(num))
f = open('issue7.html', 'w')
for i in range(0, num):
	#print (msg)
	f.write(msg.format(color()))
f.close()
webbrowser.open("C:/Users/jaysh/Desktop/pythonnew/issue7.html")
