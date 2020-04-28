import sys
import argparse

from random import randint

#######################################

def arguments():
    parser = argparse.ArgumentParser(description='Generate simple operations')

    parser.add_argument('-n','--number',help='Number of operations [default: 5]',default='5',required=False)
    parser.add_argument('-p','--operation',help='Operation to be done. [default: +; available: + -]',default='+',required=False)
    parser.add_argument('-m','--min',help='Minimum value for the operations [default: 0]',default='0',required=False)
    parser.add_argument('-M','--max',help='Maximum value for the operations [default: 10]',default='10',required=False)
    parser.add_argument('-u','--unknown',help='Missing value for the operation a+b=c [default: 0; available: 0 (None missing), a, b, c]',default='0',required=False)

    try:
        options = parser.parse_args()
    except:
        sys.exit(0)

    # Number of operations
    if options.number.isdigit():
        nb_ope = int(options.number)
    else:
        print('Error: the given operation number format is not correct: '+options.number)
        sys.exit(1)

    # Type of operation
    if '+' == options.operation or '-'==options.operation:
        ope = options.operation
    else:
        print('Error: the given operation is unknown: '+options.operation)
        sys.exit(1)

    # Minmum for the operand, and result
    if options.min.isdigit():
        vmin = int(options.min)
    else:
        print('Error: the given minimal value format is not correct: '+options.min)
        sys.exit(1)

    # Maximum for the operand and result
    if options.max.isdigit():
        vmax = int(options.max)
    else:
        print('Error: the given maximal value format is not correct: '+options.max)
        sys.exit(1)

    # Missing value
    if options.unknown in ['0','a','b','c']:
        unk = options.unknown
    else:
        print('Error: the given unknown is not correct: '+options.unknown)
        sys.exit(1)

    return (nb_ope,ope,vmin,vmax,unk)



#######################################

def getrand(vmin,vmax):
    return randint(vmin,vmax)

#######################################

def inrange(v,vmin,vmax):
    return (v>=vmin and v<=vmax)

#######################################

def operation(a,b,operation):
    if '+' == operation:
        return a+b
    elif '-' == operation:
        return a-b
    else:
        return None

#######################################

def get_operation(vmin,vmax,ope):
    result = None
    operand_a = operand_b = 0

    while None == result:
        operand_a = getrand(vmin,vmax)
        operand_b = getrand(vmin,vmax)
        result = operation(operand_a,operand_b,ope)
        #print('%d %s %d = %d' % (operand_a,ope,operand_b,result) )
        if not inrange(result,vmin,vmax):
            result = None

    return (operand_a,operand_b,result)

#######################################

if __name__ == '__main__':
    nb,ope,vmin,vmax,unk = arguments()

    operations = []
    values = []
    for n in range(nb):
        (a,b,r) = get_operation(vmin,vmax,ope)
        operations += [(a,b,r)]
        if 'a' == unk:
            values += [a]
        elif 'b' == unk:
            values += [b]
        elif 'c' == unk:
            values += [r]

    values = sorted(values)

    for n in range(len(operations)):
        (a,b,r) = operations[n]
        if 'a' == unk:
            print('___ %s %3d = %3d' % (ope,b,r) )
        elif 'b' == unk:
            print('%3d %s ___ = %3d' % (a,ope,r) )
        elif 'c' == unk:
            print('%3d %s %3d = ___' % (a,ope,b) )
        else:
            print('%3d %s %3d = %3d' % (a,ope,b,r) )

    for n in range(len(values)):
        print(values[n], end=' ')
    print('')
