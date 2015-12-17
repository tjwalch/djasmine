from django.shortcuts import render


def jasmine_run_one_spec(request, spec):
    return render(
        request,
        'djasmine/specrunner.html',
        context={'specfiles': [spec]},
    )


_specfiles = frozenset()


def jasmine_run_suite(request):
    return render(
        request,
        'djasmine/specrunner.html',
        context={'specfiles': _specfiles}
    )
