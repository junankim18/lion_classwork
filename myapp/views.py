from django.shortcuts import render


def home(request):
    return render(request, 'myapp/home.html')


def team(request):
    result_team = request.GET['teamname']
    ctx = {}
    if result_team == '2':
        ctx = {
            'result': '이 팀이 2팀이네ㅎㅎ',
        }
    elif int(result_team) in [1, 3, 4, 5]:
        ctx = {
            'result': '저희가 많이 보죠',
        }
    return render(request, 'myapp/team.html', ctx)
