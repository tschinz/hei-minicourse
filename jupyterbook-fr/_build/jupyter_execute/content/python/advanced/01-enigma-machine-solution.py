#!/usr/bin/env python
# coding: utf-8

# # Enigma Virtual Machine Solution
# 
# ```{figure} ./resources/01-enigma_machine.jpg
# ---
# width: 50%
# name: Key Exchange
# ---
# Source: Wikipedia
# ```
# 
# [Enigma Machine](https://en.wikipedia.org/wiki/Enigma_machine) is the most powerful cipher machine used by Nazi Germany during the World War II. It has an electromechanical design which can scramble 26 Letters. When you press a button the corresponding light according to the enigma setting is lit up. It was invented by [Arthur Scherbius](https://en.wikipedia.org/wiki/Arthur_Scherbius) and [Richard Ritter](https://de.wikipedia.org/wiki/Ernst_Richard_Ritter).
# 
# If plain test is entered, it is encoded into ciphertext and if ciphertext is entered the plain text is displayed. The encryption is based on [Caesar Cipher](https://en.wikipedia.org/wiki/Caesar_cipher).  It is one of the simplest and most widely used encryption techniques. The Alphabet is shifted by $k$ which connects different letters together. This means for a given cipher the letters always correspond to each other.
# 
# ```{important}
#    Caesar cipher offers nowadays essentially no communication security.
# ```
# 
# ```{figure} ./resources/01-caesar_cipher.svg
# ---
# width: 40%
# name: Caesar Cipher
# ---
# Caesar Cipher with $k = 3$ Source: Wikipedia
# ```
# 
# ## Terminology
# 
# * **Steckerbrett** - "Plugboard" in front of the machine to connect two different letters together. This is an extra scramble layer
# * **Rotors** - located between the Plugboard and the Reflector, the three Rotors left, middle and right can be set to a given position to achieve a different scrambling
# * **Reflector** - The Reflector receives the signals from the left Rotor and sends it back to him, the Reflector scrambling can not be changed. It allows the machine to encode and decode without changing any settings.
# 
# ## Algorithm
# 
# The Enigma Machine works in a similar fashion with a more complex structure.
# 
# ```{figure} ./resources/01-enigma_diagram.jpg
# ---
# width: 80%
# name: Enigma Diagram
# ---
# Enigma Diagram Source: Louise Dade
# ```
# 
# ### Rotor and Reflector Types
# 
# During the time the enigma was used, many different versions with different rotors, reflectors existed. 
# 
# | Key      | Type             | Setup                      | Usage                         |
# |----------|------------------|----------------------------|-------------------------------|
# | `etw`    | Rotor ETW        | ABCDEFGHIJKLMNOPQRSTUVWXYZ | Enigma I                      |
# | `ic`     | Rotor IC         | DMTWSILRUYQNKFEJCAZBPGXOHV | 1924 Commercial Enigma A, B   |
# | `iic`    | Rotor IIC        | HQZGPJTMOBLNCIFDYAWVEUSRKX | 1924 Commercial Enigma A, B   |
# | `iic`    | Rotor IIIC       | UQNTLSZFMREHDPXKIBVYGJCWOA | 1924 Commercial Enigma A, B   |
# | `ik`     | Rotor I-K        | PEZUOHXSCVFMTBGLRINQJWAYDK | February 1939 Swiss K         |
# | `iik`    | Rotor II-K       | ZOUESYDKFWPCIQXHMVBLGNJRAT | February 1939 Swiss K         |
# | `iiik`   | Rotor III-K      | EHRVXGAOBQUSIMZFLYNWKTPDJC | February 1939 Swiss K         |
# | `ukwk`   | Rotor UKW-K      | IMETCGFRAYSQBZXWLHKDVUPOJN | February 1939 Swiss K         |
# | `etwk`   | Rotor ETW-K      | QWERTZUIOASDFGHJKPYXCVBNML | February 1939 Swiss K         |
# | `i`      | Rotor I          | EKMFLGDQVZNTOWYHXUSPAIBRCJ | 1930 Enigma I                 |
# | `ii`     | Rotor II         | AJDKSIRUXBLHWTMCQGZNPYFVOE | 1930 Enigma I                 |
# | `iii`    | Rotor III        | BDFHJLCPRTXVZNYEIWGAKMUSQO | 1930 Enigma I                 |
# | `iv`     | Rotor IV         | ESOVPZJAYQUIRHXLNFTGKDCMWB | December 1938 M3 Army         |
# | `v`      | Rotor V          | VZBRGITYUPSDNHLXAWMJQOFECK | December 1938 M3 Army         |
# | `vi`     | Rotor VI         | JPGVOUMFYQBENHZRDKASXLICTW | 1939 M3 & M4 Naval (FEB 1942) |
# | `vii`    | Rotor VII        | NZJHGRCXMYSWBOUFAIVLPEKQDT | 1939 M3 & M4 Naval (FEB 1942) |
# | `viii`   | Rotor VIII       | FKQHTLXOCBJSPDZRAMEWNIUYGV | 1939 M3 & M4 Naval (FEB 1942) |
# | `beta`   | Rotor Beta       | LEYJVCNIXWPBQMDRTAKZGFUHOS | Spring 1941 M4 R2             |
# | `gamma`  | Rotor Gamma      | FSOKANUERHMBTIYCWLQPZXVGJD | Spring 1942 M4 R2             |
# | `a`      | Reflector A      | EJMZALYXVBWFCRQUONTSPIKHGD |                               |
# | `b`      | Reflector B      | YRUHQSLDPXNGOKMIEBFZCWVJAT |                               |
# | `c`      | Reflector C      | FVPJIAOYEDRZXWGCTKUQSBNMHL |                               |
# | `bt`     | Reflector B Thin | ENKQAUYWJICOPBLMDXZVFTHRGS | 1940 M4 R1 (M3 + Thin)        |
# | `ct`     | Reflector C Thin | RDOBJNTKVEHMLFCWZAXGYIPSUQ | 1940 M4 R1 (M3 + Thin)        |
# | `custom` | Custom           | as given by the user       |                               |
# | `random` | Random           | ???                        |                               |
# 
# ### Setting
# 
# in order to decrypt was another machine encrypted the following needs to be true:
# * The same machine with the same number and types of rotors and reflector.
# * Plugboard settings needs to be the same
# * Same starting position of the rotors
# 
# All these informations were changed daily, the  exact setup could be found in a monthly issued `codesheet`.
# 
# ```{figure} ./resources/01-enigma_codesheet.jpg
# ---
# width: 80%
# name: Enigma Codesheet
# ---
# Codesheet WWII Source: Nazis
# ```

