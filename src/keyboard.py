
from math import sqrt

ALPHABET = "abcdefghijklmnopqrstuvwxyz"
DEFAULT_DNA = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
DNA_LEN = 26

# pre-calculated distances into single lookup table
DISTANCES = [[0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 1.0307764064044151, 1.6007810593582121, 2.462214450449026, 3.400367627183861, 4.366062299143245, 5.344389581607987, 6.329494450586082, 7.318640584152224, 8.31038506929733, 2.1360009363293826, 2.6575364531836625, 3.400367627183861, 4.25, 5.153882032022076, 6.0878978309429606, 7.0400639201643616], [1.0, 0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 1.25, 1.0307764064044151, 1.6007810593582121, 2.462214450449026, 3.400367627183861, 4.366062299143245, 5.344389581607987, 6.329494450586082, 7.318640584152224, 2.0155644370746373, 2.1360009363293826, 2.6575364531836625, 3.400367627183861, 4.25, 5.153882032022076, 6.0878978309429606], [2.0, 1.0, 0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 2.0155644370746373, 1.25, 1.0307764064044151, 1.6007810593582121, 2.462214450449026, 3.400367627183861, 4.366062299143245, 5.344389581607987, 6.329494450586082, 2.358495283014151, 2.0155644370746373, 2.1360009363293826, 2.6575364531836625, 3.400367627183861, 4.25, 5.153882032022076], [3.0, 2.0, 1.0, 0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 2.9261749776799064, 2.0155644370746373, 1.25, 1.0307764064044151, 1.6007810593582121, 2.462214450449026, 3.400367627183861, 4.366062299143245, 5.344389581607987, 3.010398644698074, 2.358495283014151, 2.0155644370746373, 2.1360009363293826, 2.6575364531836625, 3.400367627183861, 4.25], [4.0, 3.0, 2.0, 1.0, 0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 3.881043674065006, 2.9261749776799064, 2.0155644370746373, 1.25, 1.0307764064044151, 1.6007810593582121, 2.462214450449026, 3.400367627183861, 4.366062299143245, 3.816084380618437, 3.010398644698074, 2.358495283014151, 2.0155644370746373, 2.1360009363293826, 2.6575364531836625, 3.400367627183861], [5.0, 4.0, 3.0, 2.0, 1.0, 0.0, 1.0, 2.0, 3.0, 4.0, 4.8541219597369, 3.881043674065006, 2.9261749776799064, 2.0155644370746373, 1.25, 1.0307764064044151, 1.6007810593582121, 2.462214450449026, 3.400367627183861, 4.697073557013984, 3.816084380618437, 3.010398644698074, 2.358495283014151, 2.0155644370746373, 2.1360009363293826, 2.6575364531836625], [6.0, 5.0, 4.0, 3.0, 2.0, 1.0, 0.0, 1.0, 2.0, 3.0, 5.836308764964376, 4.8541219597369, 3.881043674065006, 2.9261749776799064, 2.0155644370746373, 1.25, 1.0307764064044151, 1.6007810593582121, 2.462214450449026, 5.618051263561058, 4.697073557013984, 3.816084380618437, 3.010398644698074, 2.358495283014151, 2.0155644370746373, 2.1360009363293826], [7.0, 6.0, 5.0, 4.0, 3.0, 2.0, 1.0, 0.0, 1.0, 2.0, 6.823672031978091, 5.836308764964376, 4.8541219597369, 3.881043674065006, 2.9261749776799064, 2.0155644370746373, 1.25, 1.0307764064044151, 1.6007810593582121, 6.562202374203344, 5.618051263561058, 4.697073557013984, 3.816084380618437, 3.010398644698074, 2.358495283014151, 2.0155644370746373], [8.0, 7.0, 6.0, 5.0, 4.0, 3.0, 2.0, 1.0, 0.0, 1.0, 7.814249804043892, 6.823672031978091, 5.836308764964376, 4.8541219597369, 3.881043674065006, 2.9261749776799064, 2.0155644370746373, 1.25, 1.0307764064044151, 7.520804478245662, 6.562202374203344, 5.618051263561058, 4.697073557013984, 3.816084380618437, 3.010398644698074, 2.358495283014151], [9.0, 8.0, 7.0, 6.0, 5.0, 4.0, 3.0, 2.0, 1.0, 0.0, 8.806957476904268, 7.814249804043892, 6.823672031978091, 5.836308764964376, 4.8541219597369, 3.881043674065006, 2.9261749776799064, 2.0155644370746373, 1.25, 8.488963423174823, 7.520804478245662, 6.562202374203344, 5.618051263561058, 4.697073557013984, 3.816084380618437, 3.010398644698074], [1.0307764064044151, 1.25, 2.0155644370746373, 2.9261749776799064, 3.881043674065006, 4.8541219597369, 5.836308764964376, 6.823672031978091, 7.814249804043892, 8.806957476904268, 0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 1.118033988749895, 1.8027756377319946, 2.692582403567252, 3.640054944640259, 4.6097722286464435, 5.5901699437494745, 6.576473218982953], [1.6007810593582121, 1.0307764064044151, 1.25, 2.0155644370746373, 2.9261749776799064, 3.881043674065006, 4.8541219597369, 5.836308764964376, 6.823672031978091, 7.814249804043892, 1.0, 0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 1.118033988749895, 1.118033988749895, 1.8027756377319946, 2.692582403567252, 3.640054944640259, 4.6097722286464435, 5.5901699437494745], [2.462214450449026, 1.6007810593582121, 1.0307764064044151, 1.25, 2.0155644370746373, 2.9261749776799064, 3.881043674065006, 4.8541219597369, 5.836308764964376, 6.823672031978091, 2.0, 1.0, 0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 1.8027756377319946, 1.118033988749895, 1.118033988749895, 1.8027756377319946, 2.692582403567252, 3.640054944640259, 4.6097722286464435], [3.400367627183861, 2.462214450449026, 1.6007810593582121, 1.0307764064044151, 1.25, 2.0155644370746373, 2.9261749776799064, 3.881043674065006, 4.8541219597369, 5.836308764964376, 3.0, 2.0, 1.0, 0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 2.692582403567252, 1.8027756377319946, 1.118033988749895, 1.118033988749895, 1.8027756377319946, 2.692582403567252, 3.640054944640259], [4.366062299143245, 3.400367627183861, 2.462214450449026, 1.6007810593582121, 1.0307764064044151, 1.25, 2.0155644370746373, 2.9261749776799064, 3.881043674065006, 4.8541219597369, 4.0, 3.0, 2.0, 1.0, 0.0, 1.0, 2.0, 3.0, 4.0, 3.640054944640259, 2.692582403567252, 1.8027756377319946, 1.118033988749895, 1.118033988749895, 1.8027756377319946, 2.692582403567252], [5.344389581607987, 4.366062299143245, 3.400367627183861, 2.462214450449026, 1.6007810593582121, 1.0307764064044151, 1.25, 2.0155644370746373, 2.9261749776799064, 3.881043674065006, 5.0, 4.0, 3.0, 2.0, 1.0, 0.0, 1.0, 2.0, 3.0, 4.6097722286464435, 3.640054944640259, 2.692582403567252, 1.8027756377319946, 1.118033988749895, 1.118033988749895, 1.8027756377319946], [6.329494450586082, 5.344389581607987, 4.366062299143245, 3.400367627183861, 2.462214450449026, 1.6007810593582121, 1.0307764064044151, 1.25, 2.0155644370746373, 2.9261749776799064, 6.0, 5.0, 4.0, 3.0, 2.0, 1.0, 0.0, 1.0, 2.0, 5.5901699437494745, 4.6097722286464435, 3.640054944640259, 2.692582403567252, 1.8027756377319946, 1.118033988749895, 1.118033988749895], [7.318640584152224, 6.329494450586082, 5.344389581607987, 4.366062299143245, 3.400367627183861, 2.462214450449026, 1.6007810593582121, 1.0307764064044151, 1.25, 2.0155644370746373, 7.0, 6.0, 5.0, 4.0, 3.0, 2.0, 1.0, 0.0, 1.0, 6.576473218982953, 5.5901699437494745, 4.6097722286464435, 3.640054944640259, 2.692582403567252, 1.8027756377319946, 1.118033988749895], [8.31038506929733, 7.318640584152224, 6.329494450586082, 5.344389581607987, 4.366062299143245, 3.400367627183861, 2.462214450449026, 1.6007810593582121, 1.0307764064044151, 1.25, 8.0, 7.0, 6.0, 5.0, 4.0, 3.0, 2.0, 1.0, 0.0, 7.566372975210778, 6.576473218982953, 5.5901699437494745, 4.6097722286464435, 3.640054944640259, 2.692582403567252, 1.8027756377319946], [2.1360009363293826, 2.0155644370746373, 2.358495283014151, 3.010398644698074, 3.816084380618437, 4.697073557013984, 5.618051263561058, 6.562202374203344, 7.520804478245662, 8.488963423174823, 1.118033988749895, 1.118033988749895, 1.8027756377319946, 2.692582403567252, 3.640054944640259, 4.6097722286464435, 5.5901699437494745, 6.576473218982953, 7.566372975210778, 0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0], [2.6575364531836625, 2.1360009363293826, 2.0155644370746373, 2.358495283014151, 3.010398644698074, 3.816084380618437, 4.697073557013984, 5.618051263561058, 6.562202374203344, 7.520804478245662, 1.8027756377319946, 1.118033988749895, 1.118033988749895, 1.8027756377319946, 2.692582403567252, 3.640054944640259, 4.6097722286464435, 5.5901699437494745, 6.576473218982953, 1.0, 0.0, 1.0, 2.0, 3.0, 4.0, 5.0], [3.400367627183861, 2.6575364531836625, 2.1360009363293826, 2.0155644370746373, 2.358495283014151, 3.010398644698074, 3.816084380618437, 4.697073557013984, 5.618051263561058, 6.562202374203344, 2.692582403567252, 1.8027756377319946, 1.118033988749895, 1.118033988749895, 1.8027756377319946, 2.692582403567252, 3.640054944640259, 4.6097722286464435, 5.5901699437494745, 2.0, 1.0, 0.0, 1.0, 2.0, 3.0, 4.0], [4.25, 3.400367627183861, 2.6575364531836625, 2.1360009363293826, 2.0155644370746373, 2.358495283014151, 3.010398644698074, 3.816084380618437, 4.697073557013984, 5.618051263561058, 3.640054944640259, 2.692582403567252, 1.8027756377319946, 1.118033988749895, 1.118033988749895, 1.8027756377319946, 2.692582403567252, 3.640054944640259, 4.6097722286464435, 3.0, 2.0, 1.0, 0.0, 1.0, 2.0, 3.0], [5.153882032022076, 4.25, 3.400367627183861, 2.6575364531836625, 2.1360009363293826, 2.0155644370746373, 2.358495283014151, 3.010398644698074, 3.816084380618437, 4.697073557013984, 4.6097722286464435, 3.640054944640259, 2.692582403567252, 1.8027756377319946, 1.118033988749895, 1.118033988749895, 1.8027756377319946, 2.692582403567252, 3.640054944640259, 4.0, 3.0, 2.0, 1.0, 0.0, 1.0, 2.0], [6.0878978309429606, 5.153882032022076, 4.25, 3.400367627183861, 2.6575364531836625, 2.1360009363293826, 2.0155644370746373, 2.358495283014151, 3.010398644698074, 3.816084380618437, 5.5901699437494745, 4.6097722286464435, 3.640054944640259, 2.692582403567252, 1.8027756377319946, 1.118033988749895, 1.118033988749895, 1.8027756377319946, 2.692582403567252, 5.0, 4.0, 3.0, 2.0, 1.0, 0.0, 1.0], [7.0400639201643616, 6.0878978309429606, 5.153882032022076, 4.25, 3.400367627183861, 2.6575364531836625, 2.1360009363293826, 2.0155644370746373, 2.358495283014151, 3.010398644698074, 6.576473218982953, 5.5901699437494745, 4.6097722286464435, 3.640054944640259, 2.692582403567252, 1.8027756377319946, 1.118033988749895, 1.118033988749895, 1.8027756377319946, 6.0, 5.0, 4.0, 3.0, 2.0, 1.0, 0.0]]

