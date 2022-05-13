// >>>>>  T-I-N-Y  S-P-A-C-E   I-N-V-A-D-E-R-S for ATTINY85  GPL v3 <<<<
//                  Programmer: Daniel Champagne 2018
//                 Contact EMAIL: phoenixbozo@gmail.com
//           https://sites.google.com/view/arduino-collection

//  Tiny Space Invaders is free software: you can redistribute it and/or modify
//  it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.

//  This program is distributed in the hope that it will be useful,
//  but WITHOUT ANY WARRANTY; without even the implied warranty of
//  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
//  GNU General Public License for more details.

//  You should have received a copy of the GNU General Public License
// along with this program.  If not, see <http://www.gnu.org/licenses/>.

// the code work at 16MHZ internal
// and use ssd1306xled Library for SSD1306 oled display 128x64
#include <avr/pgmspace.h>

typedef struct SPACE
{
  int8_t UFOxPos = -120;
  uint8_t oneFrame = 0;
  uint8_t MonsterShoot[2][1] = {{16}, {16}};
  int8_t MonsterGrid[5][6] = {{0, 0, 0, 0, 0, 0}, {2, 2, 2, 2, 2, 2}, {4, 4, 4, 4, 4, 4}, {4, 4, 4, 4, 4, 4}, {-1, -1, -1, -1, -1, -1}};
  uint8_t Shield[6] = {0b11111111, 0b11111111, 0b11111111, 0b11111111, 0b11111111, 0b11111111};
  uint8_t ScrBackV = 52;
  int8_t MyShootBall = -1;
  uint8_t MyShootBallxpos = 0;
  uint8_t MyShootBallFrame = 0;
  uint8_t anim = 0;
  uint8_t frame = 0;
  uint8_t PositionDansGrilleMonsterX = 0;
  uint8_t PositionDansGrilleMonsterY = 0;
  uint8_t MonsterFloorMax = 3;
  uint8_t MonsterOffsetGauche = 0;
  uint8_t MonsterOffsetDroite = 44;
  uint8_t MonsterGroupeXpos = 0;
  uint8_t MonsterGroupeYpos = 0;
  uint8_t DecalageY8 = 0;
  uint8_t frameMax = 8;
  uint8_t Direction = 1; // 1 right 0 gauche
} SPACE;

const int8_t MonstersLevels[] PROGMEM = {
    0,
    0,
    0,
    0,
    0,
    0,
    2,
    2,
    2,
    2,
    2,
    2,
    4,
    4,
    4,
    4,
    4,
    4,
    4,
    4,
    4,
    4,
    4,
    4,
    4,
    4,
    4,
    4,
    4,
    4,
    4,
    2,
    0,
    0,
    2,
    4,
    4,
    2,
    0,
    0,
    2,
    4,
    4,
    4,
    4,
    4,
    4,
    4,
    -1,
    0,
    0,
    0,
    0,
    -1,
    2,
    2,
    2,
    2,
    2,
    2,
    4,
    4,
    4,
    4,
    4,
    4,
    -1,
    4,
    4,
    4,
    4,
    -1,
    0,
    -1,
    0,
    0,
    -1,
    0,
    2,
    -1,
    2,
    2,
    -1,
    2,
    4,
    -1,
    4,
    4,
    -1,
    4,
    4,
    -1,
    4,
    4,
    -1,
    4,
    -1,
    -1,
    2,
    2,
    -1,
    -1,
    0,
    2,
    2,
    2,
    2,
    0,
    2,
    4,
    2,
    2,
    4,
    2,
    2,
    -1,
    -1,
    -1,
    -1,
    2,
    4,
    4,
    4,
    4,
    4,
    4,
    2,
    2,
    2,
    2,
    2,
    2,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    -1,
    0,
    0,
    0,
    0,
    -1,
    2,
    -1,
    -1,
    -1,
    -1,
    2,
    4,
    -1,
    -1,
    -1,
    -1,
    4,
    -1,
    4,
    4,
    4,
    4,
    -1,
    4,
    -1,
    4,
    -1,
    4,
    -1,
    -1,
    4,
    -1,
    4,
    -1,
    4,
    4,
    -1,
    4,
    -1,
    4,
    -1,
    -1,
    4,
    -1,
    4,
    -1,
    4,
    -1,
    -1,
    0,
    0,
    -1,
    -1,
    2,
    2,
    4,
    4,
    2,
    2,
    2,
    2,
    4,
    4,
    2,
    2,
    -1,
    -1,
    0,
    0,
    -1,
    -1,
    0,
    0,
    4,
    4,
    2,
    2,
    0,
    0,
    4,
    4,
    2,
    2,
    0,
    0,
    4,
    4,
    2,
    2,
    0,
    0,
    4,
    4,
    2,
    2,
};

