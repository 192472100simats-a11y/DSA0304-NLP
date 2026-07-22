"""
Experiment 04: Finite-State Machine for plural noun generation
"""

def pluralize(noun: str) -> str:
    if noun.endswith(('s', 'sh', 'ch', 'x', 'z')):
        return noun + 'es'
    if noun.endswith('y') and len(noun) > 1 and noun[-2] not in 'aeiou':
        return noun[:-1] + 'ies'
    if noun.endswith('f'):
        return noun[:-1] + 'ves'
    if noun.endswith('fe'):
        return noun[:-2] + 'ves'
    return noun + 's'

nouns = ['cat', 'bus', 'brush', 'baby', 'leaf', 'knife', 'toy']
for noun in nouns:
    print(noun, '->', pluralize(noun))

# Sample output:
# cat -> cats
# bus -> buses
# brush -> brushes
# baby -> babies
# leaf -> leaves
# knife -> knives
# toy -> toys
