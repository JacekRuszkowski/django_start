from django.shortcuts import render

# Create your views here.

# from django.shortcuts import render

# def test(request, imie, wiek):
#     template_data = {
#         't_imie': imie,
#         't_wiek': wiek,
#     }
#     return render(request, 'blog/test.html', template_data)

def post_list(request):
    return render(request, 'blog/post_list.html', {})