def gen_distances():
    """
    done beforehand, copied result, pasted directly into code to reduce computation time for later runs
    distances between left-right adjacent keys is 1
    Euclidean distance measured between centers of keys
    """

    coords = {}

    for i in range(10):  # qwertyuiop
        coords[i] = (i, 2)

    for i in range(10, 19):
        coords[i] = (i - 10 + 0.25, 1)

    for i in range(19, 26):
        coords[i] = (i - 19 + 0.75, 0)

    def distance(p1, p2):
        return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

    distances = [] # 676 distances

    for i in range(26):
        distances_row = []
        for j in range(26):
            # I am aware that this generates duplicates because distance(a, b) = distance(b, a)
            distances_row.append(distance(coords[i], coords[j]))
        distances.append(distances_row)

    return distances


class Keyboard:
    """
    dna encodes the keyboard
    index in the array corresponds to the letter (a = 0, ..., z = 25)
    value at index corresponds to position of letter on keyboard in the order qwertyuiop asdfghjkl zxcvbnm
    """

    def __init__(self, dna=None):
        if dna == None:
            self.dna = DEFAULT_DNA.copy()
        else:
            self.dna = dna

    def pos(self, letter):
        return self.dna[letter]

    def draw(self):
        print("[{0}][{1}][{2}][{3}][{4}][{5}][{6}][{7}][{8}][{9}]\n [{10}][{11}][{12}][{13}][{14}][{15}][{16}][{17}][{18}]\n  [{19}][{20}][{21}][{22}][{23}][{24}][{25}]"""
        .format(*(list(map(lambda x: chr(x + 97), self.dna)))))