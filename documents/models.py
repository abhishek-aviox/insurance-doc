from django.db import models


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class InsuranceCertificate(TimeStampedModel):
    insured_name = models.CharField(max_length=255)
    cert_holder_name = models.CharField(max_length=255)
    cert_holder_address = models.CharField(max_length=255)
    cert_holder_city = models.CharField(max_length=100)
    cert_holder_state = models.CharField(max_length=2)  # 2-letter state code
    cert_holder_zip = models.CharField(max_length=10)
    email = models.EmailField()
    general_liability = models.BooleanField(default=False)
    auto_liability = models.BooleanField(default=False)
    work_comp = models.BooleanField(default=False)
    umbrella = models.BooleanField(default=False)
    ai_general_liability = models.BooleanField(default=False)
    ai_auto_liability = models.BooleanField(default=False)
    primary_general_liability = models.BooleanField(default=False)
    waiver_general_liability = models.BooleanField(default=False)
    job_location = models.CharField(max_length=255, blank=True, null=True)

    # New fields
    cert_holder_address2 = models.CharField(
        max_length=255, blank=True, null=True)
    cert_holder_name2 = models.CharField(max_length=255, blank=True, null=True)
    cert_holder_email = models.EmailField(blank=True, null=True)
    lines_business_excess = models.CharField(
        max_length=255, blank=True, null=True)
    notice_cancellation = models.CharField(
        max_length=255, blank=True, null=True)
    subject_line = models.CharField(max_length=255, blank=True, null=True)
    cc_matt = models.EmailField(blank=True, null=True)
    cc_insured = models.BooleanField(default=False)

    # Additional new fields
    form_number_gl_ongoing = models.CharField(
        max_length=255, blank=True, null=True)
    form_number_gl_complete = models.CharField(
        max_length=255, blank=True, null=True)
    form_number_auto = models.CharField(max_length=255, blank=True, null=True)
    form_number_primary_gl = models.CharField(
        max_length=255, blank=True, null=True)
    form_number_primary_auto = models.CharField(
        max_length=255, blank=True, null=True)
    form_number_waiver_gl = models.CharField(
        max_length=255, blank=True, null=True)
    form_number_waiver_auto = models.CharField(
        max_length=255, blank=True, null=True)
    form_number_waiver_work_comp = models.CharField(
        max_length=255, blank=True, null=True)
    umbrella_coi = models.CharField(max_length=255, blank=True, null=True)
    notice_cancellation_value1 = models.CharField(
        max_length=255, blank=True, null=True)
    notice_cancellation_value2 = models.CharField(
        max_length=255, blank=True, null=True)
    ai_name = models.CharField(
        max_length=255, blank=True, null=True)
    ai_complete_operations = models.BooleanField(default=False)
    primary_auto_liability = models.BooleanField(default=False)
    waiver_auto_liability = models.BooleanField(default=False)
    waiver_work_comp = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.insured_name} - {self.cert_holder_name}"