# ## Imports

# In[ ]:


import random


# ## Algorithm

# In[73]:


class Scrambler:
  def __init__(self, type_key: str = None, startpos: int = 0, custom: str = None):
    """Create a alphabet shuffle, this represents one rotor or a reflector. The configuration can be choosen from the first ever Enigma, the latest WWII Enigma machine, a Random pattern or a custom setting.
    The reflector and rotor settings are according to Wikipedia https://en.wikipedia.org/wiki/Enigma_rotor_details:

    Args:
        type_key (str): type of enigma rotor ["EI", "alpha", "beta", "gamma", "random", "custom"]
        startpos (int, optional): rotor startposition. Defaults to 0.
        custom (string, optional): string of chars representing the custom configuration. Defaults to None.
    """
    self.alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    # Possible rotor configurations
    self.configs = {
      "etw": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
      "ic" : "DMTWSILRUYQNKFEJCAZBPGXOHV",
      "iic" : "HQZGPJTMOBLNCIFDYAWVEUSRKX",
      "iiic": "UQNTLSZFMREHDPXKIBVYGJCWOA",
      "ik" : "PEZUOHXSCVFMTBGLRINQJWAYDK",
      "iik" : "ZOUESYDKFWPCIQXHMVBLGNJRAT",
      "iiik": "EHRVXGAOBQUSIMZFLYNWKTPDJC",
      "ikwk": "IMETCGFRAYSQBZXWLHKDVUPOJN",
      "etwk": "QWERTZUIOASDFGHJKPYXCVBNML",
      "i" : "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
      "ii": "AJDKSIRUXBLHWTMCQGZNPYFVOE",
      "iii": "BDFHJLCPRTXVZNYEIWGAKMUSQO",
      "iv": "ESOVPZJAYQUIRHXLNFTGKDCMWB",
      "v" : "VZBRGITYUPSDNHLXAWMJQOFECK",
      "vi" : "JPGVOUMFYQBENHZRDKASXLICTW",
      "vii" : "NZJHGRCXMYSWBOUFAIVLPEKQDT",
      "viii" : "FKQHTLXOCBJSPDZRAMEWNIUYGV",
      "beta": "LEYJVCNIXWPBQMDRTAKZGFUHOS",
      "gamma" : "FSOKANUERHMBTIYCWLQPZXVGJD",
      "a": "EJMZALYXVBWFCRQUONTSPIKHGD",
      "b" : "YRUHQSLDPXNGOKMIEBFZCWVJAT",
      "c": "FVPJIAOYEDRZXWGCTKUQSBNMHL",
      "bt" : "ENKQAUYWJICOPBLMDXZVFTHRGS",
      "ct"  : "RDOBJNTKVEHMLFCWZAXGYIPSUQ",
      "random": "ABCDEFGHIJKLMNOPQRSTUVWXYZ", # Will be scrambled later
    }

    self.type_key = type_key.lower().replace(" ", "").replace("_", "").replace("-", "")
    self.startpos = startpos

    # get the key
    if self.type_key == "custom":
      self.transformation = self.getConfig(custom)
    else:
      self.transformation = self.getConfig(self.configs[self.type_key])

    # additional scramble in case of random
    if self.type_key == "random":
      random.shuffle(self.transformation)

    # setup initial position of rotors
    self.transformation = self.rol(self.transformation, self.startpos)

    self.key = self.getKey()

  def getConfig(self, str_config: str):
    """Transforms the string configuration into an int array

    Args:
        str_config (str): string of configuration. All alphabet characters need to be represented.

    Returns:
        list: list of int representing the alphabet positions of the config
    """
    config = []
    for char in str_config:
      config.append(self.alphabet.index(char))
    return config

  def getKey(self):
    """Get the key of the current transformation config

    Returns:
        str: string of characters of the current config
    """
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    key = ""
    for idx in self.transformation:
      key += self.alphabet[idx]
    return key
  
  def rol(self,  string: str, n: int):
    """Rotating shift left of a string by n characters
       example: n=2
       "Test" => "stTe"
    Args:
        string (str): input string
        n (int): number of bits to shift

    Returns:
        str: string rotated shift left by n chars
    """
    return string[n:] + string[:n]

  def passthrough(self, idx: int):
    """Pass element through (index => element)

    Args:
        idx (int): index of character index to return

    Returns:
        int: new character index
    """
    return self.transformation[idx]

  def passthroughRev(self, elem):
    """Reverse Passthrough, enter character index and return list index

    Returns:
       int: index of character index
    """
    return self.transformation.index(elem)

  def rotate(self):
    """Rotate the rotors by one position
    """
    self.transformation = self.rol(self.transformation, 1)

  def setTransformation(self, transformation: list):
    """Set manually the tranformation. E.g. to reset the machine

    Args:
        transformation (list): transformation list to be used
    """
    self.transformation = transformation


