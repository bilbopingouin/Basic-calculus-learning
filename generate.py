import sys
import argparse

from random import randint

#######################################

def arguments():
    global opefn

    parser = argparse.ArgumentParser(description='Generate simple operations')

    parser.add_argument('-n','--number',help='Number of operations [default: 5]',type=int,default=5,required=False)
    parser.add_argument('-p','--operation',help='Operation to be done. [default: add; available: add sub div times max]',default='add',required=False)
    parser.add_argument('-m','--min',help='Minimum value for the operations [default: 0]',type=int, default=0,required=False)
    parser.add_argument('-M','--max',help='Maximum value for the operations [default: 10]',type=int,default=10,required=False)
    parser.add_argument('-u','--unknown',help='Missing value for the operation a+b=c [default: 0; available: 0 (None missing), a, b, c]',default='0',required=False)
    #parser.add_argument('--sub',dest='operation_fn',help='Set a subtraction instead of an addition',action='store_const',const=sub,default=add,required=False)

    try:
        options = parser.parse_args()
    except:
        sys.exit(0)

    # Number of operations
    nb_ope = int(options.number)

    # Type of operation
    if 'add' == options.operation: 
        ope = '+'
    elif 'sub'==options.operation:
        ope = '-'
    elif 'div'==options.operation:
        ope = '/'
    elif 'times'==options.operation:
        ope = '*'
    elif 'max'==options.operation:
        ope = '<?>' 
    else:
        print('Error: the given operation is unknown: '+options.operation)
        sys.exit(1)
    opefn=options.operation

    # Minmum for the operand, and result
    vmin = int(options.min)

    # Maximum for the operand and result
    vmax = int(options.max)

    # Missing value
    if options.unknown in ['0','a','b','c']:
        unk = options.unknown
    else:
        print('Error: the given unknown is not correct: '+options.unknown)
        sys.exit(1)

    return (nb_ope,ope,vmin,vmax,unk)



#######################################

def sub(a,b):
    return a-b

def add(a,b):
    return a+b

def div(a,b):
    return a/b

def times(a,b):
    return a*b

#######################################

def getrand(vmin,vmax):
    return randint(vmin,vmax)

#######################################

def inrange(v,vmin,vmax):
    return (v>=vmin and v<=vmax)

#######################################

def operation(a,b,operation):
    global opefn

    return eval(opefn)(a,b)
    #if '+' == operation:
    #    return a+b
    #elif '-' == operation:
    #    return a-b
    #else:
    #    return None

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
