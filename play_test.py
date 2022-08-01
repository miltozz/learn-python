from operator import itemgetter

l = ['one', 'two', 'three']
d = {'pizza': 'good', 'pasta': 'also good', 'burger': 'very good'}

g_dict = {
    'choco': 'late',
    'van': 'illa',
    'g_list1':
    [
        {
            'fdict1a': 'fdictval1a',
            'fdict1b': 'fdictval1b',
            'StartTime': 333
        },
        {
            'fdict1a': 'fdictval2a',
            'fdict1b': 'fdictval2b',
            'StartTime': 111
        },
        {
            'fdict1a': 'fdictval2a-copy',
            'fdict1b': 'fdictval2b-copy',
            'StartTime': 222
        }
    ],
    'espresso': 'freddo',
    'latte': 'machiatto',
    'g_list2':
    [
        {
            'fdict1a': 'fdictval3a',
            'fdict1b': 'fdictval3b'
        },
        {
            'fdict1a': 'fdictval4a',
            'fdict1b': 'fdictval4b'
        }
    ],
}


# sort the list of dictionaries by 'StartTime' and reverse
da_sorted = sorted(g_dict['g_list1'], key=itemgetter('StartTime'), reverse=True)

for item in da_sorted:
    print(item)
