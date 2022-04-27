from django.db import models
from ULBForms.models import AgencyProgressModel, AgencySanctionModel
from TUFIDCOapp.models import *


# Create your models here.

class ULBProgressIncompleted(AgencyProgressModel):
    class Meta:
        proxy = True
        verbose_name = 'Portal Progress Detail'
        verbose_name_plural = 'Portal Progress Details'


class ULBSanctionReportError(AgencySanctionModel):
    class Meta:
        proxy = True
        verbose_name = 'Portal Sanction Detail'
        verbose_name_plural = 'Portal Sanction Details'


class ProgressNotEntered(MasterSanctionForm):
    class Meta:
        proxy = True
        verbose_name = 'Progress Detail Not Entered'
        verbose_name_plural = 'Progress Details Not Entered'


class SanctionNotEntered(MasterSanctionForm):
    class Meta:
        proxy = True
        verbose_name = 'Sanction Detail Not Entered'
        verbose_name_plural = 'Sanction Details Not Entered'


class SRPAbstract(SRPMasterSanctionForm):
    class Meta:
        proxy = True
        verbose_name = 'SRP Abstract'
        verbose_name_plural = 'SRP Abstract'



class PhysicalandFinancialReport(MasterSanctionForm):
    class Meta:
        proxy = True
        verbose_name = "KNMT Physical & Financial Progress Report"
        verbose_name_plural = "KNMT Physical & Financial Progress Reports"