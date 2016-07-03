from django import template
#from .. import choices

register = template.Library()

@register.filter
def get_index(my_tuple, args):
    arg1, arg2 = args.split(',') # split on the comma separator
    try:
        i = int(arg1) - 1
        j = int(arg2)
        return my_tuple[i][j] #same as my_tuple[task.status][1]
    except: 
        return None