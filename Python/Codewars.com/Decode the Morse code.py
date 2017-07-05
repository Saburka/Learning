def decodeMorse(morseCode):
    MORSE_CODE['space'] = ' '  
    morseCode = morseCode.strip().replace('   ',' space ')
    morseCode = morseCode.split()
    return ''.join([MORSE_CODE[code] for code in morseCode])
