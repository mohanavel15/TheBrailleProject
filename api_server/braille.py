
brailleToEnglishDict = {
 '100000': 'a',
 '110000': 'b',
 '100100': 'c',
 '100110': 'd',
 '100010': 'e',
 '110100': 'f',
 '110110': 'g',
 '110010': 'h',
 '010100': 'i',
 '010110': 'j',
 '101000': 'k',
 '111000': 'l',
 '101100': 'm',
 '101110': 'n',
 '101010': 'o',
 '111100': 'p',
 '111110': 'q',
 '111010': 'r',
 '011100': 's',
 '011110': 't',
 '101001': 'u',
 '111001': 'v',
 '010111': 'w',
 '101101': 'x',
 '101111': 'y',
 '101011': 'z',
 '000001': "capflag",
 '001111': '#',
 '000000': ' ',
 '010011': '.',
 '010000': ',',
 '011001': '?',
 '011000': ';',
 '011010': '!',
 '001011': '"', #closing quote
 '100000_': '1',
 '110000_': '2',
 '100100_': '3',
 '100110_': '4',
 '100010_': '5',
 '110100_': '6',
 '110110_': '7',
 '110010_': '8',
 '101100_': '9',
 '010110_': '0',
}
englishToBrailleDict = {value: key for key, value in brailleToEnglishDict.items()}

tamilToBrailleDict = {
    '=': '011011',
    '+': '011010_',
    '-': '010010_',
    ' ': '000000',
    '.': '010011',
    ',': '010000',
    '?': '011001',
    ';': '011000',
    '!': '011010',
    '"': '001011',
    'ஜ': '010110',
    'ஸ': '011100',
    'ஷ': '111101',
    'ஹ': '110010',
    'க்ஷ': '111110',
    'அ': '100000',
    'ஆ': '001110',
    'இ': '010100',
    'ஈ': '001010',
    'உ': '101001',
    'ஊ': '110011',
    'எ': '010001',
    'ஏ': '100010',
    'ஐ': '001100',
    'ஒ': '101101',
    'ஓ': '101010',
    'ஔ': '010101',
    'க': '101000',
    'ங': '001101',
    'ச': '100100',
    'ஞ': '010010',
    'ட': '011111',
    'ண': '001111',
    'த': '011110',
    'ந': '101110',
    'ப': '111100',
    'ம': '101100',
    'ய': '101111',
    'ர': '111010',
    'ல': '111000',
    'வ': '111001',
    'ழ': '111011',
    'ள': '000111',
    'ற': '110111',
    'ன': '000011',
    '்': '000011_',
    'ா': '001110_',
    'ி': '010100_',
    'ீ': '001010_',
    'ு': '101001_',
    'ூ': '110011_',
    'ெ': '010001_',
    'ே': '100010_',
    'ை': '001100_',
    'ொ': '101101_',
    'ோ': '101010_',
    'ௌ': '010101_',
    '1' : '100000_',
    '2' : '110000_',
    '3' : '100100_',
    '4' : '100110_',
    '5' : '100010_',
    '6' : '110100_',
    '7' : '110110_',
    '8' : '110010_',
    '9' : '101100_',
    '0' : '010110_',
}

brailleToTamilDict = {value: key for key, value in tamilToBrailleDict.items()}

def para_to_braille(para,refDict):
    output_string = ''
    for c in para:
        if c in refDict:
            char = refDict[c.lower()]
            if char[-1] == "_":
                char=char[:-1]
            val = int(char[::-1], 2)
            toadd = chr(int(hex(10240+val), 16))
        else:
            toadd = c
        output_string = output_string+toadd
    return output_string