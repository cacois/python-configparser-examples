import ConfigParser
import ast

config = ConfigParser.RawConfigParser()
config.read('example.cfg')

# single variables
print config.get('section1', 'var1')
print config.get('section1', 'var2')
print config.get('section1', 'var3')

print config.get('section2', 'var4')
print config.get('section2', 'var5')
print config.get('section2', 'var6')

# lists
l1 = config.get('section1', 'list1').split(',')
l2 = config.get('section1', 'list2').split(',')
l3 = map(lambda s: s.strip('\''), config.get('section1', 'list3').split(','))

print l1,type(l1)
print l2,type(l2)
print l3,type(l3)

# dictionaries
d1 = ast.literal_eval(config.get('section3', 'dict1'))
print d1, type(d1)

d2 = ast.literal_eval(config.get('section3', 'dict2'))
print d2, type(d2)

d3 = ast.literal_eval(config.get('section3', 'dict3'))
print d3, type(d3)

d4 = ast.literal_eval(config.get('section3', 'dict4'))
print d4, type(d4)
print d4['key1'], type(d4['key1'])
print d4['key1'][1], type(d4['key1'][1])
print d4['key1'][2], type(d4['key1'][2])

