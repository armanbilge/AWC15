import sys
import subprocess
input()
for i, l in enumerate(map(str.strip, sys.stdin)):
    x, y, z = map(float, l.split())
    open('trajectory_{}.tex'.format(i), 'w').write("""\\documentclass{beamer}
\\usepackage{tikz,pgfplots}
\\usepackage[active,tightpage]{preview}
\\PreviewEnvironment{tikzpicture}
\\begin{document}
            \\begin{frame}
                    \centering
                    \\begin{tikzpicture}
                        \\begin{scope}[scale=0.5,shift={(-5,3)}]""" +
                        '\\draw [line width=0.5mm] (0,0) -- (0,{y2});'.format(y2=2*y) +
                        '\\draw [line width=0.5mm] (2,0) -- (2,{y2});'.format(y2=2*y) +
                        '\\draw [line width=0.5mm] (0,{y2}) -- (2,{y2});'.format(y2=2*y) +
                        '\\draw [line width=0.5mm] (1,{y2}) -- (1,{ypx2});'.format(y2=2*y, ypx2=2*(y+x)) +
                        '\\draw [line width=0.5mm] (4,0) -- (4,{ypx2});'.format(ypx2=2*(y+x)) +
                        '\\draw [line width=0.5mm] (1,{ypx2}) -- (4,{ypx2});'.format(ypx2=2*(y+x)) +
                        '\\draw [line width=0.5mm] (2.5,{ypx2}) -- (2.5,{ypx2p1});'.format(ypx2=2*(y+x), ypx2p1=2*(y+x)+1) +
                    """\end{scope}

                \\begin{axis}[colormap/greenyellow,
                         mesh/interior colormap={graygray}{color=(gray) color=(gray)},
                         view={72}{32},
                         xticklabels={,,},
                         yticklabels={,,},
                         zticklabels={,,}
                         ]
                \\addplot3[surf] table {surface.dat};
""" +
   '\\addplot3[red, mark=*, mark size=1] ' + str((x,y,z)) + ';'
    + """\\end{axis}
    \\end{tikzpicture}
    \\end{frame}
    \\end{document}
    """)
#    subprocess.run(('pdflatex', 'trajectory_{}.tex'.format(i)), stdout=None)
    # print('\\only<+->{\\addplot3[red, mark=*, mark size=1]', tuple(map(float, l.split())), ';}')
