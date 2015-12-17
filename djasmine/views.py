# -*- coding: utf-8 -*-
import os.path
import glob2
from django.conf import settings
from django.shortcuts import render_to_response


def find_specfiles():
    for filepath in glob2.iglob(
            settings.JASMINE_SPEC_ROOT + '/**/*.[Ss]pec.js'):
        yield os.path.relpath(filepath, settings.JASMINE_SPEC_ROOT)


def jasmine_run_spec(request, spec=None):
    if spec:
        specfiles = [spec]
    else:
        specfiles = find_specfiles()
    return render_to_response(
        'djasmine/specrunner.html',
        {'specfiles': specfiles},
    )
