import sys
import argparse

from random import randint

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

def arguments():
    # Known operations
    operations_functions = { 'add': {'function' : add, 'sign' : '+'}, 
                             'sub': {'function' : sub, 'sign' : '-'}, 
                             'div': {'function' : div, 'sign' : '/'},
                             'times': {'function' : times, 'sign' : '*'}, 
                             'max': { 'function' : max, 'sign' : '<?>'}
                            }

    # Initialise the parser
    parser = argparse.ArgumentParser(description='Generate simple operations')

    # Configure the parser
    parser.add_argument('-n','--number',help='Number of operations [default: 5]',type=int,default=5,required=False)
    parser.add_argument('-p','--operation',help='Operation to be done. [default: add; available: add sub div times max]',default='add',required=False)
    parser.add_argument('-m','--min',help='Minimum value for the operations [default: 0]',type=int, default=0,required=False)
    parser.add_argument('-M','--max',help='Maximum value for the operations [default: 10]',type=int,default=10,required=False)
    parser.add_argument('-u','--unknown',help='Missing value for the operation a+b=c [default: 0; available: 0 (None missing), a, b, c]',default='0',required=False)

    # Analysing the input
    options = parser.parse_args()

    # List of parameters
    params = {}

    # Number of operations
    params['nb_ope'] = int(options.number)

    # Type of operation
    if options.operation not in operations_functions:
        print('Error: the given operation is unknown: '+options.operation)
        sys.exit(1)

    params['ope'] = operations_functions[options.operation]['sign']
    params['opefn']=operations_functions[options.operation]['function']

    # Minmum for the operand, and result
    params['vmin'] = int(options.min)

    # Maximum for the operand and result
    params['vmax'] = int(options.max)

    # Missing value
    if options.unknown in ['0','a','b','c']:
        params['unk'] = options.unknown
    else:
        print('Error: the given unknown is not correct: '+options.unknown)
        sys.exit(1)

    return params



#######################################

def getrand(vmin,vmax):
    return randint(vmin,vmax)

#######################################

def inrange(v,vmin,vmax):
    return (v>=vmin and v<=vmax)

#######################################

def operation(a,b,opefn):
    return opefn(a,b)

#######################################

def get_operation(vmin,vmax,ope):
    result = None
    operand_a = operand_b = 0

    while result is None:
        operand_a = getrand(vmin,vmax)
        operand_b = getrand(vmin,vmax)
        result = operation(operand_a,operand_b,ope)
        if not inrange(result,vmin,vmax):
            result = None

    return (operand_a,operand_b,result)

#######################################

if __name__ == '__main__':
    params = arguments()

    operations = []
    values = []
    for n in range(params['nb_ope']):
        (a,b,r) = get_operation(params['vmin'],params['vmax'],params['opefn'])
        operations += [(a,b,r)]
        if 'a' == params['unk']:
            values += [a]
        elif 'b' == params['unk']:
            values += [b]
        elif 'c' == params['unk']:
            values += [r]

    values = sorted(values)

    for operation in operations:
        (a,b,r) = operation
        if 'a' == params['unk']:
            print('___ %s %3d = %3d' % (params['ope'],b,r) )
        elif 'b' == params['unk']:
            print('%3d %s ___ = %3d' % (a,params['ope'],r) )
        elif 'c' == params['unk']:
            print('%3d %s %3d = ___' % (a,params['ope'],b) )
        else:
            print('%3d %s %3d = %3d' % (a,params['ope'],b,r) )

    for v in values:
        print(v, end=' ')
    print('')
