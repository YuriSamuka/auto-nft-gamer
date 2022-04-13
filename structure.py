import pygetwindow as gw
import coordenadas as cord
import copy

def deckFormation(windowName, width = 1000, height = 730):
    # x = gw.getAllTitles();
    # AllWindows = gw.getAllWindows();
    # for i in range ( 0, len ( AllWindows)):
    #     AllWindows[i].minimize();
    ArrayScreens = gw.getWindowsWithTitle(windowName);
    tam = len (ArrayScreens);
    print (f'Size : Array de windows {tam}\n');

    # // 4k wide resolution
    deviceWidth = 3440
    deviceHeight = 1440

    Starting_x = int ( deviceWidth * 0.01 );
    Starting_y = int ( deviceHeight * 0.01 ) ;
    print(f'{Starting_x} {Starting_y}');
    k = copy.copy ( cord.k);

    for i in range (0, tam):
        cx = Starting_x + int ( i * k )
        cy = Starting_y + int ( i * k )
        ArrayScreens[i].minimize();
        ArrayScreens[i].maximize();
        ArrayScreens[i].restore();
        ArrayScreens[i].resizeTo(width, height);
        ArrayScreens[i].moveTo(cx, cy )

    print("deck formation performed!");
    return tam;




