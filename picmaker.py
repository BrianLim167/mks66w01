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
    r = 0
    g = 0
    b = 0
    for i in range(500):
        for j in range(500):
            r = (0.2 * (i-150) ** 2 + 0.05 * (j-350) ** 2) // 1 % 255 
            g = (0.4 * (i-250) - 0.3 * (j-250) ** 2) // 1 % 255 
            if (j == 300):
                b = 0
            else:
                b = (0.4 * (i-400) - 400 * (j-300) ** -1) // 1 % 255
            grid += "%d %d %d " % (r, g, b) 
        grid += '\n'
    aopen.write(grid)
    aopen.close()
        

if (__name__ == "__main__"):
    yes()
