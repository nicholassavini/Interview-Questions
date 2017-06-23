def return_list(l):
    list = '<ul>'
    for i in l:
        list += '<li>' + i + '</li>'
    list += '</ul>'
    return list

items = ['apple', 'orange', 'banana']

print(return_list(items))
