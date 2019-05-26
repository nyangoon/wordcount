from django.shortcuts import render
import operator

def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def result(request):
    full_text = request.GET['fulltext']

    word_list = full_text.split()
    word_dictionary={}
    sorted_dic={}

    for word in word_list:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1
    
    sorted_list = sorted(word_dictionary.items(), key=operator.itemgetter(1), reverse=True)

    most_key = sorted_list[0][0]
    most_value = sorted_list[0][1]

     

    return render(request,'result.html', 
    {'fulltext':full_text, 'total' : len(word_list), 'dictionary':sorted_list, 'most_key':most_key, 'most_value':most_value})
# Create your views here.
