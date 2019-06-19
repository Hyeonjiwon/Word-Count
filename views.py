from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')
    
def result(request):
    text = request.GET['fulltext'] #home.html에서 textarea의 값을 text에 할당
    word_list = text.split()
    word_dictionary = {}

    for i in word_list:
        if i in word_dictionary: #이미 있는 단어이면 
            word_dictionary[i] += 1 # 1씩 증가
        else:
            word_dictionary[i] = 1
            
    return render(request, 'result.html', {'full': text, 'total': len(word_list), 'dictionary':word_dictionary.items()})