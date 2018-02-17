from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from django_xhtml2pdf.utils import generate_pdf

# Create your views here.
from panels.models import Panel


@login_required
def print_table(request, id):
    table = get_object_or_404(Panel, pk=id)
    resp = HttpResponse(content_type='application/pdf')
    return generate_pdf('print/table.html', file_object=resp, context=locals())
