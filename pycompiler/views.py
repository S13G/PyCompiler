import sys

from django.shortcuts import render


# Create your views here.


def index(request):
    return render(request, 'index.html')


def runcode(request):
    if request.method == "POST":
        code_area_data = request.POST['code_area']

        try:
            # save standard output reference
            original_stdout = sys.stdout
            # change output file to the file created
            sys.stdout = open('file.txt', 'w')

            # execute code
            exec(code_area_data)

            sys.stdout.close()

            # reset standard output
            sys.stdout = original_stdout

            # read output from file and save it in variable
            output_data = open('file.txt', 'r').read()
        except Exception as e:
            sys.stdout = original_stdout
            output_data = e

    context = {"code": code_area_data, "output": output_data}
    return render(request, 'index.html', context)