const uint8_t LIVE[] PROGMEM = {
    0x80,
    0xC0,
    0x80,
    0x00,
    0x00,
    0x80,
    0xC0,
    0x80,
    0x00,
    0x00,
    0x80,
    0xC0,
    0x80,
    0x00,
    0x00,
};
const uint8_t SHOOT[] PROGMEM = {0b11110000, 0b00001111};

const uint8_t Monsters[] PROGMEM = {
    0x00,
    0x00,
    0x00,
    0x58,
    0xBC,
    0x16,
    0x3F,
    0x3F,
    0x16,
    0xBC,
    0x58,
    0x00,
    0x00,
    0x00,
    0x00,
    0x00,
    0x00,
    0x98,
    0x5C,
    0xB6,
    0x5F,
    0x5F,
    0xB6,
    0x5C,
    0x98,
    0x00,
    0x00,
    0x00,
    0x00,
    0x70,
    0x18,
    0x7D,
    0xB6,
    0xBC,
    0x3C,
    0x3C,
    0xBC,
    0xB6,
    0x7D,
    0x18,
    0x70,
    0x00,
    0x00,
    0x1E,
    0xB8,
    0x7D,
    0x36,
    0x3C,
    0x3C,
    0x3C,
    0x3C,
    0x36,
    0x7D,
    0xB8,
    0x1E,
    0x00,
    0x00,
    0x9C,
    0x9E,
    0x5E,
    0x76,
    0x37,
    0x5F,
    0x5F,
    0x37,
    0x76,
    0x5E,
    0x9E,
    0x9C,
    0x00,
    0x00,
    0x1C,
    0x5E,
    0xFE,
    0xB6,
    0x37,
    0x5F,
    0x5F,
    0x37,
    0xB6,
    0xFE,
    0x5E,
    0x1C,
    0x00,
    0x00,
    0x40,
    0x60,
    0xF0,
    0x50,
    0x78,
    0x58,
    0x58,
    0x78,
    0x50,
    0xF0,
    0x60,
    0x40,
    0x00,
    0x00,
    0x40,
    0x60,
    0xD0,
    0x70,
    0x58,
    0x78,
    0x78,
    0x58,
    0x70,
    0xD0,
    0x60,
    0x40,
    0x00,
    0x00,
    0x00,
    0x00,
    0x00,
    0x00,
    0x24,
    0x18,
    0x18,
    0x24,
    0x00,
    0x00,
    0x00,
    0x00,
    0x00,
    0x00,
    0x00,
    0x00,
    0x81,
    0x00,
    0x24,
    0x18,
    0x18,
    0x24,
    0x00,
    0x81,
    0x00,
    0x00,
    0x00,
    0x00,
    0x00,
    0x24,
    0x81,
    0x18,
    0x24,
    0x5A,
    0x5A,
    0x24,
    0x18,
    0x81,
    0x24,
    0x00,
    0x00,
    0x42,
    0x00,
    0x24,
    0x81,
    0x4A,
    0x3C,
    0xA4,
    0x25,
    0x3C,
    0x4A,
    0x81,
    0x24,
    0x00,
    0x42,
};

const uint8_t vesso[] PROGMEM = {
    0x70,
    0x78,
    0x78,
    0x78,
    0x78,
    0x7E,
    0x7F,
    0x7E,
    0x78,
    0x78,
    0x78,
    0x78,
    0x70,
    0x54,
    0xD1,
    0xB4,
    0x78,
    0x3C,
    0xF0,
    0x34,
    0xF8,
    0x80,
    0x78,
    0xEA,
    0xE0,
    0x74,
};

