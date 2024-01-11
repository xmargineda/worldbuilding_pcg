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
                if not len(form_list) == 0 and not len(form_list) == len(chosen_elm)-1:
                    form_list +=', '
                if len(form_list) == len(chosen_elm)-1 and len(chosen_elm) > 1:
                    form_list += ' and '
                form_list += elm
            elif format == 2:
                form_list += f'-{elm}\n'
            elif format == 3:
                form_list += f' {elm}.'

        return form_list