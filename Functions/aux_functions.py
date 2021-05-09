

def is_link(arg):
    arg_list = arg.split()
    for item in arg_list:
        if 'https://open.spotify' in item:
            return [True, item]
    
    return [False]


def type_of_link(arg):
    arg_list = arg.split('/')
    print(arg_list)

#def transform_to_uri(arg):
#spotify:track:code
#

print(type_of_link('https://open.spotify.com/track/6leYHUK1DRqLMg9yD0vo9B?si=EZmxwjj3Td6j03GDqd68_Q'))