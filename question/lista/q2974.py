def comparison(model, vector):
    higher = ''
    for i in range(len(model)):
        for j in range(i, len(model)+1):
            
            sub = model[i:j]
            is_sub_valid = all(sub in word for word in vector)

            if is_sub_valid and len(higher) < len(sub) and i != j:
                higher = sub
    return higher


def input_q2974(forms):
    forms.remove(forms[0])
    model = forms[0]
    forms.remove(forms[0])

    phrase = [word for word in forms]
    
    return comparison(model, phrase)
