import random
# format 1 is sentence (a, b, c)
# format 2 is list (-a\n-b\n-c)
def random_list_formater(lst, nelements, format):
    if not len(lst) == 0:
        count = 0
        form_list = ''
        chosen_elm = []
        if len(lst) > nelements:
            while count < nelements :
                i = random.randint(0,len(lst)-1)                
                elm = lst.pop(i)
                count += 1
                chosen_elm.append(elm)
        else:
            chosen_elm = lst
        
        for elm in chosen_elm:
            if format == 1:
                if not len(form_list) == 0:
                    form_list +=', '
                form_list += elm
            elif format == 2:
                form_list += '-' + elm + '\n'

        return form_list