const uint8_t back[] PROGMEM = {
    0xFF, 0xFF, 0xFD, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF,
    0xFF, 0xFF, 0xFF, 0xFF, 0xFD, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF,
    0xFF, 0x3F, 0x5F, 0x1F, 0xCF, 0x2F, 0xC7, 0xBF, 0xE7, 0x7F, 0xEF, 0xFF, 0xBF, 0xFF, 0xFF, 0xFF,
    0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFB, 0xFF, 0xFF, 0xFF,
    0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xF7, 0xFF, 0xFF, 0xFF, 0xFF,
    0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0x7F, 0xFF, 0xFF, 0xFF, 0xFF,
    0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0x7F, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF,
    0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xF7, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF,
    0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFE, 0xFF,
    0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFD, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF,
    0xC0, 0x14, 0xE9, 0xF6, 0xBD, 0xEF, 0xFD, 0xFF, 0xFD, 0xFF, 0xBF, 0xFF, 0xD7, 0x7F, 0xDF, 0xBF,
    0xF6, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF,
    0xFF, 0x7F, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF,
    0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF,
    0xFF, 0xFF, 0xFF, 0xFF, 0xBF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF,
    0xFF, 0xDF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xBF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF,
    0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xEF, 0xFF, 0xFF, 0xFF,
    0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF,
    0xFF, 0xFF, 0xFE, 0xFF, 0xFD, 0xF7, 0xFF, 0xF7, 0xFF, 0xF7, 0xFF, 0xFD, 0xFF, 0xFF, 0xFD, 0xFF,
    0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF,
    0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xBF, 0x7F, 0x1F, 0xBF, 0x0F, 0x47,
    0x8F, 0x23, 0x47, 0x93, 0x43, 0xB5, 0x4B, 0xA3, 0xDB, 0xA5, 0xDB, 0xB3, 0xE7, 0x5B, 0xF7, 0xAF,
    0xF7, 0x6F, 0xFF, 0xDF, 0xFF, 0x5F, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF,
    0xBF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF,
    0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF,
    0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xDF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF,
    0xFF, 0xFF, 0xEF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF,
    0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xBF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF,
    0xFF, 0xFF, 0xFF, 0xFF, 0x9F, 0x0F, 0x43, 0x15, 0x02, 0x50, 0x04, 0xA2, 0x18, 0xE2, 0x0C, 0xF2,
    0x0C, 0xF3, 0xAC, 0xDA, 0xF5, 0xBA, 0xED, 0x7A, 0xEF, 0xDA, 0xBF, 0xF6, 0xFF, 0xEF, 0xFD, 0xF7,
    0x7F, 0xFF, 0xED, 0xFF, 0x7F, 0xFB, 0xBF, 0xFE, 0xDF, 0x7D, 0xF7, 0xDF, 0xFF, 0xBF, 0xFF, 0xFF,
    0xFF, 0xBF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF,
    0xFF, 0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF,
    0xFF, 0xFF, 0xFF, 0xBF, 0xFF, 0xFF, 0xFF, 0xFF, 0xAF, 0xFF, 0xFF, 0xFF, 0xFF, 0xBF, 0xFF, 0xFF,
    0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF,
    0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF,
    0xFF, 0xFF, 0x11, 0x24, 0x08, 0x52, 0x00, 0x55, 0x28, 0xC3, 0x1C, 0xD1, 0xB6, 0x4D, 0xFA, 0x57,
    0xFD, 0xD7, 0x6E, 0xFB, 0xEE, 0x77, 0xDF, 0xF5, 0xDF, 0xFB, 0xFD, 0xBF, 0xFA, 0xFF, 0xFD, 0xFF,
    0xFD, 0x7F, 0xFE, 0xBF, 0xFF, 0xDF, 0xFF, 0xFF, 0xFF, 0xBF, 0xFF, 0xFF, 0xFF, 0xFE, 0xAB, 0xFF,
    0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFD, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF,
    0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFE, 0xFF,
    0xFF, 0xF7, 0xFF, 0xF7, 0xFF, 0xB6, 0xD5, 0xF7, 0x80, 0xF7, 0xD5, 0xB6, 0xFF, 0xF7, 0xFF, 0xF7,
    0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF,
    0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF,
    0xFF, 0xF6, 0x48, 0xA1, 0x14, 0x49, 0xA6, 0x59, 0xA5, 0xBA, 0x6B, 0xDE, 0x75, 0xFF, 0xDB, 0x7F,
    0xED, 0xFF, 0xF7, 0xFF, 0xFD, 0x7F, 0xFF, 0xFD, 0xFF, 0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0xDF, 0xFB,
    0xFF, 0xBF, 0xF7, 0xDF, 0xFB, 0xBF, 0x6D, 0xDF, 0xFF, 0xB7, 0x7F, 0xFF, 0x57, 0xBE, 0xD5, 0xFF,
    0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0x7F, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xBF, 0xFF,
    0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFD, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF,
    0xFF, 0xFF, 0xFF, 0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0xFA, 0xEF, 0xFF, 0xFF, 0xFF, 0xFE, 0xFF, 0xFF,
    0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF,
    0xFF, 0xFD, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF,
    0xFF, 0xFF, 0xFF, 0xFE, 0xE9, 0xD4, 0x6B, 0x96, 0x79, 0xD7, 0xBD, 0xD7, 0xFD, 0xEF, 0xBD, 0xF7,
    0xDF, 0xFF, 0xEE, 0xFF, 0xFF, 0xFF, 0xFF, 0xEF, 0xFF, 0xFF, 0xFF, 0xFB, 0xEE, 0xFF, 0x77, 0xFD,
    0xFF, 0xDF, 0xF6, 0xEF, 0x7D, 0xEB, 0xFF, 0x56, 0xBD, 0xCB, 0xF5, 0xF6, 0xFD, 0xFF, 0xFF, 0xFF,
    0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF,
    0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xEF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF,
    0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFB, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF,
    0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF,
    0xFF, 0x7F, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xEF, 0xFF, 0xFF, 0xFF,
    0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFD, 0xFE, 0xFF, 0xFA, 0xF7, 0xFD, 0xEF, 0xF7,
    0xDE, 0xEF, 0xFF, 0xBF, 0xEE, 0xFF, 0xDF, 0xBF, 0xFF, 0xDF, 0xFE, 0xBF, 0xFF, 0xAF, 0xFF, 0xDF,
    0xFB, 0xFF, 0xF6, 0xFF, 0xFB, 0xFF, 0xFC, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFE, 0xFF,
    0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFB, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF};

