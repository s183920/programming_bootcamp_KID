#!/usr/bin/env python3

import sys
import traceback as tb
import re

# IMPORTANT: In the CodeJudge overwrite version this must be set to /true/.
#            This allows us to pass levels in through stdin instead.
DO_READ_LEVEL_FROM_STDIN = False

MAX_STEP_COUNT = 1000 # NOTE: This should be synchronized with the animator!
_turnCount = 0

_x = 0
_y = 0
_dir = 0
_hasDied = False

_level = []
_starsLeft = 0

## Internal ##

def _gameStillGoing():
    global _starsLeft, _hasDied
    return _starsLeft > 0 and not _hasDied

def _printMove(m):
    stackTrace = tb.extract_stack() # No need to look further back.
    thisFileName = stackTrace[1][0] # Filename is first element of tuple.
    lineNumber = None
    for (filename, line, function, text) in stackTrace:
        if not filename == thisFileName:
            lineNumber = line
            break

    if lineNumber:
        print(f"{m}\t{lineNumber}")
    else:
        print(f"{m}")

def _isOutOfBounds():
    global _level, _x, _y
    return _y < 0 or _y >= len(_level) or _x < 0 or _x >= len(_level[_y])

def _isOnTile():
    global _level, _x, _y
    return not _isOutOfBounds() and _level[_y][_x] != '.'

def _collectStarUnderPlayerIfAny():
    global _level, _x, _y, _starsLeft
    if _isOutOfBounds() or not _isOnTile() or not _level[_y][_x].isupper():
        return False
    _level[_y][_x] = _level[_y][_x].lower()
    _starsLeft -= 1
    if _starsLeft == 0:
        print("won")
        exit(0)
    return True

def _allowedCell(c):
    return c in "rgbnRGBN."

def _advanceTurn():
    global _turnCount, _hasDied
    _turnCount += 1
    if _turnCount > MAX_STEP_COUNT or _isOutOfBounds() or not _isOnTile():
        if _turnCount > MAX_STEP_COUNT:
            print(f"lost by exceeding maximum allowed turns ({MAX_STEP_COUNT})")
        else:
            print("lost by falling off the edge")
        _hasDied = True
        exit(0)
    else:
        _collectStarUnderPlayerIfAny()

def _parseLevel(levelStr):
    global _level, _x, _y, _dir, _starsLeft, _turnCount, _hasDied
    if DO_READ_LEVEL_FROM_STDIN:
        lines = [line.rstrip("\n") for line in sys.stdin]
        if not lines:
            print("Failed to read any input from stdin!", file=sys.stderr)
            return False
    else:
        lines = levelStr.split("\n")

    # We use the number of input lines to differentiate between level data and player position.
    # If these lines are empty for any reason (happens on CodeJudge due to newline insert), then our parsing
    # fails. Therefore we clean these before proceeding.
    while lines and not lines[-1]:
        del lines[-1]

    if len(lines) <= 1:
        print(f"Missing level data! Expected more than {len(lines)} lines.", file=sys.stderr)
        return False

    # Parse the level data.
    _level.clear()
    _starsLeft = 0
    levelHeight = len(lines) - 1
    levelWidth  = 0
    for i in range(levelHeight):
        line = lines[i]
        levelWidth = max(levelWidth, len(line))
        _level.insert(0, []) # We insert at start to achieve (0,0) in bottom-left corner.
        for j in range(len(line)):
            c = line[j]
            if not _allowedCell(c):
                print(f"Unknown cell character at position {j} in line {i} ({c})!", file=sys.stderr)
                return False
            _level[0].append(c)
            if c.isupper():
                _starsLeft += 1
    if levelHeight == 0 or levelWidth == 0:
        print("Empty levels are not allowed!", file=sys.stderr)
        return False

    # Parse player starting position.
    parts = re.split(r'[\t ]+', lines[-1])
    if len(parts) != 3:
        print("Unable to read player position in last line. Ensure that it has the correct format: x y direction", file=sys.stderr)
        return False
    try:
        _x = int(parts[0])
        _y = int(parts[1])
    except:
        print("Player position (x,y) is in an incorrect format. Ensure it is integers, e.g.: 4 3", file=sys.stderr)
        return False
    if _isOutOfBounds():
        print(f"Player position ({_x},{_y}) is outside the level.", file=sys.stderr)
        return False
    if not _isOnTile():
        print(f"Player is not standing on a tile ({_x},{_y}).", file=sys.stderr)
        return False

    # In case the player starts on a star, collect it.
    _collectStarUnderPlayerIfAny();

    rot = parts[2]
    _dir = { "r": 0, "u": 1, "l": 2, "d": 3 }.get(rot)
    if _dir == None:
        print(f"Invalid player direction '{rot}'! Must be either 'r', 'l', 'u' or 'd'.", file=sys.stderr)
        return False

    _turnCount = 0
    _hasDied = False
    return True

## Interface ##

def move():
    global _x, _y, _dir
    if not _gameStillGoing():
        return
    _printMove("m")
    if _dir == 0:
        _x += 1
    elif _dir == 1:
        _y += 1
    elif _dir == 2:
        _x -= 1
    elif _dir == 3:
        _y -= 1
    _advanceTurn()

def turnLeft():
    global _dir
    if not _gameStillGoing():
        return
    _printMove("l")
    _dir = 0 if _dir == 3 else _dir + 1
    _advanceTurn()

def turnRight():
    global _dir
    if not _gameStillGoing():
        return
    _printMove("r")
    _dir = 3 if _dir == 0 else _dir - 1
    _advanceTurn()

def isBlue():
    global _level, _x, _y
    if not _gameStillGoing():
        return False
    _printMove("b?")
    _advanceTurn()
    return _level[_y][_x] == 'b' or _level[_y][_x] == 'B'

def isRed():
    global _level, _x, _y
    if not _gameStillGoing():
        return False
    _printMove("r?")
    _advanceTurn()
    return _level[_y][_x] == 'r' or _level[_y][_x] == 'R'

def isGreen():
    global _level, _x, _y
    if not _gameStillGoing():
        return False
    _printMove("g?")
    _advanceTurn()
    return _level[_y][_x] == 'g' or _level[_y][_x] == 'G'

def loadLevel(levelStr):
    if not _parseLevel(levelStr):
        exit(1)
