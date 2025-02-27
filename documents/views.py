from django.shortcuts import render
from .models import InsuranceCertificate

# Create your views here.


def document_view(request):
    if request.method == 'POST':
        # Extract data from the form
        insured_name = request.POST.get('insured_name')
        cert_holder_name = request.POST.get('cert_holder_name')
        cert_holder_address = request.POST.get('cert_holder_address')
        cert_holder_city = request.POST.get('cert_holder_city')
        cert_holder_state = request.POST.get('cert_holder_state')
        cert_holder_zip = request.POST.get('cert_holder_zip')
        email = request.POST.get('email')
        general_liability = request.POST.get('general_liability') is not None
        auto_liability = request.POST.get('auto_liability') is not None
        work_comp = request.POST.get('work_comp') is not None
        umbrella = request.POST.get('umbrella') is not None
        ai_general_liability = request.POST.get(
            'ai_general_liability') is not None
        ai_auto_liability = request.POST.get('ai_auto_liability') is not None
        primary_general_liability = request.POST.get(
            'primary_general_liability') is not None
        waiver_general_liability = request.POST.get(
            'waiver_general_liability') is not None
        job_location = request.POST.get('job_location')

        # Create a new InsuranceCertificate instance
        certificate = InsuranceCertificate(
            insured_name=insured_name,
            cert_holder_name=cert_holder_name,
            cert_holder_address=cert_holder_address,
            cert_holder_city=cert_holder_city,
            cert_holder_state=cert_holder_state,
            cert_holder_zip=cert_holder_zip,
            email=email,
            general_liability=general_liability,
            auto_liability=auto_liability,
            work_comp=work_comp,
            umbrella=umbrella,
            ai_general_liability=ai_general_liability,
            ai_auto_liability=ai_auto_liability,
            primary_general_liability=primary_general_liability,
            waiver_general_liability=waiver_general_liability,
            job_location=job_location
        )
        certificate.save()  # Save the instance to the database

        # Render the confirmation modal
        return render(request, 'documents/document.html', {'submitted': True})

    return render(request, 'documents/document.html')
