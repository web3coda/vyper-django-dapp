# SPDX-License-Identifier: UNLICENSED
# @version ^0.3.7

storedNumber: public(uint256)

# Storing function
@external 
def setNumber(_number: uint256):
    self.storedNumber = _number

# Reading function
@external 
def getNumber() -> uint256:
    return self.storedNumber