This is a program to automate dino game. Basically this program automates the system.
Dependendies used in this programs:
    <ul>
        <li>- cv2 (library from opencv.) - Open source python package.</li>
        <li>- mediapipe - Hand detection model</li>
        <li>- pyaautogui - Library to automate system</li>
    </ul>
Install these packages for run the code.
run the setup.sh file fisrt.
if that file not works, see the requirements.txt file and install them one by one.

working:
    open chrome and direct to chrome dino game. 
    No problem if the network is connected, follow the link chrome://dino/ 
    (Working on full automation)
    After opening the game, run the code and go back to chrome. 
    A camera window will popup and you can show your hand in cam. 
    Open your hand to keydown space key.
    Close your hand to keydown space key.
    Note that this code is automating the system. Even if the chrome is not open,
    and if the code is running and closed hand is detected, it presses space key.