const uint8_t intro[] PROGMEM = {
    0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF,
    0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0x7F, 0x3F, 0x1F, 0x07, 0x01, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x03, 0x07, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x03, 0x07, 0xFF, 0x01, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x3F, 0xFF, 0xFF, 0x0F, 0x07, 0x01, 0x01, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x03, 0x07, 0x07, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x07, 0x07, 0x27, 0x3F, 0x3F, 0xFF, 0xFF, 0xFF,
    0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF,
    0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF,
    0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xC3, 0x03, 0x38, 0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F,
    0x1F, 0x1F, 0xFF, 0xFE, 0xFC, 0xF8, 0xE0, 0x00, 0x00, 0x00, 0x0F, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF,
    0x1F, 0x1F, 0x1F, 0xFF, 0xFF, 0xFC, 0xFC, 0xF8, 0x80, 0x00, 0x00, 0x03, 0x00, 0xFF, 0xFF, 0xFF,
    0x3F, 0x3F, 0xFF, 0xFF, 0xFF, 0xC0, 0x00, 0xFF, 0x3F, 0x00, 0x00, 0x00, 0xF0, 0xF8, 0xFC, 0xFF,
    0xFF, 0x0F, 0x0F, 0x0F, 0xFF, 0xFF, 0xFF, 0xFE, 0xFC, 0xF8, 0x00, 0x00, 0x00, 0xC0, 0xFE, 0xFF,
    0xFF, 0xFF, 0x3F, 0x1F, 0x1F, 0x1F, 0xDF, 0xDF, 0xDF, 0xDF, 0xC7, 0xE0, 0xFC, 0xFF, 0xFF, 0xFF,
    0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF,
    0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF,
    0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFE, 0xE0, 0x83, 0x9F, 0x3F, 0x7F, 0xFF, 0xFE,
    0xE0, 0xE0, 0xE0, 0xE1, 0xE1, 0xE1, 0x81, 0x01, 0x00, 0x00, 0x00, 0x00, 0x7F, 0xFF, 0xFF, 0xFF,
    0xFC, 0x80, 0x80, 0x83, 0xFF, 0xFF, 0xFF, 0xFF, 0x7F, 0x00, 0x00, 0x00, 0xFF, 0xFF, 0xFF, 0xFF,
    0x00, 0x00, 0x7F, 0xFF, 0xFF, 0xFF, 0x00, 0x01, 0x00, 0x00, 0x00, 0xFC, 0xFF, 0xFF, 0xFF, 0xFF,
    0x00, 0x00, 0x00, 0x00, 0x03, 0x03, 0x03, 0x03, 0x03, 0x00, 0x00, 0x80, 0xF8, 0xFF, 0xFF, 0xFF,
    0x7F, 0x7F, 0x70, 0x70, 0x70, 0x03, 0x83, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF,
    0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF,
    0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF,
    0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0x8E, 0x0C, 0xE8, 0xE1,
    0xE3, 0xE3, 0xC3, 0x83, 0x03, 0x9F, 0xFF, 0xFF, 0xFF, 0xF8, 0x00, 0x00, 0x00, 0x3F, 0xFF, 0xFF,
    0xFF, 0xFF, 0x07, 0x87, 0x87, 0xE7, 0xE7, 0xE1, 0xF8, 0xFE, 0x00, 0xC0, 0xFF, 0xFF, 0xFF, 0x3F,
    0x38, 0xB8, 0x38, 0xFF, 0xFF, 0xFF, 0xFE, 0x00, 0xF0, 0x00, 0x00, 0xFF, 0xFF, 0xFF, 0xFF, 0x01,
    0x00, 0x00, 0xF8, 0xFC, 0xFC, 0xFC, 0x3C, 0x00, 0x00, 0x00, 0xF0, 0xFF, 0xFF, 0xFF, 0x3F, 0x03,
    0x00, 0x02, 0x02, 0x3A, 0x3E, 0x3E, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF,
    0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF,
    0xFF, 0xFF, 0xFF, 0x9F, 0x1F, 0x1F, 0x11, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x03, 0x01, 0x01,
    0x01, 0x01, 0x01, 0x01, 0x03, 0x0F, 0x11, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x00, 0x00, 0x01,
    0x01, 0x03, 0x07, 0x07, 0x07, 0x07, 0x07, 0x07, 0x03, 0x00, 0x00, 0x00, 0x00, 0x00, 0x03, 0x07,
    0x07, 0x07, 0x00, 0x00, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x00, 0x07, 0x07, 0x07, 0x07, 0x00,
    0x01, 0x01, 0x00, 0x07, 0x07, 0x07, 0x07, 0x00, 0x00, 0x00, 0x00, 0x01, 0x03, 0x07, 0x07, 0x07,
    0x07, 0x07, 0x07, 0x03, 0x01, 0x00, 0x00, 0x00, 0x00, 0x06, 0x07, 0x07, 0x07, 0x07, 0x07, 0x07,
    0x07, 0x07, 0x07, 0x01, 0x00, 0x01, 0x01, 0x01, 0x01, 0x03, 0x0F, 0x1F, 0x0F, 0x0F, 0x07, 0x03,
    0x03, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x07, 0x1F, 0x1F, 0x3F, 0xFF, 0xFF, 0xFF,
    0xF8, 0xF0, 0x86, 0x1E, 0x3E, 0xFE, 0xFC, 0xF0, 0xC0, 0x00, 0x00, 0x06, 0x3C, 0x7C, 0xF8, 0xF0,
    0xE0, 0x80, 0x00, 0x00, 0x0C, 0x7C, 0xFC, 0xFC, 0xFC, 0xC0, 0x00, 0x00, 0x04, 0x3C, 0xFC, 0xFC,
    0xF8, 0xF0, 0x80, 0x00, 0x00, 0x00, 0x1E, 0xFE, 0xFE, 0xFE, 0xFE, 0xFC, 0x00, 0x00, 0x00, 0x00,
    0x00, 0xFC, 0xFC, 0xFC, 0xFC, 0xFE, 0xFE, 0xFE, 0xFE, 0xF0, 0x00, 0x00, 0x00, 0x00, 0x00, 0xFC,
    0xFC, 0xFC, 0xFC, 0xFC, 0x0C, 0x0C, 0x0C, 0x0C, 0xFC, 0xFC, 0xF8, 0xF0, 0xF0, 0x00, 0x00, 0x00,
    0x00, 0xFC, 0xFC, 0xFC, 0xFC, 0x7C, 0x0C, 0x0C, 0x0C, 0x0C, 0x0C, 0x0C, 0x0C, 0x00, 0x00, 0x00,
    0xE0, 0xFC, 0xFE, 0xFE, 0x7E, 0x0E, 0x0E, 0x0C, 0x0C, 0xFC, 0xFC, 0xFC, 0xFC, 0x70, 0x00, 0x00,
    0x00, 0x80, 0xE0, 0xF0, 0xF0, 0x78, 0x1C, 0x0C, 0x0E, 0xCE, 0xFE, 0xFE, 0xFE, 0x7E, 0x18, 0x81,
    0xFF, 0xFF, 0xFF, 0xFF, 0xFC, 0xF8, 0xE3, 0xC7, 0x1F, 0x7F, 0xFC, 0xF8, 0xE0, 0x80, 0x01, 0x0F,
    0x1F, 0x7F, 0xFF, 0xFE, 0xF8, 0xF8, 0x31, 0x7F, 0xFF, 0xFF, 0xFF, 0xF8, 0xC0, 0x00, 0x00, 0x03,
    0x0F, 0x3F, 0xFF, 0xFC, 0xF0, 0xC0, 0x00, 0x07, 0x7F, 0xFF, 0xFF, 0xFF, 0xC0, 0x00, 0x00, 0x00,
    0x00, 0xFF, 0xFF, 0xFF, 0xFF, 0x01, 0x03, 0x1F, 0xFF, 0xFF, 0xFC, 0x00, 0x00, 0x00, 0x00, 0x00,
    0xFF, 0xFF, 0xFF, 0xFF, 0x00, 0x00, 0x00, 0xF0, 0xFF, 0xFF, 0xFF, 0xFF, 0x07, 0x00, 0x00, 0xF0,
    0xFF, 0xFF, 0xFF, 0xFF, 0x3F, 0x30, 0x30, 0x30, 0x30, 0x30, 0x00, 0x00, 0x00, 0xC0, 0xF8, 0xFE,
    0xFF, 0xFF, 0x7F, 0x61, 0x60, 0xE0, 0xF0, 0x9E, 0x1F, 0x0F, 0x0F, 0x03, 0x00, 0x00, 0x10, 0x7C,
    0x7F, 0x7F, 0x7F, 0x67, 0xE1, 0xE0, 0xE1, 0xE0, 0x09, 0x19, 0xF9, 0xF9, 0xF9, 0xF8, 0xFE, 0xFF,
    0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFE, 0xFC, 0xF0, 0xE3, 0x8F, 0x1F, 0x7E, 0x7C,
    0x70, 0x40, 0x01, 0x07, 0x1F, 0x7F, 0x7E, 0x70, 0x60, 0x01, 0x23, 0xCF, 0x1F, 0x3F, 0x7C, 0x60,
    0x00, 0x30, 0xE0, 0x83, 0x1F, 0x3F, 0x7E, 0x7C, 0x7C, 0x7F, 0x7F, 0x7F, 0x7F, 0x00, 0x00, 0xF0,
    0x00, 0x7F, 0x7F, 0x7F, 0x7F, 0x0C, 0xEC, 0xEC, 0x0F, 0x7F, 0x7F, 0x7F, 0x60, 0x00, 0x00, 0x00,
    0x7F, 0x7F, 0x7F, 0x43, 0x40, 0x40, 0x40, 0x7F, 0x7F, 0x3F, 0x1F, 0x80, 0x00, 0x00, 0x78, 0x7F,
    0x7F, 0x7F, 0x7F, 0x41, 0x40, 0x40, 0x40, 0x40, 0x00, 0x00, 0x00, 0x60, 0x7C, 0x7F, 0x7F, 0x0F,
    0x01, 0x00, 0x00, 0x70, 0x7E, 0x7F, 0x1F, 0x0F, 0xC1, 0x00, 0x20, 0x78, 0x78, 0x78, 0x68, 0x60,
    0x60, 0x20, 0x38, 0x1E, 0x9F, 0xC7, 0xE3, 0xF1, 0xFC, 0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF};
