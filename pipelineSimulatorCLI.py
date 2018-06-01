#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""CPU Pipeline algorithm simulator.
This script simulates the CPU pipeline algorithm of a emu 8086 processor.
"""
__author__ = "Altin Ukshini"
__copyright__ = "Copyright (c) 2018, Altin Ukshini"

__license__ = "GPL v3.0"
__version__ = "1.0"
__maintainer__ = "Altin Ukshini"
__email__ = "altin.ukshini@gmail.com"
__status__ = "Development"
__credits__ = "https://github.com/cvanoort/CPUPipelineSimulation"


import os
import sys
import argparse
from argparse import RawTextHelpFormatter

########################################################
# Config
########################################################

pipelineStages = 6;
numberRegisters = 46;

########################################################
# Predefined variables
########################################################

class ProcessInfo:
    idNum = 0
    operand1 = -1
    operand2 = -1
    stall = False
    result = -1

    def __init__(self, idNum = 0, operand1 = -1, operand2 = -1, result = -1, stall = False):
        self.idNum = idNum
        self.operand1 = operand1
        self.operand2 = operand2
        self.result = result
        self.stall = bool(stall)

class PipelineStatus():

    size = 0
    instructionEx = 0
    stageID = []
    pipelineStatus = []

    def __init__(self, size):
        self.size = size
        self.instructionEx = 0
        self.stageID = []
        self.pipelineStatus = []

        self.stageID.append("FI")
        self.stageID.append("DI")
        self.stageID.append("CO")
        self.stageID.append("FO")
        self.stageID.append("EI")
        self.stageID.append("WO")

        for i in range(0, self.size):
            self.pipelineStatus.append(ProcessInfo())

    def getStatus(self, index):
        if index < self.size:
            if self.pipelineStatus[index].idNum != 0:
                return True
            else:
                return False
        else:
            sys.exit("ERROR: Index out of bounds on pipelineStatus!\n")

    def getElement(self, index):
        if index < self.size:
            return self.pipelineStatus[index]
        else:
            sys.exit("ERROR: Index out of bounds on pipelineStatus!\n")

    def addInstruction(self, p):
        if self.pipelineStatus[0].idNum == 0:
            self.pipelineStatus[0] = p
        else:
            sys.exit("ERROR: FI is busy!\n")

    def setInstrEx(self, instructorNum):
        self.instructionEx = instructorNum

    def setStall(self, index, stall):
        if index < self.size:
            self.pipelineStatus[index].stall = bool(stall)

    def getStall(self, index):
        return self.pipelineStatus[index].stall

    def advancePipeline(self, resultStage):
        self.pipelineStatus[resultStage] = ProcessInfo()
        for i in range(self.size-1, 0, -1):
            if self.pipelineStatus[i-1].stall is not True and self.pipelineStatus[i].idNum == 0:
                self.pipelineStatus[i] = self.pipelineStatus[i-1]
                self.pipelineStatus[i-1] = ProcessInfo()

    def isEmpty(self):
        empty = bool(True)
        for i in range(0, self.size - 1):
            if self.pipelineStatus[i].idNum != 0:
                empty = bool(False)
        return empty

    def printGraph(self, cycleNum, startChart, stopChart):
        if self.pipelineStatus[0].idNum >= startChart and self.instructionEx <= stopChart and startChart > 0:
            for i in range(0, self.instructionEx - startChart + 1): ################################################ +1
                sys.stdout.write("   ")

            something = self.size
            while (something - 1) >= 0:  # self.sizefor i in range(self.size - 1, -1, -1):
                if self.pipelineStatus[something - 1].idNum != 0:
                    if self.pipelineStatus[something - 1].idNum >= startChart and self.pipelineStatus[something - 1].idNum <= stopChart:
                        if self.pipelineStatus[something - 1].stall:
                            sys.stdout.write("** ")
                            something = 0
                        else:
                            sys.stdout.write(self.stageID[something - 1] + " ")
                something -= 1
            sys.stdout.write(os.linesep)


class RegisterInfo:
    lastWrite = 0
    nextWrite = 0

    def __init__(self):
        self.lastWrite = 0
        self.nextWrite = 0

class RegisterStatus:

    size = 0
    registerStatus = []

    def __init__(self, size):
        self.size = size
        self.registerStatus = []

        for i in range(0, self.size):
            self.registerStatus.append(RegisterInfo())

    def setLast(self, index, instructionNumber):
        self.registerStatus[index].lastWrite = instructionNumber

    def setNext(self, index, instructionNumber):
        self.registerStatus[index].nextWrite = instructionNumber

    def getLast(self, index):
        return self.registerStatus[index].lastWrite

    def getNext(self, index):
        return self.registerStatus[index].nextWrite

    def writeBack(self, p):
        if self.registerStatus[int(p.result)].nextWrite == p.idNum:
            self.registerStatus[int(p.result)].lastWrite = p.idNum
            self.registerStatus[int(p.result)].nextWrite = 0

    def decode(self, p):
        stall = bool(False)

        # if one of p's operands has a process waiting to write to it, return true to stall
        if p.operand1 != -1:
            if self.registerStatus[int(p.operand1)].nextWrite != 0 and self.registerStatus[int(p.operand1)].nextWrite < p.idNum:
                stall = bool(True)
        if p.operand2 != -1:
            if self.registerStatus[int(p.operand2)].nextWrite != 0 and self.registerStatus[int(p.operand2)].nextWrite < p.idNum:
                stall = bool(True)

        # set the instruction number of process p to be the nextWrite of the result register of p
        if  p.result != -1 and stall is not True:
            self.registerStatus[int(p.result)].nextWrite = p.idNum

        return stall

    def printGraph(self):
        sys.stdout.write("Register Status\n")

        for i in range(0, self.size):
            # Don't output register information unless it's non-zero
            if self.registerStatus[i].lastWrite != 0 or self.registerStatus[i].nextWrite != 0:
                sys.stdout.write("  Register " + str(i) + ": Last Write - " + str(self.registerStatus[i].lastWrite) + ", Next Write - " + str(self.registerStatus[i].nextWrite) + "\n")

        sys.stdout.write(os.linesep)

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='CPU Pipeline Simulator.', formatter_class=RawTextHelpFormatter)

    parser.add_argument('-o', '--operandstage', 
                            dest='operandstage', 
                            default=1, 
                            metavar='', 
                            help='''Stage in which the operand is read (e.g., stage 1 (DI) out of cycles 0-5).\nDefault: 1\n\n''')

    parser.add_argument('-r', '--resultstage', 
                            dest='resultstage', 
                            default=5, 
                            metavar='',
                            help='''Stage in which results are available (e.g., stage 5 (WO) out of cycles 0-5).\nDefault: 5\n\n''')

    parser.add_argument('-s', '--startat', 
                            dest='startat', 
                            default=1, 
                            metavar='',
                            help='''The starting instruction for the execution chart.\nDefault: 1\n\n''')

    parser.add_argument('-e', '--endat', 
                            dest='endat', 
                            default=10, 
                            metavar='',
                            help='''The ending instruction for the execution chart (0 or < starting instruction means no execution chart)\nDefault: 10\n\n''')

    parser.add_argument('-t', '--tracefile',
                            dest='tracefile',
                            default=None,
                            metavar='',
                            help='Specify the trace file you want to use.\n\n')

    parser.add_argument('-p', '--pipelinestages', 
                            dest='pipelinestages', 
                            default=pipelineStages, 
                            metavar='',
                            help='''Pipeline stages/cycles depth.\nDefault: ''' + str(pipelineStages) + '''\n\n''')

    parser.add_argument('-re', '--registernumbers', 
                            dest='registernumbers', 
                            default=numberRegisters, 
                            metavar='',
                            help='''Number of registers.\nDefault: ''' + str(numberRegisters) + '''\n\n''')


    args = parser.parse_args()

    if not args.tracefile or os.path.isfile(args.tracefile) is not True:
        parser.error('Provided trace file does not exist: ' + args.tracefile)

    if args.pipelinestages != pipelineStages:
        pipelineStages = int(args.pipelinestages)

    if args.registernumbers != numberRegisters:
        numberRegisters = int(args.registernumbers)

    # Typecasting variables as needed
    operandStage = int(args.operandstage)
    resultStage = int(args.resultstage)
    startChart = int(args.startat)
    endChart = int(args.endat)
    traceFile = str(args.tracefile)

    print("\nBEGIN SIMULATION: CPU Pipeline simulation\n")

    print("Operands Stage: " + str(operandStage) + ", \nResults Stage: " + str(resultStage) + ", \nStarting Instruction: " + str(startChart) + ", \nEnding Instruction: " + str(endChart) + ", \nTrace File: " + traceFile + "\n")

    op1 = None
    op2 = None
    result = None
    instructionNumber = 0;
    stageNum = 0;
    stallNum = 0;

    pipe = PipelineStatus(int(pipelineStages))
    regs = RegisterStatus(int(numberRegisters))

    with open(traceFile, 'r') as traceFile:
        for line in traceFile:
            instructionNumber += 1

            op1 = int(line.split(" ")[0])
            op2 = int(line.split(" ")[1])
            result = int(line.split(" ")[2])

            if pipe.getStatus(resultStage):
                pipe.setInstrEx( pipe.getElement(resultStage).idNum )

            pipe.advancePipeline( resultStage )

            if pipe.getStatus(resultStage):
                regs.writeBack( pipe.getElement(resultStage) )

            pipe.addInstruction( ProcessInfo(instructionNumber, op1, op2, result, False) )

            # check and set stalls
            pipe.setStall( operandStage, regs.decode(pipe.getElement(operandStage)) )

            pipe.printGraph( stageNum, startChart, endChart )

            stageNum += 1

            while pipe.getStall(operandStage):
                if pipe.getStatus(resultStage):
                    pipe.setInstrEx( pipe.getElement(resultStage).idNum )

                pipe.advancePipeline( resultStage )

                if pipe.getStatus(resultStage):
                    regs.writeBack( pipe.getElement(resultStage) )

                # check and set stalls
                pipe.setStall( operandStage, regs.decode(pipe.getElement(operandStage)) )

                pipe.printGraph( stageNum, startChart, endChart )

                stageNum += 1
                stallNum += 1

    traceFile.close()

    while not pipe.isEmpty():
        if pipe.getStatus(resultStage):
            pipe.setInstrEx( pipe.getElement(resultStage).idNum )

        pipe.advancePipeline( resultStage )

        if pipe.getStatus(resultStage):
            regs.writeBack( pipe.getElement(resultStage) )

        # check and set stalls
        pipe.setStall( operandStage, regs.decode(pipe.getElement(operandStage)) )

        pipe.printGraph( stageNum, startChart, endChart )

        stageNum += 1

        # Handle Stalls
        if pipe.getStall(operandStage):
            stallNum += 1

    noPipeline = pipelineStages*instructionNumber
    speedup = round(100*(float(noPipeline)/float(stageNum)), 3)
    avgStalls = round(float(stallNum)/float(instructionNumber), 3)

    print("\nAnalysis of the simulation: ")
    print("Number of instructions executed: " + str(instructionNumber))
    print("Expected Number of stages when unpipelined: " + str(noPipeline))
    print("Number of stall stages: " + str(stallNum))
    print("Number of stages in the pipeline simulation: "+ str(stageNum))
    print("Average number of stalls per instruction: " + str(avgStalls) )
    print("Speedup: " + str(speedup) + "%")

    print("\nEND SIMULATION\n")
