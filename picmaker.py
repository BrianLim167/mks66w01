def yes():
    filename = "picmaker.ppm"
    wopen = open(filename,'w')
    wopen.write('''P3
    500 500
    255
    ''')
    wopen.close()

    aopen = open(filename,'a')
    grid = ""
    for i in range(500):
        for j in range(500):
            grid += "125 125 255 "
        grid += '\n'
    aopen.write(grid)
    aopen.close()
        

if (__name__ == "__main__"):
    yes()
