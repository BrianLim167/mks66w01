def yes():
    filename = "picmaker.ppm"
    wopen = open(filename,'w')
    wopen.write('''P3
    500 500
    255
    ''')
    wopen.close()

    aopen = open(filename,'a')
    for i in range(500):
        for j in range(500):
            aopen.write("255 125 0 ")
        aopen.write('\n')
        

if (__name__ == "__main__"):
    yes()
