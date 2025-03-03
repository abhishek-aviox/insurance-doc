from django.shortcuts import render
from .models import InsuranceCertificate


def document_view(request):
    if request.method == 'POST':
        # Extract data from the form
        insured_name = request.POST.get('insured_name')
        cert_holder_name = request.POST.get('cert_holder_name')
        cert_holder_name2 = request.POST.get('cert_holder_name2')
        cert_holder_address = request.POST.get('cert_holder_address')
        cert_holder_address2 = request.POST.get('cert_holder_address2')
        cert_holder_city = request.POST.get('cert_holder_city')
        cert_holder_state = request.POST.get('cert_holder_state')
        cert_holder_zip = request.POST.get('cert_holder_zip')
        email = request.POST.get('email')
        cert_holder_email = request.POST.get('cert_holder_email')
        cc_matt = request.POST.get('cc_matt')
        cc_insured = request.POST.get('cc_insured') is not None
        subject_line = request.POST.get('subject_line')
        lines_business_excess = request.POST.get('lines_business_excess')
        notice_cancellation = request.POST.get('notice_cancellation')
        # Additional new fields related to forms and operations
        form_number_gl_ongoing = request.POST.get('form_number_gl_ongoing', '')
        form_number_gl_complete = request.POST.get(
            'form_number_gl_complete', '')
        form_number_auto = request.POST.get('form_number_auto', '')
        form_number_primary_gl = request.POST.get('form_number_primary_gl', '')
        form_number_primary_auto = request.POST.get(
            'form_number_primary_auto', '')
        form_number_waiver_gl = request.POST.get('form_number_waiver_gl', '')
        form_number_waiver_auto = request.POST.get(
            'form_number_waiver_auto', '')
        form_number_waiver_work_comp = request.POST.get(
            'form_number_waiver_work_comp', '')
        umbrella_coi = request.POST.get('umbrella_coi', '')
        notice_cancellation_value1 = request.POST.get(
            'notice_cancellation_value1', '')
        notice_cancellation_value2 = request.POST.get(
            'notice_cancellation_value2', '')
        ai_name = request.POST.get('ai_name', '')
        # Booleans
        general_liability = request.POST.get('general_liability') is not None
        auto_liability = request.POST.get('auto_liability') is not None
        work_comp = request.POST.get('work_comp') is not None
        umbrella = request.POST.get('umbrella') is not None
        ai_general_liability = request.POST.get(
            'ai_general_liability') is not None
        ai_auto_liability = request.POST.get('ai_auto_liability') is not None
        ai_complete_operations = request.POST.get(
            'ai_complete_operations') is not None
        primary_general_liability = request.POST.get(
            'primary_general_liability') is not None
        primary_auto_liability = request.POST.get(
            'primary_auto_liability') is not None
        waiver_general_liability = request.POST.get(
            'waiver_general_liability') is not None
        waiver_auto_liability = request.POST.get(
            'waiver_auto_liability') is not None
        waiver_work_comp = request.POST.get('waiver_work_comp') is not None
        job_location = request.POST.get('job_location')

        # Create a new InsuranceCertificate instance with all fields
        certificate = InsuranceCertificate(
            insured_name=insured_name,
            cert_holder_name=cert_holder_name,
            cert_holder_name2=cert_holder_name2,
            cert_holder_address=cert_holder_address,
            cert_holder_address2=cert_holder_address2,
            cert_holder_city=cert_holder_city,
            cert_holder_state=cert_holder_state,
            cert_holder_zip=cert_holder_zip,
            email=email,
            cert_holder_email=cert_holder_email,
            general_liability=general_liability,
            auto_liability=auto_liability,
            work_comp=work_comp,
            umbrella=umbrella,
            ai_general_liability=ai_general_liability,
            ai_auto_liability=ai_auto_liability,
            primary_general_liability=primary_general_liability,
            waiver_general_liability=waiver_general_liability,
            job_location=job_location,
            lines_business_excess=lines_business_excess,
            notice_cancellation=notice_cancellation,
            subject_line=subject_line,
            cc_matt=cc_matt,
            cc_insured=cc_insured,
            form_number_gl_ongoing=form_number_gl_ongoing,
            form_number_gl_complete=form_number_gl_complete,
            form_number_auto=form_number_auto,
            form_number_primary_gl=form_number_primary_gl,
            form_number_primary_auto=form_number_primary_auto,
            form_number_waiver_gl=form_number_waiver_gl,
            form_number_waiver_auto=form_number_waiver_auto,
            form_number_waiver_work_comp=form_number_waiver_work_comp,
            umbrella_coi=umbrella_coi,
            notice_cancellation_value1=notice_cancellation_value1,
            notice_cancellation_value2=notice_cancellation_value2,
            ai_name=ai_name,
            ai_complete_operations=ai_complete_operations,
            primary_auto_liability=primary_auto_liability,
            waiver_auto_liability=waiver_auto_liability,
            waiver_work_comp=waiver_work_comp
        )
        certificate.save()  # Save the instance to the database

        # Render the confirmation modal with all fields in the context
        context = {
            'submitted': True,
            'insured_name': insured_name,
            'cert_holder_name': cert_holder_name,
            'cert_holder_name2': cert_holder_name2,
            'cert_holder_address': cert_holder_address,
            'cert_holder_address2': cert_holder_address2,
            'cert_holder_city': cert_holder_city,
            'cert_holder_state': cert_holder_state,
            'cert_holder_zip': cert_holder_zip,
            'email': email,
            'cert_holder_email': cert_holder_email,
            'general_liability': general_liability,
            'auto_liability': auto_liability,
            'work_comp': work_comp,
            'umbrella': umbrella,
            'ai_general_liability': ai_general_liability,
            'ai_auto_liability': ai_auto_liability,
            'ai_complete_operations': ai_complete_operations,
            'primary_general_liability': primary_general_liability,
            'primary_auto_liability': primary_auto_liability,
            'waiver_general_liability': waiver_general_liability,
            'waiver_auto_liability': waiver_auto_liability,
            'waiver_work_comp': waiver_work_comp,
            'job_location': job_location,
            'lines_business_excess': lines_business_excess,
            'notice_cancellation': notice_cancellation,
            'subject_line': subject_line,
            'cc_matt': cc_matt,
            'cc_insured': cc_insured,
            'form_number_gl_ongoing': form_number_gl_ongoing,
            'form_number_gl_complete': form_number_gl_complete,
            'form_number_auto': form_number_auto,
            'form_number_primary_gl': form_number_primary_gl,
            'form_number_primary_auto': form_number_primary_auto,
            'form_number_waiver_gl': form_number_waiver_gl,
            'form_number_waiver_auto': form_number_waiver_auto,
            'form_number_waiver_work_comp': form_number_waiver_work_comp,
            'umbrella_coi': umbrella_coi,
            'notice_cancellation_value1': notice_cancellation_value1,
            'notice_cancellation_value2': notice_cancellation_value2,
            'ai_name': ai_name,
        }
        return render(request, 'documents/document.html', context)

    return render(request, 'documents/document.html')