class EnigmaMachine:
  def __init__(self, nb_rotors: int = 3, rotor_types: list = ["random, random, random"], rotor_startpos: list = [random.randint(0, 25), random.randint(0, 25), random.randint(0, 25)], rotor_custom_configs: list = None, reflector_type: str = "random", plugboard_config = None, print_specialchars: bool = False):
    """Enigma Virtual Machine
        nb_rotors (int, optional): number of rotors in the machine. Defaults to 3.
        rotor_types (list, optional): list of types rotors types ["etw"|"ic"|"iic"|"iiic"|"ik"|"iik"|"iiik"|"ikwk"|"etwk"|"i"|"ii"|"iii"|"iv"|"v"|"vi"|"vii"|"viii"|"beta"|"gamma"|"random""custom"]. Needs to be size of nb_rotors. Defaults to ["random", "random", "random"].
        rotor_startpos (list, optional): list of int representing thestart positions of the rotors. Needs to be the size of nb_rotors. Defaults to three random numbers between 0 -> 25.
        rotor_custom_configs (list, optional): list of int lists representing the custom rotor configuration, only needed if "custom" type is choosen. Needs to be the size of nb_rotors if used. Defaults to None
        reflector_type (str, optional): type of reflector ["a"|"b"|"c"|"bt"|"ct"|"random"]. Defaults to "random".
        plugboard_config (list, optional): list of character combinations. Defaults to Nonee will result in A<->Z, B<->Y, ...
        print_specialchars (bool, optional): Print characters missing by enigma. Defaults to False.
    """
    self.nb_rotors = nb_rotors
    self.rotor_types = rotor_types
    self.rotor_startpos = rotor_startpos
    self.rotor_custom_configs = rotor_custom_configs
    self.reflector_type = reflector_type
    self.printspecialchars = print_specialchars
    if plugboard_config is None:
      self.plugboard_config = ["AZ", "BY", "CX", "DW", "EV", "FU", "GT", "HS", "IR", "JQ", "KP", "LO", "MN"]
    else:
      self.plugboard_config = plugboard_config

    # create the rotors and reflector
    self.rotors = []
    self.original_rotors = []
    self.reflector = None
    self.plugboard = None

    self.setupRotors()
    self.setupReflector()
    self.setupPlugboard()

  def setupRotors(self):
    """Setup the rotors configuration
    """
    for i in range(self.nb_rotors):
      if self.rotor_custom_configs is None:
        self.rotors.append(Scrambler(self.rotor_types[i], self.rotor_startpos[i]))
      else:
        self.rotors.append(Scrambler(self.rotor_types[i], self.rotor_startpos[i], self.rotor_custom_configs[i]))
      self.original_rotors.append(self.rotors[i].transformation)

  def setupReflector(self):
    """Setup the reflector
    """
    self.reflector = Scrambler(self.reflector_type)

  def setupPlugboard(self):
    """Setup the plugboard"""
    # Transform into scrambler key
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    key = " " * 26
    for elem in self.plugboard_config:
      key = key[:alphabet.index(elem[0])] + elem[1] + key[alphabet.index(elem[0])+1:]
      key = key[:alphabet.index(elem[1])] + elem[0] + key[alphabet.index(elem[1])+1:]

    self.plugboard = Scrambler("custom", 0, key)

  def printEnigmaSetup(self):
    """Print Enigma setup of plugboard, rotors and reflector
    """
    print("Enigma Setup")
    print("============\n")

    for i in range(self.nb_rotors):
      print("* Rotor {}".format(i))
      print("  - Type      : {}".format(self.rotors[i].type_key))
      print("  - Key       : {}".format(self.rotors[i].key))
      print("  - StartPos  : {}".format(self.rotors[i].startpos))
      
    print("* Reflector")
    print("  - Type      : {}".format(self.reflector.type_key))
    if self.reflector.type_key == "custom" or self.reflector.type_key == "random":
      print("  - Key       : {}".format(self.reflector.key))
      print("  - StartPos  : {}".format(self.reflector.startpos))

    print("* Plugboard")
    print("  - Key       : {}".format(self.plugboard_config))

  def reset(self):
    """Restart the original rotor start positions
    """
    for i in range(0, self.nb_rotors):
      self.rotors[i].setTransformation(self.original_rotors[i])

  def encode(self, text: str):
    """Encode and decode a string

    Args:
        text (str): string to encode

    Returns:
        str : depending on the input string, the encoded or decoded output
    """
    ln = 0
    encrypted_text = ""
    for l in text.lower():
      # get char position in alphabet
      num = ord(l) % 97
      if (num > 25 or num < 0):
        # Special character
        if (self.printspecialchars):
          encrypted_text += l
      else:
        # encodable character
        ln += 1

        # pass through plugboard
        num = self.plugboard.passthrough(num)
        
        # pass through rotors
        for i in range(0, self.nb_rotors):
          num = self.rotors[i].passthrough(num)

        # reflected by the reflector
        num = self.reflector.passthrough(num)

        # pass through rotors from the other side
        for i in range(0, self.nb_rotors):
          num = self.rotors[self.nb_rotors - i - 1].passthroughRev(num)

        # pass through plugboard from the other side
        num = self.plugboard.passthroughRev(num)
    
        # Encode character
        encrypted_text += "" + chr(97 + num)

        # rotate the rotors
        for i in range(0, self.nb_rotors):
          if (ln % ((i * 6) + 1) == 0):
            self.rotors[i].rotate()
    return encrypted_text


# ## Test

# In[74]:


plaintext = """The Enigma machines were a series of electro-mechanical rotor cipher machines developed and used in the early- to mid-20th century to protect commercial, 
diplomatic and military communication. Enigma was invented by the German engineer Arthur Scherbius at the end of World War I. 
Early models were used commercially from the early 1920s, and adopted by military and government services of several countries, 
most notably Nazi Germany before and during World War II. Several different Enigma models were produced, 
but the German military models, having a plugboard, were the most complex. Japanese and Italian models were also in use."""
enigma = EnigmaMachine(nb_rotors=3, rotor_types=["i","beta","gamma"], rotor_startpos=[17,23,12], reflector_type="a", print_specialchars=True)
enigma.printEnigmaSetup()

print("\nPlaintext:\n{}\n".format(plaintext))

# Encrypt
enigma.reset()
encrypted_text = enigma.encode(plaintext)
print("Encrypted text:\n{}\n".format(encrypted_text))

# Decrypt
enigma.reset()
plaintext = enigma.encode(encrypted_text)
print("Plaintext:\n{}".format(plaintext))

