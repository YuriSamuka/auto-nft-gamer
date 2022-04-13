import pyautogui
import time
import coordenadas as c
import math
import copy

def mult ( array , number ):
    
    d = number - 8;
    temp = copy.copy ( array );
    somaX = d * int ( copy.copy( c.k) );
    somaY = d * int ( copy.copy( c.k) );

    temp[0] += somaX;
    temp[1] += somaY;
    return temp;

def Click(target):
    pyautogui.moveTo( target[0], target[1] );
    pyautogui.click()
    return None;

def wakeup( number ):
    green = copy.copy( c.green);
    center = copy.copy( c.center);
    boneco = copy.copy( c.boneco);
    workall = copy.copy( c.workall);
    x = copy.copy ( c.x);

    green = mult ( green, number);
    center = mult ( center, number );
    boneco = mult ( boneco, number );
    workall = mult ( workall, number );
    x = mult ( x, number );

    Click(center );
    time.sleep(3);
    Click(boneco );
    time.sleep(3);
    Click(boneco );
    time.sleep(5);
    Click(workall);
    time.sleep(5);
    Click(x );
    time.sleep(3);
    Click(center );
    time.sleep(5);

    print("Tds trabalhando...");
    return None;

def shake(number ):
    green = copy.copy( c.green);
    center = copy.copy( c.center);

    green = mult ( green, number);
    center = mult ( center, number );

    Click(center );
    time.sleep (5);
    Click(green );
    time.sleep(3);
    Click(center );
    time.sleep (4);
    return None;