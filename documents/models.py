from django.db import models

# Create your models here.


class InsuranceCertificate(models.Model):
    insured_name = models.CharField(max_length=255)
    cert_holder_name = models.CharField(max_length=255)
    cert_holder_address = models.CharField(max_length=255)
    cert_holder_city = models.CharField(max_length=100)
    # Assuming state is represented by 2-letter code
    cert_holder_state = models.CharField(max_length=2)
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
    job_location = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.insured_name} - {self.cert_holder_name}"
